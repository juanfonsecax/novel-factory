#!/usr/bin/env python3
"""Local runner for the Omni queue — no APIs, no network, no external dependencies.

Modes:
  status    Progress table: which frames and clips exist, duration and next step.
  queue     Print the prompt for the next pending scene (for your own scripting/automation).
  assisted  Clipboard assistant: copies the prompt, you paste it into Omni, press Enter
            and the runner collects the downloaded clip and files it as raw_clips/scene_XXX.mp4.
  watch     Watch a downloads folder and automatically file new clips
            in scene order (you download them and the runner renames/places them).

Playwright is OPTIONAL and DISABLED by default. No website automation is included
(selectors change and automated use may violate their terms).
If you have your own local Playwright script, pass it with --playwright-script: the runner
will run it before each manual wait and pass NF_SCENE, NF_FRAME and NF_PROMPT through
environment variables.

Usage:
  python automation/omni_flow_runner.py my_episode status
  python automation/omni_flow_runner.py my_episode queue
  python automation/omni_flow_runner.py my_episode assisted --count 5
  python automation/omni_flow_runner.py my_episode assisted --platform muse
  python automation/omni_flow_runner.py my_episode assisted --platform flow
  python automation/omni_flow_runner.py my_episode watch --once
  python automation/omni_flow_runner.py my_episode watch --interval 3
  python automation/omni_flow_runner.py my_episode import-frames --frames-src "C:\\my\\images"
  python automation/omni_flow_runner.py my_episode assisted --playwright-script "C:\\my\\omni_local.py"
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

NF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(NF_ROOT))
import nf_core as nf  # noqa: E402

MEDIA_EXTS = (".mp4", ".mov", ".m4v", ".webm")
IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".webp")
DEFAULT_DOWNLOADS = Path.home() / "Downloads"
QUEUE_KEYS = {
    "omni": ("omni_json", "Omni 1.1 Flash"),
    "muse": ("muse_json", "Muse AI"),
    "flow": ("flow_json", "Google Flow (Veo)"),
}


def natural_key(text: str) -> List[Any]:
    """Natural sort key: 'clip_2' < 'clip_10' (not lexicographic)."""
    import re as _re

    return [int(part) if part.isdigit() else part.lower()
            for part in _re.split(r"(\d+)", str(text))]


def scene_hint_from_name(name: str) -> Optional[int]:
    """Extract a scene_id from a name like 'scene_007.mp4' or '007 ...'. Otherwise None."""
    import re as _re

    match = _re.search(r"(?:scene[_\-\s]*)?(\d{1,3})(?!\d)", str(name), flags=_re.IGNORECASE)
    if not match:
        return None
    try:
        sid = int(match.group(1))
    except ValueError:
        return None
    return sid if sid >= 1 else None


# ---------------------------------------------------------------------------
# Project state
# ---------------------------------------------------------------------------
def load_queue(
    paths: Dict[str, Path],
    platform: str = "omni",
    max_scene: Optional[int] = None,
) -> Dict[int, Dict[str, Any]]:
    key, _label = QUEUE_KEYS.get(str(platform or "omni").strip().lower(), QUEUE_KEYS["omni"])
    queue_path = paths.get(key)
    if not queue_path:
        return {}
    data = nf.read_json(queue_path, default=None)
    items = data.get("items") if isinstance(data, dict) else data
    out: Dict[int, Dict[str, Any]] = {}
    for item in items or []:
        if not isinstance(item, dict):
            continue
        try:
            sid = int(item.get("scene_id") or 0)
        except (TypeError, ValueError):
            continue
        if sid >= 1 and (max_scene is None or sid <= int(max_scene)):
            out[sid] = item
    return out


def build_status(paths: Dict[str, Path], master: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for scene in nf.ordered_scenes(master):
        sid = int(scene.get("scene_id") or 0)
        frame = nf.find_frame(paths["frames"], sid)
        clip = nf.find_clip(paths["raw_clips"], sid)
        dur = 0.0
        if clip:
            try:
                dur = float(nf.probe_media(clip).get("duration") or 0.0)
            except nf.NFError:
                dur = 0.0
        rows.append({"scene_id": sid, "frame": frame, "clip": clip, "duration": dur})
    return rows


def save_state(paths: Dict[str, Path], rows: List[Dict[str, Any]]) -> None:
    payload = {
        "updated_at": nf.now_iso(),
        "scenes_total": len(rows),
        "frames_present": sum(1 for r in rows if r["frame"]),
        "clips_present": sum(1 for r in rows if r["clip"]),
        "missing_frames": [r["scene_id"] for r in rows if not r["frame"]],
        "missing_clips": [r["scene_id"] for r in rows if not r["clip"]],
        "clips": {
            str(r["scene_id"]): {
                "file": Path(r["clip"]).name,
                "duration": round(float(r["duration"]), 2),
            }
            for r in rows if r["clip"]
        },
    }
    nf.write_json(paths["state"], payload)


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------
def copy_to_clipboard(text: str) -> bool:
    """Copy to the clipboard with tkinter (stdlib). Return False if there is no GUI environment."""
    try:
        import tkinter as tk

        root = tk.Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        root.destroy()
        return True
    except Exception:
        return False


def stash_prompt(paths: Dict[str, Path], scene_id: int, prompt: str) -> Path:
    target = paths["work"] / f"next_prompt_scene_{scene_id:03d}.txt"
    nf.write_text(target, prompt.strip() + "\n")
    return target


def find_newest_media(folder: Path, since_ts: float) -> Optional[Path]:
    if not folder.exists():
        return None
    hits = [
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in MEDIA_EXTS and p.stat().st_mtime >= since_ts
    ]
    return max(hits, key=lambda p: p.stat().st_mtime) if hits else None


def assign_clip(
    src: Path,
    paths: Dict[str, Path],
    scene_id: int,
    overwrite: bool = False,
    force_duration: bool = False,
) -> Tuple[bool, str]:
    """Validate and file a clip as raw_clips/scene_XXX.mp4."""
    target = paths["raw_clips"] / f"{nf.scene_stem(scene_id)}.mp4"
    if target.exists() and not overwrite:
        return False, f"{target.name} already exists (use --overwrite to replace it)"
    try:
        probe = nf.probe_media(src)
    except nf.NFError as exc:
        return False, f"invalid file: {exc}"
    if not probe.get("has_video"):
        return False, "the file has no video track"
    dur = float(probe.get("duration") or 0.0)
    if not (5.0 <= dur <= 15.0) and not force_duration:
        return False, (f"duration {dur:.1f}s outside 5-15 s (Omni should give ~10 s). "
                       "Use --force-duration if that is correct.")
    src = src.resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    if src == target.resolve():
        return True, f"{target.name} was already in place ({dur:.1f}s)"
    try:
        shutil.move(str(src), str(target))
    except OSError:
        # Fallback across different volumes: safe copy + delete.
        shutil.copy2(str(src), str(target))
        try:
            src.unlink()
        except OSError:
            pass
    note = f"{target.name} ({dur:.1f}s)"
    if abs(dur - nf.SCENE_SECONDS) > 0.8:
        note += "  [!] not exactly 10 s"
    return True, note


def run_playwright_script(script: Path, scene_id: int, frame: Optional[Path], prompt: str) -> None:
    if not script.exists():
        raise nf.NFError(f"Playwright script does not exist: {script}")
    env = {
        **__import__("os").environ,
        "NF_SCENE": str(scene_id),
        "NF_FRAME": str(frame or ""),
        "NF_PROMPT": prompt,
    }
    nf.info(f"Running local script: {script.name}")
    res = subprocess.run([sys.executable, str(script)], env=env)
    if res.returncode != 0:
        nf.warn(f"Script {script.name} exited with code {res.returncode}; continuing in manual mode.")


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------
def cmd_status(args: argparse.Namespace) -> int:
    paths, master = _prepare(args)
    rows = build_status(paths, master)
    save_state(paths, rows)
    nf.log("")
    nf.log(f"  {'Scene':>7}  {'Frame':<14}  {'Clip':<22}  {'Duration':>8}")
    nf.log("  " + "-" * 58)
    for r in rows:
        frame = Path(r["frame"]).name if r["frame"] else "—"
        clip = Path(r["clip"]).name if r["clip"] else "—"
        dur = f"{r['duration']:.1f}s" if r["clip"] else ""
        nf.log(f"  {r['scene_id']:>7}  {frame:<14}  {clip:<22}  {dur:>8}")
    frames = sum(1 for r in rows if r["frame"])
    clips = sum(1 for r in rows if r["clip"])
    nf.log("  " + "-" * 58)
    nf.info(f"Frames: {frames}/{len(rows)}   Clips: {clips}/{len(rows)}")
    if clips < len(rows):
        nf.info("Next step: python automation/omni_flow_runner.py <project> assisted")
    elif frames < len(rows):
        nf.info("Missing frames: export the ChatGPT queue (02) and generate the images.")
    else:
        nf.ok("All ready: run post_production/04_assemble_novel_ffmpeg.py")
    nf.info(f"State saved to: {paths['state']}")
    return 0


def cmd_queue(args: argparse.Namespace) -> int:
    paths, master = _prepare(args)
    platform = getattr(args, "platform", "omni")
    _key, label = QUEUE_KEYS.get(platform, QUEUE_KEYS["omni"])
    queue = load_queue(paths, platform, nf.master_scene_count(master))
    rows = build_status(paths, master)
    for r in rows:
        if r["clip"]:
            continue
        sid = r["scene_id"]
        item = queue.get(sid)
        if not item:
            nf.warn(f"Scene {sid}: not in the {label} queue; regenerate it with 03 --platform {platform}.")
            return 1
        nf.log("")
        nf.log(f"=== Scene {sid} ===")
        expected_frame = paths["frames"] / f"{nf.frame_stem(sid)}.png"
        nf.log(f"Frame : {r['frame'] or 'MISSING -> ' + str(expected_frame)}")
        nf.log(f"Output: {paths['raw_clips'] / nf.scene_stem(sid)}.mp4")
        nf.log("")
        nf.log(str(item.get("prompt") or "").strip())
        return 0
    nf.ok("No pending clips.")
    return 0


def _prepare(args: argparse.Namespace) -> Tuple[Dict[str, Path], Dict[str, Any]]:
    paths = nf.resolve_project(args.project)
    master = nf.load_master(paths["root"])
    return paths, master


def _missing_rows(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [r for r in rows if not r["clip"]]


def cmd_assisted(args: argparse.Namespace) -> int:
    nf.require_ffmpeg()
    paths, master = _prepare(args)
    platform = getattr(args, "platform", "omni")
    _key, label = QUEUE_KEYS.get(platform, QUEUE_KEYS["omni"])
    queue = load_queue(paths, platform, nf.master_scene_count(master))
    if not queue:
        nf.warn(f"No {label} queue. Run generators/03_export_omni_queue.py {args.project} --platform {platform}")
        return 1
    done = 0
    skipped: set = set()
    while True:
        rows = build_status(paths, master)
        pending = [r for r in _missing_rows(rows) if r["scene_id"] not in skipped]
        if not pending:
            save_state(paths, rows)
            if skipped:
                nf.warn(f"Skipped in this session: {', '.join(map(str, sorted(skipped)))}")
            nf.ok("Every scene (not skipped) has a clip.")
            return 0
        row = pending[0]
        sid = row["scene_id"]
        item = queue.get(sid)
        if not item:
            nf.warn(f"Scene {sid} has no prompt in the queue; skipping.")
            item = {"prompt": ""}
        prompt = str(item.get("prompt") or "").strip()
        frame = row["frame"]
        nf.log("")
        nf.log("=" * 70)
        nf.log(f"  SCENE {sid} of {len(rows)}   |   {len(pending)} left")
        nf.log("=" * 70)
        nf.log(f"  Frame : {frame or '(frame missing)'}")
        nf.log(f"  Output: {paths['raw_clips'] / nf.scene_stem(sid)}.mp4")
        nf.log("")
        nf.log(prompt or "(no prompt: use the queue CSV)")
        nf.log("")
        if args.no_clipboard:
            copied = False
        else:
            copied = copy_to_clipboard(prompt) if prompt else False
        if copied:
            nf.ok("Prompt copied to the clipboard.")
        elif prompt:
            saved = stash_prompt(paths, sid, prompt)
            nf.info(f"Clipboard unavailable: prompt saved to {saved}")

        if args.playwright_script:
            try:
                run_playwright_script(Path(args.playwright_script), sid, frame, prompt)
            except nf.NFError as exc:
                nf.warn(str(exc))

        started = time.time() - 2
        try:
            answer = input("  Press Enter when the clip is downloaded (s=skip, q=quit): ").strip().lower()
        except EOFError:
            nf.info("No interactive input; exiting.")
            return 0
        if answer in ("q", "quit", "exit"):
            nf.info("Exiting.")
            return 0
        if answer in ("s", "skip"):
            nf.warn(f"Scene {sid} skipped by the user (will not be asked again today).")
            skipped.add(sid)
            continue

        override = answer.strip('"').strip("'")
        src: Optional[Path] = Path(override) if override else None
        if src and not src.exists():
            nf.warn(f"Does not exist: {src}")
            continue
        if src is None:
            src = find_newest_media(Path(args.downloads), started)
            if src is None:
                nf.warn(f"No new video found in {args.downloads}. Paste the clip path or try again.")
                continue
        ok, note = assign_clip(src, paths, sid, overwrite=args.overwrite,
                               force_duration=args.force_duration)
        if ok:
            nf.ok(f"Scene {sid}: {note}")
            done += 1
        else:
            nf.warn(f"Scene {sid}: {note}")
        if args.count and done >= args.count:
            nf.ok(f"Processed {done} clips in this session.")
            save_state(paths, build_status(paths, master))
            return 0


def cmd_import_frames(args: argparse.Namespace) -> int:
    """Import pre-generated images into frames/frame_XXX.<ext> in natural order."""
    paths, master = _prepare(args)
    src_dir = Path(args.frames_src).expanduser()
    if not src_dir.is_dir():
        raise nf.NFError(f"Frames folder does not exist: {src_dir}")
    candidates = sorted(
        (p for p in src_dir.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTS),
        key=lambda p: natural_key(p.name),
    )
    if not candidates:
        nf.warn(f"No images ({', '.join(IMAGE_EXTS)}) in {src_dir}.")
        return 1

    rows = build_status(paths, master)
    missing = [r["scene_id"] for r in rows if not r["frame"]]
    if args.from_scene or args.to_scene:
        lo = args.from_scene or 1
        hi = args.to_scene or max((r["scene_id"] for r in rows), default=0)
        targets = [sid for sid in range(lo, hi + 1) if (args.overwrite or sid in missing)]
    else:
        targets = list(missing)

    if not targets:
        nf.ok("No target frames (use --overwrite to replace existing ones).")
        return 0
    if len(candidates) < len(targets):
        nf.warn(f"{len(candidates)} images for {len(targets)} target scenes; importing the first {len(candidates)}.")
    pairs = list(zip(targets, candidates))
    nf.log("")
    moved = 0
    for sid, src in pairs:
        dest = paths["frames"] / f"{nf.frame_stem(sid)}{src.suffix.lower()}"
        if dest.exists() and not args.overwrite:
            nf.warn(f"Scene {sid}: {dest.name} already exists (use --overwrite).")
            continue
        if args.dry_run:
            nf.info(f"[dry-run] {src.name} -> {dest.name}")
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        if args.move:
            shutil.move(str(src), str(dest))
        else:
            shutil.copy2(str(src), str(dest))
        moved += 1
        nf.ok(f"{src.name} -> {dest.name}")
    if not args.dry_run:
        nf.info(f"Imported {moved} frame(s).")
        save_state(paths, build_status(paths, master))
    return 0


def _scan_ready(downloads: Path, start: float, seen: Dict[Path, int]) -> List[Path]:
    """New video files with a stable size between two scans (download complete)."""
    ready: List[Path] = []
    for media in sorted(downloads.iterdir(), key=lambda p: natural_key(p.name)):
        if not media.is_file() or media.suffix.lower() not in MEDIA_EXTS:
            continue
        try:
            if media.stat().st_mtime < start:
                continue
            size = media.stat().st_size
        except OSError:
            continue
        if media in seen:
            last = seen[media]
            if last == size and size > 0:
                ready.append(media)
        else:
            seen[media] = size
    return ready


def cmd_watch(args: argparse.Namespace) -> int:
    nf.require_ffmpeg()
    paths, master = _prepare(args)
    downloads = Path(args.downloads).expanduser()
    if not downloads.is_dir():
        raise nf.NFError(f"Downloads folder does not exist: {downloads}")
    start = 0.0 if args.all else time.time() - 2
    seen: Dict[Path, int] = {}
    nf.info(f"Watching {downloads} (Ctrl+C to stop)")
    nf.info(f"Destination: {paths['raw_clips']}")
    try:
        if args.once:
            # Two quick scans to confirm the download finished, then exit.
            _scan_ready(downloads, start, seen)
            time.sleep(max(1.0, min(2.0, float(args.interval))))
        while True:
            rows = build_status(paths, master)
            if not _missing_rows(rows):
                nf.ok("Every scene has a clip.")
                save_state(paths, rows)
                return 0
            for media in _scan_ready(downloads, start, seen):
                rows = build_status(paths, master)
                pending = _missing_rows(rows)
                if not pending:
                    break
                pending_ids = {r["scene_id"] for r in pending}
                hint = scene_hint_from_name(media.name)
                if hint and hint in pending_ids:
                    row = next(r for r in pending if r["scene_id"] == hint)
                    nf.info(f"{media.name}: detected scene_id {hint} in the name.")
                else:
                    row = pending[0]
                sid = row["scene_id"]
                seen[media] = media.stat().st_size if media.exists() else 0
                if args.dry_run:
                    nf.info(f"[dry-run] {media.name} -> {nf.scene_stem(sid)}.mp4")
                    continue
                ok, note = assign_clip(media, paths, sid, overwrite=args.overwrite,
                                       force_duration=args.force_duration)
                if ok:
                    nf.ok(f"{media.name} -> scene {sid}: {note}")
                else:
                    nf.warn(f"{media.name}: {note}")
            if args.once:
                save_state(paths, build_status(paths, master))
                return 0
            time.sleep(max(1.0, float(args.interval)))
    except KeyboardInterrupt:
        nf.info("Watcher stopped.")
        save_state(paths, build_status(paths, master))
        return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Local Omni queue runner (status/queue/assisted/watch). No APIs.",
    )
    parser.add_argument("project", help="Episode slug.")
    parser.add_argument("command", choices=["status", "queue", "assisted", "watch", "import-frames"],
                        help="Action to run.")
    parser.add_argument("--platform", choices=list(QUEUE_KEYS), default="omni",
                        help="Video queue to use in queue/assisted: omni (default), muse or flow.")
    parser.add_argument("--downloads", default=str(DEFAULT_DOWNLOADS),
                        help="Downloads folder to watch (default: ~/Downloads).")
    parser.add_argument("--interval", type=float, default=3.0, help="Seconds between scans in watch.")
    parser.add_argument("--once", action="store_true", help="watch: single pass.")
    parser.add_argument("--all", action="store_true", help="watch: include existing files.")
    parser.add_argument("--dry-run", action="store_true", help="watch: show without moving files.")
    parser.add_argument("--count", type=int, default=0, help="assisted: clips to process in this session.")
    parser.add_argument("--no-clipboard", action="store_true", help="assisted: do not touch the clipboard.")
    parser.add_argument("--overwrite", action="store_true", help="Replace existing clips.")
    parser.add_argument("--force-duration", action="store_true",
                        help="Accept clips outside 5-15 s (in case Omni changed the format).")
    parser.add_argument("--playwright-script", default="",
                        help="Optional local script (your own Playwright) to run before each wait.")
    parser.add_argument("--frames-src", default="",
                        help="import-frames: folder with pre-generated images.")
    parser.add_argument("--from-scene", type=int, default=0,
                        help="import-frames: first target scene_id (default: missing frames).")
    parser.add_argument("--to-scene", type=int, default=0,
                        help="import-frames: last target scene_id.")
    parser.add_argument("--move", action="store_true",
                        help="import-frames: move instead of copy.")
    args = parser.parse_args(argv)

    nf.log("")
    nf.log("=" * 70)
    nf.log("  NOVEL FACTORY — Video queue runner")
    nf.log("=" * 70)
    try:
        if args.command == "status":
            return cmd_status(args)
        if args.command == "queue":
            return cmd_queue(args)
        if args.command == "assisted":
            return cmd_assisted(args)
        if args.command == "import-frames":
            return cmd_import_frames(args)
        return cmd_watch(args)
    except nf.NFError as exc:
        nf.err(str(exc))
        return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except nf.NFError as exc:
        nf.err(str(exc))
        sys.exit(1)

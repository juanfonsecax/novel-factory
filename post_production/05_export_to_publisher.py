#!/usr/bin/env python3
"""05 — Bridge from novel_factory to the USA WHITE publisher (file-based, no code changes there).

What it does:
  1. Locates the publisher system (USA WHITE folder: cola/pendientes + src/orquestador.py).
  2. Takes the three 9:16 teasers rendered by 04 (or whichever exist) and builds a JSON post
     with the EXACT schema already consumed by the orchestrator / auto_runner:
        id, personaje_id, tipo="reel", fecha_creacion, archivo_media, hook, caption,
        estado="pendiente_aprobacion", final_video=true, output_filename, plataformas
  3. Copies the MP4 next to the JSON in cola/pendientes/ (the orchestrator looks for media there).
  4. Prints how to launch publishing (safe manual run or scheduled daemon).

Safety:
  - PLAN (dry-run) by default: writes nothing. With --apply it really copies.
  - No duplicates: if the JSON or MP4 already exists in the queue, it is skipped (unless --force).
  - The id includes the episode slug; teasers are queued in order 01, 02, 03.
  - The long master is NOT exported: the USA WHITE YouTube publisher is Shorts-only;
    upload the master manually with output/publish_pack/youtube_master.md.

Usage:
  python post_production/05_export_to_publisher.py my_episode                  (plan)
  python post_production/05_export_to_publisher.py my_episode --apply          (export)
  python post_production/05_export_to_publisher.py my_episode --only 1,2 --apply
  python post_production/05_export_to_publisher.py my_episode --publisher-root "C:\\path\\USA WHITE" --apply
  python post_production/05_export_to_publisher.py my_episode --personaje eva_hayes --apply
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

NF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(NF_ROOT))
import nf_core as nf  # noqa: E402


# ---------------------------------------------------------------------------
# Publisher location
# ---------------------------------------------------------------------------
def _looks_like_publisher(path: Path) -> bool:
    return (
        (path / "src" / "orquestador.py").exists()
        and (path / "cola" / "pendientes").is_dir()
    )


def find_publisher_root(explicit: str = "") -> Optional[Path]:
    """Return the USA WHITE root. On failure, None (the caller explains how to fix it).

    With --publisher-root it searches ONLY there (the folder, its parent and its direct children);
    it never silently falls back to auto-detection, to avoid publishing to the wrong place.
    """
    if explicit:
        base = Path(explicit).expanduser()
        candidates: List[Path] = [base, base.parent]
        if base.is_dir():
            try:
                candidates += [child for child in sorted(base.iterdir()) if child.is_dir()]
            except OSError:
                pass
        for cand in candidates:
            try:
                cand = cand.resolve()
            except OSError:
                continue
            if _looks_like_publisher(cand):
                return cand
        return None

    candidates = []
    # Search around the workspace: siblings of novel_factory and of its parent
    for anchor in (NF_ROOT.parent, NF_ROOT.parent.parent):
        if anchor == anchor.parent:
            continue
        try:
            for child in sorted(anchor.iterdir()):
                if child.is_dir():
                    candidates.append(child)
        except OSError:
            continue
    seen: set = set()
    for cand in candidates:
        try:
            cand = cand.resolve()
        except OSError:
            continue
        if cand in seen:
            continue
        seen.add(cand)
        if _looks_like_publisher(cand):
            return cand
    return None


# ---------------------------------------------------------------------------
# Episode data
# ---------------------------------------------------------------------------
def collect_teasers(paths: Dict[str, Path], master: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Merge publish_pack/metadata.json (preferred) with master.teasers and the real files."""
    pack = nf.read_json(paths["output"] / "publish_pack" / "metadata.json", default=None)
    by_id: Dict[int, Dict[str, Any]] = {}
    for teaser in master.get("teasers") or []:
        if isinstance(teaser, dict):
            try:
                by_id[int(teaser.get("id") or 0)] = dict(teaser)
            except (TypeError, ValueError):
                continue
    if isinstance(pack, dict):
        for item in pack.get("teasers") or []:
            if not isinstance(item, dict):
                continue
            try:
                tid = int(item.get("id") or 0)
            except (TypeError, ValueError):
                continue
            merged = by_id.setdefault(tid, {})
            for key in ("hook_text", "scenes"):
                if item.get(key) and not merged.get(key):
                    merged[key] = item[key]
            # The pack from 04 already adds hashtags to the caption: prefer it over the master's.
            if item.get("caption"):
                merged["caption"] = item["caption"]
            if item.get("file"):
                merged["_file"] = str(item["file"])

    out: List[Dict[str, Any]] = []
    for tid in sorted(by_id):
        teaser = by_id[tid]
        file_name = str(teaser.get("_file") or f"teaser_{tid:02d}_9x16.mp4")
        media = paths["output"] / file_name
        if not media.exists():
            # tolerance: look for any teaser_XX_9x16*.mp4
            hits = sorted(paths["output"].glob(f"teaser_{tid:02d}_9x16*"))
            media = hits[0] if hits else media
        teaser["_media"] = media
        teaser["_id"] = tid
        out.append(teaser)
    return out


def verify_media(path: Path, strict: bool = False) -> List[str]:
    """Check the MP4. Return a list of problems (empty = OK).

    With `strict=True` it also requires an audio track; the caller decides whether the list
    blocks enqueueing. It never raises unless the file is unreadable (then the
    list contains the error and enqueueing must abort).
    """
    problems: List[str] = []
    try:
        probe = nf.probe_media(path)
    except nf.NFError as exc:
        return [str(exc)]
    if not path.exists() or path.stat().st_size == 0:
        return [f"{path.name}: empty or missing file"]
    if not probe.get("has_video"):
        problems.append("the file has no video track")
    if (probe.get("width"), probe.get("height")) != (nf.TEASER_W, nf.TEASER_H):
        problems.append(
            f"resolution {probe.get('width')}x{probe.get('height')} (expected {nf.TEASER_W}x{nf.TEASER_H})"
        )
    dur = float(probe.get("duration") or 0.0)
    if dur and not (45.0 <= dur <= 75.0):
        problems.append(f"duration {dur:.1f}s (teasers are usually ~60 s)")
    if strict and not probe.get("has_audio"):
        problems.append("the file has no audio track")
    return problems


def validate_post(post: Dict[str, Any]) -> List[str]:
    """Check the minimum keys consumed by the orchestrator; returns a list of problems."""
    required = ("id", "personaje_id", "tipo", "archivo_media", "estado", "plataformas")
    problems = [f"missing '{key}'" for key in required if post.get(key) in (None, "")]
    if post.get("tipo") != "reel":
        problems.append("tipo must be 'reel'")
    plats = post.get("plataformas")
    if not isinstance(plats, dict) or not plats:
        problems.append("plataformas must be a non-empty dict")
    return problems


# ---------------------------------------------------------------------------
# Atomic, idempotent enqueue
# ---------------------------------------------------------------------------
def _atomic_copy(src: Path, dest: Path) -> None:
    tmp = dest.with_name(f".{dest.name}.part-{os.getpid()}")
    try:
        shutil.copy2(src, tmp)
        os.replace(tmp, dest)
    finally:
        if tmp.exists():
            try:
                tmp.unlink()
            except OSError:
                pass


def _atomic_write_json(data: Dict[str, Any], dest: Path) -> None:
    tmp = dest.with_name(f".{dest.name}.part-{os.getpid()}")
    nf.write_json(tmp, data)
    try:
        os.replace(tmp, dest)
    finally:
        if tmp.exists():
            try:
                tmp.unlink()
            except OSError:
                pass


def enqueue_item(
    pendientes: Path,
    post: Dict[str, Any],
    src_media: Path,
    media_name: str,
    force: bool = False,
) -> Tuple[str, Path, Path]:
    """Enqueue (media + json) atomically and idempotently.

    An item is complete only when BOTH files exist. If one is missing, it is repaired
    (not skipped halfway). Returns (status, json_path, media_path) with status in
    {"copied", "repaired", "skipped"}.
    """
    dest_json = pendientes / f"{post['id']}.json"
    dest_media = pendientes / media_name
    have_json, have_media = dest_json.exists(), dest_media.exists()
    if have_json and have_media:
        if not force:
            return "skipped", dest_json, dest_media
        status = "copied"  # forced replacement of a complete item
    else:
        status = "repaired" if (have_json or have_media) else "copied"
    pendientes.mkdir(parents=True, exist_ok=True)
    _atomic_copy(src_media, dest_media)
    _atomic_write_json(post, dest_json)
    return status, dest_json, dest_media


# ---------------------------------------------------------------------------
# Post construction (USA WHITE orchestrator schema)
# ---------------------------------------------------------------------------
def build_post(
    teaser: Dict[str, Any],
    slug: str,
    personaje: str,
    media_name: str,
    stamp: str,
    hashtags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    hook = str(teaser.get("hook_text") or "").strip() or f"{slug.replace('_', ' ').title()} — teaser"
    caption = str(teaser.get("caption") or "").strip() or hook
    tags = " ".join(h for h in (hashtags or []) if str(h).strip())
    if tags and "#" not in caption:
        caption = f"{caption}\n\n{tags}"
    return {
        "id": f"nf_{slug}_teaser_{int(teaser['_id']):02d}",
        "personaje_id": personaje,
        "tipo": "reel",
        "fecha_creacion": stamp,
        "archivo_media": media_name,
        "hook": hook,
        "caption": caption,
        "estado": "pendiente_aprobacion",
        "final_video": True,
        "output_filename": media_name,
        "plataformas": {"instagram": True, "facebook": True, "tiktok": True, "youtube": True},
        "origen": {
            "modulo": "novel_factory",
            "proyecto": slug,
            "teaser": int(teaser["_id"]),
            "escenas": teaser.get("scenes"),
        },
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="05 — Export 9:16 teasers to the USA WHITE publisher queue.")
    parser.add_argument("project", help="Episode slug.")
    parser.add_argument("--publisher-root", default="", help="Path to USA WHITE (if not auto-detected).")
    parser.add_argument("--personaje", default="", help="Queue personaje_id (e.g. emma_hayes).")
    parser.add_argument("--only", default="", help="Only these teasers, e.g. '1,3'.")
    parser.add_argument("--apply", action="store_true", help="Actually copy (without this it only shows the plan).")
    parser.add_argument("--force", action="store_true", help="Overwrite if it already exists in the queue.")
    parser.add_argument("--strict", action="store_true",
                        help="Abort enqueueing teasers with media problems (resolution/audio).")
    args = parser.parse_args(argv)

    nf.log("")
    nf.log("=" * 70)
    nf.log("  NOVEL FACTORY — 05 · Export teasers to the publisher queue")
    nf.log("=" * 70)

    paths = nf.resolve_project(args.project)
    master = nf.load_master(paths["root"])
    slug = str(nf.episode_meta(master).get("slug") or args.project)
    personaje = args.personaje or str((master.get("publisher") or {}).get("personaje_id") or "emma_hayes")

    publisher = find_publisher_root(args.publisher_root)
    if publisher is None:
        nf.err("Publisher folder not found (it must contain src/orquestador.py and cola/pendientes).")
        nf.info("Specify it manually:  --publisher-root \"C:\\path\\USA WHITE\"")
        return 1

    pendientes = publisher / "cola" / "pendientes"
    nf.info(f"Publisher  : {publisher}")
    nf.info(f"Queue      : {pendientes}")
    nf.info(f"Character  : {personaje}")
    nf.info(f"Mode       : {'APPLY (copies to the queue)' if args.apply else 'PLAN (writes nothing)'}")

    only_ids = {int(x) for x in nf.parse_ranges(args.only)} if args.only.strip() else None
    teasers = collect_teasers(paths, master)
    if not teasers:
        nf.err("The master defines no teasers. Check master_episode.json (teasers) and rerun 04.")
        return 1
    if only_ids is not None:
        teasers = [t for t in teasers if int(t["_id"]) in only_ids]
    if not teasers:
        nf.err(f"--only {args.only} matches no available teaser.")
        return 1

    stamp = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    hashtags = list((master.get("publisher") or {}).get("hashtags") or [])
    pending: List[Dict[str, Any]] = []
    missing = 0
    invalid = 0
    for teaser in teasers:
        media: Path = teaser["_media"]
        if not media.exists():
            nf.warn(f"Teaser {teaser['_id']}: missing {media.name} (render it with 04_assemble_novel_ffmpeg.py).")
            missing += 1
            continue
        problems = verify_media(media, strict=args.strict)
        if problems:
            level = nf.err if args.strict else nf.warn
            for p in problems:
                level(f"Teaser {teaser['_id']}: {p}")
            if args.strict:
                invalid += 1
                continue
        media_name = f"nf_{slug}_teaser_{int(teaser['_id']):02d}_9x16.mp4"
        post = build_post(teaser, slug, personaje, media_name, stamp, hashtags)
        for p in validate_post(post):
            nf.err(f"Teaser {teaser['_id']}: invalid post: {p}")
            invalid += 1
            post = None
            break
        if post is None:
            continue
        pending.append({"teaser": teaser, "post": post, "src": media, "media_name": media_name})
    if not pending:
        if invalid:
            nf.err(f"{invalid} teaser(s) have problems; nothing to export (check with --strict).")
        elif missing:
            nf.err("No rendered teaser available to export.")
        else:
            nf.err("No teaser available to export.")
        return 1

    nf.log("")
    nf.info("Export plan:")
    for item in pending:
        dest_media = pendientes / item["media_name"]
        dest_json = pendientes / f"{item['post']['id']}.json"
        have_json, have_media = dest_json.exists(), dest_media.exists()
        if have_json and have_media and not args.force:
            flag = " (ALREADY QUEUED: skipped)"
        elif have_json or have_media:
            flag = " (incomplete enqueue: repaired)"
        else:
            flag = ""
        nf.log(f"    - {dest_json.name}")
        nf.log(f"      media : {item['src'].name}  ->  {dest_media}{flag}")
        nf.log(f"      hook  : {str(item['post']['hook'])[:70]}")

    if not args.apply:
        nf.log("")
        nf.info("This was a PLAN. Run again with --apply to copy to the queue.")
        return 0 if (missing == 0 and invalid == 0) else 1

    copied = repaired = skipped = 0
    for item in pending:
        status, dest_json, dest_media = enqueue_item(
            pendientes, item["post"], item["src"], item["media_name"], force=args.force
        )
        if status == "skipped":
            nf.warn(f"{dest_json.name}: already queued (media + json); skipped (use --force to replace).")
            skipped += 1
        elif status == "repaired":
            nf.ok(f"Repaired (part was missing): {dest_json.name} + {dest_media.name}")
            repaired += 1
        else:
            nf.ok(f"Queued: {dest_json.name} + {dest_media.name}")
            copied += 1
    if copied == 0 and repaired == 0:
        nf.warn("Nothing was copied (everything already existed). Use --force to replace.")
        return 0
    if repaired:
        nf.info(f"Repaired: {repaired} (previously incomplete enqueues).")

    nf.log("")
    nf.log("-" * 70)
    nf.ok(f"{copied + repaired} teaser(s) in cola/pendientes of {publisher.name}.")
    nf.info("Publisher dry run (publishes nothing):")
    nf.log(f'    cd "{publisher}"')
    nf.log(f"    python src\\orquestador.py --publicar-siguiente --seco")
    nf.info("Real publishing (one at a time, in order):")
    nf.log(f"    python src\\orquestador.py --publicar-siguiente")
    nf.info("Or on an automatic schedule (daemon with US EST slots): run_auto.bat")
    nf.log("")
    nf.info("16:9 master (upload manually to YouTube):")
    nf.log(f"    {paths['output'] / 'publish_pack'}")
    nf.log("")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except nf.NFError as exc:
        nf.err(str(exc))
        sys.exit(1)

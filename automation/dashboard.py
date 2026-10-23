#!/usr/bin/env python3
"""Local production dashboard for novel_factory episodes.

Builds a self-contained dashboard (HTML + embedded prompts) from
master_episode.json, frames/ and raw_clips/, with optional durable tracking
persisted to dashboard_tracking.json through a local stdlib HTTP server.

Usage:
  python automation/dashboard.py mi_episodio
  python automation/dashboard.py mi_episodio --serve --open
  python automation/dashboard.py mi_episodio --serve --port 8787
  python automation/dashboard.py mi_episodio --out otra_ruta.html
"""
from __future__ import annotations

import argparse
import html
import importlib.util
import json
import mimetypes
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import unquote, urlparse

NF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(NF_ROOT))
import nf_core as nf  # noqa: E402

TRACKING_FILENAME = "dashboard_tracking.json"
DASHBOARD_FILENAME = "dashboard.html"
DEFAULT_PORT = 8787


def _load_generator(module_name: str, filename: str):
    path = NF_ROOT / "generators" / filename
    spec = importlib.util.spec_from_file_location(module_name, path)
    if not spec or not spec.loader:
        raise nf.NFError(f"Could not load generator: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


GEN02 = _load_generator("nf_dashboard_gen02", "02_export_chatgpt_queue.py")
GEN03 = _load_generator("nf_dashboard_gen03", "03_export_omni_queue.py")
MPL = _load_generator("nf_dashboard_mpl", "master_prompts_library.py")
VIDEO_PLATFORMS = [
    {"id": "omni", "label": "Omni 1.1 Flash"},
    {"id": "muse", "label": "Muse AI"},
    {"id": "flow", "label": "Google Flow (Veo)"},
]


def _relative(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.name


def _reference_file(references_dir: Path, stem: str) -> Optional[Path]:
    for ext in nf.FRAME_EXTS:
        candidate = references_dir / f"{stem}{ext}"
        if candidate.exists():
            return candidate
    hits = sorted(p for p in references_dir.glob(f"{stem}.*") if p.suffix.lower() in nf.FRAME_EXTS)
    return hits[0] if hits else None


def _reference_entry(paths: Dict[str, Path], root: Path, sheet: Dict[str, Any]) -> Dict[str, Any]:
    stem = Path(str(sheet.get("filename") or "")).stem
    local = _reference_file(paths["references"], stem) if stem else None
    existing_raw = str(sheet.get("existing_image") or "").strip()
    existing: Optional[Path] = None
    if existing_raw:
        candidate = Path(existing_raw)
        if not candidate.is_absolute():
            candidate = paths["root"] / candidate
        if candidate.exists():
            existing = candidate
    chosen = local or existing
    inside_root = False
    if chosen:
        try:
            inside_root = chosen.resolve() == root.resolve() or root.resolve() in chosen.resolve().parents
        except OSError:
            inside_root = False
    return {
        "id": str(sheet.get("id") or ""),
        "name": str(sheet.get("name") or sheet.get("id") or ""),
        "filename": str(sheet.get("filename") or ""),
        "prompt": str(sheet.get("prompt") or ""),
        "existing_image": existing_raw,
        "file": _relative(chosen, root) if chosen and inside_root else "",
        "exists": bool(chosen),
        "external": bool(existing and existing == chosen and not local),
    }


def _scene_entry(
    master: Dict[str, Any],
    scene: Dict[str, Any],
    paths: Dict[str, Path],
    root: Path,
    style: Dict[str, Any],
    image_entry: Dict[str, Any],
    covers: set[int],
) -> Dict[str, Any]:
    sid = int(scene.get("scene_id") or 0)
    frame = nf.find_frame(paths["frames"], sid)
    clip = nf.find_clip(paths["raw_clips"], sid)
    cast = []
    for character in nf.scene_cast(master, scene):
        name = str(character.get("name") or character.get("id") or "").strip()
        if name and name not in cast:
            cast.append(name)
    if not cast:
        cast = [str(c) for c in (scene.get("characters") or []) if str(c).strip()]
    dialogue = [
        {
            "speaker": str(item.get("speaker") or "").strip(),
            "line": str(item.get("line") or "").strip(),
            "delivery": str(item.get("delivery") or "").strip(),
        }
        for item in nf.scene_dialogue_lines(scene)
    ]
    cuts = [
        {
            "at": float(cut.get("at") or 0.0),
            "framing": str(cut.get("framing") or "").strip(),
            "action": str(cut.get("action") or "").strip(),
            "dialogue": bool(cut.get("dialogue")),
            "silent": bool(cut.get("silent")),
            "kind": str(cut.get("kind") or "").strip(),
            "speakers": [str(s) for s in (cut.get("speakers") or [])],
            "range": str(cut.get("range") or ""),
        }
        for cut in (scene.get("internal_cuts") or [])
        if isinstance(cut, dict)
    ]
    return {
        "scene_id": sid,
        "act": int(scene.get("act") or 0),
        "beat": str(scene.get("beat") or ""),
        "location": str(scene.get("location") or ""),
        "time_of_day": str(scene.get("time_of_day") or ""),
        "hook": str(scene.get("on_screen_hook") or ""),
        "cast": cast,
        "dialogue": dialogue,
        "cuts": cuts,
        "present_silent": [str(item) for item in (scene.get("present_silent") or [])],
        "key_object": str((scene.get("object_start") or {}).get("name") or scene.get("key_object") or "").strip(),
        "diegetic_text": [str(item) for item in (scene.get("diegetic_text") or []) if str(item).strip()],
        "shot_lock_version": str(scene.get("shot_lock_version") or ""),
        "sfx": str(scene.get("sfx_ambience") or ""),
        "continuity": str(scene.get("continuity") or ""),
        "camera": str(scene.get("camera") or ""),
        "duration_s": float(scene.get("duration_s") or nf.SCENE_SECONDS),
        "teaser_cover": sid in covers,
        "image_prompt": str(image_entry.get("prompt") or ""),
        "references": [str(item) for item in (image_entry.get("references") or [])],
        "face_crops": [str(item) for item in (image_entry.get("face_crops") or [])],
        "video_prompt": GEN03.compose_video_prompt(master, scene, paths, style, "omni"),
        "video_prompts": {
            platform["id"]: GEN03.compose_video_prompt(master, scene, paths, style, platform["id"])
            for platform in VIDEO_PLATFORMS
        },
        "frame_file": _relative(frame, root) if frame else "",
        "frame_exists": bool(frame),
        "clip_file": _relative(clip, root) if clip else "",
        "clip_exists": bool(clip),
        "clip_size": int(clip.stat().st_size) if clip else 0,
        "scene_json": json.dumps(scene, ensure_ascii=False, indent=2),
    }


def _project_choices(current_root: Path) -> List[Dict[str, Any]]:
    choices: List[Dict[str, Any]] = []
    seen = set()
    projects_dir = NF_ROOT / "projects"
    if projects_dir.exists():
        for child in sorted(projects_dir.iterdir(), key=lambda item: item.name.lower()):
            master = child / "master_episode.json"
            if not child.is_dir() or not master.exists():
                continue
            try:
                data = nf.read_json(master, default={})
            except Exception:
                data = {}
            slug = nf.slugify(str((data.get("episode") or {}).get("slug") or child.name))
            choices.append({
                "slug": slug,
                "title": str((data.get("episode") or {}).get("title") or slug.replace("_", " ").title()),
            })
            seen.add(slug)
    current_slug = nf.slugify(current_root.name)
    if current_slug not in seen:
        try:
            data = nf.read_json(current_root / "master_episode.json", default={})
        except Exception:
            data = {}
        choices.append({
            "slug": current_slug,
            "title": str((data.get("episode") or {}).get("title") or current_root.name),
        })
    for choice in choices:
        choice["active"] = choice["slug"] == current_slug
    return sorted(choices, key=lambda item: item["title"].lower())


def build_state(project: str | Path, paths: Optional[Dict[str, Path]] = None) -> Dict[str, Any]:
    paths = paths or nf.resolve_project(project)
    master = nf.load_master(paths["root"])
    style = nf.load_style_locks()
    rules = nf.load_showrunner()
    root = paths["root"]
    ep = nf.episode_meta(master)
    prepared = nf.prepare_master_locks_safe(master, style)
    image_entries = {int(e["scene_id"]): e for e in GEN02.build_queue(prepared, style)}
    covers = set(GEN02.teaser_cover_scenes(prepared))
    references = [_reference_entry(paths, root, sheet) for sheet in GEN02.build_reference_sheets(prepared)]
    scenes = [
        _scene_entry(prepared, scene, paths, root, style, image_entries.get(int(scene.get("scene_id") or 0), {}), covers)
        for scene in nf.ordered_scenes(prepared)
    ]
    brief_path = root / "story_brief.md"
    brief_text = ""
    if brief_path.exists():
        try:
            brief_text = brief_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            brief_text = ""
    prompt_pack = MPL.build_prompt_pack(master, style, brief_text)
    try:
        viral_catalog = MPL.list_viral_templates()
    except Exception:
        viral_catalog = []
    base_prompt_000 = ""
    for prompt in prompt_pack.get("prompts") or []:
        if prompt.get("key") == "prompt_000":
            base_prompt_000 = str(prompt.get("text") or "")
            break
    viral_items: List[Dict[str, Any]] = []
    for template in viral_catalog:
        try:
            prompt_text = base_prompt_000.rstrip() + "\n\n" + MPL.render_viral_niche_block(template)
        except Exception:
            prompt_text = base_prompt_000
        viral_items.append({
            "id": str(template.get("id") or ""),
            "label": str(template.get("label") or ""),
            "category": str(template.get("category") or ""),
            "rpm_rank": template.get("rpm_rank"),
            "description": str(template.get("description") or ""),
            "prompt": prompt_text,
        })
    viral_templates = {"default": "", "count": len(viral_items), "items": viral_items}
    try:
        muse_batches = MPL.build_muse_batches(master, style)
    except Exception:
        muse_batches = []
    try:
        storyboard_grids = GEN02.build_storyboard_grid_items(master, style, prompt_pack)
        storyboard_grids_text = GEN02.render_storyboard_grid_queue_text(storyboard_grids)
    except Exception:
        storyboard_grids = []
        storyboard_grids_text = ""

    output = paths["output"]
    teasers: List[str] = []
    masters: List[str] = []
    report_exists = (output / "report.json").exists()
    if output.exists():
        teasers = sorted(p.name for p in output.glob("teaser_*.mp4"))
        masters = sorted(p.name for p in output.glob("*_master_16x9_1080p.mp4"))

    storyboards_dir = root / "storyboards"
    on_disk: Dict[str, str] = {}
    if storyboards_dir.exists():
        for candidate in storyboards_dir.iterdir():
            if candidate.is_file():
                on_disk[candidate.name.lower()] = candidate.name
    storyboards_disk = 0
    for item in storyboard_grids:
        filename = str(item.get("filename") or "")
        match = on_disk.get(filename.lower(), "")
        if item.get("kind") == "cast_sheet" and not match:
            cast_file = _reference_file(paths["references"], Path(filename).stem)
            if cast_file:
                match = cast_file.name
        item["exists"] = bool(match)
        item["disk_file"] = match
        item["save_path"] = (
            f"references/{filename}" if item.get("kind") == "cast_sheet"
            else f"storyboards/{filename}"
        )
        if match:
            storyboards_disk += 1

    batch_files: List[str] = []
    expected_batches = max(1, int(ep.get("total_blocks") or nf.master_target_minutes(master)))
    raw_clips = paths["raw_clips"]
    for number in range(1, expected_batches + 1):
        for pattern in ("minute_{n:02d}.mp4", "batch_{n:02d}.mp4",
                        "minute_{n}.mp4", "batch_{n}.mp4"):
            candidate = raw_clips / pattern.format(n=number)
            if candidate.exists():
                batch_files.append(candidate.name)
                break
    for batch in muse_batches:
        for suffix, key in (("", "16x9"), ("_vertical", "9x16")):
            number = int(batch.get("batch_id") or 0)
            filename = f"minute_{number:02d}{suffix}.mp4"
            candidate = raw_clips / filename
            batch[f"video_exists_{key}"] = candidate.exists()
            batch[f"video_file_{key}"] = candidate.name if candidate.exists() else ""
            batch[f"video_path_{key}"] = f"raw_clips/{filename}"
            batch[f"save_as_{key}"] = f"raw_clips/{filename}"
    scene_clips_disk = sum(1 for scene in scenes if scene["clip_exists"])
    if scenes and scene_clips_disk == len(scenes):
        clip_mode = "scenes"
    elif len(batch_files) == expected_batches:
        clip_mode = "batches"
    elif batch_files or scene_clips_disk:
        clip_mode = "incomplete"
    else:
        clip_mode = "empty"

    return {
        "version": 1,
        "generated_at": nf.now_iso(),
        "slug": nf.slugify(str(ep.get("slug") or root.name)),
        "title": str(ep.get("title") or ep.get("slug") or root.name),
        "logline": str(ep.get("logline") or ""),
        "genre": str(ep.get("genre") or ""),
        "setting": str(ep.get("setting") or ""),
        "project_dir": str(root),
        "platforms": VIDEO_PLATFORMS,
        "references": references,
        "scenes": scenes,
        "master_prompts": {
            "generated_at": prompt_pack["generated_at"],
            "values": prompt_pack["values"],
            "items": prompt_pack["prompts"],
        },
        "viral_templates": viral_templates,
        "viral_latam_templates": [
            template for template in (rules.get("viral_latam_to_usa_templates") or [])
            if isinstance(template, dict)
        ],
        "projects": _project_choices(root),
        "muse_batches": muse_batches,
        "storyboard_grids": {
            "count": len(storyboard_grids),
            "items": storyboard_grids,
            "text": storyboard_grids_text,
        },
        "assembly": {
            "clip_mode": clip_mode,
            "scene_clips_disk": scene_clips_disk,
            "batch_clips": batch_files,
            "batch_clips_disk": len(batch_files),
            "storyboards_disk": storyboards_disk,
            "storyboards_expected": len(storyboard_grids),
            "storyboards_dir": str(storyboards_dir),
            "minutes_expected": nf.master_target_minutes(master),
            "teasers": teasers,
            "masters": masters,
            "report": report_exists,
        },
        "totals": {
            "scenes": len(scenes),
            "minutes": nf.master_target_minutes(master),
            "blocks": max(1, int(ep.get("total_blocks") or (len(scenes) + 5) // 6)),
            "master_prompts": len(prompt_pack["prompts"]),
            "muse_batches": len(muse_batches),
            "storyboard_grids": len(storyboard_grids),
            "references": len(references),
            "references_disk": sum(1 for r in references if r["exists"]),
            "frames_disk": sum(1 for s in scenes if s["frame_exists"]),
            "clips_disk": scene_clips_disk,
            "batch_clips_disk": len(batch_files),
            "storyboards_disk": storyboards_disk,
            "teasers": len(teasers),
            "masters": len(masters),
        },
    }


def tracking_path(paths: Dict[str, Path]) -> Path:
    return paths["root"] / TRACKING_FILENAME


def load_tracking(paths: Dict[str, Path]) -> Dict[str, Any]:
    data = nf.read_json(tracking_path(paths), default=None)
    if not isinstance(data, dict):
        data = {}
    if not isinstance(data.get("scenes"), dict):
        data["scenes"] = {}
    if not isinstance(data.get("references"), dict):
        data["references"] = {}
    data.setdefault("updated_at", "")
    return data


def save_tracking(paths: Dict[str, Path], data: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(data, dict):
        raise nf.NFError("Tracking must be a JSON object.")
    if not isinstance(data.get("scenes"), dict) or not isinstance(data.get("references"), dict):
        raise nf.NFError("Tracking must include 'scenes' and 'references' as objects.")
    data["updated_at"] = nf.now_iso()
    nf.write_json(tracking_path(paths), data)
    return data


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__ · Novel Factory Dashboard</title>
<style>
  :root {
    --bg: #070b12;
    --panel: #0f1726;
    --panel-2: #131d30;
    --border: #223049;
    --border-soft: #1a2437;
    --text: #e8eefc;
    --muted: #93a3bd;
    --accent: #38bdf8;
    --accent-2: #22c55e;
    --warn: #f59e0b;
    --danger: #ef4444;
    --violet: #a78bfa;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 14px; line-height: 1.45; padding: 22px 18px 60px; }
  button, input, select, textarea { font: inherit; color: inherit; }
  a { color: var(--accent); }
  header { max-width: 1540px; margin: 0 auto 16px; }
  .title-row { display: flex; align-items: flex-start; justify-content: space-between; gap: 16px; flex-wrap: wrap; }
  h1 { font-size: 25px; letter-spacing: -0.4px; }
  h1 span { color: var(--accent); }
  .sub { color: var(--muted); margin-top: 4px; max-width: 900px; }
  .mode { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.7px; padding: 5px 10px; border-radius: 999px; border: 1px solid var(--border); color: var(--muted); background: var(--panel); white-space: nowrap; }
  .mode.server { color: #6ee7b7; border-color: #166534; background: #052e1b; }
  .progress-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 10px; margin-top: 14px; }
  .progress { background: var(--panel); border: 1px solid var(--border); border-radius: 12px; padding: 11px 13px; }
  .progress-top { display: flex; justify-content: space-between; align-items: baseline; gap: 8px; font-size: 12px; color: var(--muted); font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
  .progress-top b { color: #fff; font-size: 15px; letter-spacing: 0; }
  .bar { height: 7px; border-radius: 999px; background: #0a1220; margin-top: 8px; overflow: hidden; }
  .bar > span { display: block; height: 100%; border-radius: 999px; background: linear-gradient(90deg, var(--accent), var(--accent-2)); transition: width 0.3s; }
  .toolbar { position: sticky; top: 0; z-index: 20; background: rgba(7, 11, 18, 0.94); backdrop-filter: blur(10px); border-bottom: 1px solid var(--border-soft); padding: 12px 0; margin: 16px 0 18px; }
  .toolbar-inner { max-width: 1540px; margin: 0 auto; display: flex; gap: 10px; align-items: center; flex-wrap: wrap; }
  .tabs { display: flex; gap: 6px; flex-wrap: wrap; }
  .tab { background: var(--panel); border: 1px solid var(--border); color: var(--muted); padding: 9px 14px; border-radius: 9px; font-weight: 700; font-size: 13px; cursor: pointer; }
  .tab:hover { color: #fff; border-color: #3b4d6d; }
  .tab.active { background: var(--accent); border-color: var(--accent); color: #06121f; }
  .spacer { flex: 1; }
  .btn { background: var(--panel-2); border: 1px solid var(--border); color: var(--text); padding: 9px 13px; border-radius: 9px; font-weight: 700; font-size: 13px; cursor: pointer; white-space: nowrap; }
  .btn:hover { border-color: var(--accent); }
  .btn.primary { background: #1d4ed8; border-color: #2563eb; color: #fff; }
  .btn.primary:hover { background: #2563eb; }
  .btn.green { background: #065f46; border-color: #059669; color: #d1fae5; }
  .btn.green:hover { background: #047857; }
  .btn.ghost { background: transparent; color: var(--muted); }
  .btn.ghost:hover { color: #fff; }
  .btn.small { padding: 6px 10px; font-size: 12px; }
  .filters { max-width: 1540px; margin: 0 auto 18px; display: flex; gap: 9px; align-items: center; flex-wrap: wrap; }
  .filters input[type="search"], .filters select { background: var(--panel); border: 1px solid var(--border); border-radius: 9px; padding: 9px 12px; color: var(--text); outline: none; }
  .filters input[type="search"] { min-width: 260px; flex: 1; max-width: 460px; }
  .filters input[type="search"]:focus, .filters select:focus { border-color: var(--accent); }
  .check { display: inline-flex; gap: 7px; align-items: center; color: var(--muted); background: var(--panel); border: 1px solid var(--border); padding: 8px 11px; border-radius: 9px; cursor: pointer; user-select: none; font-size: 12px; font-weight: 600; }
  .check input { accent-color: var(--accent-2); }
  .container { max-width: 1540px; margin: 0 auto; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(390px, 1fr)); gap: 16px; }
  .card { background: var(--panel); border: 1px solid var(--border); border-radius: 14px; padding: 15px; display: flex; flex-direction: column; gap: 10px; position: relative; }
  .card:hover { border-color: #3b4d6d; }
  .card.is-done { border-color: #14532d; background: #0a1420; }
  .card-top { display: flex; gap: 10px; align-items: flex-start; }
  .scene-id { min-width: 52px; font-size: 13px; font-weight: 800; color: var(--accent); background: #082033; border: 1px solid #164e63; padding: 5px 7px; border-radius: 8px; text-align: center; }
  .card-title { font-size: 14px; font-weight: 700; color: #fff; line-height: 1.3; }
  .meta { display: flex; flex-wrap: wrap; gap: 5px; margin-top: 6px; }
  .badge { font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; padding: 3px 8px; border-radius: 999px; border: 1px solid var(--border); background: #0b1424; color: var(--muted); white-space: nowrap; }
  .badge.act { color: #c4b5fd; border-color: #4c1d95; background: #170f2e; }
  .badge.hook { color: #fcd34d; border-color: #78350f; background: #2a1a05; }
  .badge.cover { color: #fda4af; border-color: #881337; background: #2a0712; }
  .badge.ok { color: #6ee7b7; border-color: #065f46; background: #052e1b; }
  .badge.copied { color: #7dd3fc; border-color: #075985; background: #082f49; }
  .badge.file { color: #86efac; border-color: #166534; background: #052e16; }
  .thumb { width: 100%; aspect-ratio: 16 / 9; object-fit: cover; border-radius: 10px; border: 1px solid var(--border); background: #030712; }
  .hook { font-size: 12px; color: #fcd34d; font-weight: 700; }
  .cast { display: flex; flex-wrap: wrap; gap: 4px; }
  .chip { font-size: 11px; color: #cbd5e1; background: #162133; border: 1px solid var(--border); border-radius: 999px; padding: 2px 8px; }
  .prompt { background: #040810; border: 1px solid var(--border-soft); border-radius: 10px; padding: 11px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11px; line-height: 1.5; color: #b9c6dc; white-space: pre-wrap; word-break: break-word; max-height: 190px; overflow: auto; }
  .prompt.huge { max-height: 560px; }
  .master-head { display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; flex-wrap: wrap; margin-bottom: 14px; }
  .master-head h2 { font-size: 18px; }
  .master-head p { color: var(--muted); font-size: 12px; max-width: 760px; margin-top: 4px; }
  .master-actions { display: flex; gap: 8px; flex-wrap: wrap; }
  .niche-picker { background: linear-gradient(135deg, #071a2b, #0b1424 55%); border: 1px solid #164e63; border-radius: 16px; padding: 16px 18px; margin-bottom: 18px; display: flex; flex-direction: column; gap: 10px; }
  .niche-picker-head { display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; flex-wrap: wrap; }
  .niche-picker-head b { color: #fff; font-size: 15px; }
  .niche-picker-head p { color: var(--muted); font-size: 12px; margin-top: 4px; max-width: 900px; }
  .niche-picker label { color: var(--muted); font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.6px; }
  .niche-picker select { background: var(--panel); border: 1px solid var(--border); border-radius: 9px; padding: 9px 12px; color: var(--text); outline: none; max-width: 680px; }
  .niche-picker select:focus { border-color: var(--accent); }
  .badge.niche { color: #ddd6fe; border-color: #6d28d9; background: #1e1238; }
  .quick-access { display: flex; gap: 8px; flex-wrap: wrap; margin: 0 0 18px; }
  .quick-access .btn { flex: 0 1 auto; }
  .method { background: linear-gradient(135deg, #071a2b, #0b1424 55%); border: 1px solid #164e63; border-radius: 16px; padding: 18px; margin-bottom: 20px; }
  .method h2 { font-size: 18px; }
  .method p { color: var(--muted); font-size: 12px; margin-top: 4px; max-width: 900px; }
  .steps { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 12px; margin-top: 14px; }
  .step { background: #040c18; border: 1px solid var(--border); border-radius: 12px; padding: 13px; display: flex; flex-direction: column; gap: 8px; }
  .step b { color: #fff; font-size: 13px; }
  .step p { margin: 0; }
  .step-num { width: 26px; height: 26px; border-radius: 50%; background: var(--accent); color: #06121f; font-weight: 900; display: flex; align-items: center; justify-content: center; font-size: 13px; }
  .step .btn { margin-top: auto; }
  .method-foot { margin-top: 12px; color: #a5f3fc; font-size: 12px; }
  .guide-head { display: flex; align-items: flex-start; justify-content: space-between; gap: 18px; flex-wrap: wrap; background: linear-gradient(135deg, #071a2b, #0b1424 55%); border: 1px solid #164e63; border-radius: 16px; padding: 18px; margin-bottom: 18px; }
  .guide-head h2 { font-size: 20px; }
  .guide-head p { color: var(--muted); font-size: 12px; margin-top: 5px; max-width: 780px; }
  .guide-controls { display: flex; gap: 10px; flex-wrap: wrap; align-items: flex-end; }
  .guide-controls label { display: flex; flex-direction: column; gap: 5px; color: var(--muted); font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.6px; }
  .guide-controls select { background: var(--panel); border: 1px solid var(--border); border-radius: 9px; padding: 9px 11px; color: var(--text); outline: none; min-width: 180px; max-width: 280px; }
  .guide-controls select:focus { border-color: var(--accent); }
  .step-card { background: var(--panel); border: 1px solid var(--border); border-radius: 16px; padding: 17px; margin-bottom: 14px; display: flex; flex-direction: column; gap: 12px; }
  .step-card.done { border-color: #14532d; box-shadow: inset 0 0 0 1px #14532d; }
  .step-card-head { display: flex; align-items: flex-start; gap: 12px; flex-wrap: wrap; }
  .step-card-head h3 { font-size: 17px; color: #fff; }
  .step-card-head p { color: var(--muted); font-size: 12px; margin-top: 4px; max-width: 920px; }
  .step-card-head .step-status { margin-left: auto; }
  .step-body { display: flex; flex-direction: column; gap: 10px; }
  .step-status { font-size: 11px; font-weight: 800; border-radius: 999px; padding: 6px 11px; border: 1px solid var(--border); background: #0b1424; color: var(--muted); white-space: nowrap; }
  .step-status.ok { color: #6ee7b7; border-color: #166534; background: #052e1b; }
  .step-status.pending { color: #fcd34d; border-color: #78350f; background: #2a1a05; }
  .step-actions { display: flex; gap: 8px; flex-wrap: wrap; }
  .save-path { font-size: 12px; color: var(--muted); }
  .save-path code { color: #a5f3fc; background: #040c18; border: 1px solid var(--border); border-radius: 6px; padding: 2px 6px; }
  .mini-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 9px; }
  .mini-card { background: #040c18; border: 1px solid var(--border); border-radius: 10px; padding: 10px; display: flex; flex-direction: column; gap: 7px; }
  .mini-card.done { border-color: #14532d; background: #06150f; }
  .mini-card b { font-size: 12px; color: #fff; }
  .mini-card span { font-size: 11px; color: var(--muted); }
  .mini-card .actions { margin-top: auto; }
  .mini-card .btn { padding: 6px 8px; font-size: 11px; }
  .prompt-details summary { cursor: pointer; color: var(--accent); font-size: 12px; font-weight: 700; }
  .legacy { margin-top: 22px; border: 1px solid var(--border); border-radius: 14px; background: #0a111d; }
  .legacy > summary { cursor: pointer; padding: 14px 16px; font-weight: 800; color: #cbd5e1; }
  .legacy > summary::marker { color: var(--accent); }
  .legacy-body { padding: 0 16px 16px; display: flex; flex-direction: column; gap: 14px; }
  .legacy-links { display: flex; gap: 8px; flex-wrap: wrap; }
  .guide-note { color: var(--muted); font-size: 12px; }
  .actions { display: flex; gap: 8px; margin-top: auto; flex-wrap: wrap; }
  .actions .btn { flex: 1; }
  .actions .btn.ghost { flex: 0 0 auto; }
  .dialogue { display: flex; flex-direction: column; gap: 6px; }
  .line { font-size: 12px; color: #cbd5e1; }
  .line b { color: #fff; }
  .line em { color: var(--muted); font-style: normal; font-size: 11px; }
  .cuts { display: flex; flex-direction: column; gap: 4px; font-size: 11px; color: var(--muted); }
  .cuts b { color: #c4b5fd; }
  .detail { font-size: 12px; color: var(--muted); }
  .detail b { color: #cbd5e1; }
  .empty { text-align: center; color: var(--muted); padding: 60px 20px; border: 1px dashed var(--border); border-radius: 14px; }
  .toast { position: fixed; right: 20px; bottom: 20px; background: #065f46; border: 1px solid #10b981; color: #d1fae5; padding: 12px 18px; border-radius: 10px; font-weight: 700; box-shadow: 0 10px 30px rgba(0,0,0,0.45); opacity: 0; pointer-events: none; transition: opacity 0.2s; z-index: 200; }
  .toast.show { opacity: 1; }
  .toast.error { background: #7f1d1d; border-color: #ef4444; color: #fee2e2; }
  body[data-tab="references"] .scene-only, body[data-tab="prompts"] .scene-only { display: none; }
  body[data-tab="prompts"] #copy-next { display: none; }
  body[data-tab="frames"] .ref-only, body[data-tab="clips"] .ref-only, body[data-tab="script"] .ref-only, body[data-tab="prompts"] .ref-only { display: none; }
  @media (max-width: 620px) {
    body { padding: 14px 10px 40px; }
    .grid { grid-template-columns: 1fr; }
    .filters input[type="search"] { min-width: 100%; }
  }
</style>
</head>
<body>
<header>
  <div class="title-row">
    <div>
      <h1>Novel Factory <span>Dashboard</span></h1>
      <div class="sub" id="project-sub">Loading project...</div>
    </div>
    <div class="guide-controls">
      <label>Project <select id="project-select" aria-label="Project"></select></label>
      <label>Format <select id="format-select" aria-label="Output format">
        <option value="16x9">16:9 · YouTube</option>
        <option value="9x16">9:16 · Reels / TikTok / Shorts</option>
      </select></label>
      <button class="btn ghost small" id="legacy-btn" data-action="toggle-legacy">Show legacy method</button>
      <div class="mode" id="mode">file mode</div>
    </div>
  </div>
  <div class="progress-grid" id="progress"></div>
</header>

<div class="toolbar">
  <div class="toolbar-inner">
    <div class="tabs" id="tabs"></div>
    <div class="spacer"></div>
    <button class="btn primary" id="copy-next">Copy next pending</button>
    <button class="btn" id="rescan">Reload state</button>
    <button class="btn" id="export">Export tracking</button>
    <button class="btn" id="import-btn">Import</button>
    <button class="btn ghost" id="reset">Reset</button>
    <input type="file" id="import-file" accept="application/json,.json" hidden>
  </div>
</div>

<div class="filters">
  <input type="search" id="q" placeholder="Search scene, location, beat, dialogue, cast...">
  <select id="state-filter" class="scene-only">
    <option value="all">All states</option>
    <option value="pending">Pending</option>
    <option value="copied">Copied, not marked</option>
    <option value="done">Done</option>
  </select>
  <select id="platform-filter" class="scene-only" title="Video platform">
    <option value="omni">Omni 1.1 Flash</option>
    <option value="muse">Muse AI</option>
    <option value="flow">Google Flow (Veo)</option>
  </select>
  <select id="act-filter" class="scene-only">
    <option value="all">All acts</option>
    <option value="1">Act 1</option>
    <option value="2">Act 2</option>
    <option value="3">Act 3</option>
    <option value="4">Act 4</option>
    <option value="5">Act 5</option>
    <option value="6">Act 6</option>
  </select>
  <label class="check scene-only"><input type="checkbox" id="teaser-filter"> Teaser covers only</label>
  <label class="check scene-only"><input type="checkbox" id="hide-done"> Hide done</label>
</div>

<main class="container" id="content"></main>
<div class="toast" id="toast"></div>

<script>
const STATE = __STATE_JSON__;
const TRACKING_SEED = __TRACKING_JSON__;
const MODE = "__MODE__";
const LOCAL_KEY = "novelfactory_tracking_" + (STATE.slug || "episode");
const NICHE_KEY = "novelfactory_niche_" + (STATE.slug || "episode");
const FORMAT_KEY = "novelfactory_format";
const VIRAL_KEY = "novelfactory_latam_template";
let state = STATE;
let tracking = normalizeTracking(TRACKING_SEED);
let activeTab = "clips";
let platform = "omni";
let selectedNiche = "";
let format = "16x9";
let selectedViralTemplate = "";
try { selectedNiche = localStorage.getItem(NICHE_KEY) || ""; } catch (e) {}
try { format = localStorage.getItem(FORMAT_KEY) === "9x16" ? "9x16" : "16x9"; } catch (e) {}
try { selectedViralTemplate = localStorage.getItem(VIRAL_KEY) || ""; } catch (e) {}
let filters = { state: "all", act: "all", q: "", teaser: false, hideDone: false };
let saveTimer = null;

function normalizeTracking(raw) {
  const data = raw && typeof raw === "object" ? raw : {};
  if (!data.scenes || typeof data.scenes !== "object") data.scenes = {};
  if (!data.references || typeof data.references !== "object") data.references = {};
  data.updated_at = data.updated_at || "";
  return data;
}

const $ = (sel) => document.querySelector(sel);
const esc = (value) => String(value == null ? "" : value).replace(/[&<>"']/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch]));

function sceneTrack(id) {
  const key = String(id);
  if (!tracking.scenes[key] || typeof tracking.scenes[key] !== "object") tracking.scenes[key] = {};
  return tracking.scenes[key];
}
function sceneData(id) { return tracking.scenes[String(id)] || {}; }
function refTrack(id) {
  const key = String(id);
  if (!tracking.references[key] || typeof tracking.references[key] !== "object") tracking.references[key] = {};
  return tracking.references[key];
}
function refData(id) { return tracking.references[String(id)] || {}; }
function platformLabel(id) {
  const found = (state.platforms || []).find((item) => item.id === id);
  return found ? found.label : id;
}
function sceneVideoPrompt(scene) {
  return (scene.video_prompts && scene.video_prompts[platform]) || scene.video_prompt || "";
}
function frameDone(scene) { return !!scene.frame_exists || !!sceneData(scene.scene_id).image_done; }
function clipDone(scene) { return !!scene.clip_exists || !!sceneData(scene.scene_id).video_done; }
function refDone(ref) { return !!ref.exists || !!refData(ref.id).done; }
function isDone(kind, item) {
  if (kind === "frames") return frameDone(item);
  if (kind === "clips") return clipDone(item);
  if (kind === "references") return refDone(item);
  return clipDone(item);
}
function isCopied(kind, item) {
  if (kind === "references") return !!refData(item.id).copied;
  const field = kind === "frames" ? "image_copied" : "video_copied";
  return !!sceneData(item.scene_id)[field];
}
function pruneTracking() {
  for (const [key, value] of Object.entries(tracking.scenes)) {
    if (!value || typeof value !== "object" || !Object.keys(value).length) delete tracking.scenes[key];
  }
  for (const [key, value] of Object.entries(tracking.references)) {
    if (!value || typeof value !== "object" || !Object.keys(value).length) delete tracking.references[key];
  }
}
function touchTracking() {
  pruneTracking();
  tracking.updated_at = new Date().toISOString();
  try { localStorage.setItem(LOCAL_KEY, JSON.stringify(tracking)); } catch (e) {}
  if (MODE === "server") {
    clearTimeout(saveTimer);
    saveTimer = setTimeout(async () => {
      try {
        const res = await fetch("/api/tracking", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(tracking) });
        if (!res.ok) throw new Error("bad status");
        toast("Tracking saved to disk");
      } catch (e) {
        toast("Saved locally (server unavailable)", true);
      }
    }, 300);
  }
}
function toast(message, isError) {
  const el = $("#toast");
  el.textContent = message;
  el.classList.toggle("error", !!isError);
  el.classList.add("show");
  clearTimeout(el._timer);
  el._timer = setTimeout(() => el.classList.remove("show"), 1800);
}
async function copyText(text, message) {
  try {
    await navigator.clipboard.writeText(text);
    toast(message || "Copied");
  } catch (e) {
    const area = document.createElement("textarea");
    area.value = text;
    area.style.position = "fixed";
    area.style.opacity = "0";
    document.body.appendChild(area);
    area.select();
    document.execCommand("copy");
    area.remove();
    toast(message || "Copied");
  }
}

function castMaster() {
  return storyboardGrids().items.find((item) => item.kind === "cast_sheet") || null;
}

function storyboardItems() {
  return storyboardGrids().items.filter((item) => item.kind !== "cast_sheet");
}

function storyboardDoneCount() {
  return storyboardItems().filter((item) => item.exists).length;
}

function batchDone(batch, fmt) {
  return fmt === "9x16" ? !!batch.video_exists_9x16 : !!batch.video_exists_16x9;
}

function batchesDoneCount(fmt) {
  return museBatches().filter((batch) => batchDone(batch, fmt)).length;
}

function formatLabel() {
  return format === "9x16" ? "9:16 · Reels / TikTok / Shorts" : "16:9 · YouTube";
}

function batchPrompt(batch, fmt) {
  if (fmt === "9x16") return batch.prompt_9x16_vertical || batch.prompt_916 || batch.prompt || batch.muse_command_916 || "";
  return batch.prompt_16x9_youtube || batch.prompt_169 || batch.prompt || batch.muse_command || "";
}

function batchCommand(batch, fmt) {
  return fmt === "9x16" ? (batch.muse_command_916 || batch.muse_command || "") : (batch.muse_command || "");
}

function batchSavePath(batch, fmt) {
  if (fmt === "9x16") return batch.save_as_9x16 || `raw_clips/minute_${String(batch.batch_id || 0).padStart(2, "0")}_vertical.mp4`;
  return batch.save_as_16x9 || batch.save_as || `raw_clips/minute_${String(batch.batch_id || 0).padStart(2, "0")}.mp4`;
}

function renderProjectSelect() {
  const select = $("#project-select");
  if (!select) return;
  const projects = Array.isArray(state.projects) ? state.projects : [];
  select.innerHTML = projects.length
    ? projects.map((item) => `<option value="${esc(item.slug)}"${item.slug === state.slug ? " selected" : ""}>${esc(item.title)}</option>`).join("")
    : `<option value="${esc(state.slug)}">${esc(state.title)}</option>`;
}

function renderProgress() {
  const images = state.assembly.storyboards_disk || 0;
  const imagesMax = state.assembly.storyboards_expected || 1;
  const storyboardMax = storyboardItems().length || 1;
  const batchMax = museBatches().length || 1;
  const cast = castMaster();
  const bars = [
    ["STEP 1 · Character sheet", cast && cast.exists ? 1 : 0, 1],
    ["STEP 2 · Storyboards", storyboardDoneCount(), storyboardMax],
    ["STEP 3 · Muse AI batches", batchesDoneCount(format), batchMax],
    ["STEP 4 · Assembled master", state.assembly.masters.length ? 1 : 0, 1],
    ["Master prompts", (state.master_prompts && state.master_prompts.items ? state.master_prompts.items.length : 0), 4],
  ];
  $("#progress").innerHTML = bars.map(([label, value, max]) => {
    const pct = Math.min(100, Math.round((value / (max || 1)) * 100));
    return `<div class="progress"><div class="progress-top"><span>${esc(label)}</span><b>${value}/${max}</b></div><div class="bar"><span style="width:${pct}%"></span></div></div>`;
  }).join("");
  const mode = $("#mode");
  mode.textContent = MODE === "server" ? "local server · on-disk tracking" : "file mode · browser tracking";
  mode.classList.toggle("server", MODE === "server");
  const moviePart = `${images}/${imagesMax} images · ${batchesDoneCount(format)}/${batchMax} 1-min batches`;
  const durationPart = `${state.totals.minutes || 0} min · ${state.totals.blocks || 0} blocks · ${state.scenes.length} scenes`;
  $("#project-sub").innerHTML = `<b>${esc(state.title)}</b> · ${esc(state.slug)} · ${durationPart} · ${moviePart}`;
  renderProjectSelect();
  const formatSelect = $("#format-select");
  if (formatSelect) formatSelect.value = format;
  syncLegacyButton();
}

function syncLegacyButton() {
  const button = $("#legacy-btn");
  const details = $("#legacy-details");
  if (!button) return;
  const open = !!(details && details.open);
  button.textContent = open ? "Hide legacy method" : "Show legacy method";
  button.classList.toggle("active", open);
}

function renderTabs() {
  const tabs = [
    ["clips", "Clips (video v2)", state.scenes.length],
    ["frames", "Frames (image)", state.scenes.length],
    ["script", "Script", state.scenes.length],
    ["prompts", "Production guide", 4],
    ["references", References, state.references.length],
  ];
  $("#tabs").innerHTML = tabs.map(([id, label, count]) => `<button class="tab ${activeTab === id ? "active" : ""}" data-tab="${id}">${label} (${count})</button>`).join("");
  syncLegacyButton();
}

function matchesScene(scene, kind) {
  const done = isDone(kind, scene);
  const copied = isCopied(kind, scene);
  if (filters.state === "pending" && done) return false;
  if (filters.state === "done" && !done) return false;
  if (filters.state === "copied" && (!copied || done)) return false;
  if (filters.hideDone && done) return false;
  if (filters.act !== "all" && String(scene.act) !== filters.act) return false;
  if (filters.teaser && !scene.teaser_cover) return false;
  if (filters.q) {
    const hay = [
      scene.scene_id, scene.location, scene.beat, scene.hook, scene.time_of_day,
      scene.cast.join(" "), scene.dialogue.map((d) => d.speaker + " " + d.line).join(" "),
    ].join(" ").toLowerCase();
    if (!hay.includes(filters.q)) return false;
  }
  return true;
}

function matchesRef(ref) {
  const done = refDone(ref);
  if (filters.state === "pending" && done) return false;
  if (filters.state === "done" && !done) return false;
  if (filters.hideDone && done) return false;
  if (filters.q) {
    const hay = [ref.name, ref.filename, ref.prompt].join(" ").toLowerCase();
    if (!hay.includes(filters.q)) return false;
  }
  return true;
}

function metaBadges(scene) {
  const badges = [`<span class="badge act">Act ${scene.act || "?"}</span>`];
  if (scene.beat) badges.push(`<span class="badge">${esc(scene.beat)}</span>`);
  if (scene.teaser_cover) badges.push(`<span class="badge cover">Teaser cover</span>`);
  if (scene.hook) badges.push(`<span class="badge hook">Hook</span>`);
  return badges.join("");
}

function stateBadges(kind, scene) {
  const badges = [];
  const file = kind === "frames" ? scene.frame_exists : (kind === "clips" || kind === "script") ? scene.clip_exists : false;
  if (file) badges.push(`<span class="badge file">✓ File on disk</span>`);
  if (isCopied(kind, scene)) badges.push(`<span class="badge copied">Copied</span>`);
  if (isDone(kind, scene) && !file) badges.push(`<span class="badge ok">Done</span>`);
  return badges.join("");
}

function thumb(scene) {
  if (!scene.frame_exists || !scene.frame_file) return "";
  return `<img class="thumb" loading="lazy" src="${esc(scene.frame_file)}" alt="Scene ${scene.scene_id} frame">`;
}

function sceneCard(scene, kind) {
  const done = isDone(kind, scene);
  const file = kind === "frames" ? scene.frame_exists : scene.clip_exists;
  const prompt = kind === "frames" ? scene.image_prompt : sceneVideoPrompt(scene);
  const markButton = file
    ? `<span class="btn green small" style="text-align:center;cursor:default">✓ On disk</span>`
    : `<button class="btn ${done ? "green" : ""}" data-action="mark" data-kind="${kind}" data-id="${scene.scene_id}">${done ? "✓ Done" : "Mark done"}</button>`;
  return `<article class="card ${done ? "is-done" : ""}" id="card-${kind}-${scene.scene_id}">
    <div class="card-top">
      <div class="scene-id">#${scene.scene_id}</div>
      <div style="flex:1">
        <div class="card-title">${esc(scene.location || "No location")}</div>
        <div class="meta">${metaBadges(scene)} ${stateBadges(kind, scene)}</div>
      </div>
    </div>
    ${thumb(scene)}
    ${scene.hook ? `<div class="hook">${esc(scene.hook)}</div>` : ""}
    ${scene.cast.length ? `<div class="cast">${scene.cast.map((name) => `<span class="chip">${esc(name)}</span>`).join("")}</div>` : ""}
    ${kind === "frames" ? `<div class="detail"><b>Frame:</b> ${esc(scene.frame_file || `frames/frame_${String(scene.scene_id).padStart(3, "0")}.png`)}</div>` : `<div class="detail"><b>Clip:</b> ${esc(scene.clip_file || `raw_clips/scene_${String(scene.scene_id).padStart(3, "0")}.mp4`)} · <b>Platform:</b> ${esc(platformLabel(platform))}</div>`}
    ${kind === "frames" && scene.face_crops && scene.face_crops.length ? `<div class="detail"><b>Extra attachment:</b> ${esc(scene.face_crops.join(", "))} (speaking character face crop)</div>` : ""}
    <pre class="prompt">${esc(prompt)}</pre>
    <div class="actions">
      <button class="btn primary" data-action="copy" data-kind="${kind}" data-id="${scene.scene_id}">Copy prompt</button>
      ${markButton}
    </div>
  </article>`;
}

function scriptCard(scene) {
  const done = clipDone(scene);
  const dialogue = scene.dialogue.map((line) => `<div class="line"><b>${esc(line.speaker)}</b>${line.delivery ? ` <em>(${esc(line.delivery)})</em>` : ""}: ${esc(line.line)}</div>`).join("");
  const cuts = (scene.cuts || []).map((cut) => {
    let tag = "";
    if (cut.dialogue) {
      const spk = cut.speakers && cut.speakers.length ? cut.speakers.join(", ") : "";
      tag = ` <span class="badge ok" style="font-size:10px;padding:1px 5px">SPEAKING${spk ? `: ${esc(spk)}` : ""}</span>`;
    } else if (cut.silent) {
      tag = ` <span class="badge" style="font-size:10px;padding:1px 5px;background:#334155;color:#94a3b8">SILENCE</span>`;
    }
    const range = cut.range ? `[${esc(cut.range)}] ` : "";
    return `<div><b>${cut.at.toFixed(1)} s</b> · ${range}${esc(cut.framing)}: ${esc(cut.action)}${tag}</div>`;
  }).join("");
  return `<article class="card ${done ? "is-done" : ""}">
    <div class="card-top">
      <div class="scene-id">#${scene.scene_id}</div>
      <div style="flex:1">
        <div class="card-title">${esc(scene.location || "No location")}</div>
        <div class="meta">${metaBadges(scene)} ${stateBadges("script", scene)}</div>
      </div>
    </div>
    ${scene.hook ? `<div class="hook">${esc(scene.hook)}</div>` : ""}
    ${scene.cast.length ? `<div class="cast">${scene.cast.map((name) => `<span class="chip">${esc(name)}</span>`).join("")}</div>` : ""}
    <div class="detail"><b>Time:</b> ${esc(scene.time_of_day || "—")} · <b>Duration:</b> ${scene.duration_s.toFixed(1)} s</div>
    ${dialogue ? `<div class="dialogue">${dialogue}</div>` : `<div class="detail">No dialogue (diegetic ambience).</div>`}
    ${cuts ? `<div class="cuts">${cuts}</div>` : ""}
    ${scene.key_object ? `<div class="detail"><b>Key object (Lock):</b> ${esc(scene.key_object)}</div>` : ""}
    ${scene.present_silent && scene.present_silent.length ? `<div class="detail"><b>Silent characters in scene:</b> ${esc(scene.present_silent.join(", "))} (mouth closed)</div>` : ""}
    ${scene.diegetic_text && scene.diegetic_text.length ? `<div class="detail"><b>Diegetic text:</b> ${esc(scene.diegetic_text.join(", "))}</div>` : ""}
    <div class="detail"><b>SFX / ambience:</b> ${esc(scene.sfx || "—")}</div>
    <div class="detail"><b>Continuity:</b> ${esc(scene.continuity || "—")}</div>
    <div class="detail"><b>Camera:</b> ${esc(scene.camera || "—")}</div>
    <div class="actions">
      <button class="btn primary" data-action="copy-dialogue" data-kind="script" data-id="${scene.scene_id}">Copy dialogue</button>
      <button class="btn" data-action="copy-json" data-kind="script" data-id="${scene.scene_id}">Copy scene JSON</button>
    </div>
  </article>`;
}

function referenceCard(ref) {
  const done = refDone(ref);
  const prompt = ref.prompt || `Attach the existing image of ${ref.name} to the ChatGPT conversation. You do not need to generate it.`;
  return `<article class="card ${done ? "is-done" : ""}">
    <div class="card-top">
      <div class="scene-id">REF</div>
      <div style="flex:1">
        <div class="card-title">${esc(ref.name)}</div>
        <div class="meta">
          <span class="badge">${esc(ref.filename || "reference")}</span>
          ${ref.exists ? `<span class="badge file">✓ File on disk</span>` : ""}
          ${ref.external ? `<span class="badge hook">External image</span>` : ""}
          ${isCopied("references", ref) ? `<span class="badge copied">Copied</span>` : ""}
          ${done && !ref.exists ? `<span class="badge ok">Done</span>` : ""}
        </div>
      </div>
    </div>
    ${ref.file ? `<img class="thumb" loading="lazy" src="${esc(ref.file)}" alt="${esc(ref.name)}">` : ""}
    <pre class="prompt">${esc(prompt)}</pre>
    <div class="actions">
      <button class="btn primary" data-action="copy" data-kind="references" data-id="${esc(ref.id)}">Copy prompt</button>
      ${ref.exists ? `<span class="btn green small" style="text-align:center;cursor:default">✓ On disk</span>` : `<button class="btn ${done ? "green" : ""}" data-action="mark" data-kind="references" data-id="${esc(ref.id)}">${done ? "✓ Done" : "Mark done"}</button>`}
    </div>
  </article>`;
}

function masterItems() {
  return (state.master_prompts && state.master_prompts.items) || [];
}

function nicheCatalog() {
  return (state.viral_templates && Array.isArray(state.viral_templates.items)) ? state.viral_templates.items : [];
}

function currentNiche() {
  if (!selectedNiche) return null;
  return nicheCatalog().find((item) => item.id === selectedNiche) || null;
}

function effectiveMasterPrompt(prompt) {
  if (!prompt || prompt.key !== "prompt_000") return prompt;
  const niche = currentNiche();
  if (!niche || !niche.prompt) return prompt;
  const text = niche.prompt;
  return Object.assign({}, prompt, {
    text: text,
    chars: text.length,
    words: (text.match(/\S+/g) || []).length,
  });
}

function validateNiche() {
  const fallback = (state.viral_templates && state.viral_templates.default) || "";
  const ids = nicheCatalog().map((item) => item.id);
  if (selectedNiche && ids.includes(selectedNiche)) return;
  selectedNiche = fallback && ids.includes(fallback) ? fallback : "";
}

function nichePicker() {
  const catalog = nicheCatalog();
  if (!catalog.length) return "";
  const niche = currentNiche();
  const options = catalog.map((item) => `<option value="${esc(item.id)}"${niche && niche.id === item.id ? " selected" : ""}>${esc(item.category)} · ${esc(item.label)}</option>`).join("");
  return `<section class="niche-picker">
    <div class="niche-picker-head">
      <div>
        <b>USA mega-niche for PROMPT 000</b>
        <p>${niche ? esc(niche.description) : "No mega-niche: PROMPT 000 uses the project free base idea."}</p>
      </div>
      ${niche ? `<button class="btn primary" data-action="copy-master" data-id="prompt_000">Copy PROMPT 000 with this niche</button>` : ""}
    </div>
    <label for="niche-select">Archetype</label>
    <select id="niche-select">
      <option value=""${niche ? "" : " selected"}>No mega-niche (free)</option>
      ${options}
    </select>
  </section>`;
}

function museBatches() {
  return Array.isArray(state.muse_batches) ? state.muse_batches : [];
}

function storyboardGrids() {
  return state.storyboard_grids || { count: 0, items: [], text: "" };
}

function storyboardGridsText() {
  const grids = storyboardGrids();
  if (grids.text) return grids.text;
  return (grids.items || []).map((item) => item.prompt).join("\n");
}

function quickPromptButtons() {
  return masterItems().map((prompt) => `<button class="btn" data-action="copy-master" data-id="${esc(prompt.key)}">${esc(prompt.code)} · ${esc(prompt.title)}</button>`).join("");
}

function museBatchCard(batch) {
  const first = batch.scenes && batch.scenes.length ? batch.scenes[0] : "?";
  const last = batch.scenes && batch.scenes.length ? batch.scenes[batch.scenes.length - 1] : "?";
  const refs = batch.reference_images || ["REF_CAST_MASTER.png", `REF_GRID_MIN_${String(batch.batch_id || 0).padStart(2, "0")}.png`];
  const done = batchDone(batch, format);
  const active169 = format === "16x9" ? "primary" : "green";
  const active916 = format === "9x16" ? "primary" : "green";
  return `<article class="card ${done ? "is-done" : ""}">
    <div class="card-top">
      <div class="scene-id">${String(batch.batch_id || 0).padStart(2, "0")}</div>
      <div style="flex:1">
        <div class="card-title">Minute ${batch.minute} · Block ${batch.batch_id}</div>
        <div class="meta">
          <span class="badge">Scenes ${first}–${last}</span>
          <span class="badge">${esc(batch.start_timecode)}–${esc(batch.end_timecode)}</span>
          <span class="badge ${done ? "ok" : "hook"}">${done ? "✅ On disk" : "⏳ Pending"}</span>
        </div>
        <div class="cast" style="margin-top:6px">${refs.map((ref) => `<span class="chip">📎 ${esc(ref)}</span>`).join("")}</div>
      </div>
    </div>
    <div class="save-path">
      <b>16:9:</b> <code>${esc(batchSavePath(batch, "16x9"))}</code> ${batch.video_exists_16x9 ? "✅" : "⏳"} ·
      <b>9:16:</b> <code>${esc(batchSavePath(batch, "9x16"))}</code> ${batch.video_exists_9x16 ? "✅" : "⏳"}
    </div>
    <pre class="prompt huge">${esc(batchPrompt(batch, format))}</pre>
    <div class="actions">
      <button class="btn ${active169}" data-action="copy-muse-batch-169" data-id="${esc(batch.batch_id)}">Copy 16:9 YouTube</button>
      <button class="btn ${active916}" data-action="copy-muse-batch-916" data-id="${esc(batch.batch_id)}">Copy 9:16 Reels</button>
      <button class="btn ghost" data-action="download-muse-batch" data-id="${esc(batch.batch_id)}">Download .txt</button>
    </div>
  </article>`;
}

function storyboardMiniCard(item) {
  const first = item.scenes && item.scenes.length ? item.scenes[0] : "";
  const last = item.scenes && item.scenes.length ? item.scenes[item.scenes.length - 1] : "";
  return `<article class="mini-card ${item.exists ? "done" : ""}">
    <b>Minute ${esc(item.minute || item.index)}</b>
    <span>Scenes ${first}–${last}</span>
    <span>${esc(item.filename)}</span>
    <span class="step-status ${item.exists ? "ok" : "pending"}">${item.exists ? "✅ On disk" : "⏳ Pending"}</span>
    <div class="actions"><button class="btn small" data-action="copy-storyboard-grid" data-id="${esc(item.index)}">Copy prompt</button></div>
  </article>`;
}

function guideStep(number, title, description, status, body) {
  return `<section class="step-card ${status.ok ? "done" : ""}">
    <div class="step-card-head">
      <div class="step-num">${number}</div>
      <div style="flex:1">
        <h3>STEP ${number} — ${esc(title)}</h3>
        <p>${description}</p>
      </div>
      <span class="step-status ${status.ok ? "ok" : "pending"}">${status.ok ? "✅ Ready" : "⏳ Pending"} · ${status.detail}</span>
    </div>
    <div class="step-body">${body}</div>
  </section>`;
}

function productionGuide() {
  const assembly = state.assembly || {};
  const cast = castMaster();
  const grids = storyboardItems();
  const batches = museBatches();
  const castReady = !!(cast && cast.exists);
  const gridsReady = grids.filter((item) => item.exists).length;
  const batchReady = batchesDoneCount(format);
  const masterReady = !!(assembly.masters && assembly.masters.length);
  const castPrompt = cast ? cast.prompt : "";
  const batchBody = batches.length
    ? `<div class="step-actions">
        <button class="btn primary" data-action="copy-muse-batches">Copy all ${batches.length} batches in ${esc(formatLabel())}</button>
        <button class="btn" data-action="download-muse-batches">Download batch .txt files</button>
      </div>
      <div class="grid">${batches.map(museBatchCard).join("")}</div>`
    : `<div class="empty">Generate the storyboard queue first, then reload the dashboard.</div>`;
  return `<section class="guide-head">
    <div>
      <h2>Four-step production flow</h2>
      <p>Copy and paste each block in the order shown. The format selector decides which complete prompt is copied into Muse AI; the attachment instruction stays outside the copyable text.</p>
    </div>
    <div class="guide-note">Current method: 1 character sheet + one storyboard per block + one 1-minute batch per block.</div>
  </section>
  ${guideStep(1, "Master character sheet",
    "Generate <b>REF_CAST_MASTER.png</b> in ChatGPT with the project real characters. It is the fixed reference for faces and wardrobe.",
    { ok: castReady, detail: castReady ? "1/1" : "0/1" },
    `<div class="save-path"><b>Save as:</b> <code>references/REF_CAST_MASTER.png</code></div>
     <div class="step-actions">
       ${cast ? `<button class="btn primary" data-action="copy-storyboard-grid" data-id="${esc(cast.index)}">Copy character prompt</button>` : ""}
       <span class="guide-note"><code>storyboards/REF_CAST_MASTER.png</code> is also accepted.</span>
     </div>
     ${castPrompt ? `<details class="prompt-details"><summary>Show cast prompt</summary><pre class="prompt">${esc(castPrompt)}</pre></details>` : ""}`)}
  ${guideStep(2, "Storyboards per minute",
    `Generate the ${grids.length} 3x2 grids in ChatGPT. Each image covers 6 scenes from one minute and must use the same faces and wardrobe as the cast.`,
    { ok: gridsReady >= grids.length, detail: `${gridsReady}/${grids.length}` },
    `<div class="save-path"><b>Save as:</b> <code>storyboards/REF_GRID_MIN_01.png … REF_GRID_MIN_${String(grids.length).padStart(2, "0")}.png</code></div>
     <div class="step-actions">
       <button class="btn primary" data-action="copy-storyboard-grids-10">Copy all ${grids.length} storyboards</button>
       <button class="btn" data-action="copy-storyboard-grids">Copy full queue (cast + ${grids.length})</button>
       <button class="btn" data-action="download-storyboard-grids">Download queue .txt</button>
     </div>
     <div class="mini-grid">${grids.map(storyboardMiniCard).join("")}</div>`)}
  ${guideStep(3, "1-minute batches in Muse AI",
    "For each batch attach <b>REF_CAST_MASTER.png</b> + <b>REF_GRID_MIN_0X.png</b>. Paste the complete script for the chosen format; the block already ends with the final command.",
    { ok: batchReady >= batches.length, detail: `${batchReady}/${batches.length}` },
    `<div class="save-path"><b>Active format:</b> ${esc(formatLabel())} · <b>Save as:</b> <code>raw_clips/minute_0X.mp4</code> ${format === "9x16" ? "(suffix <code>_vertical.mp4</code>)" : ""}</div>
     ${batchBody}`)}
  ${guideStep(4, "Assemble the master",
    `When all ${batches.length} batches exist, run the assembler. The 16:9 master and 9:16 teasers are saved in <b>output/</b>.`,
    { ok: masterReady, detail: masterReady ? `${assembly.masters.length} master` : "0/1" },
    `<div class="save-path"><b>Output:</b> <code>output/${esc(state.slug)}_master_16x9_1080p.mp4</code> ${masterReady ? "✅" : "⏳"}</div>
     <div class="step-actions">
       <button class="btn primary" data-action="copy-assemble-command">Copy assembly command</button>
       <button class="btn" data-action="goto-script">Review script</button>
     </div>
     <div class="guide-note">Teasers on disk: ${assembly.teasers ? assembly.teasers.length : 0} · Report: ${assembly.report ? "yes" : "pending"}.</div>`)}
  ${legacyPanel()}`;
}

function storyboardGridCard(item) {
  const isCast = item.kind === "cast_sheet";
  const label = isCast ? "CAST" : String(item.minute || item.index).padStart(2, "0");
  const first = item.scenes && item.scenes.length ? item.scenes[0] : "";
  const last = item.scenes && item.scenes.length ? item.scenes[item.scenes.length - 1] : "";
  return `<article class="card">
    <div class="card-top">
      <div class="scene-id">${esc(label)}</div>
      <div style="flex:1">
        <div class="card-title">${esc(item.title)}</div>
        <div class="meta">
          <span class="badge file">${esc(item.filename)}</span>
          ${item.scenes && item.scenes.length ? `<span class="badge">Scenes ${first}–${last}</span>` : `<span class="badge">Base reference</span>`}
          <span class="badge">${isCast ? "1 image 16:9" : "Grid 3x2 · 6 panels"}</span>
          <span class="badge ${item.exists ? "ok" : ""}">${item.exists ? "On disk" : "Pending"}</span>
        </div>
      </div>
    </div>
    <pre class="prompt huge">${esc(item.prompt)}</pre>
    <div class="actions">
      <button class="btn primary" data-action="copy-storyboard-grid" data-id="${esc(item.index)}">Copy prompt</button>
      <button class="btn" data-action="download-storyboard-grid" data-id="${esc(item.index)}">Download .txt</button>
    </div>
  </article>`;
}

function methodBanner() {
  const assembly = state.assembly || {};
  return `<div class="method" style="padding:13px 16px;margin-bottom:18px">
    <div class="master-head" style="margin-bottom:0">
      <div>
        <b>V2 contract active · ${state.totals.minutes || 0} min · ${state.totals.blocks || 0} blocks · ${state.totals.scenes || 0} scenes synced</b>
        <p>Production prompts with speaker shot lock, silence and on-camera objects. Images in <b>storyboards/</b>:
        <b>${assembly.storyboards_disk || 0}/${assembly.storyboards_expected || 1}</b> ·
        detected mode: <b>${clipModeLabel(assembly.clip_mode)}</b> ·
        batches on disk: <b>${assembly.batch_clips_disk || 0}/${state.totals.blocks || 0}</b>.</p>
      </div>
      <div class="master-actions">
        <button class="btn green" data-action="goto-prompts">View 4-step guide</button>
      </div>
    </div>
  </div>`;
}

function clipModeLabel(mode) {
  const scenes = (state.totals && state.totals.scenes) || 60;
  if (mode === "scenes") return `A — ${scenes} 10 s scenes`;
  if (mode === "batches") return `B — ${Math.ceil(scenes / 6)} 1-min Muse AI batches`;
  if (mode === "incomplete") return "incomplete (missing clips)";
  return "no clips yet";
}

function legacyPanel() {
  const items = masterItems();
  const grids = storyboardGrids();
  const batches = museBatches();
  const latam = Array.isArray(state.viral_latam_templates) ? state.viral_latam_templates : [];
  const selected = latam.find((item) => item.id === selectedViralTemplate) || latam[0] || null;
  const options = latam.map((item) => `<option value="${esc(item.id)}"${selected && item.id === selected.id ? " selected" : ""}>${esc(item.name)} · ${esc(item.views)}</option>`).join("");
  return `<details class="legacy" id="legacy-details">
    <summary>Legacy method and advanced options</summary>
    <div class="legacy-body">
      <div class="guide-note"><b>New methodology</b> — 1 character sheet + one grid and one 1-minute batch per block. This section keeps the references, frames, clips and individual 000–003 prompts tabs.</div>
      <div class="legacy-links">
        <button class="btn" data-tab="references">References (${state.references.length})</button>
        <button class="btn" data-tab="frames">Image frames (${state.scenes.length})</button>
        <button class="btn" data-tab="clips">Video clips (${state.scenes.length})</button>
      </div>
      ${nichePicker()}
      <div class="master-head" style="margin-bottom:0">
        <div>
          <h2>Master prompts 000–003</h2>
          <p>Complete prompts from the legacy method. PROMPT 000 includes the LATAM -> USA catalog when a mega-niche is selected.</p>
        </div>
        <div class="master-actions">
          <button class="btn primary" data-action="copy-master-all">Copy all ${items.length}</button>
          <button class="btn" data-action="download-master-all">Download JSON</button>
          ${grids.count ? `<button class="btn green" data-action="copy-storyboard-grids">Copy queue of ${grids.count} images</button>` : ""}
          ${batches.length ? `<button class="btn green" data-action="copy-muse-batches">Copy all ${batches.length} batches</button>` : ""}
        </div>
      </div>
      <div class="quick-access">${quickPromptButtons()}</div>
      <div class="grid">${items.map((item) => masterPromptCard(effectiveMasterPrompt(item))).join("")}</div>
      <div class="master-head" style="margin-bottom:0">
        <div>
          <h2>Create a project from a LATAM template</h2>
          <p>Choose one of the six viral structures and copy the command. Replace <code>new_project</code> and the premise before running it.</p>
        </div>
      </div>
      <div class="step-actions">
        <select id="viral-template-select" aria-label="LATAM template">${options}</select>
        <button class="btn primary" data-action="copy-new-project">Copy new project command</button>
      </div>
    </div>
  </details>`;
}

function matchesMaster(prompt) {
  if (!filters.q) return true;
  const hay = [prompt.code, prompt.title, prompt.purpose, prompt.text].join(" ").toLowerCase();
  return hay.includes(filters.q);
}

function downloadText(filename, text, mime) {
  const blob = new Blob([text], { type: mime || "text/plain;charset=utf-8" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(link.href), 1000);
}

function masterPromptCard(prompt) {
  const activeNiche = prompt.key === "prompt_000" ? currentNiche() : null;
  const missing = prompt.unfilled && prompt.unfilled.length
    ? `<span class="badge hook">Unfilled: ${esc(prompt.unfilled.join(", "))}</span>`
    : `<span class="badge ok">Complete</span>`;
  return `<article class="card">
    <div class="card-top">
      <div class="scene-id">${esc(String(prompt.code || "").replace("PROMPT ", ""))}</div>
      <div style="flex:1">
        <div class="card-title">${esc(prompt.title)}</div>
        <div class="meta">
          <span class="badge">${esc(prompt.code)}</span>
          ${activeNiche ? `<span class="badge niche">USA niche</span>` : ""}
          <span class="badge">${prompt.chars.toLocaleString()} chars</span>
          <span class="badge">${prompt.words.toLocaleString()} words</span>
          ${missing}
        </div>
      </div>
    </div>
    <div class="detail">${esc(prompt.purpose || "")}</div>
    <pre class="prompt huge">${esc(prompt.text)}</pre>
    <div class="actions">
      <button class="btn primary" data-action="copy-master" data-id="${esc(prompt.key)}">Copy prompt</button>
      <button class="btn" data-action="download-master" data-id="${esc(prompt.key)}">Download .txt</button>
    </div>
  </article>`;
}

function renderContent() {
  const holder = $("#content");
  if (activeTab === "prompts") {
    holder.innerHTML = productionGuide();
    const legacy = $("#legacy-details");
    if (legacy) legacy.addEventListener("toggle", syncLegacyButton);
    syncLegacyButton();
    return;
  }
  if (activeTab === "references") {
    const refs = state.references.filter(matchesRef);
    holder.innerHTML = `${methodBanner()}${refs.length ? `<div class="grid">${refs.map(referenceCard).join("")}</div>` : `<div class="empty">No references match the filter.</div>`}`;
    return;
  }
  const kind = activeTab === "frames" ? "frames" : "clips";
  const scenes = state.scenes.filter((scene) => matchesScene(scene, activeTab === "script" ? "clips" : kind));
  if (!scenes.length) {
    holder.innerHTML = `<div class="empty">No scenes match the filter.</div>`;
    return;
  }
  const cards = activeTab === "script" ? scenes.map(scriptCard) : scenes.map((scene) => sceneCard(scene, kind));
  holder.innerHTML = `${methodBanner()}<div class="grid">${cards.join("")}</div>`;
}

function render() {
  document.body.dataset.tab = activeTab;
  renderTabs();
  renderProgress();
  renderContent();
}

function findScene(id) { return state.scenes.find((scene) => String(scene.scene_id) === String(id)); }
function findRef(id) { return state.references.find((ref) => String(ref.id) === String(id)); }

async function handleAction(button) {
  const action = button.dataset.action;
  const kind = button.dataset.kind;
  const id = button.dataset.id;
  if (action === "toggle-legacy") {
    const openDetails = () => {
      const details = $("#legacy-details");
      if (!details) return;
      details.open = true;
      details.scrollIntoView({ behavior: "smooth", block: "start" });
      syncLegacyButton();
    };
    if ($("#legacy-details")) {
      openDetails();
      return;
    }
    activeTab = "prompts";
    render();
    requestAnimationFrame(openDetails);
    return;
  }
  if (action === "copy-master" || action === "download-master") {
    const prompt = effectiveMasterPrompt(masterItems().find((item) => item.key === id));
    if (!prompt) return;
    if (action === "copy-master") {
      await copyText(prompt.text, `${prompt.code} copied in full`);
    } else {
      downloadText(`${prompt.signature || prompt.key}.txt`, prompt.text);
      toast(`${prompt.code} downloaded`);
    }
    return;
  }
  if (action === "copy-master-all") {
    const text = masterItems().map(effectiveMasterPrompt).map((item) => `${item.code} — ${item.title}\n\n${item.text}`).join("\n\n\n");
    await copyText(text, "All 4 master prompts copied");
    return;
  }
  if (action === "download-master-all") {
    const manifest = Object.assign({}, state.master_prompts, {
      items: masterItems().map(effectiveMasterPrompt),
    });
    downloadText(`master_prompts_${state.slug || "episode"}.json`, JSON.stringify(manifest, null, 2), "application/json");
    toast("Prompt manifest downloaded");
    return;
  }
  if (action === "goto-prompts") {
    activeTab = "prompts";
    render();
    window.scrollTo({ top: 0, behavior: "smooth" });
    return;
  }
  if (action === "goto-script") {
    activeTab = "script";
    render();
    window.scrollTo({ top: 0, behavior: "smooth" });
    return;
  }
  if (action === "copy-storyboard-grids") {
    await copyText(storyboardGridsText(), `Queue of ${storyboardGrids().count} images copied (1 cast + ${storyboardItems().length} storyboards)`);
    return;
  }
  if (action === "copy-storyboard-grids-10") {
    const text = storyboardItems().map((item) => item.prompt).join("\n\n\n");
    await copyText(text, `Copied ${storyboardItems().length} storyboards in order`);
    return;
  }
  if (action === "download-storyboard-grids") {
    downloadText(`chatgpt_storyboard_grids_queue_${state.slug || "episode"}.txt`, storyboardGridsText());
    toast(`Queue of ${storyboardGrids().count} images downloaded`);
    return;
  }
  if (action === "copy-storyboard-grid" || action === "download-storyboard-grid") {
    const item = storyboardGrids().items.find((grid) => String(grid.index) === String(id));
    if (!item) return;
    if (action === "copy-storyboard-grid") {
      await copyText(item.prompt, `${item.filename} copied`);
    } else {
      downloadText(`${item.filename.replace(/\.png$/i, "")}_prompt.txt`, item.prompt);
      toast(`${item.filename} downloaded`);
    }
    return;
  }
  if (action === "copy-muse-batch-169" || action === "copy-muse-batch-916") {
    const batch = museBatches().find((item) => String(item.batch_id) === String(id));
    if (!batch) return;
    const vertical = action === "copy-muse-batch-916";
    const text = batchPrompt(batch, vertical ? "9x16" : "16x9");
    await copyText(text, `Full script ${vertical ? "9:16 (Reels)" : "16:9 (YouTube)"} for batch ${batch.batch_id} copied`);
    return;
  }
  if (action === "copy-assemble-command") {
    await copyText(`./novelfactory.bat assemble ${state.slug || "<project>"}`, "Assembly command copied");
    return;
  }
  if (action === "copy-muse-batch") {
    const batch = museBatches().find((item) => String(item.batch_id) === String(id));
    if (!batch) return;
    await copyText(batchPrompt(batch, format), `Batch ${batch.batch_id} copied (${formatLabel()})`);
    return;
  }
  if (action === "download-muse-batch") {
    const batch = museBatches().find((item) => String(item.batch_id) === String(id));
    if (!batch) return;
    downloadText(`muse_ai_batch_${String(batch.batch_id).padStart(2, "0")}_${format}.txt`, batchPrompt(batch, format));
    toast(`Batch ${batch.batch_id} downloaded`);
    return;
  }
  if (action === "copy-muse-batches") {
    const text = museBatches().map((batch) => `BLOCK ${batch.batch_id} — MINUTE ${batch.minute} — ${formatLabel()}\n\n${batchPrompt(batch, format)}`).join("\n\n\n");
    await copyText(text, `${museBatches().length} Muse AI batches copied (${formatLabel()})`);
    return;
  }
  if (action === "download-muse-batches") {
    const text = museBatches().map((batch) => `BLOCK ${batch.batch_id} — MINUTE ${batch.minute} — ${formatLabel()}\n\n${batchPrompt(batch, format)}`).join("\n\n\n");
    downloadText(`muse_ai_batches_${state.slug || "episode"}_${format}.txt`, text);
    toast("Muse AI batches downloaded");
    return;
  }
  if (action === "copy-new-project") {
    const latam = Array.isArray(state.viral_latam_templates) ? state.viral_latam_templates : [];
    const template = latam.find((item) => item.id === selectedViralTemplate) || latam[0];
    if (!template) return toast("No LATAM templates available", true);
    const command = `python generators/01_story_to_master_json.py new_project --viral-template ${template.id} --idea "Premise in 3-10 lines"`;
    await copyText(command, `Command to create a project with ${template.name}`);
    return;
  }
  if (action === "copy") {
    if (kind === "references") {
      const ref = findRef(id);
      if (!ref) return;
      refTrack(id).copied = new Date().toISOString();
      touchTracking();
      await copyText(ref.prompt || ref.name, "Reference prompt copied");
    } else {
      const scene = findScene(id);
      if (!scene) return;
      const field = kind === "frames" ? "image_copied" : "video_copied";
      sceneTrack(id)[field] = new Date().toISOString();
      touchTracking();
      await copyText(kind === "frames" ? scene.image_prompt : sceneVideoPrompt(scene), kind === "frames" ? "Image prompt copied" : `${platformLabel(platform)} prompt copied`);
    }
    renderContent();
    return;
  }
  if (action === "copy-dialogue") {
    const scene = findScene(id);
    if (!scene) return;
    const text = scene.dialogue.map((line) => `${line.speaker}${line.delivery ? ` (${line.delivery})` : ""}: "${line.line}"`).join("\n");
    await copyText(text || scene.video_prompt, "Dialogue copied");
    return;
  }
  if (action === "copy-json") {
    const scene = findScene(id);
    if (!scene) return;
    await copyText(scene.scene_json, "Scene JSON copied");
    return;
  }
  if (action === "mark") {
    if (kind === "references") {
      const item = refTrack(id);
      if (item.done) delete item.done; else item.done = new Date().toISOString();
    } else {
      const item = sceneTrack(id);
      const field = kind === "frames" ? "image_done" : "video_done";
      if (item[field]) delete item[field]; else item[field] = new Date().toISOString();
    }
    touchTracking();
    render();
  }
}

function copyNextPending() {
  if (activeTab === "prompts") {
    const prompt = effectiveMasterPrompt(masterItems()[0]);
    if (!prompt) return toast("No master prompts exported");
    copyText(prompt.text, `${prompt.code} copied`);
    return;
  }
  if (activeTab === "references") {
    const ref = state.references.find((item) => !refDone(item));
    if (!ref) return toast("No pending references left");
    refTrack(ref.id).copied = new Date().toISOString();
    touchTracking();
    copyText(ref.prompt || ref.name, `Reference copied: ${ref.name}`);
    renderContent();
    return;
  }
  const kind = activeTab === "frames" ? "frames" : "clips";
  const field = kind === "frames" ? "image_copied" : "video_copied";
  const scene = state.scenes.find((item) => !isDone(kind, item));
  if (!scene) return toast("No pending scenes left");
  sceneTrack(scene.scene_id)[field] = new Date().toISOString();
  touchTracking();
  copyText(kind === "frames" ? scene.image_prompt : sceneVideoPrompt(scene), `Scene ${scene.scene_id} copied (${kind === "frames" ? "image" : platformLabel(platform)})`);
  renderContent();
}

async function rescan() {
  if (MODE !== "server") {
    location.reload();
    return;
  }
  try {
    const res = await fetch("/api/rescan", { method: "POST" });
    if (!res.ok) throw new Error("bad status");
    const data = await res.json();
    state = data.state || state;
    render();
    toast("State reloaded from disk");
  } catch (e) {
    toast("Could not reload state", true);
  }
}

function exportTracking() {
  pruneTracking();
  const blob = new Blob([JSON.stringify(tracking, null, 2)], { type: "application/json" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = `tracking_${state.slug || "episode"}.json`;
  document.body.appendChild(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(link.href), 1000);
  toast("Tracking exportado");
}

function importTracking(file) {
  const reader = new FileReader();
  reader.onload = () => {
    try {
      const data = JSON.parse(reader.result);
      if (!data || typeof data !== "object" || !data.scenes) throw new Error("invalid");
      tracking = normalizeTracking(data);
      touchTracking();
      render();
      toast("Tracking importado");
    } catch (e) {
      toast("Invalid tracking file", true);
    }
  };
  reader.readAsText(file);
}

function resetTracking() {
  if (!confirm("Reset tracking? Frame and clip files are not deleted.")) return;
  tracking = { scenes: {}, references: {}, updated_at: new Date().toISOString() };
  touchTracking();
  render();
  toast("Tracking reiniciado");
}

document.addEventListener("click", (event) => {
  const actionButton = event.target.closest("[data-action]");
  if (actionButton) {
    event.preventDefault();
    handleAction(actionButton);
    return;
  }
  const tabButton = event.target.closest("[data-tab]");
  if (tabButton) {
    activeTab = tabButton.dataset.tab;
    render();
  }
});

document.addEventListener("change", (event) => {
  if (!event.target) return;
  if (event.target.id === "niche-select") {
    const value = event.target.value || "";
    selectedNiche = nicheCatalog().some((item) => item.id === value) ? value : "";
    try { localStorage.setItem(NICHE_KEY, selectedNiche); } catch (e) {}
    renderContent();
    const niche = currentNiche();
    toast(niche ? `Mega-niche active: ${niche.label}` : "No mega-niche");
    return;
  }
  if (event.target.id === "viral-template-select") {
    selectedViralTemplate = event.target.value || "";
    try { localStorage.setItem(VIRAL_KEY, selectedViralTemplate); } catch (e) {}
  }
});

$("#format-select").addEventListener("change", (event) => {
  format = event.target.value === "9x16" ? "9x16" : "16x9";
  try { localStorage.setItem(FORMAT_KEY, format); } catch (e) {}
  render();
  toast(`Active format: ${formatLabel()}`);
});

$("#project-select").addEventListener("change", (event) => {
  const slug = event.target.value || "";
  if (!slug || slug === state.slug) return;
  const servedByDashboard = MODE === "server" || window.location.pathname.startsWith("/p/");
  const target = servedByDashboard
    ? `/p/${encodeURIComponent(slug)}/`
    : `../${encodeURIComponent(slug)}/dashboard.html`;
  window.location.href = target;
});

$("#q").addEventListener("input", (event) => { filters.q = event.target.value.trim().toLowerCase(); renderContent(); });
$("#state-filter").addEventListener("change", (event) => { filters.state = event.target.value; renderContent(); });
$("#platform-filter").addEventListener("change", (event) => { platform = event.target.value; renderContent(); });
$("#act-filter").addEventListener("change", (event) => { filters.act = event.target.value; renderContent(); });
$("#teaser-filter").addEventListener("change", (event) => { filters.teaser = event.target.checked; renderContent(); });
$("#hide-done").addEventListener("change", (event) => { filters.hideDone = event.target.checked; renderContent(); });
$("#copy-next").addEventListener("click", copyNextPending);
$("#rescan").addEventListener("click", rescan);
$("#export").addEventListener("click", exportTracking);
$("#import-btn").addEventListener("click", () => $("#import-file").click());
$("#import-file").addEventListener("change", (event) => {
  if (event.target.files && event.target.files[0]) importTracking(event.target.files[0]);
  event.target.value = "";
});
$("#reset").addEventListener("click", resetTracking);

async function boot() {
  if (MODE === "server") {
    try {
      const res = await fetch("/api/state");
      if (res.ok) {
        const data = await res.json();
        if (data.state) state = data.state;
        if (data.tracking) tracking = normalizeTracking(data.tracking);
        let local = null;
        try { local = JSON.parse(localStorage.getItem(LOCAL_KEY) || "null"); } catch (e) {}
        if (local && !tracking.updated_at && local.updated_at) {
          tracking = normalizeTracking(local);
          touchTracking();
        }
      }
    } catch (e) {}
  } else {
    let local = null;
    try { local = JSON.parse(localStorage.getItem(LOCAL_KEY) || "null"); } catch (e) {}
    if (local && local.updated_at && (!tracking.updated_at || local.updated_at > tracking.updated_at)) {
      tracking = normalizeTracking(local);
    }
  }
  validateNiche();
  if (format !== "9x16" && format !== "16x9") format = "16x9";
  const latam = Array.isArray(state.viral_latam_templates) ? state.viral_latam_templates : [];
  if (!latam.some((item) => item.id === selectedViralTemplate)) selectedViralTemplate = latam.length ? latam[0].id : "";
  render();
}

boot();
</script>
</body>
</html>
"""


def render_dashboard(state: Dict[str, Any], tracking: Dict[str, Any], mode: str = "static") -> str:
    payload = json.dumps(state, ensure_ascii=False)
    tracking_payload = json.dumps(tracking, ensure_ascii=False)
    for token in ("<", ">", "&"):
        escaped = {"<": "\\u003c", ">": "\\u003e", "&": "\\u0026"}[token]
        payload = payload.replace(token, escaped)
        tracking_payload = tracking_payload.replace(token, escaped)
    return (
        HTML_TEMPLATE
        .replace("__TITLE__", html.escape(str(state.get("title") or "Episode"), quote=False))
        .replace("__STATE_JSON__", payload)
        .replace("__TRACKING_JSON__", tracking_payload)
        .replace("__MODE__", "server" if mode == "server" else "static")
    )


def write_dashboard(paths: Dict[str, Path], state: Dict[str, Any], tracking: Dict[str, Any], out: Optional[Path] = None, mode: str = "static") -> Path:
    target = Path(out) if out else (paths["root"] / DASHBOARD_FILENAME)
    nf.write_text(target, render_dashboard(state, tracking, mode))
    return target


class DashboardHandler(BaseHTTPRequestHandler):
    server_version = "NovelFactoryDashboard/1.0"
    project_paths: Dict[str, Path] = {}
    dashboard_path: Optional[Path] = None

    def log_message(self, format: str, *args: Any) -> None:
        return

    def _send_json(self, payload: Any, status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, path: Path) -> None:
        try:
            body = path.read_bytes()
        except OSError:
            self.send_error(404, "Not found")
            return
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        self.send_response(200)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _send_html(self, body: str) -> None:
        data = body.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _safe_project_file(self, url_path: str, root: Optional[Path] = None) -> Optional[Path]:
        base = (root or self.project_paths["root"]).resolve()
        candidate = (base / unquote(url_path).lstrip("/")).resolve()
        if candidate == base or base in candidate.parents:
            if candidate.is_file():
                return candidate
        return None

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        route = parsed.path
        if route.startswith("/p/"):
            parts = [part for part in route.split("/") if part]
            if len(parts) >= 2:
                slug = unquote(parts[1])
                rest = "/".join(parts[2:])
                try:
                    project_paths = nf.resolve_project(slug)
                except nf.NFError:
                    project_paths = {}
                if project_paths:
                    if rest in ("", "index.html", "dashboard.html"):
                        try:
                            state = build_state(project_paths["root"], project_paths)
                            body = render_dashboard(
                                state,
                                load_tracking(project_paths),
                                mode="static",
                            )
                            self._send_html(body)
                        except Exception as exc:  # noqa: BLE001
                            self._send_json({"error": str(exc)}, 500)
                        return
                    candidate = self._safe_project_file(rest, project_paths["root"])
                    if candidate:
                        self._send_file(candidate)
                        return
            self.send_error(404, "Not found")
            return
        if route in ("/", "/index.html", "/dashboard.html"):
            target = self.dashboard_path or (self.project_paths["root"] / DASHBOARD_FILENAME)
            if not target.exists():
                self.send_error(404, "dashboard.html does not exist; run the generator first")
                return
            self._send_file(target)
            return
        if route == "/api/state":
            try:
                state = build_state(self.project_paths["root"], self.project_paths)
                self._send_json({"state": state, "tracking": load_tracking(self.project_paths)})
            except Exception as exc:  # noqa: BLE001
                self._send_json({"error": str(exc)}, 500)
            return
        candidate = self._safe_project_file(route)
        if candidate:
            self._send_file(candidate)
            return
        self.send_error(404, "Not found")

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/api/rescan":
            try:
                state = build_state(self.project_paths["root"], self.project_paths)
                self._send_json({"ok": True, "state": state, "tracking": load_tracking(self.project_paths)})
            except Exception as exc:  # noqa: BLE001
                self._send_json({"error": str(exc)}, 500)
            return
        if parsed.path == "/api/tracking":
            try:
                length = int(self.headers.get("Content-Length") or 0)
                body = self.rfile.read(length)
                data = json.loads(body.decode("utf-8"))
                saved = save_tracking(self.project_paths, data)
                self._send_json({"ok": True, "tracking": saved})
            except Exception as exc:  # noqa: BLE001
                self._send_json({"error": str(exc)}, 400)
            return
        self.send_error(404, "Not found")


def serve(paths: Dict[str, Path], dashboard: Path, port: int, open_browser: bool) -> None:
    DashboardHandler.project_paths = paths
    DashboardHandler.dashboard_path = dashboard
    try:
        httpd = ThreadingHTTPServer(("127.0.0.1", port), DashboardHandler)
    except OSError as exc:
        raise nf.NFError(f"Could not open port {port}: {exc}. Try --port another_number.") from exc
    url = f"http://127.0.0.1:{port}/"
    nf.ok(f"Dashboard servido en {url}")
    nf.info(f"Project: {paths['root']}")
    nf.info(f"Tracking: {tracking_path(paths)}")
    nf.info("Ctrl+C to stop.")
    if open_browser:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        nf.info("Server stopped.")
    finally:
        httpd.server_close()


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Local per-episode production dashboard.")
    parser.add_argument("project", help="Episode slug or path to its folder.")
    parser.add_argument("--out", type=str, default="", help="Path to the generated HTML (default <project>/dashboard.html).")
    parser.add_argument("--serve", action="store_true", help="Serve the dashboard on 127.0.0.1 with persistent tracking.")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help=f"Local server port (default {DEFAULT_PORT}).")
    parser.add_argument("--open", action="store_true", help="Open the dashboard in the browser.")
    parser.add_argument("--quiet", action="store_true", help="Do not print the final summary.")
    args = parser.parse_args(argv)

    paths = nf.resolve_project(args.project)
    state = build_state(paths["root"], paths)
    tracking = load_tracking(paths)
    out = Path(args.out) if args.out else (paths["root"] / DASHBOARD_FILENAME)
    dashboard = write_dashboard(paths, state, tracking, out, mode="server" if args.serve else "static")

    if not args.quiet:
        nf.ok(f"Dashboard generated: {dashboard}")
        nf.info(f"Scenes: {state['totals']['scenes']} · frames on disk: {state['totals']['frames_disk']} · clips on disk: {state['totals']['clips_disk']}")
        nf.info(f"References: {state['totals']['references']} · teasers: {state['totals']['teasers']}")
        if not args.serve:
            nf.info("File mode: tracking is stored in the browser. Use --serve to store it on disk.")

    if args.serve or args.open:
        if args.serve:
            serve(paths, dashboard, args.port, args.open)
        else:
            webbrowser.open(dashboard.resolve().as_uri())
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except nf.NFError as exc:
        nf.err(str(exc))
        raise SystemExit(1)

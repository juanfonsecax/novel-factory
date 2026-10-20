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
        raise nf.NFError(f"No se pudo cargar el generador: {path}")
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
        "sfx": str(scene.get("sfx_ambience") or ""),
        "continuity": str(scene.get("continuity") or ""),
        "camera": str(scene.get("camera") or ""),
        "duration_s": float(scene.get("duration_s") or nf.SCENE_SECONDS),
        "teaser_cover": sid in covers,
        "image_prompt": str(image_entry.get("prompt") or ""),
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


def build_state(project: str | Path, paths: Optional[Dict[str, Path]] = None) -> Dict[str, Any]:
    paths = paths or nf.resolve_project(project)
    master = nf.load_master(paths["root"])
    style = nf.load_style_locks()
    root = paths["root"]
    ep = nf.episode_meta(master)
    image_entries = {int(e["scene_id"]): e for e in GEN02.build_queue(master, style)}
    covers = set(GEN02.teaser_cover_scenes(master))
    references = [_reference_entry(paths, root, sheet) for sheet in GEN02.build_reference_sheets(master)]
    scenes = [
        _scene_entry(master, scene, paths, root, style, image_entries.get(int(scene.get("scene_id") or 0), {}), covers)
        for scene in nf.ordered_scenes(master)
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
        "muse_batches": muse_batches,
        "storyboard_grids": {
            "count": len(storyboard_grids),
            "items": storyboard_grids,
            "text": storyboard_grids_text,
        },
        "assembly": {
            "teasers": teasers,
            "masters": masters,
            "report": report_exists,
        },
        "totals": {
            "scenes": len(scenes),
            "master_prompts": len(prompt_pack["prompts"]),
            "muse_batches": len(muse_batches),
            "storyboard_grids": len(storyboard_grids),
            "references": len(references),
            "references_disk": sum(1 for r in references if r["exists"]),
            "frames_disk": sum(1 for s in scenes if s["frame_exists"]),
            "clips_disk": sum(1 for s in scenes if s["clip_exists"]),
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
        raise nf.NFError("El tracking debe ser un objeto JSON.")
    if not isinstance(data.get("scenes"), dict) or not isinstance(data.get("references"), dict):
        raise nf.NFError("El tracking debe incluir 'scenes' y 'references' como objetos.")
    data["updated_at"] = nf.now_iso()
    nf.write_json(tracking_path(paths), data)
    return data


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="es">
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
  .quick-access { display: flex; gap: 8px; flex-wrap: wrap; margin: 0 0 18px; }
  .quick-access .btn { flex: 0 1 auto; }
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
      <div class="sub" id="project-sub">Cargando proyecto...</div>
    </div>
    <div class="mode" id="mode">modo archivo</div>
  </div>
  <div class="progress-grid" id="progress"></div>
</header>

<div class="toolbar">
  <div class="toolbar-inner">
    <div class="tabs" id="tabs"></div>
    <div class="spacer"></div>
    <button class="btn primary" id="copy-next">Copiar siguiente pendiente</button>
    <button class="btn" id="rescan">Recargar estado</button>
    <button class="btn" id="export">Exportar tracking</button>
    <button class="btn" id="import-btn">Importar</button>
    <button class="btn ghost" id="reset">Reiniciar</button>
    <input type="file" id="import-file" accept="application/json,.json" hidden>
  </div>
</div>

<div class="filters">
  <input type="search" id="q" placeholder="Buscar escena, lugar, beat, diálogo, reparto...">
  <select id="state-filter" class="scene-only">
    <option value="all">Todos los estados</option>
    <option value="pending">Pendientes</option>
    <option value="copied">Copiados sin marcar</option>
    <option value="done">Hechos</option>
  </select>
  <select id="platform-filter" class="scene-only" title="Plataforma de video">
    <option value="omni">Omni 1.1 Flash</option>
    <option value="muse">Muse AI</option>
    <option value="flow">Google Flow (Veo)</option>
  </select>
  <select id="act-filter" class="scene-only">
    <option value="all">Todos los actos</option>
    <option value="1">Acto 1</option>
    <option value="2">Acto 2</option>
    <option value="3">Acto 3</option>
    <option value="4">Acto 4</option>
    <option value="5">Acto 5</option>
    <option value="6">Acto 6</option>
  </select>
  <label class="check scene-only"><input type="checkbox" id="teaser-filter"> Solo portadas de teaser</label>
  <label class="check scene-only"><input type="checkbox" id="hide-done"> Ocultar hechos</label>
</div>

<main class="container" id="content"></main>
<div class="toast" id="toast"></div>

<script>
const STATE = __STATE_JSON__;
const TRACKING_SEED = __TRACKING_JSON__;
const MODE = "__MODE__";
const LOCAL_KEY = "novelfactory_tracking_" + (STATE.slug || "episode");
let state = STATE;
let tracking = normalizeTracking(TRACKING_SEED);
let activeTab = "frames";
let platform = "omni";
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
        toast("Tracking guardado en disco");
      } catch (e) {
        toast("Guardado local (servidor no disponible)", true);
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
    toast(message || "Copiado");
  } catch (e) {
    const area = document.createElement("textarea");
    area.value = text;
    area.style.position = "fixed";
    area.style.opacity = "0";
    document.body.appendChild(area);
    area.select();
    document.execCommand("copy");
    area.remove();
    toast(message || "Copiado");
  }
}

function renderProgress() {
  const total = state.scenes.length || 1;
  const frames = state.scenes.filter(frameDone).length;
  const clips = state.scenes.filter(clipDone).length;
  const markedFrames = state.scenes.filter((s) => sceneData(s.scene_id).image_done).length;
  const markedClips = state.scenes.filter((s) => sceneData(s.scene_id).video_done).length;
  const refs = state.references.filter(refDone).length;
  const bars = [
    ["Frames listos", frames, total],
    ["Clips listos", clips, total],
    ["Escenas completas", state.scenes.filter((s) => frameDone(s) && clipDone(s)).length, total],
    ["Marcados frame", markedFrames, total],
    ["Marcados clip", markedClips, total],
    ["Referencias", refs, state.references.length || 1],
    ["Prompts maestros", (state.master_prompts && state.master_prompts.items ? state.master_prompts.items.length : 0), 4],
    ["Teasers", state.assembly.teasers.length, 3],
  ];
  $("#progress").innerHTML = bars.map(([label, value, max]) => {
    const pct = Math.min(100, Math.round((value / (max || 1)) * 100));
    return `<div class="progress"><div class="progress-top"><span>${esc(label)}</span><b>${value}/${max}</b></div><div class="bar"><span style="width:${pct}%"></span></div></div>`;
  }).join("");
  const mode = $("#mode");
  mode.textContent = MODE === "server" ? "servidor local · tracking en disco" : "modo archivo · tracking en navegador";
  mode.classList.toggle("server", MODE === "server");
  $("#project-sub").innerHTML = `<b>${esc(state.title)}</b> · ${esc(state.slug)} · ${state.scenes.length} escenas · ${state.scenes.filter((s) => s.clip_exists).length} clips en disco`;
}

function renderTabs() {
  const masterCount = state.master_prompts && state.master_prompts.items ? state.master_prompts.items.length : 0;
  const tabs = [
    ["references", "Referencias", state.references.length],
    ["frames", "Frames (imagen)", state.scenes.length],
    ["clips", "Clips (video)", state.scenes.length],
    ["script", "Guion", state.scenes.length],
    ["prompts", "Prompts maestros", masterCount],
  ];
  $("#tabs").innerHTML = tabs.map(([id, label, count]) => `<button class="tab ${activeTab === id ? "active" : ""}" data-tab="${id}">${label} (${count})</button>`).join("");
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
  const badges = [`<span class="badge act">Acto ${scene.act || "?"}</span>`];
  if (scene.beat) badges.push(`<span class="badge">${esc(scene.beat)}</span>`);
  if (scene.teaser_cover) badges.push(`<span class="badge cover">Portada teaser</span>`);
  if (scene.hook) badges.push(`<span class="badge hook">Hook</span>`);
  return badges.join("");
}

function stateBadges(kind, scene) {
  const badges = [];
  const file = kind === "frames" ? scene.frame_exists : (kind === "clips" || kind === "script") ? scene.clip_exists : false;
  if (file) badges.push(`<span class="badge file">✓ Archivo en disco</span>`);
  if (isCopied(kind, scene)) badges.push(`<span class="badge copied">Copiado</span>`);
  if (isDone(kind, scene) && !file) badges.push(`<span class="badge ok">Hecho</span>`);
  return badges.join("");
}

function thumb(scene) {
  if (!scene.frame_exists || !scene.frame_file) return "";
  return `<img class="thumb" loading="lazy" src="${esc(scene.frame_file)}" alt="Frame escena ${scene.scene_id}">`;
}

function sceneCard(scene, kind) {
  const done = isDone(kind, scene);
  const file = kind === "frames" ? scene.frame_exists : scene.clip_exists;
  const prompt = kind === "frames" ? scene.image_prompt : sceneVideoPrompt(scene);
  const markButton = file
    ? `<span class="btn green small" style="text-align:center;cursor:default">✓ En disco</span>`
    : `<button class="btn ${done ? "green" : ""}" data-action="mark" data-kind="${kind}" data-id="${scene.scene_id}">${done ? "✓ Hecho" : "Marcar hecho"}</button>`;
  return `<article class="card ${done ? "is-done" : ""}" id="card-${kind}-${scene.scene_id}">
    <div class="card-top">
      <div class="scene-id">#${scene.scene_id}</div>
      <div style="flex:1">
        <div class="card-title">${esc(scene.location || "Sin locación")}</div>
        <div class="meta">${metaBadges(scene)} ${stateBadges(kind, scene)}</div>
      </div>
    </div>
    ${thumb(scene)}
    ${scene.hook ? `<div class="hook">${esc(scene.hook)}</div>` : ""}
    ${scene.cast.length ? `<div class="cast">${scene.cast.map((name) => `<span class="chip">${esc(name)}</span>`).join("")}</div>` : ""}
    ${kind === "frames" ? `<div class="detail"><b>Frame:</b> ${esc(scene.frame_file || `frames/frame_${String(scene.scene_id).padStart(3, "0")}.png`)}</div>` : `<div class="detail"><b>Clip:</b> ${esc(scene.clip_file || `raw_clips/scene_${String(scene.scene_id).padStart(3, "0")}.mp4`)} · <b>Plataforma:</b> ${esc(platformLabel(platform))}</div>`}
    <pre class="prompt">${esc(prompt)}</pre>
    <div class="actions">
      <button class="btn primary" data-action="copy" data-kind="${kind}" data-id="${scene.scene_id}">Copiar prompt</button>
      ${markButton}
    </div>
  </article>`;
}

function scriptCard(scene) {
  const done = clipDone(scene);
  const dialogue = scene.dialogue.map((line) => `<div class="line"><b>${esc(line.speaker)}</b>${line.delivery ? ` <em>(${esc(line.delivery)})</em>` : ""}: ${esc(line.line)}</div>`).join("");
  const cuts = scene.cuts.map((cut) => `<div><b>${cut.at.toFixed(1)} s</b> · ${esc(cut.framing)}: ${esc(cut.action)}</div>`).join("");
  return `<article class="card ${done ? "is-done" : ""}">
    <div class="card-top">
      <div class="scene-id">#${scene.scene_id}</div>
      <div style="flex:1">
        <div class="card-title">${esc(scene.location || "Sin locación")}</div>
        <div class="meta">${metaBadges(scene)} ${stateBadges("script", scene)}</div>
      </div>
    </div>
    ${scene.hook ? `<div class="hook">${esc(scene.hook)}</div>` : ""}
    ${scene.cast.length ? `<div class="cast">${scene.cast.map((name) => `<span class="chip">${esc(name)}</span>`).join("")}</div>` : ""}
    <div class="detail"><b>Momento:</b> ${esc(scene.time_of_day || "—")} · <b>Duración:</b> ${scene.duration_s.toFixed(1)} s</div>
    ${dialogue ? `<div class="dialogue">${dialogue}</div>` : `<div class="detail">Sin diálogo (ambiencia diegética).</div>`}
    ${cuts ? `<div class="cuts">${cuts}</div>` : ""}
    <div class="detail"><b>SFX / ambiencia:</b> ${esc(scene.sfx || "—")}</div>
    <div class="detail"><b>Continuidad:</b> ${esc(scene.continuity || "—")}</div>
    <div class="detail"><b>Cámara:</b> ${esc(scene.camera || "—")}</div>
    <div class="actions">
      <button class="btn primary" data-action="copy-dialogue" data-kind="script" data-id="${scene.scene_id}">Copiar diálogo</button>
      <button class="btn" data-action="copy-json" data-kind="script" data-id="${scene.scene_id}">Copiar escena JSON</button>
    </div>
  </article>`;
}

function referenceCard(ref) {
  const done = refDone(ref);
  const prompt = ref.prompt || `Adjunta la imagen existente de ${ref.name} a la conversación de ChatGPT. No hace falta generarla.`;
  return `<article class="card ${done ? "is-done" : ""}">
    <div class="card-top">
      <div class="scene-id">REF</div>
      <div style="flex:1">
        <div class="card-title">${esc(ref.name)}</div>
        <div class="meta">
          <span class="badge">${esc(ref.filename || "reference")}</span>
          ${ref.exists ? `<span class="badge file">✓ Archivo en disco</span>` : ""}
          ${ref.external ? `<span class="badge hook">Imagen externa</span>` : ""}
          ${isCopied("references", ref) ? `<span class="badge copied">Copiado</span>` : ""}
          ${done && !ref.exists ? `<span class="badge ok">Hecho</span>` : ""}
        </div>
      </div>
    </div>
    ${ref.file ? `<img class="thumb" loading="lazy" src="${esc(ref.file)}" alt="${esc(ref.name)}">` : ""}
    <pre class="prompt">${esc(prompt)}</pre>
    <div class="actions">
      <button class="btn primary" data-action="copy" data-kind="references" data-id="${esc(ref.id)}">Copiar prompt</button>
      ${ref.exists ? `<span class="btn green small" style="text-align:center;cursor:default">✓ En disco</span>` : `<button class="btn ${done ? "green" : ""}" data-action="mark" data-kind="references" data-id="${esc(ref.id)}">${done ? "✓ Hecho" : "Marcar hecho"}</button>`}
    </div>
  </article>`;
}

function masterItems() {
  return (state.master_prompts && state.master_prompts.items) || [];
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
  return `<article class="card">
    <div class="card-top">
      <div class="scene-id">${String(batch.batch_id || 0).padStart(2, "0")}</div>
      <div style="flex:1">
        <div class="card-title">Bloque ${batch.batch_id} · Minuto ${batch.minute}</div>
        <div class="meta">
          <span class="badge">Escenas ${first}–${last}</span>
          <span class="badge">${esc(batch.start_timecode)}–${esc(batch.end_timecode)}</span>
          <span class="badge">${esc(batch.aspect_ratio || "16:9")}</span>
        </div>
      </div>
    </div>
    <pre class="prompt huge">${esc(batch.prompt)}</pre>
    <div class="actions">
      <button class="btn primary" data-action="copy-muse-batch" data-id="${esc(batch.batch_id)}">Copiar lote</button>
      <button class="btn" data-action="download-muse-batch" data-id="${esc(batch.batch_id)}">Descargar .txt</button>
    </div>
  </article>`;
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
  const missing = prompt.unfilled && prompt.unfilled.length
    ? `<span class="badge hook">Sin rellenar: ${esc(prompt.unfilled.join(", "))}</span>`
    : `<span class="badge ok">Completo</span>`;
  return `<article class="card">
    <div class="card-top">
      <div class="scene-id">${esc(String(prompt.code || "").replace("PROMPT ", ""))}</div>
      <div style="flex:1">
        <div class="card-title">${esc(prompt.title)}</div>
        <div class="meta">
          <span class="badge">${esc(prompt.code)}</span>
          <span class="badge">${prompt.chars.toLocaleString()} chars</span>
          <span class="badge">${prompt.words.toLocaleString()} palabras</span>
          ${missing}
        </div>
      </div>
    </div>
    <div class="detail">${esc(prompt.purpose || "")}</div>
    <pre class="prompt huge">${esc(prompt.text)}</pre>
    <div class="actions">
      <button class="btn primary" data-action="copy-master" data-id="${esc(prompt.key)}">Copiar prompt</button>
      <button class="btn" data-action="download-master" data-id="${esc(prompt.key)}">Descargar .txt</button>
    </div>
  </article>`;
}

function renderContent() {
  const holder = $("#content");
  if (activeTab === "prompts") {
    const items = masterItems().filter(matchesMaster);
    if (!items.length) {
      holder.innerHTML = `<div class="empty">No hay prompts maestros que coincidan con el filtro.</div>`;
      return;
    }
    const values = (state.master_prompts && state.master_prompts.values) || {};
    const batches = museBatches();
    const head = `<div class="master-head">
      <div>
        <h2>Prompts maestros 000–003</h2>
        <p>Rellenados con los valores del proyecto: <b>${esc(values.duration_minutes || "?")} min</b> · <b>${esc(values.total_scenes || "?")} escenas</b> · <b>${esc(values.total_grid_images || "?")} grids</b> · <b>${esc(values.aspect_ratio || "16:9")}</b>. Acceso rápido a cada prompt y a los lotes de Muse AI.</p>
      </div>
      <div class="master-actions">
        <button class="btn primary" data-action="copy-master-all">Copiar los 4</button>
        <button class="btn" data-action="download-master-all">Descargar JSON</button>
        ${storyboardGrids().count ? `<button class="btn green" data-action="copy-storyboard-grids">Copiar cola 11 imágenes (Cast + 10 Storyboards)</button>` : ""}
        ${storyboardGrids().count ? `<button class="btn" data-action="download-storyboard-grids">Descargar cola .txt</button>` : ""}
        ${batches.length ? `<button class="btn green" data-action="copy-muse-batches">Copiar lotes Muse AI</button>` : ""}
        ${batches.length ? `<button class="btn" data-action="download-muse-batches">Descargar lotes .txt</button>` : ""}
      </div>
    </div>
    <div class="quick-access">${quickPromptButtons()}</div>`;
    const batchSection = batches.length
      ? `<div class="master-head">
          <div>
            <h2>Lotes Muse AI — 1 minuto / 6 escenas</h2>
            <p>Cada bloque incluye los cortes [00s–03s], [03s–07s], [07s–10s], SFX, diálogo en inglés y el comando final para Muse AI.</p>
          </div>
        </div>
        <div class="grid">${batches.map(museBatchCard).join("")}</div>
        <div class="master-head" style="margin-top:22px">
          <div><h2>Prompts individuales</h2></div>
        </div>`
      : "";
    holder.innerHTML = `${head}${batchSection}<div class="grid">${items.map(masterPromptCard).join("")}</div>`;
    return;
  }
  if (activeTab === "references") {
    const refs = state.references.filter(matchesRef);
    holder.innerHTML = refs.length ? `<div class="grid">${refs.map(referenceCard).join("")}</div>` : `<div class="empty">No hay referencias que coincidan con el filtro.</div>`;
    return;
  }
  const kind = activeTab === "frames" ? "frames" : "clips";
  const scenes = state.scenes.filter((scene) => matchesScene(scene, activeTab === "script" ? "clips" : kind));
  if (!scenes.length) {
    holder.innerHTML = `<div class="empty">No hay escenas que coincidan con el filtro.</div>`;
    return;
  }
  const cards = activeTab === "script" ? scenes.map(scriptCard) : scenes.map((scene) => sceneCard(scene, kind));
  holder.innerHTML = `<div class="grid">${cards.join("")}</div>`;
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
  if (action === "copy-master" || action === "download-master") {
    const prompt = masterItems().find((item) => item.key === id);
    if (!prompt) return;
    if (action === "copy-master") {
      await copyText(prompt.text, `${prompt.code} copiado completo`);
    } else {
      downloadText(`${prompt.signature || prompt.key}.txt`, prompt.text);
      toast(`${prompt.code} descargado`);
    }
    return;
  }
  if (action === "copy-master-all") {
    const text = masterItems().map((item) => `${item.code} — ${item.title}\n\n${item.text}`).join("\n\n\n");
    await copyText(text, "Los 4 prompts maestros copiados");
    return;
  }
  if (action === "download-master-all") {
    downloadText(`master_prompts_${state.slug || "episode"}.json`, JSON.stringify(state.master_prompts, null, 2), "application/json");
    toast("Manifiesto de prompts descargado");
    return;
  }
  if (action === "copy-storyboard-grids") {
    await copyText(storyboardGridsText(), `Cola de ${storyboardGrids().count} imágenes copiada (1 cast + 10 storyboards)`);
    return;
  }
  if (action === "download-storyboard-grids") {
    downloadText(`chatgpt_storyboard_grids_queue_${state.slug || "episode"}.txt`, storyboardGridsText());
    toast("Cola de 11 imágenes descargada");
    return;
  }
  if (action === "copy-muse-batch") {
    const batch = museBatches().find((item) => String(item.batch_id) === String(id));
    if (!batch) return;
    await copyText(batch.prompt, `Lote ${batch.batch_id} copiado (minuto ${batch.minute})`);
    return;
  }
  if (action === "download-muse-batch") {
    const batch = museBatches().find((item) => String(item.batch_id) === String(id));
    if (!batch) return;
    downloadText(`muse_ai_batch_${String(batch.batch_id).padStart(2, "0")}.txt`, batch.prompt);
    toast(`Lote ${batch.batch_id} descargado`);
    return;
  }
  if (action === "copy-muse-batches") {
    const text = museBatches().map((batch) => `BLOQUE ${batch.batch_id} — MINUTO ${batch.minute}\n\n${batch.prompt}`).join("\n\n\n");
    await copyText(text, `${museBatches().length} lotes de Muse AI copiados`);
    return;
  }
  if (action === "download-muse-batches") {
    const text = museBatches().map((batch) => `BLOQUE ${batch.batch_id} — MINUTO ${batch.minute}\n\n${batch.prompt}`).join("\n\n\n");
    downloadText(`muse_ai_batches_${state.slug || "episode"}.txt`, text);
    toast("Lotes de Muse AI descargados");
    return;
  }
  if (action === "copy") {
    if (kind === "references") {
      const ref = findRef(id);
      if (!ref) return;
      refTrack(id).copied = new Date().toISOString();
      touchTracking();
      await copyText(ref.prompt || ref.name, "Prompt de referencia copiado");
    } else {
      const scene = findScene(id);
      if (!scene) return;
      const field = kind === "frames" ? "image_copied" : "video_copied";
      sceneTrack(id)[field] = new Date().toISOString();
      touchTracking();
      await copyText(kind === "frames" ? scene.image_prompt : sceneVideoPrompt(scene), kind === "frames" ? "Prompt de imagen copiado" : `Prompt de ${platformLabel(platform)} copiado`);
    }
    renderContent();
    return;
  }
  if (action === "copy-dialogue") {
    const scene = findScene(id);
    if (!scene) return;
    const text = scene.dialogue.map((line) => `${line.speaker}${line.delivery ? ` (${line.delivery})` : ""}: "${line.line}"`).join("\n");
    await copyText(text || scene.video_prompt, "Diálogo copiado");
    return;
  }
  if (action === "copy-json") {
    const scene = findScene(id);
    if (!scene) return;
    await copyText(scene.scene_json, "Escena JSON copiada");
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
    const prompt = masterItems()[0];
    if (!prompt) return toast("No hay prompts maestros exportados");
    copyText(prompt.text, `${prompt.code} copiado`);
    return;
  }
  if (activeTab === "references") {
    const ref = state.references.find((item) => !refDone(item));
    if (!ref) return toast("No quedan referencias pendientes");
    refTrack(ref.id).copied = new Date().toISOString();
    touchTracking();
    copyText(ref.prompt || ref.name, `Referencia copiada: ${ref.name}`);
    renderContent();
    return;
  }
  const kind = activeTab === "frames" ? "frames" : "clips";
  const field = kind === "frames" ? "image_copied" : "video_copied";
  const scene = state.scenes.find((item) => !isDone(kind, item));
  if (!scene) return toast("No quedan escenas pendientes");
  sceneTrack(scene.scene_id)[field] = new Date().toISOString();
  touchTracking();
  copyText(kind === "frames" ? scene.image_prompt : sceneVideoPrompt(scene), `Escena ${scene.scene_id} copiada (${kind === "frames" ? "imagen" : platformLabel(platform)})`);
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
    toast("Estado recargado desde disco");
  } catch (e) {
    toast("No se pudo recargar el estado", true);
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
      toast("Archivo de tracking inválido", true);
    }
  };
  reader.readAsText(file);
}

function resetTracking() {
  if (!confirm("¿Reiniciar el tracking manual? Los archivos de frames y clips no se borran.")) return;
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

    def _safe_project_file(self, url_path: str) -> Optional[Path]:
        root = self.project_paths["root"].resolve()
        candidate = (root / unquote(url_path).lstrip("/")).resolve()
        if candidate == root or root in candidate.parents:
            if candidate.is_file():
                return candidate
        return None

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        route = parsed.path
        if route in ("/", "/index.html", "/dashboard.html"):
            target = self.dashboard_path or (self.project_paths["root"] / DASHBOARD_FILENAME)
            if not target.exists():
                self.send_error(404, "dashboard.html no existe; ejecuta el generador primero")
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
        raise nf.NFError(f"No se pudo abrir el puerto {port}: {exc}. Prueba --port otro_numero.") from exc
    url = f"http://127.0.0.1:{port}/"
    nf.ok(f"Dashboard servido en {url}")
    nf.info(f"Proyecto: {paths['root']}")
    nf.info(f"Tracking: {tracking_path(paths)}")
    nf.info("Ctrl+C para detener.")
    if open_browser:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        nf.info("Servidor detenido.")
    finally:
        httpd.server_close()


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Dashboard local de producción por episodio.")
    parser.add_argument("project", help="Slug del episodio o ruta a su carpeta.")
    parser.add_argument("--out", type=str, default="", help="Ruta del HTML generado (por defecto <proyecto>/dashboard.html).")
    parser.add_argument("--serve", action="store_true", help="Sirve el dashboard en 127.0.0.1 con tracking persistente.")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help=f"Puerto del servidor local (por defecto {DEFAULT_PORT}).")
    parser.add_argument("--open", action="store_true", help="Abre el dashboard en el navegador.")
    parser.add_argument("--quiet", action="store_true", help="No imprime el resumen final.")
    args = parser.parse_args(argv)

    paths = nf.resolve_project(args.project)
    state = build_state(paths["root"], paths)
    tracking = load_tracking(paths)
    out = Path(args.out) if args.out else (paths["root"] / DASHBOARD_FILENAME)
    dashboard = write_dashboard(paths, state, tracking, out, mode="server" if args.serve else "static")

    if not args.quiet:
        nf.ok(f"Dashboard generado: {dashboard}")
        nf.info(f"Escenas: {state['totals']['scenes']} · frames en disco: {state['totals']['frames_disk']} · clips en disco: {state['totals']['clips_disk']}")
        nf.info(f"Referencias: {state['totals']['references']} · teasers: {state['totals']['teasers']}")
        if not args.serve:
            nf.info("Modo archivo: el tracking se guarda en el navegador. Usa --serve para guardarlo en disco.")

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

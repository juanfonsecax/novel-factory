#!/usr/bin/env python3
"""Shared core for novel_factory.

Design rules:
- Python standard library only + ffmpeg/ffprobe. No paid APIs, no network.
- No script in this module imports or modifies USA WHITE /
  AUTOMATED AI NEWS code: integration happens through files (queue/pending).
- Everything is auditable: explicit paths, readable JSON, errors with context.

This file is imported by the generators (01-03), the runner (automation/) and
post-production (04-05) through sys.path.insert(0, <novel_factory>).
"""
from __future__ import annotations

import copy
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

# --- UTF-8 console on Windows (same pattern as the rest of the workspace) ---
for _flujo in (sys.stdout, sys.stderr):
    try:
        _flujo.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# --- Rutas y constantes globales ---
NF_ROOT = Path(__file__).resolve().parent
CONFIG_DIR = NF_ROOT / "config"
PROJECTS_DIR = NF_ROOT / "projects"
MUSIC_DIR = NF_ROOT / "music"
ASSETS_DIR = NF_ROOT / "assets"
SHOWRUNNER_FILE = CONFIG_DIR / "showrunner_rules.json"
STYLE_FILE = CONFIG_DIR / "voice_and_style_locks.json"

SCENES_PER_BLOCK = 6
SCENE_SECONDS = 10.0
LEGACY_TARGET_MINUTES = 10
DEFAULT_TARGET_MINUTES = 22
FORMAT_PROFILE_TARGET_MINUTES = {"youtube_10": 10, "short_1": 1}
SCENE_COUNT = LEGACY_TARGET_MINUTES * SCENES_PER_BLOCK  # legacy 10-min default (60 scenes)
TOTAL_SECONDS = SCENE_COUNT * SCENE_SECONDS  # legacy 600 s = 10 min
FPS = 30
MASTER_W, MASTER_H = 1920, 1080          # 16:9
TEASER_W, TEASER_H = 1080, 1920          # 9:16
DEFAULT_SHOT_ROTATION = [
    "wide establishing shot",
    "medium shot",
    "tight close-up",
    "over-the-shoulder shot",
    "low-angle hero shot",
]
FRAME_EXTS = (".png", ".jpg", ".jpeg", ".webp")

# Subcommands that live in generators/ scripts and are dispatched from nf_core.
SUBCOMMANDS: Dict[str, str] = {
    "export-master-prompts": "generators/00_export_master_workflow_prompts.py",
    "prompts": "generators/04_export_master_prompts.py",
    "muse-pack": "generators/05_export_muse_method_pack.py",
}

# --- Content contract (P0): speech pace and per-scene budget ---
SPEECH_WORDS_PER_SECOND = 2.5    # US English conversational pace (~150 wpm)
MAX_SCENE_WORDS = 15             # global cap per 10 s scene
MAX_LINE_WORDS = 15              # cap per line
MIN_SCENE_WORDS = 6              # minimum so the scene is not empty
MAX_SCENE_SPEECH_SECONDS = 8.5   # the voice must finish before 8.5 s
CUT_MIN_GAP = 3.0
CUT_MAX_GAP = 4.0
DURATION_TOLERANCE_SEC = 0.05
SHOT_CUT_TIMES = (0.0, 3.0, 7.0)
SHOT_RANGES = ("00s-03s", "03s-07s", "07s-10s")
DIALOGUE_END_DEADLINE_SEC = 8.5

# --- Contract v2: speaker per shot, visible object and diegetic text ---
MAX_SCENE_CAST = 3               # distinct characters per scene/prompt
MAX_DIALOGUE_LINES_PER_SCENE = 2 # 2 lines per 10 s clip
MAX_CUTS_PER_SCENE = 4
OBJECT_FOCUS_MIN_SECONDS = 2.0   # reveal insert, minimum on camera
SPEECH_PAD_SECONDS = 0.45        # breathing room before/after a line
SPEECH_GAP_SECONDS = 0.35        # pause between two lines in the same shot
SCENE_TEXT_SAFE_CLAUSE = (
    "No subtitles, no captions, no overlay text, no watermark, no signage, no UI text."
)
SCENE_TEXT_HIDDEN_CLAUSE = (
    "Any paper, document, letter or sign in frame must show no legible words; "
    "do not invent readable text."
)

# --- Contract v3: ReelShort/DramaBox (proven source, bridges, rotation, pacing) ---
DEFAULT_CLIFFHANGER_ROTATION = ("identity", "emotion", "revelation")
PRODUCTION_ATTACH_NOTE = (
    "ATTACH FOR EVERY SCENE: that scene's storyboard panel + references ONLY for the "
    "characters who appear in THAT scene + that scene's prompt. "
    "Never generate a scene without its attached characters."
)
FORBIDDEN_TRANSLATION_RE = re.compile(
    r"\b(?:you\s+dare|ceo\s+[A-Z][a-z]+|president\s+[A-Z][a-z]+)\b",
    re.IGNORECASE,
)
NON_CONFRONTATIONAL_BEAT_PATTERNS = re.compile(
    r"\b(?:decision|solo|solitary|discovery|plan|planning|"
    r"tender|vulnerable|intimacy|romance|romantic|wound|"
    r"revelation|discovery|investigat|reflec|relief|curiosity|hope|"
    r"world_and_wound|setup[-_]stakes|setup)\b",
    re.IGNORECASE,
)
CONFRONTATION_BEAT_PATTERNS = re.compile(
    r"\b(?:confront|confrontation|face[-_]?slap|argument|fight|clash|crisis|brawl|standoff)\b",
    re.IGNORECASE,
)


def is_non_confrontational_scene(scene: Dict[str, Any]) -> bool:
    if scene.get("non_confrontational") is True or scene.get("is_confrontation") is False:
        return True
    beat = str(scene.get("beat") or "")
    beat_fn = str(scene.get("beat_function") or "")
    emotion = str(scene.get("emotion") or "")
    for text in (beat, beat_fn, emotion):
        if text and NON_CONFRONTATIONAL_BEAT_PATTERNS.search(text):
            return True
    return False


def is_confrontation_scene(scene: Dict[str, Any]) -> bool:
    if scene.get("is_confrontation") is True:
        return True
    beat = str(scene.get("beat") or "")
    beat_fn = str(scene.get("beat_function") or "")
    for text in (beat, beat_fn):
        if text and CONFRONTATION_BEAT_PATTERNS.search(text):
            return True
    return False


def build_scene_attachments(scene: Dict[str, Any], master: Dict[str, Any]) -> List[str]:
    sid = int(scene.get("scene_id") or 0)
    panel_ref = f"panel_{sid:03d}"
    attachments = [panel_ref]
    present = [
        str(x).strip().lower()
        for x in (scene.get("characters_present") or scene.get("characters") or [])
        if str(x).strip()
    ]
    cast_index = canonical_cast(master)
    for cid in present:
        char_info = cast_index.get(cid) or {}
        char_id = str(char_info.get("id") or cid).strip().lower().replace(" ", "_")
        ref_name = f"ref_{char_id}"
        if ref_name not in attachments:
            attachments.append(ref_name)
    return attachments


class NFError(RuntimeError):
    """Controlled module error (console-friendly message)."""


# --- Consistent console output ---
def log(msg: str = "") -> None:
    print(msg)


def info(msg: str) -> None:
    print(f"  [i] {msg}")


def ok(msg: str) -> None:
    print(f"  [OK] {msg}")


def warn(msg: str) -> None:
    print(f"  [!] {msg}")


def err(msg: str) -> None:
    print(f"  [X] {msg}")


# --- Text / file utilities ---
def slugify(text: str) -> str:
    """Turn a title into a folder-safe slug.

    ASCII first (historical behavior). If the title produces no ASCII
    (e.g. Chinese), keep alphanumeric Unicode characters and add a
    short hash to avoid collisions between different CJK titles.
    """
    import hashlib

    t = unicodedata.normalize("NFKD", text or "")
    ascii_t = "".join(ch for ch in t if not unicodedata.combining(ch)).lower().strip()
    ascii_slug = re.sub(r"[^a-z0-9]+", "_", ascii_t)
    ascii_slug = re.sub(r"_+", "_", ascii_slug).strip("_")
    if ascii_slug:
        return ascii_slug
    uni = unicodedata.normalize("NFKC", text or "").lower().strip()
    uni = re.sub(r"[^\w]+", "_", uni, flags=re.UNICODE)
    uni = re.sub(r"_+", "_", uni, flags=re.UNICODE).strip("_")
    if uni:
        digest = hashlib.sha1((text or "").encode("utf-8")).hexdigest()[:6]
        return f"{uni}_{digest}"
    return "episode"


def now_iso() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def read_json(path: Path, default: Any = None) -> Any:
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        return default
    except Exception as exc:
        raise NFError(f"Could not read JSON {path}: {exc}") from exc


def write_json(path: Path, data: Any) -> Path:
    """Atomic write (tmp + replace) so no JSON is left half-written."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)
    return path


def write_text(path: Path, text: str) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    tmp.replace(path)
    return path


def load_showrunner() -> Dict[str, Any]:
    data = read_json(SHOWRUNNER_FILE)
    if not isinstance(data, dict):
        raise NFError(f"Missing or corrupt: {SHOWRUNNER_FILE}")
    return data


def load_style_locks() -> Dict[str, Any]:
    data = read_json(STYLE_FILE)
    if not isinstance(data, dict):
        raise NFError(f"Missing or corrupt: {STYLE_FILE}")
    return data


def scenes_per_block(rules: Optional[Dict[str, Any]] = None) -> int:
    rules = rules if isinstance(rules, dict) else load_showrunner()
    engine = rules.get("narrative_continuity_engine") or {}
    profiles = rules.get("format_profiles") or {}
    profile = profiles.get("youtube_10") if isinstance(profiles, dict) else {}
    raw = engine.get("scenes_per_block") or (profile or {}).get("scenes_per_block") or SCENES_PER_BLOCK
    try:
        value = int(raw)
    except (TypeError, ValueError):
        value = SCENES_PER_BLOCK
    return value if value > 0 else SCENES_PER_BLOCK


def scene_seconds(rules: Optional[Dict[str, Any]] = None) -> float:
    rules = rules if isinstance(rules, dict) else load_showrunner()
    fmt = rules.get("format") or {}
    try:
        return float(fmt.get("scene_seconds") or SCENE_SECONDS)
    except (TypeError, ValueError):
        return SCENE_SECONDS


def resolve_target_minutes(
    target_minutes: Any = None,
    format_profile: str = "",
    default: Any = None,
) -> int:
    """Project duration in minutes. Legacy profiles are shortcuts."""
    profile = str(format_profile or "").strip().lower()
    if profile:
        if profile not in FORMAT_PROFILE_TARGET_MINUTES:
            raise NFError(
                f"Perfil de formato desconocido: {format_profile!r}. "
                f"Disponibles: {', '.join(sorted(FORMAT_PROFILE_TARGET_MINUTES))}"
            )
        if target_minutes in (None, ""):
            return int(FORMAT_PROFILE_TARGET_MINUTES[profile])
    if target_minutes in (None, ""):
        base = DEFAULT_TARGET_MINUTES if default is None else default
        try:
            return int(base)
        except (TypeError, ValueError) as exc:
            raise NFError(f"Invalid default duration: {base!r}") from exc
    try:
        value = int(target_minutes)
    except (TypeError, ValueError) as exc:
        raise NFError(f"Invalid target_minutes: {target_minutes!r}") from exc
    if value < 1:
        raise NFError(f"target_minutes must be >= 1 (received {value}).")
    return value


def scene_count_for_target(target_minutes: Any, rules: Optional[Dict[str, Any]] = None) -> int:
    return resolve_target_minutes(target_minutes) * scenes_per_block(rules)


def target_minutes_for_scene_count(scene_count: Any, rules: Optional[Dict[str, Any]] = None) -> int:
    try:
        count = int(scene_count)
    except (TypeError, ValueError):
        return 0
    if count < 1:
        return 0
    per_block = scenes_per_block(rules)
    if count % per_block == 0:
        return count // per_block
    return max(1, int(round(count / float(per_block))))


def master_target_minutes(master: Dict[str, Any]) -> int:
    ep = master.get("episode") if isinstance(master.get("episode"), dict) else {}
    for key in ("target_minutes", "total_blocks", "minute_blocks", "blocks"):
        if ep.get(key) not in (None, ""):
            try:
                return resolve_target_minutes(ep.get(key))
            except NFError:
                continue
    if ep.get("total_scenes") not in (None, ""):
        derived = target_minutes_for_scene_count(ep.get("total_scenes"))
        if derived:
            return derived
    scenes = [s for s in (master.get("scenes") or []) if isinstance(s, dict)]
    return target_minutes_for_scene_count(len(scenes)) or LEGACY_TARGET_MINUTES


def master_scene_count(master: Dict[str, Any]) -> int:
    ep = master.get("episode") if isinstance(master.get("episode"), dict) else {}
    for key in ("target_minutes", "total_blocks", "minute_blocks", "blocks"):
        if ep.get(key) not in (None, ""):
            try:
                return scene_count_for_target(ep.get(key))
            except NFError:
                continue
    if ep.get("total_scenes") not in (None, ""):
        try:
            value = int(ep.get("total_scenes"))
        except (TypeError, ValueError):
            value = 0
        if value > 0:
            return value
    scenes = [s for s in (master.get("scenes") or []) if isinstance(s, dict)]
    return len(scenes) or SCENE_COUNT


def required_beats_for_scene_count(scene_count: Any, rules: Optional[Dict[str, Any]] = None) -> Dict[int, str]:
    """Milestones by percentage of the total; with 60 scenes it produces 1/2/10..50/60."""
    rules = rules if isinstance(rules, dict) else load_showrunner()
    template = rules.get("required_beats") or {}
    try:
        count = max(1, int(scene_count))
    except (TypeError, ValueError):
        count = SCENE_COUNT
    if isinstance(template, dict) and any(str(key).isdigit() for key in template):
        return {int(k): str(v) for k, v in template.items() if str(k).isdigit()}
    first = str(template.get("first_scene") or "cold_open_hook")
    second = str(template.get("second_scene") or "world_and_wound")
    cliff = str(template.get("act_cliffhanger") or "act_cliffhanger")
    final = str(template.get("final_scene") or "payoff_next_hook")
    fractions = template.get("act_cliffhanger_fractions") or [1 / 6, 2 / 6, 3 / 6, 4 / 6, 5 / 6]
    beats: Dict[int, str] = {1: first}
    if count >= 2:
        beats[2] = second
    for fraction in fractions:
        try:
            sid = int(round(count * float(fraction)))
        except (TypeError, ValueError):
            continue
        beats.setdefault(min(max(1, sid), count), cliff)
    beats[count] = final
    return beats


def hook_scene_ids(scene_count: Any, rules: Optional[Dict[str, Any]] = None) -> List[int]:
    beats = required_beats_for_scene_count(scene_count, rules)
    return sorted(sid for sid, beat in beats.items() if beat != "world_and_wound")


def act_scene_range(act_number: int, scene_count: int, act_count: int = 6) -> Tuple[int, int]:
    total = max(1, int(scene_count))
    acts = max(1, int(act_count))
    number = min(max(1, int(act_number)), acts)
    start = ((number - 1) * total) // acts + 1
    end = (number * total) // acts
    return start, max(start, end)


def human_duration(seconds: float) -> str:
    seconds = max(0, int(round(seconds)))
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def fmt_srt(seconds: float) -> str:
    ms = int(round(max(0.0, seconds) * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1_000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def parse_ranges(spec: str, max_scene: Optional[int] = None) -> List[int]:
    """'1-5,8,10-12' -> [1..5, 8, 10..12] (1-based, no duplicates, sorted)."""
    out: set[int] = set()
    for part in str(spec or "").replace(" ", "").split(","):
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            if not (a.isdigit() and b.isdigit()):
                raise NFError(f"Invalid range: '{part}'")
            lo, hi = int(a), int(b)
            if lo > hi:
                lo, hi = hi, lo
            out.update(range(lo, hi + 1))
        elif part.isdigit():
            out.add(int(part))
        else:
            raise NFError(f"Invalid range: '{part}'")
    if max_scene is None:
        return sorted(i for i in out if i >= 1)
    return sorted(i for i in out if 1 <= i <= int(max_scene))


# --- Projects / episodes ---
def project_dir(slug: str) -> Path:
    return PROJECTS_DIR / slugify(slug)


def project_paths(slug_or_dir: str | Path) -> Dict[str, Path]:
    p = Path(slug_or_dir)
    if p.is_absolute() or (p.exists() and p.is_dir()):
        root = p
    else:
        root = project_dir(str(slug_or_dir))
    return {
        "root": root,
        "meta": root / "project.json",
        "master": root / "master_episode.json",
        "frames": root / "frames",
        "references": root / "references",
        "raw_clips": root / "raw_clips",
        "output": root / "output",
        "work": root / "output" / ".work",
        "chatgpt_txt": root / "chatgpt_image_prompts_queue.txt",
        "chatgpt_json": root / "chatgpt_image_prompts_queue.json",
        "omni_csv": root / "omni_video_prompts_queue.csv",
        "omni_json": root / "omni_video_prompts_queue.json",
        "omni_txt": root / "omni_video_prompts_queue.txt",
        "chatgpt_refs": root / "chatgpt_reference_sheets.txt",
        "chatgpt_thumbs": root / "chatgpt_thumbnail_prompts.txt",
        "state": root / "queue_state.json",
        "master_prompts_md": root / "MASTER_PROMPTS.md",
        "master_prompts_txt": root / "MASTER_PROMPTS.txt",
        "master_prompts_json": root / "master_prompts.json",
        "prompts_dir": root / "prompts",
        "master_workflow_prompts_md": root / "MASTER_WORKFLOW_PROMPTS_READY.md",
        "chatgpt_prompt_001": root / "chatgpt_prompt_001_storyboards.txt",
        "chatgpt_prompt_002": root / "chatgpt_prompt_002_characters.txt",
        "chatgpt_storyboard_grids_txt": root / "chatgpt_storyboard_grids_queue.txt",
        "chatgpt_storyboard_grids_json": root / "chatgpt_storyboard_grids_queue.json",
        "muse_ai_minute_batches_txt": root / "muse_ai_minute_batches_queue.txt",
        "muse_ai_minute_batches_json": root / "muse_ai_minute_batches_queue.json",
        "muse_ai_batches_txt": root / "muse_ai_batches_queue.txt",
        "muse_ai_batches_json": root / "muse_ai_batches_queue.json",
        "muse_csv": root / "muse_ai_video_prompts_queue.csv",
        "muse_json": root / "muse_ai_video_prompts_queue.json",
        "muse_txt": root / "muse_ai_video_prompts_queue.txt",
        "flow_csv": root / "google_flow_video_prompts_queue.csv",
        "flow_json": root / "google_flow_video_prompts_queue.json",
        "flow_txt": root / "google_flow_video_prompts_queue.txt",
    }


def load_project_meta(paths_or_dir: Dict[str, Path] | str | Path) -> Dict[str, Any]:
    paths = paths_or_dir if isinstance(paths_or_dir, dict) else project_paths(paths_or_dir)
    meta_path = paths.get("meta")
    if not meta_path:
        return {}
    data = read_json(meta_path, default={})
    return data if isinstance(data, dict) else {}


def create_project(
    slug: str,
    target_minutes: Any = None,
    format_profile: str = "",
) -> Dict[str, Path]:
    """Create the project and declare its duration in project.json."""
    paths = project_paths(project_dir(slug))
    for key in ("root", "frames", "references", "raw_clips", "output", "prompts_dir"):
        paths[key].mkdir(parents=True, exist_ok=True)
    for folder in (paths["frames"], paths["references"], paths["raw_clips"], paths["output"]):
        keep = folder / ".gitkeep"
        if not keep.exists():
            keep.write_text("", encoding="utf-8")
    existing = load_project_meta(paths)
    if target_minutes in (None, "") and not str(format_profile or "").strip() and existing.get("target_minutes") not in (None, ""):
        target = resolve_target_minutes(existing.get("target_minutes"))
    else:
        target = resolve_target_minutes(
            target_minutes, format_profile, default=DEFAULT_TARGET_MINUTES
        )
    rules = load_showrunner()
    meta = {
        "schema_version": 1,
        "slug": slugify(slug),
        "target_minutes": target,
        "total_blocks": target,
        "total_scenes": scene_count_for_target(target, rules),
        "scene_seconds": scene_seconds(rules),
        "scenes_per_block": scenes_per_block(rules),
        "created_at": str(existing.get("created_at") or now_iso()),
        "updated_at": now_iso(),
    }
    write_json(paths["meta"], meta)
    return paths


def resolve_project(slug_or_dir: str | Path, must_exist: bool = True) -> Dict[str, Path]:
    raw = str(slug_or_dir)
    candidate = Path(raw)
    if candidate.exists() and candidate.is_dir() and (
        (candidate / "master_episode.json").exists() or not must_exist
    ):
        paths = project_paths(candidate)
    else:
        paths = project_paths(project_dir(raw))
    if must_exist and not paths["master"].exists():
        raise NFError(
            f"Project '{raw}' does not exist. Expected: {paths['master']}\n"
            "  Create the episode first with generators/01_story_to_master_json.py"
        )
    return paths


def scene_stem(index: int) -> str:
    if int(index) < 1:
        raise NFError(f"scene_id fuera de rango: {index}")
    return f"scene_{int(index):03d}"


def frame_stem(index: int) -> str:
    if int(index) < 1:
        raise NFError(f"scene_id fuera de rango: {index}")
    return f"frame_{int(index):03d}"


def find_frame(frames_dir: Path, index: int) -> Optional[Path]:
    base = frame_stem(index)
    for ext in FRAME_EXTS:
        p = frames_dir / f"{base}{ext}"
        if p.exists():
            return p
    hits = sorted(p for p in frames_dir.glob(f"{base}.*") if p.suffix.lower() in FRAME_EXTS)
    return hits[0] if hits else None


def find_clip(raw_clips_dir: Path, index: int) -> Optional[Path]:
    base = scene_stem(index)
    hits = sorted(p for p in raw_clips_dir.glob(f"{base}.*") if p.suffix.lower() in (".mp4", ".mov", ".m4v", ".webm"))
    return hits[0] if hits else None


# --- FFmpeg / FFprobe ---
def has_ffmpeg() -> bool:
    return bool(shutil.which("ffmpeg") and shutil.which("ffprobe"))


def require_ffmpeg() -> None:
    missing = [b for b in ("ffmpeg", "ffprobe") if not shutil.which(b)]
    if missing:
        raise NFError(
            f"Missing from PATH: {', '.join(missing)}. Install with: winget install Gyan.FFmpeg"
        )


def run_cmd(cmd: Sequence[str], timeout: Optional[int] = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        list(cmd),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )


def run_ffmpeg(cmd: Sequence[str], timeout: Optional[int] = None) -> subprocess.CompletedProcess:
    res = run_cmd(cmd, timeout=timeout)
    if res.returncode != 0:
        tail = (res.stderr or res.stdout or "").strip().splitlines()[-12:]
        raise NFError("ffmpeg failed:\n  " + "\n  ".join(tail))
    return res


def ffprobe_json(path: Path) -> Dict[str, Any]:
    res = run_cmd([
        "ffprobe", "-v", "error", "-print_format", "json",
        "-show_format", "-show_streams", str(path),
    ])
    if res.returncode != 0:
        tail = (res.stderr or "").strip().splitlines()[-6:]
        raise NFError(f"ffprobe failed for {Path(path).name}:\n  " + "\n  ".join(tail))
    try:
        return json.loads(res.stdout or "{}")
    except Exception as exc:
        raise NFError(f"ffprobe returned invalid JSON for {Path(path).name}: {exc}") from exc


def probe_media(path: Path) -> Dict[str, Any]:
    data = ffprobe_json(path)
    fmt = data.get("format") or {}
    streams = data.get("streams") or []
    v = next((s for s in streams if s.get("codec_type") == "video"), None)
    a = next((s for s in streams if s.get("codec_type") == "audio"), None)

    duration = 0.0
    for raw in (fmt.get("duration"), (v or {}).get("duration"), (a or {}).get("duration")):
        try:
            val = float(raw)
            if val > 0:
                duration = val
                break
        except (TypeError, ValueError):
            continue

    fps = 0.0
    if v:
        rate = str(v.get("avg_frame_rate") or v.get("r_frame_rate") or "0/0")
        try:
            num, den = rate.split("/")
            fps = float(num) / float(den) if float(den) else 0.0
        except Exception:
            fps = 0.0

    return {
        "path": str(path),
        "duration": duration,
        "width": int(v.get("width") or 0) if v else 0,
        "height": int(v.get("height") or 0) if v else 0,
        "fps": fps,
        "has_video": bool(v),
        "has_audio": bool(a),
        "audio_codec": (a or {}).get("codec_name", ""),
        "size_bytes": int(fmt.get("size") or 0),
    }


def sha256_file(path: Path) -> str:
    import hashlib

    hasher = hashlib.sha256()
    with Path(path).open("rb") as fh:
        while chunk := fh.read(1 << 20):
            hasher.update(chunk)
    return hasher.hexdigest()


def detect_font() -> Optional[Path]:
    """Bold font for overlays. Prefers module assets/fonts; falls back to Windows."""
    fonts_dir = ASSETS_DIR / "fonts"
    if fonts_dir.exists():
        candidates = sorted(
            p for p in fonts_dir.iterdir()
            if p.suffix.lower() in (".ttf", ".otf") and p.is_file()
        )
        if candidates:
            preferred = [p for p in candidates if "bold" in p.name.lower() or "semibold" in p.name.lower()]
            return (preferred or candidates)[0]
    win = Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts"
    for name in ("arialbd.ttf", "seguisb.ttf", "segoeuib.ttf", "arial.ttf", "impact.ttf"):
        p = win / name
        if p.exists():
            return p
    return None


# --- Acceso al JSON Maestro ---
def load_master(project: str | Path) -> Dict[str, Any]:
    paths = project_paths(project)
    master = read_json(paths["master"])
    if not isinstance(master, dict):
        raise NFError(f"Missing or invalid: {paths['master']}")
    scenes = master.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        raise NFError(f"{paths['master']} no contiene 'scenes'.")
    return master


def episode_meta(master: Dict[str, Any]) -> Dict[str, Any]:
    ep = master.get("episode")
    return ep if isinstance(ep, dict) else {}


def ordered_scenes(master: Dict[str, Any]) -> List[Dict[str, Any]]:
    scenes = [s for s in (master.get("scenes") or []) if isinstance(s, dict)]
    return sorted(scenes, key=lambda s: int(s.get("scene_id") or 0))


def scene_dialogue_lines(scene: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Normalize dialogue to [{speaker,line,delivery,shot,recipient}]."""
    out: List[Dict[str, Any]] = []
    raw = scene.get("dialogue")
    if isinstance(raw, str):
        raw = [raw]
    for item in raw or []:
        if isinstance(item, str):
            if item.strip():
                out.append({"speaker": "", "line": item.strip(), "delivery": "", "shot": 0, "recipient": ""})
        elif isinstance(item, dict):
            line = str(item.get("line") or item.get("text") or "").strip()
            if line:
                try:
                    shot = int(item.get("shot") or 0)
                except (TypeError, ValueError):
                    shot = 0
                out.append({
                    "speaker": str(item.get("speaker") or "").strip(),
                    "line": line,
                    "delivery": str(item.get("delivery") or "").strip(),
                    "shot": shot,
                    "recipient": str(item.get("recipient") or "").strip(),
                })
    return out


def scene_dialogue_text(scene: Dict[str, Any], with_speaker: bool = True) -> str:
    parts = []
    for d in scene_dialogue_lines(scene):
        if with_speaker and d["speaker"]:
            parts.append(f'{d["speaker"].upper()}: "{d["line"]}"')
        else:
            parts.append(d["line"])
    return " ".join(parts).strip()


def scene_words(scene: Dict[str, Any]) -> int:
    return len(re.findall(r"\b[\w'-]+\b", scene_dialogue_text(scene, with_speaker=False)))


def scene_line_words(scene: Dict[str, Any]) -> List[int]:
    """Words per line, in order."""
    return [len(re.findall(r"\b[\w'-]+\b", d["line"])) for d in scene_dialogue_lines(scene)]


def scene_speech_seconds(scene: Dict[str, Any], words_per_second: float = SPEECH_WORDS_PER_SECOND) -> float:
    """Estimated speech seconds for the scene (all lines)."""
    wps = float(words_per_second or SPEECH_WORDS_PER_SECOND)
    return (scene_words(scene) / wps) if wps > 0 else 0.0


# --- Canonical cast / speakers / present continuity ---
def _cast_keys(character: Dict[str, Any]) -> List[str]:
    keys: List[str] = []
    for raw in (character.get("id"), character.get("name"), character.get("archetype")):
        text = str(raw or "").strip().lower()
        if not text:
            continue
        keys.append(text)
        keys.append(re.sub(r"[^a-z0-9]+", " ", text).strip())
        keys.append(re.sub(r"[^a-z0-9]+", "_", text).strip("_"))
        keys.append(text.split()[0] if text.split() else text)
    return [k for k in keys if k]


def canonical_cast(master: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """Character index by id / name / first name / archetype (lowercase)."""
    index: Dict[str, Dict[str, Any]] = {}
    for character in master.get("characters") or []:
        if not isinstance(character, dict):
            continue
        for key in _cast_keys(character):
            index.setdefault(key, character)
    return index


def resolve_speaker(speaker: str, master: Dict[str, Any]) -> Optional[str]:
    """Return the canonical id/name for a speaker, or None if not in the cast."""
    text = str(speaker or "").strip().lower()
    if not text:
        return None
    if text in ("narrator", "narrador", "n/a", "none", "unknown"):
        return None
    index = canonical_cast(master)
    for key in (text, re.sub(r"[^a-z0-9]+", " ", text).strip(),
                re.sub(r"[^a-z0-9]+", "_", text).strip("_"), text.split()[0] if text.split() else text):
        character = index.get(key)
        if character:
            return str(character.get("id") or character.get("name") or speaker)
    return None


def character_by_key(master: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """Character index by id AND by name (lowercase)."""
    index: Dict[str, Dict[str, Any]] = {}
    for character in master.get("characters") or []:
        if not isinstance(character, dict):
            continue
        for key in (character.get("id"), character.get("name")):
            text = str(key or "").strip().lower()
            if text:
                index.setdefault(text, character)
    return index


def reference_stem(character: Dict[str, Any]) -> str:
    """Canonical reference-sheet filename: reference_<id>.png."""
    cid = slugify(str(character.get("id") or character.get("name") or "character")) or "character"
    return f"reference_{cid}.png"


def _character_id(character: Dict[str, Any]) -> str:
    return str(character.get("id") or character.get("name") or "").strip()


def character_position_map(master: Dict[str, Any]) -> Dict[str, int]:
    """1-based position of each character in the cast-sheet order."""
    positions: Dict[str, int] = {}
    for idx, character in enumerate(master.get("characters") or [], start=1):
        if isinstance(character, dict):
            cid = _character_id(character)
            if cid:
                positions[cid] = idx
    return positions


def _character_descriptor(character: Dict[str, Any]) -> str:
    for key in ("identity_anchor", "descriptor", "visual_reference"):
        text = re.sub(r"\s+", " ", str(character.get(key) or "")).strip().rstrip(".")
        if text:
            return text
    return "distinctive face and build"


def _character_wardrobe(character: Dict[str, Any], act: int, scene: Optional[Dict[str, Any]] = None) -> str:
    locked = re.sub(r"\s+", " ", str(character.get("wardrobe_lock") or "")).strip().rstrip(".")
    if locked:
        return locked
    wardrobe_by_act = character.get("wardrobe_by_act")
    if isinstance(wardrobe_by_act, list) and wardrobe_by_act:
        idx = max(0, min(len(wardrobe_by_act) - 1, int(act or 1) - 1))
        text = re.sub(r"\s+", " ", str(wardrobe_by_act[idx] or "")).strip().rstrip(".")
        if text:
            return text
    if isinstance(scene, dict):
        text = re.sub(r"\s+", " ", str(scene.get("wardrobe") or "")).strip().rstrip(".")
        if text:
            return text
    text = re.sub(r"\s+", " ", str(character.get("wardrobe") or character.get("costume") or "")).strip().rstrip(".")
    return text or "current act wardrobe"


def _resolve_cast_entry(text: str, master: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    index = canonical_cast(master)
    key = str(text or "").strip().lower()
    if not key:
        return None
    return (
        index.get(key)
        or index.get(re.sub(r"[^a-z0-9]+", " ", key).strip())
        or index.get(re.sub(r"[^a-z0-9]+", "_", key).strip("_"))
        or index.get(key.split()[0] if key.split() else key)
    )


def mentioned_character_ids(text: str, master: Dict[str, Any]) -> List[str]:
    """IDs of characters named in a text, in cast order."""
    raw = str(text or "")
    if not raw.strip():
        return []
    found: List[str] = []
    for character in master.get("characters") or []:
        if not isinstance(character, dict):
            continue
        cid = _character_id(character)
        if not cid:
            continue
        keys = {
            str(character.get("name") or "").strip(),
            str(character.get("name") or "").strip().split(" ")[0],
            cid,
        }
        for key in keys:
            if len(key) < 3:
                continue
            if re.search(rf"(?<![A-Za-z0-9]){re.escape(key)}(?![A-Za-z0-9])", raw, re.IGNORECASE):
                found.append(cid)
                break
    return found


def scene_characters_present(scene: Dict[str, Any], master: Dict[str, Any]) -> List[str]:
    """Ordered union of visible cast, speakers and named characters."""
    present: List[str] = []

    def add(text: str) -> None:
        character = _resolve_cast_entry(text, master)
        cid = _character_id(character or {}) or str(text or "").strip()
        if cid and cid not in present:
            present.append(cid)

    for item in scene.get("characters") or []:
        add(str(item or ""))
    for entry in scene_dialogue_lines(scene):
        add(entry.get("speaker") or "")
    cuts = scene.get("internal_cuts") or []
    first_action = str((cuts[0] or {}).get("action") or "") if cuts else ""
    text = " ".join([
        str(scene.get("first_frame_prompt") or ""),
        str(scene.get("action") or ""),
        first_action,
    ]).strip()
    for cid in mentioned_character_ids(text, master):
        if cid not in present:
            present.append(cid)
    order = character_position_map(master)
    return sorted(present, key=lambda cid: order.get(cid, 999))


OBJECT_VALUE_BLACKLIST = {
    "foreground",
    "background",
    "frame",
    "shot",
    "scene",
    "silence",
    "sharp",
}
OBJECT_VALUE_VERB_RE = re.compile(
    r"\b(?:is|was|are|were|be|been|being|has|have|had|does|did|will|would|"
    r"can|could|should|may|might|must|where|when|which|that|who|whom|whose)\b",
    re.IGNORECASE,
)
OBJECT_VALUE_MAX_WORDS = 6


def _clean_object_candidate(text: Any) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip().strip(" ,;.")


def is_concrete_object_value(text: Any) -> bool:
    """True only for a concrete object name or a short noun phrase.

    Prose fragments such as ``sharp`` (from "... sharp in the foreground") and
    ``the foreground`` must never become an object lock.
    """
    value = _clean_object_candidate(text)
    if not value:
        return False
    words = re.findall(r"[\w'-]+", value.lower())
    if not words or len(words) > OBJECT_VALUE_MAX_WORDS:
        return False
    if any(word.strip("'") in OBJECT_VALUE_BLACKLIST for word in words):
        return False
    if OBJECT_VALUE_VERB_RE.search(value):
        return False
    return True


def ledger_object_names(master: Optional[Dict[str, Any]]) -> List[str]:
    ledger = (master or {}).get("object_ledger")
    names: List[str] = []
    if not isinstance(ledger, list):
        return names
    for entry in ledger:
        name = entry.get("name") if isinstance(entry, dict) else entry
        text = _clean_object_candidate(name)
        if is_concrete_object_value(text) and text not in names:
            names.append(text)
    return names


def canonicalize_object_name(text: Any, master: Optional[Dict[str, Any]] = None) -> str:
    """Map a declared alias to the single matching ledger object name."""
    value = _clean_object_candidate(text)
    if not value:
        return ""
    names = ledger_object_names(master)
    lower = value.lower()
    for name in names:
        if name.lower() == lower:
            return name
    key = re.sub(r"^(?:the|a|an|his|her|their|its)\s+", "", lower, flags=re.IGNORECASE)
    matches = []
    for name in names:
        ledger_key = re.sub(
            r"^(?:the|a|an|his|her|their|its)\s+",
            "",
            name.lower(),
            flags=re.IGNORECASE,
        )
        if ledger_key == key or ledger_key.endswith(f" {key}"):
            matches.append(name)
    return matches[0] if len(matches) == 1 else value


def extract_key_object(scene: Dict[str, Any], master: Optional[Dict[str, Any]] = None) -> str:
    """Return the declared scene object, never a fragment of cut prose.

    Allowed sources, in order: explicit ``key_object``, declared ``props`` and
    the labelled ``Evidence object in play:`` field. Cut actions and free-form
    continuity prose are never parsed here.
    """
    candidates = [scene.get("key_object")]
    candidates.extend(scene.get("props") or [])
    match = re.search(
        r"Evidence object in play:\s*([^.;]+)",
        str(scene.get("continuity") or ""),
        re.IGNORECASE,
    )
    if match:
        candidates.append(match.group(1))
    for candidate in candidates:
        value = _clean_object_candidate(candidate)
        if is_concrete_object_value(value):
            return canonicalize_object_name(value, master)
    return ""


def _scrub_object_prose(text: Any, key_object: str = "") -> str:
    """Remove legacy fragments such as ``sharp`` or ``the foreground`` from prompt text."""
    value = str(text or "")
    if not value:
        return value
    replacement = key_object or "the key object"
    value = re.sub(
        r"\bsharp\s+in\s+the\s+foreground\b",
        "clearly visible in frame",
        value,
        flags=re.IGNORECASE,
    )
    value = re.sub(
        r"\bshows\s+sharp\s+being\s+placed\s+inside\s+the\s+frame\b",
        f"shows {replacement} being placed in the frame",
        value,
        flags=re.IGNORECASE,
    )
    value = re.sub(
        r"\bsharp\s+is\s+revealed\b",
        f"{replacement} is revealed",
        value,
        flags=re.IGNORECASE,
    )
    value = re.sub(r"\bthe\s+foreground\b", "the frame", value, flags=re.IGNORECASE)
    value = re.sub(r"\bsharp\b", replacement, value, flags=re.IGNORECASE)
    value = re.sub(
        r",?\s*looking at the other person in frame",
        "",
        value,
        flags=re.IGNORECASE,
    )
    value = re.sub(r"\bthe other person in frame\b", "the scene partner", value, flags=re.IGNORECASE)
    return value


def _scrub_key_object_clauses(text: Any, key_object: str) -> str:
    value = str(text or "")
    if not value:
        return value
    if not key_object:
        return re.sub(
            r"(?:Key object in frame:\s*[^.;]+[.;]\s*)+",
            "",
            value,
            flags=re.IGNORECASE,
        )
    return re.sub(
        r"(?:Key object in frame:\s*[^.;]+[.;]\s*)+",
        f"Key object in frame: {key_object}. ",
        value,
        flags=re.IGNORECASE,
    )


def _scrub_absent_look_targets(
    text: Any, present: Sequence[str], master: Dict[str, Any]
) -> str:
    value = str(text or "")
    if not value:
        return value

    def replace(match: "re.Match[str]") -> str:
        target = _flat(match.group(1)).strip(" ,.;")
        if not target:
            return ""
        if any(_same_character(target, cid, master) for cid in present):
            return match.group(0)
        return ""

    return re.sub(
        r",?\s*looking at ([A-Z][^.;,]*?)(?=[.;,]|$)",
        replace,
        value,
    )


def _replace_object_reference(text: Any, old: str, new: str) -> str:
    value = str(text or "")
    if not value or not old or not new:
        return value
    old_flat = _clean_object_candidate(old)
    if not old_flat:
        return value
    if re.search(r"\bforeground\b", old_flat, re.IGNORECASE):
        value = re.sub(r"\b(?:\w+\s+){0,2}?in the foreground\b", "clearly visible in frame", value, flags=re.IGNORECASE)
        value = re.sub(r"\bthe foreground\b", "the frame", value, flags=re.IGNORECASE)
        return value
    value = re.sub(rf"\b{re.escape(old_flat)}\s+in the foreground\b", "clearly visible in frame", value, flags=re.IGNORECASE)
    value = re.sub(rf"\b{re.escape(old_flat)}\b", new, value, flags=re.IGNORECASE)
    return value


def format_character_anchors(scene: Dict[str, Any], characters_locked: Any) -> str:
    """List of identity anchors for everyone present in the scene.

    ``characters_locked`` may be the full master or the character list.
    Each anchor fixes cast-sheet position, stable descriptor and wardrobe.
    """
    if isinstance(characters_locked, dict):
        cast = characters_locked.get("characters_locked") or characters_locked.get("characters") or []
    else:
        cast = list(characters_locked or [])
    cast = [c for c in cast if isinstance(c, dict)]
    if not cast:
        return ""
    by_id: Dict[str, Tuple[int, Dict[str, Any]]] = {}
    for idx, character in enumerate(cast, start=1):
        cid = _character_id(character)
        if cid:
            by_id[cid] = (idx, character)
    present = [str(x) for x in (scene.get("characters_present") or scene.get("characters") or []) if str(x).strip()]
    act = int(scene.get("act") or 1)
    anchors: List[str] = []
    for cid, (pos, character) in by_id.items():
        if cid not in present:
            continue
        anchors.append(_anchor_with_position(character, f"Cast Sheet Pos #{pos}:", act, scene))
    return "; ".join(anchors)


def build_storyboard_panel_description(scene: Dict[str, Any], master: Dict[str, Any]) -> str:
    """Describe the panel that MUST be Shot 1's first frame."""
    cuts = scene.get("internal_cuts") or []
    first = cuts[0] if cuts and isinstance(cuts[0], dict) else {}
    framing = str(first.get("framing") or "cinematic shot").strip()
    action = re.sub(r"\s+", " ", str(first.get("action") or "the subject is already in motion")).strip()
    action = action.rstrip(".")
    range_label = str(first.get("range") or SHOT_RANGES[0]).strip()
    location = re.sub(r"\s+", " ", str(scene.get("location") or "the scene location")).strip().rstrip(".")
    key_object = str((scene.get("object_start") or {}).get("name") or "").strip() or (
        extract_key_object(scene) or "the scene's central visual detail"
    )
    cast_index = canonical_cast(master)
    cast_ids = [str(cid) for cid in (scene.get("characters_present") or scene.get("characters") or [])]
    if scene.get("shot_lock_version") == "2":
        cast_ids = cast_ids[:MAX_SCENE_CAST]
    names = [str((cast_index.get(cid) or {}).get("name") or cid) for cid in cast_ids]
    present = ", ".join(names) if names else "the protagonist"
    extra = " No other characters appear." if scene.get("shot_lock_version") == "2" else ""
    object_part = "" if "key object in frame:" in action.lower() else f" Key object: {key_object}."
    return (
        f"[{range_label}] {framing}: {action}. "
        f"Location: {location}.{object_part} Characters present: {present}.{extra}"
    )


def scene_cast(master: Dict[str, Any], scene: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Canonical characters present in a scene (no duplicates, in order)."""
    index = character_by_key(master)
    out: List[Dict[str, Any]] = []
    for item in scene.get("characters_present") or scene.get("characters") or []:
        text = str(item or "").strip().lower()
        if not text:
            continue
        character = (
            index.get(text)
            or index.get(re.sub(r"[^a-z0-9]+", " ", text).strip())
            or index.get(re.sub(r"[^a-z0-9]+", "_", text).strip("_"))
            or index.get(text.split()[0] if text.split() else text)
        )
        if character is not None and character not in out:
            out.append(character)
    return out


FUTURE_REF_RE = re.compile(
    r"\b(scene\s+\d+|returns?\s+in|planted\s+in|pays?\s+off|reveals?\s+in|"
    r"will\s+be\s+(?:introduced|revealed)|later\s+in|in\s+act\s+\d+|"
    r"foreshadow|comes?\s+back\s+in|callback)\b",
    re.IGNORECASE,
)


def strip_future_refs(text: str) -> Tuple[str, List[str]]:
    """Separate PRESENT continuity from future references (spoilers).

    Returns (present_text, removed_sentences). Works sentence by sentence so no
    fragments are left dangling when a future reference is removed.
    """
    raw = str(text or "").strip()
    if not raw:
        return "", []
    kept: List[str] = []
    removed: List[str] = []
    for sentence in re.split(r"(?<=[.!?])\s+", raw):
        sentence = sentence.strip()
        if not sentence:
            continue
        if FUTURE_REF_RE.search(sentence):
            removed.append(sentence)
        else:
            kept.append(sentence)
    return " ".join(kept).strip(), removed


def location_keyword_match(location: str, master: Dict[str, Any]) -> bool:
    """True if the scene location matches the declared taxonomy."""
    text = str(location or "").strip().lower()
    if not text:
        return False
    entries = master.get("locations") or []
    if not entries:
        return True
    for entry in entries:
        if isinstance(entry, str):
            name = entry
        elif isinstance(entry, dict):
            name = f"{entry.get('id') or ''} {entry.get('name') or ''}".strip()
        else:
            continue
        for word in re.split(r"[^a-z0-9]+", name.lower()):
            if len(word) >= 4 and word in text:
                return True
    return False


# --- Master JSON normalization and validation ---
def _coerce_dialogue(value: Any) -> List[Dict[str, Any]]:
    if isinstance(value, str):
        value = [value]
    if not isinstance(value, list):
        return []
    out: List[Dict[str, Any]] = []
    for item in value:
        if isinstance(item, str) and item.strip():
            out.append({"speaker": "", "line": item.strip(), "delivery": "", "shot": 0, "recipient": ""})
        elif isinstance(item, dict):
            line = str(item.get("line") or item.get("text") or "").strip()
            if line:
                try:
                    shot = int(item.get("shot") or 0)
                except (TypeError, ValueError):
                    shot = 0
                out.append({
                    "speaker": str(item.get("speaker") or "").strip(),
                    "line": line,
                    "delivery": str(item.get("delivery") or "").strip(),
                    "shot": shot,
                    "recipient": str(item.get("recipient") or "").strip(),
                })
    return out


CLOSEUP_RE = re.compile(r"close[\s-]?up|over[\s-]?the[\s-]?shoulder|\bOTS\b|medium close", re.IGNORECASE)
REACTION_RE = re.compile(r"tight close|close[\s-]?up|extreme close|insert|reaction|detail|\bPOV\b|point of view", re.IGNORECASE)
STATIC_RE = re.compile(
    r"\bstatic\b|\bposed\b|\bnot moving\b|\bhold(?:ing)? still\b|\bmotionless\b|"
    r"\bfreezes?\b|\bgo(?:es)? still\b|\bstands? (?:still|rigid|erect|immobile|frozen)\b",
    re.IGNORECASE,
)


PLACEHOLDER_ACTION_PATTERNS = (
    "hard cut into the dialogue beat with the speaker mid-line",
    "hard cut to the reaction as the line lands",
    "the subject is already moving inside the storyboard framing",
    "reacts as the line lands, no static hold",
    "the room falls quiet around it",
    "as the cost of the line lands",
    "absorbs the line, jaw tight",
)

CONTINUITY_NOTE_RE = re.compile(
    r"\b(?:hard cut|the room falls quiet|no static hold|speaker mid-line|placeholder)\b",
    re.IGNORECASE,
)
CAMERA_NOTE_RE = re.compile(
    r"^(?:close(?:-up)? on|low angle|high angle|wide|medium|tight|insert\s*:|cut to|"
    r"over (?:her|his|the|their) shoulder|angle on|camera)\b",
    re.IGNORECASE,
)


def is_placeholder_text(text: str) -> bool:
    """True if the text is a mechanical camera or continuity placeholder."""
    flat = re.sub(r"\s+", " ", str(text or "")).strip().lower()
    if not flat:
        return False
    return any(pattern in flat for pattern in PLACEHOLDER_ACTION_PATTERNS) or bool(
        CONTINUITY_NOTE_RE.search(flat)
    )


def _scene_display_names(scene: Dict[str, Any], cast_index: Dict[str, Dict[str, Any]]) -> List[str]:
    names: List[str] = []
    for raw in scene.get("characters_present") or scene.get("characters") or []:
        text = str(raw or "").strip()
        if not text:
            continue
        character = (
            cast_index.get(text.lower())
            or cast_index.get(re.sub(r"[^a-z0-9]+", " ", text.lower()).strip())
            or cast_index.get(re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_"))
        )
        name = str((character or {}).get("name") or text).strip()
        if name and name not in names:
            names.append(name)
    return names


def _concrete_cut_action(
    index: int,
    scene: Dict[str, Any],
    cast_index: Dict[str, Dict[str, Any]],
) -> str:
    """Concrete visual action when the LLM did not provide one."""
    names = _scene_display_names(scene, cast_index)
    first = names[0] if names else "The protagonist"
    second = names[1] if len(names) > 1 else first
    location = str(scene.get("location") or "the scene location").strip().rstrip(".")
    key_object = extract_key_object(scene) or "the central visual detail"
    speaker = ""
    last_speaker = ""
    listener = second
    lines = scene.get("dialogue") if isinstance(scene.get("dialogue"), list) else []
    line_text = ""

    def _speaker_name(raw: Any) -> str:
        value = str(raw or "").strip()
        return next(
            (
                name
                for name in names
                if value
                and (
                    name.lower().startswith(value.lower())
                    or value.lower() in name.lower()
                )
            ),
            value,
        )

    dialogue_names: List[str] = []
    for item in lines:
        if not isinstance(item, dict):
            continue
        name = _speaker_name(item.get("speaker"))
        if name and name not in dialogue_names:
            dialogue_names.append(name)
    if lines and isinstance(lines[0], dict):
        speaker = _speaker_name(lines[0].get("speaker"))
    if lines and isinstance(lines[-1], dict):
        last_speaker = _speaker_name(lines[-1].get("speaker"))
        line_text = str(lines[-1].get("line") or "").strip().rstrip(".")
    if last_speaker:
        listener = next(
            (name for name in reversed(dialogue_names) if name != last_speaker),
            "",
        )
        if not listener:
            listener = next((name for name in names if name != last_speaker), last_speaker)
    if index == 0:
        return (
            f"{first} is already moving through {location}, the action carrying over "
            "from the exact storyboard framing."
        )
    if index == 1:
        return (
            f"{speaker or first} speaks as the camera holds close on their face, "
            f"{key_object} catching the light between them."
        )
    if line_text and listener != last_speaker:
        return f'{listener} holds the silence after "{line_text}", {key_object} sharp in the foreground.'
    if line_text:
        return f'The silence after "{line_text}" hangs, {key_object} sharp in the foreground.'
    if listener != first:
        return f"{listener} holds {first}'s gaze while the words settle between them."
    return f"{first} takes the line without flinching, one hand closing around {key_object}."


def _coerce_cuts(
    value: Any,
    rotation: Sequence[str],
    scene: Optional[Dict[str, Any]] = None,
    cast_index: Optional[Dict[str, Dict[str, Any]]] = None,
) -> List[Dict[str, Any]]:
    """Force exactly 3 shots: 00s-03s, 03s-07s, and 07s-10s.

    Shot 1 keeps the panel framing and starts in motion. Shot 2 is
    corrects to close-up/OTS if the beat does not belong to that family. Shot 3 is
    corrected to a reaction/insert if the beat does not belong to that family.
    Mechanical placeholders are replaced with concrete scene actions.
    """
    scene = scene or {}
    cast_index = cast_index or {}
    provided: List[Dict[str, str]] = []
    if isinstance(value, list):
        for item in value:
            if isinstance(item, dict):
                provided.append({
                    "framing": str(item.get("framing") or item.get("shot") or "").strip(),
                    "action": str(item.get("action") or item.get("description") or "").strip(),
                })
            elif isinstance(item, str) and item.strip():
                provided.append({"framing": item.strip(), "action": ""})

    shot1_fallback = rotation[0] if rotation else "wide establishing shot"
    shot2_fallback = "close-up"
    shot3_fallback = "tight close-up"
    framings = [
        provided[0]["framing"] if len(provided) > 0 and provided[0]["framing"] else shot1_fallback,
        provided[1]["framing"] if len(provided) > 1 and provided[1]["framing"] else shot2_fallback,
        provided[2]["framing"] if len(provided) > 2 and provided[2]["framing"] else shot3_fallback,
    ]
    if not CLOSEUP_RE.search(framings[1]):
        framings[1] = shot2_fallback
    if not REACTION_RE.search(framings[2]):
        framings[2] = shot3_fallback

    cuts: List[Dict[str, Any]] = []
    for i, at in enumerate(SHOT_CUT_TIMES):
        raw_action = provided[i]["action"] if len(provided) > i else ""
        if (
            not raw_action
            or is_placeholder_text(raw_action)
            or (i == 0 and STATIC_RE.search(raw_action))
        ):
            raw_action = _concrete_cut_action(i, scene, cast_index)
        cuts.append({
            "at": at,
            "range": SHOT_RANGES[i],
            "framing": framings[i],
            "action": raw_action,
        })
    return cuts


# ===========================================================================
# Contract v2: one line = one shot with visible speaker + guaranteed object
# ===========================================================================
FACE_BLOCKED_RE = re.compile(
    r"\b(?:back(?:ed)? to (?:the )?camera|from behind|rear view|silhouette|"
    r"out of focus|blurred|face hidden|off[- ]screen|only (?:his|her|their) hands?|"
    r"hand insert|insert of (?:the|a|his|her) hand|empty (?:frame|shot)|"
    r"object insert|detail insert|no face)\b",
    re.IGNORECASE,
)
HAND_ONLY_RE = re.compile(
    r"\b(?:his|her|their|[A-Z][a-z]+'s) (?:gloved )?hands?\b|\bhands? only\b|"
    r"\bhand insert\b|\b(?:gloved )?fingers?\b|\bthumb\b|\bclasp\b",
    re.IGNORECASE,
)
FACE_PRESENT_RE = re.compile(
    r"\b(?:face|faces|eyes|mouth|lips|gaze|looks?|looking|stares?|staring|"
    r"turns? (?:to|toward)|two-shot|over[- ]the[- ]shoulder|OTS)\b",
    re.IGNORECASE,
)
INSERT_RE = re.compile(
    r"\b(?:insert|macro|extreme close[- ]up (?:of|on) (?:the|a|his|her) "
    r"(?:hand|object|watch|bag|paper|prop|detail))\b",
    re.IGNORECASE,
)
REACTION_ONLY_RE = re.compile(
    r"\b(?:reaction shot|says nothing|silent reaction|listens?|watches?|observes?|"
    r"holds? (?:the|her|his) (?:gaze|silence))\b",
    re.IGNORECASE,
)
AGE_RE = re.compile(
    r"\b(?:early|mid|late)[\s-]?(?:twenties|thirties|forties|fifties|sixties|"
    r"seventies)|\b(?:around|about)\s+(?:twenty|thirty|forty|fifty|sixty)|"
    r"\b(?:teenage|young|middle[- ]aged|elderly)\b",
    re.IGNORECASE,
)
HAIR_RE = re.compile(
    r"\b(?:hair|braid|braided|bob|ponytail|bun|chignon|updo|pixie|curls?|curly|wavy|straight|"
    r"bald|shaved|beard|moustache|mustache|bangs|fringe)\b",
    re.IGNORECASE,
)
PLANT_RE = re.compile(
    r"(?P<by>\b[A-Z][a-zA-Z'-]+)?\s*"
    r"(?P<verb>slips?|slides?|hides?|plants?|tucks?|drops?|puts?|places?|shoves?)\s+"
    r"(?P<obj>(?:(?:the|a|an|his|her|their|its)\s+)?[^.;,]{2,70}?)\s+"
    r"(?:inside|into|in)\s+(?P<container>[^.;,]{2,70})",
    re.IGNORECASE,
)
REVEAL_RE = re.compile(
    r"\b(?:finds?|reveals?|pulls? out|takes? out|lifts?|raises?|"
    r"shows?|discovers?|uncovers?|draws? out|produces?)\b",
    re.IGNORECASE,
)
SPEAKING_VERB_RE = re.compile(
    r"\b(?:speaks?|says|whispers?|mutters?|shouts?|yells?|talks?)\b",
    re.IGNORECASE,
)
HIDDEN_INTERIOR_RE = re.compile(
    r"\b(?:interior|inside (?:the|her|his|their) (?:open )?(?:canvas |work )?bag|"
    r"empty (?:canvas |work )?bag|empty|contents|leather tools?|drawstring open|"
    r"open(?:ed)? (?:the )?(?:canvas |work )?bag|bag (?:is )?open)\b",
    re.IGNORECASE,
)


def _flat(text: Any) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()


def _display_name(cid: str, master: Dict[str, Any]) -> str:
    resolved = resolve_speaker(str(cid or ""), master)
    key = resolved or str(cid or "").strip()
    for character in master.get("characters") or []:
        if not isinstance(character, dict):
            continue
        if str(character.get("id") or "").strip() == key or str(character.get("name") or "").strip() == key:
            return str(character.get("name") or character.get("id") or key).strip()
    return key


def _same_character(a: str, b: str, master: Dict[str, Any]) -> bool:
    ra = resolve_speaker(str(a or ""), master) or str(a or "").strip().lower()
    rb = resolve_speaker(str(b or ""), master) or str(b or "").strip().lower()
    return bool(ra) and ra == rb


def _contains_name(text: str, name: str) -> bool:
    name = str(name or "").strip()
    if len(name) < 3:
        return False
    return bool(re.search(rf"(?<![A-Za-z0-9]){re.escape(name)}(?![A-Za-z0-9])", str(text or ""), re.IGNORECASE))


def _line_addressed_ids(line: str, master: Dict[str, Any]) -> List[str]:
    """IDs named or addressed in a line (Mr. Blackwell -> the Blackwells)."""
    text = str(line or "")
    found: List[str] = []
    for character in master.get("characters") or []:
        if not isinstance(character, dict):
            continue
        cid = _character_id(character)
        if not cid:
            continue
        full = str(character.get("name") or "").strip()
        parts = full.split()
        first = parts[0] if parts else ""
        last = parts[-1] if len(parts) > 1 else ""
        matched = False
        if full and _contains_name(text, full):
            matched = True
        elif first and _contains_name(text, first):
            matched = True
        if not matched and last:
            for title in ("Mr", "Mrs", "Ms", "Miss", "Sir", "Madam", "Dr"):
                if re.search(
                    rf"(?<![A-Za-z0-9]){re.escape(title)}\.?\s+{re.escape(last)}(?![A-Za-z0-9])",
                    text,
                    re.IGNORECASE,
                ):
                    matched = True
                    break
        if matched and cid not in found:
            found.append(cid)
    return found


def line_ownership_error(line: str, speaker: str, master: Dict[str, Any]) -> Optional[str]:
    """A line that names/addresses X cannot be spoken by X (nobody calls themselves)."""
    speaker_cid = resolve_speaker(str(speaker or ""), master) or str(speaker or "").strip()
    if not speaker_cid:
        return None
    for cid in _line_addressed_ids(line, master):
        if _same_character(cid, speaker_cid, master):
            name = _display_name(cid, master)
            return f'the line "{line}" names {name}; {name} cannot say it.'
    return None


def character_prompt_anchor(character: Dict[str, Any], act: int, scene: Optional[Dict[str, Any]] = None) -> str:
    """3 discriminators visible in the image: approximate age, hairstyle, and wardrobe.

    It does not invent eye color, skin tone, build or footwear that is not visible.
    """
    name = str(character.get("name") or character.get("id") or "Character").strip()
    descriptor = _character_descriptor(character)
    segments = [s.strip() for s in re.split(r",\s*", descriptor) if s.strip()]
    age = ""
    hair = ""
    for segment in segments:
        match = AGE_RE.search(segment)
        if match and not age:
            age = match.group(0).strip()
        if HAIR_RE.search(segment) and not hair:
            hair = segment
    if age and hair.lower().startswith(age.lower()):
        hair = hair[len(age):].strip(" ,")
    if not hair:
        rest = [segment for segment in segments if segment != age]
        hair = ", ".join(rest).strip() or "distinctive face and build"
    if not age:
        age = "adult"
    wardrobe = _character_wardrobe(character, act, scene)
    wardrobe_words = wardrobe.split()
    if len(wardrobe_words) > 18:
        wardrobe = " ".join(wardrobe_words[:18])
    return f"{name} (Cast Sheet Pos #0: {age}; {hair}; wearing {wardrobe})"


def _anchor_with_position(character: Dict[str, Any], prefix: str, act: int, scene: Optional[Dict[str, Any]]) -> str:
    text = character_prompt_anchor(character, act, scene)
    return text.replace("Cast Sheet Pos #0:", prefix.strip())


def _cut_text(cut: Dict[str, Any]) -> str:
    return _flat(f"{cut.get('framing') or ''} {cut.get('action') or ''}")


def _cut_is_hand_or_insert(cut: Dict[str, Any]) -> bool:
    text = _cut_text(cut)
    if not text:
        return False
    if _flat(cut.get("kind") or "").lower() == "object":
        return True
    if INSERT_RE.search(text) and not FACE_PRESENT_RE.search(text):
        return True
    if HAND_ONLY_RE.search(text) and not FACE_PRESENT_RE.search(text):
        return True
    return False


def face_visible_in_cut(cut: Dict[str, Any]) -> bool:
    """True if the shot can hold a line with visible lips."""
    text = _cut_text(cut)
    if not text:
        return False
    if FACE_BLOCKED_RE.search(text):
        return False
    if _cut_is_hand_or_insert(cut):
        return False
    if REACTION_ONLY_RE.search(text) and not FACE_PRESENT_RE.search(text):
        return False
    return True


def _cut_mention_ids(cut: Dict[str, Any], master: Dict[str, Any]) -> List[str]:
    return mentioned_character_ids(_cut_text(cut), master)


def _cut_mentions(cut: Dict[str, Any], cid: str, master: Dict[str, Any]) -> bool:
    key = resolve_speaker(str(cid or ""), master) or str(cid or "")
    mentioned = _cut_mention_ids(cut, master)
    if key and key in mentioned:
        return True
    return _contains_name(_cut_text(cut), _display_name(key, master))


def _strip_quotes(text: Any) -> str:
    value = str(text or "")
    value = re.sub(r'"[^"]*"', "", value)
    value = re.sub(r"“[^”]*”", "", value)
    return _flat(value).strip(" ,.;")


def _spoken_action(speaker: str, recipient: str, base: str, two_shot_with: str = "") -> str:
    speaker = speaker or "The speaker"
    recipient_text = str(recipient or "").strip()
    base = _strip_quotes(base)
    if two_shot_with:
        first = (
            f"{speaker} and {two_shot_with} face each other in a two-shot, "
            "both faces and mouths fully visible, each oriented toward the other."
        )
    elif recipient_text:
        first = (
            f"{speaker} is on camera with face and mouth fully visible, "
            f"looking at {recipient_text}."
        )
    else:
        first = (
            f"{speaker} is on camera alone in the frame with face and mouth fully visible."
        )
    return _flat(f"{first} {base}") if base else first


def _dialogue_framing(framing: Any, speaker: str) -> str:
    text = _flat(framing)
    if not text or _cut_is_hand_or_insert({"framing": text, "action": ""}):
        return f"medium close-up on {speaker}, face and mouth visible"
    if text.lower().startswith("two-shot"):
        return text
    if FACE_PRESENT_RE.search(text):
        return text
    return f"{text}, face and mouth visible"


def _recipient_for(
    line: str,
    speaker_cid: str,
    speakers: Sequence[str],
    present: Sequence[str],
    master: Dict[str, Any],
    explicit: str = "",
) -> str:
    present_ids = {str(cid) for cid in present if str(cid).strip()}

    def in_scene(cid: str) -> bool:
        resolved = resolve_speaker(str(cid or ""), master) or str(cid or "").strip()
        return bool(resolved) and resolved in present_ids

    if explicit:
        resolved = resolve_speaker(explicit, master) or explicit
        if in_scene(resolved) and not _same_character(resolved, speaker_cid, master):
            return _display_name(resolved, master)
    addressed = [cid for cid in _line_addressed_ids(line, master) if not _same_character(cid, speaker_cid, master)]
    for cid in addressed:
        if cid in speakers and in_scene(cid):
            return _display_name(cid, master)
    for cid in addressed:
        if in_scene(cid):
            return _display_name(cid, master)
    for cid in speakers:
        if not _same_character(cid, speaker_cid, master) and in_scene(cid):
            return _display_name(cid, master)
    for cid in present:
        if not _same_character(cid, speaker_cid, master):
            return _display_name(cid, master)
    return ""


def _cut_range(a: float, b: float) -> str:
    return f"{int(round(a)):02d}s-{int(round(b)):02d}s"


def _retime_cuts(
    cuts: List[Dict[str, Any]],
    total: float = SCENE_SECONDS,
    lines: Optional[Sequence[Dict[str, Any]]] = None,
) -> List[Dict[str, Any]]:
    """Split 10 s across shots: each line keeps its speech time."""
    if not cuts:
        return cuts
    wps = SPEECH_WORDS_PER_SECOND
    lines = list(lines or [])
    desired: List[float] = []
    for cut in cuts:
        indexes = cut.get("line_indexes") or []
        if indexes:
            speech = 0.0
            for i in indexes:
                text = str((lines[i] if 0 <= i < len(lines) else {}).get("line") or "")
                speech += len(re.findall(r"\b[\w'-]+\b", text)) / wps
            desired.append(max(1.2, speech + SPEECH_PAD_SECONDS + SPEECH_GAP_SECONDS * max(0, len(indexes) - 1)))
        elif cut.get("kind") == "object":
            desired.append(OBJECT_FOCUS_MIN_SECONDS + 0.2)
        else:
            desired.append(1.5)
    if sum(desired) < total and any(cut.get("line_indexes") for cut in cuts):
        remaining = total - sum(desired)
        dialogue_count = sum(1 for cut in cuts if cut.get("line_indexes"))
        share = remaining / max(1, dialogue_count)
        for idx, cut in enumerate(cuts):
            if cut.get("line_indexes"):
                desired[idx] += share
    elif sum(desired) > total:
        for idx, cut in enumerate(cuts):
            if not cut.get("line_indexes") and cut.get("kind") != "object":
                desired[idx] = 1.0
            elif cut.get("kind") == "object":
                desired[idx] = OBJECT_FOCUS_MIN_SECONDS
        if sum(desired) > total:
            for idx, cut in enumerate(cuts):
                if cut.get("line_indexes"):
                    desired[idx] = max(1.0, desired[idx] - SPEECH_PAD_SECONDS)
        if sum(desired) > total:
            scale = total / sum(desired)
            desired = [d * scale for d in desired]
    at = 0.0
    for idx, cut in enumerate(cuts):
        duration = desired[idx] if idx < len(cuts) - 1 else max(0.5, total - at)
        cut["at"] = round(at, 2)
        cut["range"] = _cut_range(at, at + duration)
        at += duration
    cuts[-1]["range"] = _cut_range(float(cuts[-1]["at"]), total)
    return cuts


def _pick_spoken_cut(
    cuts: List[Dict[str, Any]],
    cid: str,
    master: Dict[str, Any],
    exclude: Optional[set] = None,
) -> Optional[int]:
    exclude = exclude or set()
    for index, cut in enumerate(cuts):
        if index in exclude:
            continue
        if not face_visible_in_cut(cut):
            continue
        if _cut_mentions(cut, cid, master):
            return index
    return None


def _new_spoken_cut(cid: str, master: Dict[str, Any]) -> Dict[str, Any]:
    name = _display_name(cid, master)
    return {
        "framing": f"medium close-up on {name}, face and mouth visible",
        "action": f"{name} holds the moment before speaking.",
        "dialogue": True,
        "silent": False,
        "kind": "dialogue",
    }


def _new_object_cut(scene: Dict[str, Any], master: Dict[str, Any]) -> Dict[str, Any]:
    obj = str(scene.get("planted_object") or extract_key_object(scene) or "the story object").strip()
    container = str(scene.get("planted_in") or "").strip()
    if scene.get("object_focus") == "plant" and container:
        action = f"A silent insert shows {obj} being placed inside {container}; no face in this shot."
    else:
        action = f"{obj} is revealed in a silent, centered close-up, clearly visible and unobstructed."
    return {
        "framing": "tight close-up of the story object, centered",
        "action": action,
        "dialogue": False,
        "silent": True,
        "kind": "object",
    }


def _find_object_cut(
    cuts: List[Dict[str, Any]],
    scene: Dict[str, Any],
    master: Dict[str, Any],
    exclude: Optional[set] = None,
) -> Optional[Dict[str, Any]]:
    exclude = exclude or set()
    names = [
        str(scene.get("planted_object") or "").strip(),
        str(scene.get("planted_in") or "").strip(),
        extract_key_object(scene),
        str((scene.get("object_start") or {}).get("name") or "").strip(),
        str((scene.get("object_end") or {}).get("name") or "").strip(),
    ]
    names = [name for name in dict.fromkeys(names) if name]
    def speaking(cut: Dict[str, Any]) -> bool:
        text = _cut_text(cut)
        return bool(cut.get("dialogue") or SPEAKING_VERB_RE.search(text) or '"' in text or "“" in text)

    for index, cut in enumerate(cuts):
        if index in exclude or speaking(cut):
            continue
        text = _cut_text(cut)
        if any(_contains_name(text, name) or name.lower() in text.lower() for name in names):
            if _cut_is_hand_or_insert(cut) or cut.get("kind") == "object":
                return cut
    for index, cut in enumerate(cuts):
        if index in exclude or speaking(cut):
            continue
        if any(_contains_name(_cut_text(cut), name) or name.lower() in _cut_text(cut).lower() for name in names):
            return cut
    return None


def _silent_kind(cut: Dict[str, Any], scene: Dict[str, Any]) -> str:
    text = _cut_text(cut)
    if scene.get("object_hidden") and HIDDEN_INTERIOR_RE.search(text):
        return "hidden"
    if _cut_is_hand_or_insert(cut):
        return "insert"
    if REACTION_ONLY_RE.search(text):
        return "reaction"
    return "silent"


def _subject_name(cut: Dict[str, Any], master: Dict[str, Any]) -> str:
    mentioned = _cut_mention_ids(cut, master)
    if mentioned:
        return _display_name(mentioned[0], master)
    return ""


def _sanitize_hidden_text(text: str) -> str:
    value = str(text or "")
    value = re.sub(
        r"\b(?:pulls?|tugs?|tears?) (?:the )?(?:drawstring )?open\b",
        "loosens the drawstring without opening the bag",
        value,
        flags=re.IGNORECASE,
    )
    value = re.sub(
        r"\bopens? (?:the )?(?:canvas |work )?bag\b",
        "loosens the bag",
        value,
        flags=re.IGNORECASE,
    )
    value = re.sub(
        r"\bopen (?:canvas |work )?bag\b",
        "loosened bag",
        value,
        flags=re.IGNORECASE,
    )
    value = re.sub(
        r"\b(?:the )?(?:canvas |work )?bag (?:is|stays) open\b",
        "the bag stays loosened but never gaping",
        value,
        flags=re.IGNORECASE,
    )
    value = re.sub(r"\bleather tools?\b", "the bag's outer seam", value, flags=re.IGNORECASE)
    value = re.sub(r"\b(?:empty|interior|contents)\b", "exterior", value, flags=re.IGNORECASE)
    return _flat(value)


def _sanitize_silent_speech(text: Any) -> str:
    value = _strip_quotes(str(text or ""))
    value = re.sub(
        r"[,;]?\s*\b(?:as|while|when)\s+(?:she|he|they|the\s+[a-z]+|[A-Z][a-z]+)\s+"
        r"(?:speaks?|says|whispers?|mutters?|shouts?|yells?|talks?)\b[^.;]*",
        "",
        value,
        flags=re.IGNORECASE,
    )
    value = SPEAKING_VERB_RE.sub("stays silent", value)
    value = re.sub(r"\bafter\s*,", "after the line,", value)
    value = re.sub(r"\bThe silence after\b", "The silence", value)
    return _flat(value)


def _rewrite_hidden_object(cut: Dict[str, Any], scene: Dict[str, Any], master: Dict[str, Any]) -> None:
    container = str(scene.get("planted_in") or "").strip()
    if not container:
        container = str((scene.get("object_start") or {}).get("name") or "").strip()
    if not container:
        container = "the bag"
    text = _cut_text(cut)
    if not HIDDEN_INTERIOR_RE.search(text):
        return
    safe = _sanitize_hidden_text(str(cut.get("action") or ""))
    rule = (
        "Its interior remains in shadow and out of frame; "
        "never show it empty and never show a full interior."
    )
    if cut.get("dialogue"):
        cut["action"] = _flat(f"{safe.rstrip('.')}. {rule}" if safe else rule)
    else:
        subject = _subject_name(cut, master) or "The camera"
        cut["action"] = _flat(
            f"{subject} stays on the outside of {container}, which stays loosened "
            f"but never gaping. {rule}"
        )


def _plan_scene_shots(scene: Dict[str, Any], master: Dict[str, Any]) -> List[Dict[str, Any]]:
    cuts = [copy.deepcopy(c) for c in (scene.get("internal_cuts") or []) if isinstance(c, dict)]
    lines = [dict(entry) for entry in scene_dialogue_lines(scene)]
    if not cuts:
        cuts = [{"framing": "medium shot", "action": ""}]
    for cut in cuts:
        cut["dialogue"] = False
        cut["silent"] = True
        cut["kind"] = "silent"
        cut["speakers"] = []
        cut.pop("line_indexes", None)
    if not lines:
        for cut in cuts:
            cut["kind"] = _silent_kind(cut, scene)
            cut["action"] = _sanitize_silent_speech(cut.get("action") or "")
        return _retime_cuts(cuts[:MAX_CUTS_PER_SCENE], lines=lines)

    present = scene_characters_present(scene, master)
    speaker_ids = [
        resolve_speaker(str(line.get("speaker") or ""), master) or str(line.get("speaker") or "").strip()
        for line in lines
    ]
    unique_speakers: List[str] = []
    for cid in speaker_ids:
        if cid and cid not in unique_speakers:
            unique_speakers.append(cid)
    object_focus = str(scene.get("object_focus") or "").strip()
    reveal = object_focus == "reveal"
    two_shot = len(lines) == 2 and len(unique_speakers) == 2 and not reveal
    selection: Dict[int, int] = {}

    if two_shot:
        shared: Optional[int] = None
        for index, cut in enumerate(cuts):
            if not _cut_is_hand_or_insert(cut) and not REACTION_ONLY_RE.search(_cut_text(cut)):
                shared = index
                break
        if shared is None:
            cuts.insert(0, {"framing": "two-shot, medium shot", "action": ""})
            shared = 0
        if shared != 0:
            cuts.insert(0, cuts.pop(shared))
            shared = 0
        first_name = _display_name(unique_speakers[0], master)
        second_name = _display_name(unique_speakers[1], master)
        base = _strip_quotes(cuts[shared].get("action") or "")
        cuts[shared]["framing"] = f"two-shot, medium shot with {first_name} and {second_name}"
        cuts[shared]["action"] = _spoken_action(first_name, second_name, base, two_shot_with=second_name)
        cuts[shared]["dialogue"] = True
        cuts[shared]["silent"] = False
        cuts[shared]["kind"] = "dialogue"
        cuts[shared]["speakers"] = [unique_speakers[0], unique_speakers[1]]
        cuts[shared]["line_indexes"] = [0, 1]
        selection[0] = shared
        selection[1] = shared
    elif reveal and len(lines) >= 2:
        first = _pick_spoken_cut(cuts, speaker_ids[0], master)
        if first is None:
            cuts.insert(0, _new_spoken_cut(speaker_ids[0], master))
            first = 0
        selection[0] = first
        second = _pick_spoken_cut(cuts, speaker_ids[1], master, exclude={first})
        if second is None:
            second = len(cuts)
            cuts.append(_new_spoken_cut(speaker_ids[1], master))
        selection[1] = second
    else:
        used: set = set()
        for index, cid in enumerate(speaker_ids):
            chosen = _pick_spoken_cut(cuts, cid, master, exclude=used)
            if chosen is None:
                chosen = len(cuts)
                cuts.append(_new_spoken_cut(cid, master))
            selection[index] = chosen
            used.add(chosen)

    groups: List[tuple] = []
    for cut_index in sorted(set(selection.values())):
        cut = cuts[cut_index]
        indexes = [i for i in range(len(lines)) if selection.get(i) == cut_index]
        groups.append((cut_index, cut, indexes))
    groups.sort(key=lambda item: min(item[2]) if item[2] else 999)

    for _cut_index, cut, indexes in groups:
        cut["dialogue"] = True
        cut["silent"] = False
        cut["kind"] = "dialogue"
        cut["line_indexes"] = indexes
        cut["speakers"] = [speaker_ids[i] for i in indexes if speaker_ids[i]]
        if not str(cut.get("framing") or "").lower().startswith("two-shot"):
            speaker_id = cut["speakers"][0] if cut["speakers"] else ""
            speaker = _display_name(speaker_id, master) if speaker_id else "The speaker"
            recipient = _recipient_for(
                lines[indexes[0]]["line"] if indexes else "",
                speaker_id,
                unique_speakers,
                present,
                master,
                explicit=str(lines[indexes[0]].get("recipient") or "") if indexes else "",
            )
            cut["framing"] = _dialogue_framing(cut.get("framing"), speaker)
            cut["action"] = _spoken_action(speaker, recipient, cut.get("action") or "")
        cut["action"] = _strip_quotes(cut.get("action") or "")

    object_cut: Optional[Dict[str, Any]] = None
    if object_focus:
        object_cut = _find_object_cut(cuts, scene, master, exclude=set(selection.values()))
        if object_cut is None:
            object_cut = _new_object_cut(scene, master)
            cuts.append(object_cut)
        object_cut["dialogue"] = False
        object_cut["silent"] = True
        object_cut["kind"] = "object"

    used = set(selection.values())
    if object_cut is not None:
        used.add(cuts.index(object_cut))
    silent_cuts: List[Dict[str, Any]] = []
    for index, cut in enumerate(cuts):
        if index in used:
            continue
        cut["dialogue"] = False
        cut["silent"] = True
        cut["kind"] = _silent_kind(cut, scene)
        cut["action"] = _sanitize_silent_speech(cut.get("action") or "")
        silent_cuts.append(cut)

    if scene.get("object_hidden"):
        for _cut_index, cut, _indexes in groups:
            _rewrite_hidden_object(cut, scene, master)
        for cut in silent_cuts:
            _rewrite_hidden_object(cut, scene, master)

    final: List[Dict[str, Any]] = []
    if reveal and len(groups) >= 2:
        final.append(groups[0][1])
        if object_cut is not None:
            final.append(object_cut)
        final.append(groups[1][1])
        final.extend(silent_cuts)
    else:
        final.extend(group[1] for group in groups)
        if object_cut is not None:
            final.append(object_cut)
        final.extend(silent_cuts)
    unique_final: List[Dict[str, Any]] = []
    for cut in final:
        if cut not in unique_final:
            unique_final.append(cut)
    if len(unique_final) > MAX_CUTS_PER_SCENE:
        keep = [cut for cut in unique_final if cut.get("dialogue") or cut.get("kind") == "object"]
        extra = [cut for cut in unique_final if cut not in keep]
        unique_final = keep[:MAX_CUTS_PER_SCENE] + extra[:max(0, MAX_CUTS_PER_SCENE - len(keep))]
    for cut in unique_final:
        cut.pop("_lines", None)
    return _retime_cuts(unique_final, lines=lines)


def _apply_dialogue_shots(scene: Dict[str, Any], master: Dict[str, Any]) -> None:
    cuts = [c for c in (scene.get("internal_cuts") or []) if isinstance(c, dict)]
    lines = [dict(entry) for entry in scene_dialogue_lines(scene)]
    if not lines:
        scene["dialogue"] = []
        return
    present = [str(cid) for cid in (scene.get("characters_present") or [])]
    speaker_ids = [
        resolve_speaker(str(entry.get("speaker") or ""), master)
        or str(entry.get("speaker") or "").strip()
        for entry in lines
    ]
    unique_speakers: List[str] = []
    for cid in speaker_ids:
        if cid and cid not in unique_speakers:
            unique_speakers.append(cid)
    for index, entry in enumerate(lines):
        shot = 1
        for cut_index, cut in enumerate(cuts, start=1):
            if index in (cut.get("line_indexes") or []):
                shot = cut_index
                break
        entry["shot"] = shot
        entry["recipient"] = _recipient_for(
            entry.get("line") or "",
            speaker_ids[index],
            unique_speakers,
            present,
            master,
            explicit=str(entry.get("recipient") or ""),
        )
    scene["dialogue"] = lines


def _scene_lock_text(scene: Dict[str, Any]) -> str:
    cuts = scene.get("internal_cuts") or []
    actions = " ".join(str((cut or {}).get("action") or "") for cut in cuts if isinstance(cut, dict))
    return _flat(" ".join([
        str(scene.get("single_change_at_end") or ""),
        str(scene.get("this_scene_starts_with") or ""),
        str(scene.get("action") or ""),
        str(scene.get("continuity") or ""),
        actions,
    ]))


def _strip_article(text: str) -> str:
    return re.sub(r"^(?:the|a|an|his|her|their|its)\s+", "", _flat(text), flags=re.IGNORECASE).strip()


def _container_key(text: str) -> str:
    value = _flat(text)
    value = re.split(r"'s\s+", value, maxsplit=1)[-1]
    return _strip_article(value).lower()


def _planting_details(scene: Dict[str, Any], text: str = "") -> Optional[Dict[str, str]]:
    text = text or _scene_lock_text(scene)
    match = PLANT_RE.search(text)
    if not match:
        return None
    obj = _flat(match.group("obj")).strip(" ,.;")
    container = _flat(match.group("container")).strip(" ,.;")
    container = re.split(r"\s+(?:while|as|before|and then|and|with)\s+", container, maxsplit=1)[0].strip(" ,.;")
    if not obj or not container or len(obj) < 3 or len(container) < 3:
        return None
    if re.search(
        r"\bframe\b|\b(?:front|back|side|top|bottom|middle|center|centre|view|"
        r"sight|place|public|air|light|dark|distance|motion|silence)\b",
        container,
        re.IGNORECASE,
    ):
        return None
    if re.search(r"\b(?:is|was|are|were|be|been)\b", obj, re.IGNORECASE):
        return None
    by = _flat(match.group("by") or "")
    return {
        "object": obj,
        "container": container,
        "container_key": _container_key(container),
        "object_key": _strip_article(obj).lower(),
        "by": by,
    }


def diegetic_text_for_scene(scene: Dict[str, Any]) -> List[str]:
    raw = scene.get("diegetic_text") or scene.get("on_object_text")
    texts: List[str] = []
    if isinstance(raw, str):
        raw = [raw]
    for item in raw or []:
        text = _flat(item).upper()
        if text and text not in texts:
            texts.append(text)
    if not texts:
        key = _flat(extract_key_object(scene)).lower()
        if "confession" in key:
            texts = ["CONFESSION"]
    scene["diegetic_text"] = texts
    scene["on_object_text"] = texts
    return texts


def diegetic_text_clause(scene: Dict[str, Any]) -> str:
    texts = [str(text) for text in (scene.get("diegetic_text") or []) if str(text).strip()]
    if texts:
        joined = ", ".join(f'"{text}"' for text in texts)
        return (
            "DIEGETIC TEXT EXCEPTION: the only legible text allowed is the exact word(s) "
            f"printed on the story object: {joined}. No other text, letters, logos, "
            "watermarks, captions or signage."
        )
    return f"{SCENE_TEXT_SAFE_CLAUSE} {SCENE_TEXT_HIDDEN_CLAUSE}"


def _matches_declared_object(candidate: str, declared: str, master: Dict[str, Any]) -> bool:
    candidate_key = canonicalize_object_name(candidate, master).lower()
    declared_key = canonicalize_object_name(declared, master).lower()
    if not candidate_key or not declared_key:
        return False
    return candidate_key == declared_key


def _apply_object_ledger(scene: Dict[str, Any], ledger: Dict[str, Any], master: Dict[str, Any]) -> None:
    """Lock the scene object to its declared value, never to cut prose.

    ``_planting_details`` may still describe a hidden container for shot
    planning, but it is accepted only when its object matches the object the
    scene itself declares. Its container must also be a concrete noun phrase.
    """
    previous_object = _clean_object_candidate(scene.get("key_object"))
    declared = extract_key_object(scene, master)
    if not declared:
        scene["key_object"] = ""
        scene["object_hidden"] = False
        scene["planted_in"] = ""
        diegetic_text_for_scene(scene)
        return

    bad_container = str(scene.get("planted_in") or "").strip()
    if bad_container and not is_concrete_object_value(bad_container):
        bad_container_re = re.compile(re.escape(bad_container), re.IGNORECASE)
    else:
        bad_container_re = None

    def clean_text(value: Any) -> str:
        cleaned = _scrub_object_prose(value, declared)
        cleaned = _scrub_key_object_clauses(cleaned, declared)
        if bad_container_re is not None:
            cleaned = bad_container_re.sub("a concealed spot", cleaned)
        return cleaned

    present_ids: List[str] = []
    for item in scene.get("characters") or []:
        cid = resolve_speaker(str(item or ""), master) or str(item or "").strip()
        if cid and cid not in present_ids:
            present_ids.append(cid)
    for entry in scene_dialogue_lines(scene):
        cid = resolve_speaker(str(entry.get("speaker") or ""), master) or str(entry.get("speaker") or "").strip()
        if cid and cid not in present_ids:
            present_ids.append(cid)
    for cut in scene.get("internal_cuts") or []:
        if isinstance(cut, dict):
            cut["action"] = _scrub_absent_look_targets(
                clean_text(cut.get("action")), present_ids, master
            )
            cut["framing"] = _scrub_absent_look_targets(
                clean_text(cut.get("framing")), present_ids, master
            )
    for key in (
        "first_frame_prompt",
        "storyboard_panel",
        "action",
        "this_scene_starts_with",
        "continuity",
    ):
        if scene.get(key):
            scene[key] = _scrub_absent_look_targets(
                clean_text(scene[key]), present_ids, master
            )
    text = clean_text(_scene_lock_text(scene))

    details = _planting_details(scene, text)
    if details and not is_concrete_object_value(details["container"]):
        details = None

    if details and _matches_declared_object(details["object"], declared, master):
        container = details["container"]
        scene["planted_object"] = declared
        scene["planted_in"] = container
        scene["planted_by"] = details["by"]
        scene["key_object"] = declared
        scene["object_focus"] = "plant"
        scene["object_hidden"] = False
        scene["object_start"] = {
            "name": container,
            "visible": "hanging open at the edge of frame, its interior out of focus",
        }
        scene["object_end"] = {
            "name": declared,
            "visible": f"inside {container} in a silent insert, placed by {details['by'] or 'the hand'}",
        }
        ledger[details["container_key"]] = {
            "object": declared,
            "object_key": _strip_article(declared).lower(),
            "container": container,
            "hidden": True,
            "revealed": False,
        }
    else:
        if details:
            container = details["container"]
            scene["planted_object"] = declared
            scene["planted_in"] = container
            ledger[details["container_key"]] = {
                "object": details["object"],
                "object_key": details["object_key"],
                "container": container,
                "hidden": True,
                "revealed": False,
            }
        if scene.get("planted_object") and not details:
            scene["planted_object"] = declared
        if not details:
            scene["planted_in"] = ""
        scene["object_hidden"] = False
        if not scene.get("object_focus"):
            scene["object_focus"] = "reveal" if REVEAL_RE.search(text) else ""

    entry: Optional[Dict[str, Any]] = None
    for key, value in ledger.items():
        if not key or not isinstance(value, dict):
            continue
        if _contains_name(text, key) or key.lower() in text.lower():
            entry = value
            break
    if entry:
        container = str(entry.get("container") or "").strip()
        obj = str(entry.get("object") or "").strip()
        obj_key = str(entry.get("object_key") or "").strip().lower()
        reveals = bool(REVEAL_RE.search(text)) and (
            obj_key in text.lower() or _contains_name(text, obj)
        )
        if container:
            scene["planted_in"] = container
        if reveals:
            scene["object_hidden"] = False
            scene["object_focus"] = "reveal"
            entry["hidden"] = False
            entry["revealed"] = True
        else:
            scene["object_hidden"] = True
            if not scene.get("object_focus"):
                scene["object_focus"] = "plant"

    scene["key_object"] = declared
    start = scene.get("object_start") if isinstance(scene.get("object_start"), dict) else {}
    end = scene.get("object_end") if isinstance(scene.get("object_end"), dict) else {}
    start_name = canonicalize_object_name(start.get("name"), master)
    end_name = canonicalize_object_name(end.get("name"), master)
    if not is_concrete_object_value(start_name) or not _matches_declared_object(start_name, declared, master):
        scene["object_start"] = {"name": declared, "visible": "in frame at the start of the scene"}
    else:
        scene["object_start"] = dict(start, name=start_name)
    if not is_concrete_object_value(end_name) or not _matches_declared_object(end_name, declared, master):
        scene["object_end"] = {"name": declared, "visible": "in frame at the end of the scene"}
    else:
        scene["object_end"] = dict(end, name=end_name)

    if previous_object and not is_concrete_object_value(previous_object):
        for cut in scene.get("internal_cuts") or []:
            if isinstance(cut, dict):
                cut["action"] = _replace_object_reference(cut.get("action"), previous_object, declared)
                cut["framing"] = _replace_object_reference(cut.get("framing"), previous_object, declared)
        for key in ("first_frame_prompt", "storyboard_panel", "action"):
            if scene.get(key):
                scene[key] = _replace_object_reference(scene[key], previous_object, declared)
    diegetic_text_for_scene(scene)


def _dialogue_end_seconds(scene: Dict[str, Any]) -> float:
    cuts = [c for c in (scene.get("internal_cuts") or []) if isinstance(c, dict)]
    lines = scene_dialogue_lines(scene)
    total = 0.0
    for cut in cuts:
        indexes = [int(i) for i in (cut.get("line_indexes") or [])]
        if not indexes:
            continue
        speech = 0.0
        for i in indexes:
            if 0 <= i < len(lines):
                speech += len(re.findall(r"\b[\w'-]+\b", lines[i]["line"])) / SPEECH_WORDS_PER_SECOND
        end = float(cut.get("at") or 0.0) + 0.2 + speech + SPEECH_GAP_SECONDS * max(0, len(indexes) - 1)
        total = max(total, end)
    return round(min(SCENE_SECONDS, total), 1)


def build_scene_first_frame_prompt(
    scene: Dict[str, Any],
    master: Dict[str, Any],
    style: Optional[Dict[str, Any]] = None,
) -> str:
    style = style if isinstance(style, dict) else load_style_locks()
    cuts = [c for c in (scene.get("internal_cuts") or []) if isinstance(c, dict)]
    first = cuts[0] if cuts else {}
    names = [
        _display_name(str(cid), master)
        for cid in (scene.get("characters_present") or [])[:MAX_SCENE_CAST]
    ]
    subject = ", ".join(name for name in names if name) or "the scene"
    location = _flat(scene.get("location") or "the scene location")
    action = _cut_action(first) or "the scene opens already in motion"
    object_name = str((scene.get("object_start") or {}).get("name") or extract_key_object(scene) or "").strip()
    if not object_name:
        object_clause = " Key object in frame: the scene central prop."
    elif re.search(r"key object in frame", action, re.IGNORECASE):
        object_clause = ""
    else:
        object_clause = f" Key object in frame: {object_name}."
    anchors = str(scene.get("character_anchors") or format_character_anchors(
        scene, master.get("characters_locked") or master.get("characters") or []
    )).strip()
    suffix = _flat((style.get("visual_style_lock") or {}).get("image_prompt_suffix") or "")
    suffix = re.sub(r"No text[^.]*\.", "", suffix).strip()
    clause = diegetic_text_clause(scene)
    return _flat(
        f"Cinematic still of {subject}, {first.get('framing') or 'medium shot'}, at {location}. "
        f"{action.rstrip(' .')}.{object_clause} "
        f"Identity anchors: {anchors or 'use the reference sheets exactly as attached'}. "
        f"{suffix} {clause} Keep the first frame exactly the same framing as Shot 1."
    )


def _first_frame_prompt_needs_repair(
    scene: Dict[str, Any],
    master: Dict[str, Any],
    orig_first: Optional[tuple],
) -> bool:
    prompt = _flat(scene.get("first_frame_prompt") or "").lower()
    if not prompt:
        return True
    cuts = [c for c in (scene.get("internal_cuts") or []) if isinstance(c, dict)]
    new_first = (_flat((cuts[0] if cuts else {}).get("framing")), _cut_action(cuts[0] if cuts else {}))
    if orig_first and (tuple(orig_first) != new_first):
        return True
    object_name = str((scene.get("object_start") or {}).get("name") or extract_key_object(scene) or "").strip()
    if object_name and object_name.lower() not in prompt:
        return True
    for cid in (scene.get("characters_present") or [])[:MAX_SCENE_CAST]:
        name = _display_name(str(cid), master).lower()
        if name and name not in prompt:
            return True
    return False


def prepare_scene_locks(
    scene: Dict[str, Any],
    master: Dict[str, Any],
    previous: Optional[Dict[str, Any]] = None,
    ledger: Optional[Dict[str, Any]] = None,
    style: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Derive contract v2 in memory (does not rewrite the project on disk)."""
    prepared = copy.deepcopy(scene)
    ledger = ledger if isinstance(ledger, dict) else {}
    prepared["dialogue"] = _coerce_dialogue(prepared.get("dialogue"))
    prepared["key_object"] = extract_key_object(prepared)
    _apply_object_ledger(prepared, ledger, master)
    cuts_before = [c for c in (prepared.get("internal_cuts") or []) if isinstance(c, dict)]
    orig_first = (
        _flat((cuts_before[0] if cuts_before else {}).get("framing")),
        _cut_action(cuts_before[0] if cuts_before else {}),
    )
    prepared["internal_cuts"] = _plan_scene_shots(prepared, master)
    present = scene_characters_present(prepared, master)
    prepared["characters_present"] = present
    speakers: List[str] = []
    for entry in scene_dialogue_lines(prepared):
        cid = resolve_speaker(entry.get("speaker") or "", master) or str(entry.get("speaker") or "").strip()
        if cid and cid not in speakers:
            speakers.append(cid)
    prepared["present_silent"] = [cid for cid in present if cid not in speakers]
    prepared["shot_lock_version"] = "2"
    prepared["character_anchors"] = format_character_anchors(
        prepared, master.get("characters_locked") or master.get("characters") or []
    )
    _ensure_key_object_in_first_cut(prepared)
    prepared["storyboard_panel"] = build_storyboard_panel_description(prepared, master)
    prepared["dialogue_end_seconds"] = _dialogue_end_seconds(prepared)
    _apply_dialogue_shots(prepared, master)
    repaired = False
    if _first_frame_prompt_needs_repair(prepared, master, orig_first):
        prepared["first_frame_prompt"] = build_scene_first_frame_prompt(prepared, master, style)
        repaired = True
    cuts_after = [c for c in (prepared.get("internal_cuts") or []) if isinstance(c, dict)]
    new_first = (
        _flat((cuts_after[0] if cuts_after else {}).get("framing")),
        _cut_action(cuts_after[0] if cuts_after else {}),
    )
    prepared["frame_regeneration_required"] = bool(repaired or (orig_first != new_first))
    return prepared


def prepare_master_locks(
    master: Dict[str, Any],
    style: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Copy of the master with all scenes prepared for contract v2."""
    if not isinstance(master, dict):
        raise NFError("prepare_master_locks expects a master JSON.")
    style = style if isinstance(style, dict) else load_style_locks()
    prepared = dict(master)
    ledger: Dict[str, Any] = {}
    scenes: List[Dict[str, Any]] = []
    previous: Optional[Dict[str, Any]] = None
    for scene in ordered_scenes(master):
        current = prepare_scene_locks(scene, master, previous=previous, ledger=ledger, style=style)
        scenes.append(current)
        previous = current
    prepared["scenes"] = scenes
    prepared["shot_lock_version"] = "2"
    return prepared


def prepare_master_locks_safe(
    master: Dict[str, Any],
    style: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """``prepare_master_locks`` only when contract v2 applies; legacy masters untouched."""
    if not isinstance(master, dict):
        return master
    if str(master.get("shot_lock_version") or "") == "2":
        return master
    if not _should_apply_v2(master):
        return master
    return prepare_master_locks(master, style)


def scene_shot_rows(scene: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for cut in scene.get("internal_cuts") or []:
        if not isinstance(cut, dict):
            continue
        rows.append({
            "range": str(cut.get("range") or ""),
            "at": float(cut.get("at") or 0.0),
            "framing": str(cut.get("framing") or "").strip(),
            "action": str(cut.get("action") or "").strip(),
            "dialogue": bool(cut.get("dialogue")),
            "silent": bool(cut.get("silent")),
            "kind": str(cut.get("kind") or "").strip(),
            "speakers": [str(s) for s in (cut.get("speakers") or [])],
            "line_indexes": [int(i) for i in (cut.get("line_indexes") or [])],
        })
    return rows


def scene_present_silent_names(scene: Dict[str, Any], master: Dict[str, Any]) -> List[str]:
    return [_display_name(str(cid), master) for cid in (scene.get("present_silent") or []) if str(cid).strip()]


def scene_speaker_names(scene: Dict[str, Any], master: Dict[str, Any]) -> List[str]:
    names: List[str] = []
    for entry in scene_dialogue_lines(scene):
        cid = resolve_speaker(entry.get("speaker") or "", master) or str(entry.get("speaker") or "").strip()
        name = _display_name(cid, master) if cid else ""
        if name and name not in names:
            names.append(name)
    return names


def _cut_action(cut: Dict[str, Any]) -> str:
    return re.sub(r"\s+", " ", str((cut or {}).get("action") or "")).strip().rstrip(".")


def _ensure_key_object_in_first_cut(scene: Dict[str, Any]) -> None:
    """Rule 4: the exact key_object name also lives in Shot 1."""
    key_object = str((scene.get("object_start") or {}).get("name") or "").strip() or extract_key_object(scene)
    cuts = scene.get("internal_cuts") or []
    if not key_object or not isinstance(cuts, list) or not cuts or not isinstance(cuts[0], dict):
        return
    action = re.sub(r"\s*Key object in frame:[^.]*\.", "", str(cuts[0].get("action") or "")).strip()
    if key_object.lower() not in action.lower():
        action = f"{action.rstrip(' .')}. Key object in frame: {key_object}."
    cuts[0]["action"] = action


def _coerce_narrative_continuity(
    scene: Dict[str, Any],
    previous: Optional[Dict[str, Any]],
) -> None:
    """Fill a scene's causal chain when the LLM did not provide it.

    ``because_previous_ended_with`` is ALWAYS anchored to the state change of the
    previous scene so the chain is verifiable and not a paraphrase.
    """
    first_action = _cut_action((scene.get("internal_cuts") or [{}])[0])
    last_action = _cut_action((scene.get("internal_cuts") or [{}])[-1])
    previous_change = _cut_action((previous.get("internal_cuts") or [{}])[-1]) if previous else ""
    previous_change = str((previous or {}).get("single_change_at_end") or previous_change).strip()

    if previous:
        because = previous_change or "the previous beat left the conflict unresolved"
    else:
        because = "The episode opens cold; there is no prior beat."
    beat = re.sub(r"^the\s+", "", str(scene.get("beat") or "beat").replace("_", " ").strip(), flags=re.IGNORECASE)
    key_object = extract_key_object(scene) or "the evidence"
    synthesized_change = f"The {beat} leaves {key_object} exposed, and there is no way back."
    started = str(scene.get("this_scene_starts_with") or "").strip()
    if not started or is_placeholder_text(started) or CAMERA_NOTE_RE.search(started):
        started = (
            first_action
            if first_action and not CAMERA_NOTE_RE.search(first_action)
            else f"The {beat} opens with {key_object} already in play."
        )
    changed = str(scene.get("single_change_at_end") or "").strip()
    if (
        not changed
        or is_placeholder_text(changed)
        or CAMERA_NOTE_RE.search(changed)
        or re.match(r"^the\s+the\b", changed, re.IGNORECASE)
        or re.sub(r"\s+", " ", changed).strip().rstrip(".") == last_action
    ):
        changed = synthesized_change

    entry_bridge = str(scene.get("entry_bridge") or "").strip()
    exit_hook = str(scene.get("exit_hook") or "").strip()

    if previous:
        prev_exit = str(previous.get("exit_hook") or "").strip()
        if not prev_exit:
            prev_exit = f"a command to resolve {key_object}"
        if not entry_bridge or is_placeholder_text(entry_bridge):
            entry_bridge = f"Following {prev_exit.rstrip('.').lower()}, action begins without pause around {key_object}."
    else:
        if not entry_bridge or is_placeholder_text(entry_bridge):
            entry_bridge = f"The story opens cold as {started.rstrip('.').lower()}."

    if not exit_hook or is_placeholder_text(exit_hook):
        exit_hook = f"A sharp ultimatum leaves {key_object} contested, forcing an urgent response."

    scene["because_previous_ended_with"] = because
    scene["this_scene_starts_with"] = started
    scene["single_change_at_end"] = changed
    scene["entry_bridge"] = entry_bridge
    scene["exit_hook"] = exit_hook


def _auto_block_question(
    group: Sequence[Dict[str, Any]],
    protagonist: str,
    block_number: int,
) -> str:
    first = group[0] if group else {}
    beat = str(first.get("beat") or "new complication").replace("_", " ")
    key_object = extract_key_object(first) or "the evidence"
    first_id = int(first.get("scene_id") or 1)
    last_id = int((group[-1] if group else first).get("scene_id") or first_id)
    return (
        f"How does {protagonist} turn the {beat} around {key_object} "
        f"in scenes {first_id}-{last_id}?"
    )


def build_narrative_continuity(
    master: Dict[str, Any],
    rules: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Build the project's N one-minute blocks with their single driving question."""
    rules = rules if isinstance(rules, dict) else load_showrunner()
    engine = rules.get("narrative_continuity_engine") or {}
    if not engine or not engine.get("enabled", True):
        return {}
    scenes = ordered_scenes(master)
    per_block = int(engine.get("scenes_per_block") or SCENES_PER_BLOCK)
    total_blocks = (len(scenes) + per_block - 1) // per_block if scenes else 0
    characters = [c for c in (master.get("characters") or []) if isinstance(c, dict)]
    protagonist = next(
        (str(c.get("name") or c.get("id") or "") for c in characters if str(c.get("role") or "") == "protagonist"),
        "",
    )
    if not protagonist and characters:
        protagonist = str(characters[0].get("name") or characters[0].get("id") or "the protagonist")
    protagonist = protagonist or "the protagonist"

    blocks: List[Dict[str, Any]] = []
    for block_number in range(1, total_blocks + 1):
        group = scenes[(block_number - 1) * per_block:block_number * per_block]
        if not group:
            continue
        question = ""
        for scene in group:
            question = str(scene.get("block_driving_question") or "").strip()
            if question:
                break
        if not question:
            question = _auto_block_question(group, protagonist, block_number)
        default_cliffhanger = DEFAULT_CLIFFHANGER_ROTATION[(block_number - 1) % len(DEFAULT_CLIFFHANGER_ROTATION)]
        cliffhanger_type = ""
        for scene in reversed(group):
            ct = str(scene.get("cliffhanger_type") or "").strip().lower()
            if ct:
                cliffhanger_type = ct
                break
        blocks.append({
            "block": block_number,
            "scenes": [int(scene.get("scene_id") or 0) for scene in group],
            "driving_question": question,
            "cliffhanger_type": cliffhanger_type or default_cliffhanger,
        })
    return {
        "schema_version": int(engine.get("schema_version") or 1),
        "engine": "narrative_continuity_engine",
        "scene_count": len(scenes),
        "total_blocks": len(blocks),
        "minute_blocks": blocks,
    }


def _normalize_teasers(
    payload: Dict[str, Any],
    scenes: List[Dict[str, Any]],
    warnings: List[str],
    scene_count: Optional[int] = None,
) -> List[Dict[str, Any]]:
    ranges = default_teaser_ranges(scene_count)
    defaults = [
        {"id": 1, "title": "Official Teaser", "scenes": ranges[0]},
        {"id": 2, "title": "The Twist", "scenes": ranges[1]},
        {"id": 3, "title": "The Cliffhanger", "scenes": ranges[2]},
    ]
    provided = payload.get("teasers")
    teasers: List[Dict[str, Any]] = []
    if isinstance(provided, list) and provided:
        for idx, item in enumerate(provided[:3]):
            base = dict(defaults[idx])
            if isinstance(item, dict):
                base.update(item)
            ids: List[int] = []
            for sid in base.get("scenes") or []:
                try:
                    val = int(sid)
                except (TypeError, ValueError):
                    continue
                if 1 <= val <= int(scene_count or SCENE_COUNT) and val not in ids:
                    ids.append(val)
            if len(ids) < 4:
                warnings.append(f"Teaser {idx + 1} has fewer than 4 valid scenes; filled with the default range.")
                for sid in defaults[idx]["scenes"]:
                    if sid not in ids:
                        ids.append(sid)
            base["scenes"] = ids[:6]
            base["id"] = idx + 1
            teasers.append(base)
    if len(teasers) < 3:
        existing = {t["id"] for t in teasers}
        for base in defaults:
            if base["id"] not in existing:
                teasers.append(dict(base))
                warnings.append(f"Teaser {base['id']} missing: generated with scenes {base['scenes'][0]}-{base['scenes'][-1]}.")
    # Fill in teaser hook/caption
    by_id = {int(s.get("scene_id") or 0): s for s in scenes}
    hook_default = str((payload.get("episode") or {}).get("hook_line") or "").strip()
    for t in teasers:
        if not str(t.get("hook_text") or "").strip():
            first = by_id.get(t["scenes"][0], {})
            t["hook_text"] = str(first.get("on_screen_hook") or hook_default or f"Episode {t['id']}").strip()
        if not str(t.get("caption") or "").strip():
            t["caption"] = str(t.get("hook_text") or "").strip()
    teasers.sort(key=lambda t: t["id"])
    return teasers


def _should_apply_v2(master: Dict[str, Any]) -> bool:
    """Only when there is a cast and at least one resolvable speaker (does not break fixtures)."""
    if not isinstance(master.get("characters"), list) or not master.get("characters"):
        return False
    for scene in master.get("scenes") or []:
        if not isinstance(scene, dict):
            continue
        for entry in scene_dialogue_lines(scene):
            if resolve_speaker(entry.get("speaker") or "", master):
                return True
    return False


def normalize_master(
    payload: Any,
    slug: str,
    title: str = "",
    repair: bool = True,
    allow_partial: bool = False,
    target_minutes: Optional[int] = None,
) -> Tuple[Dict[str, Any], List[str]]:
    """Bring the LLM response (or an existing master) into the canonical schema.

    Tolerant of common formats: scene list, 'data' wrappers,
    Markdown fences, dialogue as a string, cuts as a list of strings.
    Returns (master, warnings). Structural errors raise NFError.
    """
    warnings: List[str] = []
    if isinstance(payload, list):
        payload = {"scenes": payload}
    if not isinstance(payload, dict):
        raise NFError("The input is not a JSON object or a scene list.")
    for key in ("episode_json", "data", "result", "output", "master_episode"):
        inner = payload.get(key)
        if isinstance(inner, dict) and isinstance(inner.get("scenes"), list):
            payload = inner
            warnings.append(f"Unwrapped container key '{key}'.")
            break

    rules = load_showrunner()
    ep_in = payload.get("episode") if isinstance(payload.get("episode"), dict) else {}
    declared_target = target_minutes
    if declared_target in (None, ""):
        for key in ("target_minutes", "total_blocks", "minute_blocks", "blocks"):
            if ep_in.get(key) not in (None, ""):
                declared_target = ep_in.get(key)
                break
    if declared_target in (None, ""):
        for key in ("target_minutes", "total_blocks", "minute_blocks", "blocks"):
            if payload.get(key) not in (None, ""):
                declared_target = payload.get(key)
                break
    if declared_target in (None, "") and ep_in.get("total_scenes") not in (None, ""):
        declared_target = target_minutes_for_scene_count(ep_in.get("total_scenes"), rules) or None
    if declared_target in (None, ""):
        declared_target = LEGACY_TARGET_MINUTES
    target = resolve_target_minutes(declared_target)
    expected_scenes = scene_count_for_target(target, rules)

    raw_scenes = payload.get("scenes")
    if not isinstance(raw_scenes, list) or not raw_scenes:
        raise NFError("The JSON does not contain a 'scenes' list with the project scenes.")
    if len(raw_scenes) != expected_scenes:
        if not allow_partial:
            raise NFError(
                f"The JSON has {len(raw_scenes)} scenes and the project declares {target} min "
                f"({expected_scenes} scenes). Ask the LLM to regenerate the complete script "
                "(or split the work by acts and merge them)."
            )
        warnings.append(
            f"Partial mode: {len(raw_scenes)} of {expected_scenes} scenes "
            f"({target} min planned; not publishable yet)."
        )
    if not all(isinstance(s, dict) for s in raw_scenes):
        raise NFError("All 'scenes' entries must be JSON objects.")

    style = load_style_locks()
    rotation = ((style.get("visual_style_lock") or {}).get("default_shot_rotation") or DEFAULT_SHOT_ROTATION)
    required_beats = required_beats_for_scene_count(expected_scenes, rules)
    ep: Dict[str, Any] = dict(ep_in)
    ep.setdefault("slug", slugify(slug))
    ep.setdefault("title", title or str(ep.get("series_title") or "").strip() or slug.replace("_", " ").title())
    ep.setdefault("series_title", ep["title"])
    ep.setdefault("episode_number", 1)
    ep.setdefault("logline", "")
    ep.setdefault("genre", "romantic suspense short-drama")
    ep.setdefault("language", "en-US")
    ep.setdefault("audience", "US women 25-55, short-drama and audio-series viewers")
    ep.setdefault("tone", "cinematic, intimate, high-stakes, fast-paced")
    ep.setdefault("hook_line", "")
    ep["target_minutes"] = target
    ep["total_blocks"] = target
    ep["total_scenes"] = expected_scenes
    ep["scene_seconds"] = int(scene_seconds(rules))
    ep["total_seconds"] = int(expected_scenes * scene_seconds(rules))
    ep["aspect_master"] = "16:9"
    ep["aspect_teaser"] = "9:16"
    if not str(ep.get("logline") or "").strip():
        warnings.append("episode.logline is empty: a 1-2 line sentence is recommended for the publishing pack.")

    cast_ctx = {"characters": payload.get("characters") or []}
    cast_index = canonical_cast(cast_ctx)

    scenes: List[Dict[str, Any]] = []
    for idx, raw in enumerate(raw_scenes, start=1):
        scene = dict(raw)
        original_id = scene.get("scene_id")
        sid = idx
        if original_id not in (None, ""):
            try:
                sid = int(original_id)
            except (TypeError, ValueError):
                warnings.append(f"non-numeric scene_id ({original_id!r}); using {idx}.")
                sid = idx
        scene["scene_id"] = sid
        scene["duration_s"] = float(scene.get("duration_s") or SCENE_SECONDS)
        try:
            act = int(scene.get("act") or 0)
        except (TypeError, ValueError):
            act = 0
        act_count = len(rules.get("acts") or []) or 6
        scene["act"] = act if 1 <= act <= act_count else (
            ((max(1, sid) - 1) * act_count) // expected_scenes + 1
        )
        scene["act"] = min(act_count, scene["act"])
        scene["beat"] = str(scene.get("beat") or required_beats.get(sid) or "").strip()
        scene["dialogue"] = _coerce_dialogue(scene.get("dialogue"))
        scene["internal_cuts"] = _coerce_cuts(
            scene.get("internal_cuts"),
            rotation,
            scene=scene,
            cast_index=cast_index,
        )
        scene["first_frame_prompt"] = str(
            scene.get("first_frame_prompt") or scene.get("image_prompt") or scene.get("frame_prompt") or ""
        ).strip()
        scene["sfx_ambience"] = str(scene.get("sfx_ambience") or scene.get("ambience") or "").strip()
        raw_continuity = str(scene.get("continuity") or "").strip()
        present, future = strip_future_refs(raw_continuity)
        scene["continuity"] = raw_continuity
        scene["continuity_present"] = present
        scene["continuity_future_refs"] = future
        scene["on_screen_hook"] = str(scene.get("on_screen_hook") or "").strip()
        raw_chars = scene.get("characters")
        if isinstance(raw_chars, str):
            raw_chars = [raw_chars]
        normalized_chars: List[str] = []
        for item in raw_chars or []:
            text = str(item or "").strip()
            if not text:
                continue
            key = text.lower()
            character = (
                cast_index.get(key)
                or cast_index.get(re.sub(r"[^a-z0-9]+", " ", key).strip())
                or cast_index.get(re.sub(r"[^a-z0-9]+", "_", key).strip("_"))
                or cast_index.get(key.split()[0] if key.split() else key)
            )
            cid = str((character or {}).get("id") or (character or {}).get("name") or text)
            if cid not in normalized_chars:
                normalized_chars.append(cid)
        scene["characters"] = normalized_chars
        scene["key_object"] = extract_key_object(scene)
        _ensure_key_object_in_first_cut(scene)
        _coerce_narrative_continuity(scene, scenes[-1] if scenes else None)
        scene["characters_present"] = scene_characters_present(scene, cast_ctx)
        if not scene["first_frame_prompt"]:
            warnings.append(f"Scene {sid}: empty first_frame_prompt (the frame cannot be generated).")
        if not scene["dialogue"]:
            warnings.append(f"Scene {sid}: no dialogue (10 s of silence).")
        if future:
            warnings.append(f"Scene {sid}: continuity has future references ({len(future)}); sanitized in the video prompt.")
        scenes.append(scene)

    master: Dict[str, Any] = dict(payload)
    master["schema_version"] = str(master.get("schema_version") or "1.0")
    master["generated_by"] = str(master.get("generated_by") or "novel_factory")
    master.setdefault("generated_at", now_iso())
    master["episode"] = ep
    master["characters"] = master.get("characters") if isinstance(master.get("characters"), list) else []
    master["locations"] = master.get("locations") if isinstance(master.get("locations"), list) else []
    master["acts"] = master.get("acts") if isinstance(master.get("acts"), list) else []
    master["characters_locked"] = (
        master.get("characters_locked")
        if isinstance(master.get("characters_locked"), list) and master.get("characters_locked")
        else master["characters"]
    )
    master["scenes"] = scenes
    if _should_apply_v2(master):
        try:
            prepared_master = prepare_master_locks(master, style)
            master["scenes"] = prepared_master["scenes"]
            master["shot_lock_version"] = "2"
            scenes = master["scenes"]
        except NFError as exc:
            warnings.append(f"Contrato v2 no aplicado: {exc}")
    for scene in scenes:
        scene["character_anchors"] = format_character_anchors(scene, master["characters_locked"])
        scene["storyboard_panel"] = build_storyboard_panel_description(scene, master)
    master["partial"] = len(scenes) != expected_scenes
    master["teasers"] = _normalize_teasers(payload, scenes, warnings, expected_scenes)
    master["narrative_continuity"] = build_narrative_continuity(master, rules)

    # TAREA A: Modo fuente probada (proven_adaptation vs original_unproven)
    source_script = str(payload.get("source_script") or payload.get("source_text") or "").strip()
    source_mode = str(payload.get("source_mode") or "").strip()
    if not source_mode:
        source_mode = "proven_adaptation" if source_script else "original_unproven"
    elif source_mode == "proven_adaptation" and not source_script:
        source_mode = "original_unproven"

    master["source_mode"] = source_mode
    if source_script:
        master["source_script"] = source_script

    if source_mode == "original_unproven":
        warnings.append(
            "source_mode: 'original_unproven' — script generated without a proven source (source_script). "
            "ReelShort/DramaBox require adapting proven stories to guarantee retention."
        )

    pub = dict(master.get("publisher") or {}) if isinstance(master.get("publisher"), dict) else {}
    pub.setdefault("personaje_id", "emma_hayes")
    pub.setdefault("cta", "Follow for Episode 2.")
    pub.setdefault("hashtags", ["#shortdrama", "#novel", "#storytime", "#drama", "#episode1"])
    pub.setdefault("ai_disclosure", True)
    master["publisher"] = pub

    master["soundtrack"] = master.get("soundtrack") if isinstance(master.get("soundtrack"), dict) else {
        "mood": "tense coastal romantic suspense",
        "bpm": 78,
        "notes": "Leave dialogue forward; music will be mixed in post at low volume.",
    }

    if repair:
        master = _fill_default_prompts(master, style)
    return master, warnings


def _fill_default_prompts(master: Dict[str, Any], style: Dict[str, Any]) -> Dict[str, Any]:
    """Fill empty prompts with a cinematic template (repair only)."""
    look = (style.get("visual_style_lock") or {})
    suffix = str(look.get("image_prompt_suffix") or "").strip()
    for scene in master["scenes"]:
        if not scene.get("first_frame_prompt"):
            loc = str(scene.get("location") or "a windswept coastal town at dusk")
            shot = str((scene.get("internal_cuts") or [{}])[0].get("framing") or "medium shot")
            who = str(scene.get("characters")[0] if isinstance(scene.get("characters"), list) and scene.get("characters") else "the protagonist")
            scene["first_frame_prompt"] = (
                f"Cinematic still of {who}, {shot}, at {loc}. "
                f"Dramatic natural lighting, detailed environment, expressive eyes, "
                f"prestige short-drama production still. {suffix}"
            ).strip()
    return master


def _cut_end_seconds(cuts: Sequence[Dict[str, Any]], index: int) -> float:
    if index + 1 < len(cuts):
        return float(cuts[index + 1].get("at") or SCENE_SECONDS)
    return SCENE_SECONDS


def _validate_scene_v2(
    scene: Dict[str, Any],
    master: Dict[str, Any],
    sid: int,
    strict: Any,
) -> None:
    """Contract v2 rules: speaker per shot, mute list, object and text."""
    cuts = [c for c in (scene.get("internal_cuts") or []) if isinstance(c, dict)]
    lines = scene_dialogue_lines(scene)
    present = [str(cid) for cid in (scene.get("characters_present") or [])]
    if len(present) > MAX_SCENE_CAST:
        strict(f"Scene {sid}: {len(present)} characters in scene; the prompt maximum is {MAX_SCENE_CAST}.")
    if len(lines) > MAX_DIALOGUE_LINES_PER_SCENE:
        strict(f"Scene {sid}: {len(lines)} dialogue lines; the per-clip maximum is {MAX_DIALOGUE_LINES_PER_SCENE}.")
    if not lines and any(cut.get("dialogue") for cut in cuts):
        strict(f"Scene {sid}: a shot is marked as dialogue but has no lines.")
    speakers: List[str] = []
    for entry in lines:
        cid = resolve_speaker(entry.get("speaker") or "", master) or str(entry.get("speaker") or "").strip()
        if cid and cid not in speakers:
            speakers.append(cid)
    for index, entry in enumerate(lines):
        shot = int(entry.get("shot") or 0)
        if not 1 <= shot <= len(cuts):
            strict(f"Scene {sid}: line {index + 1} has no assigned shot.")
            continue
        cut = cuts[shot - 1]
        if not cut.get("dialogue"):
            strict(f"Scene {sid}: line {index + 1} falls on a shot marked as silence.")
        if not face_visible_in_cut(cut):
            strict(f"Scene {sid}: line {index + 1} falls on a shot without a visible face and mouth.")
        speaker = entry.get("speaker") or ""
        if not speaker:
            strict(f"Scene {sid}: line {index + 1} has no speaker.")
        else:
            ownership = line_ownership_error(entry.get("line") or "", speaker, master)
            if ownership:
                strict(f"Scene {sid}: {ownership}")
            if not _cut_mentions(cut, speaker, master):
                strict(f"Scene {sid}: the shot for line {index + 1} does not name the speaker '{speaker}'.")
            others = [
                cid for cid in (scene.get("characters_present") or [])
                if not _same_character(str(cid), speaker, master)
            ]
            recipient = str(entry.get("recipient") or "").strip()
            if recipient and _same_character(recipient, speaker, master):
                strict(f"Scene {sid}: line {index + 1} speaks to itself.")
            elif recipient and not any(
                _same_character(recipient, str(cid), master) for cid in others
            ):
                strict(
                    f"Scene {sid}: line {index + 1} looks at '{recipient}', who is not in the scene."
                )
            elif not recipient and others:
                strict(f"Scene {sid}: line {index + 1} has no recipient.")
    shots = [int(entry.get("shot") or 0) for entry in lines]
    if shots != sorted(shots):
        strict(f"Scene {sid}: lines are not in appearance order ({shots}).")
    seen: List[str] = []
    for entry in lines:
        flat = re.sub(r"[^a-z0-9 ]", "", str(entry.get("line") or "").lower()).strip()
        if flat and flat in seen:
            strict(f"Scene {sid}: a line appears more than once in the scene.")
        seen.append(flat)
    for cid in scene.get("present_silent") or []:
        if any(_same_character(str(cid), speaker, master) for speaker in speakers):
            strict(f"Scene {sid}: '{cid}' is in the silent list and also speaks.")
    for cut in cuts:
        if cut.get("dialogue"):
            continue
        action = str(cut.get("action") or "")
        if re.search(r'"[^"]+"', action) or SPEAKING_VERB_RE.search(action):
            strict(f"Scene {sid}: a silent shot contains dialogue or a speaking action.")
    start = scene.get("object_start") or {}
    end = scene.get("object_end") or {}
    if not str(start.get("name") or "").strip():
        strict(f"Scene {sid}: missing the OBJECT AT START block.")
    if not str(end.get("name") or "").strip():
        strict(f"Scene {sid}: missing the OBJECT AT END block.")
    if str(scene.get("object_focus") or "") == "reveal":
        obj = str(end.get("name") or start.get("name") or "").strip()
        focus_cut = None
        for index, cut in enumerate(cuts):
            if cut.get("dialogue"):
                continue
            text = _cut_text(cut)
            if cut.get("kind") == "object" or (obj and (obj.lower() in text.lower() or _contains_name(text, obj))):
                focus_cut = (index, cut)
                break
        if focus_cut is None:
            strict(f"Scene {sid}: the reveal of '{obj}' has no dedicated shot without dialogue.")
        else:
            index, _cut = focus_cut
            duration = _cut_end_seconds(cuts, index) - float(cuts[index].get("at") or 0.0)
            if duration < OBJECT_FOCUS_MIN_SECONDS - 0.05:
                strict(
                    f"Scene {sid}: the reveal shot lasts {duration:.1f}s; "
                    f"minimum {OBJECT_FOCUS_MIN_SECONDS:.1f}s."
                )
    if scene.get("object_hidden"):
        for cut in cuts:
            text = _cut_text(cut).lower()
            if re.search(r"\b(?:empty|interior|leather tools|inside the bag)\b", text):
                if "out of frame" not in text and "shadow" not in text:
                    strict(f"Scene {sid}: a shot shows the interior or absence of a hidden object.")
    for text in scene.get("diegetic_text") or []:
        if str(text) != str(text).upper():
            strict(f"Scene {sid}: diegetic text '{text}' must use exact uppercase.")


def validate_master(
    master: Dict[str, Any],
    allow_partial: bool = False,
    production: bool = False,
) -> Dict[str, List[str]]:
    """Semantic/structural validation. Returns {'errors': [...], 'warnings': [...]}.

    With ``production=True``, content findings (cast, speakers, speech budget,
    future continuity, location taxonomy) move from warning to error. In normal
    mode they remain warnings so existing fixtures are not broken.
    """
    errors: List[str] = []
    warnings: List[str] = []

    def strict(msg: str) -> None:
        (errors if production else warnings).append(msg)

    if master.get("source_mode") == "original_unproven":
        warnings.append(
            "source_mode: 'original_unproven' — Unproven script. Missing 'source_script'."
        )

    ep = episode_meta(master)
    scenes = [s for s in (master.get("scenes") or []) if isinstance(s, dict)]
    expected_scenes = master_scene_count(master)

    if not ep.get("slug"):
        errors.append("episode.slug ausente.")
    if not str(ep.get("title") or "").strip():
        errors.append("episode.title ausente.")
    if not allow_partial and len(scenes) != expected_scenes:
        errors.append(f"Expected {expected_scenes} scenes but found {len(scenes)}.")
    if production and master.get("partial") and not allow_partial:
        errors.append(
            f"The master is partial (<{expected_scenes} scenes): not publishable."
        )
    ids = [int(s.get("scene_id") or 0) for s in scenes]
    if len(set(ids)) != len(ids):
        errors.append("scene_id duplicado.")
    if not allow_partial and ids != list(range(1, expected_scenes + 1)):
        errors.append("scene_id must be 1..N with no gaps or duplicates.")
    elif allow_partial and ids != sorted(ids):
        warnings.append("Partial IDs are out of order: sort them before merging.")

    rules = load_showrunner()
    engine = rules.get("narrative_continuity_engine") or {}
    engine_rules = engine.get("rules") or {}
    chain_rule = engine_rules.get("2_strict_cause_and_effect_chain") or {}
    fmt = rules.get("format") or {}
    wps = float(fmt.get("speech_words_per_second") or SPEECH_WORDS_PER_SECOND)
    max_scene_words = int(fmt.get("max_scene_words") or MAX_SCENE_WORDS)
    max_line_words = int(fmt.get("max_line_words") or MAX_LINE_WORDS)
    min_scene_words = int(fmt.get("min_scene_words") or MIN_SCENE_WORDS)
    scene_seconds = float(fmt.get("scene_seconds") or SCENE_SECONDS)

    prompts = 0
    silent = 0
    unknown_chars: set[tuple[int, str]] = set()
    unknown_speakers: set[tuple[int, str]] = set()
    for scene in scenes:
        sid = int(scene.get("scene_id") or 0)
        if not 1 <= int(scene.get("act") or 0) <= 6:
            errors.append(f"Scene {sid}: invalid act.")
        prompt = str(scene.get("first_frame_prompt") or "")
        if len(prompt) < 60:
            errors.append(f"Scene {sid}: first_frame_prompt too short ({len(prompt)} chars).")
        else:
            prompts += 1
        cuts = scene.get("internal_cuts")
        v2_scene = str(scene.get("shot_lock_version") or "") == "2" or production
        if not isinstance(cuts, list) or not (1 <= len(cuts) <= MAX_CUTS_PER_SCENE):
            errors.append(
                f"Scene {sid}: between 1 and {MAX_CUTS_PER_SCENE} shots are required; found "
                f"{len(cuts) if isinstance(cuts, list) else 0}."
            )
        else:
            ats = [float(c.get("at") or 0.0) for c in cuts]
            if abs(ats[0]) > 1e-6:
                errors.append(f"Scene {sid}: the first shot must start at 0.0 s.")
            if any(b <= a for a, b in zip(ats, ats[1:])):
                errors.append(f"Scene {sid}: cuts must be increasing ({ats}).")
            if ats[-1] >= scene_seconds:
                errors.append(f"Scene {sid}: the last cut {ats[-1]} must fall before {scene_seconds} s.")
            for cut_no, cut in enumerate(cuts, start=1):
                if not str((cut or {}).get("action") or "").strip():
                    errors.append(f"Scene {sid}: Shot {cut_no} has no action.")
                if is_placeholder_text(str((cut or {}).get("action") or "")):
                    errors.append(
                        f"Scene {sid}: Shot {cut_no} uses a mechanical camera placeholder."
                    )
            first = cuts[0] if isinstance(cuts[0], dict) else {}
            if not v2_scene:
                if len(cuts) != 3:
                    errors.append(f"Scene {sid}: exactly 3 shots are required (00s-03s, 03s-07s, 07s-10s).")
                else:
                    second = cuts[1] if isinstance(cuts[1], dict) else {}
                    third = cuts[2] if isinstance(cuts[2], dict) else {}
                    if not CLOSEUP_RE.search(str(second.get("framing") or "")):
                        errors.append(f"Scene {sid}: Shot 2 must be a close-up or over-the-shoulder.")
                    if not REACTION_RE.search(str(third.get("framing") or "")):
                        errors.append(f"Scene {sid}: Shot 3 must be a tight close-up, reaction or insert.")
            if not str(first.get("action") or "").strip():
                errors.append(f"Scene {sid}: Shot 1 has no motion-start action.")
            elif STATIC_RE.search(str(first.get("action") or "")) and not v2_scene:
                errors.append(f"Scene {sid}: Shot 1 describes a static frame; it must start in motion.")
        words = scene_words(scene)
        dialogue_cap = int(fmt.get("max_dialogue_words_per_10s_scene") or max_scene_words)
        if words == 0:
            silent += 1
            warnings.append(f"Scene {sid}: no dialogue.")
        else:
            if words > dialogue_cap:
                errors.append(f"Scene {sid}: {words} dialogue words > {dialogue_cap} (global rule).")
            elif words < min_scene_words:
                warnings.append(f"Scene {sid}: only {words} dialogue words (<{min_scene_words}).")
        for line_no, count in enumerate(scene_line_words(scene), start=1):
            if count > max_line_words:
                errors.append(f"Scene {sid}: line {line_no} has {count} words > {max_line_words}.")
        speech = scene_speech_seconds(scene, wps)
        deadline = float(fmt.get("max_scene_speech_seconds") or MAX_SCENE_SPEECH_SECONDS)
        if speech > deadline:
            errors.append(f"Scene {sid}: {speech:.1f}s of speech > {deadline:.1f}s.")
        if not scene.get("beat"):
            warnings.append(f"Scene {sid}: no dramatic beat.")
        if not str(scene.get("sfx_ambience") or "").strip():
            warnings.append(f"Scene {sid}: no ambience/sfx (native audio may feel flat).")
        for item in scene.get("characters") or []:
            if str(item or "").strip() and resolve_speaker(str(item), master) is None:
                unknown_chars.add((sid, str(item)))
        present = [str(x) for x in (scene.get("characters_present") or []) if str(x).strip()]
        present_set = set(present)
        for item in present:
            if resolve_speaker(item, master) is None:
                unknown_chars.add((sid, item))
        for item in scene.get("characters") or []:
            text = str(item or "").strip()
            if not text:
                continue
            resolved = resolve_speaker(text, master) or text
            if resolved not in present_set:
                errors.append(f"Scene {sid}: '{item}' is in characters[] but not in characters_present[].")
        for entry in scene_dialogue_lines(scene):
            speaker = entry["speaker"]
            if not speaker:
                if production:
                    strict(f"Scene {sid}: line has no speaker.")
            elif resolve_speaker(speaker, master) is None:
                unknown_speakers.add((sid, speaker))
            else:
                resolved = resolve_speaker(speaker, master)
                if resolved not in present_set:
                    errors.append(f"Scene {sid}: speaker '{speaker}' is not in characters_present[].")
            line_val = str(entry.get("line") or "")
            trans_match = FORBIDDEN_TRANSLATION_RE.search(line_val)
            if trans_match:
                strict(
                    f"Scene {sid}: forbidden literal-translation artifact ('{trans_match.group(0)}') "
                    "in dialogue. Write idiomatic English with contractions."
                )
        raw_key_object = str(scene.get("key_object") or "").strip()
        key_object = extract_key_object(scene, master)
        if raw_key_object and not is_concrete_object_value(raw_key_object):
            errors.append(
                f"Scene {sid}: key_object '{raw_key_object}' is a prose fragment, not an object."
            )
        if not key_object:
            warnings.append(f"Scene {sid}: no explicit key_object (the panel stays generic).")
        elif not is_concrete_object_value(key_object):
            errors.append(
                f"Scene {sid}: key_object '{key_object}' is not a concrete object."
            )
        start_name = str((scene.get("object_start") or {}).get("name") or "").strip()
        end_name = str((scene.get("object_end") or {}).get("name") or "").strip()
        for label, value in (
            ("object_in", start_name),
            ("object_out", end_name),
        ):
            if value and not is_concrete_object_value(value):
                errors.append(
                    f"Scene {sid}: {label} '{value}' is a prose fragment, not an object."
                )
        first_object = start_name or key_object
        panel = str(scene.get("storyboard_panel") or "").strip()
        panel_flat = re.sub(r"\s+", " ", panel)
        first_cut = (scene.get("internal_cuts") or [{}])[0]
        first_framing = str(first_cut.get("framing") or "").strip()
        first_action = re.sub(r"\s+", " ", str(first_cut.get("action") or "")).strip().rstrip(".")
        if not re.match(r"^\[\d{2}s-\d{2}s\]", panel):
            errors.append(f"Scene {sid}: storyboard_panel missing or without a time range.")
        if first_framing and first_framing not in panel_flat:
            errors.append(f"Scene {sid}: storyboard_panel does not match Shot 1 framing.")
        if first_action and first_action not in panel_flat:
            errors.append(f"Scene {sid}: storyboard_panel does not match Shot 1 action.")
        scene_location = str(scene.get("location") or "").strip()
        if scene_location and scene_location not in panel_flat:
            errors.append(f"Scene {sid}: storyboard_panel does not include the scene location.")
        if first_object and first_object not in panel_flat:
            errors.append(f"Scene {sid}: storyboard_panel does not include the opening object.")
        if first_object and first_object.lower() not in first_action.lower():
            errors.append(f"Scene {sid}: Shot 1 action does not use the opening object.")
        anchors = str(scene.get("character_anchors") or "").strip()
        cast_index = canonical_cast(master)
        panel_cast = present[:MAX_SCENE_CAST] if v2_scene else present
        for cid in panel_cast:
            name = str((cast_index.get(cid) or {}).get("name") or cid)
            if name not in panel:
                errors.append(f"Scene {sid}: storyboard_panel does not include {name}.")
            if name not in anchors:
                errors.append(f"Scene {sid}: character_anchors does not include {name}.")
        if v2_scene:
            _validate_scene_v2(scene, master, sid, strict)
        future = scene.get("continuity_future_refs") or []
        if future:
            errors.append(f"Scene {sid}: continuity has a future spoiler: {future[0][:70]}")
        if scene_location and not location_keyword_match(scene_location, master):
            strict(f"Scene {sid}: location '{scene_location}' is outside the declared taxonomy.")
        if engine:
            for field in ("because_previous_ended_with", "this_scene_starts_with", "single_change_at_end"):
                value = str(scene.get(field) or "").strip()
                if not value:
                    errors.append(f"Scene {sid}: missing continuity field '{field}'.")
                elif len(value) < int(chain_rule.get("min_chars_per_field") or 24):
                    errors.append(f"Scene {sid}: '{field}' is too short to prove causality.")
                elif is_placeholder_text(value):
                    errors.append(f"Scene {sid}: '{field}' contains a mechanical placeholder.")

            exit_hook = str(scene.get("exit_hook") or "").strip()
            if not exit_hook:
                strict(f"Scene {sid}: missing 'exit_hook' field.")
            elif len(exit_hook) < 15:
                strict(f"Scene {sid}: 'exit_hook' is too short to push into the next scene.")
            elif is_placeholder_text(exit_hook):
                errors.append(f"Scene {sid}: 'exit_hook' contains a mechanical placeholder.")

            if sid >= 2:
                entry_bridge = str(scene.get("entry_bridge") or "").strip()
                if not entry_bridge:
                    strict(f"Scene {sid}: missing 'entry_bridge' field.")
                elif len(entry_bridge) < 15:
                    strict(f"Scene {sid}: 'entry_bridge' is too short to serve as a causal bridge.")
                elif is_placeholder_text(entry_bridge):
                    errors.append(f"Scene {sid}: 'entry_bridge' contains a mechanical placeholder.")

    for sid, name in sorted(unknown_chars):
        strict(f"Scene {sid}: unknown character '{name}' (not in characters[]).")
    for sid, speaker in sorted(unknown_speakers):
        strict(f"Scene {sid}: unknown speaker '{speaker}' (not in characters[]).")

    ordered = sorted(scenes, key=lambda s: int(s.get("scene_id") or 0))
    acts = [int(s.get("act") or 0) for s in ordered]
    if acts != sorted(acts):
        errors.append("Broken causal order: acts move backward between consecutive scenes.")
    for index, scene in enumerate(ordered):
        sid = int(scene.get("scene_id") or 0)
        if index == 0:
            continue
        previous = ordered[index - 1]
        expected = str(previous.get("single_change_at_end") or "").strip()
        actual = str(scene.get("because_previous_ended_with") or "").strip()
        if engine and expected and actual != expected:
            errors.append(
                f"Scene {sid}: 'because_previous_ended_with' does not match the final change "
                f"of scene {previous.get('scene_id')}."
            )
        if str(scene.get("this_scene_starts_with") or "").strip() == str(
            scene.get("single_change_at_end") or ""
        ).strip():
            errors.append(f"Scene {sid}: the scene starts and ends in the same state.")
    bases: List[str] = []
    for scene in ordered:
        base = str(scene.get("location") or "").split(",")[0].strip()
        bases.append(base)
    runs: List[int] = []
    previous = None
    for base in bases:
        if base == previous:
            runs[-1] += 1
        else:
            runs.append(1)
            previous = base
    for index in range(2, len(bases)):
        if bases[index] == bases[index - 2] and bases[index] != bases[index - 1]:
            strict(
                f"Scenes {index - 1}-{index + 1}: location ping-pong "
                f"({bases[index]} -> {bases[index - 1]} -> {bases[index]})."
            )
    if engine:
        nc = master.get("narrative_continuity") if isinstance(master.get("narrative_continuity"), dict) else {}
        blocks = nc.get("minute_blocks") if isinstance(nc.get("minute_blocks"), list) else []
        block_scene_count = expected_scenes if not allow_partial else len(scenes)
        per_block = int(engine.get("scenes_per_block") or SCENES_PER_BLOCK)
        expected_blocks = (block_scene_count + per_block - 1) // per_block if block_scene_count else 0
        if len(blocks) != expected_blocks:
            errors.append(
                f"Continuity: expected {expected_blocks} one-minute blocks but found {len(blocks)}."
            )
        for block in blocks:
            if not isinstance(block, dict):
                errors.append("Continuity: 1-minute block has invalid format.")
                continue
            question = str(block.get("driving_question") or "").strip()
            if not question:
                errors.append(f"Continuity: block {block.get('block')} has no driving_question.")
            elif is_placeholder_text(question):
                errors.append(f"Continuity: block {block.get('block')} uses a filler question.")
            elif len(question.split()) > int(
                ((engine_rules.get("1_single_driving_question_per_block") or {}).get("question_max_words")) or 24
            ):
                errors.append(f"Continuity: block {block.get('block')} question exceeds the word maximum.")
            ids = [int(i) for i in (block.get("scenes") or []) if str(i).isdigit()]
            if len(ids) != int(engine.get("scenes_per_block") or 6):
                errors.append(
                    f"Continuity: block {block.get('block')} does not cover "
                    f"{engine.get('scenes_per_block') or 6} scenes."
                )
    if runs and max(runs) < 3:
        warnings.append(
            f"Locations: {len(runs)} blocks with a maximum of {max(runs)} consecutive scene(s); "
            "the rule recommends 3-6 scenes per dramatic block."
        )

    # Block pacing rule (6 scenes): 6 confrontation peaks in a row are FORBIDDEN
    per_block = int(engine.get("scenes_per_block") or 6) if engine else 6
    if len(ordered) >= per_block:
        for b_idx in range(0, len(ordered), per_block):
            group = ordered[b_idx:b_idx + per_block]
            if len(group) == per_block:
                block_no = (b_idx // per_block) + 1
                all_confrontational = all(is_confrontation_scene(s) for s in group)
                has_non_confront = any(is_non_confrontational_scene(s) for s in group)
                if all_confrontational or (not has_non_confront and all(str(s.get("beat") or "") in ("confrontation", "crisis", "confrontation_peak") for s in group)):
                    errors.append(
                        f"Pacing: block {block_no} (scenes {group[0].get('scene_id')}-{group[-1].get('scene_id')}) "
                        "has 6 confrontation peaks in a row. Forbidden: at least 1 non-confrontational beat is required "
                        "per block (solo decision, discovery, plan, tender/vulnerable moment)."
                    )

    if engine:
        cliffhanger_types: List[str] = []
        by_id_map = {int(s.get("scene_id") or 0): s for s in scenes}
        for b in blocks:
            c_type = str(b.get("cliffhanger_type") or "").strip().lower()
            if not c_type and b.get("scenes"):
                last_sid = b["scenes"][-1]
                last_sc = by_id_map.get(last_sid) or {}
                c_type = str(last_sc.get("cliffhanger_type") or "").strip().lower()
            cliffhanger_types.append(c_type)

        for i in range(len(cliffhanger_types) - 1):
            c1, c2 = cliffhanger_types[i], cliffhanger_types[i + 1]
            if c1 and c2 and c1 == c2:
                errors.append(
                    f"Continuity: blocks {i + 1} and {i + 2} repeat the cliffhanger type '{c1}'. "
                    "Do not repeat the same type in two consecutive blocks (rotate among identity, emotion, revelation)."
                )

    if scenes:
        required = required_beats_for_scene_count(expected_scenes, rules)
        by_id = {int(s.get("scene_id") or 0): s for s in scenes}
        for sid, beat in required.items():
            if sid in by_id and str(by_id[sid].get("beat") or "") != beat:
                warnings.append(f"Scene {sid}: beat '{by_id[sid].get('beat')}' (expected '{beat}').")

    teasers = master.get("teasers")
    if not isinstance(teasers, list) or len(teasers) != 3:
        warnings.append("Expected 3 teasers (60 s each).")
    else:
        for t in teasers:
            ids_t = [int(i) for i in (t.get("scenes") or [])]
            if len(ids_t) != 6:
                warnings.append(f"Teaser {t.get('id')}: expected 6 scenes (60 s) but found {len(ids_t)}.")
            if ids_t and ids_t != list(range(min(ids_t), min(ids_t) + len(ids_t))):
                strict(f"Teaser {t.get('id')}: scenes must be consecutive ({ids_t}).")
            if any(not (1 <= i <= expected_scenes) for i in ids_t):
                errors.append(f"Teaser {t.get('id')}: references out-of-range scenes.")

    if silent > max(2, len(scenes) // 10):
        warnings.append(f"{silent} scenes without dialogue; the episode may feel empty.")
    if prompts < len(scenes):
        warnings.append(f"{len(scenes) - prompts} scenes without a usable image prompt.")
    characters = [c for c in (master.get("characters") or []) if isinstance(c, dict)]
    if not characters:
        strict("No characters[]: facial consistency and voices cannot be verified.")
    elif not any(
        str(c.get("visual_reference") or c.get("reference_image") or "").strip() for c in characters
    ):
        warnings.append(
            "No character defines visual_reference/reference_image: facial consistency "
            "will depend on manual attachments (see 02 — chatgpt_reference_sheets.txt)."
        )
    return {"errors": errors, "warnings": warnings}


def expected_scene_count_from_payloads(payloads: List[Dict[str, Any]]) -> int:
    for payload in payloads:
        if not isinstance(payload, dict):
            continue
        ep = payload.get("episode") if isinstance(payload.get("episode"), dict) else {}
        for key in ("target_minutes", "total_blocks", "minute_blocks", "blocks"):
            if ep.get(key) not in (None, ""):
                try:
                    return scene_count_for_target(ep.get(key))
                except NFError:
                    continue
        if ep.get("total_scenes") not in (None, ""):
            try:
                value = int(ep.get("total_scenes"))
            except (TypeError, ValueError):
                value = 0
            if value > 0:
                return value
    highest = 0
    longest = 0
    for payload in payloads:
        if not isinstance(payload, dict):
            continue
        raw = payload.get("scenes") if isinstance(payload.get("scenes"), list) else []
        longest = max(longest, len(raw))
        for scene in raw:
            if not isinstance(scene, dict):
                continue
            try:
                highest = max(highest, int(scene.get("scene_id") or 0))
            except (TypeError, ValueError):
                continue
    return highest or longest or SCENE_COUNT


def merge_payloads(payloads: List[Dict[str, Any]]) -> Tuple[Dict[str, Any], List[str]]:
    """Merge script parts by scene_id: sort, deduplicate and do not renumber."""
    warnings: List[str] = []
    if not payloads:
        raise NFError("No payloads to merge.")
    if len(payloads) == 1:
        return payloads[0], warnings
    expected_scenes = expected_scene_count_from_payloads(payloads)
    full = [p for p in payloads if len(p.get("scenes") or []) == expected_scenes]
    if full:
        warnings.append(
            f"Received several JSON files with {expected_scenes} scenes; "
            "the first one is used and the rest are ignored."
        )
        return full[0], warnings

    keyed: Dict[int, Dict[str, Any]] = {}
    unkeyed: List[Dict[str, Any]] = []
    for payload in payloads:
        for scene in payload.get("scenes") or []:
            if not isinstance(scene, dict):
                continue
            try:
                sid = int(scene.get("scene_id"))
            except (TypeError, ValueError):
                unkeyed.append(scene)
                continue
            if sid in keyed:
                warnings.append(f"duplicate scene_id {sid} while merging: the last occurrence is kept.")
            keyed[sid] = scene

    ordered = [keyed[sid] for sid in sorted(keyed)] + unkeyed
    merged: Dict[str, Any] = {"scenes": ordered}
    for key in (
        "episode", "characters", "characters_locked", "locations", "acts",
        "publisher", "soundtrack", "source_mode", "source_script",
        "visual_variant", "object_ledger",
    ):
        for payload in payloads:
            if payload.get(key):
                merged.setdefault(key, payload[key])
                break
    teasers: Dict[int, Dict[str, Any]] = {}
    for payload in payloads:
        for teaser in payload.get("teasers") or []:
            if not isinstance(teaser, dict):
                continue
            try:
                tid = int(teaser.get("id") or 0)
            except (TypeError, ValueError):
                continue
            if tid:
                teasers.setdefault(tid, teaser)
    if teasers:
        merged["teasers"] = [teasers[k] for k in sorted(teasers)]
    missing = [i for i in range(1, expected_scenes + 1) if i not in keyed]
    if missing:
        warnings.append(f"{len(missing)} scenes missing after merge: {missing[:12]}{'…' if len(missing) > 12 else ''}")
    warnings.append(
        f"Merged {len(payloads)} files into a master "
        f"({len(ordered)} of {expected_scenes} scenes)."
    )
    return merged, warnings


def print_validation(result: Dict[str, List[str]]) -> bool:
    errors, warnings = result.get("errors", []), result.get("warnings", [])
    for warning in warnings[:30]:
        warn(warning)
    if len(warnings) > 30:
        warn(f"... and {len(warnings) - 30} more warnings.")
    for error in errors:
        err(error)
    if not errors:
        ok(f"Validation passed ({len(warnings)} warnings).")
        return True
    err(f"Validation failed: {len(errors)} errors, {len(warnings)} warnings.")
    return False


def extract_json_blob(text: str) -> Any:
    """Extract the first JSON object/array from an LLM response with surrounding text."""
    text = (text or "").strip()
    if text.startswith("\ufeff"):
        text = text.lstrip("\ufeff")
    fences = re.findall(r"```(?:json)?\s*(.*?)```", text, flags=re.DOTALL | re.IGNORECASE)
    candidates = [f.strip() for f in fences if f.strip()] + [text]
    for candidate in candidates:
        try:
            return json.loads(candidate)
        except Exception:
            pass
    # Balanced-brace search (ignores braces inside strings)
    for opener, closer in (("{", "}"), ("[", "]")):
        start = text.find(opener)
        if start == -1:
            continue
        depth = 0
        in_str = False
        escape = False
        for pos in range(start, len(text)):
            ch = text[pos]
            if in_str:
                if escape:
                    escape = False
                elif ch == "\\":
                    escape = True
                elif ch == '"':
                    in_str = False
                continue
            if ch == '"':
                in_str = True
            elif ch == opener:
                depth += 1
            elif ch == closer:
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[start:pos + 1])
                    except Exception:
                        break
    raise NFError("No valid JSON was found in the text. Paste only the LLM JSON or check the file.")


def default_teaser_ranges(scene_count: Optional[int] = None) -> List[List[int]]:
    try:
        total = max(1, int(scene_count or SCENE_COUNT))
    except (TypeError, ValueError):
        total = SCENE_COUNT
    window = min(6, total)
    start_mid = max(1, min(total - window + 1, int(round(total * 0.35))))
    start_end = max(1, total - window + 1)
    return [
        list(range(1, window + 1)),
        list(range(start_mid, start_mid + window)),
        list(range(start_end, start_end + window)),
    ]


# --- Subcommand dispatch (optional nf_core CLI) ---
def subcommand_script(name: str) -> Optional[Path]:
    rel = SUBCOMMANDS.get(str(name or "").strip().lower())
    return (NF_ROOT / rel) if rel else None


def run_subcommand(name: str, args: Sequence[str]) -> int:
    script = subcommand_script(name)
    if not script:
        raise NFError(
            f"Subcomando desconocido: {name!r}. Disponibles: {', '.join(sorted(SUBCOMMANDS))}"
        )
    if not script.exists():
        raise NFError(f"Subcommand script does not exist: {script}")
    completed = subprocess.run([sys.executable, str(script), *args])
    return int(completed.returncode)


def cmd_prepare(project: str, extra_args: Sequence[str] = ()) -> int:
    """Regenerate the workflow (00), MASTER_PROMPTS (04) and the Muse pack (05).

    This keeps MASTER_WORKFLOW_PROMPTS_READY.md, MASTER_PROMPTS.md and
    MUSE_PRODUCTION_PACK.md always 100% synchronized with the brief and
    master_episode.json.
    """
    common = [str(project), *extra_args]
    for name in ("export-master-prompts", "prompts"):
        rc = run_subcommand(name, common)
        if rc:
            return rc
    return run_subcommand("muse-pack", [str(project)])


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = list(argv if argv is not None else sys.argv[1:])
    if not args or args[0] in ("-h", "--help"):
        print("Usage: python nf_core.py <subcommand> <project> [options]")
        print("Subcomandos: prepare, " + ", ".join(sorted(SUBCOMMANDS)))
        return 0
    if args[0].lower() == "prepare":
        if len(args) < 2:
            raise NFError("Usage: python nf_core.py prepare <project> [options]")
        return cmd_prepare(args[1], args[2:])
    return run_subcommand(args[0], args[1:])


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except NFError as exc:
        err(str(exc))
        raise SystemExit(1)

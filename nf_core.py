#!/usr/bin/env python3
"""Núcleo compartido de novel_factory.

Reglas de diseño:
- Solo biblioteca estándar de Python + ffmpeg/ffprobe. Cero APIs de pago, cero red.
- Ningún script de este módulo importa ni modifica el código de USA WHITE /
  NOTICIAS IA AUTOMATIZADO: la integración es por archivos (cola/pendientes).
- Todo es auditable: rutas explícitas, JSON legible, errores con contexto.

Este archivo lo importan los generadores (01-03), el runner (automation/) y la
postproducción (04-05) mediante sys.path.insert(0, <novel_factory>).
"""
from __future__ import annotations

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

# --- Consola UTF-8 en Windows (mismo patrón que el resto del workspace) ---
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

SCENE_COUNT = 60
SCENE_SECONDS = 10.0
TOTAL_SECONDS = SCENE_COUNT * SCENE_SECONDS  # 600 s = 10 min
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

# Subcomandos que viven en scripts de generators/ y se despachan desde nf_core.
SUBCOMMANDS: Dict[str, str] = {
    "export-master-prompts": "generators/00_export_master_workflow_prompts.py",
    "prompts": "generators/04_export_master_prompts.py",
    "muse-pack": "generators/05_export_muse_method_pack.py",
}

# --- Contrato de contenido (P0): ritmo de habla y presupuesto por escena ---
SPEECH_WORDS_PER_SECOND = 2.5    # ritmo conversacional US English (~150 wpm)
MAX_SCENE_WORDS = 15             # tope global por escena de 10 s
MAX_LINE_WORDS = 15              # tope por intervenci�n
MIN_SCENE_WORDS = 6              # m�nimo para que la escena no quede vac�a
MAX_SCENE_SPEECH_SECONDS = 8.5   # la voz debe terminar antes de 8.5 s
CUT_MIN_GAP = 3.0
CUT_MAX_GAP = 4.0
DURATION_TOLERANCE_SEC = 0.05
SHOT_CUT_TIMES = (0.0, 3.0, 7.0)
SHOT_RANGES = ("00s-03s", "03s-07s", "07s-10s")
DIALOGUE_END_DEADLINE_SEC = 8.5


class NFError(RuntimeError):
    """Error controlado del módulo (mensaje apto para consola)."""


# --- Salida de consola homogénea ---
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


# --- Utilidades de texto / ficheros ---
def slugify(text: str) -> str:
    """Convierte un título en slug seguro para carpeta.

    ASCII primero (comportamiento histórico). Si el título no genera nada ASCII
    (p. ej. chino), conserva caracteres Unicode alfanuméricos y añade un hash
    corto para evitar colisiones entre títulos CJK distintos.
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
        raise NFError(f"No se pudo leer JSON {path}: {exc}") from exc


def write_json(path: Path, data: Any) -> Path:
    """Escritura atómica (tmp + replace) para no dejar JSON a medias."""
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
        raise NFError(f"Falta o está corrupto: {SHOWRUNNER_FILE}")
    return data


def load_style_locks() -> Dict[str, Any]:
    data = read_json(STYLE_FILE)
    if not isinstance(data, dict):
        raise NFError(f"Falta o está corrupto: {STYLE_FILE}")
    return data


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


def parse_ranges(spec: str) -> List[int]:
    """'1-5,8,10-12' -> [1..5, 8, 10..12] (1-based, sin duplicados, ordenado)."""
    out: set[int] = set()
    for part in str(spec or "").replace(" ", "").split(","):
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            if not (a.isdigit() and b.isdigit()):
                raise NFError(f"Rango inválido: '{part}'")
            lo, hi = int(a), int(b)
            if lo > hi:
                lo, hi = hi, lo
            out.update(range(lo, hi + 1))
        elif part.isdigit():
            out.add(int(part))
        else:
            raise NFError(f"Rango inválido: '{part}'")
    return sorted(i for i in out if 1 <= i <= SCENE_COUNT)


# --- Proyectos / episodios ---
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


def create_project(slug: str) -> Dict[str, Path]:
    paths = project_paths(project_dir(slug))
    for key in ("root", "frames", "references", "raw_clips", "output", "prompts_dir"):
        paths[key].mkdir(parents=True, exist_ok=True)
    for folder in (paths["frames"], paths["references"], paths["raw_clips"], paths["output"]):
        keep = folder / ".gitkeep"
        if not keep.exists():
            keep.write_text("", encoding="utf-8")
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
            f"No existe el proyecto '{raw}'. Se esperaba: {paths['master']}\n"
            "  Crea el episodio primero con generators/01_story_to_master_json.py"
        )
    return paths


def scene_stem(index: int) -> str:
    if not 1 <= int(index) <= SCENE_COUNT:
        raise NFError(f"scene_id fuera de rango: {index}")
    return f"scene_{int(index):03d}"


def frame_stem(index: int) -> str:
    if not 1 <= int(index) <= SCENE_COUNT:
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
            f"Falta en PATH: {', '.join(missing)}. Instala con: winget install Gyan.FFmpeg"
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
        raise NFError("ffmpeg falló:\n  " + "\n  ".join(tail))
    return res


def ffprobe_json(path: Path) -> Dict[str, Any]:
    res = run_cmd([
        "ffprobe", "-v", "error", "-print_format", "json",
        "-show_format", "-show_streams", str(path),
    ])
    if res.returncode != 0:
        tail = (res.stderr or "").strip().splitlines()[-6:]
        raise NFError(f"ffprobe falló para {Path(path).name}:\n  " + "\n  ".join(tail))
    try:
        return json.loads(res.stdout or "{}")
    except Exception as exc:
        raise NFError(f"ffprobe devolvió JSON inválido para {Path(path).name}: {exc}") from exc


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
    """Fuente bold para overlays. Prioriza assets/fonts del módulo; cae a Windows."""
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
        raise NFError(f"No existe o es inválido: {paths['master']}")
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


def scene_dialogue_lines(scene: Dict[str, Any]) -> List[Dict[str, str]]:
    """Normaliza la diálogo a [{speaker,line,delivery}] (tolera strings/legado)."""
    out: List[Dict[str, str]] = []
    raw = scene.get("dialogue")
    if isinstance(raw, str):
        raw = [raw]
    for item in raw or []:
        if isinstance(item, str):
            if item.strip():
                out.append({"speaker": "", "line": item.strip(), "delivery": ""})
        elif isinstance(item, dict):
            line = str(item.get("line") or item.get("text") or "").strip()
            if line:
                out.append({
                    "speaker": str(item.get("speaker") or "").strip(),
                    "line": line,
                    "delivery": str(item.get("delivery") or "").strip(),
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
    """Palabras por intervención, en orden."""
    return [len(re.findall(r"\b[\w'-]+\b", d["line"])) for d in scene_dialogue_lines(scene)]


def scene_speech_seconds(scene: Dict[str, Any], words_per_second: float = SPEECH_WORDS_PER_SECOND) -> float:
    """Segundos estimados de habla de la escena (todas las líneas)."""
    wps = float(words_per_second or SPEECH_WORDS_PER_SECOND)
    return (scene_words(scene) / wps) if wps > 0 else 0.0


# --- Reparto canónico / hablantes / continuidad presente ---
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
    """Índice de personajes por id / nombre / primer nombre / arquetipo (minúsculas)."""
    index: Dict[str, Dict[str, Any]] = {}
    for character in master.get("characters") or []:
        if not isinstance(character, dict):
            continue
        for key in _cast_keys(character):
            index.setdefault(key, character)
    return index


def resolve_speaker(speaker: str, master: Dict[str, Any]) -> Optional[str]:
    """Devuelve el id/name canónico de un hablante, o None si no está en el reparto."""
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
    """Índice de personajes por id Y por nombre (minúsculas)."""
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
    """Nombre de archivo can�nico de la hoja de referencia: reference_<id>.png."""
    cid = slugify(str(character.get("id") or character.get("name") or "character")) or "character"
    return f"reference_{cid}.png"


def _character_id(character: Dict[str, Any]) -> str:
    return str(character.get("id") or character.get("name") or "").strip()


def character_position_map(master: Dict[str, Any]) -> Dict[str, int]:
    """Posición 1-based de cada personaje en el orden de la hoja de reparto."""
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
    """IDs de personajes nombrados en un texto, en orden de reparto."""
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
    """Unión ordenada de reparto visible, hablantes y personajes nombrados."""
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


def extract_key_object(scene: Dict[str, Any]) -> str:
    explicit = re.sub(r"\s+", " ", str(scene.get("key_object") or "")).strip().rstrip(".")
    if explicit:
        return explicit
    for prop in scene.get("props") or []:
        text = re.sub(r"\s+", " ", str(prop or "")).strip().rstrip(".")
        if text:
            return text
    match = re.search(
        r"Evidence object in play:\s*([^.;]+)",
        str(scene.get("continuity") or ""),
        re.IGNORECASE,
    )
    if match:
        return re.sub(r"\s+", " ", match.group(1)).strip().rstrip(".")
    return ""


def format_character_anchors(scene: Dict[str, Any], characters_locked: Any) -> str:
    """Lista de anclas de identidad para todos los presentes en la escena.

    ``characters_locked`` puede ser el maestro completo o la lista de personajes.
    Cada ancla fija posición en la hoja de reparto, descriptor estable y vestuario.
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
        name = str(character.get("name") or cid)
        descriptor = _character_descriptor(character)
        wardrobe = _character_wardrobe(character, act, scene)
        anchors.append(f"{name} (Cast Sheet Pos #{pos}: {descriptor}, wearing {wardrobe})")
    return "; ".join(anchors)


def build_storyboard_panel_description(scene: Dict[str, Any], master: Dict[str, Any]) -> str:
    """Describe la viñeta que DEBE ser el primer frame de la Toma 1."""
    cuts = scene.get("internal_cuts") or []
    first = cuts[0] if cuts and isinstance(cuts[0], dict) else {}
    framing = str(first.get("framing") or "cinematic shot").strip()
    action = re.sub(r"\s+", " ", str(first.get("action") or "the subject is already in motion")).strip()
    action = action.rstrip(".")
    location = re.sub(r"\s+", " ", str(scene.get("location") or "the scene location")).strip().rstrip(".")
    key_object = extract_key_object(scene) or "the scene's central visual detail"
    cast_index = canonical_cast(master)
    names = [
        str((cast_index.get(cid) or {}).get("name") or cid)
        for cid in (scene.get("characters_present") or scene.get("characters") or [])
    ]
    present = ", ".join(names) if names else "the protagonist"
    return (
        f"[00s-03s] {framing}: {action}. "
        f"Location: {location}. Key object: {key_object}. Characters present: {present}."
    )


def scene_cast(master: Dict[str, Any], scene: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Personajes canónicos presentes en una escena (sin duplicados, en orden)."""
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
    """Separa continuidad en PRESENTE de referencias futuras (spoilers).

    Devuelve (texto_presente, frases_eliminadas). Trabaja por frases para no
    dejar fragmentos colgando cuando se elimina una referencia futura.
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
    """True si la ubicación de escena encaja con la taxonomía declarada."""
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


# --- Normalización y validación del JSON Maestro ---
def _coerce_dialogue(value: Any) -> List[Dict[str, str]]:
    if isinstance(value, str):
        value = [value]
    if not isinstance(value, list):
        return []
    out: List[Dict[str, str]] = []
    for item in value:
        if isinstance(item, str) and item.strip():
            out.append({"speaker": "", "line": item.strip(), "delivery": ""})
        elif isinstance(item, dict):
            line = str(item.get("line") or item.get("text") or "").strip()
            if line:
                out.append({
                    "speaker": str(item.get("speaker") or "").strip(),
                    "line": line,
                    "delivery": str(item.get("delivery") or "").strip(),
                })
    return out


CLOSEUP_RE = re.compile(r"close[\s-]?up|over[\s-]?the[\s-]?shoulder|\bOTS\b|medium close", re.IGNORECASE)
REACTION_RE = re.compile(r"tight close|close[\s-]?up|extreme close|insert|reaction|detail|\bPOV\b|point of view", re.IGNORECASE)
STATIC_RE = re.compile(
    r"\bstatic\b|\bposed\b|\bnot moving\b|\bhold(?:ing)? still\b|\bmotionless\b|"
    r"\bfreezes?\b|\bgo(?:es)? still\b|\bstands? (?:still|rigid|erect|immobile|frozen)\b",
    re.IGNORECASE,
)


def _coerce_cuts(value: Any, rotation: Sequence[str]) -> List[Dict[str, Any]]:
    """Fuerza exactamente 3 tomas: 00s-03s, 03s-07s y 07s-10s.

    Toma 1 conserva el encuadre de la viñeta y arranca en movimiento. Toma 2 se
    corrige a close-up/OTS si el dato no pertenece a esa familia. Toma 3 se
    corrige a reacción/insert si el dato no pertenece a esa familia.
    """
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
    actions = [
        "the subject is already moving inside the storyboard framing",
        "hard cut into the dialogue beat with the speaker mid-line",
        "hard cut to the reaction as the line lands",
    ]
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
        if not raw_action or STATIC_RE.search(raw_action):
            raw_action = actions[i]
        cuts.append({
            "at": at,
            "range": SHOT_RANGES[i],
            "framing": framings[i],
            "action": raw_action,
        })
    return cuts


def _normalize_teasers(payload: Dict[str, Any], scenes: List[Dict[str, Any]], warnings: List[str]) -> List[Dict[str, Any]]:
    defaults = [
        {"id": 1, "title": "Official Teaser", "scenes": list(range(1, 7))},
        {"id": 2, "title": "The Twist", "scenes": list(range(21, 27))},
        {"id": 3, "title": "The Cliffhanger", "scenes": list(range(55, 61))},
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
                if 1 <= val <= SCENE_COUNT and val not in ids:
                    ids.append(val)
            if len(ids) < 4:
                warnings.append(f"Teaser {idx + 1} tiene menos de 4 escenas válidas; se completa con el rango por defecto.")
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
                warnings.append(f"Teaser {base['id']} ausente: se generó con escenas {base['scenes'][0]}-{base['scenes'][-1]}.")
    # Completa hook/caption de teasers
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


def normalize_master(
    payload: Any,
    slug: str,
    title: str = "",
    repair: bool = True,
    allow_partial: bool = False,
) -> Tuple[Dict[str, Any], List[str]]:
    """Lleva la respuesta del LLM (o un maestro existente) al esquema canónico.

    Tolerante con formatos habituales: lista de escenas, envoltorios 'data',
    fences Markdown, diálogo como string, cortes como lista de strings.
    Devuelve (master, warnings). Los errores estructurales lanzan NFError.
    """
    warnings: List[str] = []
    if isinstance(payload, list):
        payload = {"scenes": payload}
    if not isinstance(payload, dict):
        raise NFError("La entrada no es un objeto JSON ni una lista de escenas.")
    for key in ("episode_json", "data", "result", "output", "master_episode"):
        inner = payload.get(key)
        if isinstance(inner, dict) and isinstance(inner.get("scenes"), list):
            payload = inner
            warnings.append(f"Se desenvolvió la clave contenedora '{key}'.")
            break

    raw_scenes = payload.get("scenes")
    if not isinstance(raw_scenes, list) or not raw_scenes:
        raise NFError("El JSON no contiene una lista 'scenes' con las 60 escenas.")
    if len(raw_scenes) != SCENE_COUNT:
        if not allow_partial:
            raise NFError(
                f"El JSON trae {len(raw_scenes)} escenas y el formato exige exactamente {SCENE_COUNT}. "
                "Pide al LLM que regenere el guion completo (o divide el trabajo por actos y únelos)."
            )
        warnings.append(f"Modo parcial: {len(raw_scenes)} de {SCENE_COUNT} escenas (no publicable todavía).")
    if not all(isinstance(s, dict) for s in raw_scenes):
        raise NFError("Todas las entradas de 'scenes' deben ser objetos JSON.")

    style = load_style_locks()
    rotation = ((style.get("visual_style_lock") or {}).get("default_shot_rotation") or DEFAULT_SHOT_ROTATION)
    rules = load_showrunner()
    required_beats = {int(k): v for k, v in (rules.get("required_beats") or {}).items() if str(k).isdigit()}

    ep_in = payload.get("episode") if isinstance(payload.get("episode"), dict) else {}
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
    ep["total_scenes"] = SCENE_COUNT
    ep["scene_seconds"] = int(SCENE_SECONDS)
    ep["total_seconds"] = int(TOTAL_SECONDS)
    ep["aspect_master"] = "16:9"
    ep["aspect_teaser"] = "9:16"
    if not str(ep.get("logline") or "").strip():
        warnings.append("episode.logline vacío: se recomienda una frase de 1-2 líneas para el pack de publicación.")

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
                warnings.append(f"scene_id no numérico ({original_id!r}); se usa {idx}.")
                sid = idx
        scene["scene_id"] = sid
        scene["duration_s"] = float(scene.get("duration_s") or SCENE_SECONDS)
        try:
            act = int(scene.get("act") or 0)
        except (TypeError, ValueError):
            act = 0
        scene["act"] = act if 1 <= act <= 6 else ((max(1, sid) - 1) // 10 + 1)
        scene["beat"] = str(scene.get("beat") or required_beats.get(sid) or "").strip()
        scene["dialogue"] = _coerce_dialogue(scene.get("dialogue"))
        scene["internal_cuts"] = _coerce_cuts(scene.get("internal_cuts"), rotation)
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
        scene["characters_present"] = scene_characters_present(scene, cast_ctx)
        if not scene["first_frame_prompt"]:
            warnings.append(f"Escena {sid}: first_frame_prompt vacío (el frame no se podrá generar).")
        if not scene["dialogue"]:
            warnings.append(f"Escena {sid}: sin diálogo (10 s de silencio).")
        if future:
            warnings.append(f"Escena {sid}: continuidad con referencias futuras ({len(future)}); se sanean en el prompt de vídeo.")
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
    for scene in scenes:
        scene["character_anchors"] = format_character_anchors(scene, master["characters_locked"])
        scene["storyboard_panel"] = build_storyboard_panel_description(scene, master)
    master["partial"] = len(scenes) != SCENE_COUNT
    master["teasers"] = _normalize_teasers(payload, scenes, warnings)

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
    """Completa prompts vacíos con una plantilla cinematográfica (solo reparación)."""
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


def validate_master(
    master: Dict[str, Any],
    allow_partial: bool = False,
    production: bool = False,
) -> Dict[str, List[str]]:
    """Validación semántica/estructural. Devuelve {'errors': [...], 'warnings': [...]}.

    Con ``production=True`` los hallazgos de contenido (reparto, hablantes,
    presupuesto de habla, continuidad futura, taxonomía de ubicaciones) pasan de
    advertencia a error. En modo normal se conservan como advertencias para no
    romper los fixtures existentes.
    """
    errors: List[str] = []
    warnings: List[str] = []

    def strict(msg: str) -> None:
        (errors if production else warnings).append(msg)

    ep = episode_meta(master)
    scenes = [s for s in (master.get("scenes") or []) if isinstance(s, dict)]

    if not ep.get("slug"):
        errors.append("episode.slug ausente.")
    if not str(ep.get("title") or "").strip():
        errors.append("episode.title ausente.")
    if not allow_partial and len(scenes) != SCENE_COUNT:
        errors.append(f"Se esperaban {SCENE_COUNT} escenas y hay {len(scenes)}.")
    if production and master.get("partial") and not allow_partial:
        errors.append("El maestro es parcial (<60 escenas): no es publicable.")
    ids = [int(s.get("scene_id") or 0) for s in scenes]
    if len(set(ids)) != len(ids):
        errors.append("scene_id duplicado.")
    if not allow_partial and ids != list(range(1, len(scenes) + 1)):
        errors.append("scene_id debe ser 1..N sin huecos ni duplicados.")
    elif allow_partial and ids != sorted(ids):
        warnings.append("IDs parciales desordenados: ordénalos antes de fusionar.")

    rules = load_showrunner()
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
            errors.append(f"Escena {sid}: act inválido.")
        prompt = str(scene.get("first_frame_prompt") or "")
        if len(prompt) < 60:
            errors.append(f"Escena {sid}: first_frame_prompt demasiado corto ({len(prompt)} chars).")
        else:
            prompts += 1
        cuts = scene.get("internal_cuts")
        if not isinstance(cuts, list) or len(cuts) != 3:
            errors.append(f"Escena {sid}: se requieren exactamente 3 tomas (00s-03s, 03s-07s, 07s-10s).")
        else:
            ats = [float(c.get("at") or 0.0) for c in cuts]
            if any(abs(a - e) > 1e-6 for a, e in zip(ats, SHOT_CUT_TIMES)):
                errors.append(f"Escena {sid}: cortes en {ats}; se esperan {list(SHOT_CUT_TIMES)}.")
            first = cuts[0] if isinstance(cuts[0], dict) else {}
            second = cuts[1] if isinstance(cuts[1], dict) else {}
            third = cuts[2] if isinstance(cuts[2], dict) else {}
            if not str(first.get("action") or "").strip():
                errors.append(f"Escena {sid}: Toma 1 sin acción de arranque en movimiento.")
            if STATIC_RE.search(str(first.get("action") or "")):
                errors.append(f"Escena {sid}: Toma 1 describe un frame estático; debe arrancar en movimiento.")
            if not CLOSEUP_RE.search(str(second.get("framing") or "")):
                errors.append(f"Escena {sid}: Toma 2 debe ser close-up u over-the-shoulder.")
            if not REACTION_RE.search(str(third.get("framing") or "")):
                errors.append(f"Escena {sid}: Toma 3 debe ser tight close-up, reacción o insert.")
            if not str(second.get("action") or "").strip():
                errors.append(f"Escena {sid}: Toma 2 sin acción de diálogo/acción.")
            if not str(third.get("action") or "").strip():
                errors.append(f"Escena {sid}: Toma 3 sin acción de reacción.")
        words = scene_words(scene)
        dialogue_cap = int(fmt.get("max_dialogue_words_per_10s_scene") or max_scene_words)
        if words == 0:
            silent += 1
            warnings.append(f"Escena {sid}: sin diálogo.")
        else:
            if words > dialogue_cap:
                errors.append(f"Escena {sid}: {words} palabras de diálogo > {dialogue_cap} (regla global).")
            elif words < min_scene_words:
                warnings.append(f"Escena {sid}: solo {words} palabras de diálogo (<{min_scene_words}).")
        for line_no, count in enumerate(scene_line_words(scene), start=1):
            if count > max_line_words:
                errors.append(f"Escena {sid}: línea {line_no} con {count} palabras > {max_line_words}.")
        speech = scene_speech_seconds(scene, wps)
        deadline = float(fmt.get("max_scene_speech_seconds") or MAX_SCENE_SPEECH_SECONDS)
        if speech > deadline:
            errors.append(f"Escena {sid}: {speech:.1f}s de habla > {deadline:.1f}s.")
        if not scene.get("beat"):
            warnings.append(f"Escena {sid}: sin beat dramático.")
        if not str(scene.get("sfx_ambience") or "").strip():
            warnings.append(f"Escena {sid}: sin ambiencia/sfx (el audio nativo puede quedar plano).")
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
                errors.append(f"Escena {sid}: '{item}' está en characters[] pero no en characters_present[].")
        for entry in scene_dialogue_lines(scene):
            speaker = entry["speaker"]
            if not speaker:
                if production:
                    strict(f"Escena {sid}: línea sin hablante.")
            elif resolve_speaker(speaker, master) is None:
                unknown_speakers.add((sid, speaker))
            else:
                resolved = resolve_speaker(speaker, master)
                if resolved not in present_set:
                    errors.append(f"Escena {sid}: hablante '{speaker}' no está en characters_present[].")
        key_object = extract_key_object(scene)
        if not key_object:
            warnings.append(f"Escena {sid}: sin key_object explícito (la viñeta queda genérica).")
        panel = str(scene.get("storyboard_panel") or "").strip()
        panel_flat = re.sub(r"\s+", " ", panel)
        first_cut = (scene.get("internal_cuts") or [{}])[0]
        first_framing = str(first_cut.get("framing") or "").strip()
        first_action = re.sub(r"\s+", " ", str(first_cut.get("action") or "")).strip().rstrip(".")
        if not panel.startswith("[00s-03s]"):
            errors.append(f"Escena {sid}: storyboard_panel ausente o sin rango [00s-03s].")
        if first_framing and first_framing not in panel_flat:
            errors.append(f"Escena {sid}: storyboard_panel no coincide con el encuadre de Toma 1.")
        if first_action and first_action not in panel_flat:
            errors.append(f"Escena {sid}: storyboard_panel no coincide con la acción de Toma 1.")
        scene_location = str(scene.get("location") or "").strip()
        if scene_location and scene_location not in panel_flat:
            errors.append(f"Escena {sid}: storyboard_panel no incluye la ubicación de la escena.")
        if key_object and key_object not in panel_flat:
            errors.append(f"Escena {sid}: storyboard_panel no incluye el key_object.")
        anchors = str(scene.get("character_anchors") or "").strip()
        cast_index = canonical_cast(master)
        for cid in present:
            name = str((cast_index.get(cid) or {}).get("name") or cid)
            if name not in panel:
                errors.append(f"Escena {sid}: storyboard_panel no incluye a {name}.")
            if name not in anchors:
                errors.append(f"Escena {sid}: character_anchors no incluye a {name}.")
        future = scene.get("continuity_future_refs") or []
        if future:
            errors.append(f"Escena {sid}: continuidad con spoiler futuro: {future[0][:70]}")
        if scene_location and not location_keyword_match(scene_location, master):
            strict(f"Escena {sid}: ubicación '{scene_location}' fuera de la taxonomía declarada.")

    for sid, name in sorted(unknown_chars):
        strict(f"Escena {sid}: personaje desconocido '{name}' (no está en characters[]).")
    for sid, speaker in sorted(unknown_speakers):
        strict(f"Escena {sid}: hablante desconocido '{speaker}' (no está en characters[]).")

    ordered = sorted(scenes, key=lambda s: int(s.get("scene_id") or 0))
    acts = [int(s.get("act") or 0) for s in ordered]
    if acts != sorted(acts):
        errors.append("Orden causal roto: los actos retroceden entre escenas consecutivas.")
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
    if runs and max(runs) < 3:
        warnings.append(
            f"Ubicaciones: {len(runs)} bloques con máximo {max(runs)} escena(s) seguida(s); "
            "la regla recomienda 3-6 escenas por bloque dramático."
        )

    if scenes:
        required = {int(k): v for k, v in (rules.get("required_beats") or {}).items() if str(k).isdigit()}
        by_id = {int(s.get("scene_id") or 0): s for s in scenes}
        for sid, beat in required.items():
            if sid in by_id and str(by_id[sid].get("beat") or "") != beat:
                warnings.append(f"Escena {sid}: beat '{by_id[sid].get('beat')}' (se esperaba '{beat}').")

    teasers = master.get("teasers")
    if not isinstance(teasers, list) or len(teasers) != 3:
        warnings.append("Se esperaban 3 teasers (60 s cada uno).")
    else:
        for t in teasers:
            ids_t = [int(i) for i in (t.get("scenes") or [])]
            if len(ids_t) != 6:
                warnings.append(f"Teaser {t.get('id')}: se esperaban 6 escenas (60 s) y hay {len(ids_t)}.")
            if ids_t and ids_t != list(range(min(ids_t), min(ids_t) + len(ids_t))):
                strict(f"Teaser {t.get('id')}: las escenas deben ser consecutivas ({ids_t}).")
            if any(not (1 <= i <= len(scenes)) for i in ids_t):
                errors.append(f"Teaser {t.get('id')}: referencia escenas fuera de rango.")

    if silent > max(2, len(scenes) // 10):
        warnings.append(f"{silent} escenas sin diálogo; el episodio puede sentirse vacío.")
    if prompts < len(scenes):
        warnings.append(f"{len(scenes) - prompts} escenas sin prompt de imagen utilizable.")
    characters = [c for c in (master.get("characters") or []) if isinstance(c, dict)]
    if not characters:
        strict("No hay characters[]: la coherencia facial y las voces no se pueden verificar.")
    elif not any(
        str(c.get("visual_reference") or c.get("reference_image") or "").strip() for c in characters
    ):
        strict(
            "Ningún personaje define visual_reference/reference_image: la coherencia facial "
            "dependerá de adjuntos manuales (ver 02 — chatgpt_reference_sheets.txt)."
        )
    return {"errors": errors, "warnings": warnings}


def merge_payloads(payloads: List[Dict[str, Any]]) -> Tuple[Dict[str, Any], List[str]]:
    """Fusiona partes del guion por scene_id: ordena, deduplica y no renumera."""
    warnings: List[str] = []
    if not payloads:
        raise NFError("No hay payloads para fusionar.")
    if len(payloads) == 1:
        return payloads[0], warnings
    full = [p for p in payloads if len(p.get("scenes") or []) == SCENE_COUNT]
    if full:
        warnings.append("Se recibieron varios JSON con 60 escenas; se usa el primero y se ignoran los demás.")
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
                warnings.append(f"scene_id {sid} duplicado al fusionar: se conserva la última aparición.")
            keyed[sid] = scene

    ordered = [keyed[sid] for sid in sorted(keyed)] + unkeyed
    merged: Dict[str, Any] = {"scenes": ordered}
    for key in ("episode", "characters", "locations", "acts", "publisher", "soundtrack"):
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
    missing = [i for i in range(1, SCENE_COUNT + 1) if i not in keyed]
    if missing:
        warnings.append(f"Faltan {len(missing)} escenas tras fusionar: {missing[:12]}{'…' if len(missing) > 12 else ''}")
    warnings.append(f"Fusionados {len(payloads)} archivos en un maestro ({len(ordered)} escenas).")
    return merged, warnings


def print_validation(result: Dict[str, List[str]]) -> bool:
    errors, warnings = result.get("errors", []), result.get("warnings", [])
    for warning in warnings[:30]:
        warn(warning)
    if len(warnings) > 30:
        warn(f"... y {len(warnings) - 30} advertencias más.")
    for error in errors:
        err(error)
    if not errors:
        ok(f"Validación superada ({len(warnings)} advertencias).")
        return True
    err(f"Validación fallida: {len(errors)} errores, {len(warnings)} advertencias.")
    return False


def extract_json_blob(text: str) -> Any:
    """Extrae el primer objeto/array JSON de una respuesta LLM con texto alrededor."""
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
    # Búsqueda por llaves equilibradas (ignora llaves dentro de strings)
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
    raise NFError("No se encontró un JSON válido en el texto. Pega solo el JSON del LLM o revisa el archivo.")


def default_teaser_ranges() -> List[List[int]]:
    return [list(range(1, 7)), list(range(21, 27)), list(range(55, 61))]


# --- Despacho de subcomandos (CLI opcional de nf_core) ---
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
        raise NFError(f"No existe el script del subcomando: {script}")
    completed = subprocess.run([sys.executable, str(script), *args])
    return int(completed.returncode)


def cmd_prepare(project: str, extra_args: Sequence[str] = ()) -> int:
    """Regenera el workflow (00), MASTER_PROMPTS (04) y el paquete Muse (05).

    Así MASTER_WORKFLOW_PROMPTS_READY.md, MASTER_PROMPTS.md y
    MUSE_PRODUCTION_PACK.md quedan siempre 100% sincronizados con el brief
    y el master_episode.json.
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
        print("Uso: python nf_core.py <subcomando> <proyecto> [opciones]")
        print("Subcomandos: prepare, " + ", ".join(sorted(SUBCOMMANDS)))
        return 0
    if args[0].lower() == "prepare":
        if len(args) < 2:
            raise NFError("Uso: python nf_core.py prepare <proyecto> [opciones]")
        return cmd_prepare(args[1], args[2:])
    return run_subcommand(args[0], args[1:])


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except NFError as exc:
        err(str(exc))
        raise SystemExit(1)

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
MAX_LINE_WORDS = 15              # tope por intervención
MIN_SCENE_WORDS = 6              # mínimo para que la escena no quede vacía
MAX_SCENE_SPEECH_SECONDS = 8.5   # la voz debe terminar antes de 8.5 s
CUT_MIN_GAP = 3.0
CUT_MAX_GAP = 4.0
DURATION_TOLERANCE_SEC = 0.05
SHOT_CUT_TIMES = (0.0, 3.0, 7.0)
SHOT_RANGES = ("00s-03s", "03s-07s", "07s-10s")
DIALOGUE_END_DEADLINE_SEC = 8.5

# --- Contrato v2: hablante por toma, objeto visible y texto diegético ---
MAX_SCENE_CAST = 3               # personajes distintos por escena/prompt
MAX_DIALOGUE_LINES_PER_SCENE = 2 # 2 líneas por clip de 10 s
MAX_CUTS_PER_SCENE = 4
OBJECT_FOCUS_MIN_SECONDS = 2.0   # insert del hallazgo, mínimo en cámara
SPEECH_PAD_SECONDS = 0.45        # aire antes/después de una línea
SPEECH_GAP_SECONDS = 0.35        # pausa entre dos líneas en el mismo plano
SCENE_TEXT_SAFE_CLAUSE = (
    "No subtitles, no captions, no overlay text, no watermark, no signage, no UI text."
)
SCENE_TEXT_HIDDEN_CLAUSE = (
    "Any paper, document, letter or sign in frame must show no legible words; "
    "do not invent readable text."
)

# --- Contrato v3: ReelShort/DramaBox (fuente probada, puentes, rotación, ritmo) ---
DEFAULT_CLIFFHANGER_ROTATION = ("identity", "emotion", "revelation")
PRODUCTION_ATTACH_NOTE = (
    "ADJUNTA EN CADA ESCENA: la viñeta de esa escena + las referencias SOLO de los "
    "personajes que salen en ESA escena + el prompt de esa escena. "
    "No generes ninguna escena sin sus personajes adjuntos."
)
FORBIDDEN_TRANSLATION_RE = re.compile(
    r"\b(?:you\s+dare|ceo\s+[A-Z][a-z]+|president\s+[A-Z][a-z]+)\b",
    re.IGNORECASE,
)
NON_CONFRONTATIONAL_BEAT_PATTERNS = re.compile(
    r"\b(?:decision|decisi[oó]n|solo|solitari[oa]|discovery|descubrimiento|plan|planning|"
    r"tender|tierno|tierna|vulnerable|intimacy|intimidad|romance|rom[aá]ntic[oa]|wound|herida|"
    r"revelation|revelaci[oó]n|hallazgo|investigat|reflec|alivio|curiosidad|esperanza|"
    r"world_and_wound|setup[-_]stakes|setup)\b",
    re.IGNORECASE,
)
CONFRONTATION_BEAT_PATTERNS = re.compile(
    r"\b(?:confront|confrontaci[oó]n|face[-_]?slap|argument|fight|clash|crisis|brawl|standoff)\b",
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


def scene_dialogue_lines(scene: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Normaliza el diálogo a [{speaker,line,delivery,shot,recipient}]."""
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
    """Nombre de archivo canónico de la hoja de referencia: reference_<id>.png."""
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
        anchors.append(_anchor_with_position(character, f"Cast Sheet Pos #{pos}:", act, scene))
    return "; ".join(anchors)


def build_storyboard_panel_description(scene: Dict[str, Any], master: Dict[str, Any]) -> str:
    """Describe la viñeta que DEBE ser el primer frame de la Toma 1."""
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
    """True si el texto es un relleno mecánico de cámara o continuidad."""
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
    """Acción visual concreta cuando el LLM no la entregó."""
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
    """Fuerza exactamente 3 tomas: 00s-03s, 03s-07s y 07s-10s.

    Toma 1 conserva el encuadre de la viñeta y arranca en movimiento. Toma 2 se
    corrige a close-up/OTS si el dato no pertenece a esa familia. Toma 3 se
    corrige a reacción/insert si el dato no pertenece a esa familia. Los
    placeholders mecánicos se sustituyen por acciones concretas de la escena.
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
# Contrato v2: una línea = un plano con hablante visible + objeto asegurado
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
    r"\b(?:hair|braid|braided|bob|ponytail|bun|curls?|curly|wavy|straight|"
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
    """IDs nombrados o tratados en una línea (Mr. Blackwell -> los Blackwell)."""
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
    """Una línea que nombra/trata a X no puede ser dicha por X (nadie se llama a sí mismo)."""
    speaker_cid = resolve_speaker(str(speaker or ""), master) or str(speaker or "").strip()
    if not speaker_cid:
        return None
    for cid in _line_addressed_ids(line, master):
        if _same_character(cid, speaker_cid, master):
            name = _display_name(cid, master)
            return f'la línea "{line}" nombra a {name}; {name} no puede decirla.'
    return None


def character_prompt_anchor(character: Dict[str, Any], act: int, scene: Optional[Dict[str, Any]] = None) -> str:
    """3 discriminadores que existen en la imagen: edad aprox., peinado y vestuario.

    No inventa color de ojos, tono de piel, complexión ni calzado no visible.
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
        hair = "hair as shown in the reference sheet"
    if not age:
        age = "age as shown in the reference sheet"
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
    """True si el plano puede sostener una línea con labios visibles."""
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
    recipient_text = recipient or "the other person in frame"
    base = _strip_quotes(base)
    if two_shot_with:
        first = (
            f"{speaker} and {two_shot_with} face each other in a two-shot, "
            "both faces and mouths fully visible, each oriented toward the other."
        )
    else:
        first = (
            f"{speaker} is on camera with face and mouth fully visible, "
            f"looking at {recipient_text}."
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
    if explicit:
        resolved = resolve_speaker(explicit, master) or explicit
        return _display_name(resolved, master)
    addressed = [cid for cid in _line_addressed_ids(line, master) if not _same_character(cid, speaker_cid, master)]
    for cid in addressed:
        if cid in speakers:
            return _display_name(cid, master)
    if addressed:
        return _display_name(addressed[0], master)
    for cid in speakers:
        if not _same_character(cid, speaker_cid, master):
            return _display_name(cid, master)
    for cid in present:
        if not _same_character(cid, speaker_cid, master):
            return _display_name(cid, master)
    return "the other person in frame"


def _cut_range(a: float, b: float) -> str:
    return f"{int(round(a)):02d}s-{int(round(b)):02d}s"


def _retime_cuts(
    cuts: List[Dict[str, Any]],
    total: float = SCENE_SECONDS,
    lines: Optional[Sequence[Dict[str, Any]]] = None,
) -> List[Dict[str, Any]]:
    """Reparte 10 s entre tomas: cada línea conserva su tiempo de habla."""
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


def _planting_details(scene: Dict[str, Any]) -> Optional[Dict[str, str]]:
    text = _scene_lock_text(scene)
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


def _apply_object_ledger(scene: Dict[str, Any], ledger: Dict[str, Any], master: Dict[str, Any]) -> None:
    text = _scene_lock_text(scene)
    details = _planting_details(scene)
    if details:
        container = details["container"]
        obj = details["object"]
        scene["planted_object"] = obj
        scene["planted_in"] = container
        scene["planted_by"] = details["by"]
        scene["key_object"] = obj
        scene["object_focus"] = "plant"
        scene["object_hidden"] = False
        scene["object_start"] = {
            "name": container,
            "visible": "hanging open at the edge of frame, its interior out of focus",
        }
        scene["object_end"] = {
            "name": obj,
            "visible": f"inside {container} in a silent insert, placed by {details['by'] or 'the hand'}",
        }
        ledger[details["container_key"]] = {
            "object": obj,
            "object_key": details["object_key"],
            "container": container,
            "hidden": True,
            "revealed": False,
        }
        diegetic_text_for_scene(scene)
        return

    entry: Optional[Dict[str, Any]] = None
    for key, value in ledger.items():
        if not key or not isinstance(value, dict):
            continue
        if _contains_name(text, key) or key.lower() in text.lower():
            entry = value
            break
    if entry:
        obj = str(entry.get("object") or "").strip()
        obj_key = str(entry.get("object_key") or "").strip().lower()
        container = str(entry.get("container") or "").strip()
        reveals = bool(REVEAL_RE.search(text)) and (
            obj_key in text.lower() or _contains_name(text, obj)
        )
        if reveals:
            scene["object_focus"] = "reveal"
            scene["object_hidden"] = False
            scene["key_object"] = obj or extract_key_object(scene)
            scene["object_start"] = {
                "name": obj,
                "visible": f"inside {container}, its chain catching the light at the frame edge",
            }
            scene["object_end"] = {
                "name": obj,
                "visible": "hanging in the hand, centered, at least 2 seconds on screen",
            }
            entry["hidden"] = False
            entry["revealed"] = True
        else:
            scene["object_hidden"] = True
            if not extract_key_object(scene):
                scene["key_object"] = container
            scene["object_start"] = {
                "name": container,
                "visible": "loosened, the interior in shadow and out of frame",
                "contains": obj,
            }
            scene["object_end"] = {
                "name": container,
                "visible": "in frame at the end, its interior never shown",
                "contains": obj,
            }
        diegetic_text_for_scene(scene)
        return

    scene["object_hidden"] = False
    obj = extract_key_object(scene)
    if obj:
        scene["object_start"] = {"name": obj, "visible": "in frame at the start of the scene"}
        scene["object_end"] = {"name": obj, "visible": "in frame at the end of the scene"}
        if REVEAL_RE.search(text):
            scene["object_focus"] = "reveal"
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
    """Deriva en memoria el contrato v2 (no reescribe el proyecto en disco)."""
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
    """Copia del maestro con todas las escenas preparadas para el contrato v2."""
    if not isinstance(master, dict):
        raise NFError("prepare_master_locks espera un JSON maestro.")
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
    """``prepare_master_locks`` solo cuando el contrato v2 aplica; maestros legados intactos."""
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
    """Regla 4: el nombre exacto del key_object también vive en la Toma 1."""
    key_object = str((scene.get("object_start") or {}).get("name") or "").strip() or extract_key_object(scene)
    cuts = scene.get("internal_cuts") or []
    if not key_object or not isinstance(cuts, list) or not cuts or not isinstance(cuts[0], dict):
        return
    action = str(cuts[0].get("action") or "")
    if key_object.lower() in action.lower():
        return
    cuts[0]["action"] = f"{action.rstrip(' .')}. Key object in frame: {key_object}."


def _coerce_narrative_continuity(
    scene: Dict[str, Any],
    previous: Optional[Dict[str, Any]],
) -> None:
    """Rellena la cadena causal de una escena cuando el LLM no la entregó.

    ``because_previous_ended_with`` se ancla SIEMPRE al cambio de estado de la
    escena anterior para que la cadena sea verificable y no una paráfrasis.
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
    """Construye los 10 bloques de 1 minuto con su única pregunta motriz."""
    rules = rules if isinstance(rules, dict) else load_showrunner()
    engine = rules.get("narrative_continuity_engine") or {}
    if not engine or not engine.get("enabled", True):
        return {}
    scenes = ordered_scenes(master)
    per_block = int(engine.get("scenes_per_block") or 6)
    total_blocks = int(engine.get("minute_blocks") or 10)
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
        "minute_blocks": blocks,
    }


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


def _should_apply_v2(master: Dict[str, Any]) -> bool:
    """Solo si hay reparto y al menos un hablante resoluble (no rompe fixtures)."""
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
    master["partial"] = len(scenes) != SCENE_COUNT
    master["teasers"] = _normalize_teasers(payload, scenes, warnings)
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
            "source_mode: 'original_unproven' — guion generado sin fuente probada (source_script). "
            "ReelShort/DramaBox exigen adaptar historias probadas para garantizar retención."
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
    """Reglas del contrato v2: hablante por toma, mute list, objeto y texto."""
    cuts = [c for c in (scene.get("internal_cuts") or []) if isinstance(c, dict)]
    lines = scene_dialogue_lines(scene)
    present = [str(cid) for cid in (scene.get("characters_present") or [])]
    if len(present) > MAX_SCENE_CAST:
        strict(f"Escena {sid}: {len(present)} personajes en escena; el máximo del prompt es {MAX_SCENE_CAST}.")
    if len(lines) > MAX_DIALOGUE_LINES_PER_SCENE:
        strict(f"Escena {sid}: {len(lines)} líneas de diálogo; el máximo por clip es {MAX_DIALOGUE_LINES_PER_SCENE}.")
    if not lines and any(cut.get("dialogue") for cut in cuts):
        strict(f"Escena {sid}: hay una toma marcada como diálogo sin líneas.")
    speakers: List[str] = []
    for entry in lines:
        cid = resolve_speaker(entry.get("speaker") or "", master) or str(entry.get("speaker") or "").strip()
        if cid and cid not in speakers:
            speakers.append(cid)
    for index, entry in enumerate(lines):
        shot = int(entry.get("shot") or 0)
        if not 1 <= shot <= len(cuts):
            strict(f"Escena {sid}: línea {index + 1} sin toma asignada.")
            continue
        cut = cuts[shot - 1]
        if not cut.get("dialogue"):
            strict(f"Escena {sid}: línea {index + 1} cae en una toma marcada como silencio.")
        if not face_visible_in_cut(cut):
            strict(f"Escena {sid}: línea {index + 1} cae en un plano sin rostro y boca visibles.")
        speaker = entry.get("speaker") or ""
        if not speaker:
            strict(f"Escena {sid}: línea {index + 1} sin hablante.")
        else:
            ownership = line_ownership_error(entry.get("line") or "", speaker, master)
            if ownership:
                strict(f"Escena {sid}: {ownership}")
            if not _cut_mentions(cut, speaker, master):
                strict(f"Escena {sid}: la toma de la línea {index + 1} no nombra al hablante '{speaker}'.")
            recipient = str(entry.get("recipient") or "").strip()
            if not recipient:
                strict(f"Escena {sid}: línea {index + 1} sin destinatario.")
            elif _same_character(recipient, speaker, master):
                strict(f"Escena {sid}: línea {index + 1} se habla a sí misma.")
    shots = [int(entry.get("shot") or 0) for entry in lines]
    if shots != sorted(shots):
        strict(f"Escena {sid}: las líneas no están en orden de aparición ({shots}).")
    seen: List[str] = []
    for entry in lines:
        flat = re.sub(r"[^a-z0-9 ]", "", str(entry.get("line") or "").lower()).strip()
        if flat and flat in seen:
            strict(f"Escena {sid}: una línea aparece más de una vez en la escena.")
        seen.append(flat)
    for cid in scene.get("present_silent") or []:
        if any(_same_character(str(cid), speaker, master) for speaker in speakers):
            strict(f"Escena {sid}: '{cid}' está en la lista de mudos y también habla.")
    for cut in cuts:
        if cut.get("dialogue"):
            continue
        action = str(cut.get("action") or "")
        if re.search(r'"[^"]+"', action) or SPEAKING_VERB_RE.search(action):
            strict(f"Escena {sid}: una toma silenciosa contiene diálogo o la acción de hablar.")
    start = scene.get("object_start") or {}
    end = scene.get("object_end") or {}
    if not str(start.get("name") or "").strip():
        strict(f"Escena {sid}: falta el bloque OBJETO AL INICIAR.")
    if not str(end.get("name") or "").strip():
        strict(f"Escena {sid}: falta el bloque OBJETO AL TERMINAR.")
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
            strict(f"Escena {sid}: el hallazgo de '{obj}' no tiene toma propia sin diálogo.")
        else:
            index, _cut = focus_cut
            duration = _cut_end_seconds(cuts, index) - float(cuts[index].get("at") or 0.0)
            if duration < OBJECT_FOCUS_MIN_SECONDS - 0.05:
                strict(
                    f"Escena {sid}: la toma del hallazgo dura {duration:.1f}s; "
                    f"mínimo {OBJECT_FOCUS_MIN_SECONDS:.1f}s."
                )
    if scene.get("object_hidden"):
        for cut in cuts:
            text = _cut_text(cut).lower()
            if re.search(r"\b(?:empty|interior|leather tools|inside the bag)\b", text):
                if "out of frame" not in text and "shadow" not in text:
                    strict(f"Escena {sid}: una toma muestra el interior o la ausencia de un objeto oculto.")
    for text in scene.get("diegetic_text") or []:
        if str(text) != str(text).upper():
            strict(f"Escena {sid}: el texto diegético '{text}' debe ir en mayúsculas exactas.")


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

    if master.get("source_mode") == "original_unproven":
        warnings.append(
            "source_mode: 'original_unproven' — Guion no probado. Falta 'source_script'."
        )

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
            errors.append(f"Escena {sid}: act inválido.")
        prompt = str(scene.get("first_frame_prompt") or "")
        if len(prompt) < 60:
            errors.append(f"Escena {sid}: first_frame_prompt demasiado corto ({len(prompt)} chars).")
        else:
            prompts += 1
        cuts = scene.get("internal_cuts")
        v2_scene = str(scene.get("shot_lock_version") or "") == "2" or production
        if not isinstance(cuts, list) or not (1 <= len(cuts) <= MAX_CUTS_PER_SCENE):
            errors.append(
                f"Escena {sid}: se requieren entre 1 y {MAX_CUTS_PER_SCENE} tomas; hay "
                f"{len(cuts) if isinstance(cuts, list) else 0}."
            )
        else:
            ats = [float(c.get("at") or 0.0) for c in cuts]
            if abs(ats[0]) > 1e-6:
                errors.append(f"Escena {sid}: la primera toma debe empezar en 0.0 s.")
            if any(b <= a for a, b in zip(ats, ats[1:])):
                errors.append(f"Escena {sid}: los cortes deben ser crecientes ({ats}).")
            if ats[-1] >= scene_seconds:
                errors.append(f"Escena {sid}: el último corte {ats[-1]} debe caer antes de {scene_seconds} s.")
            for cut_no, cut in enumerate(cuts, start=1):
                if not str((cut or {}).get("action") or "").strip():
                    errors.append(f"Escena {sid}: Toma {cut_no} sin acción.")
                if is_placeholder_text(str((cut or {}).get("action") or "")):
                    errors.append(
                        f"Escena {sid}: Toma {cut_no} usa un placeholder mecánico de cámara."
                    )
            first = cuts[0] if isinstance(cuts[0], dict) else {}
            if not v2_scene:
                if len(cuts) != 3:
                    errors.append(f"Escena {sid}: se requieren exactamente 3 tomas (00s-03s, 03s-07s, 07s-10s).")
                else:
                    second = cuts[1] if isinstance(cuts[1], dict) else {}
                    third = cuts[2] if isinstance(cuts[2], dict) else {}
                    if not CLOSEUP_RE.search(str(second.get("framing") or "")):
                        errors.append(f"Escena {sid}: Toma 2 debe ser close-up u over-the-shoulder.")
                    if not REACTION_RE.search(str(third.get("framing") or "")):
                        errors.append(f"Escena {sid}: Toma 3 debe ser tight close-up, reacción o insert.")
            if not str(first.get("action") or "").strip():
                errors.append(f"Escena {sid}: Toma 1 sin acción de arranque en movimiento.")
            elif STATIC_RE.search(str(first.get("action") or "")) and not v2_scene:
                errors.append(f"Escena {sid}: Toma 1 describe un frame estático; debe arrancar en movimiento.")
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
            line_val = str(entry.get("line") or "")
            trans_match = FORBIDDEN_TRANSLATION_RE.search(line_val)
            if trans_match:
                strict(
                    f"Escena {sid}: artefacto de traducción literal prohibido ('{trans_match.group(0)}') "
                    "en diálogo. Escribe en inglés idiomático con contracciones."
                )
        key_object = extract_key_object(scene)
        if not key_object:
            warnings.append(f"Escena {sid}: sin key_object explícito (la viñeta queda genérica).")
        first_object = str((scene.get("object_start") or {}).get("name") or "").strip() or key_object
        panel = str(scene.get("storyboard_panel") or "").strip()
        panel_flat = re.sub(r"\s+", " ", panel)
        first_cut = (scene.get("internal_cuts") or [{}])[0]
        first_framing = str(first_cut.get("framing") or "").strip()
        first_action = re.sub(r"\s+", " ", str(first_cut.get("action") or "")).strip().rstrip(".")
        if not re.match(r"^\[\d{2}s-\d{2}s\]", panel):
            errors.append(f"Escena {sid}: storyboard_panel ausente o sin rango de tiempo.")
        if first_framing and first_framing not in panel_flat:
            errors.append(f"Escena {sid}: storyboard_panel no coincide con el encuadre de Toma 1.")
        if first_action and first_action not in panel_flat:
            errors.append(f"Escena {sid}: storyboard_panel no coincide con la acción de Toma 1.")
        scene_location = str(scene.get("location") or "").strip()
        if scene_location and scene_location not in panel_flat:
            errors.append(f"Escena {sid}: storyboard_panel no incluye la ubicación de la escena.")
        if first_object and first_object not in panel_flat:
            errors.append(f"Escena {sid}: storyboard_panel no incluye el objeto de arranque.")
        if first_object and first_object.lower() not in first_action.lower():
            errors.append(f"Escena {sid}: la acción de Toma 1 no usa el objeto de arranque.")
        anchors = str(scene.get("character_anchors") or "").strip()
        cast_index = canonical_cast(master)
        panel_cast = present[:MAX_SCENE_CAST] if v2_scene else present
        for cid in panel_cast:
            name = str((cast_index.get(cid) or {}).get("name") or cid)
            if name not in panel:
                errors.append(f"Escena {sid}: storyboard_panel no incluye a {name}.")
            if name not in anchors:
                errors.append(f"Escena {sid}: character_anchors no incluye a {name}.")
        if v2_scene:
            _validate_scene_v2(scene, master, sid, strict)
        future = scene.get("continuity_future_refs") or []
        if future:
            errors.append(f"Escena {sid}: continuidad con spoiler futuro: {future[0][:70]}")
        if scene_location and not location_keyword_match(scene_location, master):
            strict(f"Escena {sid}: ubicación '{scene_location}' fuera de la taxonomía declarada.")
        if engine:
            for field in ("because_previous_ended_with", "this_scene_starts_with", "single_change_at_end"):
                value = str(scene.get(field) or "").strip()
                if not value:
                    errors.append(f"Escena {sid}: falta el campo de continuidad '{field}'.")
                elif len(value) < int(chain_rule.get("min_chars_per_field") or 24):
                    errors.append(f"Escena {sid}: '{field}' es demasiado corto para probar causalidad.")
                elif is_placeholder_text(value):
                    errors.append(f"Escena {sid}: '{field}' contiene un placeholder mecánico.")

            exit_hook = str(scene.get("exit_hook") or "").strip()
            if not exit_hook:
                strict(f"Escena {sid}: falta el campo 'exit_hook'.")
            elif len(exit_hook) < 15:
                strict(f"Escena {sid}: 'exit_hook' es demasiado corto para empujar a la siguiente escena.")
            elif is_placeholder_text(exit_hook):
                errors.append(f"Escena {sid}: 'exit_hook' contiene un placeholder mecánico.")

            if sid >= 2:
                entry_bridge = str(scene.get("entry_bridge") or "").strip()
                if not entry_bridge:
                    strict(f"Escena {sid}: falta el campo 'entry_bridge'.")
                elif len(entry_bridge) < 15:
                    strict(f"Escena {sid}: 'entry_bridge' es demasiado corto para servir de puente causal.")
                elif is_placeholder_text(entry_bridge):
                    errors.append(f"Escena {sid}: 'entry_bridge' contiene un placeholder mecánico.")

    for sid, name in sorted(unknown_chars):
        strict(f"Escena {sid}: personaje desconocido '{name}' (no está en characters[]).")
    for sid, speaker in sorted(unknown_speakers):
        strict(f"Escena {sid}: hablante desconocido '{speaker}' (no está en characters[]).")

    ordered = sorted(scenes, key=lambda s: int(s.get("scene_id") or 0))
    acts = [int(s.get("act") or 0) for s in ordered]
    if acts != sorted(acts):
        errors.append("Orden causal roto: los actos retroceden entre escenas consecutivas.")
    for index, scene in enumerate(ordered):
        sid = int(scene.get("scene_id") or 0)
        if index == 0:
            continue
        previous = ordered[index - 1]
        expected = str(previous.get("single_change_at_end") or "").strip()
        actual = str(scene.get("because_previous_ended_with") or "").strip()
        if engine and expected and actual != expected:
            errors.append(
                f"Escena {sid}: 'because_previous_ended_with' no coincide con el cambio "
                f"final de la escena {previous.get('scene_id')}."
            )
        if str(scene.get("this_scene_starts_with") or "").strip() == str(
            scene.get("single_change_at_end") or ""
        ).strip():
            errors.append(f"Escena {sid}: la escena empieza y termina en el mismo estado.")
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
                f"Escenas {index - 1}-{index + 1}: ping-pong de locaciones "
                f"({bases[index]} -> {bases[index - 1]} -> {bases[index]})."
            )
    if engine:
        nc = master.get("narrative_continuity") if isinstance(master.get("narrative_continuity"), dict) else {}
        blocks = nc.get("minute_blocks") if isinstance(nc.get("minute_blocks"), list) else []
        expected_blocks = int(engine.get("minute_blocks") or 10)
        if len(blocks) != expected_blocks:
            errors.append(
                f"Continuidad: se esperaban {expected_blocks} bloques de 1 minuto y hay {len(blocks)}."
            )
        for block in blocks:
            if not isinstance(block, dict):
                errors.append("Continuidad: bloque de 1 minuto con formato inválido.")
                continue
            question = str(block.get("driving_question") or "").strip()
            if not question:
                errors.append(f"Continuidad: bloque {block.get('block')} sin driving_question.")
            elif is_placeholder_text(question):
                errors.append(f"Continuidad: bloque {block.get('block')} usa una pregunta de relleno.")
            elif len(question.split()) > int(
                ((engine_rules.get("1_single_driving_question_per_block") or {}).get("question_max_words")) or 24
            ):
                errors.append(f"Continuidad: la pregunta del bloque {block.get('block')} excede el máximo de palabras.")
            ids = [int(i) for i in (block.get("scenes") or []) if str(i).isdigit()]
            if len(ids) != int(engine.get("scenes_per_block") or 6):
                errors.append(
                    f"Continuidad: bloque {block.get('block')} no cubre "
                    f"{engine.get('scenes_per_block') or 6} escenas."
                )
    if runs and max(runs) < 3:
        warnings.append(
            f"Ubicaciones: {len(runs)} bloques con máximo {max(runs)} escena(s) seguida(s); "
            "la regla recomienda 3-6 escenas por bloque dramático."
        )

    # Regla de ritmo por bloque (6 escenas): PROHIBIDO 6 picos de confrontación seguidos
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
                        f"Ritmo: bloque {block_no} (escenas {group[0].get('scene_id')}-{group[-1].get('scene_id')}) "
                        "tiene 6 picos de confrontación seguidos. Prohibido: se requiere al menos 1 beat no confrontacional "
                        "por bloque (decisión en solitario, descubrimiento, plan, momento tierno/vulnerable)."
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
                    f"Continuidad: bloques {i + 1} y {i + 2} repiten el tipo de cliffhanger '{c1}'. "
                    "Prohibido repetir el mismo tipo en dos bloques seguidos (rotar entre identity, emotion, revelation)."
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
        warnings.append(
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

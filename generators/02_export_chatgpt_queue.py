#!/usr/bin/env python3
"""02 — Exporta la cola de fotogramas iniciales para la extensión de ChatGPT.

Genera tres artefactos en la carpeta del episodio:
  chatgpt_image_prompts_queue.txt          -> 1 prompt por línea (cola automática)
  chatgpt_image_prompts_queue_labeled.txt  -> legible, con el nombre de archivo esperado
  chatgpt_image_prompts_queue.json         -> índice máquina-legible

El prompt final = cuerpo del maestro + sufijo de estilo global (una sola vez) +
cláusula anti-texto. Cada línea corresponde EXACTAMENTE a:
  frames/frame_001.png ... frames/frame_060.png

No abre navegadores, no toca sesiones de ChatGPT y no descarga nada: solo escribe
texto local que tú pegas (o tu extensión de cola lee) en orden.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

NF_ROOT = Path(__file__).resolve().parent.parent
GENERATORS_DIR = Path(__file__).resolve().parent
for _path in (NF_ROOT, GENERATORS_DIR):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))
import nf_core as nf  # noqa: E402
import master_prompts_library as mpl  # noqa: E402

SUFFIX_MARKER = "35mm anamorphic glass"
NO_TEXT_CLAUSE = ("No text, no letters, no logos, no watermarks, no captions inside the image. "
                  "No border and no UI elements.")
SHEET_TEMPLATE = (
    "Photorealistic character reference sheet of {name}: three views of the same person on one wide "
    "16:9 image — front view, three-quarter view and profile view of the head and shoulders — "
    "identical face in all three views, neutral medium-grey seamless studio background, even soft key "
    "light with gentle falloff, neutral expression. {visual_reference} Keep the exact same face, "
    "hairline and features in every view. No other people. No text, no letters, no labels, no "
    "watermark. Natural skin texture, no airbrushing, no plastic skin, no CGI sheen."
)


def build_reference_sheets(master: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Hojas de referencia (PASO 0): una por personaje, se generan UNA vez antes de la cola.

    Un personaje participa si define `visual_reference` (descripción de casting -> prompt de hoja)
    o `reference_image` (ya tiene imagen propia -> solo se adjunta, no se genera).
    """
    sheets: List[Dict[str, Any]] = []
    for character in master.get("characters") or []:
        if not isinstance(character, dict):
            continue
        cid = nf.slugify(str(character.get("id") or character.get("name") or "")) or "character"
        visual = str(character.get("visual_reference") or "").strip()
        existing = str(character.get("reference_image") or "").strip()
        if not visual and not existing:
            continue
        entry: Dict[str, Any] = {
            "id": cid,
            "name": str(character.get("name") or cid),
            "filename": nf.reference_stem({"id": cid, "name": character.get("name")}),
            "existing_image": existing,
            "prompt": "",
        }
        if visual and not existing:
            entry["prompt"] = SHEET_TEMPLATE.format(name=entry["name"], visual_reference=visual)
        sheets.append(entry)
    return sheets


def write_reference_sheets(paths: Dict[str, Path], master: Dict[str, Any], sheets: List[Dict[str, Any]]) -> Path:
    ep = nf.episode_meta(master)
    refs_dir = paths.get("references") or (paths["root"] / "references")
    lines = [
        f"NOVEL FACTORY — Hojas de referencia de personajes (PASO 0) · {ep.get('title') or ep.get('slug')}",
        "",
        "Esto se genera UNA sola vez por episodio, ANTES de la cola de frames:",
        "  1. Abre una conversación nueva de ChatGPT con generación de imágenes.",
        "  2. Pega el prompt de cada personaje; guarda el resultado en la carpeta del",
        f"     proyecto: {refs_dir}",
        "     con el nombre exacto que se indica abajo (reference_<id>.png).",
        "  3. Recorta además la cara en primer plano de cada personaje y guarda el",
        "     recorte en la misma carpeta como reference_<id>_face.png (se adjunta en las",
        "     escenas donde ese personaje HABLA).",
        "  4. Adjunta TODAS las hojas de referencia a la conversación y déjalas ahí",
        "     mientras generas frame_001.png … frame_060.png (chatgpt_image_prompts_queue.txt).",
        "     En escenas habladas adjunta también el recorte reference_<id>_face.png del hablante.",
        "  5. Los prompts de escena nombran al personaje y su archivo reference_<id>.png:",
        "     la cara nunca se describe en texto, se copia de estas hojas.",
        "",
    ]
    for sheet in sheets:
        lines.append(f"=== {sheet['name'].upper()} -> {sheet['filename']} ===")
        if sheet["prompt"]:
            lines.append(sheet["prompt"])
        else:
            lines.append(f"Ya tienes una imagen de referencia ({sheet['existing_image']}): "
                         "adjúntala a la conversación; no hace falta generarla.")
        lines.append("")
    out = paths.get("chatgpt_refs") or (paths["root"] / "chatgpt_reference_sheets.txt")
    return nf.write_text(out, "\n".join(lines))


def compose_image_prompt(body: str, style: Dict[str, Any]) -> str:
    """Cuerpo del maestro + sufijo de estilo (sin duplicar) + cláusula anti-texto.

    Si la escena trae la excepción de texto diegético (p. ej. CONFESSION), no se
    añade la cláusula genérica anti-texto: esa escena declara su único texto legible.
    """
    prompt = " ".join(str(body or "").split())
    if not prompt:
        return ""
    suffix = str((style.get("visual_style_lock") or {}).get("image_prompt_suffix") or "").strip()
    low = prompt.lower()
    if suffix and SUFFIX_MARKER not in low:
        prompt = prompt.rstrip(" .") + ". " + suffix
        low = prompt.lower()
    if "no text" not in low and "diegetic text exception" not in low:
        prompt = prompt.rstrip(" .") + ". " + NO_TEXT_CLAUSE
        low = prompt.lower()
    if "16:9" not in low:
        prompt = "16:9 widescreen cinematic still. " + prompt
    return " ".join(prompt.split())


def face_crop_name(reference: str) -> str:
    """Recorte de cara para escenas donde el personaje habla: reference_<id>_face.png."""
    value = str(reference or "").strip()
    if value.lower().endswith(".png"):
        return value[:-4] + "_face.png"
    return value + "_face.png" if value else ""


def scene_cast_entries(master: Dict[str, Any], scene: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Reparto canónico de la escena con posición fija y hoja de referencia."""
    positions = nf.character_position_map(master)
    out: List[Dict[str, Any]] = []
    for character in nf.scene_cast(master, scene):
        cid = str(character.get("id") or nf.slugify(str(character.get("name") or "")))
        out.append({
            "id": cid,
            "name": str(character.get("name") or character.get("id") or ""),
            "position": int(positions.get(cid, 0)),
            "reference": nf.reference_stem(character),
        })
    return out


def _identity_anchor(cast: List[Dict[str, Any]]) -> str:
    if not cast:
        return ""
    names = ", ".join(
        f"{c['name']} (Cast Sheet Pos #{c.get('position') or '?'}; {c['reference']})"
        for c in cast
    )
    return f"On screen: {names}. Keep every face, cast position and wardrobe identical to the attached reference sheets."


def teaser_cover_scenes(master: Dict[str, Any]) -> List[int]:
    """Primera escena de cada teaser: portada candidata 9:16."""
    covers: List[int] = []
    for teaser in master.get("teasers") or []:
        if not isinstance(teaser, dict):
            continue
        ids = [int(i) for i in (teaser.get("scenes") or []) if str(i).strip().isdigit()]
        if ids:
            covers.append(ids[0])
    return covers


def build_queue(master: Dict[str, Any], style: Dict[str, Any]) -> List[Dict[str, Any]]:
    covers = set(teaser_cover_scenes(master))
    entries: List[Dict[str, Any]] = []
    prepared = nf.prepare_master_locks_safe(master, style)
    for scene in nf.ordered_scenes(prepared):
        sid = int(scene.get("scene_id") or 0)
        cast = scene_cast_entries(master, scene)
        speaking = {
            str(nf.resolve_speaker(entry.get("speaker") or "", master) or "").strip()
            for entry in nf.scene_dialogue_lines(scene)
            if str(entry.get("speaker") or "").strip()
        }
        for character in cast:
            character["speaks"] = character["id"] in speaking
            character["face_crop"] = face_crop_name(character["reference"]) if character["speaks"] else ""
        body = str(scene.get("first_frame_prompt") or "")
        panel = str(scene.get("storyboard_panel") or nf.build_storyboard_panel_description(scene, master)).strip()
        anchors = str(
            scene.get("character_anchors")
            or nf.format_character_anchors(scene, master.get("characters_locked") or master.get("characters") or [])
        ).strip()
        if panel:
            body = (body.rstrip(" .") + ". Storyboard panel (exact first frame of Shot 1): " + panel).strip()
        if anchors:
            body = (body.rstrip(" .") + ". Identity anchors: " + anchors).strip()
        if cast and "reference_" not in body.lower():
            body = (body.rstrip(" .") + ". " + _identity_anchor(cast)).strip()
        entries.append({
            "index": sid,
            "scene_id": sid,
            "filename": f"{nf.frame_stem(sid)}.png",
            "shot": str((scene.get("internal_cuts") or [{}])[0].get("framing") or ""),
            "location": str(scene.get("location") or ""),
            "cast": cast,
            "references": [c["reference"] for c in cast],
            "face_crops": [c["face_crop"] for c in cast if c.get("face_crop")],
            "teaser_cover": sid in covers,
            "prompt": compose_image_prompt(body, style),
        })
    return entries


def write_queue_files(paths: Dict[str, Path], master: Dict[str, Any], entries: List[Dict[str, Any]]) -> None:
    ep = nf.episode_meta(master)
    title = ep.get("title") or ep.get("slug") or "episode"

    pure = "\n".join(e["prompt"] for e in entries) + "\n"
    nf.write_text(paths["chatgpt_txt"], pure)

    labeled_lines = [
        f"NOVEL FACTORY — Cola de fotogramas iniciales (ChatGPT) · {title}",
        f"Escenas: {len(entries)} · Carpeta destino: {paths['frames']}",
        "",
    ]
    if master.get("source_mode") == "original_unproven":
        labeled_lines += [
            "⚠️ WARNING: source_mode es 'original_unproven' — Guion generado sin fuente probada.",
            "",
        ]
    labeled_lines += [
        "Cómo usarla:",
        "  0. Genera PRIMERO las hojas de referencia con chatgpt_reference_sheets.txt (una sola vez)",
        "     y adjúntalas TODAS en la conversación de ChatGPT.",
        "  1. Cada prompt nombra al personaje y su reference_<id>.png: la cara se copia de esas",
        "     hojas, nunca se describe en texto.",
        "  2. Carga chatgpt_image_prompts_queue.txt en tu extensión de cola (1 prompt por línea).",
        "  3. Guarda cada imagen generada como frame_001.png ... frame_060.png en frames/.",
        "  4. Verifica con: python generators/02_export_chatgpt_queue.py "
        f"{ep.get('slug', '')} --check --strict",
        "",
    ]
    for entry in entries:
        cast_note = ", ".join(
            f"{c['name']} (Pos #{c.get('position') or '?'}{'; habla' if c.get('speaks') else ''})"
            for c in entry["cast"]
        ) or "—"
        cover = "  [9:16 PORTADA]" if entry["teaser_cover"] else ""
        attach = ", ".join(entry.get("references") or []) or "—"
        if entry.get("face_crops"):
            attach += " + " + ", ".join(entry["face_crops"]) + " (recorte de cara del hablante)"
        labeled_lines += [
            f"=== SCENE {entry['scene_id']:03d} | {entry['filename']} | {entry['shot']} | "
            f"{entry['location']} | cast: {cast_note}{cover} ===",
            f"Adjuntar: {attach}",
            entry["prompt"],
            "",
        ]
    nf.write_text(paths["root"] / "chatgpt_image_prompts_queue_labeled.txt", "\n".join(labeled_lines))

    nf.write_json(paths["chatgpt_json"], {
        "episode": ep.get("slug"),
        "title": title,
        "count": len(entries),
        "note": "Cada prompt ya incluye el sufijo de estilo global y la cláusula anti-texto "
                "(las escenas con texto diegético declarado usan su excepción). "
                "face_crops lista los recortes reference_<id>_face.png a adjuntar en escenas habladas.",
        "items": entries,
    })


def compose_vertical_prompt(body: str, style: Dict[str, Any]) -> str:
    """Igual que el horizontal, pero forzando encuadre 9:16 (portada de teaser)."""
    prompt = compose_image_prompt(body, style)
    prompt = prompt.replace("16:9 widescreen cinematic still.", "9:16 vertical cinematic still.")
    if "9:16" not in prompt.lower():
        prompt = "9:16 vertical teaser cover. " + prompt
    return " ".join(prompt.split())


def write_thumbnail_prompts(
    paths: Dict[str, Path], master: Dict[str, Any], style: Dict[str, Any], entries: List[Dict[str, Any]]
) -> Optional[Path]:
    """Portadas 9:16 para los teasers (la primera escena de cada ventana de 6)."""
    by_id = {e["scene_id"]: e for e in entries}
    covers = teaser_cover_scenes(master)
    if not covers:
        return None
    lines = [
        "NOVEL FACTORY — Portadas de teaser 9:16 (opcional, 3 imágenes verticales)",
        "",
        "Genera estas portadas ADEMÁS de los frames 16:9 del proyecto. Mismo personaje y referencia.",
        "Nombre sugerido: thumbnail_teaser_01.png … thumbnail_teaser_03.png",
        "",
    ]
    for idx, sid in enumerate(covers, start=1):
        entry = by_id.get(sid)
        body = str(entry["prompt"]) if entry else ""
        lines += [
            f"=== TEASER {idx} | portada de scene {sid:03d} -> thumbnail_teaser_{idx:02d}.png ===",
            compose_vertical_prompt(body, style),
            "",
        ]
    out = paths.get("chatgpt_thumbs") or (paths["root"] / "chatgpt_thumbnail_prompts.txt")
    return nf.write_text(out, "\n".join(lines))


ROLE_LABELS = {
    "protagonist": "Protagonista",
    "love_interest": "Interés romántico",
    "antagonist": "Antagonista",
    "antagonist_heir": "Heredero antagonista",
    "ally": "Aliada",
    "mentor": "Mentor",
    "supporting": "Secundario",
}


def _project_characters(master: Dict[str, Any]) -> List[Dict[str, Any]]:
    raw = master.get("characters_locked") or master.get("characters") or []
    if isinstance(raw, dict):
        raw = list(raw.values())
    return [character for character in raw if isinstance(character, dict)]


def _character_role(character: Dict[str, Any]) -> str:
    role = str(character.get("role") or character.get("archetype") or "principal").strip().lower()
    return ROLE_LABELS.get(role, role or "principal")


def _character_age(character: Dict[str, Any]) -> str:
    explicit = str(character.get("age") or character.get("age_range") or character.get("apparent_age") or "").strip()
    if explicit:
        return explicit
    text = " ".join(str(character.get(key) or "") for key in (
        "visual_reference", "description", "appearance",
    ))
    patterns = (
        r"\b(?:in (?:her|his) )?((?:early|mid|late)[- ](?:twenties|thirties|forties|fifties|sixties|seventies))\b",
        r"\b(?:in (?:her|his) )?(twenties|thirties|forties|fifties|sixties|seventies)\b",
        r"\baround (thirty|forty|fifty|sixty|seventy)\b",
    )
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return match.group(1).lower().replace(" ", "-")
    return "adulto"


def _character_visual(character: Dict[str, Any]) -> str:
    visual = str(
        character.get("visual_reference")
        or character.get("description")
        or character.get("appearance")
        or ""
    ).strip()
    return visual or "rasgos y complexion definidos por su ficha de casting"


def _character_wardrobe(character: Dict[str, Any]) -> str:
    for key in ("wardrobe_lock", "wardrobe", "signature_wardrobe", "outfit_lock"):
        value = character.get(key)
        if isinstance(value, list):
            value = next((str(item).strip() for item in value if str(item).strip()), "")
        if str(value or "").strip():
            return str(value).strip()
    wardrobes = character.get("wardrobe_by_act") or []
    if isinstance(wardrobes, list):
        for item in wardrobes:
            if str(item or "").strip():
                return str(item).strip()
    match = re.search(r"signature\s+(.+?)(?:\.|$)", _character_visual(character), flags=re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return "el vestuario principal descrito en su ficha de casting"


def short_scene_brief(scene: Dict[str, Any], max_words: int = 10) -> str:
    """Resumen de 5–10 palabras para una viñeta del storyboard."""
    cuts = [c for c in (scene.get("internal_cuts") or []) if isinstance(c, dict)]
    candidates = [
        str(cuts[0].get("action") or "") if cuts else "",
        str(scene.get("on_screen_hook") or ""),
        str(scene.get("first_frame_prompt") or ""),
    ]
    text = next((c for c in candidates if c.strip()), "key story beat")
    words = " ".join(text.split()).split()
    brief = " ".join(words[:max_words]).rstrip(".,;:")
    if len(brief.split()) < 5:
        location = " ".join(str(scene.get("location") or "").split()[:4]).strip(" ,")
        if location:
            brief = f"{brief} — {location}".strip(" —")
    return brief + ("…" if len(words) > max_words else "")


def scene_breakdown_lines(master: Dict[str, Any]) -> List[str]:
    """Todas las escenas del proyecto (nunca truncadas) para PROMPT 001."""
    lines: List[str] = []
    for scene in nf.ordered_scenes(master):
        sid = int(scene.get("scene_id") or 0)
        cast = ", ".join(c["name"] for c in scene_cast_entries(master, scene)) or "—"
        dialogue = " / ".join(
            f"{entry['speaker']}: {entry['line']}" for entry in nf.scene_dialogue_lines(scene)
        ) or "—"
        lines.append(
            f"ESCENA {sid:03d} | Acto {int(scene.get('act') or 0)} | "
            f"{str(scene.get('location') or '—')} | {str(scene.get('time_of_day') or '—')} | "
            f"Hook: {str(scene.get('on_screen_hook') or '—')} | Cast: {cast} | "
            f"Diálogo: {dialogue}"
        )
    return lines


def _cast_sheet_prompt(master: Dict[str, Any], prompt_002_text: str = "") -> str:
    return mpl.build_cast_sheet_prompt(master)


def _storyboard_grid_prompt(
    master: Dict[str, Any],
    style: Dict[str, Any],
    batch_number: int,
    group: List[Dict[str, Any]],
    total_batches: int,
) -> str:
    first = int(group[0].get("scene_id") or 1)
    last = int(group[-1].get("scene_id") or first)
    visual = str((style.get("visual_style_lock") or {}).get("look") or "").strip()
    lines = [
        f"Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO {batch_number} (Escenas {first} a {last}) de la historia en estilo Cinematográfico Realista 35mm:",
        "",
    ]
    if visual:
        lines += [f"Look visual: {visual}.", ""]
    for idx, scene in enumerate(group, start=1):
        sid = int(scene.get("scene_id") or 0)
        location = str(scene.get("location") or "").strip()
        panel = str(scene.get("storyboard_panel") or nf.build_storyboard_panel_description(scene, master)).strip()
        anchors = str(
            scene.get("character_anchors")
            or nf.format_character_anchors(scene, master.get("characters_locked") or master.get("characters") or [])
        ).strip()
        place = f" ({location})" if location else ""
        lines.append(
            f"Viñeta {idx} — Escena {sid}{place}: {panel} "
            f"Identity anchors: {anchors or 'use the cast sheet positions exactly as attached'}."
        )
    lines += [
        "",
        "Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.",
        "FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.",
    ]
    return "\n".join(lines)


def build_storyboard_grid_items(
    master: Dict[str, Any],
    style: Dict[str, Any],
    pack: Optional[Dict[str, Any]] = None,
) -> List[Dict[str, Any]]:
    """Cola de imágenes: 1 hoja de casting + un storyboard de 6 viñetas por bloque."""
    pack = pack or mpl.build_prompt_pack(master, style)
    ep = nf.episode_meta(master)
    title = str(ep.get("title") or ep.get("slug") or "Episodio")
    scenes = nf.ordered_scenes(nf.prepare_master_locks_safe(master, style))
    groups = [scenes[i:i + 6] for i in range(0, len(scenes), 6)]
    total_batches = len(groups)

    cast_prompt = _cast_sheet_prompt(master)
    items: List[Dict[str, Any]] = [{
        "index": 1,
        "filename": "REF_CAST_MASTER.png",
        "kind": "cast_sheet",
        "minute": 0,
        "scenes": [],
        "title": f"Hoja maestra de personajes — {title}",
        "prompt": cast_prompt,
    }]
    for batch_number, group in enumerate(groups, start=1):
        if not group:
            continue
        first = int(group[0].get("scene_id") or 1)
        last = int(group[-1].get("scene_id") or first)
        items.append({
            "index": len(items) + 1,
            "filename": f"REF_GRID_MIN_{batch_number:02d}.png",
            "kind": "storyboard_grid",
            "minute": batch_number,
            "scenes": [int(scene.get("scene_id") or 0) for scene in group],
            "title": f"Storyboard minuto {batch_number}: escenas {first}–{last}",
            "prompt": _storyboard_grid_prompt(master, style, batch_number, group, total_batches),
        })
    return items


def render_storyboard_grid_queue_text(items: List[Dict[str, Any]]) -> str:
    """Una línea por prompt (formato de cola de la extensión de ChatGPT)."""
    return "\n".join(" ".join(str(item.get("prompt") or "").split()) for item in items) + "\n"


def write_storyboard_grid_queue(
    paths: Dict[str, Path],
    master: Dict[str, Any],
    style: Dict[str, Any],
    pack: Optional[Dict[str, Any]] = None,
) -> Dict[str, Path]:
    """Exporta la cola de imágenes (cast sheet + un grid por bloque) en .txt y .json."""
    root = paths["root"]
    ep = nf.episode_meta(master)
    items = build_storyboard_grid_items(master, style, pack)
    txt_path = paths.get("chatgpt_storyboard_grids_txt") or (root / "chatgpt_storyboard_grids_queue.txt")
    json_path = paths.get("chatgpt_storyboard_grids_json") or (root / "chatgpt_storyboard_grids_queue.json")
    nf.write_text(txt_path, render_storyboard_grid_queue_text(items))
    storyboard_count = max(0, len(items) - 1)
    nf.write_json(json_path, {
        "schema_version": "1.0",
        "episode": ep.get("slug"),
        "title": ep.get("title"),
        "count": len(items),
        "note": f"1 hoja de personajes (REF_CAST_MASTER.png) + {storyboard_count} storyboards "
                f"de 6 viñetas (REF_GRID_MIN_01.png … REF_GRID_MIN_{storyboard_count:02d}.png).",
        "items": items,
    })
    return {"txt": txt_path, "json": json_path, "items": items}


def write_master_image_prompt_files(
    paths: Dict[str, Path],
    master: Dict[str, Any],
    style: Dict[str, Any],
) -> Dict[str, Path]:
    """Exporta PROMPT 001, PROMPT 002 y la cola de imágenes del proyecto."""
    pack = mpl.build_prompt_pack(master, style)
    by_key = {prompt["key"]: prompt for prompt in pack["prompts"]}
    root = paths["root"]
    ep = nf.episode_meta(master)
    title = ep.get("title") or ep.get("slug") or "Episodio"
    grid_items = build_storyboard_grid_items(master, style, pack)
    total_scenes = len(nf.ordered_scenes(master))
    storyboard_count = max(0, len(grid_items) - 1)

    prompt_001 = paths.get("chatgpt_prompt_001") or (root / "chatgpt_prompt_001_storyboards.txt")
    prompt_002 = paths.get("chatgpt_prompt_002") or (root / "chatgpt_prompt_002_characters.txt")

    header_001 = (
        f"NOVEL FACTORY — PROMPT 001 — GENERADOR DE STORYBOARD · {title}\n"
        f"Incluye la historia completa ({total_scenes} escenas, sin truncar) y los "
        f"{storyboard_count} prompts individuales de una imagen por minuto.\n\n"
    )
    header_002 = (
        f"NOVEL FACTORY — PROMPT 002 — HOJA MAESTRA DE PERSONAJES · {title}\n"
        "Adjunta el storyboard creado con PROMPT 001 antes de pegar este prompt.\n\n"
    )
    storyboard_lines = [
        header_001.rstrip(),
        by_key["prompt_001"]["text"].strip(),
        "",
        "=" * 78,
        f"HISTORIA COMPLETA — {total_scenes} ESCENAS (SIN TRUNCAR)",
        "=" * 78,
        "",
        *scene_breakdown_lines(master),
        "",
        "=" * 78,
        f"{storyboard_count} PROMPTS INDIVIDUALES — UNA IMAGEN DE STORYBOARD POR MINUTO",
        "=" * 78,
        "",
    ]
    for item in grid_items[1:]:
        storyboard_lines += [f"=== {item['filename']} ===", item["prompt"], ""]
    nf.write_text(prompt_001, "\n".join(storyboard_lines))
    nf.write_text(prompt_002, header_002 + by_key["prompt_002"]["text"].strip() + "\n")

    grids = write_storyboard_grid_queue(paths, master, style, pack)
    return {
        "prompt_001": prompt_001,
        "prompt_002": prompt_002,
        "grids_txt": grids["txt"],
        "grids_json": grids["json"],
    }


def run_check(
    paths: Dict[str, Path],
    entries: List[Dict[str, Any]],
    allow_missing: bool,
    sheets: Optional[List[Dict[str, Any]]] = None,
    strict: bool = False,
) -> int:
    present: List[int] = []
    missing: List[int] = []
    for entry in entries:
        if nf.find_frame(paths["frames"], entry["scene_id"]):
            present.append(entry["scene_id"])
        else:
            missing.append(entry["scene_id"])
    nf.log("")
    nf.info(f"Frames presentes: {len(present)}/{len(entries)}")
    ok = True
    if missing:
        nf.warn(f"Faltan {len(missing)} frames: {', '.join(str(i) for i in missing[:20])}" +
                (" …" if len(missing) > 20 else ""))
        nf.info("Esperados como frame_XXX.png / .jpg / .jpeg / .webp en " + str(paths["frames"]))
        if not allow_missing:
            ok = False

    if sheets:
        refs_dir = paths.get("references") or (paths["root"] / "references")
        missing_refs = [s for s in sheets if not (refs_dir / s["filename"]).exists() and not s.get("existing_image")]
        if missing_refs:
            names = ", ".join(s["filename"] for s in missing_refs)
            msg = f"Faltan {len(missing_refs)} hojas de referencia en {refs_dir}: {names}"
            if strict:
                nf.err(msg)
                ok = False
            else:
                nf.warn(msg + " (usa --strict para que sea error)")
        else:
            nf.ok(f"Hojas de referencia presentes: {len(sheets)}.")

    if ok:
        nf.ok("Los fotogramas iniciales (y sus referencias) están en su sitio.")
        return 0
    return 0 if allow_missing else 1


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="02 — Cola de prompts de fotogramas para ChatGPT.")
    parser.add_argument("project", help="Slug del episodio.")
    parser.add_argument("--check", action="store_true", help="Solo verifica los frames en frames/.")
    parser.add_argument("--allow-missing", action="store_true", help="No falla si faltan frames.")
    parser.add_argument("--strict", action="store_true", help="Falla también si faltan hojas de referencia.")
    parser.add_argument("--show", type=str, default="", help="Imprime los prompts de un rango (ej: 1-3).")
    args = parser.parse_args(argv)

    nf.log("")
    nf.log("=" * 70)
    nf.log("  NOVEL FACTORY — 02 · Cola de fotogramas iniciales (ChatGPT)")
    nf.log("=" * 70)

    paths = nf.resolve_project(args.project)
    master = nf.load_master(paths["root"])
    style = nf.load_style_locks()
    entries = build_queue(master, style)
    sheets = build_reference_sheets(master)
    ep = nf.episode_meta(master)

    if not args.check:
        write_queue_files(paths, master, entries)
        image_prompts = write_master_image_prompt_files(paths, master, style)
        nf.log("")
        nf.ok(f"{len(entries)} prompts exportados:")
        nf.info(f"{paths['chatgpt_txt'].name}          (cola pura, 1 prompt por línea)")
        nf.info(f"chatgpt_image_prompts_queue_labeled.txt (con nombre de archivo por escena)")
        nf.info(f"{paths['chatgpt_json'].name}         (índice JSON)")
        grid_count = nf.master_target_minutes(master)
        nf.ok("Prompts maestros de imagen:")
        nf.info(f"{image_prompts['prompt_001'].name}  (PROMPT 001 — {len(entries)} escenas + {grid_count} grids)")
        nf.info(f"{image_prompts['prompt_002'].name}  (PROMPT 002 — hoja maestra de personajes)")
        nf.info(f"{image_prompts['grids_txt'].name}  (cola de {grid_count + 1} imágenes: 1 cast + {grid_count} grids)")
        nf.info(f"{image_prompts['grids_json'].name} (manifiesto de la cola de {grid_count + 1} imágenes)")

    if not args.check:
        if sheets:
            refs_path = write_reference_sheets(paths, master, sheets)
            to_generate = sum(1 for s in sheets if s["prompt"])
            nf.ok(f"PASO 0 — hojas de referencia: {len(sheets)} personaje(s), {to_generate} por generar.")
            nf.info(f"{refs_path.name}   (adjúntalas en ChatGPT antes de la cola)")
        else:
            nf.info("Sin visual_reference/reference_image en el maestro: adjunta tus propias imágenes de referencia.")
        thumbs = write_thumbnail_prompts(paths, master, style, entries)
        if thumbs:
            nf.ok(f"Portadas 9:16 de teaser: {thumbs.name}")

    if args.show:
        want = set(nf.parse_ranges(args.show))
        nf.log("")
        for entry in entries:
            if entry["index"] in want:
                nf.log(f"--- SCENE {entry['scene_id']:03d} -> {entry['filename']} ---")
                nf.log(entry["prompt"])
                nf.log("")

    rc = run_check(paths, entries, args.allow_missing, sheets=sheets, strict=args.strict) if (args.check or not args.show) else 0
    if not args.check and not args.show:
        nf.log("")
        nf.log(f"  Siguiente: genera los frames y confirma con --check, luego")
        nf.log(f"  python generators/03_export_omni_queue.py {args.project}")
        nf.log("")
    return rc


if __name__ == "__main__":
    try:
        sys.exit(main())
    except nf.NFError as exc:
        nf.err(str(exc))
        sys.exit(1)

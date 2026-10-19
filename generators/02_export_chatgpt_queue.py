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
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

NF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(NF_ROOT))
import nf_core as nf  # noqa: E402

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
        "Esto se genera UNA sola vez por episodio, ANTES de la cola de los 60 frames:",
        "  1. Abre una conversación nueva de ChatGPT con generación de imágenes.",
        "  2. Pega el prompt de cada personaje; guarda el resultado en la carpeta del",
        f"     proyecto: {refs_dir}",
        "     con el nombre exacto que se indica abajo (reference_<id>.png).",
        "  3. Adjunta TODAS las hojas de referencia a la conversación y déjalas ahí",
        "     mientras generas frame_001.png … frame_060.png (chatgpt_image_prompts_queue.txt).",
        "  4. Los prompts de escena nombran al personaje y su archivo reference_<id>.png:",
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
    """Cuerpo del maestro + sufijo de estilo (sin duplicar) + cláusula anti-texto."""
    prompt = " ".join(str(body or "").split())
    if not prompt:
        return ""
    suffix = str((style.get("visual_style_lock") or {}).get("image_prompt_suffix") or "").strip()
    low = prompt.lower()
    if suffix and SUFFIX_MARKER not in low:
        prompt = prompt.rstrip(" .") + ". " + suffix
        low = prompt.lower()
    if "no text" not in low:
        prompt = prompt.rstrip(" .") + ". " + NO_TEXT_CLAUSE
        low = prompt.lower()
    if "16:9" not in low:
        prompt = "16:9 widescreen cinematic still. " + prompt
    return " ".join(prompt.split())


def scene_cast_entries(master: Dict[str, Any], scene: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Reparto canónico de la escena con el nombre de archivo de su hoja de referencia."""
    out: List[Dict[str, Any]] = []
    for character in nf.scene_cast(master, scene):
        out.append({
            "id": str(character.get("id") or nf.slugify(str(character.get("name") or ""))),
            "name": str(character.get("name") or character.get("id") or ""),
            "reference": nf.reference_stem(character),
        })
    return out


def _identity_anchor(cast: List[Dict[str, Any]]) -> str:
    if not cast:
        return ""
    names = ", ".join(f"{c['name']} ({c['reference']})" for c in cast)
    return f"On screen: {names}. Keep every face and wardrobe identical to the attached reference sheets."


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
    for scene in nf.ordered_scenes(master):
        sid = int(scene.get("scene_id") or 0)
        cast = scene_cast_entries(master, scene)
        body = str(scene.get("first_frame_prompt") or "")
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
        cast_note = ", ".join(c["name"] for c in entry["cast"]) or "—"
        cover = "  [9:16 PORTADA]" if entry["teaser_cover"] else ""
        labeled_lines += [
            f"=== SCENE {entry['scene_id']:03d} | {entry['filename']} | {entry['shot']} | "
            f"{entry['location']} | cast: {cast_note}{cover} ===",
            entry["prompt"],
            "",
        ]
    nf.write_text(paths["root"] / "chatgpt_image_prompts_queue_labeled.txt", "\n".join(labeled_lines))

    nf.write_json(paths["chatgpt_json"], {
        "episode": ep.get("slug"),
        "title": title,
        "count": len(entries),
        "note": "Cada prompt ya incluye el sufijo de estilo global y la cláusula anti-texto.",
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
        "Genera estas portadas ADEMÁS de los 60 frames 16:9. Mismo personaje y referencia.",
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
        nf.log("")
        nf.ok(f"{len(entries)} prompts exportados:")
        nf.info(f"{paths['chatgpt_txt'].name}          (cola pura, 1 prompt por línea)")
        nf.info(f"chatgpt_image_prompts_queue_labeled.txt (con nombre de archivo por escena)")
        nf.info(f"{paths['chatgpt_json'].name}         (índice JSON)")

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

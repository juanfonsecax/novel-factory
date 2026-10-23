#!/usr/bin/env python3
"""05 — Paquete único de producción con el método nuevo de Muse AI.

Reúne, en orden y listo para copiar/pegar:
  1. Hoja maestra de personajes (REF_CAST_MASTER.png).
  2. Diez storyboards de 6 viñetas (REF_GRID_MIN_01.png … REF_GRID_MIN_10.png).
  3. Diez lotes Muse AI de 1 minuto con adjuntos y comandos 16:9 / 9:16.
  4. Checklist de archivos y comando de ensamblaje.

Salidas en la carpeta del episodio:
  MUSE_PRODUCTION_PACK.md     Guía completa (prompts + instrucciones)
  MUSE_PRODUCTION_PACK.json   Manifiesto máquina-legible
  MUSE_CHECKLIST.md           Checklist imprimible
  storyboards/README.md       Dónde guardar las imágenes del proyecto

Uso:
  python generators/05_export_muse_method_pack.py mi_episodio
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path
from typing import Any, Dict, List

NF_ROOT = Path(__file__).resolve().parent.parent
GENERATORS_DIR = Path(__file__).resolve().parent
for _path in (NF_ROOT, GENERATORS_DIR):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

import nf_core as nf  # noqa: E402
import master_prompts_library as mpl  # noqa: E402

format_character_anchors = nf.format_character_anchors


def _load_gen02():
    path = GENERATORS_DIR / "02_export_chatgpt_queue.py"
    spec = importlib.util.spec_from_file_location("nf_gen02_muse_pack", path)
    if not spec or not spec.loader:
        raise nf.NFError(f"No se pudo cargar el generador: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


GEN02 = _load_gen02()


def build_pack(master: Dict[str, Any], style: Dict[str, Any]) -> Dict[str, Any]:
    ep = nf.episode_meta(master)
    grids = GEN02.build_storyboard_grid_items(master, style)
    batches = mpl.build_muse_batches(master, style)
    slug = nf.slugify(str(ep.get("slug") or "episodio"))
    scene_lookup = {int(s.get("scene_id") or 0): s for s in nf.ordered_scenes(master)}
    for batch in batches:
        batch["scene_attachments"] = [
            {
                "scene_id": sid,
                "attach": nf.build_scene_attachments(scene_lookup.get(sid, {}), master),
            }
            for sid in batch.get("scenes", [])
        ]
    return {
        "schema_version": "1.0",
        "method": "muse-minute-batches",
        "production_note": nf.PRODUCTION_ATTACH_NOTE,
        "source_mode": master.get("source_mode", "proven_adaptation"),
        "episode": {
            "slug": slug,
            "title": str(ep.get("title") or slug),
            "logline": str(ep.get("logline") or ""),
            "genre": str(ep.get("genre") or ""),
        },
        "counts": {
            "scenes": len(nf.ordered_scenes(master)),
            "storyboards": len(grids) - 1,
            "images": len(grids),
            "batches": len(batches),
        },
        "cast_master": grids[0],
        "storyboards": grids[1:],
        "batches": batches,
        "assemble_command": f"./novelfactory.bat assemble {slug}",
    }


def _prompt_block(text: str) -> List[str]:
    return ["```text", text.strip(), "```"]


def render_markdown(pack: Dict[str, Any]) -> str:
    ep = pack["episode"]
    counts = pack["counts"]
    cast = pack["cast_master"]
    lines: List[str] = [
        f"# {ep['title']} — Producción con Muse AI (método nuevo)",
        "",
        f"**Slug:** `{ep['slug']}`  ·  **Escenas:** {counts['scenes']}  ·  "
        f"**Imágenes:** {counts['images']}  ·  **Lotes:** {counts['batches']}",
        "",
        f"> **NOTA DE PRODUCCIÓN:** {pack.get('production_note', nf.PRODUCTION_ATTACH_NOTE)}",
        "",
    ]
    if pack.get("source_mode") == "original_unproven":
        lines += [
            "> ⚠️ **WARNING: source_mode es 'original_unproven' — Guion generado sin fuente probada.**",
            "",
        ]
    if ep.get("logline"):
        lines += [f"> {ep['logline']}", ""]
    lines += [
        "## Cómo funciona",
        "",
        "1. Genera **una** hoja maestra de personajes con los rostros y vestuarios fijos.",
        f"2. Genera **{counts['batches']}** storyboards (uno por minuto) usando esa hoja como referencia.",
        "3. En Muse AI, sube la hoja maestra + el storyboard del minuto y pega el bloque del lote.",
        "4. Guarda cada video como `raw_clips/minute_0X.mp4` y ejecuta el comando de ensamblaje.",
        "",
        "> No necesitas frames por escena ni clips de 10 s: el ensamblador detecta los lotes de 1 minuto.",
        "",
        "---",
        "",
        "## Paso 1 — Hoja maestra de personajes",
        "",
        f"Guarda el resultado como `storyboards/{cast['filename']}`.",
        "",
        "**Prompt:**",
        "",
        *_prompt_block(cast["prompt"]),
        "",
        "---",
        "",
        f"## Paso 2 — Storyboards ({counts['batches']} imágenes)",
        "",
        "Genera cada imagen con el mismo estilo y los mismos personajes de la hoja maestra.",
        "Guarda cada archivo en `storyboards/` con el nombre indicado.",
        "",
    ]
    for item in pack["storyboards"]:
        first = item["scenes"][0]
        last = item["scenes"][-1]
        lines += [
            f"### {item['filename']} — Minuto {item['minute']} (escenas {first}–{last})",
            "",
            *_prompt_block(item["prompt"]),
            "",
        ]
    lines += [
        "---",
        "",
        f"## Paso 3 — Lotes Muse AI ({counts['batches']} videos de 1 minuto)",
        "",
        "En cada lote: adjunta los dos archivos indicados y pega **un guion completo**",
        "(16:9 para YouTube o 9:16 para Reels/Shorts). El guion ya termina con el comando final.",
        "",
    ]
    for batch in pack["batches"]:
        refs = " + ".join(f"`{name}`" for name in batch["reference_images"])
        first = batch["scenes"][0]
        last = batch["scenes"][-1]
        lines += [
            f"### Lote {batch['batch_id']:02d} — Minuto {batch['minute']} (escenas {first}–{last})",
            "",
            f"**Adjuntar:** {refs}",
            "",
            "**Adjuntos por escena de este lote:**",
            "",
        ]
        for item in batch.get("scene_attachments") or []:
            attach_str = ", ".join(item.get("attach") or [])
            lines.append(f"- Escena {item['scene_id']:03d}: `attach: [{attach_str}]`")
        lines += [
            "",
            f"**Guardar 16:9 como:** `{batch.get('save_as_16x9') or batch['save_as']}`",
            "",
            f"**Guardar 9:16 como:** `{batch.get('save_as_9x16') or 'raw_clips/minute_' + format(batch['batch_id'], '02d') + '_vertical.mp4'}`",
            "",
            "**Bloque 16:9 para Muse AI (YouTube):**",
            "",
            *_prompt_block(batch["prompt_16x9_youtube"]),
            "",
            "**Comando final 9:16 (Reels/Shorts):**",
            "",
            *_prompt_block(batch["prompt_9x16_vertical"]),
            "",
        ]
    lines += [
        "---",
        "",
        "## Paso 4 — Ensamblar",
        "",
        f"Cuando existan los {counts['batches']} archivos "
        f"`minute_01.mp4 … minute_{counts['batches']:02d}.mp4`:",
        "",
        "```powershell",
        pack["assemble_command"],
        "```",
        "",
        "El ensamblador detecta el modo B, genera el máster 16:9 completo,",
        "el SRT sincronizado y el teaser vertical automático de 20 segundos.",
        "",
    ]
    return "\n".join(lines)


def render_checklist(pack: Dict[str, Any]) -> str:
    ep = pack["episode"]
    lines = [
        f"# Checklist — {ep['title']}",
        "",
        f"> **NOTA DE PRODUCCIÓN:** {pack.get('production_note', nf.PRODUCTION_ATTACH_NOTE)}",
        "",
        "## Imágenes del método nuevo (`storyboards/`)",
        "",
    ]
    cast = pack["cast_master"]
    lines.append(f"- [ ] `{cast['filename']}` — hoja maestra de personajes")
    for item in pack["storyboards"]:
        first = item["scenes"][0]
        last = item["scenes"][-1]
        lines.append(f"- [ ] `{item['filename']}` — minuto {item['minute']} (escenas {first}–{last})")
    lines += ["", "## Videos Muse AI (`raw_clips/`)", ""]
    for batch in pack["batches"]:
        refs = " + ".join(batch["reference_images"])
        lines.append(
            f"- [ ] `minute_{batch['batch_id']:02d}.mp4` — lote {batch['batch_id']:02d} "
            f"(adjuntos: {refs})"
        )
    lines += [
        "",
        "## Cierre",
        "",
        f"- [ ] Los {pack['counts']['batches']} lotes están en `raw_clips/`.",
        f"- [ ] Ejecutar `{pack['assemble_command']}`.",
        "- [ ] Revisar `output/<slug>_master_16x9_1080p.mp4` y `output/<slug>_teaser_9x16.mp4`.",
        "",
    ]
    return "\n".join(lines)


def write_pack(paths: Dict[str, Path], pack: Dict[str, Any]) -> Dict[str, Path]:
    root = paths["root"]
    md_path = root / "MUSE_PRODUCTION_PACK.md"
    json_path = root / "MUSE_PRODUCTION_PACK.json"
    checklist_path = root / "MUSE_CHECKLIST.md"
    storyboards_dir = root / "storyboards"
    storyboards_dir.mkdir(parents=True, exist_ok=True)
    readme_path = storyboards_dir / "README.md"
    nf.write_text(md_path, render_markdown(pack))
    nf.write_json(json_path, pack)
    nf.write_text(checklist_path, render_checklist(pack))
    if not readme_path.exists():
        grid_count = int(pack["counts"]["batches"])
        image_count = int(pack["counts"]["images"])
        nf.write_text(readme_path, "\n".join([
            "# Storyboards del método Muse AI",
            "",
            "Guarda aquí las imágenes generadas en ChatGPT con estos nombres exactos:",
            "",
            "- `REF_CAST_MASTER.png` (hoja maestra de personajes)",
            f"- `REF_GRID_MIN_01.png` … `REF_GRID_MIN_{grid_count:02d}.png` (un storyboard por minuto)",
            "",
            f"El dashboard detecta estos archivos y marca el progreso de las {image_count} imágenes.",
            "",
        ]))
    return {
        "md": md_path,
        "json": json_path,
        "checklist": checklist_path,
        "storyboards_dir": storyboards_dir,
        "storyboards_readme": readme_path,
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Exporta el paquete completo de producción con el método Muse AI de 1 minuto."
    )
    parser.add_argument("project", help="Slug o ruta del proyecto.")
    args = parser.parse_args(argv)

    nf.log("=" * 78)
    nf.log("  NOVEL FACTORY — 05 · Paquete de producción Muse AI (método nuevo)")
    nf.log("=" * 78)
    paths = nf.resolve_project(args.project)
    master = nf.load_master(paths["root"])
    style = nf.load_style_locks()
    pack = build_pack(master, style)
    written = write_pack(paths, pack)

    nf.ok(f"Paquete exportado en: {paths['root']}")
    nf.info(f"{written['md'].name}  (guía completa: {pack['counts']['images']} imágenes + "
            f"{pack['counts']['batches']} lotes)")
    nf.info(f"{written['checklist'].name}  (checklist imprimible)")
    nf.info(f"{written['json'].name}  (manifiesto máquina-legible)")
    nf.info(f"storyboards/README.md  (dónde guardar las {pack['counts']['images']} imágenes)")
    nf.info(f"Comando final: {pack['assemble_command']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

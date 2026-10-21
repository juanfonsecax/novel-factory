#!/usr/bin/env python3
"""00 — Exporta el workflow maestro de prompts listo para copiar y pegar.

Entradas:
  projects/<proyecto>/story_brief.md   (preferido)
  projects/<proyecto>/idea_input.md    (fallback)
  projects/<proyecto>/master_episode.json (opcional, para los lotes de Muse AI)

Salidas en la carpeta del episodio:
  MASTER_WORKFLOW_PROMPTS_READY.md        PROMPT 000/001/002/003 rellenados
  muse_ai_minute_batches_queue.txt        Lotes de 1 minuto (6 escenas) para Muse AI
  muse_ai_minute_batches_queue.json       Manifiesto máquina-legible de esos lotes
  muse_ai_batches_queue.txt / .json       Alias compatible con el exportador 03

Uso:
  python generators/00_export_master_workflow_prompts.py mi_episodio
  python generators/00_export_master_workflow_prompts.py mi_episodio --show prompt_003
  python generators/00_export_master_workflow_prompts.py mi_episodio --out-dir "C:\\salida"
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

NF_ROOT = Path(__file__).resolve().parent.parent
GENERATORS_DIR = Path(__file__).resolve().parent
for _path in (NF_ROOT, GENERATORS_DIR):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

import nf_core as nf  # noqa: E402
import master_prompts_library as mpl  # noqa: E402

STORY_FILENAMES = ("story_brief.md", "idea_input.md")


def read_story(paths: Dict[str, Path]) -> Tuple[str, Optional[Path]]:
    """Lee story_brief.md o, si no existe/vacío, idea_input.md."""
    for name in STORY_FILENAMES:
        path = paths["root"] / name
        if not path.exists():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace").strip()
        except OSError:
            continue
        if text:
            return text, path
    return "", None


def load_master_if_available(paths: Dict[str, Path]) -> Dict[str, Any]:
    if not paths["master"].exists():
        return {}
    try:
        return nf.load_master(paths["root"])
    except nf.NFError:
        return {}


def _story_fallback() -> str:
    return (
        "(Completa story_brief.md o idea_input.md con la premisa: quién quiere qué, "
        "quién se lo impide y qué secreto mueve la historia)"
    )


def render_workflow_markdown(
    pack: Dict[str, Any],
    prompt_003_916: str,
    story_path: Optional[Path],
    batch_paths: Dict[str, Path],
) -> str:
    project = pack.get("project") or {}
    values = pack.get("values") or {}
    viral = pack.get("viral_template") or {}
    title = project.get("title") or project.get("slug") or "Episodio"
    lines: List[str] = [
        f"# MASTER WORKFLOW PROMPTS READY — {title}",
        "",
        f"- Generado: {pack.get('generated_at')}",
        f"- Historia fuente: {story_path.name if story_path else '(sin archivo de historia)'}",
        f"- Duración: {values.get('duration_minutes')} minuto(s)",
        f"- Escenas: {values.get('total_scenes')} (10 s cada una)",
        f"- Bloques de storyboard: {values.get('total_grid_images')} (6 escenas por imagen)",
        f"- Formato máster: 16:9",
        f"- Formato teasers/Reels: 9:16",
        f"- Estilo visual: {values.get('visual_style')}",
    ]
    if viral:
        lines += [
            f"- Mega-nicho USA: {viral.get('label')} ({viral.get('id')})",
            f"- Categoría: {viral.get('category')}",
        ]
    lines += [
        "",
        "> Los cuatro prompts ya están rellenados con los datos de este proyecto.",
        "> Copia cada bloque completo y úsalo en el orden 000 → 001 → 002 → 003.",
        "",
        "## Cómo usar este documento",
        "",
        "1. **PROMPT 000** genera la arquitectura narrativa y el elenco.",
        "2. **PROMPT 001** convierte esa arquitectura en storyboards de 6 viñetas por imagen.",
        "3. **PROMPT 002** extrae del storyboard la hoja maestra de personajes en una sola imagen.",
        "4. **PROMPT 003** convierte el storyboard en guion técnico con cámara, sonido y diálogo en inglés.",
        "5. Copia el comando final de cada bloque de 1 minuto en Muse AI junto con el storyboard y la hoja de personajes.",
        "",
    ]
    if batch_paths:
        lines += [
            f"Lotes de 1 minuto listos: `{batch_paths['txt'].name}` "
            f"({len(batch_paths.get('batches') or [])} bloques).",
            "",
        ]
    else:
        lines += [
            "Sin `master_episode.json`: el documento se generó solo con la historia. "
            "Cuando exista el maestro, vuelve a ejecutar este comando para crear los lotes de Muse AI.",
            "",
        ]

    for prompt in pack.get("prompts") or []:
        lines += [
            "---",
            "",
            f"## {prompt['code']} — {prompt['title']}",
            "",
            f"_{prompt['purpose']}_",
            "",
            f"**{prompt['chars']:,} caracteres · {prompt['words']:,} palabras**",
            "",
            "````text",
            prompt["text"],
            "````",
            "",
        ]
        if prompt["key"] == "prompt_003":
            lines += [
                f"## {prompt['code']} — Variante 9:16 (teasers / Reels / Shorts)",
                "",
                "Misma estructura del PROMPT 003, pero con el comando final en formato 9:16.",
                "",
                "````text",
                prompt_003_916,
                "````",
                "",
            ]
    return "\n".join(lines)


def export_workflow(project: str | Path, out_dir: Optional[Path] = None, niche: str = "") -> Dict[str, Any]:
    paths = nf.resolve_project(project, must_exist=False)
    root = paths["root"]
    if not root.exists() or not root.is_dir():
        raise nf.NFError(f"No existe la carpeta del proyecto: {root}")

    style = nf.load_style_locks()
    brief_text, story_path = read_story(paths)
    master = load_master_if_available(paths)

    overrides: Dict[str, Any] = {}
    if not master:
        overrides = {
            "story_idea": brief_text or _story_fallback(),
            "duration_minutes": "10",
            "total_scenes": "60",
            "total_grid_images": "10",
            "aspect_ratio": str(style.get("master_aspect") or "16:9"),
        }

    pack = mpl.build_prompt_pack(master, style, brief_text, overrides=overrides, niche=niche)
    values_916 = dict(pack.get("values") or {})
    values_916["aspect_ratio"] = str(style.get("teaser_aspect") or "9:16")
    prompt_003_916 = mpl.render_prompt("prompt_003", values_916)

    target_root = Path(out_dir) if out_dir else root
    target_root.mkdir(parents=True, exist_ok=True)

    batch_paths: Dict[str, Any] = {}
    if master.get("scenes"):
        minute_files = mpl.write_muse_batch_files(
            target_root,
            master,
            style,
            basename="muse_ai_minute_batches_queue",
        )
        alias_files = mpl.write_muse_batch_files(
            target_root,
            master,
            style,
            basename="muse_ai_batches_queue",
        )
        batch_paths = {
            "txt": minute_files["txt"],
            "json": minute_files["json"],
            "alias_txt": alias_files["txt"],
            "alias_json": alias_files["json"],
            "batches": minute_files["batches"],
        }

    markdown = render_workflow_markdown(pack, prompt_003_916, story_path, batch_paths)
    written: Dict[str, Any] = {
        "markdown": nf.write_text(target_root / "MASTER_WORKFLOW_PROMPTS_READY.md", markdown),
    }
    written.update(batch_paths)

    return {
        "pack": pack,
        "written": written,
        "target_root": target_root,
        "story_path": story_path,
        "batches": batch_paths.get("batches") or [],
    }


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="00 — Exporta PROMPT 000/001/002/003 y los lotes de Muse AI listos para usar.",
    )
    parser.add_argument("project", nargs="?", default="", help="Slug del episodio o ruta a su carpeta.")
    parser.add_argument("--out-dir", default="", help="Carpeta de salida (por defecto, la del proyecto).")
    parser.add_argument("--show", default="", help="Imprime un prompt: prompt_000..prompt_003 o all.")
    parser.add_argument("--quiet", action="store_true", help="No imprime el resumen.")
    parser.add_argument("--niche", "--archetype", dest="niche", default="",
                        help="ID del mega-nicho USA que se añade al PROMPT 000.")
    parser.add_argument("--list-niches", action="store_true",
                        help="Lista los mega-nichos USA disponibles y termina.")
    args = parser.parse_args(argv)

    if args.list_niches:
        for template in mpl.list_viral_templates():
            nf.log(f"{template.get('id')} · {template.get('category')} · {template.get('label')}")
        return 0
    if not args.project:
        parser.error("Debes indicar un proyecto (o usa --list-niches).")

    niche = str(args.niche or "").strip()
    selected_niche: Optional[Dict[str, Any]] = None
    if niche:
        try:
            selected_niche = mpl.get_viral_template(niche)
        except KeyError as exc:
            nf.err(str(exc))
            return 1

    nf.log("")
    nf.log("=" * 70)
    nf.log("  NOVEL FACTORY — 00 · Workflow maestro (000/001/002/003 + lotes Muse AI)")
    nf.log("=" * 70)

    result = export_workflow(args.project, Path(args.out_dir) if args.out_dir else None, niche=niche)
    pack = result["pack"]
    written = result["written"]
    target_root = result["target_root"]

    if not args.quiet:
        nf.ok(f"Workflow exportado en: {target_root}")
        nf.info(written["markdown"].name + "  (4 prompts rellenados + variante 9:16)")
        if result["batches"]:
            nf.info(written["txt"].name + f"  ({len(result['batches'])} lotes de 6 escenas)")
            nf.info(written["json"].name + "  (manifiesto de lotes)")
            nf.info(written["alias_txt"].name + "  (alias para el exportador 03)")
            nf.info("Cada lote adjunta REF_CAST_MASTER.png + REF_GRID_MIN_XX.png y trae "
                    "comandos finales 16:9 (YouTube) y 9:16 (Reels).")
        else:
            nf.warn("Sin master_episode.json: no se generaron lotes de Muse AI.")
        if result["story_path"]:
            nf.info(f"Historia fuente: {result['story_path'].name}")
        if selected_niche:
            nf.info(f"Mega-nicho USA: {selected_niche.get('label')} ({selected_niche.get('id')})")
        nf.log("")
        for prompt in pack["prompts"]:
            nf.info(f"{prompt['code']}: {prompt['chars']:,} chars · {prompt['words']:,} palabras")

    if args.show:
        wanted = {p["key"] for p in pack["prompts"]} if args.show == "all" else {args.show}
        nf.log("")
        for prompt in pack["prompts"]:
            if prompt["key"] in wanted:
                nf.log("=" * 70)
                nf.log(f"{prompt['code']} — {prompt['title']}")
                nf.log("=" * 70)
                nf.log(prompt["text"])
                nf.log("")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except nf.NFError as exc:
        nf.err(str(exc))
        raise SystemExit(1)

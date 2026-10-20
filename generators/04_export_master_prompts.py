#!/usr/bin/env python3
"""04 — Exporta los cuatro prompts maestros rellenados con el proyecto.

Salidas en la carpeta del episodio:
  MASTER_PROMPTS.md              (lectura + bloques copiables)
  MASTER_PROMPTS.txt             (texto plano, ideal para copiar y pegar)
  master_prompts.json            (manifiesto con valores y prompts renderizados)
  prompts/PROMPT_000_...txt      (un archivo por prompt, listo para copiar)

Uso:
  python generators/04_export_master_prompts.py mi_episodio
  python generators/04_export_master_prompts.py mi_episodio --show prompt_003
  python generators/04_export_master_prompts.py mi_episodio --out-dir "C:\\salida"
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, Dict, Optional

NF_ROOT = Path(__file__).resolve().parent.parent
GENERATORS_DIR = Path(__file__).resolve().parent
for _path in (NF_ROOT, GENERATORS_DIR):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

import nf_core as nf  # noqa: E402
import master_prompts_library as mpl  # noqa: E402


def read_brief(paths: Dict[str, Path]) -> str:
    brief = paths["root"] / "story_brief.md"
    if not brief.exists():
        return ""
    try:
        return brief.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def export_prompts(project: str | Path, out_dir: Optional[Path] = None) -> Dict[str, Any]:
    paths = nf.resolve_project(project)
    master = nf.load_master(paths["root"])
    style = nf.load_style_locks()
    brief_text = read_brief(paths)
    pack = mpl.build_prompt_pack(master, style, brief_text)
    target_root = Path(out_dir) if out_dir else paths["root"]
    written = mpl.write_prompt_pack(target_root, pack)
    return {"pack": pack, "written": written, "target_root": target_root}


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="04 — Exporta PROMPT 000/001/002/003 rellenados con los datos del episodio.",
    )
    parser.add_argument("project", help="Slug del episodio o ruta a su carpeta.")
    parser.add_argument("--out-dir", default="", help="Carpeta de salida (por defecto, la del proyecto).")
    parser.add_argument("--show", default="", help="Imprime un prompt: prompt_000..prompt_003 o all.")
    parser.add_argument("--quiet", action="store_true", help="No imprime el resumen.")
    args = parser.parse_args(argv)

    nf.log("")
    nf.log("=" * 70)
    nf.log("  NOVEL FACTORY — 04 · Prompts maestros (000/001/002/003)")
    nf.log("=" * 70)

    result = export_prompts(args.project, Path(args.out_dir) if args.out_dir else None)
    pack = result["pack"]
    written = result["written"]
    target_root = result["target_root"]

    if not args.quiet:
        nf.ok(f"Prompts exportados en: {target_root}")
        nf.info(written["markdown"].name + "  (lectura + bloques copiables)")
        nf.info(written["plain"].name + "     (texto plano)")
        nf.info(written["json"].name + "    (manifiesto)")
        nf.info("prompts/  (4 archivos .txt individuales)")
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

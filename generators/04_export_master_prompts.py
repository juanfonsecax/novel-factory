#!/usr/bin/env python3
"""04 - Export the four master prompts filled with project data.

Outputs in the episode folder:
  MASTER_PROMPTS.md              (readable + copyable blocks)
  MASTER_PROMPTS.txt             (plain text, easy to copy and paste)
  master_prompts.json            (manifest with values and rendered prompts)
  prompts/PROMPT_000_...txt      (one file per prompt, ready to copy)

Usage:
  python generators/04_export_master_prompts.py my_episode
  python generators/04_export_master_prompts.py my_episode --show prompt_003
  python generators/04_export_master_prompts.py my_episode --out-dir "C:\\output"
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
        description="04 - Export PROMPT 000/001/002/003 filled with episode data.",
    )
    parser.add_argument("project", help="Episode slug or path to its folder.")
    parser.add_argument("--out-dir", default="", help="Output folder (defaults to the project folder).")
    parser.add_argument("--show", default="", help="Print one prompt: prompt_000..prompt_003 or all.")
    parser.add_argument("--quiet", action="store_true", help="Do not print the summary.")
    args = parser.parse_args(argv)

    nf.log("")
    nf.log("=" * 70)
    nf.log("  NOVEL FACTORY - 04 - Master prompts (000/001/002/003)")
    nf.log("=" * 70)

    result = export_prompts(args.project, Path(args.out_dir) if args.out_dir else None)
    pack = result["pack"]
    written = result["written"]
    target_root = result["target_root"]

    if not args.quiet:
        nf.ok(f"Prompts exported to: {target_root}")
        nf.info(written["markdown"].name + "  (readable + copyable blocks)")
        nf.info(written["plain"].name + "     (plain text)")
        nf.info(written["json"].name + "    (manifest)")
        nf.info("prompts/  (4 individual .txt files)")
        nf.log("")
        for prompt in pack["prompts"]:
            nf.info(f"{prompt['code']}: {prompt['chars']:,} chars - {prompt['words']:,} words")

    if args.show:
        wanted = {p["key"] for p in pack["prompts"]} if args.show == "all" else {args.show}
        nf.log("")
        for prompt in pack["prompts"]:
            if prompt["key"] in wanted:
                nf.log("=" * 70)
                nf.log(f"{prompt['code']} - {prompt['title']}")
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

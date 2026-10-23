#!/usr/bin/env python3
"""00 — Export the master prompt workflow ready to copy and paste.

Inputs:
  projects/<project>/story_brief.md   (preferred)
  projects/<project>/idea_input.md    (fallback)
  projects/<project>/master_episode.json (optional, for Muse AI batches)

Outputs in the episode folder:
  MASTER_WORKFLOW_PROMPTS_READY.md        PROMPT 000/001/002/003 filled in
  muse_ai_minute_batches_queue.txt        1-minute batches (6 scenes) for Muse AI
  muse_ai_minute_batches_queue.json       Machine-readable manifest of those batches
  muse_ai_batches_queue.txt / .json       Alias compatible with exporter 03

Usage:
  python generators/00_export_master_workflow_prompts.py my_episode
  python generators/00_export_master_workflow_prompts.py my_episode --show prompt_003
  python generators/00_export_master_workflow_prompts.py my_episode --out-dir "C:\\output"
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
    """Read story_brief.md or, if missing/empty, idea_input.md."""
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
        "(Complete story_brief.md or idea_input.md with the premise: who wants what, "
        "who blocks them and what secret drives the story)"
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
    title = project.get("title") or project.get("slug") or "Episode"
    lines: List[str] = [
        f"# MASTER WORKFLOW PROMPTS READY — {title}",
        "",
        f"- Generated: {pack.get('generated_at')}",
        f"- Source story: {story_path.name if story_path else '(no story file)'}",
        f"- Runtime: {values.get('duration_minutes')} minute(s)",
        f"- Scenes: {values.get('total_scenes')} (10 s each)",
        f"- Storyboard blocks: {values.get('total_grid_images')} (6 scenes per image)",
        f"- Master format: 16:9",
        f"- Teaser/Reels format: 9:16",
        f"- Visual style: {values.get('visual_style')}",
    ]
    if viral:
        lines += [
            f"- USA mega-niche: {viral.get('label')} ({viral.get('id')})",
            f"- Category: {viral.get('category')}",
        ]
    if pack.get("source_mode") == "original_unproven" or (pack.get("project") or {}).get("source_mode") == "original_unproven":
        lines += [
            "",
            "> ⚠️ **WARNING: source_mode is 'original_unproven' — script generated without a proven source.**",
        ]
    lines += [
        "",
        "> All four prompts are already filled with this project's data.",
        "> Copy each complete block and use it in the order 000 → 001 → 002 → 003.",
        "",
        "## How to use this document",
        "",
        "1. **PROMPT 000** generates the narrative architecture and cast.",
        "2. **PROMPT 001** turns that architecture into storyboards with 6 panels per image.",
        "3. **PROMPT 002** extracts the master character sheet from the storyboard in a single image.",
        "4. **PROMPT 003** turns the storyboard into a technical script with camera, sound and English dialogue.",
        "5. Copy the final command for each 1-minute block into Muse AI together with the storyboard and character sheet.",
        "",
    ]
    if batch_paths:
        lines += [
            f"1-minute batches ready: `{batch_paths['txt'].name}` "
            f"({len(batch_paths.get('batches') or [])} blocks).",
            "",
        ]
    else:
        lines += [
            "No `master_episode.json`: the document was generated from the story alone. "
            "Once the master exists, run this command again to create the Muse AI batches.",
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
            f"**{prompt['chars']:,} characters · {prompt['words']:,} words**",
            "",
            "````text",
            prompt["text"],
            "````",
            "",
        ]
        if prompt["key"] == "prompt_003":
            lines += [
                f"## {prompt['code']} — 9:16 variant (teasers / Reels / Shorts)",
                "",
                "Same PROMPT 003 structure, but with the final command in 9:16 format.",
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
        raise nf.NFError(f"Project folder does not exist: {root}")

    style = nf.load_style_locks()
    brief_text, story_path = read_story(paths)
    master = load_master_if_available(paths)

    overrides: Dict[str, Any] = {}
    if not master:
        meta = nf.load_project_meta(paths)
        target = int(meta.get("target_minutes") or nf.DEFAULT_TARGET_MINUTES)
        total_scenes = nf.scene_count_for_target(target)
        overrides = {
            "story_idea": brief_text or _story_fallback(),
            "duration_minutes": str(target),
            "total_scenes": str(total_scenes),
            "total_grid_images": str(target),
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
        description="00 — Export PROMPT 000/001/002/003 and ready-to-use Muse AI batches.",
    )
    parser.add_argument("project", nargs="?", default="", help="Episode slug or path to its folder.")
    parser.add_argument("--out-dir", default="", help="Output folder (default: the project folder).")
    parser.add_argument("--show", default="", help="Print one prompt: prompt_000..prompt_003 or all.")
    parser.add_argument("--quiet", action="store_true", help="Do not print the summary.")
    parser.add_argument("--niche", "--archetype", dest="niche", default="",
                        help="ID of the USA mega-niche added to PROMPT 000.")
    parser.add_argument("--list-niches", action="store_true",
                        help="List the available USA mega-niches and exit.")
    args = parser.parse_args(argv)

    if args.list_niches:
        for template in mpl.list_viral_templates():
            nf.log(f"{template.get('id')} · {template.get('category')} · {template.get('label')}")
        return 0
    if not args.project:
        parser.error("You must provide a project (or use --list-niches).")

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
    nf.log("  NOVEL FACTORY — 00 · Master workflow (000/001/002/003 + Muse AI batches)")
    nf.log("=" * 70)

    result = export_workflow(args.project, Path(args.out_dir) if args.out_dir else None, niche=niche)
    pack = result["pack"]
    written = result["written"]
    target_root = result["target_root"]

    if not args.quiet:
        nf.ok(f"Workflow exported to: {target_root}")
        nf.info(written["markdown"].name + "  (4 filled prompts + 9:16 variant)")
        if result["batches"]:
            nf.info(written["txt"].name + f"  ({len(result['batches'])} batches of 6 scenes)")
            nf.info(written["json"].name + "  (batch manifest)")
            nf.info(written["alias_txt"].name + "  (alias for exporter 03)")
            nf.info("Each batch attaches REF_CAST_MASTER.png + REF_GRID_MIN_XX.png and includes "
                    "final 16:9 (YouTube) and 9:16 (Reels) commands.")
        else:
            nf.warn("No master_episode.json: no Muse AI batches were generated.")
        if result["story_path"]:
            nf.info(f"Source story: {result['story_path'].name}")
        if selected_niche:
            nf.info(f"USA mega-niche: {selected_niche.get('label')} ({selected_niche.get('id')})")
        nf.log("")
        for prompt in pack["prompts"]:
            nf.info(f"{prompt['code']}: {prompt['chars']:,} chars · {prompt['words']:,} words")

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

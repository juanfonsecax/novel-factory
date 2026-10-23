#!/usr/bin/env python3
"""05 — Single production pack for the new Muse AI method.

Collects, in order and ready to copy/paste:
  1. Master character sheet (REF_CAST_MASTER.png).
  2. Ten 6-panel storyboards (REF_GRID_MIN_01.png … REF_GRID_MIN_10.png).
  3. Ten 1-minute Muse AI batches with attachments and 16:9 / 9:16 commands.
  4. File checklist and assembly command.

Outputs in the episode folder:
  MUSE_PRODUCTION_PACK.md     Complete guide (prompts + instructions)
  MUSE_PRODUCTION_PACK.json   Machine-readable manifest
  MUSE_CHECKLIST.md           Printable checklist
  storyboards/README.md       Where to save the project images

Usage:
  python generators/05_export_muse_method_pack.py my_episode
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
        raise nf.NFError(f"Could not load the generator: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


GEN02 = _load_gen02()


def build_pack(master: Dict[str, Any], style: Dict[str, Any]) -> Dict[str, Any]:
    ep = nf.episode_meta(master)
    grids = GEN02.build_storyboard_grid_items(master, style)
    batches = mpl.build_muse_batches(master, style)
    slug = nf.slugify(str(ep.get("slug") or "episode"))
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
        f"# {ep['title']} — Muse AI Production (new method)",
        "",
        f"**Slug:** `{ep['slug']}`  ·  **Scenes:** {counts['scenes']}  ·  "
        f"**Images:** {counts['images']}  ·  **Batches:** {counts['batches']}",
        "",
        f"> **PRODUCTION NOTE:** {pack.get('production_note', nf.PRODUCTION_ATTACH_NOTE)}",
        "",
    ]
    if pack.get("source_mode") == "original_unproven":
        lines += [
            "> ⚠️ **WARNING: source_mode is 'original_unproven' — script generated without a proven source.**",
            "",
        ]
    if ep.get("logline"):
        lines += [f"> {ep['logline']}", ""]
    lines += [
        "## How it works",
        "",
        "1. Generate **one** master character sheet with fixed faces and wardrobes.",
        f"2. Generate **{counts['batches']}** storyboards (one per minute) using that sheet as reference.",
        "3. In Muse AI, upload the master sheet + the minute storyboard and paste the batch block.",
        "4. Save each video as `raw_clips/minute_0X.mp4` and run the assembly command.",
        "",
        "> You do not need per-scene frames or 10 s clips: the assembler detects 1-minute batches.",
        "",
        "---",
        "",
        "## Step 1 — Master character sheet",
        "",
        f"Save the result as `storyboards/{cast['filename']}`.",
        "",
        "**Prompt:**",
        "",
        *_prompt_block(cast["prompt"]),
        "",
        "---",
        "",
        f"## Step 2 — Storyboards ({counts['batches']} images)",
        "",
        "Generate each image with the same style and the same characters as the master sheet.",
        "Save each file in `storyboards/` with the indicated filename.",
        "",
    ]
    for item in pack["storyboards"]:
        first = item["scenes"][0]
        last = item["scenes"][-1]
        lines += [
            f"### {item['filename']} — Minute {item['minute']} (scenes {first}–{last})",
            "",
            *_prompt_block(item["prompt"]),
            "",
        ]
    lines += [
        "---",
        "",
        f"## Step 3 — Muse AI batches ({counts['batches']} 1-minute videos)",
        "",
        "For each batch: attach the two indicated files and paste **one complete script**",
        "(16:9 for YouTube or 9:16 for Reels/Shorts). The script already ends with the final command.",
        "",
    ]
    for batch in pack["batches"]:
        refs = " + ".join(f"`{name}`" for name in batch["reference_images"])
        first = batch["scenes"][0]
        last = batch["scenes"][-1]
        lines += [
            f"### Batch {batch['batch_id']:02d} — Minute {batch['minute']} (scenes {first}–{last})",
            "",
            f"**Attach:** {refs}",
            "",
            "**Per-scene attachments for this batch:**",
            "",
        ]
        for item in batch.get("scene_attachments") or []:
            attach_str = ", ".join(item.get("attach") or [])
            lines.append(f"- Scene {item['scene_id']:03d}: `attach: [{attach_str}]`")
        lines += [
            "",
            f"**Save 16:9 as:** `{batch.get('save_as_16x9') or batch['save_as']}`",
            "",
            f"**Save 9:16 as:** `{batch.get('save_as_9x16') or 'raw_clips/minute_' + format(batch['batch_id'], '02d') + '_vertical.mp4'}`",
            "",
            "**16:9 block for Muse AI (YouTube):**",
            "",
            *_prompt_block(batch["prompt_16x9_youtube"]),
            "",
            "**Final 9:16 command (Reels/Shorts):**",
            "",
            *_prompt_block(batch["prompt_9x16_vertical"]),
            "",
        ]
    lines += [
        "---",
        "",
        "## Step 4 — Assemble",
        "",
        f"Once the {counts['batches']} files exist: "
        f"`minute_01.mp4 … minute_{counts['batches']:02d}.mp4`:",
        "",
        "```powershell",
        pack["assemble_command"],
        "```",
        "",
        "The assembler detects mode B, generates the complete 16:9 master,",
        "the synchronized SRT and the automatic 20-second vertical teaser.",
        "",
    ]
    return "\n".join(lines)


def render_checklist(pack: Dict[str, Any]) -> str:
    ep = pack["episode"]
    lines = [
        f"# Checklist — {ep['title']}",
        "",
        f"> **PRODUCTION NOTE:** {pack.get('production_note', nf.PRODUCTION_ATTACH_NOTE)}",
        "",
        "## New-method images (`storyboards/`)",
        "",
    ]
    cast = pack["cast_master"]
    lines.append(f"- [ ] `{cast['filename']}` — master character sheet")
    for item in pack["storyboards"]:
        first = item["scenes"][0]
        last = item["scenes"][-1]
        lines.append(f"- [ ] `{item['filename']}` — minute {item['minute']} (scenes {first}–{last})")
    lines += ["", "## Muse AI videos (`raw_clips/`)", ""]
    for batch in pack["batches"]:
        refs = " + ".join(batch["reference_images"])
        lines.append(
            f"- [ ] `minute_{batch['batch_id']:02d}.mp4` — batch {batch['batch_id']:02d} "
            f"(attachments: {refs})"
        )
    lines += [
        "",
        "## Close-out",
        "",
        f"- [ ] All {pack['counts']['batches']} batches are in `raw_clips/`.",
        f"- [ ] Run `{pack['assemble_command']}`.",
        "- [ ] Review `output/<slug>_master_16x9_1080p.mp4` and `output/<slug>_teaser_9x16.mp4`.",
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
            "# Muse AI method storyboards",
            "",
            "Save the images generated in ChatGPT here with these exact filenames:",
            "",
            "- `REF_CAST_MASTER.png` (master character sheet)",
            f"- `REF_GRID_MIN_01.png` … `REF_GRID_MIN_{grid_count:02d}.png` (one storyboard per minute)",
            "",
            f"The dashboard detects these files and tracks progress across the {image_count} images.",
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
        description="Export the complete production pack for the 1-minute Muse AI method."
    )
    parser.add_argument("project", help="Project slug or path.")
    args = parser.parse_args(argv)

    nf.log("=" * 78)
    nf.log("  NOVEL FACTORY — 05 · Muse AI production pack (new method)")
    nf.log("=" * 78)
    paths = nf.resolve_project(args.project)
    master = nf.load_master(paths["root"])
    style = nf.load_style_locks()
    pack = build_pack(master, style)
    written = write_pack(paths, pack)

    nf.ok(f"Pack exported to: {paths['root']}")
    nf.info(f"{written['md'].name}  (complete guide: {pack['counts']['images']} images + "
            f"{pack['counts']['batches']} batches)")
    nf.info(f"{written['checklist'].name}  (printable checklist)")
    nf.info(f"{written['json'].name}  (machine-readable manifest)")
    nf.info(f"storyboards/README.md  (where to save the {pack['counts']['images']} images)")
    nf.info(f"Final command: {pack['assemble_command']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""02 — Export the first-frame queue for the ChatGPT extension.

Generates three artifacts in the episode folder:
  chatgpt_image_prompts_queue.txt          -> 1 prompt per line (automatic queue)
  chatgpt_image_prompts_queue_labeled.txt  -> readable, with the expected filename
  chatgpt_image_prompts_queue.json         -> machine-readable index

Final prompt = master body + global style suffix (once) + anti-text clause.
Each line corresponds EXACTLY to:
  frames/frame_001.png ... frames/frame_060.png

Opens no browsers, touches no ChatGPT sessions and downloads nothing: it only writes
local text that you paste (or your queue extension reads) in order.
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
    """Reference sheets (STEP 0): one per character, generated ONCE before the queue.

    A character participates if it defines `visual_reference` (casting description -> sheet prompt)
    or `reference_image` (already has its own image -> only attach it, do not generate).
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
        f"NOVEL FACTORY — Character reference sheets (STEP 0) · {ep.get('title') or ep.get('slug')}",
        "",
        "This is generated ONCE per episode, BEFORE the frame queue:",
        "  1. Open a new ChatGPT conversation with image generation.",
        "  2. Paste each character prompt; save the result in the project",
        f"     folder: {refs_dir}",
        "     with the exact filename shown below (reference_<id>.png).",
        "  3. Also crop each character's face in close-up and save the",
        "     crop in the same folder as reference_<id>_face.png (attached in",
        "     scenes where that character SPEAKS).",
        "  4. Attach ALL reference sheets to the conversation and keep them there",
        "     while you generate frame_001.png … frame_060.png (chatgpt_image_prompts_queue.txt).",
        "     In speaking scenes also attach the speaker's reference_<id>_face.png crop.",
        "  5. Scene prompts name the character and their reference_<id>.png file:",
        "     the face is never described in text; it is copied from these sheets.",
        "",
    ]
    for sheet in sheets:
        lines.append(f"=== {sheet['name'].upper()} -> {sheet['filename']} ===")
        if sheet["prompt"]:
            lines.append(sheet["prompt"])
        else:
            lines.append(f"You already have a reference image ({sheet['existing_image']}): "
                         "attach it to the conversation; no need to generate it.")
        lines.append("")
    out = paths.get("chatgpt_refs") or (paths["root"] / "chatgpt_reference_sheets.txt")
    return nf.write_text(out, "\n".join(lines))


def compose_image_prompt(body: str, style: Dict[str, Any]) -> str:
    """Master body + style suffix (no duplication) + anti-text clause.

    If the scene carries the diegetic-text exception (e.g. CONFESSION), the generic
    anti-text clause is not added: that scene declares its only legible text.
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
    """Face crop for scenes where the character speaks: reference_<id>_face.png."""
    value = str(reference or "").strip()
    if value.lower().endswith(".png"):
        return value[:-4] + "_face.png"
    return value + "_face.png" if value else ""


def scene_cast_entries(master: Dict[str, Any], scene: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Canonical scene cast with fixed position and reference sheet."""
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
    """First scene of each teaser: candidate 9:16 cover."""
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
        f"NOVEL FACTORY — First-frame queue (ChatGPT) · {title}",
        f"Scenes: {len(entries)} · Destination folder: {paths['frames']}",
        "",
    ]
    if master.get("source_mode") == "original_unproven":
        labeled_lines += [
            "⚠️ WARNING: source_mode is 'original_unproven' — script generated without a proven source.",
            "",
        ]
    labeled_lines += [
        "How to use it:",
        "  0. Generate the reference sheets FIRST with chatgpt_reference_sheets.txt (once)",
        "     and attach ALL of them in the ChatGPT conversation.",
        "  1. Each prompt names the character and their reference_<id>.png: the face is copied from those",
        "     sheets, never described in text.",
        "  2. Load chatgpt_image_prompts_queue.txt in your queue extension (1 prompt per line).",
        "  3. Save each generated image as frame_001.png ... frame_060.png in frames/.",
        "  4. Verify with: python generators/02_export_chatgpt_queue.py "
        f"{ep.get('slug', '')} --check --strict",
        "",
    ]
    for entry in entries:
        cast_note = ", ".join(
            f"{c['name']} (Pos #{c.get('position') or '?'}{'; speaks' if c.get('speaks') else ''})"
            for c in entry["cast"]
        ) or "—"
        cover = "  [9:16 COVER]" if entry["teaser_cover"] else ""
        attach = ", ".join(entry.get("references") or []) or "—"
        if entry.get("face_crops"):
            attach += " + " + ", ".join(entry["face_crops"]) + " (speaker face crop)"
        labeled_lines += [
            f"=== SCENE {entry['scene_id']:03d} | {entry['filename']} | {entry['shot']} | "
            f"{entry['location']} | cast: {cast_note}{cover} ===",
            f"Attach: {attach}",
            entry["prompt"],
            "",
        ]
    nf.write_text(paths["root"] / "chatgpt_image_prompts_queue_labeled.txt", "\n".join(labeled_lines))

    nf.write_json(paths["chatgpt_json"], {
        "episode": ep.get("slug"),
        "title": title,
        "count": len(entries),
        "note": "Each prompt already includes the global style suffix and anti-text clause "
                "(scenes with declared diegetic text use their exception). "
                "face_crops lists the reference_<id>_face.png crops to attach in speaking scenes.",
        "items": entries,
    })


def compose_vertical_prompt(body: str, style: Dict[str, Any]) -> str:
    """Same as horizontal, but forcing 9:16 framing (teaser cover)."""
    prompt = compose_image_prompt(body, style)
    prompt = prompt.replace("16:9 widescreen cinematic still.", "9:16 vertical cinematic still.")
    if "9:16" not in prompt.lower():
        prompt = "9:16 vertical teaser cover. " + prompt
    return " ".join(prompt.split())


def write_thumbnail_prompts(
    paths: Dict[str, Path], master: Dict[str, Any], style: Dict[str, Any], entries: List[Dict[str, Any]]
) -> Optional[Path]:
    """9:16 teaser covers (the first scene of each 6-scene window)."""
    by_id = {e["scene_id"]: e for e in entries}
    covers = teaser_cover_scenes(master)
    if not covers:
        return None
    lines = [
        "NOVEL FACTORY — 9:16 teaser covers (optional, 3 vertical images)",
        "",
        "Generate these covers IN ADDITION to the project's 16:9 frames. Same character and reference.",
        "Suggested filename: thumbnail_teaser_01.png … thumbnail_teaser_03.png",
        "",
    ]
    for idx, sid in enumerate(covers, start=1):
        entry = by_id.get(sid)
        body = str(entry["prompt"]) if entry else ""
        lines += [
            f"=== TEASER {idx} | cover for scene {sid:03d} -> thumbnail_teaser_{idx:02d}.png ===",
            compose_vertical_prompt(body, style),
            "",
        ]
    out = paths.get("chatgpt_thumbs") or (paths["root"] / "chatgpt_thumbnail_prompts.txt")
    return nf.write_text(out, "\n".join(lines))


ROLE_LABELS = {
    "protagonist": "Protagonist",
    "love_interest": "Love interest",
    "antagonist": "Antagonist",
    "antagonist_heir": "Antagonist heir",
    "ally": "Ally",
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
    return visual or "features and build defined by the casting sheet"


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
    return "the main wardrobe described in the casting sheet"


def short_scene_brief(scene: Dict[str, Any], max_words: int = 10) -> str:
    """5-10 word summary for a storyboard panel."""
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
    """All project scenes (never truncated) for PROMPT 001."""
    lines: List[str] = []
    for scene in nf.ordered_scenes(master):
        sid = int(scene.get("scene_id") or 0)
        cast = ", ".join(c["name"] for c in scene_cast_entries(master, scene)) or "—"
        dialogue = " / ".join(
            f"{entry['speaker']}: {entry['line']}" for entry in nf.scene_dialogue_lines(scene)
        ) or "—"
        lines.append(
            f"SCENE {sid:03d} | Act {int(scene.get('act') or 0)} | "
            f"{str(scene.get('location') or '—')} | {str(scene.get('time_of_day') or '—')} | "
            f"Hook: {str(scene.get('on_screen_hook') or '—')} | Cast: {cast} | "
            f"Dialogue: {dialogue}"
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
        f"Using the characters in REF_CAST_MASTER.png as fixed references for faces, ages, bodies and wardrobes, generate A SINGLE horizontal 16:9 storyboard IMAGE divided into a clean 3x2 grid (6 panels numbered 1 to 6) representing MINUTE {batch_number} (Scenes {first} to {last}) of the story in Realistic Cinematic 35mm style:",
        "",
    ]
    if visual:
        lines += [f"Visual look: {visual}.", ""]
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
            f"Panel {idx} — Scene {sid}{place}: {panel} "
            f"Identity anchors: {anchors or 'use the cast sheet positions exactly as attached'}."
        )
    lines += [
        "",
        "Keep exact continuity of positions, faces, bodies, wardrobe, props, locations, lighting and time of day across the 6 panels. Each panel is the literal FIRST FRAME of Shot 1 in its scene: same framing, same camera, same blocking and same key object; the action is already in motion, never frozen. Each panel is a 16:9 cinematic shot with legible action.",
        "100% VISUAL PANEL FORMAT (NO TEXT BOXES): The 6 photographic panels in a 3x2 grid must fill 100% of the 16:9 canvas, separated only by thin divider lines. Place ONLY the small number [1], [2], [3], [4], [5], [6] in the top-left corner of each panel. Drawing dark bottom bars, subtitles, text boxes or written descriptions inside the image is FORBIDDEN.",
    ]
    return "\n".join(lines)


def build_storyboard_grid_items(
    master: Dict[str, Any],
    style: Dict[str, Any],
    pack: Optional[Dict[str, Any]] = None,
) -> List[Dict[str, Any]]:
    """Image queue: 1 cast sheet + one 6-panel storyboard per block."""
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
        "title": f"Master character sheet — {title}",
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
            "title": f"Storyboard minute {batch_number}: scenes {first}–{last}",
            "prompt": _storyboard_grid_prompt(master, style, batch_number, group, total_batches),
        })
    return items


def render_storyboard_grid_queue_text(items: List[Dict[str, Any]]) -> str:
    """One line per prompt (ChatGPT extension queue format)."""
    return "\n".join(" ".join(str(item.get("prompt") or "").split()) for item in items) + "\n"


def write_storyboard_grid_queue(
    paths: Dict[str, Path],
    master: Dict[str, Any],
    style: Dict[str, Any],
    pack: Optional[Dict[str, Any]] = None,
) -> Dict[str, Path]:
    """Export the image queue (cast sheet + one grid per block) as .txt and .json."""
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
        "note": f"1 character sheet (REF_CAST_MASTER.png) + {storyboard_count} storyboards "
                f"with 6 panels (REF_GRID_MIN_01.png … REF_GRID_MIN_{storyboard_count:02d}.png).",
        "items": items,
    })
    return {"txt": txt_path, "json": json_path, "items": items}


def write_master_image_prompt_files(
    paths: Dict[str, Path],
    master: Dict[str, Any],
    style: Dict[str, Any],
) -> Dict[str, Path]:
    """Export PROMPT 001, PROMPT 002 and the project image queue."""
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
        f"NOVEL FACTORY — PROMPT 001 — STORYBOARD GENERATOR · {title}\n"
        f"Includes the full story ({total_scenes} scenes, untruncated) and the "
        f"{storyboard_count} individual prompts for one image per minute.\n\n"
    )
    header_002 = (
        f"NOVEL FACTORY — PROMPT 002 — MASTER CHARACTER SHEET · {title}\n"
        "Attach the storyboard created with PROMPT 001 before pasting this prompt.\n\n"
    )
    storyboard_lines = [
        header_001.rstrip(),
        by_key["prompt_001"]["text"].strip(),
        "",
        "=" * 78,
        f"FULL STORY — {total_scenes} SCENES (UNTRUNCATED)",
        "=" * 78,
        "",
        *scene_breakdown_lines(master),
        "",
        "=" * 78,
        f"{storyboard_count} INDIVIDUAL PROMPTS — ONE STORYBOARD IMAGE PER MINUTE",
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
    nf.info(f"Frames present: {len(present)}/{len(entries)}")
    ok = True
    if missing:
        nf.warn(f"Missing {len(missing)} frames: {', '.join(str(i) for i in missing[:20])}" +
                (" …" if len(missing) > 20 else ""))
        nf.info("Expected as frame_XXX.png / .jpg / .jpeg / .webp in " + str(paths["frames"]))
        if not allow_missing:
            ok = False

    if sheets:
        refs_dir = paths.get("references") or (paths["root"] / "references")
        missing_refs = [s for s in sheets if not (refs_dir / s["filename"]).exists() and not s.get("existing_image")]
        if missing_refs:
            names = ", ".join(s["filename"] for s in missing_refs)
            msg = f"Missing {len(missing_refs)} reference sheets in {refs_dir}: {names}"
            if strict:
                nf.err(msg)
                ok = False
            else:
                nf.warn(msg + " (use --strict to make it an error)")
        else:
            nf.ok(f"Reference sheets present: {len(sheets)}.")

    if ok:
        nf.ok("First frames (and their references) are in place.")
        return 0
    return 0 if allow_missing else 1


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="02 — ChatGPT frame prompt queue.")
    parser.add_argument("project", help="Episode slug.")
    parser.add_argument("--check", action="store_true", help="Only verify the frames in frames/.")
    parser.add_argument("--allow-missing", action="store_true", help="Do not fail if frames are missing.")
    parser.add_argument("--strict", action="store_true", help="Also fail if reference sheets are missing.")
    parser.add_argument("--show", type=str, default="", help="Print prompts from a range (e.g. 1-3).")
    args = parser.parse_args(argv)

    nf.log("")
    nf.log("=" * 70)
    nf.log("  NOVEL FACTORY — 02 · First-frame queue (ChatGPT)")
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
        nf.ok(f"{len(entries)} prompts exported:")
        nf.info(f"{paths['chatgpt_txt'].name}          (pure queue, 1 prompt per line)")
        nf.info(f"chatgpt_image_prompts_queue_labeled.txt (with filename per scene)")
        nf.info(f"{paths['chatgpt_json'].name}         (JSON index)")
        grid_count = nf.master_target_minutes(master)
        nf.ok("Master image prompts:")
        nf.info(f"{image_prompts['prompt_001'].name}  (PROMPT 001 — {len(entries)} scenes + {grid_count} grids)")
        nf.info(f"{image_prompts['prompt_002'].name}  (PROMPT 002 — master character sheet)")
        nf.info(f"{image_prompts['grids_txt'].name}  (queue of {grid_count + 1} images: 1 cast + {grid_count} grids)")
        nf.info(f"{image_prompts['grids_json'].name} (manifest for the queue of {grid_count + 1} images)")

    if not args.check:
        if sheets:
            refs_path = write_reference_sheets(paths, master, sheets)
            to_generate = sum(1 for s in sheets if s["prompt"])
            nf.ok(f"STEP 0 — reference sheets: {len(sheets)} character(s), {to_generate} to generate.")
            nf.info(f"{refs_path.name}   (attach them in ChatGPT before the queue)")
        else:
            nf.info("No visual_reference/reference_image in the master: attach your own reference images.")
        thumbs = write_thumbnail_prompts(paths, master, style, entries)
        if thumbs:
            nf.ok(f"9:16 teaser covers: {thumbs.name}")

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
        nf.log(f"  Next: generate the frames and confirm with --check, then")
        nf.log(f"  python generators/03_export_omni_queue.py {args.project}")
        nf.log("")
    return rc


if __name__ == "__main__":
    try:
        sys.exit(main())
    except nf.NFError as exc:
        nf.err(str(exc))
        sys.exit(1)

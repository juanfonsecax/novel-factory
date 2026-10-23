#!/usr/bin/env python3
"""03 — Export the video queues (Omni 1.1 Flash, Muse AI and Google Flow).

Composes, scene by scene, the final video prompt from structured master data
(nothing is trusted to loose LLM prose):

  - shot plan with hard internal cuts and their timings,
  - dialogue with per-character voice and delivery (English voice lock),
  - ambience/sfx, continuity, style and negative prompts.

Outputs in the episode folder (depending on --platform):
  omni_video_prompts_queue.{csv,json,txt}         Omni 1.1 Flash (default)
  muse_ai_video_prompts_queue.{csv,json,txt}      Muse AI
  google_flow_video_prompts_queue.{csv,json,txt}  Google Flow (Veo)

Usage:
  python generators/03_export_omni_queue.py my_episode
  python generators/03_export_omni_queue.py my_episode --platform muse
  python generators/03_export_omni_queue.py my_episode --platform flow
  python generators/03_export_omni_queue.py my_episode --platform all
  python generators/03_export_omni_queue.py my_episode --only-missing
  python generators/03_export_omni_queue.py my_episode --check
"""
from __future__ import annotations

import argparse
import csv
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

format_character_anchors = nf.format_character_anchors


class _SafeDict(dict):
    def __missing__(self, key: str) -> str:  # keep the placeholder if a key is missing
        return "{" + key + "}"


PLATFORM_SPECS: Dict[str, Dict[str, Any]] = {
    "omni": {
        "id": "omni",
        "label": "Omni 1.1 Flash",
        "template": "omni_prompt_template",
        "csv": "omni_csv",
        "json": "omni_json",
        "txt": "omni_txt",
        "manifest": "omni_video_prompts_queue",
        "notes": [
            "First Frame mode: upload frame_XXX.png and paste the full prompt.",
            "Exact duration: 10 s. Native English audio. No music.",
            "Download the clip as scene_XXX.mp4 inside raw_clips/.",
        ],
    },
    "muse": {
        "id": "muse",
        "label": "Muse AI",
        "template": "muse_prompt_template",
        "csv": "muse_csv",
        "json": "muse_json",
        "txt": "muse_txt",
        "manifest": "muse_ai_video_prompts_queue",
        "notes": [
            "Upload frame_XXX.png as the first frame and paste the full prompt.",
            "Request 10 s, 16:9 and native English audio.",
            "Verify the 3 exact cuts (0/3/7 s) and download as scene_XXX.mp4 in raw_clips/.",
        ],
    },
    "flow": {
        "id": "flow",
        "label": "Google Flow (Veo)",
        "template": "flow_prompt_template",
        "csv": "flow_csv",
        "json": "flow_json",
        "txt": "flow_txt",
        "manifest": "google_flow_video_prompts_queue",
        "notes": [
            "Use 'Frames to Video' with frame_XXX.png as the ingredient/first frame.",
            "If Flow limits you to 8 s, generate 8 s: post-production extends it to 10 s.",
            "Dialogue must finish before 8.5 s. Download as scene_XXX.mp4.",
        ],
    },
}
PLATFORM_ORDER = ("omni", "muse", "flow")


def _characters_by_key(master: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    out: Dict[str, Dict[str, Any]] = {}
    for character in master.get("characters") or []:
        if not isinstance(character, dict):
            continue
        for key in (str(character.get("id") or ""), str(character.get("name") or "")):
            if key:
                out[key.strip().upper()] = character
    return out


def _voice_for(speaker: str, characters: Dict[str, Dict[str, Any]], style: Dict[str, Any]) -> str:
    archetypes = ((style.get("voice_lock") or {}).get("character_voice_archetypes") or {})
    character = characters.get(str(speaker or "").strip().upper())
    if character:
        explicit = str(character.get("voice_lock") or "").strip()
        if explicit:
            return explicit
        archetype = str(character.get("archetype") or "").strip().lower()
        if archetype and archetypes.get(archetype):
            return str(archetypes[archetype])
    return ""


def _shot_block(scene: Dict[str, Any], templates: Dict[str, Any],
                characters: Optional[Dict[str, Dict[str, Any]]] = None) -> str:
    characters = characters or {}
    cuts = scene.get("internal_cuts") or []
    lines: List[str] = [str(templates.get("shot_block_header") or "SHOT PLAN:")]
    for idx, cut in enumerate(cuts):
        at = float(cut.get("at") or 0.0)
        framing = str(cut.get("framing") or "medium shot").strip()
        action = str(cut.get("action") or "").strip() or "the subject continues the motion from the previous beat."
        shot_range = str(cut.get("range") or (nf.SHOT_RANGES[idx] if idx < len(nf.SHOT_RANGES) else "")).strip()
        if cut.get("dialogue"):
            action = f"{action} [DIALOGUE SHOT: speaker on camera, mouth visible for the whole line.]"
        elif cut.get("silent"):
            action = f"{action} [SILENT SHOT: no dialogue, no speaking, mouths closed.]"
        if idx == 0:
            end = float(cuts[1].get("at") or 10.0) if len(cuts) > 1 else 10.0
            line = str(templates.get("shot_first_template") or "").format_map(_SafeDict(
                n=idx + 1, end=end, framing=framing, action=action, range=shot_range))
        else:
            line = str(templates.get("shot_cut_template") or "").format_map(_SafeDict(
                n=idx + 1, at=at, framing=framing, action=action, range=shot_range))
        lines.append(line)
    suffix = str(templates.get("shot_last_suffix") or "").strip()
    if suffix:
        lines.append(suffix)
    if scene.get("present_silent"):
        names = []
        for cid in scene.get("present_silent") or []:
            character = characters.get(str(cid or "").strip().upper()) or {}
            names.append(str(character.get("name") or cid or "").strip())
        names = ", ".join(name for name in names if name)
        if names:
            lines.append(f"PRESENT BUT SILENT: {names} — mouths closed for the whole scene, no lines.")
    start = scene.get("object_start") or {}
    end = scene.get("object_end") or {}
    if str(start.get("name") or "").strip():
        lines.append(
            f"OBJECT LOCK: {start.get('name')} stays visible on camera at the start — {start.get('visible')}; "
            f"at the end — {end.get('visible')}."
        )
        if scene.get("object_hidden"):
            lines.append(
                "The container interior is never shown: no empty interior, no full look inside, "
                "it stays in shadow and out of frame."
            )
    texts = scene.get("diegetic_text") or []
    if texts:
        lines.append(
            "DIEGETIC TEXT ON OBJECT (the only legible text allowed in frame): "
            + ", ".join(f'"{str(t)}"' for t in texts) + "."
        )
    return "\n".join(lines)


def _timeline_block(scene: Dict[str, Any], templates: Dict[str, Any]) -> str:
    """Explicit timeline: segments and absolute hard-cut marks."""
    cuts = scene.get("internal_cuts") or []
    total = float(scene.get("duration_s") or nf.SCENE_SECONDS)
    header = str(templates.get("timeline_header") or "TIMELINE (one continuous 10 s take):")
    line_tpl = str(templates.get("timeline_line_template") or "  {a:.1f}s to {b:.1f}s  [{framing}] {action}")
    marks_tpl = str(templates.get("timeline_marks_template") or "Hard cuts exactly at {marks} s. No dissolves.")
    lines: List[str] = [header]
    marks: List[float] = []
    for idx, cut in enumerate(cuts):
        a = float(cut.get("at") or 0.0)
        b = float(cuts[idx + 1].get("at")) if idx + 1 < len(cuts) else total
        framing = str(cut.get("framing") or "medium shot").strip()
        action = str(cut.get("action") or "").strip() or "the subject continues moving from the previous beat."
        lines.append(line_tpl.format(a=a, b=b, framing=framing, action=action))
        if idx:
            marks.append(a)
    if marks:
        lines.append(marks_tpl.format(marks=", ".join(f"{m:.1f}" for m in marks)))
    return "\n".join(lines)


def _dialogue_block(scene: Dict[str, Any], characters: Dict[str, Dict[str, Any]],
                    style: Dict[str, Any]) -> str:
    voice_lock = style.get("voice_lock") or {}
    line_template = str(voice_lock.get("dialogue_line_template") or '{speaker} ({delivery}): "{line}"')
    default_delivery = str(voice_lock.get("default_delivery") or "measured, low")
    lines: List[str] = []
    voices: List[str] = []
    for entry in nf.scene_dialogue_lines(scene):
        speaker = entry["speaker"] or "NARRATOR"
        delivery = entry["delivery"] or default_delivery
        lines.append(line_template.format_map(_SafeDict(
            speaker=speaker.upper(), delivery=delivery, line=entry["line"])))
        voice = _voice_for(speaker, characters, style)
        if voice and f"{speaker.upper()} —" not in " ".join(voices):
            voices.append(f"{speaker.upper()} — {voice}")
    if not lines:
        lines = ["(no spoken dialogue in this scene: diegetic ambience only, no voices)"]
    block = "\n".join(lines)
    if voices:
        block += "\n\nVOICE NOTES: " + "; ".join(voices) + "."
    return block


def _continuity_block(scene: Dict[str, Any], master: Dict[str, Any], characters: Dict[str, Dict[str, Any]]) -> str:
    parts: List[str] = []
    explicit = str(scene.get("continuity_present") or "").strip()
    if not explicit:
        raw = str(scene.get("continuity") or "").strip()
        explicit, _removed = nf.strip_future_refs(raw)
    if explicit:
        parts.append(explicit)
    act = int(scene.get("act") or 0)
    for key in scene.get("characters_present") or scene.get("characters") or []:
        character = characters.get(str(key).strip().upper())
        if not character:
            continue
        wardrobes = character.get("wardrobe_by_act") or []
        if isinstance(wardrobes, list) and 1 <= act <= len(wardrobes) and str(wardrobes[act - 1]).strip():
            parts.append(f"{character.get('name') or key} wardrobe (act {act}): {str(wardrobes[act - 1]).strip()}")
    key_object = str((scene.get("object_start") or {}).get("name") or "").strip() or nf.extract_key_object(scene)
    if key_object:
        parts.append(f"Key object in frame: {key_object}.")
    if not parts:
        parts.append("Keep the same faces, wardrobe, props and location as the provided first frame.")
    return " ".join(parts)


def compose_video_prompt(
    master: Dict[str, Any],
    scene: Dict[str, Any],
    paths: Dict[str, Path],
    style: Dict[str, Any],
    platform: str = "omni",
) -> str:
    platform = str(platform or "omni").strip().lower()
    spec = PLATFORM_SPECS.get(platform)
    if not spec:
        raise nf.NFError(f"Plataforma desconocida: {platform!r}. Usa: {', '.join(PLATFORM_ORDER)}")
    templates = style.get("prompt_templates") or {}
    visual = style.get("visual_style_lock") or {}
    characters = _characters_by_key(master)
    frame = nf.find_frame(paths["frames"], int(scene.get("scene_id") or 0))
    sid = int(scene.get("scene_id") or 0)
    frame_file = frame.name if frame else f"{nf.frame_stem(sid)}.png"

    values = _SafeDict(
        frame_file=frame_file,
        scene_id=f"{sid:03d}",
        platform_label=str(spec.get("label") or platform),
        speech_seconds=f"{nf.scene_speech_seconds(scene):.1f}",
        dialogue_words=str(nf.scene_words(scene)),
        shot_block=_shot_block(scene, templates, characters),
        timeline_block=_timeline_block(scene, templates),
        dialogue_block=_dialogue_block(scene, characters, style),
        storyboard_panel=str(scene.get("storyboard_panel") or nf.build_storyboard_panel_description(scene, master)),
        character_anchors=str(
            scene.get("character_anchors")
            or format_character_anchors(scene, master.get("characters_locked") or master.get("characters") or [])
        ),
        key_object=nf.extract_key_object(scene),
        ambience=str(scene.get("sfx_ambience") or "").strip() or "natural room tone, cloth movement, footfalls",
        camera_block=str(scene.get("camera") or "").strip()
        or str(templates.get("camera_block_default") or "Handheld but controlled, subtle drift."),
        continuity=_continuity_block(scene, master, characters),
        style=str(visual.get("look") or "prestige cinematic short-drama, photoreal, 35mm anamorphic"),
        negative=str(visual.get("video_negative") or "").strip(),
    )
    template = str(
        templates.get(str(spec.get("template") or "omni_prompt_template"))
        or templates.get("omni_prompt_template")
        or "{shot_block}\n{dialogue_block}"
    )
    prompt = template.format_map(values)
    return "\n".join(line.rstrip() for line in prompt.splitlines()).strip()


def build_rows(
    master: Dict[str, Any],
    paths: Dict[str, Path],
    style: Dict[str, Any],
    platform: str = "omni",
) -> List[Dict[str, Any]]:
    platform = str(platform or "omni").strip().lower()
    spec = PLATFORM_SPECS.get(platform)
    if not spec:
        raise nf.NFError(f"Plataforma desconocida: {platform!r}. Usa: {', '.join(PLATFORM_ORDER)}")
    rows: List[Dict[str, Any]] = []
    prepared = nf.prepare_master_locks_safe(master, style)
    for scene in nf.ordered_scenes(prepared):
        sid = int(scene.get("scene_id") or 0)
        frame = nf.find_frame(paths["frames"], sid)
        clip = nf.find_clip(paths["raw_clips"], sid)
        attach_list = nf.build_scene_attachments(scene, master)
        rows.append({
            "scene_id": sid,
            "platform": platform,
            "platform_label": str(spec.get("label") or platform),
            "frame_file": frame.name if frame else f"{nf.frame_stem(sid)}.png",
            "frame_status": "ok" if frame else "missing",
            "output_file": f"{nf.scene_stem(sid)}.mp4",
            "duration_seconds": int(scene.get("duration_s") or nf.SCENE_SECONDS),
            "dialogue_words": nf.scene_words(scene),
            "speech_seconds": round(nf.scene_speech_seconds(scene), 2),
            "status": "done" if clip else "pending",
            "attach": attach_list,
            "prompt": compose_video_prompt(master, scene, paths, style, platform),
        })
    return rows


def write_queue_files(
    paths: Dict[str, Path],
    master: Dict[str, Any],
    rows: List[Dict[str, Any]],
    platform: str = "omni",
) -> None:
    platform = str(platform or "omni").strip().lower()
    spec = PLATFORM_SPECS.get(platform)
    if not spec:
        raise nf.NFError(f"Plataforma desconocida: {platform!r}. Usa: {', '.join(PLATFORM_ORDER)}")
    label = str(spec.get("label") or platform)
    fieldnames = [
        "scene_id", "platform", "frame_file", "output_file", "duration_seconds",
        "dialogue_words", "speech_seconds", "status", "attach", "prompt",
    ]
    with paths[str(spec["csv"])].open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for row in rows:
            entry = dict(row)
            if isinstance(entry.get("attach"), list):
                entry["attach"] = ", ".join(entry["attach"])
            writer.writerow({k: entry.get(k, "") for k in fieldnames})

    ep = nf.episode_meta(master)
    notes = list(spec.get("notes") or [])
    notes.insert(0, nf.PRODUCTION_ATTACH_NOTE)
    if master.get("source_mode") == "original_unproven":
        notes.insert(1, "WARNING: source_mode is original_unproven (script not validated).")

    nf.write_json(paths[str(spec["json"])], {
        "episode": ep.get("slug"),
        "title": ep.get("title"),
        "platform": platform,
        "platform_label": label,
        "production_note": nf.PRODUCTION_ATTACH_NOTE,
        "source_mode": master.get("source_mode", "proven_adaptation"),
        "frame_dir": str(paths["frames"]),
        "raw_clips_dir": str(paths["raw_clips"]),
        "output_pattern": "scene_XXX.mp4",
        "duration_seconds": nf.SCENE_SECONDS,
        "aspect": "16:9",
        "notes": notes,
        "items": rows,
    })

    lines = [
        f"NOVEL FACTORY — Video queue ({label}, First Frame, 10 s) · {ep.get('title')}",
        f"Frames: {paths['frames']}  →  Clips: {paths['raw_clips']}",
        "",
        f"PRODUCTION NOTE: {nf.PRODUCTION_ATTACH_NOTE}",
        "",
    ]
    if master.get("source_mode") == "original_unproven":
        lines += [
            "⚠️ WARNING: source_mode is 'original_unproven' — script generated without a proven source.",
            "",
        ]
    for row in rows:
        attach_str = ", ".join(row.get("attach") or [])
        lines += [
            f"=== SCENE {row['scene_id']:03d} | frame: {row['frame_file']} | output: {row['output_file']} "
            f"| status: {row['status']} ===",
            f"attach: [{attach_str}]",
            row["prompt"],
            "",
        ]
    nf.write_text(paths[str(spec["txt"])], "\n".join(lines))


def write_muse_batches(
    paths: Dict[str, Path],
    master: Dict[str, Any],
    style: Dict[str, Any],
    aspect_ratio: str = "",
) -> Dict[str, Any]:
    """Muse AI queue grouped into 6-scene blocks (1 minute per block)."""
    return mpl.write_muse_batch_files(
        paths["root"],
        master,
        style,
        basename="muse_ai_batches_queue",
        aspect_ratio=aspect_ratio,
    )


def run_check(paths: Dict[str, Path], rows: List[Dict[str, Any]], allow_missing: bool) -> int:
    frames_ok = sum(1 for r in rows if r["frame_status"] == "ok")
    clips_ok = sum(1 for r in rows if r["status"] == "done")
    missing_frames = [r["scene_id"] for r in rows if r["frame_status"] != "ok"]
    missing_clips = [r["scene_id"] for r in rows if r["status"] != "done"]
    nf.log("")
    nf.info(f"First frames: {frames_ok}/{len(rows)}")
    nf.info(f"Video clips:         {clips_ok}/{len(rows)}")
    if missing_frames:
        nf.warn("Missing frames: " + ", ".join(map(str, missing_frames[:20])) +
                (" …" if len(missing_frames) > 20 else ""))
    if missing_clips:
        nf.info("Missing clips: " + ", ".join(map(str, missing_clips[:20])) +
                (" …" if len(missing_clips) > 20 else ""))
    if not missing_clips:
        nf.ok(f"All {len(rows)} clips are ready for assembly.")
        return 0
    if missing_frames and not allow_missing:
        nf.warn("Generate the missing frames first (02) before producing the videos.")
    return 0 if allow_missing else 1


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="03 — Video prompt queue for Omni, Muse AI and Google Flow.")
    parser.add_argument("project", help="Episode slug.")
    parser.add_argument("--platform", choices=list(PLATFORM_ORDER) + ["all"], default="omni",
                        help="Video platform: omni (default), muse, flow or all.")
    parser.add_argument("--only-missing", action="store_true", help="Export only scenes without a clip.")
    parser.add_argument("--check", action="store_true", help="Verify frames and clips without re-exporting.")
    parser.add_argument("--allow-missing", action="store_true", help="Do not fail if files are missing.")
    parser.add_argument("--show", type=str, default="", help="Print prompts from a range (e.g. 1-2).")
    args = parser.parse_args(argv)

    platforms = list(PLATFORM_ORDER) if args.platform == "all" else [args.platform]
    labels = ", ".join(str(PLATFORM_SPECS[p]["label"]) for p in platforms)
    nf.log("")
    nf.log("=" * 70)
    nf.log(f"  NOVEL FACTORY — 03 · Video queue ({labels} · 10 s · First Frame)")
    nf.log("=" * 70)

    paths = nf.resolve_project(args.project)
    master = nf.load_master(paths["root"])
    style = nf.load_style_locks()
    last_rows: List[Dict[str, Any]] = []
    want = set(nf.parse_ranges(args.show)) if args.show else set()

    for platform in platforms:
        spec = PLATFORM_SPECS[platform]
        label = str(spec["label"])
        rows = build_rows(master, paths, style, platform)
        total = len(rows)

        if args.only_missing:
            rows = [r for r in rows if r["status"] != "done"]
            nf.info(f"[{label}] --only-missing filter: {len(rows)} of {total} scenes to generate.")

        if not args.check:
            write_queue_files(paths, master, rows, platform)
            nf.log("")
            nf.ok(f"[{label}] {len(rows)} video prompts exported:")
            nf.info(paths[str(spec["csv"])].name + "  (main queue, quoted fields)")
            nf.info(paths[str(spec["json"])].name + " (full manifest)")
            nf.info(paths[str(spec["txt"])].name + "  (readable, block per scene)")

        if want:
            nf.log("")
            for row in rows:
                if row["scene_id"] in want:
                    nf.log(f"--- [{label}] SCENE {row['scene_id']:03d} -> {row['output_file']} ---")
                    nf.log(row["prompt"])
                    nf.log("")
        last_rows = rows

    if not args.check:
        batch_files = write_muse_batches(paths, master, style)
        nf.log("")
        nf.ok(
            f"[Muse AI] {len(batch_files['batches'])} 1-minute batches (6 scenes) exported:"
        )
        nf.info(batch_files["txt"].name + "  (blocks with attachments, camera, SFX, dialogue and 2 commands)")
        nf.info(batch_files["json"].name + " (batch manifest)")
        nf.info("Attachments per batch: REF_CAST_MASTER.png + REF_GRID_MIN_XX.png · "
                "16:9 (YouTube) and 9:16 (Reels) commands.")

    rc = run_check(paths, last_rows, args.allow_missing) if not want or args.check else 0
    if not args.check and not want:
        nf.log("")
        nf.log(f"  When you have clips in raw_clips/: python post_production/04_assemble_novel_ffmpeg.py {args.project}")
        nf.log("")
    return rc


if __name__ == "__main__":
    try:
        sys.exit(main())
    except nf.NFError as exc:
        nf.err(str(exc))
        sys.exit(1)

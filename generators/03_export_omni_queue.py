#!/usr/bin/env python3
"""03 — Exporta la cola de video (Omni 1.1 Flash, modo First Frame, 10 s).

Compone, escena por escena, el prompt de video definitivo a partir de datos
estructurados del maestro (nada se confía a prosa suelta del LLM):

  - plan de planos con cortes internos duros y sus tiempos,
  - diálogo con voz y entrega por personaje (bloqueo de voz en inglés),
  - ambiencia/sfx, continuidad, estilo y prompts negativos.

Salidas en la carpeta del episodio:
  omni_video_prompts_queue.csv   (cola principal: scene_id, frame, output, prompt)
  omni_video_prompts_queue.json  (manifiesto completo)
  omni_video_prompts_queue.txt   (legible, un bloque por escena)

Uso:
  python generators/03_export_omni_queue.py mi_episodio
  python generators/03_export_omni_queue.py mi_episodio --only-missing
  python generators/03_export_omni_queue.py mi_episodio --check
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

NF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(NF_ROOT))
import nf_core as nf  # noqa: E402


class _SafeDict(dict):
    def __missing__(self, key: str) -> str:  # deja el marcador si falta una clave
        return "{" + key + "}"


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


def _shot_block(scene: Dict[str, Any], templates: Dict[str, Any]) -> str:
    cuts = scene.get("internal_cuts") or []
    lines: List[str] = [str(templates.get("shot_block_header") or "SHOT PLAN:")]
    for idx, cut in enumerate(cuts):
        at = float(cut.get("at") or 0.0)
        framing = str(cut.get("framing") or "medium shot").strip()
        action = str(cut.get("action") or "").strip() or "Hold the moment with minimal movement."
        if idx == 0:
            end = float(cuts[1].get("at") or 10.0) if len(cuts) > 1 else 10.0
            line = str(templates.get("shot_first_template") or "").format_map(_SafeDict(
                n=idx + 1, end=end, framing=framing, action=action))
        else:
            line = str(templates.get("shot_cut_template") or "").format_map(_SafeDict(
                n=idx + 1, at=at, framing=framing, action=action))
        lines.append(line)
    suffix = str(templates.get("shot_last_suffix") or "").strip()
    if suffix:
        lines.append(suffix)
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
    explicit = str(scene.get("continuity") or "").strip()
    if explicit:
        parts.append(explicit)
    act = int(scene.get("act") or 0)
    for key in scene.get("characters") or []:
        character = characters.get(str(key).strip().upper())
        if not character:
            continue
        wardrobes = character.get("wardrobe_by_act") or []
        if isinstance(wardrobes, list) and 1 <= act <= len(wardrobes) and str(wardrobes[act - 1]).strip():
            parts.append(f"{character.get('name') or key} wardrobe (act {act}): {str(wardrobes[act - 1]).strip()}")
    if not parts:
        parts.append("Keep the same faces, wardrobe, props and location as the provided first frame.")
    return " ".join(parts)


def compose_video_prompt(
    master: Dict[str, Any],
    scene: Dict[str, Any],
    paths: Dict[str, Path],
    style: Dict[str, Any],
) -> str:
    templates = style.get("prompt_templates") or {}
    visual = style.get("visual_style_lock") or {}
    characters = _characters_by_key(master)
    frame = nf.find_frame(paths["frames"], int(scene.get("scene_id") or 0))
    sid = int(scene.get("scene_id") or 0)
    frame_file = frame.name if frame else f"{nf.frame_stem(sid)}.png"

    values = _SafeDict(
        frame_file=frame_file,
        scene_id=f"{sid:03d}",
        shot_block=_shot_block(scene, templates),
        dialogue_block=_dialogue_block(scene, characters, style),
        ambience=str(scene.get("sfx_ambience") or "").strip() or "natural room tone, cloth movement, footfalls",
        camera_block=str(scene.get("camera") or "").strip()
        or str(templates.get("camera_block_default") or "Handheld but controlled, subtle drift."),
        continuity=_continuity_block(scene, master, characters),
        style=str(visual.get("look") or "prestige cinematic short-drama, photoreal, 35mm anamorphic"),
        negative=str(visual.get("video_negative") or "").strip(),
    )
    template = str(templates.get("omni_prompt_template") or "{shot_block}\n{dialogue_block}")
    prompt = template.format_map(values)
    return "\n".join(line.rstrip() for line in prompt.splitlines()).strip()


def build_rows(master: Dict[str, Any], paths: Dict[str, Path], style: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for scene in nf.ordered_scenes(master):
        sid = int(scene.get("scene_id") or 0)
        frame = nf.find_frame(paths["frames"], sid)
        clip = nf.find_clip(paths["raw_clips"], sid)
        rows.append({
            "scene_id": sid,
            "frame_file": frame.name if frame else f"{nf.frame_stem(sid)}.png",
            "frame_status": "ok" if frame else "missing",
            "output_file": f"{nf.scene_stem(sid)}.mp4",
            "duration_seconds": int(scene.get("duration_s") or nf.SCENE_SECONDS),
            "status": "done" if clip else "pending",
            "prompt": compose_video_prompt(master, scene, paths, style),
        })
    return rows


def write_queue_files(paths: Dict[str, Path], master: Dict[str, Any], rows: List[Dict[str, Any]]) -> None:
    fieldnames = ["scene_id", "frame_file", "output_file", "duration_seconds", "status", "prompt"]
    with paths["omni_csv"].open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row[k] for k in fieldnames})

    ep = nf.episode_meta(master)
    nf.write_json(paths["omni_json"], {
        "episode": ep.get("slug"),
        "title": ep.get("title"),
        "frame_dir": str(paths["frames"]),
        "raw_clips_dir": str(paths["raw_clips"]),
        "output_pattern": "scene_XXX.mp4",
        "duration_seconds": nf.SCENE_SECONDS,
        "aspect": "16:9",
        "notes": [
            "Modo First Frame: sube el frame_XXX.png y pega el prompt completo.",
            "Duración exacta: 10 s. Audio nativo en inglés. Sin música.",
            "Descarga el clip como scene_XXX.mp4 dentro de raw_clips/.",
        ],
        "items": rows,
    })

    lines = [
        f"NOVEL FACTORY — Cola de video (Omni 1.1 Flash, First Frame, 10 s) · {ep.get('title')}",
        f"Frames: {paths['frames']}  →  Clips: {paths['raw_clips']}",
        "",
    ]
    for row in rows:
        lines += [
            f"=== SCENE {row['scene_id']:03d} | frame: {row['frame_file']} | salida: {row['output_file']} "
            f"| estado: {row['status']} ===",
            row["prompt"],
            "",
        ]
    nf.write_text(paths["omni_txt"], "\n".join(lines))


def run_check(paths: Dict[str, Path], rows: List[Dict[str, Any]], allow_missing: bool) -> int:
    frames_ok = sum(1 for r in rows if r["frame_status"] == "ok")
    clips_ok = sum(1 for r in rows if r["status"] == "done")
    missing_frames = [r["scene_id"] for r in rows if r["frame_status"] != "ok"]
    missing_clips = [r["scene_id"] for r in rows if r["status"] != "done"]
    nf.log("")
    nf.info(f"Fotogramas iniciales: {frames_ok}/{len(rows)}")
    nf.info(f"Clips de video:      {clips_ok}/{len(rows)}")
    if missing_frames:
        nf.warn("Faltan frames: " + ", ".join(map(str, missing_frames[:20])) +
                (" …" if len(missing_frames) > 20 else ""))
    if missing_clips:
        nf.info("Faltan clips: " + ", ".join(map(str, missing_clips[:20])) +
                (" …" if len(missing_clips) > 20 else ""))
    if not missing_clips:
        nf.ok("Los 60 clips están listos para el ensamblaje.")
        return 0
    if missing_frames and not allow_missing:
        nf.warn("Genera primero los frames faltantes (02) antes de producir los videos.")
    return 0 if allow_missing else 1


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="03 — Cola de prompts de video para Omni 1.1 Flash.")
    parser.add_argument("project", help="Slug del episodio.")
    parser.add_argument("--only-missing", action="store_true", help="Exporta solo las escenas sin clip.")
    parser.add_argument("--check", action="store_true", help="Verifica frames y clips sin reexportar.")
    parser.add_argument("--allow-missing", action="store_true", help="No falla si faltan archivos.")
    parser.add_argument("--show", type=str, default="", help="Imprime prompts de un rango (ej: 1-2).")
    args = parser.parse_args(argv)

    nf.log("")
    nf.log("=" * 70)
    nf.log("  NOVEL FACTORY — 03 · Cola de video (Omni 1.1 Flash · 10 s · First Frame)")
    nf.log("=" * 70)

    paths = nf.resolve_project(args.project)
    master = nf.load_master(paths["root"])
    style = nf.load_style_locks()
    rows = build_rows(master, paths, style)
    total = len(rows)

    if args.only_missing:
        rows = [r for r in rows if r["status"] != "done"]
        nf.info(f"Filtro --only-missing: {len(rows)} de {total} escenas por generar.")

    if not args.check:
        write_queue_files(paths, master, rows)
        nf.log("")
        nf.ok(f"{len(rows)} prompts de video exportados:")
        nf.info(paths["omni_csv"].name + "  (cola principal, campos citados)")
        nf.info(paths["omni_json"].name + " (manifiesto completo)")
        nf.info(paths["omni_txt"].name + "  (legible, bloque por escena)")

    if args.show:
        want = set(nf.parse_ranges(args.show))
        nf.log("")
        for row in rows:
            if row["scene_id"] in want:
                nf.log(f"--- SCENE {row['scene_id']:03d} -> {row['output_file']} ---")
                nf.log(row["prompt"])
                nf.log("")

    rc = run_check(paths, rows, args.allow_missing) if not args.show or args.check else 0
    if not args.check and not args.show:
        nf.log("")
        nf.log(f"  Cuando tengas clips en raw_clips/: python post_production/04_assemble_novel_ffmpeg.py {args.project}")
        nf.log("")
    return rc


if __name__ == "__main__":
    try:
        sys.exit(main())
    except nf.NFError as exc:
        nf.err(str(exc))
        sys.exit(1)

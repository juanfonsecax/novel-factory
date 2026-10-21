#!/usr/bin/env python3
"""03 — Exporta las colas de video (Omni 1.1 Flash, Muse AI y Google Flow).

Compone, escena por escena, el prompt de video definitivo a partir de datos
estructurados del maestro (nada se confía a prosa suelta del LLM):

  - plan de planos con cortes internos duros y sus tiempos,
  - diálogo con voz y entrega por personaje (bloqueo de voz en inglés),
  - ambiencia/sfx, continuidad, estilo y prompts negativos.

Salidas en la carpeta del episodio (según --platform):
  omni_video_prompts_queue.{csv,json,txt}         Omni 1.1 Flash (default)
  muse_ai_video_prompts_queue.{csv,json,txt}      Muse AI
  google_flow_video_prompts_queue.{csv,json,txt}  Google Flow (Veo)

Uso:
  python generators/03_export_omni_queue.py mi_episodio
  python generators/03_export_omni_queue.py mi_episodio --platform muse
  python generators/03_export_omni_queue.py mi_episodio --platform flow
  python generators/03_export_omni_queue.py mi_episodio --platform all
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
GENERATORS_DIR = Path(__file__).resolve().parent
for _path in (NF_ROOT, GENERATORS_DIR):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))
import nf_core as nf  # noqa: E402
import master_prompts_library as mpl  # noqa: E402

format_character_anchors = nf.format_character_anchors


class _SafeDict(dict):
    def __missing__(self, key: str) -> str:  # deja el marcador si falta una clave
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
            "Modo First Frame: sube el frame_XXX.png y pega el prompt completo.",
            "Duración exacta: 10 s. Audio nativo en inglés. Sin música.",
            "Descarga el clip como scene_XXX.mp4 dentro de raw_clips/.",
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
            "Sube el frame_XXX.png como primer fotograma y pega el prompt completo.",
            "Solicita 10 s, 16:9 y audio nativo en inglés.",
            "Verifica los 3 cortes exactos (0/3/7 s) y descarga como scene_XXX.mp4 en raw_clips/.",
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
            "Usa 'Frames to Video' con frame_XXX.png como ingrediente/primer fotograma.",
            "Si Flow limita a 8 s, genera 8 s: la postproducción extiende a 10 s.",
            "El diálogo debe terminar antes de 8.5 s. Descarga como scene_XXX.mp4.",
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


def _shot_block(scene: Dict[str, Any], templates: Dict[str, Any]) -> str:
    cuts = scene.get("internal_cuts") or []
    lines: List[str] = [str(templates.get("shot_block_header") or "SHOT PLAN:")]
    for idx, cut in enumerate(cuts):
        at = float(cut.get("at") or 0.0)
        framing = str(cut.get("framing") or "medium shot").strip()
        action = str(cut.get("action") or "").strip() or "the subject continues the motion from the previous beat."
        shot_range = str(cut.get("range") or (nf.SHOT_RANGES[idx] if idx < len(nf.SHOT_RANGES) else "")).strip()
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
    return "\n".join(lines)


def _timeline_block(scene: Dict[str, Any], templates: Dict[str, Any]) -> str:
    """Línea de tiempo explícita: tramos y marcas absolutas de corte duro."""
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
    key_object = nf.extract_key_object(scene)
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
        shot_block=_shot_block(scene, templates),
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
    for scene in nf.ordered_scenes(master):
        sid = int(scene.get("scene_id") or 0)
        frame = nf.find_frame(paths["frames"], sid)
        clip = nf.find_clip(paths["raw_clips"], sid)
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
        "dialogue_words", "speech_seconds", "status", "prompt",
    ]
    with paths[str(spec["csv"])].open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})

    ep = nf.episode_meta(master)
    nf.write_json(paths[str(spec["json"])], {
        "episode": ep.get("slug"),
        "title": ep.get("title"),
        "platform": platform,
        "platform_label": label,
        "frame_dir": str(paths["frames"]),
        "raw_clips_dir": str(paths["raw_clips"]),
        "output_pattern": "scene_XXX.mp4",
        "duration_seconds": nf.SCENE_SECONDS,
        "aspect": "16:9",
        "notes": list(spec.get("notes") or []),
        "items": rows,
    })

    lines = [
        f"NOVEL FACTORY — Cola de video ({label}, First Frame, 10 s) · {ep.get('title')}",
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
    nf.write_text(paths[str(spec["txt"])], "\n".join(lines))


def write_muse_batches(
    paths: Dict[str, Path],
    master: Dict[str, Any],
    style: Dict[str, Any],
    aspect_ratio: str = "",
) -> Dict[str, Any]:
    """Cola de Muse AI agrupada en bloques de 6 escenas (1 minuto por bloque)."""
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
    parser = argparse.ArgumentParser(description="03 — Cola de prompts de video para Omni, Muse AI y Google Flow.")
    parser.add_argument("project", help="Slug del episodio.")
    parser.add_argument("--platform", choices=list(PLATFORM_ORDER) + ["all"], default="omni",
                        help="Plataforma de video: omni (default), muse, flow o all.")
    parser.add_argument("--only-missing", action="store_true", help="Exporta solo las escenas sin clip.")
    parser.add_argument("--check", action="store_true", help="Verifica frames y clips sin reexportar.")
    parser.add_argument("--allow-missing", action="store_true", help="No falla si faltan archivos.")
    parser.add_argument("--show", type=str, default="", help="Imprime prompts de un rango (ej: 1-2).")
    args = parser.parse_args(argv)

    platforms = list(PLATFORM_ORDER) if args.platform == "all" else [args.platform]
    labels = ", ".join(str(PLATFORM_SPECS[p]["label"]) for p in platforms)
    nf.log("")
    nf.log("=" * 70)
    nf.log(f"  NOVEL FACTORY — 03 · Cola de video ({labels} · 10 s · First Frame)")
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
            nf.info(f"[{label}] Filtro --only-missing: {len(rows)} de {total} escenas por generar.")

        if not args.check:
            write_queue_files(paths, master, rows, platform)
            nf.log("")
            nf.ok(f"[{label}] {len(rows)} prompts de video exportados:")
            nf.info(paths[str(spec["csv"])].name + "  (cola principal, campos citados)")
            nf.info(paths[str(spec["json"])].name + " (manifiesto completo)")
            nf.info(paths[str(spec["txt"])].name + "  (legible, bloque por escena)")

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
            f"[Muse AI] {len(batch_files['batches'])} lotes de 1 minuto (6 escenas) exportados:"
        )
        nf.info(batch_files["txt"].name + "  (bloques con adjuntos, cámara, SFX, diálogo y 2 comandos)")
        nf.info(batch_files["json"].name + " (manifiesto de lotes)")
        nf.info("Adjuntos por lote: REF_CAST_MASTER.png + REF_GRID_MIN_XX.png · "
                "comandos 16:9 (YouTube) y 9:16 (Reels).")

    rc = run_check(paths, last_rows, args.allow_missing) if not want or args.check else 0
    if not args.check and not want:
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

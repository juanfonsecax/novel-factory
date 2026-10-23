#!/usr/bin/env python3
"""04 — Episode assembly with ffmpeg: clips -> 16:9 master + 9:16 teasers.

What it does, in order:
  1. Preflight: detects the input mode and verifies clips, frames and music.
     · Mode A: individual 10 s scenes (scene_001.mp4 … scene_NNN.mp4).
     · Mode B: 1-minute Muse AI batches (minute_01.mp4 … minute_NN.mp4 or
       batch_01.mp4 … batch_NN.mp4); assembles the master without per-scene clips.
  2. Normalizes each clip: in mode A it trims dead silence and locks 10.0 s; in mode B
     it locks 60 s per batch without trimming. Standardizes to 1920x1080 / 30 fps / H.264+AAC
     with an audio micro-fade (0.08 s) and caches in output/.work/norm/.
  3. Concatenates the clips without re-encoding (concat demuxer + -c copy).
  4. Mixes looping BGM at low volume, fades and YouTube loudnorm (-14 LUFS).
  5. Writes .srt subtitles synchronized with the project timeline.
  6. Renders an automatic 20 s vertical teaser (9:16) and, in mode A, the 3
     60 s teasers with an optional headline.
  7. Leaves a publish pack (title, description, tags, chapters) and a JSON report.

Usage:
  python post_production/04_assemble_novel_ffmpeg.py my_episode
  python post_production/04_assemble_novel_ffmpeg.py my_episode --check
  python post_production/04_assemble_novel_ffmpeg.py my_episode --limit 4 --skip-teasers --no-music  (tests)
  python post_production/04_assemble_novel_ffmpeg.py my_episode --only-missing-work --force

No network, no APIs: only local ffmpeg/ffprobe.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import zlib
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

NF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(NF_ROOT))
import nf_core as nf  # noqa: E402

AUDIO_EXTS = (".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac")
SCENES_PER_BATCH = 6
BATCH_PATTERNS = ("minute_{n:02d}.mp4", "batch_{n:02d}.mp4", "minute_{n}.mp4", "batch_{n}.mp4")


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------
def _run_ffmpeg(cmd: Sequence[str], cwd: Optional[Path] = None) -> None:
    if cwd is None:
        nf.run_ffmpeg(cmd)
        return
    # nf.run_cmd does not accept cwd: run it with its own cwd here (drawtext filters with relative paths).
    import subprocess

    res = subprocess.run([str(c) for c in cmd], capture_output=True, text=True,
                         encoding="utf-8", errors="replace", cwd=str(cwd))
    if res.returncode != 0:
        tail = (res.stderr or res.stdout or "").strip().splitlines()[-12:]
        raise nf.NFError("ffmpeg failed:\n  " + "\n  ".join(tail))


def batch_for_scene(scene_id: int) -> int:
    return (max(1, int(scene_id)) - 1) // SCENES_PER_BATCH + 1


def find_batch_clip(raw_clips_dir: Path, batch_number: int) -> Optional[Path]:
    """Look for minute_01.mp4 / batch_01.mp4 (and variants without a leading zero)."""
    for pattern in BATCH_PATTERNS:
        candidate = raw_clips_dir / pattern.format(n=batch_number)
        if candidate.exists():
            return candidate
    return None


def detect_clip_mode(raw_clips_dir: Path, scene_ids: Sequence[int]) -> Dict[str, Any]:
    """Detect the input mode: 10 s scenes (A) or 1-minute batches (B).

    Returns a dict with `mode` = "scenes" | "batches" | "missing", the clips
    found and the missing scenes/batches. It does not touch ffmpeg or the master.
    """
    ids = [int(sid) for sid in scene_ids]
    scene_clips: Dict[int, Path] = {}
    missing_scenes: List[int] = []
    for sid in ids:
        clip = nf.find_clip(raw_clips_dir, sid)
        if clip:
            scene_clips[sid] = clip
        else:
            missing_scenes.append(sid)

    if not missing_scenes:
        return {
            "mode": "scenes",
            "scene_clips": scene_clips,
            "batch_clips": {},
            "missing_scenes": [],
            "missing_batches": [],
        }

    batch_numbers = sorted({batch_for_scene(sid) for sid in ids})
    batch_clips: Dict[int, Path] = {}
    missing_batches: List[int] = []
    for number in batch_numbers:
        clip = find_batch_clip(raw_clips_dir, number)
        if clip:
            batch_clips[number] = clip
        else:
            missing_batches.append(number)

    if batch_clips and not missing_batches:
        return {
            "mode": "batches",
            "scene_clips": scene_clips,
            "batch_clips": batch_clips,
            "missing_scenes": [],
            "missing_batches": [],
        }
    return {
        "mode": "missing",
        "scene_clips": scene_clips,
        "batch_clips": batch_clips,
        "missing_scenes": missing_scenes,
        "missing_batches": missing_batches,
    }


def concat_list(paths: List[Path], list_file: Path, cwd: Optional[Path] = None) -> Path:
    lines = ["file '" + p.resolve().as_posix().replace("'", "'\\''") + "'" for p in paths]
    nf.write_text(list_file, "\n".join(lines) + "\n")
    return list_file


def pick_music(master: Dict[str, Any], slug: str, override: str = "") -> Optional[Path]:
    if override:
        path = Path(override)
        if not path.exists():
            raise nf.NFError(f"Music file does not exist: {path}")
        return path
    tracks = sorted(p for p in nf.MUSIC_DIR.iterdir() if p.suffix.lower() in AUDIO_EXTS) \
        if nf.MUSIC_DIR.exists() else []
    if not tracks:
        return None
    hint = str(((master.get("soundtrack") or {}).get("suggested_track")) or "").strip().lower()
    if hint:
        for track in tracks:
            if hint in track.stem.lower() or track.stem.lower() in hint:
                return track
    return tracks[zlib.crc32(slug.encode("utf-8")) % len(tracks)]


# ---------------------------------------------------------------------------
# 1-2. Per-scene normalization
# ---------------------------------------------------------------------------
def analyze_silence(src: Path, probe: Dict[str, Any], pp: Dict[str, Any]) -> Tuple[float, float, str]:
    """Return (usable_start, usable_end, note) after trimming head/tail silence."""
    duration = float(probe.get("duration") or 0.0)
    if not probe.get("has_audio") or duration <= 0:
        return 0.0, duration, "no audio"
    threshold = float(pp.get("silence_threshold_db", -35))
    min_len = float(pp.get("silence_min_sec", 0.35))
    res = nf.run_cmd([
        "ffmpeg", "-hide_banner", "-nostats", "-i", str(src),
        "-af", f"silencedetect=noise={threshold}dB:d={min_len}",
        "-f", "null", "-",
    ])
    log = (res.stderr or "") + (res.stdout or "")
    starts = [float(m) for m in re.findall(r"silence_start:\s*([0-9.]+)", log)]
    ends = [float(m) for m in re.findall(r"silence_end:\s*([0-9.]+)", log)]

    head_max = float(pp.get("head_trim_max_sec", 2.5))
    tail_max = float(pp.get("tail_trim_max_sec", 2.5))
    min_keep = float(pp.get("min_scene_after_trim_sec", 6.0))

    head, tail = 0.0, duration
    if starts and starts[0] <= 0.10 and ends:
        head = max(0.0, min(ends[0] - 0.05, head_max))
    if len(starts) > len(ends):
        tail = max(starts[-1] + 0.05, duration - tail_max)
    elif ends and abs(ends[-1] - duration) < 0.25 and starts:
        tail = max(starts[-1] + 0.05, duration - tail_max)
    tail = min(tail, duration)
    if tail - head < min_keep:
        return 0.0, duration, "trim discarded (clip would be too short)"
    note = ""
    if head > 0.01 or tail < duration - 0.01:
        note = f"trim {head:.2f}s head / {duration - tail:.2f}s tail"
    return head, tail, note


def scene_target_seconds(pp: Dict[str, Any]) -> float:
    return float(pp.get("scene_seconds") or nf.SCENE_SECONDS)


def normalize_scene(
    src: Path,
    dst: Path,
    head: float,
    pp: Dict[str, Any],
    crf: int,
    force: bool,
    target: Optional[float] = None,
) -> None:
    """Normalize a scene (10 s) or a Muse AI batch (60 s) to an exact duration.

    Trims the given head and pads with the last frame / silence if the
    clip is shorter, so every clip has the same exact duration.
    """
    target = float(target) if target is not None else scene_target_seconds(pp)
    if dst.exists() and not force and dst.stat().st_mtime >= src.stat().st_mtime:
        return
    probe = nf.probe_media(src)
    vf = (
        "scale=1920:1080:force_original_aspect_ratio=increase,"
        "crop=1920:1080,setsar=1,fps=30,"
        f"tpad=stop_mode=clone:stop_duration={target:.3f}:start_duration=0,"
        f"trim=0:{target:.3f},format=yuv420p"
    )
    base = [
        "ffmpeg", "-y", "-v", "error", "-hide_banner",
        "-ss", f"{max(0.0, head):.3f}", "-t", f"{target:.3f}", "-i", str(src),
    ]
    if probe.get("has_audio"):
        map_args = ["-map", "0:v:0", "-map", "0:a:0",
                    "-af", (f"aresample=48000,aformat=channel_layouts=stereo,"
                            f"apad=whole_dur={target:.3f},atrim=0:{target:.3f},"
                            f"afade=t=in:st=0:d=0.08")]
    else:
        base += ["-f", "lavfi", "-t", f"{target:.3f}", "-i", "anullsrc=r=48000:cl=stereo"]
        map_args = ["-map", "0:v:0", "-map", "1:a:0"]
    cmd = base + map_args + [
        "-vf", vf,
        "-c:v", "libx264", "-preset", "veryfast", "-crf", str(crf), "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-t", f"{target:.3f}",
        "-movflags", "+faststart", str(dst),
    ]
    dstdir = dst.parent
    dstdir.mkdir(parents=True, exist_ok=True)
    nf.run_ffmpeg(cmd)


def apply_punch_ins(
    src: Path,
    dst: Path,
    cuts: List[Dict[str, Any]],
    crf: int,
    target: Optional[float] = None,
) -> bool:
    """Subtle digital zoom on alternating segments to distinguish internal cuts.

    Operates on the ALREADY normalized and trimmed clip (its t=0 matches the scene
    start), so the master's cut times are used as-is, without adding the head
    offset. The segments add up to exactly `target` seconds.
    """
    dst.parent.mkdir(parents=True, exist_ok=True)
    probe = nf.probe_media(src)
    duration = float(target or probe.get("duration") or 0.0)
    times = sorted({0.0} | {float(c.get("at") or 0.0) for c in cuts if 0 < float(c.get("at") or 0.0) < duration})
    times = [t for t in times if 0 <= t < duration - 0.35]
    if len(times) < 2 or duration <= 0:
        return False
    bounds = times + [duration]
    chains: List[str] = []
    labels: List[str] = []
    for idx in range(len(bounds) - 1):
        start, end = bounds[idx], bounds[idx + 1]
        if end - start < 0.3:
            continue
        label = f"v{idx}"
        scale = 1.06 if idx % 2 == 1 else 1.0
        if scale > 1.0:
            chains.append(
                f"[0:v]trim=start={start:.3f}:end={end:.3f},setpts=PTS-STARTPTS,"
                f"scale=iw*{scale}:ih*{scale},crop=1920:1080,setsar=1[{label}]"
            )
        else:
            chains.append(
                f"[0:v]trim=start={start:.3f}:end={end:.3f},setpts=PTS-STARTPTS,setsar=1[{label}]"
            )
        labels.append(f"[{label}]")
    if len(labels) < 2:
        return False
    graph = ";".join(chains) + ";" + "".join(labels) + f"concat=n={len(labels)}:v=1:a=0[vout]"
    cmd = ["ffmpeg", "-y", "-v", "error", "-hide_banner", "-i", str(src),
           "-filter_complex", graph, "-map", "[vout]"]
    if probe.get("has_audio"):
        cmd += ["-map", "0:a:0", "-c:a", "copy"]
    cmd += ["-c:v", "libx264", "-preset", "veryfast", "-crf", str(crf), "-pix_fmt", "yuv420p",
            "-t", f"{duration:.3f}", "-movflags", "+faststart", str(dst)]
    nf.run_ffmpeg(cmd)
    return True


# ---------------------------------------------------------------------------
# 3-4. Concat + mezcla final
# ---------------------------------------------------------------------------
def mix_master(
    video: Path,
    out: Path,
    music: Optional[Path],
    total: float,
    pp: Dict[str, Any],
    video_fade: bool,
    crf: int,
) -> None:
    vol = float(pp.get("music_volume_db", -22.0))
    fade_in = float(pp.get("music_fade_in_sec", 2.0))
    fade_out = float(pp.get("music_fade_out_sec", 4.0))
    lufs = float(pp.get("loudness_target_lufs", -14.0))
    tp = float(pp.get("true_peak_db", -1.5))
    loudnorm = f"loudnorm=I={lufs}:TP={tp}:LRA=11"
    video_fade_chain = ""
    if video_fade:
        vfo = max(0.0, total - 1.2)
        video_fade_chain = f"fade=t=in:st=0:d=0.6,fade=t=out:st={vfo:.2f}:d=1.2"

    cmd = ["ffmpeg", "-y", "-v", "error", "-hide_banner", "-i", str(video)]
    if music is not None:
        cmd += ["-stream_loop", "-1", "-i", str(music)]
        fade_out_start = max(0.0, total - fade_out)
        duck_threshold = float(pp.get("duck_threshold", 0.03))
        duck_ratio = float(pp.get("duck_ratio", 8.0))
        # Ducked BGM: the music lowers itself when characters speak.
        graph = (
            f"[1:a]volume={vol}dB,afade=t=in:st=0:d={fade_in},"
            f"afade=t=out:st={fade_out_start:.2f}:d={fade_out}[bg];"
            f"[0:a]asplit=2[dial][key];"
            f"[bg][key]sidechaincompress=threshold={duck_threshold}:ratio={duck_ratio}:"
            f"attack=20:release=400:makeup=1[bgduck];"
            f"[dial][bgduck]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[mix];"
            f"[mix]{loudnorm}[aout]"
        )
        if video_fade:
            graph = f"[0:v]{video_fade_chain}[vout];" + graph
            cmd += ["-filter_complex", graph, "-map", "[vout]", "-map", "[aout]",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", str(crf), "-pix_fmt", "yuv420p"]
        else:
            cmd += ["-filter_complex", graph, "-map", "0:v:0", "-map", "[aout]", "-c:v", "copy"]
        cmd += ["-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
                "-shortest", "-movflags", "+faststart", str(out)]
        try:
            nf.run_ffmpeg(cmd)
        except nf.NFError:
            # Retry without normalize=0 (compatibility with older ffmpeg)
            idx = cmd.index("-filter_complex") + 1
            cmd[idx] = cmd[idx].replace(":normalize=0", "")
            nf.run_ffmpeg(cmd)
        return

    cmd += ["-map", "0:v:0", "-map", "0:a:0", "-af", loudnorm]
    if video_fade:
        cmd += ["-vf", video_fade_chain, "-c:v", "libx264", "-preset", "veryfast",
                "-crf", str(crf), "-pix_fmt", "yuv420p"]
    else:
        cmd += ["-c:v", "copy"]
    cmd += ["-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
            "-shortest", "-movflags", "+faststart", str(out)]
    nf.run_ffmpeg(cmd)


# ---------------------------------------------------------------------------
# 5. Subtitles
# ---------------------------------------------------------------------------
def build_cues(timeline: List[Dict[str, Any]]) -> List[Tuple[float, float, str]]:
    """Cues (start, end, text) proportional to the words in each line."""
    cues: List[Tuple[float, float, str]] = []
    for item in timeline:
        scene = item["scene"]
        start = float(item["start"])
        dur = float(item["dur"])
        lines = nf.scene_dialogue_lines(scene)
        if not lines:
            continue
        words = [max(1, len(re.findall(r"\b[\w'-]+\b", d["line"]))) for d in lines]
        total_words = sum(words)
        window_start = start + 0.25
        window = max(0.8, dur - 0.45)
        cursor = window_start
        for entry, count in zip(lines, words):
            share = window * (count / total_words) if total_words else window / len(lines)
            text = entry["line"]
            if entry["speaker"]:
                text = f"{entry['speaker'].upper()}: {text}"
            cues.append((cursor, min(cursor + share - 0.05, start + dur - 0.15), text))
            cursor += share
    return cues


def write_cues_file(cues: List[Tuple[float, float, str]], out: Path) -> None:
    blocks = []
    for idx, (start, end, text) in enumerate(cues, start=1):
        blocks.append(f"{idx}\n{nf.fmt_srt(start)} --> {nf.fmt_srt(max(start + 0.4, end))}\n{text}\n")
    nf.write_text(out, "\n".join(blocks))


def write_srt(timeline: List[Dict[str, Any]], out: Path) -> int:
    cues = build_cues(timeline)
    if not cues:
        nf.warn("No dialogue: no .srt was written.")
        return 0
    write_cues_file(cues, out)
    return len(cues)


# ---------------------------------------------------------------------------
# 6. 9:16 teasers
# ---------------------------------------------------------------------------
def render_auto_teaser(
    src: Path,
    out: Path,
    pp: Dict[str, Any],
    crf: int,
    seconds: float = 20.0,
) -> float:
    """Extract the first 15–20 s of the master and convert them to 9:16 (Reels/Shorts)."""
    target = float(seconds or pp.get("auto_teaser_seconds", 20.0))
    vf = "crop=ih*9/16:ih,scale=1080:1920,setsar=1"
    af = "afade=t=in:st=0:d=0.08"
    cmd = [
        "ffmpeg", "-y", "-v", "error", "-hide_banner", "-i", str(src),
        "-t", f"{target:.3f}", "-vf", vf, "-af", af,
        "-c:v", "libx264", "-preset", "veryfast", "-crf", str(crf), "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-shortest", "-movflags", "+faststart", str(out),
    ]
    try:
        nf.run_ffmpeg(cmd)
    except nf.NFError:
        fallback = "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1"
        idx = cmd.index("-vf") + 1
        cmd[idx] = fallback
        nf.run_ffmpeg(cmd)
    return float(nf.probe_media(out).get("duration") or target)


def render_teaser(
    segments: List[Path],
    out: Path,
    hook_text: str,
    pp: Dict[str, Any],
    font: Optional[Path],
    music: Optional[Path],
    crf: int,
    work: Path,
    teaser_timeline: Optional[List[Dict[str, Any]]] = None,
) -> float:
    """9:16 teaser with hybrid fit (blurred background + centered foreground).

    If there is a timeline for the teaser scenes, burns in the dialogue subtitles.
    """
    list_file = concat_list(segments, work / f"{out.stem}_list.txt")
    fg_ratio = float(pp.get("teaser_foreground_width_ratio", 0.8))
    fw = int(round(1080 * fg_ratio / 2) * 2)
    base_chain = (
        "[0:v]split=2[bgsrc][fgsrc];"
        "[bgsrc]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
        "gblur=sigma=32,setsar=1[bg];"
        f"[fgsrc]scale={fw}:-2,setsar=1[fg];"
        "[bg][fg]overlay=(W-w)/2:(H-h)/2,fps=30,format=yuv420p[base]"
    )

    cues = build_cues(teaser_timeline or [])
    caption_style = (
        f"Fontsize={int(pp.get('teaser_caption_font_size', 44))},"
        "PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
        f"BorderStyle=1,Outline=3,Shadow=0,Alignment=2,"
        f"MarginV={int(pp.get('teaser_caption_margin_v', 260))}"
    )
    srt_name = ""
    if cues:
        srt_path = work / f"{out.stem}_captions.srt"
        write_cues_file(cues, srt_path)
        srt_name = srt_path.name

    headline_ready = bool(hook_text) and font is not None
    if hook_text and font is None:
        nf.warn("No TTF font available: the teaser will have no burned-in headline.")
    if headline_ready:
        local_font = work / "nf_overlay_font.ttf"
        if not local_font.exists():
            shutil.copyfile(font, local_font)
    text_file = work / f"{out.stem}_hook.txt"
    if headline_ready:
        nf.write_text(text_file, hook_text.strip() + "\n")

    def video_chain(with_captions: bool) -> str:
        chain = base_chain
        label = "[base]"
        if with_captions and srt_name:
            chain += f";{label}subtitles={srt_name}:force_style='{caption_style}'[cap]"
            label = "[cap]"
        if headline_ready:
            seconds = float(pp.get("teaser_hook_seconds", 6.0))
            size = int(pp.get("teaser_font_size", 64))
            y = int(pp.get("teaser_text_y", 150))
            alpha = float(pp.get("teaser_text_box_alpha", 0.55))
            chain += (
                f";{label}drawtext=fontfile=nf_overlay_font.ttf:textfile={text_file.name}:expansion=none:"
                f"fontcolor=white:fontsize={size}:line_spacing=12:"
                f"box=1:boxcolor=black@{alpha}:boxborderw=26:"
                f"x=(w-text_w)/2:y={y}:enable='between(t,0,{seconds})'[v]"
            )
        else:
            chain += f";{label}null[v]"
        return chain

    total = sum((nf.probe_media(p).get("duration") or 0.0) for p in segments)
    vol = float(pp.get("music_volume_db", -22.0)) - 2.0
    lufs = float(pp.get("loudness_target_lufs", -14.0))
    tp = float(pp.get("true_peak_db", -1.5))
    loudnorm = f"loudnorm=I={lufs}:TP={tp}:LRA=11"
    duck_threshold = float(pp.get("duck_threshold", 0.03))
    duck_ratio = float(pp.get("duck_ratio", 8.0))

    def build_graph(with_captions: bool) -> str:
        graph = video_chain(with_captions)
        if music is not None:
            fade_out = min(3.0, max(1.0, total * 0.1))
            graph += (
                f";[1:a]volume={vol}dB,afade=t=in:st=0:d=1,"
                f"afade=t=out:st={max(0.0, total - fade_out):.2f}:d={fade_out}[bg];"
                f"[0:a]asplit=2[dial][key];"
                f"[bg][key]sidechaincompress=threshold={duck_threshold}:ratio={duck_ratio}:"
                f"attack=20:release=400[bgd];"
                f"[dial][bgd]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[mix];"
                f"[mix]{loudnorm}[a]"
            )
        else:
            graph += f";[0:a]{loudnorm}[a]"
        return graph

    def build_cmd(with_captions: bool) -> List[str]:
        cmd = ["ffmpeg", "-y", "-v", "error", "-hide_banner", "-f", "concat", "-safe", "0",
               "-i", list_file.name]
        if music is not None:
            cmd += ["-stream_loop", "-1", "-i", str(music.resolve())]
        cmd += ["-filter_complex", build_graph(with_captions), "-map", "[v]", "-map", "[a]"]
        cmd += ["-c:v", "libx264", "-preset", "veryfast", "-crf", str(crf), "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
                "-movflags", "+faststart", str(out.resolve())]
        return cmd

    try:
        _run_ffmpeg(build_cmd(bool(srt_name)), cwd=work)
    except nf.NFError:
        if not srt_name:
            raise
        nf.warn("Could not burn in the teaser subtitles (libass?); retrying without captions.")
        _run_ffmpeg(build_cmd(False), cwd=work)
    return total


# ---------------------------------------------------------------------------
# 7. Publish pack
# ---------------------------------------------------------------------------
def build_publish_pack(
    paths: Dict[str, Path],
    master: Dict[str, Any],
    timeline: List[Dict[str, Any]],
    teaser_files: List[Tuple[Dict[str, Any], Path, float]],
    master_file: Optional[Path],
    master_dur: float,
) -> Dict[str, Any]:
    ep = nf.episode_meta(master)
    pub = master.get("publisher") or {}
    pack_dir = paths["output"] / "publish_pack"
    pack_dir.mkdir(parents=True, exist_ok=True)

    chapters: List[Tuple[float, str]] = []
    for act in master.get("acts") or []:
        if not isinstance(act, dict):
            continue
        scene_ids = [int(i) for i in (act.get("scenes") or []) if str(i).isdigit()] or []
        first = scene_ids[0] if scene_ids else None
        if first is None:
            act_no = int(act.get("act") or 0)
            first = (act_no - 1) * 10 + 1 if act_no else None
        item = next((t for t in timeline if int(t["scene"].get("scene_id") or 0) == first), None)
        if item:
            chapters.append((float(item["start"]), f"Act {act.get('act')} — {act.get('title')}"))

    tags = [h.lstrip("#") for h in (pub.get("hashtags") or [])]
    hashtags = " ".join(pub.get("hashtags") or [])
    description_lines = [
        str(ep.get("logline") or ""),
        "",
        f"A {nf.human_duration(master_dur)} cinematic short-drama episode in native English audio.",
        "",
        "Chapters:",
    ]
    for stamp, name in chapters:
        description_lines.append(f"{nf.fmt_srt(stamp)[:8]} {name}")
    description_lines += ["", str(pub.get("cta") or ""), "", hashtags]
    if pub.get("ai_disclosure", True):
        description_lines += ["", "Voices and visuals are AI-generated. Story and edit by the creator."]
    description = "\n".join(line for line in description_lines if line is not None)

    metadata: Dict[str, Any] = {
        "episode": ep,
        "master": {
            "file": master_file.name if master_file else None,
            "duration_seconds": round(master_dur, 2),
            "aspect": "16:9",
            "title": ep.get("title"),
            "description": description,
            "tags": tags,
            "chapters": [{"start": round(s, 2), "title": t} for s, t in chapters],
        },
        "teasers": [],
    }

    if master_file:
        nf.write_text(pack_dir / "youtube_master.md", "\n".join([
            f"# {ep.get('title')} — YouTube pack",
            "",
            f"- File: `{master_file.name}`",
            f"- Runtime: {nf.human_duration(master_dur)}",
            f"- Format: 1920x1080, 30 fps, H.264 + AAC",
            "",
            "## Title",
            "",
            str(ep.get("title") or ""),
            "",
            "## Description",
            "",
            "```text",
            description,
            "```",
            "",
            "## Tags",
            "",
            ", ".join(tags),
            "",
        ]))

    for teaser, path, dur in teaser_files:
        caption = str(teaser.get("caption") or teaser.get("hook_text") or "").strip()
        full_caption = f"{caption}\n\n{hashtags}" if hashtags else caption
        metadata["teasers"].append({
            "id": teaser.get("id"),
            "file": path.name,
            "duration_seconds": round(dur, 2),
            "hook_text": teaser.get("hook_text"),
            "caption": full_caption,
            "scenes": teaser.get("scenes"),
        })
        nf.write_text(pack_dir / f"teaser_{int(teaser.get('id') or 0):02d}.md", "\n".join([
            f"# Teaser {teaser.get('id')} — publish pack (9:16)",
            "",
            f"- File: `{path.name}`",
            f"- Runtime: {dur:.1f} s",
            f"- Headline: {teaser.get('hook_text')}",
            f"- Scenes: {teaser.get('scenes')}",
            "",
            "## Caption",
            "",
            "```text",
            full_caption,
            "```",
            "",
        ]))

    nf.write_json(pack_dir / "metadata.json", metadata)
    return metadata


# ---------------------------------------------------------------------------
# CLI / orchestration
# ---------------------------------------------------------------------------
def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="04 — Final assembly (16:9 master + 3 9:16 teasers).")
    parser.add_argument("project", help="Episode slug.")
    parser.add_argument("--check", action="store_true", help="Preflight only; renders nothing.")
    parser.add_argument("--limit", type=int, default=0, help="Use only the first N scenes (tests).")
    parser.add_argument("--skip-teasers", action="store_true", help="Do not render teasers.")
    parser.add_argument("--no-music", action="store_true", help="No BGM.")
    parser.add_argument("--music", type=str, default="", help="Path to a specific MP3.")
    parser.add_argument("--punch-ins", action="store_true", help="Subtle digital zoom on internal cuts.")
    parser.add_argument("--no-trim", action="store_true", help="Do not trim head/tail silence.")
    parser.add_argument("--video-fade", action="store_true", help="Fade to black at the start/end of the master.")
    parser.add_argument("--no-srt", action="store_true", help="Do not write subtitles.")
    parser.add_argument("--force", action="store_true", help="Recompute cached normalization.")
    parser.add_argument("--allow-gaps", action="store_true", help="Continue even if clips are missing.")
    parser.add_argument("--font", type=str, default="", help="TTF for the teaser headline.")
    args = parser.parse_args(argv)

    nf.log("")
    nf.log("=" * 70)
    nf.log("  NOVEL FACTORY — 04 · ffmpeg assembly (16:9 master + 9:16 teasers)")
    nf.log("=" * 70)
    nf.require_ffmpeg()

    paths = nf.resolve_project(args.project)
    master = nf.load_master(paths["root"])
    style = nf.load_style_locks()
    pp = style.get("post_production") or {}
    ep = nf.episode_meta(master)
    slug = str(ep.get("slug") or args.project)

    scenes = nf.ordered_scenes(master)
    if args.limit:
        scenes = scenes[: max(1, args.limit)]

    # --- Preflight: mode A (10 s scenes) or mode B (1-min Muse AI batches) ---
    scene_ids = [int(scene.get("scene_id") or 0) for scene in scenes]
    detected = detect_clip_mode(paths["raw_clips"], scene_ids)
    clip_mode = str(detected["mode"])
    batch_clips: Dict[int, Path] = detected["batch_clips"] if clip_mode == "batches" else {}
    missing: List[int] = detected["missing_scenes"] if clip_mode != "batches" else []
    music = None if args.no_music else pick_music(master, slug, args.music)

    nf.info(f"Episode: {ep.get('title')}  ({len(scenes)} scenes · {nf.human_duration(sum(10 for _ in scenes))})")
    if clip_mode == "batches":
        nf.info(f"Clip mode: B — {len(batch_clips)} 1-minute Muse AI batch(es)")
    else:
        nf.info(f"Clip mode: A — individual 10 s scenes "
                f"({len(detected['scene_clips'])}/{len(scenes)} present)")
    nf.info(f"BGM: {music.name if music else '(no music)'}")
    font = Path(args.font) if args.font else nf.detect_font()
    if not args.skip_teasers:
        nf.info(f"Overlay font: {font.name if font else '(none: teaser without headline)'}")

    if detected.get("missing_batches") and detected.get("batch_clips"):
        nf.warn("Incomplete Muse AI batches; missing: " +
                ", ".join(f"minute_{n:02d}.mp4/batch_{n:02d}.mp4"
                          for n in detected["missing_batches"][:20]))
    if missing:
        nf.warn(f"Missing {len(missing)} clips: {', '.join(map(str, missing[:20]))}" +
                (" …" if len(missing) > 20 else ""))
        if not args.allow_gaps:
            nf.err("Generate the clips with the Omni queue (03), the project's Muse AI "
                   "batches, or use --allow-gaps / --limit for tests.")
            return 1
    if args.check:
        nf.log("")
        nf.ok("Preflight complete (--check: nothing was rendered).")
        return 0 if not missing else 1

    # --- Normalization ---
    work = paths["work"]
    norm_dir = work / "norm"
    norm_dir.mkdir(parents=True, exist_ok=True)
    crf_scene = int(pp.get("scene_crf", 20))
    scene_seconds = scene_target_seconds(pp)
    timeline: List[Dict[str, Any]] = []
    concat_clips: List[Path] = []
    cursor = 0.0
    nf.log("")
    nf.info("Normalizing clips (1920x1080 · 30 fps · AAC 48 kHz · 0.08 s micro-fade)…")

    if clip_mode == "batches":
        if args.punch_ins:
            nf.warn("--punch-ins is skipped in Muse AI batch mode (cuts are already in the video).")
        for number in sorted(batch_clips):
            group = [scene for scene in scenes if batch_for_scene(int(scene.get("scene_id") or 0)) == number]
            if not group:
                continue
            src = batch_clips[number]
            target = len(group) * scene_seconds
            dst = norm_dir / f"minute_{number:02d}.mp4"
            normalize_scene(src, dst, 0.0, pp, crf_scene, args.force, target=target)
            dur = float(nf.probe_media(dst).get("duration") or target)
            if abs(dur - target) > nf.DURATION_TOLERANCE_SEC:
                nf.warn(f"Batch {number:02d}: {dur:.3f}s (expected {target:.3f}s).")
            for offset, scene in enumerate(group):
                timeline.append({
                    "scene": scene,
                    "clip": dst,
                    "start": cursor + offset * scene_seconds,
                    "dur": scene_seconds,
                    "trim": "Muse AI batch (no trim)",
                })
            concat_clips.append(dst)
            cursor += dur
            nf.info(f"  … batch {number:02d} normalized ({nf.human_duration(cursor)})")
    else:
        for idx, scene in enumerate(scenes, start=1):
            sid = int(scene.get("scene_id") or 0)
            if sid not in detected["scene_clips"]:
                continue
            src = detected["scene_clips"][sid]
            probe = nf.probe_media(src)
            if args.no_trim:
                head, tail, note = 0.0, min(float(probe.get("duration") or 0.0), nf.SCENE_SECONDS), "no trim"
            else:
                head, tail, note = analyze_silence(src, probe, pp)
            dst = norm_dir / f"{nf.scene_stem(sid)}.mp4"
            normalize_scene(src, dst, head, pp, crf_scene, args.force, target=scene_seconds)
            if args.punch_ins:
                punch_dst = work / "norm_punch" / f"{nf.scene_stem(sid)}.mp4"
                if apply_punch_ins(dst, punch_dst, scene.get("internal_cuts") or [], crf_scene, scene_seconds):
                    dst = punch_dst
            dur = float(nf.probe_media(dst).get("duration") or scene_seconds)
            if abs(dur - scene_seconds) > nf.DURATION_TOLERANCE_SEC:
                nf.warn(f"Scene {sid}: {dur:.3f}s (expected {scene_seconds:.3f}s).")
            timeline.append({"scene": scene, "clip": dst, "start": cursor, "dur": dur, "trim": note})
            concat_clips.append(dst)
            cursor += dur
            if idx % 10 == 0 or idx == len(scenes):
                nf.info(f"  … {idx}/{len(scenes)} normalized ({nf.human_duration(cursor)})")

    if not timeline:
        nf.err("Nothing to assemble.")
        return 1

    # --- Concat ---
    nf.log("")
    nf.info("Joining clips (concat demuxer, no re-encoding)…")
    list_file = concat_list(concat_clips, work / "master_concat.txt")
    master_video = work / "master_video.mp4"
    nf.run_ffmpeg(["ffmpeg", "-y", "-v", "error", "-hide_banner", "-f", "concat", "-safe", "0",
                   "-i", str(list_file), "-c", "copy", "-movflags", "+faststart", str(master_video)])

    # --- Final mix ---
    total = sum(float(t["dur"]) for t in timeline)
    master_out = paths["output"] / f"{slug}_master_16x9_1080p.mp4"
    nf.log("")
    nf.info(f"Mixing audio and finalizing the master ({nf.human_duration(total)})…")
    mix_master(master_video, master_out, music, total, pp, args.video_fade, int(pp.get("master_crf", 20)))
    master_dur = float(nf.probe_media(master_out).get("duration") or total)
    nf.ok(f"Master: {master_out.name} ({nf.human_duration(master_dur)})")

    # --- Automatic vertical teaser (20 s hook for Reels/Shorts) ---
    auto_teaser: Optional[Path] = None
    auto_teaser_dur = 0.0
    if not args.skip_teasers:
        nf.log("")
        nf.info("Rendering automatic vertical teaser (first 20 s → 9:16)…")
        auto_teaser = paths["output"] / f"{slug}_teaser_9x16.mp4"
        auto_teaser_dur = render_auto_teaser(
            master_out, auto_teaser, pp, int(pp.get("teaser_crf", 20))
        )
        nf.ok(f"Vertical teaser: {auto_teaser.name} ({auto_teaser_dur:.1f} s)")

    # --- Subtitles ---
    if not args.no_srt:
        srt_path = paths["output"] / f"{slug}_master.srt"
        n = write_srt(timeline, srt_path)
        if n:
            nf.ok(f"Subtitles: {srt_path.name} ({n} cues, {len(timeline)} scenes)")

    # --- Teasers ---
    teaser_files: List[Tuple[Dict[str, Any], Path, float]] = []
    if not args.skip_teasers and clip_mode == "batches":
        nf.warn("Muse AI batch mode: skipping the 3 per-scene teasers; "
                "use the automatic 20 s vertical teaser.")
    elif not args.skip_teasers:
        nf.log("")
        nf.info("Rendering 9:16 teasers…")
        crf_teaser = int(pp.get("teaser_crf", 20))
        for teaser in master.get("teasers") or []:
            if not isinstance(teaser, dict):
                continue
            ids = [int(i) for i in (teaser.get("scenes") or []) if str(i).isdigit()]
            segments = [t["clip"] for t in timeline if int(t["scene"].get("scene_id") or 0) in ids]
            if len(segments) < len(ids):
                nf.warn(f"Teaser {teaser.get('id')}: missing scenes ({len(segments)}/{len(ids)}); skipped.")
                continue
            t_timeline = [t for t in timeline if int(t["scene"].get("scene_id") or 0) in ids]
            if t_timeline:
                base_start = float(t_timeline[0]["start"])
                t_timeline = [{"scene": t["scene"], "start": float(t["start"]) - base_start,
                               "dur": float(t["dur"])} for t in t_timeline]
            out = paths["output"] / f"teaser_{int(teaser.get('id') or 0):02d}_9x16.mp4"
            dur = render_teaser(segments, out, str(teaser.get("hook_text") or ""), pp, font,
                                music, crf_teaser, work, t_timeline)
            teaser_files.append((teaser, out, dur))
            nf.ok(f"Teaser {teaser.get('id')}: {out.name} ({dur:.1f} s)")

    # --- Pack + report ---
    metadata = build_publish_pack(paths, master, timeline, teaser_files,
                                 master_out if master_out.exists() else None, master_dur)
    report = {
        "episode": ep.get("slug"),
        "generated_at": nf.now_iso(),
        "scene_count": len(timeline),
        "total_seconds": round(total, 2),
        "master": {"file": master_out.name, "duration_seconds": round(master_dur, 2)},
        "clip_mode": clip_mode,
        "auto_teaser": (
            {"file": auto_teaser.name, "duration_seconds": round(auto_teaser_dur, 2)}
            if auto_teaser else None
        ),
        "teasers": [{"id": t.get("id"), "file": p.name, "duration_seconds": round(d, 2)}
                    for t, p, d in teaser_files],
        "music": music.name if music else None,
        "scenes": [{"scene_id": t["scene"].get("scene_id"), "start": round(t["start"], 3),
                    "duration": round(t["dur"], 3), "trim": t["trim"],
                    "source": Path(t["clip"]).name} for t in timeline],
        "missing_clips": missing,
    }
    nf.write_json(paths["output"] / "report.json", report)

    nf.log("")
    nf.log("-" * 70)
    nf.ok("Assembly complete.")
    nf.info(f"Master 16:9 : {master_out}  ({nf.human_duration(master_dur)})")
    if auto_teaser:
        nf.info(f"Teaser 9:16 : {auto_teaser}  ({auto_teaser_dur:.1f} s, first 20 s)")
    for teaser, path, dur in teaser_files:
        nf.info(f"Teaser 9:16 : {path}  ({dur:.1f} s)")
    nf.info(f"Pack         : {paths['output'] / 'publish_pack'}")
    nf.info(f"Report       : {paths['output'] / 'report.json'}")
    nf.log("")
    nf.log(f"  Publishing: python post_production/05_export_to_publisher.py {args.project} --personaje "
           f"{master.get('publisher', {}).get('personaje_id', 'emma_hayes')}")
    nf.log("")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except nf.NFError as exc:
        nf.err(str(exc))
        sys.exit(1)

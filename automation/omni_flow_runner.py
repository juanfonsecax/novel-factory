#!/usr/bin/env python3
"""Runner local de la cola de Omni — sin APIs, sin red, sin dependencias externas.

Modos:
  status    Tabla de progreso: qué frames y qué clips existen, duración y siguiente paso.
  queue     Imprime el prompt de la siguiente escena pendiente (para scripting/automatización propia).
  assisted  Asistente de portapapeles: copia el prompt, tú lo pegas en Omni, pulsas Enter
            y el runner recoge el clip descargado y lo archiva como raw_clips/scene_XXX.mp4.
  watch     Vigila una carpeta de descargas y archiva automáticamente los clips nuevos
            en el orden de las escenas (los descargas y el runner los renombra/coloca).

Playwright es OPCIONAL y está DESACTIVADO por defecto. No se incluye automatización de
sitios web (los selectores cambian y el uso automatizado puede violar sus términos).
Si tienes tu propio script local de Playwright, pásalo con --playwright-script: el runner
lo ejecutará antes de cada espera manual y le pasará NF_SCENE, NF_FRAME y NF_PROMPT por
variables de entorno.

Uso:
  python automation/omni_flow_runner.py mi_episodio status
  python automation/omni_flow_runner.py mi_episodio queue
  python automation/omni_flow_runner.py mi_episodio assisted --count 5
  python automation/omni_flow_runner.py mi_episodio watch --once
  python automation/omni_flow_runner.py mi_episodio watch --interval 3
  python automation/omni_flow_runner.py mi_episodio assisted --playwright-script "C:\\mi\\omni_local.py"
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

NF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(NF_ROOT))
import nf_core as nf  # noqa: E402

MEDIA_EXTS = (".mp4", ".mov", ".m4v", ".webm")
DEFAULT_DOWNLOADS = Path.home() / "Downloads"


# ---------------------------------------------------------------------------
# Estado del proyecto
# ---------------------------------------------------------------------------
def load_queue(paths: Dict[str, Path]) -> Dict[int, Dict[str, Any]]:
    data = nf.read_json(paths["omni_json"], default=None)
    items = data.get("items") if isinstance(data, dict) else data
    out: Dict[int, Dict[str, Any]] = {}
    for item in items or []:
        if not isinstance(item, dict):
            continue
        try:
            sid = int(item.get("scene_id") or 0)
        except (TypeError, ValueError):
            continue
        if 1 <= sid <= nf.SCENE_COUNT:
            out[sid] = item
    return out


def build_status(paths: Dict[str, Path], master: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for scene in nf.ordered_scenes(master):
        sid = int(scene.get("scene_id") or 0)
        frame = nf.find_frame(paths["frames"], sid)
        clip = nf.find_clip(paths["raw_clips"], sid)
        dur = 0.0
        if clip:
            try:
                dur = float(nf.probe_media(clip).get("duration") or 0.0)
            except nf.NFError:
                dur = 0.0
        rows.append({"scene_id": sid, "frame": frame, "clip": clip, "duration": dur})
    return rows


def save_state(paths: Dict[str, Path], rows: List[Dict[str, Any]]) -> None:
    payload = {
        "updated_at": nf.now_iso(),
        "scenes_total": len(rows),
        "frames_present": sum(1 for r in rows if r["frame"]),
        "clips_present": sum(1 for r in rows if r["clip"]),
        "missing_frames": [r["scene_id"] for r in rows if not r["frame"]],
        "missing_clips": [r["scene_id"] for r in rows if not r["clip"]],
        "clips": {
            str(r["scene_id"]): {
                "file": Path(r["clip"]).name,
                "duration": round(float(r["duration"]), 2),
            }
            for r in rows if r["clip"]
        },
    }
    nf.write_json(paths["state"], payload)


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def copy_to_clipboard(text: str) -> bool:
    """Copia al portapapeles con tkinter (stdlib). Devuelve False si no hay entorno gráfico."""
    try:
        import tkinter as tk

        root = tk.Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        root.destroy()
        return True
    except Exception:
        return False


def stash_prompt(paths: Dict[str, Path], scene_id: int, prompt: str) -> Path:
    target = paths["work"] / f"next_prompt_scene_{scene_id:03d}.txt"
    nf.write_text(target, prompt.strip() + "\n")
    return target


def find_newest_media(folder: Path, since_ts: float) -> Optional[Path]:
    if not folder.exists():
        return None
    hits = [
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in MEDIA_EXTS and p.stat().st_mtime >= since_ts
    ]
    return max(hits, key=lambda p: p.stat().st_mtime) if hits else None


def assign_clip(
    src: Path,
    paths: Dict[str, Path],
    scene_id: int,
    overwrite: bool = False,
    force_duration: bool = False,
) -> Tuple[bool, str]:
    """Valida y archiva un clip como raw_clips/scene_XXX.mp4."""
    target = paths["raw_clips"] / f"{nf.scene_stem(scene_id)}.mp4"
    if target.exists() and not overwrite:
        return False, f"{target.name} ya existe (usa --overwrite para reemplazarlo)"
    try:
        probe = nf.probe_media(src)
    except nf.NFError as exc:
        return False, f"archivo inválido: {exc}"
    if not probe.get("has_video"):
        return False, "el archivo no tiene pista de vídeo"
    dur = float(probe.get("duration") or 0.0)
    if not (5.0 <= dur <= 15.0) and not force_duration:
        return False, (f"duración {dur:.1f}s fuera de 5-15 s (Omni debe dar ~10 s). "
                       "Usa --force-duration si es correcto.")
    src = src.resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    if src != target.resolve():
        shutil.move(str(src), str(target))
    note = f"{target.name} ({dur:.1f}s)"
    if abs(dur - nf.SCENE_SECONDS) > 0.8:
        note += "  [!] no dura 10 s exactos"
    return True, note


def run_playwright_script(script: Path, scene_id: int, frame: Optional[Path], prompt: str) -> None:
    if not script.exists():
        raise nf.NFError(f"No existe el script de Playwright: {script}")
    env = {
        **__import__("os").environ,
        "NF_SCENE": str(scene_id),
        "NF_FRAME": str(frame or ""),
        "NF_PROMPT": prompt,
    }
    nf.info(f"Ejecutando script local: {script.name}")
    res = subprocess.run([sys.executable, str(script)], env=env)
    if res.returncode != 0:
        nf.warn(f"El script {script.name} terminó con código {res.returncode}; sigo en modo manual.")


# ---------------------------------------------------------------------------
# Comandos
# ---------------------------------------------------------------------------
def cmd_status(args: argparse.Namespace) -> int:
    paths, master = _prepare(args)
    rows = build_status(paths, master)
    save_state(paths, rows)
    nf.log("")
    nf.log(f"  {'Escena':>7}  {'Frame':<14}  {'Clip':<22}  {'Duración':>8}")
    nf.log("  " + "-" * 58)
    for r in rows:
        frame = Path(r["frame"]).name if r["frame"] else "—"
        clip = Path(r["clip"]).name if r["clip"] else "—"
        dur = f"{r['duration']:.1f}s" if r["clip"] else ""
        nf.log(f"  {r['scene_id']:>7}  {frame:<14}  {clip:<22}  {dur:>8}")
    frames = sum(1 for r in rows if r["frame"])
    clips = sum(1 for r in rows if r["clip"])
    nf.log("  " + "-" * 58)
    nf.info(f"Frames: {frames}/{len(rows)}   Clips: {clips}/{len(rows)}")
    if clips < len(rows):
        nf.info("Siguiente paso: python automation/omni_flow_runner.py <proyecto> assisted")
    elif frames < len(rows):
        nf.info("Faltan frames: exporta la cola de ChatGPT (02) y genera las imágenes.")
    else:
        nf.ok("Todo listo: ejecuta post_production/04_assemble_novel_ffmpeg.py")
    nf.info(f"Estado guardado en: {paths['state']}")
    return 0


def cmd_queue(args: argparse.Namespace) -> int:
    paths, master = _prepare(args)
    queue = load_queue(paths)
    rows = build_status(paths, master)
    for r in rows:
        if r["clip"]:
            continue
        sid = r["scene_id"]
        item = queue.get(sid)
        if not item:
            nf.warn(f"Escena {sid}: no está en la cola de Omni; regenera la cola con 03.")
            return 1
        nf.log("")
        nf.log(f"=== Escena {sid} ===")
        expected_frame = paths["frames"] / f"{nf.frame_stem(sid)}.png"
        nf.log(f"Frame : {r['frame'] or 'FALTA -> ' + str(expected_frame)}")
        nf.log(f"Salida: {paths['raw_clips'] / nf.scene_stem(sid)}.mp4")
        nf.log("")
        nf.log(str(item.get("prompt") or "").strip())
        return 0
    nf.ok("No hay clips pendientes.")
    return 0


def _prepare(args: argparse.Namespace) -> Tuple[Dict[str, Path], Dict[str, Any]]:
    paths = nf.resolve_project(args.project)
    master = nf.load_master(paths["root"])
    return paths, master


def _missing_rows(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [r for r in rows if not r["clip"]]


def cmd_assisted(args: argparse.Namespace) -> int:
    nf.require_ffmpeg()
    paths, master = _prepare(args)
    queue = load_queue(paths)
    if not queue:
        nf.warn("No hay cola de Omni. Ejecuta generators/03_export_omni_queue.py primero.")
        return 1
    done = 0
    skipped: set = set()
    while True:
        rows = build_status(paths, master)
        pending = [r for r in _missing_rows(rows) if r["scene_id"] not in skipped]
        if not pending:
            save_state(paths, rows)
            if skipped:
                nf.warn(f"Omitidas en esta sesión: {', '.join(map(str, sorted(skipped)))}")
            nf.ok("Todas las escenas (no omitidas) tienen clip.")
            return 0
        row = pending[0]
        sid = row["scene_id"]
        item = queue.get(sid)
        if not item:
            nf.warn(f"Escena {sid} sin prompt en la cola; saltando.")
            item = {"prompt": ""}
        prompt = str(item.get("prompt") or "").strip()
        frame = row["frame"]
        nf.log("")
        nf.log("=" * 70)
        nf.log(f"  ESCENA {sid} de {len(rows)}   |   quedan {len(pending)}")
        nf.log("=" * 70)
        nf.log(f"  Frame : {frame or '(falta el frame)'}")
        nf.log(f"  Salida: {paths['raw_clips'] / nf.scene_stem(sid)}.mp4")
        nf.log("")
        nf.log(prompt or "(sin prompt: usa el CSV de la cola)")
        nf.log("")
        if args.no_clipboard:
            copied = False
        else:
            copied = copy_to_clipboard(prompt) if prompt else False
        if copied:
            nf.ok("Prompt copiado al portapapeles.")
        elif prompt:
            saved = stash_prompt(paths, sid, prompt)
            nf.info(f"Portapapeles no disponible: prompt guardado en {saved}")

        if args.playwright_script:
            try:
                run_playwright_script(Path(args.playwright_script), sid, frame, prompt)
            except nf.NFError as exc:
                nf.warn(str(exc))

        started = time.time() - 2
        try:
            answer = input("  Enter cuando el clip esté descargado (s=omitir, q=salir): ").strip().lower()
        except EOFError:
            nf.info("Sin entrada interactiva; salgo.")
            return 0
        if answer in ("q", "quit", "exit"):
            nf.info("Saliendo.")
            return 0
        if answer in ("s", "skip"):
            nf.warn(f"Escena {sid} omitida por el usuario (no se volverá a preguntar hoy).")
            skipped.add(sid)
            continue

        override = answer.strip('"').strip("'")
        src: Optional[Path] = Path(override) if override else None
        if src and not src.exists():
            nf.warn(f"No existe: {src}")
            continue
        if src is None:
            src = find_newest_media(Path(args.downloads), started)
            if src is None:
                nf.warn(f"No veo un vídeo nuevo en {args.downloads}. Pega la ruta del clip o vuelve a intentarlo.")
                continue
        ok, note = assign_clip(src, paths, sid, overwrite=args.overwrite,
                               force_duration=args.force_duration)
        if ok:
            nf.ok(f"Escena {sid}: {note}")
            done += 1
        else:
            nf.warn(f"Escena {sid}: {note}")
        if args.count and done >= args.count:
            nf.ok(f"Procesados {done} clips en esta sesión.")
            save_state(paths, build_status(paths, master))
            return 0


def _scan_ready(downloads: Path, start: float, seen: Dict[Path, int]) -> List[Path]:
    """Archivos de vídeo nuevos y con tamaño estable entre dos sondeos (descarga completa)."""
    ready: List[Path] = []
    for media in sorted(downloads.iterdir()):
        if not media.is_file() or media.suffix.lower() not in MEDIA_EXTS:
            continue
        try:
            if media.stat().st_mtime < start:
                continue
            size = media.stat().st_size
        except OSError:
            continue
        if media in seen:
            last = seen[media]
            if last == size and size > 0:
                ready.append(media)
        else:
            seen[media] = size
    return ready


def cmd_watch(args: argparse.Namespace) -> int:
    nf.require_ffmpeg()
    paths, master = _prepare(args)
    downloads = Path(args.downloads).expanduser()
    if not downloads.is_dir():
        raise nf.NFError(f"No existe la carpeta de descargas: {downloads}")
    start = 0.0 if args.all else time.time() - 2
    seen: Dict[Path, int] = {}
    nf.info(f"Vigilando {downloads} (Ctrl+C para parar)")
    nf.info(f"Destino: {paths['raw_clips']}")
    try:
        if args.once:
            # Dos sondeos rápidos para confirmar que la descarga terminó, y salir.
            _scan_ready(downloads, start, seen)
            time.sleep(max(1.0, min(2.0, float(args.interval))))
        while True:
            rows = build_status(paths, master)
            if not _missing_rows(rows):
                nf.ok("Todas las escenas tienen clip.")
                save_state(paths, rows)
                return 0
            for media in _scan_ready(downloads, start, seen):
                rows = build_status(paths, master)
                pending = _missing_rows(rows)
                if not pending:
                    break
                row = pending[0]
                sid = row["scene_id"]
                seen[media] = media.stat().st_size if media.exists() else 0
                if args.dry_run:
                    nf.info(f"[dry-run] {media.name} -> {nf.scene_stem(sid)}.mp4")
                    continue
                ok, note = assign_clip(media, paths, sid, overwrite=args.overwrite,
                                       force_duration=args.force_duration)
                if ok:
                    nf.ok(f"{media.name} -> escena {sid}: {note}")
                else:
                    nf.warn(f"{media.name}: {note}")
            if args.once:
                save_state(paths, build_status(paths, master))
                return 0
            time.sleep(max(1.0, float(args.interval)))
    except KeyboardInterrupt:
        nf.info("Watcher detenido.")
        save_state(paths, build_status(paths, master))
        return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Runner local de la cola de Omni (status/queue/assisted/watch). Sin APIs.",
    )
    parser.add_argument("project", help="Slug del episodio.")
    parser.add_argument("command", choices=["status", "queue", "assisted", "watch"],
                        help="Acción a ejecutar.")
    parser.add_argument("--downloads", default=str(DEFAULT_DOWNLOADS),
                        help="Carpeta de descargas a vigilar (por defecto: ~/Downloads).")
    parser.add_argument("--interval", type=float, default=3.0, help="Segundos entre sondeos en watch.")
    parser.add_argument("--once", action="store_true", help="watch: una sola pasada.")
    parser.add_argument("--all", action="store_true", help="watch: incluye archivos ya existentes.")
    parser.add_argument("--dry-run", action="store_true", help="watch: muestra sin mover archivos.")
    parser.add_argument("--count", type=int, default=0, help="assisted: clips a procesar en esta sesión.")
    parser.add_argument("--no-clipboard", action="store_true", help="assisted: no tocar el portapapeles.")
    parser.add_argument("--overwrite", action="store_true", help="Reemplaza clips existentes.")
    parser.add_argument("--force-duration", action="store_true",
                        help="Acepta clips fuera de 5-15 s (por si Omni cambió el formato).")
    parser.add_argument("--playwright-script", default="",
                        help="Script local opcional (Playwright propio) a ejecutar antes de cada espera.")
    args = parser.parse_args(argv)

    nf.log("")
    nf.log("=" * 70)
    nf.log("  NOVEL FACTORY — Runner de la cola de Omni")
    nf.log("=" * 70)
    try:
        if args.command == "status":
            return cmd_status(args)
        if args.command == "queue":
            return cmd_queue(args)
        if args.command == "assisted":
            return cmd_assisted(args)
        return cmd_watch(args)
    except nf.NFError as exc:
        nf.err(str(exc))
        return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except nf.NFError as exc:
        nf.err(str(exc))
        sys.exit(1)

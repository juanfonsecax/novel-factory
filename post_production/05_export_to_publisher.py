#!/usr/bin/env python3
"""05 — Puente novel_factory -> publicador de USA WHITE (por archivos, sin tocar su código).

Qué hace:
  1. Localiza el sistema publicador (carpeta USA WHITE: cola/pendientes + src/orquestador.py).
  2. Toma los 3 teasers 9:16 renderizados por 04 (o los que existan) y arma un post JSON
     con el esquema EXACTO que ya consume el orquestador / auto_runner:
        id, personaje_id, tipo="reel", fecha_creacion, archivo_media, hook, caption,
        estado="pendiente_aprobacion", final_video=true, output_filename, plataformas
  3. Copia el MP4 junto al JSON en cola/pendientes/ (el orquestador busca la media ahí).
  4. Imprime cómo lanzar la publicación (manual segura o daemon por horarios).

Seguridad:
  - Por defecto es PLAN (dry-run): no escribe nada. Con --apply copia de verdad.
  - No duplica: si el JSON o el MP4 ya existen en la cola, se omite (salvo --force).
  - El id incluye el slug del episodio; los teasers entran ordenados 01, 02, 03.
  - NO se exporta el master largo: el publicador de YouTube de USA WHITE es solo Shorts;
    el master se sube a mano con output/publish_pack/youtube_master.md.

Uso:
  python post_production/05_export_to_publisher.py mi_episodio                  (plan)
  python post_production/05_export_to_publisher.py mi_episodio --apply          (exporta)
  python post_production/05_export_to_publisher.py mi_episodio --only 1,2 --apply
  python post_production/05_export_to_publisher.py mi_episodio --publisher-root "C:\\ruta\\USA WHITE" --apply
  python post_production/05_export_to_publisher.py mi_episodio --personaje eva_hayes --apply
"""
from __future__ import annotations

import argparse
import datetime as dt
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

NF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(NF_ROOT))
import nf_core as nf  # noqa: E402


# ---------------------------------------------------------------------------
# Localización del publicador
# ---------------------------------------------------------------------------
def _looks_like_publisher(path: Path) -> bool:
    return (
        (path / "src" / "orquestador.py").exists()
        and (path / "cola" / "pendientes").is_dir()
    )


def find_publisher_root(explicit: str = "") -> Optional[Path]:
    """Devuelve la raíz de USA WHITE. Si falla, None (el llamador explica cómo arreglarlo).

    Con --publisher-root se busca SOLO ahí (la carpeta, su padre y sus hijas directas);
    nunca se cae silenciosamente a la autodetección, para no publicar en el sitio equivocado.
    """
    if explicit:
        base = Path(explicit).expanduser()
        candidates: List[Path] = [base, base.parent]
        if base.is_dir():
            try:
                candidates += [child for child in sorted(base.iterdir()) if child.is_dir()]
            except OSError:
                pass
        for cand in candidates:
            try:
                cand = cand.resolve()
            except OSError:
                continue
            if _looks_like_publisher(cand):
                return cand
        return None

    candidates = []
    # Búsqueda alrededor del workspace: hermanos de novel_factory y de su padre
    for anchor in (NF_ROOT.parent, NF_ROOT.parent.parent):
        if anchor == anchor.parent:
            continue
        try:
            for child in sorted(anchor.iterdir()):
                if child.is_dir():
                    candidates.append(child)
        except OSError:
            continue
    seen: set = set()
    for cand in candidates:
        try:
            cand = cand.resolve()
        except OSError:
            continue
        if cand in seen:
            continue
        seen.add(cand)
        if _looks_like_publisher(cand):
            return cand
    return None


# ---------------------------------------------------------------------------
# Datos del episodio
# ---------------------------------------------------------------------------
def collect_teasers(paths: Dict[str, Path], master: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Combina publish_pack/metadata.json (preferente) con master.teasers y los archivos reales."""
    pack = nf.read_json(paths["output"] / "publish_pack" / "metadata.json", default=None)
    by_id: Dict[int, Dict[str, Any]] = {}
    for teaser in master.get("teasers") or []:
        if isinstance(teaser, dict):
            try:
                by_id[int(teaser.get("id") or 0)] = dict(teaser)
            except (TypeError, ValueError):
                continue
    if isinstance(pack, dict):
        for item in pack.get("teasers") or []:
            if not isinstance(item, dict):
                continue
            try:
                tid = int(item.get("id") or 0)
            except (TypeError, ValueError):
                continue
            merged = by_id.setdefault(tid, {})
            for key in ("hook_text", "scenes"):
                if item.get(key) and not merged.get(key):
                    merged[key] = item[key]
            # El pack de 04 ya añade los hashtags al caption: es preferible al del maestro.
            if item.get("caption"):
                merged["caption"] = item["caption"]
            if item.get("file"):
                merged["_file"] = str(item["file"])

    out: List[Dict[str, Any]] = []
    for tid in sorted(by_id):
        teaser = by_id[tid]
        file_name = str(teaser.get("_file") or f"teaser_{tid:02d}_9x16.mp4")
        media = paths["output"] / file_name
        if not media.exists():
            # tolerancia: buscar cualquier teaser_XX_9x16*.mp4
            hits = sorted(paths["output"].glob(f"teaser_{tid:02d}_9x16*"))
            media = hits[0] if hits else media
        teaser["_media"] = media
        teaser["_id"] = tid
        out.append(teaser)
    return out


def verify_media(path: Path) -> List[str]:
    warnings: List[str] = []
    try:
        probe = nf.probe_media(path)
    except nf.NFError as exc:
        return [str(exc)]
    if not probe.get("has_video"):
        warnings.append("el archivo no tiene pista de vídeo")
    if probe.get("width") and probe.get("height"):
        if (probe["width"], probe["height"]) != (nf.TEASER_W, nf.TEASER_H):
            warnings.append(f"resolución {probe['width']}x{probe['height']} (se esperaba 1080x1920)")
    dur = float(probe.get("duration") or 0.0)
    if dur and not (45.0 <= dur <= 75.0):
        warnings.append(f"duración {dur:.1f}s (los teasers suelen ser ~60 s)")
    return warnings


# ---------------------------------------------------------------------------
# Construcción del post (esquema del orquestador de USA WHITE)
# ---------------------------------------------------------------------------
def build_post(
    teaser: Dict[str, Any],
    slug: str,
    personaje: str,
    media_name: str,
    stamp: str,
    hashtags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    hook = str(teaser.get("hook_text") or "").strip() or f"{slug.replace('_', ' ').title()} — teaser"
    caption = str(teaser.get("caption") or "").strip() or hook
    tags = " ".join(h for h in (hashtags or []) if str(h).strip())
    if tags and "#" not in caption:
        caption = f"{caption}\n\n{tags}"
    return {
        "id": f"nf_{slug}_teaser_{int(teaser['_id']):02d}",
        "personaje_id": personaje,
        "tipo": "reel",
        "fecha_creacion": stamp,
        "archivo_media": media_name,
        "hook": hook,
        "caption": caption,
        "estado": "pendiente_aprobacion",
        "final_video": True,
        "output_filename": media_name,
        "plataformas": {"instagram": True, "facebook": True, "tiktok": True, "youtube": True},
        "origen": {
            "modulo": "novel_factory",
            "proyecto": slug,
            "teaser": int(teaser["_id"]),
            "escenas": teaser.get("scenes"),
        },
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="05 — Exporta teasers 9:16 a la cola del publicador USA WHITE.")
    parser.add_argument("project", help="Slug del episodio.")
    parser.add_argument("--publisher-root", default="", help="Ruta a USA WHITE (si no se autodetecta).")
    parser.add_argument("--personaje", default="", help="personaje_id de la cola (p. ej. emma_hayes).")
    parser.add_argument("--only", default="", help="Solo estos teasers, p. ej. '1,3'.")
    parser.add_argument("--apply", action="store_true", help="Copia de verdad (sin esto solo muestra el plan).")
    parser.add_argument("--force", action="store_true", help="Sobrescribe si ya existe en la cola.")
    args = parser.parse_args(argv)

    nf.log("")
    nf.log("=" * 70)
    nf.log("  NOVEL FACTORY — 05 · Exportar teasers a la cola del publicador")
    nf.log("=" * 70)

    paths = nf.resolve_project(args.project)
    master = nf.load_master(paths["root"])
    slug = str(nf.episode_meta(master).get("slug") or args.project)
    personaje = args.personaje or str((master.get("publisher") or {}).get("personaje_id") or "emma_hayes")

    publisher = find_publisher_root(args.publisher_root)
    if publisher is None:
        nf.err("No se encontró la carpeta del publicador (debe contener src/orquestador.py y cola/pendientes).")
        nf.info("Indícala a mano:  --publisher-root \"C:\\ruta\\USA WHITE\"")
        return 1

    pendientes = publisher / "cola" / "pendientes"
    nf.info(f"Publicador : {publisher}")
    nf.info(f"Cola       : {pendientes}")
    nf.info(f"Personaje  : {personaje}")
    nf.info(f"Modo       : {'APPLY (copia a la cola)' if args.apply else 'PLAN (no escribe nada)'}")

    only_ids = {int(x) for x in nf.parse_ranges(args.only)} if args.only.strip() else None
    teasers = collect_teasers(paths, master)
    if not teasers:
        nf.err("El maestro no define teasers. Revisa master_episode.json (teasers) y re-ejecuta 04.")
        return 1
    if only_ids is not None:
        teasers = [t for t in teasers if int(t["_id"]) in only_ids]
    if not teasers:
        nf.err(f"--only {args.only} no coincide con ningún teaser disponible.")
        return 1

    stamp = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    pending: List[Dict[str, Any]] = []
    missing = 0
    for teaser in teasers:
        media: Path = teaser["_media"]
        if not media.exists():
            nf.warn(f"Teaser {teaser['_id']}: falta {media.name} (renderízalo con 04_assemble_novel_ffmpeg.py).")
            missing += 1
            continue
        for w in verify_media(media):
            nf.warn(f"Teaser {teaser['_id']}: {w}")
        media_name = f"nf_{slug}_teaser_{int(teaser['_id']):02d}_9x16.mp4"
        hashtags = list((master.get("publisher") or {}).get("hashtags") or [])
        post = build_post(teaser, slug, personaje, media_name, stamp, hashtags)
        dest_json = pendientes / f"{post['id']}.json"
        dest_media = pendientes / media_name
        pending.append({"teaser": teaser, "post": post, "src": media,
                        "json": dest_json, "media": dest_media})
    if not pending:
        nf.err("No hay ningún teaser renderizado para exportar.")
        return 1

    nf.log("")
    nf.info("Plan de exportación:")
    for item in pending:
        exists = item["json"].exists() or item["media"].exists()
        flag = " (YA EN COLA: se omite)" if exists and not args.force else ""
        nf.log(f"    - {item['json'].name}")
        nf.log(f"      media : {item['src'].name}  ->  {item['media']}{flag}")
        nf.log(f"      hook  : {str(item['post']['hook'])[:70]}")

    if not args.apply:
        nf.log("")
        nf.info("Esto ha sido un PLAN. Repite con --apply para copiar a la cola.")
        return 0 if missing == 0 else 1

    copied = 0
    for item in pending:
        if (item["json"].exists() or item["media"].exists()) and not args.force:
            nf.warn(f"{item['json'].name}: ya existía en la cola; se omite (usa --force para sobrescribir).")
            continue
        shutil.copy2(item["src"], item["media"])
        nf.write_json(item["json"], item["post"])
        nf.ok(f"Encolado: {item['json'].name} + {item['media'].name}")
        copied += 1
    if copied == 0:
        nf.warn("No se copió nada (todo existía ya). Usa --force para reemplazar.")
        return 0

    nf.log("")
    nf.log("-" * 70)
    nf.ok(f"{copied} teaser(s) en cola/pendientes de {publisher.name}.")
    nf.info("Prueba en seco del publicador (no publica nada):")
    nf.log(f'    cd "{publisher}"')
    nf.log(f"    python src\\orquestador.py --publicar-siguiente --seco")
    nf.info("Publicación real (uno a uno, en orden):")
    nf.log(f"    python src\\orquestador.py --publicar-siguiente")
    nf.info("O por horarios automáticos (daemon con slots US EST): run_auto.bat")
    nf.log("")
    nf.info("Master 16:9 (subirlo a mano a YouTube):")
    nf.log(f"    {paths['output'] / 'publish_pack'}")
    nf.log("")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except nf.NFError as exc:
        nf.err(str(exc))
        sys.exit(1)

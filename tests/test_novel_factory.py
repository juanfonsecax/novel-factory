#!/usr/bin/env python3
"""Tests offline de novel_factory — solo stdlib + (opcional) ffmpeg/ffprobe. Sin red, sin APIs.

Ejecutar desde la raíz del workspace:
    python -m unittest discover -s novel_factory/tests -v
    novel_factory\\novelfactory.bat test
"""
from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

NF_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(NF_ROOT))
import nf_core as nf  # noqa: E402


def load_module(name: str, *parts: str):
    path = NF_ROOT.joinpath(*parts)
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


GEN01 = load_module("nf_gen01", "generators", "01_story_to_master_json.py")
GEN02 = load_module("nf_gen02", "generators", "02_export_chatgpt_queue.py")
GEN03 = load_module("nf_gen03", "generators", "03_export_omni_queue.py")
ASM04 = load_module("nf_asm04", "post_production", "04_assemble_novel_ffmpeg.py")
PUB05 = load_module("nf_pub05", "post_production", "05_export_to_publisher.py")
RUNNER = load_module("nf_runner", "automation", "omni_flow_runner.py")
DASH = load_module("nf_dashboard", "automation", "dashboard.py")

DEMO_DIR = NF_ROOT / "projects" / "demo_contract"
HAS_FFMPEG = nf.has_ffmpeg()


def minimal_payload(scenes: int = 60) -> dict:
    return {
        "episode": {"title": "Unit Test Episode", "logline": "A test of the schema."},
        "scenes": [
            {
                "scene_id": i + 1,
                "beat": "test beat",
                "dialogue": f"Line number {i + 1} spoken by someone at the table.",
                "internal_cuts": ["wide establishing shot"],
                "first_frame_prompt": f"Cinematic still of the protagonist at location {i + 1}, " + "x" * 40,
                "sfx_ambience": "wind and distant waves",
            }
            for i in range(scenes)
        ],
    }


class CoreTests(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(nf.slugify("The Silent Contract!"), "the_silent_contract")
        self.assertEqual(nf.slugify("Corazón Roto"), "corazon_roto")
        self.assertEqual(nf.slugify(""), "episode")

    def test_parse_ranges(self):
        self.assertEqual(nf.parse_ranges("1-3,5"), [1, 2, 3, 5])
        self.assertEqual(nf.parse_ranges("3-1"), [1, 2, 3])
        self.assertEqual(nf.parse_ranges(""), [])
        with self.assertRaises(nf.NFError):
            nf.parse_ranges("a-b")

    def test_scene_stems(self):
        self.assertEqual(nf.scene_stem(1), "scene_001")
        self.assertEqual(nf.frame_stem(60), "frame_060")
        with self.assertRaises(nf.NFError):
            nf.scene_stem(61)

    def test_time_helpers(self):
        self.assertEqual(nf.fmt_srt(3661.5), "01:01:01,500")
        self.assertEqual(nf.human_duration(600), "10:00")
        self.assertEqual(nf.human_duration(55), "0:55")

    def test_extract_json_blob(self):
        fenced = 'bla bla\n```json\n{"a": 1}\n```\ntrailing'
        self.assertEqual(nf.extract_json_blob(fenced), {"a": 1})
        self.assertEqual(nf.extract_json_blob('prefix {"scenes": []} suffix'), {"scenes": []})
        with self.assertRaises(nf.NFError):
            nf.extract_json_blob("sin json aquí")

    def test_constants_locked(self):
        self.assertEqual((nf.SCENE_COUNT, nf.SCENE_SECONDS), (60, 10.0))
        self.assertEqual((nf.MASTER_W, nf.MASTER_H), (1920, 1080))
        self.assertEqual((nf.TEASER_W, nf.TEASER_H), (1080, 1920))
        self.assertEqual(nf.default_teaser_ranges(), [list(range(1, 7)), list(range(21, 27)), list(range(55, 61))])


class MasterSchemaTests(unittest.TestCase):
    def test_minimal_payload_normalizes(self):
        master, warnings = nf.normalize_master(minimal_payload(), "unit_slug", "Unit Title")
        self.assertEqual(len(master["scenes"]), 60)
        first = master["scenes"][0]
        self.assertEqual(first["dialogue"][0]["line"], "Line number 1 spoken by someone at the table.")
        self.assertGreaterEqual(len(first["internal_cuts"]), 2)
        self.assertEqual(first["internal_cuts"][0]["at"], 0.0)
        self.assertEqual(len(master["teasers"]), 3)
        for teaser in master["teasers"]:
            self.assertEqual(len(teaser["scenes"]), 6)
            self.assertTrue(teaser["hook_text"])
        self.assertIsInstance(warnings, list)

    def test_partial_rejected_without_flag(self):
        with self.assertRaises(nf.NFError):
            nf.normalize_master(minimal_payload(10), "unit_slug", "Unit Title")
        master, warnings = nf.normalize_master(minimal_payload(10), "unit_slug", "Unit Title", allow_partial=True)
        self.assertEqual(len(master["scenes"]), 10)
        self.assertTrue(any("parcial" in w.lower() for w in warnings))

    def test_demo_template_is_strictly_valid(self):
        payload = GEN01.build_demo_payload("unit_demo", "Unit Demo", "emma_hayes", 1)
        master, _ = nf.normalize_master(payload, "unit_demo", "Unit Demo")
        result = nf.validate_master(master)
        self.assertEqual(result["errors"], [], msg=f"errores: {result['errors']}")

    @unittest.skipUnless(DEMO_DIR.exists(), "no existe projects/demo_contract")
    def test_demo_master_on_disk_valid(self):
        master = nf.load_master(DEMO_DIR)
        result = nf.validate_master(master)
        self.assertEqual(result["errors"], [], msg=f"errores: {result['errors']}")


@unittest.skipUnless(DEMO_DIR.exists(), "no existe projects/demo_contract")
class GeneratorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.master = nf.load_master(DEMO_DIR)
        cls.style = nf.load_style_locks()
        cls.paths = nf.project_paths(DEMO_DIR)

    def test_chatgpt_queue_has_60_prompts(self):
        entries = GEN02.build_queue(self.master, self.style)
        self.assertEqual(len(entries), 60)
        self.assertEqual(entries[0]["scene_id"], 1)
        self.assertGreater(len(entries[0]["prompt"]), 60)

    def test_omni_rows_have_full_prompts(self):
        rows = GEN03.build_rows(self.master, self.paths, self.style)
        self.assertEqual(len(rows), 60)
        prompt = rows[0]["prompt"]
        self.assertIn("Begin exactly on the provided first frame", prompt)
        self.assertIn("DIALOGUE", prompt)
        self.assertEqual(rows[0]["duration_seconds"], 10)

    def test_reference_sheets_from_visual_reference(self):
        master = dict(self.master)
        master["characters"] = [
            {"id": "elena", "name": "Elena Vance",
             "visual_reference": "mid-twenties ranch maid, chestnut low braid, faded denim work shirt"},
            {"id": "victoria", "name": "Victoria Blackwell"},
            {"id": "cole", "name": "Cole Barrett", "reference_image": "cole_ref.png"},
        ]
        sheets = GEN02.build_reference_sheets(master)
        self.assertEqual([s["id"] for s in sheets], ["elena", "cole"])
        self.assertIn("chestnut low braid", sheets[0]["prompt"])
        self.assertEqual(sheets[0]["filename"], "reference_elena.png")
        self.assertEqual(sheets[1]["existing_image"], "cole_ref.png")
        self.assertEqual(sheets[1]["prompt"], "")
        with tempfile.TemporaryDirectory() as tmp:
            paths = {"root": Path(tmp)}
            out = GEN02.write_reference_sheets(paths, master, sheets)
            text = out.read_text(encoding="utf-8")
            self.assertIn("reference_elena.png", text)
            self.assertIn("reference_cole.png", text)


class AssemblerTests(unittest.TestCase):
    def test_write_srt(self):
        timeline = [
            {"scene": {"scene_id": 1, "dialogue": [{"speaker": "Nora", "line": "I don't believe you."}]},
             "start": 0.0, "dur": 10.0},
            {"scene": {"scene_id": 2, "dialogue": [
                {"speaker": "", "line": "Then check the ledger."},
                {"speaker": "Mara", "line": "The ledger is gone."},
            ]}, "start": 10.0, "dur": 9.0},
        ]
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "x.srt"
            cues = ASM04.write_srt(timeline, out)
            self.assertEqual(cues, 3)
            text = out.read_text(encoding="utf-8")
            self.assertIn("NORA: I don't believe you.", text)
            self.assertIn("MARA: The ledger is gone.", text)
            self.assertIn("00:00:00,250 -->", text)

    def test_added_output_args_are_before_output_file(self):
        """Regresión: los -map/-af deben ir antes del archivo de salida (ffmpeg los ignora si van después)."""
        import inspect

        src = inspect.getsource(ASM04.normalize_scene)
        self.assertIn("map_args", src)
        self.assertLess(src.index("map_args + ["), src.index("str(dst)"))

    def test_concat_list_escaping(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            tricky = base / "clip_with_'quote.mp4"
            tricky.write_bytes(b"x")
            list_file = ASM04.concat_list([tricky], base / "list.txt")
            content = list_file.read_text(encoding="utf-8")
            self.assertIn("'\\''", content)
            self.assertTrue(content.startswith("file '"))
            self.assertTrue(list_file.read_text(encoding="utf-8").endswith("\n"))

    def test_pick_music_missing_override(self):
        with self.assertRaises(nf.NFError):
            ASM04.pick_music({}, "slug", str(Path(tempfile.gettempdir()) / "no_existe_nf.mp3"))

    @unittest.skipUnless(HAS_FFMPEG, "ffmpeg no disponible")
    def test_analyze_silence_detects_head(self):
        with tempfile.TemporaryDirectory() as tmp:
            clip = Path(tmp) / "silent_head.mp4"
            nf.run_ffmpeg([
                "ffmpeg", "-y", "-v", "error",
                "-f", "lavfi", "-i", "color=c=black:s=320x180:d=6:r=30",
                "-f", "lavfi", "-i", "sine=frequency=440:duration=3:sample_rate=48000",
                "-filter_complex", "[1:a]volume=0.5,adelay=1500,apad=whole_dur=6[a]",
                "-map", "0:v", "-map", "[a]", "-t", "6",
                "-c:v", "libx264", "-preset", "ultrafast", "-crf", "35",
                "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k", str(clip),
            ])
            probe = nf.probe_media(clip)
            # min_keep bajo: este clip de prueba dura 6 s (las escenas reales duran 10 s)
            head, tail, note = ASM04.analyze_silence(clip, probe, {"min_scene_after_trim_sec": 1.0})
            self.assertGreater(head, 1.2)
            self.assertLess(head, 1.6)
            self.assertGreater(tail, 4.2)
            self.assertLess(tail, 4.9)
            self.assertIn("recorte", note)

    @unittest.skipUnless(HAS_FFMPEG, "ffmpeg no disponible")
    def test_analyze_silence_discards_when_too_short(self):
        """Con min_keep por defecto (6 s) un clip de 6 s no se recorta: se conserva entero."""
        with tempfile.TemporaryDirectory() as tmp:
            clip = Path(tmp) / "tiny.mp4"
            nf.run_ffmpeg([
                "ffmpeg", "-y", "-v", "error",
                "-f", "lavfi", "-i", "color=c=black:s=320x180:d=6:r=30",
                "-f", "lavfi", "-i", "sine=frequency=440:duration=3:sample_rate=48000",
                "-filter_complex", "[1:a]volume=0.5,adelay=1500,apad=whole_dur=6[a]",
                "-map", "0:v", "-map", "[a]", "-t", "6",
                "-c:v", "libx264", "-preset", "ultrafast", "-crf", "35",
                "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k", str(clip),
            ])
            probe = nf.probe_media(clip)
            head, tail, note = ASM04.analyze_silence(clip, probe, {})
            self.assertEqual(head, 0.0)
            self.assertAlmostEqual(tail, float(probe["duration"]), delta=0.3)
            self.assertIn("descartado", note)


    def test_scene_target_seconds_default_and_override(self):
        self.assertEqual(ASM04.scene_target_seconds({}), nf.SCENE_SECONDS)
        self.assertEqual(ASM04.scene_target_seconds({"scene_seconds": 10.0}), 10.0)
        self.assertEqual(ASM04.scene_target_seconds({"scene_seconds": "8"}), 8.0)

    def test_build_cues_proportional_and_rebased(self):
        timeline = [
            {"scene": {"scene_id": 5, "dialogue": [
                {"speaker": "Nora", "line": "One two"},
                {"speaker": "", "line": "Three four five six"},
            ]}, "start": 20.0, "dur": 10.0},
        ]
        cues = ASM04.build_cues(timeline)
        self.assertEqual(len(cues), 2)
        self.assertAlmostEqual(cues[0][0], 20.25, delta=0.001)
        self.assertGreater(cues[1][0], cues[0][0])
        self.assertGreater(cues[0][1] - cues[0][0], 0.2)
        self.assertIn("NORA: One two", cues[0][2])

    def test_build_cues_empty_dialogue(self):
        timeline = [{"scene": {"scene_id": 1, "dialogue": []}, "start": 0.0, "dur": 10.0}]
        self.assertEqual(ASM04.build_cues(timeline), [])

    @unittest.skipUnless(HAS_FFMPEG, "ffmpeg no disponible")
    def test_normalize_scene_exact_duration(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            src = base / "short.mp4"
            nf.run_ffmpeg([
                "ffmpeg", "-y", "-v", "error",
                "-f", "lavfi", "-i", "color=c=blue:s=320x180:d=4:r=30",
                "-f", "lavfi", "-i", "sine=frequency=440:duration=4:sample_rate=48000",
                "-map", "0:v", "-map", "1:a", "-t", "4",
                "-c:v", "libx264", "-preset", "ultrafast", "-crf", "35",
                "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k", str(src),
            ])
            dst = base / "norm.mp4"
            ASM04.normalize_scene(src, dst, 0.2, {"scene_seconds": 3.0}, 30, True)
            dur = float(nf.probe_media(dst).get("duration") or 0.0)
            self.assertAlmostEqual(dur, 3.0, delta=nf.DURATION_TOLERANCE_SEC + 0.05)


class PublisherTests(unittest.TestCase):
    def _fake_publisher(self, base: Path) -> Path:
        (base / "src").mkdir(parents=True)
        (base / "src" / "orquestador.py").write_text("", encoding="utf-8")
        (base / "cola" / "pendientes").mkdir(parents=True)
        return base

    def test_find_publisher_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self._fake_publisher(Path(tmp) / "USA WHITE")
            found = PUB05.find_publisher_root(str(root))
            self.assertEqual(Path(found).resolve(), root.resolve())
            # acepta también el padre
            found_parent = PUB05.find_publisher_root(str(root.parent))
            self.assertEqual(Path(found_parent).resolve(), root.resolve())
            # ruta explícita inválida -> None (jamás se cae a la autodetección)
            self.assertIsNone(PUB05.find_publisher_root(str(Path(tmp) / "no_publisher")))

    def test_build_post_adds_hashtags(self):
        teaser = {"_id": 2, "hook_text": "HOOK TEXT", "caption": "Plain caption."}
        post = PUB05.build_post(teaser, "my_slug", "eva_hayes", "media.mp4", "stamp", ["#a", "#b"])
        self.assertEqual(post["id"], "nf_my_slug_teaser_02")
        self.assertEqual(post["tipo"], "reel")
        self.assertEqual(post["personaje_id"], "eva_hayes")
        self.assertIn("#a #b", post["caption"])
        self.assertTrue(post["plataformas"]["youtube"])

    def test_collect_teasers_prefers_pack_caption(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "output"
            (output / "publish_pack").mkdir(parents=True)
            (output / "teaser_01_9x16.mp4").write_bytes(b"x")
            nf.write_json(output / "publish_pack" / "metadata.json", {
                "teasers": [{"id": 1, "file": "teaser_01_9x16.mp4",
                             "caption": "Pack caption with #tags"}],
            })
            master = {"teasers": [{"id": 1, "hook_text": "H", "caption": "Master caption",
                                   "scenes": [1, 2, 3, 4, 5, 6]}]}
            teasers = PUB05.collect_teasers({"output": output}, master)
            self.assertEqual(len(teasers), 1)
            self.assertEqual(teasers[0]["caption"], "Pack caption with #tags")

    @unittest.skipUnless(HAS_FFMPEG, "ffmpeg no disponible")
    def test_verify_media_flags_wrong_aspect(self):
        with tempfile.TemporaryDirectory() as tmp:
            clip = Path(tmp) / "wrong.mp4"
            nf.run_ffmpeg(["ffmpeg", "-y", "-v", "error", "-f", "lavfi",
                           "-i", "color=c=black:s=640x360:d=1:r=30",
                           "-c:v", "libx264", "-preset", "ultrafast", "-crf", "40",
                           "-pix_fmt", "yuv420p", str(clip)])
            warnings = PUB05.verify_media(clip)
            self.assertTrue(any("1080x1920" in w for w in warnings))

    def test_enqueue_item_idempotent_and_atomic(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            pend = base / "cola" / "pendientes"
            src = base / "src.mp4"
            src.write_bytes(b"video")
            post = {"id": "nf_slug_teaser_01", "personaje_id": "eva", "tipo": "reel",
                    "archivo_media": "m.mp4", "estado": "pendiente_aprobacion",
                    "plataformas": {"instagram": True}}
            status, dj, dm = PUB05.enqueue_item(pend, post, src, "m.mp4")
            self.assertEqual(status, "copied")
            self.assertTrue(dj.exists() and dm.exists())
            self.assertEqual(dm.read_bytes(), b"video")
            # re-run: no duplica ni reescribe
            status2, _, _ = PUB05.enqueue_item(pend, post, src, "m.mp4")
            self.assertEqual(status2, "skipped")
            # force reemplaza
            status3, _, _ = PUB05.enqueue_item(pend, post, src, "m.mp4", force=True)
            self.assertEqual(status3, "copied")
            # no quedan temporales .part-*
            self.assertEqual(list(pend.glob("*.part-*")), [])

    def test_enqueue_item_repairs_partial(self):
        with tempfile.TemporaryDirectory() as tmp:
            pend = Path(tmp) / "cola" / "pendientes"
            pend.mkdir(parents=True)
            src = Path(tmp) / "src.mp4"
            src.write_bytes(b"video")
            post = {"id": "nf_slug_teaser_02", "personaje_id": "eva", "tipo": "reel",
                    "archivo_media": "m2.mp4", "estado": "pendiente_aprobacion",
                    "plataformas": {"instagram": True}}
            # encolado incompleto: solo el JSON
            nf.write_json(pend / "nf_slug_teaser_02.json", post)
            status, dj, dm = PUB05.enqueue_item(pend, post, src, "m2.mp4")
            self.assertEqual(status, "repaired")
            self.assertTrue(dm.exists())

    def test_validate_post(self):
        good = {"id": "x", "personaje_id": "eva", "tipo": "reel",
                "archivo_media": "m.mp4", "estado": "pendiente_aprobacion",
                "plataformas": {"instagram": True}}
        self.assertEqual(PUB05.validate_post(good), [])
        bad = dict(good, tipo="video", plataformas={})
        problems = PUB05.validate_post(bad)
        self.assertTrue(any("reel" in p for p in problems))
        self.assertTrue(any("plataformas" in p for p in problems))


class RunnerTests(unittest.TestCase):
    def test_load_queue(self):
        with tempfile.TemporaryDirectory() as tmp:
            queue_file = Path(tmp) / "omni_video_prompts_queue.json"
            nf.write_json(queue_file, {"items": [{"scene_id": 1, "prompt": "p1"},
                                                {"scene_id": 2, "prompt": "p2"}]})
            queue = RUNNER.load_queue({"omni_json": queue_file})
            self.assertEqual(sorted(queue), [1, 2])
            self.assertEqual(queue[1]["prompt"], "p1")

    def test_find_newest_media_respects_since(self):
        import os
        import time

        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            old = folder / "old.mp4"
            old.write_bytes(b"x")
            os.utime(old, (time.time() - 600, time.time() - 600))
            new = folder / "new.mp4"
            new.write_bytes(b"y")
            self.assertEqual(RUNNER.find_newest_media(folder, time.time() - 60), new)
            self.assertIsNone(RUNNER.find_newest_media(folder, time.time() + 60))

    @unittest.skipUnless(HAS_FFMPEG, "ffmpeg no disponible")
    def test_assign_clip_rejects_non_video(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            bogus = base / "bogus.mp4"
            bogus.write_text("esto no es un vídeo", encoding="utf-8")
            paths = {"raw_clips": base / "raw_clips"}
            ok, note = RUNNER.assign_clip(bogus, paths, 1)
            self.assertFalse(ok)
            self.assertIn("inválido", note)

    @unittest.skipUnless(HAS_FFMPEG, "ffmpeg no disponible")
    def test_assign_clip_moves_and_names(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            clip = base / "descarga.mp4"
            nf.run_ffmpeg(["ffmpeg", "-y", "-v", "error",
                           "-f", "lavfi", "-i", "color=c=black:s=320x180:d=2:r=30",
                           "-c:v", "libx264", "-preset", "ultrafast", "-crf", "40",
                           "-pix_fmt", "yuv420p", str(clip)])
            paths = {"raw_clips": base / "raw_clips"}
            ok, note = RUNNER.assign_clip(clip, paths, 7, force_duration=True)
            self.assertTrue(ok, msg=note)
            self.assertTrue((paths["raw_clips"] / "scene_007.mp4").exists())
            self.assertFalse(clip.exists())


class DashboardTests(unittest.TestCase):
    def test_build_state_from_demo(self):
        state = DASH.build_state(DEMO_DIR)
        self.assertEqual(state["totals"]["scenes"], 60)
        self.assertEqual(len(state["scenes"]), 60)
        first = state["scenes"][0]
        self.assertTrue(first["image_prompt"])
        self.assertTrue(first["video_prompt"])
        self.assertEqual(first["scene_id"], 1)
        self.assertTrue(first["scene_json"].startswith("{"))
        self.assertGreaterEqual(state["totals"]["clips_disk"], 1)

    def test_render_escapes_script_tags(self):
        state = DASH.build_state(DEMO_DIR)
        state["logline"] = "cierre </script><script>alert(1)</script>"
        html = DASH.render_dashboard(state, {"scenes": {}, "references": {}})
        self.assertEqual(html.count("</script>"), 1)
        self.assertIn("const STATE =", html)
        self.assertIn("Novel Factory", html)

    def test_tracking_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = {"root": Path(tmp)}
            data = {"scenes": {"1": {"image_done": "2026-01-01T00:00:00Z"}}, "references": {}}
            saved = DASH.save_tracking(paths, data)
            self.assertTrue(saved["updated_at"])
            loaded = DASH.load_tracking(paths)
            self.assertEqual(loaded["scenes"]["1"]["image_done"], "2026-01-01T00:00:00Z")

    def test_tracking_rejects_invalid(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(nf.NFError):
                DASH.save_tracking({"root": Path(tmp)}, ["not", "an", "object"])


class LauncherTests(unittest.TestCase):
    def test_bat_dispatches_import_frames(self):
        bat = (NF_ROOT / "novelfactory.bat").read_text(encoding="utf-8", errors="replace")
        self.assertIn('"%CMD%"=="import-frames"', bat)
        self.assertIn("omni_flow_runner.py", bat)
        self.assertIn("MODE=import-frames", bat)

    def test_bat_dispatches_dashboard(self):
        bat = (NF_ROOT / "novelfactory.bat").read_text(encoding="utf-8", errors="replace")
        self.assertIn('"%CMD%"=="dashboard"', bat)
        self.assertIn("dashboard.py", bat)

    def test_bat_propagates_errors(self):
        bat = (NF_ROOT / "novelfactory.bat").read_text(encoding="utf-8", errors="replace")
        self.assertIn("if errorlevel 1", bat)
        self.assertIn(":INGEST_RUN", bat)


if __name__ == "__main__":
    unittest.main(verbosity=2)

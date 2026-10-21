#!/usr/bin/env python3
"""Tests offline de novel_factory — solo stdlib + (opcional) ffmpeg/ffprobe. Sin red, sin APIs.

Ejecutar desde la raíz del workspace:
    python -m unittest discover -s novel_factory/tests -v
    novel_factory\\novelfactory.bat test
"""
from __future__ import annotations

import importlib.util
import json
import shutil
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


GEN00 = load_module("nf_gen00", "generators", "00_export_master_workflow_prompts.py")
GEN01 = load_module("nf_gen01", "generators", "01_story_to_master_json.py")
GEN02 = load_module("nf_gen02", "generators", "02_export_chatgpt_queue.py")
GEN03 = load_module("nf_gen03", "generators", "03_export_omni_queue.py")
MPL = load_module("nf_mpl", "generators", "master_prompts_library.py")
GEN04 = load_module("nf_gen04", "generators", "04_export_master_prompts.py")
GEN05 = load_module("nf_gen05", "generators", "05_export_muse_method_pack.py")
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


@unittest.skipUnless(DEMO_DIR.exists(), "no existe projects/demo_contract")
class MasterPromptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.master = nf.load_master(DEMO_DIR)
        cls.style = nf.load_style_locks()
        cls.paths = nf.project_paths(DEMO_DIR)
        cls.pack = MPL.build_prompt_pack(cls.master, cls.style)

    def test_four_prompts_and_no_unfilled(self):
        self.assertEqual([p["key"] for p in self.pack["prompts"]], list(MPL.PROMPT_ORDER))
        self.assertEqual(int(self.pack["values"]["total_scenes"]), 60)
        for prompt in self.pack["prompts"]:
            self.assertEqual(prompt["unfilled"], [], msg=prompt["key"])
            self.assertGreater(prompt["chars"], 500)

    def test_prompt_000_keeps_literal_header(self):
        text = MPL.TEMPLATES["prompt_000"]["text"]
        self.assertTrue(text.startswith("🧠 PROMPT 000"))
        self.assertIn("ARQUITECTO DE HISTORIAS VIRALES", text)
        self.assertIn("CHINA / USA MICRO-DRAMA", text)

    def test_platform_prompts_differ(self):
        muse = GEN03.build_rows(self.master, self.paths, self.style, "muse")
        flow = GEN03.build_rows(self.master, self.paths, self.style, "flow")
        self.assertEqual(len(muse), 60)
        self.assertTrue(muse[0]["prompt"].startswith("MUSE AI"))
        self.assertIn("10 SECONDS", muse[0]["prompt"])
        self.assertTrue(flow[0]["prompt"].startswith("GOOGLE FLOW"))
        self.assertIn("7.5 s", flow[0]["prompt"])
        self.assertEqual(muse[0]["platform"], "muse")
        self.assertEqual(flow[0]["platform"], "flow")

    def test_write_prompt_pack(self):
        with tempfile.TemporaryDirectory() as tmp:
            written = MPL.write_prompt_pack(Path(tmp), self.pack)
            for key in ("markdown", "plain", "json"):
                self.assertTrue(written[key].exists(), msg=key)
            prompt_files = list((Path(tmp) / "prompts").glob("*.txt"))
            self.assertEqual(len(prompt_files), 4)
            self.assertIn("PROMPT 000", written["markdown"].read_text(encoding="utf-8"))

    def test_export_entrypoint(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = GEN04.export_prompts(DEMO_DIR, Path(tmp))
            self.assertEqual(len(result["pack"]["prompts"]), 4)
            self.assertTrue((Path(tmp) / "master_prompts.json").exists())

    def test_four_literal_prompt_constants(self):
        expected = {
            "PROMPT_000_VIRAL_STORY_ARCHITECT": "PROMPT 000",
            "PROMPT_001_STORYBOARD_GENERATOR": "PROMPT 001",
            "PROMPT_002_CHARACTER_SHEET_GENERATOR": "PROMPT 002",
            "PROMPT_003_SCRIPT_CAMERA_SOUND_GENERATOR": "PROMPT 003",
        }
        for name, header in expected.items():
            text = getattr(MPL, name)
            self.assertIn(header, text)
            self.assertGreater(len(text), 500, msg=name)
        self.assertIn("6 viñetas", MPL.PROMPT_001_STORYBOARD_GENERATOR)
        self.assertIn("UNA SOLA IMAGEN", MPL.PROMPT_002_CHARACTER_SHEET_GENERATOR)
        self.assertIn("COMANDO FINAL PARA PEGAR EN MUSE AI", MPL.PROMPT_003_SCRIPT_CAMERA_SOUND_GENERATOR)

    def test_workflow_export_writes_ready_and_batches(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = GEN00.export_workflow(DEMO_DIR, Path(tmp))
            target = Path(tmp)
            ready = target / "MASTER_WORKFLOW_PROMPTS_READY.md"
            self.assertTrue(ready.exists())
            text = ready.read_text(encoding="utf-8")
            for code in ("PROMPT 000", "PROMPT 001", "PROMPT 002", "PROMPT 003", "9:16"):
                self.assertIn(code, text)
            self.assertEqual(len(result["batches"]), 10)
            for name in (
                "muse_ai_minute_batches_queue.txt",
                "muse_ai_minute_batches_queue.json",
                "muse_ai_batches_queue.txt",
                "muse_ai_batches_queue.json",
            ):
                self.assertTrue((target / name).exists(), msg=name)
            batches_text = (target / "muse_ai_batches_queue.txt").read_text(encoding="utf-8")
            self.assertIn("ESCENA 1", batches_text)
            self.assertIn("[00s–03s]", batches_text)
            self.assertIn("[03s–07s]", batches_text)
            self.assertIn("[07s–10s]", batches_text)
            self.assertIn("=== COPIA 16:9 (YouTube) ===", batches_text)
            self.assertIn("=== COPIA 9:16 (Reels / TikTok / Shorts) ===", batches_text)
            self.assertIn("📎 ADJUNTAR EN MUSE AI", batches_text)
            self.assertIn("REF_CAST_MASTER.png", batches_text)
            self.assertIn("REF_GRID_MIN_01.png", batches_text)
            self.assertIn("formato horizontal 16:9", batches_text)
            self.assertIn("formato vertical 9:16", batches_text)

    def test_viral_templates_catalog_has_six_us_meganiches(self):
        templates = MPL.list_viral_templates()
        expected = [
            "usa_01_secret_billionaire_divorce",
            "usa_02_heartland_ranch_heiress",
            "usa_03_instant_karma_vip_humiliation",
            "usa_04_silver_hair_grandma_inheritance",
            "usa_05_wrongful_sacrifice_gala_revenge",
            "usa_06_decorated_veteran_homecoming",
        ]
        self.assertEqual([template["id"] for template in templates], expected)
        for template in templates:
            for field in ("label", "category", "premise_seed", "must_include"):
                self.assertTrue(template.get(field), msg=f"{template.get('id')}: {field}")

    def test_prompt_000_with_niche_appends_us_archetype(self):
        niche_id = "usa_03_instant_karma_vip_humiliation"
        pack = MPL.build_prompt_pack(self.master, self.style, niche=niche_id)
        prompts = {prompt["key"]: prompt for prompt in pack["prompts"]}
        text = prompts["prompt_000"]["text"]
        self.assertTrue(text.startswith("🧠 PROMPT 000"))
        self.assertIn("USA MEGA-NICHE ARCHETYPE", text)
        self.assertIn(niche_id, text)
        self.assertEqual(MPL.unfilled_placeholders(text), [])
        self.assertNotIn("USA MEGA-NICHE ARCHETYPE", prompts["prompt_001"]["text"])
        self.assertEqual(pack["viral_template"]["id"], niche_id)
        with self.assertRaises(KeyError):
            MPL.build_prompt_pack(self.master, self.style, niche="no_existe")

    def test_workflow_export_with_niche(self):
        with tempfile.TemporaryDirectory() as tmp:
            GEN00.export_workflow(DEMO_DIR, Path(tmp), niche="usa_06_decorated_veteran_homecoming")
            text = (Path(tmp) / "MASTER_WORKFLOW_PROMPTS_READY.md").read_text(encoding="utf-8")
            self.assertIn("usa_06_decorated_veteran_homecoming", text)
            self.assertIn("USA MEGA-NICHE ARCHETYPE", text)

    def test_chatgpt_prompt_exports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = {"root": Path(tmp)}
            written = GEN02.write_master_image_prompt_files(paths, self.master, self.style)
            storyboard = written["prompt_001"].read_text(encoding="utf-8")
            characters = written["prompt_002"].read_text(encoding="utf-8")
            self.assertIn("GENERADOR DE STORYBOARD", storyboard)
            self.assertIn("HOJA MAESTRA DE PERSONAJES", characters)
            self.assertNotIn("{story_idea}", storyboard)
            self.assertNotIn("{visual_style}", characters)

    def test_muse_batches_export(self):
        with tempfile.TemporaryDirectory() as tmp:
            files = GEN03.write_muse_batches({"root": Path(tmp)}, self.master, self.style)
            self.assertTrue(files["txt"].exists())
            self.assertTrue(files["json"].exists())
            data = json.loads(files["json"].read_text(encoding="utf-8"))
            self.assertEqual(data["count"], 10)
            self.assertEqual(len(data["items"]), 10)
            self.assertEqual(data["items"][0]["scenes"], [1, 2, 3, 4, 5, 6])
            first = data["items"][0]
            self.assertEqual(first["reference_images"], ["REF_CAST_MASTER.png", "REF_GRID_MIN_01.png"])
            self.assertIn("formato horizontal 16:9", first["muse_command"])
            self.assertIn("formato vertical 9:16", first["muse_command_916"])

    def test_storyboard_prompt_includes_all_60_scenes(self):
        with tempfile.TemporaryDirectory() as tmp:
            written = GEN02.write_master_image_prompt_files({"root": Path(tmp)}, self.master, self.style)
            storyboard = written["prompt_001"].read_text(encoding="utf-8")
            self.assertIn("ESCENA 001", storyboard)
            self.assertIn("ESCENA 024", storyboard)
            self.assertIn("ESCENA 025", storyboard)
            self.assertIn("ESCENA 060", storyboard)
            self.assertIn("MINUTO 1 (Escenas 1 a 6)", storyboard)
            self.assertIn("MINUTO 10 (Escenas 55 a 60)", storyboard)
            self.assertGreaterEqual(storyboard.count("ESCENA "), 60)

    def test_storyboard_grids_queue_has_11_prompts(self):
        with tempfile.TemporaryDirectory() as tmp:
            written = GEN02.write_storyboard_grid_queue({"root": Path(tmp)}, self.master, self.style)
            data = json.loads(written["json"].read_text(encoding="utf-8"))
            self.assertEqual(data["count"], 11)
            self.assertEqual(len(data["items"]), 11)
            self.assertEqual(data["items"][0]["filename"], "REF_CAST_MASTER.png")
            self.assertEqual(data["items"][0]["kind"], "cast_sheet")
            self.assertIn("gris neutro", data["items"][0]["prompt"])
            self.assertEqual(
                [item["filename"] for item in data["items"][1:]],
                [f"REF_GRID_MIN_{n:02d}.png" for n in range(1, 11)],
            )
            self.assertEqual(data["items"][1]["scenes"], [1, 2, 3, 4, 5, 6])
            self.assertEqual(data["items"][10]["scenes"], [55, 56, 57, 58, 59, 60])
            self.assertIn("Viñeta 1 — Escena 1", data["items"][1]["prompt"])
            self.assertIn("Viñeta 6 — Escena 6", data["items"][1]["prompt"])
            self.assertIn("REF_CAST_MASTER.png", data["items"][1]["prompt"])
            lines = written["txt"].read_text(encoding="utf-8").strip().splitlines()
            self.assertEqual(len(lines), 11)


@unittest.skipUnless(DEMO_DIR.exists(), "no existe projects/demo_contract")
class MusePackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.master = nf.load_master(DEMO_DIR)
        cls.style = nf.load_style_locks()
        cls.pack = GEN05.build_pack(cls.master, cls.style)

    def test_pack_counts_and_order(self):
        self.assertEqual(self.pack["counts"]["images"], 11)
        self.assertEqual(self.pack["counts"]["storyboards"], 10)
        self.assertEqual(self.pack["counts"]["batches"], 10)
        self.assertEqual(self.pack["cast_master"]["filename"], "REF_CAST_MASTER.png")
        self.assertEqual(self.pack["batches"][0]["reference_images"], [
            "REF_CAST_MASTER.png", "REF_GRID_MIN_01.png",
        ])
        self.assertEqual(self.pack["batches"][-1]["scenes"], [55, 56, 57, 58, 59, 60])

    def test_markdown_has_the_four_steps(self):
        text = GEN05.render_markdown(self.pack)
        for step in ("Paso 1", "Paso 2", "Paso 3", "Paso 4"):
            self.assertIn(step, text)
        self.assertIn("REF_GRID_MIN_10.png", text)
        self.assertIn("minute_10.mp4", text)
        self.assertIn("Comando final 9:16", text)

    def test_write_pack_creates_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            written = GEN05.write_pack({"root": Path(tmp)}, self.pack)
            self.assertTrue(written["md"].exists())
            self.assertTrue(written["checklist"].exists())
            self.assertTrue(written["json"].exists())
            self.assertTrue(written["storyboards_readme"].exists())
            checklist = written["checklist"].read_text(encoding="utf-8")
            self.assertEqual(checklist.count("- [ ] `REF_GRID_MIN_"), 10)
            self.assertEqual(checklist.count("- [ ] `minute_"), 10)

    def test_muse_pack_subcommand_registered(self):
        script = nf.subcommand_script("muse-pack")
        self.assertIsNotNone(script)
        self.assertTrue(script.exists())

    def test_cast_prompt_has_no_attachment_placeholders_and_real_names(self):
        prompt = self.pack["cast_master"]["prompt"]
        self.assertNotIn("[ADJUNTAR", prompt)
        for name in ("NORA HALE", "SAM CALLOWAY", "MARGARET KELLER", "ADRIAN KELLER", "CLAIRE BOONE"):
            self.assertIn(name, prompt)

    def test_storyboard_queue_cast_prompt_is_clean(self):
        grids = GEN02.build_storyboard_grid_items(self.master, self.style)
        cast_prompt = grids[0]["prompt"]
        self.assertNotIn("[ADJUNTAR", cast_prompt)
        for name in ("NORA HALE", "SAM CALLOWAY", "MARGARET KELLER"):
            self.assertIn(name, cast_prompt)

    def test_muse_prompts_are_split_by_format_without_attachment_headers(self):
        first = self.pack["batches"][0]
        self.assertIn("formato horizontal 16:9", first["prompt_16x9_youtube"])
        self.assertIn("formato vertical 9:16", first["prompt_9x16_vertical"])
        self.assertNotIn("[ADJUNTAR", first["prompt_16x9_youtube"])
        self.assertNotIn("[ADJUNTAR", first["prompt_9x16_vertical"])
        self.assertNotIn("📎 ADJUNTAR", first["prompt_16x9_youtube"])
        self.assertNotIn("📎 ADJUNTAR", first["prompt_9x16_vertical"])
        self.assertEqual(first["save_as_16x9"], "raw_clips/minute_01.mp4")
        self.assertEqual(first["save_as_9x16"], "raw_clips/minute_01_vertical.mp4")
        self.assertEqual(first["attach_instruction"], first["attach"])


class ViralLatamTests(unittest.TestCase):
    def test_catalog_has_the_six_proven_structures(self):
        rules = nf.load_showrunner()
        templates = rules.get("viral_latam_to_usa_templates") or []
        expected = [
            ("ranch_laundress_stolen_heirloom", "@novelasaa7", "831K"),
            ("humiliated_vagabond_is_billionaire_owner", "@Mini_Dramas07", "658K"),
            ("hidden_will_secret_daughter", "@Mini_Dramas07 & @TIEMPOCONLASABUELAS", "578K"),
            ("contract_marriage_proud_foreman", "@Mini_Dramas07", "185K"),
            ("untamable_champion_horse", "@Mini_Dramas07", "122K"),
            ("grandmas_buried_secret_betrayal", "@TIEMPOCONLASABUELAS & @Dramasquetocanelalma", "+500K"),
        ]
        self.assertEqual([(t["id"], t["source"], t["views"]) for t in templates], expected)
        for template in templates:
            self.assertEqual(len(template["structure"]), 6, msg=template["id"])

    def test_story_prompt_injects_catalog_and_selected_structure(self):
        rules = nf.load_showrunner()
        style = nf.load_style_locks()
        prompt = GEN01.build_llm_prompt(
            slug="demo",
            title="Demo",
            brief_md="A brief.",
            rules=rules,
            style=style,
            personaje="emma_hayes",
            episode_number=1,
            viral_template="ranch_laundress_stolen_heirloom",
        )
        self.assertIn("VIRAL STRUCTURE CATALOG (LATAM -> USA)", prompt)
        for template in rules["viral_latam_to_usa_templates"]:
            self.assertIn(template["id"], prompt)
        self.assertIn("SELECTED VIRAL STRUCTURE (MANDATORY)", prompt)
        self.assertIn("ranch_laundress_stolen_heirloom", prompt)


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

    def test_normalize_scene_has_audio_micro_fade(self):
        import inspect

        src = inspect.getsource(ASM04.normalize_scene)
        self.assertIn("afade=t=in:st=0:d=0.08", src)

    def test_detect_clip_mode_scene_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp)
            for sid in range(1, 7):
                (raw / f"scene_{sid:03d}.mp4").write_bytes(b"x")
            detected = ASM04.detect_clip_mode(raw, list(range(1, 7)))
            self.assertEqual(detected["mode"], "scenes")
            self.assertEqual(detected["scene_clips"][1].name, "scene_001.mp4")
            self.assertEqual(detected["missing_scenes"], [])

    def test_detect_clip_mode_minute_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp)
            (raw / "minute_01.mp4").write_bytes(b"x")
            detected = ASM04.detect_clip_mode(raw, list(range(1, 7)))
            self.assertEqual(detected["mode"], "batches")
            self.assertEqual(detected["batch_clips"][1].name, "minute_01.mp4")
            self.assertEqual(detected["missing_batches"], [])

    def test_detect_clip_mode_batch_alias_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp)
            for number in range(1, 11):
                (raw / f"batch_{number:02d}.mp4").write_bytes(b"x")
            detected = ASM04.detect_clip_mode(raw, list(range(1, 61)))
            self.assertEqual(detected["mode"], "batches")
            self.assertEqual(len(detected["batch_clips"]), 10)
            self.assertEqual(detected["batch_clips"][10].name, "batch_10.mp4")

    def test_auto_teaser_uses_vertical_crop(self):
        import inspect

        src = inspect.getsource(ASM04.render_auto_teaser)
        self.assertIn("crop=ih*9/16:ih", src)
        self.assertIn("scale=1080:1920", src)
        self.assertIn("-t", src)


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

    def test_load_platform_queue(self):
        with tempfile.TemporaryDirectory() as tmp:
            queue_file = Path(tmp) / "muse_ai_video_prompts_queue.json"
            nf.write_json(queue_file, {"items": [{"scene_id": 3, "prompt": "muse prompt"}]})
            queue = RUNNER.load_queue({"muse_json": queue_file}, "muse")
            self.assertEqual(queue[3]["prompt"], "muse prompt")

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
        self.assertEqual(state["totals"]["master_prompts"], 4)
        self.assertEqual(sorted(first["video_prompts"]), ["flow", "muse", "omni"])
        self.assertEqual(len(state["master_prompts"]["items"]), 4)
        self.assertEqual(state["storyboard_grids"]["count"], 11)
        self.assertEqual(len(state["storyboard_grids"]["items"]), 11)
        self.assertIn("REF_CAST_MASTER.png", state["storyboard_grids"]["text"])
        self.assertEqual(state["assembly"]["minutes_expected"], 10)
        self.assertIn(state["assembly"]["clip_mode"], ("scenes", "batches", "incomplete", "empty"))
        self.assertIn("batch_clips_disk", state["totals"])
        self.assertEqual(state["assembly"]["storyboards_expected"], 11)
        self.assertIn("storyboards_disk", state["totals"])

    def test_build_state_detects_batch_mode(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "demo_contract"
            shutil.copytree(DEMO_DIR, root)
            raw = root / "raw_clips"
            raw.mkdir(exist_ok=True)
            for number in range(1, 11):
                (raw / f"minute_{number:02d}.mp4").write_bytes(b"x")
            storyboards = root / "storyboards"
            storyboards.mkdir(exist_ok=True)
            (storyboards / "REF_CAST_MASTER.png").write_bytes(b"x")
            (storyboards / "ref_grid_min_01.PNG").write_bytes(b"x")
            state = DASH.build_state(root)
            self.assertEqual(state["assembly"]["clip_mode"], "batches")
            self.assertEqual(state["assembly"]["batch_clips_disk"], 10)
            self.assertEqual(state["totals"]["batch_clips_disk"], 10)
            self.assertEqual(state["assembly"]["storyboards_disk"], 2)
            grid = state["storyboard_grids"]["items"][0]
            self.assertTrue(grid["exists"])
            self.assertEqual(grid["disk_file"], "REF_CAST_MASTER.png")

    def test_state_has_projects_and_latam_templates(self):
        state = DASH.build_state(DEMO_DIR)
        self.assertTrue(state["projects"])
        self.assertIn(state["slug"], [item["slug"] for item in state["projects"]])
        latam = state["viral_latam_templates"]
        self.assertEqual(len(latam), 6)
        self.assertEqual(latam[0]["id"], "ranch_laundress_stolen_heirloom")
        first = state["muse_batches"][0]
        for field in ("video_exists_16x9", "video_exists_9x16", "save_as_16x9", "save_as_9x16"):
            self.assertIn(field, first)

    def test_dashboard_has_four_step_guide_and_selectors(self):
        state = DASH.build_state(DEMO_DIR)
        html = DASH.render_dashboard(state, {"scenes": {}, "references": {}})
        for token in (
            "PASO 1", "PASO 2", "PASO 3", "PASO 4",
            "project-select", "format-select", "16:9 · YouTube", "9:16 · Reels / TikTok / Shorts",
            "references/REF_CAST_MASTER.png", "storyboards/REF_GRID_MIN_01.png",
            "raw_clips/minute_0X.mp4", "viral-template-select", "copy-storyboard-grids-10",
            "prompt_16x9_youtube", "prompt_9x16_vertical", "legacy-details",
        ):
            self.assertIn(token, html)

    def test_render_escapes_script_tags(self):
        state = DASH.build_state(DEMO_DIR)
        state["logline"] = "cierre </script><script>alert(1)</script>"
        html = DASH.render_dashboard(state, {"scenes": {}, "references": {}})
        self.assertEqual(html.count("</script>"), 1)
        self.assertIn("const STATE =", html)
        self.assertIn("Nueva metodología", html)
        self.assertIn("copy-muse-batch-169", html)
        self.assertIn("copy-storyboard-grid", html)
        self.assertIn("toggle-legacy", html)
        self.assertIn("Ver método anterior", html)
        self.assertIn("storyboards_disk", html)
        self.assertIn("Novel Factory", html)
        self.assertIn("Prompts maestros", html)
        self.assertIn("platform-filter", html)
        self.assertIn("Copiar prompt", html)

    def test_build_state_exposes_viral_template_selector(self):
        state = DASH.build_state(DEMO_DIR)
        catalog = state["viral_templates"]
        self.assertEqual(catalog["count"], 6)
        expected = [
            "usa_01_secret_billionaire_divorce",
            "usa_02_heartland_ranch_heiress",
            "usa_03_instant_karma_vip_humiliation",
            "usa_04_silver_hair_grandma_inheritance",
            "usa_05_wrongful_sacrifice_gala_revenge",
            "usa_06_decorated_veteran_homecoming",
        ]
        self.assertEqual([item["id"] for item in catalog["items"]], expected)
        for item in catalog["items"]:
            self.assertIn(item["id"], item["prompt"])
            self.assertIn("USA MEGA-NICHE ARCHETYPE", item["prompt"])
        html = DASH.render_dashboard(state, {"scenes": {}, "references": {}})
        for token in ("niche-select", "viral_templates", "usa_01_secret_billionaire_divorce", "Sin mega-nicho"):
            self.assertIn(token, html)

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

    def test_bat_dispatches_master_prompts_and_platforms(self):
        bat = (NF_ROOT / "novelfactory.bat").read_text(encoding="utf-8", errors="replace")
        self.assertIn('"%CMD%"=="prompts"', bat)
        self.assertIn("04_export_master_prompts.py", bat)
        self.assertIn('"%CMD%"=="export-master-prompts"', bat)
        self.assertIn("00_export_master_workflow_prompts.py", bat)
        self.assertIn('"%CMD%"=="muse"', bat)
        self.assertIn('"%CMD%"=="flow"', bat)
        self.assertIn("--platform muse", bat)
        self.assertIn("--platform flow", bat)

    def test_nf_core_registers_export_master_prompts(self):
        self.assertIn("export-master-prompts", nf.SUBCOMMANDS)
        script = nf.subcommand_script("export-master-prompts")
        self.assertIsNotNone(script)
        self.assertTrue(script.exists())
        self.assertIn("prompts", nf.SUBCOMMANDS)
        self.assertTrue(nf.subcommand_script("prompts").exists())
        self.assertIn("muse-pack", nf.SUBCOMMANDS)
        self.assertTrue(nf.subcommand_script("muse-pack").exists())
        self.assertTrue(callable(nf.cmd_prepare))

    def test_bat_dispatches_prepare(self):
        bat = (NF_ROOT / "novelfactory.bat").read_text(encoding="utf-8", errors="replace")
        self.assertIn('"%CMD%"=="prepare"', bat)
        self.assertIn("nf_core.py\" prepare", bat)

    def test_bat_dispatches_muse_pack(self):
        bat = (NF_ROOT / "novelfactory.bat").read_text(encoding="utf-8", errors="replace")
        self.assertIn('"%CMD%"=="muse-pack"', bat)
        self.assertIn("05_export_muse_method_pack.py", bat)

    def test_bat_propagates_errors(self):
        bat = (NF_ROOT / "novelfactory.bat").read_text(encoding="utf-8", errors="replace")
        self.assertIn("if errorlevel 1", bat)
        self.assertIn(":INGEST_RUN", bat)


if __name__ == "__main__":
    unittest.main(verbosity=2)

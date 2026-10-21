# Viral UX 4-Step Dashboard + Copy/Paste Prompts — novel_factory

## Objective
Make the full production flow operable from the HTML dashboard with zero prompt editing:
4 numbered steps, separate 16:9/9:16 Muse AI prompts, no `[ADJUNTAR...]` placeholders,
and the six proven LATAM -> USA viral structures preloaded.

## Problem
The generated artifacts still contain attachment instructions inside the copyable prompt,
the dashboard exposes a flat set of panels instead of a guided flow, the Muse buttons copy
only the final command (not the full minute script), and `01_story_to_master_json.py` does
not use the LATAM catalog.

## Why
The operator must be able to copy/paste each block without guessing which image to attach or
which format to choose, and every new story must start from a proven +500K-view structure.

## Scope (authorized)
- `config/showrunner_rules.json`
- `generators/master_prompts_library.py`
- `generators/01_story_to_master_json.py`
- `generators/02_export_chatgpt_queue.py`
- `generators/05_export_muse_method_pack.py`
- `automation/dashboard.py`
- `tests/test_novel_factory.py`
- generated artifacts under `projects/demo_contract` and `projects/the_ranch_maid_heiress`
- `odd/tasks/viral_ux_4_steps.md`

## Out of scope
- No changes to the 60x10s format, assembler, publisher or 9:16 teaser logic.
- No paid APIs, network calls or new dependencies.

## Constraints
- Cast/storyboard prompts must contain zero `[ADJUNTAR...]` text and must inject real project characters.
- Copyable Muse prompts must contain only the minute script + one final format command.
- Attachment instructions remain visible in the dashboard card, outside the copied text.
- Legacy Google Flow/60-scene tools stay hidden in a `<details>` accordion.

## Route declaration
Substantial multi-file feature -> delegated direct (one bounded writer); parent verifies,
regenerates projects, runs `pytest -v` and commits.

## Checklist
- [x] T1 Config: rewrite `viral_latam_to_usa_templates` with the six requested structures.
- [x] T2 Library: shared cast prompt builder, clean 16:9/9:16 prompts, no attach text in prompts.
- [x] T3 Generator 01: inject the LATAM catalog and support `--viral-template`.
- [x] T4 Generators 02/05: export the clean cast/storyboard prompts and split Muse prompts.
- [x] T5 Dashboard: 4 numbered steps, project selector, format selector, 10+10 cards, legacy accordion.
- [x] T6 Tests: prompt cleanliness, split prompts, six templates, dashboard guide.
- [x] T7 Regenerate `demo_contract` and `the_ranch_maid_heiress`; run `pytest -v`.
- [ ] T8 Commit the verified change.

## Acceptance criteria
- `MUSE_PRODUCTION_PACK.json` and `chatgpt_storyboard_grids_queue.json` contain no `[ADJUNTAR`
  and contain the real character names.
- Every batch has `prompt_16x9_youtube` and `prompt_9x16_vertical`; neither contains attachment headers.
- `config/showrunner_rules.json` includes the six `viral_latam_to_usa_templates`.
- Dashboard shows PASO 1..4 with the required buttons, badges, save paths and status indicators.
- `pytest -v` passes.

## Applicable checks
- `python -m compileall -q .`
- `pytest -v`

## Progress / evidence
- T1: `config/showrunner_rules.json` holds exactly 6 `viral_latam_to_usa_templates` with the requested IDs, sources, views and 6-beat structures.
- T2: `master_prompts_library.py` exposes `build_cast_sheet_prompt` and per-format `prompt_16x9_youtube` / `prompt_9x16_vertical`; the generated prompts contain no `[ADJUNTAR`.
- T3: `01_story_to_master_json.py --viral-template <id>` injects the LATAM catalog plus the selected structure block.
- T4: `02` and `05` consume the shared cast prompt; `MUSE_PRODUCTION_PACK.md` lists both formats with save paths `raw_clips/minute_01.mp4` and `raw_clips/minute_01_vertical.mp4`.
- T5: dashboard renders PASO 1–4, project and format selectors, 10 storyboard mini-cards, 10 batch cards, dual save paths/status, assembly command and the closed legacy accordion.
- T6: new tests cover cast prompt cleanliness, split format prompts, six templates, generator 01 catalog injection and dashboard tokens.
- T7: regenerated both projects; `python -m compileall -q automation generators nf_core.py` OK; `pytest -v` -> 78 passed. Server smoke test: `/`, `/p/<slug>/` and a project asset return HTTP 200; inline JS passes `node --check`.
- T8: pending commit.

## Next step
- Commit the verified change and record the commit identity here.

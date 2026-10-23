# V4 Phase 0 - Per-project declared runtime

## Objective
Remove the fixed 10-minute runtime (60 scenes) as the single source of truth and derive
blocks/scenes/validation from each project's declared `target_minutes`.

## Scope
- `config/showrunner_rules.json`: `format_profiles`, beats by fraction, acts without fixed ranges.
- `nf_core.py`: duration helpers, per-project counts, project metadata, beats, and validators.
- `generators/01_story_to_master_json.py`: `--minutes` / `--profile`, dynamic brief and prompt.
- `generators/master_prompts_library.py`, `00`, `02`, `03`, `05`: prompts and counts without a fixed 60.
- `automation/omni_flow_runner.py` and `automation/dashboard.py`: limits and totals from the master.
- `post_production/04_assemble_novel_ffmpeg.py`: text and errors without a fixed duration.
- Tests: legacy 10 min intact; 22-min (132 scenes) and 19-min (114 scenes) fixtures.
- `README.md`: per-project runtime documentation.

## Out of scope
- Phase 1 (long-form `long_form_arc` template and PROMPT_00C).
- Phase 2 (long source map), Phase 3 (USA visual profile), Phase 4 (REEL_CUTS/production_state).

## Task list
- [x] T1 Parameterized config (profiles, beats, acts).
- [x] T2 Duration helpers and project metadata in `nf_core`.
- [x] T3 Normalization/validation by N scenes and N blocks.
- [x] T4 Generator 01 with per-project runtime.
- [x] T5 Runner, dashboard, and generators without 60-scene limits.
- [x] T6 22/19 tests + full suite green.
- [x] T7 Documentation and commit.

## Route
Direct inline: mechanical, coherent changes to files already understood; no writer was
delegated because each edit depended on the phase's accumulated context.

## Verification
- `python -m unittest discover -s tests -v` -> 107 tests OK.
- CLI 01 with `--brief --minutes 22`: `project.json` declares 22 min / 22 blocks / 132 scenes;
  the brief and prompt show cliffhangers 22/44/66/88/110, payoff 131, and hook 132.
- 22-min E2E with a synthetic 132-scene master: 02 (132 prompts, 22 grids),
  03 (132 clips, 22 batches), 05 (23 images, 22 batches), 00 (22 batches), dashboard
  (22 min / 132 scenes), and runner (132 rows) with no references to 60/10.
- `--template` still generates the legacy 60-scene / 10-min fixture and rejects
  `--minutes 22`.

## Acceptance criteria
- `resolve_target_minutes` accepts `youtube_10` (10) and `short_1` (1) profiles; default 22.
- A 132-scene payload with target 22 normalizes/validates with 22 blocks and no count errors.
- A 114-scene payload with target 19 normalizes/validates with 19 blocks and no count errors.
- Legacy 60-scene fixtures still normalize/validate the same way.
- `format_profiles` only declares `scenes_per_block` and `scene_seconds`; it contains no total runtime.

## Checks
- `python -m unittest discover -s tests -v`

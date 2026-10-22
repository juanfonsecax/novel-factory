# Prompt V2 — Speaker shot lock + visual object lock

## Objective
Prevent the Minute 01 class of failures in generated clips: a line spoken by the wrong character, dialogue over inserts/reactions, a story object absent from frame, diegetic text erased, and identity drift from over-specified anchors.

## Scope
- `nf_core.py`: schema v2 derivation, dialogue-to-shot planner, line-ownership validator, object ledger, diegetic text whitelist, variable cuts.
- `config/showrunner_rules.json`, `config/voice_and_style_locks.json`: limits and prompt blocks.
- `generators/01_story_to_master_json.py`: schema/LLM prompt.
- `generators/02_export_chatgpt_queue.py`: scene-only cast references + face crops + text exception.
- `generators/03_export_omni_queue.py`: render speaker lock, mute list, object lock, diegetic text, attachments.
- `generators/05_export_muse_method_pack.py`, `generators/master_prompts_library.py`: same rules in the manual/Muse pack.
- `tests/test_novel_factory.py`: regression coverage.

## Constraints
- Python stdlib only; no network, no paid APIs, no new dependencies.
- Do not touch `USA WHITE` or `Noticias IA automatizado`.
- `--strict` opts into production errors; default validation keeps legacy fixtures green.
- Old masters are repaired in memory by generators, not rewritten on disk.

## Tasks
- [x] T1. Add v2 helpers to `nf_core.py` (dialogue planner, face/insert detection, line ownership, object ledger, diegetic text, variable-cut retiming). Evidence: ranch scenes 1 (two-shot both lines + insert + reaction), 3 (hidden rewrite), 4 (spoken/object/spoken), 5 (CONFESSION exception) verified via `prepare_master_locks`; 87 tests green.
- [x] T2. Integrate v2 normalization into `normalize_master`/`_coerce_dialogue` and add `prepare_master_locks` for read-only derivation. Evidence: `_should_apply_v2` gate skips fixtures without cast; `_coerce_cuts` untouched (planner derives flags).
- [x] T3. Extend `validate_master` with speaker-lock, order, object-lock, cast-cap and diegetic-text rules. Evidence: production mode on ranch master yields 1 genuine data finding (escena 54: Elena says her own name); false positives from `_planting_details` (ledger keys `frame`, `front of the heir`) fixed with guards.
- [x] T4. Update configs and prompt templates (variable cuts, new blocks, corrected negatives). Evidence: `showrunner_rules.json` (`internal_cuts_per_scene` 1-4, `internal_cut_policy`, new `scene_contract`, `per_scene_max_lines` 2) and `voice_and_style_locks.json` (`video_negative` overlay text, omni/muse/flow rules, `timeline_header` 1-4 shots) validated as JSON.
- [x] T5. Update generators 01/02/03/05 and `master_prompts_library.py`. Evidence: 01 prompt/schema now mandates speaker-shot lock, mute list, object in/out, diegetic exception (schema + rules sections); 02 skips the anti-text clause on diegetic scenes and emits `reference_<id>_face.png` attachments; 03 renders DIALOGUE/SILENT tags, PRESENT BUT SILENT, OBJECT LOCK and diegetic clause; Muse command/rows/batches use 1-4 shots, object in/out, silent present and prepared scenes; 05 inherited via shared builders.
- [x] T6. Add regression tests and run the suite. Evidence: `SpeakerShotLockTests` (two-hander, hidden container, silent cuts, reveal interleave, face crops, diegetic clause, self-naming) added; `python -m unittest discover -s tests` -> 94 tests OK.
- [x] T7. Inspect the ranch scenes 1/4/5 generated prompts against the golden examples. Evidence: scene 1 `[00s-06s]` two-shot both lines -> `06s-08s` watch insert -> `08s-10s` Cole reaction; scene 3 hidden bag rewritten ("interior remains in shadow... never show it empty"); scene 4 spoken -> silent watch 2 s -> spoken; scene 5 CONFESSION gets `DIEGETIC TEXT EXCEPTION`; production validation reports only the genuine scene 54 self-naming line.

## Checks
- `python -m unittest discover -s novel_factory/tests -v`
- `python -c "..."` prompt inspection for `projects/the_ranch_maid_heiress` scenes 1, 4, 5.

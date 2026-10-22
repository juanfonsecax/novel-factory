# Narrative Continuity Engine - novel_factory

## Objective
Add a mandatory cause-and-effect continuity engine to the 60x10s master pipeline:
one driving question per 6-scene minute block, a three-field causal ledger per scene,
canonical key-object locking, anti-ping-pong location checks, and rejection of
mechanical camera placeholders. Rewrite minute 1 of `the_ranch_maid_heiress` around
the planted-watch trap and regenerate both project packs.

## Problem
The masters contained camera placeholders (`hard cut to the reaction as the line lands`,
`the room falls quiet around it`) and no enforceable scene-to-scene causal chain. The
ranch opening used a different theft (shattered decanter) from the rest of the episode,
the demo contract had 60 placeholder reaction cuts, and Muse grids allowed rendered text
plus an unwanted scar on the protagonist.

## Why
The showrunner needs auditable continuity before image/video generation. A prompt-only
rule cannot prevent a model from returning disconnected scenes; the normalizer must
repair the ledger and the validator must reject mechanical cuts.

## Scope (authorized)
- `nf_core.py`, `config/showrunner_rules.json`
- `generators/00..05`, `generators/master_prompts_library.py`
- `projects/the_ranch_maid_heiress/*`, `projects/demo_contract/*`
- `tests/test_novel_factory.py`, this task card

## Constraints
- 60 scenes x 10 s = 600 s; US English; stdlib + local ffmpeg only.
- Do not rewrite scenes 7-60 of the ranch; only minute 1 changes.
- Keep existing prompt test literals and avoid unfilled placeholders.
- TDD: existing unittest suite is the regression gate; no new framework.

## Route declaration
Substantial feature -> direct inline for the already-mapped core and prompt edits.
No delegation: edits are localized and the repository was mapped before implementation.

## Checklist
- [x] T1 Config: add `narrative_continuity_engine` (10 blocks x 6 scenes, rules 1-5)
      and raise total dialogue cap to 20 words while keeping 15 words per line.
- [x] T2 `nf_core`: detect and replace mechanical placeholders; scene-aware cut fallback;
      canonical key object in Shot 1; synthesize/normalize the causal ledger; build
      `narrative_continuity.minute_blocks`; validate missing fields, placeholder text,
      exact chain links, key-object use, block coverage, question length, and ping-pong.
- [x] T3 `01`: add the continuity prompt block and schema fields, including
      `narrative_continuity.minute_blocks`.
- [x] T4 `master_prompts_library`: inject the continuity rule into PROMPT 000/001/003;
      make PROMPT 001 grids 100% visual; add frontal close-up rules and Muse negative rules.
- [x] T5 `02`: append the exact 100% visual grid instruction (propagates to `05`).
- [x] T6 Ranch master: replace scenes 1-6 with the planted-watch trap; add 10 authored
      block questions; remove Elena's scar; normalize placeholders in scenes 7-60.
- [x] T7 Demo master: add 10 block questions; normalize all 60 placeholder reactions;
      keep the existing story.
- [x] T8 Regenerate 00-05 for both projects and verify no mechanical placeholder remains.
- [x] T9 Tests: continuity fields/blocks, missing-field error, placeholder error,
      ping-pong warning/strict error, prompt rule injection, Muse negatives, visual grids,
      demo placeholder-free master.
- [x] T10 Demo scenes 37-39: unify the interior beat under `Hale lighthouse` so the
      location sequence is A-A-A instead of A-B-A; regenerate the demo packs.

## Verification evidence
- `python -m pytest -q` -> `87 passed`.
- `nf.validate_master` -> ranch: 0 errors / 0 warnings; demo: 0 errors / 0 warnings.
- `nf.validate_master(production=True)` -> ranch and demo: 0 errors / 0 warnings.
- Ranch cuts: 180 unique actions, 0 placeholders. Demo cuts: 166 unique actions, 0 placeholders.
- Generated Muse batches: 10 per project, both 16:9 and 9:16 commands carry the exact
  negative rule. Generated grid queues: 10 per project carry the 100% visual rule.
- Generated scene 1 prompt uses the stable aisle, canvas work bag, and no scar.

## Next step
No implementation pending. Commit and push the demo location fix and regenerated packs.

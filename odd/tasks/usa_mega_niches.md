# USA Mega-Niches — novel_factory

## Objective
Add the six highest-RPM US short-drama archetypes as a selectable catalog for PROMPT 000
in `config/showrunner_rules.json`, `generators/00_export_master_workflow_prompts.py` and
`automation/dashboard.py`, keeping the 11-image ChatGPT + 10-minute Muse AI workflow intact.

## Problem
PROMPT 000 only accepts the free-form project premise. The user cannot switch between
proven US mega-niches, so batch output risks repeating one story engine.

## Why
Higher RPM and retention depend on testing distinct proven archetypes: CEO/divorce,
heartland ranch, VIP karma, family inheritance, high-society revenge and veteran homecoming.

## Scope (authorized)
- `config/showrunner_rules.json`
- `generators/master_prompts_library.py`
- `generators/00_export_master_workflow_prompts.py`
- `automation/dashboard.py`
- `tests/test_novel_factory.py`
- `odd/tasks/usa_mega_niches.md`

## Out of scope (hard constraint)
- No changes to the 60x10s format, Muse batches, assembler or publisher.
- No paid APIs, no network, no new dependencies.

## Constraints
- Prompt 000 literal header/body must remain unchanged; the niche block is appended at render time.
- Catalog ids must match exactly the six requested keys.
- English story output, native US English.

## Route declaration
Substantial multi-file feature -> one bounded writer (delegated direct); parent verifies diff,
runs `pytest -v` and performs a spot check.

## Checklist
- [x] T1 config: `viral_story_templates` catalog with six US mega-niches (ids, labels,
      categories, premise seeds, beats, locations, visual signature).
- [x] T2 library: load/list/get templates; render niche block; `build_prompt_pack(..., niche=)`.
- [x] T3 exporter 00: `--niche/--archetype` and `--list-niches`; niche included in exported PROMPT 000.
- [x] T4 dashboard: expose catalog in state; `niche-select` selector; effective PROMPT 000 in
      card, copy, download and copy-all actions.
- [x] T5 tests: catalog count/ids, prompt 000 variant, workflow export and dashboard state.
- [x] T6 Verify `pytest -v` green.

## Acceptance criteria
- Selecting any of the six ids produces a PROMPT 000 containing its archetype block and no unfilled placeholders.
- Dashboard selector alternates the six templates and copies/downloads the selected variant.
- Exporter 00 accepts a niche and writes the variant into `MASTER_WORKFLOW_PROMPTS_READY.md`.
- All tests pass.

## Applicable checks
- `pytest -v`
- `python -m compileall -q .`

## Progress / evidence
- T1-T5 done. `python -m compileall -q .` clean.
- `python -m pytest -v`: 71 passed in 2.34s.
- Manual check: all six ids render PROMPT 000 with no unfilled placeholders and the
  `USA MEGA-NICHE ARCHETYPE` block; `--list-niches` lists the six in order.

## Next step
- Task complete. Pending: user decision on commit/push.

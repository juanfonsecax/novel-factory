# Dashboard Object Lock and English Migration

## Objective
Fix the object-lock data source, replace Eleanor's placeholder identity anchor, correct
single-character look targets, migrate every Novel Factory-owned human-readable string to
English, regenerate all project artifacts, and leave the full test suite green.

## Problem
- `key_object`/`object_start`/`object_end` were derived from cut-description prose, producing
  values such as `sharp` and `the foreground`.
- Generated prompts and dashboard labels are still in Spanish.
- Eleanor's anchor falls back to `hair as shown in the reference sheet`.
- Single-character scenes describe the subject looking at a person who is not in the scene.

## Scope
- `nf_core.py` object resolution, validation, anchor construction, recipient resolution.
- `generators/master_prompts_library.py` prompts and final Muse command.
- `automation/dashboard.py` UI and CLI text.
- Generator scripts, post-production scripts, config descriptions, README, docs, tests.
- `projects/the_christmas_letters` master cleanup and all project exports/dashboards.

## Constraints
- Do not rename identifiers, files, JSON keys, or project slugs.
- Do not rewrite story content or dialogue.
- Never derive object lock fields from cut prose.
- Keep one commit and push to `main` as requested.

## Tasks
- [x] T1 Diagnose and fix object source in normalizer/exporter.
- [x] T2 Add concrete-object validation and regression test.
- [x] T3 Clean the Christmas master and regenerate derived fields.
- [x] T4 Control-check ranch and demo object values.
- [x] T5 Fix Eleanor anchor at the cast source.
- [x] T6 Fix single-character recipient/look-target generation.
- [x] T7 Translate generator prompts and FINAL COMMAND.
- [x] T8 Translate dashboard UI and CLI/system messages.
- [x] T9 Translate repository docs, comments, config text, and tests.
- [x] T10 Regenerate packs and dashboards for all three projects.
- [x] T11 Run language inventory and test suite; report exceptions.
- [x] T12 Commit and push to main.

## Checks
- `python -m unittest discover -s tests`
- `validate_master(..., production=True)` on `the_christmas_letters`
- ripgrep checks for `Key Object: the foreground`, `key_object: "sharp"`, old Spanish
  FINAL COMMAND, and Spanish labels in generated outputs.

## Progress
- Root cause fixed in `nf_core.py`: `_planting_details` no longer parses cut prose;
  `extract_key_object` accepts only explicit scene fields or a declared ledger;
  `_apply_object_ledger` canonicalizes valid values and scrubs prose fragments.
- Validation now rejects blacklisted, conjugated, and over-six-word object values.
  Regression tests cover the prose source, invalid values, solo look targets, and the
  real Eleanor anchor.
- Christmas master cleaned to 132 scenes and validates in production mode with
  0 errors / 0 warnings. Scene 13 is `the delivery slip`, scene 24 is
  `the crystal star ornament`, and scene 79 is `the red cookie tin`.
- Anchor fallback now uses real descriptors; Eleanor resolves to `silver hair in a
  chignon`. Recipient resolution returns only cast present in the scene, with an empty
  target for solo scenes.
- All generator prompts, wrappers, pack labels, reports, CLI/help text, comments,
  README/docs, and dashboard UI are English. The FINAL COMMAND matches the required
  English text.
- All three projects re-exported; dashboards regenerated. Demo publish-pack and
  storyboard README artifacts were rebuilt so no stale Spanish labels remain.
- Language inventory: no Spanish labels or accents remain in Novel Factory-owned
  source, docs, or generated outputs after fixes.
- Exact English FINAL COMMAND is present in 34 generated files; the required prefix is
  present in the Christmas Muse queue.
- Verification greps: 0 `Key Object: the foreground`, 0 `key_object: "sharp"`,
  0 old Spanish FINAL COMMAND, and 0 forbidden dashboard labels.
- Full suite: `Ran 116 tests ... OK`. `novelfactory.bat validate the_christmas_letters`
  exits 0. Christmas production validation is 0 errors / 0 warnings.
- Control check (report only, per mission): `the_ranch_maid_heiress` has 10 legacy
  prose `key_object` values; `demo_contract` has 0 object errors and 13 production
  look-target errors for absent cast. Their masters were not rewritten.

## Exceptions
- `post_production/05_export_to_publisher.py` keeps the external USA WHITE schema and
  CLI contract: `personaje`, `cola/pendientes`, `pendiente_aprobacion`, `proyecto`,
  `archivo_media`, `--personaje`, `--publicar-siguiente`, `--seco`, `estado`, and
  `plataformas`. These are interface names, not UI copy.
- `config/showrunner_rules.json` and the Christmas dialogue keep the French word
  `fiancé` / `fiancée`; the accents are not Spanish.
- `projects/the_ranch_maid_heiress/idea_input.md`, `llm_prompt.md`, and
  `story_brief.md` keep the user-supplied Spanish premise and character notes. This is
  source story material, not Novel Factory UI copy, so it was preserved.
- `projects/the_christmas_letters/story_brief.md` keeps the quoted source title
  `La Lavandera del Rancho`.
- Test fixtures keep intentional Unicode and source-preservation inputs such as
  `Corazón Roto`, `Escena 1: El gancho de la herencia...`, and `sin json aquí`.
- The Christmas master keeps its existing English story/dialogue, including the two
  intentional `library where Eleanor` continuity references.

## Next Step
None. Ship as the single requested commit on `main`.

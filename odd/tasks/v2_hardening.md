# V2.0 Hardening — novel_factory

## Objective
Ship the V2.0 hardening plan (7 patches) inside `novel_factory` only: identity/references,
dialogue-to-shot sync, continuity spoiler filtering, parts/merge/IDs, exact duration +
punch-ins + audio, hybrid teaser with captions, import-frames/watch, publisher idempotency,
plus tests and docs.

## Problem
The generated 60x10s master had: duplicated/truncated scene prompts, no character
references wired into prompts, "same woman" identity drift, future-scene continuity
spoilers leaking into clips, over-budget dialogue (up to 30 words for 10s), non-exact
clip durations (head trim up to 2.5s), punch-ins ignoring the head offset, un-ducked
music, no burned teaser captions, unsafe publisher idempotency (JSON OR media -> skip),
and no way to import existing frames.

## Why
Downstream Omni/ffmpeg pipeline needs deterministic, production-safe inputs so the
600s master assembles exactly and teasers publish idempotently.

## Scope (authorized)
- `nf_core.py`, `config/*.json`
- `generators/01..03`
- `automation/omni_flow_runner.py`
- `post_production/04..05`
- `novelfactory.bat`, `tests/test_novel_factory.py`, `README.md`

## Out of scope (hard constraint)
- Never modify/touch `USA WHITE` or `Noticias IA automatizado`. Publisher integration is
  files-only (`cola/pendientes`). Python stdlib + local ffmpeg/ffprobe only.

## Constraints
- 60 scenes x 10s = 600s master 16:9; 3 teasers 9:16 (scenes 1-6, 21-26, 55-60); US English.
- TDD: disabled (stdlib `unittest` regression suite run per task).
- No paid APIs, no network, no new deps.

## Route declaration
Substantial feature -> direct inline for already-understood mechanical edits; single writer.
Delegation not used because edits are localized and the code was already mapped.

## Checklist
- [x] T0 nf_core: slugify CJK-safe; speech/budget constants; cast/speaker/continuity helpers;
      normalize_master preserves ids + continuity split + canonical characters;
      validate_master strict content checks; merge_payloads sort/dedupe/preserve ids.
- [x] T1 config: showrunner budget+speech keys; style exact duration + hybrid teaser keys.
- [x] T2 gen01: demo truncation fix + demo character refs; prompt budget/identity/continuity
      rules; parts `1of3/2of3/3of3`; delegate to `nf.merge_payloads`; `--strict`.
- [x] T3 gen02: cast prefix per scene, reference filenames, thumbnail sheet, strict check.
- [x] T4 gen03: `_timeline_block` + spoiler-filtered continuity.
- [x] T5 runner: `import-frames`, deterministic watch mapping, safer assign.
- [x] T6 asm04: exact duration (clip normalizado a EXACTAMENTE 10.0s con `tpad`/`apad`),
      punch-ins sobre el clip ya recortado, audio ducking (`sidechaincompress`),
      teaser híbrido (fondo blur + foreground `teaser_foreground_width_ratio`) + captions
      quemadas (fallback sin libass).
- [x] T7 pub05: `enqueue_item` atómico (`.part-*` + `os.replace`) e idempotente
      (completo=omite, parcial=repara, `--force`=reemplaza), `verify_media(strict)`,
      `validate_post`; `--strict` aborta teasers inválidos.
- [x] T8 bat dispatcher `import-frames` + error propagation; tests; README/docs.
- [x] T9 Full run: compileall + unittest green; demo_contract re-ensamblado
      (`--limit 12 --force`): escenas normalizadas = 10.000 s exactos, teaser_01
      1080x1920 con captions, master 120.02 s.

## Acceptance criteria
- `python -m compileall -q .` clean; `python -m unittest discover -s tests` green.
- Demo master validates with `production=True` (no errors).
- Exact-duration assembly verified on demo_contract (scene 1 == 10.00s within 0.05s).
- Publisher enqueue is idempotent (re-run creates no duplicates).

## Applicable checks
- `python -m compileall -q .`
- `python -m unittest discover -s tests -v`

## Progress / evidence
- T0-T9 done; 36/36 tests pass (`python -m unittest discover -s tests`).
- Demo validates with `production=True` (0 errors, 0 warnings).
- Evidence demo_contract: scene_001..003 = 10.000 s; tea. teaser_01 1080x1920/60.1s;
  master_16x9 = 120.02 s (12 escenas).
- Baseline HEAD 556d8ae (origin/main), branch main.

## Next step
- Plan completo (T0-T9). Pendiente: commit de los cambios (autorización del usuario).

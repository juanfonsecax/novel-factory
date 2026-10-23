# V4 Fase 0 — Duración declarada por proyecto

## Objective
Eliminar la duración fija de 10 minutos (60 escenas) como verdad única y derivar
bloques/escenas/validación de `target_minutes` declarado por cada proyecto.

## Scope
- `config/showrunner_rules.json`: `format_profiles`, beats por fracción, actos sin rangos fijos.
- `nf_core.py`: helpers de duración, conteo por proyecto, meta de proyecto, beats y validadores.
- `generators/01_story_to_master_json.py`: `--minutes` / `--profile`, brief y prompt dinámicos.
- `generators/master_prompts_library.py`, `00`, `02`, `03`, `05`: prompts y conteos sin 60 fijo.
- `automation/omni_flow_runner.py` y `automation/dashboard.py`: límites y totales desde el maestro.
- `post_production/04_assemble_novel_ffmpeg.py`: textos y errores sin duración fija.
- Tests: legacy 10 min intacto; fixtures de 22 min (132 escenas) y 19 min (114 escenas).
- `README.md`: documentación de la duración por proyecto.

## Out of scope
- Fase 1 (plantilla de arco largo `long_form_arc` y PROMPT_00C).
- Fase 2 (source map largo), Fase 3 (perfil visual USA), Fase 4 (REEL_CUTS/production_state).

## Task list
- [x] T1 Config paramétrica (profiles, beats, acts).
- [x] T2 Helpers de duración y meta de proyecto en `nf_core`.
- [x] T3 Normalización/validación por N escenas y N bloques.
- [x] T4 Generator 01 con duración por proyecto.
- [x] T5 Runner, dashboard y generadores sin límites de 60.
- [x] T6 Tests 22/19 + suite completa verde.
- [x] T7 Documentación y commit.

## Route
Directo inline: cambios mecánicos y coherentes sobre archivos ya entendidos; no se
delegó escritor porque cada edición dependía del contexto acumulado de la fase.

## Verification
- `python -m unittest discover -s tests -v` → 107 tests OK.
- CLI 01 con `--brief --minutes 22`: `project.json` declara 22 min / 22 bloques / 132 escenas;
  brief y prompt muestran cliffhangers 22/44/66/88/110, payoff 131 y hook 132.
- E2E 22 min con maestro sintético de 132 escenas: 02 (132 prompts, 22 grids),
  03 (132 clips, 22 lotes), 05 (23 imágenes, 22 lotes), 00 (22 lotes), dashboard
  (22 min / 132 escenas) y runner (132 filas) sin referencias a 60/10.
- `--template` sigue generando el fixture legacy de 60 escenas / 10 min y rechaza
  `--minutes 22`.

## Acceptance criteria
- `resolve_target_minutes` acepta perfiles `youtube_10` (10) y `short_1` (1), default 22.
- Un payload de 132 escenas con target 22 normaliza/valida con 22 bloques y sin errores de conteo.
- Un payload de 114 escenas con target 19 normaliza/valida con 19 bloques y sin errores de conteo.
- Los fixtures legacy de 60 escenas siguen normalizando/validando igual.
- `format_profiles` solo declara `scenes_per_block` y `scene_seconds`; no contiene duración total.

## Checks
- `python -m unittest discover -s tests -v`

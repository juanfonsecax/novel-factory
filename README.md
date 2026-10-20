# novel_factory — Novelas IA en formato 60 × 10 s (10 min por episodio)

Módulo **autónomo, local y auditable** para producir episodios de novela corta
("short-drama") en inglés nativo de EE. UU.: **60 escenas de 10 s = 10 minutos**,
con máster **16:9** para YouTube y **teasers 9:16** (automático de 20 s + 3 de 60 s)
listos para el publicador multicanal existente (`USA WHITE/cola/pendientes`).

- **Cero APIs de pago y cero red**: el guion lo escribe tu LLM en el chat, las
  imágenes vía la cola de ChatGPT y los clips vía **Omni 1.1 Flash** (First Frame,
  10 s, audio nativo). Todo lo demás es **Python estándar + ffmpeg/ffprobe**.
- **No toca el código existente**: la integración con `USA WHITE` es **por archivos**
  (JSON + MP4 en su cola). Nada de imports cruzados ni dependencias.
- **Auditable**: JSON legible, rutas explícitas, reanudable (no repite trabajo),
  tests offline incluidos.

---

## 1. El método: "Single First-Frame + Internal Multi-Cut 10 s"

Cada escena se genera como **un único clip de 10 s** a partir de **un único
primer fotograma** (First Frame), pero **dentro** de esos 10 s el guion define
**2-4 cortes de cámara internos** (wide → medium → close-up...). Resultado:

| Ventaja | Por qué importa |
|---|---|
| 1 frame + 1 clip por escena | 60 generaciones de imagen + 60 generaciones de vídeo: el mínimo posible |
| Cortes internos en el prompt | El clip no se ve "de una sola toma": ritmo de serie, no de presentación |
| 10 s con audio nativo | Diálogo con lip-sync real, sin TTS externo ni APIs de voz |
| Máster 16:9 | YouTube largo (mejor retención y monetización que solo Shorts) |
| Teaser 9:16 (center-crop) | Los prompts de imagen ya piden composición centrada: el recorte vertical funciona sin re-render |

El ensamblador además **recorta segundos muertos** (silencio al inicio/final detectado
con `silencedetect`), mezcla BGM local y normaliza a **-14 LUFS**.

---

## 2. Requisitos

- **Python 3.10+** (probado con 3.12). Solo biblioteca estándar.
- **ffmpeg + ffprobe** en el PATH (probado con la build Gyan 8.x).
  Si falta: `winget install Gyan.FFmpeg`
- Windows (probado), Linux/macOS deberían funcionar igual (rutas y fuentes se autodetectan).

---

## 3. Estructura

```
novel_factory/
├─ novelfactory.bat            Lanzador de todos los comandos (Windows)
├─ nf_core.py                  Núcleo compartido (rutas, validación, ffmpeg, JSON atómico)
├─ config/
│  ├─ showrunner_rules.json    Reglas dramáticas: 6 actos, beats, retención, teasers, compliance
│  └─ voice_and_style_locks.json  Bloqueos visuales/voz/prompts y parámetros de postproducción
├─ generators/
│  ├─ 00_export_master_workflow_prompts.py  Workflow 000-003 en un .md + lotes Muse AI de 1 min
│  ├─ 01_story_to_master_json.py  Brief + prompt-pack para tu LLM + ingesta + demo
│  ├─ 02_export_chatgpt_queue.py  Cola de 60 prompts de imagen (ChatGPT) + verificación de frames
│  ├─ 03_export_omni_queue.py     Cola de 60 prompts de vídeo (Omni / Muse AI / Google Flow)
│  ├─ 04_export_master_prompts.py Exporta los 4 prompts maestros rellenados
│  └─ master_prompts_library.py   PROMPT 000-003 (historia, guion, grids, video por lotes)
├─ automation/
│  ├─ omni_flow_runner.py      status · queue · assisted · watch (Descargas) · import-frames
│  └─ dashboard.py             Dashboard local: copiar prompts, ver progreso y tracking
├─ post_production/
│  ├─ 04_assemble_novel_ffmpeg.py   Máster 16:9 (escenas o lotes Muse AI) + teaser 20 s 9:16 + SRT + pack + report
│  └─ 05_export_to_publisher.py     Exporta teasers a USA WHITE/cola/pendientes
├─ music/                      BGM local (ver music/README.md)
├─ assets/fonts/               TTF opcional para el headline de los teasers
├─ tests/test_novel_factory.py 61 tests offline (unittest)
└─ projects/
   └─ <episodio>/
      ├─ story_brief.md              Premisa + reglas (para ti)
      ├─ llm_prompt.md               Prompt-pack para pegar en tu LLM
      ├─ master_episode.json         Guion maestro (60 escenas, fuente de todo)
      ├─ chatgpt_image_prompts_queue.{txt,json,md}
      ├─ chatgpt_reference_sheets.txt  PASO 0: hoja de referencia por personaje
      ├─ MASTER_PROMPTS.md · .txt · master_prompts.json · prompts/
      ├─ MASTER_WORKFLOW_PROMPTS_READY.md      Workflow 000-003 rellenado + variante 9:16
      ├─ chatgpt_prompt_001_storyboards.txt    PROMPT 001 completo (60 escenas + 10 grids 3x2, sin truncar)
      ├─ chatgpt_prompt_002_characters.txt     PROMPT 002 literal (hoja de personajes)
      ├─ chatgpt_storyboard_grids_queue.{txt,json}  Cola de 11 imágenes: REF_CAST_MASTER + REF_GRID_MIN_01…10
      ├─ muse_ai_batches_queue.{txt,json}      Lotes Muse AI de 1 min (6 escenas c/u, adjuntos + 16:9/9:16)
      ├─ omni_video_prompts_queue.{csv,json,txt}
      ├─ muse_ai_video_prompts_queue.{csv,json,txt}
      ├─ google_flow_video_prompts_queue.{csv,json,txt}
      ├─ queue_state.json            Progreso (lo escribe el runner)
      ├─ references/ reference_<id>.png (hojas de referencia de ChatGPT)
      ├─ frames/   frame_001.png … frame_060.png
      ├─ raw_clips/ scene_001.mp4 … scene_060.mp4  (modo A)
      │              o minute_01.mp4 … minute_10.mp4 / batch_01…10.mp4  (modo B, Muse AI)
      └─ output/
         ├─ <slug>_master_16x9_1080p.mp4
         ├─ <slug>_master.srt
         ├─ <slug>_teaser_9x16.mp4        Teaser automático de 20 s (9:16)
         ├─ teaser_01_9x16.mp4 · teaser_02_9x16.mp4 · teaser_03_9x16.mp4  (solo modo A)
         ├─ report.json
         └─ publish_pack/ (título, descripción, tags, capítulos, captions)
```

---

## 4. Flujo completo (orden exacto)

```
 FASE                        COMANDO                                    PRODUCTO
 ─────────────────────────────────────────────────────────────────────────────────────
 1. Guion        novelfactory.bat new mi_episodio --title "..."      story_brief.md
                 (pegar llm_prompt.md en Claude/ChatGPT/Gemini)      llm_prompt.md
                 novelfactory.bat ingest mi_episodio guion.json      master_episode.json
                 novelfactory.bat validate mi_episodio
 2. Frames       novelfactory.bat frames mi_episodio                 cola ChatGPT (60)
                 (ChatGPT genera las imágenes con la referencia      frames/frame_XXX.png
                 del personaje; adjúntalas a la carpeta del proyecto)
 2.5 Dashboard   novelfactory.bat dashboard mi_episodio --serve --open  dashboard.html + tracking
                 (copiar prompts, marcar frames/clips, ver progreso)
 3. Clips        novelfactory.bat omni mi_episodio                   cola Omni (60)
                 novelfactory.bat muse mi_episodio                   cola Muse AI (60)
                 novelfactory.bat flow mi_episodio                   cola Google Flow (60)
                 novelfactory.bat assisted mi_episodio               raw_clips/scene_XXX.mp4
                 (o) novelfactory.bat assisted mi_episodio --platform muse
                 (o) novelfactory.bat watch mi_episodio
                 (o) novelfactory.bat import-frames mi_episodio --frames-src DIR
 3.5 Prompts      novelfactory.bat prompts mi_episodio               MASTER_PROMPTS + prompts/*.txt
                  novelfactory.bat export-master-prompts mi_episodio  WORKFLOW 000-003 + lotes Muse AI
                  novelfactory.bat prepare mi_episodio                workflow 00 + MASTER_PROMPTS 04 sincronizados
 4. Ensamble     novelfactory.bat check mi_episodio                  preflight (sin render)
                  novelfactory.bat assemble mi_episodio               máster + teaser 9:16 + SRT
 5. Publicar     novelfactory.bat publish mi_episodio                plan de exportación
                 novelfactory.bat publish mi_episodio --apply        posts en cola USA WHITE
```

> **Demo de calibración sin LLM ni IA**: `novelfactory.bat demo demo_contract`
> genera un maestro completo (fixture "The Silent Contract") para probar todo el
> pipeline con clips sintéticos antes de gastar esfuerzo creativo.

### 4.1 Guion (01)

- `new <slug>` crea `story_brief.md` + `llm_prompt.md`. El prompt-pack pide al LLM
  **JSON puro** con el esquema exacto (60 escenas, actos, beats, cortes internos,
  diálogo, prompt de imagen, ambience, continuidad).
- `--part 1` / `--part 2` divide la petición en dos mitades (útil con contextos
  pequeños: escenas 1-30 y 31-60); `--ingest` acepta **varios JSON** y los fusiona.
- `--template` (o `demo`) genera el fixture de calibración marcado `demo_fixture: true`.
- `--validate` revisa un maestro existente (errores bloqueantes vs advertencias).
- `--allow-partial` permite ingerir menos de 60 escenas (solo para depurar).
- Tolerancias del ingest: desenvuelve envoltorios (`data`, `episode_json`...),
  extrae JSON de fences Markdown, coacciona diálogo en string y cortes en lista
  de strings, completa teasers y prompts vacíos (con avisos).

### 4.2 Frames (02)

- Exporta `frames.txt` + `frames.json` + fichas `.md`: **un prompt de imagen 16:9
  por escena** con el sufijo/negativo de estilo ya aplicado.
- Reglas inyectadas: composición centrada (recorte 9:16), sin texto/logos, sin
  describir identidad (solo estado transitorio), 20 % de aire arriba para overlay.
- `--check` verifica qué `frame_XXX.png` faltan; `--show 1-3` imprime prompts sueltos.
- **PASO 0 — hojas de referencia (`chatgpt_reference_sheets.txt`)**: una hoja por
  personaje a partir de `characters[].visual_reference` (o `reference_image` si ya
  tienes la imagen). Se generan UNA vez, se guardan en `references/` y se adjuntan
  todas en el mismo hilo de ChatGPT antes de la cola. Así la cara nunca se describe
  en texto: se copia de la referencia (misma filosofía que USA WHITE).
- Flujo ChatGPT: adjunta las hojas de referencia, carga
  `chatgpt_image_prompts_queue.txt`, guarda cada imagen en `frames/` como
  `frame_XXX.png` y verifica con `--check`.

### 4.3 Clips (03 + runner)

- `omni` exporta la cola: `omni_video_prompts_queue.csv` (abre en Excel),
  `...json` (lo consume el runner) y `...txt`. Cada prompt incluye: First Frame,
  plan de cortes internos con tiempos exactos, diálogo con voz/delivery,
  audio bed, movimiento de cámara, continuidad, estilo, reglas y negativos
  (todo determinista desde el maestro, no prosa libre).
- `--only-missing` re-exporta solo escenas sin clip; `--show 1-2` imprime prompts.
- `--platform omni|muse|flow|all`: mismo maestro, tres plantillas de prompt nativas.
  `muse` pide 10 s exactos con audio nativo; `flow` (Veo) asume el tope de 8 s, cierra
  el diálogo antes de 7.5 s y deja que la postproducción extienda a 10 s.
- **Runner** (`automation/omni_flow_runner.py`):
  - `status`: tabla escena a escena (frame/clip/duración) + `queue_state.json`.
  - `queue`: imprime el prompt de la siguiente escena pendiente (scripting).
  - `assisted`: copia el prompt al portapapeles (tkinter), tú lo pegas en Omni,
    pulsas Enter y el runner detecta el clip más reciente en `~/Downloads`,
    valida duración (5-15 s) y lo archiva como `raw_clips/scene_XXX.mp4`.
  - `watch --once` (o continuo): vigila Descargas y archiva automáticamente los
    clips nuevos en orden de escena (espera a que la descarga termine; orden
    natural `clip_2` antes que `clip_10`).
  - `import-frames <slug> --frames-src DIR`: importa frames ya generados
    (`frame_1.png`/`frame_01.png`/`scene_001.png`…) a `frames/`, con
    `--from-scene/--to-scene` para un rango y `--move` para moverlos en vez de copiar.
  - `--platform omni|muse|flow` (en `queue`/`assisted`): elige qué cola consume el
    runner. `assisted` copia el prompt renderizado para esa plataforma.
  - `--playwright-script tu_script.py`: hook opcional a **tu** automatización local
    (recibe `NF_SCENE`, `NF_FRAME`, `NF_PROMPT` por entorno). El módulo **no**
    incluye ni ejecuta automatización de sitios por defecto (los selectores
    cambian y el uso automatizado puede violar sus términos).

### 4.4 Ensamble (04)

`python post_production/04_assemble_novel_ffmpeg.py <proyecto> [opciones]`

| Opción | Efecto |
|---|---|
| `--check` | Preflight: qué falta, sin renderizar nada |
| `--limit N` | Solo las primeras N escenas (pruebas rápidas) |
| `--skip-teasers` / `--no-music` / `--no-srt` | Saltar fases |
| `--music ruta.mp3` | BGM concreta (si no, autodetecta en `music/`) |
| `--punch-ins` | Zoom digital sutil en los cortes internos, alineado con la cabecera recortada |
| `--no-trim` | No recortar silencio de cabecera/cola |
| `--video-fade` | Fade a negro al inicio/fin del máster |
| `--allow-gaps` | Continúa aunque falten clips (marca huecos en `report.json`) |
| `--force` | Recalcula la normalización cacheada |
| `--font ruta.ttf` | Fuente del headline de los teasers |

Detección automática del modo de entrada:
- **Modo A — escenas**: `raw_clips/scene_001.mp4 … scene_060.mp4` (10 s cada una).
- **Modo B — lotes Muse AI**: `raw_clips/minute_01.mp4 … minute_10.mp4` o
  `batch_01.mp4 … batch_10.mp4` (1 min cada uno). Ensambla el máster de 10 min sin
  necesitar clips por escena y mantiene el SRT sincronizado a 600 s.

Pipeline interno: preflight → normalización (1920×1080, 30 fps, AAC 48k, **micro-fade
de audio 0.08 s**; modo A recorta silencio ≤ 0.35 s y fija 10.0 s por escena; modo B
fija 60 s por lote sin recorte; caché reanudable en `output/.work/norm/`) → concat sin
recomprimir → mezcla BGM + fade + **ducking** (`sidechaincompress`) + `loudnorm`
-14 LUFS → `.srt` con tiempos reales → **teaser vertical automático de 20 s**
(`<slug>_teaser_9x16.mp4`, primer gancho → 1080×1920) y, en modo A, 3 teasers 9:16 con
**encaje híbrido** (fondo desenfocado + primer plano centrado) + headline y
**subtítulos quemados** → `publish_pack/` + `report.json`.

> En modo A cada escena dura exactamente `scene_seconds` (10.0 s; tolerancia 0.05 s) y
> en modo B cada lote 60 s, de modo que el máster concatenado mide 600 s exactos.

### 4.5 Publicación (05)

`python post_production/05_export_to_publisher.py <proyecto> [opciones]`

| Opción | Efecto |
|---|---|
| (sin flags) | PLAN: muestra qué copiaría, no escribe nada |
| `--apply` | Copia los teasers + JSON de post a `USA WHITE/cola/pendientes/` |
| `--only 1,3` | Exporta solo esos teasers |
| `--personaje eva_hayes` | Cuenta destino (por defecto, la del maestro) |
| `--publisher-root "C:\...\USA WHITE"` | Ruta explícita si la autodetección falla |
| `--force` | Sobrescribe si ya existe en la cola |
| `--strict` | Aborta el encolado de teasers con problemas de media (resolución/audio) |

La autodetección busca una carpeta con `src/orquestador.py` + `cola/pendientes`
entre los hermanos del workspace. **Con `--publisher-root` nunca hay fallback
silencioso**: si la ruta no es válida, se aborta.

**Encolado atómico e idempotente**: la media se copia a un temporal `.part-*` y se
renombra con `os.replace`, y el JSON se escribe igual; re-ejecutar `--apply` no
duplica nada (un item cuenta como completo solo si existen **ambos** archivos: media
+ JSON). Si falta una parte, el item se **repara** en vez de omitirse.

### 4.6 Dashboard local (copiar y pegar con tracking)

`novelfactory.bat dashboard mi_episodio [--serve] [--open] [--port 8787]`

Genera `projects/<episodio>/dashboard.html`: un tablero autocontenido (sin build, sin
npm, sin red) con los 60 prompts de imagen, los 60 prompts de vídeo, las hojas de
referencia y el guion. Sirve para el trabajo manual de copiar/pegar en ChatGPT y Omni
sin abrir los JSON.

- **Tabs**: Referencias · Frames (imagen) · Clips (video) · Guion · **Prompts maestros**.
- **Plataforma de video**: selector en la barra de filtros (Omni / Muse AI / Google
  Flow); cambia el prompt de cada escena y el texto copiado, sin regenerar el HTML.
- **Prompts maestros**: los 4 prompts (000-003) rellenados con los valores del
  proyecto, con botones de copiar uno, copiar los 4, descargar `.txt` y JSON, y
  acceso rápido por prompt.
- **Lotes Muse AI**: bloques de 1 minuto (6 escenas) con adjuntos
  (`REF_CAST_MASTER.png` + `REF_GRID_MIN_XX.png`), cortes de cámara, SFX, diálogo y
  dos comandos finales (horizontal 16:9 / vertical 9:16), cada uno con copiar y descargar.
- **Cola de 11 imágenes**: botón para copiar/descargar la cola completa
  (`REF_CAST_MASTER.png` + 10 storyboards `3x2`), lista para pegar en ChatGPT.
- **Copiar prompt**: botón por escena; marca la escena como "copiada".
- **Marcar hecho**: tracking manual separado del disco. Si `frames/frame_XXX.png` o
  `raw_clips/scene_XXX.mp4` ya existen, el dashboard lo detecta solo y muestra
  "Archivo en disco" (no hay que marcarlo a mano).
- **Filtros**: búsqueda por lugar/beat/diálogo/reparto, estado (pendiente, copiado,
  hecho), acto, portadas de teaser y "ocultar hechos".
- **Copiar siguiente pendiente**: toma la primera escena sin frame/clip de la tab
  activa, copia su prompt y la registra.
- **Progreso**: frames, clips, marcados manuales, referencias y teasers.

Dos modos de persistencia:

| Modo | Comando | Tracking |
|---|---|---|
| Archivo | `dashboard mi_episodio` | `localStorage` del navegador + exportar/importar JSON |
| Servidor local | `dashboard mi_episodio --serve --open` | `projects/<episodio>/dashboard_tracking.json` (atómico, en disco) |

`--serve` levanta solo `127.0.0.1` (sin red externa) y añade `Recargar estado`
para releer `frames/`, `raw_clips/` y `output/` sin regenerar el HTML. El botón
**Exportar tracking** descarga el JSON y **Importar** lo restaura, así el progreso
nunca queda atado a un navegador. Los archivos de media no se tocan.

> Si regeneras `master_episode.json`, vuelve a ejecutar `dashboard` para refrescar
> los prompts embebidos; el tracking existente se conserva.

### 4.7 Prompts maestros (000–003)

La librería `generators/master_prompts_library.py` contiene los cuatro prompts de
producción encadenados y los rellena con los valores reales del episodio:

| Prompt | Para qué sirve | Salida esperada |
|---|---|---|
| **000** Arquitecto de historias virales | Convierte tu idea en título, elenco y sinopsis por bloques | Texto que alimenta al 001 |
| **001** Guionista de micro-dramas | Desglose técnico de 60 escenas × 10 s con JSON exacto | `master_episode.json` (vía `ingest`) |
| **002** Arquitecto de grids de imagen | Plan de contact sheets por minuto (6 paneles) para las imágenes | Grids/frames para ChatGPT |
| **003** Director de video por lotes | Flujo Muse AI + Google Flow con reglas de plataforma | Clips `scene_XXX.mp4` |

- Se generan solos al crear/plantilla/ingerir (`01` los exporta), y también a mano:
  `novelfactory.bat prompts mi_episodio` → `MASTER_PROMPTS.md` + `.txt` + `prompts/*.txt`.
- **Relleno literal**: los marcadores (`{story_idea}`, `{duration_minutes}`,
  `{total_scenes}`, `{total_grid_images}`, `{visual_style}`, `{aspect_ratio}`) se
  sustituyen por reemplazo de texto, así los ejemplos JSON de los prompts nunca se rompen.
- El **PROMPT 000** conserva el texto original íntegro (cabecera 🧠 incluida).

---

## 5. Informe de auditoría del workspace (por qué esta integración)

### 5.1 ¿Dónde está el módulo de edición y qué entradas recibe?

| Proyecto | Módulo | Entrada → Salida |
|---|---|---|
| **USA WHITE** | `src/final_video_pipeline.py` (orquestado por `auto_runner.py`) | `inbox_raw/<personaje>/` (frames/clips) → vídeo final **1080×1920 / 6 s** (180 frames) con subtítulos y copy → `output_final/` → `--export-to-cola <job>` |
| **NOTICIAS IA AUTOMATIZADO** | `compose.py` + Whisper | noticias → vertical 1080×1920 30 fps con subtítulos `.ass` |
| **NEW YOUTUBE** | (vacío) | — |

Conclusión: los pipelines existentes editan **verticales cortos (6-60 s)** para
Reels/Shorts. Un episodio de 10 minutos en **16:9** con SRT, capítulos y teasers
derivados no entra en ellos sin reescribirlos. De ahí que `novel_factory` traiga su
propio ensamblador (04) con el mismo lenguaje técnico (ffmpeg, H.264/AAC, loudnorm).

### 5.2 ¿Dónde está el módulo de publicación y cómo se dispara?

- **`USA WHITE/src/orquestador.py`** publica el post más antiguo de
  `cola/pendientes/` a Instagram (Graph API), Facebook, TikTok (worker con cookies
  propias) y YouTube **Shorts** (API), con validación anti-repetición SHA-256
  (`anti_ban.py`), proxy fail-closed y pausas humanas.
- Disparadores: `python src\orquestador.py --publicar-siguiente [--seco]` (manual)
  o el daemon `run_auto.bat` → `src/auto_runner.py --daemon`, que produce, exporta
  jobs READY y publica **por slots de cada personaje** (`posting_schedule_us_est`),
  con **tope diario** (`max_posts_por_dia_por_persona: 2`) y **espaciado mínimo**
  entre publicaciones del mismo día. Los posts se filtran por `personaje_id`
  activo (`automatico.personas_activas`).
- **Límite detectado**: `publicador_youtube.py` solo sube **Shorts** (añade
  `#Shorts` y usa la API de vídeos verticales cortos). El máster de 10 min
  **no** debe encolarse ahí.

### 5.3 ¿Qué scripts/carpetas de prompts o automatización de navegador ya existen?

- USA WHITE: `src/auto_copywriter.py` (copy), `src/frame_prompt.py` +
  `prompts_pendientes/` (prompts de frame inicial con archivo), `compositor.yaml`,
  `config/HEADLINES_PLAYBOOK.md` y `VISUAL_PLAYBOOK.md`, y un **TikTok worker**
  (`tiktok-worker/venv_tiktok` con Playwright local para subir con cookies).
- NOTICIAS IA AUTOMATIZADO: su propio motor vertical con Whisper + `.ass`.
- Patrón del workspace: **todo por carpetas de cola** (`cola/pendientes`,
  `inbox`, `procesados`), con JSON intermedios y validaciones anti-duplicado.

Conclusión: no había ningún sistema de "novela larga por escenas" ni colas de
prompts para generadores First-Frame; el patrón dominante (colas + JSON + worker
de navegador) es exactamente el que sigue `novel_factory` (menos el navegador:
aquí el runner es asistido, no automatizado).

### 5.4 ¿Cómo se conecta `novel_factory` sin romper nada?

1. **Cero imports cruzados**: `novel_factory` solo escribe **archivos** en
   `USA WHITE/cola/pendientes/` con el esquema exacto que ya consume el
   orquestador (ver §6). No se modifica ni una línea de USA WHITE.
2. **El máster largo no se encola**: `publicador_youtube.py` es solo Shorts. El
   máster 16:9 se sube **a mano** con el `publish_pack/` (título, descripción con
   capítulos, tags). Documentado dentro del propio pack.
3. **Los 3 teasers** entran como posts `tipo: "reel"` normales: el daemon los
   reparte por slots y tope diario del personaje elegido; o se publican uno a uno
   con `--publicar-siguiente` (previo `--seco` de prueba).
4. **Anti-duplicado integrado**: 05 no pisa nada existente (salvo `--force`) y los
   `id` (`nf_<slug>_teaser_XX`) permiten reconocerlos en `cola/publicados`/`errores`.
5. **Si mañana cambia USA WHITE**: la única superficie de contacto es el esquema
   del post (5 campos clave) — está aislado en `build_post()` de 05.

---

## 6. Esquema del post encolado (contrato con el publicador)

```json
{
  "id": "nf_the_silent_contract_teaser_01",
  "personaje_id": "emma_hayes",
  "tipo": "reel",
  "fecha_creacion": "2026-10-19T12:32:14-05:00",
  "archivo_media": "nf_the_silent_contract_teaser_01_9x16.mp4",
  "hook": "THE LIGHT WAS NEVER OFF",
  "caption": "…texto del teaser…\n\n#shortdrama #novel …",
  "estado": "pendiente_aprobacion",
  "final_video": true,
  "output_filename": "nf_the_silent_contract_teaser_01_9x16.mp4",
  "plataformas": {"instagram": true, "facebook": true, "tiktok": true, "youtube": true},
  "origen": {"modulo": "novel_factory", "proyecto": "the_silent_contract", "teaser": 1, "escenas": [1,2,3,4,5,6]}
}
```

- El MP4 se copia **junto al JSON** en `cola/pendientes/` (el orquestador busca la
  media ahí o en `procesados/`).
- Publicación de prueba sin publicar nada:
  `cd "USA WHITE" && python src\orquestador.py --publicar-siguiente --seco`

---

## 7. Configuración

### `config/showrunner_rules.json` (reglas dramáticas)

- Formato: 60 escenas × 10 s, 6 actos de 10, 3 teasers de 6 escenas, 18-30 palabras
  de diálogo por escena, 2-4 cortes internos (a 2.5-4 s), máx. 5 personajes y 4
  localizaciones.
- `required_beats`: escenas 1 (hook), 2 (mundo/herida), 10/20/30/40/50 (cliffhangers
  de acto) y 60 (payoff + nuevo hook).
- Cada acto define objetivo, "must_happen", device de retención y punto de dopamina.
- Motor de retención: tipos de open loop, cadencia de dopamina cada 2-3 escenas,
  tipos de cliffhanger y una lista de **prohibiciones** (montaje lento, monólogo del
  villano, resolución por casualidad...).
- Compliance: sin celebridades reales, sin marcas, sin contenido explícito, sin
  violencia gráfica, sin claims médicos/legales, divulgación de IA recomendada.

### `config/voice_and_style_locks.json` (bloqueos de estilo)

- Look fotoreal 35 mm, lista de luces (nunca luz plana de estudio), lenguaje de
  cámara, composición segura para recorte 9:16, rotación de planos por defecto.
- `image_prompt_suffix` / `image_negative` / `video_negative` (se aplican siempre).
- **Identity lock**: las caras vienen de las imágenes de referencia; nunca se
  describe edad, nombre, color de ojos ni pelo base (solo estado transitorio).
- **Voice lock**: arquetipos de voz (protagonista/antagonista/aliado/amor/autoridad),
  velocidad ~2.5 palabras/s, inglés nativo, sin narrador salvo línea explícita.
- Plantillas completas de prompt para Omni, Muse AI (`muse_prompt_template`) y
  Google Flow (`flow_prompt_template`), y los parámetros de postproducción
  (volumen de música, fades, loudness, CRF, recorte de silencio, overlay del teaser).

---

## 8. Tests

```powershell
python -m unittest discover -s novel_factory\tests -v
# o
novel_factory\novelfactory.bat test
```

48 tests offline: núcleo y esquema del maestro, generadores (60 prompts de imagen y
de vídeo por plataforma), librería de prompts maestros (000-003 sin marcadores),
dashboard (estado, render, prompts y tracking), helpers del ensamblador (SRT, escape
del concat, detección de silencio con clips generados al vuelo), exportador
(detección de publicador, post JSON) y runner (cola por plataforma, detección de
descargas, archivado y validación de clips). Los tests que necesitan ffmpeg se saltan
solos si no está instalado.

---

## 9. Decisiones y límites conocidos

- **Sin APIs de pago / sin red.** Nada de ElevenLabs, OpenAI o Vertex. El audio es
  el nativo de Omni; la música es local.
- **Playwright no incluido por diseño** (nunca se clonó ni ejecutó código externo;
  tus cookies y sesiones no se exponen). Existe el hook `--playwright-script` para
  tus propias automatizaciones locales.
- **SRT sin quemar en el máster** (subtítulos como archivo, no hard-subs): evita
  tapar planos y permite subir el .srt a YouTube.
- **Loudnorm de una pasada** (-14 LUFS / TP -1.5 / LRA 11): suficiente para redes;
  dos pasadas queda como mejora opcional.
- **`--punch-ins`** re-encodea cada clip con cortes (más tiempo por episodio);
  desactivado por defecto.
- **El máster largo es manual** en YouTube (limitación real del publicador actual).
- El fixture demo (`demo_contract`) está pensado para probar el pipeline con
  material sintético; bórralo o renómbralo cuando produzcas el primer episodio real.

## 10. Próximos pasos sugeridos

1. Episodio 1 real: `new` → tu LLM → `ingest` → frames → clips → `assemble`.
2. Bajar 2-4 pistas libres a `music/` (ver ideas de mood en `music/README.md`).
3. Prueba `publish` (plan) y luego la publicación en seco del publicador
   (`--publicar-siguiente --seco`) antes del primer envío real.
4. Opcional a futuro: dos pasadas de loudnorm, SRT quemado para teasers,
   variantes de teaser (gancho vs. cliffhanger) y subtítulos bilingües.

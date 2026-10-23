# novel_factory - Long-form AI novels per project (default 22 min)

An **autonomous, local, auditable** module for producing short-drama episodes in
native US English. Each project declares its runtime (**default 22 min = 132
10-second scenes**; legacy 10-min and 1-min profiles are still supported), with a
**16:9** master for YouTube and **9:16 teasers** (one automatic 20-second teaser
plus three 60-second teasers) ready for the existing multi-channel publisher
(`USA WHITE/cola/pendientes`).

- **No paid APIs and no network**: your LLM writes the script in chat, images come
  from the ChatGPT queue, and clips come from **Omni 1.1 Flash** (First Frame,
  10 s, native audio). Everything else is **standard Python + ffmpeg/ffprobe**.
- **Does not touch existing code**: the `USA WHITE` integration is **file-based**
  (JSON + MP4 in its queue). No cross-imports or dependencies.
- **Auditable**: readable JSON, explicit paths, resumable (no repeated work), and
  offline tests included.

---

## 1. The method: "Single First-Frame + Internal Multi-Cut 10 s"

Each scene is generated as **one 10-second clip** from **one first frame**, but
**inside** those 10 seconds the script defines **3 exact camera cuts**
(00s-03s -> 03s-07s -> 07s-10s). The result:

| Benefit | Why it matters |
|---|---|
| 1 frame + 1 clip per scene | One image generation and one video generation per scene: the minimum possible |
| Internal cuts in the prompt | The clip does not look like a single take: series pacing, not a presentation |
| 10 s with native audio | Dialogue with real lip-sync, no external TTS or voice APIs |
| 16:9 master | Long-form YouTube (better retention and monetization than Shorts alone) |
| 9:16 teaser (center crop) | Image prompts already request centered composition, so the vertical crop works without re-rendering |

The assembler also **trims dead seconds** (leading/trailing silence detected with
`silencedetect`), mixes local BGM, and normalizes to **-14 LUFS**.

---

## 2. Requirements

- **Python 3.10+** (tested with 3.12). Standard library only.
- **ffmpeg + ffprobe** on the PATH (tested with the Gyan 8.x build).
  If missing: `winget install Gyan.FFmpeg`
- Windows (tested); Linux/macOS should work the same way (paths and fonts are
  auto-detected).

---

## 3. Structure

```
novel_factory/
  novelfactory.bat            Launcher for every command (Windows)
  nf_core.py                  Shared core (paths, validation, ffmpeg, atomic JSON)
  config/
    showrunner_rules.json     Dramatic rules: 6 acts, beats, retention, teasers, compliance
    voice_and_style_locks.json  Visual/voice/prompt locks and post-production parameters
  generators/
    00_export_master_workflow_prompts.py  Workflow 000-003 in one .md + 1-min Muse AI batches
    01_story_to_master_json.py  Brief + prompt pack for your LLM + ingest + demo
    02_export_chatgpt_queue.py  Image prompt queue (ChatGPT) + frame verification
    03_export_omni_queue.py     Video prompt queue (Omni / Muse AI / Google Flow)
    04_export_master_prompts.py Export the four filled master prompts
    05_export_muse_method_pack.py Pack: cast sheet + grids/batches per block + checklist
    master_prompts_library.py   PROMPT 000-003 (story, script, grids, batch video)
  automation/
    omni_flow_runner.py       status / queue / assisted / watch (Downloads) / import-frames
    dashboard.py              Local dashboard: copy prompts, view progress and tracking
  post_production/
    04_assemble_novel_ffmpeg.py   16:9 master (scenes or Muse AI batches) + 20 s 9:16 teaser + SRT + pack + report
    05_export_to_publisher.py     Export teasers to USA WHITE/cola/pendientes
  music/                      Local BGM (see music/README.md)
  assets/fonts/               Optional TTF for the teaser headline
  tests/test_novel_factory.py 116 offline tests (unittest)
  projects/
    <episode>/
      story_brief.md              Premise + rules (for you)
      llm_prompt.md               Prompt pack to paste into your LLM
      project.json                Declared runtime (target_minutes, blocks, scenes)
      master_episode.json         Master script (scenes from project.json, source of everything)
      chatgpt_image_prompts_queue.{txt,json,md}
      chatgpt_reference_sheets.txt  STEP 0: one reference sheet per character
      MASTER_PROMPTS.md / .txt / master_prompts.json / prompts/
      MASTER_WORKFLOW_PROMPTS_READY.md      Filled workflow 000-003 + 9:16 variant
      chatgpt_prompt_001_storyboards.txt    Full PROMPT 001 (all scenes + one 3x2 grid per block)
      chatgpt_prompt_002_characters.txt     Literal PROMPT 002 (character sheet)
      chatgpt_storyboard_grids_queue.{txt,json}  Image queue: REF_CAST_MASTER + one grid per block
      muse_ai_batches_queue.{txt,json}      1-min Muse AI batches (6 scenes each, attachments + 16:9/9:16)
      MUSE_PRODUCTION_PACK.md / .json       Complete guide to the new method (in order)
      MUSE_CHECKLIST.md                     Image checklist + one video per block
      storyboards/   REF_CAST_MASTER.png ... REF_GRID_MIN_01..NN.png (save images here)
      omni_video_prompts_queue.{csv,json,txt}
      muse_ai_video_prompts_queue.{csv,json,txt}
      google_flow_video_prompts_queue.{csv,json,txt}
      queue_state.json            Progress (written by the runner)
      references/ reference_<id>.png (ChatGPT reference sheets)
      frames/   frame_001.png ... frame_<total_scenes>.png
      raw_clips/ scene_001.mp4 ... scene_<total_scenes>.mp4  (mode A)
                   or minute_01.mp4 ... minute_<total_blocks>.mp4 / batch_01..NN.mp4  (mode B, Muse AI)
      output/
        <slug>_master_16x9_1080p.mp4
        <slug>_master.srt
        <slug>_teaser_9x16.mp4        Automatic 20 s teaser (9:16)
        teaser_01_9x16.mp4 ... teaser_02_9x16.mp4 ... teaser_03_9x16.mp4  (mode A only)
        report.json
        publish_pack/ (title, description, tags, chapters, captions)
```

---

## 4. Full flow (exact order)

```
 STAGE                  COMMAND                                      PRODUCT
 -----------------------------------------------------------------------------------
 1. Script               novelfactory.bat new my_episode --title "..."   story_brief.md
                        (paste llm_prompt.md into Claude/ChatGPT/Gemini) llm_prompt.md
                        novelfactory.bat ingest my_episode script.json  master_episode.json
                        novelfactory.bat validate my_episode
 2. New method           novelfactory.bat prepare my_episode            MUSE_PRODUCTION_PACK.md + queues
                        (ChatGPT: master sheet + one storyboard per block) storyboards/REF_*.png
                        (Muse AI: one 1-minute batch per block)          raw_clips/minute_01..NN.mp4
 2.5 Dashboard           novelfactory.bat dashboard my_episode --serve --open  dashboard.html + tracking
                        (new method only; the previous method lives under "Show legacy method")
 3. Legacy (optional)
                        novelfactory.bat frames my_episode              ChatGPT queue (one per scene)
                        novelfactory.bat omni my_episode                Omni queue (one per scene)
                        novelfactory.bat flow my_episode                Google Flow queue (one per scene)
                        novelfactory.bat assisted my_episode            raw_clips/scene_XXX.mp4
                        (or) novelfactory.bat watch my_episode
                        (or) novelfactory.bat import-frames my_episode --frames-src DIR
 3.5 Prompts            novelfactory.bat prompts my_episode             MASTER_PROMPTS + prompts/*.txt
                        novelfactory.bat export-master-prompts my_episode  WORKFLOW 000-003 + Muse AI batches
                        novelfactory.bat muse-pack my_episode           pack: cast sheet + one grid/batch per block
                        novelfactory.bat prepare my_episode            workflow 00 + 04 + Muse pack 05
 4. Assembly            novelfactory.bat check my_episode               preflight (no render)
                        novelfactory.bat assemble my_episode            master + 9:16 teaser + SRT
 5. Publish             novelfactory.bat publish my_episode             export plan
                        novelfactory.bat publish my_episode --apply     posts queued in USA WHITE
```

> **Calibration demo without an LLM or AI**: `novelfactory.bat demo demo_contract`
> generates a complete master (the "The Silent Contract" fixture) so you can test
> the whole pipeline with synthetic clips before spending creative effort.

### 4.1 Script (01)

- `new <slug>` creates `story_brief.md` + `llm_prompt.md`. The prompt pack asks the
  LLM for **pure JSON** using the exact schema (project scenes, acts, beats,
  internal cuts, dialogue, image prompt, ambience, continuity).
- `--part 1` / `--part 2` splits the request into two halves (useful with small
  contexts); `--part 1of3/2of3/3of3` splits it into thirds. `--ingest` accepts
  **multiple JSON files** and merges them.
- `--template` (or `demo`) generates the calibration fixture marked `demo_fixture: true`.
- `--validate` checks an existing master (blocking errors vs. warnings).
- `--minutes 22` (or `--profile youtube_10|short_1`) sets the runtime when creating
  the project; the default is 22 min. `--allow-partial` allows ingesting fewer
  scenes than declared.
- Ingest tolerances: unwraps envelopes (`data`, `episode_json`, ...), extracts JSON
  from Markdown fences, coerces string dialogue and list cuts, and fills empty
  teasers/prompts (with warnings).

### 4.2 Frames (02)

- Exports `frames.txt` + `frames.json` + `.md` cards: **one 16:9 image prompt per
  scene** with the style suffix/negative already applied.
- Injected rules: centered composition (9:16 crop), no text/logos, no describing
  identity (only transient state), and 20% headroom for overlays.
- `--check` verifies which `frame_XXX.png` files are missing; `--show 1-3` prints
  individual prompts.
- **STEP 0 - reference sheets (`chatgpt_reference_sheets.txt`)**: one sheet per
  character from `characters[].visual_reference` (or `reference_image` if the image
  already exists). Generate them ONCE, save them in `references/`, and attach all of
  them in the same ChatGPT thread before the queue. The face is never described in
  text; it is copied from the reference (the same philosophy as USA WHITE).
- ChatGPT flow: attach the reference sheets, load
  `chatgpt_image_prompts_queue.txt`, save each image in `frames/` as
  `frame_XXX.png`, and verify with `--check`.

### 4.3 Clips (03 + runner)

- `omni` exports the queue: `omni_video_prompts_queue.csv` (opens in Excel),
  `...json` (consumed by the runner), and `...txt`. Each prompt includes: First
  Frame, internal cut plan with exact timings, dialogue with voice/delivery, audio
  bed, camera movement, continuity, style, rules, and negatives (all deterministic
  from the master, not free prose).
- `--only-missing` re-exports only scenes without a clip; `--show 1-2` prints prompts.
- `--platform omni|muse|flow|all`: same master, three native prompt templates.
  `muse` asks for exactly 10 s with native audio; `flow` (Veo) assumes the 8 s cap,
  ends dialogue before 8.5 s, and lets post-production extend to 10 s.
- **Runner** (`automation/omni_flow_runner.py`):
  - `status`: scene-by-scene table (frame/clip/duration) + `queue_state.json`.
  - `queue`: prints the prompt for the next pending scene (scripting).
  - `assisted`: copies the prompt to the clipboard (tkinter), you paste it into Omni,
    press Enter, and the runner detects the most recent clip in `~/Downloads`,
    validates duration (5-15 s), and archives it as `raw_clips/scene_XXX.mp4`.
  - `watch --once` (or continuous): watches Downloads and automatically archives new
    clips in scene order (waits for the download to finish; natural order
    `clip_2` before `clip_10`).
  - `import-frames <slug> --frames-src DIR`: imports already-generated frames
    (`frame_1.png`/`frame_01.png`/`scene_001.png`) into `frames/`, with
    `--from-scene/--to-scene` for a range and `--move` to move instead of copy.
  - `--platform omni|muse|flow` (in `queue`/`assisted`): selects which queue the
    runner consumes. `assisted` copies the prompt rendered for that platform.
  - `--playwright-script your_script.py`: optional hook to **your** local
    automation (receives `NF_SCENE`, `NF_FRAME`, `NF_PROMPT` via the environment).
    The module **does not** include or run site automation by default (selectors
    change and automated use may violate their terms).

### 4.4 Assembly (04)

`python post_production/04_assemble_novel_ffmpeg.py <project> [options]`

| Option | Effect |
|---|---|
| `--check` | Preflight: what is missing, without rendering |
| `--limit N` | Only the first N scenes (quick tests) |
| `--skip-teasers` / `--no-music` / `--no-srt` | Skip phases |
| `--music path.mp3` | Specific BGM (otherwise auto-detects in `music/`) |
| `--punch-ins` | Subtle digital zoom on internal cuts, aligned with the trimmed header |
| `--no-trim` | Do not trim leading/trailing silence |
| `--video-fade` | Fade to black at the start/end of the master |
| `--allow-gaps` | Continue even if clips are missing (marks gaps in `report.json`) |
| `--force` | Recompute the cached normalization |
| `--font path.ttf` | Headline font for the teasers |

Automatic input-mode detection:
- **Mode A - scenes**: `raw_clips/scene_001.mp4 ... scene_<total_scenes>.mp4` (10 s each).
- **Mode B - Muse AI batches**: `raw_clips/minute_01.mp4 ... minute_<total_blocks>.mp4`
  or `batch_01.mp4 ... batch_NN.mp4` (1 min each). Assembles the complete master
  without per-scene clips and keeps the SRT synchronized to the declared runtime.

Internal pipeline: preflight -> normalization (1920x1080, 30 fps, AAC 48k, **0.08 s
audio micro-fade**; mode A trims silence to 0.35 s and fixes each scene at 10.0 s;
mode B fixes each batch at 60 s without trimming; resumable cache in
`output/.work/norm/`) -> concat without re-encoding -> BGM mix + fade + **ducking**
(`sidechaincompress`) + `loudnorm` -14 LUFS -> `.srt` with real timings ->
**automatic 20 s vertical teaser** (`<slug>_teaser_9x16.mp4`, first hook ->
1080x1920) and, in mode A, three 9:16 teasers with a **hybrid fit** (blurred
background + centered foreground) + headline and **burned-in subtitles** ->
`publish_pack/` + `report.json`.

> In mode A each scene lasts exactly `scene_seconds` (10.0 s; tolerance 0.05 s) and
> in mode B each batch lasts 60 s, so the concatenated master measures exactly
> `target_minutes`.

### 4.5 Publishing (05)

`python post_production/05_export_to_publisher.py <project> [options]`

| Option | Effect |
|---|---|
| (no flags) | PLAN: shows what would be copied, writes nothing |
| `--apply` | Copies the teasers + post JSON to `USA WHITE/cola/pendientes/` |
| `--only 1,3` | Exports only those teasers |
| `--personaje eva_hayes` | Destination account (defaults to the master's account) |
| `--publisher-root "C:\...\USA WHITE"` | Explicit path if auto-detection fails |
| `--force` | Overwrites if the item already exists in the queue |
| `--strict` | Aborts queuing teasers with media problems (resolution/audio) |

Auto-detection looks for a folder containing `src/orquestador.py` +
`cola/pendientes` among the workspace siblings. **With `--publisher-root` there is
never a silent fallback**: if the path is invalid, it aborts.

**Atomic, idempotent queuing**: media is copied to a temporary `.part-*` file and
renamed with `os.replace`, and the JSON is written the same way; re-running
`--apply` never duplicates anything (an item counts as complete only when **both**
files exist: media + JSON). If one part is missing, the item is **repaired**
instead of skipped.

### 4.6 Local dashboard (copy and paste with tracking)

`novelfactory.bat dashboard my_episode [--serve] [--open] [--port 8787]`

Generates `projects/<episode>/dashboard.html`: a self-contained board (no build, no
npm, no network) with one image prompt and one video prompt per scene, the reference
sheets, and the script. It supports manual copy/paste into ChatGPT and Omni without
opening the JSON files.

- **Tabs**: **Method and prompts** (default tab) / Script. The previous method
  (References -> Frames -> Clips) is hidden behind the **Show legacy method** button.
- **New methodology**: a 4-step panel with the grid queue, Muse AI batches, and the
  assembly command; it also appears as a banner in the other tabs.
- **Images on disk**: the dashboard reads `storyboards/` and marks each card
  **On disk** or **Pending**; the top bar shows grid and batch progress for the project.
- **Video platform**: selector in the filter bar (Omni / Muse AI / Google Flow);
  changes each scene's prompt and copied text without regenerating the HTML.
- **Master prompts**: the four prompts (000-003) filled with project values, with
  buttons to copy one, copy all four, download `.txt` and JSON, and quick access
  per prompt.
- **Muse AI batches**: 1-minute blocks (6 scenes) with attachments
  (`REF_CAST_MASTER.png` + `REF_GRID_MIN_XX.png`), camera cuts, SFX, dialogue, and
  two final commands (horizontal 16:9 / vertical 9:16), with separate buttons to
  copy each variant, copy the full block, or download it.
- **Image queue**: one card per image (`REF_CAST_MASTER.png` and
  `REF_GRID_MIN_01..NN.png`) with its own prompt, plus buttons to copy/download the
  full queue, ready to paste into ChatGPT.
- **Assembly mode**: the dashboard detects scenes (`scene_XXX.mp4`) or batches
  (`minute_XX.mp4` / `batch_XX.mp4`) and shows project batch progress.
- **Copy prompt**: button per scene; marks the scene as "copied".
- **Mark done**: manual tracking separate from disk. If `frames/frame_XXX.png` or
  `raw_clips/scene_XXX.mp4` already exists, the dashboard detects it automatically
  and shows "File on disk" (no need to mark it by hand).
- **Filters**: search by location/beat/dialogue/cast, status (pending, copied,
  done), act, teaser covers, and "hide done".
- **Copy next pending**: takes the first scene without a frame/clip in the active
  tab, copies its prompt, and records it.
- **Progress**: frames, clips, manual marks, references, and teasers.

Two persistence modes:

| Mode | Command | Tracking |
|---|---|---|
| File | `dashboard my_episode` | Browser `localStorage` + export/import JSON |
| Local server | `dashboard my_episode --serve --open` | `projects/<episode>/dashboard_tracking.json` (atomic, on disk) |

`--serve` listens only on `127.0.0.1` (no external network) and adds **Reload
state** to re-read `frames/`, `raw_clips/`, and `output/` without regenerating the
HTML. **Export tracking** downloads the JSON and **Import** restores it, so progress
is never tied to a browser. Media files are never touched.

> If you regenerate `master_episode.json`, run `dashboard` again to refresh the
> embedded prompts; existing tracking is preserved.

### 4.7 Master prompts (000-003)

The `generators/master_prompts_library.py` library contains the four chained
production prompts and fills them with the episode's real values:

| Prompt | Purpose | Expected output |
|---|---|---|
| **000** Viral story architect | Turns your idea into a title, cast, and block synopsis | Text that feeds 001 |
| **001** Micro-drama screenwriter | Technical breakdown of the project scenes -> 10 s with exact JSON | `master_episode.json` (via `ingest`) |
| **002** Image grid architect | Per-minute contact-sheet plan (6 panels) for the images | Grids/frames for ChatGPT |
| **003** Batch video director | Muse AI + Google Flow flow with platform rules | `scene_XXX.mp4` clips |

- They are generated automatically on create/template/ingest (`01` exports them),
  and manually with `novelfactory.bat prompts my_episode` ->
  `MASTER_PROMPTS.md` + `.txt` + `prompts/*.txt`.
- **Literal fill**: placeholders (`{story_idea}`, `{duration_minutes}`,
  `{total_scenes}`, `{total_grid_images}`, `{visual_style}`, `{aspect_ratio}`) are
  replaced as text, so the JSON examples inside the prompts never break.
- **PROMPT 000** keeps its original text intact (including its header).

---

## 5. Workspace audit report (why this integration)

### 5.1 Where is the editing module and what inputs does it receive?

| Project | Module | Input -> Output |
|---|---|---|
| **USA WHITE** | `src/final_video_pipeline.py` (orchestrated by `auto_runner.py`) | `inbox_raw/<personaje>/` (frames/clips) -> final video **1080x1920 / 6 s** (180 frames) with subtitles and copy -> `output_final/` -> `--export-to-cola <job>` |
| **NOTICIAS IA AUTOMATIZADO** | `compose.py` + Whisper | news -> vertical 1080x1920 30 fps with `.ass` subtitles |
| **NEW YOUTUBE** | (empty) | - |

Conclusion: the existing pipelines edit **short vertical videos (6-60 s)** for
Reels/Shorts. A long episode (default 22 min) in **16:9** with SRT, chapters, and
derived teasers does not fit them without a rewrite. That is why `novel_factory`
brings its own assembler (04) using the same technical stack (ffmpeg, H.264/AAC,
loudnorm).

### 5.2 Where is the publishing module and how is it triggered?

- **`USA WHITE/src/orquestador.py`** publishes the oldest post in
  `cola/pendientes/` to Instagram (Graph API), Facebook, TikTok (a worker with its
  own cookies), and YouTube **Shorts** (API), with SHA-256 anti-repetition
  validation (`anti_ban.py`), a fail-closed proxy, and human-like pauses.
- Triggers: `python src\orquestador.py --publicar-siguiente [--seco]` (manual) or
  the `run_auto.bat` daemon -> `src/auto_runner.py --daemon`, which produces,
  exports READY jobs, and publishes **per character slot**
  (`posting_schedule_us_est`), with a **daily cap**
  (`max_posts_por_dia_por_persona: 2`) and **minimum spacing** between posts on the
  same day. Posts are filtered by the active `personaje_id`
  (`automatico.personas_activas`).
- **Known limit**: `publicador_youtube.py` only uploads **Shorts** (it adds
  `#Shorts` and uses the short vertical video API). The long master **must not** be
  queued there.

### 5.3 What prompt/browser-automation scripts or folders already exist?

- USA WHITE: `src/auto_copywriter.py` (copy), `src/frame_prompt.py` +
  `prompts_pendientes/` (first-frame prompts with files), `compositor.yaml`,
  `config/HEADLINES_PLAYBOOK.md` and `VISUAL_PLAYBOOK.md`, and a **TikTok worker**
  (`tiktok-worker/venv_tiktok` with local Playwright for uploading with cookies).
- NOTICIAS IA AUTOMATIZADO: its own vertical engine with Whisper + `.ass`.
- Workspace pattern: **everything through queue folders** (`cola/pendientes`,
  `inbox`, `procesados`), with intermediate JSON and anti-duplicate validation.

Conclusion: there was no "long novel by scenes" system or prompt queues for
First-Frame generators; the dominant pattern (queues + JSON + browser worker) is
exactly what `novel_factory` follows (minus the browser: here the runner is
assisted, not automated).

### 5.4 How does `novel_factory` connect without breaking anything?

1. **Zero cross-imports**: `novel_factory` only writes **files** to
   `USA WHITE/cola/pendientes/` using the exact schema the orchestrator already
   consumes (see section 6). Not one line of USA WHITE is modified.
2. **The long master is not queued**: `publicador_youtube.py` is Shorts-only. The
   16:9 master is uploaded **manually** with `publish_pack/` (title, description
   with chapters, tags). This is documented inside the pack itself.
3. **The 3 teasers** enter as normal `tipo: "reel"` posts: the daemon distributes
   them by slot and daily cap for the selected character, or they are published one
   at a time with `--publicar-siguiente` (test first with `--seco`).
4. **Built-in anti-duplication**: 05 never overwrites anything existing (unless
   `--force`) and the `id` values (`nf_<slug>_teaser_XX`) make them recognizable in
   `cola/publicados`/`errores`.
5. **If USA WHITE changes tomorrow**: the only contact surface is the post schema
   (5 key fields), isolated in `build_post()` in 05.

---

## 6. Queued post schema (contract with the publisher)

```json
{
  "id": "nf_the_silent_contract_teaser_01",
  "personaje_id": "emma_hayes",
  "tipo": "reel",
  "fecha_creacion": "2026-10-19T12:32:14-05:00",
  "archivo_media": "nf_the_silent_contract_teaser_01_9x16.mp4",
  "hook": "THE LIGHT WAS NEVER OFF",
  "caption": ".teaser text.\n\n#shortdrama #novel .",
  "estado": "pendiente_aprobacion",
  "final_video": true,
  "output_filename": "nf_the_silent_contract_teaser_01_9x16.mp4",
  "plataformas": {"instagram": true, "facebook": true, "tiktok": true, "youtube": true},
  "origen": {"modulo": "novel_factory", "proyecto": "the_silent_contract", "teaser": 1, "escenas": [1,2,3,4,5,6]}
}
```

- The MP4 is copied **next to the JSON** in `cola/pendientes/` (the orchestrator
  looks for the media there or in `procesados/`).
- Test publishing without posting anything:
  `cd "USA WHITE" && python src\orquestador.py --publicar-siguiente --seco`

---

## 7. Configuration

### `config/showrunner_rules.json` (dramatic rules)

- Per-project runtime: each project declares `target_minutes` (default 22;
  suggested range 18-26). Blocks = minutes; scenes = blocks x 6. Legacy profiles:
  `youtube_10` (10 min) and `short_1` (1 min). `format_profiles` only stores
  `scenes_per_block` and `scene_seconds`; the runtime lives in `project.json`.
- 6 acts scaled to the total, 3 teasers of 6 scenes (proportional windows),
  6-15 words of dialogue per scene, 3 exact cuts (0/3/7 s), max. 5 characters and
  5 locations, with blocks of 3-6 scenes per dramatic situation.
- `required_beats`: milestones by fraction of the total (scene 1 hook, scene 2
  world/wound, act closers, final payoff + new hook). With 60 scenes it reproduces
  1/2/10/20/30/40/50/60.
- Each act defines a goal, "must_happen", a retention device, and a dopamine point.
- Retention engine: open-loop types, dopamine cadence every 2-3 scenes,
  cliffhanger types, and a list of **prohibitions** (slow editing, villain
  monologue, resolution by coincidence, ...).
- Compliance: no real celebrities, no brands, no explicit content, no graphic
  violence, no medical/legal claims, and recommended AI disclosure.

### `config/voice_and_style_locks.json` (style locks)

- Photoreal 35 mm look, lighting list (never flat studio light), camera language,
  safe composition for 9:16 cropping, and default shot rotation.
- `image_prompt_suffix` / `image_negative` / `video_negative` (always applied).
- **Identity lock**: faces come from the reference images; age, name, eye color,
  and base hair are never described (only transient state).
- **Voice lock**: voice archetypes (protagonist/antagonist/ally/love interest/
  authority), pace ~2.5 words/s, native English, no narrator unless explicitly
  scripted.
- Complete prompt templates for Omni, Muse AI (`muse_prompt_template`), and Google
  Flow (`flow_prompt_template`), plus post-production parameters (music volume,
  fades, loudness, CRF, silence trimming, teaser overlay).

---

## 8. Tests

```powershell
python -m unittest discover -s novel_factory\tests -v
# or
novel_factory\novelfactory.bat test
```

116 offline tests: master core and schema, generators (one image prompt and one
video prompt per platform), master prompt library (000-003 without unresolved
placeholders), dashboard (state, render, prompts, and tracking), assembler helpers
(SRT, concat escaping, silence detection with clips generated on the fly), exporter
(publisher detection, post JSON), and runner (per-platform queue, download
detection, archiving, and clip validation). Tests that need ffmpeg skip themselves
when it is not installed.

---

## 9. Decisions and known limits

- **No paid APIs / no network.** No ElevenLabs, OpenAI, or Vertex. Audio is Omni's
  native audio; music is local.
- **Playwright not included by design** (external code was never cloned or run;
  your cookies and sessions are not exposed). The `--playwright-script` hook exists
  for your own local automation.
- **SRT not burned into the master** (subtitles as a file, not hard-subs): this
  avoids covering shots and lets you upload the .srt to YouTube.
- **Single-pass loudnorm** (-14 LUFS / TP -1.5 / LRA 11): sufficient for social
  platforms; two-pass remains an optional improvement.
- **`--punch-ins`** re-encodes each clip with cuts (slower per episode); disabled by
  default.
- **The long master is manual** on YouTube (a real limitation of the current
  publisher).
- The demo fixture (`demo_contract`) is meant for testing the pipeline with
  synthetic material; delete or rename it when you produce the first real episode.

## 10. Suggested next steps

1. Real episode 1: `new` -> your LLM -> `ingest` -> frames -> clips -> `assemble`.
2. Download 2-4 royalty-free tracks into `music/` (see mood ideas in `music/README.md`).
3. Test `publish` (plan) and then the publisher's dry run
   (`--publicar-siguiente --seco`) before the first real send.
4. Optional future work: two-pass loudnorm, burned-in SRT for teasers, teaser
   variants (hook vs. cliffhanger), and bilingual subtitles.

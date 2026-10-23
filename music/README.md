# music/ - local BGM for the module

Place **instrumental tracks without vocals** here, with clean loops and commercial-use
rights (downloaded manually once; novel_factory never downloads anything).

## Recommended free sources (manual download)

- **YouTube Audio Library** (Studio -> Audio library): filter "no attribution".
- **Pixabay Music**: free license for commercial use without attribution.
- **Free Music Archive** (CC0 / CC-BY tracks): check each track's license.
- **Uppbeat / Bensound**: free tier with credit where required.

> Do not use copyrighted commercial music: content is published on Instagram / TikTok /
> YouTube, and a copyright claim kills reach.

## Formats

`.mp3`, `.wav`, `.m4a`, `.aac`, `.ogg`, or `.flac`. Ideally 60-120 s loops.

## How the assembler (04) chooses music

1. `--music "path.mp3"` -> uses that exact file.
2. If the master defines `soundtrack.suggested_track`, it looks for a track whose name
   contains that text (for example `dark_tide` -> `dark_tide_loop.mp3`).
3. Otherwise it chooses deterministically from the episode slug (the same track for the
   same episode every time).

## What the assembler does with music

- Loops it (`-stream_loop -1`) for the whole episode.
- Keeps it low (default `-22 dB`) so it does not cover native dialogue.
- Fade in (2 s) and fade out (4 s).
- Final mix normalized to **-14 LUFS / True Peak -1.5 dB** (YouTube standard).

All of this can be adjusted in `config/voice_and_style_locks.json`
(`post_production.music_volume_db`, `music_fade_in_sec`, `music_fade_out_sec`,
`loudness_target_lufs`).

Without tracks here, the assembler still works: no BGM (native dialogue only).

## Mood ideas by genre (name files accordingly)

| File prefix | Mood | Typical genre |
|---|---|---|
| `dark_tide_*` | tense, mysterious | romantic suspense, thriller |
| `harbor_lights_*` | warm, melancholic | family drama, romance |
| `cold_ledger_*` | corporate, oppressive | power drama, revenge |
| `open_road_*` | hopeful, expansive | overcoming, second chances |
| `night_motel_*` | unsettling, nocturnal | mystery, disappearance |

# music/ — BGM local del módulo

Coloca aquí pistas **instrumentales sin voces**, en bucle limpio, con derechos libres
de uso comercial (descargadas a mano una vez; novel_factory nunca descarga nada).

## Fuentes gratuitas recomendadas (descarga manual)

- **YouTube Audio Library** (Studio → Audio library): filtro "no attribution".
- **Pixabay Music**: licencia gratuita para uso comercial sin atribución.
- **Free Music Archive** (pistas CC0 / CC-BY): revisa la licencia de cada pista.
- **Uppbeat / Bensound**: versión gratuita con créditos si aplica.

> No uses música comercial con copyright: el contenido se publica en
> Instagram / TikTok / YouTube y el reclamo de derechos mata el alcance.

## Formatos

`.mp3`, `.wav`, `.m4a`, `.aac`, `.ogg` o `.flac`. Idealmente loops de 60-120 s.

## Cómo elige el ensamblador (04)

1. `--music "ruta.mp3"` → usa ese archivo exacto.
2. Si el maestro define `soundtrack.suggested_track`, busca una pista cuyo nombre
   contenga ese texto (por ejemplo `dark_tide` → `dark_tide_loop.mp3`).
3. Si no, elige de forma estable según el slug del episodio (siempre la misma
   pista para el mismo episodio).

## Qué hace el ensamblador con la música

- La repite en bucle (`-stream_loop -1`) durante todo el episodio.
- Volumen bajo (por defecto `-22 dB`) para no tapar el diálogo nativo.
- Fade in (2 s) y fade out (4 s).
- Mezcla final normalizada a **-14 LUFS / True Peak -1.5 dB** (estándar YouTube).

Todo esto se puede ajustar en `config/voice_and_style_locks.json`
(`post_production.music_volume_db`, `music_fade_in_sec`, `music_fade_out_sec`,
`loudness_target_lufs`).

Sin pistas aquí, el ensamblador funciona igual: sin BGM (solo diálogo nativo).

## Ideas de mood por género (nombra los archivos así)

| Prefijo de archivo | Mood | Género típico |
|---|---|---|
| `dark_tide_*` | tenso, misterioso | romantic suspense, thriller |
| `harbor_lights_*` | cálido, melancólico | drama familiar, romance |
| `cold_ledger_*` | corporativo, opresivo | drama de poder, venganza |
| `open_road_*` | esperanzador, expansivo | superación, segundas oportunidades |
| `night_motel_*` | inquietante, nocturno | misterio, desaparición |

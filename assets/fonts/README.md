# assets/fonts/ — typografía opcional para los teasers

El ensamblador (04) quema el headline (hook) sobre los primeros ~6 s de cada teaser 9:16.

## Orden de búsqueda de la fuente

1. Un `.ttf`/`.otf` landa en esta carpeta (se priorizan nombres con `bold` o `semibold`).
2. Fuentes del sistema en Windows: `arialbd.ttf`, `seguisb.ttf`, `segoeuib.ttf`,
   `arial.ttf`, `impact.ttf`.

## Cómo cambiar la fuente

- Copia tu `.ttf` aquí (por ejemplo `Anton-Regular.ttf` o `Montserrat-ExtraBold.ttf`)
  y ya se usará automáticamente, o
- Pasa una ruta explícita: `python post_production/04_assemble_novel_ffmpeg.py <proyecto> --font "C:\ruta\Anton-Regular.ttf"`.

Sugerencias que funcionan bien en vertical (montserrat/anton/bebas/archivo black):
descárgalas de Google Fonts (uso libre, incluido comercial).

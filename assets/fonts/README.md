# assets/fonts/ - optional typography for teasers

The assembler (04) burns the headline (hook) over the first ~6 s of each 9:16 teaser.

## Font lookup order

1. A `.ttf`/`.otf` file placed in this folder (names containing `bold` or `semibold`
   are preferred).
2. Windows system fonts: `arialbd.ttf`, `seguisb.ttf`, `segoeuib.ttf`, `arial.ttf`,
   `impact.ttf`.

## How to change the font

- Copy your `.ttf` here (for example `Anton-Regular.ttf` or
  `Montserrat-ExtraBold.ttf`) and it is used automatically, or
- Pass an explicit path:
  `python post_production/04_assemble_novel_ffmpeg.py <project> --font "C:\path\Anton-Regular.ttf"`.

Fonts that work well in vertical format: Montserrat, Anton, Bebas, Archivo Black.
Download them from Google Fonts (free for commercial use).

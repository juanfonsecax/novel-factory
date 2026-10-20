# The Silent Contract — Producción con Muse AI (método nuevo)

**Slug:** `demo_contract`  ·  **Escenas:** 60  ·  **Imágenes:** 11  ·  **Lotes:** 10

> Ten years after the fire that ruined her family, Nora Hale returns to inherit a lighthouse and finds the town's most powerful family has been paying her dead mother's debts.

## Cómo funciona

1. Genera **una** hoja maestra de personajes con los rostros y vestuarios fijos.
2. Genera **diez** storyboards (uno por minuto) usando esa hoja como referencia.
3. En Muse AI, sube la hoja maestra + el storyboard del minuto y pega el bloque del lote.
4. Guarda cada video como `raw_clips/minute_0X.mp4` y ejecuta el comando de ensamblaje.

> No necesitas frames por escena ni clips de 10 s: el ensamblador detecta los lotes de 1 minuto.

---

## Paso 1 — Hoja maestra de personajes

Guarda el resultado como `storyboards/REF_CAST_MASTER.png`.

**Prompt:**

```text
REF_CAST_MASTER.png — HOJA MAESTRA DE PERSONAJES

Genera UNA SOLA IMAGEN 16:9 sobre fondo gris neutro uniforme, con todos los personajes principales del proyecto en una hoja de casting limpia y profesional.

👤 PROMPT 002 — GENERADOR DE PERSONAJES (HOJA MAESTRA EN UNA SOLA IMAGEN)
Actúa como director de casting y diseñador de personajes.
Ya tenemos creado el storyboard de la historia.
Ahora analiza ese storyboard e identifica los personajes principales y secundarios relevantes que aparecen en la historia.
Tu tarea es generar UNA SOLA IMAGEN que muestre juntos a todos los personajes identificados.

REFERENCIA
Storyboard:
[ADJUNTAR EL STORYBOARD CREADO ANTERIORMENTE]

REGLA PRINCIPAL
Los personajes deben basarse directamente en el storyboard.
Debes mantener exactamente su:
- Sexo.
- Edad aproximada.
- Etnia y rasgos físicos.
- Rostro.
- Cabello.
- Tono de piel.
- Complexión.
- Vestuario principal.
- Accesorios importantes.
- Estilo visual (prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette Lighting palette: late-afternoon sun raking across the scene with long shadows; overcast storm light with a cold rim on faces; practical tungsten warmth inside against a blue dusk exterior. Camera language: wide establishing shot with a human scale reference; medium shot, chest up, subject slightly off-center; tight close-up, eyes in sharp focus, background falling off; over-the-shoulder shot with the listener soft in foreground.).

Si el storyboard tiene 2 personajes, muestra los 2 en una sola imagen.
Si tiene 3 personajes, muestra los 3 en una sola imagen.
Si tiene 4 personajes, muestra los 4 en una sola imagen.
Y así sucesivamente (priorizando los 3 a 5 personajes principales de la trama).
No inventes personajes que no sean relevantes para la historia.

COMPOSICIÓN DE LA IMAGEN
Genera una hoja de referencia de personajes limpia y profesional.
Todos los personajes deben aparecer:
- En una sola imagen.
- Uno al lado del otro.
- Claramente separados.
- De cuerpo completo.
- De pie.
- Mirando hacia la cámara.
- En una pose natural y neutral.
- Sin taparse entre ellos.
- Sin interactuar físicamente entre ellos.
Debe verse claramente el rostro y el cuerpo completo de cada personaje.
Usa un fondo sencillo y neutro (gris estudio limpio) para que los personajes sean los protagonistas de la imagen.

CONSISTENCIA
Esta imagen funcionará como referencia oficial de los personajes para las siguientes generaciones de imágenes y videos en Muse AI y Google Flow.
Por eso, los rostros y características físicas deben corresponder lo máximo posible con los personajes mostrados en el storyboard.
No rediseñes a los personajes.
El objetivo es extraer del storyboard una referencia visual clara y consistente de cada personaje.

ESTILO VISUAL
Utiliza exactamente el mismo estilo visual utilizado en el storyboard (prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette Lighting palette: late-afternoon sun raking across the scene with long shadows; overcast storm light with a cold rim on faces; practical tungsten warmth inside against a blue dusk exterior. Camera language: wide establishing shot with a human scale reference; medium shot, chest up, subject slightly off-center; tight close-up, eyes in sharp focus, background falling off; over-the-shoulder shot with the listener soft in foreground.).
No cambiar el estilo visual de la historia.

VESTUARIO
Utiliza para cada personaje su vestuario más representativo o principal dentro de la historia.
El vestuario debe ayudar a identificar inmediatamente quién es cada personaje.

TEXTO
Coloca debajo de cada personaje únicamente:
Nombre del personaje y su rol corto.
Ejemplo:
ELENA — Protagonist
COLTON — Gardener
VICTORIA — Mother
No incluir:
- Descripciones largas.
- Diálogos.
- Biografías.
- Párrafos.
- Información de las escenas.
El texto debe ser mínimo para mantener la imagen limpia.

RESULTADO FINAL
Genera UNA SOLA IMAGEN que contenga a todos los personajes relevantes de la historia.
La imagen debe funcionar como una hoja maestra de referencia de personajes, que posteriormente pueda utilizarse para mantener la misma apariencia de los personajes en todas las escenas y videos.
Entrega solamente la imagen de los personajes.

PERSONAJES DEL PROYECTO — nombres, rostros y vestuarios fijos:
- Nora Hale: protagonist del proyecto
- Sam Calloway: love_interest del proyecto
- Margaret Keller: antagonist del proyecto
- Adrian Keller: antagonist_heir del proyecto
- Claire Boone: ally del proyecto

Mantén exactamente los mismos rostros, peinados y vestuarios en todas las imágenes del storyboard y de los lotes de Muse AI. Sin texto, sin letras, sin etiquetas, sin logos, sin marcas de agua. Fondo gris neutro, luz suave y pareja, sin otros elementos.
```

---

## Paso 2 — Storyboards (10 imágenes)

Genera cada imagen con el mismo estilo y los mismos personajes de la hoja maestra.
Guarda cada archivo en `storyboards/` con el nombre indicado.

### REF_GRID_MIN_01.png — Minuto 1 (escenas 1–6)

```text
STORYBOARD IMAGE 01/10 — MINUTE 1 (Scenes 1–6)

Genera UNA SOLA IMAGEN 16:9 con una cuadrícula de storyboard de 3 columnas x 2 filas (6 viñetas), en orden de lectura izquierda a derecha y de arriba abajo.
Usa exactamente los mismos personajes, rostros, edades y vestuarios que REF_CAST_MASTER.png (Hoja de Personajes adjunta). Mantén continuidad de vestuario, props y locaciones entre viñetas.
Estilo visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.
Cada viñeta es un plano cinematográfico 16:9 con encuadre claro y acción legible.
Sin texto, sin letras, sin globos de diálogo, sin logos, sin marcas de agua, sin bordes.

VIÑETAS EXACTAS:
Viñeta 1: Escena 1 — Nora stands at the cliff edge, the lighthouse dark behind… (Hale lighthouse cliff edge, storm dusk, wind and salt spray).
Viñeta 2: Escena 2 — Nora steps off the ferry with one duffel bag, the… (Keller harbor boardwalk, blue hour, wet planks and dock lights).
Viñeta 3: Escena 3 — Sam leans against a harbor truck with his arms crossed… (Hale lighthouse kitchen, night, one warm lamp and a cold stove).
Viñeta 4: Escena 4 — Nora sets a brass key on the lighthouse kitchen table… (Hale lighthouse cliff edge, storm dusk, wind and salt spray).
Viñeta 5: Escena 5 — Sam points through the rain at fresh survey stakes driven… (Keller harbor boardwalk, blue hour, wet planks and dock lights).
Viñeta 6: Escena 6 — Margaret waits under the dry awning of the Keller estate… (Hale lighthouse kitchen, night, one warm lamp and a cold stove).
```

### REF_GRID_MIN_02.png — Minuto 2 (escenas 7–12)

```text
STORYBOARD IMAGE 02/10 — MINUTE 2 (Scenes 7–12)

Genera UNA SOLA IMAGEN 16:9 con una cuadrícula de storyboard de 3 columnas x 2 filas (6 viñetas), en orden de lectura izquierda a derecha y de arriba abajo.
Usa exactamente los mismos personajes, rostros, edades y vestuarios que REF_CAST_MASTER.png (Hoja de Personajes adjunta). Mantén continuidad de vestuario, props y locaciones entre viñetas.
Estilo visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.
Cada viñeta es un plano cinematográfico 16:9 con encuadre claro y acción legible.
Sin texto, sin letras, sin globos de diálogo, sin logos, sin marcas de agua, sin bordes.

VIÑETAS EXACTAS:
Viñeta 1: Escena 7 — Nora reads the deed by a single warm lamp, jaw… (Hale lighthouse cliff edge, storm dusk, wind and salt spray).
Viñeta 2: Escena 8 — Adrian blocks the lighthouse door with a folder under his… (Keller harbor boardwalk, blue hour, wet planks and dock lights).
Viñeta 3: Escena 9 — Nora stands alone on the point, the town lights small… (Hale lighthouse kitchen, night, one warm lamp and a cold stove).
Viñeta 4: Escena 10 — Nora crouches at the lighthouse base, finding a keyhole hidden… (Hale lighthouse cliff edge, storm dusk, wind and salt spray).
Viñeta 5: Escena 11 — Claire slides a sealed envelope across the lawyer's desk (Claire Boone's law office, grey morning, rain on the windows).
Viñeta 6: Escena 12 — Nora reads the witness signature and looks up slowly (Keller boathouse, night, one hanging bulb and a flashlight).
```

### REF_GRID_MIN_03.png — Minuto 3 (escenas 13–18)

```text
STORYBOARD IMAGE 03/10 — MINUTE 3 (Scenes 13–18)

Genera UNA SOLA IMAGEN 16:9 con una cuadrícula de storyboard de 3 columnas x 2 filas (6 viñetas), en orden de lectura izquierda a derecha y de arriba abajo.
Usa exactamente los mismos personajes, rostros, edades y vestuarios que REF_CAST_MASTER.png (Hoja de Personajes adjunta). Mantén continuidad de vestuario, props y locaciones entre viñetas.
Estilo visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.
Cada viñeta es un plano cinematográfico 16:9 con encuadre claro y acción legible.
Sin texto, sin letras, sin globos de diálogo, sin logos, sin marcas de agua, sin bordes.

VIÑETAS EXACTAS:
Viñeta 1: Escena 13 — Sam stands in the boathouse doorway, rain behind him (Keller estate, dusk, warm interior against blue windows).
Viñeta 2: Escena 14 — Nora sweeps a flashlight over scorched beams (Claire Boone's law office, grey morning, rain on the windows).
Viñeta 3: Escena 15 — Margaret pours tea without offering a cup (Keller boathouse, night, one hanging bulb and a flashlight).
Viñeta 4: Escena 16 — Nora stands in the town hall doorway as every head… (Keller estate, dusk, warm interior against blue windows).
Viñeta 5: Escena 17 — Adrian corners Nora by the harbor railing (Claire Boone's law office, grey morning, rain on the windows).
Viñeta 6: Escena 18 — Nora stares at a survey map pinned to the boathouse… (Keller boathouse, night, one hanging bulb and a flashlight).
```

### REF_GRID_MIN_04.png — Minuto 4 (escenas 19–24)

```text
STORYBOARD IMAGE 04/10 — MINUTE 4 (Scenes 19–24)

Genera UNA SOLA IMAGEN 16:9 con una cuadrícula de storyboard de 3 columnas x 2 filas (6 viñetas), en orden de lectura izquierda a derecha y de arriba abajo.
Usa exactamente los mismos personajes, rostros, edades y vestuarios que REF_CAST_MASTER.png (Hoja de Personajes adjunta). Mantén continuidad de vestuario, props y locaciones entre viñetas.
Estilo visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.
Cada viñeta es un plano cinematográfico 16:9 con encuadre claro y acción legible.
Sin texto, sin letras, sin globos de diálogo, sin logos, sin marcas de agua, sin bordes.

VIÑETAS EXACTAS:
Viñeta 1: Escena 19 — Sam watches Nora from across the dock, unable to speak (Keller estate, dusk, warm interior against blue windows).
Viñeta 2: Escena 20 — Adrian holds the lighthouse door open, waiting (Claire Boone's law office, grey morning, rain on the windows).
Viñeta 3: Escena 21 — Nora spreads water-stained survey files across the lighthouse floor (Keller boathouse, night, flashlight and dust).
Viñeta 4: Escena 22 — Sam jimmies the boathouse lock with a pry bar (Hale lighthouse archive room, night, a single desk lamp).
Viñeta 5: Escena 23 — Nora's flashlight beam catches a metal box under the floorboards (Harbor diner, dawn, cold fluorescent light and steam).
Viñeta 6: Escena 24 — Sam watches Nora read the permits, his face falling (Keller boathouse, night, flashlight and dust).
```

### REF_GRID_MIN_05.png — Minuto 5 (escenas 25–30)

```text
STORYBOARD IMAGE 05/10 — MINUTE 5 (Scenes 25–30)

Genera UNA SOLA IMAGEN 16:9 con una cuadrícula de storyboard de 3 columnas x 2 filas (6 viñetas), en orden de lectura izquierda a derecha y de arriba abajo.
Usa exactamente los mismos personajes, rostros, edades y vestuarios que REF_CAST_MASTER.png (Hoja de Personajes adjunta). Mantén continuidad de vestuario, props y locaciones entre viñetas.
Estilo visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.
Cada viñeta es un plano cinematográfico 16:9 con encuadre claro y acción legible.
Sin texto, sin letras, sin globos de diálogo, sin logos, sin marcas de agua, sin bordes.

VIÑETAS EXACTAS:
Viñeta 1: Escena 25 — Nora holds a permit signed by Margaret, dated before the… (Hale lighthouse archive room, night, a single desk lamp).
Viñeta 2: Escena 26 — Nora and Sam stand close in the archive, the file… (Harbor diner, dawn, cold fluorescent light and steam).
Viñeta 3: Escena 27 — Adrian waits in a diner booth across from Nora (Keller boathouse, night, flashlight and dust).
Viñeta 4: Escena 28 — Nora slides the file across the table, keeping one page… (Hale lighthouse archive room, night, a single desk lamp).
Viñeta 5: Escena 29 — Adrian leans in, his hand covering hers (Harbor diner, dawn, cold fluorescent light and steam).
Viñeta 6: Escena 30 — Nora stands alone in the lamp room, the file in… (Keller boathouse, night, flashlight and dust).
```

### REF_GRID_MIN_06.png — Minuto 6 (escenas 31–36)

```text
STORYBOARD IMAGE 06/10 — MINUTE 6 (Scenes 31–36)

Genera UNA SOLA IMAGEN 16:9 con una cuadrícula de storyboard de 3 columnas x 2 filas (6 viñetas), en orden de lectura izquierda a derecha y de arriba abajo.
Usa exactamente los mismos personajes, rostros, edades y vestuarios que REF_CAST_MASTER.png (Hoja de Personajes adjunta). Mantén continuidad de vestuario, props y locaciones entre viñetas.
Estilo visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.
Cada viñeta es un plano cinematográfico 16:9 con encuadre claro y acción legible.
Sin texto, sin letras, sin globos de diálogo, sin logos, sin marcas de agua, sin bordes.

VIÑETAS EXACTAS:
Viñeta 1: Escena 31 — Rain hammers the town hall windows as Nora faces the… (Town hall hearing room, grey morning, rain streaking the windows).
Viñeta 2: Escena 32 — Margaret sits perfectly still in the front row (Hale lighthouse, storm night, lightning through the glass).
Viñeta 3: Escena 33 — Claire reads the emergency petition aloud (Hale lighthouse kitchen, night, one lamp, rain outside).
Viñeta 4: Escena 34 — Nora stands in the empty lighthouse, the lamp cold above… (Town hall hearing room, grey morning, rain streaking the windows).
Viñeta 5: Escena 35 — Sam signs a statement at the harbor office, hand shaking (Hale lighthouse, storm night, lightning through the glass).
Viñeta 6: Escena 36 — Nora listens through a half-open door, unseen (Hale lighthouse kitchen, night, one lamp, rain outside).
```

### REF_GRID_MIN_07.png — Minuto 7 (escenas 37–42)

```text
STORYBOARD IMAGE 07/10 — MINUTE 7 (Scenes 37–42)

Genera UNA SOLA IMAGEN 16:9 con una cuadrícula de storyboard de 3 columnas x 2 filas (6 viñetas), en orden de lectura izquierda a derecha y de arriba abajo.
Usa exactamente los mismos personajes, rostros, edades y vestuarios que REF_CAST_MASTER.png (Hoja de Personajes adjunta). Mantén continuidad de vestuario, props y locaciones entre viñetas.
Estilo visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.
Cada viñeta es un plano cinematográfico 16:9 con encuadre claro y acción legible.
Sin texto, sin letras, sin globos de diálogo, sin logos, sin marcas de agua, sin bordes.

VIÑETAS EXACTAS:
Viñeta 1: Escena 37 — Nora walks the storm beach alone, hair plastered to her… (Town hall hearing room, grey morning, rain streaking the windows).
Viñeta 2: Escena 38 — Adrian waits in her kitchen with the sale papers (Hale lighthouse, storm night, lightning through the glass).
Viñeta 3: Escena 39 — Nora stares into the lighthouse lens, thinking (Hale lighthouse kitchen, night, one lamp, rain outside).
Viñeta 4: Escena 40 — Nora finds an old harbor logbook behind the lens housing (Town hall hearing room, grey morning, rain streaking the windows).
Viñeta 5: Escena 41 — Nora opens the logbook on the lighthouse table, pages brittle (Hale lighthouse archive room, dawn, cold blue light).
Viñeta 6: Escena 42 — Nora and Sam compare timestamps under a desk lamp (Harbor pier, morning, flat silver water).
```

### REF_GRID_MIN_08.png — Minuto 8 (escenas 43–48)

```text
STORYBOARD IMAGE 08/10 — MINUTE 8 (Scenes 43–48)

Genera UNA SOLA IMAGEN 16:9 con una cuadrícula de storyboard de 3 columnas x 2 filas (6 viñetas), en orden de lectura izquierda a derecha y de arriba abajo.
Usa exactamente los mismos personajes, rostros, edades y vestuarios que REF_CAST_MASTER.png (Hoja de Personajes adjunta). Mantén continuidad de vestuario, props y locaciones entre viñetas.
Estilo visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.
Cada viñeta es un plano cinematográfico 16:9 con encuadre claro y acción legible.
Sin texto, sin letras, sin globos de diálogo, sin logos, sin marcas de agua, sin bordes.

VIÑETAS EXACTAS:
Viñeta 1: Escena 43 — Nora traces a line in the log with her finger (Town hall steps, dusk, wet stone).
Viñeta 2: Escena 44 — Sam reads over her shoulder, close enough to touch (Hale lighthouse archive room, dawn, cold blue light).
Viñeta 3: Escena 45 — Nora looks up at Sam, a decision forming (Harbor pier, morning, flat silver water).
Viñeta 4: Escena 46 — Adrian stands on the town hall steps, trying to smile (Town hall steps, dusk, wet stone).
Viñeta 5: Escena 47 — Nora walks past him without stopping (Hale lighthouse archive room, dawn, cold blue light).
Viñeta 6: Escena 48 — Margaret waits in the hall, gloves in hand (Harbor pier, morning, flat silver water).
```

### REF_GRID_MIN_09.png — Minuto 9 (escenas 49–54)

```text
STORYBOARD IMAGE 09/10 — MINUTE 9 (Scenes 49–54)

Genera UNA SOLA IMAGEN 16:9 con una cuadrícula de storyboard de 3 columnas x 2 filas (6 viñetas), en orden de lectura izquierda a derecha y de arriba abajo.
Usa exactamente los mismos personajes, rostros, edades y vestuarios que REF_CAST_MASTER.png (Hoja de Personajes adjunta). Mantén continuidad de vestuario, props y locaciones entre viñetas.
Estilo visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.
Cada viñeta es un plano cinematográfico 16:9 con encuadre claro y acción legible.
Sin texto, sin letras, sin globos de diálogo, sin logos, sin marcas de agua, sin bordes.

VIÑETAS EXACTAS:
Viñeta 1: Escena 49 — Nora faces Margaret on the empty hearing floor (Town hall steps, dusk, wet stone).
Viñeta 2: Escena 50 — Nora stands at the lighthouse door as the town lights… (Hale lighthouse archive room, dawn, cold blue light).
Viñeta 3: Escena 51 — The hearing room fills; Nora stands alone at the table (Town hall hearing room, day, hard window light).
Viñeta 4: Escena 52 — Sam steps to the microphone, the room silent (Hale lighthouse point, golden hour, wind down).
Viñeta 5: Escena 53 — Margaret's smile falters for the first time (Harbor, golden hour, calm water).
Viñeta 6: Escena 54 — Nora holds up the harbor log, open to the page (Town hall hearing room, day, hard window light).
```

### REF_GRID_MIN_10.png — Minuto 10 (escenas 55–60)

```text
STORYBOARD IMAGE 10/10 — MINUTE 10 (Scenes 55–60)

Genera UNA SOLA IMAGEN 16:9 con una cuadrícula de storyboard de 3 columnas x 2 filas (6 viñetas), en orden de lectura izquierda a derecha y de arriba abajo.
Usa exactamente los mismos personajes, rostros, edades y vestuarios que REF_CAST_MASTER.png (Hoja de Personajes adjunta). Mantén continuidad de vestuario, props y locaciones entre viñetas.
Estilo visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.
Cada viñeta es un plano cinematográfico 16:9 con encuadre claro y acción legible.
Sin texto, sin letras, sin globos de diálogo, sin logos, sin marcas de agua, sin bordes.

VIÑETAS EXACTAS:
Viñeta 1: Escena 55 — Adrian half-rises from his chair (Hale lighthouse point, golden hour, wind down).
Viñeta 2: Escena 56 — Nora sets the log on the clerk's desk (Harbor, golden hour, calm water).
Viñeta 3: Escena 57 — Margaret reaches for the log; Nora slides it away (Town hall hearing room, day, hard window light).
Viñeta 4: Escena 58 — Sam takes Nora's hand under the table (Hale lighthouse point, golden hour, wind down).
Viñeta 5: Escena 59 — Nora walks out of the town hall into the light (Harbor, golden hour, calm water).
Viñeta 6: Escena 60 — Nora and Sam stand on the lighthouse point at dusk… (Town hall hearing room, day, hard window light).
```

---

## Paso 3 — Lotes Muse AI (10 videos de 1 minuto)

En cada lote: adjunta los dos archivos indicados y pega **un** comando final
(16:9 para YouTube o 9:16 para Reels/Shorts).

### Lote 01 — Minuto 1 (escenas 1–6)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_01.png`

**Guardar como:** `raw_clips/minute_01.mp4`

**Bloque para Muse AI:**

```text
📎 ADJUNTAR EN MUSE AI: [1] REF_CAST_MASTER.png (Hoja de Personajes) + [2] REF_GRID_MIN_01.png (Storyboard Minuto 1: Escenas 1–6)

ESCENA 1 (Viñeta #1 del Storyboard) — 00:00–00:10
- Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray
- Characters Present: Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — Nora stands at the cliff edge, the lighthouse dark behind her, salt wind whipping her coat.
  * [03s–07s]: tight close-up — Close detail on a brass key; the room falls quiet around it.
  * [07s–10s]: over-the-shoulder shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  NORA (cold, quiet): "They said the lighthouse was empty for ten years. So who left the light on?"

ESCENA 2 (Viñeta #2 del Storyboard) — 00:10–00:20
- Location: Keller harbor boardwalk, blue hour, wet planks and dock lights
- Characters Present: Sam Calloway
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Nora steps off the ferry with one duffel bag, the town sign behind her.
  * [03s–07s]: tight close-up — Close detail on the deed; the room falls quiet around it.
  * [07s–10s]: low-angle hero shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, 6–8 sec max):
  SAM (dry, warm): "Nora Hale. Ten years, and you still drive like the road owes you money."

ESCENA 3 (Viñeta #3 del Storyboard) — 00:20–00:30
- Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove
- Characters Present: Nora Hale, Sam Calloway
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: tight close-up — Sam leans against a harbor truck with his arms crossed, trying not to smile.
  * [03s–07s]: medium shot — Close detail on fresh survey stakes; the room falls quiet around it.
  * [07s–10s]: insert shot of the evidence object — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, 6–8 sec max):
  NORA (guarded): "I inherited a lighthouse, Sam. Not a welcome party."
  SAM (low): "I'm not happy. I'm careful."

ESCENA 4 (Viñeta #4 del Storyboard) — 00:30–00:40
- Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray
- Characters Present: Sam Calloway, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: over-the-shoulder shot — Nora sets a brass key on the lighthouse kitchen table between them.
  * [03s–07s]: tight close-up — Close detail on the dead lighthouse lamp; the room falls quiet around it.
  * [07s–10s]: wide establishing shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  SAM (flat): "The Kellers already had surveyors on your land. Twice."
  NORA (steady): "Then they can explain it to the state. The trust is mine now."

ESCENA 5 (Viñeta #5 del Storyboard) — 00:40–00:50
- Location: Keller harbor boardwalk, blue hour, wet planks and dock lights
- Characters Present: Margaret Keller, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: low-angle hero shot — Sam points through the rain at fresh survey stakes driven into the cliff.
  * [03s–07s]: tight close-up — Close detail on a brass key; the room falls quiet around it.
  * [07s–10s]: over-the-shoulder shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  MARGARET (silk over steel): "Your father was a liar, dear. Sentiment won't change what the deed says."
  NORA (quiet): "Then you won't mind me reading the deed. Slowly."

ESCENA 6 (Viñeta #6 del Storyboard) — 00:50–01:00
- Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove
- Characters Present: Adrian Keller, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — Margaret waits under the dry awning of the Keller estate, gloves folded.
  * [03s–07s]: tight close-up — Close detail on the deed; the room falls quiet around it.
  * [07s–10s]: low-angle hero shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  ADRIAN (reasonable, rehearsed): "Sell us the point. Name your price and leave the past where it belongs."
  NORA (cold): "The past is the only thing you've ever asked me to leave behind."

COMANDOS FINALES PARA PEGAR EN MUSE AI (ELIGE SEGÚN EL CANAL):

**Opción YouTube Monetización Long-Form (16:9 Horizontal):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_01.mp4)."

**Opción Reels / TikTok / Shorts (9:16 Vertical):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_01.mp4)."
```

**Comando final 16:9 (YouTube):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_01.mp4).

**Comando final 9:16 (Reels/Shorts):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_01.mp4).

### Lote 02 — Minuto 2 (escenas 7–12)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_02.png`

**Guardar como:** `raw_clips/minute_02.mp4`

**Bloque para Muse AI:**

```text
📎 ADJUNTAR EN MUSE AI: [1] REF_CAST_MASTER.png (Hoja de Personajes) + [2] REF_GRID_MIN_02.png (Storyboard Minuto 2: Escenas 7–12)

ESCENA 7 (Viñeta #7 del Storyboard) — 01:00–01:10
- Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray
- Characters Present: Nora Hale, Margaret Keller
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Nora reads the deed by a single warm lamp, jaw tight.
  * [03s–07s]: tight close-up — Close detail on fresh survey stakes; the room falls quiet around it.
  * [07s–10s]: insert shot of the evidence object — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, 6–8 sec max):
  NORA (suspicious): "You had ten years to buy this land. Why wait until I came back?"
  MARGARET (pleasant): "Because a deed is cleaner than a funeral."

ESCENA 8 (Viñeta #8 del Storyboard) — 01:10–01:20
- Location: Keller harbor boardwalk, blue hour, wet planks and dock lights
- Characters Present: Claire Boone, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: tight close-up — Adrian blocks the lighthouse door with a folder under his arm.
  * [03s–07s]: medium shot — Close detail on the dead lighthouse lamp; the room falls quiet around it.
  * [07s–10s]: wide establishing shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  CLAIRE (careful): "Your father changed his will three days before he died. That's not nothing."
  NORA (sharp): "Who witnessed it?"

ESCENA 9 (Viñeta #9 del Storyboard) — 01:20–01:30
- Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove
- Characters Present: Claire Boone, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: over-the-shoulder shot — Nora stands alone on the point, the town lights small below her.
  * [03s–07s]: tight close-up — Close detail on a brass key; the room falls quiet around it.
  * [07s–10s]: insert shot of the evidence object — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  CLAIRE (quiet): "Margaret Keller's attorney. And a man named Sam."
  NORA (low): "Sam was there that night? At the lighthouse?"

ESCENA 10 (Viñeta #10 del Storyboard) — 01:30–01:40
- Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray
- Characters Present: Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: low-angle hero shot — Nora crouches at the lighthouse base, finding a keyhole hidden under peeling paint.
  * [03s–07s]: tight close-up — Close detail on the deed; the room falls quiet around it.
  * [07s–10s]: insert shot of the evidence object — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  NORA (hushed): "Dad... what did you lock in the lighthouse?"
  NORA (breaking): "And why did you leave me the key?"

ESCENA 11 (Viñeta #11 del Storyboard) — 01:40–01:50
- Location: Claire Boone's law office, grey morning, rain on the windows
- Characters Present: Claire Boone, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Claire slides a sealed envelope across the lawyer's desk.
  * [03s–07s]: tight close-up — Close detail on the sealed petition; the room falls quiet around it.
  * [07s–10s]: over-the-shoulder shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  CLAIRE (clinical): "The petition says you're unfit to manage the trust. They want a guardian by Friday."
  NORA (flat): "On what grounds?"

ESCENA 12 (Viñeta #12 del Storyboard) — 01:50–02:00
- Location: Keller boathouse, night, one hanging bulb and a flashlight
- Characters Present: Nora Hale, Claire Boone
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: tight close-up — Nora reads the witness signature and looks up slowly.
  * [03s–07s]: medium shot — Close detail on a witness signature; the room falls quiet around it.
  * [07s–10s]: low-angle hero shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; CLAIRE — grounded, plainspoken American English with a slight coastal New England softness
- Dialogue (English, 6–8 sec max):
  NORA (sharp): "Who signed the statement?"
  CLAIRE (quiet): "Half the harbor. And one name you won't like: Sam."
  NORA (bitter): "Of course."

COMANDOS FINALES PARA PEGAR EN MUSE AI (ELIGE SEGÚN EL CANAL):

**Opción YouTube Monetización Long-Form (16:9 Horizontal):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_02.mp4)."

**Opción Reels / TikTok / Shorts (9:16 Vertical):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_02.mp4)."
```

**Comando final 16:9 (YouTube):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_02.mp4).

**Comando final 9:16 (Reels/Shorts):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_02.mp4).

### Lote 03 — Minuto 3 (escenas 13–18)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_03.png`

**Guardar como:** `raw_clips/minute_03.mp4`

**Bloque para Muse AI:**

```text
📎 ADJUNTAR EN MUSE AI: [1] REF_CAST_MASTER.png (Hoja de Personajes) + [2] REF_GRID_MIN_03.png (Storyboard Minuto 3: Escenas 13–18)

ESCENA 13 (Viñeta #13 del Storyboard) — 02:00–02:10
- Location: Keller estate, dusk, warm interior against blue windows
- Characters Present: Sam Calloway, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: over-the-shoulder shot — Sam stands in the boathouse doorway, rain behind him.
  * [03s–07s]: tight close-up — Close detail on a scorched beam; the room falls quiet around it.
  * [07s–10s]: medium shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  SAM (ashamed): "I signed a paper. I didn't read it. I was twenty-two and scared."
  NORA (cutting): "Scared of what? Of being poor? Of her?"

ESCENA 14 (Viñeta #14 del Storyboard) — 02:10–02:20
- Location: Claire Boone's law office, grey morning, rain on the windows
- Characters Present: Sam Calloway, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: low-angle hero shot — Nora sweeps a flashlight over scorched beams.
  * [03s–07s]: tight close-up — Close detail on the survey map; the room falls quiet around it.
  * [07s–10s]: wide establishing shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  SAM (low): "The fire started in the boathouse, Nora. Not the cliffs."
  NORA (raw): "Then why did the whole town say it was me?"

ESCENA 15 (Viñeta #15 del Storyboard) — 02:20–02:30
- Location: Keller boathouse, night, one hanging bulb and a flashlight
- Characters Present: Margaret Keller, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — Margaret pours tea without offering a cup.
  * [03s–07s]: tight close-up — Close detail on the sealed petition; the room falls quiet around it.
  * [07s–10s]: over-the-shoulder shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  MARGARET (pleasant threat): "If you reopen that investigation, I'll make sure the town remembers who lit the match."
  NORA (tired): "Go ahead. I've played the villain in your story for ten years."

ESCENA 16 (Viñeta #16 del Storyboard) — 02:30–02:40
- Location: Keller estate, dusk, warm interior against blue windows
- Characters Present: Nora Hale, Adrian Keller
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Nora stands in the town hall doorway as every head turns.
  * [03s–07s]: tight close-up — Close detail on a witness signature; the room falls quiet around it.
  * [07s–10s]: low-angle hero shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  NORA (precise): "A debt doesn't transfer with land, Adrian. But fraud does."
  ADRIAN (smiling): "Big words for someone with no lawyer."

ESCENA 17 (Viñeta #17 del Storyboard) — 02:40–02:50
- Location: Claire Boone's law office, grey morning, rain on the windows
- Characters Present: Sam Calloway, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: tight close-up — Adrian corners Nora by the harbor railing.
  * [03s–07s]: medium shot — Close detail on a scorched beam; the room falls quiet around it.
  * [07s–10s]: insert shot of the evidence object — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  SAM (urgent): "The old survey files are in the boathouse. What's left of them."
  NORA (decided): "Then we go tonight, before the hearing."

ESCENA 18 (Viñeta #18 del Storyboard) — 02:50–03:00
- Location: Keller boathouse, night, one hanging bulb and a flashlight
- Characters Present: Sam Calloway, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: over-the-shoulder shot — Nora stares at a survey map pinned to the boathouse wall.
  * [03s–07s]: tight close-up — Close detail on the survey map; the room falls quiet around it.
  * [07s–10s]: wide establishing shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  SAM (dry): "You always did like a bad idea with good lighting."
  NORA (impatient): "You coming or not? Bring the pry bar."

COMANDOS FINALES PARA PEGAR EN MUSE AI (ELIGE SEGÚN EL CANAL):

**Opción YouTube Monetización Long-Form (16:9 Horizontal):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_03.mp4)."

**Opción Reels / TikTok / Shorts (9:16 Vertical):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_03.mp4)."
```

**Comando final 16:9 (YouTube):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_03.mp4).

**Comando final 9:16 (Reels/Shorts):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_03.mp4).

### Lote 04 — Minuto 4 (escenas 19–24)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_04.png`

**Guardar como:** `raw_clips/minute_04.mp4`

**Bloque para Muse AI:**

```text
📎 ADJUNTAR EN MUSE AI: [1] REF_CAST_MASTER.png (Hoja de Personajes) + [2] REF_GRID_MIN_04.png (Storyboard Minuto 4: Escenas 19–24)

ESCENA 19 (Viñeta #19 del Storyboard) — 03:00–03:10
- Location: Keller estate, dusk, warm interior against blue windows
- Characters Present: Nora Hale, Sam Calloway
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: low-angle hero shot — Sam watches Nora from across the dock, unable to speak.
  * [03s–07s]: tight close-up — Close detail on the sealed petition; the room falls quiet around it.
  * [07s–10s]: over-the-shoulder shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, 6–8 sec max):
  NORA (shaking): "There. Seawall permits. Signed by Margaret. Dated before the fire."
  SAM (quiet): "That's not a permit. That's a motive."

ESCENA 20 (Viñeta #20 del Storyboard) — 03:10–03:20
- Location: Claire Boone's law office, grey morning, rain on the windows
- Characters Present: Adrian Keller, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — Adrian holds the lighthouse door open, waiting.
  * [03s–07s]: tight close-up — Close detail on a witness signature; the room falls quiet around it.
  * [07s–10s]: low-angle hero shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  ADRIAN (reasonable): "Give me the file and I'll tell the town the fire was an accident."
  NORA (wary): "And in exchange?"
  ADRIAN (soft): "I'll say you were with me that night. Everything goes away."

ESCENA 21 (Viñeta #21 del Storyboard) — 03:20–03:30
- Location: Keller boathouse, night, flashlight and dust
- Characters Present: Adrian Keller, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: tight close-up — Nora spreads water-stained survey files across the lighthouse floor.
  * [03s–07s]: medium shot — Close detail on the metal evidence box; the room falls quiet around it.
  * [07s–10s]: over-the-shoulder shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  ADRIAN (incredulous): "You'd rather be the arsonist than my alibi?"
  NORA (flat): "I'd rather be alone than owned. Now move."

ESCENA 22 (Viñeta #22 del Storyboard) — 03:30–03:40
- Location: Hale lighthouse archive room, night, a single desk lamp
- Characters Present: Margaret Keller, Nora Hale, Claire Boone
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: over-the-shoulder shot — Sam jimmies the boathouse lock with a pry bar.
  * [03s–07s]: tight close-up — Close detail on the seawall permit; the room falls quiet around it.
  * [07s–10s]: low-angle hero shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure; CLAIRE — grounded, plainspoken American English with a slight coastal New England softness
- Dialogue (English, 6–8 sec max):
  MARGARET (satisfied): "The trust is frozen. Emergency petition. Effective this morning."
  NORA (steady): "On what grounds?"
  CLAIRE (ashamed): "Mental incompetence. They have statements."

ESCENA 23 (Viñeta #23 del Storyboard) — 03:40–03:50
- Location: Harbor diner, dawn, cold fluorescent light and steam
- Characters Present: Claire Boone, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: low-angle hero shot — Nora's flashlight beam catches a metal box under the floorboards.
  * [03s–07s]: tight close-up — Close detail on a folded page; the room falls quiet around it.
  * [07s–10s]: medium shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  CLAIRE (gentle): "One of the statements is from Sam."
  NORA (low): "Sam... tell me that's a lie. Tell me to my face."

ESCENA 24 (Viñeta #24 del Storyboard) — 03:50–04:00
- Location: Keller boathouse, night, flashlight and dust
- Characters Present: Sam Calloway, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — Sam watches Nora read the permits, his face falling.
  * [03s–07s]: tight close-up — Close detail on a diner coffee cup; the room falls quiet around it.
  * [07s–10s]: insert shot of the evidence object — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  SAM (broken): "They threatened my sister's job. I'm sorry."
  NORA (bitter): "Everyone keeps apologizing while they take everything."
  NORA (hard): "Don't apologize. Fix it."

COMANDOS FINALES PARA PEGAR EN MUSE AI (ELIGE SEGÚN EL CANAL):

**Opción YouTube Monetización Long-Form (16:9 Horizontal):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_04.mp4)."

**Opción Reels / TikTok / Shorts (9:16 Vertical):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_04.mp4)."
```

**Comando final 16:9 (YouTube):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_04.mp4).

**Comando final 9:16 (Reels/Shorts):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_04.mp4).

### Lote 05 — Minuto 5 (escenas 25–30)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_05.png`

**Guardar como:** `raw_clips/minute_05.mp4`

**Bloque para Muse AI:**

```text
📎 ADJUNTAR EN MUSE AI: [1] REF_CAST_MASTER.png (Hoja de Personajes) + [2] REF_GRID_MIN_05.png (Storyboard Minuto 5: Escenas 25–30)

ESCENA 25 (Viñeta #25 del Storyboard) — 04:00–04:10
- Location: Hale lighthouse archive room, night, a single desk lamp
- Characters Present: Adrian Keller, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Nora holds a permit signed by Margaret, dated before the fire.
  * [03s–07s]: tight close-up — Close detail on the metal evidence box; the room falls quiet around it.
  * [07s–10s]: over-the-shoulder shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  ADRIAN (reasonable): "Sign the sale. I'll make the petition disappear."
  NORA (quiet): "And if I don't?"
  ADRIAN (soft): "Then I own your father's name."

ESCENA 26 (Viñeta #26 del Storyboard) — 04:10–04:20
- Location: Harbor diner, dawn, cold fluorescent light and steam
- Characters Present: Nora Hale, Sam Calloway
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: tight close-up — Nora and Sam stand close in the archive, the file between them.
  * [03s–07s]: medium shot — Close detail on the seawall permit; the room falls quiet around it.
  * [07s–10s]: low-angle hero shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, 6–8 sec max):
  NORA (realizing): "Lighthouses keep logs. Every ship, every storm, every night."
  SAM (nodding): "Your father logged the harbor for thirty years."

ESCENA 27 (Viñeta #27 del Storyboard) — 04:20–04:30
- Location: Keller boathouse, night, flashlight and dust
- Characters Present: Nora Hale, Sam Calloway
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: over-the-shoulder shot — Adrian waits in a diner booth across from Nora.
  * [03s–07s]: tight close-up — Close detail on a folded page; the room falls quiet around it.
  * [07s–10s]: medium shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, 6–8 sec max):
  NORA (urgent): "Including the night of the fire. And the boat that left at two a.m."
  SAM (cold): "That's the Keller launch."

ESCENA 28 (Viñeta #28 del Storyboard) — 04:30–04:40
- Location: Hale lighthouse archive room, night, a single desk lamp
- Characters Present: Nora Hale, Sam Calloway
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: low-angle hero shot — Nora slides the file across the table, keeping one page back.
  * [03s–07s]: tight close-up — Close detail on a diner coffee cup; the room falls quiet around it.
  * [07s–10s]: wide establishing shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, 6–8 sec max):
  NORA (quiet): "No. That's Margaret's launch. With Adrian at the helm."
  SAM (careful): "Nora. Are you sure?"
  NORA (steady): "I've never been surer of anything."

ESCENA 29 (Viñeta #29 del Storyboard) — 04:40–04:50
- Location: Harbor diner, dawn, cold fluorescent light and steam
- Characters Present: Adrian Keller, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — Adrian leans in, his hand covering hers.
  * [03s–07s]: tight close-up — Close detail on the metal evidence box; the room falls quiet around it.
  * [07s–10s]: over-the-shoulder shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  ADRIAN (amused): "You think a notebook beats a town full of witnesses?"
  NORA (calm): "I think a notebook beats you. And you know it."

ESCENA 30 (Viñeta #30 del Storyboard) — 04:50–05:00
- Location: Keller boathouse, night, flashlight and dust
- Characters Present: Margaret Keller, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Nora stands alone in the lamp room, the file in her hands.
  * [03s–07s]: tight close-up — Close detail on the seawall permit; the room falls quiet around it.
  * [07s–10s]: low-angle hero shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  MARGARET (tired): "Name your price, Nora. One last time."
  NORA (final): "The hearing. Tomorrow. Public. All of it."
  MARGARET (quiet): "Then you'll lose the only home you have left."

COMANDOS FINALES PARA PEGAR EN MUSE AI (ELIGE SEGÚN EL CANAL):

**Opción YouTube Monetización Long-Form (16:9 Horizontal):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_05.mp4)."

**Opción Reels / TikTok / Shorts (9:16 Vertical):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_05.mp4)."
```

**Comando final 16:9 (YouTube):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_05.mp4).

**Comando final 9:16 (Reels/Shorts):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_05.mp4).

### Lote 06 — Minuto 6 (escenas 31–36)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_06.png`

**Guardar como:** `raw_clips/minute_06.mp4`

**Bloque para Muse AI:**

```text
📎 ADJUNTAR EN MUSE AI: [1] REF_CAST_MASTER.png (Hoja de Personajes) + [2] REF_GRID_MIN_06.png (Storyboard Minuto 6: Escenas 31–36)

ESCENA 31 (Viñeta #31 del Storyboard) — 05:00–05:10
- Location: Town hall hearing room, grey morning, rain streaking the windows
- Characters Present: Nora Hale, Margaret Keller
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: over-the-shoulder shot — Rain hammers the town hall windows as Nora faces the panel.
  * [03s–07s]: tight close-up — Close detail on the emergency petition; the room falls quiet around it.
  * [07s–10s]: insert shot of the evidence object — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, 6–8 sec max):
  NORA (steady): "I'd rather lose the house than let you keep my father's name."
  MARGARET (soft): "You already lost it ten years ago."

ESCENA 32 (Viñeta #32 del Storyboard) — 05:10–05:20
- Location: Hale lighthouse, storm night, lightning through the glass
- Characters Present: Claire Boone, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: low-angle hero shot — Margaret sits perfectly still in the front row.
  * [03s–07s]: tight close-up — Close detail on a statement form; the room falls quiet around it.
  * [07s–10s]: insert shot of the evidence object — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  CLAIRE (nervous): "The hearing is packed. Half the town came."
  NORA (resolved): "Good. This time, I want witnesses."

ESCENA 33 (Viñeta #33 del Storyboard) — 05:20–05:30
- Location: Hale lighthouse kitchen, night, one lamp, rain outside
- Characters Present: Sam Calloway, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — Claire reads the emergency petition aloud.
  * [03s–07s]: tight close-up — Close detail on the harbor logbook; the room falls quiet around it.
  * [07s–10s]: medium shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  SAM (low): "Nora. Whatever happens in there... I should have told you the truth ten years ago."
  NORA (fierce): "Then tell it now. Loud enough for the back row."

ESCENA 34 (Viñeta #34 del Storyboard) — 05:30–05:40
- Location: Town hall hearing room, grey morning, rain streaking the windows
- Characters Present: Sam Calloway, Margaret Keller
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Nora stands in the empty lighthouse, the lamp cold above her.
  * [03s–07s]: tight close-up — Close detail on the cold lamp; the room falls quiet around it.
  * [07s–10s]: wide establishing shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, 6–8 sec max):
  SAM (public, shaking): "I signed a false statement. Margaret Keller wrote it. I was paid to stay quiet."
  MARGARET (dismissive): "He's a firefighter with a grudge."

ESCENA 35 (Viñeta #35 del Storyboard) — 05:40–05:50
- Location: Hale lighthouse, storm night, lightning through the glass
- Characters Present: Nora Hale, Adrian Keller
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: tight close-up — Sam signs a statement at the harbor office, hand shaking.
  * [03s–07s]: medium shot — Close detail on the emergency petition; the room falls quiet around it.
  * [07s–10s]: over-the-shoulder shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  NORA (calm): "Then let's hear from someone who can't be bought."
  ADRIAN (uneasy): "You're bluffing."
  NORA (flat): "I don't bluff. I document."

ESCENA 36 (Viñeta #36 del Storyboard) — 05:50–06:00
- Location: Hale lighthouse kitchen, night, one lamp, rain outside
- Characters Present: Nora Hale, Margaret Keller
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: over-the-shoulder shot — Nora listens through a half-open door, unseen.
  * [03s–07s]: tight close-up — Close detail on a statement form; the room falls quiet around it.
  * [07s–10s]: low-angle hero shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, 6–8 sec max):
  NORA (precise): "The harbor log. 2:14 a.m. Keller launch. Adrian at the helm."
  MARGARET (sharp): "That log is thirty years of weather and guesswork."

COMANDOS FINALES PARA PEGAR EN MUSE AI (ELIGE SEGÚN EL CANAL):

**Opción YouTube Monetización Long-Form (16:9 Horizontal):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_06.mp4)."

**Opción Reels / TikTok / Shorts (9:16 Vertical):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_06.mp4)."
```

**Comando final 16:9 (YouTube):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_06.mp4).

**Comando final 9:16 (Reels/Shorts):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_06.mp4).

### Lote 07 — Minuto 7 (escenas 37–42)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_07.png`

**Guardar como:** `raw_clips/minute_07.mp4`

**Bloque para Muse AI:**

```text
📎 ADJUNTAR EN MUSE AI: [1] REF_CAST_MASTER.png (Hoja de Personajes) + [2] REF_GRID_MIN_07.png (Storyboard Minuto 7: Escenas 37–42)

ESCENA 37 (Viñeta #37 del Storyboard) — 06:00–06:10
- Location: Town hall hearing room, grey morning, rain streaking the windows
- Characters Present: Nora Hale, Adrian Keller
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: low-angle hero shot — Nora walks the storm beach alone, hair plastered to her face.
  * [03s–07s]: tight close-up — Close detail on the harbor logbook; the room falls quiet around it.
  * [07s–10s]: medium shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  NORA (quiet): "2:14 a.m. One passenger. Margaret."
  ADRIAN (breaking): "It was an accident. We only meant to scare him."
  NORA (raw): "You burned a boathouse and let a town bury my father."

ESCENA 38 (Viñeta #38 del Storyboard) — 06:10–06:20
- Location: Hale lighthouse, storm night, lightning through the glass
- Characters Present: Nora Hale, Adrian Keller
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — Adrian waits in her kitchen with the sale papers.
  * [03s–07s]: tight close-up — Close detail on the cold lamp; the room falls quiet around it.
  * [07s–10s]: insert shot of the evidence object — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  NORA (cold): "You didn't scare him. You killed the only man who could prove it."
  ADRIAN (whisper): "He was already dead when we got there."

ESCENA 39 (Viñeta #39 del Storyboard) — 06:20–06:30
- Location: Hale lighthouse kitchen, night, one lamp, rain outside
- Characters Present: Nora Hale, Adrian Keller
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Nora stares into the lighthouse lens, thinking.
  * [03s–07s]: tight close-up — Close detail on the emergency petition; the room falls quiet around it.
  * [07s–10s]: over-the-shoulder shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  NORA (sharp): "Then who was in the boathouse with him?"
  ADRIAN (quiet): "Ask your mother."

ESCENA 40 (Viñeta #40 del Storyboard) — 06:30–06:40
- Location: Town hall hearing room, grey morning, rain streaking the windows
- Characters Present: Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: tight close-up — Nora finds an old harbor logbook behind the lens housing.
  * [03s–07s]: medium shot — Close detail on a statement form; the room falls quiet around it.
  * [07s–10s]: low-angle hero shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  NORA (hushed): "The harbor log. Every boat, every night. Dad, what did you see?"
  NORA (breaking): "And why did you hide it behind the lens?"

ESCENA 41 (Viñeta #41 del Storyboard) — 06:40–06:50
- Location: Hale lighthouse archive room, dawn, cold blue light
- Characters Present: Nora Hale, Sam Calloway
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: low-angle hero shot — Nora opens the logbook on the lighthouse table, pages brittle.
  * [03s–07s]: tight close-up — Close detail on the harbor log; the room falls quiet around it.
  * [07s–10s]: over-the-shoulder shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, 6–8 sec max):
  NORA (focused): "Every keeper signs the log. Date, time, weather. No exceptions."
  SAM (quiet): "Your father never missed a night."
  NORA (steady): "Then neither will I."

ESCENA 42 (Viñeta #42 del Storyboard) — 06:50–07:00
- Location: Harbor pier, morning, flat silver water
- Characters Present: Sam Calloway, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — Nora and Sam compare timestamps under a desk lamp.
  * [03s–07s]: tight close-up — Close detail on a torn page; the room falls quiet around it.
  * [07s–10s]: low-angle hero shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  SAM (grim): "The page from that night is torn out."
  NORA (triumphant whisper): "No. It's not torn. It's folded. He hid it behind the lens."

COMANDOS FINALES PARA PEGAR EN MUSE AI (ELIGE SEGÚN EL CANAL):

**Opción YouTube Monetización Long-Form (16:9 Horizontal):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_07.mp4)."

**Opción Reels / TikTok / Shorts (9:16 Vertical):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_07.mp4)."
```

**Comando final 16:9 (YouTube):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_07.mp4).

**Comando final 9:16 (Reels/Shorts):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_07.mp4).

### Lote 08 — Minuto 8 (escenas 43–48)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_08.png`

**Guardar como:** `raw_clips/minute_08.mp4`

**Bloque para Muse AI:**

```text
📎 ADJUNTAR EN MUSE AI: [1] REF_CAST_MASTER.png (Hoja de Personajes) + [2] REF_GRID_MIN_08.png (Storyboard Minuto 8: Escenas 43–48)

ESCENA 43 (Viñeta #43 del Storyboard) — 07:00–07:10
- Location: Town hall steps, dusk, wet stone
- Characters Present: Nora Hale, Sam Calloway
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Nora traces a line in the log with her finger.
  * [03s–07s]: tight close-up — Close detail on a timestamp; the room falls quiet around it.
  * [07s–10s]: insert shot of the evidence object — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, 6–8 sec max):
  NORA (urgent): "2:14 a.m. Keller launch. Two passengers, not one."
  SAM (low): "Who's the second?"
  NORA (cold): "Someone who signed as a witness."

ESCENA 44 (Viñeta #44 del Storyboard) — 07:10–07:20
- Location: Hale lighthouse archive room, dawn, cold blue light
- Characters Present: Sam Calloway, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: tight close-up — Sam reads over her shoulder, close enough to touch.
  * [03s–07s]: medium shot — Close detail on the town hall steps; the room falls quiet around it.
  * [07s–10s]: wide establishing shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  SAM (stunned): "Your mother's name."
  NORA (flat): "She died when I was eleven. I watched them bury her."
  SAM (quiet): "Then who's been paying the lighthouse taxes?"

ESCENA 45 (Viñeta #45 del Storyboard) — 07:20–07:30
- Location: Harbor pier, morning, flat silver water
- Characters Present: Nora Hale, Sam Calloway
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: over-the-shoulder shot — Nora looks up at Sam, a decision forming.
  * [03s–07s]: tight close-up — Close detail on the harbor log; the room falls quiet around it.
  * [07s–10s]: insert shot of the evidence object — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, 6–8 sec max):
  NORA (shaking): "Every year. In cash. Under my mother's maiden name."
  SAM (gentle): "Nora, look at me. We can still stop this."

ESCENA 46 (Viñeta #46 del Storyboard) — 07:30–07:40
- Location: Town hall steps, dusk, wet stone
- Characters Present: Adrian Keller, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: low-angle hero shot — Adrian stands on the town hall steps, trying to smile.
  * [03s–07s]: tight close-up — Close detail on a torn page; the room falls quiet around it.
  * [07s–10s]: insert shot of the evidence object — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  ADRIAN (reasonable): "The hearing is tomorrow. You have one night to change your mind."
  NORA (calm): "I've had ten years. I'm not changing anything."

ESCENA 47 (Viñeta #47 del Storyboard) — 07:40–07:50
- Location: Hale lighthouse archive room, dawn, cold blue light
- Characters Present: Margaret Keller, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — Nora walks past him without stopping.
  * [03s–07s]: tight close-up — Close detail on a timestamp; the room falls quiet around it.
  * [07s–10s]: medium shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  MARGARET (controlled): "You've made your point. Name a number."
  NORA (final): "The number is zero. You leave with nothing. That's the price."

ESCENA 48 (Viñeta #48 del Storyboard) — 07:50–08:00
- Location: Harbor pier, morning, flat silver water
- Characters Present: Claire Boone, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Margaret waits in the hall, gloves in hand.
  * [03s–07s]: tight close-up — Close detail on the town hall steps; the room falls quiet around it.
  * [07s–10s]: wide establishing shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  CLAIRE (worried): "If you present that log, the town will turn on the Kellers. And on your mother."
  NORA (steady): "Then they'll finally tell the truth about her."

COMANDOS FINALES PARA PEGAR EN MUSE AI (ELIGE SEGÚN EL CANAL):

**Opción YouTube Monetización Long-Form (16:9 Horizontal):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_08.mp4)."

**Opción Reels / TikTok / Shorts (9:16 Vertical):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_08.mp4)."
```

**Comando final 16:9 (YouTube):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_08.mp4).

**Comando final 9:16 (Reels/Shorts):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_08.mp4).

### Lote 09 — Minuto 9 (escenas 49–54)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_09.png`

**Guardar como:** `raw_clips/minute_09.mp4`

**Bloque para Muse AI:**

```text
📎 ADJUNTAR EN MUSE AI: [1] REF_CAST_MASTER.png (Hoja de Personajes) + [2] REF_GRID_MIN_09.png (Storyboard Minuto 9: Escenas 49–54)

ESCENA 49 (Viñeta #49 del Storyboard) — 08:00–08:10
- Location: Town hall steps, dusk, wet stone
- Characters Present: Nora Hale, Sam Calloway
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: tight close-up — Nora faces Margaret on the empty hearing floor.
  * [03s–07s]: medium shot — Close detail on the harbor log; the room falls quiet around it.
  * [07s–10s]: over-the-shoulder shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, 6–8 sec max):
  NORA (vulnerable): "Whatever they say about me tomorrow, I want you to hear it from me first."
  SAM (low): "I'm not going anywhere."

ESCENA 50 (Viñeta #50 del Storyboard) — 08:10–08:20
- Location: Hale lighthouse archive room, dawn, cold blue light
- Characters Present: Margaret Keller, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: over-the-shoulder shot — Nora stands at the lighthouse door as the town lights come on.
  * [03s–07s]: tight close-up — Close detail on a torn page; the room falls quiet around it.
  * [07s–10s]: low-angle hero shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  MARGARET (cold): "You'll lose the only home you have left."
  NORA (fierce): "I'm not doing this to keep the house. I'm doing it to keep his name."

ESCENA 51 (Viñeta #51 del Storyboard) — 08:20–08:30
- Location: Town hall hearing room, day, hard window light
- Characters Present: Claire Boone, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — The hearing room fills; Nora stands alone at the table.
  * [03s–07s]: tight close-up — Close detail on the harbor log; the room falls quiet around it.
  * [07s–10s]: over-the-shoulder shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  CLAIRE (nervous): "They're calling it an emergency hearing. Every seat is full."
  NORA (resolved): "Good. Let them watch. Let them remember."

ESCENA 52 (Viñeta #52 del Storyboard) — 08:30–08:40
- Location: Hale lighthouse point, golden hour, wind down
- Characters Present: Sam Calloway, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Sam steps to the microphone, the room silent.
  * [03s–07s]: tight close-up — Close detail on the clerk's desk; the room falls quiet around it.
  * [07s–10s]: low-angle hero shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  SAM (steady): "If I do this, I lose the department. I'm still doing it."
  NORA (gentle): "Then do it for the right reason."

ESCENA 53 (Viñeta #53 del Storyboard) — 08:40–08:50
- Location: Harbor, golden hour, calm water
- Characters Present: Nora Hale, Sam Calloway
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: tight close-up — Margaret's smile falters for the first time.
  * [03s–07s]: medium shot — Close detail on a second ledger; the room falls quiet around it.
  * [07s–10s]: insert shot of the evidence object — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, 6–8 sec max):
  NORA (quiet): "You don't have to prove anything to me. Just tell them the truth."
  SAM (breaking): "The truth is I let them bury your father."

ESCENA 54 (Viñeta #54 del Storyboard) — 08:50–09:00
- Location: Town hall hearing room, day, hard window light
- Characters Present: Sam Calloway, Margaret Keller
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: over-the-shoulder shot — Nora holds up the harbor log, open to the page.
  * [03s–07s]: tight close-up — Close detail on Sam's hand; the room falls quiet around it.
  * [07s–10s]: wide establishing shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, 6–8 sec max):
  SAM (public, clear): "I signed a false statement. Margaret Keller wrote it. I was paid to stay quiet."
  MARGARET (dismissive): "He's a firefighter with a grudge. Nothing he says survives cross."

COMANDOS FINALES PARA PEGAR EN MUSE AI (ELIGE SEGÚN EL CANAL):

**Opción YouTube Monetización Long-Form (16:9 Horizontal):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_09.mp4)."

**Opción Reels / TikTok / Shorts (9:16 Vertical):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_09.mp4)."
```

**Comando final 16:9 (YouTube):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_09.mp4).

**Comando final 9:16 (Reels/Shorts):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_09.mp4).

### Lote 10 — Minuto 10 (escenas 55–60)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_10.png`

**Guardar como:** `raw_clips/minute_10.mp4`

**Bloque para Muse AI:**

```text
📎 ADJUNTAR EN MUSE AI: [1] REF_CAST_MASTER.png (Hoja de Personajes) + [2] REF_GRID_MIN_10.png (Storyboard Minuto 10: Escenas 55–60)

ESCENA 55 (Viñeta #55 del Storyboard) — 09:00–09:10
- Location: Hale lighthouse point, golden hour, wind down
- Characters Present: Nora Hale, Adrian Keller
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: low-angle hero shot — Adrian half-rises from his chair.
  * [03s–07s]: tight close-up — Close detail on the harbor log; the room falls quiet around it.
  * [07s–10s]: over-the-shoulder shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  NORA (calm): "Then let's hear from someone who can't be bought. The harbor log."
  ADRIAN (uneasy): "That's a piece of paper."

ESCENA 56 (Viñeta #56 del Storyboard) — 09:10–09:20
- Location: Harbor, golden hour, calm water
- Characters Present: Nora Hale, Margaret Keller
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — Nora sets the log on the clerk's desk.
  * [03s–07s]: tight close-up — Close detail on the clerk's desk; the room falls quiet around it.
  * [07s–10s]: low-angle hero shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, 6–8 sec max):
  NORA (precise): "2:14 a.m. Keller launch. Two passengers. Adrian at the helm."
  MARGARET (sharp): "That log is thirty years of weather and guesswork."

ESCENA 57 (Viñeta #57 del Storyboard) — 09:20–09:30
- Location: Town hall hearing room, day, hard window light
- Characters Present: Nora Hale, Claire Boone
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Margaret reaches for the log; Nora slides it away.
  * [03s–07s]: tight close-up — Close detail on a second ledger; the room falls quiet around it.
  * [07s–10s]: insert shot of the evidence object — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; CLAIRE — grounded, plainspoken American English with a slight coastal New England softness
- Dialogue (English, 6–8 sec max):
  NORA (quiet): "One passenger is Margaret. The other signed the fire report."
  CLAIRE (stunned): "The fire marshal. It's his signature."

ESCENA 58 (Viñeta #58 del Storyboard) — 09:30–09:40
- Location: Hale lighthouse point, golden hour, wind down
- Characters Present: Adrian Keller, Nora Hale
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: tight close-up — Sam takes Nora's hand under the table.
  * [03s–07s]: medium shot — Close detail on Sam's hand; the room falls quiet around it.
  * [07s–10s]: wide establishing shot — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, 6–8 sec max):
  ADRIAN (breaking): "It was an accident. We only meant to scare him."
  NORA (raw): "You burned a boathouse and let a town bury my father for it."

ESCENA 59 (Viñeta #59 del Storyboard) — 09:40–09:50
- Location: Harbor, golden hour, calm water
- Characters Present: Nora Hale, Margaret Keller
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: over-the-shoulder shot — Nora walks out of the town hall into the light.
  * [03s–07s]: tight close-up — Close detail on the harbor log; the room falls quiet around it.
  * [07s–10s]: insert shot of the evidence object — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, 6–8 sec max):
  NORA (fierce): "That's not an accident. That's a choice. And this town gets to see it."
  MARGARET (quiet): "You'll regret this."

ESCENA 60 (Viñeta #60 del Storyboard) — 09:50–10:00
- Location: Town hall hearing room, day, hard window light
- Characters Present: Nora Hale, Sam Calloway
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: low-angle hero shot — Nora and Sam stand on the lighthouse point at dusk, an older ledger in Nora's hands.
  * [03s–07s]: tight close-up — Close detail on the clerk's desk; the room falls quiet around it.
  * [07s–10s]: insert shot of the evidence object — Nora Hale reacts, holding the moment before the next line.
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, 6–8 sec max):
  NORA (hushed): "Wait. This ledger is older. My mother's name is on every page."
  SAM (stunned): "Nora... she's alive?"
  NORA (cold): "She's been here the whole time."

COMANDOS FINALES PARA PEGAR EN MUSE AI (ELIGE SEGÚN EL CANAL):

**Opción YouTube Monetización Long-Form (16:9 Horizontal):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_10.mp4)."

**Opción Reels / TikTok / Shorts (9:16 Vertical):**

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_10.mp4)."
```

**Comando final 16:9 (YouTube):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 (guardar como raw_clips/minute_10.mp4).

**Comando final 9:16 (Reels/Shorts):**

> Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 (guardar como raw_clips/minute_10.mp4).

---

## Paso 4 — Ensamblar

Cuando existan los 10 archivos `minute_01.mp4 … minute_10.mp4`:

```powershell
./novelfactory.bat assemble demo_contract
```

El ensamblador detecta el modo B, genera el máster 16:9 de 10 minutos,
el SRT sincronizado y el teaser vertical automático de 20 segundos.

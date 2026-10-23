# The Silent Contract — Producción con Muse AI (método nuevo)

**Slug:** `demo_contract`  ·  **Escenas:** 60  ·  **Imágenes:** 11  ·  **Lotes:** 10

> **NOTA DE PRODUCCIÓN:** ADJUNTA EN CADA ESCENA: la viñeta de esa escena + las referencias SOLO de los personajes que salen en ESA escena + el prompt de esa escena. No generes ninguna escena sin sus personajes adjuntos.

> Ten years after the fire that ruined her family, Nora Hale returns to inherit a lighthouse and finds the town's most powerful family has been paying her dead mother's debts.

## Cómo funciona

1. Genera **una** hoja maestra de personajes con los rostros y vestuarios fijos.
2. Genera **10** storyboards (uno por minuto) usando esa hoja como referencia.
3. En Muse AI, sube la hoja maestra + el storyboard del minuto y pega el bloque del lote.
4. Guarda cada video como `raw_clips/minute_0X.mp4` y ejecuta el comando de ensamblaje.

> No necesitas frames por escena ni clips de 10 s: el ensamblador detecta los lotes de 1 minuto.

---

## Paso 1 — Hoja maestra de personajes

Guarda el resultado como `storyboards/REF_CAST_MASTER.png`.

**Prompt:**

```text
Actúa como director de casting y diseñador de personajes. Genera UNA SOLA IMAGEN horizontal 16:9 que muestre juntos, de cuerpo completo, de pie, mirando al frente sobre un fondo gris neutro de estudio (#808080) y sin tocarse entre sí, a los siguientes personajes de nuestra novela en estilo Cinematográfico Realista 35mm:

Position #1 (Far Left) — NORA HALE. Rol: Protagonista. Edad: early-thirties. Rasgos físicos: early thirties coastal New England woman, wiry build, dark auburn hair worn loose, storm-grey eyes, fair weathered skin, charcoal wool coat over a dark sweater. Vestuario fijo: el vestuario principal descrito en su ficha de casting.
Position #2 — SAM CALLOWAY. Rol: Interés romántico. Edad: mid-thirties. Rasgos físicos: mid-thirties harbor firefighter, broad-shouldered, short dark-sand hair, hazel eyes, tanned skin with salt creases, faded canvas work jacket. Vestuario fijo: faded canvas work jacket, dark trousers, worn boots.
Position #3 — MARGARET KELLER. Rol: Antagonista. Edad: late-sixties. Rasgos físicos: late sixties matriarch, tall and straight-backed, silver hair in a low chignon, pale blue eyes, porcelain skin, tailored dove-grey suit and pearls. Vestuario fijo: tailored dove-grey suit, pearls, low-heeled shoes.
Position #4 — ADRIAN KELLER. Rol: Heredero antagonista. Edad: late-thirties. Rasgos físicos: late thirties heir, lean and groomed, ash-blond hair swept back, cold grey eyes, even features, navy blazer over an open collar. Vestuario fijo: navy blazer, open-collared white shirt, dark trousers.
Position #5 (Far Right) — CLAIRE BOONE. Rol: Aliada. Edad: forties. Rasgos físicos: forties small-town lawyer, compact and practical, brown hair in a blunt bob, warm brown eyes, reading glasses on a cord, forest-green cardigan. Vestuario fijo: forest-green cardigan, cream blouse, dark trousers.

Ordena a los personajes de izquierda a derecha y coloca debajo de cada uno únicamente 'Position #N — NOMBRE EN MAYÚSCULAS'. Mantén exactamente las mismas posiciones, rostros, peinados y vestuarios en todas las imágenes del storyboard y de los lotes de Muse AI. Sin texto adicional, sin títulos, sin frases, sin logos, sin marcas de agua; solo la imagen de los personajes y sus posiciones.
```

---

## Paso 2 — Storyboards (10 imágenes)

Genera cada imagen con el mismo estilo y los mismos personajes de la hoja maestra.
Guarda cada archivo en `storyboards/` con el nombre indicado.

### REF_GRID_MIN_01.png — Minuto 1 (escenas 1–6)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 1 (Escenas 1 a 6) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 1 (Hale lighthouse cliff edge, storm dusk, wind and salt spray): [00s-07s] wide establishing shot, face and mouth visible: Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora stands at the cliff edge, the lighthouse dark behind her, salt wind whipping her coat. Key object in frame: a brass key. Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray. Characters present: Nora Hale. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair).
Viñeta 2 — Escena 2 (Keller harbor boardwalk, blue hour, wet planks and dock lights): [00s-07s] close-up, face and mouth visible: Sam Calloway is on camera with face and mouth fully visible, looking at Nora Hale. Sam Calloway speaks as the camera holds close on their face, the deed catching the light between them. Location: Keller harbor boardwalk, blue hour, wet planks and dock lights. Key object: the deed. Characters present: Nora Hale, Sam Calloway. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots).
Viñeta 3 — Escena 3 (Hale lighthouse kitchen, night, one warm lamp and a cold stove): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam leans against a harbor truck with his arms crossed, trying not to smile. Key object in frame: fresh survey stakes. Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove. Characters present: Nora Hale, Sam Calloway. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots).
Viñeta 4 — Escena 4 (Hale lighthouse cliff edge, storm dusk, wind and salt spray): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora sets a brass key on the lighthouse kitchen table between them. Key object in frame: the dead lighthouse lamp. Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray. Characters present: Nora Hale, Sam Calloway. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots).
Viñeta 5 — Escena 5 (Keller harbor boardwalk, blue hour, wet planks and dock lights): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam points through the rain at fresh survey stakes driven into the cliff. Key object in frame: a brass key. Location: Keller harbor boardwalk, blue hour, wet planks and dock lights. Characters present: Nora Hale, Sam Calloway, Margaret Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes).
Viñeta 6 — Escena 6 (Hale lighthouse kitchen, night, one warm lamp and a cold stove): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret waits under the dry awning of the Keller estate, gloves folded. Key object in frame: the deed. Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove. Characters present: Nora Hale, Margaret Keller, Adrian Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_02.png — Minuto 2 (escenas 7–12)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 2 (Escenas 7 a 12) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 7 (Hale lighthouse cliff edge, storm dusk, wind and salt spray): [00s-07s] two-shot, medium shot with Nora Hale and Margaret Keller: Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora reads the deed by a single warm lamp, jaw tight. Key object in frame: fresh survey stakes. Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray. Characters present: Nora Hale, Margaret Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes).
Viñeta 2 — Escena 8 (Keller harbor boardwalk, blue hour, wet planks and dock lights): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian blocks the lighthouse door with a folder under his arm. Key object in frame: the dead lighthouse lamp. Location: Keller harbor boardwalk, blue hour, wet planks and dock lights. Characters present: Nora Hale, Adrian Keller, Claire Boone. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers).
Viñeta 3 — Escena 9 (Hale lighthouse kitchen, night, one warm lamp and a cold stove): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stands alone on the point, the town lights small below her. Key object in frame: a brass key. Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove. Characters present: Nora Hale, Claire Boone. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers).
Viñeta 4 — Escena 10 (Hale lighthouse cliff edge, storm dusk, wind and salt spray): [00s-05s] low-angle hero shot, face and mouth visible: Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora crouches at the lighthouse base, finding a keyhole hidden under peeling paint. Key object in frame: the deed. Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray. Characters present: Nora Hale. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair).
Viñeta 5 — Escena 11 (Claire Boone's law office, grey morning, rain on the windows): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Claire slides a sealed envelope across the lawyer's desk. Key object in frame: the sealed petition. Location: Claire Boone's law office, grey morning, rain on the windows. Characters present: Nora Hale, Claire Boone. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers).
Viñeta 6 — Escena 12 (Keller boathouse, night, one hanging bulb and a flashlight): [00s-07s] two-shot, medium shot with Nora Hale and Claire Boone: Nora Hale and Claire Boone face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora reads the witness signature and looks up slowly. Key object in frame: a witness signature. Location: Keller boathouse, night, one hanging bulb and a flashlight. Characters present: Nora Hale, Claire Boone. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_03.png — Minuto 3 (escenas 13–18)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 3 (Escenas 13 a 18) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 13 (Keller estate, dusk, warm interior against blue windows): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam stands in the boathouse doorway, rain behind him. Key object in frame: a scorched beam. Location: Keller estate, dusk, warm interior against blue windows. Characters present: Nora Hale, Sam Calloway. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots).
Viñeta 2 — Escena 14 (Claire Boone's law office, grey morning, rain on the windows): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora sweeps a flashlight over scorched beams. Key object in frame: the survey map. Location: Claire Boone's law office, grey morning, rain on the windows. Characters present: Nora Hale, Sam Calloway, Claire Boone. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers).
Viñeta 3 — Escena 15 (Keller boathouse, night, one hanging bulb and a flashlight): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret pours tea without offering a cup. Key object in frame: the sealed petition. Location: Keller boathouse, night, one hanging bulb and a flashlight. Characters present: Nora Hale, Margaret Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes).
Viñeta 4 — Escena 16 (Keller estate, dusk, warm interior against blue windows): [00s-07s] two-shot, medium shot with Nora Hale and Adrian Keller: Nora Hale and Adrian Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stands in the town hall doorway as every head turns. Key object in frame: a witness signature. Location: Keller estate, dusk, warm interior against blue windows. Characters present: Nora Hale, Adrian Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers).
Viñeta 5 — Escena 17 (Boone law office, grey morning, rain on the windows): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian corners Nora by the harbor railing. Key object in frame: a scorched beam. Location: Boone law office, grey morning, rain on the windows. Characters present: Nora Hale, Sam Calloway, Adrian Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers).
Viñeta 6 — Escena 18 (Keller boathouse, night, one hanging bulb and a flashlight): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stares at a survey map pinned to the boathouse wall. Key object in frame: the survey map. Location: Keller boathouse, night, one hanging bulb and a flashlight. Characters present: Nora Hale, Sam Calloway. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_04.png — Minuto 4 (escenas 19–24)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 4 (Escenas 19 a 24) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 19 (Keller estate, dusk, warm interior against blue windows): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora Hale speaks as the camera holds close on their face, the sealed petition catching the light between them. Location: Keller estate, dusk, warm interior against blue windows. Key object: the sealed petition. Characters present: Nora Hale, Sam Calloway. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots).
Viñeta 2 — Escena 20 (Claire Boone's law office, grey morning, rain on the windows): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian holds the lighthouse door open, waiting. Key object in frame: a witness signature. Location: Claire Boone's law office, grey morning, rain on the windows. Characters present: Nora Hale, Adrian Keller, Claire Boone. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers).
Viñeta 3 — Escena 21 (Keller boathouse, night, flashlight and dust): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora spreads water-stained survey files across the lighthouse floor. Key object in frame: the metal evidence box. Location: Keller boathouse, night, flashlight and dust. Characters present: Nora Hale, Adrian Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers).
Viñeta 4 — Escena 22 (Hale lighthouse archive room, night, a single desk lamp): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam jimmies the boathouse lock with a pry bar. Key object in frame: the seawall permit. Location: Hale lighthouse archive room, night, a single desk lamp. Characters present: Nora Hale, Sam Calloway, Margaret Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes).
Viñeta 5 — Escena 23 (Harbor diner, dawn, cold fluorescent light and steam): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora's flashlight beam catches a metal box under the floorboards. Key object in frame: a folded page. Location: Harbor diner, dawn, cold fluorescent light and steam. Characters present: Nora Hale, Claire Boone. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers).
Viñeta 6 — Escena 24 (Keller boathouse, night, flashlight and dust): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam Calloway speaks as the camera holds close on their face, a diner coffee cup catching the light between them. Location: Keller boathouse, night, flashlight and dust. Key object: a diner coffee cup. Characters present: Nora Hale, Sam Calloway. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_05.png — Minuto 5 (escenas 25–30)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 5 (Escenas 25 a 30) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 25 (Hale lighthouse archive room, night, a single desk lamp): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora holds a permit signed by Margaret, dated before the fire. Key object in frame: the metal evidence box. Location: Hale lighthouse archive room, night, a single desk lamp. Characters present: Nora Hale, Margaret Keller, Adrian Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers).
Viñeta 2 — Escena 26 (Harbor diner, dawn, cold fluorescent light and steam): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora and Sam stand close in the archive, the file between them. Key object in frame: the seawall permit. Location: Harbor diner, dawn, cold fluorescent light and steam. Characters present: Nora Hale, Sam Calloway. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots).
Viñeta 3 — Escena 27 (Keller boathouse, night, flashlight and dust): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian waits in a diner booth across from Nora. Key object in frame: a folded page. Location: Keller boathouse, night, flashlight and dust. Characters present: Nora Hale, Sam Calloway, Adrian Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers).
Viñeta 4 — Escena 28 (Hale lighthouse archive room, night, a single desk lamp): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora slides the file across the table, keeping one page back. Key object in frame: a diner coffee cup. Location: Hale lighthouse archive room, night, a single desk lamp. Characters present: Nora Hale, Sam Calloway. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots).
Viñeta 5 — Escena 29 (Harbor diner, dawn, cold fluorescent light and steam): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian Keller speaks as the camera holds close on their face, the metal evidence box catching the light between them. Location: Harbor diner, dawn, cold fluorescent light and steam. Key object: the metal evidence box. Characters present: Nora Hale, Adrian Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers).
Viñeta 6 — Escena 30 (Keller boathouse, night, flashlight and dust): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret Keller speaks as the camera holds close on their face, the seawall permit catching the light between them. Location: Keller boathouse, night, flashlight and dust. Key object: the seawall permit. Characters present: Nora Hale, Margaret Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_06.png — Minuto 6 (escenas 31–36)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 6 (Escenas 31 a 36) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 31 (Town hall hearing room, grey morning, rain streaking the windows): [00s-07s] two-shot, medium shot with Nora Hale and Margaret Keller: Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Rain hammers the town hall windows as Nora faces the panel. Key object in frame: the emergency petition. Location: Town hall hearing room, grey morning, rain streaking the windows. Characters present: Nora Hale, Margaret Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes).
Viñeta 2 — Escena 32 (Town hall hearing room, grey morning, rain streaking the windows): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. The hearing room is packed; Claire leans close to Nora. Key object in frame: the emergency petition. Location: Town hall hearing room, grey morning, rain streaking the windows. Characters present: Nora Hale, Claire Boone. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers).
Viñeta 3 — Escena 33 (Town hall hearing room, grey morning, rain streaking the windows): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam catches Nora in the hearing room before she takes her seat. Key object in frame: a statement form. Location: Town hall hearing room, grey morning, rain streaking the windows. Characters present: Nora Hale, Sam Calloway. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots).
Viñeta 4 — Escena 34 (Town hall hearing room, grey morning, rain streaking the windows): [00s-07s] two-shot, medium shot with Sam Calloway and Margaret Keller: Sam Calloway and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam Calloway speaks as the camera holds close on their face, a statement form catching the light between them. Location: Town hall hearing room, grey morning, rain streaking the windows. Key object: a statement form. Characters present: Sam Calloway, Margaret Keller. No other characters appear. Identity anchors: Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes).
Viñeta 5 — Escena 35 (Town hall hearing room, grey morning, rain streaking the windows): [00s-04s] tight close-up, face and mouth visible: Nora Hale is on camera with face and mouth fully visible, looking at Adrian Keller. Nora faces Adrian across the hearing room. Key object in frame: the petition ruling. Location: Town hall hearing room, grey morning, rain streaking the windows. Characters present: Nora Hale, Adrian Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers).
Viñeta 6 — Escena 36 (Town hall hearing room, grey morning, rain streaking the windows): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. The clerk stamps the petition; the room goes silent. Key object in frame: the petition ruling. Location: Town hall hearing room, grey morning, rain streaking the windows. Characters present: Nora Hale, Margaret Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_07.png — Minuto 7 (escenas 37–42)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 7 (Escenas 37 a 42) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 37 (Hale lighthouse, storm night, lightning through the glass): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. At the lighthouse door, Margaret holds out the eviction notice. Location: Hale lighthouse, storm night, lightning through the glass. Key object: the eviction notice. Characters present: Nora Hale, Margaret Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes).
Viñeta 2 — Escena 38 (Hale lighthouse, night, one lamp, rain outside): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian waits in the lighthouse with the sale papers. Location: Hale lighthouse, night, one lamp, rain outside. Key object: the sale papers. Characters present: Nora Hale, Adrian Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers).
Viñeta 3 — Escena 39 (Hale lighthouse, storm night, lightning through the glass): [00s-07s] medium shot, face and mouth visible: Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora stands alone in the dark lighthouse, the cold lens above her. Key object in frame: the cold lamp. Location: Hale lighthouse, storm night, lightning through the glass. Characters present: Nora Hale. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down).
Viñeta 4 — Escena 40 (Hale lighthouse, storm night, lightning through the glass): [00s-04s] tight close-up, face and mouth visible: Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora finds an old harbor logbook behind the lens housing. Key object in frame: the harbor logbook. Location: Hale lighthouse, storm night, lightning through the glass. Characters present: Nora Hale. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down).
Viñeta 5 — Escena 41 (Hale lighthouse archive room, dawn, cold blue light): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora opens the logbook on the lighthouse table, pages brittle. Key object in frame: the harbor log. Location: Hale lighthouse archive room, dawn, cold blue light. Characters present: Nora Hale, Sam Calloway. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots).
Viñeta 6 — Escena 42 (Harbor pier, morning, flat silver water): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora and Sam compare timestamps under a desk lamp. Key object in frame: a torn page. Location: Harbor pier, morning, flat silver water. Characters present: Nora Hale, Sam Calloway. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_08.png — Minuto 8 (escenas 43–48)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 8 (Escenas 43 a 48) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 43 (Town hall steps, dusk, wet stone): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora Hale speaks as the camera holds close on their face, a timestamp catching the light between them. Location: Town hall steps, dusk, wet stone. Key object: a timestamp. Characters present: Nora Hale, Sam Calloway. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots).
Viñeta 2 — Escena 44 (Hale lighthouse archive room, dawn, cold blue light): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam reads over her shoulder, close enough to touch. Key object in frame: the town hall steps. Location: Hale lighthouse archive room, dawn, cold blue light. Characters present: Nora Hale, Sam Calloway. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots).
Viñeta 3 — Escena 45 (Harbor pier, morning, flat silver water): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora looks up at Sam, a decision forming. Key object in frame: the harbor log. Location: Harbor pier, morning, flat silver water. Characters present: Nora Hale, Sam Calloway. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots).
Viñeta 4 — Escena 46 (Town hall steps, dusk, wet stone): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian stands on the town hall steps, trying to smile. Key object in frame: a torn page. Location: Town hall steps, dusk, wet stone. Characters present: Nora Hale, Adrian Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers).
Viñeta 5 — Escena 47 (Hale lighthouse archive room, dawn, cold blue light): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora walks past him without stopping. Key object in frame: a timestamp. Location: Hale lighthouse archive room, dawn, cold blue light. Characters present: Nora Hale, Margaret Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes).
Viñeta 6 — Escena 48 (Harbor pier, morning, flat silver water): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret waits in the hall, gloves in hand. Key object in frame: the town hall steps. Location: Harbor pier, morning, flat silver water. Characters present: Nora Hale, Margaret Keller, Claire Boone. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_09.png — Minuto 9 (escenas 49–54)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 9 (Escenas 49 a 54) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 49 (Town hall steps, dusk, wet stone): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora faces Margaret on the empty hearing floor. Key object in frame: the harbor log. Location: Town hall steps, dusk, wet stone. Characters present: Nora Hale, Sam Calloway, Margaret Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes).
Viñeta 2 — Escena 50 (Hale lighthouse archive room, dawn, cold blue light): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stands at the lighthouse door as the town lights come on. Key object in frame: a torn page. Location: Hale lighthouse archive room, dawn, cold blue light. Characters present: Nora Hale, Margaret Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes).
Viñeta 3 — Escena 51 (Town hall hearing room, day, hard window light): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. The hearing room fills; Nora stands alone at the table. Key object in frame: the harbor log. Location: Town hall hearing room, day, hard window light. Characters present: Nora Hale, Claire Boone. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers).
Viñeta 4 — Escena 52 (Hale lighthouse point, golden hour, wind down): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam steps to the microphone, the room silent. Key object in frame: the clerk's desk. Location: Hale lighthouse point, golden hour, wind down. Characters present: Nora Hale, Sam Calloway. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots).
Viñeta 5 — Escena 53 (Harbor, golden hour, calm water): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret's smile falters for the first time. Key object in frame: a second ledger. Location: Harbor, golden hour, calm water. Characters present: Nora Hale, Sam Calloway, Margaret Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes).
Viñeta 6 — Escena 54 (Town hall hearing room, day, hard window light): [00s-07s] two-shot, medium shot with Sam Calloway and Margaret Keller: Sam Calloway and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora holds up the harbor log, open to the page. Key object in frame: Sam's hand. Location: Town hall hearing room, day, hard window light. Characters present: Nora Hale, Sam Calloway, Margaret Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_10.png — Minuto 10 (escenas 55–60)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 10 (Escenas 55 a 60) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 55 (Hale lighthouse point, golden hour, wind down): [00s-07s] two-shot, medium shot with Nora Hale and Adrian Keller: Nora Hale and Adrian Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian half-rises from his chair. Key object in frame: the harbor log. Location: Hale lighthouse point, golden hour, wind down. Characters present: Nora Hale, Adrian Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers).
Viñeta 2 — Escena 56 (Harbor, golden hour, calm water): [00s-07s] two-shot, medium shot with Nora Hale and Margaret Keller: Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora sets the log on the clerk's desk. Location: Harbor, golden hour, calm water. Key object: the clerk's desk. Characters present: Nora Hale, Margaret Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes).
Viñeta 3 — Escena 57 (Town hall hearing room, day, hard window light): [00s-07s] two-shot, medium shot with Nora Hale and Claire Boone: Nora Hale and Claire Boone face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret reaches for the log; Nora slides it away. Key object in frame: a second ledger. Location: Town hall hearing room, day, hard window light. Characters present: Nora Hale, Margaret Keller, Claire Boone. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers).
Viñeta 4 — Escena 58 (Hale lighthouse point, golden hour, wind down): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian Keller speaks as the camera holds close on their face, Sam's hand catching the light between them. Location: Hale lighthouse point, golden hour, wind down. Key object: Sam's hand. Characters present: Nora Hale, Sam Calloway, Adrian Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers).
Viñeta 5 — Escena 59 (Harbor, golden hour, calm water): [00s-07s] two-shot, medium shot with Nora Hale and Margaret Keller: Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora walks out of the town hall into the light. Key object in frame: the harbor log. Location: Harbor, golden hour, calm water. Characters present: Nora Hale, Margaret Keller. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes).
Viñeta 6 — Escena 60 (Town hall hearing room, day, hard window light): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora Hale speaks as the camera holds close on their face, the clerk's desk catching the light between them. Location: Town hall hearing room, day, hard window light. Key object: the clerk's desk. Characters present: Nora Hale, Sam Calloway. No other characters appear. Identity anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

---

## Paso 3 — Lotes Muse AI (10 videos de 1 minuto)

En cada lote: adjunta los dos archivos indicados y pega **un guion completo**
(16:9 para YouTube o 9:16 para Reels/Shorts). El guion ya termina con el comando final.

### Lote 01 — Minuto 1 (escenas 1–6)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_01.png`

**Adjuntos por escena de este lote:**

- Escena 001: `attach: [panel_001, ref_nora]`
- Escena 002: `attach: [panel_002, ref_nora, ref_sam]`
- Escena 003: `attach: [panel_003, ref_nora, ref_sam]`
- Escena 004: `attach: [panel_004, ref_nora, ref_sam]`
- Escena 005: `attach: [panel_005, ref_nora, ref_sam, ref_margaret]`
- Escena 006: `attach: [panel_006, ref_nora, ref_margaret, ref_adrian]`

**Guardar 16:9 como:** `raw_clips/minute_01.mp4`

**Guardar 9:16 como:** `raw_clips/minute_01_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 1 (Viñeta #1 del Storyboard) — 00:00–00:10
- Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray
- Characters Present: Nora Hale
- Storyboard Panel (Shot 1 exact framing): [00s-07s] wide establishing shot, face and mouth visible: Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora stands at the cliff edge, the lighthouse dark behind her, salt wind whipping her coat. Key object in frame: a brass key. Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray. Characters present: Nora Hale. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair)
- Key Object: a brass key → Object In / Object Out: a brass key → a brass key
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: wide establishing shot, face and mouth visible — Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora stands at the cliff edge, the lighthouse dark behind her, salt wind whipping her coat. Key object in frame: a brass key  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, a brass key catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — The silence hangs, a brass key sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (cold, quiet): "They said the lighthouse was empty for ten years. So who left the light on?"

ESCENA 2 (Viñeta #2 del Storyboard) — 00:10–00:20
- Location: Keller harbor boardwalk, blue hour, wet planks and dock lights
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] close-up, face and mouth visible: Sam Calloway is on camera with face and mouth fully visible, looking at Nora Hale. Sam Calloway speaks as the camera holds close on their face, the deed catching the light between them. Location: Keller harbor boardwalk, blue hour, wet planks and dock lights. Key object: the deed. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the deed → Object In / Object Out: the deed → the deed
- Silent Present: Nora Hale — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: close-up, face and mouth visible — Sam Calloway is on camera with face and mouth fully visible, looking at Nora Hale. Sam Calloway speaks as the camera holds close on their face, the deed catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: medium shot — Nora steps off the ferry with one duffel bag, the town sign behind her. Key object in frame: the deed  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Nora Hale holds the silence after the line, the deed sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (dry, warm): "Nora Hale. Ten years, and you still drive like a storm."

ESCENA 3 (Viñeta #3 del Storyboard) — 00:20–00:30
- Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam leans against a harbor truck with his arms crossed, trying not to smile. Key object in frame: fresh survey stakes. Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: fresh survey stakes → Object In / Object Out: fresh survey stakes → fresh survey stakes
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam leans against a harbor truck with his arms crossed, trying not to smile. Key object in frame: fresh survey stakes  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, fresh survey stakes catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, fresh survey stakes sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (guarded): "I inherited a lighthouse, Sam. Not a welcome party."
  SAM (low): "I'm not happy. I'm careful."

ESCENA 4 (Viñeta #4 del Storyboard) — 00:30–00:40
- Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora sets a brass key on the lighthouse kitchen table between them. Key object in frame: the dead lighthouse lamp. Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the dead lighthouse lamp → Object In / Object Out: the dead lighthouse lamp → the dead lighthouse lamp
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora sets a brass key on the lighthouse kitchen table between them. Key object in frame: the dead lighthouse lamp  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, the dead lighthouse lamp catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, the dead lighthouse lamp sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (flat): "The Kellers already had surveyors on your land."
  NORA (steady): "Then explain it to the state."

ESCENA 5 (Viñeta #5 del Storyboard) — 00:40–00:50
- Location: Keller harbor boardwalk, blue hour, wet planks and dock lights
- Characters Present: Nora Hale, Sam Calloway, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam points through the rain at fresh survey stakes driven into the cliff. Key object in frame: a brass key. Location: Keller harbor boardwalk, blue hour, wet planks and dock lights. Characters present: Nora Hale, Sam Calloway, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: a brass key → Object In / Object Out: a brass key → a brass key
- Silent Present: Sam Calloway — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Margaret Keller and Nora Hale — Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam points through the rain at fresh survey stakes driven into the cliff. Key object in frame: a brass key  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Margaret Keller stays silent as the camera holds close on their face, a brass key catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Margaret Keller holds the silence after the line, a brass key sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MARGARET (silk over steel): "Your father was a liar. The deed stands."
  NORA (quiet): "Then you won't mind me reading it."

ESCENA 6 (Viñeta #6 del Storyboard) — 00:50–01:00
- Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove
- Characters Present: Nora Hale, Margaret Keller, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret waits under the dry awning of the Keller estate, gloves folded. Key object in frame: the deed. Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove. Characters present: Nora Hale, Margaret Keller, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: the deed → Object In / Object Out: the deed → the deed
- Silent Present: Margaret Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Adrian Keller and Nora Hale — Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret waits under the dry awning of the Keller estate, gloves folded. Key object in frame: the deed  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Adrian Keller stays silent as the camera holds close on their face, the deed catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Adrian Keller holds the silence after the line, the deed sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ADRIAN (reasonable, rehearsed): "Sell us the point. Name your price."
  NORA (cold): "You only ask me to leave the past."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 1 (Viñeta #1 del Storyboard) — 00:00–00:10
- Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray
- Characters Present: Nora Hale
- Storyboard Panel (Shot 1 exact framing): [00s-07s] wide establishing shot, face and mouth visible: Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora stands at the cliff edge, the lighthouse dark behind her, salt wind whipping her coat. Key object in frame: a brass key. Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray. Characters present: Nora Hale. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair)
- Key Object: a brass key → Object In / Object Out: a brass key → a brass key
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: wide establishing shot, face and mouth visible — Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora stands at the cliff edge, the lighthouse dark behind her, salt wind whipping her coat. Key object in frame: a brass key  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, a brass key catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — The silence hangs, a brass key sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (cold, quiet): "They said the lighthouse was empty for ten years. So who left the light on?"

ESCENA 2 (Viñeta #2 del Storyboard) — 00:10–00:20
- Location: Keller harbor boardwalk, blue hour, wet planks and dock lights
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] close-up, face and mouth visible: Sam Calloway is on camera with face and mouth fully visible, looking at Nora Hale. Sam Calloway speaks as the camera holds close on their face, the deed catching the light between them. Location: Keller harbor boardwalk, blue hour, wet planks and dock lights. Key object: the deed. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the deed → Object In / Object Out: the deed → the deed
- Silent Present: Nora Hale — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: close-up, face and mouth visible — Sam Calloway is on camera with face and mouth fully visible, looking at Nora Hale. Sam Calloway speaks as the camera holds close on their face, the deed catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: medium shot — Nora steps off the ferry with one duffel bag, the town sign behind her. Key object in frame: the deed  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Nora Hale holds the silence after the line, the deed sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (dry, warm): "Nora Hale. Ten years, and you still drive like a storm."

ESCENA 3 (Viñeta #3 del Storyboard) — 00:20–00:30
- Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam leans against a harbor truck with his arms crossed, trying not to smile. Key object in frame: fresh survey stakes. Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: fresh survey stakes → Object In / Object Out: fresh survey stakes → fresh survey stakes
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam leans against a harbor truck with his arms crossed, trying not to smile. Key object in frame: fresh survey stakes  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, fresh survey stakes catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, fresh survey stakes sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (guarded): "I inherited a lighthouse, Sam. Not a welcome party."
  SAM (low): "I'm not happy. I'm careful."

ESCENA 4 (Viñeta #4 del Storyboard) — 00:30–00:40
- Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora sets a brass key on the lighthouse kitchen table between them. Key object in frame: the dead lighthouse lamp. Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the dead lighthouse lamp → Object In / Object Out: the dead lighthouse lamp → the dead lighthouse lamp
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora sets a brass key on the lighthouse kitchen table between them. Key object in frame: the dead lighthouse lamp  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, the dead lighthouse lamp catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, the dead lighthouse lamp sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (flat): "The Kellers already had surveyors on your land."
  NORA (steady): "Then explain it to the state."

ESCENA 5 (Viñeta #5 del Storyboard) — 00:40–00:50
- Location: Keller harbor boardwalk, blue hour, wet planks and dock lights
- Characters Present: Nora Hale, Sam Calloway, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam points through the rain at fresh survey stakes driven into the cliff. Key object in frame: a brass key. Location: Keller harbor boardwalk, blue hour, wet planks and dock lights. Characters present: Nora Hale, Sam Calloway, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: a brass key → Object In / Object Out: a brass key → a brass key
- Silent Present: Sam Calloway — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Margaret Keller and Nora Hale — Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam points through the rain at fresh survey stakes driven into the cliff. Key object in frame: a brass key  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Margaret Keller stays silent as the camera holds close on their face, a brass key catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Margaret Keller holds the silence after the line, a brass key sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MARGARET (silk over steel): "Your father was a liar. The deed stands."
  NORA (quiet): "Then you won't mind me reading it."

ESCENA 6 (Viñeta #6 del Storyboard) — 00:50–01:00
- Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove
- Characters Present: Nora Hale, Margaret Keller, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret waits under the dry awning of the Keller estate, gloves folded. Key object in frame: the deed. Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove. Characters present: Nora Hale, Margaret Keller, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: the deed → Object In / Object Out: the deed → the deed
- Silent Present: Margaret Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Adrian Keller and Nora Hale — Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret waits under the dry awning of the Keller estate, gloves folded. Key object in frame: the deed  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Adrian Keller stays silent as the camera holds close on their face, the deed catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Adrian Keller holds the silence after the line, the deed sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ADRIAN (reasonable, rehearsed): "Sell us the point. Name your price."
  NORA (cold): "You only ask me to leave the past."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 02 — Minuto 2 (escenas 7–12)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_02.png`

**Adjuntos por escena de este lote:**

- Escena 007: `attach: [panel_007, ref_nora, ref_margaret]`
- Escena 008: `attach: [panel_008, ref_nora, ref_adrian, ref_claire]`
- Escena 009: `attach: [panel_009, ref_nora, ref_claire]`
- Escena 010: `attach: [panel_010, ref_nora]`
- Escena 011: `attach: [panel_011, ref_nora, ref_claire]`
- Escena 012: `attach: [panel_012, ref_nora, ref_claire]`

**Guardar 16:9 como:** `raw_clips/minute_02.mp4`

**Guardar 9:16 como:** `raw_clips/minute_02_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 7 (Viñeta #7 del Storyboard) — 01:00–01:10
- Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Margaret Keller: Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora reads the deed by a single warm lamp, jaw tight. Key object in frame: fresh survey stakes. Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: fresh survey stakes → Object In / Object Out: fresh survey stakes → fresh survey stakes
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Margaret Keller — Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora reads the deed by a single warm lamp, jaw tight. Key object in frame: fresh survey stakes  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, fresh survey stakes catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, fresh survey stakes sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (suspicious): "Ten years. Why wait until I came back?"
  MARGARET (pleasant): "A deed is cleaner than a funeral."

ESCENA 8 (Viñeta #8 del Storyboard) — 01:10–01:20
- Location: Keller harbor boardwalk, blue hour, wet planks and dock lights
- Characters Present: Nora Hale, Adrian Keller, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian blocks the lighthouse door with a folder under his arm. Key object in frame: the dead lighthouse lamp. Location: Keller harbor boardwalk, blue hour, wet planks and dock lights. Characters present: Nora Hale, Adrian Keller, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: the dead lighthouse lamp → Object In / Object Out: the dead lighthouse lamp → the dead lighthouse lamp
- Silent Present: Adrian Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Claire Boone and Nora Hale — Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian blocks the lighthouse door with a folder under his arm. Key object in frame: the dead lighthouse lamp  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Claire Boone stays silent as the camera holds close on their face, the dead lighthouse lamp catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Claire Boone holds the silence after the line, the dead lighthouse lamp sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  CLAIRE (careful): "Your father changed his will three days before he died."
  NORA (sharp): "Who witnessed it?"

ESCENA 9 (Viñeta #9 del Storyboard) — 01:20–01:30
- Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove
- Characters Present: Nora Hale, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stands alone on the point, the town lights small below her. Key object in frame: a brass key. Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove. Characters present: Nora Hale, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: a brass key → Object In / Object Out: a brass key → a brass key
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Claire Boone and Nora Hale — Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stands alone on the point, the town lights small below her. Key object in frame: a brass key  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Claire Boone stays silent as the camera holds close on their face, a brass key catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Claire Boone holds the silence after the line, a brass key sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  CLAIRE (quiet): "Margaret's attorney. And a man named Sam."
  NORA (low): "Sam was there that night?"

ESCENA 10 (Viñeta #10 del Storyboard) — 01:30–01:40
- Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray
- Characters Present: Nora Hale
- Storyboard Panel (Shot 1 exact framing): [00s-05s] low-angle hero shot, face and mouth visible: Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora crouches at the lighthouse base, finding a keyhole hidden under peeling paint. Key object in frame: the deed. Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray. Characters present: Nora Hale. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair)
- Key Object: the deed → Object In / Object Out: the deed → the deed
- Camera Cuts & Visual Action (10s):
  * [00s-05s]: low-angle hero shot, face and mouth visible — Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora crouches at the lighthouse base, finding a keyhole hidden under peeling paint. Key object in frame: the deed  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [05s-08s]: close-up, face and mouth visible — Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora Hale speaks as the camera holds close on their face, the deed catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: insert shot of the evidence object — The silence hangs, the deed sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (hushed): "Dad, what did you lock in the lighthouse?"
  NORA (breaking): "And why leave me the key?"

ESCENA 11 (Viñeta #11 del Storyboard) — 01:40–01:50
- Location: Claire Boone's law office, grey morning, rain on the windows
- Characters Present: Nora Hale, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Claire slides a sealed envelope across the lawyer's desk. Key object in frame: the sealed petition. Location: Claire Boone's law office, grey morning, rain on the windows. Characters present: Nora Hale, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: the sealed petition → Object In / Object Out: the sealed petition → the sealed petition
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Claire Boone and Nora Hale — Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Claire slides a sealed envelope across the lawyer's desk. Key object in frame: the sealed petition  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Claire Boone stays silent as the camera holds close on their face, the sealed petition catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Claire Boone holds the silence after the line, the sealed petition sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  CLAIRE (clinical): "The petition calls you unfit. They want a guardian by Friday."
  NORA (flat): "On what grounds?"

ESCENA 12 (Viñeta #12 del Storyboard) — 01:50–02:00
- Location: Keller boathouse, night, one hanging bulb and a flashlight
- Characters Present: Nora Hale, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Claire Boone: Nora Hale and Claire Boone face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora reads the witness signature and looks up slowly. Key object in frame: a witness signature. Location: Keller boathouse, night, one hanging bulb and a flashlight. Characters present: Nora Hale, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: a witness signature → Object In / Object Out: a witness signature → a witness signature
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Claire Boone — Nora Hale and Claire Boone face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora reads the witness signature and looks up slowly. Key object in frame: a witness signature  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, a witness signature catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Nora Hale holds the silence after the line, a witness signature sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; CLAIRE — grounded, plainspoken American English with a slight coastal New England softness
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (sharp): "Who signed the statement?"
  CLAIRE (quiet): "Half the harbor. And Sam."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 7 (Viñeta #7 del Storyboard) — 01:00–01:10
- Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Margaret Keller: Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora reads the deed by a single warm lamp, jaw tight. Key object in frame: fresh survey stakes. Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: fresh survey stakes → Object In / Object Out: fresh survey stakes → fresh survey stakes
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Margaret Keller — Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora reads the deed by a single warm lamp, jaw tight. Key object in frame: fresh survey stakes  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, fresh survey stakes catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, fresh survey stakes sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (suspicious): "Ten years. Why wait until I came back?"
  MARGARET (pleasant): "A deed is cleaner than a funeral."

ESCENA 8 (Viñeta #8 del Storyboard) — 01:10–01:20
- Location: Keller harbor boardwalk, blue hour, wet planks and dock lights
- Characters Present: Nora Hale, Adrian Keller, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian blocks the lighthouse door with a folder under his arm. Key object in frame: the dead lighthouse lamp. Location: Keller harbor boardwalk, blue hour, wet planks and dock lights. Characters present: Nora Hale, Adrian Keller, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: the dead lighthouse lamp → Object In / Object Out: the dead lighthouse lamp → the dead lighthouse lamp
- Silent Present: Adrian Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Claire Boone and Nora Hale — Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian blocks the lighthouse door with a folder under his arm. Key object in frame: the dead lighthouse lamp  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Claire Boone stays silent as the camera holds close on their face, the dead lighthouse lamp catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Claire Boone holds the silence after the line, the dead lighthouse lamp sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  CLAIRE (careful): "Your father changed his will three days before he died."
  NORA (sharp): "Who witnessed it?"

ESCENA 9 (Viñeta #9 del Storyboard) — 01:20–01:30
- Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove
- Characters Present: Nora Hale, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stands alone on the point, the town lights small below her. Key object in frame: a brass key. Location: Hale lighthouse kitchen, night, one warm lamp and a cold stove. Characters present: Nora Hale, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: a brass key → Object In / Object Out: a brass key → a brass key
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Claire Boone and Nora Hale — Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stands alone on the point, the town lights small below her. Key object in frame: a brass key  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Claire Boone stays silent as the camera holds close on their face, a brass key catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Claire Boone holds the silence after the line, a brass key sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  CLAIRE (quiet): "Margaret's attorney. And a man named Sam."
  NORA (low): "Sam was there that night?"

ESCENA 10 (Viñeta #10 del Storyboard) — 01:30–01:40
- Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray
- Characters Present: Nora Hale
- Storyboard Panel (Shot 1 exact framing): [00s-05s] low-angle hero shot, face and mouth visible: Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora crouches at the lighthouse base, finding a keyhole hidden under peeling paint. Key object in frame: the deed. Location: Hale lighthouse cliff edge, storm dusk, wind and salt spray. Characters present: Nora Hale. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat over a dark sweater, dark jeans, rain-wet hair)
- Key Object: the deed → Object In / Object Out: the deed → the deed
- Camera Cuts & Visual Action (10s):
  * [00s-05s]: low-angle hero shot, face and mouth visible — Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora crouches at the lighthouse base, finding a keyhole hidden under peeling paint. Key object in frame: the deed  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [05s-08s]: close-up, face and mouth visible — Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora Hale speaks as the camera holds close on their face, the deed catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: insert shot of the evidence object — The silence hangs, the deed sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, distant surf, a gull, wet gravel underfoot. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (hushed): "Dad, what did you lock in the lighthouse?"
  NORA (breaking): "And why leave me the key?"

ESCENA 11 (Viñeta #11 del Storyboard) — 01:40–01:50
- Location: Claire Boone's law office, grey morning, rain on the windows
- Characters Present: Nora Hale, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Claire slides a sealed envelope across the lawyer's desk. Key object in frame: the sealed petition. Location: Claire Boone's law office, grey morning, rain on the windows. Characters present: Nora Hale, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: the sealed petition → Object In / Object Out: the sealed petition → the sealed petition
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Claire Boone and Nora Hale — Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Claire slides a sealed envelope across the lawyer's desk. Key object in frame: the sealed petition  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Claire Boone stays silent as the camera holds close on their face, the sealed petition catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Claire Boone holds the silence after the line, the sealed petition sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  CLAIRE (clinical): "The petition calls you unfit. They want a guardian by Friday."
  NORA (flat): "On what grounds?"

ESCENA 12 (Viñeta #12 del Storyboard) — 01:50–02:00
- Location: Keller boathouse, night, one hanging bulb and a flashlight
- Characters Present: Nora Hale, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Claire Boone: Nora Hale and Claire Boone face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora reads the witness signature and looks up slowly. Key object in frame: a witness signature. Location: Keller boathouse, night, one hanging bulb and a flashlight. Characters present: Nora Hale, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: a witness signature → Object In / Object Out: a witness signature → a witness signature
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Claire Boone — Nora Hale and Claire Boone face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora reads the witness signature and looks up slowly. Key object in frame: a witness signature  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, a witness signature catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Nora Hale holds the silence after the line, a witness signature sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; CLAIRE — grounded, plainspoken American English with a slight coastal New England softness
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (sharp): "Who signed the statement?"
  CLAIRE (quiet): "Half the harbor. And Sam."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 03 — Minuto 3 (escenas 13–18)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_03.png`

**Adjuntos por escena de este lote:**

- Escena 013: `attach: [panel_013, ref_nora, ref_sam]`
- Escena 014: `attach: [panel_014, ref_nora, ref_sam, ref_claire]`
- Escena 015: `attach: [panel_015, ref_nora, ref_margaret]`
- Escena 016: `attach: [panel_016, ref_nora, ref_adrian]`
- Escena 017: `attach: [panel_017, ref_nora, ref_sam, ref_adrian]`
- Escena 018: `attach: [panel_018, ref_nora, ref_sam]`

**Guardar 16:9 como:** `raw_clips/minute_03.mp4`

**Guardar 9:16 como:** `raw_clips/minute_03_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 13 (Viñeta #13 del Storyboard) — 02:00–02:10
- Location: Keller estate, dusk, warm interior against blue windows
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam stands in the boathouse doorway, rain behind him. Key object in frame: a scorched beam. Location: Keller estate, dusk, warm interior against blue windows. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: a scorched beam → Object In / Object Out: a scorched beam → a scorched beam
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam stands in the boathouse doorway, rain behind him. Key object in frame: a scorched beam  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, a scorched beam catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Sam Calloway holds the silence after the line, a scorched beam sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (ashamed): "I signed a paper. I was twenty-two and scared."
  NORA (cutting): "Scared of being poor? Or her?"

ESCENA 14 (Viñeta #14 del Storyboard) — 02:10–02:20
- Location: Claire Boone's law office, grey morning, rain on the windows
- Characters Present: Nora Hale, Sam Calloway, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora sweeps a flashlight over scorched beams. Key object in frame: the survey map. Location: Claire Boone's law office, grey morning, rain on the windows. Characters present: Nora Hale, Sam Calloway, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: the survey map → Object In / Object Out: the survey map → the survey map
- Silent Present: Claire Boone — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora sweeps a flashlight over scorched beams. Key object in frame: the survey map  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, the survey map catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, the survey map sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (low): "The fire started in the boathouse, not the cliffs."
  NORA (raw): "Why did the town blame me?"

ESCENA 15 (Viñeta #15 del Storyboard) — 02:20–02:30
- Location: Keller boathouse, night, one hanging bulb and a flashlight
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret pours tea without offering a cup. Key object in frame: the sealed petition. Location: Keller boathouse, night, one hanging bulb and a flashlight. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the sealed petition → Object In / Object Out: the sealed petition → the sealed petition
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Margaret Keller and Nora Hale — Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret pours tea without offering a cup. Key object in frame: the sealed petition  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Margaret Keller stays silent as the camera holds close on their face, the sealed petition catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Margaret Keller holds the silence after the line, the sealed petition sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MARGARET (pleasant threat): "Reopen it, and the town remembers the match."
  NORA (tired): "I've played your villain ten years."

ESCENA 16 (Viñeta #16 del Storyboard) — 02:30–02:40
- Location: Keller estate, dusk, warm interior against blue windows
- Characters Present: Nora Hale, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Adrian Keller: Nora Hale and Adrian Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stands in the town hall doorway as every head turns. Key object in frame: a witness signature. Location: Keller estate, dusk, warm interior against blue windows. Characters present: Nora Hale, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: a witness signature → Object In / Object Out: a witness signature → a witness signature
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Adrian Keller — Nora Hale and Adrian Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stands in the town hall doorway as every head turns. Key object in frame: a witness signature  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, a witness signature catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Nora Hale holds the silence after the line, a witness signature sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (precise): "A debt doesn't transfer with land. Fraud does."
  ADRIAN (smiling): "Big words for someone with no lawyer."

ESCENA 17 (Viñeta #17 del Storyboard) — 02:40–02:50
- Location: Boone law office, grey morning, rain on the windows
- Characters Present: Nora Hale, Sam Calloway, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian corners Nora by the harbor railing. Key object in frame: a scorched beam. Location: Boone law office, grey morning, rain on the windows. Characters present: Nora Hale, Sam Calloway, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: a scorched beam → Object In / Object Out: a scorched beam → a scorched beam
- Silent Present: Adrian Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian corners Nora by the harbor railing. Key object in frame: a scorched beam  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, a scorched beam catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Sam Calloway holds the silence after the line, a scorched beam sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (urgent): "The old survey files are in the boathouse."
  NORA (decided): "Tonight, before the hearing."

ESCENA 18 (Viñeta #18 del Storyboard) — 02:50–03:00
- Location: Keller boathouse, night, one hanging bulb and a flashlight
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stares at a survey map pinned to the boathouse wall. Key object in frame: the survey map. Location: Keller boathouse, night, one hanging bulb and a flashlight. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the survey map → Object In / Object Out: the survey map → the survey map
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stares at a survey map pinned to the boathouse wall. Key object in frame: the survey map  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, the survey map catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, the survey map sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (dry): "You always liked bad ideas with good lighting."
  NORA (impatient): "You coming? Bring the pry bar."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 13 (Viñeta #13 del Storyboard) — 02:00–02:10
- Location: Keller estate, dusk, warm interior against blue windows
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam stands in the boathouse doorway, rain behind him. Key object in frame: a scorched beam. Location: Keller estate, dusk, warm interior against blue windows. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: a scorched beam → Object In / Object Out: a scorched beam → a scorched beam
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam stands in the boathouse doorway, rain behind him. Key object in frame: a scorched beam  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, a scorched beam catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Sam Calloway holds the silence after the line, a scorched beam sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (ashamed): "I signed a paper. I was twenty-two and scared."
  NORA (cutting): "Scared of being poor? Or her?"

ESCENA 14 (Viñeta #14 del Storyboard) — 02:10–02:20
- Location: Claire Boone's law office, grey morning, rain on the windows
- Characters Present: Nora Hale, Sam Calloway, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora sweeps a flashlight over scorched beams. Key object in frame: the survey map. Location: Claire Boone's law office, grey morning, rain on the windows. Characters present: Nora Hale, Sam Calloway, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: the survey map → Object In / Object Out: the survey map → the survey map
- Silent Present: Claire Boone — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora sweeps a flashlight over scorched beams. Key object in frame: the survey map  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, the survey map catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, the survey map sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (low): "The fire started in the boathouse, not the cliffs."
  NORA (raw): "Why did the town blame me?"

ESCENA 15 (Viñeta #15 del Storyboard) — 02:20–02:30
- Location: Keller boathouse, night, one hanging bulb and a flashlight
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret pours tea without offering a cup. Key object in frame: the sealed petition. Location: Keller boathouse, night, one hanging bulb and a flashlight. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the sealed petition → Object In / Object Out: the sealed petition → the sealed petition
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Margaret Keller and Nora Hale — Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret pours tea without offering a cup. Key object in frame: the sealed petition  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Margaret Keller stays silent as the camera holds close on their face, the sealed petition catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Margaret Keller holds the silence after the line, the sealed petition sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MARGARET (pleasant threat): "Reopen it, and the town remembers the match."
  NORA (tired): "I've played your villain ten years."

ESCENA 16 (Viñeta #16 del Storyboard) — 02:30–02:40
- Location: Keller estate, dusk, warm interior against blue windows
- Characters Present: Nora Hale, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Adrian Keller: Nora Hale and Adrian Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stands in the town hall doorway as every head turns. Key object in frame: a witness signature. Location: Keller estate, dusk, warm interior against blue windows. Characters present: Nora Hale, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: a witness signature → Object In / Object Out: a witness signature → a witness signature
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Adrian Keller — Nora Hale and Adrian Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stands in the town hall doorway as every head turns. Key object in frame: a witness signature  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, a witness signature catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Nora Hale holds the silence after the line, a witness signature sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (precise): "A debt doesn't transfer with land. Fraud does."
  ADRIAN (smiling): "Big words for someone with no lawyer."

ESCENA 17 (Viñeta #17 del Storyboard) — 02:40–02:50
- Location: Boone law office, grey morning, rain on the windows
- Characters Present: Nora Hale, Sam Calloway, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian corners Nora by the harbor railing. Key object in frame: a scorched beam. Location: Boone law office, grey morning, rain on the windows. Characters present: Nora Hale, Sam Calloway, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: a scorched beam → Object In / Object Out: a scorched beam → a scorched beam
- Silent Present: Adrian Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian corners Nora by the harbor railing. Key object in frame: a scorched beam  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, a scorched beam catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Sam Calloway holds the silence after the line, a scorched beam sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (urgent): "The old survey files are in the boathouse."
  NORA (decided): "Tonight, before the hearing."

ESCENA 18 (Viñeta #18 del Storyboard) — 02:50–03:00
- Location: Keller boathouse, night, one hanging bulb and a flashlight
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stares at a survey map pinned to the boathouse wall. Key object in frame: the survey map. Location: Keller boathouse, night, one hanging bulb and a flashlight. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the survey map → Object In / Object Out: the survey map → the survey map
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stares at a survey map pinned to the boathouse wall. Key object in frame: the survey map  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, the survey map catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, the survey map sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (dry): "You always liked bad ideas with good lighting."
  NORA (impatient): "You coming? Bring the pry bar."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 04 — Minuto 4 (escenas 19–24)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_04.png`

**Adjuntos por escena de este lote:**

- Escena 019: `attach: [panel_019, ref_nora, ref_sam]`
- Escena 020: `attach: [panel_020, ref_nora, ref_adrian, ref_claire]`
- Escena 021: `attach: [panel_021, ref_nora, ref_adrian]`
- Escena 022: `attach: [panel_022, ref_nora, ref_sam, ref_margaret]`
- Escena 023: `attach: [panel_023, ref_nora, ref_claire]`
- Escena 024: `attach: [panel_024, ref_nora, ref_sam]`

**Guardar 16:9 como:** `raw_clips/minute_04.mp4`

**Guardar 9:16 como:** `raw_clips/minute_04_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 19 (Viñeta #19 del Storyboard) — 03:00–03:10
- Location: Keller estate, dusk, warm interior against blue windows
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora Hale speaks as the camera holds close on their face, the sealed petition catching the light between them. Location: Keller estate, dusk, warm interior against blue windows. Key object: the sealed petition. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the sealed petition → Object In / Object Out: the sealed petition → the sealed petition
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora Hale speaks as the camera holds close on their face, the sealed petition catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: low-angle hero shot — Sam watches Nora from across the dock, unable to stays silent. Key object in frame: the sealed petition  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, the sealed petition sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (shaking): "Seawall permits. Signed by Margaret, before the fire."
  SAM (quiet): "That's not a permit. That's a motive."

ESCENA 20 (Viñeta #20 del Storyboard) — 03:10–03:20
- Location: Claire Boone's law office, grey morning, rain on the windows
- Characters Present: Nora Hale, Adrian Keller, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian holds the lighthouse door open, waiting. Key object in frame: a witness signature. Location: Claire Boone's law office, grey morning, rain on the windows. Characters present: Nora Hale, Adrian Keller, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: a witness signature → Object In / Object Out: a witness signature → a witness signature
- Silent Present: Claire Boone — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Adrian Keller and Nora Hale — Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian holds the lighthouse door open, waiting. Key object in frame: a witness signature  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Adrian Keller stays silent as the camera holds close on their face, a witness signature catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Adrian Keller holds the silence after the line, a witness signature sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ADRIAN (reasonable): "Give me the file. I'll call the fire an accident."
  NORA (wary): "In exchange for what?"

ESCENA 21 (Viñeta #21 del Storyboard) — 03:20–03:30
- Location: Keller boathouse, night, flashlight and dust
- Characters Present: Nora Hale, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora spreads water-stained survey files across the lighthouse floor. Key object in frame: the metal evidence box. Location: Keller boathouse, night, flashlight and dust. Characters present: Nora Hale, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: the metal evidence box → Object In / Object Out: the metal evidence box → the metal evidence box
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Adrian Keller and Nora Hale — Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora spreads water-stained survey files across the lighthouse floor. Key object in frame: the metal evidence box  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Adrian Keller stays silent as the camera holds close on their face, the metal evidence box catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Adrian Keller holds the silence after the line, the metal evidence box sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ADRIAN (incredulous): "You'd rather be the arsonist than my alibi?"
  NORA (flat): "I'd rather be alone than owned. Move."

ESCENA 22 (Viñeta #22 del Storyboard) — 03:30–03:40
- Location: Hale lighthouse archive room, night, a single desk lamp
- Characters Present: Nora Hale, Sam Calloway, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam jimmies the boathouse lock with a pry bar. Key object in frame: the seawall permit. Location: Hale lighthouse archive room, night, a single desk lamp. Characters present: Nora Hale, Sam Calloway, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the seawall permit → Object In / Object Out: the seawall permit → the seawall permit
- Silent Present: Sam Calloway — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Margaret Keller and Nora Hale — Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam jimmies the boathouse lock with a pry bar. Key object in frame: the seawall permit  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Margaret Keller stays silent as the camera holds close on their face, the seawall permit catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Margaret Keller holds the silence after the line, the seawall permit sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MARGARET (satisfied): "The trust is frozen. Emergency petition, effective this morning."
  NORA (steady): "On what grounds?"

ESCENA 23 (Viñeta #23 del Storyboard) — 03:40–03:50
- Location: Harbor diner, dawn, cold fluorescent light and steam
- Characters Present: Nora Hale, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora's flashlight beam catches a metal box under the floorboards. Key object in frame: a folded page. Location: Harbor diner, dawn, cold fluorescent light and steam. Characters present: Nora Hale, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: a folded page → Object In / Object Out: a folded page → a folded page
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Claire Boone and Nora Hale — Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora's flashlight beam catches a metal box under the floorboards. Key object in frame: a folded page  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Claire Boone stays silent as the camera holds close on their face, a folded page catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Claire Boone holds the silence after the line, a folded page sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  CLAIRE (gentle): "One of the statements is from Sam."
  NORA (low): "Tell me that's a lie. To my face."

ESCENA 24 (Viñeta #24 del Storyboard) — 03:50–04:00
- Location: Keller boathouse, night, flashlight and dust
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam Calloway speaks as the camera holds close on their face, a diner coffee cup catching the light between them. Location: Keller boathouse, night, flashlight and dust. Key object: a diner coffee cup. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: a diner coffee cup → Object In / Object Out: a diner coffee cup → a diner coffee cup
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam Calloway speaks as the camera holds close on their face, a diner coffee cup catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: wide establishing shot — Sam watches Nora read the permits, his face falling. Key object in frame: a diner coffee cup  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, a diner coffee cup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (broken): "They threatened my sister's job. I'm sorry."
  NORA (hard): "Don't apologize. Fix it."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 19 (Viñeta #19 del Storyboard) — 03:00–03:10
- Location: Keller estate, dusk, warm interior against blue windows
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora Hale speaks as the camera holds close on their face, the sealed petition catching the light between them. Location: Keller estate, dusk, warm interior against blue windows. Key object: the sealed petition. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the sealed petition → Object In / Object Out: the sealed petition → the sealed petition
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora Hale speaks as the camera holds close on their face, the sealed petition catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: low-angle hero shot — Sam watches Nora from across the dock, unable to stays silent. Key object in frame: the sealed petition  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, the sealed petition sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (shaking): "Seawall permits. Signed by Margaret, before the fire."
  SAM (quiet): "That's not a permit. That's a motive."

ESCENA 20 (Viñeta #20 del Storyboard) — 03:10–03:20
- Location: Claire Boone's law office, grey morning, rain on the windows
- Characters Present: Nora Hale, Adrian Keller, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian holds the lighthouse door open, waiting. Key object in frame: a witness signature. Location: Claire Boone's law office, grey morning, rain on the windows. Characters present: Nora Hale, Adrian Keller, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing charcoal wool coat, dark jeans, hair dry now, no umbrella); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: a witness signature → Object In / Object Out: a witness signature → a witness signature
- Silent Present: Claire Boone — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Adrian Keller and Nora Hale — Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian holds the lighthouse door open, waiting. Key object in frame: a witness signature  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Adrian Keller stays silent as the camera holds close on their face, a witness signature catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Adrian Keller holds the silence after the line, a witness signature sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): rain on windows, a ticking clock, tea poured, a door closing. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ADRIAN (reasonable): "Give me the file. I'll call the fire an accident."
  NORA (wary): "In exchange for what?"

ESCENA 21 (Viñeta #21 del Storyboard) — 03:20–03:30
- Location: Keller boathouse, night, flashlight and dust
- Characters Present: Nora Hale, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora spreads water-stained survey files across the lighthouse floor. Key object in frame: the metal evidence box. Location: Keller boathouse, night, flashlight and dust. Characters present: Nora Hale, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: the metal evidence box → Object In / Object Out: the metal evidence box → the metal evidence box
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Adrian Keller and Nora Hale — Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora spreads water-stained survey files across the lighthouse floor. Key object in frame: the metal evidence box  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Adrian Keller stays silent as the camera holds close on their face, the metal evidence box catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Adrian Keller holds the silence after the line, the metal evidence box sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ADRIAN (incredulous): "You'd rather be the arsonist than my alibi?"
  NORA (flat): "I'd rather be alone than owned. Move."

ESCENA 22 (Viñeta #22 del Storyboard) — 03:30–03:40
- Location: Hale lighthouse archive room, night, a single desk lamp
- Characters Present: Nora Hale, Sam Calloway, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam jimmies the boathouse lock with a pry bar. Key object in frame: the seawall permit. Location: Hale lighthouse archive room, night, a single desk lamp. Characters present: Nora Hale, Sam Calloway, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the seawall permit → Object In / Object Out: the seawall permit → the seawall permit
- Silent Present: Sam Calloway — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Margaret Keller and Nora Hale — Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam jimmies the boathouse lock with a pry bar. Key object in frame: the seawall permit  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Margaret Keller stays silent as the camera holds close on their face, the seawall permit catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Margaret Keller holds the silence after the line, the seawall permit sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MARGARET (satisfied): "The trust is frozen. Emergency petition, effective this morning."
  NORA (steady): "On what grounds?"

ESCENA 23 (Viñeta #23 del Storyboard) — 03:40–03:50
- Location: Harbor diner, dawn, cold fluorescent light and steam
- Characters Present: Nora Hale, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora's flashlight beam catches a metal box under the floorboards. Key object in frame: a folded page. Location: Harbor diner, dawn, cold fluorescent light and steam. Characters present: Nora Hale, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: a folded page → Object In / Object Out: a folded page → a folded page
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Claire Boone and Nora Hale — Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora's flashlight beam catches a metal box under the floorboards. Key object in frame: a folded page  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Claire Boone stays silent as the camera holds close on their face, a folded page catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Claire Boone holds the silence after the line, a folded page sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  CLAIRE (gentle): "One of the statements is from Sam."
  NORA (low): "Tell me that's a lie. To my face."

ESCENA 24 (Viñeta #24 del Storyboard) — 03:50–04:00
- Location: Keller boathouse, night, flashlight and dust
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam Calloway speaks as the camera holds close on their face, a diner coffee cup catching the light between them. Location: Keller boathouse, night, flashlight and dust. Key object: a diner coffee cup. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: a diner coffee cup → Object In / Object Out: a diner coffee cup → a diner coffee cup
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam Calloway speaks as the camera holds close on their face, a diner coffee cup catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: wide establishing shot — Sam watches Nora read the permits, his face falling. Key object in frame: a diner coffee cup  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, a diner coffee cup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (broken): "They threatened my sister's job. I'm sorry."
  NORA (hard): "Don't apologize. Fix it."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 05 — Minuto 5 (escenas 25–30)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_05.png`

**Adjuntos por escena de este lote:**

- Escena 025: `attach: [panel_025, ref_nora, ref_margaret, ref_adrian]`
- Escena 026: `attach: [panel_026, ref_nora, ref_sam]`
- Escena 027: `attach: [panel_027, ref_nora, ref_sam, ref_adrian]`
- Escena 028: `attach: [panel_028, ref_nora, ref_sam]`
- Escena 029: `attach: [panel_029, ref_nora, ref_adrian]`
- Escena 030: `attach: [panel_030, ref_nora, ref_margaret]`

**Guardar 16:9 como:** `raw_clips/minute_05.mp4`

**Guardar 9:16 como:** `raw_clips/minute_05_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 25 (Viñeta #25 del Storyboard) — 04:00–04:10
- Location: Hale lighthouse archive room, night, a single desk lamp
- Characters Present: Nora Hale, Margaret Keller, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora holds a permit signed by Margaret, dated before the fire. Key object in frame: the metal evidence box. Location: Hale lighthouse archive room, night, a single desk lamp. Characters present: Nora Hale, Margaret Keller, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: the metal evidence box → Object In / Object Out: the metal evidence box → the metal evidence box
- Silent Present: Margaret Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Adrian Keller and Nora Hale — Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora holds a permit signed by Margaret, dated before the fire. Key object in frame: the metal evidence box  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Adrian Keller stays silent as the camera holds close on their face, the metal evidence box catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Adrian Keller holds the silence after the line, the metal evidence box sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ADRIAN (reasonable): "Sign the sale. I'll make the petition disappear."
  NORA (quiet): "And if I don't?"

ESCENA 26 (Viñeta #26 del Storyboard) — 04:10–04:20
- Location: Harbor diner, dawn, cold fluorescent light and steam
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora and Sam stand close in the archive, the file between them. Key object in frame: the seawall permit. Location: Harbor diner, dawn, cold fluorescent light and steam. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the seawall permit → Object In / Object Out: the seawall permit → the seawall permit
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora and Sam stand close in the archive, the file between them. Key object in frame: the seawall permit  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the seawall permit catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Nora Hale holds the silence after the line, the seawall permit sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (realizing): "Lighthouses keep logs. Every ship, every storm."
  SAM (nodding): "Your father logged the harbor for thirty years."

ESCENA 27 (Viñeta #27 del Storyboard) — 04:20–04:30
- Location: Keller boathouse, night, flashlight and dust
- Characters Present: Nora Hale, Sam Calloway, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian waits in a diner booth across from Nora. Key object in frame: a folded page. Location: Keller boathouse, night, flashlight and dust. Characters present: Nora Hale, Sam Calloway, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: a folded page → Object In / Object Out: a folded page → a folded page
- Silent Present: Adrian Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian waits in a diner booth across from Nora. Key object in frame: a folded page  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, a folded page catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, a folded page sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (urgent): "Including the night of the fire. And the boat at two."
  SAM (cold): "That's the Keller launch."

ESCENA 28 (Viñeta #28 del Storyboard) — 04:30–04:40
- Location: Hale lighthouse archive room, night, a single desk lamp
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora slides the file across the table, keeping one page back. Key object in frame: a diner coffee cup. Location: Hale lighthouse archive room, night, a single desk lamp. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: a diner coffee cup → Object In / Object Out: a diner coffee cup → a diner coffee cup
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora slides the file across the table, keeping one page back. Key object in frame: a diner coffee cup  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, a diner coffee cup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Nora Hale holds the silence after the line, a diner coffee cup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (quiet): "No. Margaret's launch. Adrian at the helm."
  SAM (careful): "Nora, are you sure?"

ESCENA 29 (Viñeta #29 del Storyboard) — 04:40–04:50
- Location: Harbor diner, dawn, cold fluorescent light and steam
- Characters Present: Nora Hale, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian Keller speaks as the camera holds close on their face, the metal evidence box catching the light between them. Location: Harbor diner, dawn, cold fluorescent light and steam. Key object: the metal evidence box. Characters present: Nora Hale, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: the metal evidence box → Object In / Object Out: the metal evidence box → the metal evidence box
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Adrian Keller and Nora Hale — Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian Keller speaks as the camera holds close on their face, the metal evidence box catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: wide establishing shot — Adrian leans in, his hand covering hers. Key object in frame: the metal evidence box  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Adrian Keller holds the silence after the line, the metal evidence box sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ADRIAN (amused): "A notebook beats a town of witnesses?"
  NORA (calm): "It beats you. You know it."

ESCENA 30 (Viñeta #30 del Storyboard) — 04:50–05:00
- Location: Keller boathouse, night, flashlight and dust
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret Keller speaks as the camera holds close on their face, the seawall permit catching the light between them. Location: Keller boathouse, night, flashlight and dust. Key object: the seawall permit. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the seawall permit → Object In / Object Out: the seawall permit → the seawall permit
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Margaret Keller and Nora Hale — Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret Keller speaks as the camera holds close on their face, the seawall permit catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: medium shot — Nora stands alone in the lamp room, the file in her hands. Key object in frame: the seawall permit  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Margaret Keller holds the silence after the line, the seawall permit sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MARGARET (tired): "Name your price, Nora. One last time."
  NORA (final): "The hearing. Tomorrow. Public. All of it."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 25 (Viñeta #25 del Storyboard) — 04:00–04:10
- Location: Hale lighthouse archive room, night, a single desk lamp
- Characters Present: Nora Hale, Margaret Keller, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora holds a permit signed by Margaret, dated before the fire. Key object in frame: the metal evidence box. Location: Hale lighthouse archive room, night, a single desk lamp. Characters present: Nora Hale, Margaret Keller, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: the metal evidence box → Object In / Object Out: the metal evidence box → the metal evidence box
- Silent Present: Margaret Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Adrian Keller and Nora Hale — Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora holds a permit signed by Margaret, dated before the fire. Key object in frame: the metal evidence box  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Adrian Keller stays silent as the camera holds close on their face, the metal evidence box catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Adrian Keller holds the silence after the line, the metal evidence box sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ADRIAN (reasonable): "Sign the sale. I'll make the petition disappear."
  NORA (quiet): "And if I don't?"

ESCENA 26 (Viñeta #26 del Storyboard) — 04:10–04:20
- Location: Harbor diner, dawn, cold fluorescent light and steam
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora and Sam stand close in the archive, the file between them. Key object in frame: the seawall permit. Location: Harbor diner, dawn, cold fluorescent light and steam. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the seawall permit → Object In / Object Out: the seawall permit → the seawall permit
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora and Sam stand close in the archive, the file between them. Key object in frame: the seawall permit  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the seawall permit catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Nora Hale holds the silence after the line, the seawall permit sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (realizing): "Lighthouses keep logs. Every ship, every storm."
  SAM (nodding): "Your father logged the harbor for thirty years."

ESCENA 27 (Viñeta #27 del Storyboard) — 04:20–04:30
- Location: Keller boathouse, night, flashlight and dust
- Characters Present: Nora Hale, Sam Calloway, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian waits in a diner booth across from Nora. Key object in frame: a folded page. Location: Keller boathouse, night, flashlight and dust. Characters present: Nora Hale, Sam Calloway, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: a folded page → Object In / Object Out: a folded page → a folded page
- Silent Present: Adrian Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian waits in a diner booth across from Nora. Key object in frame: a folded page  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, a folded page catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, a folded page sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (urgent): "Including the night of the fire. And the boat at two."
  SAM (cold): "That's the Keller launch."

ESCENA 28 (Viñeta #28 del Storyboard) — 04:30–04:40
- Location: Hale lighthouse archive room, night, a single desk lamp
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora slides the file across the table, keeping one page back. Key object in frame: a diner coffee cup. Location: Hale lighthouse archive room, night, a single desk lamp. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: a diner coffee cup → Object In / Object Out: a diner coffee cup → a diner coffee cup
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora slides the file across the table, keeping one page back. Key object in frame: a diner coffee cup  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, a diner coffee cup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Nora Hale holds the silence after the line, a diner coffee cup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (quiet): "No. Margaret's launch. Adrian at the helm."
  SAM (careful): "Nora, are you sure?"

ESCENA 29 (Viñeta #29 del Storyboard) — 04:40–04:50
- Location: Harbor diner, dawn, cold fluorescent light and steam
- Characters Present: Nora Hale, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian Keller speaks as the camera holds close on their face, the metal evidence box catching the light between them. Location: Harbor diner, dawn, cold fluorescent light and steam. Key object: the metal evidence box. Characters present: Nora Hale, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: the metal evidence box → Object In / Object Out: the metal evidence box → the metal evidence box
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Adrian Keller and Nora Hale — Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian Keller speaks as the camera holds close on their face, the metal evidence box catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: wide establishing shot — Adrian leans in, his hand covering hers. Key object in frame: the metal evidence box  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Adrian Keller holds the silence after the line, the metal evidence box sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ADRIAN (amused): "A notebook beats a town of witnesses?"
  NORA (calm): "It beats you. You know it."

ESCENA 30 (Viñeta #30 del Storyboard) — 04:50–05:00
- Location: Keller boathouse, night, flashlight and dust
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret Keller speaks as the camera holds close on their face, the seawall permit catching the light between them. Location: Keller boathouse, night, flashlight and dust. Key object: the seawall permit. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing cream knit sweater under the charcoal coat, hair loose); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the seawall permit → Object In / Object Out: the seawall permit → the seawall permit
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Margaret Keller and Nora Hale — Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret Keller speaks as the camera holds close on their face, the seawall permit catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: medium shot — Nora stands alone in the lamp room, the file in her hands. Key object in frame: the seawall permit  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Margaret Keller holds the silence after the line, the seawall permit sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): flashlight click, floorboards, rain on a tin roof, a paper unfolding. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MARGARET (tired): "Name your price, Nora. One last time."
  NORA (final): "The hearing. Tomorrow. Public. All of it."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 06 — Minuto 6 (escenas 31–36)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_06.png`

**Adjuntos por escena de este lote:**

- Escena 031: `attach: [panel_031, ref_nora, ref_margaret]`
- Escena 032: `attach: [panel_032, ref_nora, ref_claire]`
- Escena 033: `attach: [panel_033, ref_nora, ref_sam]`
- Escena 034: `attach: [panel_034, ref_sam, ref_margaret]`
- Escena 035: `attach: [panel_035, ref_nora, ref_adrian]`
- Escena 036: `attach: [panel_036, ref_nora, ref_margaret]`

**Guardar 16:9 como:** `raw_clips/minute_06.mp4`

**Guardar 9:16 como:** `raw_clips/minute_06_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 31 (Viñeta #31 del Storyboard) — 05:00–05:10
- Location: Town hall hearing room, grey morning, rain streaking the windows
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Margaret Keller: Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Rain hammers the town hall windows as Nora faces the panel. Key object in frame: the emergency petition. Location: Town hall hearing room, grey morning, rain streaking the windows. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the emergency petition → Object In / Object Out: the emergency petition → the emergency petition
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Margaret Keller — Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Rain hammers the town hall windows as Nora faces the panel. Key object in frame: the emergency petition  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the emergency petition catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, the emergency petition sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (steady): "I'd rather lose the house than his name."
  MARGARET (soft): "You lost it ten years ago."

ESCENA 32 (Viñeta #32 del Storyboard) — 05:10–05:20
- Location: Town hall hearing room, grey morning, rain streaking the windows
- Characters Present: Nora Hale, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. The hearing room is packed; Claire leans close to Nora. Key object in frame: the emergency petition. Location: Town hall hearing room, grey morning, rain streaking the windows. Characters present: Nora Hale, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: the emergency petition → Object In / Object Out: the emergency petition → the emergency petition
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Claire Boone and Nora Hale — Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. The hearing room is packed; Claire leans close to Nora. Key object in frame: the emergency petition  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Claire Boone stays silent as the camera holds close on their face, the emergency petition catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Claire Boone holds the silence after the line, the emergency petition sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  CLAIRE (nervous): "The hearing is packed. Half the town came."
  NORA (resolved): "Good. This time, I want witnesses."

ESCENA 33 (Viñeta #33 del Storyboard) — 05:20–05:30
- Location: Town hall hearing room, grey morning, rain streaking the windows
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam catches Nora in the hearing room before she takes her seat. Key object in frame: a statement form. Location: Town hall hearing room, grey morning, rain streaking the windows. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: a statement form → Object In / Object Out: a statement form → a statement form
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam catches Nora in the hearing room before she takes her seat. Key object in frame: a statement form  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, a statement form catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Sam Calloway holds the silence after the line, a statement form sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (low): "I should have told you ten years ago."
  NORA (fierce): "Tell it now. Loud enough for everyone."

ESCENA 34 (Viñeta #34 del Storyboard) — 05:30–05:40
- Location: Town hall hearing room, grey morning, rain streaking the windows
- Characters Present: Sam Calloway, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Margaret Keller: Sam Calloway and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam Calloway speaks as the camera holds close on their face, a statement form catching the light between them. Location: Town hall hearing room, grey morning, rain streaking the windows. Key object: a statement form. Characters present: Sam Calloway, Margaret Keller. No other characters appear.
- Identity Anchors: Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: a statement form → Object In / Object Out: a statement form → a statement form
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Margaret Keller — Sam Calloway and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam Calloway speaks as the camera holds close on their face, a statement form catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: medium shot — Sam stands before the panel; Margaret watches from the front row. Key object in frame: a statement form  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, a statement form sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (public, shaking): "I signed a false statement. Margaret wrote it."
  MARGARET (dismissive): "He's a firefighter with a grudge."

ESCENA 35 (Viñeta #35 del Storyboard) — 05:40–05:50
- Location: Town hall hearing room, grey morning, rain streaking the windows
- Characters Present: Nora Hale, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-04s] tight close-up, face and mouth visible: Nora Hale is on camera with face and mouth fully visible, looking at Adrian Keller. Nora faces Adrian across the hearing room. Key object in frame: the petition ruling. Location: Town hall hearing room, grey morning, rain streaking the windows. Characters present: Nora Hale, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: the petition ruling → Object In / Object Out: the petition ruling → the petition ruling
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: tight close-up, face and mouth visible — Nora Hale is on camera with face and mouth fully visible, looking at Adrian Keller. Nora faces Adrian across the hearing room. Key object in frame: the petition ruling  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: medium close-up on Adrian Keller, face and mouth visible — Adrian Keller is on camera with face and mouth fully visible, looking at Nora Hale. Adrian Keller holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [06s-10s]: tight close-up — Adrian Keller holds the silence after the line, the petition ruling sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (calm): "Then hear someone who can't be bought."
  ADRIAN (uneasy): "You're bluffing."

ESCENA 36 (Viñeta #36 del Storyboard) — 05:50–06:00
- Location: Town hall hearing room, grey morning, rain streaking the windows
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. The clerk stamps the petition; the room goes silent. Key object in frame: the petition ruling. Location: Town hall hearing room, grey morning, rain streaking the windows. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the petition ruling → Object In / Object Out: the petition ruling → the petition ruling
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Margaret Keller and Nora Hale — Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. The clerk stamps the petition; the room goes silent. Key object in frame: the petition ruling  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Margaret Keller stays silent as the camera holds close on their face, the petition ruling catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Margaret Keller holds the silence after the line, the petition ruling sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MARGARET (controlled): "The petition is granted. The trust is frozen."
  NORA (raw): "On mental incompetence? That's a lie."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 31 (Viñeta #31 del Storyboard) — 05:00–05:10
- Location: Town hall hearing room, grey morning, rain streaking the windows
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Margaret Keller: Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Rain hammers the town hall windows as Nora faces the panel. Key object in frame: the emergency petition. Location: Town hall hearing room, grey morning, rain streaking the windows. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the emergency petition → Object In / Object Out: the emergency petition → the emergency petition
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Margaret Keller — Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Rain hammers the town hall windows as Nora faces the panel. Key object in frame: the emergency petition  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the emergency petition catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, the emergency petition sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (steady): "I'd rather lose the house than his name."
  MARGARET (soft): "You lost it ten years ago."

ESCENA 32 (Viñeta #32 del Storyboard) — 05:10–05:20
- Location: Town hall hearing room, grey morning, rain streaking the windows
- Characters Present: Nora Hale, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. The hearing room is packed; Claire leans close to Nora. Key object in frame: the emergency petition. Location: Town hall hearing room, grey morning, rain streaking the windows. Characters present: Nora Hale, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: the emergency petition → Object In / Object Out: the emergency petition → the emergency petition
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Claire Boone and Nora Hale — Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. The hearing room is packed; Claire leans close to Nora. Key object in frame: the emergency petition  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Claire Boone stays silent as the camera holds close on their face, the emergency petition catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Claire Boone holds the silence after the line, the emergency petition sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  CLAIRE (nervous): "The hearing is packed. Half the town came."
  NORA (resolved): "Good. This time, I want witnesses."

ESCENA 33 (Viñeta #33 del Storyboard) — 05:20–05:30
- Location: Town hall hearing room, grey morning, rain streaking the windows
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam catches Nora in the hearing room before she takes her seat. Key object in frame: a statement form. Location: Town hall hearing room, grey morning, rain streaking the windows. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: a statement form → Object In / Object Out: a statement form → a statement form
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam catches Nora in the hearing room before she takes her seat. Key object in frame: a statement form  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, a statement form catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Sam Calloway holds the silence after the line, a statement form sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (low): "I should have told you ten years ago."
  NORA (fierce): "Tell it now. Loud enough for everyone."

ESCENA 34 (Viñeta #34 del Storyboard) — 05:30–05:40
- Location: Town hall hearing room, grey morning, rain streaking the windows
- Characters Present: Sam Calloway, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Margaret Keller: Sam Calloway and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam Calloway speaks as the camera holds close on their face, a statement form catching the light between them. Location: Town hall hearing room, grey morning, rain streaking the windows. Key object: a statement form. Characters present: Sam Calloway, Margaret Keller. No other characters appear.
- Identity Anchors: Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: a statement form → Object In / Object Out: a statement form → a statement form
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Margaret Keller — Sam Calloway and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam Calloway speaks as the camera holds close on their face, a statement form catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: medium shot — Sam stands before the panel; Margaret watches from the front row. Key object in frame: a statement form  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, a statement form sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (public, shaking): "I signed a false statement. Margaret wrote it."
  MARGARET (dismissive): "He's a firefighter with a grudge."

ESCENA 35 (Viñeta #35 del Storyboard) — 05:40–05:50
- Location: Town hall hearing room, grey morning, rain streaking the windows
- Characters Present: Nora Hale, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-04s] tight close-up, face and mouth visible: Nora Hale is on camera with face and mouth fully visible, looking at Adrian Keller. Nora faces Adrian across the hearing room. Key object in frame: the petition ruling. Location: Town hall hearing room, grey morning, rain streaking the windows. Characters present: Nora Hale, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: the petition ruling → Object In / Object Out: the petition ruling → the petition ruling
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: tight close-up, face and mouth visible — Nora Hale is on camera with face and mouth fully visible, looking at Adrian Keller. Nora faces Adrian across the hearing room. Key object in frame: the petition ruling  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: medium close-up on Adrian Keller, face and mouth visible — Adrian Keller is on camera with face and mouth fully visible, looking at Nora Hale. Adrian Keller holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [06s-10s]: tight close-up — Adrian Keller holds the silence after the line, the petition ruling sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (calm): "Then hear someone who can't be bought."
  ADRIAN (uneasy): "You're bluffing."

ESCENA 36 (Viñeta #36 del Storyboard) — 05:50–06:00
- Location: Town hall hearing room, grey morning, rain streaking the windows
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. The clerk stamps the petition; the room goes silent. Key object in frame: the petition ruling. Location: Town hall hearing room, grey morning, rain streaking the windows. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the petition ruling → Object In / Object Out: the petition ruling → the petition ruling
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Margaret Keller and Nora Hale — Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. The clerk stamps the petition; the room goes silent. Key object in frame: the petition ruling  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Margaret Keller stays silent as the camera holds close on their face, the petition ruling catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Margaret Keller holds the silence after the line, the petition ruling sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MARGARET (controlled): "The petition is granted. The trust is frozen."
  NORA (raw): "On mental incompetence? That's a lie."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 07 — Minuto 7 (escenas 37–42)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_07.png`

**Adjuntos por escena de este lote:**

- Escena 037: `attach: [panel_037, ref_nora, ref_margaret]`
- Escena 038: `attach: [panel_038, ref_nora, ref_adrian]`
- Escena 039: `attach: [panel_039, ref_nora]`
- Escena 040: `attach: [panel_040, ref_nora]`
- Escena 041: `attach: [panel_041, ref_nora, ref_sam]`
- Escena 042: `attach: [panel_042, ref_nora, ref_sam]`

**Guardar 16:9 como:** `raw_clips/minute_07.mp4`

**Guardar 9:16 como:** `raw_clips/minute_07_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 37 (Viñeta #37 del Storyboard) — 06:00–06:10
- Location: Hale lighthouse, storm night, lightning through the glass
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. At the lighthouse door, Margaret holds out the eviction notice. Location: Hale lighthouse, storm night, lightning through the glass. Key object: the eviction notice. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the eviction notice → Object In / Object Out: the eviction notice → the eviction notice
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Margaret Keller and Nora Hale — Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. At the lighthouse door, Margaret holds out the eviction notice  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Margaret Keller stays silent as the camera holds close on their face, the eviction notice catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Margaret Keller holds the silence after the line, the eviction notice sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MARGARET (cold): "You have until midnight to leave the lighthouse."
  NORA (flat): "She bought the county. Not me."

ESCENA 38 (Viñeta #38 del Storyboard) — 06:10–06:20
- Location: Hale lighthouse, night, one lamp, rain outside
- Characters Present: Nora Hale, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian waits in the lighthouse with the sale papers. Location: Hale lighthouse, night, one lamp, rain outside. Key object: the sale papers. Characters present: Nora Hale, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: the sale papers → Object In / Object Out: the sale papers → the sale papers
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Adrian Keller and Nora Hale — Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian waits in the lighthouse with the sale papers  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Adrian Keller stays silent as the camera holds close on their face, the sale papers catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Adrian Keller holds the silence after the line, the sale papers sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ADRIAN (reasonable): "Sign the sale. I'll make the eviction disappear."
  NORA (quiet): "And if I don't?"

ESCENA 39 (Viñeta #39 del Storyboard) — 06:20–06:30
- Location: Hale lighthouse, storm night, lightning through the glass
- Characters Present: Nora Hale
- Storyboard Panel (Shot 1 exact framing): [00s-07s] medium shot, face and mouth visible: Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora stands alone in the dark lighthouse, the cold lens above her. Key object in frame: the cold lamp. Location: Hale lighthouse, storm night, lightning through the glass. Characters present: Nora Hale. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down)
- Key Object: the cold lamp → Object In / Object Out: the cold lamp → the cold lamp
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: medium shot, face and mouth visible — Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora stands alone in the dark lighthouse, the cold lens above her. Key object in frame: the cold lamp  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the cold lamp catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — The silence hangs, the cold lamp sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (hushed): "He left me a key. There has to be something."

ESCENA 40 (Viñeta #40 del Storyboard) — 06:30–06:40
- Location: Hale lighthouse, storm night, lightning through the glass
- Characters Present: Nora Hale
- Storyboard Panel (Shot 1 exact framing): [00s-04s] tight close-up, face and mouth visible: Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora finds an old harbor logbook behind the lens housing. Key object in frame: the harbor logbook. Location: Hale lighthouse, storm night, lightning through the glass. Characters present: Nora Hale. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down)
- Key Object: the harbor logbook → Object In / Object Out: the harbor logbook → the harbor logbook
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: tight close-up, face and mouth visible — Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora finds an old harbor logbook behind the lens housing. Key object in frame: the harbor logbook  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the harbor logbook is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: close-up, face and mouth visible — Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora Hale speaks as the camera holds close on their face, the harbor logbook catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: insert shot of the evidence object — The silence hangs, the harbor logbook sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (precise): "The harbor log. Every boat, every night."
  NORA (breaking): "Dad, what did you see?"

ESCENA 41 (Viñeta #41 del Storyboard) — 06:40–06:50
- Location: Hale lighthouse archive room, dawn, cold blue light
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora opens the logbook on the lighthouse table, pages brittle. Key object in frame: the harbor log. Location: Hale lighthouse archive room, dawn, cold blue light. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the harbor log → Object In / Object Out: the harbor log → the harbor log
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora opens the logbook on the lighthouse table, pages brittle. Key object in frame: the harbor log  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the harbor log catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, the harbor log sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (focused): "Every keeper signs the log. Date, time, weather."
  SAM (quiet): "Your father never missed a night."

ESCENA 42 (Viñeta #42 del Storyboard) — 06:50–07:00
- Location: Harbor pier, morning, flat silver water
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora and Sam compare timestamps under a desk lamp. Key object in frame: a torn page. Location: Harbor pier, morning, flat silver water. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: a torn page → Object In / Object Out: a torn page → a torn page
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora and Sam compare timestamps under a desk lamp. Key object in frame: a torn page  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, a torn page catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, a torn page sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (grim): "The page is torn out."
  NORA (triumphant whisper): "No. Folded. He hid it behind the lens."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 37 (Viñeta #37 del Storyboard) — 06:00–06:10
- Location: Hale lighthouse, storm night, lightning through the glass
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. At the lighthouse door, Margaret holds out the eviction notice. Location: Hale lighthouse, storm night, lightning through the glass. Key object: the eviction notice. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the eviction notice → Object In / Object Out: the eviction notice → the eviction notice
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Margaret Keller and Nora Hale — Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. At the lighthouse door, Margaret holds out the eviction notice  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Margaret Keller stays silent as the camera holds close on their face, the eviction notice catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Margaret Keller holds the silence after the line, the eviction notice sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MARGARET (cold): "You have until midnight to leave the lighthouse."
  NORA (flat): "She bought the county. Not me."

ESCENA 38 (Viñeta #38 del Storyboard) — 06:10–06:20
- Location: Hale lighthouse, night, one lamp, rain outside
- Characters Present: Nora Hale, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian waits in the lighthouse with the sale papers. Location: Hale lighthouse, night, one lamp, rain outside. Key object: the sale papers. Characters present: Nora Hale, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: the sale papers → Object In / Object Out: the sale papers → the sale papers
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Adrian Keller and Nora Hale — Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian waits in the lighthouse with the sale papers  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Adrian Keller stays silent as the camera holds close on their face, the sale papers catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Adrian Keller holds the silence after the line, the sale papers sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ADRIAN (reasonable): "Sign the sale. I'll make the eviction disappear."
  NORA (quiet): "And if I don't?"

ESCENA 39 (Viñeta #39 del Storyboard) — 06:20–06:30
- Location: Hale lighthouse, storm night, lightning through the glass
- Characters Present: Nora Hale
- Storyboard Panel (Shot 1 exact framing): [00s-07s] medium shot, face and mouth visible: Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora stands alone in the dark lighthouse, the cold lens above her. Key object in frame: the cold lamp. Location: Hale lighthouse, storm night, lightning through the glass. Characters present: Nora Hale. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down)
- Key Object: the cold lamp → Object In / Object Out: the cold lamp → the cold lamp
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: medium shot, face and mouth visible — Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora stands alone in the dark lighthouse, the cold lens above her. Key object in frame: the cold lamp  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the cold lamp catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — The silence hangs, the cold lamp sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (hushed): "He left me a key. There has to be something."

ESCENA 40 (Viñeta #40 del Storyboard) — 06:30–06:40
- Location: Hale lighthouse, storm night, lightning through the glass
- Characters Present: Nora Hale
- Storyboard Panel (Shot 1 exact framing): [00s-04s] tight close-up, face and mouth visible: Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora finds an old harbor logbook behind the lens housing. Key object in frame: the harbor logbook. Location: Hale lighthouse, storm night, lightning through the glass. Characters present: Nora Hale. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing storm-soaked shirt and trousers, no coat, hair plastered down)
- Key Object: the harbor logbook → Object In / Object Out: the harbor logbook → the harbor logbook
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: tight close-up, face and mouth visible — Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora finds an old harbor logbook behind the lens housing. Key object in frame: the harbor logbook  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the harbor logbook is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: close-up, face and mouth visible — Nora Hale is on camera with face and mouth fully visible, looking at the other person in frame. Nora Hale speaks as the camera holds close on their face, the harbor logbook catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: insert shot of the evidence object — The silence hangs, the harbor logbook sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): storm wind, rain on glass, a gavel, a chair scraping. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (precise): "The harbor log. Every boat, every night."
  NORA (breaking): "Dad, what did you see?"

ESCENA 41 (Viñeta #41 del Storyboard) — 06:40–06:50
- Location: Hale lighthouse archive room, dawn, cold blue light
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora opens the logbook on the lighthouse table, pages brittle. Key object in frame: the harbor log. Location: Hale lighthouse archive room, dawn, cold blue light. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the harbor log → Object In / Object Out: the harbor log → the harbor log
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora opens the logbook on the lighthouse table, pages brittle. Key object in frame: the harbor log  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the harbor log catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, the harbor log sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (focused): "Every keeper signs the log. Date, time, weather."
  SAM (quiet): "Your father never missed a night."

ESCENA 42 (Viñeta #42 del Storyboard) — 06:50–07:00
- Location: Harbor pier, morning, flat silver water
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora and Sam compare timestamps under a desk lamp. Key object in frame: a torn page. Location: Harbor pier, morning, flat silver water. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: a torn page → Object In / Object Out: a torn page → a torn page
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora and Sam compare timestamps under a desk lamp. Key object in frame: a torn page  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, a torn page catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, a torn page sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (grim): "The page is torn out."
  NORA (triumphant whisper): "No. Folded. He hid it behind the lens."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 08 — Minuto 8 (escenas 43–48)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_08.png`

**Adjuntos por escena de este lote:**

- Escena 043: `attach: [panel_043, ref_nora, ref_sam]`
- Escena 044: `attach: [panel_044, ref_nora, ref_sam]`
- Escena 045: `attach: [panel_045, ref_nora, ref_sam]`
- Escena 046: `attach: [panel_046, ref_nora, ref_adrian]`
- Escena 047: `attach: [panel_047, ref_nora, ref_margaret]`
- Escena 048: `attach: [panel_048, ref_nora, ref_margaret, ref_claire]`

**Guardar 16:9 como:** `raw_clips/minute_08.mp4`

**Guardar 9:16 como:** `raw_clips/minute_08_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 43 (Viñeta #43 del Storyboard) — 07:00–07:10
- Location: Town hall steps, dusk, wet stone
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora Hale speaks as the camera holds close on their face, a timestamp catching the light between them. Location: Town hall steps, dusk, wet stone. Key object: a timestamp. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: a timestamp → Object In / Object Out: a timestamp → a timestamp
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora Hale speaks as the camera holds close on their face, a timestamp catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: medium shot — Nora traces a line in the log with her finger. Key object in frame: a timestamp  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, a timestamp sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (urgent): "2:14 a.m. Keller launch. Two passengers, not one."
  SAM (low): "Who's the second?"

ESCENA 44 (Viñeta #44 del Storyboard) — 07:10–07:20
- Location: Hale lighthouse archive room, dawn, cold blue light
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam reads over her shoulder, close enough to touch. Key object in frame: the town hall steps. Location: Hale lighthouse archive room, dawn, cold blue light. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the town hall steps → Object In / Object Out: the town hall steps → the town hall steps
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam reads over her shoulder, close enough to touch. Key object in frame: the town hall steps  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, the town hall steps catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, the town hall steps sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (stunned): "Your mother's name."
  NORA (flat): "She died when I was eleven. I watched them bury her."

ESCENA 45 (Viñeta #45 del Storyboard) — 07:20–07:30
- Location: Harbor pier, morning, flat silver water
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora looks up at Sam, a decision forming. Key object in frame: the harbor log. Location: Harbor pier, morning, flat silver water. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the harbor log → Object In / Object Out: the harbor log → the harbor log
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora looks up at Sam, a decision forming. Key object in frame: the harbor log  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the harbor log catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, the harbor log sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (shaking): "Every year, in cash, under her maiden name."
  SAM (gentle): "Nora, we can still stop this."

ESCENA 46 (Viñeta #46 del Storyboard) — 07:30–07:40
- Location: Town hall steps, dusk, wet stone
- Characters Present: Nora Hale, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian stands on the town hall steps, trying to smile. Key object in frame: a torn page. Location: Town hall steps, dusk, wet stone. Characters present: Nora Hale, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: a torn page → Object In / Object Out: a torn page → a torn page
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Adrian Keller and Nora Hale — Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian stands on the town hall steps, trying to smile. Key object in frame: a torn page  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Adrian Keller stays silent as the camera holds close on their face, a torn page catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Adrian Keller holds the silence after the line, a torn page sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ADRIAN (reasonable): "The hearing is tomorrow. Change your mind tonight."
  NORA (calm): "I've had ten years. I'm not changing."

ESCENA 47 (Viñeta #47 del Storyboard) — 07:40–07:50
- Location: Hale lighthouse archive room, dawn, cold blue light
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora walks past him without stopping. Key object in frame: a timestamp. Location: Hale lighthouse archive room, dawn, cold blue light. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: a timestamp → Object In / Object Out: a timestamp → a timestamp
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Margaret Keller and Nora Hale — Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora walks past him without stopping. Key object in frame: a timestamp  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Margaret Keller stays silent as the camera holds close on their face, a timestamp catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Margaret Keller holds the silence after the line, a timestamp sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MARGARET (controlled): "You've made your point. Name a number."
  NORA (final): "Zero. You leave with nothing."

ESCENA 48 (Viñeta #48 del Storyboard) — 07:50–08:00
- Location: Harbor pier, morning, flat silver water
- Characters Present: Nora Hale, Margaret Keller, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret waits in the hall, gloves in hand. Key object in frame: the town hall steps. Location: Harbor pier, morning, flat silver water. Characters present: Nora Hale, Margaret Keller, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: the town hall steps → Object In / Object Out: the town hall steps → the town hall steps
- Silent Present: Margaret Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Claire Boone and Nora Hale — Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret waits in the hall, gloves in hand. Key object in frame: the town hall steps  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Claire Boone stays silent as the camera holds close on their face, the town hall steps catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Claire Boone holds the silence after the line, the town hall steps sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  CLAIRE (worried): "Present that log, and the town turns on your mother."
  NORA (steady): "Then they'll tell the truth."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 43 (Viñeta #43 del Storyboard) — 07:00–07:10
- Location: Town hall steps, dusk, wet stone
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora Hale speaks as the camera holds close on their face, a timestamp catching the light between them. Location: Town hall steps, dusk, wet stone. Key object: a timestamp. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: a timestamp → Object In / Object Out: a timestamp → a timestamp
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora Hale speaks as the camera holds close on their face, a timestamp catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: medium shot — Nora traces a line in the log with her finger. Key object in frame: a timestamp  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, a timestamp sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (urgent): "2:14 a.m. Keller launch. Two passengers, not one."
  SAM (low): "Who's the second?"

ESCENA 44 (Viñeta #44 del Storyboard) — 07:10–07:20
- Location: Hale lighthouse archive room, dawn, cold blue light
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam reads over her shoulder, close enough to touch. Key object in frame: the town hall steps. Location: Hale lighthouse archive room, dawn, cold blue light. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the town hall steps → Object In / Object Out: the town hall steps → the town hall steps
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam reads over her shoulder, close enough to touch. Key object in frame: the town hall steps  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, the town hall steps catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, the town hall steps sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (stunned): "Your mother's name."
  NORA (flat): "She died when I was eleven. I watched them bury her."

ESCENA 45 (Viñeta #45 del Storyboard) — 07:20–07:30
- Location: Harbor pier, morning, flat silver water
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora looks up at Sam, a decision forming. Key object in frame: the harbor log. Location: Harbor pier, morning, flat silver water. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the harbor log → Object In / Object Out: the harbor log → the harbor log
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora looks up at Sam, a decision forming. Key object in frame: the harbor log  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the harbor log catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, the harbor log sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (shaking): "Every year, in cash, under her maiden name."
  SAM (gentle): "Nora, we can still stop this."

ESCENA 46 (Viñeta #46 del Storyboard) — 07:30–07:40
- Location: Town hall steps, dusk, wet stone
- Characters Present: Nora Hale, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian stands on the town hall steps, trying to smile. Key object in frame: a torn page. Location: Town hall steps, dusk, wet stone. Characters present: Nora Hale, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: a torn page → Object In / Object Out: a torn page → a torn page
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Adrian Keller and Nora Hale — Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian stands on the town hall steps, trying to smile. Key object in frame: a torn page  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Adrian Keller stays silent as the camera holds close on their face, a torn page catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Adrian Keller holds the silence after the line, a torn page sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ADRIAN (reasonable): "The hearing is tomorrow. Change your mind tonight."
  NORA (calm): "I've had ten years. I'm not changing."

ESCENA 47 (Viñeta #47 del Storyboard) — 07:40–07:50
- Location: Hale lighthouse archive room, dawn, cold blue light
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora walks past him without stopping. Key object in frame: a timestamp. Location: Hale lighthouse archive room, dawn, cold blue light. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: a timestamp → Object In / Object Out: a timestamp → a timestamp
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Margaret Keller and Nora Hale — Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora walks past him without stopping. Key object in frame: a timestamp  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Margaret Keller stays silent as the camera holds close on their face, a timestamp catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Margaret Keller holds the silence after the line, a timestamp sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MARGARET (controlled): "You've made your point. Name a number."
  NORA (final): "Zero. You leave with nothing."

ESCENA 48 (Viñeta #48 del Storyboard) — 07:50–08:00
- Location: Harbor pier, morning, flat silver water
- Characters Present: Nora Hale, Margaret Keller, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret waits in the hall, gloves in hand. Key object in frame: the town hall steps. Location: Harbor pier, morning, flat silver water. Characters present: Nora Hale, Margaret Keller, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: the town hall steps → Object In / Object Out: the town hall steps → the town hall steps
- Silent Present: Margaret Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Claire Boone and Nora Hale — Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret waits in the hall, gloves in hand. Key object in frame: the town hall steps  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Claire Boone stays silent as the camera holds close on their face, the town hall steps catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Claire Boone holds the silence after the line, the town hall steps sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  CLAIRE (worried): "Present that log, and the town turns on your mother."
  NORA (steady): "Then they'll tell the truth."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 09 — Minuto 9 (escenas 49–54)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_09.png`

**Adjuntos por escena de este lote:**

- Escena 049: `attach: [panel_049, ref_nora, ref_sam, ref_margaret]`
- Escena 050: `attach: [panel_050, ref_nora, ref_margaret]`
- Escena 051: `attach: [panel_051, ref_nora, ref_claire]`
- Escena 052: `attach: [panel_052, ref_nora, ref_sam]`
- Escena 053: `attach: [panel_053, ref_nora, ref_sam, ref_margaret]`
- Escena 054: `attach: [panel_054, ref_nora, ref_sam, ref_margaret]`

**Guardar 16:9 como:** `raw_clips/minute_09.mp4`

**Guardar 9:16 como:** `raw_clips/minute_09_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 49 (Viñeta #49 del Storyboard) — 08:00–08:10
- Location: Town hall steps, dusk, wet stone
- Characters Present: Nora Hale, Sam Calloway, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora faces Margaret on the empty hearing floor. Key object in frame: the harbor log. Location: Town hall steps, dusk, wet stone. Characters present: Nora Hale, Sam Calloway, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the harbor log → Object In / Object Out: the harbor log → the harbor log
- Silent Present: Margaret Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora faces Margaret on the empty hearing floor. Key object in frame: the harbor log  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the harbor log catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, the harbor log sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (vulnerable): "Whatever they say tomorrow, hear it from me first."
  SAM (low): "I'm not going anywhere."

ESCENA 50 (Viñeta #50 del Storyboard) — 08:10–08:20
- Location: Hale lighthouse archive room, dawn, cold blue light
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stands at the lighthouse door as the town lights come on. Key object in frame: a torn page. Location: Hale lighthouse archive room, dawn, cold blue light. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: a torn page → Object In / Object Out: a torn page → a torn page
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Margaret Keller and Nora Hale — Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stands at the lighthouse door as the town lights come on. Key object in frame: a torn page  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Margaret Keller stays silent as the camera holds close on their face, a torn page catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Margaret Keller holds the silence after the line, a torn page sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MARGARET (cold): "You'll lose the only home you have left."
  NORA (fierce): "Not for the house. For his name."

ESCENA 51 (Viñeta #51 del Storyboard) — 08:20–08:30
- Location: Town hall hearing room, day, hard window light
- Characters Present: Nora Hale, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. The hearing room fills; Nora stands alone at the table. Key object in frame: the harbor log. Location: Town hall hearing room, day, hard window light. Characters present: Nora Hale, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: the harbor log → Object In / Object Out: the harbor log → the harbor log
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Claire Boone and Nora Hale — Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. The hearing room fills; Nora stands alone at the table. Key object in frame: the harbor log  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Claire Boone stays silent as the camera holds close on their face, the harbor log catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Claire Boone holds the silence after the line, the harbor log sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  CLAIRE (nervous): "Emergency hearing. Every seat is full."
  NORA (resolved): "Good. Let them watch. Let them remember."

ESCENA 52 (Viñeta #52 del Storyboard) — 08:30–08:40
- Location: Hale lighthouse point, golden hour, wind down
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam steps to the microphone, the room silent. Key object in frame: the clerk's desk. Location: Hale lighthouse point, golden hour, wind down. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the clerk's desk → Object In / Object Out: the clerk's desk → the clerk's desk
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam steps to the microphone, the room silent. Key object in frame: the clerk's desk  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, the clerk's desk catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, the clerk's desk sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (steady): "If I do this, I lose the department."
  NORA (gentle): "Then do it for the right reason."

ESCENA 53 (Viñeta #53 del Storyboard) — 08:40–08:50
- Location: Harbor, golden hour, calm water
- Characters Present: Nora Hale, Sam Calloway, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret's smile falters for the first time. Key object in frame: a second ledger. Location: Harbor, golden hour, calm water. Characters present: Nora Hale, Sam Calloway, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: a second ledger → Object In / Object Out: a second ledger → a second ledger
- Silent Present: Margaret Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret's smile falters for the first time. Key object in frame: a second ledger  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, a second ledger catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, a second ledger sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (quiet): "Just tell them the truth."
  SAM (breaking): "The truth is I let them bury your father."

ESCENA 54 (Viñeta #54 del Storyboard) — 08:50–09:00
- Location: Town hall hearing room, day, hard window light
- Characters Present: Nora Hale, Sam Calloway, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Margaret Keller: Sam Calloway and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora holds up the harbor log, open to the page. Key object in frame: Sam's hand. Location: Town hall hearing room, day, hard window light. Characters present: Nora Hale, Sam Calloway, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: Sam's hand → Object In / Object Out: Sam's hand → Sam's hand
- Silent Present: Nora Hale — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Margaret Keller — Sam Calloway and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora holds up the harbor log, open to the page. Key object in frame: Sam's hand  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, Sam's hand catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, Sam's hand sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (public, clear): "I signed a false statement. Margaret paid me."
  MARGARET (dismissive): "He's a firefighter with a grudge."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 49 (Viñeta #49 del Storyboard) — 08:00–08:10
- Location: Town hall steps, dusk, wet stone
- Characters Present: Nora Hale, Sam Calloway, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora faces Margaret on the empty hearing floor. Key object in frame: the harbor log. Location: Town hall steps, dusk, wet stone. Characters present: Nora Hale, Sam Calloway, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the harbor log → Object In / Object Out: the harbor log → the harbor log
- Silent Present: Margaret Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora faces Margaret on the empty hearing floor. Key object in frame: the harbor log  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the harbor log catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, the harbor log sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (vulnerable): "Whatever they say tomorrow, hear it from me first."
  SAM (low): "I'm not going anywhere."

ESCENA 50 (Viñeta #50 del Storyboard) — 08:10–08:20
- Location: Hale lighthouse archive room, dawn, cold blue light
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Margaret Keller and Nora Hale: Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stands at the lighthouse door as the town lights come on. Key object in frame: a torn page. Location: Hale lighthouse archive room, dawn, cold blue light. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer over a black shirt, hair tied back); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: a torn page → Object In / Object Out: a torn page → a torn page
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Margaret Keller and Nora Hale — Margaret Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora stands at the lighthouse door as the town lights come on. Key object in frame: a torn page  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Margaret Keller stays silent as the camera holds close on their face, a torn page catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Margaret Keller holds the silence after the line, a torn page sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): pages turning, a desk lamp humming, gulls outside, footsteps on wet stone. Voice tone: MARGARET — low, polished, unhurried American English, never shouts; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MARGARET (cold): "You'll lose the only home you have left."
  NORA (fierce): "Not for the house. For his name."

ESCENA 51 (Viñeta #51 del Storyboard) — 08:20–08:30
- Location: Town hall hearing room, day, hard window light
- Characters Present: Nora Hale, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Claire Boone and Nora Hale: Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. The hearing room fills; Nora stands alone at the table. Key object in frame: the harbor log. Location: Town hall hearing room, day, hard window light. Characters present: Nora Hale, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: the harbor log → Object In / Object Out: the harbor log → the harbor log
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Claire Boone and Nora Hale — Claire Boone and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. The hearing room fills; Nora stands alone at the table. Key object in frame: the harbor log  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Claire Boone stays silent as the camera holds close on their face, the harbor log catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Claire Boone holds the silence after the line, the harbor log sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: CLAIRE — grounded, plainspoken American English with a slight coastal New England softness; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  CLAIRE (nervous): "Emergency hearing. Every seat is full."
  NORA (resolved): "Good. Let them watch. Let them remember."

ESCENA 52 (Viñeta #52 del Storyboard) — 08:30–08:40
- Location: Hale lighthouse point, golden hour, wind down
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Nora Hale: Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam steps to the microphone, the room silent. Key object in frame: the clerk's desk. Location: Hale lighthouse point, golden hour, wind down. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the clerk's desk → Object In / Object Out: the clerk's desk → the clerk's desk
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Nora Hale — Sam Calloway and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Sam steps to the microphone, the room silent. Key object in frame: the clerk's desk  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, the clerk's desk catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, the clerk's desk sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (steady): "If I do this, I lose the department."
  NORA (gentle): "Then do it for the right reason."

ESCENA 53 (Viñeta #53 del Storyboard) — 08:40–08:50
- Location: Harbor, golden hour, calm water
- Characters Present: Nora Hale, Sam Calloway, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret's smile falters for the first time. Key object in frame: a second ledger. Location: Harbor, golden hour, calm water. Characters present: Nora Hale, Sam Calloway, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: a second ledger → Object In / Object Out: a second ledger → a second ledger
- Silent Present: Margaret Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret's smile falters for the first time. Key object in frame: a second ledger  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, a second ledger catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, a second ledger sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (quiet): "Just tell them the truth."
  SAM (breaking): "The truth is I let them bury your father."

ESCENA 54 (Viñeta #54 del Storyboard) — 08:50–09:00
- Location: Town hall hearing room, day, hard window light
- Characters Present: Nora Hale, Sam Calloway, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Sam Calloway and Margaret Keller: Sam Calloway and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora holds up the harbor log, open to the page. Key object in frame: Sam's hand. Location: Town hall hearing room, day, hard window light. Characters present: Nora Hale, Sam Calloway, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: Sam's hand → Object In / Object Out: Sam's hand → Sam's hand
- Silent Present: Nora Hale — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Sam Calloway and Margaret Keller — Sam Calloway and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora holds up the harbor log, open to the page. Key object in frame: Sam's hand  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Sam Calloway stays silent as the camera holds close on their face, Sam's hand catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Sam Calloway holds the silence after the line, Sam's hand sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: SAM — quiet, low American English, careful diction, warmth under restraint; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, max 15 words, finish before 8.5 s):
  SAM (public, clear): "I signed a false statement. Margaret paid me."
  MARGARET (dismissive): "He's a firefighter with a grudge."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 10 — Minuto 10 (escenas 55–60)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_10.png`

**Adjuntos por escena de este lote:**

- Escena 055: `attach: [panel_055, ref_nora, ref_adrian]`
- Escena 056: `attach: [panel_056, ref_nora, ref_margaret]`
- Escena 057: `attach: [panel_057, ref_nora, ref_margaret, ref_claire]`
- Escena 058: `attach: [panel_058, ref_nora, ref_sam, ref_adrian]`
- Escena 059: `attach: [panel_059, ref_nora, ref_margaret]`
- Escena 060: `attach: [panel_060, ref_nora, ref_sam]`

**Guardar 16:9 como:** `raw_clips/minute_10.mp4`

**Guardar 9:16 como:** `raw_clips/minute_10_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 55 (Viñeta #55 del Storyboard) — 09:00–09:10
- Location: Hale lighthouse point, golden hour, wind down
- Characters Present: Nora Hale, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Adrian Keller: Nora Hale and Adrian Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian half-rises from his chair. Key object in frame: the harbor log. Location: Hale lighthouse point, golden hour, wind down. Characters present: Nora Hale, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: the harbor log → Object In / Object Out: the harbor log → the harbor log
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Adrian Keller — Nora Hale and Adrian Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian half-rises from his chair. Key object in frame: the harbor log  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the harbor log catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, the harbor log sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (calm): "Then hear someone who can't be bought. The log."
  ADRIAN (uneasy): "That's a piece of paper."

ESCENA 56 (Viñeta #56 del Storyboard) — 09:10–09:20
- Location: Harbor, golden hour, calm water
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Margaret Keller: Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora sets the log on the clerk's desk. Location: Harbor, golden hour, calm water. Key object: the clerk's desk. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the clerk's desk → Object In / Object Out: the clerk's desk → the clerk's desk
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Margaret Keller — Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora sets the log on the clerk's desk  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the clerk's desk catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Nora Hale holds the silence after the line, the clerk's desk sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (precise): "2:14. Keller launch. Two aboard. Adrian steering."
  MARGARET (sharp): "That log is weather and guesswork."

ESCENA 57 (Viñeta #57 del Storyboard) — 09:20–09:30
- Location: Town hall hearing room, day, hard window light
- Characters Present: Nora Hale, Margaret Keller, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Claire Boone: Nora Hale and Claire Boone face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret reaches for the log; Nora slides it away. Key object in frame: a second ledger. Location: Town hall hearing room, day, hard window light. Characters present: Nora Hale, Margaret Keller, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: a second ledger → Object In / Object Out: a second ledger → a second ledger
- Silent Present: Margaret Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Claire Boone — Nora Hale and Claire Boone face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret reaches for the log; Nora slides it away. Key object in frame: a second ledger  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, a second ledger catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, a second ledger sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; CLAIRE — grounded, plainspoken American English with a slight coastal New England softness
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (quiet): "Margaret. And the man who signed the fire report."
  CLAIRE (stunned): "The fire marshal."

ESCENA 58 (Viñeta #58 del Storyboard) — 09:30–09:40
- Location: Hale lighthouse point, golden hour, wind down
- Characters Present: Nora Hale, Sam Calloway, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian Keller speaks as the camera holds close on their face, Sam's hand catching the light between them. Location: Hale lighthouse point, golden hour, wind down. Key object: Sam's hand. Characters present: Nora Hale, Sam Calloway, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: Sam's hand → Object In / Object Out: Sam's hand → Sam's hand
- Silent Present: Sam Calloway — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Adrian Keller and Nora Hale — Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian Keller speaks as the camera holds close on their face, Sam's hand catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: tight close-up — Sam takes Nora's hand under the table. Key object in frame: Sam's hand  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Adrian Keller holds the silence after the line, Sam's hand sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ADRIAN (breaking): "An accident. We meant to scare him."
  NORA (raw): "You burned it and buried my father."

ESCENA 59 (Viñeta #59 del Storyboard) — 09:40–09:50
- Location: Harbor, golden hour, calm water
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Margaret Keller: Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora walks out of the town hall into the light. Key object in frame: the harbor log. Location: Harbor, golden hour, calm water. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the harbor log → Object In / Object Out: the harbor log → the harbor log
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Margaret Keller — Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora walks out of the town hall into the light. Key object in frame: the harbor log  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the harbor log catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, the harbor log sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (fierce): "That's not an accident. That's a choice."
  MARGARET (quiet): "You'll regret this."

ESCENA 60 (Viñeta #60 del Storyboard) — 09:50–10:00
- Location: Town hall hearing room, day, hard window light
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora Hale speaks as the camera holds close on their face, the clerk's desk catching the light between them. Location: Town hall hearing room, day, hard window light. Key object: the clerk's desk. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the clerk's desk → Object In / Object Out: the clerk's desk → the clerk's desk
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora Hale speaks as the camera holds close on their face, the clerk's desk catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: low-angle hero shot — Nora and Sam stand on the lighthouse point at dusk, an older ledger in Nora's hands. Key object in frame: the clerk's desk  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Nora Hale holds the silence after the line, the clerk's desk sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (hushed): "Wait. This ledger is older. Her name is on every page."
  SAM (stunned): "Nora... she's alive?"

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 55 (Viñeta #55 del Storyboard) — 09:00–09:10
- Location: Hale lighthouse point, golden hour, wind down
- Characters Present: Nora Hale, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Adrian Keller: Nora Hale and Adrian Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian half-rises from his chair. Key object in frame: the harbor log. Location: Hale lighthouse point, golden hour, wind down. Characters present: Nora Hale, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: the harbor log → Object In / Object Out: the harbor log → the harbor log
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Adrian Keller — Nora Hale and Adrian Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian half-rises from his chair. Key object in frame: the harbor log  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the harbor log catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, the harbor log sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (calm): "Then hear someone who can't be bought. The log."
  ADRIAN (uneasy): "That's a piece of paper."

ESCENA 56 (Viñeta #56 del Storyboard) — 09:10–09:20
- Location: Harbor, golden hour, calm water
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Margaret Keller: Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora sets the log on the clerk's desk. Location: Harbor, golden hour, calm water. Key object: the clerk's desk. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the clerk's desk → Object In / Object Out: the clerk's desk → the clerk's desk
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Margaret Keller — Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora sets the log on the clerk's desk  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the clerk's desk catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Nora Hale holds the silence after the line, the clerk's desk sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (precise): "2:14. Keller launch. Two aboard. Adrian steering."
  MARGARET (sharp): "That log is weather and guesswork."

ESCENA 57 (Viñeta #57 del Storyboard) — 09:20–09:30
- Location: Town hall hearing room, day, hard window light
- Characters Present: Nora Hale, Margaret Keller, Claire Boone
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Claire Boone: Nora Hale and Claire Boone face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret reaches for the log; Nora slides it away. Key object in frame: a second ledger. Location: Town hall hearing room, day, hard window light. Characters present: Nora Hale, Margaret Keller, Claire Boone. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes); Claire Boone (Cast Sheet Pos #5: age as shown in the reference sheet; brown blunt bob; wearing forest-green cardigan, cream blouse, dark trousers)
- Key Object: a second ledger → Object In / Object Out: a second ledger → a second ledger
- Silent Present: Margaret Keller — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Claire Boone — Nora Hale and Claire Boone face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Margaret reaches for the log; Nora slides it away. Key object in frame: a second ledger  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, a second ledger catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, a second ledger sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; CLAIRE — grounded, plainspoken American English with a slight coastal New England softness
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (quiet): "Margaret. And the man who signed the fire report."
  CLAIRE (stunned): "The fire marshal."

ESCENA 58 (Viñeta #58 del Storyboard) — 09:30–09:40
- Location: Hale lighthouse point, golden hour, wind down
- Characters Present: Nora Hale, Sam Calloway, Adrian Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Adrian Keller and Nora Hale: Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian Keller speaks as the camera holds close on their face, Sam's hand catching the light between them. Location: Hale lighthouse point, golden hour, wind down. Key object: Sam's hand. Characters present: Nora Hale, Sam Calloway, Adrian Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots); Adrian Keller (Cast Sheet Pos #4: late thirties; ash-blond hair swept back; wearing navy blazer, open-collared white shirt, dark trousers)
- Key Object: Sam's hand → Object In / Object Out: Sam's hand → Sam's hand
- Silent Present: Sam Calloway — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Adrian Keller and Nora Hale — Adrian Keller and Nora Hale face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Adrian Keller speaks as the camera holds close on their face, Sam's hand catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: tight close-up — Sam takes Nora's hand under the table. Key object in frame: Sam's hand  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Adrian Keller holds the silence after the line, Sam's hand sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: ADRIAN — smooth mid-range American English, reasonable tone that never quite reaches sincerity; NORA — warm mid-range American English, controlled, slightly breathy under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ADRIAN (breaking): "An accident. We meant to scare him."
  NORA (raw): "You burned it and buried my father."

ESCENA 59 (Viñeta #59 del Storyboard) — 09:40–09:50
- Location: Harbor, golden hour, calm water
- Characters Present: Nora Hale, Margaret Keller
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Margaret Keller: Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora walks out of the town hall into the light. Key object in frame: the harbor log. Location: Harbor, golden hour, calm water. Characters present: Nora Hale, Margaret Keller. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Margaret Keller (Cast Sheet Pos #3: late sixties; tall and straight-backed; wearing tailored dove-grey suit, pearls, low-heeled shoes)
- Key Object: the harbor log → Object In / Object Out: the harbor log → the harbor log
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Margaret Keller — Nora Hale and Margaret Keller face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora walks out of the town hall into the light. Key object in frame: the harbor log  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Nora Hale stays silent as the camera holds close on their face, the harbor log catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Nora Hale holds the silence after the line, the harbor log sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; MARGARET — low, polished, unhurried American English, never shouts
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (fierce): "That's not an accident. That's a choice."
  MARGARET (quiet): "You'll regret this."

ESCENA 60 (Viñeta #60 del Storyboard) — 09:50–10:00
- Location: Town hall hearing room, day, hard window light
- Characters Present: Nora Hale, Sam Calloway
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nora Hale and Sam Calloway: Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora Hale speaks as the camera holds close on their face, the clerk's desk catching the light between them. Location: Town hall hearing room, day, hard window light. Key object: the clerk's desk. Characters present: Nora Hale, Sam Calloway. No other characters appear.
- Identity Anchors: Nora Hale (Cast Sheet Pos #1: early thirties; dark auburn hair worn loose; wearing dark blazer, hair down, salt wind in it); Sam Calloway (Cast Sheet Pos #2: mid-thirties; short dark-sand hair; wearing faded canvas work jacket, dark trousers, worn boots)
- Key Object: the clerk's desk → Object In / Object Out: the clerk's desk → the clerk's desk
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nora Hale and Sam Calloway — Nora Hale and Sam Calloway face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nora Hale speaks as the camera holds close on their face, the clerk's desk catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: low-angle hero shot — Nora and Sam stand on the lighthouse point at dusk, an older ledger in Nora's hands. Key object in frame: the clerk's desk  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: insert shot of the evidence object — Nora Hale holds the silence after the line, the clerk's desk sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a crowded room holding its breath, paper on wood, wind off the water. Voice tone: NORA — warm mid-range American English, controlled, slightly breathy under pressure; SAM — quiet, low American English, careful diction, warmth under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NORA (hushed): "Wait. This ledger is older. Her name is on every page."
  SAM (stunned): "Nora... she's alive?"

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

---

## Paso 4 — Ensamblar

Cuando existan los 10 archivos `minute_01.mp4 … minute_10.mp4`:

```powershell
./novelfactory.bat assemble demo_contract
```

El ensamblador detecta el modo B, genera el máster 16:9 completo,
el SRT sincronizado y el teaser vertical automático de 20 segundos.

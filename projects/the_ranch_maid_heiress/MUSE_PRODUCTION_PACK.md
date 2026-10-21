# The Stable Girl — Producción con Muse AI (método nuevo)

**Slug:** `the_ranch_maid_heiress`  ·  **Escenas:** 60  ·  **Imágenes:** 11  ·  **Lotes:** 10

> Framed for stealing from the Montana ranch family that raised her, the stable maid discovers Silver Creek was never theirs to keep: her mother owned the land, and the proof is hidden in the barn where she died.

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
Actúa como director de casting y diseñador de personajes. Genera UNA SOLA IMAGEN horizontal 16:9 que muestre juntos, de cuerpo completo, de pie, mirando al frente sobre un fondo gris neutro de estudio (#808080) y sin tocarse entre sí, a los siguientes personajes de nuestra novela en estilo Cinematográfico Realista 35mm:

1. ELENA VANCE — Rol: Protagonista. Edad: mid-twenties. Rasgos físicos: Casting sheet for the character reference image: woman in her mid-twenties, sun-weathered gently angular face, long chestnut hair worn in a single low braid, calm dark-brown eyes, light freckling across the nose, a faint old scar through one eyebrow, slender but strong ranch build, signature faded blue denim work shirt and dark riding jeans.. Vestuario fijo: faded blue denim work shirt, dark riding jeans, worn boots, low braid.
2. VICTORIA BLACKWELL — Rol: Antagonista. Edad: mid-forties. Rasgos físicos: Casting sheet for the character reference image: woman in her mid-forties, sleek platinum-blonde bob, sharp cheekbones, cool grey eyes, immaculate posture, dark red lipstick, pearl earrings, signature emerald silk blouse over tailored black trousers.. Vestuario fijo: emerald silk blouse, tailored black trousers, pearl earrings.
3. RICHARD BLACKWELL — Rol: Heredero antagonista. Edad: thirty. Rasgos físicos: Casting sheet for the character reference image: man around thirty, clean-cut, sandy hair combed back, pale blue eyes, a practiced easy smile, tall athletic build, signature pressed white shirt under a charcoal blazer.. Vestuario fijo: pressed white shirt, charcoal blazer, polished boots.
4. COLE BARRETT — Rol: Interés romántico. Edad: early-thirties. Rasgos físicos: Casting sheet for the character reference image: man in his early thirties, weathered rancher hands, dark hair a little long under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, signature oiled tan canvas chore jacket over a grey henley.. Vestuario fijo: oiled tan canvas chore jacket over a grey henley, worn felt hat.
5. MAGGIE DOYLE — Rol: Aliada. Edad: late-fifties. Rasgos físicos: Casting sheet for the character reference image: woman in her late fifties, iron-grey hair pinned up in a loose bun, kind weathered face, small round glasses on a chain, floral house apron over a beige cardigan and a long dark skirt.. Vestuario fijo: floral house apron over a beige cardigan, long dark skirt.

Coloca únicamente debajo de cada personaje su nombre en mayúsculas. Mantén exactamente los mismos rostros, peinados y vestuarios en todas las imágenes del storyboard y de los lotes de Muse AI. Sin texto adicional, sin títulos, sin frases, sin logos, sin marcas de agua; solo la imagen de los personajes y sus nombres.
```

---

## Paso 2 — Storyboards (10 imágenes)

Genera cada imagen con el mismo estilo y los mismos personajes de la hoja maestra.
Guarda cada archivo en `storyboards/` con el nombre indicado.

### REF_GRID_MIN_01.png — Minuto 1 (escenas 1–6)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 1 (Escenas 1 a 6) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 1 (Blackwell mansion foyer, storm dusk): Acción visual: In the grand foyer, the maid in the denim work shirt freezes beside the shattered decanter while the woman in emerald silk towers over… Descripción: In the grand foyer, the maid in the denim work….
Viñeta 2 — Escena 2 (Silver Creek barn aisle, night): Acción visual: The barn aisle at night: the maid stands small between the stalls, the housekeeper a silhouette in the doorway, rain drumming on the tin… Descripción: The barn aisle at night: the maid stands small between….
Viñeta 3 — Escena 3 (Blackwell mansion foyer, night): Acción visual: In the foyer, the maid holds open her saddle bag while the woman in emerald silk points at it like evidence. Descripción: In the foyer, the maid holds open her saddle bag….
Viñeta 4 — Escena 4 (Silver Creek stable aisle, morning): Acción visual: In the stable aisle, the maid tightens a saddle girth while the heir behind her lifts the silver watch from her open bag. Descripción: In the stable aisle, the maid tightens a saddle girth….
Viñeta 5 — Escena 5 (Blackwell great room, morning): Acción visual: In the timber great room, the woman in emerald silk gestures to a chair; the maid in the denim work shirt stays standing. Descripción: In the timber great room, the woman in emerald silk….
Viñeta 6 — Escena 6 (Silver Creek barn doorway, late afternoon): Acción visual: At the barn door, the maid works a curry comb in slow circles while the foreman leans on the stall, speaking low. Descripción: At the barn door, the maid works a curry comb….

Mantén continuidad exacta de rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_02.png — Minuto 2 (escenas 7–12)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 2 (Escenas 7 a 12) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 7 (Blackwell study, late afternoon): Acción visual: In the lamplit study, the mistress sits behind the desk with one finger on a closed file; the maid stands before it. Descripción: In the lamplit study, the mistress sits behind the desk….
Viñeta 2 — Escena 8 (gatehouse cottage, dusk): Acción visual: In the small stone cottage, the maid kneels with the old saddle across her knees and works the leather lining open. Descripción: In the small stone cottage, the maid kneels with the….
Viñeta 3 — Escena 9 (Silver Creek barn aisle, night): Acción visual: In the barn aisle at night, the maid holds up the brass key while the foreman studies the whitewashed tack-room door behind them. Descripción: In the barn aisle at night, the maid holds up….
Viñeta 4 — Escena 10 (Silver Creek sealed tack room, night): Acción visual: Inside the tack room, the maid kneels over an open tin box while the foreman stands in the doorway with bolt cutters. Descripción: Inside the tack room, the maid kneels over an open….
Viñeta 5 — Escena 11 (Silver Creek county records office, morning): Acción visual: At the oak counter, the maid lays the old deed down while the clerk turns a heavy ledger toward her. Descripción: At the oak counter, the maid lays the old deed….
Viñeta 6 — Escena 12 (county records steps, grey morning): Acción visual: On the stone steps, the maid holds a folder to her chest while the foreman waits a step below, hat in hand. Descripción: On the stone steps, the maid holds a folder to….

Mantén continuidad exacta de rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_03.png — Minuto 3 (escenas 13–18)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 3 (Escenas 13 a 18) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 13 (Blackwell paneled office, afternoon): Acción visual: In the paneled office, the maid holds a single sheet of paper while the woman in black cashmere stands by the window, gloves in… Descripción: In the paneled office, the maid holds a single sheet….
Viñeta 2 — Escena 14 (Blackwell dark-paneled hallway, afternoon): Acción visual: In the dark-paneled hallway, the heir speaks low to the maid, hands open, while she holds her folder like a shield. Descripción: In the dark-paneled hallway, the heir speaks low to the….
Viñeta 3 — Escena 15 (gatehouse cottage, dusk): Acción visual: At the oilcloth table, the maid and the housekeeper sit across a covered pie neither has touched. Descripción: At the oilcloth table, the maid and the housekeeper sit….
Viñeta 4 — Escena 16 (Silver Creek barn aisle, night): Acción visual: In the barn aisle, the maid and the foreman stand on either side of a lantern, rain crossing the doorway behind him. Descripción: In the barn aisle, the maid and the foreman stand….
Viñeta 5 — Escena 17 (Blackwell study, night): Acción visual: In the lamplit study, the mistress stands over the desk while the heir paces and loosens his collar. Descripción: In the lamplit study, the mistress stands over the desk….
Viñeta 6 — Escena 18 (Silver Creek county records office, morning): Acción visual: At the counter, the clerk shakes her head over a sealed drawer while the maid's open folder waits untouched. Descripción: At the counter, the clerk shakes her head over a….

Mantén continuidad exacta de rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_04.png — Minuto 4 (escenas 19–24)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 4 (Escenas 19 a 24) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 19 (Blackwell great room, dinner, night): Acción visual: In the candlelit great room, the mistress rises with a glass while the maid stands at the edge of the tables, napkin in hand. Descripción: In the candlelit great room, the mistress rises with a….
Viñeta 2 — Escena 20 (Blackwell gravel yard, night): Acción visual: In the gravel yard at night, a steel barrel burns while the mistress holds out a folded paper and the maid watches the flames. Descripción: In the gravel yard at night, a steel barrel burns….
Viñeta 3 — Escena 21 (gatehouse cottage, night): Acción visual: In the cottage lamplight, the maid unrolls the old county survey map while the foreman anchors the curling corners with heavy iron horseshoes. Descripción: In the cottage lamplight, the maid unrolls the old county….
Viñeta 4 — Escena 22 (Blackwell tack room, night): Acción visual: In the shadowy tack room, the maid kneels beside the wall timber and slides a cylindrical tin case from the hollow cavity. Descripción: In the shadowy tack room, the maid kneels beside the….
Viñeta 5 — Escena 23 (Silver Creek barn hayloft, night): Acción visual: In the moonlight, the foreman gently binds the maid's bruised palm with white tape, his touch slow and deliberate. Descripción: In the moonlight, the foreman gently binds the maid's bruised….
Viñeta 6 — Escena 24 (Blackwell study archives, night): Acción visual: Behind the desk, the maid freezes with the open ledger as the heir steps over the threshold into the room. Descripción: Behind the desk, the maid freezes with the open ledger….

Mantén continuidad exacta de rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_05.png — Minuto 5 (escenas 25–30)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 5 (Escenas 25 a 30) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 25 (Blackwell mansion great room, night): Acción visual: In the vast room, the mistress dangles a small brass ribboned key while the maid stands rigid near the cold hearth. Descripción: In the vast room, the mistress dangles a small brass….
Viñeta 2 — Escena 26 (Blackwell mansion gravel drive, night): Acción visual: Under harsh halogen yard lights, the foreman plants his boots in front of the heir, refusing to yield the driveway. Descripción: Under harsh halogen yard lights, the foreman plants his boots….
Viñeta 3 — Escena 27 (gatehouse cottage porch, night): Acción visual: On the rain-slick porch steps, the heir reaches out with a cream envelope while the maid refuses to accept it. Descripción: On the rain-slick porch steps, the heir reaches out with….
Viñeta 4 — Escena 28 (Silver Creek barn aisle, night): Acción visual: In the barn aisle, the housekeeper rushes to the maid and grabs both of her elbows with trembling hands. Descripción: In the barn aisle, the housekeeper rushes to the maid….
Viñeta 5 — Escena 29 (Blackwell estate gates, midnight): Acción visual: By the iron gates, the mistress steps out of the luxury car into the headlights, holding a checkbook open. Descripción: By the iron gates, the mistress steps out of the….
Viñeta 6 — Escena 30 (Blackwell estate gates, midnight): Acción visual: Under the headlights, the mistress thrusts the certified check into the maid's face like an execution order. Descripción: Under the headlights, the mistress thrusts the certified check into….

Mantén continuidad exacta de rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_06.png — Minuto 6 (escenas 31–36)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 6 (Escenas 31 a 36) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 31 (gatehouse cottage, storm night): Acción visual: Inside the ransacked cottage, the storm sweeps through shattered windows, scattering torn clothes and broken crockery across wet stones. Descripción: Inside the ransacked cottage, the storm sweeps through shattered windows….
Viñeta 2 — Escena 32 (gatehouse cottage yard, storm night): Acción visual: In the swirling red and blue emergency light, the maid faces the padlocked gate as rain washes mud over her boots. Descripción: In the swirling red and blue emergency light, the maid….
Viñeta 3 — Escena 33 (Silver Creek hay shed, storm night): Acción visual: In the drafty shelter, the maid wraps her own dry flannel scarf around the weeping housekeeper's neck. Descripción: In the drafty shelter, the maid wraps her own dry….
Viñeta 4 — Escena 34 (Blackwell mansion rear terrace, storm night): Acción visual: Inside the glowing library, the mistress feeds the ancient deed into the fireplace flames while rain streaks the window. Descripción: Inside the glowing library, the mistress feeds the ancient deed….
Viñeta 5 — Escena 35 (Silver Creek stable tack room, storm night): Acción visual: In a sudden flash of lightning, the maid appears like a ghost in the stable door, blocking the heir's retreat. Descripción: In a sudden flash of lightning, the maid appears like….
Viñeta 6 — Escena 36 (ranch ridge overlook, storm dawn): Acción visual: On the high ridge, the small figure of the maid stands against the vast Montana valley as dawn breaks slate grey. Descripción: On the high ridge, the small figure of the maid….

Mantén continuidad exacta de rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_07.png — Minuto 7 (escenas 37–42)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 7 (Escenas 37 a 42) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 37 (ranch ridge road, dawn): Acción visual: On the muddy road, the foreman wraps his dry wool jacket around her, pulling the collar up against the wind. Descripción: On the muddy road, the foreman wraps his dry wool….
Viñeta 2 — Escena 38 (green truck cab, dawn): Acción visual: Inside the bouncing truck cab, the maid turns the brass key in the dashboard light, scraping away years of verdigris. Descripción: Inside the bouncing truck cab, the maid turns the brass….
Viñeta 3 — Escena 39 (town bank exterior, morning): Acción visual: On the bank steps, the maid and foreman turn together as the limousine door opens across the street. Descripción: On the bank steps, the maid and foreman turn together….
Viñeta 4 — Escena 40 (First Valley Trust vault corridor, morning): Acción visual: Inside the gleaming vault, the maid turns the brass key into Lock 14; the heavy tumbler clicks open with a hollow ring. Descripción: Inside the gleaming vault, the maid turns the brass key….
Viñeta 5 — Escena 41 (First Valley Trust manager office, morning): Acción visual: In the sunlit bank office, the maid stands tall as the grey-haired bank manager examines the embossed blue notary seal through his bifocals. Descripción: In the sunlit bank office, the maid stands tall as….
Viñeta 6 — Escena 42 (town bank steps, morning): Acción visual: On the stone steps, the foreman stands immovable between the mistress and the bank doors, ignoring the sheriff's warning stance. Descripción: On the stone steps, the foreman stands immovable between the….

Mantén continuidad exacta de rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_08.png — Minuto 8 (escenas 43–48)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 8 (Escenas 43 a 48) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 43 (town bank steps, morning): Acción visual: The maid emerges onto the sunlit steps, lifting the stamped court-certified envelope for the entire sidewalk to see. Descripción: The maid emerges onto the sunlit steps, lifting the stamped….
Viñeta 2 — Escena 44 (Blackwell town car, morning): Acción visual: Inside the town car, the mistress grabs her son's lapel as he pulls himself back against the passenger door. Descripción: Inside the town car, the mistress grabs her son's lapel….
Viñeta 3 — Escena 45 (county civic hall back alley, noon): Acción visual: In the brick alleyway, the housekeeper presses an aged leather journal into the maid's hands, tears in her eyes. Descripción: In the brick alleyway, the housekeeper presses an aged leather….
Viñeta 4 — Escena 46 (Silver Creek civic hall foyer, afternoon): Acción visual: Before the towering carved oak doors, the maid pauses, adjusting her mother's silver belt buckle. Descripción: Before the towering carved oak doors, the maid pauses, adjusting….
Viñeta 5 — Escena 47 (civic hall grand ballroom, afternoon): Acción visual: The grand ballroom falls utterly silent as the ranch maid in her simple white shirt strides down the red carpet toward the stage. Descripción: The grand ballroom falls utterly silent as the ranch maid….
Viñeta 6 — Escena 48 (civic hall auction stage, afternoon): Acción visual: Under the blinding stage lights, the mistress steps right into the maid's face, abandoning all high-society poise. Descripción: Under the blinding stage lights, the mistress steps right into….

Mantén continuidad exacta de rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_09.png — Minuto 9 (escenas 49–54)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 9 (Escenas 49 a 54) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 49 (civic hall auction stage, afternoon): Acción visual: At the edge of the stage, the maid hands the heavy blue legal dossier down to the seated county probate judge. Descripción: At the edge of the stage, the maid hands the….
Viñeta 2 — Escena 50 (civic hall stage wings, afternoon): Acción visual: In the red velvet backstage shadows, the mistress corners the maid against the rope rigging, eyes feverish with malice. Descripción: In the red velvet backstage shadows, the mistress corners the….
Viñeta 3 — Escena 51 (Silver Creek barn exterior, dusk): Acción visual: The maid sprints through the barn gates as the foreman yanks a lit flare from a captured trespasser's hand. Descripción: The maid sprints through the barn gates as the foreman….
Viñeta 4 — Escena 52 (civic hall courtroom chamber, evening): Acción visual: At the witness stand, the heir raises his right hand before the court clerk, his voice echoing across the silent gallery. Descripción: At the witness stand, the heir raises his right hand….
Viñeta 5 — Escena 53 (civic hall courtroom chamber, evening): Acción visual: The housekeeper stands tall at the microphone, looking directly at the district attorney with tearful dignity. Descripción: The housekeeper stands tall at the microphone, looking directly at….
Viñeta 6 — Escena 54 (civic hall courtroom chamber, evening): Acción visual: At the plaintiff's table, the maid stands erect as the judge brings the wooden gavel down with final authority. Descripción: At the plaintiff's table, the maid stands erect as the….

Mantén continuidad exacta de rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_10.png — Minuto 10 (escenas 55–60)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 10 (Escenas 55 a 60) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 55 (civic hall grand steps, night): Acción visual: Under the flashing blue lights of state police cruisers, the troopers secure handcuffs behind the mistress's back. Descripción: Under the flashing blue lights of state police cruisers, the….
Viñeta 2 — Escena 56 (civic hall grand steps, night): Acción visual: On the wet steps, the handcuffed mistress collapses forward onto her knees before the maid she once tormented. Descripción: On the wet steps, the handcuffed mistress collapses forward onto….
Viñeta 3 — Escena 57 (Silver Creek mansion foyer, night): Acción visual: The grand foyer is warm with lamplight; the maid stands where she was once humiliated, now as the estate's mistress. Descripción: The grand foyer is warm with lamplight; the maid stands….
Viñeta 4 — Escena 58 (Silver Creek barn gate, moonlight): Acción visual: At the corral gate, the foreman turns to the maid, nervously rolling the brim of his felt hat in both hands. Descripción: At the corral gate, the foreman turns to the maid….
Viñeta 5 — Escena 59 (Blackwell great room mantelpiece, night): Acción visual: Before the roaring stone hearth, the maid steps back as June Vance's smiling photograph occupies the place of honor. Descripción: Before the roaring stone hearth, the maid steps back as….
Viñeta 6 — Escena 60 (mansion study desk, night): Acción visual: At the quiet study desk, the maid notices a sealed wax envelope attached to the back of the will parchment. Descripción: At the quiet study desk, the maid notices a sealed….

Mantén continuidad exacta de rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

---

## Paso 3 — Lotes Muse AI (10 videos de 1 minuto)

En cada lote: adjunta los dos archivos indicados y pega **un guion completo**
(16:9 para YouTube o 9:16 para Reels/Shorts). El guion ya termina con el comando final.

### Lote 01 — Minuto 1 (escenas 1–6)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_01.png`

**Guardar 16:9 como:** `raw_clips/minute_01.mp4`

**Guardar 9:16 como:** `raw_clips/minute_01_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 1 (Viñeta #1 del Storyboard) — 00:00–00:10
- Location: Blackwell mansion foyer, storm dusk
- Characters Present: Victoria Blackwell, Elena Vance, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the grand foyer, the maid in the denim work shirt freezes beside the shattered decanter while the woman in emerald silk towers over her.
  * [03s–07s]: tight close-up — Close on the maid's hands withdrawing from the broken crystal; her fingers tremble once, then go still.
  * [07s–10s]: over-the-shoulder shot — Over the maid's shoulder, the woman in emerald silk stares her down while the heir in the white shirt watches from the staircase.
- Sound Design (SFX & Voice Tone): storm wind at the tall windows, crystal settling on oak, the chandelier's faint creak, one held breath. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (cold, precise): "Twelve years in my house, and you steal from me at my son's welcome party."
  ELENA (quiet, shaking): "I didn't touch it. I was in the barn, where I always am."

ESCENA 2 (Viñeta #2 del Storyboard) — 00:10–00:20
- Location: Silver Creek barn aisle, night
- Characters Present: Elena Vance, Maggie Doyle
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — The barn aisle at night: the maid stands small between the stalls, the housekeeper a silhouette in the doorway, rain drumming on the tin roof.
  * [03s–07s]: over-the-shoulder shot — Over the maid's shoulder, the old photograph shows a woman at a ranch gate, sun-bleached and smiling.
  * [07s–10s]: tight close-up — Close on the housekeeper's face as she recognizes the photograph; she closes her eyes for one beat.
- Sound Design (SFX & Voice Tone): rain on a tin roof, a horse shifting in straw, a bucket chain rattling. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  MAGGIE (gentle): "Your mother fed this barn before you could walk. Don't let them erase her."
  ELENA (low): "They erased her fifteen years ago. I was too small to stop them."

ESCENA 3 (Viñeta #3 del Storyboard) — 00:20–00:30
- Location: Blackwell mansion foyer, night
- Characters Present: Victoria Blackwell, Elena Vance, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the foyer, the maid holds open her saddle bag while the woman in emerald silk points at it like evidence.
  * [03s–07s]: tight close-up — Close on the maid's face as she sets her jaw; her hands close around the worn leather.
  * [07s–10s]: low-angle hero shot — Low angle on the maid from below the staircase, chin lifted, the chandelier hard above her.
- Sound Design (SFX & Voice Tone): leather creaking, a clock ticking somewhere deep in the house, rain softening. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (silky, cruel): "Empty it. If my husband's watch is in there, you leave this ranch tonight."
  ELENA (steady): "My mother's things are in that bag. You will not touch them."

ESCENA 4 (Viñeta #4 del Storyboard) — 00:30–00:40
- Location: Silver Creek stable aisle, morning
- Characters Present: Elena Vance, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the stable aisle, the maid tightens a saddle girth while the heir behind her lifts the silver watch from her open bag.
  * [03s–07s]: insert shot of the evidence object — Insert: the silver watch turns once in the heir's fingers, catching a blade of window light.
  * [07s–10s]: tight close-up — Close on the maid as she turns and sees him; her hands go still on the leather.
- Sound Design (SFX & Voice Tone): a horse snorting, leather straps, straw under boots, the watch's tiny clasp. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  RICHARD (light, rehearsed): "Look what your mother's saddle was hiding. Twelve years, and you kept it close."
  ELENA (low, furious): "You were in the tack room last night. I saw your boots."

ESCENA 5 (Viñeta #5 del Storyboard) — 00:40–00:50
- Location: Blackwell great room, morning
- Characters Present: Victoria Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the timber great room, the woman in emerald silk gestures to a chair; the maid in the denim work shirt stays standing.
  * [03s–07s]: over-the-shoulder shot — Over the mistress's shoulder, the folded confession paper waits on the low table between them.
  * [07s–10s]: tight close-up — Close on the maid's hand as she slides the paper back across the table without sitting.
- Sound Design (SFX & Voice Tone): a fireplace ticking as it cools, paper sliding on wood, a chair creaking. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (patient, poisoned): "Sign it, take your pay, and this stays private. The watch never happened."
  ELENA (flat): "It never happened to you. It happened to me the moment you decided it did."

ESCENA 6 (Viñeta #6 del Storyboard) — 00:50–01:00
- Location: Silver Creek barn doorway, late afternoon
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the barn door, the maid works a curry comb in slow circles while the foreman leans on the stall, speaking low.
  * [03s–07s]: over-the-shoulder shot — Over the maid's shoulder: the foreman's hands tighten on the stall door as he finishes his sentence.
  * [07s–10s]: tight close-up — Close on the maid's eyes lifting at last, weighing what he just offered.
- Sound Design (SFX & Voice Tone): curry comb against hide, a horse's low nicker, wind under the eaves. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (quiet): "I saw Richard at the saddles last night. Say the word and I'll swear it."
  ELENA (careful): "He'll only call you a liar. And then he'll take your house too."

COMANDO FINAL (16:9 YouTube):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 1 (Viñeta #1 del Storyboard) — 00:00–00:10
- Location: Blackwell mansion foyer, storm dusk
- Characters Present: Victoria Blackwell, Elena Vance, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the grand foyer, the maid in the denim work shirt freezes beside the shattered decanter while the woman in emerald silk towers over her.
  * [03s–07s]: tight close-up — Close on the maid's hands withdrawing from the broken crystal; her fingers tremble once, then go still.
  * [07s–10s]: over-the-shoulder shot — Over the maid's shoulder, the woman in emerald silk stares her down while the heir in the white shirt watches from the staircase.
- Sound Design (SFX & Voice Tone): storm wind at the tall windows, crystal settling on oak, the chandelier's faint creak, one held breath. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (cold, precise): "Twelve years in my house, and you steal from me at my son's welcome party."
  ELENA (quiet, shaking): "I didn't touch it. I was in the barn, where I always am."

ESCENA 2 (Viñeta #2 del Storyboard) — 00:10–00:20
- Location: Silver Creek barn aisle, night
- Characters Present: Elena Vance, Maggie Doyle
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — The barn aisle at night: the maid stands small between the stalls, the housekeeper a silhouette in the doorway, rain drumming on the tin roof.
  * [03s–07s]: over-the-shoulder shot — Over the maid's shoulder, the old photograph shows a woman at a ranch gate, sun-bleached and smiling.
  * [07s–10s]: tight close-up — Close on the housekeeper's face as she recognizes the photograph; she closes her eyes for one beat.
- Sound Design (SFX & Voice Tone): rain on a tin roof, a horse shifting in straw, a bucket chain rattling. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  MAGGIE (gentle): "Your mother fed this barn before you could walk. Don't let them erase her."
  ELENA (low): "They erased her fifteen years ago. I was too small to stop them."

ESCENA 3 (Viñeta #3 del Storyboard) — 00:20–00:30
- Location: Blackwell mansion foyer, night
- Characters Present: Victoria Blackwell, Elena Vance, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the foyer, the maid holds open her saddle bag while the woman in emerald silk points at it like evidence.
  * [03s–07s]: tight close-up — Close on the maid's face as she sets her jaw; her hands close around the worn leather.
  * [07s–10s]: low-angle hero shot — Low angle on the maid from below the staircase, chin lifted, the chandelier hard above her.
- Sound Design (SFX & Voice Tone): leather creaking, a clock ticking somewhere deep in the house, rain softening. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (silky, cruel): "Empty it. If my husband's watch is in there, you leave this ranch tonight."
  ELENA (steady): "My mother's things are in that bag. You will not touch them."

ESCENA 4 (Viñeta #4 del Storyboard) — 00:30–00:40
- Location: Silver Creek stable aisle, morning
- Characters Present: Elena Vance, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the stable aisle, the maid tightens a saddle girth while the heir behind her lifts the silver watch from her open bag.
  * [03s–07s]: insert shot of the evidence object — Insert: the silver watch turns once in the heir's fingers, catching a blade of window light.
  * [07s–10s]: tight close-up — Close on the maid as she turns and sees him; her hands go still on the leather.
- Sound Design (SFX & Voice Tone): a horse snorting, leather straps, straw under boots, the watch's tiny clasp. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  RICHARD (light, rehearsed): "Look what your mother's saddle was hiding. Twelve years, and you kept it close."
  ELENA (low, furious): "You were in the tack room last night. I saw your boots."

ESCENA 5 (Viñeta #5 del Storyboard) — 00:40–00:50
- Location: Blackwell great room, morning
- Characters Present: Victoria Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the timber great room, the woman in emerald silk gestures to a chair; the maid in the denim work shirt stays standing.
  * [03s–07s]: over-the-shoulder shot — Over the mistress's shoulder, the folded confession paper waits on the low table between them.
  * [07s–10s]: tight close-up — Close on the maid's hand as she slides the paper back across the table without sitting.
- Sound Design (SFX & Voice Tone): a fireplace ticking as it cools, paper sliding on wood, a chair creaking. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (patient, poisoned): "Sign it, take your pay, and this stays private. The watch never happened."
  ELENA (flat): "It never happened to you. It happened to me the moment you decided it did."

ESCENA 6 (Viñeta #6 del Storyboard) — 00:50–01:00
- Location: Silver Creek barn doorway, late afternoon
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the barn door, the maid works a curry comb in slow circles while the foreman leans on the stall, speaking low.
  * [03s–07s]: over-the-shoulder shot — Over the maid's shoulder: the foreman's hands tighten on the stall door as he finishes his sentence.
  * [07s–10s]: tight close-up — Close on the maid's eyes lifting at last, weighing what he just offered.
- Sound Design (SFX & Voice Tone): curry comb against hide, a horse's low nicker, wind under the eaves. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (quiet): "I saw Richard at the saddles last night. Say the word and I'll swear it."
  ELENA (careful): "He'll only call you a liar. And then he'll take your house too."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 para Reels, TikTok y Shorts."
```

### Lote 02 — Minuto 2 (escenas 7–12)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_02.png`

**Guardar 16:9 como:** `raw_clips/minute_02.mp4`

**Guardar 9:16 como:** `raw_clips/minute_02_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 7 (Viñeta #7 del Storyboard) — 01:00–01:10
- Location: Blackwell study, late afternoon
- Characters Present: Victoria Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the lamplit study, the mistress sits behind the desk with one finger on a closed file; the maid stands before it.
  * [03s–07s]: tight close-up — Close on the file as her finger lifts, leaving a clean mark in the dust.
  * [07s–10s]: low-angle hero shot — Low angle on the maid as she absorbs the deadline without looking away.
- Sound Design (SFX & Voice Tone): a desk clock ticking, leather chair creaking, the window rattling softly. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (unhurried): "Sheriff Drummond is a family friend. You have until Friday midnight, Elena. Sign, or be charged."
  ELENA (quiet): "And my mother's grave? Do you still pay the keeper to keep it?"

ESCENA 8 (Viñeta #8 del Storyboard) — 01:10–01:20
- Location: gatehouse cottage, dusk
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium close-up — In the small stone cottage, the maid kneels with the old saddle across her knees and works the leather lining open.
  * [03s–07s]: insert shot of the evidence object — Insert: her fingers draw a small brass key from the hidden seam, warm against the cold leather.
  * [07s–10s]: tight close-up — Close on her face as she recognizes the key; the room darkens around her.
- Sound Design (SFX & Voice Tone): wind pressing the eaves, leather creaking, a stove ticking as it cools. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (whispered): "You sewed it into the lining, Mama. What were you afraid someone would find?"
  ELENA (breaking): "And why did you never tell me?"

ESCENA 9 (Viñeta #9 del Storyboard) — 01:20–01:30
- Location: Silver Creek barn aisle, night
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the barn aisle at night, the maid holds up the brass key while the foreman studies the whitewashed tack-room door behind them.
  * [03s–07s]: insert shot of the evidence object — Insert: the small brass key turns under the bulb, too delicate for any hasp in the barn.
  * [07s–10s]: over-the-shoulder shot — Over her shoulder: the painted-over iron hasp, sealed with fifteen years of whitewash.
- Sound Design (SFX & Voice Tone): a bulb humming, a horse stamping, wind rattling the barn planks. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (low): "That key fits no door in this valley. Your mother never did one thing without a reason."
  ELENA (decided): "Then we open that room. Tonight."

ESCENA 10 (Viñeta #10 del Storyboard) — 01:30–01:40
- Location: Silver Creek sealed tack room, night
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Inside the tack room, the maid kneels over an open tin box while the foreman stands in the doorway with bolt cutters.
  * [03s–07s]: insert shot of the evidence object — Insert: a cream deed unfolds in her hands, its old seal still intact.
  * [07s–10s]: tight close-up — Close on her face as she reads the name; her lips part, and she has to steady the paper.
- Sound Design (SFX & Voice Tone): a work lamp buzzing, old paper unfolding, a chain shifting outside, rain starting. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; COLE — quiet, low American English, careful diction, warmth held under restraint
- Dialogue (English, 6–8 sec max):
  ELENA (barely audible): "This deed says Vance. Not Blackwell. My mother owned Silver Creek."
  COLE (rough): "Then the fire wasn't bad luck. And I should have told you something years ago."

ESCENA 11 (Viñeta #11 del Storyboard) — 01:40–01:50
- Location: Silver Creek county records office, morning
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the oak counter, the maid lays the old deed down while the clerk turns a heavy ledger toward her.
  * [03s–07s]: insert shot of the evidence object — Insert: the ledger's ruled page for the Silver Creek parcel, stamped and countersigned.
  * [07s–10s]: tight close-up — Close on the maid as the clerk's answer lands; her jaw sets, but her eyes drop.
- Sound Design (SFX & Voice Tone): ledger pages turning, a wall clock, boots on creaking wood. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  CLERK (neutral): "The sale was recorded in 2009. Blackwell owns it. Without a probate file, miss, you're not even her heir."
  ELENA (low): "Then open a probate file."

ESCENA 12 (Viñeta #12 del Storyboard) — 01:50–02:00
- Location: county records steps, grey morning
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — On the stone steps, the maid holds a folder to her chest while the foreman waits a step below, hat in hand.
  * [03s–07s]: tight close-up — Close on her hands tightening on the folder's edge until the card bends.
  * [07s–10s]: over-the-shoulder shot — Over the foreman's shoulder: her face against the grey street, deciding.
- Sound Design (SFX & Voice Tone): wind across stone steps, a truck passing on wet asphalt, a flag snapping. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (careful): "Probate takes months. Victoria's already on the phone with her lawyer."
  ELENA (steady): "Then I won't fight her with a lawyer. I'll fight her with what she's afraid of."

COMANDO FINAL (16:9 YouTube):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 7 (Viñeta #7 del Storyboard) — 01:00–01:10
- Location: Blackwell study, late afternoon
- Characters Present: Victoria Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the lamplit study, the mistress sits behind the desk with one finger on a closed file; the maid stands before it.
  * [03s–07s]: tight close-up — Close on the file as her finger lifts, leaving a clean mark in the dust.
  * [07s–10s]: low-angle hero shot — Low angle on the maid as she absorbs the deadline without looking away.
- Sound Design (SFX & Voice Tone): a desk clock ticking, leather chair creaking, the window rattling softly. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (unhurried): "Sheriff Drummond is a family friend. You have until Friday midnight, Elena. Sign, or be charged."
  ELENA (quiet): "And my mother's grave? Do you still pay the keeper to keep it?"

ESCENA 8 (Viñeta #8 del Storyboard) — 01:10–01:20
- Location: gatehouse cottage, dusk
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium close-up — In the small stone cottage, the maid kneels with the old saddle across her knees and works the leather lining open.
  * [03s–07s]: insert shot of the evidence object — Insert: her fingers draw a small brass key from the hidden seam, warm against the cold leather.
  * [07s–10s]: tight close-up — Close on her face as she recognizes the key; the room darkens around her.
- Sound Design (SFX & Voice Tone): wind pressing the eaves, leather creaking, a stove ticking as it cools. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (whispered): "You sewed it into the lining, Mama. What were you afraid someone would find?"
  ELENA (breaking): "And why did you never tell me?"

ESCENA 9 (Viñeta #9 del Storyboard) — 01:20–01:30
- Location: Silver Creek barn aisle, night
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the barn aisle at night, the maid holds up the brass key while the foreman studies the whitewashed tack-room door behind them.
  * [03s–07s]: insert shot of the evidence object — Insert: the small brass key turns under the bulb, too delicate for any hasp in the barn.
  * [07s–10s]: over-the-shoulder shot — Over her shoulder: the painted-over iron hasp, sealed with fifteen years of whitewash.
- Sound Design (SFX & Voice Tone): a bulb humming, a horse stamping, wind rattling the barn planks. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (low): "That key fits no door in this valley. Your mother never did one thing without a reason."
  ELENA (decided): "Then we open that room. Tonight."

ESCENA 10 (Viñeta #10 del Storyboard) — 01:30–01:40
- Location: Silver Creek sealed tack room, night
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Inside the tack room, the maid kneels over an open tin box while the foreman stands in the doorway with bolt cutters.
  * [03s–07s]: insert shot of the evidence object — Insert: a cream deed unfolds in her hands, its old seal still intact.
  * [07s–10s]: tight close-up — Close on her face as she reads the name; her lips part, and she has to steady the paper.
- Sound Design (SFX & Voice Tone): a work lamp buzzing, old paper unfolding, a chain shifting outside, rain starting. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; COLE — quiet, low American English, careful diction, warmth held under restraint
- Dialogue (English, 6–8 sec max):
  ELENA (barely audible): "This deed says Vance. Not Blackwell. My mother owned Silver Creek."
  COLE (rough): "Then the fire wasn't bad luck. And I should have told you something years ago."

ESCENA 11 (Viñeta #11 del Storyboard) — 01:40–01:50
- Location: Silver Creek county records office, morning
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the oak counter, the maid lays the old deed down while the clerk turns a heavy ledger toward her.
  * [03s–07s]: insert shot of the evidence object — Insert: the ledger's ruled page for the Silver Creek parcel, stamped and countersigned.
  * [07s–10s]: tight close-up — Close on the maid as the clerk's answer lands; her jaw sets, but her eyes drop.
- Sound Design (SFX & Voice Tone): ledger pages turning, a wall clock, boots on creaking wood. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  CLERK (neutral): "The sale was recorded in 2009. Blackwell owns it. Without a probate file, miss, you're not even her heir."
  ELENA (low): "Then open a probate file."

ESCENA 12 (Viñeta #12 del Storyboard) — 01:50–02:00
- Location: county records steps, grey morning
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — On the stone steps, the maid holds a folder to her chest while the foreman waits a step below, hat in hand.
  * [03s–07s]: tight close-up — Close on her hands tightening on the folder's edge until the card bends.
  * [07s–10s]: over-the-shoulder shot — Over the foreman's shoulder: her face against the grey street, deciding.
- Sound Design (SFX & Voice Tone): wind across stone steps, a truck passing on wet asphalt, a flag snapping. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (careful): "Probate takes months. Victoria's already on the phone with her lawyer."
  ELENA (steady): "Then I won't fight her with a lawyer. I'll fight her with what she's afraid of."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 para Reels, TikTok y Shorts."
```

### Lote 03 — Minuto 3 (escenas 13–18)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_03.png`

**Guardar 16:9 como:** `raw_clips/minute_03.mp4`

**Guardar 9:16 como:** `raw_clips/minute_03_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 13 (Viñeta #13 del Storyboard) — 02:00–02:10
- Location: Blackwell paneled office, afternoon
- Characters Present: Victoria Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the paneled office, the maid holds a single sheet of paper while the woman in black cashmere stands by the window, gloves in hand.
  * [03s–07s]: over-the-shoulder shot — Over the maid's shoulder: the paper offers a year of grave upkeep and a dropped charge.
  * [07s–10s]: tight close-up — Close on the maid's face: she reads the terms, and something in her goes cold.
- Sound Design (SFX & Voice Tone): a coal settling in the grate, gloves creaking, wind at the window. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (soft, final): "I'll keep your mother's grave tended another year. Leave Silver Creek, and the watch charge disappears."
  ELENA (quiet): "You're offering me a gardener. Not my mother's name."

ESCENA 14 (Viñeta #14 del Storyboard) — 02:10–02:20
- Location: Blackwell dark-paneled hallway, afternoon
- Characters Present: Richard Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the dark-paneled hallway, the heir speaks low to the maid, hands open, while she holds her folder like a shield.
  * [03s–07s]: tight close-up — Close on the heir's face: the practiced smile is gone for once.
  * [07s–10s]: over-the-shoulder shot — Over his shoulder: the maid's eyes narrow, reading the first honest thing he's said.
- Sound Design (SFX & Voice Tone): a floorboard creaking, wind at the high window, muffled voices from below. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  RICHARD (low): "I know you didn't take the watch. Leave before she decides you're dangerous."
  ELENA (cold): "Why do you care?"
  RICHARD (beat): "Because you keep digging where the whole valley is buried."

ESCENA 15 (Viñeta #15 del Storyboard) — 02:20–02:30
- Location: gatehouse cottage, dusk
- Characters Present: Elena Vance, Maggie Doyle
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the oilcloth table, the maid and the housekeeper sit across a covered pie neither has touched.
  * [03s–07s]: tight close-up — Close on the housekeeper's hands twisting a napkin until the linen frays.
  * [07s–10s]: over-the-shoulder shot — Over the housekeeper's shoulder: the maid's face as she understands what was signed.
- Sound Design (SFX & Voice Tone): the stove ticking, wind at the eaves, a spoon rattling against china. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  MAGGIE (unsteady): "The night of the fire, I signed a statement for her. I said the lamp fell. It was a lie."
  ELENA (hurt): "You told them my mother was careless."

ESCENA 16 (Viñeta #16 del Storyboard) — 02:30–02:40
- Location: Silver Creek barn aisle, night
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the barn aisle, the maid and the foreman stand on either side of a lantern, rain crossing the doorway behind him.
  * [03s–07s]: tight close-up — Close on the foreman's jaw as he forces the words out.
  * [07s–10s]: over-the-shoulder shot — Over his shoulder: the maid's face as she takes the confession without blinking.
- Sound Design (SFX & Voice Tone): rain hammering the doorway, lantern glass ticking, a horse stamping in straw. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (rough): "The night of the fire I was fifteen. I saw a truck leave."
  ELENA (quiet): "You watched it leave and said nothing."

ESCENA 17 (Viñeta #17 del Storyboard) — 02:40–02:50
- Location: Blackwell study, night
- Characters Present: Victoria Blackwell, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the lamplit study, the mistress stands over the desk while the heir paces and loosens his collar.
  * [03s–07s]: tight close-up — Close on her hand closing a folder marked only by a county seal.
  * [07s–10s]: over-the-shoulder shot — Over her shoulder: the heir's reflection in the dark window, caught between defiance and fear.
- Sound Design (SFX & Voice Tone): a drawer sliding shut, rain against glass, a lamp humming. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  VICTORIA (cold): "The probate clerk called. Someone requested June Vance's file. Bury it."
  RICHARD (edged): "You're good at that. The watch was your idea, remember?"

ESCENA 18 (Viñeta #18 del Storyboard) — 02:50–03:00
- Location: Silver Creek county records office, morning
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the counter, the clerk shakes her head over a sealed drawer while the maid's open folder waits untouched.
  * [03s–07s]: insert shot of the evidence object — Insert: the drawer's small brass lock, closed and freshly oiled.
  * [07s–10s]: tight close-up — Close on the maid as the refusal lands; she doesn't look away.
- Sound Design (SFX & Voice Tone): a drawer lock clicking, a clock, a pen set down too carefully. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  CLERK (uncomfortable): "The file was pulled by the Blackwell estate. There's no record you're her daughter."
  ELENA (quiet): "There's a record somewhere. She made sure of it."

COMANDO FINAL (16:9 YouTube):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 13 (Viñeta #13 del Storyboard) — 02:00–02:10
- Location: Blackwell paneled office, afternoon
- Characters Present: Victoria Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the paneled office, the maid holds a single sheet of paper while the woman in black cashmere stands by the window, gloves in hand.
  * [03s–07s]: over-the-shoulder shot — Over the maid's shoulder: the paper offers a year of grave upkeep and a dropped charge.
  * [07s–10s]: tight close-up — Close on the maid's face: she reads the terms, and something in her goes cold.
- Sound Design (SFX & Voice Tone): a coal settling in the grate, gloves creaking, wind at the window. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (soft, final): "I'll keep your mother's grave tended another year. Leave Silver Creek, and the watch charge disappears."
  ELENA (quiet): "You're offering me a gardener. Not my mother's name."

ESCENA 14 (Viñeta #14 del Storyboard) — 02:10–02:20
- Location: Blackwell dark-paneled hallway, afternoon
- Characters Present: Richard Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the dark-paneled hallway, the heir speaks low to the maid, hands open, while she holds her folder like a shield.
  * [03s–07s]: tight close-up — Close on the heir's face: the practiced smile is gone for once.
  * [07s–10s]: over-the-shoulder shot — Over his shoulder: the maid's eyes narrow, reading the first honest thing he's said.
- Sound Design (SFX & Voice Tone): a floorboard creaking, wind at the high window, muffled voices from below. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  RICHARD (low): "I know you didn't take the watch. Leave before she decides you're dangerous."
  ELENA (cold): "Why do you care?"
  RICHARD (beat): "Because you keep digging where the whole valley is buried."

ESCENA 15 (Viñeta #15 del Storyboard) — 02:20–02:30
- Location: gatehouse cottage, dusk
- Characters Present: Elena Vance, Maggie Doyle
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the oilcloth table, the maid and the housekeeper sit across a covered pie neither has touched.
  * [03s–07s]: tight close-up — Close on the housekeeper's hands twisting a napkin until the linen frays.
  * [07s–10s]: over-the-shoulder shot — Over the housekeeper's shoulder: the maid's face as she understands what was signed.
- Sound Design (SFX & Voice Tone): the stove ticking, wind at the eaves, a spoon rattling against china. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  MAGGIE (unsteady): "The night of the fire, I signed a statement for her. I said the lamp fell. It was a lie."
  ELENA (hurt): "You told them my mother was careless."

ESCENA 16 (Viñeta #16 del Storyboard) — 02:30–02:40
- Location: Silver Creek barn aisle, night
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the barn aisle, the maid and the foreman stand on either side of a lantern, rain crossing the doorway behind him.
  * [03s–07s]: tight close-up — Close on the foreman's jaw as he forces the words out.
  * [07s–10s]: over-the-shoulder shot — Over his shoulder: the maid's face as she takes the confession without blinking.
- Sound Design (SFX & Voice Tone): rain hammering the doorway, lantern glass ticking, a horse stamping in straw. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (rough): "The night of the fire I was fifteen. I saw a truck leave."
  ELENA (quiet): "You watched it leave and said nothing."

ESCENA 17 (Viñeta #17 del Storyboard) — 02:40–02:50
- Location: Blackwell study, night
- Characters Present: Victoria Blackwell, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the lamplit study, the mistress stands over the desk while the heir paces and loosens his collar.
  * [03s–07s]: tight close-up — Close on her hand closing a folder marked only by a county seal.
  * [07s–10s]: over-the-shoulder shot — Over her shoulder: the heir's reflection in the dark window, caught between defiance and fear.
- Sound Design (SFX & Voice Tone): a drawer sliding shut, rain against glass, a lamp humming. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  VICTORIA (cold): "The probate clerk called. Someone requested June Vance's file. Bury it."
  RICHARD (edged): "You're good at that. The watch was your idea, remember?"

ESCENA 18 (Viñeta #18 del Storyboard) — 02:50–03:00
- Location: Silver Creek county records office, morning
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the counter, the clerk shakes her head over a sealed drawer while the maid's open folder waits untouched.
  * [03s–07s]: insert shot of the evidence object — Insert: the drawer's small brass lock, closed and freshly oiled.
  * [07s–10s]: tight close-up — Close on the maid as the refusal lands; she doesn't look away.
- Sound Design (SFX & Voice Tone): a drawer lock clicking, a clock, a pen set down too carefully. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  CLERK (uncomfortable): "The file was pulled by the Blackwell estate. There's no record you're her daughter."
  ELENA (quiet): "There's a record somewhere. She made sure of it."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 para Reels, TikTok y Shorts."
```

### Lote 04 — Minuto 4 (escenas 19–24)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_04.png`

**Guardar 16:9 como:** `raw_clips/minute_04.mp4`

**Guardar 9:16 como:** `raw_clips/minute_04_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 19 (Viñeta #19 del Storyboard) — 03:00–03:10
- Location: Blackwell great room, dinner, night
- Characters Present: Victoria Blackwell, Elena Vance, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the candlelit great room, the mistress rises with a glass while the maid stands at the edge of the tables, napkin in hand.
  * [03s–07s]: tight close-up — Close on the maid's face as every guest turns toward her.
  * [07s–10s]: low-angle hero shot — Low angle on the maid as she answers the toast without dropping her gaze.
- Sound Design (SFX & Voice Tone): silverware on china, a glass set down, a room going quiet. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (bright, public): "Elena will be leaving us soon. Tell them, dear — what are your plans?"
  ELENA (calm, clear): "Mrs. Blackwell is too kind. My plans haven't changed. I'm staying."

ESCENA 20 (Viñeta #20 del Storyboard) — 03:10–03:20
- Location: Blackwell gravel yard, night
- Characters Present: Victoria Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the gravel yard at night, a steel barrel burns while the mistress holds out a folded paper and the maid watches the flames.
  * [03s–07s]: insert shot of the evidence object — Insert: the old saddle's leather curling in the fire, stitching glowing before it blackens.
  * [07s–10s]: tight close-up — Close on the maid's face lit by fire; she does not step back.
- Sound Design (SFX & Voice Tone): fire roaring in a steel barrel, gravel under boots, a radio crackling in the sheriff's car. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (quiet, absolute): "Sign by midnight, or I press charges for arson as well as theft."
  ELENA (low): "You burned her saddle. That means you're afraid of what was in it."

ESCENA 21 (Viñeta #21 del Storyboard) — 03:20–03:30
- Location: gatehouse cottage, night
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the cottage lamplight, the maid unrolls the old county survey map while the foreman anchors the curling corners with heavy iron horseshoes.
  * [03s–07s]: insert shot of the evidence object — Insert: a calloused finger traces the parcel boundary where the original boundary line was scraped off with a razor blade.
  * [07s–10s]: tight close-up — Close on the maid looking up from the map, determination sharpening her eyes.
- Sound Design (SFX & Voice Tone): kerosene lamp humming, wind whistling through window joints, heavy paper creaking. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; COLE — quiet, low American English, careful diction, warmth held under restraint
- Dialogue (English, 6–8 sec max):
  ELENA (intense, low): "Look at the parcel boundary. Someone scraped the original section line off with a blade."
  COLE (gravelly): "That's Walter Blackwell's handwriting underneath. He signed over the whole north valley."

ESCENA 22 (Viñeta #22 del Storyboard) — 03:30–03:40
- Location: Blackwell tack room, night
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the shadowy tack room, the maid kneels beside the wall timber and slides a cylindrical tin case from the hollow cavity.
  * [03s–07s]: insert shot of the evidence object — Insert: the cap unscrews with a grinding squeak, revealing rolled bank tax receipts tied with red butcher twine.
  * [07s–10s]: tight close-up — Close on her face as flashlight beam illuminates the receipts bearing her mother's signature.
- Sound Design (SFX & Voice Tone): tin cap grinding, owls hooting in barn rafters, distant horse snorting softly. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (shivering whisper): "Every property tax installment from 2005 to 2008. My mother paid them in cash at First Valley Bank."

ESCENA 23 (Viñeta #23 del Storyboard) — 03:40–03:50
- Location: Silver Creek barn hayloft, night
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the moonlight, the foreman gently binds the maid's bruised palm with white tape, his touch slow and deliberate.
  * [03s–07s]: tight close-up — Close on their intertwined hands as his thumb brushes over her calloused knuckles.
  * [07s–10s]: over-the-shoulder shot — Over the foreman's broad shoulder, her eyes soften as she looks directly into his face.
- Sound Design (SFX & Voice Tone): dry hay rustling, cricket chirps, soft breathing, timber creaking in night breeze. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (soft, rough): "You don't have to carry this alone in the dark, Elena. I'm with you."
  ELENA (tender, guarded): "Everyone who stood beside my mother paid for it. Be careful."

ESCENA 24 (Viñeta #24 del Storyboard) — 03:50–04:00
- Location: Blackwell study archives, night
- Characters Present: Elena Vance, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Behind the desk, the maid freezes with the open ledger as the heir steps over the threshold into the room.
  * [03s–07s]: tight close-up — Close on the heir's eyes shifting down to the gold-stamped estate accounts ledger in her arms.
  * [07s–10s]: over-the-shoulder shot — Over the maid's shoulder, the heir slowly reaches behind his back to shut the study door.
- Sound Design (SFX & Voice Tone): heavy oak door latching softly, clock pendulum ticking, distant dogs barking. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  RICHARD (nervous, tense): "You shouldn't have opened that drawer, Elena. That book lists payments my father made to keep quiet."
  ELENA (cold, piercing): "Payments to the county coroner. Your mother bought the death certificate."

COMANDO FINAL (16:9 YouTube):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 19 (Viñeta #19 del Storyboard) — 03:00–03:10
- Location: Blackwell great room, dinner, night
- Characters Present: Victoria Blackwell, Elena Vance, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the candlelit great room, the mistress rises with a glass while the maid stands at the edge of the tables, napkin in hand.
  * [03s–07s]: tight close-up — Close on the maid's face as every guest turns toward her.
  * [07s–10s]: low-angle hero shot — Low angle on the maid as she answers the toast without dropping her gaze.
- Sound Design (SFX & Voice Tone): silverware on china, a glass set down, a room going quiet. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (bright, public): "Elena will be leaving us soon. Tell them, dear — what are your plans?"
  ELENA (calm, clear): "Mrs. Blackwell is too kind. My plans haven't changed. I'm staying."

ESCENA 20 (Viñeta #20 del Storyboard) — 03:10–03:20
- Location: Blackwell gravel yard, night
- Characters Present: Victoria Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the gravel yard at night, a steel barrel burns while the mistress holds out a folded paper and the maid watches the flames.
  * [03s–07s]: insert shot of the evidence object — Insert: the old saddle's leather curling in the fire, stitching glowing before it blackens.
  * [07s–10s]: tight close-up — Close on the maid's face lit by fire; she does not step back.
- Sound Design (SFX & Voice Tone): fire roaring in a steel barrel, gravel under boots, a radio crackling in the sheriff's car. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (quiet, absolute): "Sign by midnight, or I press charges for arson as well as theft."
  ELENA (low): "You burned her saddle. That means you're afraid of what was in it."

ESCENA 21 (Viñeta #21 del Storyboard) — 03:20–03:30
- Location: gatehouse cottage, night
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the cottage lamplight, the maid unrolls the old county survey map while the foreman anchors the curling corners with heavy iron horseshoes.
  * [03s–07s]: insert shot of the evidence object — Insert: a calloused finger traces the parcel boundary where the original boundary line was scraped off with a razor blade.
  * [07s–10s]: tight close-up — Close on the maid looking up from the map, determination sharpening her eyes.
- Sound Design (SFX & Voice Tone): kerosene lamp humming, wind whistling through window joints, heavy paper creaking. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; COLE — quiet, low American English, careful diction, warmth held under restraint
- Dialogue (English, 6–8 sec max):
  ELENA (intense, low): "Look at the parcel boundary. Someone scraped the original section line off with a blade."
  COLE (gravelly): "That's Walter Blackwell's handwriting underneath. He signed over the whole north valley."

ESCENA 22 (Viñeta #22 del Storyboard) — 03:30–03:40
- Location: Blackwell tack room, night
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the shadowy tack room, the maid kneels beside the wall timber and slides a cylindrical tin case from the hollow cavity.
  * [03s–07s]: insert shot of the evidence object — Insert: the cap unscrews with a grinding squeak, revealing rolled bank tax receipts tied with red butcher twine.
  * [07s–10s]: tight close-up — Close on her face as flashlight beam illuminates the receipts bearing her mother's signature.
- Sound Design (SFX & Voice Tone): tin cap grinding, owls hooting in barn rafters, distant horse snorting softly. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (shivering whisper): "Every property tax installment from 2005 to 2008. My mother paid them in cash at First Valley Bank."

ESCENA 23 (Viñeta #23 del Storyboard) — 03:40–03:50
- Location: Silver Creek barn hayloft, night
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the moonlight, the foreman gently binds the maid's bruised palm with white tape, his touch slow and deliberate.
  * [03s–07s]: tight close-up — Close on their intertwined hands as his thumb brushes over her calloused knuckles.
  * [07s–10s]: over-the-shoulder shot — Over the foreman's broad shoulder, her eyes soften as she looks directly into his face.
- Sound Design (SFX & Voice Tone): dry hay rustling, cricket chirps, soft breathing, timber creaking in night breeze. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (soft, rough): "You don't have to carry this alone in the dark, Elena. I'm with you."
  ELENA (tender, guarded): "Everyone who stood beside my mother paid for it. Be careful."

ESCENA 24 (Viñeta #24 del Storyboard) — 03:50–04:00
- Location: Blackwell study archives, night
- Characters Present: Elena Vance, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Behind the desk, the maid freezes with the open ledger as the heir steps over the threshold into the room.
  * [03s–07s]: tight close-up — Close on the heir's eyes shifting down to the gold-stamped estate accounts ledger in her arms.
  * [07s–10s]: over-the-shoulder shot — Over the maid's shoulder, the heir slowly reaches behind his back to shut the study door.
- Sound Design (SFX & Voice Tone): heavy oak door latching softly, clock pendulum ticking, distant dogs barking. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  RICHARD (nervous, tense): "You shouldn't have opened that drawer, Elena. That book lists payments my father made to keep quiet."
  ELENA (cold, piercing): "Payments to the county coroner. Your mother bought the death certificate."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 para Reels, TikTok y Shorts."
```

### Lote 05 — Minuto 5 (escenas 25–30)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_05.png`

**Guardar 16:9 como:** `raw_clips/minute_05.mp4`

**Guardar 9:16 como:** `raw_clips/minute_05_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 25 (Viñeta #25 del Storyboard) — 04:00–04:10
- Location: Blackwell mansion great room, night
- Characters Present: Victoria Blackwell, Elena Vance, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the vast room, the mistress dangles a small brass ribboned key while the maid stands rigid near the cold hearth.
  * [03s–07s]: tight close-up — Close on the mistress's painted red lips curling into an amused, predatory smile.
  * [07s–10s]: low-angle hero shot — Low angle on the maid squaring her shoulders against the firelight's orange glow.
- Sound Design (SFX & Voice Tone): grandfather clock striking the quarter hour, embers crackling, wind buffeting glass. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (smooth venom): "Did you think Walter was a saint? He gave promises because he was weak."
  ELENA (unflinching): "He gave her the ranch. And you murdered him before he could file it."

ESCENA 26 (Viñeta #26 del Storyboard) — 04:10–04:20
- Location: Blackwell mansion gravel drive, night
- Characters Present: Cole Barrett, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Under harsh halogen yard lights, the foreman plants his boots in front of the heir, refusing to yield the driveway.
  * [03s–07s]: tight close-up — Close on the foreman's clenched fist at his side, knuckles white against the tan canvas.
  * [07s–10s]: over-the-shoulder shot — Over the heir's shoulder, the foreman steps forward into the beam of light.
- Sound Design (SFX & Voice Tone): gravel shifting under heavy work boots, halogen floodlights buzzing, cold fog horn far off. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  COLE (deadly, calm): "Take one step toward the gatehouse tonight, Richard, and I'll finish what your father started."
  RICHARD (bitter, spiteful): "You're throwing your whole life away for a girl who won't even kiss you."

ESCENA 27 (Viñeta #27 del Storyboard) — 04:20–04:30
- Location: gatehouse cottage porch, night
- Characters Present: Elena Vance, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — On the rain-slick porch steps, the heir reaches out with a cream envelope while the maid refuses to accept it.
  * [03s–07s]: insert shot of the evidence object — Insert: the wet envelope bears the embossed gold seal of the county probate registry.
  * [07s–10s]: tight close-up — Close on the heir's eyes searching her face, genuine dread beneath his charm.
- Sound Design (SFX & Voice Tone): rain dripping from wooden eaves, porch boards creaking, distant thunder rumble. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  RICHARD (shaken, urgent): "My mother hired two men from Billings. If you are here at sunrise, they won't talk."
  ELENA (quiet iron): "Then tell them to bring their shovels. I'm not running."

ESCENA 28 (Viñeta #28 del Storyboard) — 04:30–04:40
- Location: Silver Creek barn aisle, night
- Characters Present: Elena Vance, Maggie Doyle
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the barn aisle, the housekeeper rushes to the maid and grabs both of her elbows with trembling hands.
  * [03s–07s]: tight close-up — Close on the housekeeper's tear-streaked spectacles reflecting the amber glow of the hanging bulb.
  * [07s–10s]: over-the-shoulder shot — Over the housekeeper's shoulder, the maid gently pulls her close to steady her shaking.
- Sound Design (SFX & Voice Tone): horses rustling nervous in stalls, wind howling through wall cracks, floor chains clinking. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  MAGGIE (frantic whisper): "Victoria cleared the safe in the master bedroom. She's packing to leave after the county gala."
  ELENA (grim, steady): "She won't leave Montana until the auction deed is stamped. We have until midnight."

ESCENA 29 (Viñeta #29 del Storyboard) — 04:40–04:50
- Location: Blackwell estate gates, midnight
- Characters Present: Victoria Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — By the iron gates, the mistress steps out of the luxury car into the headlights, holding a checkbook open.
  * [03s–07s]: tight close-up — Close on the cashier's draft: five hundred thousand dollars drawn on First Valley Bank.
  * [07s–10s]: low-angle hero shot — Low angle on the maid standing in the glare of the car beams, unblinking in the gale.
- Sound Design (SFX & Voice Tone): car engine idling low, wind screaming through iron bars, headlights humming. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (velvet bribe): "Half a million dollars in cash. You can buy any ranch from here to Texas, Elena."
  ELENA (ice cold): "And all I have to do is swear my mother was a thief."

ESCENA 30 (Viñeta #30 del Storyboard) — 04:50–05:00
- Location: Blackwell estate gates, midnight
- Characters Present: Victoria Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Under the headlights, the mistress thrusts the certified check into the maid's face like an execution order.
  * [03s–07s]: insert shot of the evidence object — Insert: the maid's fingers close around the paper edge, lingering as if about to fold it.
  * [07s–10s]: tight close-up — Extreme close-up on the maid's eyes, blazing with an impossible choice as rain strikes her skin.
- Sound Design (SFX & Voice Tone): thunderclaps shaking the valley, heavy rain drumming car hood, paper ripping slightly in wind. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (whispered, ruthless): "Take the money, Elena. Leave the name behind. Or by morning, you won't have either."
  ELENA (defiant roar): "My mother died for this name. You can't afford it."

COMANDO FINAL (16:9 YouTube):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 25 (Viñeta #25 del Storyboard) — 04:00–04:10
- Location: Blackwell mansion great room, night
- Characters Present: Victoria Blackwell, Elena Vance, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the vast room, the mistress dangles a small brass ribboned key while the maid stands rigid near the cold hearth.
  * [03s–07s]: tight close-up — Close on the mistress's painted red lips curling into an amused, predatory smile.
  * [07s–10s]: low-angle hero shot — Low angle on the maid squaring her shoulders against the firelight's orange glow.
- Sound Design (SFX & Voice Tone): grandfather clock striking the quarter hour, embers crackling, wind buffeting glass. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (smooth venom): "Did you think Walter was a saint? He gave promises because he was weak."
  ELENA (unflinching): "He gave her the ranch. And you murdered him before he could file it."

ESCENA 26 (Viñeta #26 del Storyboard) — 04:10–04:20
- Location: Blackwell mansion gravel drive, night
- Characters Present: Cole Barrett, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Under harsh halogen yard lights, the foreman plants his boots in front of the heir, refusing to yield the driveway.
  * [03s–07s]: tight close-up — Close on the foreman's clenched fist at his side, knuckles white against the tan canvas.
  * [07s–10s]: over-the-shoulder shot — Over the heir's shoulder, the foreman steps forward into the beam of light.
- Sound Design (SFX & Voice Tone): gravel shifting under heavy work boots, halogen floodlights buzzing, cold fog horn far off. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  COLE (deadly, calm): "Take one step toward the gatehouse tonight, Richard, and I'll finish what your father started."
  RICHARD (bitter, spiteful): "You're throwing your whole life away for a girl who won't even kiss you."

ESCENA 27 (Viñeta #27 del Storyboard) — 04:20–04:30
- Location: gatehouse cottage porch, night
- Characters Present: Elena Vance, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — On the rain-slick porch steps, the heir reaches out with a cream envelope while the maid refuses to accept it.
  * [03s–07s]: insert shot of the evidence object — Insert: the wet envelope bears the embossed gold seal of the county probate registry.
  * [07s–10s]: tight close-up — Close on the heir's eyes searching her face, genuine dread beneath his charm.
- Sound Design (SFX & Voice Tone): rain dripping from wooden eaves, porch boards creaking, distant thunder rumble. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  RICHARD (shaken, urgent): "My mother hired two men from Billings. If you are here at sunrise, they won't talk."
  ELENA (quiet iron): "Then tell them to bring their shovels. I'm not running."

ESCENA 28 (Viñeta #28 del Storyboard) — 04:30–04:40
- Location: Silver Creek barn aisle, night
- Characters Present: Elena Vance, Maggie Doyle
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the barn aisle, the housekeeper rushes to the maid and grabs both of her elbows with trembling hands.
  * [03s–07s]: tight close-up — Close on the housekeeper's tear-streaked spectacles reflecting the amber glow of the hanging bulb.
  * [07s–10s]: over-the-shoulder shot — Over the housekeeper's shoulder, the maid gently pulls her close to steady her shaking.
- Sound Design (SFX & Voice Tone): horses rustling nervous in stalls, wind howling through wall cracks, floor chains clinking. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  MAGGIE (frantic whisper): "Victoria cleared the safe in the master bedroom. She's packing to leave after the county gala."
  ELENA (grim, steady): "She won't leave Montana until the auction deed is stamped. We have until midnight."

ESCENA 29 (Viñeta #29 del Storyboard) — 04:40–04:50
- Location: Blackwell estate gates, midnight
- Characters Present: Victoria Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — By the iron gates, the mistress steps out of the luxury car into the headlights, holding a checkbook open.
  * [03s–07s]: tight close-up — Close on the cashier's draft: five hundred thousand dollars drawn on First Valley Bank.
  * [07s–10s]: low-angle hero shot — Low angle on the maid standing in the glare of the car beams, unblinking in the gale.
- Sound Design (SFX & Voice Tone): car engine idling low, wind screaming through iron bars, headlights humming. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (velvet bribe): "Half a million dollars in cash. You can buy any ranch from here to Texas, Elena."
  ELENA (ice cold): "And all I have to do is swear my mother was a thief."

ESCENA 30 (Viñeta #30 del Storyboard) — 04:50–05:00
- Location: Blackwell estate gates, midnight
- Characters Present: Victoria Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Under the headlights, the mistress thrusts the certified check into the maid's face like an execution order.
  * [03s–07s]: insert shot of the evidence object — Insert: the maid's fingers close around the paper edge, lingering as if about to fold it.
  * [07s–10s]: tight close-up — Extreme close-up on the maid's eyes, blazing with an impossible choice as rain strikes her skin.
- Sound Design (SFX & Voice Tone): thunderclaps shaking the valley, heavy rain drumming car hood, paper ripping slightly in wind. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (whispered, ruthless): "Take the money, Elena. Leave the name behind. Or by morning, you won't have either."
  ELENA (defiant roar): "My mother died for this name. You can't afford it."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 para Reels, TikTok y Shorts."
```

### Lote 06 — Minuto 6 (escenas 31–36)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_06.png`

**Guardar 16:9 como:** `raw_clips/minute_06.mp4`

**Guardar 9:16 como:** `raw_clips/minute_06_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 31 (Viñeta #31 del Storyboard) — 05:00–05:10
- Location: gatehouse cottage, storm night
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — Inside the ransacked cottage, the storm sweeps through shattered windows, scattering torn clothes and broken crockery across wet stones.
  * [03s–07s]: tight close-up — Close on the maid's boots stepping through broken glass as rain drips from her soaked chin.
  * [07s–10s]: medium shot — She kneels in the center of the wreckage, her hands feeling frantically beneath a loose hearthstone.
- Sound Design (SFX & Voice Tone): gale force winds howl through glass shards, torrents of rain hitting stone floor, thunder. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (choked, breathless): "They took the tin box. They tore through my floorboards and took the original deed."
  ELENA (shattered whisper): "They took everything."

ESCENA 32 (Viñeta #32 del Storyboard) — 05:10–05:20
- Location: gatehouse cottage yard, storm night
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the swirling red and blue emergency light, the maid faces the padlocked gate as rain washes mud over her boots.
  * [03s–07s]: insert shot of the evidence object — Insert: a laminated county eviction warrant stapled to the post: 'Immediate Vacate — Trespassing Order'.
  * [07s–10s]: tight close-up — Close on her wet face illuminated by strobe flashes, defiant rage replacing fear.
- Sound Design (SFX & Voice Tone): police cruiser siren chirping, heavy rain squall, chain links rattling against timber post. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (bitter, low): "Sheriff Drummond signed an eviction without a hearing. Victoria bought the whole county, but she never bought me."

ESCENA 33 (Viñeta #33 del Storyboard) — 05:20–05:30
- Location: Silver Creek hay shed, storm night
- Characters Present: Elena Vance, Maggie Doyle
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the drafty shelter, the maid wraps her own dry flannel scarf around the weeping housekeeper's neck.
  * [03s–07s]: tight close-up — Close on the housekeeper's trembling chin as she clasps Elena's wet wrists with both hands.
  * [07s–10s]: over-the-shoulder shot — Over the maid's shoulder, the older woman looks up with fifteen years of buried grief.
- Sound Design (SFX & Voice Tone): rain thundering deafeningly on corrugated iron roof, gusting wind, weeping breath. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  MAGGIE (sobbing, broken): "Victoria threatened my sister's nursing care in Helena. That is why I signed the lie."
  ELENA (fierce, gentle): "You kept your family alive, Maggie. I forgive you. Now help me finish this."

ESCENA 34 (Viñeta #34 del Storyboard) — 05:30–05:40
- Location: Blackwell mansion rear terrace, storm night
- Characters Present: Victoria Blackwell, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Inside the glowing library, the mistress feeds the ancient deed into the fireplace flames while rain streaks the window.
  * [03s–07s]: insert shot of the evidence object — Insert: the wax seal on June Vance's deed melts into blackened bubbles in the fire.
  * [07s–10s]: tight close-up — Close on the heir turning away from the fireplace, draining his amber glass in one swallow.
- Sound Design (SFX & Voice Tone): fireplace flames roaring, rain drumming on terrace panes, crystal glass setting down. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  VICTORIA (triumphant, quiet): "There goes Walter's grand sentiment. No deed, no contract, no legal claim in Montana."
  RICHARD (dark, uneasy): "You burned the paper, Mother. You didn't burn what Walter put in the vault."

ESCENA 35 (Viñeta #35 del Storyboard) — 05:40–05:50
- Location: Silver Creek stable tack room, storm night
- Characters Present: Elena Vance, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In a sudden flash of lightning, the maid appears like a ghost in the stable door, blocking the heir's retreat.
  * [03s–07s]: tight close-up — Close on the heir stumbling backward against a stall door, dropping his car keys onto the straw.
  * [07s–10s]: over-the-shoulder shot — Over the maid's shoulder, she steps forward and steps firmly onto his dropped keys.
- Sound Design (SFX & Voice Tone): thunderclap echoing in barn rafters, straw crunching underfoot, keys jangling on wood. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  ELENA (ice cold command): "Tell me what your father put in the vault, Richard. Or sleep in this stable tonight."
  RICHARD (stammering, cornered): "Box 14 at First Valley Trust. The original will. He never revoked it."

ESCENA 36 (Viñeta #36 del Storyboard) — 05:50–06:00
- Location: ranch ridge overlook, storm dawn
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — On the high ridge, the small figure of the maid stands against the vast Montana valley as dawn breaks slate grey.
  * [03s–07s]: tight close-up — Close on her wet face, eyes stinging with salt and cold wind, but chin jutting forward in stubborn pride.
  * [07s–10s]: low-angle hero shot — Low angle from the rocks below, framing her towering against the gathering dawn light.
- Sound Design (SFX & Voice Tone): gale wind howling over mountain crest, distant hawk cry, thunder rolling away into hills. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (unbroken, resonant): "They took the house. They burned the deed. But every inch of this dirt remembers my mother's sweat."

COMANDO FINAL (16:9 YouTube):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 31 (Viñeta #31 del Storyboard) — 05:00–05:10
- Location: gatehouse cottage, storm night
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — Inside the ransacked cottage, the storm sweeps through shattered windows, scattering torn clothes and broken crockery across wet stones.
  * [03s–07s]: tight close-up — Close on the maid's boots stepping through broken glass as rain drips from her soaked chin.
  * [07s–10s]: medium shot — She kneels in the center of the wreckage, her hands feeling frantically beneath a loose hearthstone.
- Sound Design (SFX & Voice Tone): gale force winds howl through glass shards, torrents of rain hitting stone floor, thunder. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (choked, breathless): "They took the tin box. They tore through my floorboards and took the original deed."
  ELENA (shattered whisper): "They took everything."

ESCENA 32 (Viñeta #32 del Storyboard) — 05:10–05:20
- Location: gatehouse cottage yard, storm night
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the swirling red and blue emergency light, the maid faces the padlocked gate as rain washes mud over her boots.
  * [03s–07s]: insert shot of the evidence object — Insert: a laminated county eviction warrant stapled to the post: 'Immediate Vacate — Trespassing Order'.
  * [07s–10s]: tight close-up — Close on her wet face illuminated by strobe flashes, defiant rage replacing fear.
- Sound Design (SFX & Voice Tone): police cruiser siren chirping, heavy rain squall, chain links rattling against timber post. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (bitter, low): "Sheriff Drummond signed an eviction without a hearing. Victoria bought the whole county, but she never bought me."

ESCENA 33 (Viñeta #33 del Storyboard) — 05:20–05:30
- Location: Silver Creek hay shed, storm night
- Characters Present: Elena Vance, Maggie Doyle
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the drafty shelter, the maid wraps her own dry flannel scarf around the weeping housekeeper's neck.
  * [03s–07s]: tight close-up — Close on the housekeeper's trembling chin as she clasps Elena's wet wrists with both hands.
  * [07s–10s]: over-the-shoulder shot — Over the maid's shoulder, the older woman looks up with fifteen years of buried grief.
- Sound Design (SFX & Voice Tone): rain thundering deafeningly on corrugated iron roof, gusting wind, weeping breath. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  MAGGIE (sobbing, broken): "Victoria threatened my sister's nursing care in Helena. That is why I signed the lie."
  ELENA (fierce, gentle): "You kept your family alive, Maggie. I forgive you. Now help me finish this."

ESCENA 34 (Viñeta #34 del Storyboard) — 05:30–05:40
- Location: Blackwell mansion rear terrace, storm night
- Characters Present: Victoria Blackwell, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Inside the glowing library, the mistress feeds the ancient deed into the fireplace flames while rain streaks the window.
  * [03s–07s]: insert shot of the evidence object — Insert: the wax seal on June Vance's deed melts into blackened bubbles in the fire.
  * [07s–10s]: tight close-up — Close on the heir turning away from the fireplace, draining his amber glass in one swallow.
- Sound Design (SFX & Voice Tone): fireplace flames roaring, rain drumming on terrace panes, crystal glass setting down. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  VICTORIA (triumphant, quiet): "There goes Walter's grand sentiment. No deed, no contract, no legal claim in Montana."
  RICHARD (dark, uneasy): "You burned the paper, Mother. You didn't burn what Walter put in the vault."

ESCENA 35 (Viñeta #35 del Storyboard) — 05:40–05:50
- Location: Silver Creek stable tack room, storm night
- Characters Present: Elena Vance, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In a sudden flash of lightning, the maid appears like a ghost in the stable door, blocking the heir's retreat.
  * [03s–07s]: tight close-up — Close on the heir stumbling backward against a stall door, dropping his car keys onto the straw.
  * [07s–10s]: over-the-shoulder shot — Over the maid's shoulder, she steps forward and steps firmly onto his dropped keys.
- Sound Design (SFX & Voice Tone): thunderclap echoing in barn rafters, straw crunching underfoot, keys jangling on wood. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  ELENA (ice cold command): "Tell me what your father put in the vault, Richard. Or sleep in this stable tonight."
  RICHARD (stammering, cornered): "Box 14 at First Valley Trust. The original will. He never revoked it."

ESCENA 36 (Viñeta #36 del Storyboard) — 05:50–06:00
- Location: ranch ridge overlook, storm dawn
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — On the high ridge, the small figure of the maid stands against the vast Montana valley as dawn breaks slate grey.
  * [03s–07s]: tight close-up — Close on her wet face, eyes stinging with salt and cold wind, but chin jutting forward in stubborn pride.
  * [07s–10s]: low-angle hero shot — Low angle from the rocks below, framing her towering against the gathering dawn light.
- Sound Design (SFX & Voice Tone): gale wind howling over mountain crest, distant hawk cry, thunder rolling away into hills. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (unbroken, resonant): "They took the house. They burned the deed. But every inch of this dirt remembers my mother's sweat."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 para Reels, TikTok y Shorts."
```

### Lote 07 — Minuto 7 (escenas 37–42)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_07.png`

**Guardar 16:9 como:** `raw_clips/minute_07.mp4`

**Guardar 9:16 como:** `raw_clips/minute_07_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 37 (Viñeta #37 del Storyboard) — 06:00–06:10
- Location: ranch ridge road, dawn
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — On the muddy road, the foreman wraps his dry wool jacket around her, pulling the collar up against the wind.
  * [03s–07s]: tight close-up — Close on his calloused hand lingering at the lapel, steadying her trembling frame.
  * [07s–10s]: over-the-shoulder shot — Over the maid's shoulder, the foreman looks straight down the mountain toward town.
- Sound Design (SFX & Voice Tone): diesel truck engine rumbling steady, windshield wipers clicking, wind whistling through pines. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (quiet, loyal): "The bank opens in two hours. I've got gas and nothing left to lose."
  ELENA (soft warning): "If we do this, Victoria will have the sheriff arrest us at the door."

ESCENA 38 (Viñeta #38 del Storyboard) — 06:10–06:20
- Location: green truck cab, dawn
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Inside the bouncing truck cab, the maid turns the brass key in the dashboard light, scraping away years of verdigris.
  * [03s–07s]: insert shot of the evidence object — Insert: under the brass patina, tiny stamped numerals read: 'FVT — 14'.
  * [07s–10s]: tight close-up — Close on her lips parting as the final realization clicks into place.
- Sound Design (SFX & Voice Tone): truck tires humming on wet highway, heater blower whirring, key clicking against metal coin tray. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; COLE — quiet, low American English, careful diction, warmth held under restraint
- Dialogue (English, 6–8 sec max):
  ELENA (hushed awe): "FVT fourteen. First Valley Trust. This was never a saddle lock or a barn key."
  COLE (stunned breath): "It's a bank safety deposit box key. Walter's private vault."

ESCENA 39 (Viñeta #39 del Storyboard) — 06:20–06:30
- Location: town bank exterior, morning
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — On the bank steps, the maid and foreman turn together as the limousine door opens across the street.
  * [03s–07s]: over-the-shoulder shot — Over the maid's shoulder, Victoria steps out in her emerald gala dress, accompanied by Sheriff Drummond.
  * [07s–10s]: tight close-up — Close on the maid slipping the brass key into her fist and bounding up the bank steps.
- Sound Design (SFX & Voice Tone): town church bell tolling nine, limousine door slamming, boots racing up granite stairs. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (urgent): "Victoria's here with Drummond. They're going to seal the vault before you reach the counter."
  ELENA (determined): "Then hold Drummond on the steps for sixty seconds. Just sixty seconds."

ESCENA 40 (Viñeta #40 del Storyboard) — 06:30–06:40
- Location: First Valley Trust vault corridor, morning
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Inside the gleaming vault, the maid turns the brass key into Lock 14; the heavy tumbler clicks open with a hollow ring.
  * [03s–07s]: insert shot of the evidence object — Insert: the long metal deposit box slides out, containing a blue ribboned document: 'Last Will and Testament of Walter Blackwell'.
  * [07s–10s]: tight close-up — Close on her eyes widening in profound shock as she reads the bold heading across the parchment.
- Sound Design (SFX & Voice Tone): heavy steel tumbler clunking open, metal drawer sliding on runners, fluorescent bulb hum. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (reverent whisper): "The key was never for a door. It was for Walter Blackwell's final will."
  ELENA (rising triumph): "And the first page leaves Silver Creek entirely to me."

ESCENA 41 (Viñeta #41 del Storyboard) — 06:40–06:50
- Location: First Valley Trust manager office, morning
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the sunlit bank office, the maid stands tall as the grey-haired bank manager examines the embossed blue notary seal through his bifocals.
  * [03s–07s]: insert shot of the evidence object — Insert: the manager's heavy gold signet embosser stamps 'CERTIFIED ORIGINAL COPY — FIRST VALLEY TRUST' across the parchment.
  * [07s–10s]: tight close-up — Close on the maid's face as the heavy brass stamp thuds down, her breath releasing in steady relief.
- Sound Design (SFX & Voice Tone): heavy brass seal clunking on paper, ticking grandfather clock, muffled street traffic outside. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (crisp, steady): "Is the notary seal intact, sir? Does this will hold legal standing in Montana?"
  CLERK (formal, solemn): "It is completely valid, Miss Vance. Walter Blackwell deposited this with his own hand."

ESCENA 42 (Viñeta #42 del Storyboard) — 06:50–07:00
- Location: town bank steps, morning
- Characters Present: Cole Barrett, Victoria Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — On the stone steps, the foreman stands immovable between the mistress and the bank doors, ignoring the sheriff's warning stance.
  * [03s–07s]: tight close-up — Close on the mistress's furious eyes narrowing beneath her sleek platinum bob.
  * [07s–10s]: over-the-shoulder shot — Over the foreman's shoulder, the bank double doors click open behind him.
- Sound Design (SFX & Voice Tone): heavy brass door latch clicking open, morning wind rustling dry leaves on stone, town murmurs. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; COLE — quiet, low American English, careful diction, warmth held under restraint
- Dialogue (English, 6–8 sec max):
  VICTORIA (venomous hiss): "Step aside, Cole. You are an employee on my payroll until I fire you."
  COLE (unshakable, low): "I don't work for you anymore, Victoria. I work for Silver Creek's real owner."

COMANDO FINAL (16:9 YouTube):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 37 (Viñeta #37 del Storyboard) — 06:00–06:10
- Location: ranch ridge road, dawn
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — On the muddy road, the foreman wraps his dry wool jacket around her, pulling the collar up against the wind.
  * [03s–07s]: tight close-up — Close on his calloused hand lingering at the lapel, steadying her trembling frame.
  * [07s–10s]: over-the-shoulder shot — Over the maid's shoulder, the foreman looks straight down the mountain toward town.
- Sound Design (SFX & Voice Tone): diesel truck engine rumbling steady, windshield wipers clicking, wind whistling through pines. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (quiet, loyal): "The bank opens in two hours. I've got gas and nothing left to lose."
  ELENA (soft warning): "If we do this, Victoria will have the sheriff arrest us at the door."

ESCENA 38 (Viñeta #38 del Storyboard) — 06:10–06:20
- Location: green truck cab, dawn
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Inside the bouncing truck cab, the maid turns the brass key in the dashboard light, scraping away years of verdigris.
  * [03s–07s]: insert shot of the evidence object — Insert: under the brass patina, tiny stamped numerals read: 'FVT — 14'.
  * [07s–10s]: tight close-up — Close on her lips parting as the final realization clicks into place.
- Sound Design (SFX & Voice Tone): truck tires humming on wet highway, heater blower whirring, key clicking against metal coin tray. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; COLE — quiet, low American English, careful diction, warmth held under restraint
- Dialogue (English, 6–8 sec max):
  ELENA (hushed awe): "FVT fourteen. First Valley Trust. This was never a saddle lock or a barn key."
  COLE (stunned breath): "It's a bank safety deposit box key. Walter's private vault."

ESCENA 39 (Viñeta #39 del Storyboard) — 06:20–06:30
- Location: town bank exterior, morning
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — On the bank steps, the maid and foreman turn together as the limousine door opens across the street.
  * [03s–07s]: over-the-shoulder shot — Over the maid's shoulder, Victoria steps out in her emerald gala dress, accompanied by Sheriff Drummond.
  * [07s–10s]: tight close-up — Close on the maid slipping the brass key into her fist and bounding up the bank steps.
- Sound Design (SFX & Voice Tone): town church bell tolling nine, limousine door slamming, boots racing up granite stairs. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (urgent): "Victoria's here with Drummond. They're going to seal the vault before you reach the counter."
  ELENA (determined): "Then hold Drummond on the steps for sixty seconds. Just sixty seconds."

ESCENA 40 (Viñeta #40 del Storyboard) — 06:30–06:40
- Location: First Valley Trust vault corridor, morning
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Inside the gleaming vault, the maid turns the brass key into Lock 14; the heavy tumbler clicks open with a hollow ring.
  * [03s–07s]: insert shot of the evidence object — Insert: the long metal deposit box slides out, containing a blue ribboned document: 'Last Will and Testament of Walter Blackwell'.
  * [07s–10s]: tight close-up — Close on her eyes widening in profound shock as she reads the bold heading across the parchment.
- Sound Design (SFX & Voice Tone): heavy steel tumbler clunking open, metal drawer sliding on runners, fluorescent bulb hum. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (reverent whisper): "The key was never for a door. It was for Walter Blackwell's final will."
  ELENA (rising triumph): "And the first page leaves Silver Creek entirely to me."

ESCENA 41 (Viñeta #41 del Storyboard) — 06:40–06:50
- Location: First Valley Trust manager office, morning
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the sunlit bank office, the maid stands tall as the grey-haired bank manager examines the embossed blue notary seal through his bifocals.
  * [03s–07s]: insert shot of the evidence object — Insert: the manager's heavy gold signet embosser stamps 'CERTIFIED ORIGINAL COPY — FIRST VALLEY TRUST' across the parchment.
  * [07s–10s]: tight close-up — Close on the maid's face as the heavy brass stamp thuds down, her breath releasing in steady relief.
- Sound Design (SFX & Voice Tone): heavy brass seal clunking on paper, ticking grandfather clock, muffled street traffic outside. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (crisp, steady): "Is the notary seal intact, sir? Does this will hold legal standing in Montana?"
  CLERK (formal, solemn): "It is completely valid, Miss Vance. Walter Blackwell deposited this with his own hand."

ESCENA 42 (Viñeta #42 del Storyboard) — 06:50–07:00
- Location: town bank steps, morning
- Characters Present: Cole Barrett, Victoria Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — On the stone steps, the foreman stands immovable between the mistress and the bank doors, ignoring the sheriff's warning stance.
  * [03s–07s]: tight close-up — Close on the mistress's furious eyes narrowing beneath her sleek platinum bob.
  * [07s–10s]: over-the-shoulder shot — Over the foreman's shoulder, the bank double doors click open behind him.
- Sound Design (SFX & Voice Tone): heavy brass door latch clicking open, morning wind rustling dry leaves on stone, town murmurs. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; COLE — quiet, low American English, careful diction, warmth held under restraint
- Dialogue (English, 6–8 sec max):
  VICTORIA (venomous hiss): "Step aside, Cole. You are an employee on my payroll until I fire you."
  COLE (unshakable, low): "I don't work for you anymore, Victoria. I work for Silver Creek's real owner."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 para Reels, TikTok y Shorts."
```

### Lote 08 — Minuto 8 (escenas 43–48)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_08.png`

**Guardar 16:9 como:** `raw_clips/minute_08.mp4`

**Guardar 9:16 como:** `raw_clips/minute_08_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 43 (Viñeta #43 del Storyboard) — 07:00–07:10
- Location: town bank steps, morning
- Characters Present: Elena Vance, Victoria Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — The maid emerges onto the sunlit steps, lifting the stamped court-certified envelope for the entire sidewalk to see.
  * [03s–07s]: tight close-up — Close on the mistress's painted smile slipping, raw panic flashing behind her eyes for the first time.
  * [07s–10s]: low-angle hero shot — Low angle on the maid looking down from the granite steps with quiet authority.
- Sound Design (SFX & Voice Tone): onlookers murmuring on sidewalk, pigeon wings flapping, wind snapping county banners. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts
- Dialogue (English, 6–8 sec max):
  ELENA (ringing, clear): "You told the county my mother had no standing. Walter's certified will begs to differ."
  VICTORIA (strained composure): "That paper is an obsolete draft. It means nothing without court ratification."

ESCENA 44 (Viñeta #44 del Storyboard) — 07:10–07:20
- Location: Blackwell town car, morning
- Characters Present: Victoria Blackwell, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Inside the town car, the mistress grabs her son's lapel as he pulls himself back against the passenger door.
  * [03s–07s]: tight close-up — Close on the heir unfastening her gloved fingers from his jacket with quiet distaste.
  * [07s–10s]: over-the-shoulder shot — Over the mistress's shoulder, the heir stares out at the courthouse steps.
- Sound Design (SFX & Voice Tone): muffled car interior hush, rain starting to tap car glass, engine ticking as it idles. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  VICTORIA (panicked command): "You will tell Judge Miller the will was stolen from Walter's desk while he was demented."
  RICHARD (quiet, finished): "Father was never demented, Mother. I'm not perjuring myself for your stolen mansion."

ESCENA 45 (Viñeta #45 del Storyboard) — 07:20–07:30
- Location: county civic hall back alley, noon
- Characters Present: Elena Vance, Maggie Doyle, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the brick alleyway, the housekeeper presses an aged leather journal into the maid's hands, tears in her eyes.
  * [03s–07s]: insert shot of the evidence object — Insert: the journal page opens to October 12, 2008: 'Paid Sheriff Drummond $10,000 to classify barn fire as accidental'.
  * [07s–10s]: tight close-up — Close on the housekeeper whispering her final truth as she holds Elena's fingers tight.
- Sound Design (SFX & Voice Tone): water dripping from fire escape iron, muffled brass band tuning inside civic hall, distant crowd chatter. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  MAGGIE (solemn, tearful): "Walter kept this fire log. He wrote down the payoff check number right here."
  ELENA (reverent, warm): "This proves the fire was arson, Maggie. You just saved my mother's honor."

ESCENA 46 (Viñeta #46 del Storyboard) — 07:30–07:40
- Location: Silver Creek civic hall foyer, afternoon
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Before the towering carved oak doors, the maid pauses, adjusting her mother's silver belt buckle.
  * [03s–07s]: tight close-up — Close on the foreman reaching out, adjusting the collar of her white shirt with quiet tenderness.
  * [07s–10s]: low-angle hero shot — Low angle as the maid places her hand on the brass door handle and pushes both doors open.
- Sound Design (SFX & Voice Tone): crystal chandelier hum, ballroom orchestra playing light waltz, heavy oak doors swinging wide. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (gentle awe): "Every rancher, judge and banker in the state is in that room, Elena."
  ELENA (unshakable pride): "Good. It's time they learned who fed their horses for the last fifteen years."

ESCENA 47 (Viñeta #47 del Storyboard) — 07:40–07:50
- Location: civic hall grand ballroom, afternoon
- Characters Present: Elena Vance, Victoria Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — The grand ballroom falls utterly silent as the ranch maid in her simple white shirt strides down the red carpet toward the stage.
  * [03s–07s]: tight close-up — Close on the mistress's hand tightening around the podium microphone until her diamond ring clicks against the steel.
  * [07s–10s]: over-the-shoulder shot — Over the maid's shoulder, she ascends the three wooden stage stairs without breaking stride.
- Sound Design (SFX & Voice Tone): champagne glasses clinking nervously, ballroom murmur rising, microphone feedback whine. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (strangled anger): "Security, remove this girl immediately. This is a private county charity gala."
  ELENA (crystal clear): "You're auctioning Silver Creek land tonight, Victoria. But you don't own the dirt."

ESCENA 48 (Viñeta #48 del Storyboard) — 07:50–08:00
- Location: civic hall auction stage, afternoon
- Characters Present: Elena Vance, Victoria Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Under the blinding stage lights, the mistress steps right into the maid's face, abandoning all high-society poise.
  * [03s–07s]: tight close-up — Extreme close-up on the mistress's twisted expression as she speaks directly into Elena's ear.
  * [07s–10s]: insert shot of the evidence object — Insert: Elena lays Walter's blue-sealed will onto the auctioneer's reading desk.
- Sound Design (SFX & Voice Tone): dramatic crowd gasps echoing in high hall, spotlight hum, microphone catching ragged breaths. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (hissed fury): "You are a stable rat playing dress-up. No judge will ever take my ranch away."
  ELENA (level, devastating): "It was never your ranch. You were just warming the chair until I grew up."

COMANDO FINAL (16:9 YouTube):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 43 (Viñeta #43 del Storyboard) — 07:00–07:10
- Location: town bank steps, morning
- Characters Present: Elena Vance, Victoria Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — The maid emerges onto the sunlit steps, lifting the stamped court-certified envelope for the entire sidewalk to see.
  * [03s–07s]: tight close-up — Close on the mistress's painted smile slipping, raw panic flashing behind her eyes for the first time.
  * [07s–10s]: low-angle hero shot — Low angle on the maid looking down from the granite steps with quiet authority.
- Sound Design (SFX & Voice Tone): onlookers murmuring on sidewalk, pigeon wings flapping, wind snapping county banners. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts
- Dialogue (English, 6–8 sec max):
  ELENA (ringing, clear): "You told the county my mother had no standing. Walter's certified will begs to differ."
  VICTORIA (strained composure): "That paper is an obsolete draft. It means nothing without court ratification."

ESCENA 44 (Viñeta #44 del Storyboard) — 07:10–07:20
- Location: Blackwell town car, morning
- Characters Present: Victoria Blackwell, Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Inside the town car, the mistress grabs her son's lapel as he pulls himself back against the passenger door.
  * [03s–07s]: tight close-up — Close on the heir unfastening her gloved fingers from his jacket with quiet distaste.
  * [07s–10s]: over-the-shoulder shot — Over the mistress's shoulder, the heir stares out at the courthouse steps.
- Sound Design (SFX & Voice Tone): muffled car interior hush, rain starting to tap car glass, engine ticking as it idles. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  VICTORIA (panicked command): "You will tell Judge Miller the will was stolen from Walter's desk while he was demented."
  RICHARD (quiet, finished): "Father was never demented, Mother. I'm not perjuring myself for your stolen mansion."

ESCENA 45 (Viñeta #45 del Storyboard) — 07:20–07:30
- Location: county civic hall back alley, noon
- Characters Present: Elena Vance, Maggie Doyle, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the brick alleyway, the housekeeper presses an aged leather journal into the maid's hands, tears in her eyes.
  * [03s–07s]: insert shot of the evidence object — Insert: the journal page opens to October 12, 2008: 'Paid Sheriff Drummond $10,000 to classify barn fire as accidental'.
  * [07s–10s]: tight close-up — Close on the housekeeper whispering her final truth as she holds Elena's fingers tight.
- Sound Design (SFX & Voice Tone): water dripping from fire escape iron, muffled brass band tuning inside civic hall, distant crowd chatter. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  MAGGIE (solemn, tearful): "Walter kept this fire log. He wrote down the payoff check number right here."
  ELENA (reverent, warm): "This proves the fire was arson, Maggie. You just saved my mother's honor."

ESCENA 46 (Viñeta #46 del Storyboard) — 07:30–07:40
- Location: Silver Creek civic hall foyer, afternoon
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Before the towering carved oak doors, the maid pauses, adjusting her mother's silver belt buckle.
  * [03s–07s]: tight close-up — Close on the foreman reaching out, adjusting the collar of her white shirt with quiet tenderness.
  * [07s–10s]: low-angle hero shot — Low angle as the maid places her hand on the brass door handle and pushes both doors open.
- Sound Design (SFX & Voice Tone): crystal chandelier hum, ballroom orchestra playing light waltz, heavy oak doors swinging wide. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (gentle awe): "Every rancher, judge and banker in the state is in that room, Elena."
  ELENA (unshakable pride): "Good. It's time they learned who fed their horses for the last fifteen years."

ESCENA 47 (Viñeta #47 del Storyboard) — 07:40–07:50
- Location: civic hall grand ballroom, afternoon
- Characters Present: Elena Vance, Victoria Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — The grand ballroom falls utterly silent as the ranch maid in her simple white shirt strides down the red carpet toward the stage.
  * [03s–07s]: tight close-up — Close on the mistress's hand tightening around the podium microphone until her diamond ring clicks against the steel.
  * [07s–10s]: over-the-shoulder shot — Over the maid's shoulder, she ascends the three wooden stage stairs without breaking stride.
- Sound Design (SFX & Voice Tone): champagne glasses clinking nervously, ballroom murmur rising, microphone feedback whine. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (strangled anger): "Security, remove this girl immediately. This is a private county charity gala."
  ELENA (crystal clear): "You're auctioning Silver Creek land tonight, Victoria. But you don't own the dirt."

ESCENA 48 (Viñeta #48 del Storyboard) — 07:50–08:00
- Location: civic hall auction stage, afternoon
- Characters Present: Elena Vance, Victoria Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Under the blinding stage lights, the mistress steps right into the maid's face, abandoning all high-society poise.
  * [03s–07s]: tight close-up — Extreme close-up on the mistress's twisted expression as she speaks directly into Elena's ear.
  * [07s–10s]: insert shot of the evidence object — Insert: Elena lays Walter's blue-sealed will onto the auctioneer's reading desk.
- Sound Design (SFX & Voice Tone): dramatic crowd gasps echoing in high hall, spotlight hum, microphone catching ragged breaths. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (hissed fury): "You are a stable rat playing dress-up. No judge will ever take my ranch away."
  ELENA (level, devastating): "It was never your ranch. You were just warming the chair until I grew up."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 para Reels, TikTok y Shorts."
```

### Lote 09 — Minuto 9 (escenas 49–54)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_09.png`

**Guardar 16:9 como:** `raw_clips/minute_09.mp4`

**Guardar 9:16 como:** `raw_clips/minute_09_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 49 (Viñeta #49 del Storyboard) — 08:00–08:10
- Location: civic hall auction stage, afternoon
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the edge of the stage, the maid hands the heavy blue legal dossier down to the seated county probate judge.
  * [03s–07s]: tight close-up — Close on the judge adjusting his spectacles, his eyebrows climbing higher as he reads the notary stamp.
  * [07s–10s]: over-the-shoulder shot — Over the judge's shoulder, the maid stands perfectly still as the entire hall holds its breath.
- Sound Design (SFX & Voice Tone): gavel wooden strike on table, stunned uproar from crowd, chairs scraping parquet floor. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  CLERK (booming, judicial): "This signature is Walter Blackwell's. And the bank vault seal is verified. The auction is halted."
  ELENA (firm, calm): "Thank you, Your Honor. Now ask Mrs. Blackwell about the fire."

ESCENA 50 (Viñeta #50 del Storyboard) — 08:10–08:20
- Location: civic hall stage wings, afternoon
- Characters Present: Victoria Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the red velvet backstage shadows, the mistress corners the maid against the rope rigging, eyes feverish with malice.
  * [03s–07s]: tight close-up — Close on the mistress's diamond-ringed hand touching the maid's cheek with chilling faux affection.
  * [07s–10s]: extreme close-up — Extreme close-up on the mistress's whispered threat, her lips parting with vicious triumph.
- Sound Design (SFX & Voice Tone): muffled hall applause continuing outside, heavy rope groaning under tension, hiss of stage lamps. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts
- Dialogue (English, 6–8 sec max):
  VICTORIA (whispered madness): "Enjoy your paper victory, girl. Two barrels of kerosene are already in Silver Creek barn."
  VICTORIA (deadly hiss): "Sign the release, or watch your horses burn alive tonight."

ESCENA 51 (Viñeta #51 del Storyboard) — 08:20–08:30
- Location: Silver Creek barn exterior, dusk
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — The maid sprints through the barn gates as the foreman yanks a lit flare from a captured trespasser's hand.
  * [03s–07s]: insert shot of the evidence object — Insert: the foreman grinds the smoking red flare out beneath his heavy work boot into the damp mud.
  * [07s–10s]: tight close-up — Close on the foreman looking up at Elena, breathing hard but smiling with fierce triumph.
- Sound Design (SFX & Voice Tone): flare hissing into wet gravel, horses whinnying safe inside, heavy boots running on dirt. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (breathless, triumphant): "We were waiting for them in the hayloft, Elena. Not a single spark touched this barn."
  ELENA (steely relief): "Tie them up. Sheriff Drummond will need company in his own jail."

ESCENA 52 (Viñeta #52 del Storyboard) — 08:30–08:40
- Location: civic hall courtroom chamber, evening
- Characters Present: Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the witness stand, the heir raises his right hand before the court clerk, his voice echoing across the silent gallery.
  * [03s–07s]: tight close-up — Close on his pale face as he speaks the words that end his family's dynasty.
  * [07s–10s]: over-the-shoulder shot — Over the heir's shoulder, Victoria watches from the defense table, face white as chalk.
- Sound Design (SFX & Voice Tone): courtroom gavel banging, reporters' camera shutters clicking, collective gasp from gallery. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  RICHARD (resigned, clear): "I planted the silver watch in Elena Vance's saddle bag on my mother's direct orders."
  RICHARD (choked with shame): "Elena never stole anything. We stole fifteen years from her."

ESCENA 53 (Viñeta #53 del Storyboard) — 08:40–08:50
- Location: civic hall courtroom chamber, evening
- Characters Present: Maggie Doyle
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — The housekeeper stands tall at the microphone, looking directly at the district attorney with tearful dignity.
  * [03s–07s]: tight close-up — Close on her hand pressing the original fire log onto the court clerk's cedar bench.
  * [07s–10s]: over-the-shoulder shot — Over the housekeeper's shoulder, Elena nods from the front bench with unconditional love.
- Sound Design (SFX & Voice Tone): courtroom stenographer machine clicking rapidly, paper rustling, silence falling heavy. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana
- Dialogue (English, 6–8 sec max):
  MAGGIE (firm, unshakeable): "I formally recant my 2008 testimony. The barn fire was set deliberately by Victoria Blackwell."
  MAGGIE (hallowed truth): "June Vance was murdered protecting that ranch."

ESCENA 54 (Viñeta #54 del Storyboard) — 08:50–09:00
- Location: civic hall courtroom chamber, evening
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the plaintiff's table, the maid stands erect as the judge brings the wooden gavel down with final authority.
  * [03s–07s]: insert shot of the evidence object — Insert: the judge signs 'CERTIFICATE OF OWNERSHIP — SILVER CREEK RANCH — OWNER: ELENA VANCE'.
  * [07s–10s]: tight close-up — Close on Elena's eyes filling with tears of vindication, a slow, radiant smile breaking across her face.
- Sound Design (SFX & Voice Tone): resounding gavel strike, loud sustained applause from gallery, floorboards creaking. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  CLERK (booming proclamation): "This court recognizes Elena Vance as the sole legal heir and owner of Silver Creek Ranch."
  ELENA (whispered joy): "We did it, Mama. The ranch is home again."

COMANDO FINAL (16:9 YouTube):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 49 (Viñeta #49 del Storyboard) — 08:00–08:10
- Location: civic hall auction stage, afternoon
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the edge of the stage, the maid hands the heavy blue legal dossier down to the seated county probate judge.
  * [03s–07s]: tight close-up — Close on the judge adjusting his spectacles, his eyebrows climbing higher as he reads the notary stamp.
  * [07s–10s]: over-the-shoulder shot — Over the judge's shoulder, the maid stands perfectly still as the entire hall holds its breath.
- Sound Design (SFX & Voice Tone): gavel wooden strike on table, stunned uproar from crowd, chairs scraping parquet floor. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  CLERK (booming, judicial): "This signature is Walter Blackwell's. And the bank vault seal is verified. The auction is halted."
  ELENA (firm, calm): "Thank you, Your Honor. Now ask Mrs. Blackwell about the fire."

ESCENA 50 (Viñeta #50 del Storyboard) — 08:10–08:20
- Location: civic hall stage wings, afternoon
- Characters Present: Victoria Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the red velvet backstage shadows, the mistress corners the maid against the rope rigging, eyes feverish with malice.
  * [03s–07s]: tight close-up — Close on the mistress's diamond-ringed hand touching the maid's cheek with chilling faux affection.
  * [07s–10s]: extreme close-up — Extreme close-up on the mistress's whispered threat, her lips parting with vicious triumph.
- Sound Design (SFX & Voice Tone): muffled hall applause continuing outside, heavy rope groaning under tension, hiss of stage lamps. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts
- Dialogue (English, 6–8 sec max):
  VICTORIA (whispered madness): "Enjoy your paper victory, girl. Two barrels of kerosene are already in Silver Creek barn."
  VICTORIA (deadly hiss): "Sign the release, or watch your horses burn alive tonight."

ESCENA 51 (Viñeta #51 del Storyboard) — 08:20–08:30
- Location: Silver Creek barn exterior, dusk
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — The maid sprints through the barn gates as the foreman yanks a lit flare from a captured trespasser's hand.
  * [03s–07s]: insert shot of the evidence object — Insert: the foreman grinds the smoking red flare out beneath his heavy work boot into the damp mud.
  * [07s–10s]: tight close-up — Close on the foreman looking up at Elena, breathing hard but smiling with fierce triumph.
- Sound Design (SFX & Voice Tone): flare hissing into wet gravel, horses whinnying safe inside, heavy boots running on dirt. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (breathless, triumphant): "We were waiting for them in the hayloft, Elena. Not a single spark touched this barn."
  ELENA (steely relief): "Tie them up. Sheriff Drummond will need company in his own jail."

ESCENA 52 (Viñeta #52 del Storyboard) — 08:30–08:40
- Location: civic hall courtroom chamber, evening
- Characters Present: Richard Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the witness stand, the heir raises his right hand before the court clerk, his voice echoing across the silent gallery.
  * [03s–07s]: tight close-up — Close on his pale face as he speaks the words that end his family's dynasty.
  * [07s–10s]: over-the-shoulder shot — Over the heir's shoulder, Victoria watches from the defense table, face white as chalk.
- Sound Design (SFX & Voice Tone): courtroom gavel banging, reporters' camera shutters clicking, collective gasp from gallery. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, 6–8 sec max):
  RICHARD (resigned, clear): "I planted the silver watch in Elena Vance's saddle bag on my mother's direct orders."
  RICHARD (choked with shame): "Elena never stole anything. We stole fifteen years from her."

ESCENA 53 (Viñeta #53 del Storyboard) — 08:40–08:50
- Location: civic hall courtroom chamber, evening
- Characters Present: Maggie Doyle
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — The housekeeper stands tall at the microphone, looking directly at the district attorney with tearful dignity.
  * [03s–07s]: tight close-up — Close on her hand pressing the original fire log onto the court clerk's cedar bench.
  * [07s–10s]: over-the-shoulder shot — Over the housekeeper's shoulder, Elena nods from the front bench with unconditional love.
- Sound Design (SFX & Voice Tone): courtroom stenographer machine clicking rapidly, paper rustling, silence falling heavy. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana
- Dialogue (English, 6–8 sec max):
  MAGGIE (firm, unshakeable): "I formally recant my 2008 testimony. The barn fire was set deliberately by Victoria Blackwell."
  MAGGIE (hallowed truth): "June Vance was murdered protecting that ranch."

ESCENA 54 (Viñeta #54 del Storyboard) — 08:50–09:00
- Location: civic hall courtroom chamber, evening
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the plaintiff's table, the maid stands erect as the judge brings the wooden gavel down with final authority.
  * [03s–07s]: insert shot of the evidence object — Insert: the judge signs 'CERTIFICATE OF OWNERSHIP — SILVER CREEK RANCH — OWNER: ELENA VANCE'.
  * [07s–10s]: tight close-up — Close on Elena's eyes filling with tears of vindication, a slow, radiant smile breaking across her face.
- Sound Design (SFX & Voice Tone): resounding gavel strike, loud sustained applause from gallery, floorboards creaking. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  CLERK (booming proclamation): "This court recognizes Elena Vance as the sole legal heir and owner of Silver Creek Ranch."
  ELENA (whispered joy): "We did it, Mama. The ranch is home again."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 para Reels, TikTok y Shorts."
```

### Lote 10 — Minuto 10 (escenas 55–60)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_10.png`

**Guardar 16:9 como:** `raw_clips/minute_10.mp4`

**Guardar 9:16 como:** `raw_clips/minute_10_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 55 (Viñeta #55 del Storyboard) — 09:00–09:10
- Location: civic hall grand steps, night
- Characters Present: Victoria Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Under the flashing blue lights of state police cruisers, the troopers secure handcuffs behind the mistress's back.
  * [03s–07s]: tight close-up — Close on the steel cuffs ratcheting shut with sharp metallic clicks over her bare wrists.
  * [07s–10s]: over-the-shoulder shot — Over the mistress's shoulder, she sees the entire town watching her downfall in silence.
- Sound Design (SFX & Voice Tone): handcuffs clicking into place, police radios squawking, crowd watching without a sound. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts
- Dialogue (English, 6–8 sec max):
  CLERK (clipped, official): "Victoria Blackwell, you are under arrest for conspiracy, insurance fraud and attempted arson."
  VICTORIA (screeching, desperate): "You cannot do this to me! I built this town!"

ESCENA 56 (Viñeta #56 del Storyboard) — 09:10–09:20
- Location: civic hall grand steps, night
- Characters Present: Victoria Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — On the wet steps, the handcuffed mistress collapses forward onto her knees before the maid she once tormented.
  * [03s–07s]: tight close-up — Close on the mistress's mascara running in black streaks down her pale, pleading face.
  * [07s–10s]: low-angle hero shot — Low angle on the maid, dignified and untouchable as the night rain begins to fall gently.
- Sound Design (SFX & Voice Tone): rain softly pattering on granite steps, police cruiser doors opening, distant train whistle. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (weeping, broken): "Elena, please! Leave me the guesthouse. Don't throw me onto the street with nothing!"
  ELENA (calm, absolute): "You left me with a broken teacup and a broom. You'll leave with your suitcase."

ESCENA 57 (Viñeta #57 del Storyboard) — 09:20–09:30
- Location: Silver Creek mansion foyer, night
- Characters Present: Elena Vance, Maggie Doyle
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — The grand foyer is warm with lamplight; the maid stands where she was once humiliated, now as the estate's mistress.
  * [03s–07s]: tight close-up — Close on her fingers tracing the polished oak table where the crystal decanter was once smashed.
  * [07s–10s]: over-the-shoulder shot — Over the maid's shoulder, the housekeeper sets down a porcelain teacup with gentle reverence.
- Sound Design (SFX & Voice Tone): warm fire crackling in hearth, porcelain cup settling on wood, night breeze through tall windows. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  MAGGIE (tender, peaceful): "The house is quiet, Elena. For the first time in thirty years, it feels clean."
  ELENA (warm, resolute): "It's not just a house anymore, Maggie. It's a sanctuary for everyone they pushed down."

ESCENA 58 (Viñeta #58 del Storyboard) — 09:30–09:40
- Location: Silver Creek barn gate, moonlight
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — At the corral gate, the foreman turns to the maid, nervously rolling the brim of his felt hat in both hands.
  * [03s–07s]: tight close-up — Close on Elena's hand reaching up to touch his weathered cheek, stopping his nervous motion.
  * [07s–10s]: over-the-shoulder shot — Over the foreman's shoulder, she steps into his arms, resting her forehead against his chest.
- Sound Design (SFX & Voice Tone): night crickets singing in prairie grass, horses grazing peacefully, soft warm breeze. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (vulnerable, quiet): "You're the master of twenty thousand acres now, Elena. You don't need a stray foreman."
  ELENA (intimate, fierce): "I don't need a foreman, Cole. I need you. Stay and build this with me."

ESCENA 59 (Viñeta #59 del Storyboard) — 09:40–09:50
- Location: Blackwell great room mantelpiece, night
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Before the roaring stone hearth, the maid steps back as June Vance's smiling photograph occupies the place of honor.
  * [03s–07s]: insert shot of the evidence object — Insert: the silver belt buckle catches the orange firelight beside the tin frame, engraved: 'VANCE RANCH — 1982'.
  * [07s–10s]: tight close-up — Close on Elena's face, radiant with deep peace as a single grateful tear slips down her cheek.
- Sound Design (SFX & Voice Tone): deep hearth fire crackling warmly, pine wood popping, soft wind against glass. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (solemn, joyous): "Your name will never be erased from Montana again, Mama. Silver Creek is ours, and justice has finally been done."

ESCENA 60 (Viñeta #60 del Storyboard) — 09:50–10:00
- Location: mansion study desk, night
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the quiet study desk, the maid notices a sealed wax envelope attached to the back of the will parchment.
  * [03s–07s]: insert shot of the evidence object — Insert: her thumb cracks the red wax seal: 'To Elena — Read in private after you claim the ranch'.
  * [07s–10s]: tight close-up — Close on Elena's eyes widening in stunned alarm as she reads Walter's final words in the letter.
- Sound Design (SFX & Voice Tone): paper crackling in silence, banker lamp humming softly, sudden wind banging study shutters. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (shivering shock): "There is another clause... 'Elena, you are not June's only child. Find your brother before Victoria's family does.'"
  ELENA (breathless cliffhanger): "I have a brother?"

COMANDO FINAL (16:9 YouTube):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 55 (Viñeta #55 del Storyboard) — 09:00–09:10
- Location: civic hall grand steps, night
- Characters Present: Victoria Blackwell
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Under the flashing blue lights of state police cruisers, the troopers secure handcuffs behind the mistress's back.
  * [03s–07s]: tight close-up — Close on the steel cuffs ratcheting shut with sharp metallic clicks over her bare wrists.
  * [07s–10s]: over-the-shoulder shot — Over the mistress's shoulder, she sees the entire town watching her downfall in silence.
- Sound Design (SFX & Voice Tone): handcuffs clicking into place, police radios squawking, crowd watching without a sound. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts
- Dialogue (English, 6–8 sec max):
  CLERK (clipped, official): "Victoria Blackwell, you are under arrest for conspiracy, insurance fraud and attempted arson."
  VICTORIA (screeching, desperate): "You cannot do this to me! I built this town!"

ESCENA 56 (Viñeta #56 del Storyboard) — 09:10–09:20
- Location: civic hall grand steps, night
- Characters Present: Victoria Blackwell, Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — On the wet steps, the handcuffed mistress collapses forward onto her knees before the maid she once tormented.
  * [03s–07s]: tight close-up — Close on the mistress's mascara running in black streaks down her pale, pleading face.
  * [07s–10s]: low-angle hero shot — Low angle on the maid, dignified and untouchable as the night rain begins to fall gently.
- Sound Design (SFX & Voice Tone): rain softly pattering on granite steps, police cruiser doors opening, distant train whistle. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  VICTORIA (weeping, broken): "Elena, please! Leave me the guesthouse. Don't throw me onto the street with nothing!"
  ELENA (calm, absolute): "You left me with a broken teacup and a broom. You'll leave with your suitcase."

ESCENA 57 (Viñeta #57 del Storyboard) — 09:20–09:30
- Location: Silver Creek mansion foyer, night
- Characters Present: Elena Vance, Maggie Doyle
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — The grand foyer is warm with lamplight; the maid stands where she was once humiliated, now as the estate's mistress.
  * [03s–07s]: tight close-up — Close on her fingers tracing the polished oak table where the crystal decanter was once smashed.
  * [07s–10s]: over-the-shoulder shot — Over the maid's shoulder, the housekeeper sets down a porcelain teacup with gentle reverence.
- Sound Design (SFX & Voice Tone): warm fire crackling in hearth, porcelain cup settling on wood, night breeze through tall windows. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  MAGGIE (tender, peaceful): "The house is quiet, Elena. For the first time in thirty years, it feels clean."
  ELENA (warm, resolute): "It's not just a house anymore, Maggie. It's a sanctuary for everyone they pushed down."

ESCENA 58 (Viñeta #58 del Storyboard) — 09:30–09:40
- Location: Silver Creek barn gate, moonlight
- Characters Present: Elena Vance, Cole Barrett
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — At the corral gate, the foreman turns to the maid, nervously rolling the brim of his felt hat in both hands.
  * [03s–07s]: tight close-up — Close on Elena's hand reaching up to touch his weathered cheek, stopping his nervous motion.
  * [07s–10s]: over-the-shoulder shot — Over the foreman's shoulder, she steps into his arms, resting her forehead against his chest.
- Sound Design (SFX & Voice Tone): night crickets singing in prairie grass, horses grazing peacefully, soft warm breeze. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  COLE (vulnerable, quiet): "You're the master of twenty thousand acres now, Elena. You don't need a stray foreman."
  ELENA (intimate, fierce): "I don't need a foreman, Cole. I need you. Stay and build this with me."

ESCENA 59 (Viñeta #59 del Storyboard) — 09:40–09:50
- Location: Blackwell great room mantelpiece, night
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Before the roaring stone hearth, the maid steps back as June Vance's smiling photograph occupies the place of honor.
  * [03s–07s]: insert shot of the evidence object — Insert: the silver belt buckle catches the orange firelight beside the tin frame, engraved: 'VANCE RANCH — 1982'.
  * [07s–10s]: tight close-up — Close on Elena's face, radiant with deep peace as a single grateful tear slips down her cheek.
- Sound Design (SFX & Voice Tone): deep hearth fire crackling warmly, pine wood popping, soft wind against glass. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (solemn, joyous): "Your name will never be erased from Montana again, Mama. Silver Creek is ours, and justice has finally been done."

ESCENA 60 (Viñeta #60 del Storyboard) — 09:50–10:00
- Location: mansion study desk, night
- Characters Present: Elena Vance
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the quiet study desk, the maid notices a sealed wax envelope attached to the back of the will parchment.
  * [03s–07s]: insert shot of the evidence object — Insert: her thumb cracks the red wax seal: 'To Elena — Read in private after you claim the ranch'.
  * [07s–10s]: tight close-up — Close on Elena's eyes widening in stunned alarm as she reads Walter's final words in the letter.
- Sound Design (SFX & Voice Tone): paper crackling in silence, banker lamp humming softly, sudden wind banging study shutters. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, 6–8 sec max):
  ELENA (shivering shock): "There is another clause... 'Elena, you are not June's only child. Find your brother before Victoria's family does.'"
  ELENA (breathless cliffhanger): "I have a brother?"

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato vertical 9:16 para Reels, TikTok y Shorts."
```

---

## Paso 4 — Ensamblar

Cuando existan los 10 archivos `minute_01.mp4 … minute_10.mp4`:

```powershell
./novelfactory.bat assemble the_ranch_maid_heiress
```

El ensamblador detecta el modo B, genera el máster 16:9 de 10 minutos,
el SRT sincronizado y el teaser vertical automático de 20 segundos.

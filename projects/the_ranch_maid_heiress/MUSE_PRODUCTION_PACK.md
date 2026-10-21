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

Position #1 (Far Left) — ELENA VANCE. Rol: Protagonista. Edad: mid-twenties. Rasgos físicos: Casting sheet for the character reference image: woman in her mid-twenties, sun-weathered gently angular face, long chestnut hair worn in a single low braid, calm dark-brown eyes, light freckling across the nose, a faint old scar through one eyebrow, slender but strong ranch build, signature faded blue denim work shirt and dark riding jeans.. Vestuario fijo: faded blue denim work shirt, dark riding jeans, worn boots, low braid.
Position #2 — VICTORIA BLACKWELL. Rol: Antagonista. Edad: mid-forties. Rasgos físicos: Casting sheet for the character reference image: woman in her mid-forties, sleek platinum-blonde bob, sharp cheekbones, cool grey eyes, immaculate posture, dark red lipstick, pearl earrings, signature emerald silk blouse over tailored black trousers.. Vestuario fijo: emerald silk blouse, tailored black trousers, pearl earrings.
Position #3 — RICHARD BLACKWELL. Rol: Heredero antagonista. Edad: thirty. Rasgos físicos: Casting sheet for the character reference image: man around thirty, clean-cut, sandy hair combed back, pale blue eyes, a practiced easy smile, tall athletic build, signature pressed white shirt under a charcoal blazer.. Vestuario fijo: pressed white shirt, charcoal blazer, polished boots.
Position #4 — COLE BARRETT. Rol: Interés romántico. Edad: early-thirties. Rasgos físicos: Casting sheet for the character reference image: man in his early thirties, weathered rancher hands, dark hair a little long under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, signature oiled tan canvas chore jacket over a grey henley.. Vestuario fijo: oiled tan canvas chore jacket over a grey henley, worn felt hat.
Position #5 (Far Right) — MAGGIE DOYLE. Rol: Aliada. Edad: late-fifties. Rasgos físicos: Casting sheet for the character reference image: woman in her late fifties, iron-grey hair pinned up in a loose bun, kind weathered face, small round glasses on a chain, floral house apron over a beige cardigan and a long dark skirt.. Vestuario fijo: floral house apron over a beige cardigan, long dark skirt.

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

Viñeta 1 — Escena 1 (Blackwell mansion foyer, storm dusk): [00s-03s] medium two-shot: In the grand foyer, the maid recoils from the shattered decanter as the woman in emerald silk advances on her. Location: Blackwell mansion foyer, storm dusk. Key object: the shattered crystal decanter. Characters present: Elena Vance, Victoria Blackwell, Richard Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald silk blouse, tailored black trousers, pearl earrings); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing pressed white shirt, charcoal blazer, polished boots).
Viñeta 2 — Escena 2 (Silver Creek barn aisle, night): [00s-03s] wide establishing shot: The barn aisle at night: the maid steps back between the stalls as the housekeeper fills the doorway, rain drumming on the tin roof. Location: Silver Creek barn aisle, night. Key object: a worn leather halter. Characters present: Elena Vance, Maggie Doyle. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing floral house apron over a beige cardigan, long dark skirt).
Viñeta 3 — Escena 3 (Blackwell mansion foyer, night): [00s-03s] medium shot: In the foyer, the maid pulls her saddle bag open while the woman in emerald silk jabs a finger at it. Location: Blackwell mansion foyer, night. Key object: Elena's canvas duffel bag. Characters present: Elena Vance, Victoria Blackwell, Richard Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald silk blouse, tailored black trousers, pearl earrings); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing pressed white shirt, charcoal blazer, polished boots).
Viñeta 4 — Escena 4 (Silver Creek stable aisle, morning): [00s-03s] medium shot: In the stable aisle, the maid tightens a saddle girth while the heir behind her lifts the silver watch from her open bag. Location: Silver Creek stable aisle, morning. Key object: the silver watch. Characters present: Elena Vance, Richard Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing pressed white shirt, charcoal blazer, polished boots).
Viñeta 5 — Escena 5 (Blackwell great room, morning): [00s-03s] medium shot: In the timber great room, the woman in emerald silk gestures to a chair; the maid stays on her feet and steps back. Location: Blackwell great room, morning. Key object: a folded release form. Characters present: Elena Vance, Victoria Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald silk blouse, tailored black trousers, pearl earrings).
Viñeta 6 — Escena 6 (Silver Creek barn doorway, late afternoon): [00s-03s] medium shot: At the barn door, the maid works a curry comb in slow circles while the foreman leans on the stall, speaking low. Location: Silver Creek barn doorway, late afternoon. Key object: a bridle repaired with waxed thread. Characters present: Elena Vance, Cole Barrett. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing oiled tan canvas chore jacket over a grey henley, worn felt hat).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_02.png — Minuto 2 (escenas 7–12)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 2 (Escenas 7 a 12) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 7 (Blackwell study, late afternoon): [00s-03s] medium shot: In the lamplit study, the mistress slides a closed file across the desk; the maid steps up to it. Location: Blackwell study, late afternoon. Key object: a bank envelope of hush money. Characters present: Elena Vance, Victoria Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald silk blouse, tailored black trousers, pearl earrings).
Viñeta 2 — Escena 8 (gatehouse cottage, dusk): [00s-03s] medium close-up: In the small stone cottage, the maid works the old saddle's leather lining open with her thumbs. Location: gatehouse cottage, dusk. Key object: a hand-sewn lining with a waxed envelope. Characters present: Elena Vance. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid).
Viñeta 3 — Escena 9 (Silver Creek barn aisle, night): [00s-03s] medium shot: In the barn aisle at night, the maid lifts the brass key to the light while the foreman turns toward the whitewashed tack-room door. Location: Silver Creek barn aisle, night. Key object: a small brass key. Characters present: Elena Vance, Cole Barrett. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing oiled tan canvas chore jacket over a grey henley, worn felt hat).
Viñeta 4 — Escena 10 (Silver Creek sealed tack room, night): [00s-03s] medium shot: Inside the tack room, the maid pulls an open tin box from the floor while the foreman steps in with bolt cutters. Location: Silver Creek sealed tack room, night. Key object: a fire-scorched property deed. Characters present: Elena Vance, Cole Barrett. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing oiled tan canvas chore jacket over a grey henley, worn felt hat).
Viñeta 5 — Escena 11 (Silver Creek county records office, morning): [00s-03s] medium shot: At the oak counter, the maid lays the old deed down while the clerk turns a heavy ledger toward her. Location: Silver Creek county records office, morning. Key object: a county sale record. Characters present: Elena Vance. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work).
Viñeta 6 — Escena 12 (county records steps, grey morning): [00s-03s] medium shot: On the stone steps, the maid backs up with a folder clutched to her chest while the foreman follows, hat in hand. Location: county records steps, grey morning. Key object: a probate form. Characters present: Elena Vance, Cole Barrett. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing canvas chore jacket, collar turned up, rain-darkened at the shoulders).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_03.png — Minuto 3 (escenas 13–18)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 3 (Escenas 13 a 18) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 13 (Blackwell paneled office, afternoon): [00s-03s] medium shot: In the paneled office, the maid lifts a single sheet of paper while the woman in black cashmere turns from the window. Location: Blackwell paneled office, afternoon. Key object: a grave-tending receipt. Characters present: Elena Vance, Victoria Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing black cashmere turtleneck, long grey riding coat, leather gloves).
Viñeta 2 — Escena 14 (Blackwell dark-paneled hallway, afternoon): [00s-03s] medium shot: In the dark-paneled hallway, the heir steps close to the maid, hands open, while she backs away with her folder. Location: Blackwell dark-paneled hallway, afternoon. Key object: the planted silver watch. Characters present: Elena Vance, Richard Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing grey wool overcoat over the white shirt, silver cufflinks).
Viñeta 3 — Escena 15 (gatehouse cottage, dusk): [00s-03s] medium shot: At the oilcloth table, the maid pushes a covered pie aside while the housekeeper leans across it. Location: gatehouse cottage, dusk. Key object: a signed 2008 statement. Characters present: Elena Vance, Maggie Doyle. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing wool shawl pinned over the cardigan, apron folded over one arm).
Viñeta 4 — Escena 16 (Silver Creek barn aisle, night): [00s-03s] medium shot: In the barn aisle, the maid sets a lantern between them as the foreman steps in from the rain. Location: Silver Creek barn aisle, night. Key object: a truck's tire tracks. Characters present: Elena Vance, Cole Barrett. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing canvas chore jacket, collar turned up, rain-darkened at the shoulders).
Viñeta 5 — Escena 17 (Blackwell study, night): [00s-03s] medium shot: In the lamplit study, the mistress leans over the desk while the heir paces and loosens his collar. Location: Blackwell study, night. Key object: June Vance's probate file. Characters present: Victoria Blackwell, Richard Blackwell. Identity anchors: Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing black cashmere turtleneck, long grey riding coat, leather gloves); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing grey wool overcoat over the white shirt, silver cufflinks).
Viñeta 6 — Escena 18 (Silver Creek county records office, morning): [00s-03s] medium shot: At the counter, the clerk shakes her head over a sealed drawer while the maid pulls her folder back. Location: Silver Creek county records office, morning. Key object: a missing-file receipt. Characters present: Elena Vance. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_04.png — Minuto 4 (escenas 19–24)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 4 (Escenas 19 a 24) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 19 (Blackwell great room, dinner, night): [00s-03s] medium shot: In the candlelit great room, the mistress rises with a glass while the maid steps to the edge of the tables. Location: Blackwell great room, dinner, night. Key object: a dinner place card. Characters present: Elena Vance, Victoria Blackwell, Richard Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing black cashmere turtleneck, long grey riding coat, leather gloves); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing grey wool overcoat over the white shirt, silver cufflinks).
Viñeta 2 — Escena 20 (Blackwell gravel yard, night): [00s-03s] medium shot: In the gravel yard at night, a steel barrel burns as the mistress thrusts a folded paper at the maid. Location: Blackwell gravel yard, night. Key object: a signed release form. Characters present: Elena Vance, Victoria Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing black cashmere turtleneck, long grey riding coat, leather gloves).
Viñeta 3 — Escena 21 (gatehouse cottage, night): [00s-03s] medium two-shot: In the cottage lamplight, the maid unrolls the old county survey map while the foreman anchors the curling corners with heavy iron horseshoes. Location: gatehouse cottage, night. Key object: a scraped parcel map. Characters present: Elena Vance, Cole Barrett. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing chore jacket with a broken zipper pull, leather work gloves).
Viñeta 4 — Escena 22 (Blackwell tack room, night): [00s-03s] medium shot: In the shadowy tack room, the maid kneels beside the wall timber and slides a cylindrical tin case from the hollow cavity. Location: Blackwell tack room, night. Key object: a stack of cash tax receipts. Characters present: Elena Vance. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt).
Viñeta 5 — Escena 23 (Silver Creek barn hayloft, night): [00s-03s] medium two-shot: In the moonlight, the foreman gently binds the maid's bruised palm with white tape, his touch slow and deliberate. Location: Silver Creek barn hayloft, night. Key object: a lantern in the hayloft. Characters present: Elena Vance, Cole Barrett. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing chore jacket with a broken zipper pull, leather work gloves).
Viñeta 6 — Escena 24 (Blackwell study archives, night): [00s-03s] medium shot: Behind the desk, the maid turns with the open ledger as the heir steps over the threshold. Location: Blackwell study archives, night. Key object: a ledger of quiet payments. Characters present: Elena Vance, Richard Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing white shirt with sleeves rolled, dark trousers).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_05.png — Minuto 5 (escenas 25–30)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 5 (Escenas 25 a 30) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 25 (Blackwell mansion great room, night): [00s-03s] medium shot: In the vast room, the mistress swings a small brass ribboned key while the maid backs toward the cold hearth. Location: Blackwell mansion great room, night. Key object: Walter's unsigned will. Characters present: Elena Vance, Victoria Blackwell, Richard Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing silver-grey silk blouse, charcoal skirt, single pearl strand); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing white shirt with sleeves rolled, dark trousers).
Viñeta 2 — Escena 26 (Blackwell mansion gravel drive, night): [00s-03s] medium two-shot: Under harsh halogen yard lights, the foreman plants his boots in front of the heir, refusing to yield the driveway. Location: Blackwell mansion gravel drive, night. Key object: a shotgun on the porch. Characters present: Richard Blackwell, Cole Barrett. Identity anchors: Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing white shirt with sleeves rolled, dark trousers); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing chore jacket with a broken zipper pull, leather work gloves).
Viñeta 3 — Escena 27 (gatehouse cottage porch, night): [00s-03s] medium shot: On the rain-slick porch steps, the heir reaches out with a cream envelope while the maid refuses to accept it. Location: gatehouse cottage porch, night. Key object: a threat written on a feed receipt. Characters present: Elena Vance, Richard Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing white shirt with sleeves rolled, dark trousers).
Viñeta 4 — Escena 28 (Silver Creek barn aisle, night): [00s-03s] medium shot: In the barn aisle, the housekeeper rushes to the maid and grabs both of her elbows with trembling hands. Location: Silver Creek barn aisle, night. Key object: an empty wall safe. Characters present: Elena Vance, Maggie Doyle. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing beige cardigan under the wool shawl, apron gone).
Viñeta 5 — Escena 29 (Blackwell estate gates, midnight): [00s-03s] medium shot: By the iron gates, the mistress steps out of the luxury car into the headlights, holding a checkbook open. Location: Blackwell estate gates, midnight. Key object: a suitcase full of cash. Characters present: Elena Vance, Victoria Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing silver-grey silk blouse, charcoal skirt, single pearl strand).
Viñeta 6 — Escena 30 (Blackwell estate gates, midnight): [00s-03s] medium two-shot: Under the headlights, the mistress thrusts the certified check into the maid's face like an execution order. Location: Blackwell estate gates, midnight. Key object: a final cash offer. Characters present: Elena Vance, Victoria Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing silver-grey silk blouse, charcoal skirt, single pearl strand).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_06.png — Minuto 6 (escenas 31–36)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 6 (Escenas 31 a 36) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 31 (gatehouse cottage, storm night): [00s-03s] wide establishing shot: Inside the ransacked cottage, the storm sweeps through shattered windows, scattering torn clothes and broken crockery across wet stones. Location: gatehouse cottage, storm night. Key object: a broken floorboard. Characters present: Elena Vance. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain).
Viñeta 2 — Escena 32 (gatehouse cottage yard, storm night): [00s-03s] medium shot: In the swirling red and blue emergency light, the maid runs to the padlocked gate as rain washes mud over her boots. Location: gatehouse cottage yard, storm night. Key object: an eviction notice. Characters present: Elena Vance. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain).
Viñeta 3 — Escena 33 (Silver Creek hay shed, storm night): [00s-03s] medium two-shot: In the drafty shelter, the maid wraps her own dry flannel scarf around the weeping housekeeper's neck. Location: Silver Creek hay shed, storm night. Key object: a nursing-home bill. Characters present: Elena Vance, Maggie Doyle. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing wool shawl against the storm, glasses fogged, small travel bag).
Viñeta 4 — Escena 34 (Blackwell mansion rear terrace, storm night): [00s-03s] medium shot: Inside the glowing library, the mistress feeds the ancient deed into the fireplace flames while rain streaks the window. Location: Blackwell mansion rear terrace, storm night. Key object: a burned deed in the fireplace. Characters present: Victoria Blackwell, Richard Blackwell. Identity anchors: Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing black cashmere sweater, thin diamond bracelet, hair set perfectly despite the storm); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing dark rain jacket over the white shirt, collar up against the storm).
Viñeta 5 — Escena 35 (Silver Creek stable tack room, storm night): [00s-03s] medium shot: In a sudden flash of lightning, the maid appears like a ghost in the stable door, blocking the heir's retreat. Location: Silver Creek stable tack room, storm night. Key object: a safe-deposit box key. Characters present: Elena Vance, Richard Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing dark rain jacket over the white shirt, collar up against the storm).
Viñeta 6 — Escena 36 (ranch ridge overlook, storm dawn): [00s-03s] wide establishing shot: On the high ridge, the maid walks into frame against the vast Montana valley as dawn breaks slate grey. Location: ranch ridge overlook, storm dawn. Key object: a handful of red Montana dirt. Characters present: Elena Vance. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_07.png — Minuto 7 (escenas 37–42)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 7 (Escenas 37 a 42) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 37 (ranch ridge road, dawn): [00s-03s] medium two-shot: On the muddy road, the foreman wraps his dry wool jacket around her, pulling the collar up against the wind. Location: ranch ridge road, dawn. Key object: a truck key and gas can. Characters present: Elena Vance, Cole Barrett. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing soaked canvas jacket, grey henley underneath, no hat).
Viñeta 2 — Escena 38 (ranch ridge road, green truck cab, dawn): [00s-03s] medium shot: Inside the bouncing truck cab, the maid turns the brass key in the dashboard light, scraping away years of verdigris. Location: ranch ridge road, green truck cab, dawn. Key object: a brass bank key stamped FVT 14. Characters present: Elena Vance, Cole Barrett. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing soaked canvas jacket, grey henley underneath, no hat).
Viñeta 3 — Escena 39 (town bank exterior, morning): [00s-03s] medium shot: On the bank steps, the maid and foreman turn together as the limousine door opens across the street. Location: town bank exterior, morning. Key object: the bank vault door. Characters present: Elena Vance, Cole Barrett. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing soaked canvas jacket, grey henley underneath, no hat).
Viñeta 4 — Escena 40 (First Valley Trust vault corridor, morning): [00s-03s] medium shot: Inside the gleaming vault, the maid turns the brass key into Lock 14; the heavy tumbler clicks open with a hollow ring. Location: First Valley Trust vault corridor, morning. Key object: Walter's certified will. Characters present: Elena Vance. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain).
Viñeta 5 — Escena 41 (First Valley Trust manager office, morning): [00s-03s] medium shot: In the sunlit bank office, the maid steps up to the desk as the grey-haired bank manager lifts the embossed blue notary seal to his bifocals. Location: First Valley Trust manager office, morning. Key object: a notary seal. Characters present: Elena Vance. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat).
Viñeta 6 — Escena 42 (town bank steps, morning): [00s-03s] medium two-shot: On the stone steps, the foreman plants himself between the mistress and the bank doors as the sheriff steps forward. Location: town bank steps, morning. Key object: a bank payroll ledger. Characters present: Victoria Blackwell, Cole Barrett. Identity anchors: Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing clean denim jacket over the grey henley, hat brushed for once).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_08.png — Minuto 8 (escenas 43–48)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 8 (Escenas 43 a 48) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 43 (town bank steps, morning): [00s-03s] medium shot: The maid emerges onto the sunlit steps, lifting the stamped court-certified envelope for the entire sidewalk to see. Location: town bank steps, morning. Key object: a court filing stamp. Characters present: Elena Vance, Victoria Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings).
Viñeta 2 — Escena 44 (Blackwell town car, morning): [00s-03s] medium two-shot: Inside the town car, the mistress grabs her son's lapel as he pulls himself back against the passenger door. Location: Blackwell town car, morning. Key object: a perjury statement. Characters present: Victoria Blackwell, Richard Blackwell. Identity anchors: Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing black suit for the gala, sharp lapels, slicked hair).
Viñeta 3 — Escena 45 (county civic hall back alley, noon): [00s-03s] medium shot: In the brick alleyway, the housekeeper presses an aged leather journal into the maid's hands, tears in her eyes. Location: county civic hall back alley, noon. Key object: a fire log with a check number. Characters present: Elena Vance, Cole Barrett, Maggie Doyle. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing clean denim jacket over the grey henley, hat brushed for once); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing best Sunday cardigan, the apron folded neatly on a chair).
Viñeta 4 — Escena 46 (Silver Creek civic hall foyer, afternoon): [00s-03s] medium two-shot: Before the towering carved oak doors, the maid walks up and adjusts her mother's silver belt buckle. Location: Silver Creek civic hall foyer, afternoon. Key object: a gala invitation. Characters present: Elena Vance, Cole Barrett. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing clean denim jacket over the grey henley, hat brushed for once).
Viñeta 5 — Escena 47 (civic hall grand ballroom, afternoon): [00s-03s] wide establishing shot: The grand ballroom falls utterly silent as the ranch maid in her simple white shirt strides down the red carpet toward the stage. Location: civic hall grand ballroom, afternoon. Key object: an auction catalog. Characters present: Elena Vance, Victoria Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings).
Viñeta 6 — Escena 48 (civic hall auction stage, afternoon): [00s-03s] medium two-shot: Under the blinding stage lights, the mistress steps right into the maid's face, abandoning all high-society poise. Location: civic hall auction stage, afternoon. Key object: a gavel on the auction block. Characters present: Elena Vance, Victoria Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_09.png — Minuto 9 (escenas 49–54)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 9 (Escenas 49 a 54) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 49 (civic hall auction stage, afternoon): [00s-03s] medium shot: At the edge of the stage, the maid hands the heavy blue legal dossier down to the seated county probate judge. Location: civic hall auction stage, afternoon. Key object: a verified signature card. Characters present: Elena Vance, Cole Barrett. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing clean denim jacket over the grey henley, hat brushed for once).
Viñeta 2 — Escena 50 (civic hall stage wings, afternoon): [00s-03s] medium two-shot: In the red velvet backstage shadows, the mistress corners the maid against the rope rigging, eyes feverish with malice. Location: civic hall stage wings, afternoon. Key object: a kerosene can. Characters present: Elena Vance, Victoria Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings).
Viñeta 3 — Escena 51 (Silver Creek barn exterior, dusk): [00s-03s] medium shot: The maid sprints through the barn gates as the foreman yanks a lit flare from a captured trespasser's hand. Location: Silver Creek barn exterior, dusk. Key object: a coil of rope in the hayloft. Characters present: Elena Vance, Cole Barrett. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing same denim jacket, hat in hand, standing at the barn door).
Viñeta 4 — Escena 52 (civic hall courtroom chamber, evening): [00s-03s] medium shot: At the witness stand, the heir raises his right hand before the court clerk, his voice echoing across the silent gallery. Location: civic hall courtroom chamber, evening. Key object: a handwritten confession. Characters present: Richard Blackwell. Identity anchors: Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing black gala suit, tie loosened, shaken).
Viñeta 5 — Escena 53 (civic hall courtroom chamber, evening): [00s-03s] medium shot: The housekeeper grips the microphone and lifts her chin toward the district attorney. Location: civic hall courtroom chamber, evening. Key object: a recantation form. Characters present: Maggie Doyle. Identity anchors: Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing same Sunday cardigan, hair escaped from the bun, standing tall).
Viñeta 6 — Escena 54 (civic hall courtroom chamber, evening): [00s-03s] medium shot: At the plaintiff's table, the maid rises as the judge brings the wooden gavel down. Location: civic hall courtroom chamber, evening. Key object: a court order. Characters present: Elena Vance. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
```

### REF_GRID_MIN_10.png — Minuto 10 (escenas 55–60)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 10 (Escenas 55 a 60) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 55 (civic hall grand steps, night): [00s-03s] medium shot: Under the flashing blue lights of state police cruisers, the troopers secure handcuffs behind the mistress's back. Location: civic hall grand steps, night. Key object: a pair of handcuffs. Characters present: Elena Vance, Victoria Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald gala dress, gloves gone, jewelry missing).
Viñeta 2 — Escena 56 (civic hall grand steps, night): [00s-03s] medium two-shot: On the wet steps, the handcuffed mistress collapses forward onto her knees before the maid she once tormented. Location: civic hall grand steps, night. Key object: a suitcase on the steps. Characters present: Elena Vance, Victoria Blackwell. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald gala dress, gloves gone, jewelry missing).
Viñeta 3 — Escena 57 (Silver Creek mansion foyer, night): [00s-03s] wide establishing shot: The grand foyer is warm with lamplight; the maid crosses the floor where she was once humiliated, now as the estate's mistress. Location: Silver Creek mansion foyer, night. Key object: a clean white teacup. Characters present: Elena Vance, Maggie Doyle. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing same Sunday cardigan, hair escaped from the bun, standing tall).
Viñeta 4 — Escena 58 (Silver Creek barn gate, moonlight): [00s-03s] medium two-shot: At the corral gate, the foreman turns to the maid, nervously rolling the brim of his felt hat in both hands. Location: Silver Creek barn gate, moonlight. Key object: a set of ranch keys. Characters present: Elena Vance, Cole Barrett. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing same denim jacket, hat in hand, standing at the barn door).
Viñeta 5 — Escena 59 (Blackwell great room mantelpiece, night): [00s-03s] medium shot: Before the roaring stone hearth, the maid steps back as June Vance's smiling photograph occupies the place of honor. Location: Blackwell great room mantelpiece, night. Key object: a framed photograph of June. Characters present: Elena Vance. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle).
Viñeta 6 — Escena 60 (mansion study desk, night): [00s-03s] medium shot: At the quiet study desk, the maid lifts the will parchment and finds a sealed wax envelope attached to the back. Location: mansion study desk, night. Key object: a folded letter with a second clause. Characters present: Elena Vance. Identity anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible. No incluyas diálogos, párrafos largos, subtítulos, globos de texto, logos ni marcas de agua; solo la cuadrícula, la numeración y la descripción breve de cada viñeta.
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
- Characters Present: Elena Vance, Victoria Blackwell, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: In the grand foyer, the maid recoils from the shattered decanter as the woman in emerald silk advances on her. Location: Blackwell mansion foyer, storm dusk. Key object: the shattered crystal decanter. Characters present: Elena Vance, Victoria Blackwell, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald silk blouse, tailored black trousers, pearl earrings); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing pressed white shirt, charcoal blazer, polished boots)
- Key Object: the shattered crystal decanter
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the grand foyer, the maid recoils from the shattered decanter as the woman in emerald silk advances on her.
  * [03s–07s]: tight close-up — hard cut into the dialogue beat with the speaker mid-line
  * [07s–10s]: tight close-up — Over the maid's shoulder, the woman in emerald silk stares her down while the heir in the white shirt watches from the staircase.
- Sound Design (SFX & Voice Tone): storm wind at the tall windows, crystal settling on oak, the chandelier's faint creak, one held breath. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (cold, precise): "You steal at my son's party."
  ELENA (quiet, shaking): "I didn't touch it. I was in the barn."

ESCENA 2 (Viñeta #2 del Storyboard) — 00:10–00:20
- Location: Silver Creek barn aisle, night
- Characters Present: Elena Vance, Maggie Doyle
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot: The barn aisle at night: the maid steps back between the stalls as the housekeeper fills the doorway, rain drumming on the tin roof. Location: Silver Creek barn aisle, night. Key object: a worn leather halter. Characters present: Elena Vance, Maggie Doyle.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing floral house apron over a beige cardigan, long dark skirt)
- Key Object: a worn leather halter
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — The barn aisle at night: the maid steps back between the stalls as the housekeeper fills the doorway, rain drumming on the tin roof.
  * [03s–07s]: over-the-shoulder shot — Over the maid's shoulder, the old photograph shows a woman at a ranch gate, sun-bleached and smiling.
  * [07s–10s]: tight close-up — Close on the housekeeper's face as she recognizes the photograph; she closes her eyes for one beat.
- Sound Design (SFX & Voice Tone): rain on a tin roof, a horse shifting in straw, a bucket chain rattling. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  MAGGIE (rough, kind): "Your mother fed this barn before you could walk."
  ELENA (low): "They erased her fifteen years ago."

ESCENA 3 (Viñeta #3 del Storyboard) — 00:20–00:30
- Location: Blackwell mansion foyer, night
- Characters Present: Elena Vance, Victoria Blackwell, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the foyer, the maid pulls her saddle bag open while the woman in emerald silk jabs a finger at it. Location: Blackwell mansion foyer, night. Key object: Elena's canvas duffel bag. Characters present: Elena Vance, Victoria Blackwell, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald silk blouse, tailored black trousers, pearl earrings); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing pressed white shirt, charcoal blazer, polished boots)
- Key Object: Elena's canvas duffel bag
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the foyer, the maid pulls her saddle bag open while the woman in emerald silk jabs a finger at it.
  * [03s–07s]: tight close-up — Close on the maid's face as she sets her jaw; her hands close around the worn leather.
  * [07s–10s]: tight close-up — Low angle on the maid from below the staircase, chin lifted, the chandelier hard above her.
- Sound Design (SFX & Voice Tone): leather creaking, a clock ticking somewhere deep in the house, rain softening. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (cold): "Empty it. If his watch is there, you leave tonight."
  ELENA (flat): "My mother's things stay."

ESCENA 4 (Viñeta #4 del Storyboard) — 00:30–00:40
- Location: Silver Creek stable aisle, morning
- Characters Present: Elena Vance, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the stable aisle, the maid tightens a saddle girth while the heir behind her lifts the silver watch from her open bag. Location: Silver Creek stable aisle, morning. Key object: the silver watch. Characters present: Elena Vance, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing pressed white shirt, charcoal blazer, polished boots)
- Key Object: the silver watch
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the stable aisle, the maid tightens a saddle girth while the heir behind her lifts the silver watch from her open bag.
  * [03s–07s]: close-up — Insert: the silver watch turns once in the heir's fingers, catching a blade of window light.
  * [07s–10s]: tight close-up — hard cut to the reaction as the line lands
- Sound Design (SFX & Voice Tone): a horse snorting, leather straps, straw under boots, the watch's tiny clasp. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  RICHARD (low): "Look what her saddle was hiding."
  ELENA (steady): "You were in the tack room last night."

ESCENA 5 (Viñeta #5 del Storyboard) — 00:40–00:50
- Location: Blackwell great room, morning
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the timber great room, the woman in emerald silk gestures to a chair; the maid stays on her feet and steps back. Location: Blackwell great room, morning. Key object: a folded release form. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald silk blouse, tailored black trousers, pearl earrings)
- Key Object: a folded release form
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the timber great room, the woman in emerald silk gestures to a chair; the maid stays on her feet and steps back.
  * [03s–07s]: over-the-shoulder shot — Over the mistress's shoulder, the folded confession paper waits on the low table between them.
  * [07s–10s]: tight close-up — Close on the maid's hand as she slides the paper back across the table without sitting.
- Sound Design (SFX & Voice Tone): a fireplace ticking as it cools, paper sliding on wood, a chair creaking. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (silky): "Sign it, take your pay, and stay quiet."
  ELENA (quiet): "It happened when you decided it did."

ESCENA 6 (Viñeta #6 del Storyboard) — 00:50–01:00
- Location: Silver Creek barn doorway, late afternoon
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: At the barn door, the maid works a curry comb in slow circles while the foreman leans on the stall, speaking low. Location: Silver Creek barn doorway, late afternoon. Key object: a bridle repaired with waxed thread. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing oiled tan canvas chore jacket over a grey henley, worn felt hat)
- Key Object: a bridle repaired with waxed thread
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the barn door, the maid works a curry comb in slow circles while the foreman leans on the stall, speaking low.
  * [03s–07s]: over-the-shoulder shot — Over the maid's shoulder: the foreman's hands tighten on the stall door as he finishes his sentence.
  * [07s–10s]: tight close-up — Close on the maid's eyes lifting at last, weighing what he just offered.
- Sound Design (SFX & Voice Tone): curry comb against hide, a horse's low nicker, wind under the eaves. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (blunt): "I saw Richard at the saddles."
  ELENA (tired): "He'll call you a liar and take your house."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 1 (Viñeta #1 del Storyboard) — 00:00–00:10
- Location: Blackwell mansion foyer, storm dusk
- Characters Present: Elena Vance, Victoria Blackwell, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: In the grand foyer, the maid recoils from the shattered decanter as the woman in emerald silk advances on her. Location: Blackwell mansion foyer, storm dusk. Key object: the shattered crystal decanter. Characters present: Elena Vance, Victoria Blackwell, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald silk blouse, tailored black trousers, pearl earrings); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing pressed white shirt, charcoal blazer, polished boots)
- Key Object: the shattered crystal decanter
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the grand foyer, the maid recoils from the shattered decanter as the woman in emerald silk advances on her.
  * [03s–07s]: tight close-up — hard cut into the dialogue beat with the speaker mid-line
  * [07s–10s]: tight close-up — Over the maid's shoulder, the woman in emerald silk stares her down while the heir in the white shirt watches from the staircase.
- Sound Design (SFX & Voice Tone): storm wind at the tall windows, crystal settling on oak, the chandelier's faint creak, one held breath. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (cold, precise): "You steal at my son's party."
  ELENA (quiet, shaking): "I didn't touch it. I was in the barn."

ESCENA 2 (Viñeta #2 del Storyboard) — 00:10–00:20
- Location: Silver Creek barn aisle, night
- Characters Present: Elena Vance, Maggie Doyle
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot: The barn aisle at night: the maid steps back between the stalls as the housekeeper fills the doorway, rain drumming on the tin roof. Location: Silver Creek barn aisle, night. Key object: a worn leather halter. Characters present: Elena Vance, Maggie Doyle.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing floral house apron over a beige cardigan, long dark skirt)
- Key Object: a worn leather halter
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — The barn aisle at night: the maid steps back between the stalls as the housekeeper fills the doorway, rain drumming on the tin roof.
  * [03s–07s]: over-the-shoulder shot — Over the maid's shoulder, the old photograph shows a woman at a ranch gate, sun-bleached and smiling.
  * [07s–10s]: tight close-up — Close on the housekeeper's face as she recognizes the photograph; she closes her eyes for one beat.
- Sound Design (SFX & Voice Tone): rain on a tin roof, a horse shifting in straw, a bucket chain rattling. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  MAGGIE (rough, kind): "Your mother fed this barn before you could walk."
  ELENA (low): "They erased her fifteen years ago."

ESCENA 3 (Viñeta #3 del Storyboard) — 00:20–00:30
- Location: Blackwell mansion foyer, night
- Characters Present: Elena Vance, Victoria Blackwell, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the foyer, the maid pulls her saddle bag open while the woman in emerald silk jabs a finger at it. Location: Blackwell mansion foyer, night. Key object: Elena's canvas duffel bag. Characters present: Elena Vance, Victoria Blackwell, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald silk blouse, tailored black trousers, pearl earrings); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing pressed white shirt, charcoal blazer, polished boots)
- Key Object: Elena's canvas duffel bag
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the foyer, the maid pulls her saddle bag open while the woman in emerald silk jabs a finger at it.
  * [03s–07s]: tight close-up — Close on the maid's face as she sets her jaw; her hands close around the worn leather.
  * [07s–10s]: tight close-up — Low angle on the maid from below the staircase, chin lifted, the chandelier hard above her.
- Sound Design (SFX & Voice Tone): leather creaking, a clock ticking somewhere deep in the house, rain softening. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (cold): "Empty it. If his watch is there, you leave tonight."
  ELENA (flat): "My mother's things stay."

ESCENA 4 (Viñeta #4 del Storyboard) — 00:30–00:40
- Location: Silver Creek stable aisle, morning
- Characters Present: Elena Vance, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the stable aisle, the maid tightens a saddle girth while the heir behind her lifts the silver watch from her open bag. Location: Silver Creek stable aisle, morning. Key object: the silver watch. Characters present: Elena Vance, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing pressed white shirt, charcoal blazer, polished boots)
- Key Object: the silver watch
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the stable aisle, the maid tightens a saddle girth while the heir behind her lifts the silver watch from her open bag.
  * [03s–07s]: close-up — Insert: the silver watch turns once in the heir's fingers, catching a blade of window light.
  * [07s–10s]: tight close-up — hard cut to the reaction as the line lands
- Sound Design (SFX & Voice Tone): a horse snorting, leather straps, straw under boots, the watch's tiny clasp. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  RICHARD (low): "Look what her saddle was hiding."
  ELENA (steady): "You were in the tack room last night."

ESCENA 5 (Viñeta #5 del Storyboard) — 00:40–00:50
- Location: Blackwell great room, morning
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the timber great room, the woman in emerald silk gestures to a chair; the maid stays on her feet and steps back. Location: Blackwell great room, morning. Key object: a folded release form. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald silk blouse, tailored black trousers, pearl earrings)
- Key Object: a folded release form
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the timber great room, the woman in emerald silk gestures to a chair; the maid stays on her feet and steps back.
  * [03s–07s]: over-the-shoulder shot — Over the mistress's shoulder, the folded confession paper waits on the low table between them.
  * [07s–10s]: tight close-up — Close on the maid's hand as she slides the paper back across the table without sitting.
- Sound Design (SFX & Voice Tone): a fireplace ticking as it cools, paper sliding on wood, a chair creaking. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (silky): "Sign it, take your pay, and stay quiet."
  ELENA (quiet): "It happened when you decided it did."

ESCENA 6 (Viñeta #6 del Storyboard) — 00:50–01:00
- Location: Silver Creek barn doorway, late afternoon
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: At the barn door, the maid works a curry comb in slow circles while the foreman leans on the stall, speaking low. Location: Silver Creek barn doorway, late afternoon. Key object: a bridle repaired with waxed thread. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing oiled tan canvas chore jacket over a grey henley, worn felt hat)
- Key Object: a bridle repaired with waxed thread
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the barn door, the maid works a curry comb in slow circles while the foreman leans on the stall, speaking low.
  * [03s–07s]: over-the-shoulder shot — Over the maid's shoulder: the foreman's hands tighten on the stall door as he finishes his sentence.
  * [07s–10s]: tight close-up — Close on the maid's eyes lifting at last, weighing what he just offered.
- Sound Design (SFX & Voice Tone): curry comb against hide, a horse's low nicker, wind under the eaves. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (blunt): "I saw Richard at the saddles."
  ELENA (tired): "He'll call you a liar and take your house."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts."
```

### Lote 02 — Minuto 2 (escenas 7–12)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_02.png`

**Guardar 16:9 como:** `raw_clips/minute_02.mp4`

**Guardar 9:16 como:** `raw_clips/minute_02_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 7 (Viñeta #7 del Storyboard) — 01:00–01:10
- Location: Blackwell study, late afternoon
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the lamplit study, the mistress slides a closed file across the desk; the maid steps up to it. Location: Blackwell study, late afternoon. Key object: a bank envelope of hush money. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald silk blouse, tailored black trousers, pearl earrings)
- Key Object: a bank envelope of hush money
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the lamplit study, the mistress slides a closed file across the desk; the maid steps up to it.
  * [03s–07s]: tight close-up — Close on the file as her finger lifts, leaving a clean mark in the dust.
  * [07s–10s]: tight close-up — Low angle on the maid as she absorbs the deadline without looking away.
- Sound Design (SFX & Voice Tone): a desk clock ticking, leather chair creaking, the window rattling softly. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (pleasant threat): "Sheriff Drummond is a friend. Sign by Friday."
  ELENA (cold): "Do you still tend her grave?"

ESCENA 8 (Viñeta #8 del Storyboard) — 01:10–01:20
- Location: gatehouse cottage, dusk
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium close-up: In the small stone cottage, the maid works the old saddle's leather lining open with her thumbs. Location: gatehouse cottage, dusk. Key object: a hand-sewn lining with a waxed envelope. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid)
- Key Object: a hand-sewn lining with a waxed envelope
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium close-up — In the small stone cottage, the maid works the old saddle's leather lining open with her thumbs.
  * [03s–07s]: close-up — Insert: her fingers draw a small brass key from the hidden seam, warm against the cold leather.
  * [07s–10s]: tight close-up — Close on her face as she recognizes the key; the room darkens around her.
- Sound Design (SFX & Voice Tone): wind pressing the eaves, leather creaking, a stove ticking as it cools. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (hushed): "You sewed it into the lining, Mama."
  ELENA (breaking): "What were you afraid I'd find?"

ESCENA 9 (Viñeta #9 del Storyboard) — 01:20–01:30
- Location: Silver Creek barn aisle, night
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the barn aisle at night, the maid lifts the brass key to the light while the foreman turns toward the whitewashed tack-room door. Location: Silver Creek barn aisle, night. Key object: a small brass key. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing oiled tan canvas chore jacket over a grey henley, worn felt hat)
- Key Object: a small brass key
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the barn aisle at night, the maid lifts the brass key to the light while the foreman turns toward the whitewashed tack-room door.
  * [03s–07s]: close-up — Insert: the small brass key turns under the bulb, too delicate for any hasp in the barn.
  * [07s–10s]: tight close-up — Over her shoulder: the painted-over iron hasp, sealed with fifteen years of whitewash.
- Sound Design (SFX & Voice Tone): a bulb humming, a horse stamping, wind rattling the barn planks. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (low): "That key fits no door in this valley."
  ELENA (decided): "Then we open that room tonight."

ESCENA 10 (Viñeta #10 del Storyboard) — 01:30–01:40
- Location: Silver Creek sealed tack room, night
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: Inside the tack room, the maid pulls an open tin box from the floor while the foreman steps in with bolt cutters. Location: Silver Creek sealed tack room, night. Key object: a fire-scorched property deed. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing oiled tan canvas chore jacket over a grey henley, worn felt hat)
- Key Object: a fire-scorched property deed
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Inside the tack room, the maid pulls an open tin box from the floor while the foreman steps in with bolt cutters.
  * [03s–07s]: close-up — Insert: a cream deed unfolds in her hands, its old seal still intact.
  * [07s–10s]: tight close-up — Close on her face as she reads the name; her lips part, and she has to steady the paper.
- Sound Design (SFX & Voice Tone): a work lamp buzzing, old paper unfolding, a chain shifting outside, rain starting. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; COLE — quiet, low American English, careful diction, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (shaking): "This deed says Vance. My mother owned Silver Creek."
  COLE (grim): "Then the fire wasn't bad luck."

ESCENA 11 (Viñeta #11 del Storyboard) — 01:40–01:50
- Location: Silver Creek county records office, morning
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: At the oak counter, the maid lays the old deed down while the clerk turns a heavy ledger toward her. Location: Silver Creek county records office, morning. Key object: a county sale record. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work)
- Key Object: a county sale record
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the oak counter, the maid lays the old deed down while the clerk turns a heavy ledger toward her.
  * [03s–07s]: close-up — Insert: the ledger's ruled page for the Silver Creek parcel, stamped and countersigned.
  * [07s–10s]: tight close-up — Close on the maid as the clerk's answer lands; her jaw sets, but her eyes drop.
- Sound Design (SFX & Voice Tone): ledger pages turning, a wall clock, boots on creaking wood. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (flat): "The sale was recorded in 2009. Blackwell owns it."
  ELENA (hard): "Then open a probate file."

ESCENA 12 (Viñeta #12 del Storyboard) — 01:50–02:00
- Location: county records steps, grey morning
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: On the stone steps, the maid backs up with a folder clutched to her chest while the foreman follows, hat in hand. Location: county records steps, grey morning. Key object: a probate form. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing canvas chore jacket, collar turned up, rain-darkened at the shoulders)
- Key Object: a probate form
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — On the stone steps, the maid backs up with a folder clutched to her chest while the foreman follows, hat in hand.
  * [03s–07s]: tight close-up — Close on her hands tightening on the folder's edge until the card bends.
  * [07s–10s]: tight close-up — Over the foreman's shoulder: her face against the grey street, deciding.
- Sound Design (SFX & Voice Tone): wind across stone steps, a truck passing on wet asphalt, a flag snapping. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (urgent): "Probate takes months. She's already calling her lawyer."
  ELENA (quiet): "Then I'll fight with what she fears."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 7 (Viñeta #7 del Storyboard) — 01:00–01:10
- Location: Blackwell study, late afternoon
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the lamplit study, the mistress slides a closed file across the desk; the maid steps up to it. Location: Blackwell study, late afternoon. Key object: a bank envelope of hush money. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald silk blouse, tailored black trousers, pearl earrings)
- Key Object: a bank envelope of hush money
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the lamplit study, the mistress slides a closed file across the desk; the maid steps up to it.
  * [03s–07s]: tight close-up — Close on the file as her finger lifts, leaving a clean mark in the dust.
  * [07s–10s]: tight close-up — Low angle on the maid as she absorbs the deadline without looking away.
- Sound Design (SFX & Voice Tone): a desk clock ticking, leather chair creaking, the window rattling softly. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (pleasant threat): "Sheriff Drummond is a friend. Sign by Friday."
  ELENA (cold): "Do you still tend her grave?"

ESCENA 8 (Viñeta #8 del Storyboard) — 01:10–01:20
- Location: gatehouse cottage, dusk
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium close-up: In the small stone cottage, the maid works the old saddle's leather lining open with her thumbs. Location: gatehouse cottage, dusk. Key object: a hand-sewn lining with a waxed envelope. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid)
- Key Object: a hand-sewn lining with a waxed envelope
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium close-up — In the small stone cottage, the maid works the old saddle's leather lining open with her thumbs.
  * [03s–07s]: close-up — Insert: her fingers draw a small brass key from the hidden seam, warm against the cold leather.
  * [07s–10s]: tight close-up — Close on her face as she recognizes the key; the room darkens around her.
- Sound Design (SFX & Voice Tone): wind pressing the eaves, leather creaking, a stove ticking as it cools. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (hushed): "You sewed it into the lining, Mama."
  ELENA (breaking): "What were you afraid I'd find?"

ESCENA 9 (Viñeta #9 del Storyboard) — 01:20–01:30
- Location: Silver Creek barn aisle, night
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the barn aisle at night, the maid lifts the brass key to the light while the foreman turns toward the whitewashed tack-room door. Location: Silver Creek barn aisle, night. Key object: a small brass key. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing oiled tan canvas chore jacket over a grey henley, worn felt hat)
- Key Object: a small brass key
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the barn aisle at night, the maid lifts the brass key to the light while the foreman turns toward the whitewashed tack-room door.
  * [03s–07s]: close-up — Insert: the small brass key turns under the bulb, too delicate for any hasp in the barn.
  * [07s–10s]: tight close-up — Over her shoulder: the painted-over iron hasp, sealed with fifteen years of whitewash.
- Sound Design (SFX & Voice Tone): a bulb humming, a horse stamping, wind rattling the barn planks. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (low): "That key fits no door in this valley."
  ELENA (decided): "Then we open that room tonight."

ESCENA 10 (Viñeta #10 del Storyboard) — 01:30–01:40
- Location: Silver Creek sealed tack room, night
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: Inside the tack room, the maid pulls an open tin box from the floor while the foreman steps in with bolt cutters. Location: Silver Creek sealed tack room, night. Key object: a fire-scorched property deed. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt, dark riding jeans, worn boots, low braid); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing oiled tan canvas chore jacket over a grey henley, worn felt hat)
- Key Object: a fire-scorched property deed
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Inside the tack room, the maid pulls an open tin box from the floor while the foreman steps in with bolt cutters.
  * [03s–07s]: close-up — Insert: a cream deed unfolds in her hands, its old seal still intact.
  * [07s–10s]: tight close-up — Close on her face as she reads the name; her lips part, and she has to steady the paper.
- Sound Design (SFX & Voice Tone): a work lamp buzzing, old paper unfolding, a chain shifting outside, rain starting. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; COLE — quiet, low American English, careful diction, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (shaking): "This deed says Vance. My mother owned Silver Creek."
  COLE (grim): "Then the fire wasn't bad luck."

ESCENA 11 (Viñeta #11 del Storyboard) — 01:40–01:50
- Location: Silver Creek county records office, morning
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: At the oak counter, the maid lays the old deed down while the clerk turns a heavy ledger toward her. Location: Silver Creek county records office, morning. Key object: a county sale record. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work)
- Key Object: a county sale record
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the oak counter, the maid lays the old deed down while the clerk turns a heavy ledger toward her.
  * [03s–07s]: close-up — Insert: the ledger's ruled page for the Silver Creek parcel, stamped and countersigned.
  * [07s–10s]: tight close-up — Close on the maid as the clerk's answer lands; her jaw sets, but her eyes drop.
- Sound Design (SFX & Voice Tone): ledger pages turning, a wall clock, boots on creaking wood. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (flat): "The sale was recorded in 2009. Blackwell owns it."
  ELENA (hard): "Then open a probate file."

ESCENA 12 (Viñeta #12 del Storyboard) — 01:50–02:00
- Location: county records steps, grey morning
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: On the stone steps, the maid backs up with a folder clutched to her chest while the foreman follows, hat in hand. Location: county records steps, grey morning. Key object: a probate form. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing canvas chore jacket, collar turned up, rain-darkened at the shoulders)
- Key Object: a probate form
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — On the stone steps, the maid backs up with a folder clutched to her chest while the foreman follows, hat in hand.
  * [03s–07s]: tight close-up — Close on her hands tightening on the folder's edge until the card bends.
  * [07s–10s]: tight close-up — Over the foreman's shoulder: her face against the grey street, deciding.
- Sound Design (SFX & Voice Tone): wind across stone steps, a truck passing on wet asphalt, a flag snapping. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (urgent): "Probate takes months. She's already calling her lawyer."
  ELENA (quiet): "Then I'll fight with what she fears."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts."
```

### Lote 03 — Minuto 3 (escenas 13–18)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_03.png`

**Guardar 16:9 como:** `raw_clips/minute_03.mp4`

**Guardar 9:16 como:** `raw_clips/minute_03_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 13 (Viñeta #13 del Storyboard) — 02:00–02:10
- Location: Blackwell paneled office, afternoon
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the paneled office, the maid lifts a single sheet of paper while the woman in black cashmere turns from the window. Location: Blackwell paneled office, afternoon. Key object: a grave-tending receipt. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing black cashmere turtleneck, long grey riding coat, leather gloves)
- Key Object: a grave-tending receipt
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the paneled office, the maid lifts a single sheet of paper while the woman in black cashmere turns from the window.
  * [03s–07s]: over-the-shoulder shot — Over the maid's shoulder: the paper offers a year of grave upkeep and a dropped charge.
  * [07s–10s]: tight close-up — Close on the maid's face: she reads the terms, and something in her goes cold.
- Sound Design (SFX & Voice Tone): a coal settling in the grate, gloves creaking, wind at the window. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (controlled): "I'll tend her grave. Leave Silver Creek."
  ELENA (flat): "You're offering a gardener, not her name."

ESCENA 14 (Viñeta #14 del Storyboard) — 02:10–02:20
- Location: Blackwell dark-paneled hallway, afternoon
- Characters Present: Elena Vance, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the dark-paneled hallway, the heir steps close to the maid, hands open, while she backs away with her folder. Location: Blackwell dark-paneled hallway, afternoon. Key object: the planted silver watch. Characters present: Elena Vance, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing grey wool overcoat over the white shirt, silver cufflinks)
- Key Object: the planted silver watch
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the dark-paneled hallway, the heir steps close to the maid, hands open, while she backs away with her folder.
  * [03s–07s]: tight close-up — Close on the heir's face: the practiced smile is gone for once.
  * [07s–10s]: tight close-up — Over his shoulder: the maid's eyes narrow, reading the first honest thing he's said.
- Sound Design (SFX & Voice Tone): a floorboard creaking, wind at the high window, muffled voices from below. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  RICHARD (low): "I know you didn't take the watch. Leave before she decides."
  ELENA (sharp): "Why do you care?"

ESCENA 15 (Viñeta #15 del Storyboard) — 02:20–02:30
- Location: gatehouse cottage, dusk
- Characters Present: Elena Vance, Maggie Doyle
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: At the oilcloth table, the maid pushes a covered pie aside while the housekeeper leans across it. Location: gatehouse cottage, dusk. Key object: a signed 2008 statement. Characters present: Elena Vance, Maggie Doyle.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing wool shawl pinned over the cardigan, apron folded over one arm)
- Key Object: a signed 2008 statement
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the oilcloth table, the maid pushes a covered pie aside while the housekeeper leans across it.
  * [03s–07s]: tight close-up — Close on the housekeeper's hands twisting a napkin until the linen frays.
  * [07s–10s]: tight close-up — Over the housekeeper's shoulder: the maid's face as she understands what was signed.
- Sound Design (SFX & Voice Tone): the stove ticking, wind at the eaves, a spoon rattling against china. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  MAGGIE (ashamed): "I signed a lie about the fire."
  ELENA (raw): "You told them my mother was careless."

ESCENA 16 (Viñeta #16 del Storyboard) — 02:30–02:40
- Location: Silver Creek barn aisle, night
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the barn aisle, the maid sets a lantern between them as the foreman steps in from the rain. Location: Silver Creek barn aisle, night. Key object: a truck's tire tracks. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing canvas chore jacket, collar turned up, rain-darkened at the shoulders)
- Key Object: a truck's tire tracks
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the barn aisle, the maid sets a lantern between them as the foreman steps in from the rain.
  * [03s–07s]: tight close-up — Close on the foreman's jaw as he forces the words out.
  * [07s–10s]: tight close-up — Over his shoulder: the maid's face as she takes the confession without blinking.
- Sound Design (SFX & Voice Tone): rain hammering the doorway, lantern glass ticking, a horse stamping in straw. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (quiet): "I was fifteen. I saw a truck leave."
  ELENA (cold): "You watched it leave and said nothing."

ESCENA 17 (Viñeta #17 del Storyboard) — 02:40–02:50
- Location: Blackwell study, night
- Characters Present: Victoria Blackwell, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the lamplit study, the mistress leans over the desk while the heir paces and loosens his collar. Location: Blackwell study, night. Key object: June Vance's probate file. Characters present: Victoria Blackwell, Richard Blackwell.
- Identity Anchors: Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing black cashmere turtleneck, long grey riding coat, leather gloves); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing grey wool overcoat over the white shirt, silver cufflinks)
- Key Object: June Vance's probate file
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the lamplit study, the mistress leans over the desk while the heir paces and loosens his collar.
  * [03s–07s]: tight close-up — Close on her hand closing a folder marked only by a county seal.
  * [07s–10s]: tight close-up — Over her shoulder: the heir's reflection in the dark window, caught between defiance and fear.
- Sound Design (SFX & Voice Tone): a drawer sliding shut, rain against glass, a lamp humming. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (sharp): "The probate clerk called. Someone requested June's file."
  RICHARD (tired): "The watch was your idea, remember?"

ESCENA 18 (Viñeta #18 del Storyboard) — 02:50–03:00
- Location: Silver Creek county records office, morning
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: At the counter, the clerk shakes her head over a sealed drawer while the maid pulls her folder back. Location: Silver Creek county records office, morning. Key object: a missing-file receipt. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work)
- Key Object: a missing-file receipt
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the counter, the clerk shakes her head over a sealed drawer while the maid pulls her folder back.
  * [03s–07s]: close-up — Insert: the drawer's small brass lock, closed and freshly oiled.
  * [07s–10s]: tight close-up — Close on the maid as the refusal lands; she doesn't look away.
- Sound Design (SFX & Voice Tone): a drawer lock clicking, a clock, a pen set down too carefully. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (flat): "Blackwell pulled the file. No record remains."
  ELENA (determined): "She made sure there's a record somewhere."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 13 (Viñeta #13 del Storyboard) — 02:00–02:10
- Location: Blackwell paneled office, afternoon
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the paneled office, the maid lifts a single sheet of paper while the woman in black cashmere turns from the window. Location: Blackwell paneled office, afternoon. Key object: a grave-tending receipt. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing black cashmere turtleneck, long grey riding coat, leather gloves)
- Key Object: a grave-tending receipt
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the paneled office, the maid lifts a single sheet of paper while the woman in black cashmere turns from the window.
  * [03s–07s]: over-the-shoulder shot — Over the maid's shoulder: the paper offers a year of grave upkeep and a dropped charge.
  * [07s–10s]: tight close-up — Close on the maid's face: she reads the terms, and something in her goes cold.
- Sound Design (SFX & Voice Tone): a coal settling in the grate, gloves creaking, wind at the window. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (controlled): "I'll tend her grave. Leave Silver Creek."
  ELENA (flat): "You're offering a gardener, not her name."

ESCENA 14 (Viñeta #14 del Storyboard) — 02:10–02:20
- Location: Blackwell dark-paneled hallway, afternoon
- Characters Present: Elena Vance, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the dark-paneled hallway, the heir steps close to the maid, hands open, while she backs away with her folder. Location: Blackwell dark-paneled hallway, afternoon. Key object: the planted silver watch. Characters present: Elena Vance, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing grey wool overcoat over the white shirt, silver cufflinks)
- Key Object: the planted silver watch
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the dark-paneled hallway, the heir steps close to the maid, hands open, while she backs away with her folder.
  * [03s–07s]: tight close-up — Close on the heir's face: the practiced smile is gone for once.
  * [07s–10s]: tight close-up — Over his shoulder: the maid's eyes narrow, reading the first honest thing he's said.
- Sound Design (SFX & Voice Tone): a floorboard creaking, wind at the high window, muffled voices from below. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  RICHARD (low): "I know you didn't take the watch. Leave before she decides."
  ELENA (sharp): "Why do you care?"

ESCENA 15 (Viñeta #15 del Storyboard) — 02:20–02:30
- Location: gatehouse cottage, dusk
- Characters Present: Elena Vance, Maggie Doyle
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: At the oilcloth table, the maid pushes a covered pie aside while the housekeeper leans across it. Location: gatehouse cottage, dusk. Key object: a signed 2008 statement. Characters present: Elena Vance, Maggie Doyle.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing wool shawl pinned over the cardigan, apron folded over one arm)
- Key Object: a signed 2008 statement
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the oilcloth table, the maid pushes a covered pie aside while the housekeeper leans across it.
  * [03s–07s]: tight close-up — Close on the housekeeper's hands twisting a napkin until the linen frays.
  * [07s–10s]: tight close-up — Over the housekeeper's shoulder: the maid's face as she understands what was signed.
- Sound Design (SFX & Voice Tone): the stove ticking, wind at the eaves, a spoon rattling against china. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  MAGGIE (ashamed): "I signed a lie about the fire."
  ELENA (raw): "You told them my mother was careless."

ESCENA 16 (Viñeta #16 del Storyboard) — 02:30–02:40
- Location: Silver Creek barn aisle, night
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the barn aisle, the maid sets a lantern between them as the foreman steps in from the rain. Location: Silver Creek barn aisle, night. Key object: a truck's tire tracks. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing canvas chore jacket, collar turned up, rain-darkened at the shoulders)
- Key Object: a truck's tire tracks
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the barn aisle, the maid sets a lantern between them as the foreman steps in from the rain.
  * [03s–07s]: tight close-up — Close on the foreman's jaw as he forces the words out.
  * [07s–10s]: tight close-up — Over his shoulder: the maid's face as she takes the confession without blinking.
- Sound Design (SFX & Voice Tone): rain hammering the doorway, lantern glass ticking, a horse stamping in straw. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (quiet): "I was fifteen. I saw a truck leave."
  ELENA (cold): "You watched it leave and said nothing."

ESCENA 17 (Viñeta #17 del Storyboard) — 02:40–02:50
- Location: Blackwell study, night
- Characters Present: Victoria Blackwell, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the lamplit study, the mistress leans over the desk while the heir paces and loosens his collar. Location: Blackwell study, night. Key object: June Vance's probate file. Characters present: Victoria Blackwell, Richard Blackwell.
- Identity Anchors: Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing black cashmere turtleneck, long grey riding coat, leather gloves); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing grey wool overcoat over the white shirt, silver cufflinks)
- Key Object: June Vance's probate file
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the lamplit study, the mistress leans over the desk while the heir paces and loosens his collar.
  * [03s–07s]: tight close-up — Close on her hand closing a folder marked only by a county seal.
  * [07s–10s]: tight close-up — Over her shoulder: the heir's reflection in the dark window, caught between defiance and fear.
- Sound Design (SFX & Voice Tone): a drawer sliding shut, rain against glass, a lamp humming. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (sharp): "The probate clerk called. Someone requested June's file."
  RICHARD (tired): "The watch was your idea, remember?"

ESCENA 18 (Viñeta #18 del Storyboard) — 02:50–03:00
- Location: Silver Creek county records office, morning
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: At the counter, the clerk shakes her head over a sealed drawer while the maid pulls her folder back. Location: Silver Creek county records office, morning. Key object: a missing-file receipt. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work)
- Key Object: a missing-file receipt
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the counter, the clerk shakes her head over a sealed drawer while the maid pulls her folder back.
  * [03s–07s]: close-up — Insert: the drawer's small brass lock, closed and freshly oiled.
  * [07s–10s]: tight close-up — Close on the maid as the refusal lands; she doesn't look away.
- Sound Design (SFX & Voice Tone): a drawer lock clicking, a clock, a pen set down too carefully. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (flat): "Blackwell pulled the file. No record remains."
  ELENA (determined): "She made sure there's a record somewhere."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts."
```

### Lote 04 — Minuto 4 (escenas 19–24)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_04.png`

**Guardar 16:9 como:** `raw_clips/minute_04.mp4`

**Guardar 9:16 como:** `raw_clips/minute_04_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 19 (Viñeta #19 del Storyboard) — 03:00–03:10
- Location: Blackwell great room, dinner, night
- Characters Present: Elena Vance, Victoria Blackwell, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the candlelit great room, the mistress rises with a glass while the maid steps to the edge of the tables. Location: Blackwell great room, dinner, night. Key object: a dinner place card. Characters present: Elena Vance, Victoria Blackwell, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing black cashmere turtleneck, long grey riding coat, leather gloves); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing grey wool overcoat over the white shirt, silver cufflinks)
- Key Object: a dinner place card
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the candlelit great room, the mistress rises with a glass while the maid steps to the edge of the tables.
  * [03s–07s]: tight close-up — Close on the maid's face as every guest turns toward her.
  * [07s–10s]: tight close-up — Low angle on the maid as she answers the toast without dropping her gaze.
- Sound Design (SFX & Voice Tone): silverware on china, a glass set down, a room going quiet. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (sweet): "Elena leaves soon. Tell them your plans, dear."
  ELENA (polite): "She's kind. My plans haven't changed."

ESCENA 20 (Viñeta #20 del Storyboard) — 03:10–03:20
- Location: Blackwell gravel yard, night
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the gravel yard at night, a steel barrel burns as the mistress thrusts a folded paper at the maid. Location: Blackwell gravel yard, night. Key object: a signed release form. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing black cashmere turtleneck, long grey riding coat, leather gloves)
- Key Object: a signed release form
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the gravel yard at night, a steel barrel burns as the mistress thrusts a folded paper at the maid.
  * [03s–07s]: close-up — Insert: the old saddle's leather curling in the fire, stitching glowing before it blackens.
  * [07s–10s]: tight close-up — Close on the maid's face lit by fire; she does not step back.
- Sound Design (SFX & Voice Tone): fire roaring in a steel barrel, gravel under boots, a radio crackling in the sheriff's car. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (cold): "Sign by midnight, or I add arson."
  ELENA (steady): "You burned her saddle. You're afraid of it."

ESCENA 21 (Viñeta #21 del Storyboard) — 03:20–03:30
- Location: gatehouse cottage, night
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: In the cottage lamplight, the maid unrolls the old county survey map while the foreman anchors the curling corners with heavy iron horseshoes. Location: gatehouse cottage, night. Key object: a scraped parcel map. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing chore jacket with a broken zipper pull, leather work gloves)
- Key Object: a scraped parcel map
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the cottage lamplight, the maid unrolls the old county survey map while the foreman anchors the curling corners with heavy iron horseshoes.
  * [03s–07s]: close-up — Insert: a calloused finger traces the parcel boundary where the original boundary line was scraped off with a razor blade.
  * [07s–10s]: tight close-up — Close on the maid looking up from the map, determination sharpening her eyes.
- Sound Design (SFX & Voice Tone): kerosene lamp humming, wind whistling through window joints, heavy paper creaking. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; COLE — quiet, low American English, careful diction, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (urgent): "Someone scraped the original section line off with a blade."
  COLE (low): "That's Walter Blackwell's handwriting underneath."

ESCENA 22 (Viñeta #22 del Storyboard) — 03:30–03:40
- Location: Blackwell tack room, night
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the shadowy tack room, the maid kneels beside the wall timber and slides a cylindrical tin case from the hollow cavity. Location: Blackwell tack room, night. Key object: a stack of cash tax receipts. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt)
- Key Object: a stack of cash tax receipts
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the shadowy tack room, the maid kneels beside the wall timber and slides a cylindrical tin case from the hollow cavity.
  * [03s–07s]: close-up — Insert: the cap unscrews with a grinding squeak, revealing rolled bank tax receipts tied with red butcher twine.
  * [07s–10s]: tight close-up — Close on her face as flashlight beam illuminates the receipts bearing her mother's signature.
- Sound Design (SFX & Voice Tone): tin cap grinding, owls hooting in barn rafters, distant horse snorting softly. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (focused): "Every tax installment from 2005 to 2008. Paid in cash."

ESCENA 23 (Viñeta #23 del Storyboard) — 03:40–03:50
- Location: Silver Creek barn hayloft, night
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: In the moonlight, the foreman gently binds the maid's bruised palm with white tape, his touch slow and deliberate. Location: Silver Creek barn hayloft, night. Key object: a lantern in the hayloft. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing chore jacket with a broken zipper pull, leather work gloves)
- Key Object: a lantern in the hayloft
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the moonlight, the foreman gently binds the maid's bruised palm with white tape, his touch slow and deliberate.
  * [03s–07s]: tight close-up — Close on their intertwined hands as his thumb brushes over her calloused knuckles.
  * [07s–10s]: tight close-up — Over the foreman's broad shoulder, her eyes soften as she looks directly into his face.
- Sound Design (SFX & Voice Tone): dry hay rustling, cricket chirps, soft breathing, timber creaking in night breeze. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (warm): "You don't have to carry this alone."
  ELENA (quiet): "Everyone beside my mother paid for it."

ESCENA 24 (Viñeta #24 del Storyboard) — 03:50–04:00
- Location: Blackwell study archives, night
- Characters Present: Elena Vance, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: Behind the desk, the maid turns with the open ledger as the heir steps over the threshold. Location: Blackwell study archives, night. Key object: a ledger of quiet payments. Characters present: Elena Vance, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing white shirt with sleeves rolled, dark trousers)
- Key Object: a ledger of quiet payments
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Behind the desk, the maid turns with the open ledger as the heir steps over the threshold.
  * [03s–07s]: tight close-up — Close on the heir's eyes shifting down to the gold-stamped estate accounts ledger in her arms.
  * [07s–10s]: tight close-up — Over the maid's shoulder, the heir slowly reaches behind his back to shut the study door.
- Sound Design (SFX & Voice Tone): heavy oak door latching softly, clock pendulum ticking, distant dogs barking. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  RICHARD (low): "That book lists my father's quiet payments."
  ELENA (cold): "Payments to the coroner. She bought the certificate."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 19 (Viñeta #19 del Storyboard) — 03:00–03:10
- Location: Blackwell great room, dinner, night
- Characters Present: Elena Vance, Victoria Blackwell, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the candlelit great room, the mistress rises with a glass while the maid steps to the edge of the tables. Location: Blackwell great room, dinner, night. Key object: a dinner place card. Characters present: Elena Vance, Victoria Blackwell, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing black cashmere turtleneck, long grey riding coat, leather gloves); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing grey wool overcoat over the white shirt, silver cufflinks)
- Key Object: a dinner place card
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the candlelit great room, the mistress rises with a glass while the maid steps to the edge of the tables.
  * [03s–07s]: tight close-up — Close on the maid's face as every guest turns toward her.
  * [07s–10s]: tight close-up — Low angle on the maid as she answers the toast without dropping her gaze.
- Sound Design (SFX & Voice Tone): silverware on china, a glass set down, a room going quiet. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (sweet): "Elena leaves soon. Tell them your plans, dear."
  ELENA (polite): "She's kind. My plans haven't changed."

ESCENA 20 (Viñeta #20 del Storyboard) — 03:10–03:20
- Location: Blackwell gravel yard, night
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the gravel yard at night, a steel barrel burns as the mistress thrusts a folded paper at the maid. Location: Blackwell gravel yard, night. Key object: a signed release form. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing faded blue denim work shirt under a tan canvas barn coat, braid loosened by work); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing black cashmere turtleneck, long grey riding coat, leather gloves)
- Key Object: a signed release form
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the gravel yard at night, a steel barrel burns as the mistress thrusts a folded paper at the maid.
  * [03s–07s]: close-up — Insert: the old saddle's leather curling in the fire, stitching glowing before it blackens.
  * [07s–10s]: tight close-up — Close on the maid's face lit by fire; she does not step back.
- Sound Design (SFX & Voice Tone): fire roaring in a steel barrel, gravel under boots, a radio crackling in the sheriff's car. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (cold): "Sign by midnight, or I add arson."
  ELENA (steady): "You burned her saddle. You're afraid of it."

ESCENA 21 (Viñeta #21 del Storyboard) — 03:20–03:30
- Location: gatehouse cottage, night
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: In the cottage lamplight, the maid unrolls the old county survey map while the foreman anchors the curling corners with heavy iron horseshoes. Location: gatehouse cottage, night. Key object: a scraped parcel map. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing chore jacket with a broken zipper pull, leather work gloves)
- Key Object: a scraped parcel map
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the cottage lamplight, the maid unrolls the old county survey map while the foreman anchors the curling corners with heavy iron horseshoes.
  * [03s–07s]: close-up — Insert: a calloused finger traces the parcel boundary where the original boundary line was scraped off with a razor blade.
  * [07s–10s]: tight close-up — Close on the maid looking up from the map, determination sharpening her eyes.
- Sound Design (SFX & Voice Tone): kerosene lamp humming, wind whistling through window joints, heavy paper creaking. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; COLE — quiet, low American English, careful diction, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (urgent): "Someone scraped the original section line off with a blade."
  COLE (low): "That's Walter Blackwell's handwriting underneath."

ESCENA 22 (Viñeta #22 del Storyboard) — 03:30–03:40
- Location: Blackwell tack room, night
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the shadowy tack room, the maid kneels beside the wall timber and slides a cylindrical tin case from the hollow cavity. Location: Blackwell tack room, night. Key object: a stack of cash tax receipts. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt)
- Key Object: a stack of cash tax receipts
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the shadowy tack room, the maid kneels beside the wall timber and slides a cylindrical tin case from the hollow cavity.
  * [03s–07s]: close-up — Insert: the cap unscrews with a grinding squeak, revealing rolled bank tax receipts tied with red butcher twine.
  * [07s–10s]: tight close-up — Close on her face as flashlight beam illuminates the receipts bearing her mother's signature.
- Sound Design (SFX & Voice Tone): tin cap grinding, owls hooting in barn rafters, distant horse snorting softly. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (focused): "Every tax installment from 2005 to 2008. Paid in cash."

ESCENA 23 (Viñeta #23 del Storyboard) — 03:40–03:50
- Location: Silver Creek barn hayloft, night
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: In the moonlight, the foreman gently binds the maid's bruised palm with white tape, his touch slow and deliberate. Location: Silver Creek barn hayloft, night. Key object: a lantern in the hayloft. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing chore jacket with a broken zipper pull, leather work gloves)
- Key Object: a lantern in the hayloft
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the moonlight, the foreman gently binds the maid's bruised palm with white tape, his touch slow and deliberate.
  * [03s–07s]: tight close-up — Close on their intertwined hands as his thumb brushes over her calloused knuckles.
  * [07s–10s]: tight close-up — Over the foreman's broad shoulder, her eyes soften as she looks directly into his face.
- Sound Design (SFX & Voice Tone): dry hay rustling, cricket chirps, soft breathing, timber creaking in night breeze. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (warm): "You don't have to carry this alone."
  ELENA (quiet): "Everyone beside my mother paid for it."

ESCENA 24 (Viñeta #24 del Storyboard) — 03:50–04:00
- Location: Blackwell study archives, night
- Characters Present: Elena Vance, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: Behind the desk, the maid turns with the open ledger as the heir steps over the threshold. Location: Blackwell study archives, night. Key object: a ledger of quiet payments. Characters present: Elena Vance, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing white shirt with sleeves rolled, dark trousers)
- Key Object: a ledger of quiet payments
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Behind the desk, the maid turns with the open ledger as the heir steps over the threshold.
  * [03s–07s]: tight close-up — Close on the heir's eyes shifting down to the gold-stamped estate accounts ledger in her arms.
  * [07s–10s]: tight close-up — Over the maid's shoulder, the heir slowly reaches behind his back to shut the study door.
- Sound Design (SFX & Voice Tone): heavy oak door latching softly, clock pendulum ticking, distant dogs barking. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  RICHARD (low): "That book lists my father's quiet payments."
  ELENA (cold): "Payments to the coroner. She bought the certificate."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts."
```

### Lote 05 — Minuto 5 (escenas 25–30)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_05.png`

**Guardar 16:9 como:** `raw_clips/minute_05.mp4`

**Guardar 9:16 como:** `raw_clips/minute_05_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 25 (Viñeta #25 del Storyboard) — 04:00–04:10
- Location: Blackwell mansion great room, night
- Characters Present: Elena Vance, Victoria Blackwell, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the vast room, the mistress swings a small brass ribboned key while the maid backs toward the cold hearth. Location: Blackwell mansion great room, night. Key object: Walter's unsigned will. Characters present: Elena Vance, Victoria Blackwell, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing silver-grey silk blouse, charcoal skirt, single pearl strand); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing white shirt with sleeves rolled, dark trousers)
- Key Object: Walter's unsigned will
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the vast room, the mistress swings a small brass ribboned key while the maid backs toward the cold hearth.
  * [03s–07s]: tight close-up — Close on the mistress's painted red lips curling into an amused, predatory smile.
  * [07s–10s]: tight close-up — Low angle on the maid squaring her shoulders against the firelight's orange glow.
- Sound Design (SFX & Voice Tone): grandfather clock striking the quarter hour, embers crackling, wind buffeting glass. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (mocking): "Did you think Walter was a saint?"
  ELENA (fierce): "He gave her the ranch. You murdered him."

ESCENA 26 (Viñeta #26 del Storyboard) — 04:10–04:20
- Location: Blackwell mansion gravel drive, night
- Characters Present: Richard Blackwell, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: Under harsh halogen yard lights, the foreman plants his boots in front of the heir, refusing to yield the driveway. Location: Blackwell mansion gravel drive, night. Key object: a shotgun on the porch. Characters present: Richard Blackwell, Cole Barrett.
- Identity Anchors: Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing white shirt with sleeves rolled, dark trousers); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing chore jacket with a broken zipper pull, leather work gloves)
- Key Object: a shotgun on the porch
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Under harsh halogen yard lights, the foreman plants his boots in front of the heir, refusing to yield the driveway.
  * [03s–07s]: tight close-up — Close on the foreman's clenched fist at his side, knuckles white against the tan canvas.
  * [07s–10s]: tight close-up — Over the heir's shoulder, the foreman steps forward into the beam of light.
- Sound Design (SFX & Voice Tone): gravel shifting under heavy work boots, halogen floodlights buzzing, cold fog horn far off. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (hard): "One step toward the gatehouse, Richard."
  RICHARD (scornful): "You're throwing your life away for a girl."

ESCENA 27 (Viñeta #27 del Storyboard) — 04:20–04:30
- Location: gatehouse cottage porch, night
- Characters Present: Elena Vance, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: On the rain-slick porch steps, the heir reaches out with a cream envelope while the maid refuses to accept it. Location: gatehouse cottage porch, night. Key object: a threat written on a feed receipt. Characters present: Elena Vance, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing white shirt with sleeves rolled, dark trousers)
- Key Object: a threat written on a feed receipt
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — On the rain-slick porch steps, the heir reaches out with a cream envelope while the maid refuses to accept it.
  * [03s–07s]: close-up — Insert: the wet envelope bears the embossed gold seal of the county probate registry.
  * [07s–10s]: tight close-up — Close on the heir's eyes searching her face, genuine dread beneath his charm.
- Sound Design (SFX & Voice Tone): rain dripping from wooden eaves, porch boards creaking, distant thunder rumble. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  RICHARD (flat): "My mother hired two men from Billings."
  ELENA (defiant): "Tell them to bring shovels. I'm not running."

ESCENA 28 (Viñeta #28 del Storyboard) — 04:30–04:40
- Location: Silver Creek barn aisle, night
- Characters Present: Elena Vance, Maggie Doyle
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the barn aisle, the housekeeper rushes to the maid and grabs both of her elbows with trembling hands. Location: Silver Creek barn aisle, night. Key object: an empty wall safe. Characters present: Elena Vance, Maggie Doyle.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing beige cardigan under the wool shawl, apron gone)
- Key Object: an empty wall safe
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the barn aisle, the housekeeper rushes to the maid and grabs both of her elbows with trembling hands.
  * [03s–07s]: tight close-up — Close on the housekeeper's tear-streaked spectacles reflecting the amber glow of the hanging bulb.
  * [07s–10s]: tight close-up — Over the housekeeper's shoulder, the maid gently pulls her close to steady her shaking.
- Sound Design (SFX & Voice Tone): horses rustling nervous in stalls, wind howling through wall cracks, floor chains clinking. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  MAGGIE (urgent): "Victoria cleared the safe. She's leaving after the gala."
  ELENA (steady): "We have until midnight."

ESCENA 29 (Viñeta #29 del Storyboard) — 04:40–04:50
- Location: Blackwell estate gates, midnight
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: By the iron gates, the mistress steps out of the luxury car into the headlights, holding a checkbook open. Location: Blackwell estate gates, midnight. Key object: a suitcase full of cash. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing silver-grey silk blouse, charcoal skirt, single pearl strand)
- Key Object: a suitcase full of cash
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — By the iron gates, the mistress steps out of the luxury car into the headlights, holding a checkbook open.
  * [03s–07s]: tight close-up — Close on the cashier's draft: five hundred thousand dollars drawn on First Valley Bank.
  * [07s–10s]: tight close-up — Low angle on the maid standing in the glare of the car beams, unblinking in the gale.
- Sound Design (SFX & Voice Tone): car engine idling low, wind screaming through iron bars, headlights humming. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (reasonable): "Half a million. Buy any ranch you want."
  ELENA (cold): "I just call my mother a thief."

ESCENA 30 (Viñeta #30 del Storyboard) — 04:50–05:00
- Location: Blackwell estate gates, midnight
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: Under the headlights, the mistress thrusts the certified check into the maid's face like an execution order. Location: Blackwell estate gates, midnight. Key object: a final cash offer. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing silver-grey silk blouse, charcoal skirt, single pearl strand)
- Key Object: a final cash offer
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Under the headlights, the mistress thrusts the certified check into the maid's face like an execution order.
  * [03s–07s]: close-up — Insert: the maid's fingers close around the paper edge, lingering as if about to fold it.
  * [07s–10s]: tight close-up — Extreme close-up on the maid's eyes, blazing with an impossible choice as rain strikes her skin.
- Sound Design (SFX & Voice Tone): thunderclaps shaking the valley, heavy rain drumming car hood, paper ripping slightly in wind. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (final): "Take the money. Leave the name behind."
  ELENA (quiet): "My mother died for that name."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 25 (Viñeta #25 del Storyboard) — 04:00–04:10
- Location: Blackwell mansion great room, night
- Characters Present: Elena Vance, Victoria Blackwell, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the vast room, the mistress swings a small brass ribboned key while the maid backs toward the cold hearth. Location: Blackwell mansion great room, night. Key object: Walter's unsigned will. Characters present: Elena Vance, Victoria Blackwell, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing silver-grey silk blouse, charcoal skirt, single pearl strand); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing white shirt with sleeves rolled, dark trousers)
- Key Object: Walter's unsigned will
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the vast room, the mistress swings a small brass ribboned key while the maid backs toward the cold hearth.
  * [03s–07s]: tight close-up — Close on the mistress's painted red lips curling into an amused, predatory smile.
  * [07s–10s]: tight close-up — Low angle on the maid squaring her shoulders against the firelight's orange glow.
- Sound Design (SFX & Voice Tone): grandfather clock striking the quarter hour, embers crackling, wind buffeting glass. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (mocking): "Did you think Walter was a saint?"
  ELENA (fierce): "He gave her the ranch. You murdered him."

ESCENA 26 (Viñeta #26 del Storyboard) — 04:10–04:20
- Location: Blackwell mansion gravel drive, night
- Characters Present: Richard Blackwell, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: Under harsh halogen yard lights, the foreman plants his boots in front of the heir, refusing to yield the driveway. Location: Blackwell mansion gravel drive, night. Key object: a shotgun on the porch. Characters present: Richard Blackwell, Cole Barrett.
- Identity Anchors: Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing white shirt with sleeves rolled, dark trousers); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing chore jacket with a broken zipper pull, leather work gloves)
- Key Object: a shotgun on the porch
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Under harsh halogen yard lights, the foreman plants his boots in front of the heir, refusing to yield the driveway.
  * [03s–07s]: tight close-up — Close on the foreman's clenched fist at his side, knuckles white against the tan canvas.
  * [07s–10s]: tight close-up — Over the heir's shoulder, the foreman steps forward into the beam of light.
- Sound Design (SFX & Voice Tone): gravel shifting under heavy work boots, halogen floodlights buzzing, cold fog horn far off. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (hard): "One step toward the gatehouse, Richard."
  RICHARD (scornful): "You're throwing your life away for a girl."

ESCENA 27 (Viñeta #27 del Storyboard) — 04:20–04:30
- Location: gatehouse cottage porch, night
- Characters Present: Elena Vance, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: On the rain-slick porch steps, the heir reaches out with a cream envelope while the maid refuses to accept it. Location: gatehouse cottage porch, night. Key object: a threat written on a feed receipt. Characters present: Elena Vance, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing white shirt with sleeves rolled, dark trousers)
- Key Object: a threat written on a feed receipt
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — On the rain-slick porch steps, the heir reaches out with a cream envelope while the maid refuses to accept it.
  * [03s–07s]: close-up — Insert: the wet envelope bears the embossed gold seal of the county probate registry.
  * [07s–10s]: tight close-up — Close on the heir's eyes searching her face, genuine dread beneath his charm.
- Sound Design (SFX & Voice Tone): rain dripping from wooden eaves, porch boards creaking, distant thunder rumble. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  RICHARD (flat): "My mother hired two men from Billings."
  ELENA (defiant): "Tell them to bring shovels. I'm not running."

ESCENA 28 (Viñeta #28 del Storyboard) — 04:30–04:40
- Location: Silver Creek barn aisle, night
- Characters Present: Elena Vance, Maggie Doyle
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the barn aisle, the housekeeper rushes to the maid and grabs both of her elbows with trembling hands. Location: Silver Creek barn aisle, night. Key object: an empty wall safe. Characters present: Elena Vance, Maggie Doyle.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing beige cardigan under the wool shawl, apron gone)
- Key Object: an empty wall safe
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the barn aisle, the housekeeper rushes to the maid and grabs both of her elbows with trembling hands.
  * [03s–07s]: tight close-up — Close on the housekeeper's tear-streaked spectacles reflecting the amber glow of the hanging bulb.
  * [07s–10s]: tight close-up — Over the housekeeper's shoulder, the maid gently pulls her close to steady her shaking.
- Sound Design (SFX & Voice Tone): horses rustling nervous in stalls, wind howling through wall cracks, floor chains clinking. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  MAGGIE (urgent): "Victoria cleared the safe. She's leaving after the gala."
  ELENA (steady): "We have until midnight."

ESCENA 29 (Viñeta #29 del Storyboard) — 04:40–04:50
- Location: Blackwell estate gates, midnight
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: By the iron gates, the mistress steps out of the luxury car into the headlights, holding a checkbook open. Location: Blackwell estate gates, midnight. Key object: a suitcase full of cash. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing silver-grey silk blouse, charcoal skirt, single pearl strand)
- Key Object: a suitcase full of cash
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — By the iron gates, the mistress steps out of the luxury car into the headlights, holding a checkbook open.
  * [03s–07s]: tight close-up — Close on the cashier's draft: five hundred thousand dollars drawn on First Valley Bank.
  * [07s–10s]: tight close-up — Low angle on the maid standing in the glare of the car beams, unblinking in the gale.
- Sound Design (SFX & Voice Tone): car engine idling low, wind screaming through iron bars, headlights humming. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (reasonable): "Half a million. Buy any ranch you want."
  ELENA (cold): "I just call my mother a thief."

ESCENA 30 (Viñeta #30 del Storyboard) — 04:50–05:00
- Location: Blackwell estate gates, midnight
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: Under the headlights, the mistress thrusts the certified check into the maid's face like an execution order. Location: Blackwell estate gates, midnight. Key object: a final cash offer. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt with rolled sleeves, dark riding jeans, leather work gloves tucked in the belt); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing silver-grey silk blouse, charcoal skirt, single pearl strand)
- Key Object: a final cash offer
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Under the headlights, the mistress thrusts the certified check into the maid's face like an execution order.
  * [03s–07s]: close-up — Insert: the maid's fingers close around the paper edge, lingering as if about to fold it.
  * [07s–10s]: tight close-up — Extreme close-up on the maid's eyes, blazing with an impossible choice as rain strikes her skin.
- Sound Design (SFX & Voice Tone): thunderclaps shaking the valley, heavy rain drumming car hood, paper ripping slightly in wind. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (final): "Take the money. Leave the name behind."
  ELENA (quiet): "My mother died for that name."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts."
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
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot: Inside the ransacked cottage, the storm sweeps through shattered windows, scattering torn clothes and broken crockery across wet stones. Location: gatehouse cottage, storm night. Key object: a broken floorboard. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain)
- Key Object: a broken floorboard
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — Inside the ransacked cottage, the storm sweeps through shattered windows, scattering torn clothes and broken crockery across wet stones.
  * [03s–07s]: tight close-up — Close on the maid's boots stepping through broken glass as rain drips from her soaked chin.
  * [07s–10s]: tight close-up — She kneels in the center of the wreckage, her hands feeling frantically beneath a loose hearthstone.
- Sound Design (SFX & Voice Tone): gale force winds howl through glass shards, torrents of rain hitting stone floor, thunder. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (shaking): "They took the tin box and the original deed."
  ELENA (broken): "They took everything."

ESCENA 32 (Viñeta #32 del Storyboard) — 05:10–05:20
- Location: gatehouse cottage yard, storm night
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the swirling red and blue emergency light, the maid runs to the padlocked gate as rain washes mud over her boots. Location: gatehouse cottage yard, storm night. Key object: an eviction notice. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain)
- Key Object: an eviction notice
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the swirling red and blue emergency light, the maid runs to the padlocked gate as rain washes mud over her boots.
  * [03s–07s]: close-up — Insert: a laminated county eviction warrant stapled to the post: 'Immediate Vacate — Trespassing Order'.
  * [07s–10s]: tight close-up — Close on her wet face illuminated by strobe flashes, defiant rage replacing fear.
- Sound Design (SFX & Voice Tone): police cruiser siren chirping, heavy rain squall, chain links rattling against timber post. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (raw): "Drummond signed an eviction without a hearing."
  ELENA (defiant): "Victoria bought the county, not me."

ESCENA 33 (Viñeta #33 del Storyboard) — 05:20–05:30
- Location: Silver Creek hay shed, storm night
- Characters Present: Elena Vance, Maggie Doyle
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: In the drafty shelter, the maid wraps her own dry flannel scarf around the weeping housekeeper's neck. Location: Silver Creek hay shed, storm night. Key object: a nursing-home bill. Characters present: Elena Vance, Maggie Doyle.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing wool shawl against the storm, glasses fogged, small travel bag)
- Key Object: a nursing-home bill
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the drafty shelter, the maid wraps her own dry flannel scarf around the weeping housekeeper's neck.
  * [03s–07s]: tight close-up — Close on the housekeeper's trembling chin as she clasps Elena's wet wrists with both hands.
  * [07s–10s]: tight close-up — Over the maid's shoulder, the older woman looks up with fifteen years of buried grief.
- Sound Design (SFX & Voice Tone): rain thundering deafeningly on corrugated iron roof, gusting wind, weeping breath. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  MAGGIE (ashamed): "She threatened my sister's care in Helena."
  ELENA (gentle): "You kept your family alive. Help me finish."

ESCENA 34 (Viñeta #34 del Storyboard) — 05:30–05:40
- Location: Blackwell mansion rear terrace, storm night
- Characters Present: Victoria Blackwell, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: Inside the glowing library, the mistress feeds the ancient deed into the fireplace flames while rain streaks the window. Location: Blackwell mansion rear terrace, storm night. Key object: a burned deed in the fireplace. Characters present: Victoria Blackwell, Richard Blackwell.
- Identity Anchors: Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing black cashmere sweater, thin diamond bracelet, hair set perfectly despite the storm); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing dark rain jacket over the white shirt, collar up against the storm)
- Key Object: a burned deed in the fireplace
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Inside the glowing library, the mistress feeds the ancient deed into the fireplace flames while rain streaks the window.
  * [03s–07s]: close-up — Insert: the wax seal on June Vance's deed melts into blackened bubbles in the fire.
  * [07s–10s]: tight close-up — Close on the heir turning away from the fireplace, draining his amber glass in one swallow.
- Sound Design (SFX & Voice Tone): fireplace flames roaring, rain drumming on terrace panes, crystal glass setting down. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (satisfied): "No deed, no contract, no claim."
  RICHARD (quiet): "You burned the paper, not what Walter hid."

ESCENA 35 (Viñeta #35 del Storyboard) — 05:40–05:50
- Location: Silver Creek stable tack room, storm night
- Characters Present: Elena Vance, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In a sudden flash of lightning, the maid appears like a ghost in the stable door, blocking the heir's retreat. Location: Silver Creek stable tack room, storm night. Key object: a safe-deposit box key. Characters present: Elena Vance, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing dark rain jacket over the white shirt, collar up against the storm)
- Key Object: a safe-deposit box key
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In a sudden flash of lightning, the maid appears like a ghost in the stable door, blocking the heir's retreat.
  * [03s–07s]: tight close-up — Close on the heir stumbling backward against a stall door, dropping his car keys onto the straw.
  * [07s–10s]: tight close-up — Over the maid's shoulder, she steps forward and steps firmly onto his dropped keys.
- Sound Design (SFX & Voice Tone): thunderclap echoing in barn rafters, straw crunching underfoot, keys jangling on wood. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (sharp): "What did your father put in the vault?"
  RICHARD (low): "Box 14. The original will."

ESCENA 36 (Viñeta #36 del Storyboard) — 05:50–06:00
- Location: ranch ridge overlook, storm dawn
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot: On the high ridge, the maid walks into frame against the vast Montana valley as dawn breaks slate grey. Location: ranch ridge overlook, storm dawn. Key object: a handful of red Montana dirt. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain)
- Key Object: a handful of red Montana dirt
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — On the high ridge, the maid walks into frame against the vast Montana valley as dawn breaks slate grey.
  * [03s–07s]: tight close-up — Close on her wet face, eyes stinging with salt and cold wind, but chin jutting forward in stubborn pride.
  * [07s–10s]: tight close-up — Low angle from the rocks below, framing her towering against the gathering dawn light.
- Sound Design (SFX & Voice Tone): gale wind howling over mountain crest, distant hawk cry, thunder rolling away into hills. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (tired): "They took the house and burned the deed."
  ELENA (fierce): "But this dirt remembers her sweat."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 31 (Viñeta #31 del Storyboard) — 05:00–05:10
- Location: gatehouse cottage, storm night
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot: Inside the ransacked cottage, the storm sweeps through shattered windows, scattering torn clothes and broken crockery across wet stones. Location: gatehouse cottage, storm night. Key object: a broken floorboard. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain)
- Key Object: a broken floorboard
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — Inside the ransacked cottage, the storm sweeps through shattered windows, scattering torn clothes and broken crockery across wet stones.
  * [03s–07s]: tight close-up — Close on the maid's boots stepping through broken glass as rain drips from her soaked chin.
  * [07s–10s]: tight close-up — She kneels in the center of the wreckage, her hands feeling frantically beneath a loose hearthstone.
- Sound Design (SFX & Voice Tone): gale force winds howl through glass shards, torrents of rain hitting stone floor, thunder. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (shaking): "They took the tin box and the original deed."
  ELENA (broken): "They took everything."

ESCENA 32 (Viñeta #32 del Storyboard) — 05:10–05:20
- Location: gatehouse cottage yard, storm night
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the swirling red and blue emergency light, the maid runs to the padlocked gate as rain washes mud over her boots. Location: gatehouse cottage yard, storm night. Key object: an eviction notice. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain)
- Key Object: an eviction notice
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the swirling red and blue emergency light, the maid runs to the padlocked gate as rain washes mud over her boots.
  * [03s–07s]: close-up — Insert: a laminated county eviction warrant stapled to the post: 'Immediate Vacate — Trespassing Order'.
  * [07s–10s]: tight close-up — Close on her wet face illuminated by strobe flashes, defiant rage replacing fear.
- Sound Design (SFX & Voice Tone): police cruiser siren chirping, heavy rain squall, chain links rattling against timber post. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (raw): "Drummond signed an eviction without a hearing."
  ELENA (defiant): "Victoria bought the county, not me."

ESCENA 33 (Viñeta #33 del Storyboard) — 05:20–05:30
- Location: Silver Creek hay shed, storm night
- Characters Present: Elena Vance, Maggie Doyle
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: In the drafty shelter, the maid wraps her own dry flannel scarf around the weeping housekeeper's neck. Location: Silver Creek hay shed, storm night. Key object: a nursing-home bill. Characters present: Elena Vance, Maggie Doyle.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing wool shawl against the storm, glasses fogged, small travel bag)
- Key Object: a nursing-home bill
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the drafty shelter, the maid wraps her own dry flannel scarf around the weeping housekeeper's neck.
  * [03s–07s]: tight close-up — Close on the housekeeper's trembling chin as she clasps Elena's wet wrists with both hands.
  * [07s–10s]: tight close-up — Over the maid's shoulder, the older woman looks up with fifteen years of buried grief.
- Sound Design (SFX & Voice Tone): rain thundering deafeningly on corrugated iron roof, gusting wind, weeping breath. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  MAGGIE (ashamed): "She threatened my sister's care in Helena."
  ELENA (gentle): "You kept your family alive. Help me finish."

ESCENA 34 (Viñeta #34 del Storyboard) — 05:30–05:40
- Location: Blackwell mansion rear terrace, storm night
- Characters Present: Victoria Blackwell, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: Inside the glowing library, the mistress feeds the ancient deed into the fireplace flames while rain streaks the window. Location: Blackwell mansion rear terrace, storm night. Key object: a burned deed in the fireplace. Characters present: Victoria Blackwell, Richard Blackwell.
- Identity Anchors: Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing black cashmere sweater, thin diamond bracelet, hair set perfectly despite the storm); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing dark rain jacket over the white shirt, collar up against the storm)
- Key Object: a burned deed in the fireplace
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Inside the glowing library, the mistress feeds the ancient deed into the fireplace flames while rain streaks the window.
  * [03s–07s]: close-up — Insert: the wax seal on June Vance's deed melts into blackened bubbles in the fire.
  * [07s–10s]: tight close-up — Close on the heir turning away from the fireplace, draining his amber glass in one swallow.
- Sound Design (SFX & Voice Tone): fireplace flames roaring, rain drumming on terrace panes, crystal glass setting down. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (satisfied): "No deed, no contract, no claim."
  RICHARD (quiet): "You burned the paper, not what Walter hid."

ESCENA 35 (Viñeta #35 del Storyboard) — 05:40–05:50
- Location: Silver Creek stable tack room, storm night
- Characters Present: Elena Vance, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In a sudden flash of lightning, the maid appears like a ghost in the stable door, blocking the heir's retreat. Location: Silver Creek stable tack room, storm night. Key object: a safe-deposit box key. Characters present: Elena Vance, Richard Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing dark rain jacket over the white shirt, collar up against the storm)
- Key Object: a safe-deposit box key
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In a sudden flash of lightning, the maid appears like a ghost in the stable door, blocking the heir's retreat.
  * [03s–07s]: tight close-up — Close on the heir stumbling backward against a stall door, dropping his car keys onto the straw.
  * [07s–10s]: tight close-up — Over the maid's shoulder, she steps forward and steps firmly onto his dropped keys.
- Sound Design (SFX & Voice Tone): thunderclap echoing in barn rafters, straw crunching underfoot, keys jangling on wood. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (sharp): "What did your father put in the vault?"
  RICHARD (low): "Box 14. The original will."

ESCENA 36 (Viñeta #36 del Storyboard) — 05:50–06:00
- Location: ranch ridge overlook, storm dawn
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot: On the high ridge, the maid walks into frame against the vast Montana valley as dawn breaks slate grey. Location: ranch ridge overlook, storm dawn. Key object: a handful of red Montana dirt. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain)
- Key Object: a handful of red Montana dirt
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — On the high ridge, the maid walks into frame against the vast Montana valley as dawn breaks slate grey.
  * [03s–07s]: tight close-up — Close on her wet face, eyes stinging with salt and cold wind, but chin jutting forward in stubborn pride.
  * [07s–10s]: tight close-up — Low angle from the rocks below, framing her towering against the gathering dawn light.
- Sound Design (SFX & Voice Tone): gale wind howling over mountain crest, distant hawk cry, thunder rolling away into hills. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (tired): "They took the house and burned the deed."
  ELENA (fierce): "But this dirt remembers her sweat."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts."
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
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: On the muddy road, the foreman wraps his dry wool jacket around her, pulling the collar up against the wind. Location: ranch ridge road, dawn. Key object: a truck key and gas can. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing soaked canvas jacket, grey henley underneath, no hat)
- Key Object: a truck key and gas can
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — On the muddy road, the foreman wraps his dry wool jacket around her, pulling the collar up against the wind.
  * [03s–07s]: tight close-up — Close on his calloused hand lingering at the lapel, steadying her trembling frame.
  * [07s–10s]: tight close-up — Over the maid's shoulder, the foreman looks straight down the mountain toward town.
- Sound Design (SFX & Voice Tone): diesel truck engine rumbling steady, windshield wipers clicking, wind whistling through pines. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (urgent): "The bank opens in two hours."
  ELENA (wary): "Victoria will have the sheriff arrest us."

ESCENA 38 (Viñeta #38 del Storyboard) — 06:10–06:20
- Location: ranch ridge road, green truck cab, dawn
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: Inside the bouncing truck cab, the maid turns the brass key in the dashboard light, scraping away years of verdigris. Location: ranch ridge road, green truck cab, dawn. Key object: a brass bank key stamped FVT 14. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing soaked canvas jacket, grey henley underneath, no hat)
- Key Object: a brass bank key stamped FVT 14
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Inside the bouncing truck cab, the maid turns the brass key in the dashboard light, scraping away years of verdigris.
  * [03s–07s]: close-up — Insert: under the brass patina, tiny stamped numerals read: 'FVT — 14'.
  * [07s–10s]: tight close-up — Close on her lips parting as the final realization clicks into place.
- Sound Design (SFX & Voice Tone): truck tires humming on wet highway, heater blower whirring, key clicking against metal coin tray. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; COLE — quiet, low American English, careful diction, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (realizing): "FVT fourteen. This was never a saddle key."
  COLE (low): "It's Walter's private vault key."

ESCENA 39 (Viñeta #39 del Storyboard) — 06:20–06:30
- Location: town bank exterior, morning
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: On the bank steps, the maid and foreman turn together as the limousine door opens across the street. Location: town bank exterior, morning. Key object: the bank vault door. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing soaked canvas jacket, grey henley underneath, no hat)
- Key Object: the bank vault door
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — On the bank steps, the maid and foreman turn together as the limousine door opens across the street.
  * [03s–07s]: over-the-shoulder shot — Over the maid's shoulder, Victoria steps out in her emerald gala dress, accompanied by Sheriff Drummond.
  * [07s–10s]: tight close-up — Close on the maid slipping the brass key into her fist and bounding up the bank steps.
- Sound Design (SFX & Voice Tone): town church bell tolling nine, limousine door slamming, boots racing up granite stairs. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (urgent): "Victoria's here with Drummond."
  ELENA (fast): "Hold Drummond on the steps for sixty seconds."

ESCENA 40 (Viñeta #40 del Storyboard) — 06:30–06:40
- Location: First Valley Trust vault corridor, morning
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: Inside the gleaming vault, the maid turns the brass key into Lock 14; the heavy tumbler clicks open with a hollow ring. Location: First Valley Trust vault corridor, morning. Key object: Walter's certified will. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain)
- Key Object: Walter's certified will
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Inside the gleaming vault, the maid turns the brass key into Lock 14; the heavy tumbler clicks open with a hollow ring.
  * [03s–07s]: close-up — Insert: the long metal deposit box slides out, containing a blue ribboned document: 'Last Will and Testament of Walter Blackwell'.
  * [07s–10s]: tight close-up — Close on her eyes widening in profound shock as she reads the bold heading across the parchment.
- Sound Design (SFX & Voice Tone): heavy steel tumbler clunking open, metal drawer sliding on runners, fluorescent bulb hum. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (hushed): "The key was never for a door."
  ELENA (stunned): "The first page leaves Silver Creek to me."

ESCENA 41 (Viñeta #41 del Storyboard) — 06:40–06:50
- Location: First Valley Trust manager office, morning
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the sunlit bank office, the maid steps up to the desk as the grey-haired bank manager lifts the embossed blue notary seal to his bifocals. Location: First Valley Trust manager office, morning. Key object: a notary seal. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat)
- Key Object: a notary seal
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the sunlit bank office, the maid steps up to the desk as the grey-haired bank manager lifts the embossed blue notary seal to his bifocals.
  * [03s–07s]: close-up — Insert: the manager's heavy gold signet embosser stamps 'CERTIFIED ORIGINAL COPY — FIRST VALLEY TRUST' across the parchment.
  * [07s–10s]: tight close-up — Close on the maid's face as the heavy brass stamp thuds down, her breath releasing in steady relief.
- Sound Design (SFX & Voice Tone): heavy brass seal clunking on paper, ticking grandfather clock, muffled street traffic outside. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (urgent): "Is the notary seal intact?"
  ELENA (stunned): "It's valid. Walter deposited it himself."

ESCENA 42 (Viñeta #42 del Storyboard) — 06:50–07:00
- Location: town bank steps, morning
- Characters Present: Victoria Blackwell, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: On the stone steps, the foreman plants himself between the mistress and the bank doors as the sheriff steps forward. Location: town bank steps, morning. Key object: a bank payroll ledger. Characters present: Victoria Blackwell, Cole Barrett.
- Identity Anchors: Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing clean denim jacket over the grey henley, hat brushed for once)
- Key Object: a bank payroll ledger
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — On the stone steps, the foreman plants himself between the mistress and the bank doors as the sheriff steps forward.
  * [03s–07s]: tight close-up — Close on the mistress's furious eyes narrowing beneath her sleek platinum bob.
  * [07s–10s]: tight close-up — Over the foreman's shoulder, the bank double doors click open behind him.
- Sound Design (SFX & Voice Tone): heavy brass door latch clicking open, morning wind rustling dry leaves on stone, town murmurs. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; COLE — quiet, low American English, careful diction, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (cold): "Step aside, Cole. You're on my payroll."
  COLE (steady): "I work for Silver Creek's real owner now."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 37 (Viñeta #37 del Storyboard) — 06:00–06:10
- Location: ranch ridge road, dawn
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: On the muddy road, the foreman wraps his dry wool jacket around her, pulling the collar up against the wind. Location: ranch ridge road, dawn. Key object: a truck key and gas can. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing soaked canvas jacket, grey henley underneath, no hat)
- Key Object: a truck key and gas can
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — On the muddy road, the foreman wraps his dry wool jacket around her, pulling the collar up against the wind.
  * [03s–07s]: tight close-up — Close on his calloused hand lingering at the lapel, steadying her trembling frame.
  * [07s–10s]: tight close-up — Over the maid's shoulder, the foreman looks straight down the mountain toward town.
- Sound Design (SFX & Voice Tone): diesel truck engine rumbling steady, windshield wipers clicking, wind whistling through pines. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (urgent): "The bank opens in two hours."
  ELENA (wary): "Victoria will have the sheriff arrest us."

ESCENA 38 (Viñeta #38 del Storyboard) — 06:10–06:20
- Location: ranch ridge road, green truck cab, dawn
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: Inside the bouncing truck cab, the maid turns the brass key in the dashboard light, scraping away years of verdigris. Location: ranch ridge road, green truck cab, dawn. Key object: a brass bank key stamped FVT 14. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing soaked canvas jacket, grey henley underneath, no hat)
- Key Object: a brass bank key stamped FVT 14
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Inside the bouncing truck cab, the maid turns the brass key in the dashboard light, scraping away years of verdigris.
  * [03s–07s]: close-up — Insert: under the brass patina, tiny stamped numerals read: 'FVT — 14'.
  * [07s–10s]: tight close-up — Close on her lips parting as the final realization clicks into place.
- Sound Design (SFX & Voice Tone): truck tires humming on wet highway, heater blower whirring, key clicking against metal coin tray. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; COLE — quiet, low American English, careful diction, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (realizing): "FVT fourteen. This was never a saddle key."
  COLE (low): "It's Walter's private vault key."

ESCENA 39 (Viñeta #39 del Storyboard) — 06:20–06:30
- Location: town bank exterior, morning
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: On the bank steps, the maid and foreman turn together as the limousine door opens across the street. Location: town bank exterior, morning. Key object: the bank vault door. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing soaked canvas jacket, grey henley underneath, no hat)
- Key Object: the bank vault door
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — On the bank steps, the maid and foreman turn together as the limousine door opens across the street.
  * [03s–07s]: over-the-shoulder shot — Over the maid's shoulder, Victoria steps out in her emerald gala dress, accompanied by Sheriff Drummond.
  * [07s–10s]: tight close-up — Close on the maid slipping the brass key into her fist and bounding up the bank steps.
- Sound Design (SFX & Voice Tone): town church bell tolling nine, limousine door slamming, boots racing up granite stairs. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (urgent): "Victoria's here with Drummond."
  ELENA (fast): "Hold Drummond on the steps for sixty seconds."

ESCENA 40 (Viñeta #40 del Storyboard) — 06:30–06:40
- Location: First Valley Trust vault corridor, morning
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: Inside the gleaming vault, the maid turns the brass key into Lock 14; the heavy tumbler clicks open with a hollow ring. Location: First Valley Trust vault corridor, morning. Key object: Walter's certified will. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing denim work shirt under a charcoal storm coat, hair wet from rain)
- Key Object: Walter's certified will
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Inside the gleaming vault, the maid turns the brass key into Lock 14; the heavy tumbler clicks open with a hollow ring.
  * [03s–07s]: close-up — Insert: the long metal deposit box slides out, containing a blue ribboned document: 'Last Will and Testament of Walter Blackwell'.
  * [07s–10s]: tight close-up — Close on her eyes widening in profound shock as she reads the bold heading across the parchment.
- Sound Design (SFX & Voice Tone): heavy steel tumbler clunking open, metal drawer sliding on runners, fluorescent bulb hum. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (hushed): "The key was never for a door."
  ELENA (stunned): "The first page leaves Silver Creek to me."

ESCENA 41 (Viñeta #41 del Storyboard) — 06:40–06:50
- Location: First Valley Trust manager office, morning
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the sunlit bank office, the maid steps up to the desk as the grey-haired bank manager lifts the embossed blue notary seal to his bifocals. Location: First Valley Trust manager office, morning. Key object: a notary seal. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat)
- Key Object: a notary seal
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the sunlit bank office, the maid steps up to the desk as the grey-haired bank manager lifts the embossed blue notary seal to his bifocals.
  * [03s–07s]: close-up — Insert: the manager's heavy gold signet embosser stamps 'CERTIFIED ORIGINAL COPY — FIRST VALLEY TRUST' across the parchment.
  * [07s–10s]: tight close-up — Close on the maid's face as the heavy brass stamp thuds down, her breath releasing in steady relief.
- Sound Design (SFX & Voice Tone): heavy brass seal clunking on paper, ticking grandfather clock, muffled street traffic outside. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (urgent): "Is the notary seal intact?"
  ELENA (stunned): "It's valid. Walter deposited it himself."

ESCENA 42 (Viñeta #42 del Storyboard) — 06:50–07:00
- Location: town bank steps, morning
- Characters Present: Victoria Blackwell, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: On the stone steps, the foreman plants himself between the mistress and the bank doors as the sheriff steps forward. Location: town bank steps, morning. Key object: a bank payroll ledger. Characters present: Victoria Blackwell, Cole Barrett.
- Identity Anchors: Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing clean denim jacket over the grey henley, hat brushed for once)
- Key Object: a bank payroll ledger
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — On the stone steps, the foreman plants himself between the mistress and the bank doors as the sheriff steps forward.
  * [03s–07s]: tight close-up — Close on the mistress's furious eyes narrowing beneath her sleek platinum bob.
  * [07s–10s]: tight close-up — Over the foreman's shoulder, the bank double doors click open behind him.
- Sound Design (SFX & Voice Tone): heavy brass door latch clicking open, morning wind rustling dry leaves on stone, town murmurs. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; COLE — quiet, low American English, careful diction, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (cold): "Step aside, Cole. You're on my payroll."
  COLE (steady): "I work for Silver Creek's real owner now."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts."
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
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: The maid emerges onto the sunlit steps, lifting the stamped court-certified envelope for the entire sidewalk to see. Location: town bank steps, morning. Key object: a court filing stamp. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings)
- Key Object: a court filing stamp
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — The maid emerges onto the sunlit steps, lifting the stamped court-certified envelope for the entire sidewalk to see.
  * [03s–07s]: tight close-up — Close on the mistress's painted smile slipping, raw panic flashing behind her eyes for the first time.
  * [07s–10s]: tight close-up — Low angle on the maid looking down from the granite steps with quiet authority.
- Sound Design (SFX & Voice Tone): onlookers murmuring on sidewalk, pigeon wings flapping, wind snapping county banners. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (calm): "You said she had no standing. This will differs."
  VICTORIA (sharp): "That paper is an obsolete draft."

ESCENA 44 (Viñeta #44 del Storyboard) — 07:10–07:20
- Location: Blackwell town car, morning
- Characters Present: Victoria Blackwell, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: Inside the town car, the mistress grabs her son's lapel as he pulls himself back against the passenger door. Location: Blackwell town car, morning. Key object: a perjury statement. Characters present: Victoria Blackwell, Richard Blackwell.
- Identity Anchors: Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing black suit for the gala, sharp lapels, slicked hair)
- Key Object: a perjury statement
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Inside the town car, the mistress grabs her son's lapel as he pulls himself back against the passenger door.
  * [03s–07s]: tight close-up — Close on the heir unfastening her gloved fingers from his jacket with quiet distaste.
  * [07s–10s]: tight close-up — Over the mistress's shoulder, the heir stares out at the courthouse steps.
- Sound Design (SFX & Voice Tone): muffled car interior hush, rain starting to tap car glass, engine ticking as it idles. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (cold): "Tell the judge the will was stolen."
  RICHARD (firm): "Father was never demented. I won't perjure myself."

ESCENA 45 (Viñeta #45 del Storyboard) — 07:20–07:30
- Location: county civic hall back alley, noon
- Characters Present: Elena Vance, Cole Barrett, Maggie Doyle
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the brick alleyway, the housekeeper presses an aged leather journal into the maid's hands, tears in her eyes. Location: county civic hall back alley, noon. Key object: a fire log with a check number. Characters present: Elena Vance, Cole Barrett, Maggie Doyle.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing clean denim jacket over the grey henley, hat brushed for once); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing best Sunday cardigan, the apron folded neatly on a chair)
- Key Object: a fire log with a check number
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the brick alleyway, the housekeeper presses an aged leather journal into the maid's hands, tears in her eyes.
  * [03s–07s]: close-up — Insert: the journal page opens to October 12, 2008: 'Paid Sheriff Drummond $10,000 to classify barn fire as accidental'.
  * [07s–10s]: tight close-up — Close on the housekeeper whispering her final truth as she holds Elena's fingers tight.
- Sound Design (SFX & Voice Tone): water dripping from fire escape iron, muffled brass band tuning inside civic hall, distant crowd chatter. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  MAGGIE (urgent): "Walter kept this log. The check is here."
  ELENA (grateful): "This proves arson. You saved her honor."

ESCENA 46 (Viñeta #46 del Storyboard) — 07:30–07:40
- Location: Silver Creek civic hall foyer, afternoon
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: Before the towering carved oak doors, the maid walks up and adjusts her mother's silver belt buckle. Location: Silver Creek civic hall foyer, afternoon. Key object: a gala invitation. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing clean denim jacket over the grey henley, hat brushed for once)
- Key Object: a gala invitation
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Before the towering carved oak doors, the maid walks up and adjusts her mother's silver belt buckle.
  * [03s–07s]: tight close-up — Close on the foreman reaching out, adjusting the collar of her white shirt with quiet tenderness.
  * [07s–10s]: tight close-up — Low angle as the maid places her hand on the brass door handle and pushes both doors open.
- Sound Design (SFX & Voice Tone): crystal chandelier hum, ballroom orchestra playing light waltz, heavy oak doors swinging wide. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (low): "Every rancher and judge is here."
  ELENA (resolved): "Good. They should know who fed their horses."

ESCENA 47 (Viñeta #47 del Storyboard) — 07:40–07:50
- Location: civic hall grand ballroom, afternoon
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot: The grand ballroom falls utterly silent as the ranch maid in her simple white shirt strides down the red carpet toward the stage. Location: civic hall grand ballroom, afternoon. Key object: an auction catalog. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings)
- Key Object: an auction catalog
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — The grand ballroom falls utterly silent as the ranch maid in her simple white shirt strides down the red carpet toward the stage.
  * [03s–07s]: tight close-up — Close on the mistress's hand tightening around the podium microphone until her diamond ring clicks against the steel.
  * [07s–10s]: tight close-up — Over the maid's shoulder, she ascends the three wooden stage stairs without breaking stride.
- Sound Design (SFX & Voice Tone): champagne glasses clinking nervously, ballroom murmur rising, microphone feedback whine. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (cold): "Security, remove her. This is a private gala."
  ELENA (calm): "You're auctioning land you don't own."

ESCENA 48 (Viñeta #48 del Storyboard) — 07:50–08:00
- Location: civic hall auction stage, afternoon
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: Under the blinding stage lights, the mistress steps right into the maid's face, abandoning all high-society poise. Location: civic hall auction stage, afternoon. Key object: a gavel on the auction block. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings)
- Key Object: a gavel on the auction block
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Under the blinding stage lights, the mistress steps right into the maid's face, abandoning all high-society poise.
  * [03s–07s]: tight close-up — Extreme close-up on the mistress's twisted expression as she speaks directly into Elena's ear.
  * [07s–10s]: insert shot of the evidence object — Insert: Elena lays Walter's blue-sealed will onto the auctioneer's reading desk.
- Sound Design (SFX & Voice Tone): dramatic crowd gasps echoing in high hall, spotlight hum, microphone catching ragged breaths. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (mocking): "You are a stable rat playing dress-up."
  ELENA (quiet): "It was never yours. You warmed the chair."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 43 (Viñeta #43 del Storyboard) — 07:00–07:10
- Location: town bank steps, morning
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: The maid emerges onto the sunlit steps, lifting the stamped court-certified envelope for the entire sidewalk to see. Location: town bank steps, morning. Key object: a court filing stamp. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings)
- Key Object: a court filing stamp
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — The maid emerges onto the sunlit steps, lifting the stamped court-certified envelope for the entire sidewalk to see.
  * [03s–07s]: tight close-up — Close on the mistress's painted smile slipping, raw panic flashing behind her eyes for the first time.
  * [07s–10s]: tight close-up — Low angle on the maid looking down from the granite steps with quiet authority.
- Sound Design (SFX & Voice Tone): onlookers murmuring on sidewalk, pigeon wings flapping, wind snapping county banners. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical; VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (calm): "You said she had no standing. This will differs."
  VICTORIA (sharp): "That paper is an obsolete draft."

ESCENA 44 (Viñeta #44 del Storyboard) — 07:10–07:20
- Location: Blackwell town car, morning
- Characters Present: Victoria Blackwell, Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: Inside the town car, the mistress grabs her son's lapel as he pulls himself back against the passenger door. Location: Blackwell town car, morning. Key object: a perjury statement. Characters present: Victoria Blackwell, Richard Blackwell.
- Identity Anchors: Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings); Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing black suit for the gala, sharp lapels, slicked hair)
- Key Object: a perjury statement
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Inside the town car, the mistress grabs her son's lapel as he pulls himself back against the passenger door.
  * [03s–07s]: tight close-up — Close on the heir unfastening her gloved fingers from his jacket with quiet distaste.
  * [07s–10s]: tight close-up — Over the mistress's shoulder, the heir stares out at the courthouse steps.
- Sound Design (SFX & Voice Tone): muffled car interior hush, rain starting to tap car glass, engine ticking as it idles. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (cold): "Tell the judge the will was stolen."
  RICHARD (firm): "Father was never demented. I won't perjure myself."

ESCENA 45 (Viñeta #45 del Storyboard) — 07:20–07:30
- Location: county civic hall back alley, noon
- Characters Present: Elena Vance, Cole Barrett, Maggie Doyle
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: In the brick alleyway, the housekeeper presses an aged leather journal into the maid's hands, tears in her eyes. Location: county civic hall back alley, noon. Key object: a fire log with a check number. Characters present: Elena Vance, Cole Barrett, Maggie Doyle.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing clean denim jacket over the grey henley, hat brushed for once); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing best Sunday cardigan, the apron folded neatly on a chair)
- Key Object: a fire log with a check number
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — In the brick alleyway, the housekeeper presses an aged leather journal into the maid's hands, tears in her eyes.
  * [03s–07s]: close-up — Insert: the journal page opens to October 12, 2008: 'Paid Sheriff Drummond $10,000 to classify barn fire as accidental'.
  * [07s–10s]: tight close-up — Close on the housekeeper whispering her final truth as she holds Elena's fingers tight.
- Sound Design (SFX & Voice Tone): water dripping from fire escape iron, muffled brass band tuning inside civic hall, distant crowd chatter. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  MAGGIE (urgent): "Walter kept this log. The check is here."
  ELENA (grateful): "This proves arson. You saved her honor."

ESCENA 46 (Viñeta #46 del Storyboard) — 07:30–07:40
- Location: Silver Creek civic hall foyer, afternoon
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: Before the towering carved oak doors, the maid walks up and adjusts her mother's silver belt buckle. Location: Silver Creek civic hall foyer, afternoon. Key object: a gala invitation. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing clean denim jacket over the grey henley, hat brushed for once)
- Key Object: a gala invitation
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Before the towering carved oak doors, the maid walks up and adjusts her mother's silver belt buckle.
  * [03s–07s]: tight close-up — Close on the foreman reaching out, adjusting the collar of her white shirt with quiet tenderness.
  * [07s–10s]: tight close-up — Low angle as the maid places her hand on the brass door handle and pushes both doors open.
- Sound Design (SFX & Voice Tone): crystal chandelier hum, ballroom orchestra playing light waltz, heavy oak doors swinging wide. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (low): "Every rancher and judge is here."
  ELENA (resolved): "Good. They should know who fed their horses."

ESCENA 47 (Viñeta #47 del Storyboard) — 07:40–07:50
- Location: civic hall grand ballroom, afternoon
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot: The grand ballroom falls utterly silent as the ranch maid in her simple white shirt strides down the red carpet toward the stage. Location: civic hall grand ballroom, afternoon. Key object: an auction catalog. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings)
- Key Object: an auction catalog
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — The grand ballroom falls utterly silent as the ranch maid in her simple white shirt strides down the red carpet toward the stage.
  * [03s–07s]: tight close-up — Close on the mistress's hand tightening around the podium microphone until her diamond ring clicks against the steel.
  * [07s–10s]: tight close-up — Over the maid's shoulder, she ascends the three wooden stage stairs without breaking stride.
- Sound Design (SFX & Voice Tone): champagne glasses clinking nervously, ballroom murmur rising, microphone feedback whine. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (cold): "Security, remove her. This is a private gala."
  ELENA (calm): "You're auctioning land you don't own."

ESCENA 48 (Viñeta #48 del Storyboard) — 07:50–08:00
- Location: civic hall auction stage, afternoon
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: Under the blinding stage lights, the mistress steps right into the maid's face, abandoning all high-society poise. Location: civic hall auction stage, afternoon. Key object: a gavel on the auction block. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings)
- Key Object: a gavel on the auction block
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — Under the blinding stage lights, the mistress steps right into the maid's face, abandoning all high-society poise.
  * [03s–07s]: tight close-up — Extreme close-up on the mistress's twisted expression as she speaks directly into Elena's ear.
  * [07s–10s]: insert shot of the evidence object — Insert: Elena lays Walter's blue-sealed will onto the auctioneer's reading desk.
- Sound Design (SFX & Voice Tone): dramatic crowd gasps echoing in high hall, spotlight hum, microphone catching ragged breaths. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (mocking): "You are a stable rat playing dress-up."
  ELENA (quiet): "It was never yours. You warmed the chair."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts."
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
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: At the edge of the stage, the maid hands the heavy blue legal dossier down to the seated county probate judge. Location: civic hall auction stage, afternoon. Key object: a verified signature card. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing clean denim jacket over the grey henley, hat brushed for once)
- Key Object: a verified signature card
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the edge of the stage, the maid hands the heavy blue legal dossier down to the seated county probate judge.
  * [03s–07s]: tight close-up — Close on the judge adjusting his spectacles, his eyebrows climbing higher as he reads the notary stamp.
  * [07s–10s]: tight close-up — Over the judge's shoulder, the maid stands perfectly still as the entire hall holds its breath.
- Sound Design (SFX & Voice Tone): gavel wooden strike on table, stunned uproar from crowd, chairs scraping parquet floor. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (clear): "Walter's signature is verified. The auction is halted."
  ELENA (cold): "Now ask Mrs. Blackwell about the fire."

ESCENA 50 (Viñeta #50 del Storyboard) — 08:10–08:20
- Location: civic hall stage wings, afternoon
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: In the red velvet backstage shadows, the mistress corners the maid against the rope rigging, eyes feverish with malice. Location: civic hall stage wings, afternoon. Key object: a kerosene can. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings)
- Key Object: a kerosene can
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the red velvet backstage shadows, the mistress corners the maid against the rope rigging, eyes feverish with malice.
  * [03s–07s]: tight close-up — Close on the mistress's diamond-ringed hand touching the maid's cheek with chilling faux affection.
  * [07s–10s]: extreme close-up — Extreme close-up on the mistress's whispered threat, her lips parting with vicious triumph.
- Sound Design (SFX & Voice Tone): muffled hall applause continuing outside, heavy rope groaning under tension, hiss of stage lamps. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (quiet threat): "Sign the release, or your horses burn tonight."

ESCENA 51 (Viñeta #51 del Storyboard) — 08:20–08:30
- Location: Silver Creek barn exterior, dusk
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: The maid sprints through the barn gates as the foreman yanks a lit flare from a captured trespasser's hand. Location: Silver Creek barn exterior, dusk. Key object: a coil of rope in the hayloft. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing same denim jacket, hat in hand, standing at the barn door)
- Key Object: a coil of rope in the hayloft
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — The maid sprints through the barn gates as the foreman yanks a lit flare from a captured trespasser's hand.
  * [03s–07s]: close-up — Insert: the foreman grinds the smoking red flare out beneath his heavy work boot into the damp mud.
  * [07s–10s]: tight close-up — Close on the foreman looking up at Elena, breathing hard but smiling with fierce triumph.
- Sound Design (SFX & Voice Tone): flare hissing into wet gravel, horses whinnying safe inside, heavy boots running on dirt. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (dry): "We waited in the hayloft. No spark."
  ELENA (hard): "Tie them up. Drummond needs company."

ESCENA 52 (Viñeta #52 del Storyboard) — 08:30–08:40
- Location: civic hall courtroom chamber, evening
- Characters Present: Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: At the witness stand, the heir raises his right hand before the court clerk, his voice echoing across the silent gallery. Location: civic hall courtroom chamber, evening. Key object: a handwritten confession. Characters present: Richard Blackwell.
- Identity Anchors: Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing black gala suit, tie loosened, shaken)
- Key Object: a handwritten confession
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the witness stand, the heir raises his right hand before the court clerk, his voice echoing across the silent gallery.
  * [03s–07s]: tight close-up — Close on his pale face as he speaks the words that end his family's dynasty.
  * [07s–10s]: tight close-up — Over the heir's shoulder, Victoria watches from the defense table, face white as chalk.
- Sound Design (SFX & Voice Tone): courtroom gavel banging, reporters' camera shutters clicking, collective gasp from gallery. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  RICHARD (public, shaking): "I planted the watch for my mother."
  RICHARD (breaking): "Elena never stole anything. We stole fifteen years."

ESCENA 53 (Viñeta #53 del Storyboard) — 08:40–08:50
- Location: civic hall courtroom chamber, evening
- Characters Present: Maggie Doyle
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: The housekeeper grips the microphone and lifts her chin toward the district attorney. Location: civic hall courtroom chamber, evening. Key object: a recantation form. Characters present: Maggie Doyle.
- Identity Anchors: Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing same Sunday cardigan, hair escaped from the bun, standing tall)
- Key Object: a recantation form
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — The housekeeper grips the microphone and lifts her chin toward the district attorney.
  * [03s–07s]: tight close-up — Close on her hand pressing the original fire log onto the court clerk's cedar bench.
  * [07s–10s]: tight close-up — Over the housekeeper's shoulder, Elena nods from the front bench with unconditional love.
- Sound Design (SFX & Voice Tone): courtroom stenographer machine clicking rapidly, paper rustling, silence falling heavy. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana
- Dialogue (English, max 15 words, finish before 8.5 s):
  MAGGIE (clear): "I recant. Victoria set the fire."
  MAGGIE (raw): "June Vance was murdered protecting that ranch."

ESCENA 54 (Viñeta #54 del Storyboard) — 08:50–09:00
- Location: civic hall courtroom chamber, evening
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: At the plaintiff's table, the maid rises as the judge brings the wooden gavel down. Location: civic hall courtroom chamber, evening. Key object: a court order. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle)
- Key Object: a court order
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the plaintiff's table, the maid rises as the judge brings the wooden gavel down.
  * [03s–07s]: close-up — Insert: the judge signs 'CERTIFICATE OF OWNERSHIP — SILVER CREEK RANCH — OWNER: ELENA VANCE'.
  * [07s–10s]: tight close-up — Close on Elena's eyes filling with tears of vindication, a slow, radiant smile breaking across her face.
- Sound Design (SFX & Voice Tone): resounding gavel strike, loud sustained applause from gallery, floorboards creaking. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (steady): "The court recognizes Elena Vance as sole heir."
  ELENA (breaking): "We did it, Mama. We're home."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 49 (Viñeta #49 del Storyboard) — 08:00–08:10
- Location: civic hall auction stage, afternoon
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: At the edge of the stage, the maid hands the heavy blue legal dossier down to the seated county probate judge. Location: civic hall auction stage, afternoon. Key object: a verified signature card. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing clean denim jacket over the grey henley, hat brushed for once)
- Key Object: a verified signature card
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the edge of the stage, the maid hands the heavy blue legal dossier down to the seated county probate judge.
  * [03s–07s]: tight close-up — Close on the judge adjusting his spectacles, his eyebrows climbing higher as he reads the notary stamp.
  * [07s–10s]: tight close-up — Over the judge's shoulder, the maid stands perfectly still as the entire hall holds its breath.
- Sound Design (SFX & Voice Tone): gavel wooden strike on table, stunned uproar from crowd, chairs scraping parquet floor. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (clear): "Walter's signature is verified. The auction is halted."
  ELENA (cold): "Now ask Mrs. Blackwell about the fire."

ESCENA 50 (Viñeta #50 del Storyboard) — 08:10–08:20
- Location: civic hall stage wings, afternoon
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: In the red velvet backstage shadows, the mistress corners the maid against the rope rigging, eyes feverish with malice. Location: civic hall stage wings, afternoon. Key object: a kerosene can. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing clean white button shirt under the tan barn coat, braid neat); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing deep emerald high-collar dress for the gala, diamond earrings)
- Key Object: a kerosene can
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — In the red velvet backstage shadows, the mistress corners the maid against the rope rigging, eyes feverish with malice.
  * [03s–07s]: tight close-up — Close on the mistress's diamond-ringed hand touching the maid's cheek with chilling faux affection.
  * [07s–10s]: extreme close-up — Extreme close-up on the mistress's whispered threat, her lips parting with vicious triumph.
- Sound Design (SFX & Voice Tone): muffled hall applause continuing outside, heavy rope groaning under tension, hiss of stage lamps. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (quiet threat): "Sign the release, or your horses burn tonight."

ESCENA 51 (Viñeta #51 del Storyboard) — 08:20–08:30
- Location: Silver Creek barn exterior, dusk
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: The maid sprints through the barn gates as the foreman yanks a lit flare from a captured trespasser's hand. Location: Silver Creek barn exterior, dusk. Key object: a coil of rope in the hayloft. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing same denim jacket, hat in hand, standing at the barn door)
- Key Object: a coil of rope in the hayloft
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — The maid sprints through the barn gates as the foreman yanks a lit flare from a captured trespasser's hand.
  * [03s–07s]: close-up — Insert: the foreman grinds the smoking red flare out beneath his heavy work boot into the damp mud.
  * [07s–10s]: tight close-up — Close on the foreman looking up at Elena, breathing hard but smiling with fierce triumph.
- Sound Design (SFX & Voice Tone): flare hissing into wet gravel, horses whinnying safe inside, heavy boots running on dirt. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (dry): "We waited in the hayloft. No spark."
  ELENA (hard): "Tie them up. Drummond needs company."

ESCENA 52 (Viñeta #52 del Storyboard) — 08:30–08:40
- Location: civic hall courtroom chamber, evening
- Characters Present: Richard Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: At the witness stand, the heir raises his right hand before the court clerk, his voice echoing across the silent gallery. Location: civic hall courtroom chamber, evening. Key object: a handwritten confession. Characters present: Richard Blackwell.
- Identity Anchors: Richard Blackwell (Cast Sheet Pos #3: around thirty, clean-cut, sandy hair combed back, pale blue eyes, practiced smile, tall athletic build, wearing black gala suit, tie loosened, shaken)
- Key Object: a handwritten confession
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the witness stand, the heir raises his right hand before the court clerk, his voice echoing across the silent gallery.
  * [03s–07s]: tight close-up — Close on his pale face as he speaks the words that end his family's dynasty.
  * [07s–10s]: tight close-up — Over the heir's shoulder, Victoria watches from the defense table, face white as chalk.
- Sound Design (SFX & Voice Tone): courtroom gavel banging, reporters' camera shutters clicking, collective gasp from gallery. Voice tone: RICHARD — smooth mid-range American English, reasonable tone that never quite reaches sincerity
- Dialogue (English, max 15 words, finish before 8.5 s):
  RICHARD (public, shaking): "I planted the watch for my mother."
  RICHARD (breaking): "Elena never stole anything. We stole fifteen years."

ESCENA 53 (Viñeta #53 del Storyboard) — 08:40–08:50
- Location: civic hall courtroom chamber, evening
- Characters Present: Maggie Doyle
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: The housekeeper grips the microphone and lifts her chin toward the district attorney. Location: civic hall courtroom chamber, evening. Key object: a recantation form. Characters present: Maggie Doyle.
- Identity Anchors: Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing same Sunday cardigan, hair escaped from the bun, standing tall)
- Key Object: a recantation form
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — The housekeeper grips the microphone and lifts her chin toward the district attorney.
  * [03s–07s]: tight close-up — Close on her hand pressing the original fire log onto the court clerk's cedar bench.
  * [07s–10s]: tight close-up — Over the housekeeper's shoulder, Elena nods from the front bench with unconditional love.
- Sound Design (SFX & Voice Tone): courtroom stenographer machine clicking rapidly, paper rustling, silence falling heavy. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana
- Dialogue (English, max 15 words, finish before 8.5 s):
  MAGGIE (clear): "I recant. Victoria set the fire."
  MAGGIE (raw): "June Vance was murdered protecting that ranch."

ESCENA 54 (Viñeta #54 del Storyboard) — 08:50–09:00
- Location: civic hall courtroom chamber, evening
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: At the plaintiff's table, the maid rises as the judge brings the wooden gavel down. Location: civic hall courtroom chamber, evening. Key object: a court order. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle)
- Key Object: a court order
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the plaintiff's table, the maid rises as the judge brings the wooden gavel down.
  * [03s–07s]: close-up — Insert: the judge signs 'CERTIFICATE OF OWNERSHIP — SILVER CREEK RANCH — OWNER: ELENA VANCE'.
  * [07s–10s]: tight close-up — Close on Elena's eyes filling with tears of vindication, a slow, radiant smile breaking across her face.
- Sound Design (SFX & Voice Tone): resounding gavel strike, loud sustained applause from gallery, floorboards creaking. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (steady): "The court recognizes Elena Vance as sole heir."
  ELENA (breaking): "We did it, Mama. We're home."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts."
```

### Lote 10 — Minuto 10 (escenas 55–60)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_10.png`

**Guardar 16:9 como:** `raw_clips/minute_10.mp4`

**Guardar 9:16 como:** `raw_clips/minute_10_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 55 (Viñeta #55 del Storyboard) — 09:00–09:10
- Location: civic hall grand steps, night
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: Under the flashing blue lights of state police cruisers, the troopers secure handcuffs behind the mistress's back. Location: civic hall grand steps, night. Key object: a pair of handcuffs. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald gala dress, gloves gone, jewelry missing)
- Key Object: a pair of handcuffs
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Under the flashing blue lights of state police cruisers, the troopers secure handcuffs behind the mistress's back.
  * [03s–07s]: tight close-up — Close on the steel cuffs ratcheting shut with sharp metallic clicks over her bare wrists.
  * [07s–10s]: tight close-up — Over the mistress's shoulder, she sees the entire town watching her downfall in silence.
- Sound Design (SFX & Voice Tone): handcuffs clicking into place, police radios squawking, crowd watching without a sound. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (furious): "You cannot do this! I built this town!"
  ELENA (cold): "You built it on my mother's grave."

ESCENA 56 (Viñeta #56 del Storyboard) — 09:10–09:20
- Location: civic hall grand steps, night
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: On the wet steps, the handcuffed mistress collapses forward onto her knees before the maid she once tormented. Location: civic hall grand steps, night. Key object: a suitcase on the steps. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald gala dress, gloves gone, jewelry missing)
- Key Object: a suitcase on the steps
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — On the wet steps, the handcuffed mistress collapses forward onto her knees before the maid she once tormented.
  * [03s–07s]: tight close-up — Close on the mistress's mascara running in black streaks down her pale, pleading face.
  * [07s–10s]: tight close-up — Low angle on the maid, dignified and untouchable as the night rain begins to fall gently.
- Sound Design (SFX & Voice Tone): rain softly pattering on granite steps, police cruiser doors opening, distant train whistle. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (small): "Leave me the guesthouse."
  ELENA (flat): "You left me a broken cup and a broom."

ESCENA 57 (Viñeta #57 del Storyboard) — 09:20–09:30
- Location: Silver Creek mansion foyer, night
- Characters Present: Elena Vance, Maggie Doyle
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot: The grand foyer is warm with lamplight; the maid crosses the floor where she was once humiliated, now as the estate's mistress. Location: Silver Creek mansion foyer, night. Key object: a clean white teacup. Characters present: Elena Vance, Maggie Doyle.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing same Sunday cardigan, hair escaped from the bun, standing tall)
- Key Object: a clean white teacup
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — The grand foyer is warm with lamplight; the maid crosses the floor where she was once humiliated, now as the estate's mistress.
  * [03s–07s]: tight close-up — Close on her fingers tracing the polished oak table where the crystal decanter was once smashed.
  * [07s–10s]: tight close-up — Over the maid's shoulder, the housekeeper sets down a porcelain teacup with gentle reverence.
- Sound Design (SFX & Voice Tone): warm fire crackling in hearth, porcelain cup settling on wood, night breeze through tall windows. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  MAGGIE (warm): "The house is quiet. It feels clean."
  ELENA (quiet): "It's a sanctuary for everyone they pushed down."

ESCENA 58 (Viñeta #58 del Storyboard) — 09:30–09:40
- Location: Silver Creek barn gate, moonlight
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: At the corral gate, the foreman turns to the maid, nervously rolling the brim of his felt hat in both hands. Location: Silver Creek barn gate, moonlight. Key object: a set of ranch keys. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing same denim jacket, hat in hand, standing at the barn door)
- Key Object: a set of ranch keys
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — At the corral gate, the foreman turns to the maid, nervously rolling the brim of his felt hat in both hands.
  * [03s–07s]: tight close-up — Close on Elena's hand reaching up to touch his weathered cheek, stopping his nervous motion.
  * [07s–10s]: tight close-up — Over the foreman's shoulder, she steps into his arms, resting her forehead against his chest.
- Sound Design (SFX & Voice Tone): night crickets singing in prairie grass, horses grazing peacefully, soft warm breeze. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (dry): "You own twenty thousand acres now."
  ELENA (warm): "I need you. Stay and build this with me."

ESCENA 59 (Viñeta #59 del Storyboard) — 09:40–09:50
- Location: Blackwell great room mantelpiece, night
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: Before the roaring stone hearth, the maid steps back as June Vance's smiling photograph occupies the place of honor. Location: Blackwell great room mantelpiece, night. Key object: a framed photograph of June. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle)
- Key Object: a framed photograph of June
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Before the roaring stone hearth, the maid steps back as June Vance's smiling photograph occupies the place of honor.
  * [03s–07s]: close-up — Insert: the silver belt buckle catches the orange firelight beside the tin frame, engraved: 'VANCE RANCH — 1982'.
  * [07s–10s]: tight close-up — Close on Elena's face, radiant with deep peace as a single grateful tear slips down her cheek.
- Sound Design (SFX & Voice Tone): deep hearth fire crackling warmly, pine wood popping, soft wind against glass. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (fierce): "Your name will never be erased again."
  ELENA (quiet): "Silver Creek is ours. Justice is done."

ESCENA 60 (Viñeta #60 del Storyboard) — 09:50–10:00
- Location: mansion study desk, night
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: At the quiet study desk, the maid lifts the will parchment and finds a sealed wax envelope attached to the back. Location: mansion study desk, night. Key object: a folded letter with a second clause. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle)
- Key Object: a folded letter with a second clause
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the quiet study desk, the maid lifts the will parchment and finds a sealed wax envelope attached to the back.
  * [03s–07s]: close-up — Insert: her thumb cracks the red wax seal: 'To Elena — Read in private after you claim the ranch'.
  * [07s–10s]: tight close-up — Close on Elena's eyes widening in stunned alarm as she reads Walter's final words in the letter.
- Sound Design (SFX & Voice Tone): paper crackling in silence, banker lamp humming softly, sudden wind banging study shutters. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (stunned): "There's another clause. You have a brother."
  ELENA (urgent): "Find him before Victoria's family does."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 55 (Viñeta #55 del Storyboard) — 09:00–09:10
- Location: civic hall grand steps, night
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: Under the flashing blue lights of state police cruisers, the troopers secure handcuffs behind the mistress's back. Location: civic hall grand steps, night. Key object: a pair of handcuffs. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald gala dress, gloves gone, jewelry missing)
- Key Object: a pair of handcuffs
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Under the flashing blue lights of state police cruisers, the troopers secure handcuffs behind the mistress's back.
  * [03s–07s]: tight close-up — Close on the steel cuffs ratcheting shut with sharp metallic clicks over her bare wrists.
  * [07s–10s]: tight close-up — Over the mistress's shoulder, she sees the entire town watching her downfall in silence.
- Sound Design (SFX & Voice Tone): handcuffs clicking into place, police radios squawking, crowd watching without a sound. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (furious): "You cannot do this! I built this town!"
  ELENA (cold): "You built it on my mother's grave."

ESCENA 56 (Viñeta #56 del Storyboard) — 09:10–09:20
- Location: civic hall grand steps, night
- Characters Present: Elena Vance, Victoria Blackwell
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: On the wet steps, the handcuffed mistress collapses forward onto her knees before the maid she once tormented. Location: civic hall grand steps, night. Key object: a suitcase on the steps. Characters present: Elena Vance, Victoria Blackwell.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle); Victoria Blackwell (Cast Sheet Pos #2: mid-forties platinum-blonde bob, sharp cheekbones, cool grey eyes, dark red lipstick, pearl earrings, wearing emerald gala dress, gloves gone, jewelry missing)
- Key Object: a suitcase on the steps
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — On the wet steps, the handcuffed mistress collapses forward onto her knees before the maid she once tormented.
  * [03s–07s]: tight close-up — Close on the mistress's mascara running in black streaks down her pale, pleading face.
  * [07s–10s]: tight close-up — Low angle on the maid, dignified and untouchable as the night rain begins to fall gently.
- Sound Design (SFX & Voice Tone): rain softly pattering on granite steps, police cruiser doors opening, distant train whistle. Voice tone: VICTORIA — low, polished, unhurried American English, smiles through threats, never shouts; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  VICTORIA (small): "Leave me the guesthouse."
  ELENA (flat): "You left me a broken cup and a broom."

ESCENA 57 (Viñeta #57 del Storyboard) — 09:20–09:30
- Location: Silver Creek mansion foyer, night
- Characters Present: Elena Vance, Maggie Doyle
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot: The grand foyer is warm with lamplight; the maid crosses the floor where she was once humiliated, now as the estate's mistress. Location: Silver Creek mansion foyer, night. Key object: a clean white teacup. Characters present: Elena Vance, Maggie Doyle.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle); Maggie Doyle (Cast Sheet Pos #5: late fifties iron-grey hair in a loose bun, kind weathered face, small round glasses on a chain, wearing same Sunday cardigan, hair escaped from the bun, standing tall)
- Key Object: a clean white teacup
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: wide establishing shot — The grand foyer is warm with lamplight; the maid crosses the floor where she was once humiliated, now as the estate's mistress.
  * [03s–07s]: tight close-up — Close on her fingers tracing the polished oak table where the crystal decanter was once smashed.
  * [07s–10s]: tight close-up — Over the maid's shoulder, the housekeeper sets down a porcelain teacup with gentle reverence.
- Sound Design (SFX & Voice Tone): warm fire crackling in hearth, porcelain cup settling on wood, night breeze through tall windows. Voice tone: MAGGIE — grounded, plainspoken American English with a soft Irish lilt worn thin by thirty years in Montana; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  MAGGIE (warm): "The house is quiet. It feels clean."
  ELENA (quiet): "It's a sanctuary for everyone they pushed down."

ESCENA 58 (Viñeta #58 del Storyboard) — 09:30–09:40
- Location: Silver Creek barn gate, moonlight
- Characters Present: Elena Vance, Cole Barrett
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium two-shot: At the corral gate, the foreman turns to the maid, nervously rolling the brim of his felt hat in both hands. Location: Silver Creek barn gate, moonlight. Key object: a set of ranch keys. Characters present: Elena Vance, Cole Barrett.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle); Cole Barrett (Cast Sheet Pos #4: early thirties weathered rancher, dark hair under a dust-worn felt hat, steady hazel eyes, quiet jaw, broad shoulders, wearing same denim jacket, hat in hand, standing at the barn door)
- Key Object: a set of ranch keys
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium two-shot — At the corral gate, the foreman turns to the maid, nervously rolling the brim of his felt hat in both hands.
  * [03s–07s]: tight close-up — Close on Elena's hand reaching up to touch his weathered cheek, stopping his nervous motion.
  * [07s–10s]: tight close-up — Over the foreman's shoulder, she steps into his arms, resting her forehead against his chest.
- Sound Design (SFX & Voice Tone): night crickets singing in prairie grass, horses grazing peacefully, soft warm breeze. Voice tone: COLE — quiet, low American English, careful diction, warmth held under restraint; ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  COLE (dry): "You own twenty thousand acres now."
  ELENA (warm): "I need you. Stay and build this with me."

ESCENA 59 (Viñeta #59 del Storyboard) — 09:40–09:50
- Location: Blackwell great room mantelpiece, night
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: Before the roaring stone hearth, the maid steps back as June Vance's smiling photograph occupies the place of honor. Location: Blackwell great room mantelpiece, night. Key object: a framed photograph of June. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle)
- Key Object: a framed photograph of June
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — Before the roaring stone hearth, the maid steps back as June Vance's smiling photograph occupies the place of honor.
  * [03s–07s]: close-up — Insert: the silver belt buckle catches the orange firelight beside the tin frame, engraved: 'VANCE RANCH — 1982'.
  * [07s–10s]: tight close-up — Close on Elena's face, radiant with deep peace as a single grateful tear slips down her cheek.
- Sound Design (SFX & Voice Tone): deep hearth fire crackling warmly, pine wood popping, soft wind against glass. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (fierce): "Your name will never be erased again."
  ELENA (quiet): "Silver Creek is ours. Justice is done."

ESCENA 60 (Viñeta #60 del Storyboard) — 09:50–10:00
- Location: mansion study desk, night
- Characters Present: Elena Vance
- Storyboard Panel (Shot 1 exact framing): [00s-03s] medium shot: At the quiet study desk, the maid lifts the will parchment and finds a sealed wax envelope attached to the back. Location: mansion study desk, night. Key object: a folded letter with a second clause. Characters present: Elena Vance.
- Identity Anchors: Elena Vance (Cast Sheet Pos #1: mid-twenties sun-weathered woman, long chestnut low braid, dark-brown eyes, light freckles, faint scar through one eyebrow, slender strong build, wearing deep green flannel shirt, dark jeans, her mother's silver belt buckle)
- Key Object: a folded letter with a second clause
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: medium shot — At the quiet study desk, the maid lifts the will parchment and finds a sealed wax envelope attached to the back.
  * [03s–07s]: close-up — Insert: her thumb cracks the red wax seal: 'To Elena — Read in private after you claim the ranch'.
  * [07s–10s]: tight close-up — Close on Elena's eyes widening in stunned alarm as she reads Walter's final words in the letter.
- Sound Design (SFX & Voice Tone): paper crackling in silence, banker lamp humming softly, sudden wind banging study shutters. Voice tone: ELENA — warm mid-range American English, plain Montana vowels, steady under pressure, never theatrical
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELENA (stunned): "There's another clause. You have a brother."
  ELENA (urgent): "Find him before Victoria's family does."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando los 3 cambios de cámara ([00s-03s] arrancando directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos, [03s-07s] corte a plano de diálogo/acción, y [07s-10s] corte a plano de reacción), manteniendo estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts."
```

---

## Paso 4 — Ensamblar

Cuando existan los 10 archivos `minute_01.mp4 … minute_10.mp4`:

```powershell
./novelfactory.bat assemble the_ranch_maid_heiress
```

El ensamblador detecta el modo B, genera el máster 16:9 de 10 minutos,
el SRT sincronizado y el teaser vertical automático de 20 segundos.

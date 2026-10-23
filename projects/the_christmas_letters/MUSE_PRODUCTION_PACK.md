# The Christmas Letters — Producción con Muse AI (método nuevo)

**Slug:** `the_christmas_letters`  ·  **Escenas:** 132  ·  **Imágenes:** 23  ·  **Lotes:** 22

> **NOTA DE PRODUCCIÓN:** ADJUNTA EN CADA ESCENA: la viñeta de esa escena + las referencias SOLO de los personajes que salen en ESA escena + el prompt de esa escena. No generes ninguna escena sin sus personajes adjuntos.

> Six years after Eleanor Cole threw her out, Valentina Reyes returns to decorate the mansion and discovers the 72 letters she wrote to Nate were stolen, and his Christmas Eve wedding is her last chance to prove it.

## Cómo funciona

1. Genera **una** hoja maestra de personajes con los rostros y vestuarios fijos.
2. Genera **22** storyboards (uno por minuto) usando esa hoja como referencia.
3. En Muse AI, sube la hoja maestra + el storyboard del minuto y pega el bloque del lote.
4. Guarda cada video como `raw_clips/minute_0X.mp4` y ejecuta el comando de ensamblaje.

> No necesitas frames por escena ni clips de 10 s: el ensamblador detecta los lotes de 1 minuto.

---

## Paso 1 — Hoja maestra de personajes

Guarda el resultado como `storyboards/REF_CAST_MASTER.png`.

**Prompt:**

```text
Actúa como director de casting y diseñador de personajes. Genera UNA SOLA IMAGEN horizontal 16:9 que muestre juntos, de cuerpo completo, de pie, mirando al frente sobre un fondo gris neutro de estudio (#808080) y sin tocarse entre sí, a los siguientes personajes de nuestra novela en estilo Cinematográfico Realista 35mm:

Position #1 (Far Left) — VALENTINA REYES. Rol: Protagonista. Edad: late-twenties. Rasgos físicos: late twenties Latina event decorator, long dark wavy hair, warm brown eyes, full lips, golden-brown skin, cream cashmere turtleneck and dark tailored trousers. Vestuario fijo: cream cashmere turtleneck, dark tailored trousers, pearl studs.
Position #2 — NATHANIEL COLE. Rol: Interés romántico. Edad: early-thirties. Rasgos físicos: early thirties hotel heir, square jaw, short dark-brown hair, intense grey eyes, athletic build, charcoal overcoat over a black suit. Vestuario fijo: charcoal overcoat over a black suit, no tie.
Position #3 — MADISON PIERCE. Rol: antagonist_rival. Edad: late-twenties. Rasgos físicos: late twenties socialite, platinum blonde bob, sharp cheekbones, pale blue eyes, ivory shearling coat and gold hoops. Vestuario fijo: ivory shearling coat, gold hoops, white gloves.
Position #4 — ELEANOR COLE. Rol: Antagonista. Edad: early-sixties. Rasgos físicos: early sixties matriarch, tall and straight-backed, silver chignon, pale blue eyes, porcelain skin, midnight-blue dress and pearls. Vestuario fijo: midnight-blue dress, pearls, silver hair in a chignon.
Position #5 — WALTER BRIGGS. Rol: witness. Edad: late-fifties. Rasgos físicos: late fifties mansion porter, weathered face, grey hair, heavy build, grey uniform with brass buttons. Vestuario fijo: grey porter uniform, brass buttons, polished shoes.
Position #6 — JUNE ALVAREZ. Rol: Aliada. Edad: early-fifties. Rasgos físicos: early fifties cook, dark hair pulled back, warm brown eyes, strong hands, white chef coat and red scarf. Vestuario fijo: white chef coat, red scarf, dark hair pulled back.
Position #7 (Far Right) — ROSA REYES. Rol: Aliada. Edad: mid-fifties. Rasgos físicos: mid fifties mother, dark wavy hair, warm brown eyes, flour on her sleeve, rust cardigan. Vestuario fijo: rust cardigan, flour on her sleeve, warm slippers.

Ordena a los personajes de izquierda a derecha y coloca debajo de cada uno únicamente 'Position #N — NOMBRE EN MAYÚSCULAS'. Mantén exactamente las mismas posiciones, rostros, peinados y vestuarios en todas las imágenes del storyboard y de los lotes de Muse AI. Sin texto adicional, sin títulos, sin frases, sin logos, sin marcas de agua; solo la imagen de los personajes y sus posiciones.
```

---

## Paso 2 — Storyboards (22 imágenes)

Genera cada imagen con el mismo estilo y los mismos personajes de la hoja maestra.
Guarda cada archivo en `storyboards/` con el nombre indicado.

### REF_GRID_MIN_01.png — Minuto 1 (escenas 1–6)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 1 (Escenas 1 a 6) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 1 (Cole mansion foyer, Christmas week, a giant half-decorated tree): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Nathaniel Cole, Madison Pierce. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing ivory shearling coat, gold hoops, white gloves).
Viñeta 2 — Escena 2 (Cole mansion foyer, Christmas week, a giant half-decorated tree): [00s-07s] two-shot, medium shot with Madison Pierce and Nathaniel Cole: Madison Pierce and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: a silver tray. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Nathaniel Cole, Madison Pierce. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing ivory shearling coat, gold hoops, white gloves).
Viñeta 3 — Escena 3 (Reyes house, warm kitchen, a small tree with one crystal star): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Rosa Reyes. Valentina Reyes is already moving through Reyes house, warm kitchen, a small tree with one crystal star, the action carrying over from the exact storyboard framing. Key object in frame: the twin crystal star. Location: Reyes house, warm kitchen, a small tree with one crystal star. Characters present: Valentina Reyes, Rosa Reyes. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Rosa Reyes (Cast Sheet Pos #7: mid fifties; mother with dark wavy hair; wearing rust cardigan, flour on her sleeve, warm slippers).
Viñeta 4 — Escena 4 (Cole mansion study, firelight and dark wood): [00s-08s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon).
Viñeta 5 — Escena 5 (Cole mansion service hall, coat racks and mail slots): [00s-04s] wide establishing shot, face and mouth visible: Walter Briggs is on camera with face and mouth fully visible, looking at the other person in frame. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Walter Briggs. No other characters appear. Identity anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes).
Viñeta 6 — Escena 6 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-03s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at June Alvarez. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Eleanor Cole, June Alvarez. No other characters appear. Identity anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_02.png — Minuto 2 (escenas 7–12)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 2 (Escenas 7 a 12) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 7 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-08s] two-shot, medium shot with Eleanor Cole and June Alvarez: Eleanor Cole and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Eleanor Cole, June Alvarez. No other characters appear. Identity anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back).
Viñeta 2 — Escena 8 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-03s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: June Alvarez. No other characters appear. Identity anchors: June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back).
Viñeta 3 — Escena 9 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-03s] close-up, face and mouth visible: Walter Briggs is on camera with face and mouth fully visible, looking at June Alvarez. Walter Briggs speaks as the camera holds close on their face, the old letter catching the light between them. Location: Cole mansion library, lamplight and floor-to-ceiling books. Key object: the old letter. Characters present: Walter Briggs, June Alvarez. No other characters appear. Identity anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back).
Viñeta 4 — Escena 10 (Cole mansion wine cellar, stone stairs and a single bulb): [00s-05s] wide establishing shot, face and mouth visible: Walter Briggs is on camera with face and mouth fully visible, looking at the other person in frame. Walter Briggs is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Walter Briggs. No other characters appear. Identity anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes).
Viñeta 5 — Escena 11 (Cole mansion wine cellar, stone stairs and a single bulb): [00s-05s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: June Alvarez. No other characters appear. Identity anchors: June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back).
Viñeta 6 — Escena 12 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-07s] two-shot, medium shot with Eleanor Cole and June Alvarez: Eleanor Cole and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Eleanor Cole, June Alvarez. No other characters appear. Identity anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_03.png — Minuto 3 (escenas 13–18)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 3 (Escenas 13 a 18) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 13 (Cole mansion kitchen, warm steel and hanging copper): [00s-06s] two-shot, medium shot with June Alvarez and Valentina Reyes: June Alvarez and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the delivery slip. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes, June Alvarez. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back).
Viñeta 2 — Escena 14 (Cole mansion service hall, coat racks and mail slots): [00s-08s] two-shot, medium shot with Eleanor Cole and Valentina Reyes: Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: a silver box of ornaments. Key object in frame: the foreground. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon).
Viñeta 3 — Escena 15 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-07s] two-shot, medium shot with June Alvarez and Valentina Reyes: June Alvarez and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: a stack of law books. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, June Alvarez. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back).
Viñeta 4 — Escena 16 (Cole mansion foyer, Christmas week, a giant half-decorated tree): [00s-07s] two-shot, medium shot with Madison Pierce and Valentina Reyes: Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: a silver tray. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Madison Pierce. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing ivory shearling coat, gold hoops, white gloves).
Viñeta 5 — Escena 17 (Cole mansion foyer, Christmas week, a giant half-decorated tree): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: a silver box of ornaments. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie).
Viñeta 6 — Escena 18 (Cole mansion study, firelight and dark wood): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the wedding invitation. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Madison Pierce, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing ivory shearling coat, gold hoops, white gloves); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_04.png — Minuto 4 (escenas 19–24)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 4 (Escenas 19 a 24) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 19 (Cole mansion study, firelight and dark wood): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon).
Viñeta 2 — Escena 20 (Cole mansion terrace, snow falling over the lit garden): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: a string of lights. Key object in frame: the foreground. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie).
Viñeta 3 — Escena 21 (Cole mansion terrace, snow falling over the lit garden): [00s-07s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the phone. Key object in frame: the foreground. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Valentina Reyes. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs).
Viñeta 4 — Escena 22 (Cole mansion terrace, snow falling over the lit garden): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie).
Viñeta 5 — Escena 23 (Cole mansion study, firelight and dark wood): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Eleanor Cole. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing emerald gown, pearl necklace, silver hair in a chignon).
Viñeta 6 — Escena 24 (Cole mansion study, firelight and dark wood): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at the other person in frame. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: sharp. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_05.png — Minuto 5 (escenas 25–30)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 5 (Escenas 25 a 30) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 25 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-04s] wide establishing shot, face and mouth visible: Madison Pierce is on camera with face and mouth fully visible, looking at Valentina Reyes. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the white tablecloth. Key object in frame: sharp. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Madison Pierce. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing champagne gown, diamond drop earrings, white fur stole).
Viñeta 2 — Escena 26 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the delivery invoice. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie).
Viñeta 3 — Escena 27 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Madison Pierce and Valentina Reyes: Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the champagne coupe. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Madison Pierce. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing champagne gown, diamond drop earrings, white fur stole).
Viñeta 4 — Escena 28 (Cole mansion service hall, coat racks and mail slots): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Walter Briggs. Valentina Reyes is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: sharp. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Valentina Reyes, Walter Briggs. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes).
Viñeta 5 — Escena 29 (Cole mansion service hall, coat racks and mail slots): [00s-03s] close-up, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Walter Briggs. June Alvarez speaks as the camera holds close on their face, the cellar key catching the light between them. Key object in frame: sharp. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Valentina Reyes, Walter Briggs, June Alvarez. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back).
Viñeta 6 — Escena 30 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-04s] wide establishing shot, face and mouth visible: Madison Pierce is on camera with face and mouth fully visible, looking at Nathaniel Cole. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the delivery invoice. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing champagne gown, diamond drop earrings, white fur stole).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_06.png — Minuto 6 (escenas 31–36)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 6 (Escenas 31 a 36) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 31 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the coffee cup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie).
Viñeta 2 — Escena 32 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: a paper napkin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie).
Viñeta 3 — Escena 33 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the seating chart. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing emerald gown, pearl necklace, silver hair in a chignon).
Viñeta 4 — Escena 34 (Cole mansion service hall, coat racks and mail slots): [00s-07s] two-shot, medium shot with Nathaniel Cole and Walter Briggs: Nathaniel Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the mail slot. Key object in frame: the foreground. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes).
Viñeta 5 — Escena 35 (Cole mansion service hall, coat racks and mail slots): [00s-07s] two-shot, medium shot with Walter Briggs and Eleanor Cole: Walter Briggs and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Eleanor Cole, Walter Briggs. No other characters appear. Identity anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing emerald gown, pearl necklace, silver hair in a chignon); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes).
Viñeta 6 — Escena 36 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_07.png — Minuto 7 (escenas 37–42)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 7 (Escenas 37 a 42) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 37 (Cole mansion study, firelight and dark wood): [00s-04s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Walter Briggs. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the burning envelope. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Eleanor Cole, Walter Briggs, June Alvarez. No other characters appear. Identity anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing emerald gown, pearl necklace, silver hair in a chignon); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back).
Viñeta 2 — Escena 38 (Cole mansion study, firelight and dark wood): [00s-03s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the charred letter scrap. Key object in frame: her apron. Location: Cole mansion study, firelight and dark wood. Characters present: June Alvarez. No other characters appear. Identity anchors: June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back).
Viñeta 3 — Escena 39 (Cole mansion study, firelight and dark wood): [00s-07s] two-shot, medium shot with Eleanor Cole and Madison Pierce: Eleanor Cole and Madison Pierce face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the calendar. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Madison Pierce, Eleanor Cole. No other characters appear. Identity anchors: Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing champagne gown, diamond drop earrings, white fur stole); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing emerald gown, pearl necklace, silver hair in a chignon).
Viñeta 4 — Escena 40 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-03s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Valentina Reyes. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the charred letter scrap. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, June Alvarez. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back).
Viñeta 5 — Escena 41 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-05s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Valentina Reyes. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, June Alvarez. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back).
Viñeta 6 — Escena 42 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the cellar key. Key object in frame: sharp. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, June Alvarez. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_08.png — Minuto 8 (escenas 43–48)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 8 (Escenas 43 a 48) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 43 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-05s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the old Christmas photograph. Key object in frame: sharp. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie).
Viñeta 2 — Escena 44 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the old Christmas photograph. Key object in frame: sharp. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie).
Viñeta 3 — Escena 45 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the old Christmas photograph. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon).
Viñeta 4 — Escena 46 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Madison Pierce and Nathaniel Cole: Madison Pierce and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: a champagne flute. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up).
Viñeta 5 — Escena 47 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Madison Pierce and Valentina Reyes: Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the silver tray. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Madison Pierce. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up).
Viñeta 6 — Escena 48 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Walter Briggs and June Alvarez: Walter Briggs and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: a crystal star pin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Walter Briggs, June Alvarez. No other characters appear. Identity anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_09.png — Minuto 9 (escenas 49–54)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 9 (Escenas 49 a 54) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 49 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-04s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the wedding announcement. Key object in frame: sharp. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon).
Viñeta 2 — Escena 50 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-04s] wide establishing shot, face and mouth visible: Madison Pierce is on camera with face and mouth fully visible, looking at Valentina Reyes. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Madison Pierce. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up).
Viñeta 3 — Escena 51 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie).
Viñeta 4 — Escena 52 (Cole mansion study, firelight and dark wood): [00s-05s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: sharp. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie).
Viñeta 5 — Escena 53 (Cole mansion study, firelight and dark wood): [00s-07s] two-shot, medium shot with Eleanor Cole and Valentina Reyes: Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the study door. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon).
Viñeta 6 — Escena 54 (Cole mansion study, firelight and dark wood): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the study door. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_10.png — Minuto 10 (escenas 55–60)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 10 (Escenas 55 a 60) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 55 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Madison Pierce and Valentina Reyes: Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the champagne glass. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Madison Pierce. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up).
Viñeta 2 — Escena 56 (Cole mansion kitchen, warm steel and hanging copper): [00s-07s] two-shot, medium shot with June Alvarez and Valentina Reyes: June Alvarez and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the cellar key. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes, June Alvarez. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back).
Viñeta 3 — Escena 57 (Cole mansion kitchen, warm steel and hanging copper): [00s-07s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the phone. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail).
Viñeta 4 — Escena 58 (Cole mansion wine cellar, stone stairs and a single bulb): [00s-05s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the flashlight. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Valentina Reyes, June Alvarez. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back).
Viñeta 5 — Escena 59 (Cole mansion wine cellar, stone stairs and a single bulb): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Walter Briggs. Valentina Reyes is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: sharp. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Valentina Reyes, Walter Briggs. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes).
Viñeta 6 — Escena 60 (Cole mansion wine cellar, stone stairs and a single bulb): [00s-03s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Eleanor Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_11.png — Minuto 11 (escenas 61–66)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 11 (Escenas 61 a 66) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 61 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole, Madison Pierce. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up).
Viñeta 2 — Escena 62 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-04s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon).
Viñeta 3 — Escena 63 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-04s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie).
Viñeta 4 — Escena 64 (Cole mansion terrace, snow falling over the lit garden): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie).
Viñeta 5 — Escena 65 (Cole mansion terrace, snow falling over the lit garden): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: sharp. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie).
Viñeta 6 — Escena 66 (Cole mansion terrace, snow falling over the lit garden): [00s-07s] two-shot, medium shot with Eleanor Cole and Madison Pierce: Eleanor Cole and Madison Pierce face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Madison Pierce, Eleanor Cole. No other characters appear. Identity anchors: Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_12.png — Minuto 12 (escenas 67–72)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 12 (Escenas 67 a 72) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 67 (Cole mansion kitchen, warm steel and hanging copper): [00s-04s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Valentina Reyes. June Alvarez is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes, June Alvarez. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow in her hair); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron).
Viñeta 2 — Escena 68 (Cole mansion kitchen, warm steel and hanging copper): [00s-07s] two-shot, medium shot with Walter Briggs and Valentina Reyes: Walter Briggs and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes, Walter Briggs, June Alvarez. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow in her hair); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron).
Viñeta 3 — Escena 69 (Cole mansion kitchen, warm steel and hanging copper): [00s-07s] two-shot, medium shot with Walter Briggs and Valentina Reyes: Walter Briggs and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes, Walter Briggs. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow in her hair); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform).
Viñeta 4 — Escena 70 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at June Alvarez. Nathaniel Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Nathaniel Cole, June Alvarez. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron).
Viñeta 5 — Escena 71 (Cole mansion wine cellar, stone stairs and a single bulb): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Walter Briggs. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the furnace. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform).
Viñeta 6 — Escena 72 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-04s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_13.png — Minuto 13 (escenas 73–78)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 13 (Escenas 73 a 78) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 73 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-04s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Eleanor Cole. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow in her hair); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls).
Viñeta 2 — Escena 74 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls).
Viñeta 3 — Escena 75 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Madison Pierce and Eleanor Cole: Madison Pierce and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Madison Pierce, Eleanor Cole. No other characters appear. Identity anchors: Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, white fur stole, diamonds); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls).
Viñeta 4 — Escena 76 (Cole mansion study, firelight and dark wood): [00s-07s] two-shot, medium shot with Eleanor Cole and Walter Briggs: Eleanor Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Eleanor Cole, Walter Briggs. No other characters appear. Identity anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform).
Viñeta 5 — Escena 77 (Cole mansion service hall, coat racks and mail slots): [00s-07s] two-shot, medium shot with Walter Briggs and June Alvarez: Walter Briggs and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the cellar key. Key object in frame: the foreground. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Walter Briggs, June Alvarez. No other characters appear. Identity anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron).
Viñeta 6 — Escena 78 (Cole mansion wine cellar, stone stairs and a single bulb): [00s-04s] close-up, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Walter Briggs. June Alvarez speaks as the camera holds close on their face, the red cookie tin catching the light between them. Key object in frame: sharp. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Walter Briggs, June Alvarez. No other characters appear. Identity anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_14.png — Minuto 14 (escenas 79–84)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 14 (Escenas 79 a 84) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 79 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-06s] two-shot, medium shot with June Alvarez and Walter Briggs: June Alvarez and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the library where Eleanor will not think to look. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Walter Briggs, June Alvarez. No other characters appear. Identity anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron).
Viñeta 2 — Escena 80 (Cole mansion service hall, coat racks and mail slots): [00s-07s] two-shot, medium shot with Walter Briggs and Nathaniel Cole: Walter Briggs and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform).
Viñeta 3 — Escena 81 (Cole mansion study, firelight and dark wood): [00s-03s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Nathaniel Cole. June Alvarez is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, June Alvarez. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron).
Viñeta 4 — Escena 82 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls).
Viñeta 5 — Escena 83 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-07s] two-shot, medium shot with Walter Briggs and Eleanor Cole: Walter Briggs and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the book cart. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Eleanor Cole, Walter Briggs. No other characters appear. Identity anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform).
Viñeta 6 — Escena 84 (Cole mansion terrace, snow falling over the lit garden): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at June Alvarez. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Nathaniel Cole, June Alvarez. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_15.png — Minuto 15 (escenas 85–90)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 15 (Escenas 85 a 90) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 85 (Cole mansion study, firelight and dark wood): [00s-07s] two-shot, medium shot with Walter Briggs and Nathaniel Cole: Walter Briggs and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank envelope. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform).
Viñeta 2 — Escena 86 (Cole mansion study, firelight and dark wood): [00s-03s] wide establishing shot, face and mouth visible: Walter Briggs is on camera with face and mouth fully visible, looking at Nathaniel Cole. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform).
Viñeta 3 — Escena 87 (Cole mansion study, firelight and dark wood): [00s-03s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Walter Briggs. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: sharp. Location: Cole mansion study, firelight and dark wood. Characters present: Eleanor Cole, Walter Briggs. No other characters appear. Identity anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform).
Viñeta 4 — Escena 88 (Cole mansion study, firelight and dark wood): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls).
Viñeta 5 — Escena 89 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie).
Viñeta 6 — Escena 90 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Madison Pierce and Eleanor Cole: Madison Pierce and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, white fur stole, diamonds); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_16.png — Minuto 16 (escenas 91–96)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 16 (Escenas 91 a 96) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 91 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Nathaniel Cole and Madison Pierce: Nathaniel Cole and Madison Pierce face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, white fur stole, diamonds).
Viñeta 2 — Escena 92 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-04s] close-up, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole speaks as the camera holds close on their face, the prenup catching the light between them. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon).
Viñeta 3 — Escena 93 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Madison Pierce and Nathaniel Cole: Madison Pierce and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the torn prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, white fur stole, diamonds).
Viñeta 4 — Escena 94 (Cole mansion study, firelight and dark wood): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie).
Viñeta 5 — Escena 95 (Cole mansion study, firelight and dark wood): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie).
Viñeta 6 — Escena 96 (Cole mansion study, firelight and dark wood): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_17.png — Minuto 17 (escenas 97–102)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 17 (Escenas 97 a 102) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 97 (Cole mansion study, firelight and dark wood): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the old letters. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie).
Viñeta 2 — Escena 98 (Cole mansion study, firelight and dark wood): [00s-03s] wide establishing shot, face and mouth visible: Walter Briggs is on camera with face and mouth fully visible, looking at Valentina Reyes. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole, Walter Briggs. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform).
Viñeta 3 — Escena 99 (Cole mansion study, firelight and dark wood): [00s-07s] two-shot, medium shot with Walter Briggs and Valentina Reyes: Walter Briggs and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Walter Briggs. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform).
Viñeta 4 — Escena 100 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon).
Viñeta 5 — Escena 101 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Madison Pierce. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, white fur stole, diamonds).
Viñeta 6 — Escena 102 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Eleanor Cole and Walter Briggs: Eleanor Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole, Walter Briggs. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_18.png — Minuto 18 (escenas 103–108)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 18 (Escenas 103 a 108) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 103 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the ballroom doors. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon).
Viñeta 2 — Escena 104 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-04s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie).
Viñeta 3 — Escena 105 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon).
Viñeta 4 — Escena 106 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Nathaniel Cole, June Alvarez. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron).
Viñeta 5 — Escena 107 (Cole mansion study, firelight and dark wood): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie).
Viñeta 6 — Escena 108 (Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows): [00s-07s] two-shot, medium shot with Eleanor Cole and Valentina Reyes: Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_19.png — Minuto 19 (escenas 109–114)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 19 (Escenas 109 a 114) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 109 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie).
Viñeta 2 — Escena 110 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-07s] two-shot, medium shot with Eleanor Cole and Valentina Reyes: Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the checkbook. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon).
Viñeta 3 — Escena 111 (Cole mansion library, lamplight and floor-to-ceiling books): [00s-07s] two-shot, medium shot with Valentina Reyes and Eleanor Cole: Valentina Reyes and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the checkbook. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds).
Viñeta 4 — Escena 112 (Cole mansion wine cellar, stone stairs and a single bulb): [00s-07s] two-shot, medium shot with Eleanor Cole and Walter Briggs: Eleanor Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Eleanor Cole, Walter Briggs. No other characters appear. Identity anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform).
Viñeta 5 — Escena 113 (Cole mansion wine cellar, stone stairs and a single bulb): [00s-07s] two-shot, medium shot with Walter Briggs and June Alvarez: Walter Briggs and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Walter Briggs, June Alvarez. No other characters appear. Identity anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing wool coat over her chef whites, red scarf).
Viñeta 6 — Escena 114 (Cole mansion wine cellar, stone stairs and a single bulb): [00s-03s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at June Alvarez. Eleanor Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the furnace. Key object in frame: sharp. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Eleanor Cole, June Alvarez. No other characters appear. Identity anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing wool coat over her chef whites, red scarf).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_20.png — Minuto 20 (escenas 115–120)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 20 (Escenas 115 a 120) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 115 (Cole mansion foyer, Christmas week, a giant half-decorated tree): [00s-07s] two-shot, medium shot with Eleanor Cole and Valentina Reyes: Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds).
Viñeta 2 — Escena 116 (Cole mansion foyer, Christmas week, a giant half-decorated tree): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the door. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds).
Viñeta 3 — Escena 117 (Cole mansion foyer, Christmas week, a giant half-decorated tree): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat).
Viñeta 4 — Escena 118 (Manhattan street, Christmas Eve, wet snow and yellow cabs): [00s-04s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Manhattan street, Christmas Eve, wet snow and yellow cabs, the action carrying over from the exact storyboard framing. Key object in frame: the train ticket. Key object in frame: the foreground. Location: Manhattan street, Christmas Eve, wet snow and yellow cabs. Characters present: Valentina Reyes. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin).
Viñeta 5 — Escena 119 (Cole mansion wine cellar, stone stairs and a single bulb): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at June Alvarez. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole, June Alvarez. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing wool coat over her chef whites, red scarf).
Viñeta 6 — Escena 120 (Cole mansion wine cellar, stone stairs and a single bulb): [00s-07s] two-shot, medium shot with Nathaniel Cole and Walter Briggs: Nathaniel Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the furnace. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_21.png — Minuto 21 (escenas 121–126)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 21 (Escenas 121 a 126) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 121 (Cole mansion wine cellar, stone stairs and a single bulb): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at the other person in frame. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat).
Viñeta 2 — Escena 122 (Cole mansion wine cellar, stone stairs and a single bulb): [00s-07s] two-shot, medium shot with June Alvarez and Nathaniel Cole: June Alvarez and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: a kitchen towel. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole, June Alvarez. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing wool coat over her chef whites, red scarf).
Viñeta 3 — Escena 123 (Cole mansion wine cellar, stone stairs and a single bulb): [00s-07s] two-shot, medium shot with Walter Briggs and Nathaniel Cole: Walter Briggs and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform).
Viñeta 4 — Escena 124 (Cole mansion foyer, Christmas week, a giant half-decorated tree): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds).
Viñeta 5 — Escena 125 (Cole mansion foyer, Christmas week, a giant half-decorated tree): [00s-07s] two-shot, medium shot with Madison Pierce and Eleanor Cole: Madison Pierce and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the torn prenup. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Madison Pierce, Eleanor Cole. No other characters appear. Identity anchors: Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown under a white fur coat); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds).
Viñeta 6 — Escena 126 (Cole mansion foyer, Christmas week, a giant half-decorated tree): [00s-07s] two-shot, medium shot with Eleanor Cole and June Alvarez: Eleanor Cole and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Eleanor Cole, June Alvarez. No other characters appear. Identity anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing wool coat over her chef whites, red scarf).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

### REF_GRID_MIN_22.png — Minuto 22 (escenas 127–132)

```text
Usando los personajes de REF_CAST_MASTER.png como referencia fija de rostros, edades, cuerpos y vestuarios, genera UNA IMAGEN horizontal 16:9 de Storyboard dividida en una cuadrícula limpia de 3x2 (6 viñetas numeradas del 1 al 6) que represente el MINUTO 22 (Escenas 127 a 132) de la historia en estilo Cinematográfico Realista 35mm:

Look visual: prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette.

Viñeta 1 — Escena 127 (Grand Central Station, midnight, snow on the marble floor): [00s-04s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the train ticket. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Valentina Reyes. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin).
Viñeta 2 — Escena 128 (Grand Central Station, midnight, snow on the marble floor): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat).
Viñeta 3 — Escena 129 (Grand Central Station, midnight, snow on the marble floor): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat).
Viñeta 4 — Escena 130 (Grand Central Station, midnight, snow on the marble floor): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear. Identity anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds).
Viñeta 5 — Escena 131 (Grand Central Station, midnight, snow on the marble floor): [00s-07s] two-shot, medium shot with Rosa Reyes and Valentina Reyes: Rosa Reyes and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Rosa Reyes is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Valentina Reyes, Rosa Reyes. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Rosa Reyes (Cast Sheet Pos #7: mid fifties; mother with dark wavy hair; wearing rust cardigan under a wool coat, warm slippers).
Viñeta 6 — Escena 132 (Grand Central Station, midnight, snow on the marble floor): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear. Identity anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat).

Mantén continuidad exacta de posiciones, rostros, cuerpos, vestuario, props, locaciones, luz y hora del día entre las 6 viñetas. Cada viñeta es el PRIMER FRAME literal de la Toma 1 de su escena: mismo encuadre, misma cámara, mismo blocking y mismo objeto clave; la acción ya está en movimiento, nunca congelada. Cada viñeta es un plano cinematográfico 16:9 con acción legible.
FORMATO DE VIÑETAS 100% VISUAL (SIN CAJAS DE TEXTO): Las 6 viñetas fotográficas en cuadrícula 3x2 deben ocupar el 100% del lienzo 16:9 separadas únicamente por líneas divisorias finas. Coloca SOLO el número pequeño [1], [2], [3], [4], [5], [6] en la esquina superior izquierda de cada viñeta. PROHIBIDO dibujar barras inferiores oscuras, subtítulos, cajas de texto o descripciones escritas dentro de la imagen.
```

---

## Paso 3 — Lotes Muse AI (22 videos de 1 minuto)

En cada lote: adjunta los dos archivos indicados y pega **un guion completo**
(16:9 para YouTube o 9:16 para Reels/Shorts). El guion ya termina con el comando final.

### Lote 01 — Minuto 1 (escenas 1–6)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_01.png`

**Adjuntos por escena de este lote:**

- Escena 001: `attach: [panel_001, ref_valentina, ref_nate, ref_madison]`
- Escena 002: `attach: [panel_002, ref_valentina, ref_nate, ref_madison]`
- Escena 003: `attach: [panel_003, ref_valentina, ref_rosa]`
- Escena 004: `attach: [panel_004, ref_nate, ref_eleanor]`
- Escena 005: `attach: [panel_005, ref_walter]`
- Escena 006: `attach: [panel_006, ref_eleanor, ref_june]`

**Guardar 16:9 como:** `raw_clips/minute_01.mp4`

**Guardar 9:16 como:** `raw_clips/minute_01_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 1 (Viñeta #1 del Storyboard) — 00:00–00:10
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Valentina Reyes, Nathaniel Cole, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Nathaniel Cole, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing ivory shearling coat, gold hoops, white gloves)
- Key Object: the crystal star ornament → Object In / Object Out: the crystal star ornament → the crystal star ornament
- Silent Present: Madison Pierce — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Do I know you?"
  VALENTINA (controlled, quiet): "You did. Six Christmases ago."

ESCENA 2 (Viñeta #2 del Storyboard) — 00:10–00:20
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Valentina Reyes, Nathaniel Cole, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Nathaniel Cole: Madison Pierce and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: a silver tray. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Nathaniel Cole, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing ivory shearling coat, gold hoops, white gloves)
- Key Object: a silver tray → Object In / Object Out: a silver tray → a silver tray
- Silent Present: Valentina Reyes — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Nathaniel Cole — Madison Pierce and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: a silver tray  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, a silver tray catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, a silver tray sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: MADISON — bright, polished American English with a competitive edge; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "Staff should use the service entrance."
  NATE (controlled, quiet): "She stays until the house is finished."

ESCENA 3 (Viñeta #3 del Storyboard) — 00:20–00:30
- Location: Reyes house, warm kitchen, a small tree with one crystal star
- Characters Present: Valentina Reyes, Rosa Reyes
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Rosa Reyes. Valentina Reyes is already moving through Reyes house, warm kitchen, a small tree with one crystal star, the action carrying over from the exact storyboard framing. Key object in frame: the twin crystal star. Location: Reyes house, warm kitchen, a small tree with one crystal star. Characters present: Valentina Reyes, Rosa Reyes. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Rosa Reyes (Cast Sheet Pos #7: mid fifties; mother with dark wavy hair; wearing rust cardigan, flour on her sleeve, warm slippers)
- Key Object: the twin crystal star → Object In / Object Out: the twin crystal star → the twin crystal star
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Rosa Reyes. Valentina Reyes is already moving through Reyes house, warm kitchen, a small tree with one crystal star, the action carrying over from the exact storyboard framing. Key object in frame: the twin crystal star  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the twin crystal star is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-09s]: medium close-up on Rosa Reyes, face and mouth visible — Rosa Reyes is on camera with face and mouth fully visible, looking at Valentina Reyes. Rosa Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [09s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the twin crystal star catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): radio carol, cocoa steaming, a neighbor's dog. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; ROSA — soft, warm American English with a protective edge
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "He looked right through me, Mama."
  ROSA (controlled, quiet): "Then let him. We survived six years without him."

ESCENA 4 (Viñeta #4 del Storyboard) — 00:30–00:40
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-08s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon)
- Key Object: the crystal star ornament → Object In / Object Out: the crystal star ornament → the crystal star ornament
- Camera Cuts & Visual Action (10s):
  * [00s-08s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-09s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [09s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "That girl married a sailor two months after you left, son."
  NATE (controlled, quiet): "Then why did she keep my ornament?"

ESCENA 5 (Viñeta #5 del Storyboard) — 00:40–00:50
- Location: Cole mansion service hall, coat racks and mail slots
- Characters Present: Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Walter Briggs is on camera with face and mouth fully visible, looking at the other person in frame. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Walter Briggs. No other characters appear.
- Identity Anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes)
- Key Object: the old letter → Object In / Object Out: the old letter → the old letter
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at the other person in frame. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the old letter  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the old letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: close-up, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at the other person in frame. Walter Briggs speaks as the camera holds close on their face, the old letter catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — The silence hangs, the old letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): mail slot clatter, coats brushing, distant music. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "Six years of lies in a cookie tin."
  WALTER (controlled, quiet): "God forgive me."

ESCENA 6 (Viñeta #6 del Storyboard) — 00:50–01:00
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Eleanor Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at June Alvarez. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Eleanor Cole, June Alvarez. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the red cookie tin → Object In / Object Out: the red cookie tin → the red cookie tin
- Silent Present: June Alvarez — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at June Alvarez. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the red cookie tin is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: close-up, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Madison Pierce. Eleanor Cole speaks as the camera holds close on their face, the red cookie tin catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — June Alvarez holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Seventy-two letters, and he never read one."
  ELEANOR (controlled, quiet): "My son marries Madison on Christmas Eve."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 1 (Viñeta #1 del Storyboard) — 00:00–00:10
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Valentina Reyes, Nathaniel Cole, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Nathaniel Cole, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing ivory shearling coat, gold hoops, white gloves)
- Key Object: the crystal star ornament → Object In / Object Out: the crystal star ornament → the crystal star ornament
- Silent Present: Madison Pierce — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Do I know you?"
  VALENTINA (controlled, quiet): "You did. Six Christmases ago."

ESCENA 2 (Viñeta #2 del Storyboard) — 00:10–00:20
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Valentina Reyes, Nathaniel Cole, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Nathaniel Cole: Madison Pierce and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: a silver tray. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Nathaniel Cole, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing ivory shearling coat, gold hoops, white gloves)
- Key Object: a silver tray → Object In / Object Out: a silver tray → a silver tray
- Silent Present: Valentina Reyes — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Nathaniel Cole — Madison Pierce and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: a silver tray  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, a silver tray catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, a silver tray sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: MADISON — bright, polished American English with a competitive edge; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "Staff should use the service entrance."
  NATE (controlled, quiet): "She stays until the house is finished."

ESCENA 3 (Viñeta #3 del Storyboard) — 00:20–00:30
- Location: Reyes house, warm kitchen, a small tree with one crystal star
- Characters Present: Valentina Reyes, Rosa Reyes
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Rosa Reyes. Valentina Reyes is already moving through Reyes house, warm kitchen, a small tree with one crystal star, the action carrying over from the exact storyboard framing. Key object in frame: the twin crystal star. Location: Reyes house, warm kitchen, a small tree with one crystal star. Characters present: Valentina Reyes, Rosa Reyes. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Rosa Reyes (Cast Sheet Pos #7: mid fifties; mother with dark wavy hair; wearing rust cardigan, flour on her sleeve, warm slippers)
- Key Object: the twin crystal star → Object In / Object Out: the twin crystal star → the twin crystal star
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Rosa Reyes. Valentina Reyes is already moving through Reyes house, warm kitchen, a small tree with one crystal star, the action carrying over from the exact storyboard framing. Key object in frame: the twin crystal star  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the twin crystal star is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-09s]: medium close-up on Rosa Reyes, face and mouth visible — Rosa Reyes is on camera with face and mouth fully visible, looking at Valentina Reyes. Rosa Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [09s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the twin crystal star catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): radio carol, cocoa steaming, a neighbor's dog. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; ROSA — soft, warm American English with a protective edge
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "He looked right through me, Mama."
  ROSA (controlled, quiet): "Then let him. We survived six years without him."

ESCENA 4 (Viñeta #4 del Storyboard) — 00:30–00:40
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-08s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon)
- Key Object: the crystal star ornament → Object In / Object Out: the crystal star ornament → the crystal star ornament
- Camera Cuts & Visual Action (10s):
  * [00s-08s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-09s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [09s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "That girl married a sailor two months after you left, son."
  NATE (controlled, quiet): "Then why did she keep my ornament?"

ESCENA 5 (Viñeta #5 del Storyboard) — 00:40–00:50
- Location: Cole mansion service hall, coat racks and mail slots
- Characters Present: Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Walter Briggs is on camera with face and mouth fully visible, looking at the other person in frame. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Walter Briggs. No other characters appear.
- Identity Anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes)
- Key Object: the old letter → Object In / Object Out: the old letter → the old letter
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at the other person in frame. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the old letter  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the old letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: close-up, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at the other person in frame. Walter Briggs speaks as the camera holds close on their face, the old letter catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — The silence hangs, the old letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): mail slot clatter, coats brushing, distant music. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "Six years of lies in a cookie tin."
  WALTER (controlled, quiet): "God forgive me."

ESCENA 6 (Viñeta #6 del Storyboard) — 00:50–01:00
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Eleanor Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at June Alvarez. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Eleanor Cole, June Alvarez. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the red cookie tin → Object In / Object Out: the red cookie tin → the red cookie tin
- Silent Present: June Alvarez — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at June Alvarez. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the red cookie tin is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: close-up, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Madison Pierce. Eleanor Cole speaks as the camera holds close on their face, the red cookie tin catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — June Alvarez holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Seventy-two letters, and he never read one."
  ELEANOR (controlled, quiet): "My son marries Madison on Christmas Eve."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 02 — Minuto 2 (escenas 7–12)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_02.png`

**Adjuntos por escena de este lote:**

- Escena 007: `attach: [panel_007, ref_eleanor, ref_june]`
- Escena 008: `attach: [panel_008, ref_june]`
- Escena 009: `attach: [panel_009, ref_walter, ref_june]`
- Escena 010: `attach: [panel_010, ref_walter]`
- Escena 011: `attach: [panel_011, ref_june]`
- Escena 012: `attach: [panel_012, ref_eleanor, ref_june]`

**Guardar 16:9 como:** `raw_clips/minute_02.mp4`

**Guardar 9:16 como:** `raw_clips/minute_02_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 7 (Viñeta #7 del Storyboard) — 01:00–01:10
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Eleanor Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-08s] two-shot, medium shot with Eleanor Cole and June Alvarez: Eleanor Cole and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Eleanor Cole, June Alvarez. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the red cookie tin → Object In / Object Out: the red cookie tin → the red cookie tin
- Camera Cuts & Visual Action (10s):
  * [00s-08s]: two-shot, medium shot with Eleanor Cole and June Alvarez — Eleanor Cole and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-09s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [09s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: ELEANOR — low, polished American English, never raises her voice; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "You saw nothing, June. You cook, you clean, you forget."
  JUNE (controlled, quiet): "I have forgotten six years of things, ma'am."

ESCENA 8 (Viñeta #8 del Storyboard) — 01:10–01:20
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: June Alvarez. No other characters appear.
- Identity Anchors: June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the red cookie tin → Object In / Object Out: the red cookie tin → the red cookie tin
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the red cookie tin is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: close-up, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez speaks as the camera holds close on their face, the red cookie tin catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — The silence hangs, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "Seventy-two letters. All still sealed."
  JUNE (controlled, quiet): "That woman stole a marriage."

ESCENA 9 (Viñeta #9 del Storyboard) — 01:20–01:30
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] close-up, face and mouth visible: Walter Briggs is on camera with face and mouth fully visible, looking at June Alvarez. Walter Briggs speaks as the camera holds close on their face, the old letter catching the light between them. Location: Cole mansion library, lamplight and floor-to-ceiling books. Key object: the old letter. Characters present: Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the old letter → Object In / Object Out: the old letter → the old letter
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: close-up, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at June Alvarez. Walter Briggs speaks as the camera holds close on their face, the old letter catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the old letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-09s]: wide establishing shot, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Walter Briggs. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the old letter  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [09s-10s]: tight close-up — Walter Briggs holds the silence after the line, the old letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "You should forget what you saw."
  JUNE (controlled, quiet): "Then why do you keep your coat buttoned indoors?"

ESCENA 10 (Viñeta #10 del Storyboard) — 01:30–01:40
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-05s] wide establishing shot, face and mouth visible: Walter Briggs is on camera with face and mouth fully visible, looking at the other person in frame. Walter Briggs is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Walter Briggs. No other characters appear.
- Identity Anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes)
- Key Object: the old letter → Object In / Object Out: the old letter → the old letter
- Camera Cuts & Visual Action (10s):
  * [00s-05s]: wide establishing shot, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at the other person in frame. Walter Briggs is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the old letter  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [05s-08s]: close-up, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at the other person in frame. Walter Briggs speaks as the camera holds close on their face, the old letter catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — The silence hangs, the old letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "One letter. If I burn one, the rest are just paper."
  WALTER (controlled, quiet): "God help me, I can't."

ESCENA 11 (Viñeta #11 del Storyboard) — 01:40–01:50
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-05s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: June Alvarez. No other characters appear.
- Identity Anchors: June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the old letter → Object In / Object Out: the old letter → the old letter
- Camera Cuts & Visual Action (10s):
  * [00s-05s]: wide establishing shot, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the old letter  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [05s-07s]: tight close-up of the story object, centered — the old letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [07s-09s]: close-up, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez speaks as the camera holds close on their face, the old letter catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [09s-10s]: tight close-up — The silence hangs, the old letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "A man who hides letters in a wine cellar is already confessing."
  JUNE (controlled, quiet): "I can wait."

ESCENA 12 (Viñeta #12 del Storyboard) — 01:50–02:00
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Eleanor Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and June Alvarez: Eleanor Cole and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Eleanor Cole, June Alvarez. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the red cookie tin → Object In / Object Out: the red cookie tin → the red cookie tin
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and June Alvarez — Eleanor Cole and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: ELEANOR — low, polished American English, never raises her voice; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "One envelope is missing."
  JUNE (controlled, quiet): "Perhaps the fire took it."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 7 (Viñeta #7 del Storyboard) — 01:00–01:10
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Eleanor Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-08s] two-shot, medium shot with Eleanor Cole and June Alvarez: Eleanor Cole and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Eleanor Cole, June Alvarez. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the red cookie tin → Object In / Object Out: the red cookie tin → the red cookie tin
- Camera Cuts & Visual Action (10s):
  * [00s-08s]: two-shot, medium shot with Eleanor Cole and June Alvarez — Eleanor Cole and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-09s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [09s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: ELEANOR — low, polished American English, never raises her voice; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "You saw nothing, June. You cook, you clean, you forget."
  JUNE (controlled, quiet): "I have forgotten six years of things, ma'am."

ESCENA 8 (Viñeta #8 del Storyboard) — 01:10–01:20
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: June Alvarez. No other characters appear.
- Identity Anchors: June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the red cookie tin → Object In / Object Out: the red cookie tin → the red cookie tin
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the red cookie tin is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: close-up, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez speaks as the camera holds close on their face, the red cookie tin catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — The silence hangs, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "Seventy-two letters. All still sealed."
  JUNE (controlled, quiet): "That woman stole a marriage."

ESCENA 9 (Viñeta #9 del Storyboard) — 01:20–01:30
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] close-up, face and mouth visible: Walter Briggs is on camera with face and mouth fully visible, looking at June Alvarez. Walter Briggs speaks as the camera holds close on their face, the old letter catching the light between them. Location: Cole mansion library, lamplight and floor-to-ceiling books. Key object: the old letter. Characters present: Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the old letter → Object In / Object Out: the old letter → the old letter
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: close-up, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at June Alvarez. Walter Briggs speaks as the camera holds close on their face, the old letter catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the old letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-09s]: wide establishing shot, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Walter Briggs. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the old letter  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [09s-10s]: tight close-up — Walter Briggs holds the silence after the line, the old letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "You should forget what you saw."
  JUNE (controlled, quiet): "Then why do you keep your coat buttoned indoors?"

ESCENA 10 (Viñeta #10 del Storyboard) — 01:30–01:40
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-05s] wide establishing shot, face and mouth visible: Walter Briggs is on camera with face and mouth fully visible, looking at the other person in frame. Walter Briggs is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Walter Briggs. No other characters appear.
- Identity Anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes)
- Key Object: the old letter → Object In / Object Out: the old letter → the old letter
- Camera Cuts & Visual Action (10s):
  * [00s-05s]: wide establishing shot, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at the other person in frame. Walter Briggs is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the old letter  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [05s-08s]: close-up, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at the other person in frame. Walter Briggs speaks as the camera holds close on their face, the old letter catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — The silence hangs, the old letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "One letter. If I burn one, the rest are just paper."
  WALTER (controlled, quiet): "God help me, I can't."

ESCENA 11 (Viñeta #11 del Storyboard) — 01:40–01:50
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-05s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: June Alvarez. No other characters appear.
- Identity Anchors: June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the old letter → Object In / Object Out: the old letter → the old letter
- Camera Cuts & Visual Action (10s):
  * [00s-05s]: wide establishing shot, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the old letter  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [05s-07s]: tight close-up of the story object, centered — the old letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [07s-09s]: close-up, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez speaks as the camera holds close on their face, the old letter catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [09s-10s]: tight close-up — The silence hangs, the old letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "A man who hides letters in a wine cellar is already confessing."
  JUNE (controlled, quiet): "I can wait."

ESCENA 12 (Viñeta #12 del Storyboard) — 01:50–02:00
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Eleanor Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and June Alvarez: Eleanor Cole and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Eleanor Cole, June Alvarez. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the red cookie tin → Object In / Object Out: the red cookie tin → the red cookie tin
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and June Alvarez — Eleanor Cole and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: ELEANOR — low, polished American English, never raises her voice; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "One envelope is missing."
  JUNE (controlled, quiet): "Perhaps the fire took it."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 03 — Minuto 3 (escenas 13–18)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_03.png`

**Adjuntos por escena de este lote:**

- Escena 013: `attach: [panel_013, ref_valentina, ref_june]`
- Escena 014: `attach: [panel_014, ref_valentina, ref_eleanor]`
- Escena 015: `attach: [panel_015, ref_valentina, ref_june]`
- Escena 016: `attach: [panel_016, ref_valentina, ref_madison]`
- Escena 017: `attach: [panel_017, ref_valentina, ref_nate]`
- Escena 018: `attach: [panel_018, ref_nate, ref_madison, ref_eleanor]`

**Guardar 16:9 como:** `raw_clips/minute_03.mp4`

**Guardar 9:16 como:** `raw_clips/minute_03_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 13 (Viñeta #13 del Storyboard) — 02:00–02:10
- Location: Cole mansion kitchen, warm steel and hanging copper
- Characters Present: Valentina Reyes, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-06s] two-shot, medium shot with June Alvarez and Valentina Reyes: June Alvarez and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the delivery slip. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the foreground → Object In / Object Out: the foreground → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-06s]: two-shot, medium shot with June Alvarez and Valentina Reyes — June Alvarez and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the delivery slip. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [06s-08s]: tight close-up of the story object, centered — A silent insert shows sharp being placed inside the foreground; no face in this shot.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-09s]: close-up — June Alvarez stays silent as the camera holds close on their face, the delivery slip catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [09s-10s]: tight close-up — June Alvarez holds the silence after the line, the delivery slip sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): copper pots, running water, a radio carol. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "You are the decorator Eleanor hired?"
  VALENTINA (controlled, quiet): "She hired me before she knew my name."

ESCENA 14 (Viñeta #14 del Storyboard) — 02:10–02:20
- Location: Cole mansion service hall, coat racks and mail slots
- Characters Present: Valentina Reyes, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-08s] two-shot, medium shot with Eleanor Cole and Valentina Reyes: Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: a silver box of ornaments. Key object in frame: the foreground. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-08s]: two-shot, medium shot with Eleanor Cole and Valentina Reyes — Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: a silver box of ornaments. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-09s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, a silver box of ornaments catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [09s-10s]: tight close-up — Eleanor Cole holds the silence after the line, a silver box of ornaments sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): mail slot clatter, coats brushing, distant music. Voice tone: ELEANOR — low, polished American English, never raises her voice; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "You will use the service stairs. The guests use the front."
  VALENTINA (controlled, quiet): "Then I'll make the service stairs beautiful."

ESCENA 15 (Viñeta #15 del Storyboard) — 02:20–02:30
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with June Alvarez and Valentina Reyes: June Alvarez and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: a stack of law books. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with June Alvarez and Valentina Reyes — June Alvarez and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: a stack of law books. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — June Alvarez stays silent as the camera holds close on their face, a stack of law books catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — June Alvarez holds the silence after the line, a stack of law books sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "That woman keeps everything she takes."
  VALENTINA (controlled, quiet): "I'm not here to take anything back."

ESCENA 16 (Viñeta #16 del Storyboard) — 02:30–02:40
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Valentina Reyes, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Valentina Reyes: Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: a silver tray. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing ivory shearling coat, gold hoops, white gloves)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Valentina Reyes — Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: a silver tray. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, a silver tray catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, a silver tray sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: MADISON — bright, polished American English with a competitive edge; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "The help doesn't touch the champagne."
  VALENTINA (controlled, quiet): "Then you'll have to pour it yourself."

ESCENA 17 (Viñeta #17 del Storyboard) — 02:40–02:50
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: a silver box of ornaments. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: a silver box of ornaments. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, a silver box of ornaments catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, a silver box of ornaments sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "You disappeared without a word."
  VALENTINA (controlled, quiet): "Your mother made sure of that."

ESCENA 18 (Viñeta #18 del Storyboard) — 02:50–03:00
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, Madison Pierce, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the wedding invitation. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Madison Pierce, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing ivory shearling coat, gold hoops, white gloves); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: Madison Pierce — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the wedding invitation. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the wedding invitation catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the wedding invitation sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "The gala is in three days. We announce the wedding there."
  NATE (controlled, quiet): "You've already announced it."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 13 (Viñeta #13 del Storyboard) — 02:00–02:10
- Location: Cole mansion kitchen, warm steel and hanging copper
- Characters Present: Valentina Reyes, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-06s] two-shot, medium shot with June Alvarez and Valentina Reyes: June Alvarez and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the delivery slip. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the foreground → Object In / Object Out: the foreground → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-06s]: two-shot, medium shot with June Alvarez and Valentina Reyes — June Alvarez and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the delivery slip. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [06s-08s]: tight close-up of the story object, centered — A silent insert shows sharp being placed inside the foreground; no face in this shot.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-09s]: close-up — June Alvarez stays silent as the camera holds close on their face, the delivery slip catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [09s-10s]: tight close-up — June Alvarez holds the silence after the line, the delivery slip sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): copper pots, running water, a radio carol. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "You are the decorator Eleanor hired?"
  VALENTINA (controlled, quiet): "She hired me before she knew my name."

ESCENA 14 (Viñeta #14 del Storyboard) — 02:10–02:20
- Location: Cole mansion service hall, coat racks and mail slots
- Characters Present: Valentina Reyes, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-08s] two-shot, medium shot with Eleanor Cole and Valentina Reyes: Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: a silver box of ornaments. Key object in frame: the foreground. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-08s]: two-shot, medium shot with Eleanor Cole and Valentina Reyes — Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: a silver box of ornaments. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-09s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, a silver box of ornaments catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [09s-10s]: tight close-up — Eleanor Cole holds the silence after the line, a silver box of ornaments sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): mail slot clatter, coats brushing, distant music. Voice tone: ELEANOR — low, polished American English, never raises her voice; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "You will use the service stairs. The guests use the front."
  VALENTINA (controlled, quiet): "Then I'll make the service stairs beautiful."

ESCENA 15 (Viñeta #15 del Storyboard) — 02:20–02:30
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with June Alvarez and Valentina Reyes: June Alvarez and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: a stack of law books. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with June Alvarez and Valentina Reyes — June Alvarez and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: a stack of law books. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — June Alvarez stays silent as the camera holds close on their face, a stack of law books catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — June Alvarez holds the silence after the line, a stack of law books sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "That woman keeps everything she takes."
  VALENTINA (controlled, quiet): "I'm not here to take anything back."

ESCENA 16 (Viñeta #16 del Storyboard) — 02:30–02:40
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Valentina Reyes, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Valentina Reyes: Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: a silver tray. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing ivory shearling coat, gold hoops, white gloves)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Valentina Reyes — Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: a silver tray. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, a silver tray catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, a silver tray sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: MADISON — bright, polished American English with a competitive edge; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "The help doesn't touch the champagne."
  VALENTINA (controlled, quiet): "Then you'll have to pour it yourself."

ESCENA 17 (Viñeta #17 del Storyboard) — 02:40–02:50
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: a silver box of ornaments. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: a silver box of ornaments. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, a silver box of ornaments catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, a silver box of ornaments sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "You disappeared without a word."
  VALENTINA (controlled, quiet): "Your mother made sure of that."

ESCENA 18 (Viñeta #18 del Storyboard) — 02:50–03:00
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, Madison Pierce, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the wedding invitation. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Madison Pierce, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing ivory shearling coat, gold hoops, white gloves); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: Madison Pierce — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the wedding invitation. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the wedding invitation catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the wedding invitation sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "The gala is in three days. We announce the wedding there."
  NATE (controlled, quiet): "You've already announced it."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 04 — Minuto 4 (escenas 19–24)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_04.png`

**Adjuntos por escena de este lote:**

- Escena 019: `attach: [panel_019, ref_nate, ref_eleanor]`
- Escena 020: `attach: [panel_020, ref_valentina, ref_nate]`
- Escena 021: `attach: [panel_021, ref_valentina]`
- Escena 022: `attach: [panel_022, ref_valentina, ref_nate]`
- Escena 023: `attach: [panel_023, ref_nate, ref_eleanor]`
- Escena 024: `attach: [panel_024, ref_nate]`

**Guardar 16:9 como:** `raw_clips/minute_04.mp4`

**Guardar 9:16 como:** `raw_clips/minute_04_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 19 (Viñeta #19 del Storyboard) — 03:00–03:10
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Eleanor Cole — Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: NATE — low, clipped American English, warmth held under restraint; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "She kept my ornament. That isn't nothing."
  ELEANOR (controlled, quiet): "Sentiment is how poor men stay poor."

ESCENA 20 (Viñeta #20 del Storyboard) — 03:10–03:20
- Location: Cole mansion terrace, snow falling over the lit garden
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: a string of lights. Key object in frame: the foreground. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: a string of lights. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, a string of lights catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, a string of lights sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, snow, muffled music behind glass. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "My mother says you married a sailor."
  VALENTINA (controlled, quiet): "Your mother says a lot of things."

ESCENA 21 (Viñeta #21 del Storyboard) — 03:20–03:30
- Location: Cole mansion terrace, snow falling over the lit garden
- Characters Present: Valentina Reyes
- Storyboard Panel (Shot 1 exact framing): [00s-07s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the phone. Key object in frame: the foreground. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Valentina Reyes. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the phone. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the phone catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — The silence hangs, the phone sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, snow, muffled music behind glass. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "He asked me to meet him. I should ask about the letters."

ESCENA 22 (Viñeta #22 del Storyboard) — 03:30–03:40
- Location: Cole mansion terrace, snow falling over the lit garden
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, snow, muffled music behind glass. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "There was never a sailor, was there?"
  VALENTINA (controlled, quiet): "There was a letter. Seventy-two of them."

ESCENA 23 (Viñeta #23 del Storyboard) — 03:40–03:50
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Eleanor Cole. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing emerald gown, pearl necklace, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Eleanor Cole. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-06s]: tight close-up of the story object, centered — the crystal star ornament is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Eleanor Cole, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: NATE — low, clipped American English, warmth held under restraint; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "What letters did you take from me?"
  ELEANOR (controlled, quiet): "You were nineteen. She was nobody."

ESCENA 24 (Viñeta #24 del Storyboard) — 03:50–04:00
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at the other person in frame. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: sharp. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at the other person in frame. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: close-up, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at the other person in frame. nate speaks as the camera holds close on their face, the crystal star ornament catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — Nathaniel Cole holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "You kept it. All these years."
  NATE (controlled, quiet): "What else did you keep?"

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 19 (Viñeta #19 del Storyboard) — 03:00–03:10
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing midnight-blue dress, pearls, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Eleanor Cole — Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: NATE — low, clipped American English, warmth held under restraint; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "She kept my ornament. That isn't nothing."
  ELEANOR (controlled, quiet): "Sentiment is how poor men stay poor."

ESCENA 20 (Viñeta #20 del Storyboard) — 03:10–03:20
- Location: Cole mansion terrace, snow falling over the lit garden
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: a string of lights. Key object in frame: the foreground. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: a string of lights. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, a string of lights catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, a string of lights sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, snow, muffled music behind glass. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "My mother says you married a sailor."
  VALENTINA (controlled, quiet): "Your mother says a lot of things."

ESCENA 21 (Viñeta #21 del Storyboard) — 03:20–03:30
- Location: Cole mansion terrace, snow falling over the lit garden
- Characters Present: Valentina Reyes
- Storyboard Panel (Shot 1 exact framing): [00s-07s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the phone. Key object in frame: the foreground. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Valentina Reyes. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the phone. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the phone catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — The silence hangs, the phone sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, snow, muffled music behind glass. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "He asked me to meet him. I should ask about the letters."

ESCENA 22 (Viñeta #22 del Storyboard) — 03:30–03:40
- Location: Cole mansion terrace, snow falling over the lit garden
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing cream cashmere turtleneck, dark tailored trousers, pearl studs); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing charcoal overcoat over a black suit, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, snow, muffled music behind glass. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "There was never a sailor, was there?"
  VALENTINA (controlled, quiet): "There was a letter. Seventy-two of them."

ESCENA 23 (Viñeta #23 del Storyboard) — 03:40–03:50
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Eleanor Cole. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing emerald gown, pearl necklace, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Eleanor Cole. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-06s]: tight close-up of the story object, centered — the crystal star ornament is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Eleanor Cole, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: NATE — low, clipped American English, warmth held under restraint; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "What letters did you take from me?"
  ELEANOR (controlled, quiet): "You were nineteen. She was nobody."

ESCENA 24 (Viñeta #24 del Storyboard) — 03:50–04:00
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at the other person in frame. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: sharp. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at the other person in frame. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: close-up, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at the other person in frame. nate speaks as the camera holds close on their face, the crystal star ornament catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — Nathaniel Cole holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "You kept it. All these years."
  NATE (controlled, quiet): "What else did you keep?"

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 05 — Minuto 5 (escenas 25–30)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_05.png`

**Adjuntos por escena de este lote:**

- Escena 025: `attach: [panel_025, ref_valentina, ref_madison]`
- Escena 026: `attach: [panel_026, ref_valentina, ref_nate]`
- Escena 027: `attach: [panel_027, ref_valentina, ref_madison]`
- Escena 028: `attach: [panel_028, ref_valentina, ref_walter]`
- Escena 029: `attach: [panel_029, ref_valentina, ref_walter, ref_june]`
- Escena 030: `attach: [panel_030, ref_nate, ref_madison]`

**Guardar 16:9 como:** `raw_clips/minute_05.mp4`

**Guardar 9:16 como:** `raw_clips/minute_05_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 25 (Viñeta #25 del Storyboard) — 04:00–04:10
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Madison Pierce is on camera with face and mouth fully visible, looking at Valentina Reyes. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the white tablecloth. Key object in frame: sharp. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing champagne gown, diamond drop earrings, white fur stole)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Madison Pierce is on camera with face and mouth fully visible, looking at Valentina Reyes. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the white tablecloth. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Madison Pierce. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the white tablecloth catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "Everything white. No red, no pine, no sentiment."
  VALENTINA (controlled, quiet): "Then it won't look like Christmas."

ESCENA 26 (Viñeta #26 del Storyboard) — 04:10–04:20
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the delivery invoice. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the delivery invoice. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the delivery invoice is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-09s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the delivery invoice catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "You still sign with a star."
  VALENTINA (controlled, quiet): "Some habits survive."

ESCENA 27 (Viñeta #27 del Storyboard) — 04:20–04:30
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Valentina Reyes: Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the champagne coupe. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing champagne gown, diamond drop earrings, white fur stole)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Valentina Reyes — Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the champagne coupe. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the champagne coupe catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, the champagne coupe sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "He's mine in three days. Enjoy the decorations."
  VALENTINA (controlled, quiet): "I'm here for the receipts, not the ring."

ESCENA 28 (Viñeta #28 del Storyboard) — 04:30–04:40
- Location: Cole mansion service hall, coat racks and mail slots
- Characters Present: Valentina Reyes, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Walter Briggs. Valentina Reyes is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: sharp. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Valentina Reyes, Walter Briggs. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Walter Briggs. Valentina Reyes is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on Walter Briggs, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at Valentina Reyes. Walter Briggs holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the old letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): mail slot clatter, coats brushing, distant music. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "This is my handwriting."
  WALTER (controlled, quiet): "You should give that to me."

ESCENA 29 (Viñeta #29 del Storyboard) — 04:40–04:50
- Location: Cole mansion service hall, coat racks and mail slots
- Characters Present: Valentina Reyes, Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] close-up, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Walter Briggs. June Alvarez speaks as the camera holds close on their face, the cellar key catching the light between them. Key object in frame: sharp. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Valentina Reyes, Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Silent Present: Walter Briggs — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: close-up, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Walter Briggs. June Alvarez speaks as the camera holds close on their face, the cellar key catching the light between them. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the cellar key  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — June Alvarez holds the silence after the line, the cellar key sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): mail slot clatter, coats brushing, distant music. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "Walter keeps what he can't burn."
  VALENTINA (controlled, quiet): "Then I need to see his cellar."

ESCENA 30 (Viñeta #30 del Storyboard) — 04:50–05:00
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Madison Pierce is on camera with face and mouth fully visible, looking at Nathaniel Cole. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the delivery invoice. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing champagne gown, diamond drop earrings, white fur stole)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Madison Pierce is on camera with face and mouth fully visible, looking at Nathaniel Cole. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the delivery invoice. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the delivery invoice is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Madison Pierce. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the delivery invoice catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "Why does she sign her work with a star?"
  NATE (controlled, quiet): "Because I gave her one."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 25 (Viñeta #25 del Storyboard) — 04:00–04:10
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Madison Pierce is on camera with face and mouth fully visible, looking at Valentina Reyes. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the white tablecloth. Key object in frame: sharp. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing champagne gown, diamond drop earrings, white fur stole)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Madison Pierce is on camera with face and mouth fully visible, looking at Valentina Reyes. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the white tablecloth. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Madison Pierce. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the white tablecloth catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "Everything white. No red, no pine, no sentiment."
  VALENTINA (controlled, quiet): "Then it won't look like Christmas."

ESCENA 26 (Viñeta #26 del Storyboard) — 04:10–04:20
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the delivery invoice. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the delivery invoice. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the delivery invoice is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-09s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the delivery invoice catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "You still sign with a star."
  VALENTINA (controlled, quiet): "Some habits survive."

ESCENA 27 (Viñeta #27 del Storyboard) — 04:20–04:30
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Valentina Reyes: Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the champagne coupe. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing champagne gown, diamond drop earrings, white fur stole)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Valentina Reyes — Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the champagne coupe. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the champagne coupe catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, the champagne coupe sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "He's mine in three days. Enjoy the decorations."
  VALENTINA (controlled, quiet): "I'm here for the receipts, not the ring."

ESCENA 28 (Viñeta #28 del Storyboard) — 04:30–04:40
- Location: Cole mansion service hall, coat racks and mail slots
- Characters Present: Valentina Reyes, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Walter Briggs. Valentina Reyes is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: sharp. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Valentina Reyes, Walter Briggs. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Walter Briggs. Valentina Reyes is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on Walter Briggs, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at Valentina Reyes. Walter Briggs holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the old letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): mail slot clatter, coats brushing, distant music. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "This is my handwriting."
  WALTER (controlled, quiet): "You should give that to me."

ESCENA 29 (Viñeta #29 del Storyboard) — 04:40–04:50
- Location: Cole mansion service hall, coat racks and mail slots
- Characters Present: Valentina Reyes, Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] close-up, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Walter Briggs. June Alvarez speaks as the camera holds close on their face, the cellar key catching the light between them. Key object in frame: sharp. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Valentina Reyes, Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Silent Present: Walter Briggs — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: close-up, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Walter Briggs. June Alvarez speaks as the camera holds close on their face, the cellar key catching the light between them. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the cellar key  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — June Alvarez holds the silence after the line, the cellar key sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): mail slot clatter, coats brushing, distant music. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "Walter keeps what he can't burn."
  VALENTINA (controlled, quiet): "Then I need to see his cellar."

ESCENA 30 (Viñeta #30 del Storyboard) — 04:50–05:00
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Madison Pierce is on camera with face and mouth fully visible, looking at Nathaniel Cole. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the delivery invoice. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing champagne gown, diamond drop earrings, white fur stole)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Madison Pierce is on camera with face and mouth fully visible, looking at Nathaniel Cole. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the delivery invoice. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the delivery invoice is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Madison Pierce. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the delivery invoice catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "Why does she sign her work with a star?"
  NATE (controlled, quiet): "Because I gave her one."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 06 — Minuto 6 (escenas 31–36)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_06.png`

**Adjuntos por escena de este lote:**

- Escena 031: `attach: [panel_031, ref_valentina, ref_nate]`
- Escena 032: `attach: [panel_032, ref_valentina, ref_nate]`
- Escena 033: `attach: [panel_033, ref_nate, ref_eleanor]`
- Escena 034: `attach: [panel_034, ref_nate, ref_walter]`
- Escena 035: `attach: [panel_035, ref_eleanor, ref_walter]`
- Escena 036: `attach: [panel_036, ref_valentina, ref_nate]`

**Guardar 16:9 como:** `raw_clips/minute_06.mp4`

**Guardar 9:16 como:** `raw_clips/minute_06_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 31 (Viñeta #31 del Storyboard) — 05:00–05:10
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the coffee cup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the coffee cup. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the coffee cup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the coffee cup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "You used to hate cold coffee."
  VALENTINA (controlled, quiet): "You used to write back."

ESCENA 32 (Viñeta #32 del Storyboard) — 05:10–05:20
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: a paper napkin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: a paper napkin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, a paper napkin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, a paper napkin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "I checked the mailbox myself."
  VALENTINA (controlled, quiet): "Someone checked it before you."

ESCENA 33 (Viñeta #33 del Storyboard) — 05:20–05:30
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the seating chart. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing emerald gown, pearl necklace, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the seating chart. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the seating chart catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the seating chart sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "The guests arrive in an hour. Nathaniel, come."
  NATE (controlled, quiet): "I'm not finished."

ESCENA 34 (Viñeta #34 del Storyboard) — 05:30–05:40
- Location: Cole mansion service hall, coat racks and mail slots
- Characters Present: Nathaniel Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Walter Briggs: Nathaniel Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the mail slot. Key object in frame: the foreground. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Walter Briggs — Nathaniel Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the mail slot. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the mail slot catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the mail slot sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): mail slot clatter, coats brushing, distant music. Voice tone: NATE — low, clipped American English, warmth held under restraint; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Did you take my letters?"
  WALTER (controlled, quiet): "I took orders, sir."

ESCENA 35 (Viñeta #35 del Storyboard) — 05:40–05:50
- Location: Cole mansion service hall, coat racks and mail slots
- Characters Present: Eleanor Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and Eleanor Cole: Walter Briggs and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Eleanor Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing emerald gown, pearl necklace, silver hair in a chignon); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and Eleanor Cole — Walter Briggs and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the old letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the old letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): mail slot clatter, coats brushing, distant music. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "Your mother—"
  ELEANOR (controlled, quiet): "Walter, the guests need their coats."

ESCENA 36 (Viñeta #36 del Storyboard) — 05:50–06:00
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "It was Walter. I know it was Walter."
  VALENTINA (controlled, quiet): "Knowing isn't proof."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 31 (Viñeta #31 del Storyboard) — 05:00–05:10
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the coffee cup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the coffee cup. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the coffee cup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the coffee cup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "You used to hate cold coffee."
  VALENTINA (controlled, quiet): "You used to write back."

ESCENA 32 (Viñeta #32 del Storyboard) — 05:10–05:20
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: a paper napkin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: a paper napkin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, a paper napkin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, a paper napkin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "I checked the mailbox myself."
  VALENTINA (controlled, quiet): "Someone checked it before you."

ESCENA 33 (Viñeta #33 del Storyboard) — 05:20–05:30
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the seating chart. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing emerald gown, pearl necklace, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the seating chart. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the seating chart catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the seating chart sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "The guests arrive in an hour. Nathaniel, come."
  NATE (controlled, quiet): "I'm not finished."

ESCENA 34 (Viñeta #34 del Storyboard) — 05:30–05:40
- Location: Cole mansion service hall, coat racks and mail slots
- Characters Present: Nathaniel Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Walter Briggs: Nathaniel Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the mail slot. Key object in frame: the foreground. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Walter Briggs — Nathaniel Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the mail slot. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the mail slot catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the mail slot sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): mail slot clatter, coats brushing, distant music. Voice tone: NATE — low, clipped American English, warmth held under restraint; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Did you take my letters?"
  WALTER (controlled, quiet): "I took orders, sir."

ESCENA 35 (Viñeta #35 del Storyboard) — 05:40–05:50
- Location: Cole mansion service hall, coat racks and mail slots
- Characters Present: Eleanor Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and Eleanor Cole: Walter Briggs and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Eleanor Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing emerald gown, pearl necklace, silver hair in a chignon); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and Eleanor Cole — Walter Briggs and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the old letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the old letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): mail slot clatter, coats brushing, distant music. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "Your mother—"
  ELEANOR (controlled, quiet): "Walter, the guests need their coats."

ESCENA 36 (Viñeta #36 del Storyboard) — 05:50–06:00
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "It was Walter. I know it was Walter."
  VALENTINA (controlled, quiet): "Knowing isn't proof."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 07 — Minuto 7 (escenas 37–42)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_07.png`

**Adjuntos por escena de este lote:**

- Escena 037: `attach: [panel_037, ref_eleanor, ref_walter, ref_june]`
- Escena 038: `attach: [panel_038, ref_june]`
- Escena 039: `attach: [panel_039, ref_madison, ref_eleanor]`
- Escena 040: `attach: [panel_040, ref_valentina, ref_june]`
- Escena 041: `attach: [panel_041, ref_valentina, ref_june]`
- Escena 042: `attach: [panel_042, ref_valentina, ref_june]`

**Guardar 16:9 como:** `raw_clips/minute_07.mp4`

**Guardar 9:16 como:** `raw_clips/minute_07_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 37 (Viñeta #37 del Storyboard) — 06:00–06:10
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Eleanor Cole, Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Walter Briggs. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the burning envelope. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Eleanor Cole, Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing emerald gown, pearl necklace, silver hair in a chignon); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: Walter Briggs — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Walter Briggs. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the burning envelope. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the burning envelope is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on June Alvarez, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Eleanor Cole. June Alvarez holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the burning envelope catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: ELEANOR — low, polished American English, never raises her voice; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Walter is a sentimental fool."
  JUNE (controlled, quiet): "He's a witness."

ESCENA 38 (Viñeta #38 del Storyboard) — 06:10–06:20
- Location: Cole mansion study, firelight and dark wood
- Characters Present: June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the charred letter scrap. Key object in frame: her apron. Location: Cole mansion study, firelight and dark wood. Characters present: June Alvarez. No other characters appear.
- Identity Anchors: June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: her apron → Object In / Object Out: her apron → the scrap
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the charred letter scrap. Key object in frame: her apron.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-06s]: close-up, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez speaks as the camera holds close on their face, the charred letter scrap catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [06s-08s]: tight close-up of the story object, centered — A silent insert shows the scrap being placed inside her apron; no face in this shot.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — The silence hangs, the charred letter scrap sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "One star survived the fire."
  JUNE (controlled, quiet): "That is enough to start."

ESCENA 39 (Viñeta #39 del Storyboard) — 06:20–06:30
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Madison Pierce, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Madison Pierce: Eleanor Cole and Madison Pierce face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the calendar. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Madison Pierce, Eleanor Cole. No other characters appear.
- Identity Anchors: Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing champagne gown, diamond drop earrings, white fur stole); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing emerald gown, pearl necklace, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Madison Pierce — Eleanor Cole and Madison Pierce face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the calendar. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the calendar catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the calendar sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: ELEANOR — low, polished American English, never raises her voice; MADISON — bright, polished American English with a competitive edge
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Christmas Eve. The wedding. Then the girl leaves."
  MADISON (controlled, quiet): "And the shares?"

ESCENA 40 (Viñeta #40 del Storyboard) — 06:30–06:40
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Valentina Reyes. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the charred letter scrap. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Valentina Reyes. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the charred letter scrap. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-06s]: tight close-up of the story object, centered — the charred letter scrap is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — June Alvarez stays silent as the camera holds close on their face, the charred letter scrap catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "Your star. Your letter. She's burning them."
  VALENTINA (controlled, quiet): "Then the tin is still here."

ESCENA 41 (Viñeta #41 del Storyboard) — 06:40–06:50
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-05s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Valentina Reyes. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-05s]: wide establishing shot, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Valentina Reyes. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [05s-07s]: tight close-up of the story object, centered — the red cookie tin is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [07s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — June Alvarez stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "Behind the law books. She moved it after I saw her."
  VALENTINA (controlled, quiet): "Moved it where?"

ESCENA 42 (Viñeta #42 del Storyboard) — 06:50–07:00
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the cellar key. Key object in frame: sharp. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the cellar key. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on June Alvarez, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Valentina Reyes. June Alvarez holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the cellar key catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "The key is gone."
  JUNE (controlled, quiet): "Then she knows we're looking."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 37 (Viñeta #37 del Storyboard) — 06:00–06:10
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Eleanor Cole, Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Walter Briggs. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the burning envelope. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Eleanor Cole, Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing emerald gown, pearl necklace, silver hair in a chignon); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: Walter Briggs — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Walter Briggs. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the burning envelope. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the burning envelope is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on June Alvarez, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Eleanor Cole. June Alvarez holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the burning envelope catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: ELEANOR — low, polished American English, never raises her voice; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Walter is a sentimental fool."
  JUNE (controlled, quiet): "He's a witness."

ESCENA 38 (Viñeta #38 del Storyboard) — 06:10–06:20
- Location: Cole mansion study, firelight and dark wood
- Characters Present: June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the charred letter scrap. Key object in frame: her apron. Location: Cole mansion study, firelight and dark wood. Characters present: June Alvarez. No other characters appear.
- Identity Anchors: June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: her apron → Object In / Object Out: her apron → the scrap
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the charred letter scrap. Key object in frame: her apron.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-06s]: close-up, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at the other person in frame. June Alvarez speaks as the camera holds close on their face, the charred letter scrap catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [06s-08s]: tight close-up of the story object, centered — A silent insert shows the scrap being placed inside her apron; no face in this shot.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — The silence hangs, the charred letter scrap sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "One star survived the fire."
  JUNE (controlled, quiet): "That is enough to start."

ESCENA 39 (Viñeta #39 del Storyboard) — 06:20–06:30
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Madison Pierce, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Madison Pierce: Eleanor Cole and Madison Pierce face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the calendar. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Madison Pierce, Eleanor Cole. No other characters appear.
- Identity Anchors: Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing champagne gown, diamond drop earrings, white fur stole); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing emerald gown, pearl necklace, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Madison Pierce — Eleanor Cole and Madison Pierce face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the calendar. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the calendar catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the calendar sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: ELEANOR — low, polished American English, never raises her voice; MADISON — bright, polished American English with a competitive edge
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Christmas Eve. The wedding. Then the girl leaves."
  MADISON (controlled, quiet): "And the shares?"

ESCENA 40 (Viñeta #40 del Storyboard) — 06:30–06:40
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Valentina Reyes. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the charred letter scrap. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Valentina Reyes. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the charred letter scrap. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-06s]: tight close-up of the story object, centered — the charred letter scrap is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — June Alvarez stays silent as the camera holds close on their face, the charred letter scrap catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "Your star. Your letter. She's burning them."
  VALENTINA (controlled, quiet): "Then the tin is still here."

ESCENA 41 (Viñeta #41 del Storyboard) — 06:40–06:50
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-05s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Valentina Reyes. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-05s]: wide establishing shot, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Valentina Reyes. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [05s-07s]: tight close-up of the story object, centered — the red cookie tin is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [07s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — June Alvarez stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "Behind the law books. She moved it after I saw her."
  VALENTINA (controlled, quiet): "Moved it where?"

ESCENA 42 (Viñeta #42 del Storyboard) — 06:50–07:00
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the cellar key. Key object in frame: sharp. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the cellar key. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on June Alvarez, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Valentina Reyes. June Alvarez holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the cellar key catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "The key is gone."
  JUNE (controlled, quiet): "Then she knows we're looking."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 08 — Minuto 8 (escenas 43–48)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_08.png`

**Adjuntos por escena de este lote:**

- Escena 043: `attach: [panel_043, ref_valentina, ref_nate]`
- Escena 044: `attach: [panel_044, ref_valentina, ref_nate]`
- Escena 045: `attach: [panel_045, ref_nate, ref_eleanor]`
- Escena 046: `attach: [panel_046, ref_nate, ref_madison]`
- Escena 047: `attach: [panel_047, ref_valentina, ref_madison]`
- Escena 048: `attach: [panel_048, ref_walter, ref_june]`

**Guardar 16:9 como:** `raw_clips/minute_08.mp4`

**Guardar 9:16 como:** `raw_clips/minute_08_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 43 (Viñeta #43 del Storyboard) — 07:00–07:10
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-05s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the old Christmas photograph. Key object in frame: sharp. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-05s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the old Christmas photograph. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [05s-07s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [07s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the old Christmas photograph catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "She wouldn't destroy them. She'd keep them as leverage."
  VALENTINA (controlled, quiet): "Then where?"

ESCENA 44 (Viñeta #44 del Storyboard) — 07:10–07:20
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the old Christmas photograph. Key object in frame: sharp. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the old Christmas photograph. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the old Christmas photograph catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "You kept the star. I kept this."
  VALENTINA (controlled, quiet): "We were children."

ESCENA 45 (Viñeta #45 del Storyboard) — 07:20–07:30
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the old Christmas photograph. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the old Christmas photograph. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the old Christmas photograph catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the old Christmas photograph sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Sentiment. You learned nothing."
  NATE (controlled, quiet): "I learned who you are."

ESCENA 46 (Viñeta #46 del Storyboard) — 07:30–07:40
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Nathaniel Cole: Madison Pierce and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: a champagne flute. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Nathaniel Cole — Madison Pierce and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: a champagne flute. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, a champagne flute catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, a champagne flute sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "Smile. The papers are watching."
  NATE (controlled, quiet): "Then they'll see the truth."

ESCENA 47 (Viñeta #47 del Storyboard) — 07:40–07:50
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Valentina Reyes: Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the silver tray. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Valentina Reyes — Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the silver tray. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the silver tray catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, the silver tray sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "The help should curtsy when spoken to."
  VALENTINA (controlled, quiet): "I'm not the help you're looking for."

ESCENA 48 (Viñeta #48 del Storyboard) — 07:50–08:00
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and June Alvarez: Walter Briggs and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: a crystal star pin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and June Alvarez — Walter Briggs and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: a crystal star pin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, a crystal star pin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, a crystal star pin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "She still draws the star."
  JUNE (controlled, quiet): "You knew her name."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 43 (Viñeta #43 del Storyboard) — 07:00–07:10
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-05s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the old Christmas photograph. Key object in frame: sharp. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-05s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the old Christmas photograph. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [05s-07s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [07s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the old Christmas photograph catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "She wouldn't destroy them. She'd keep them as leverage."
  VALENTINA (controlled, quiet): "Then where?"

ESCENA 44 (Viñeta #44 del Storyboard) — 07:10–07:20
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the old Christmas photograph. Key object in frame: sharp. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black work trousers, silver star pin, cream blouse); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the old Christmas photograph. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the old Christmas photograph catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "You kept the star. I kept this."
  VALENTINA (controlled, quiet): "We were children."

ESCENA 45 (Viñeta #45 del Storyboard) — 07:20–07:30
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the old Christmas photograph. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the old Christmas photograph. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the old Christmas photograph catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the old Christmas photograph sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Sentiment. You learned nothing."
  NATE (controlled, quiet): "I learned who you are."

ESCENA 46 (Viñeta #46 del Storyboard) — 07:30–07:40
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Nathaniel Cole: Madison Pierce and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: a champagne flute. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Nathaniel Cole — Madison Pierce and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: a champagne flute. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, a champagne flute catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, a champagne flute sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "Smile. The papers are watching."
  NATE (controlled, quiet): "Then they'll see the truth."

ESCENA 47 (Viñeta #47 del Storyboard) — 07:40–07:50
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Valentina Reyes: Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the silver tray. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Valentina Reyes — Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the silver tray. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the silver tray catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, the silver tray sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "The help should curtsy when spoken to."
  VALENTINA (controlled, quiet): "I'm not the help you're looking for."

ESCENA 48 (Viñeta #48 del Storyboard) — 07:50–08:00
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and June Alvarez: Walter Briggs and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: a crystal star pin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and June Alvarez — Walter Briggs and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: a crystal star pin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, a crystal star pin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, a crystal star pin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "She still draws the star."
  JUNE (controlled, quiet): "You knew her name."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 09 — Minuto 9 (escenas 49–54)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_09.png`

**Adjuntos por escena de este lote:**

- Escena 049: `attach: [panel_049, ref_nate, ref_eleanor]`
- Escena 050: `attach: [panel_050, ref_valentina, ref_madison]`
- Escena 051: `attach: [panel_051, ref_valentina, ref_nate]`
- Escena 052: `attach: [panel_052, ref_valentina, ref_nate]`
- Escena 053: `attach: [panel_053, ref_valentina, ref_eleanor]`
- Escena 054: `attach: [panel_054, ref_valentina, ref_nate]`

**Guardar 16:9 como:** `raw_clips/minute_09.mp4`

**Guardar 9:16 como:** `raw_clips/minute_09_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 49 (Viñeta #49 del Storyboard) — 08:00–08:10
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the wedding announcement. Key object in frame: sharp. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the wedding announcement. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Eleanor Cole. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the wedding announcement catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Nathaniel and Madison will marry on Christmas Eve."
  NATE (controlled, quiet): "We agreed on spring."

ESCENA 50 (Viñeta #50 del Storyboard) — 08:10–08:20
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Madison Pierce is on camera with face and mouth fully visible, looking at Valentina Reyes. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Madison Pierce is on camera with face and mouth fully visible, looking at Valentina Reyes. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the prenup is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Madison Pierce. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the prenup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "Half the hotels, and I'll keep him happy."
  VALENTINA (controlled, quiet): "You should charge more."

ESCENA 51 (Viñeta #51 del Storyboard) — 08:20–08:30
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Valentina Reyes and Nathaniel Cole — Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the prenup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Valentina Reyes holds the silence after the line, the prenup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "She wants half the hotels."
  NATE (controlled, quiet): "She can have the buildings."

ESCENA 52 (Viñeta #52 del Storyboard) — 08:30–08:40
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-05s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: sharp. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-05s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [05s-07s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [07s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "One night. Give me one night to prove it."
  VALENTINA (controlled, quiet): "Prove what?"

ESCENA 53 (Viñeta #53 del Storyboard) — 08:40–08:50
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Valentina Reyes: Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the study door. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Valentina Reyes — Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the study door. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the study door catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the study door sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: ELEANOR — low, polished American English, never raises her voice; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "You will not ruin this family twice."
  VALENTINA (controlled, quiet): "I'm not the one who lied."

ESCENA 54 (Viñeta #54 del Storyboard) — 08:50–09:00
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the study door. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the study door. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the study door catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the study door sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "She locked us in."
  VALENTINA (controlled, quiet): "She's giving them a reason to talk."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 49 (Viñeta #49 del Storyboard) — 08:00–08:10
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the wedding announcement. Key object in frame: sharp. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the wedding announcement. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Eleanor Cole. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the wedding announcement catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Nathaniel and Madison will marry on Christmas Eve."
  NATE (controlled, quiet): "We agreed on spring."

ESCENA 50 (Viñeta #50 del Storyboard) — 08:10–08:20
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Madison Pierce is on camera with face and mouth fully visible, looking at Valentina Reyes. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Madison Pierce is on camera with face and mouth fully visible, looking at Valentina Reyes. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the prenup is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Madison Pierce. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the prenup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "Half the hotels, and I'll keep him happy."
  VALENTINA (controlled, quiet): "You should charge more."

ESCENA 51 (Viñeta #51 del Storyboard) — 08:20–08:30
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Valentina Reyes and Nathaniel Cole — Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the prenup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Valentina Reyes holds the silence after the line, the prenup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "She wants half the hotels."
  NATE (controlled, quiet): "She can have the buildings."

ESCENA 52 (Viñeta #52 del Storyboard) — 08:30–08:40
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-05s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: sharp. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-05s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [05s-07s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [07s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "One night. Give me one night to prove it."
  VALENTINA (controlled, quiet): "Prove what?"

ESCENA 53 (Viñeta #53 del Storyboard) — 08:40–08:50
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Valentina Reyes: Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the study door. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Valentina Reyes — Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the study door. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the study door catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the study door sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: ELEANOR — low, polished American English, never raises her voice; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "You will not ruin this family twice."
  VALENTINA (controlled, quiet): "I'm not the one who lied."

ESCENA 54 (Viñeta #54 del Storyboard) — 08:50–09:00
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the study door. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the study door. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the study door catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the study door sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "She locked us in."
  VALENTINA (controlled, quiet): "She's giving them a reason to talk."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 10 — Minuto 10 (escenas 55–60)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_10.png`

**Adjuntos por escena de este lote:**

- Escena 055: `attach: [panel_055, ref_valentina, ref_madison]`
- Escena 056: `attach: [panel_056, ref_valentina, ref_june]`
- Escena 057: `attach: [panel_057, ref_valentina]`
- Escena 058: `attach: [panel_058, ref_valentina, ref_june]`
- Escena 059: `attach: [panel_059, ref_valentina, ref_walter]`
- Escena 060: `attach: [panel_060, ref_valentina, ref_eleanor]`

**Guardar 16:9 como:** `raw_clips/minute_10.mp4`

**Guardar 9:16 como:** `raw_clips/minute_10_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 55 (Viñeta #55 del Storyboard) — 09:00–09:10
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Valentina Reyes: Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the champagne glass. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Valentina Reyes — Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the champagne glass. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the champagne glass catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, the champagne glass sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "There she is. The decorator who traps my fiancé."
  VALENTINA (controlled, quiet): "He was trapped long before I arrived."

ESCENA 56 (Viñeta #56 del Storyboard) — 09:10–09:20
- Location: Cole mansion kitchen, warm steel and hanging copper
- Characters Present: Valentina Reyes, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with June Alvarez and Valentina Reyes: June Alvarez and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the cellar key. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with June Alvarez and Valentina Reyes — June Alvarez and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the cellar key. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — June Alvarez stays silent as the camera holds close on their face, the cellar key catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — June Alvarez holds the silence after the line, the cellar key sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): copper pots, running water, a radio carol. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "Walter has the cellar key."
  VALENTINA (controlled, quiet): "Then we use the servant stairs."

ESCENA 57 (Viñeta #57 del Storyboard) — 09:20–09:30
- Location: Cole mansion kitchen, warm steel and hanging copper
- Characters Present: Valentina Reyes
- Storyboard Panel (Shot 1 exact framing): [00s-07s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the phone. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the phone. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the phone catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — The silence hangs, the phone sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): copper pots, running water, a radio carol. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "I need the letters, Mama. I can't come home yet."

ESCENA 58 (Viñeta #58 del Storyboard) — 09:30–09:40
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Valentina Reyes, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-05s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the flashlight. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Valentina Reyes, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: June Alvarez — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-05s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the flashlight. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [05s-08s]: close-up, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes speaks as the camera holds close on their face, the flashlight catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — The silence hangs, the flashlight sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "June said behind the wine racks."
  VALENTINA (controlled, quiet): "Please still be here."

ESCENA 59 (Viñeta #59 del Storyboard) — 09:40–09:50
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Valentina Reyes, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Walter Briggs. Valentina Reyes is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: sharp. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Valentina Reyes, Walter Briggs. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Silent Present: Walter Briggs — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Walter Briggs. Valentina Reyes is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: close-up, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes speaks as the camera holds close on their face, the old letter catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — The silence hangs, the old letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "Walter's letter."
  VALENTINA (controlled, quiet): "He kept one letter."

ESCENA 60 (Viñeta #60 del Storyboard) — 09:50–10:00
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Valentina Reyes, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Eleanor Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Eleanor Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the red cookie tin is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Eleanor Cole. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: ELEANOR — low, polished American English, never raises her voice; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Looking for this?"
  VALENTINA (controlled, quiet): "You kept them."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 55 (Viñeta #55 del Storyboard) — 09:00–09:10
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Valentina Reyes: Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the champagne glass. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Valentina Reyes — Madison Pierce and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the champagne glass. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the champagne glass catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, the champagne glass sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "There she is. The decorator who traps my fiancé."
  VALENTINA (controlled, quiet): "He was trapped long before I arrived."

ESCENA 56 (Viñeta #56 del Storyboard) — 09:10–09:20
- Location: Cole mansion kitchen, warm steel and hanging copper
- Characters Present: Valentina Reyes, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with June Alvarez and Valentina Reyes: June Alvarez and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the cellar key. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with June Alvarez and Valentina Reyes — June Alvarez and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the cellar key. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — June Alvarez stays silent as the camera holds close on their face, the cellar key catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — June Alvarez holds the silence after the line, the cellar key sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): copper pots, running water, a radio carol. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "Walter has the cellar key."
  VALENTINA (controlled, quiet): "Then we use the servant stairs."

ESCENA 57 (Viñeta #57 del Storyboard) — 09:20–09:30
- Location: Cole mansion kitchen, warm steel and hanging copper
- Characters Present: Valentina Reyes
- Storyboard Panel (Shot 1 exact framing): [00s-07s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the phone. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the phone. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the phone catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — The silence hangs, the phone sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): copper pots, running water, a radio carol. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "I need the letters, Mama. I can't come home yet."

ESCENA 58 (Viñeta #58 del Storyboard) — 09:30–09:40
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Valentina Reyes, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-05s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the flashlight. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Valentina Reyes, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, dark hair pulled back)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: June Alvarez — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-05s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the flashlight. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [05s-08s]: close-up, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes speaks as the camera holds close on their face, the flashlight catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — The silence hangs, the flashlight sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "June said behind the wine racks."
  VALENTINA (controlled, quiet): "Please still be here."

ESCENA 59 (Viñeta #59 del Storyboard) — 09:40–09:50
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Valentina Reyes, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Walter Briggs. Valentina Reyes is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: sharp. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Valentina Reyes, Walter Briggs. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey porter uniform, brass buttons, polished shoes)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Silent Present: Walter Briggs — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Walter Briggs. Valentina Reyes is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: close-up, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes speaks as the camera holds close on their face, the old letter catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — The silence hangs, the old letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "Walter's letter."
  VALENTINA (controlled, quiet): "He kept one letter."

ESCENA 60 (Viñeta #60 del Storyboard) — 09:50–10:00
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Valentina Reyes, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Eleanor Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Eleanor Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the red cookie tin is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Eleanor Cole. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: ELEANOR — low, polished American English, never raises her voice; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Looking for this?"
  VALENTINA (controlled, quiet): "You kept them."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 11 — Minuto 11 (escenas 61–66)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_11.png`

**Adjuntos por escena de este lote:**

- Escena 061: `attach: [panel_061, ref_valentina, ref_nate, ref_madison]`
- Escena 062: `attach: [panel_062, ref_nate, ref_eleanor]`
- Escena 063: `attach: [panel_063, ref_valentina, ref_nate]`
- Escena 064: `attach: [panel_064, ref_valentina, ref_nate]`
- Escena 065: `attach: [panel_065, ref_valentina, ref_nate]`
- Escena 066: `attach: [panel_066, ref_madison, ref_eleanor]`

**Guardar 16:9 como:** `raw_clips/minute_11.mp4`

**Guardar 9:16 como:** `raw_clips/minute_11_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 61 (Viñeta #61 del Storyboard) — 10:00–10:10
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: Madison Pierce — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Valentina Reyes and Nathaniel Cole — Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the old letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Valentina Reyes holds the silence after the line, the old letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "Your mother has the tin."
  NATE (controlled, quiet): "Where?"

ESCENA 62 (Viñeta #62 del Storyboard) — 10:10–10:20
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the fake letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Eleanor Cole. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "She wrote this. 'I'm marrying another man.'"
  NATE (controlled, quiet): "That's her handwriting."

ESCENA 63 (Viñeta #63 del Storyboard) — 10:20–10:30
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the fake letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "There is no star beside my name."
  NATE (controlled, quiet): "What does that mean?"

ESCENA 64 (Viñeta #64 del Storyboard) — 10:30–10:40
- Location: Cole mansion terrace, snow falling over the lit garden
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the fake letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, snow, muffled music behind glass. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Why would she forge a letter?"
  VALENTINA (controlled, quiet): "Because you believe paper over me."

ESCENA 65 (Viñeta #65 del Storyboard) — 10:40–10:50
- Location: Cole mansion terrace, snow falling over the lit garden
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: sharp. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, snow, muffled music behind glass. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "If I bring the tin, will you stay?"
  VALENTINA (controlled, quiet): "Bring the tin and we'll talk."

ESCENA 66 (Viñeta #66 del Storyboard) — 10:50–11:00
- Location: Cole mansion terrace, snow falling over the lit garden
- Characters Present: Madison Pierce, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Madison Pierce: Eleanor Cole and Madison Pierce face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Madison Pierce, Eleanor Cole. No other characters appear.
- Identity Anchors: Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Madison Pierce — Eleanor Cole and Madison Pierce face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, snow, muffled music behind glass. Voice tone: ELEANOR — low, polished American English, never raises her voice; MADISON — bright, polished American English with a competitive edge
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "She'll be gone by midnight."
  MADISON (controlled, quiet): "And the tin?"

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 61 (Viñeta #61 del Storyboard) — 10:00–10:10
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole, Madison Pierce. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: Madison Pierce — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Valentina Reyes and Nathaniel Cole — Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the old letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Valentina Reyes holds the silence after the line, the old letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "Your mother has the tin."
  NATE (controlled, quiet): "Where?"

ESCENA 62 (Viñeta #62 del Storyboard) — 10:10–10:20
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the fake letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Eleanor Cole. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "She wrote this. 'I'm marrying another man.'"
  NATE (controlled, quiet): "That's her handwriting."

ESCENA 63 (Viñeta #63 del Storyboard) — 10:20–10:30
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the fake letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "There is no star beside my name."
  NATE (controlled, quiet): "What does that mean?"

ESCENA 64 (Viñeta #64 del Storyboard) — 10:30–10:40
- Location: Cole mansion terrace, snow falling over the lit garden
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the fake letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, snow, muffled music behind glass. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Why would she forge a letter?"
  VALENTINA (controlled, quiet): "Because you believe paper over me."

ESCENA 65 (Viñeta #65 del Storyboard) — 10:40–10:50
- Location: Cole mansion terrace, snow falling over the lit garden
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: sharp. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black event uniform, silver star pin, neat ponytail); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, white shirt, no tie)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, snow, muffled music behind glass. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "If I bring the tin, will you stay?"
  VALENTINA (controlled, quiet): "Bring the tin and we'll talk."

ESCENA 66 (Viñeta #66 del Storyboard) — 10:50–11:00
- Location: Cole mansion terrace, snow falling over the lit garden
- Characters Present: Madison Pierce, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Madison Pierce: Eleanor Cole and Madison Pierce face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Madison Pierce, Eleanor Cole. No other characters appear.
- Identity Anchors: Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, diamond necklace, platinum hair swept up); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Madison Pierce — Eleanor Cole and Madison Pierce face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, snow, muffled music behind glass. Voice tone: ELEANOR — low, polished American English, never raises her voice; MADISON — bright, polished American English with a competitive edge
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "She'll be gone by midnight."
  MADISON (controlled, quiet): "And the tin?"

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 12 — Minuto 12 (escenas 67–72)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_12.png`

**Adjuntos por escena de este lote:**

- Escena 067: `attach: [panel_067, ref_valentina, ref_june]`
- Escena 068: `attach: [panel_068, ref_valentina, ref_walter, ref_june]`
- Escena 069: `attach: [panel_069, ref_valentina, ref_walter]`
- Escena 070: `attach: [panel_070, ref_nate, ref_june]`
- Escena 071: `attach: [panel_071, ref_nate, ref_walter]`
- Escena 072: `attach: [panel_072, ref_nate, ref_eleanor]`

**Guardar 16:9 como:** `raw_clips/minute_12.mp4`

**Guardar 9:16 como:** `raw_clips/minute_12_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 67 (Viñeta #67 del Storyboard) — 11:00–11:10
- Location: Cole mansion kitchen, warm steel and hanging copper
- Characters Present: Valentina Reyes, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Valentina Reyes. June Alvarez is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow in her hair); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Valentina Reyes. June Alvarez is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the fake letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — June Alvarez stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): copper pots, running water, a radio carol. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "Your star is always here, beside the name."
  VALENTINA (controlled, quiet): "This one has nothing."

ESCENA 68 (Viñeta #68 del Storyboard) — 11:10–11:20
- Location: Cole mansion kitchen, warm steel and hanging copper
- Characters Present: Valentina Reyes, Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and Valentina Reyes: Walter Briggs and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes, Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow in her hair); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: June Alvarez — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and Valentina Reyes — Walter Briggs and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the fake letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): copper pots, running water, a radio carol. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "She told me to copy your hand."
  VALENTINA (controlled, quiet): "You watched me sign for six years."

ESCENA 69 (Viñeta #69 del Storyboard) — 11:20–11:30
- Location: Cole mansion kitchen, warm steel and hanging copper
- Characters Present: Valentina Reyes, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and Valentina Reyes: Walter Briggs and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes, Walter Briggs. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow in her hair); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and Valentina Reyes — Walter Briggs and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the old letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the old letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): copper pots, running water, a radio carol. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "Every letter. Both directions. For six years."
  VALENTINA (controlled, quiet): "And you kept them all?"

ESCENA 70 (Viñeta #70 del Storyboard) — 11:30–11:40
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Nathaniel Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at June Alvarez. Nathaniel Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Nathaniel Cole, June Alvarez. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at June Alvarez. Nathaniel Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on June Alvarez, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Nathaniel Cole. June Alvarez holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: NATE — low, clipped American English, warmth held under restraint; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "The shelf is empty."
  JUNE (controlled, quiet): "She moved it to the cellar."

ESCENA 71 (Viñeta #71 del Storyboard) — 11:40–11:50
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Nathaniel Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Walter Briggs. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the furnace. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Walter Briggs. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the furnace. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the furnace is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on Walter Briggs, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at Nathaniel Cole. Walter Briggs holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the furnace catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: NATE — low, clipped American English, warmth held under restraint; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Where is it?"
  WALTER (controlled, quiet): "She took it to the ballroom."

ESCENA 72 (Viñeta #72 del Storyboard) — 11:50–12:00
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the red cookie tin is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Eleanor Cole. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "A decoration from the family archive."
  NATE (controlled, quiet): "Those are her letters."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 67 (Viñeta #67 del Storyboard) — 11:00–11:10
- Location: Cole mansion kitchen, warm steel and hanging copper
- Characters Present: Valentina Reyes, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Valentina Reyes. June Alvarez is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow in her hair); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Valentina Reyes. June Alvarez is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the fake letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at June Alvarez. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — June Alvarez stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): copper pots, running water, a radio carol. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "Your star is always here, beside the name."
  VALENTINA (controlled, quiet): "This one has nothing."

ESCENA 68 (Viñeta #68 del Storyboard) — 11:10–11:20
- Location: Cole mansion kitchen, warm steel and hanging copper
- Characters Present: Valentina Reyes, Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and Valentina Reyes: Walter Briggs and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes, Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow in her hair); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: June Alvarez — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and Valentina Reyes — Walter Briggs and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the fake letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): copper pots, running water, a radio carol. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "She told me to copy your hand."
  VALENTINA (controlled, quiet): "You watched me sign for six years."

ESCENA 69 (Viñeta #69 del Storyboard) — 11:20–11:30
- Location: Cole mansion kitchen, warm steel and hanging copper
- Characters Present: Valentina Reyes, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and Valentina Reyes: Walter Briggs and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground. Location: Cole mansion kitchen, warm steel and hanging copper. Characters present: Valentina Reyes, Walter Briggs. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow in her hair); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and Valentina Reyes — Walter Briggs and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion kitchen, warm steel and hanging copper, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the old letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the old letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): copper pots, running water, a radio carol. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "Every letter. Both directions. For six years."
  VALENTINA (controlled, quiet): "And you kept them all?"

ESCENA 70 (Viñeta #70 del Storyboard) — 11:30–11:40
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Nathaniel Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at June Alvarez. Nathaniel Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Nathaniel Cole, June Alvarez. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at June Alvarez. Nathaniel Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on June Alvarez, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Nathaniel Cole. June Alvarez holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: NATE — low, clipped American English, warmth held under restraint; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "The shelf is empty."
  JUNE (controlled, quiet): "She moved it to the cellar."

ESCENA 71 (Viñeta #71 del Storyboard) — 11:40–11:50
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Nathaniel Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Walter Briggs. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the furnace. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Walter Briggs. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the furnace. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the furnace is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on Walter Briggs, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at Nathaniel Cole. Walter Briggs holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the furnace catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: NATE — low, clipped American English, warmth held under restraint; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Where is it?"
  WALTER (controlled, quiet): "She took it to the ballroom."

ESCENA 72 (Viñeta #72 del Storyboard) — 11:50–12:00
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the red cookie tin is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Eleanor Cole. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "A decoration from the family archive."
  NATE (controlled, quiet): "Those are her letters."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 13 — Minuto 13 (escenas 73–78)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_13.png`

**Adjuntos por escena de este lote:**

- Escena 073: `attach: [panel_073, ref_valentina, ref_eleanor]`
- Escena 074: `attach: [panel_074, ref_nate, ref_eleanor]`
- Escena 075: `attach: [panel_075, ref_madison, ref_eleanor]`
- Escena 076: `attach: [panel_076, ref_eleanor, ref_walter]`
- Escena 077: `attach: [panel_077, ref_walter, ref_june]`
- Escena 078: `attach: [panel_078, ref_walter, ref_june]`

**Guardar 16:9 como:** `raw_clips/minute_13.mp4`

**Guardar 9:16 como:** `raw_clips/minute_13_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 73 (Viñeta #73 del Storyboard) — 12:00–12:10
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Eleanor Cole. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow in her hair); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Eleanor Cole. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Eleanor Cole, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Eleanor Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "Those letters are mine."
  ELEANOR (controlled, quiet): "Prove it."

ESCENA 74 (Viñeta #74 del Storyboard) — 12:10–12:20
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Eleanor Cole — Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Then we open it."
  ELEANOR (controlled, quiet): "Touch it and you lose the company."

ESCENA 75 (Viñeta #75 del Storyboard) — 12:20–12:30
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Madison Pierce, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Eleanor Cole: Madison Pierce and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Madison Pierce, Eleanor Cole. No other characters appear.
- Identity Anchors: Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, white fur stole, diamonds); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Eleanor Cole — Madison Pierce and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "Open it. I want to see her face."
  ELEANOR (controlled, quiet): "Madison."

ESCENA 76 (Viñeta #76 del Storyboard) — 12:30–12:40
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Eleanor Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Walter Briggs: Eleanor Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Eleanor Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Walter Briggs — Eleanor Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: ELEANOR — low, polished American English, never raises her voice; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "They will never see those letters."
  WALTER (controlled, quiet): "They already know they exist."

ESCENA 77 (Viñeta #77 del Storyboard) — 12:40–12:50
- Location: Cole mansion service hall, coat racks and mail slots
- Characters Present: Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and June Alvarez: Walter Briggs and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the cellar key. Key object in frame: the foreground. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and June Alvarez — Walter Briggs and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the cellar key. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the cellar key catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the cellar key sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): mail slot clatter, coats brushing, distant music. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "One more sin."
  JUNE (controlled, quiet): "The last one."

ESCENA 78 (Viñeta #78 del Storyboard) — 12:50–13:00
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-04s] close-up, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Walter Briggs. June Alvarez speaks as the camera holds close on their face, the red cookie tin catching the light between them. Key object in frame: sharp. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: close-up, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Walter Briggs. June Alvarez speaks as the camera holds close on their face, the red cookie tin catching the light between them. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: wide establishing shot, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at June Alvarez. Walter Briggs is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — June Alvarez holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "I moved it while you were praying."
  WALTER (controlled, quiet): "Then where is it?"

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 73 (Viñeta #73 del Storyboard) — 12:00–12:10
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Eleanor Cole. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow in her hair); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Eleanor Cole. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Eleanor Cole, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Eleanor Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "Those letters are mine."
  ELEANOR (controlled, quiet): "Prove it."

ESCENA 74 (Viñeta #74 del Storyboard) — 12:10–12:20
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Eleanor Cole — Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Then we open it."
  ELEANOR (controlled, quiet): "Touch it and you lose the company."

ESCENA 75 (Viñeta #75 del Storyboard) — 12:20–12:30
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Madison Pierce, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Eleanor Cole: Madison Pierce and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Madison Pierce, Eleanor Cole. No other characters appear.
- Identity Anchors: Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, white fur stole, diamonds); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Eleanor Cole — Madison Pierce and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "Open it. I want to see her face."
  ELEANOR (controlled, quiet): "Madison."

ESCENA 76 (Viñeta #76 del Storyboard) — 12:30–12:40
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Eleanor Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Walter Briggs: Eleanor Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Eleanor Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Walter Briggs — Eleanor Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: ELEANOR — low, polished American English, never raises her voice; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "They will never see those letters."
  WALTER (controlled, quiet): "They already know they exist."

ESCENA 77 (Viñeta #77 del Storyboard) — 12:40–12:50
- Location: Cole mansion service hall, coat racks and mail slots
- Characters Present: Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and June Alvarez: Walter Briggs and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the cellar key. Key object in frame: the foreground. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and June Alvarez — Walter Briggs and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the cellar key. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the cellar key catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the cellar key sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): mail slot clatter, coats brushing, distant music. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "One more sin."
  JUNE (controlled, quiet): "The last one."

ESCENA 78 (Viñeta #78 del Storyboard) — 12:50–13:00
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-04s] close-up, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Walter Briggs. June Alvarez speaks as the camera holds close on their face, the red cookie tin catching the light between them. Key object in frame: sharp. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: close-up, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Walter Briggs. June Alvarez speaks as the camera holds close on their face, the red cookie tin catching the light between them. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: wide establishing shot, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at June Alvarez. Walter Briggs is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — June Alvarez holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "I moved it while you were praying."
  WALTER (controlled, quiet): "Then where is it?"

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 14 — Minuto 14 (escenas 79–84)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_14.png`

**Adjuntos por escena de este lote:**

- Escena 079: `attach: [panel_079, ref_walter, ref_june]`
- Escena 080: `attach: [panel_080, ref_nate, ref_walter]`
- Escena 081: `attach: [panel_081, ref_nate, ref_june]`
- Escena 082: `attach: [panel_082, ref_nate, ref_eleanor]`
- Escena 083: `attach: [panel_083, ref_eleanor, ref_walter]`
- Escena 084: `attach: [panel_084, ref_nate, ref_june]`

**Guardar 16:9 como:** `raw_clips/minute_14.mp4`

**Guardar 9:16 como:** `raw_clips/minute_14_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 79 (Viñeta #79 del Storyboard) — 13:00–13:10
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-06s] two-shot, medium shot with June Alvarez and Walter Briggs: June Alvarez and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the library where Eleanor will not think to look. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: the library where Eleanor will not think to look → Object In / Object Out: the library where Eleanor will not think to look → the tin
- Camera Cuts & Visual Action (10s):
  * [00s-06s]: two-shot, medium shot with June Alvarez and Walter Briggs — June Alvarez and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the library where Eleanor will not think to look.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [06s-08s]: tight close-up of the story object, centered — A silent insert shows the tin being placed inside the library where Eleanor will not think to look; no face in this shot.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-09s]: close-up — June Alvarez stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [09s-10s]: tight close-up — June Alvarez holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "The cellar is the first place she'll look."
  WALTER (controlled, quiet): "Then we need Nate."

ESCENA 80 (Viñeta #80 del Storyboard) — 13:10–13:20
- Location: Cole mansion service hall, coat racks and mail slots
- Characters Present: Nathaniel Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and Nathaniel Cole: Walter Briggs and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and Nathaniel Cole — Walter Briggs and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): mail slot clatter, coats brushing, distant music. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "The tin is safe. June has it."
  NATE (controlled, quiet): "Take me to it."

ESCENA 81 (Viñeta #81 del Storyboard) — 13:20–13:30
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Nathaniel Cole. June Alvarez is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, June Alvarez. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Nathaniel Cole. June Alvarez is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-06s]: tight close-up of the story object, centered — the red cookie tin is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at June Alvarez. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — June Alvarez stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "Your letters. All of them."
  NATE (controlled, quiet): "She wrote every one?"

ESCENA 82 (Viñeta #82 del Storyboard) — 13:30–13:40
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Put that down."
  NATE (controlled, quiet): "You don't own this."

ESCENA 83 (Viñeta #83 del Storyboard) — 13:40–13:50
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Eleanor Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and Eleanor Cole: Walter Briggs and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the book cart. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Eleanor Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and Eleanor Cole — Walter Briggs and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the book cart. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the book cart catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the book cart sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "I took the letters. Arrest me."
  ELEANOR (controlled, quiet): "Walter, be quiet."

ESCENA 84 (Viñeta #84 del Storyboard) — 13:50–14:00
- Location: Cole mansion terrace, snow falling over the lit garden
- Characters Present: Nathaniel Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at June Alvarez. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Nathaniel Cole, June Alvarez. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at June Alvarez. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on June Alvarez, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Nathaniel Cole. June Alvarez holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, snow, muffled music behind glass. Voice tone: NATE — low, clipped American English, warmth held under restraint; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "She drew a star on every one."
  JUNE (controlled, quiet): "Every single one."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 79 (Viñeta #79 del Storyboard) — 13:00–13:10
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-06s] two-shot, medium shot with June Alvarez and Walter Briggs: June Alvarez and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the library where Eleanor will not think to look. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: the library where Eleanor will not think to look → Object In / Object Out: the library where Eleanor will not think to look → the tin
- Camera Cuts & Visual Action (10s):
  * [00s-06s]: two-shot, medium shot with June Alvarez and Walter Briggs — June Alvarez and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the library where Eleanor will not think to look.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [06s-08s]: tight close-up of the story object, centered — A silent insert shows the tin being placed inside the library where Eleanor will not think to look; no face in this shot.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-09s]: close-up — June Alvarez stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [09s-10s]: tight close-up — June Alvarez holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "The cellar is the first place she'll look."
  WALTER (controlled, quiet): "Then we need Nate."

ESCENA 80 (Viñeta #80 del Storyboard) — 13:10–13:20
- Location: Cole mansion service hall, coat racks and mail slots
- Characters Present: Nathaniel Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and Nathaniel Cole: Walter Briggs and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion service hall, coat racks and mail slots. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and Nathaniel Cole — Walter Briggs and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion service hall, coat racks and mail slots, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): mail slot clatter, coats brushing, distant music. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "The tin is safe. June has it."
  NATE (controlled, quiet): "Take me to it."

ESCENA 81 (Viñeta #81 del Storyboard) — 13:20–13:30
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: June Alvarez is on camera with face and mouth fully visible, looking at Nathaniel Cole. June Alvarez is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, June Alvarez. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Nathaniel Cole. June Alvarez is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-06s]: tight close-up of the story object, centered — the red cookie tin is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at June Alvarez. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — June Alvarez stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "Your letters. All of them."
  NATE (controlled, quiet): "She wrote every one?"

ESCENA 82 (Viñeta #82 del Storyboard) — 13:30–13:40
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Put that down."
  NATE (controlled, quiet): "You don't own this."

ESCENA 83 (Viñeta #83 del Storyboard) — 13:40–13:50
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Eleanor Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and Eleanor Cole: Walter Briggs and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the book cart. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Eleanor Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and Eleanor Cole — Walter Briggs and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the book cart. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the book cart catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the book cart sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "I took the letters. Arrest me."
  ELEANOR (controlled, quiet): "Walter, be quiet."

ESCENA 84 (Viñeta #84 del Storyboard) — 13:50–14:00
- Location: Cole mansion terrace, snow falling over the lit garden
- Characters Present: Nathaniel Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at June Alvarez. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp. Location: Cole mansion terrace, snow falling over the lit garden. Characters present: Nathaniel Cole, June Alvarez. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at June Alvarez. Nathaniel Cole is already moving through Cole mansion terrace, snow falling over the lit garden, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on June Alvarez, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Nathaniel Cole. June Alvarez holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wind, snow, muffled music behind glass. Voice tone: NATE — low, clipped American English, warmth held under restraint; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "She drew a star on every one."
  JUNE (controlled, quiet): "Every single one."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 15 — Minuto 15 (escenas 85–90)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_15.png`

**Adjuntos por escena de este lote:**

- Escena 085: `attach: [panel_085, ref_nate, ref_walter]`
- Escena 086: `attach: [panel_086, ref_nate, ref_walter]`
- Escena 087: `attach: [panel_087, ref_eleanor, ref_walter]`
- Escena 088: `attach: [panel_088, ref_nate, ref_eleanor]`
- Escena 089: `attach: [panel_089, ref_valentina, ref_nate]`
- Escena 090: `attach: [panel_090, ref_nate, ref_madison, ref_eleanor]`

**Guardar 16:9 como:** `raw_clips/minute_15.mp4`

**Guardar 9:16 como:** `raw_clips/minute_15_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 85 (Viñeta #85 del Storyboard) — 14:00–14:10
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and Nathaniel Cole: Walter Briggs and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank envelope. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and Nathaniel Cole — Walter Briggs and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank envelope. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the bank envelope catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the bank envelope sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "Your mother paid me every month."
  NATE (controlled, quiet): "For six years?"

ESCENA 86 (Viñeta #86 del Storyboard) — 14:10–14:20
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Walter Briggs is on camera with face and mouth fully visible, looking at Nathaniel Cole. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at Nathaniel Cole. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-06s]: tight close-up of the story object, centered — the bank ledger is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Walter Briggs. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the bank ledger catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "Twenty thousand dollars. Every Christmas."
  NATE (controlled, quiet): "And the fake letter?"

ESCENA 87 (Viñeta #87 del Storyboard) — 14:20–14:30
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Eleanor Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Walter Briggs. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: sharp. Location: Cole mansion study, firelight and dark wood. Characters present: Eleanor Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Walter Briggs. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Walter Briggs, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at Eleanor Cole. Walter Briggs holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the bank ledger catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: ELEANOR — low, polished American English, never raises her voice; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Walter is confused. He's been drinking."
  WALTER (controlled, quiet): "I haven't touched a drop."

ESCENA 88 (Viñeta #88 del Storyboard) — 14:30–14:40
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Eleanor Cole — Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the fake letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: NATE — low, clipped American English, warmth held under restraint; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "You stole my life."
  ELEANOR (controlled, quiet): "She wrote this one herself."

ESCENA 89 (Viñeta #89 del Storyboard) — 14:40–14:50
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the fake letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Did you write this?"
  VALENTINA (controlled, quiet): "Not that one."

ESCENA 90 (Viñeta #90 del Storyboard) — 14:50–15:00
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Madison Pierce, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Eleanor Cole: Madison Pierce and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, white fur stole, diamonds); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: Nathaniel Cole — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Eleanor Cole — Madison Pierce and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the prenup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, the prenup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "I'm not the bride. I'm the investor."
  ELEANOR (controlled, quiet): "You're a parasite."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 85 (Viñeta #85 del Storyboard) — 14:00–14:10
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and Nathaniel Cole: Walter Briggs and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank envelope. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and Nathaniel Cole — Walter Briggs and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank envelope. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the bank envelope catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the bank envelope sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "Your mother paid me every month."
  NATE (controlled, quiet): "For six years?"

ESCENA 86 (Viñeta #86 del Storyboard) — 14:10–14:20
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Walter Briggs is on camera with face and mouth fully visible, looking at Nathaniel Cole. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at Nathaniel Cole. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-06s]: tight close-up of the story object, centered — the bank ledger is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Walter Briggs. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the bank ledger catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "Twenty thousand dollars. Every Christmas."
  NATE (controlled, quiet): "And the fake letter?"

ESCENA 87 (Viñeta #87 del Storyboard) — 14:20–14:30
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Eleanor Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Walter Briggs. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: sharp. Location: Cole mansion study, firelight and dark wood. Characters present: Eleanor Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Walter Briggs. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-06s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Walter Briggs, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at Eleanor Cole. Walter Briggs holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the bank ledger catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: ELEANOR — low, polished American English, never raises her voice; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Walter is confused. He's been drinking."
  WALTER (controlled, quiet): "I haven't touched a drop."

ESCENA 88 (Viñeta #88 del Storyboard) — 14:30–14:40
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing ivory robe over a silver gown, pearls)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Eleanor Cole — Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the fake letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: NATE — low, clipped American English, warmth held under restraint; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "You stole my life."
  ELEANOR (controlled, quiet): "She wrote this one herself."

ESCENA 89 (Viñeta #89 del Storyboard) — 14:40–14:50
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the fake letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Did you write this?"
  VALENTINA (controlled, quiet): "Not that one."

ESCENA 90 (Viñeta #90 del Storyboard) — 14:50–15:00
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Madison Pierce, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Eleanor Cole: Madison Pierce and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, white fur stole, diamonds); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: Nathaniel Cole — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Eleanor Cole — Madison Pierce and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the prenup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, the prenup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "I'm not the bride. I'm the investor."
  ELEANOR (controlled, quiet): "You're a parasite."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 16 — Minuto 16 (escenas 91–96)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_16.png`

**Adjuntos por escena de este lote:**

- Escena 091: `attach: [panel_091, ref_nate, ref_madison]`
- Escena 092: `attach: [panel_092, ref_nate, ref_eleanor]`
- Escena 093: `attach: [panel_093, ref_nate, ref_madison]`
- Escena 094: `attach: [panel_094, ref_valentina, ref_nate]`
- Escena 095: `attach: [panel_095, ref_valentina, ref_nate]`
- Escena 096: `attach: [panel_096, ref_nate, ref_eleanor]`

**Guardar 16:9 como:** `raw_clips/minute_16.mp4`

**Guardar 9:16 como:** `raw_clips/minute_16_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 91 (Viñeta #91 del Storyboard) — 15:00–15:10
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Madison Pierce: Nathaniel Cole and Madison Pierce face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, white fur stole, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Madison Pierce — Nathaniel Cole and Madison Pierce face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the prenup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the prenup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; MADISON — bright, polished American English with a competitive edge
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "You want the shares."
  MADISON (controlled, quiet): "I want the life. The shares are the life."

ESCENA 92 (Viñeta #92 del Storyboard) — 15:10–15:20
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] close-up, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole speaks as the camera holds close on their face, the prenup catching the light between them. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: close-up, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole speaks as the camera holds close on their face, the prenup catching the light between them. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the prenup is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Eleanor Cole. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the prenup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "That contract is binding."
  NATE (controlled, quiet): "Not anymore."

ESCENA 93 (Viñeta #93 del Storyboard) — 15:20–15:30
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Nathaniel Cole: Madison Pierce and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the torn prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, white fur stole, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Nathaniel Cole — Madison Pierce and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the torn prenup. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the torn prenup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, the torn prenup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "You'll regret this."
  NATE (controlled, quiet): "I already do."

ESCENA 94 (Viñeta #94 del Storyboard) — 15:30–15:40
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Valentina Reyes and Nathaniel Cole — Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Valentina Reyes holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "You just lost everything."
  NATE (controlled, quiet): "I found the letters."

ESCENA 95 (Viñeta #95 del Storyboard) — 15:40–15:50
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "Seventy-two letters."
  NATE (controlled, quiet): "And I read none."

ESCENA 96 (Viñeta #96 del Storyboard) — 15:50–16:00
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "I would do it again."
  NATE (controlled, quiet): "Then you'll do it alone."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 91 (Viñeta #91 del Storyboard) — 15:00–15:10
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Madison Pierce: Nathaniel Cole and Madison Pierce face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, white fur stole, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Madison Pierce — Nathaniel Cole and Madison Pierce face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the prenup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the prenup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; MADISON — bright, polished American English with a competitive edge
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "You want the shares."
  MADISON (controlled, quiet): "I want the life. The shares are the life."

ESCENA 92 (Viñeta #92 del Storyboard) — 15:10–15:20
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] close-up, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole speaks as the camera holds close on their face, the prenup catching the light between them. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: close-up, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at Nathaniel Cole. Eleanor Cole speaks as the camera holds close on their face, the prenup catching the light between them. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the prenup is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Eleanor Cole. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the prenup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "That contract is binding."
  NATE (controlled, quiet): "Not anymore."

ESCENA 93 (Viñeta #93 del Storyboard) — 15:20–15:30
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Nathaniel Cole: Madison Pierce and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the torn prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, white fur stole, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Nathaniel Cole — Madison Pierce and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the torn prenup. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the torn prenup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, the torn prenup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: MADISON — bright, polished American English with a competitive edge; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "You'll regret this."
  NATE (controlled, quiet): "I already do."

ESCENA 94 (Viñeta #94 del Storyboard) — 15:30–15:40
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Valentina Reyes and Nathaniel Cole — Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Valentina Reyes holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "You just lost everything."
  NATE (controlled, quiet): "I found the letters."

ESCENA 95 (Viñeta #95 del Storyboard) — 15:40–15:50
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "Seventy-two letters."
  NATE (controlled, quiet): "And I read none."

ESCENA 96 (Viñeta #96 del Storyboard) — 15:50–16:00
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "I would do it again."
  NATE (controlled, quiet): "Then you'll do it alone."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 17 — Minuto 17 (escenas 97–102)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_17.png`

**Adjuntos por escena de este lote:**

- Escena 097: `attach: [panel_097, ref_valentina, ref_nate]`
- Escena 098: `attach: [panel_098, ref_valentina, ref_nate, ref_walter]`
- Escena 099: `attach: [panel_099, ref_valentina, ref_walter]`
- Escena 100: `attach: [panel_100, ref_nate, ref_eleanor]`
- Escena 101: `attach: [panel_101, ref_nate, ref_madison]`
- Escena 102: `attach: [panel_102, ref_nate, ref_eleanor, ref_walter]`

**Guardar 16:9 como:** `raw_clips/minute_17.mp4`

**Guardar 9:16 como:** `raw_clips/minute_17_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 97 (Viñeta #97 del Storyboard) — 16:00–16:10
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the old letters. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Valentina Reyes and Nathaniel Cole — Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the old letters. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the old letters catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Valentina Reyes holds the silence after the line, the old letters sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "We show the letters at the ceremony."
  NATE (controlled, quiet): "She'll say they're forgeries."

ESCENA 98 (Viñeta #98 del Storyboard) — 16:10–16:20
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Nathaniel Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Walter Briggs is on camera with face and mouth fully visible, looking at Valentina Reyes. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: Nathaniel Cole — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at Valentina Reyes. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the bank ledger is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Walter Briggs. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the bank ledger catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "This proves she paid me."
  VALENTINA (controlled, quiet): "Then you'll read it aloud."

ESCENA 99 (Viñeta #99 del Storyboard) — 16:20–16:30
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and Valentina Reyes: Walter Briggs and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Walter Briggs. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and Valentina Reyes — Walter Briggs and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the bank ledger catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the bank ledger sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "I don't deserve this."
  VALENTINA (controlled, quiet): "You're the only one who told the truth."

ESCENA 100 (Viñeta #100 del Storyboard) — 16:30–16:40
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "We are gathered to witness a union."
  NATE (controlled, quiet): "Stop."

ESCENA 101 (Viñeta #101 del Storyboard) — 16:40–16:50
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Madison Pierce. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, white fur stole, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Madison Pierce. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the prenup is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Madison Pierce, face and mouth visible — Madison Pierce is on camera with face and mouth fully visible, looking at Nathaniel Cole. Madison Pierce holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the prenup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; MADISON — bright, polished American English with a competitive edge
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Madison wanted shares, not vows."
  MADISON (controlled, quiet): "You signed it."

ESCENA 102 (Viñeta #102 del Storyboard) — 16:50–17:00
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Walter Briggs: Eleanor Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: Nathaniel Cole — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Walter Briggs — Eleanor Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the bank ledger catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the bank ledger sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: ELEANOR — low, polished American English, never raises her voice; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "These letters prove nothing."
  WALTER (controlled, quiet): "They prove I was paid."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 97 (Viñeta #97 del Storyboard) — 16:00–16:10
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the old letters. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Valentina Reyes and Nathaniel Cole — Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the old letters. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the old letters catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Valentina Reyes holds the silence after the line, the old letters sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "We show the letters at the ceremony."
  NATE (controlled, quiet): "She'll say they're forgeries."

ESCENA 98 (Viñeta #98 del Storyboard) — 16:10–16:20
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Nathaniel Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Walter Briggs is on camera with face and mouth fully visible, looking at Valentina Reyes. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: Nathaniel Cole — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Walter Briggs is on camera with face and mouth fully visible, looking at Valentina Reyes. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the bank ledger is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Walter Briggs. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the bank ledger catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "This proves she paid me."
  VALENTINA (controlled, quiet): "Then you'll read it aloud."

ESCENA 99 (Viñeta #99 del Storyboard) — 16:20–16:30
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and Valentina Reyes: Walter Briggs and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Walter Briggs. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and Valentina Reyes — Walter Briggs and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the bank ledger catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the bank ledger sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "I don't deserve this."
  VALENTINA (controlled, quiet): "You're the only one who told the truth."

ESCENA 100 (Viñeta #100 del Storyboard) — 16:30–16:40
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "We are gathered to witness a union."
  NATE (controlled, quiet): "Stop."

ESCENA 101 (Viñeta #101 del Storyboard) — 16:40–16:50
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Madison Pierce
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Madison Pierce. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Madison Pierce. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown, white fur stole, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Madison Pierce. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the prenup. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the prenup is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Madison Pierce, face and mouth visible — Madison Pierce is on camera with face and mouth fully visible, looking at Nathaniel Cole. Madison Pierce holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the prenup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; MADISON — bright, polished American English with a competitive edge
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Madison wanted shares, not vows."
  MADISON (controlled, quiet): "You signed it."

ESCENA 102 (Viñeta #102 del Storyboard) — 16:50–17:00
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Walter Briggs: Eleanor Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: Nathaniel Cole — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Walter Briggs — Eleanor Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the bank ledger. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the bank ledger catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the bank ledger sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: ELEANOR — low, polished American English, never raises her voice; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "These letters prove nothing."
  WALTER (controlled, quiet): "They prove I was paid."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 18 — Minuto 18 (escenas 103–108)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_18.png`

**Adjuntos por escena de este lote:**

- Escena 103: `attach: [panel_103, ref_nate, ref_eleanor]`
- Escena 104: `attach: [panel_104, ref_valentina, ref_nate]`
- Escena 105: `attach: [panel_105, ref_nate, ref_eleanor]`
- Escena 106: `attach: [panel_106, ref_valentina, ref_nate, ref_june]`
- Escena 107: `attach: [panel_107, ref_valentina, ref_nate]`
- Escena 108: `attach: [panel_108, ref_valentina, ref_eleanor]`

**Guardar 16:9 como:** `raw_clips/minute_18.mp4`

**Guardar 9:16 como:** `raw_clips/minute_18_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 103 (Viñeta #103 del Storyboard) — 17:00–17:10
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the ballroom doors. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Eleanor Cole — Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the ballroom doors. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the ballroom doors catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the ballroom doors sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "No one leaves."
  ELEANOR (controlled, quiet): "This is my house."

ESCENA 104 (Viñeta #104 del Storyboard) — 17:10–17:20
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the old letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the old letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "Dear Nate, this is my sixth Christmas without you."
  NATE (controlled, quiet): "I never got it."

ESCENA 105 (Viñeta #105 del Storyboard) — 17:20–17:30
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Eleanor Cole — Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "You're destroying evidence."
  ELEANOR (controlled, quiet): "I'm destroying a mistake."

ESCENA 106 (Viñeta #106 del Storyboard) — 17:30–17:40
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, Nathaniel Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Nathaniel Cole, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: June Alvarez — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Valentina Reyes and Nathaniel Cole — Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Valentina Reyes holds the silence after the line, the fake letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "The fake letter is the proof."
  NATE (controlled, quiet): "She keeps it in the study safe."

ESCENA 107 (Viñeta #107 del Storyboard) — 17:40–17:50
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the fake letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "Christmas Eve. Of course."
  NATE (controlled, quiet): "Hurry. They'll notice we're gone."

ESCENA 108 (Viñeta #108 del Storyboard) — 17:50–18:00
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Valentina Reyes: Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Valentina Reyes — Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the fake letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: ELEANOR — low, polished American English, never raises her voice; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "The ceremony continues at midnight."
  VALENTINA (controlled, quiet): "With this?"

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 103 (Viñeta #103 del Storyboard) — 17:00–17:10
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the ballroom doors. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Eleanor Cole — Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the ballroom doors. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the ballroom doors catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the ballroom doors sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "No one leaves."
  ELEANOR (controlled, quiet): "This is my house."

ESCENA 104 (Viñeta #104 del Storyboard) — 17:10–17:20
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the old letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the old letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the old letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "Dear Nate, this is my sixth Christmas without you."
  NATE (controlled, quiet): "I never got it."

ESCENA 105 (Viñeta #105 del Storyboard) — 17:20–17:30
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Eleanor Cole — Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: NATE — low, clipped American English, warmth held under restraint; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "You're destroying evidence."
  ELEANOR (controlled, quiet): "I'm destroying a mistake."

ESCENA 106 (Viñeta #106 del Storyboard) — 17:30–17:40
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, Nathaniel Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Nathaniel Cole, June Alvarez. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing white chef coat, red scarf, apron)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: June Alvarez — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Valentina Reyes and Nathaniel Cole — Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Valentina Reyes is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Valentina Reyes holds the silence after the line, the fake letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "The fake letter is the proof."
  NATE (controlled, quiet): "She keeps it in the study safe."

ESCENA 107 (Viñeta #107 del Storyboard) — 17:40–17:50
- Location: Cole mansion study, firelight and dark wood
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion study, firelight and dark wood. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion study, firelight and dark wood, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the fake letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): fire crackle, clock ticking, snow at the window. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "Christmas Eve. Of course."
  NATE (controlled, quiet): "Hurry. They'll notice we're gone."

ESCENA 108 (Viñeta #108 del Storyboard) — 17:50–18:00
- Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows
- Characters Present: Valentina Reyes, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Valentina Reyes: Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Valentina Reyes — Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion ballroom, Christmas Eve, gold chairs and snowlit windows, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the fake letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): string quartet, glassware, guests murmuring. Voice tone: ELEANOR — low, polished American English, never raises her voice; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "The ceremony continues at midnight."
  VALENTINA (controlled, quiet): "With this?"

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 19 — Minuto 19 (escenas 109–114)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_19.png`

**Adjuntos por escena de este lote:**

- Escena 109: `attach: [panel_109, ref_valentina, ref_nate]`
- Escena 110: `attach: [panel_110, ref_valentina, ref_eleanor]`
- Escena 111: `attach: [panel_111, ref_valentina, ref_nate, ref_eleanor]`
- Escena 112: `attach: [panel_112, ref_eleanor, ref_walter]`
- Escena 113: `attach: [panel_113, ref_walter, ref_june]`
- Escena 114: `attach: [panel_114, ref_eleanor, ref_june]`

**Guardar 16:9 como:** `raw_clips/minute_19.mp4`

**Guardar 9:16 como:** `raw_clips/minute_19_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 109 (Viñeta #109 del Storyboard) — 18:00–18:10
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the fake letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "My star. Every letter."
  NATE (controlled, quiet): "This one has none."

ESCENA 110 (Viñeta #110 del Storyboard) — 18:10–18:20
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Valentina Reyes: Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the checkbook. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Valentina Reyes — Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the checkbook. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the checkbook catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the checkbook sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: ELEANOR — low, polished American English, never raises her voice; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "You came back for a box, not for him."
  VALENTINA (controlled, quiet): "I came back for the truth."

ESCENA 111 (Viñeta #111 del Storyboard) — 18:20–18:30
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Valentina Reyes and Eleanor Cole: Valentina Reyes and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the checkbook. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: Nathaniel Cole — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Valentina Reyes and Eleanor Cole — Valentina Reyes and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the checkbook. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the checkbook catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Valentina Reyes holds the silence after the line, the checkbook sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "My mother worked. That's not a sin."
  ELEANOR (controlled, quiet): "She also cleaned my house."

ESCENA 112 (Viñeta #112 del Storyboard) — 18:30–18:40
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Eleanor Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Walter Briggs: Eleanor Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Eleanor Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Walter Briggs — Eleanor Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: ELEANOR — low, polished American English, never raises her voice; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Burn it. All of it."
  WALTER (controlled, quiet): "There are seventy-two letters."

ESCENA 113 (Viñeta #113 del Storyboard) — 18:40–18:50
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and June Alvarez: Walter Briggs and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing wool coat over her chef whites, red scarf)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and June Alvarez — Walter Briggs and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "I won't do it again."
  JUNE (controlled, quiet): "Then help me."

ESCENA 114 (Viñeta #114 del Storyboard) — 18:50–19:00
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Eleanor Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at June Alvarez. Eleanor Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the furnace. Key object in frame: sharp. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Eleanor Cole, June Alvarez. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing wool coat over her chef whites, red scarf)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at June Alvarez. Eleanor Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the furnace. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on June Alvarez, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Eleanor Cole. June Alvarez holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the furnace catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: ELEANOR — low, polished American English, never raises her voice; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Where is the tin?"
  JUNE (controlled, quiet): "Gone. Like your son."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 109 (Viñeta #109 del Storyboard) — 18:00–18:10
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo, open collar, no tie)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the fake letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "My star. Every letter."
  NATE (controlled, quiet): "This one has none."

ESCENA 110 (Viñeta #110 del Storyboard) — 18:10–18:20
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Valentina Reyes: Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the checkbook. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black wool coat, silver star pin, snow on her shoulders); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver gown, diamond brooch, silver hair in a chignon)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Valentina Reyes — Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the checkbook. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the checkbook catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the checkbook sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: ELEANOR — low, polished American English, never raises her voice; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "You came back for a box, not for him."
  VALENTINA (controlled, quiet): "I came back for the truth."

ESCENA 111 (Viñeta #111 del Storyboard) — 18:20–18:30
- Location: Cole mansion library, lamplight and floor-to-ceiling books
- Characters Present: Valentina Reyes, Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Valentina Reyes and Eleanor Cole: Valentina Reyes and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the checkbook. Key object in frame: the foreground. Location: Cole mansion library, lamplight and floor-to-ceiling books. Characters present: Valentina Reyes, Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Silent Present: Nathaniel Cole — mouths closed for the whole scene, no lines.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Valentina Reyes and Eleanor Cole — Valentina Reyes and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion library, lamplight and floor-to-ceiling books, the action carrying over from the exact storyboard framing. Key object in frame: the checkbook. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the checkbook catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Valentina Reyes holds the silence after the line, the checkbook sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): clock ticking, paper shifting, radiator hum. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "My mother worked. That's not a sin."
  ELEANOR (controlled, quiet): "She also cleaned my house."

ESCENA 112 (Viñeta #112 del Storyboard) — 18:30–18:40
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Eleanor Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Walter Briggs: Eleanor Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Eleanor Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Walter Briggs — Eleanor Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: ELEANOR — low, polished American English, never raises her voice; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Burn it. All of it."
  WALTER (controlled, quiet): "There are seventy-two letters."

ESCENA 113 (Viñeta #113 del Storyboard) — 18:40–18:50
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Walter Briggs, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and June Alvarez: Walter Briggs and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Walter Briggs, June Alvarez. No other characters appear.
- Identity Anchors: Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing wool coat over her chef whites, red scarf)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and June Alvarez — Walter Briggs and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "I won't do it again."
  JUNE (controlled, quiet): "Then help me."

ESCENA 114 (Viñeta #114 del Storyboard) — 18:50–19:00
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Eleanor Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Eleanor Cole is on camera with face and mouth fully visible, looking at June Alvarez. Eleanor Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the furnace. Key object in frame: sharp. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Eleanor Cole, June Alvarez. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing wool coat over her chef whites, red scarf)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Eleanor Cole is on camera with face and mouth fully visible, looking at June Alvarez. Eleanor Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the furnace. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on June Alvarez, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Eleanor Cole. June Alvarez holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the furnace catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: ELEANOR — low, polished American English, never raises her voice; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Where is the tin?"
  JUNE (controlled, quiet): "Gone. Like your son."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 20 — Minuto 20 (escenas 115–120)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_20.png`

**Adjuntos por escena de este lote:**

- Escena 115: `attach: [panel_115, ref_valentina, ref_eleanor]`
- Escena 116: `attach: [panel_116, ref_nate, ref_eleanor]`
- Escena 117: `attach: [panel_117, ref_valentina, ref_nate]`
- Escena 118: `attach: [panel_118, ref_valentina]`
- Escena 119: `attach: [panel_119, ref_nate, ref_june]`
- Escena 120: `attach: [panel_120, ref_nate, ref_walter]`

**Guardar 16:9 como:** `raw_clips/minute_20.mp4`

**Guardar 9:16 como:** `raw_clips/minute_20_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 115 (Viñeta #115 del Storyboard) — 19:00–19:10
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Valentina Reyes, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Valentina Reyes: Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Valentina Reyes — Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the fake letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: ELEANOR — low, polished American English, never raises her voice; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Get out. The wedding goes on."
  VALENTINA (controlled, quiet): "I have the letter."

ESCENA 116 (Viñeta #116 del Storyboard) — 19:10–19:20
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the door. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Eleanor Cole — Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the door. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the door catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the door sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: NATE — low, clipped American English, warmth held under restraint; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "She stays."
  ELEANOR (controlled, quiet): "Then you lose everything."

ESCENA 117 (Viñeta #117 del Storyboard) — 19:20–19:30
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Valentina Reyes and Nathaniel Cole — Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Valentina Reyes holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "Don't lose your family over me."
  NATE (controlled, quiet): "I lost them six years ago."

ESCENA 118 (Viñeta #118 del Storyboard) — 19:30–19:40
- Location: Manhattan street, Christmas Eve, wet snow and yellow cabs
- Characters Present: Valentina Reyes
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Manhattan street, Christmas Eve, wet snow and yellow cabs, the action carrying over from the exact storyboard framing. Key object in frame: the train ticket. Key object in frame: the foreground. Location: Manhattan street, Christmas Eve, wet snow and yellow cabs. Characters present: Valentina Reyes. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Manhattan street, Christmas Eve, wet snow and yellow cabs, the action carrying over from the exact storyboard framing. Key object in frame: the train ticket. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-08s]: close-up, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes speaks as the camera holds close on their face, the train ticket catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — The silence hangs, the train ticket sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wet tires, taxi horns, snow underfoot. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "Grand Central. Midnight. One way."
  VALENTINA (controlled, quiet): "If he doesn't come, I'm gone."

ESCENA 119 (Viñeta #119 del Storyboard) — 19:40–19:50
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Nathaniel Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at June Alvarez. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole, June Alvarez. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing wool coat over her chef whites, red scarf)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at June Alvarez. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on June Alvarez, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Nathaniel Cole. June Alvarez holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: NATE — low, clipped American English, warmth held under restraint; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Where is the tin?"
  JUNE (controlled, quiet): "She took it to the furnace."

ESCENA 120 (Viñeta #120 del Storyboard) — 19:50–20:00
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Nathaniel Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Walter Briggs: Nathaniel Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the furnace. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Walter Briggs — Nathaniel Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the furnace. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the furnace catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the furnace sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: NATE — low, clipped American English, warmth held under restraint; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Tell me it's not in there."
  WALTER (controlled, quiet): "She fed it to the fire."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 115 (Viñeta #115 del Storyboard) — 19:00–19:10
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Valentina Reyes, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Valentina Reyes: Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Eleanor Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Valentina Reyes — Eleanor Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the fake letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: ELEANOR — low, polished American English, never raises her voice; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "Get out. The wedding goes on."
  VALENTINA (controlled, quiet): "I have the letter."

ESCENA 116 (Viñeta #116 del Storyboard) — 19:10–19:20
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Eleanor Cole: Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the door. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Eleanor Cole — Nathaniel Cole and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the door. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the door catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the door sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: NATE — low, clipped American English, warmth held under restraint; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "She stays."
  ELEANOR (controlled, quiet): "Then you lose everything."

ESCENA 117 (Viñeta #117 del Storyboard) — 19:20–19:30
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Valentina Reyes and Nathaniel Cole: Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Valentina Reyes and Nathaniel Cole — Valentina Reyes and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Valentina Reyes holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "Don't lose your family over me."
  NATE (controlled, quiet): "I lost them six years ago."

ESCENA 118 (Viñeta #118 del Storyboard) — 19:30–19:40
- Location: Manhattan street, Christmas Eve, wet snow and yellow cabs
- Characters Present: Valentina Reyes
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Manhattan street, Christmas Eve, wet snow and yellow cabs, the action carrying over from the exact storyboard framing. Key object in frame: the train ticket. Key object in frame: the foreground. Location: Manhattan street, Christmas Eve, wet snow and yellow cabs. Characters present: Valentina Reyes. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Manhattan street, Christmas Eve, wet snow and yellow cabs, the action carrying over from the exact storyboard framing. Key object in frame: the train ticket. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-08s]: close-up, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes speaks as the camera holds close on their face, the train ticket catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — The silence hangs, the train ticket sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): wet tires, taxi horns, snow underfoot. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "Grand Central. Midnight. One way."
  VALENTINA (controlled, quiet): "If he doesn't come, I'm gone."

ESCENA 119 (Viñeta #119 del Storyboard) — 19:40–19:50
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Nathaniel Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at June Alvarez. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole, June Alvarez. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing wool coat over her chef whites, red scarf)
- Key Object: sharp → Object In / Object Out: sharp → sharp
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at June Alvarez. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: sharp.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — sharp is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on June Alvarez, face and mouth visible — June Alvarez is on camera with face and mouth fully visible, looking at Nathaniel Cole. June Alvarez holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: NATE — low, clipped American English, warmth held under restraint; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Where is the tin?"
  JUNE (controlled, quiet): "She took it to the furnace."

ESCENA 120 (Viñeta #120 del Storyboard) — 19:50–20:00
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Nathaniel Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Walter Briggs: Nathaniel Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the furnace. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Walter Briggs — Nathaniel Cole and Walter Briggs face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the furnace. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the furnace catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the furnace sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: NATE — low, clipped American English, warmth held under restraint; WALTER — rough, quiet American English, a lifetime of service in it
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Tell me it's not in there."
  WALTER (controlled, quiet): "She fed it to the fire."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 21 — Minuto 21 (escenas 121–126)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_21.png`

**Adjuntos por escena de este lote:**

- Escena 121: `attach: [panel_121, ref_nate]`
- Escena 122: `attach: [panel_122, ref_nate, ref_june]`
- Escena 123: `attach: [panel_123, ref_nate, ref_walter]`
- Escena 124: `attach: [panel_124, ref_nate, ref_eleanor]`
- Escena 125: `attach: [panel_125, ref_madison, ref_eleanor]`
- Escena 126: `attach: [panel_126, ref_eleanor, ref_june]`

**Guardar 16:9 como:** `raw_clips/minute_21.mp4`

**Guardar 9:16 como:** `raw_clips/minute_21_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 121 (Viñeta #121 del Storyboard) — 20:00–20:10
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at the other person in frame. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at the other person in frame. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the red cookie tin is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: close-up, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at the other person in frame. nate speaks as the camera holds close on their face, the red cookie tin catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — Nathaniel Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "It's not burning."
  NATE (controlled, quiet): "The tin held."

ESCENA 122 (Viñeta #122 del Storyboard) — 20:10–20:20
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Nathaniel Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with June Alvarez and Nathaniel Cole: June Alvarez and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: a kitchen towel. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole, June Alvarez. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing wool coat over her chef whites, red scarf)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with June Alvarez and Nathaniel Cole — June Alvarez and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: a kitchen towel. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — June Alvarez stays silent as the camera holds close on their face, a kitchen towel catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — June Alvarez holds the silence after the line, a kitchen towel sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "You'll need a doctor."
  NATE (controlled, quiet): "After midnight."

ESCENA 123 (Viñeta #123 del Storyboard) — 20:20–20:30
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Nathaniel Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and Nathaniel Cole: Walter Briggs and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and Nathaniel Cole — Walter Briggs and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "The tin is evidence. Give it to the police."
  NATE (controlled, quiet): "After I give it to Val."

ESCENA 124 (Viñeta #124 del Storyboard) — 20:30–20:40
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "You will not humiliate this family."
  NATE (controlled, quiet): "You already did."

ESCENA 125 (Viñeta #125 del Storyboard) — 20:40–20:50
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Madison Pierce, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Eleanor Cole: Madison Pierce and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the torn prenup. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Madison Pierce, Eleanor Cole. No other characters appear.
- Identity Anchors: Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown under a white fur coat); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Eleanor Cole — Madison Pierce and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the torn prenup. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the torn prenup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, the torn prenup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: MADISON — bright, polished American English with a competitive edge; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "I'll take what I'm owed."
  ELEANOR (controlled, quiet): "Not one share."

ESCENA 126 (Viñeta #126 del Storyboard) — 20:50–21:00
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Eleanor Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and June Alvarez: Eleanor Cole and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Eleanor Cole, June Alvarez. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing wool coat over her chef whites, red scarf)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and June Alvarez — Eleanor Cole and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: ELEANOR — low, polished American English, never raises her voice; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "I would do it again."
  JUNE (controlled, quiet): "I know."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 121 (Viñeta #121 del Storyboard) — 20:00–20:10
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at the other person in frame. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at the other person in frame. Nathaniel Cole is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the red cookie tin is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: close-up, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at the other person in frame. nate speaks as the camera holds close on their face, the red cookie tin catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — Nathaniel Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "It's not burning."
  NATE (controlled, quiet): "The tin held."

ESCENA 122 (Viñeta #122 del Storyboard) — 20:10–20:20
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Nathaniel Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with June Alvarez and Nathaniel Cole: June Alvarez and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: a kitchen towel. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole, June Alvarez. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing wool coat over her chef whites, red scarf)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with June Alvarez and Nathaniel Cole — June Alvarez and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. June Alvarez is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: a kitchen towel. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — June Alvarez stays silent as the camera holds close on their face, a kitchen towel catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — June Alvarez holds the silence after the line, a kitchen towel sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: JUNE — warm, plainspoken American English with a slight Spanish accent; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  JUNE (controlled, quiet): "You'll need a doctor."
  NATE (controlled, quiet): "After midnight."

ESCENA 123 (Viñeta #123 del Storyboard) — 20:20–20:30
- Location: Cole mansion wine cellar, stone stairs and a single bulb
- Characters Present: Nathaniel Cole, Walter Briggs
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Walter Briggs and Nathaniel Cole: Walter Briggs and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion wine cellar, stone stairs and a single bulb. Characters present: Nathaniel Cole, Walter Briggs. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Walter Briggs (Cast Sheet Pos #5: late fifties; porter with grey hair; wearing grey overcoat over his porter uniform)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Walter Briggs and Nathaniel Cole — Walter Briggs and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Walter Briggs is already moving through Cole mansion wine cellar, stone stairs and a single bulb, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Walter Briggs stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Walter Briggs holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): furnace roar, dripping stone, wine bottles creaking. Voice tone: WALTER — rough, quiet American English, a lifetime of service in it; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  WALTER (controlled, quiet): "The tin is evidence. Give it to the police."
  NATE (controlled, quiet): "After I give it to Val."

ESCENA 124 (Viñeta #124 del Storyboard) — 20:30–20:40
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the red cookie tin sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "You will not humiliate this family."
  NATE (controlled, quiet): "You already did."

ESCENA 125 (Viñeta #125 del Storyboard) — 20:40–20:50
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Madison Pierce, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Madison Pierce and Eleanor Cole: Madison Pierce and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the torn prenup. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Madison Pierce, Eleanor Cole. No other characters appear.
- Identity Anchors: Madison Pierce (Cast Sheet Pos #3: late twenties; socialite with a platinum blonde bob; wearing red gown under a white fur coat); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Madison Pierce and Eleanor Cole — Madison Pierce and Eleanor Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Madison Pierce is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the torn prenup. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Madison Pierce stays silent as the camera holds close on their face, the torn prenup catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Madison Pierce holds the silence after the line, the torn prenup sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: MADISON — bright, polished American English with a competitive edge; ELEANOR — low, polished American English, never raises her voice
- Dialogue (English, max 15 words, finish before 8.5 s):
  MADISON (controlled, quiet): "I'll take what I'm owed."
  ELEANOR (controlled, quiet): "Not one share."

ESCENA 126 (Viñeta #126 del Storyboard) — 20:50–21:00
- Location: Cole mansion foyer, Christmas week, a giant half-decorated tree
- Characters Present: Eleanor Cole, June Alvarez
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and June Alvarez: Eleanor Cole and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Cole mansion foyer, Christmas week, a giant half-decorated tree. Characters present: Eleanor Cole, June Alvarez. No other characters appear.
- Identity Anchors: Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds); June Alvarez (Cast Sheet Pos #6: early fifties; cook with dark hair pulled back; wearing wool coat over her chef whites, red scarf)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and June Alvarez — Eleanor Cole and June Alvarez face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Cole mansion foyer, Christmas week, a giant half-decorated tree, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): a distant orchestra, fire crackle, snow against the windows. Voice tone: ELEANOR — low, polished American English, never raises her voice; JUNE — warm, plainspoken American English with a slight Spanish accent
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "I would do it again."
  JUNE (controlled, quiet): "I know."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

### Lote 22 — Minuto 22 (escenas 127–132)

**Adjuntar:** `REF_CAST_MASTER.png` + `REF_GRID_MIN_22.png`

**Adjuntos por escena de este lote:**

- Escena 127: `attach: [panel_127, ref_valentina]`
- Escena 128: `attach: [panel_128, ref_valentina, ref_nate]`
- Escena 129: `attach: [panel_129, ref_valentina, ref_nate]`
- Escena 130: `attach: [panel_130, ref_nate, ref_eleanor]`
- Escena 131: `attach: [panel_131, ref_valentina, ref_rosa]`
- Escena 132: `attach: [panel_132, ref_valentina, ref_nate]`

**Guardar 16:9 como:** `raw_clips/minute_22.mp4`

**Guardar 9:16 como:** `raw_clips/minute_22_vertical.mp4`

**Bloque 16:9 para Muse AI (YouTube):**

```text
ESCENA 127 (Viñeta #127 del Storyboard) — 21:00–21:10
- Location: Grand Central Station, midnight, snow on the marble floor
- Characters Present: Valentina Reyes
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the train ticket. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Valentina Reyes. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the train ticket. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-08s]: close-up, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes speaks as the camera holds close on their face, the train ticket catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — The silence hangs, the train ticket sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): train brakes, station echo, an announcement chime. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "He's not coming."
  VALENTINA (controlled, quiet): "I should board."

ESCENA 128 (Viñeta #128 del Storyboard) — 21:10–21:20
- Location: Grand Central Station, midnight, snow on the marble floor
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the red cookie tin is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): train brakes, station echo, an announcement chime. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "I have them. All seventy-two."
  VALENTINA (controlled, quiet): "You're bleeding."

ESCENA 129 (Viñeta #129 del Storyboard) — 21:20–21:30
- Location: Grand Central Station, midnight, snow on the marble floor
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the fake letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): train brakes, station echo, an announcement chime. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "My star. Every one."
  NATE (controlled, quiet): "And the fake one has none."

ESCENA 130 (Viñeta #130 del Storyboard) — 21:30–21:40
- Location: Grand Central Station, midnight, snow on the marble floor
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the fake letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): train brakes, station echo, an announcement chime. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "I would do it again."
  NATE (controlled, quiet): "Then you die alone."

ESCENA 131 (Viñeta #131 del Storyboard) — 21:40–21:50
- Location: Grand Central Station, midnight, snow on the marble floor
- Characters Present: Valentina Reyes, Rosa Reyes
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Rosa Reyes and Valentina Reyes: Rosa Reyes and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Rosa Reyes is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Valentina Reyes, Rosa Reyes. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Rosa Reyes (Cast Sheet Pos #7: mid fifties; mother with dark wavy hair; wearing rust cardigan under a wool coat, warm slippers)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Rosa Reyes and Valentina Reyes — Rosa Reyes and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Rosa Reyes is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Rosa Reyes stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Rosa Reyes holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): train brakes, station echo, an announcement chime. Voice tone: ROSA — soft, warm American English with a protective edge; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ROSA (controlled, quiet): "You kept this for six years."
  VALENTINA (controlled, quiet): "I kept everything."

ESCENA 132 (Viñeta #132 del Storyboard) — 21:50–22:00
- Location: Grand Central Station, midnight, snow on the marble floor
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): train brakes, station echo, an announcement chime. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Do I know you?"
  VALENTINA (controlled, quiet): "You're learning."

COMANDO FINAL (16:9 YouTube):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: horizontal 16:9 para YouTube. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

**Comando final 9:16 (Reels/Shorts):**

```text
ESCENA 127 (Viñeta #127 del Storyboard) — 21:00–21:10
- Location: Grand Central Station, midnight, snow on the marble floor
- Characters Present: Valentina Reyes
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the train ticket. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Valentina Reyes. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the train ticket. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-08s]: close-up, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at the other person in frame. Valentina Reyes speaks as the camera holds close on their face, the train ticket catching the light between them  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: tight close-up — The silence hangs, the train ticket sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): train brakes, station echo, an announcement chime. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "He's not coming."
  VALENTINA (controlled, quiet): "I should board."

ESCENA 128 (Viñeta #128 del Storyboard) — 21:10–21:20
- Location: Grand Central Station, midnight, snow on the marble floor
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-04s] wide establishing shot, face and mouth visible: Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-04s]: wide establishing shot, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the red cookie tin. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [04s-06s]: tight close-up of the story object, centered — the red cookie tin is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [06s-08s]: medium close-up on Valentina Reyes, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — nate stays silent as the camera holds close on their face, the red cookie tin catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): train brakes, station echo, an announcement chime. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "I have them. All seventy-two."
  VALENTINA (controlled, quiet): "You're bleeding."

ESCENA 129 (Viñeta #129 del Storyboard) — 21:20–21:30
- Location: Grand Central Station, midnight, snow on the marble floor
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-03s] wide establishing shot, face and mouth visible: Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-03s]: wide establishing shot, face and mouth visible — Valentina Reyes is on camera with face and mouth fully visible, looking at Nathaniel Cole. Valentina Reyes is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [03s-05s]: tight close-up of the story object, centered — the fake letter is revealed in a silent, centered close-up, clearly visible and unobstructed.  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [05s-08s]: medium close-up on Nathaniel Cole, face and mouth visible — Nathaniel Cole is on camera with face and mouth fully visible, looking at Valentina Reyes. Nathaniel Cole holds the moment before speaking  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [08s-10s]: close-up — Valentina Reyes stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): train brakes, station echo, an announcement chime. Voice tone: VALENTINA — warm mid-range American English, controlled, dignity under pressure; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  VALENTINA (controlled, quiet): "My star. Every one."
  NATE (controlled, quiet): "And the fake one has none."

ESCENA 130 (Viñeta #130 del Storyboard) — 21:30–21:40
- Location: Grand Central Station, midnight, snow on the marble floor
- Characters Present: Nathaniel Cole, Eleanor Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Eleanor Cole and Nathaniel Cole: Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Nathaniel Cole, Eleanor Cole. No other characters appear.
- Identity Anchors: Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat); Eleanor Cole (Cast Sheet Pos #4: early sixties; hair as shown in the reference sheet; wearing silver mink coat over her gown, diamonds)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Eleanor Cole and Nathaniel Cole — Eleanor Cole and Nathaniel Cole face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Eleanor Cole is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the fake letter. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Eleanor Cole stays silent as the camera holds close on their face, the fake letter catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Eleanor Cole holds the silence after the line, the fake letter sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): train brakes, station echo, an announcement chime. Voice tone: ELEANOR — low, polished American English, never raises her voice; NATE — low, clipped American English, warmth held under restraint
- Dialogue (English, max 15 words, finish before 8.5 s):
  ELEANOR (controlled, quiet): "I would do it again."
  NATE (controlled, quiet): "Then you die alone."

ESCENA 131 (Viñeta #131 del Storyboard) — 21:40–21:50
- Location: Grand Central Station, midnight, snow on the marble floor
- Characters Present: Valentina Reyes, Rosa Reyes
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Rosa Reyes and Valentina Reyes: Rosa Reyes and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Rosa Reyes is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Valentina Reyes, Rosa Reyes. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Rosa Reyes (Cast Sheet Pos #7: mid fifties; mother with dark wavy hair; wearing rust cardigan under a wool coat, warm slippers)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Rosa Reyes and Valentina Reyes — Rosa Reyes and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Rosa Reyes is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — Rosa Reyes stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — Rosa Reyes holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): train brakes, station echo, an announcement chime. Voice tone: ROSA — soft, warm American English with a protective edge; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  ROSA (controlled, quiet): "You kept this for six years."
  VALENTINA (controlled, quiet): "I kept everything."

ESCENA 132 (Viñeta #132 del Storyboard) — 21:50–22:00
- Location: Grand Central Station, midnight, snow on the marble floor
- Characters Present: Valentina Reyes, Nathaniel Cole
- Storyboard Panel (Shot 1 exact framing): [00s-07s] two-shot, medium shot with Nathaniel Cole and Valentina Reyes: Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground. Location: Grand Central Station, midnight, snow on the marble floor. Characters present: Valentina Reyes, Nathaniel Cole. No other characters appear.
- Identity Anchors: Valentina Reyes (Cast Sheet Pos #1: late twenties; Latina event decorator with long dark wavy hair; wearing black traveling coat, red scarf, silver star pin); Nathaniel Cole (Cast Sheet Pos #2: early thirties; hotel heir with short dark-brown hair; wearing black tuxedo under a charcoal overcoat)
- Key Object: the foreground → Object In / Object Out: the foreground → the foreground
- Object Rule: never show the container interior; it stays in shadow and out of frame.
- Camera Cuts & Visual Action (10s):
  * [00s-07s]: two-shot, medium shot with Nathaniel Cole and Valentina Reyes — Nathaniel Cole and Valentina Reyes face each other in a two-shot, both faces and mouths fully visible, each oriented toward the other. Nathaniel Cole is already moving through Grand Central Station, midnight, snow on the marble floor, the action carrying over from the exact storyboard framing. Key object in frame: the crystal star ornament. Key object in frame: the foreground.  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]
  * [07s-08s]: close-up — nate stays silent as the camera holds close on their face, the crystal star ornament catching the light between them  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
  * [08s-10s]: tight close-up — nate holds the silence after the line, the crystal star ornament sharp in the foreground  [SILENT SHOT: no dialogue, no speaking, mouths closed.]
- Sound Design (SFX & Voice Tone): train brakes, station echo, an announcement chime. Voice tone: NATE — low, clipped American English, warmth held under restraint; VALENTINA — warm mid-range American English, controlled, dignity under pressure
- Dialogue (English, max 15 words, finish before 8.5 s):
  NATE (controlled, quiet): "Do I know you?"
  VALENTINA (controlled, quiet): "You're learning."

COMANDO FINAL (9:16 Reels/TikTok/Shorts):

"Haz un video cinematográfico realista de 10 segundos por cada escena ejecutando entre 1 y 4 tomas exactamente como las lista el guion: la Toma 1 arranca directamente en movimiento desde el encuadre exacto de la viñeta correspondiente sin frames estáticos (two-shot si hablan dos personajes); cada línea hablada tiene su propio plano con el hablante de frente, rostro y boca visibles, nunca desde detrás del personaje; los planos silenciosos (insert, reacción, objeto) van después del diálogo y nunca contienen habla. Mantén estrictamente la misma raza, rostro y vestuario de cada personaje según su posición en la Hoja de Personajes adjunta, y únelos en un solo video continuo sin insertar jamás la imagen de referencia entre escenas. Formato: vertical 9:16 para Reels, TikTok y Shorts. Reglas negativas estrictas: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue."
```

---

## Paso 4 — Ensamblar

Cuando existan los 22 archivos `minute_01.mp4 … minute_22.mp4`:

```powershell
./novelfactory.bat assemble the_christmas_letters
```

El ensamblador detecta el modo B, genera el máster 16:9 completo,
el SRT sincronizado y el teaser vertical automático de 20 segundos.

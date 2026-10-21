#!/usr/bin/env python3
"""Biblioteca de plantillas maestras de novel_factory.

Contiene los cuatro prompts maestros del sistema, completos y sin resumir:

  PROMPT 000 — Arquitecto de historias virales (China / USA micro-drama).
  PROMPT 001 — Generador de storyboard cinematográfico (6 viñetas por imagen).
  PROMPT 002 — Generador de la hoja maestra de personajes (una sola imagen).
  PROMPT 003 — Generador de guion + cámara + sonido + comando Muse AI.

Los marcadores que el sistema rellena automáticamente son exactamente:

  {story_idea}          Idea base / arquitectura narrativa del proyecto.
  {duration_minutes}    Duración total del episodio en minutos.
  {total_scenes}        Número total de escenas (60 por defecto).
  {total_grid_images}   Número de bloques de 1 minuto (6 escenas cada uno).
  {visual_style}        Look visual bloqueado del proyecto.
  {aspect_ratio}        Relación de aspecto del máster (16:9 por defecto).

El relleno se hace con reemplazo literal de tokens (no con str.format), para
que las llaves de los ejemplos de los prompts nunca se rompan.
"""
from __future__ import annotations

import datetime as dt
import json
import math
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

NF_ROOT = Path(__file__).resolve().parent.parent
if str(NF_ROOT) not in sys.path:
    sys.path.insert(0, str(NF_ROOT))

PLACEHOLDERS = (
    "story_idea",
    "duration_minutes",
    "total_scenes",
    "total_grid_images",
    "visual_style",
    "aspect_ratio",
)

PROMPT_ORDER = ("prompt_000", "prompt_001", "prompt_002", "prompt_003")
VIRAL_TEMPLATES_TOKEN = "<<<VIRAL_TEMPLATES>>>"


# ---------------------------------------------------------------------------
# PROMPT 000 — texto literal solicitado (no modificar)
# ---------------------------------------------------------------------------
PROMPT_000_VIRAL_STORY_ARCHITECT = """🧠 PROMPT 000 — ARQUITECTO DE HISTORIAS VIRALES (CHINA / USA MICRO-DRAMA SHOWRUNNER)
Actúa como un Showrunner experto en Micro-Dramas virales de Estados Unidos y China (estilo ReelShort, DramaBox y canales de novelas con IA de +500,000 vistas).

Tu objetivo es transformar mi idea base en una HISTORIA DE ALTA RETENCIÓN pensada para el mercado en INGLÉS (alto RPM), estructurada matemáticamente para una duración de {duration_minutes} minuto(s) ({total_scenes} escenas de 10 segundos cada una, divididas en {total_grid_images} bloques de 1 minuto / 6 escenas).

IDEA BASE / SEMILLA:
{story_idea}

REGLAS DE ORO DE DRAMATURGIA Y RETENCIÓN QUE DEBES APLICAR:
1. GANCHO EXPLOSIVO EN LOS PRIMEROS 10 SEGUNDOS (ESCENA 1): La historia jamás debe empezar de forma lenta. Debe abrir en medio de una tensión máxima: una humillación pública, una traición descubierta, un secreto millonario, una diferencia extrema de clases sociales o un contrato inesperado.
2. MICRO-GIROS CADA 30 SEGUNDOS (CADA 3 ESCENAS): Cada 3 escenas debe ocurrir una revelación, un conflicto emocional, una mirada prohibida, una confrontación o un obstáculo que impida que el espectador cierre el video.
3. CLIFFHANGER AL FINAL DE CADA MINUTO (ESCENAS 6, 12, 18...): La última escena de cada bloque de 6 escenas debe terminar en máxima tensión dramática.
4. PERSONAJES CON CONTRASTE VISUAL INMEDIATO (MÁXIMO 3 A 5 PERSONAJES PRINCIPALES): Diseña personajes cuyo estatus social y personalidad se entiendan en 1 segundo solo por su vestuario (ej. multimillonario arrogante vs. trabajadora humilde con dignidad de hierro; heredera secreta vs. villana elitista).
5. ECONOMÍA DE ESCENARIOS (MÁXIMO 3 A 5 LOCACIONES): Concentra la acción en locaciones visualmente ricas y contrastantes para mantener continuidad perfecta.
6. CATÁLOGO DE 6 ESTRUCTURAS VIRALES PROBADAS (LATAM → USA, +500,000 VISTAS): Usa este catálogo como banco de estructuras. Elige UNA sola como columna vertebral de la historia y adáptala al mercado estadounidense en inglés. No copies nombres, marcas ni diálogos: conserva la mecánica emocional y el orden de beats.
<<<VIRAL_TEMPLATES>>>

ENTREGA EL RESULTADO EN ESTE FORMATO EXACTO (LISTO PARA COPIAR AL PROMPT 001):
1. TÍTULO VIRAL EN INGLÉS (3 opciones de alto CTR).
2. ELENCO PRINCIPAL (3 a 5 personajes: Nombre, Edad, Apariencia Física exacta, Vestuario característico fijo y Timbre de Voz en inglés).
3. SINOPSIS NARRATIVA INTENSA BLOQUE POR BLOQUE (1 párrafo por cada minuto de historia = 6 escenas por minuto, describiendo inicio, conflicto, giros y desenlace/cliffhanger)."""


# ---------------------------------------------------------------------------
# PROMPT 001 — generador de storyboard cinematográfico (6 escenas por imagen)
# ---------------------------------------------------------------------------
PROMPT_001_STORYBOARD_GENERATOR = """🎬 PROMPT 001 — GENERADOR DE STORYBOARD CINEMATOGRÁFICO (6 ESCENAS POR IMAGEN)
Actúa como director de cine y crea un storyboard visual para la historia que te voy a proporcionar.

DATOS DE LA HISTORIA
Historia:
{story_idea}

Duración:
{duration_minutes} minuto(s) ({total_scenes} escenas de 10 segundos = {total_grid_images} imagen(es) de storyboard de 6 viñetas cada una)

Estilo visual:
{visual_style}
(Opciones: Cinematográfico realista 35mm / Realista / Animación 3D / Animación 2D / Anime / Ilustración)

REGLAS DEL STORYBOARD
Cada escena dura exactamente 10 segundos.
Calcula automáticamente el número de escenas según la duración.
Cada imagen debe contener 6 escenas/viñetas (en cuadrícula limpia de 3x2: 6 viñetas numeradas del 1 al 6).
Por lo tanto:
1 minuto = 6 escenas = 1 imagen
2 minutos = 12 escenas = 2 imágenes
3 minutos = 18 escenas = 3 imágenes
4 minutos = 24 escenas = 4 imágenes
5 minutos = 30 escenas = 5 imágenes
10 minutos = 60 escenas = 10 imágenes
Cada imagen representa exactamente 1 minuto de historia.

CADA VIÑETA
Cada viñeta debe mostrar visualmente el momento correspondiente de la historia con encuadre de cine profesional (alternando planos generales establecedores, planos medios dramáticos y primeros planos emocionales).
Debe incluir:
- Personajes.
- Lugar.
- Acción física clara.
- Emoción intensa en los rostros.
- Composición e iluminación cinematográfica.
Debajo de cada viñeta puede aparecer una descripción extremadamente breve de la escena, de aproximadamente 5 a 10 palabras.
Ejemplo:
“1. Elena meets the billionaire in the rain.”
“4. The father discovers the secret romance.”
La descripción debe ser únicamente una referencia rápida de lo que ocurre.

IMPORTANTE:
No escribir diálogos ni párrafos dentro del storyboard.
Las descripciones deben ser:
- Muy breves (5 a 10 palabras).
- Claras.
- Fáciles de leer.
- Sin saturar la imagen.
- Máximo una línea cuando sea posible.

CONTINUIDAD
Mantén la misma apariencia exacta de los personajes durante todo el storyboard.
Conserva también la continuidad estricta de:
- Rostros.
- Cabello.
- Edad.
- Complexión.
- Vestuario.
- Locaciones.
- Época.
- Objetos importantes (anillos, contratos, vehículos, herramientas).
- Iluminación.
- Ambiente.
Si un personaje cambia de ropa por motivos narrativos, el cambio debe ser coherente.

ESTILO VISUAL
Utiliza exactamente el estilo visual seleccionado ({visual_style}).
Mantén ese estilo de manera consistente en todas las imágenes y todas las viñetas.
El storyboard debe tener apariencia profesional y cinematográfica.

IMPORTANTE
El resultado debe ser principalmente visual.
No incluir:
- Diálogos.
- Narración extensa.
- Subtítulos.
- Párrafos.
- Prompts de video.
- Explicaciones del proceso.
Solo incluir una descripción muy breve debajo de cada viñeta para identificar la acción.

RESULTADO FINAL
A partir de la historia, duración y estilo proporcionados:
1. Calcula el número total de escenas ({total_scenes} escenas).
2. Cada escena debe durar 10 segundos.
3. Divide las escenas en grupos de 6.
4. Genera una imagen por cada grupo de 6 escenas.
5. Cada imagen debe contener 6 viñetas claramente divididas.
6. Añade debajo de cada viñeta una descripción de máximo 5–10 palabras.
7. Mantén la continuidad absoluta de personajes y escenarios.
8. Cuenta toda la historia visualmente de principio a fin."""


# ---------------------------------------------------------------------------
# PROMPT 002 — hoja maestra de personajes en una sola imagen
# ---------------------------------------------------------------------------
PROMPT_002_CHARACTER_SHEET_GENERATOR = """👤 PROMPT 002 — GENERADOR DE PERSONAJES (HOJA MAESTRA EN UNA SOLA IMAGEN)
Actúa como director de casting y diseñador de personajes.
Ya tenemos creado el storyboard de la historia.
Ahora analiza ese storyboard e identifica los personajes principales y secundarios relevantes que aparecen en la historia.
Tu tarea es generar UNA SOLA IMAGEN que muestre juntos a todos los personajes identificados.

REFERENCIA
Storyboard: el storyboard completo creado en el paso anterior. La hoja debe mantener exactamente los rostros, edades, etnias, vestuarios y accesorios que aparecen en ese storyboard.

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
- Estilo visual ({visual_style}).

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
Utiliza exactamente el mismo estilo visual utilizado en el storyboard ({visual_style}).
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
Entrega solamente la imagen de los personajes."""


# ---------------------------------------------------------------------------
# PROMPT 003 — guion cinematográfico + cámara + sonido + comando Muse AI
# ---------------------------------------------------------------------------
PROMPT_003_SCRIPT_CAMERA_SOUND_GENERATOR = """🎬 PROMPT 003 — GENERADOR DE GUION CINEMATOGRÁFICO EN INGLÉS + CAMBIOS DE CÁMARA + SONIDO (OPTIMIZADO PARA MUSE AI Y GOOGLE FLOW)
Actúa como guionista de Hollywood, director de fotografía y diseñador sonoro.
Ya tenemos creado el storyboard de la historia y la hoja maestra de personajes. Ahora debes convertir ese storyboard en un guion cinematográfico y técnico completo en texto, respetando exactamente las escenas que aparecen en el storyboard, con todos los diálogos hablados en INGLÉS (English) para monetización internacional.

DATOS DEL PROYECTO
Storyboard:
El storyboard completo creado en el paso 1: 10 imágenes de 6 viñetas, una por minuto. Cada escena debe corresponder exactamente a su viñeta.
Duración del bloque:
1 minuto = 6 escenas de 10 segundos (o el total de escenas del storyboard adjunto).

REGLA PRINCIPAL
Cada escena dura exactamente 10 segundos.
Debes mantener exactamente el mismo número y orden de escenas del storyboard.
NO debes agregar ni eliminar escenas.
Cada escena debe corresponder directamente a su respectiva viñeta del storyboard.

DIÁLOGOS EN INGLÉS (REGLA DE ORO DE 7–8 SEGUNDOS)
Todos los diálogos hablados deben estar en INGLÉS natural, dramático y emocional.
Los diálogos deben estar diseñados para poder decirse completamente dentro de los 10 segundos de duración de cada escena.
Como regla estricta de seguridad:
- El diálogo hablado NO debe superar 7–8 segundos (máximo entre 15 y 20 palabras en inglés por escena).
- Esto deja entre 2 y 3 segundos obligatorios para: pausas dramáticas, expresiones faciales, gestos, movimientos, miradas y reacciones visuales.
- Nunca cortes una frase simplemente porque terminó el tiempo. El diálogo de cada escena debe tener inicio y final completo dentro de esos 7–8 segundos. Si una idea necesita más tiempo, divídela entre diferentes escenas de forma natural.
- NO TODAS LAS ESCENAS NECESITAN DIÁLOGO: Si una escena funciona mejor visualmente (un beso, una mirada de impacto, descubrir una prueba), déjala como “Dialogue: No dialogue (Pure visual & sound tension).”

DIRECCIÓN DE CÁMARA MULTI-PLANO Y SONIDO (DENTRO DE CADA ESCENA DE 10s)
Para que el video generado en Muse AI / Google Flow sea dinámico como una serie real y nunca sea una toma estática aburrida, en cada escena de 10 segundos debes especificar:
1. CAMBIOS DE CÁMARA INTERNOS (2 a 3 cortes dentro del mismo lugar de la viñeta):
   - [00s–03s] Plano inicial (ej. Medium/Wide Shot estableciendo la acción de la viñeta).
   - [03s–07s] Corte a Primer Plano (Close-Up / Over-the-Shoulder del personaje hablando con lip-sync claro).
   - [07s–10s] Corte a Plano de Reacción (Extreme Close-Up de los ojos, manos temblando o impacto emocional del otro personaje).
2. DISEÑO SONORO (SFX & AMBIENCE) Y VOZ:
   - Especifica el timbre de voz constante de quien habla (ej. "Warm emotional young female voice" / "Deep authoritative male baritone voice").
   - Especifica los efectos de sonido realistas del entorno (ej. "Rain on window, footsteps on gravel, tense dramatic silence").

ESTRUCTURA OBLIGATORIA DE CADA ESCENA
Para cada escena utiliza exactamente esta estructura:

ESCENA [N] (Viñeta #[N] del Storyboard) — [MM:SS–MM:SS]
- Location: [Lugar exacto de la viñeta]
- Characters Present: [Nombres exactos según la Hoja de Personajes]
- Camera Cuts & Visual Action (10s):
  * [00s–03s]: [Encuadre + acción inicial]
  * [03s–07s]: [Corte de cámara + gesto mientras habla]
  * [07s–10s]: [Corte de cámara + reacción emocional final]
- Sound Design (SFX & Voice Tone): [Efectos de sonido del ambiente + tono de voz fijo del personaje]
- Dialogue (English, 6–8 sec max):
  [NOMBRE DEL PERSONAJE]: “[Diálogo en inglés breve, potente y 100% completo, máx. 18-20 palabras]”

RESULTADO FINAL
Entrega únicamente el bloque de escenas con la estructura anterior y, al final de las escenas, incluye este comando exacto listo para copiar y pegar junto con el guion en MUSE AI:

COMANDO FINAL PARA PEGAR EN MUSE AI (JUNTO CON EL STORYBOARD Y LA HOJA DE PERSONAJES ADJUNTOS):
"Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de 10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego únelos todos para que quede un solo video continuo en formato {aspect_ratio}.\""""


TEMPLATES: Dict[str, Dict[str, str]] = {
    "prompt_000": {
        "key": "prompt_000",
        "code": "PROMPT 000",
        "signature": "PROMPT_000_VIRAL_STORY_ARCHITECT",
        "title": "Arquitecto de Historias Virales (China / USA Micro-Drama)",
        "purpose": "Convierte la idea base en una arquitectura de alta retención con elenco, locaciones y sinopsis bloque por bloque.",
        "text": PROMPT_000_VIRAL_STORY_ARCHITECT,
    },
    "prompt_001": {
        "key": "prompt_001",
        "code": "PROMPT 001",
        "signature": "PROMPT_001_STORYBOARD_GENERATOR",
        "title": "Generador de Storyboard Cinematográfico (6 Escenas por Imagen)",
        "purpose": "Crea un storyboard visual en cuadrículas de 6 viñetas (3x2), una imagen por minuto de historia.",
        "text": PROMPT_001_STORYBOARD_GENERATOR,
    },
    "prompt_002": {
        "key": "prompt_002",
        "code": "PROMPT 002",
        "signature": "PROMPT_002_CHARACTER_SHEET_GENERATOR",
        "title": "Generador de la Hoja Maestra de Personajes (Una Sola Imagen)",
        "purpose": "Extrae del storyboard una hoja maestra con todos los personajes relevantes y su vestuario principal.",
        "text": PROMPT_002_CHARACTER_SHEET_GENERATOR,
    },
    "prompt_003": {
        "key": "prompt_003",
        "code": "PROMPT 003",
        "signature": "PROMPT_003_SCRIPT_CAMERA_SOUND_GENERATOR",
        "title": "Generador de Guion + Cámara + Sonido + Comando Muse AI",
        "purpose": "Convierte el storyboard en escenas de 10 s con cortes internos, SFX, diálogo en inglés y comando final para Muse AI.",
        "text": PROMPT_003_SCRIPT_CAMERA_SOUND_GENERATOR,
    },
}


# ---------------------------------------------------------------------------
# Valores del proyecto
# ---------------------------------------------------------------------------
DEFAULT_VISUAL_STYLE = (
    "prestige cinematic short-drama, photoreal, 35mm anamorphic glass, "
    "shallow depth of field, fine film grain, natural skin texture, "
    "muted teal-and-amber palette, practical motivated lighting"
)


def _fmt_number(value: float) -> str:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return str(value)
    if abs(number - round(number)) < 1e-9:
        return str(int(round(number)))
    return f"{number:.1f}"


def _extract_premise(brief_text: str) -> str:
    text = str(brief_text or "").strip()
    if not text:
        return ""
    patterns = (
        r"##\s+Premise\s*/\s*idea\s*(.*?)(?=\n##\s|\Z)",
        r"##\s+Premisa\s*(.*?)(?=\n##\s|\Z)",
        r"##\s+Idea\s*(.*?)(?=\n##\s|\Z)",
        r"##\s+Logline\s*(.*?)(?=\n##\s|\Z)",
    )
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.DOTALL | re.IGNORECASE)
        if match:
            value = match.group(1).strip()
            if value:
                return value
    return text if len(text) <= 4000 else text[:4000].rstrip() + "…"


def _story_idea_from_master(master: Dict[str, Any], brief_text: str = "") -> str:
    master = master if isinstance(master, dict) else {}
    episode = master.get("episode") if isinstance(master.get("episode"), dict) else {}
    characters = [c for c in (master.get("characters") or []) if isinstance(c, dict)]
    locations = [l for l in (master.get("locations") or []) if isinstance(l, dict)]
    acts = [a for a in (master.get("acts") or []) if isinstance(a, dict)]

    parts: List[str] = []
    premise = _extract_premise(brief_text)
    if premise:
        parts.append("PREMISE:\n" + premise)
    elif str(master.get("story_idea") or master.get("premise") or master.get("idea") or "").strip():
        parts.append("PREMISE:\n" + str(master.get("story_idea") or master.get("premise") or master.get("idea")).strip())

    if episode:
        parts.append(
            "EPISODE:\n"
            f"- Title: {episode.get('title') or episode.get('slug') or 'Untitled'}\n"
            f"- Series: {episode.get('series_title') or 'Untitled series'}\n"
            f"- Logline: {episode.get('logline') or '(no logline)'}\n"
            f"- Genre: {episode.get('genre') or 'short-drama'}\n"
            f"- Tone: {episode.get('tone') or 'high-stakes, fast-paced'}\n"
            f"- Setting: {episode.get('setting') or '(not specified)'}"
        )

    if characters:
        lines = ["CAST:"]
        for character in characters[:6]:
            name = character.get("name") or character.get("id") or "Character"
            archetype = character.get("archetype") or "principal"
            visual = (
                character.get("visual_reference")
                or character.get("reference_image")
                or character.get("appearance")
                or ""
            )
            voice = character.get("voice_lock") or ""
            line = f"- {name} ({archetype})"
            if visual:
                line += f": {visual}"
            if voice:
                line += f" | voice: {voice}"
            lines.append(line)
        parts.append("\n".join(lines))

    if locations:
        names = []
        for location in locations[:6]:
            names.append(str(location.get("name") or location.get("id") or "Location"))
        parts.append("LOCATIONS:\n- " + "\n- ".join(names))

    if acts:
        lines = ["ACT MAP:"]
        for act in acts:
            scenes = act.get("scenes") or []
            span = f"scenes {scenes[0]}-{scenes[1]}" if len(scenes) >= 2 else ""
            lines.append(
                f"- Act {act.get('act')} — {act.get('title') or ''} {('(' + span + ')') if span else ''}: "
                f"{act.get('goal') or ''}"
            )
        parts.append("\n".join(lines))

    idea = "\n\n".join(part.strip() for part in parts if part.strip()).strip()
    return idea or "(describe aquí la idea base: quién quiere qué, quién se lo impide y qué secreto mueve la historia)"


def visual_style_from_style(style: Dict[str, Any]) -> str:
    style = style if isinstance(style, dict) else {}
    visual = style.get("visual_style_lock") if isinstance(style.get("visual_style_lock"), dict) else {}
    look = str(visual.get("look") or "").strip()
    lighting = [str(x).strip() for x in (visual.get("lighting") or []) if str(x).strip()]
    camera = [str(x).strip() for x in (visual.get("camera_language") or []) if str(x).strip()]
    parts: List[str] = []
    if look:
        parts.append(look)
    if lighting:
        parts.append("Lighting palette: " + "; ".join(lighting[:3]) + ".")
    if camera:
        parts.append("Camera language: " + "; ".join(camera[:4]) + ".")
    return " ".join(parts).strip() or DEFAULT_VISUAL_STYLE


def values_from_master(
    master: Optional[Dict[str, Any]] = None,
    style: Optional[Dict[str, Any]] = None,
    brief_text: str = "",
    **overrides: Any,
) -> Dict[str, str]:
    master = master if isinstance(master, dict) else {}
    episode = master.get("episode") if isinstance(master.get("episode"), dict) else {}
    scenes = [s for s in (master.get("scenes") or []) if isinstance(s, dict)]

    total_scenes_raw = overrides.get("total_scenes") or episode.get("total_scenes") or len(scenes) or 60
    try:
        total_scenes = int(total_scenes_raw)
    except (TypeError, ValueError):
        total_scenes = 60
    total_scenes = max(1, total_scenes)

    total_seconds_raw = episode.get("total_seconds")
    try:
        total_seconds = float(total_seconds_raw) if total_seconds_raw else total_scenes * 10.0
    except (TypeError, ValueError):
        total_seconds = total_scenes * 10.0
    duration_minutes = overrides.get("duration_minutes") or (total_seconds / 60.0)

    total_grid_images_raw = overrides.get("total_grid_images") or math.ceil(total_scenes / 6)
    try:
        total_grid_images = int(total_grid_images_raw)
    except (TypeError, ValueError):
        total_grid_images = math.ceil(total_scenes / 6)

    story_idea = str(overrides.get("story_idea") or "").strip()
    if not story_idea:
        story_idea = _story_idea_from_master(master, brief_text)
    visual_style = str(overrides.get("visual_style") or "").strip()
    if not visual_style:
        visual_style = visual_style_from_style(style or {})
    aspect_ratio = str(overrides.get("aspect_ratio") or episode.get("aspect_master") or "16:9").strip()

    return {
        "story_idea": story_idea,
        "duration_minutes": _fmt_number(duration_minutes),
        "total_scenes": str(total_scenes),
        "total_grid_images": str(total_grid_images),
        "visual_style": visual_style,
        "aspect_ratio": aspect_ratio,
    }


# ---------------------------------------------------------------------------
# Render y exportación
# ---------------------------------------------------------------------------
def list_viral_templates() -> List[Dict[str, Any]]:
    import copy

    import nf_core as nf

    try:
        rules = nf.load_showrunner()
    except Exception:
        return []
    catalog = rules.get("viral_story_templates") if isinstance(rules, dict) else None
    items = catalog.get("items") if isinstance(catalog, dict) else None
    if not isinstance(items, list):
        return []
    return [copy.deepcopy(item) for item in items if isinstance(item, dict)]


def get_viral_template(template_id: str) -> Dict[str, Any]:
    templates = list_viral_templates()
    wanted = str(template_id or "").strip()
    for item in templates:
        if str(item.get("id") or "") == wanted:
            return item
    valid = ", ".join(str(item.get("id") or "") for item in templates) or "(ninguno)"
    raise KeyError(f"Plantilla viral desconocida: {template_id}. Válidas: {valid}")


def render_viral_niche_block(template: Dict[str, Any]) -> str:
    template = template if isinstance(template, dict) else {}

    def text(key: str) -> str:
        return str(template.get(key) or "").strip()

    def bullets(key: str) -> List[str]:
        return [str(value).strip() for value in (template.get(key) or []) if str(value).strip()]

    lines: List[str] = [
        "USA MEGA-NICHE ARCHETYPE — SELECCIÓN DEL USUARIO",
        "",
        f"- ID: {text('id')}",
        f"- Arquetipo: {text('label')}",
        f"- Categoría: {text('category')}",
        f"- Descripción del nicho (ES): {text('description')}",
    ]
    audience = text("audience")
    if audience:
        lines.append(f"- Audiencia: {audience}")
    lines += [
        "",
        "SEMILLA EN INGLÉS (US MARKET, en-US):",
        f"- Premise seed: {text('premise_seed')}",
        f"- Opening hook: {text('opening_hook')}",
        "",
        "BEATS OBLIGATORIOS:",
    ]
    lines += [f"- {item}" for item in bullets("must_include")] or ["- (sin beats definidos)"]
    lines += ["", "LOCACIONES PRIMARIAS:"]
    lines += [f"- {item}" for item in bullets("primary_locations")] or ["- (sin locaciones definidas)"]
    lines += ["", f"FIRMA VISUAL: {text('visual_signature')}"]
    series_hook = text("series_hook")
    if series_hook:
        lines.append(f"SERIES HOOK: {series_hook}")
    lines += [
        "",
        "REGLAS DE USO DEL ARQUETIPO:",
        "- Usa este arquetipo como el único motor de la historia; no mezcles nichos ni tramas de otros arquetipos.",
        "- Escribe títulos, elenco y sinopsis en inglés nativo de Estados Unidos (en-US).",
        "- Mantén de 3 a 5 personajes principales y de 3 a 5 locaciones.",
        "- Conserva 60 escenas / 10 minutos y un cliffhanger al final de cada minuto.",
        "- La semilla en inglés es el material canónico; esta selección manda sobre la idea base.",
    ]
    return "\n".join(lines).strip()


def viral_latam_templates(rules: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    if rules is None:
        try:
            import nf_core as nf
            rules = nf.load_showrunner()
        except Exception:
            rules = {}
    items = rules.get("viral_latam_to_usa_templates") if isinstance(rules, dict) else None
    if not isinstance(items, list):
        return []
    return [dict(item) for item in items if isinstance(item, dict)]


def find_viral_latam_template(template_id: str, rules: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
    wanted = str(template_id or "").strip().lower()
    if not wanted:
        return None
    for item in viral_latam_templates(rules):
        if str(item.get("id") or "").strip().lower() == wanted:
            return item
    return None


def render_viral_latam_block(templates: Optional[List[Dict[str, Any]]] = None) -> str:
    items = templates if templates is not None else viral_latam_templates()
    if not items:
        return ("(Catálogo no disponible: usa una estructura de micro-drama LATAM -> USA con "
                "gancho público, secreto familiar y status reversal.)")
    lines: List[str] = []
    for index, item in enumerate(items, start=1):
        beats = " -> ".join(str(beat).strip() for beat in (item.get("structure") or []) if str(beat).strip())
        lines.extend([
            f"{index}. {item.get('name') or item.get('id')} (`{item.get('id')}`)",
            f"   Inspiración: {item.get('source') or 'LATAM viral'} · {item.get('views') or '+500K'} vistas · "
            f"{item.get('genre') or 'micro-drama'}.",
            f"   Premisa: {item.get('premise') or ''}",
            f"   Gancho: {item.get('hook') or ''}",
            f"   Beats: {beats}",
            f"   Adaptación USA: {item.get('usa_adaptation') or ''}",
        ])
    return "\n".join(lines).strip()


def render_prompt(key: str, values: Dict[str, Any], niche: str = "") -> str:
    template = TEMPLATES.get(str(key))
    if not template:
        raise KeyError(f"Plantilla desconocida: {key}. Usa: {', '.join(PROMPT_ORDER)}")
    text = template["text"]
    for placeholder in PLACEHOLDERS:
        token = "{" + placeholder + "}"
        text = text.replace(token, str(values.get(placeholder, token)))
    if str(key) == "prompt_000" and VIRAL_TEMPLATES_TOKEN in text:
        text = text.replace(VIRAL_TEMPLATES_TOKEN, render_viral_latam_block())
    if str(key) == "prompt_000" and str(niche or "").strip():
        selected = get_viral_template(niche)
        text = text.rstrip() + "\n\n" + render_viral_niche_block(selected)
    return text


def unfilled_placeholders(text: str) -> List[str]:
    return [name for name in PLACEHOLDERS if "{" + name + "}" in str(text or "")]


def render_all(values: Dict[str, Any], niche: str = "") -> List[Dict[str, Any]]:
    prompts: List[Dict[str, Any]] = []
    for key in PROMPT_ORDER:
        meta = TEMPLATES[key]
        text = render_prompt(key, values, niche=niche)
        prompts.append({
            "key": key,
            "code": meta["code"],
            "signature": meta["signature"],
            "title": meta["title"],
            "purpose": meta["purpose"],
            "text": text,
            "chars": len(text),
            "words": len(re.findall(r"\S+", text)),
            "unfilled": unfilled_placeholders(text),
        })
    return prompts


def build_prompt_pack(
    master: Optional[Dict[str, Any]] = None,
    style: Optional[Dict[str, Any]] = None,
    brief_text: str = "",
    overrides: Optional[Dict[str, Any]] = None,
    niche: str = "",
) -> Dict[str, Any]:
    values = values_from_master(master, style, brief_text, **(overrides or {}))
    prompts = render_all(values, niche=niche)
    selected = get_viral_template(niche) if str(niche or "").strip() else None
    episode = (master or {}).get("episode") if isinstance((master or {}).get("episode"), dict) else {}
    return {
        "schema_version": "1.0",
        "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "project": {
            "slug": str(episode.get("slug") or ""),
            "title": str(episode.get("title") or ""),
            "duration_minutes": values["duration_minutes"],
            "total_scenes": values["total_scenes"],
            "total_grid_images": values["total_grid_images"],
            "aspect_ratio": values["aspect_ratio"],
        },
        "values": values,
        "prompts": prompts,
        "viral_template": ({
            "id": str(selected.get("id") or ""),
            "label": str(selected.get("label") or ""),
            "category": str(selected.get("category") or ""),
            "rpm_rank": selected.get("rpm_rank"),
            "description": str(selected.get("description") or ""),
        } if selected else None),
    }


def _atomic_write_text(path: Path, text: str) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    tmp.replace(path)
    return path


def render_markdown(pack: Dict[str, Any]) -> str:
    project = pack.get("project") or {}
    values = pack.get("values") or {}
    lines: List[str] = [
        f"# MASTER PROMPTS — {project.get('title') or project.get('slug') or 'Episodio'}",
        "",
        f"- Generado: {pack.get('generated_at')}",
        f"- Duración: {values.get('duration_minutes')} minuto(s)",
        f"- Escenas: {values.get('total_scenes')}",
        f"- Grids de 1 minuto: {values.get('total_grid_images')}",
        f"- Aspect ratio: {values.get('aspect_ratio')}",
        f"- Estilo visual: {values.get('visual_style')}",
        "",
        "> Todos los prompts están rellenados con los datos del proyecto. Copia cada bloque completo.",
        "",
    ]
    for prompt in pack.get("prompts") or []:
        lines += [
            "---",
            "",
            f"## {prompt['code']} — {prompt['title']}",
            "",
            f"_{prompt['purpose']}_",
            "",
            f"**{prompt['chars']:,} caracteres · {prompt['words']:,} palabras**",
            "",
            "````text",
            prompt["text"],
            "````",
            "",
        ]
    return "\n".join(lines)


def render_plain(pack: Dict[str, Any]) -> str:
    project = pack.get("project") or {}
    values = pack.get("values") or {}
    lines: List[str] = [
        "=" * 78,
        f"NOVEL FACTORY — MASTER PROMPTS — {project.get('title') or project.get('slug') or 'Episodio'}",
        "=" * 78,
        f"Generado: {pack.get('generated_at')}",
        f"Duración: {values.get('duration_minutes')} minuto(s) · Escenas: {values.get('total_scenes')} · "
        f"Grids: {values.get('total_grid_images')} · Aspect: {values.get('aspect_ratio')}",
        "",
    ]
    for prompt in pack.get("prompts") or []:
        lines += [
            "",
            "=" * 78,
            f"{prompt['code']} — {prompt['title']}",
            prompt["purpose"],
            "=" * 78,
            "",
            prompt["text"],
            "",
        ]
    return "\n".join(lines)


def write_prompt_pack(root: Path, pack: Dict[str, Any]) -> Dict[str, Path]:
    root = Path(root)
    written: Dict[str, Path] = {}
    written["markdown"] = _atomic_write_text(root / "MASTER_PROMPTS.md", render_markdown(pack))
    written["plain"] = _atomic_write_text(root / "MASTER_PROMPTS.txt", render_plain(pack))
    written["json"] = _atomic_write_text(
        root / "master_prompts.json",
        json.dumps(pack, ensure_ascii=False, indent=2) + "\n",
    )
    prompts_dir = root / "prompts"
    for prompt in pack.get("prompts") or []:
        filename = f"{prompt['signature']}.txt"
        written[prompt["key"]] = _atomic_write_text(
            prompts_dir / filename,
            prompt["text"].strip() + "\n",
        )
    return written


# ---------------------------------------------------------------------------
# Lotes de 1 minuto para Muse AI (6 escenas por bloque)
# ---------------------------------------------------------------------------
MUSE_FINAL_COMMAND_HEADER = (
    "COMANDOS FINALES PARA PEGAR EN MUSE AI (ELIGE SEGÚN EL CANAL):"
)
MUSE_FINAL_COMMAND_TEMPLATE = (
    "Usando estrictamente la apariencia y vestuario de los personajes en la Hoja de Personajes adjunta "
    "y recreando en orden cada viñeta del Storyboard adjunto: Haz un video cinematográfico realista de "
    "10 segundos por cada escena respetando los cambios de cámara ([00s-03s], [03s-07s], [07s-10s]), "
    "el diseño sonoro y los diálogos hablados en INGLÉS con la misma voz para cada personaje, y luego "
    "únelos todos para que quede un solo video continuo en formato {orientation} {aspect_ratio} "
    "{destination}."
)
MUSE_FINAL_COMMAND = MUSE_FINAL_COMMAND_TEMPLATE
MUSE_ATTACH_LINE = (
    "📎 ADJUNTAR EN MUSE AI: REF_CAST_MASTER.png (Hoja de Personajes) + "
    "REF_GRID_MIN_{batch:02d}.png (Storyboard Minuto {minute}: Escenas {first}–{last})"
)


def _muse_final_command(batch_number: int, orientation: str, aspect: str, destination: str = "") -> str:
    return MUSE_FINAL_COMMAND_TEMPLATE.format(
        orientation=orientation,
        aspect_ratio=aspect,
        destination=destination.strip(),
    )


ROLE_LABELS = {
    "protagonist": "Protagonista",
    "love_interest": "Interés romántico",
    "antagonist": "Antagonista",
    "antagonist_heir": "Heredero antagonista",
    "ally": "Aliada",
    "mentor": "Mentor",
    "supporting": "Secundario",
}


def project_characters(master: Optional[Dict[str, Any]]) -> List[Dict[str, Any]]:
    master = master if isinstance(master, dict) else {}
    raw = master.get("characters_locked") or master.get("characters") or []
    if isinstance(raw, dict):
        raw = list(raw.values())
    return [character for character in raw if isinstance(character, dict)]


def _character_role(character: Dict[str, Any]) -> str:
    role = str(character.get("role") or character.get("archetype") or "principal").strip().lower()
    return ROLE_LABELS.get(role, role or "principal")


def _character_age(character: Dict[str, Any]) -> str:
    explicit = str(character.get("age") or character.get("age_range") or character.get("apparent_age") or "").strip()
    if explicit:
        return explicit
    text = " ".join(str(character.get(key) or "") for key in (
        "visual_reference", "description", "appearance",
    ))
    patterns = (
        r"\b(?:in (?:her|his) )?((?:early|mid|late)[- ](?:twenties|thirties|forties|fifties|sixties|seventies))\b",
        r"\b(?:in (?:her|his) )?(twenties|thirties|forties|fifties|sixties|seventies)\b",
        r"\baround (thirty|forty|fifty|sixty|seventy)\b",
    )
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return match.group(1).lower().replace(" ", "-")
    return "adulto"


def _character_visual(character: Dict[str, Any]) -> str:
    visual = str(
        character.get("visual_reference")
        or character.get("description")
        or character.get("appearance")
        or ""
    ).strip()
    return visual or "rasgos y complexión definidos por su ficha de casting"


def _character_wardrobe(character: Dict[str, Any]) -> str:
    for key in ("wardrobe_lock", "wardrobe", "signature_wardrobe", "outfit_lock"):
        value = character.get(key)
        if isinstance(value, list):
            value = next((str(item).strip() for item in value if str(item).strip()), "")
        if str(value or "").strip():
            return str(value).strip()
    wardrobes = character.get("wardrobe_by_act") or []
    if isinstance(wardrobes, list):
        for item in wardrobes:
            if str(item or "").strip():
                return str(item).strip()
    match = re.search(r"signature\s+(.+?)(?:\.|$)", _character_visual(character), flags=re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return "el vestuario principal descrito en su ficha de casting"


def build_cast_sheet_prompt(master: Optional[Dict[str, Any]]) -> str:
    """Prompt 100% copiable para REF_CAST_MASTER.png, sin adjuntos ni corchetes."""
    characters = project_characters(master)
    lines = [
        "Actúa como director de casting y diseñador de personajes. Genera UNA SOLA IMAGEN horizontal 16:9 "
        "que muestre juntos, de cuerpo completo, de pie, mirando al frente sobre un fondo gris neutro de "
        "estudio (#808080) y sin tocarse entre sí, a los siguientes personajes de nuestra novela en estilo "
        "Cinematográfico Realista 35mm:",
        "",
    ]
    for index, character in enumerate(characters, start=1):
        name = str(character.get("name") or character.get("id") or "PERSONAJE").strip().upper()
        lines.append(
            f"{index}. {name} — Rol: {_character_role(character)}. "
            f"Edad: {_character_age(character)}. "
            f"Rasgos físicos: {_character_visual(character)}. "
            f"Vestuario fijo: {_character_wardrobe(character)}."
        )
    if not characters:
        lines.append(
            "1. LOS PERSONAJES PRINCIPALES DEL PROYECTO — usa exactamente los nombres, roles, "
            "edades y vestuarios definidos en story_brief.md y master_episode.json."
        )
    lines += [
        "",
        "Coloca únicamente debajo de cada personaje su nombre en mayúsculas. Mantén exactamente los "
        "mismos rostros, peinados y vestuarios en todas las imágenes del storyboard y de los lotes de "
        "Muse AI. Sin texto adicional, sin títulos, sin frases, sin logos, sin marcas de agua; solo la "
        "imagen de los personajes y sus nombres.",
    ]
    return "\n".join(lines)


def _muse_timecode(seconds: float) -> str:
    total = max(0, int(round(float(seconds))))
    return f"{total // 60:02d}:{total % 60:02d}"


def _aspect_ratio_from(master: Dict[str, Any], style: Dict[str, Any], override: str = "") -> str:
    if str(override or "").strip():
        return str(override).strip()
    episode = master.get("episode") if isinstance(master.get("episode"), dict) else {}
    return str(episode.get("aspect_master") or style.get("master_aspect") or "16:9").strip()


def _character_index(master: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    index: Dict[str, Dict[str, Any]] = {}
    for character in master.get("characters") or []:
        if not isinstance(character, dict):
            continue
        for key in (character.get("id"), character.get("name")):
            text = str(key or "").strip().lower()
            if text:
                index.setdefault(text, character)
    return index


def _voice_tone(character: Optional[Dict[str, Any]], style: Dict[str, Any]) -> str:
    if not isinstance(character, dict):
        return ""
    explicit = str(character.get("voice_lock") or "").strip()
    if explicit:
        return explicit
    archetype = str(character.get("archetype") or "").strip().lower()
    archetypes = ((style.get("voice_lock") or {}).get("character_voice_archetypes") or {})
    return str(archetypes.get(archetype) or "").strip()


def _scene_characters(master: Dict[str, Any], scene: Dict[str, Any]) -> List[str]:
    import nf_core as nf

    index = _character_index(master)
    names: List[str] = []

    def add(raw: Any) -> None:
        text = str(raw or "").strip()
        if not text:
            return
        character = index.get(text.lower()) or {}
        name = str(character.get("name") or character.get("id") or text).strip()
        if name and name not in names:
            names.append(name)

    for raw in scene.get("characters") or []:
        add(raw)
    if not names:
        for entry in nf.scene_dialogue_lines(scene):
            add(entry.get("speaker"))
    return names


def _muse_cut_rows(scene: Dict[str, Any]) -> List[Dict[str, str]]:
    cuts = [c for c in (scene.get("internal_cuts") or []) if isinstance(c, dict)]
    fallbacks = (
        "Open on the action of the storyboard panel; establish who is in control.",
        "Hard cut to the speaking character; lip-sync is clear and the gesture lands the line.",
        "Hard cut to the emotional reaction: eyes, trembling hands, impact of the line.",
    )
    rows: List[Dict[str, str]] = []
    for idx, (label, fallback) in enumerate(zip(("00s–03s", "03s–07s", "07s–10s"), fallbacks)):
        if cuts:
            if idx < len(cuts):
                cut = cuts[idx]
            elif len(cuts) >= 2:
                cut = cuts[-1]
            else:
                cut = cuts[0]
            framing = str(cut.get("framing") or "").strip()
            action = str(cut.get("action") or "").strip()
        else:
            framing = ("wide establishing shot", "medium shot", "extreme close-up")[idx]
            action = ""
        rows.append({
            "range": label,
            "framing": framing or ("wide establishing shot", "medium shot", "extreme close-up")[idx],
            "action": action or fallback,
        })
    return rows


def render_muse_scene_block(
    scene: Dict[str, Any],
    master: Dict[str, Any],
    style: Dict[str, Any],
    start_seconds: Optional[float] = None,
) -> str:
    import nf_core as nf

    sid = int(scene.get("scene_id") or 0)
    duration = float(scene.get("duration_s") or nf.SCENE_SECONDS)
    start = float(start_seconds) if start_seconds is not None else max(0.0, (sid - 1) * duration)
    end = start + duration
    characters = _scene_characters(master, scene)
    index = _character_index(master)
    voice_notes: List[str] = []
    dialogue_lines = nf.scene_dialogue_lines(scene)
    for entry in dialogue_lines:
        speaker = str(entry.get("speaker") or "").strip()
        character = index.get(speaker.lower()) if speaker else None
        tone = _voice_tone(character, style)
        if tone and f"{speaker.upper()} — {tone}" not in voice_notes:
            voice_notes.append(f"{speaker.upper()} — {tone}")
    voice_text = "; ".join(voice_notes) or "Natural US English voices with fixed tone per character."
    sfx = str(scene.get("sfx_ambience") or "").strip() or "natural room tone, footsteps, cloth movement, tense silence"
    location = str(scene.get("location") or "the storyboard location").strip()

    lines: List[str] = [
        f"ESCENA {sid} (Viñeta #{sid} del Storyboard) — {_muse_timecode(start)}–{_muse_timecode(end)}",
        f"- Location: {location}",
        f"- Characters Present: {', '.join(characters) if characters else 'the characters visible in the storyboard panel'}",
        "- Camera Cuts & Visual Action (10s):",
    ]
    for row in _muse_cut_rows(scene):
        lines.append(f"  * [{row['range']}]: {row['framing']} — {row['action']}")
    lines.append(f"- Sound Design (SFX & Voice Tone): {sfx}. Voice tone: {voice_text}")
    if dialogue_lines:
        lines.append("- Dialogue (English, 6–8 sec max):")
        for entry in dialogue_lines:
            speaker = (entry.get("speaker") or "CHARACTER").upper()
            delivery = f" ({entry['delivery']})" if entry.get("delivery") else ""
            lines.append(f'  {speaker}{delivery}: "{entry["line"]}"')
    else:
        lines.append("- Dialogue (English, 6–8 sec max):")
        lines.append("  No dialogue (Pure visual & sound tension).")
    return "\n".join(lines)


def build_muse_batches(
    master: Dict[str, Any],
    style: Optional[Dict[str, Any]] = None,
    aspect_ratio: str = "",
) -> List[Dict[str, Any]]:
    import nf_core as nf

    style = style if isinstance(style, dict) else {}
    scenes = nf.ordered_scenes(master)
    aspect = _aspect_ratio_from(master, style, aspect_ratio)
    batches: List[Dict[str, Any]] = []
    for position in range(0, len(scenes), 6):
        group = scenes[position:position + 6]
        if not group:
            continue
        first_id = int(group[0].get("scene_id") or position + 1)
        last_id = int(group[-1].get("scene_id") or position + len(group))
        start_seconds = (first_id - 1) * nf.SCENE_SECONDS
        end_seconds = last_id * nf.SCENE_SECONDS
        batch_number = len(batches) + 1
        blocks = [render_muse_scene_block(scene, master, style) for scene in group]
        attach = MUSE_ATTACH_LINE.format(
            batch=batch_number,
            minute=batch_number,
            first=first_id,
            last=last_id,
        )
        save_as = f"raw_clips/minute_{batch_number:02d}.mp4"
        command_169 = _muse_final_command(
            batch_number, "horizontal", "16:9", "para YouTube"
        )
        command_916 = _muse_final_command(
            batch_number, "vertical", "9:16", "para Reels, TikTok y Shorts"
        )
        script = "\n\n".join(blocks)
        prompt_169 = "\n\n".join([
            script,
            "COMANDO FINAL (16:9 YouTube):",
            f"\"{command_169}\"",
        ])
        prompt_916 = "\n\n".join([
            script,
            "COMANDO FINAL (9:16 Reels/TikTok/Shorts):",
            f"\"{command_916}\"",
        ])
        batches.append({
            "batch_id": batch_number,
            "minute": batch_number,
            "scenes": [int(s.get("scene_id") or 0) for s in group],
            "start_seconds": int(start_seconds),
            "end_seconds": int(end_seconds),
            "start_timecode": _muse_timecode(start_seconds),
            "end_timecode": _muse_timecode(end_seconds),
            "aspect_ratio": aspect,
            "aspect_ratio_vertical": "9:16",
            "attach": attach,
            "attach_instruction": attach,
            "reference_images": ["REF_CAST_MASTER.png", f"REF_GRID_MIN_{batch_number:02d}.png"],
            "save_as": save_as,
            "save_as_16x9": save_as,
            "save_as_9x16": f"raw_clips/minute_{batch_number:02d}_vertical.mp4",
            "prompt": prompt_169,
            "prompt_16x9_youtube": prompt_169,
            "prompt_9x16_vertical": prompt_916,
            "muse_command": command_169,
            "muse_command_916": command_916,
        })
    return batches


def render_muse_batches_text(master: Dict[str, Any], batches: List[Dict[str, Any]]) -> str:
    import nf_core as nf

    episode = nf.episode_meta(master)
    title = str(episode.get("title") or episode.get("slug") or "Episodio")
    lines: List[str] = [
        "=" * 78,
        f"NOVEL FACTORY — MUSE AI — LOTES DE 1 MINUTO (6 ESCENAS) — {title}",
        "=" * 78,
        f"Escenas: {len(nf.ordered_scenes(master))} · Lotes: {len(batches)} · 10 s por escena",
        "Cada bloque incluye los adjuntos requeridos y DOS comandos finales: 16:9 (YouTube) y 9:16 (Reels).",
        "",
    ]
    for batch in batches:
        first = batch["scenes"][0] if batch.get("scenes") else 0
        last = batch["scenes"][-1] if batch.get("scenes") else 0
        lines += [
            "=" * 78,
            f"BLOQUE {batch['batch_id']:02d} — MINUTO {batch['minute']:02d} — "
            f"ESCENAS {first}–{last} — {batch['start_timecode']}–{batch['end_timecode']}",
            "=" * 78,
            "",
            batch["attach"],
            "",
            "=== COPIA 16:9 (YouTube) ===",
            batch["prompt_16x9_youtube"],
            "",
            "=== COPIA 9:16 (Reels / TikTok / Shorts) ===",
            batch["prompt_9x16_vertical"],
            "",
        ]
    return "\n".join(lines)


def write_muse_batch_files(
    root: Path,
    master: Dict[str, Any],
    style: Optional[Dict[str, Any]] = None,
    basename: str = "muse_ai_batches_queue",
    aspect_ratio: str = "",
) -> Dict[str, Any]:
    root = Path(root)
    style = style if isinstance(style, dict) else {}
    batches = build_muse_batches(master, style, aspect_ratio)
    episode = master.get("episode") if isinstance(master.get("episode"), dict) else {}
    aspect = _aspect_ratio_from(master, style, aspect_ratio)
    text = render_muse_batches_text(master, batches)
    txt_path = _atomic_write_text(root / f"{basename}.txt", text)
    payload = {
        "schema_version": "1.0",
        "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "episode": episode.get("slug"),
        "title": episode.get("title"),
        "aspect_ratio": aspect,
        "aspect_ratios": {"youtube": "16:9", "reels": "9:16"},
        "scene_seconds": 10,
        "scenes_per_batch": 6,
        "count": len(batches),
        "items": batches,
    }
    json_path = _atomic_write_text(
        root / f"{basename}.json",
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
    )
    return {"txt": txt_path, "json": json_path, "batches": batches}


def main(argv: Optional[List[str]] = None) -> int:
    """Render rápido desde consola (útil para depurar la librería)."""
    import argparse

    parser = argparse.ArgumentParser(description="Renderiza los prompts maestros de novel_factory.")
    parser.add_argument("prompt", nargs="?", default="all", choices=list(PROMPT_ORDER) + ["all"])
    parser.add_argument("--idea", default="", help="Idea base para el marcador {story_idea}.")
    parser.add_argument("--project", default="", help="Proyecto existente del que tomar los datos.")
    args = parser.parse_args(argv)

    master: Dict[str, Any] = {}
    style: Dict[str, Any] = {}
    brief_text = ""
    if args.project:
        import nf_core as nf

        paths = nf.resolve_project(args.project)
        master = nf.load_master(paths["root"])
        style = nf.load_style_locks()
        brief_path = paths["root"] / "story_brief.md"
        if brief_path.exists():
            brief_text = brief_path.read_text(encoding="utf-8", errors="replace")

    overrides = {"story_idea": args.idea} if args.idea else {}
    pack = build_prompt_pack(master, style, brief_text, overrides)
    prompts = pack["prompts"]
    if args.prompt != "all":
        prompts = [p for p in prompts if p["key"] == args.prompt]
    for prompt in prompts:
        print("=" * 78)
        print(f"{prompt['code']} — {prompt['title']}")
        print("=" * 78)
        print(prompt["text"])
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

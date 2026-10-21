#!/usr/bin/env python3
"""01 — Del brief al JSON Maestro de 60 escenas (10 min).

No llama a ninguna API. Genera:
  1) story_brief.md  — la fuente (idea, sinopsis o transcripción).
  2) llm_prompt.md   — el prompt exacto para Claude / Gemini / ChatGPT, con el
                       esquema JSON, las reglas del showrunner y el brief.
  3) master_episode.json — el JSON Maestro validado (tras pegar la respuesta).

Flujo recomendado:
  python generators/01_story_to_master_json.py mi_episodio --idea "..." --brief
  -> pegas llm_prompt.md en el LLM y guardas su respuesta como llm_response.json
  python generators/01_story_to_master_json.py mi_episodio --ingest llm_response.json

Si el LLM no puede devolver 60 escenas de una vez, usa --part 1 / --part 2 y
luego ingiere los dos archivos juntos.

Modo de calibración sin LLM:
  python generators/01_story_to_master_json.py demo_contract --template
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from string import Template
from typing import Any, Dict, List, Optional, Tuple

NF_ROOT = Path(__file__).resolve().parent.parent
GENERATORS_DIR = Path(__file__).resolve().parent
for _path in (NF_ROOT, GENERATORS_DIR):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))
import nf_core as nf  # noqa: E402
import master_prompts_library as mpl  # noqa: E402


# ---------------------------------------------------------------------------
# Brief de historia
# ---------------------------------------------------------------------------
def build_brief_markdown(
    slug: str,
    title: str,
    idea: str,
    source_text: str,
    genre: str,
    personaje: str,
    episode_number: int,
) -> str:
    parts = [
        f"# Story Brief — {title or slug}",
        "",
        f"- **Slug:** {slug}",
        f"- **Episode:** {episode_number}",
        f"- **Genre:** {genre}",
        f"- **Language:** English (US) — all dialogue and prompts",
        f"- **Publisher persona (USA WHITE):** {personaje}",
        "",
        "## Premise / idea",
        "",
        idea.strip() or "_Describe here the premise in 3-10 lines: who wants what, who blocks it, what secret powers the story._",
        "",
    ]
    if source_text.strip():
        parts += [
            "## Source material",
            "",
            "```text",
            source_text.strip(),
            "```",
            "",
        ]
    parts += [
        "## Non-negotiables",
        "",
        "- 60 scenes x 10 seconds = 600 seconds (10:00) master in 16:9.",
        "- English only. US short-drama cadence: short lines, concrete stakes, no exposition dumps.",
        "- 6 acts of 10 scenes. Cliffhanger at 10 / 20 / 30 / 40 / 50. Payoff at 59 and a next-episode hook at 60.",
        "- One first-frame still per scene (16:9, center-weighted so a 9:16 crop works).",
        "- Native audio in the generated clip: dialogue + diegetic ambience only. No music.",
        "- No real celebrities, brands, explicit content, graphic violence or hate.",
        "- Reference images define faces: never describe age, eye color or base hair color in prompts.",
        "",
        "## Deliverable",
        "",
        "The JSON described in `llm_prompt.md`, saved as `llm_response.json` next to this file.",
        "",
    ]
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Prompt para el LLM
# ---------------------------------------------------------------------------
def _acts_block(rules: Dict[str, Any]) -> str:
    lines: List[str] = []
    for act in rules.get("acts") or []:
        lines.append(
            f"### Act {act.get('act')} — {act.get('title')} (scenes {act.get('scenes', [0, 0])[0]}-{act.get('scenes', [0, 0])[1]})\n"
            f"Goal: {act.get('goal')}\n"
            f"Must happen: " + "; ".join(act.get("must_happen") or []) + "\n"
            f"Retention device: {act.get('retention_device')}\n"
            f"Dopamine point: {act.get('dopamine_point')}"
        )
    return "\n\n".join(lines)


def _retention_block(rules: Dict[str, Any]) -> str:
    eng = rules.get("retention_engine") or {}
    fmt = rules.get("format") or {}
    max_words = fmt.get("max_scene_words", 15)
    max_line = fmt.get("max_line_words", 15)
    max_speech = fmt.get("max_scene_speech_seconds", 8.5)
    wps = fmt.get("speech_words_per_second", 2.5)
    return (
        f"- Total scenes: {fmt.get('total_scenes')} x {fmt.get('scene_seconds')} s = {fmt.get('total_seconds')} s.\n"
        f"- Dialogue per scene: {max_words} words TOTAL across all speakers (hard cap). "
        f"Target {fmt.get('words_per_scene_dialogue')}. Never exceed {max_words}.\n"
        f"- Max {max_line} words per single line. At ~{wps} words/second that is <= {max_speech} s of speech "
        f"in a {fmt.get('scene_seconds')} s scene, leaving room for pauses.\n"
        f"- Internal cuts per scene: exactly 3 shots at 0/3/7 s, ranges 00s-03s, 03s-07s and 07s-10s. "
        "Shot 1 starts in motion from the storyboard panel, Shot 2 is close-up/OTS dialogue/action, "
        "Shot 3 is tight close-up/reaction/insert.\n"
        "- Causal order is strict: consequences never precede their cause, clues are revealed once, and every "
        "location change needs a visible transition. Group 3-6 consecutive scenes per dramatic situation/location block.\n"
        f"- Open-loop types allowed: " + "; ".join(eng.get("open_loop_types") or []) + ".\n"
        f"- Dopamine cadence: {eng.get('dopamine_cadence')}\n"
        f"- Cliffhanger types allowed: " + "; ".join(eng.get("cliffhanger_types") or []) + ".\n"
        f"- Forbidden: " + "; ".join(eng.get("forbidden") or []) + "."
    )


def _viral_latam_block(rules: Dict[str, Any]) -> str:
    templates = [t for t in (rules.get("viral_latam_to_usa_templates") or []) if isinstance(t, dict)]
    if not templates:
        return ""
    lines = [
        "Use one of these six PROVEN LATAM -> USA structures as the skeleton of the episode.",
        "Keep the structure, stakes and hook type; adapt names, locations and dialogue to the brief.",
        "",
    ]
    for index, template in enumerate(templates, start=1):
        beats = template.get("structure") or []
        lines += [
            f"### {index}. {template.get('id')} — {template.get('name')} "
            f"({template.get('source')}, {template.get('views')} views)",
            f"Genre: {template.get('genre')} | Setting: {template.get('setting')}",
            f"Premise: {template.get('premise')}",
            f"Hook: {template.get('hook')}",
            "Structure: " + " -> ".join(str(beat) for beat in beats),
            f"USA adaptation: {template.get('usa_adaptation')}",
            "",
        ]
    return "\n".join(lines)


def _selected_viral_template_block(rules: Dict[str, Any], template_id: str) -> str:
    wanted = str(template_id or "").strip().lower()
    if not wanted:
        return ""
    for template in rules.get("viral_latam_to_usa_templates") or []:
        if not isinstance(template, dict):
            continue
        if str(template.get("id") or "").strip().lower() == wanted:
            return (
                f"## SELECTED VIRAL STRUCTURE (MANDATORY)\n\n"
                f"Build the whole episode on `{template.get('id')}` — {template.get('name')}.\n"
                f"Follow its six-beat structure in order and keep its hook promise.\n"
            )
    return (
        f"## SELECTED VIRAL STRUCTURE (MANDATORY)\n\n"
        f"The requested template `{template_id}` does not exist. Choose the closest one from the catalog above "
        f"and state its id in the episode logline.\n"
    )


def _part_plan(part: str) -> Dict[str, Any]:
    """Traduce --part a rango de escenas + reglas de prompts/teasers.

    Acepta 'full', la división clásica en 2 ('1'/'2') y las etiquetas explícitas
    '1of2'/'2of2' y '1of3'/'2of3'/'3of3'.
    """
    key = str(part or "full").strip().lower()
    if key in ("", "full", "0", "all"):
        return {
            "label": "",
            "lo": 1, "hi": 60,
            "rule": "Write the COMPLETE episode: all 60 scenes, Acts 1-6. Do not summarize or skip scenes.",
            "teasers": "Teasers: include all 3 (6 consecutive scenes each, 60 s each).",
        }
    if key in ("1of3", "2of3", "3of3"):
        idx = int(key[0])
        lo, hi = (idx - 1) * 20 + 1, idx * 20
        label = f"PART {idx} OF 3"
    else:
        idx = 1 if key in ("1", "1of2") else 2 if key in ("2", "2of2") else None
        if idx is None:
            raise NFError(f"--part inválido: {part!r} (usa full, 1of3/2of3/3of3 o 1of2/2of2)")
        lo, hi = (1, 30) if idx == 1 else (31, 60)
        label = f"PART {idx} OF 2"

    teaser_ranges = {1: (1, 6), 2: (21, 26), 3: (55, 60)}
    within = [tid for tid, (a, b) in teaser_ranges.items() if a >= lo and b <= hi]
    if within:
        teaser_rule = (
            "Teasers: include ONLY teaser(s) " + ", ".join(str(t) for t in within) +
            " (6 consecutive scenes each). Omit the others."
        )
    else:
        teaser_rule = "Teasers: this part covers no full teaser window; return an empty teasers list."

    return {
        "label": label,
        "lo": lo,
        "hi": hi,
        "rule": (
            f"{label}: write ONLY scenes {lo}-{hi}. scene_id must run {lo}..{hi}. "
            "Keep the exact same characters, wardrobe, props and locations as the rest of the episode. "
            "Do not summarize any scene."
        ),
        "teasers": teaser_rule,
    }


def export_master_prompts(
    paths: Dict[str, Path],
    master: Optional[Dict[str, Any]] = None,
    brief_text: str = "",
    overrides: Optional[Dict[str, Any]] = None,
) -> Optional[Dict[str, Any]]:
    """Escribe MASTER_PROMPTS.md/.txt/.json + prompts/*.txt junto al proyecto."""
    try:
        style = nf.load_style_locks()
        pack = mpl.build_prompt_pack(master or {}, style, brief_text, overrides)
        written = mpl.write_prompt_pack(paths["root"], pack)
        nf.ok(f"Prompts maestros: {written['markdown'].name} (+4 en prompts/)")
        return pack
    except Exception as exc:  # noqa: BLE001 - nunca bloquea la creación del maestro
        nf.warn(f"No se pudieron exportar los prompts maestros: {exc}")
        return None


def _read_brief_text(paths: Dict[str, Path]) -> str:
    brief = paths["root"] / "story_brief.md"
    if not brief.exists():
        return ""
    try:
        return brief.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def build_llm_prompt(
    slug: str,
    title: str,
    brief_md: str,
    rules: Dict[str, Any],
    style: Dict[str, Any],
    personaje: str,
    episode_number: int,
    part: str = "full",
    context_text: str = "",
    viral_template: str = "",
) -> str:
    fmt = rules.get("format") or {}
    identity = style.get("identity_lock") or {}
    voice = style.get("voice_lock") or {}
    visual = style.get("visual_style_lock") or {}

    plan = _part_plan(part)
    part_rule = plan["rule"]
    teaser_rule = plan["teasers"]

    schema = """{
  "episode": {
    "slug": "$slug",
    "title": "$title",
    "series_title": "Series name",
    "episode_number": $episode_number,
    "logline": "1-2 sentences. Who wants what, who blocks it, what it costs.",
    "genre": "romantic suspense short-drama",
    "language": "en-US",
    "audience": "US women 25-55, short-drama and audio-series viewers",
    "tone": "cinematic, intimate, high-stakes, fast-paced",
    "hook_line": "The line that opens the episode (also usable as the teaser headline)."
  },
  "characters": [
    {
      "id": "nora",
      "name": "Nora Hale",
      "role": "protagonist",
      "archetype": "protagonist",
      "pronoun": "she",
      "voice_lock": "one line describing the voice, native US English",
      "visual_reference": "One-time casting description for the character reference sheet ONLY: age range, build, hair, eyes, skin tone, signature styling. It is never repeated in scene prompts (the reference images define the face).",
      "reference_image": "optional filename if the user already owns a reference image for this character",
      "wardrobe_by_act": ["act 1 outfit", "act 2 outfit", "act 3 outfit", "act 4 outfit", "act 5 outfit", "act 6 outfit"]
    }
  ],
  "locations": [
    {"id": "lighthouse", "name": "Hale lighthouse", "visual": "one line of production design"}
  ],
  "acts": [
    {"act": 1, "title": "The Bait", "goal": "one line", "cliffhanger": "what the audience learns or fears at scene 10"}
  ],
  "scenes": [
    {
      "scene_id": 1,
      "act": 1,
      "beat": "cold_open_hook",
      "location": "Hale lighthouse cliff edge, storm dusk",
      "time_of_day": "storm dusk",
      "characters": ["nora"],
      "on_screen_hook": "5-10 word teaser headline (only for scenes 1, 10, 20, 30, 40, 50, 60; empty elsewhere)",
      "first_frame_prompt": "Cinematic still of Nora Hale (the character in reference_nora.png), wide establishing shot, at the Hale lighthouse cliff edge, storm dusk. Nora strides along the cliff edge, coat snapping in the wind, jaw set, eyes bright with contained anger. Wardrobe: charcoal wool coat over a dark sweater, dark jeans, rain-wet hair. Keep Nora Hale's face and wardrobe identical to reference_nora.png. Framing keeps the face unobstructed and centered for a 9:16 crop. 45-80 words, no style suffix (it is appended automatically), no text or logos.",
      "internal_cuts": [
        {"at": 0.0, "range": "00s-03s", "framing": "wide establishing shot", "action": "Nora strides along the cliff edge, the lighthouse dark behind her, salt wind whipping her coat."},
        {"at": 3.0, "range": "03s-07s", "framing": "close-up", "action": "Her hand closes around a brass key in her pocket; her jaw tightens."},
        {"at": 7.0, "range": "07s-10s", "framing": "tight close-up", "action": "Headlights sweep across her eyes; she turns toward the road."}
      ],
      "dialogue": [
        {"speaker": "NORA", "line": "They said the lighthouse was empty for ten years. So who left the light on?", "delivery": "cold, quiet"}
      ],
      "sfx_ambience": "wind, distant surf, a gull, wet gravel underfoot",
      "continuity": "Act 1 wardrobe. She is holding the brass key; salt wind, wet gravel, cold hands. Present state only."
    }
  ],
  "teasers": [
    {"id": 1, "title": "Official Teaser", "hook_text": "THE LIGHT WAS NEVER OFF", "scenes": [1, 2, 3, 4, 5, 6], "caption": "2-4 short lines, one question, honest CTA."}
  ],
  "publisher": {
    "personaje_id": "$personaje",
    "cta": "Follow for Episode 2.",
    "hashtags": ["#shortdrama", "#novel", "#storytime", "#drama", "#episode1"],
    "ai_disclosure": true
  },
  "soundtrack": {"mood": "tense coastal romantic suspense", "bpm": 78, "notes": "Dialogue forward; music mixed in post."}
}"""
    schema = Template(schema).safe_substitute(
        slug=slug, title=title or "Untitled Episode", episode_number=episode_number, personaje=personaje
    )

    context_block = ""
    if context_text.strip():
        context_block = (
            "\n## PREVIOUS PART / CONTINUITY CONTEXT\n\n"
            "Use this to keep faces, names, wardrobe, props and unresolved questions consistent. "
            "Do not copy its scenes; continue the story.\n\n```text\n"
            + context_text.strip()[:20000]
            + "\n```\n"
        )

    return f"""# SHORT-DRAMA SHOWRUNNER TASK — {title or slug} (Episode {episode_number})

You are a senior US short-drama showrunner and screenwriter. You write cinematic,
vertically-shot soap suspense for an English-speaking US audience. Your scripts
are performed by AI characters with native audio, one 10-second clip per scene.

## OBJECTIVE

Write the complete episode as ONE valid JSON object that follows the schema below.
{part_rule}

## SOURCE BRIEF

{brief_md}

{context_block}
## FORMAT (NON-NEGOTIABLE)

{_retention_block(rules)}

## ACT MAP

{_acts_block(rules)}

## VIRAL STRUCTURE CATALOG (LATAM -> USA)

{_viral_latam_block(rules)}

{_selected_viral_template_block(rules, viral_template)}

## FIRST-FRAME / VISUAL RULES

- Step 0 (once per episode): fill "visual_reference" for every main character. generators/02 exports chatgpt_reference_sheets.txt so the user can create one reference sheet per character BEFORE the frames and keep all of them attached in the same ChatGPT thread.
- One still per scene, 16:9, cinematic, photoreal. It must be the literal first frame of the clip.
- Open every prompt with the character name and the reference file: e.g. "Cinematic still of Nora Hale (the character in reference_nora.png), ...". Use the character's own id in the filename (lowercase, underscores).
- Identity comes from the attached reference images and the reference file. NEVER write age, eye color, skin tone or base hair color in the prompt. Describe only transient state: moment hairstyle, wet hair, flush, sweat, expression, gaze, wardrobe, pose, light, framing.
- Close the prompt with a one-line binding: "Keep <Name>'s face and wardrobe identical to reference_<id>.png."
- Include framing, location, time of day, wardrobe, expression and one telling environmental detail.
- Center-weight the subject so a 9:16 crop still works. Keep the face unobstructed.
- 45-80 words per prompt. Do NOT include the global style suffix or negative prompt; they are appended automatically.
- No text, letters, logos, watermarks or captions inside the image.
- Global look (for your reference, not to repeat verbatim): {visual.get('look', '')}
- Allowed lighting: {'; '.join(visual.get('lighting') or [])}
- Camera vocabulary: {'; '.join(visual.get('camera_language') or [])}

## AUDIO / VOICE RULES

- Native US English only. Conversational pace (~2.5 words/second).
- 6-15 words of dialogue TOTAL per scene across all speakers (hard cap 15). 1-2 lines, max 15 words each. Finish before 8.5 s. Silence is allowed but rare.
- Every "speaker" MUST be the exact name of a character declared in "characters[].name". Never invent speakers (no CLERK, no NARRATOR, no unnamed roles).
- Subtext over exposition. Concrete nouns. No therapy-speak, no lectures, no villain monologues.
- The clip contains dialogue + diegetic ambience only. NO music, NO narrator, NO subtitles.
- Voice archetypes you may reference: {json.dumps(voice.get('character_voice_archetypes') or {}, ensure_ascii=False)}
- Delivery format: {voice.get('dialogue_line_template', '{speaker} ({delivery}): "{line}"')}

## CONTINUITY

{json.dumps((rules.get('continuity_rules') or {}), ensure_ascii=False, indent=2)}

- Write "continuity" in PRESENT tense only: current wardrobe, current props, current state of mind or body. NO spoilers.
- NEVER mention a future scene, act or event (no "returns in scene 40", "pays off later", "is revealed in act 5", "it is planted now"). The clip for this scene must not hint at scenes the viewer has not seen.

## TEASERS

{teaser_rule}
Each teaser is exactly 6 consecutive scenes (60 s), a 5-10 word hook_text (one CAPS word allowed),
and a caption of 2-4 short lines with one question and an honest CTA (follow/save/comment).
Do not promise DMs, downloads or links that do not exist.

## JSON SCHEMA (fields are mandatory unless marked optional)

```json
{schema}
```

Rules for the JSON:
- "scenes" must contain exactly the scene range requested for this part, in order, with all required fields.
- "internal_cuts": exactly 3 items at 0.0, 3.0 and 7.0 s with ranges 00s-03s, 03s-07s and 07s-10s. Shot 1 starts in motion from the exact storyboard panel; Shot 2 is close-up/OTS dialogue/action; Shot 3 is tight close-up/reaction/insert.
- "internal_cuts[].action" is VISUAL ONLY (no dialogue in it). "dialogue" is separate.
- Shot 1 (at 0.0) defines the storyboard panel: its framing and action MUST describe the literal first frame, already in motion, with the location, key object and every character present matching "first_frame_prompt".
- "teasers[].scenes" must reference real scene_id values from this episode and be consecutive.
- Keep the cast to 3-5 characters and 3-5 primary locations. Every scene "location" must reuse one of the declared locations (same wording), never a brand-new place. Group 3-6 consecutive scenes per location block whenever the story allows it.
- Causal order: never show a consequence before its cause, never reveal the same clue twice, and never jump location without a transition.
- Every dialogue "speaker" and every entry in scene "characters" must match a character declared in "characters[].name".
- Scene 1 must open with a question or contradiction, not a slow establishing montage.
- Scenes 10, 20, 30, 40 and 50 must end on a cliffhanger. Scene 59 pays off. Scene 60 opens the next episode.
- No real celebrities, brands, explicit content, graphic violence, hate or medical/legal claims.

## OUTPUT

Return ONLY the JSON object. No Markdown fence, no commentary, no explanations.
If you cannot fit the whole part, stop at the last complete scene and say nothing else.
"""


# ---------------------------------------------------------------------------
# Episodio de calibración (sin LLM) — fixture de pipeline, no guion final
# ---------------------------------------------------------------------------
DEMO_ACTS: List[Dict[str, Any]] = [
    {
        "act": 1,
        "title": "The Bait",
        "locations": [
            ("Hale lighthouse cliff edge", "storm dusk, wind and salt spray"),
            ("Keller harbor boardwalk", "blue hour, wet planks and dock lights"),
            ("Hale lighthouse kitchen", "night, one warm lamp and a cold stove"),
        ],
        "wardrobe": "charcoal wool coat over a dark sweater, dark jeans, rain-wet hair",
        "props": ["a brass key", "the deed", "fresh survey stakes", "the dead lighthouse lamp"],
        "actions": [
            "Nora stands at the cliff edge, the lighthouse dark behind her, salt wind whipping her coat.",
            "Nora steps off the ferry with one duffel bag, the town sign behind her.",
            "Sam leans against a harbor truck with his arms crossed, trying not to smile.",
            "Nora sets a brass key on the lighthouse kitchen table between them.",
            "Sam points through the rain at fresh survey stakes driven into the cliff.",
            "Margaret waits under the dry awning of the Keller estate, gloves folded.",
            "Nora reads the deed by a single warm lamp, jaw tight.",
            "Adrian blocks the lighthouse door with a folder under his arm.",
            "Nora stands alone on the point, the town lights small below her.",
            "Nora crouches at the lighthouse base, finding a keyhole hidden under peeling paint.",
        ],
        "sfx": "wind, distant surf, a gull, wet gravel underfoot",
        "lines": [
            [("NORA", "They said the lighthouse was empty for ten years. So who left the light on?", "cold, quiet")],
            [("SAM", "Nora Hale. Ten years, and you still drive like the road owes you money.", "dry, warm")],
            [("NORA", "I inherited a lighthouse, Sam. Not a welcome party.", "guarded"),
             ("SAM", "I'm not happy. I'm careful.", "low")],
            [("SAM", "The Kellers already had surveyors on your land. Twice.", "flat"),
             ("NORA", "Then they can explain it to the state. The trust is mine now.", "steady")],
            [("MARGARET", "Your father was a liar, dear. Sentiment won't change what the deed says.", "silk over steel"),
             ("NORA", "Then you won't mind me reading the deed. Slowly.", "quiet")],
            [("ADRIAN", "Sell us the point. Name your price and leave.", "reasonable, rehearsed"),
             ("NORA", "The past is the only thing you've asked me to leave behind.", "cold")],
            [("NORA", "You had ten years to buy this land. Why wait until I came back?", "suspicious"),
             ("MARGARET", "Because a deed is cleaner than a funeral.", "pleasant")],
            [("CLAIRE", "Your father changed his will three days before he died. That's not nothing.", "careful"),
             ("NORA", "Who witnessed it?", "sharp")],
            [("CLAIRE", "Margaret Keller's attorney. And a man named Sam.", "quiet"),
             ("NORA", "Sam was there that night? At the lighthouse?", "low")],
            [("NORA", "Dad... what did you lock in the lighthouse?", "hushed"),
             ("NORA", "And why did you leave me the key?", "breaking")],
        ],
    },
    {
        "act": 2,
        "title": "The Trap",
        "locations": [
            ("Claire Boone's law office", "grey morning, rain on the windows"),
            ("Keller boathouse", "night, one hanging bulb and a flashlight"),
            ("Keller estate", "dusk, warm interior against blue windows"),
        ],
        "wardrobe": "charcoal wool coat, dark jeans, hair dry now, no umbrella",
        "props": ["the sealed petition", "a witness signature", "a scorched beam", "the survey map"],
        "actions": [
            "Claire slides a sealed envelope across the lawyer's desk.",
            "Nora reads the witness signature and looks up slowly.",
            "Sam stands in the boathouse doorway, rain behind him.",
            "Nora sweeps a flashlight over scorched beams.",
            "Margaret pours tea without offering a cup.",
            "Nora stands in the town hall doorway as every head turns.",
            "Adrian corners Nora by the harbor railing.",
            "Nora stares at a survey map pinned to the boathouse wall.",
            "Sam watches Nora from across the dock, unable to speak.",
            "Adrian holds the lighthouse door open, waiting.",
        ],
        "sfx": "rain on windows, a ticking clock, tea poured, a door closing",
        "lines": [
            [("CLAIRE", "The petition says you're unfit to manage the trust. They want a guardian by Friday.", "clinical"),
             ("NORA", "On what grounds?", "flat")],
            [("NORA", "Who signed the statement?", "sharp"),
             ("CLAIRE", "Half the harbor. And one name you won't like: Sam.", "quiet"),
             ("NORA", "Of course.", "bitter")],
            [("SAM", "I signed a paper. I didn't read it. I was twenty-two and scared.", "ashamed"),
             ("NORA", "Scared of what? Of being poor? Of her?", "cutting")],
            [("SAM", "The fire started in the boathouse, Nora. Not the cliffs.", "low"),
             ("NORA", "Then why did the whole town say it was me?", "raw")],
            [("MARGARET", "Reopen that investigation and the town remembers who lit the match.", "pleasant threat"),
             ("NORA", "I've played the villain in your story for ten years.", "tired")],
            [("NORA", "A debt doesn't transfer with land, Adrian. But fraud does.", "precise"),
             ("ADRIAN", "Big words for someone with no lawyer.", "smiling")],
            [("SAM", "The old survey files are in the boathouse. What's left of them.", "urgent"),
             ("NORA", "Then we go tonight, before the hearing.", "decided")],
            [("SAM", "You always did like a bad idea with good lighting.", "dry"),
             ("NORA", "You coming or not? Bring the pry bar.", "impatient")],
            [("NORA", "There. Seawall permits. Signed by Margaret. Dated before the fire.", "shaking"),
             ("SAM", "That's not a permit. That's a motive.", "quiet")],
            [("ADRIAN", "Give me the file and I'll call the fire an accident.", "reasonable"),
             ("NORA", "In exchange?", "wary"),
             ("ADRIAN", "I'll say you were with me. Everything goes away.", "soft")],
        ],
    },
    {
        "act": 3,
        "title": "The First Crack",
        "locations": [
            ("Keller boathouse", "night, flashlight and dust"),
            ("Hale lighthouse archive room", "night, a single desk lamp"),
            ("Harbor diner", "dawn, cold fluorescent light and steam"),
        ],
        "wardrobe": "cream knit sweater under the charcoal coat, hair loose",
        "props": ["the metal evidence box", "the seawall permit", "a folded page", "a diner coffee cup"],
        "actions": [
            "Nora spreads water-stained survey files across the lighthouse floor.",
            "Sam jimmies the boathouse lock with a pry bar.",
            "Nora's flashlight beam catches a metal box under the floorboards.",
            "Sam watches Nora read the permits, his face falling.",
            "Nora holds a permit signed by Margaret, dated before the fire.",
            "Nora and Sam stand close in the archive, the file between them.",
            "Adrian waits in a diner booth across from Nora.",
            "Nora slides the file across the table, keeping one page back.",
            "Adrian leans in, his hand covering hers.",
            "Nora stands alone in the lamp room, the file in her hands.",
        ],
        "sfx": "flashlight click, floorboards, rain on a tin roof, a paper unfolding",
        "lines": [
            [("ADRIAN", "You'd rather be the arsonist than my alibi?", "incredulous"),
             ("NORA", "I'd rather be alone than owned. Now move.", "flat")],
            [("MARGARET", "The trust is frozen. Emergency petition. Effective this morning.", "satisfied"),
             ("NORA", "On what grounds?", "steady"),
             ("CLAIRE", "Mental incompetence. They have statements.", "ashamed")],
            [("CLAIRE", "One of the statements is from Sam.", "gentle"),
             ("NORA", "Sam... tell me that's a lie. Tell me to my face.", "low")],
            [("SAM", "They threatened my sister's job. I'm sorry.", "broken"),
             ("NORA", "Everyone keeps apologizing while they take everything.", "bitter"),
             ("NORA", "Don't apologize. Fix it.", "hard")],
            [("ADRIAN", "Sign the sale. I'll make the petition disappear.", "reasonable"),
             ("NORA", "And if I don't?", "quiet"),
             ("ADRIAN", "Then I own your father's name.", "soft")],
            [("NORA", "Lighthouses keep logs. Every ship, every storm, every night.", "realizing"),
             ("SAM", "Your father logged the harbor for thirty years.", "nodding")],
            [("NORA", "Including the night of the fire. And the boat that left at two a.m.", "urgent"),
             ("SAM", "That's the Keller launch.", "cold")],
            [("NORA", "No. That's Margaret's launch. With Adrian at the helm.", "quiet"),
             ("SAM", "Nora. Are you sure?", "careful"),
             ("NORA", "I've never been surer of anything.", "steady")],
            [("ADRIAN", "You think a notebook beats a town full of witnesses?", "amused"),
             ("NORA", "I think a notebook beats you. And you know it.", "calm")],
            [("MARGARET", "Name your price, Nora. One last time.", "tired"),
             ("NORA", "The hearing. Tomorrow. Public. All of it.", "final"),
             ("MARGARET", "Then you'll lose your only home.", "quiet")],
        ],
    },
    {
        "act": 4,
        "title": "The Dark Night",
        "locations": [
            ("Town hall hearing room", "grey morning, rain streaking the windows"),
            ("Hale lighthouse", "storm night, lightning through the glass"),
            ("Hale lighthouse kitchen", "night, one lamp, rain outside"),
        ],
        "scene_locations": [
            ("Town hall hearing room", "grey morning, rain streaking the windows"),
            ("Town hall hearing room", "grey morning, rain streaking the windows"),
            ("Town hall hearing room", "grey morning, rain streaking the windows"),
            ("Town hall hearing room", "grey morning, rain streaking the windows"),
            ("Town hall hearing room", "grey morning, rain streaking the windows"),
            ("Town hall hearing room", "grey morning, rain streaking the windows"),
            ("Hale lighthouse", "storm night, lightning through the glass"),
            ("Hale lighthouse kitchen", "night, one lamp, rain outside"),
            ("Hale lighthouse", "storm night, lightning through the glass"),
            ("Hale lighthouse", "storm night, lightning through the glass"),
        ],
        "wardrobe": "storm-soaked shirt and trousers, no coat, hair plastered down",
        "props": [
            "the emergency petition", "the emergency petition", "a statement form",
            "a statement form", "the petition ruling", "the petition ruling",
            "the eviction notice", "the sale papers", "the cold lamp", "the harbor logbook",
        ],
        "actions": [
            "Rain hammers the town hall windows as Nora faces the panel.",
            "The hearing room is packed; Claire leans close to Nora.",
            "Sam catches Nora in the hearing room before she takes her seat.",
            "Sam stands before the panel; Margaret watches from the front row.",
            "Nora faces Adrian across the hearing room.",
            "The clerk stamps the petition; the room goes silent.",
            "At the lighthouse door, Margaret holds out the eviction notice.",
            "Adrian waits in the lighthouse kitchen with the sale papers.",
            "Nora stands alone in the dark lighthouse, the cold lens above her.",
            "Nora finds an old harbor logbook behind the lens housing.",
        ],
        "sfx": "storm wind, rain on glass, a gavel, a chair scraping",
        "lines": [
            [("NORA", "I'd rather lose the house than let you keep my father's name.", "steady"),
             ("MARGARET", "You already lost it ten years ago.", "soft")],
            [("CLAIRE", "The hearing is packed. Half the town came.", "nervous"),
             ("NORA", "Good. This time, I want witnesses.", "resolved")],
            [("SAM", "Nora. Whatever happens in there, I should have told you the truth.", "low"),
             ("NORA", "Then tell it now. Loud enough for the back row.", "fierce")],
            [("SAM", "I signed a false statement. Margaret Keller wrote it. I was paid to stay quiet.", "public, shaking"),
             ("MARGARET", "He's a firefighter with a grudge.", "dismissive")],
            [("NORA", "Then let's hear from someone who can't be bought.", "calm"),
             ("ADRIAN", "You're bluffing.", "uneasy"),
             ("NORA", "I don't bluff. I document.", "flat")],
            [("NORA", "The harbor log. 2:14 a.m. Keller launch. Adrian at the helm.", "precise"),
             ("MARGARET", "That log is thirty years of weather and guesswork.", "sharp")],
            [("NORA", "2:14 a.m. One passenger, Margaret.", "quiet"),
             ("ADRIAN", "An accident. We meant to scare him.", "breaking"),
             ("NORA", "You let a town bury my father.", "raw")],
            [("NORA", "You didn't scare him. You killed the only man who could prove it.", "cold"),
             ("ADRIAN", "He was already dead when we got there.", "whisper")],
            [("NORA", "Then who was in the boathouse with him that night?", "sharp"),
             ("ADRIAN", "Ask your mother where she's been.", "quiet")],
            [("NORA", "The harbor log. Every boat, every night. Dad, what did you see?", "hushed"),
             ("NORA", "And why did you hide it behind the lens?", "breaking")],
        ],
    },
    {
        "act": 5,
        "title": "The Turn",
        "locations": [
            ("Hale lighthouse archive room", "dawn, cold blue light"),
            ("Harbor pier", "morning, flat silver water"),
            ("Town hall steps", "dusk, wet stone"),
        ],
        "wardrobe": "dark blazer over a black shirt, hair tied back",
        "props": ["the harbor log", "a torn page", "a timestamp", "the town hall steps"],
        "actions": [
            "Nora opens the logbook on the lighthouse table, pages brittle.",
            "Nora and Sam compare timestamps under a desk lamp.",
            "Nora traces a line in the log with her finger.",
            "Sam reads over her shoulder, close enough to touch.",
            "Nora looks up at Sam, a decision forming.",
            "Adrian stands on the town hall steps, trying to smile.",
            "Nora walks past him without stopping.",
            "Margaret waits in the hall, gloves in hand.",
            "Nora faces Margaret on the empty hearing floor.",
            "Nora stands at the lighthouse door as the town lights come on.",
        ],
        "sfx": "pages turning, a desk lamp humming, gulls outside, footsteps on wet stone",
        "lines": [
            [("NORA", "Every keeper signs the log. Date, time, weather. No exceptions.", "focused"),
             ("SAM", "Your father never missed a night.", "quiet"),
             ("NORA", "Then neither will I.", "steady")],
            [("SAM", "The page from that night is torn out.", "grim"),
             ("NORA", "No. It's not torn. It's folded. He hid it behind the lens.", "triumphant whisper")],
            [("NORA", "2:14 a.m. Keller launch. Two passengers, not one.", "urgent"),
             ("SAM", "Who's the second?", "low"),
             ("NORA", "Someone who signed as a witness.", "cold")],
            [("SAM", "Your mother's name.", "stunned"),
             ("NORA", "She died when I was eleven. I watched them bury her.", "flat"),
             ("SAM", "Then who's been paying the lighthouse taxes?", "quiet")],
            [("NORA", "Every year. In cash. Under my mother's maiden name.", "shaking"),
             ("SAM", "Nora, look at me. We can still stop this.", "gentle")],
            [("ADRIAN", "The hearing is tomorrow. You have one night to change your mind.", "reasonable"),
             ("NORA", "I've had ten years. I'm not changing anything.", "calm")],
            [("MARGARET", "You've made your point. Name a number.", "controlled"),
             ("NORA", "The number is zero. You leave with nothing. That's the price.", "final")],
            [("CLAIRE", "If you present that log, the town turns on your mother.", "worried"),
             ("NORA", "Then they'll finally tell the truth about her.", "steady")],
            [("NORA", "Whatever they say about me tomorrow, I want you to hear it from me first.", "vulnerable"),
             ("SAM", "I'm not going anywhere.", "low")],
            [("MARGARET", "You'll lose the only home you have left.", "cold"),
             ("NORA", "I'm not doing this for the house. I'm doing it for his name.", "fierce")],
        ],
    },
    {
        "act": 6,
        "title": "The Payoff",
        "locations": [
            ("Town hall hearing room", "day, hard window light"),
            ("Hale lighthouse point", "golden hour, wind down"),
            ("Harbor", "golden hour, calm water"),
        ],
        "wardrobe": "dark blazer, hair down, salt wind in it",
        "props": ["the harbor log", "the clerk's desk", "a second ledger", "Sam's hand"],
        "actions": [
            "The hearing room fills; Nora stands alone at the table.",
            "Sam steps to the microphone, the room silent.",
            "Margaret's smile falters for the first time.",
            "Nora holds up the harbor log, open to the page.",
            "Adrian half-rises from his chair.",
            "Nora sets the log on the clerk's desk.",
            "Margaret reaches for the log; Nora slides it away.",
            "Sam takes Nora's hand under the table.",
            "Nora walks out of the town hall into the light.",
            "Nora and Sam stand on the lighthouse point at dusk, an older ledger in Nora's hands.",
        ],
        "sfx": "a crowded room holding its breath, paper on wood, wind off the water",
        "lines": [
            [("CLAIRE", "They're calling it an emergency hearing. Every seat is full.", "nervous"),
             ("NORA", "Good. Let them watch. Let them remember.", "resolved")],
            [("SAM", "If I do this, I lose the department. I'm still doing it.", "steady"),
             ("NORA", "Then do it for the right reason.", "gentle")],
            [("NORA", "You don't have to prove anything to me. Just tell them the truth.", "quiet"),
             ("SAM", "The truth is I let them bury your father.", "breaking")],
            [("SAM", "I signed a false statement. Margaret wrote it and paid me to stay quiet.", "public, clear"),
             ("MARGARET", "He's a firefighter with a grudge. Nothing more.", "dismissive")],
            [("NORA", "Then let's hear from someone who can't be bought. The harbor log.", "calm"),
             ("ADRIAN", "That's a piece of paper.", "uneasy")],
            [("NORA", "2:14 a.m. Keller launch. Two passengers. Adrian at the helm.", "precise"),
             ("MARGARET", "That log is thirty years of weather and guesswork.", "sharp")],
            [("NORA", "One passenger is Margaret. The other signed the fire report.", "quiet"),
             ("CLAIRE", "The fire marshal. It's his signature.", "stunned")],
            [("ADRIAN", "It was an accident. We only meant to scare him.", "breaking"),
             ("NORA", "You burned a boathouse and let a town bury my father.", "raw")],
            [("NORA", "That's not an accident. That's a choice. And this town gets to see it.", "fierce"),
             ("MARGARET", "You'll regret this.", "quiet")],
            [("NORA", "Wait. This ledger is older. My mother's name is on every page.", "hushed"),
             ("SAM", "Nora... she's alive?", "stunned"),
             ("NORA", "She's been here the whole time.", "cold")],
        ],
    },
]

DEMO_DIALOGUES: List[List[Tuple[str, str, str]]] = [
    [("NORA", "They said the lighthouse was empty for ten years. So who left the light on?", "cold, quiet")],
    [("SAM", "Nora Hale. Ten years, and you still drive like a storm.", "dry, warm")],
    [("NORA", "I inherited a lighthouse, Sam. Not a welcome party.", "guarded"),
     ("SAM", "I'm not happy. I'm careful.", "low")],
    [("SAM", "The Kellers already had surveyors on your land.", "flat"),
     ("NORA", "Then explain it to the state.", "steady")],
    [("MARGARET", "Your father was a liar. The deed stands.", "silk over steel"),
     ("NORA", "Then you won't mind me reading it.", "quiet")],
    [("ADRIAN", "Sell us the point. Name your price.", "reasonable, rehearsed"),
     ("NORA", "You only ask me to leave the past.", "cold")],
    [("NORA", "Ten years. Why wait until I came back?", "suspicious"),
     ("MARGARET", "A deed is cleaner than a funeral.", "pleasant")],
    [("CLAIRE", "Your father changed his will three days before he died.", "careful"),
     ("NORA", "Who witnessed it?", "sharp")],
    [("CLAIRE", "Margaret's attorney. And a man named Sam.", "quiet"),
     ("NORA", "Sam was there that night?", "low")],
    [("NORA", "Dad, what did you lock in the lighthouse?", "hushed"),
     ("NORA", "And why leave me the key?", "breaking")],
    [("CLAIRE", "The petition calls you unfit. They want a guardian by Friday.", "clinical"),
     ("NORA", "On what grounds?", "flat")],
    [("NORA", "Who signed the statement?", "sharp"),
     ("CLAIRE", "Half the harbor. And Sam.", "quiet")],
    [("SAM", "I signed a paper. I was twenty-two and scared.", "ashamed"),
     ("NORA", "Scared of being poor? Or her?", "cutting")],
    [("SAM", "The fire started in the boathouse, not the cliffs.", "low"),
     ("NORA", "Why did the town blame me?", "raw")],
    [("MARGARET", "Reopen it, and the town remembers the match.", "pleasant threat"),
     ("NORA", "I've played your villain ten years.", "tired")],
    [("NORA", "A debt doesn't transfer with land. Fraud does.", "precise"),
     ("ADRIAN", "Big words for someone with no lawyer.", "smiling")],
    [("SAM", "The old survey files are in the boathouse.", "urgent"),
     ("NORA", "Tonight, before the hearing.", "decided")],
    [("SAM", "You always liked bad ideas with good lighting.", "dry"),
     ("NORA", "You coming? Bring the pry bar.", "impatient")],
    [("NORA", "Seawall permits. Signed by Margaret, before the fire.", "shaking"),
     ("SAM", "That's not a permit. That's a motive.", "quiet")],
    [("ADRIAN", "Give me the file. I'll call the fire an accident.", "reasonable"),
     ("NORA", "In exchange for what?", "wary")],
    [("ADRIAN", "You'd rather be the arsonist than my alibi?", "incredulous"),
     ("NORA", "I'd rather be alone than owned. Move.", "flat")],
    [("MARGARET", "The trust is frozen. Emergency petition, effective this morning.", "satisfied"),
     ("NORA", "On what grounds?", "steady")],
    [("CLAIRE", "One of the statements is from Sam.", "gentle"),
     ("NORA", "Tell me that's a lie. To my face.", "low")],
    [("SAM", "They threatened my sister's job. I'm sorry.", "broken"),
     ("NORA", "Don't apologize. Fix it.", "hard")],
    [("ADRIAN", "Sign the sale. I'll make the petition disappear.", "reasonable"),
     ("NORA", "And if I don't?", "quiet")],
    [("NORA", "Lighthouses keep logs. Every ship, every storm.", "realizing"),
     ("SAM", "Your father logged the harbor for thirty years.", "nodding")],
    [("NORA", "Including the night of the fire. And the boat at two.", "urgent"),
     ("SAM", "That's the Keller launch.", "cold")],
    [("NORA", "No. Margaret's launch. Adrian at the helm.", "quiet"),
     ("SAM", "Nora, are you sure?", "careful")],
    [("ADRIAN", "A notebook beats a town of witnesses?", "amused"),
     ("NORA", "It beats you. You know it.", "calm")],
    [("MARGARET", "Name your price, Nora. One last time.", "tired"),
     ("NORA", "The hearing. Tomorrow. Public. All of it.", "final")],
    [("NORA", "I'd rather lose the house than his name.", "steady"),
     ("MARGARET", "You lost it ten years ago.", "soft")],
    [("CLAIRE", "The hearing is packed. Half the town came.", "nervous"),
     ("NORA", "Good. This time, I want witnesses.", "resolved")],
    [("SAM", "I should have told you ten years ago.", "low"),
     ("NORA", "Tell it now. Loud enough for everyone.", "fierce")],
    [("SAM", "I signed a false statement. Margaret wrote it.", "public, shaking"),
     ("MARGARET", "He's a firefighter with a grudge.", "dismissive")],
    [("NORA", "Then hear someone who can't be bought.", "calm"),
     ("ADRIAN", "You're bluffing.", "uneasy"),
     ("NORA", "I document.", "flat")],
    [("MARGARET", "The petition is granted. The trust is frozen.", "controlled"),
     ("NORA", "On mental incompetence? That's a lie.", "raw")],
    [("MARGARET", "You have until midnight to leave the lighthouse.", "cold"),
     ("NORA", "She bought the county. Not me.", "flat")],
    [("ADRIAN", "Sign the sale. I'll make the eviction disappear.", "reasonable"),
     ("NORA", "And if I don't?", "quiet")],
    [("NORA", "He left me a key. There has to be something.", "hushed")],
    [("NORA", "The harbor log. Every boat, every night.", "precise"),
     ("NORA", "Dad, what did you see?", "breaking")],
    [("NORA", "Every keeper signs the log. Date, time, weather.", "focused"),
     ("SAM", "Your father never missed a night.", "quiet")],
    [("SAM", "The page is torn out.", "grim"),
     ("NORA", "No. Folded. He hid it behind the lens.", "triumphant whisper")],
    [("NORA", "2:14 a.m. Keller launch. Two passengers, not one.", "urgent"),
     ("SAM", "Who's the second?", "low")],
    [("SAM", "Your mother's name.", "stunned"),
     ("NORA", "She died when I was eleven. I watched them bury her.", "flat")],
    [("NORA", "Every year, in cash, under her maiden name.", "shaking"),
     ("SAM", "Nora, we can still stop this.", "gentle")],
    [("ADRIAN", "The hearing is tomorrow. Change your mind tonight.", "reasonable"),
     ("NORA", "I've had ten years. I'm not changing.", "calm")],
    [("MARGARET", "You've made your point. Name a number.", "controlled"),
     ("NORA", "Zero. You leave with nothing.", "final")],
    [("CLAIRE", "Present that log, and the town turns on your mother.", "worried"),
     ("NORA", "Then they'll tell the truth.", "steady")],
    [("NORA", "Whatever they say tomorrow, hear it from me first.", "vulnerable"),
     ("SAM", "I'm not going anywhere.", "low")],
    [("MARGARET", "You'll lose the only home you have left.", "cold"),
     ("NORA", "Not for the house. For his name.", "fierce")],
    [("CLAIRE", "Emergency hearing. Every seat is full.", "nervous"),
     ("NORA", "Good. Let them watch. Let them remember.", "resolved")],
    [("SAM", "If I do this, I lose the department.", "steady"),
     ("NORA", "Then do it for the right reason.", "gentle")],
    [("NORA", "Just tell them the truth.", "quiet"),
     ("SAM", "The truth is I let them bury your father.", "breaking")],
    [("SAM", "I signed a false statement. Margaret paid me.", "public, clear"),
     ("MARGARET", "He's a firefighter with a grudge.", "dismissive")],
    [("NORA", "Then hear someone who can't be bought. The log.", "calm"),
     ("ADRIAN", "That's a piece of paper.", "uneasy")],
    [("NORA", "2:14. Keller launch. Two aboard. Adrian steering.", "precise"),
     ("MARGARET", "That log is weather and guesswork.", "sharp")],
    [("NORA", "Margaret. And the man who signed the fire report.", "quiet"),
     ("CLAIRE", "The fire marshal.", "stunned")],
    [("ADRIAN", "An accident. We meant to scare him.", "breaking"),
     ("NORA", "You burned it and buried my father.", "raw")],
    [("NORA", "That's not an accident. That's a choice.", "fierce"),
     ("MARGARET", "You'll regret this.", "quiet")],
    [("NORA", "Wait. This ledger is older. Her name is on every page.", "hushed"),
     ("SAM", "Nora... she's alive?", "stunned")],
]

DEMO_CHARACTERS = [
    {"id": "nora", "name": "Nora Hale", "role": "protagonist", "archetype": "protagonist",
     "pronoun": "she", "voice_lock": "warm mid-range American English, controlled, slightly breathy under pressure",
     "identity_anchor": "early thirties coastal New England woman, dark auburn hair worn loose, storm-grey eyes, fair weathered skin",
     "visual_reference": "early thirties coastal New England woman, wiry build, dark auburn hair worn loose, storm-grey eyes, fair weathered skin, charcoal wool coat over a dark sweater"},
    {"id": "sam", "name": "Sam Calloway", "role": "love_interest", "archetype": "love_interest",
     "pronoun": "he", "voice_lock": "quiet, low American English, careful diction, warmth under restraint",
     "identity_anchor": "mid-thirties harbor firefighter, broad-shouldered, short dark-sand hair, hazel eyes, tanned skin",
     "wardrobe_lock": "faded canvas work jacket, dark trousers, worn boots",
     "visual_reference": "mid-thirties harbor firefighter, broad-shouldered, short dark-sand hair, hazel eyes, tanned skin with salt creases, faded canvas work jacket"},
    {"id": "margaret", "name": "Margaret Keller", "role": "antagonist", "archetype": "antagonist",
     "pronoun": "she", "voice_lock": "low, polished, unhurried American English, never shouts",
     "identity_anchor": "late sixties matriarch, tall and straight-backed, silver chignon, pale blue eyes, porcelain skin",
     "wardrobe_lock": "tailored dove-grey suit, pearls, low-heeled shoes",
     "visual_reference": "late sixties matriarch, tall and straight-backed, silver hair in a low chignon, pale blue eyes, porcelain skin, tailored dove-grey suit and pearls"},
    {"id": "adrian", "name": "Adrian Keller", "role": "antagonist_heir", "archetype": "antagonist",
     "pronoun": "he", "voice_lock": "smooth mid-range American English, reasonable tone that never quite reaches sincerity",
     "identity_anchor": "late thirties lean groomed heir, ash-blond hair swept back, cold grey eyes, even features",
     "wardrobe_lock": "navy blazer, open-collared white shirt, dark trousers",
     "visual_reference": "late thirties heir, lean and groomed, ash-blond hair swept back, cold grey eyes, even features, navy blazer over an open collar"},
    {"id": "claire", "name": "Claire Boone", "role": "ally", "archetype": "ally",
     "pronoun": "she", "voice_lock": "grounded, plainspoken American English with a slight coastal New England softness",
     "identity_anchor": "forties compact small-town lawyer, brown blunt bob, warm brown eyes, reading glasses on a cord",
     "wardrobe_lock": "forest-green cardigan, cream blouse, dark trousers",
     "visual_reference": "forties small-town lawyer, compact and practical, brown hair in a blunt bob, warm brown eyes, reading glasses on a cord, forest-green cardigan"},
]

DEMO_EXPRESSIONS = [
    "jaw set, eyes bright with contained anger",
    "guarded, a half-smile that never reaches the eyes",
    "tired but alert, watching the room",
    "quiet grief held behind the eyes",
    "defiant, chin lifted",
    "afraid and refusing to show it",
    "cold, clinical calm",
    "warmth breaking through fatigue",
    "focused like a lawyer about to object",
    "relief and dread at the same time",
]

DEMO_HOOKS = {
    1: "THE LIGHT WAS NEVER OFF",
    10: "THE KEY DOESN'T OPEN THE DOOR",
    20: "THEY BOUGHT HIS SILENCE",
    30: "NAME THE PRICE",
    40: "HER MOTHER'S NAME IS IN THE LOG",
    50: "ONE NIGHT TO CHANGE HER MIND",
    60: "SHE'S BEEN HERE THE WHOLE TIME",
}


def build_demo_payload(slug: str, title: str, personaje: str, episode_number: int) -> Dict[str, Any]:
    style = nf.load_style_locks()
    rotation = (style.get("visual_style_lock") or {}).get("default_shot_rotation") or nf.DEFAULT_SHOT_ROTATION
    by_speaker: Dict[str, Dict[str, Any]] = {}
    for character in DEMO_CHARACTERS:
        for key in (character["name"].upper(), character["name"].split()[0].upper(), str(character["id"]).upper()):
            by_speaker.setdefault(key, character)
    scenes: List[Dict[str, Any]] = []

    for idx in range(1, nf.SCENE_COUNT + 1):
        act_idx = (idx - 1) // 10
        local = (idx - 1) % 10
        act = DEMO_ACTS[act_idx]
        explicit_locations = act.get("scene_locations") or []
        if isinstance(explicit_locations, list) and len(explicit_locations) == 10:
            loc_name, light = explicit_locations[local]
        else:
            loc_name, light = act["locations"][local % len(act["locations"])]
        lines = DEMO_DIALOGUES[idx - 1] if idx - 1 < len(DEMO_DIALOGUES) else act["lines"][local]
        primary_speaker = lines[0][0]
        character = by_speaker.get(primary_speaker.upper(), DEMO_CHARACTERS[0])
        reference = f"reference_{character['id']}.png"

        shot1 = rotation[(local + act_idx) % len(rotation)]
        shot2 = "close-up"
        if str(shot1).strip().lower() == "close-up":
            shot2 = "over-the-shoulder shot"
        shot3 = ["tight close-up", "insert shot of the evidence object"][local % 2]

        prop = act["props"][local % len(act["props"])]
        expression = DEMO_EXPRESSIONS[(idx - 1) % len(DEMO_EXPRESSIONS)]
        action = str(act["actions"][local]).strip()
        body = (
            f"Cinematic still of {character['name']} (the character in {reference}), "
            f"{shot1}, at {loc_name}, {light}. {action} "
            f"Expression: {expression}. Wardrobe: {act['wardrobe']}. "
            f"Keep {character['name']}'s face and wardrobe identical to {reference}. "
            f"Framing keeps the face unobstructed and centered for a 9:16 crop."
        )

        lead = action.split(" ", 1)[0].rstrip(".,;:!?").upper() if action else ""
        on_screen: List[str] = []
        for candidate in DEMO_CHARACTERS:
            keys = {candidate["name"].upper(), candidate["name"].split()[0].upper(), str(candidate["id"]).upper()}
            if lead in keys or any(line[0].upper() in keys for line in lines):
                if candidate["id"] not in on_screen:
                    on_screen.append(candidate["id"])
        if not on_screen:
            on_screen = [character["id"]]

        dialogue = [
            {"speaker": speaker, "line": line, "delivery": delivery}
            for speaker, line, delivery in lines
        ]

        scenes.append({
            "scene_id": idx,
            "act": act_idx + 1,
            "beat": (
                "cold_open_hook" if idx == 1 else
                "world_and_wound" if idx == 2 else
                "act_cliffhanger" if idx in (10, 20, 30, 40, 50) else
                "payoff_next_hook" if idx == 60 else
                "escalation"
            ),
            "location": f"{loc_name}, {light}",
            "time_of_day": light,
            "characters": on_screen,
            "wardrobe": act["wardrobe"],
            "on_screen_hook": DEMO_HOOKS.get(idx, ""),
            "first_frame_prompt": body,
            "internal_cuts": [
                {"at": 0.0, "framing": shot1, "action": act["actions"][local]},
                {"at": 3.0, "framing": shot2, "action": f"Close detail on {prop}; the room falls quiet around it."},
                {"at": 7.0, "framing": shot3, "action": f"{character['name']} reacts as the line lands, no static hold."},
            ],
            "dialogue": dialogue,
            "sfx_ambience": act["sfx"],
            "continuity": f"Act {act_idx + 1} wardrobe: {act['wardrobe']}. Evidence object in play: {prop}.",
        })

    teasers = [
        {"id": 1, "title": "Official Teaser", "hook_text": "THE LIGHT WAS NEVER OFF",
         "scenes": [1, 2, 3, 4, 5, 6],
         "caption": "She came back for a lighthouse.\n\nShe found a debt written in blood.\n\nEpisode 1 is live.\n\nFollow for the next chapter."},
        {"id": 2, "title": "The Proof", "hook_text": "THE PROOF WAS UNDER THE FLOOR",
         "scenes": [21, 22, 23, 24, 25, 26],
         "caption": "Everyone swore the fire was her fault.\n\nThe permits say otherwise.\n\nFollow for Episode 2."},
        {"id": 3, "title": "The Cliffhanger", "hook_text": "NAME THE PRICE. THEN LOSE EVERYTHING.",
         "scenes": [55, 56, 57, 58, 59, 60],
         "caption": "The town came to watch her fail.\n\nShe came to read the log.\n\nFollow for the finale."},
    ]

    location_bases: List[str] = []
    for scene in scenes:
        base = str(scene.get("location") or "").split(",")[0].strip()
        if base and base not in location_bases:
            location_bases.append(base)
    location_visuals = {
        "Hale lighthouse cliff edge": "whitewashed stone tower on a black cliff, salt-eaten wood, cold lamp",
        "Keller harbor boardwalk": "working docks, wet planks, sodium lights, a family launch named MARGARET II",
        "Hale lighthouse kitchen": "small cold kitchen, one warm lamp, chipped enamel stove",
        "Claire Boone's law office": "small-town law office, law books, rain on tall windows",
        "Keller boathouse": "dark timber boathouse, wet floor, hanging bulb, scorched beams",
        "Keller estate": "glass and cedar house above the water, warm interiors, no clutter",
        "Hale lighthouse archive room": "lighthouse archive, one desk lamp, dust and old ledgers",
        "Harbor diner": "harbor diner at dawn, cold fluorescent light, steam and vinyl booths",
        "Harbor": "working harbor, gold light on calm water",
        "Hale lighthouse point": "rocky point below the tower, wind down, gold light",
    }
    locations = [
        {
            "id": (nf.slugify(base)[:40].strip("_") or f"location_{idx + 1}"),
            "name": base,
            "visual": location_visuals.get(base, "coastal New England location, cinematic production design"),
        }
        for idx, base in enumerate(location_bases)
    ]

    return {
        "schema_version": "1.0",
        "generated_by": "novel_factory/01_story_to_master_json.py --template",
        "demo_fixture": True,
        "episode": {
            "slug": slug,
            "title": title or "The Silent Contract",
            "series_title": "Salt & Secrets",
            "episode_number": episode_number,
            "logline": "Ten years after the fire that ruined her family, Nora Hale returns to inherit a lighthouse and finds the town's most powerful family has been paying her dead mother's debts.",
            "genre": "romantic suspense short-drama",
            "language": "en-US",
            "audience": "US women 25-55, short-drama and audio-series viewers",
            "tone": "cinematic, intimate, high-stakes, fast-paced",
            "hook_line": "They said the lighthouse was empty. Someone left the light on.",
        },
        "characters": DEMO_CHARACTERS,
        "locations": locations,
        "acts": [
            {"act": a["act"], "title": a["title"],
             "goal": (nf.load_showrunner().get("acts") or [])[a["act"] - 1].get("goal", ""),
             "cliffhanger": next(iter([v for k, v in DEMO_HOOKS.items() if (k - 1) // 10 == a["act"] - 1]), "")}
            for a in DEMO_ACTS
        ],
        "scenes": scenes,
        "teasers": teasers,
        "publisher": {
            "personaje_id": personaje,
            "cta": "Follow for Episode 2.",
            "hashtags": ["#shortdrama", "#novel", "#storytime", "#suspense", "#drama", "#episode1"],
            "ai_disclosure": True,
        },
        "soundtrack": {
            "mood": "tense coastal romantic suspense",
            "bpm": 78,
            "notes": "Low strings and room tone under dialogue; no music inside the generated clips.",
        },
    }


# ---------------------------------------------------------------------------
# Ingesta / fusión de respuestas LLM
# ---------------------------------------------------------------------------
def _unwrap(payload: Any) -> Any:
    if isinstance(payload, list):
        return {"scenes": payload}
    if not isinstance(payload, dict):
        raise nf.NFError("La respuesta no es un objeto JSON.")
    for key in ("episode_json", "data", "result", "output", "master_episode"):
        inner = payload.get(key)
        if isinstance(inner, dict) and isinstance(inner.get("scenes"), list):
            return inner
    return payload


def load_payloads(paths: List[Path]) -> Tuple[List[Dict[str, Any]], List[str]]:
    payloads: List[Dict[str, Any]] = []
    warnings: List[str] = []
    for path in paths:
        if not path.exists():
            raise nf.NFError(f"No existe el archivo: {path}")
        text = path.read_text(encoding="utf-8", errors="replace")
        payload = _unwrap(nf.extract_json_blob(text))
        scenes = payload.get("scenes")
        if not isinstance(scenes, list) or not scenes:
            raise nf.NFError(f"{path.name} no contiene una lista 'scenes'.")
        payloads.append(payload)
        nf.info(f"{path.name}: {len(scenes)} escenas leídas.")
    return payloads, warnings


def merge_payloads(payloads: List[Dict[str, Any]]) -> Tuple[Dict[str, Any], List[str]]:
    """Compatibilidad: delega en el fusionador canónico de nf_core."""
    return nf.merge_payloads(payloads)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="01 — Convierte idea/transcripción en el JSON Maestro de 60 escenas.",
    )
    parser.add_argument("slug", help="Slug del episodio (carpeta en projects/).")
    parser.add_argument("--title", default="", help="Título del episodio.")
    parser.add_argument("--idea", default="", help="Premisa en 3-10 líneas.")
    parser.add_argument("--idea-file", type=str, default="", help="Archivo con la premisa.")
    parser.add_argument("--from-text", type=str, default="", help="Transcripción / material fuente.")
    parser.add_argument("--genre", default="romantic suspense short-drama")
    parser.add_argument("--episode-number", type=int, default=1)
    parser.add_argument("--personaje", default="emma_hayes",
                        help="Persona de USA WHITE para el pack de publicación (default: emma_hayes).")
    parser.add_argument("--part", default="full",
                        help="Divide el guion: full, 1of2/2of2 o 1of3/2of3/3of3 (por tandas de 20).")
    parser.add_argument("--context", type=str, default="",
                        help="Archivo de la parte anterior para continuidad (modo --part por tandas).")
    parser.add_argument("--viral-template", default="",
                        help="ID de una de las 6 estructuras LATAM->USA (config/showrunner_rules.json).")
    parser.add_argument("--brief", action="store_true", help="Genera story_brief.md + llm_prompt.md (default).")
    parser.add_argument("--template", action="store_true", help="Episodio demo de calibración, sin LLM.")
    parser.add_argument("--ingest", nargs="+", default=None, metavar="JSON",
                        help="Uno o varios JSON del LLM para validar y guardar como master_episode.json.")
    parser.add_argument("--validate", action="store_true", help="Valida un master_episode.json existente.")
    parser.add_argument("--strict", action="store_true",
                        help="Modo producción: reparto, hablantes, presupuesto de habla y continuidad pasan a error.")
    parser.add_argument("--allow-partial", action="store_true", help="Permite ingerir menos de 60 escenas.")
    parser.add_argument("--force", action="store_true", help="Sobrescribe sin preguntar (siempre deja backup).")
    args = parser.parse_args(argv)

    slug = nf.slugify(args.slug)
    nf.log("")
    nf.log("=" * 70)
    nf.log("  NOVEL FACTORY — 01 · Guion maestro de 60 escenas (10:00)")
    nf.log("=" * 70)

    if args.validate:
        paths = nf.resolve_project(args.slug)
        nf.info(f"Proyecto: {paths['root']}")
        master = nf.load_master(paths["root"])
        result = nf.validate_master(master, allow_partial=args.allow_partial, production=args.strict)
        nf.log("")
        return 0 if nf.print_validation(result) else 1

    paths = nf.create_project(slug)
    nf.info(f"Proyecto: {paths['root']}")

    if args.ingest:
        nf.log("")
        nf.info("Ingiriendo respuesta del LLM…")
        payloads, warnings = load_payloads([Path(p) for p in args.ingest])
        payload, merge_warnings = merge_payloads(payloads)
        warnings.extend(merge_warnings)
        master, norm_warnings = nf.normalize_master(
            payload, slug, args.title, repair=True, allow_partial=args.allow_partial
        )
        warnings.extend(norm_warnings)
        result = nf.validate_master(master, allow_partial=args.allow_partial, production=args.strict)
        for w in warnings:
            nf.warn(w)
        nf.log("")
        if not nf.print_validation(result):
            out = paths["root"] / "llm_response_merged.json"
            nf.write_json(out, payload)
            nf.warn(f"El JSON crudo quedó en {out} para inspección. No se escribió el maestro.")
            return 1
        if paths["master"].exists() and not args.force:
            backup = paths["root"] / "master_episode.backup.json"
            backup.write_bytes(paths["master"].read_bytes())
            nf.info(f"Backup del maestro anterior: {backup.name}")
        nf.write_json(paths["master"], master)
        nf.write_json(paths["root"] / "llm_response_merged.json", payload)
        ep = nf.episode_meta(master)
        nf.log("")
        nf.ok(f"Maestro escrito: {paths['master']}")
        nf.info(f"{ep.get('title')} · {len(master['scenes'])} escenas · {nf.human_duration(ep.get('total_seconds', 600))}")
        nf.info(f"Personaje de publicación: {master.get('publisher', {}).get('personaje_id')}")
        export_master_prompts(paths, master, _read_brief_text(paths))
        nf.log("")
        nf.log("  Siguiente: python generators/02_export_chatgpt_queue.py " + slug)
        return 0

    if args.template:
        nf.info("Generando episodio demo de calibración (sin LLM)…")
        payload = build_demo_payload(slug, args.title or "The Silent Contract", args.personaje, args.episode_number)
        master, warnings = nf.normalize_master(payload, slug, args.title, repair=True)
        result = nf.validate_master(master, production=args.strict)
        for w in warnings:
            nf.warn(w)
        if not nf.print_validation(result):
            return 1
        if paths["master"].exists() and not args.force:
            (paths["root"] / "master_episode.backup.json").write_bytes(paths["master"].read_bytes())
        nf.write_json(paths["master"], master)
        nf.write_text(
            paths["root"] / "story_brief.md",
            build_brief_markdown(slug, master["episode"]["title"], master["episode"]["logline"],
                                 "", master["episode"]["genre"], args.personaje, args.episode_number),
        )
        nf.log("")
        nf.ok(f"Episodio demo listo: {paths['master']}")
        nf.warn("Es un fixture de calibración, no un guion final. Reemplázalo con --brief + --ingest.")
        export_master_prompts(paths, master, _read_brief_text(paths))
        nf.log("")
        nf.log("  Siguiente: python generators/02_export_chatgpt_queue.py " + slug)
        return 0

    # --- Modo brief (default) ---
    idea = args.idea.strip()
    if args.idea_file:
        idea = Path(args.idea_file).read_text(encoding="utf-8", errors="replace").strip()
    source_text = ""
    if args.from_text:
        source_text = Path(args.from_text).read_text(encoding="utf-8", errors="replace").strip()
    if not idea and not source_text and not args.idea_file:
        nf.warn("No diste --idea ni --from-text: el brief quedará con un placeholder editable.")

    title = args.title or args.slug.replace("_", " ").title()
    brief = build_brief_markdown(slug, title, idea, source_text, args.genre, args.personaje, args.episode_number)
    brief_path = nf.write_text(paths["root"] / "story_brief.md", brief)

    context_text = ""
    if args.context:
        context_path = Path(args.context)
        if not context_path.exists():
            nf.err(f"No existe --context: {context_path}")
            return 2
        context_text = context_path.read_text(encoding="utf-8", errors="replace")

    prompt = build_llm_prompt(
        slug=slug,
        title=title,
        brief_md=brief,
        rules=nf.load_showrunner(),
        style=nf.load_style_locks(),
        personaje=args.personaje,
        episode_number=args.episode_number,
        part=args.part,
        context_text=context_text,
        viral_template=args.viral_template,
    )
    prompt_path = nf.write_text(paths["root"] / "llm_prompt.md", prompt)

    style = nf.load_style_locks()
    seed = (idea or source_text or title).strip()
    export_master_prompts(
        paths,
        {},
        brief,
        overrides={
            "story_idea": seed,
            "duration_minutes": 10,
            "total_scenes": 60,
            "total_grid_images": 10,
            "visual_style": mpl.visual_style_from_style(style),
            "aspect_ratio": "16:9",
        },
    )

    nf.log("")
    nf.ok(f"Brief:  {brief_path}")
    nf.ok(f"Prompt: {prompt_path}  ({len(prompt):,} caracteres)")
    nf.log("")
    plan = _part_plan(args.part)
    nf.log("  Pasos:")
    nf.log("   1. Abre llm_prompt.md, cópialo completo y pégalo en Claude / Gemini / ChatGPT.")
    nf.log("   2. Guarda la respuesta como projects/" + slug + "/llm_response.json")
    nf.log("   3. python generators/01_story_to_master_json.py " + slug + " --ingest " +
           f"projects/{slug}/llm_response.json --strict")
    if plan["label"]:
        nf.log(f"   (Tanda {plan['label']}: escenas {plan['lo']}-{plan['hi']}. Repite con la siguiente")
        nf.log("    --part y --context <json anterior>; luego ingiere TODAS juntas)")
        nf.log("    python generators/01_story_to_master_json.py " + slug +
               " --ingest parte1.json parte2.json ... --strict")
    nf.log("")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except nf.NFError as exc:
        nf.err(str(exc))
        sys.exit(1)

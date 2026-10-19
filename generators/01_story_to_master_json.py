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
sys.path.insert(0, str(NF_ROOT))
import nf_core as nf  # noqa: E402


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
    return (
        f"- Total scenes: {fmt.get('total_scenes')} x {fmt.get('scene_seconds')} s = {fmt.get('total_seconds')} s.\n"
        f"- Dialogue per scene: {fmt.get('words_per_scene_dialogue')} words TOTAL (all speakers).\n"
        f"- Internal cuts per scene: {fmt.get('internal_cuts_per_scene')}, first at 0.0 s, separated by 2.5-4 s.\n"
        f"- Open-loop types allowed: " + "; ".join(eng.get("open_loop_types") or []) + ".\n"
        f"- Dopamine cadence: {eng.get('dopamine_cadence')}\n"
        f"- Cliffhanger types allowed: " + "; ".join(eng.get("cliffhanger_types") or []) + ".\n"
        f"- Forbidden: " + "; ".join(eng.get("forbidden") or []) + "."
    )


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
) -> str:
    fmt = rules.get("format") or {}
    identity = style.get("identity_lock") or {}
    voice = style.get("voice_lock") or {}
    visual = style.get("visual_style_lock") or {}

    if part == "1":
        part_rule = (
            "PART 1 OF 2: write ONLY scenes 1-30 (Acts 1-3). scene_id must run 1..30. "
            "Do not summarize scenes 31-60. Include teasers 1 and 2 only."
        )
        teaser_rule = "Teasers: include teaser 1 (scenes 1-6) and teaser 2 (6 consecutive scenes from acts 3-4). Omit teaser 3."
    elif part == "2":
        part_rule = (
            "PART 2 OF 2: write ONLY scenes 31-60 (Acts 4-6). scene_id must run 31..60. "
            "Continue the exact same characters, wardrobe, props and locations. Include teaser 3 only."
        )
        teaser_rule = "Teasers: include teaser 3 only (6 consecutive scenes from acts 5-6). Omit teasers 1-2."
    else:
        part_rule = "Write the COMPLETE episode: all 60 scenes, Acts 1-6. Do not summarize or skip scenes."
        teaser_rule = "Teasers: include all 3 (6 consecutive scenes each, 60 s each)."

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
      "first_frame_prompt": "Cinematic still of the same woman as the reference image, wide establishing shot, at the Hale lighthouse cliff edge, storm dusk. She stands with her coat snapping in the wind, jaw set, eyes bright with contained anger. Wardrobe: charcoal wool coat over a dark sweater, dark jeans, rain-wet hair. Her face is unobstructed and centered for a 9:16 crop. 45-80 words, no style suffix (it is appended automatically), no text or logos.",
      "internal_cuts": [
        {"at": 0.0, "framing": "wide establishing shot", "action": "Nora stands at the cliff edge, the lighthouse dark behind her, salt wind whipping her coat."},
        {"at": 3.6, "framing": "tight close-up", "action": "Her hand closes around a brass key in her pocket; her jaw tightens."},
        {"at": 7.0, "framing": "over-the-shoulder shot", "action": "Headlights sweep the road below; she turns toward them."}
      ],
      "dialogue": [
        {"speaker": "NORA", "line": "They said the lighthouse was empty for ten years. So who left the light on?", "delivery": "cold, quiet"}
      ],
      "sfx_ambience": "wind, distant surf, a gull, wet gravel underfoot",
      "continuity": "Act 1 wardrobe. The brass key is introduced here and returns in scene 40."
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

## FIRST-FRAME / VISUAL RULES

- Step 0 (once per episode): fill "visual_reference" for every main character. generators/02 exports chatgpt_reference_sheets.txt so the user can create one reference sheet per character BEFORE the frames and keep all of them attached in the same ChatGPT thread.
- One still per scene, 16:9, cinematic, photoreal. It must be the literal first frame of the clip.
- Start the prompt with "Cinematic still of the same woman as the reference image" (or "the same man...").
- Identity comes from the attached reference images: NEVER write age, name, eye color, skin tone or base hair color in the prompt. Describe only transient state: moment hairstyle, wet hair, flush, sweat, expression, gaze, wardrobe, pose, light, framing.
- Include framing, location, time of day, wardrobe, expression and one telling environmental detail.
- Center-weight the subject so a 9:16 crop still works. Keep the face unobstructed.
- 45-80 words per prompt. Do NOT include the global style suffix or negative prompt; they are appended automatically.
- No text, letters, logos, watermarks or captions inside the image.
- Global look (for your reference, not to repeat verbatim): {visual.get('look', '')}
- Allowed lighting: {'; '.join(visual.get('lighting') or [])}
- Camera vocabulary: {'; '.join(visual.get('camera_language') or [])}

## AUDIO / VOICE RULES

- Native US English only. Conversational pace (~2.5 words/second).
- 18-30 words of dialogue TOTAL per scene across all speakers. 1-3 lines. Silence is allowed but rare.
- Subtext over exposition. Concrete nouns. No therapy-speak, no lectures, no villain monologues.
- The clip contains dialogue + diegetic ambience only. NO music, NO narrator, NO subtitles.
- Voice archetypes you may reference: {json.dumps(voice.get('character_voice_archetypes') or {}, ensure_ascii=False)}
- Delivery format: {voice.get('dialogue_line_template', '{speaker} ({delivery}): "{line}"')}

## CONTINUITY

{json.dumps((rules.get('continuity_rules') or {}), ensure_ascii=False, indent=2)}

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
- "internal_cuts": 2-4 items. The first "at" is 0.0. Later cuts must be 2.5-4 s apart. Each cut changes framing and/or blocking.
- "internal_cuts[].action" is VISUAL ONLY (no dialogue in it). "dialogue" is separate.
- "teasers[].scenes" must reference real scene_id values from this episode and be consecutive.
- Keep the cast to 3-5 characters and 3-4 primary locations.
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
            [("ADRIAN", "Sell us the point. Name your price and leave the past where it belongs.", "reasonable, rehearsed"),
             ("NORA", "The past is the only thing you've ever asked me to leave behind.", "cold")],
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
            [("MARGARET", "If you reopen that investigation, I'll make sure the town remembers who lit the match.", "pleasant threat"),
             ("NORA", "Go ahead. I've played the villain in your story for ten years.", "tired")],
            [("NORA", "A debt doesn't transfer with land, Adrian. But fraud does.", "precise"),
             ("ADRIAN", "Big words for someone with no lawyer.", "smiling")],
            [("SAM", "The old survey files are in the boathouse. What's left of them.", "urgent"),
             ("NORA", "Then we go tonight, before the hearing.", "decided")],
            [("SAM", "You always did like a bad idea with good lighting.", "dry"),
             ("NORA", "You coming or not? Bring the pry bar.", "impatient")],
            [("NORA", "There. Seawall permits. Signed by Margaret. Dated before the fire.", "shaking"),
             ("SAM", "That's not a permit. That's a motive.", "quiet")],
            [("ADRIAN", "Give me the file and I'll tell the town the fire was an accident.", "reasonable"),
             ("NORA", "And in exchange?", "wary"),
             ("ADRIAN", "I'll say you were with me that night. Everything goes away.", "soft")],
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
             ("MARGARET", "Then you'll lose the only home you have left.", "quiet")],
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
        "wardrobe": "storm-soaked shirt and trousers, no coat, hair plastered down",
        "props": ["the emergency petition", "a statement form", "the harbor logbook", "the cold lamp"],
        "actions": [
            "Rain hammers the town hall windows as Nora faces the panel.",
            "Margaret sits perfectly still in the front row.",
            "Claire reads the emergency petition aloud.",
            "Nora stands in the empty lighthouse, the lamp cold above her.",
            "Sam signs a statement at the harbor office, hand shaking.",
            "Nora listens through a half-open door, unseen.",
            "Nora walks the storm beach alone, hair plastered to her face.",
            "Adrian waits in her kitchen with the sale papers.",
            "Nora stares into the lighthouse lens, thinking.",
            "Nora finds an old harbor logbook behind the lens housing.",
        ],
        "sfx": "storm wind, rain on glass, a gavel, a chair scraping",
        "lines": [
            [("NORA", "I'd rather lose the house than let you keep my father's name.", "steady"),
             ("MARGARET", "You already lost it ten years ago.", "soft")],
            [("CLAIRE", "The hearing is packed. Half the town came.", "nervous"),
             ("NORA", "Good. This time, I want witnesses.", "resolved")],
            [("SAM", "Nora. Whatever happens in there... I should have told you the truth ten years ago.", "low"),
             ("NORA", "Then tell it now. Loud enough for the back row.", "fierce")],
            [("SAM", "I signed a false statement. Margaret Keller wrote it. I was paid to stay quiet.", "public, shaking"),
             ("MARGARET", "He's a firefighter with a grudge.", "dismissive")],
            [("NORA", "Then let's hear from someone who can't be bought.", "calm"),
             ("ADRIAN", "You're bluffing.", "uneasy"),
             ("NORA", "I don't bluff. I document.", "flat")],
            [("NORA", "The harbor log. 2:14 a.m. Keller launch. Adrian at the helm.", "precise"),
             ("MARGARET", "That log is thirty years of weather and guesswork.", "sharp")],
            [("NORA", "2:14 a.m. One passenger. Margaret.", "quiet"),
             ("ADRIAN", "It was an accident. We only meant to scare him.", "breaking"),
             ("NORA", "You burned a boathouse and let a town bury my father.", "raw")],
            [("NORA", "You didn't scare him. You killed the only man who could prove it.", "cold"),
             ("ADRIAN", "He was already dead when we got there.", "whisper")],
            [("NORA", "Then who was in the boathouse with him?", "sharp"),
             ("ADRIAN", "Ask your mother.", "quiet")],
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
            [("CLAIRE", "If you present that log, the town will turn on the Kellers. And on your mother.", "worried"),
             ("NORA", "Then they'll finally tell the truth about her.", "steady")],
            [("NORA", "Whatever they say about me tomorrow, I want you to hear it from me first.", "vulnerable"),
             ("SAM", "I'm not going anywhere.", "low")],
            [("MARGARET", "You'll lose the only home you have left.", "cold"),
             ("NORA", "I'm not doing this to keep the house. I'm doing it to keep his name.", "fierce")],
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
            [("SAM", "I signed a false statement. Margaret Keller wrote it. I was paid to stay quiet.", "public, clear"),
             ("MARGARET", "He's a firefighter with a grudge. Nothing he says survives cross.", "dismissive")],
            [("NORA", "Then let's hear from someone who can't be bought. The harbor log.", "calm"),
             ("ADRIAN", "That's a piece of paper.", "uneasy")],
            [("NORA", "2:14 a.m. Keller launch. Two passengers. Adrian at the helm.", "precise"),
             ("MARGARET", "That log is thirty years of weather and guesswork.", "sharp")],
            [("NORA", "One passenger is Margaret. The other signed the fire report.", "quiet"),
             ("CLAIRE", "The fire marshal. It's his signature.", "stunned")],
            [("ADRIAN", "It was an accident. We only meant to scare him.", "breaking"),
             ("NORA", "You burned a boathouse and let a town bury my father for it.", "raw")],
            [("NORA", "That's not an accident. That's a choice. And this town gets to see it.", "fierce"),
             ("MARGARET", "You'll regret this.", "quiet")],
            [("NORA", "Wait. This ledger is older. My mother's name is on every page.", "hushed"),
             ("SAM", "Nora... she's alive?", "stunned"),
             ("NORA", "She's been here the whole time.", "cold")],
        ],
    },
]

DEMO_CHARACTERS = [
    {"id": "nora", "name": "Nora Hale", "role": "protagonist", "archetype": "protagonist",
     "pronoun": "she", "voice_lock": "warm mid-range American English, controlled, slightly breathy under pressure"},
    {"id": "sam", "name": "Sam Calloway", "role": "love_interest", "archetype": "love_interest",
     "pronoun": "he", "voice_lock": "quiet, low American English, careful diction, warmth under restraint"},
    {"id": "margaret", "name": "Margaret Keller", "role": "antagonist", "archetype": "antagonist",
     "pronoun": "she", "voice_lock": "low, polished, unhurried American English, never shouts"},
    {"id": "adrian", "name": "Adrian Keller", "role": "antagonist_heir", "archetype": "antagonist",
     "pronoun": "he", "voice_lock": "smooth mid-range American English, reasonable tone that never quite reaches sincerity"},
    {"id": "claire", "name": "Claire Boone", "role": "ally", "archetype": "ally",
     "pronoun": "she", "voice_lock": "grounded, plainspoken American English with a slight coastal New England softness"},
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
    pronoun_to_phrase = {
        "she": "the same woman as the reference image",
        "he": "the same man as the reference image",
    }
    by_speaker = {c["name"].upper(): c for c in DEMO_CHARACTERS}
    scenes: List[Dict[str, Any]] = []

    for idx in range(1, nf.SCENE_COUNT + 1):
        act_idx = (idx - 1) // 10
        local = (idx - 1) % 10
        act = DEMO_ACTS[act_idx]
        loc_name, light = act["locations"][local % len(act["locations"])]
        lines = act["lines"][local]
        primary_speaker = lines[0][0]
        character = by_speaker.get(primary_speaker, DEMO_CHARACTERS[0])
        who = pronoun_to_phrase[character["pronoun"]]

        shot1 = rotation[(local + act_idx) % len(rotation)]
        shot2 = "tight close-up"
        if shot1 == shot2:
            shot2 = "medium shot"
        shot3 = ["over-the-shoulder shot", "low-angle hero shot", "medium shot", "wide establishing shot"][local % 4]
        if shot3 in (shot1, shot2):
            shot3 = "insert shot of the evidence object"

        prop = act["props"][local % len(act["props"])]
        expression = DEMO_EXPRESSIONS[(idx - 1) % len(DEMO_EXPRESSIONS)]
        body = (
            f"Cinematic still of {who}, {shot1}, at {loc_name}, {light}. "
            f"{character['name']} {act['actions'][local][len(character['name']) + 1:].strip()} "
            f"Expression: {expression}. Wardrobe: {act['wardrobe']}. "
            f"Framing keeps the face unobstructed and centered for a 9:16 crop."
        )
        body = body.replace("..", ".")

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
            "characters": [c["name"] for c in DEMO_CHARACTERS if any(line[0] == c["name"].upper() for line in lines)],
            "on_screen_hook": DEMO_HOOKS.get(idx, ""),
            "first_frame_prompt": body,
            "internal_cuts": [
                {"at": 0.0, "framing": shot1, "action": act["actions"][local]},
                {"at": 3.5, "framing": shot2, "action": f"Close detail on {prop}; the room falls quiet around it."},
                {"at": 6.9, "framing": shot3, "action": f"{character['name']} reacts, holding the moment before the next line."},
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
        "locations": [
            {"id": "lighthouse", "name": "Hale lighthouse", "visual": "whitewashed stone tower on a black cliff, cold lamp, salt-eaten wood"},
            {"id": "harbor", "name": "Keller harbor", "visual": "working docks, wet planks, sodium lights, a family launch named MARGARET II"},
            {"id": "townhall", "name": "Town hall", "visual": "1930s council chamber, dark wood, tall windows, folding chairs"},
            {"id": "estate", "name": "Keller estate", "visual": "glass and cedar house above the water, warm interiors, no clutter"},
        ],
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
    warnings: List[str] = []
    if len(payloads) == 1:
        return payloads[0], warnings
    full = [p for p in payloads if len(p.get("scenes") or []) == nf.SCENE_COUNT]
    if full:
        warnings.append("Se recibieron varios JSON con 60 escenas; se usa el primero y se ignoran los demás.")
        return full[0], warnings

    merged: Dict[str, Any] = {"scenes": []}
    teasers: Dict[int, Dict[str, Any]] = {}
    for pos, payload in enumerate(payloads):
        merged["scenes"].extend(payload.get("scenes") or [])
        for key in ("episode", "characters", "locations", "acts", "publisher", "soundtrack"):
            if key not in merged and payload.get(key):
                merged[key] = payload[key]
        for teaser in payload.get("teasers") or []:
            if not isinstance(teaser, dict):
                continue
            try:
                tid = int(teaser.get("id") or 0)
            except (TypeError, ValueError):
                continue
            if tid and tid not in teasers:
                teasers[tid] = teaser
    if teasers:
        merged["teasers"] = [teasers[k] for k in sorted(teasers)]
    warnings.append(f"Fusionados {len(payloads)} archivos en un solo maestro ({len(merged['scenes'])} escenas).")
    return merged, warnings


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
    parser.add_argument("--part", choices=["full", "1", "2"], default="full",
                        help="Divide el guion en 2 tandas si el LLM no alcanza 60 escenas.")
    parser.add_argument("--context", type=str, default="",
                        help="Archivo de la parte anterior para continuidad (modo --part 2).")
    parser.add_argument("--brief", action="store_true", help="Genera story_brief.md + llm_prompt.md (default).")
    parser.add_argument("--template", action="store_true", help="Episodio demo de calibración, sin LLM.")
    parser.add_argument("--ingest", nargs="+", default=None, metavar="JSON",
                        help="Uno o dos JSON del LLM para validar y guardar como master_episode.json.")
    parser.add_argument("--validate", action="store_true", help="Valida un master_episode.json existente.")
    parser.add_argument("--allow-partial", action="store_true", help="Permite ingerir menos de 60 escenas.")
    parser.add_argument("--force", action="store_true", help="Sobrescribe sin preguntar (siempre deja backup).")
    args = parser.parse_args(argv)

    slug = nf.slugify(args.slug)
    paths = nf.create_project(slug)
    nf.log("")
    nf.log("=" * 70)
    nf.log("  NOVEL FACTORY — 01 · Guion maestro de 60 escenas (10:00)")
    nf.log("=" * 70)
    nf.info(f"Proyecto: {paths['root']}")

    if args.validate:
        master = nf.load_master(paths["root"])
        result = nf.validate_master(master, allow_partial=args.allow_partial)
        nf.log("")
        return 0 if nf.print_validation(result) else 1

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
        result = nf.validate_master(master, allow_partial=args.allow_partial)
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
        nf.log("")
        nf.log("  Siguiente: python generators/02_export_chatgpt_queue.py " + slug)
        return 0

    if args.template:
        nf.info("Generando episodio demo de calibración (sin LLM)…")
        payload = build_demo_payload(slug, args.title or "The Silent Contract", args.personaje, args.episode_number)
        master, warnings = nf.normalize_master(payload, slug, args.title, repair=True)
        result = nf.validate_master(master)
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
    )
    prompt_path = nf.write_text(paths["root"] / "llm_prompt.md", prompt)

    nf.log("")
    nf.ok(f"Brief:  {brief_path}")
    nf.ok(f"Prompt: {prompt_path}  ({len(prompt):,} caracteres)")
    nf.log("")
    nf.log("  Pasos:")
    nf.log("   1. Abre llm_prompt.md, cópialo completo y pégalo en Claude / Gemini / ChatGPT.")
    nf.log("   2. Guarda la respuesta como projects/" + slug + "/llm_response.json")
    nf.log("   3. python generators/01_story_to_master_json.py " + slug + " --ingest " +
           f"projects/{slug}/llm_response.json")
    if args.part != "full":
        nf.log("   (Modo por partes: repite --brief --part 2 --context <parte1.json> y luego")
        nf.log("    ingiere los dos JSON juntos con --ingest parte1.json parte2.json)")
    nf.log("")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except nf.NFError as exc:
        nf.err(str(exc))
        sys.exit(1)

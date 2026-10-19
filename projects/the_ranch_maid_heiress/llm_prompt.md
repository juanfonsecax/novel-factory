# SHORT-DRAMA SHOWRUNNER TASK — The Stable Girl (Episode 1)

You are a senior US short-drama showrunner and screenwriter. You write cinematic,
vertically-shot soap suspense for an English-speaking US audience. Your scripts
are performed by AI characters with native audio, one 10-second clip per scene.

## OBJECTIVE

Write the complete episode as ONE valid JSON object that follows the schema below.
Write the COMPLETE episode: all 60 scenes, Acts 1-6. Do not summarize or skip scenes.

## SOURCE BRIEF

# Story Brief — The Stable Girl

- **Slug:** the_ranch_maid_heiress
- **Episode:** 1
- **Genre:** romantic suspense short-drama
- **Language:** English (US) — all dialogue and prompts
- **Publisher persona (USA WHITE):** emma_hayes

## Premise / idea

# THE STABLE GIRL — Episodio 1 de "Silver Creek Secrets"

## Premisa

Elena Vance trabaja desde niña como moza de cuadra y criada en el rancho Silver Creek, la propiedad de los Blackwell en Montana. Su madre, June Vance, murió en un incendio en el establo quince años atrás. La noche de la fiesta de bienvenida de Richard, heredero de los Blackwell, Victoria Blackwell acusa públicamente a Elena de robar el reloj de plata de su difunto marido: el reloj aparece "casualmente" en la bolsa de montura de Elena. Es un montaje del propio Richard.

Cuando Elena está a punto de ser detenida, encuentra en el forro del viejo montura de su madre una llave de latón. Detrás de la pared del cuarto de aperos, sellado desde el incendio, aparece una caja de hojalata con la escritura original: en 2008 Walter Blackwell vendió Silver Creek a June Vance por un dólar. La escritura registrada en el condado en 2009 —seis meses después de la muerte de June— es una falsificación de Victoria.

Elena deberá probar que su madre era la dueña, recuperar el testamento de Walter de la caja 14 del banco, sobrevivir a un segundo montaje (incendio provocado) y enfrentarse a Victoria en la gala del condado, donde la verdad sale a la luz en público y aparece un segundo heredero que nadie conocía.

## Tono y formato

Short-drama de suspense romántico para audiencia US (mujeres 25-55). 60 escenas de 10 s = 10 minutos. Inglés nativo US en todos los diálogos y prompts. Tono cinematográfico, íntimo, de alto riesgo y ritmo rápido.

## Reparto

- **Elena Vance** — protagonista, moza de cuadra. Digna, observadora, se cansa de pedir permiso.
- **Victoria Blackwell** — antagonista, dueña aparente del rancho. Elegante, paciente, sonríe mientras amenaza.
- **Richard Blackwell** — heredero. Encantador y cobarde; plantó el reloj.
- **Cole Barrett** — capataz del rancho, interés romántico. Callado, leal, carga con una culpa de la noche del incendio.
- **Maggie Doyle** — ama de llaves, aliada. Firmó una declaración falsa hace quince años y busca redimirse.

## Localizaciones

Casa Blackwell (vestíbulo y gran salón), establo de Silver Creek, la casita del guarda y la oficina de registros del condado / banco.

## Non-negotiables

- 60 scenes x 10 seconds = 600 seconds (10:00) master in 16:9.
- English only. US short-drama cadence: short lines, concrete stakes, no exposition dumps.
- 6 acts of 10 scenes. Cliffhanger at 10 / 20 / 30 / 40 / 50. Payoff at 59 and a next-episode hook at 60.
- One first-frame still per scene (16:9, center-weighted so a 9:16 crop works).
- Native audio in the generated clip: dialogue + diegetic ambience only. No music.
- No real celebrities, brands, explicit content, graphic violence or hate.
- Reference images define faces: never describe age, eye color or base hair color in prompts.

## Deliverable

The JSON described in `llm_prompt.md`, saved as `llm_response.json` next to this file.



## FORMAT (NON-NEGOTIABLE)

- Total scenes: 60 x 10 s = 600 s.
- Dialogue per scene: [18, 30] words TOTAL (all speakers).
- Internal cuts per scene: [2, 4], first at 0.0 s, separated by 2.5-4 s.
- Open-loop types allowed: unanswered question in the first line; object that should not exist; person who knows more than they admit; deadline announced by a third party; public accusation with no proof yet; romantic confession interrupted; a lie the audience can see.
- Dopamine cadence: Every 2-3 scenes deliver one of: reveal, comeback line, protective gesture, status flip, romantic near-miss, micro-revenge, public embarrassment of the antagonist.
- Cliffhanger types allowed: new evidence that reframes the case; forced choice with a deadline; betrayal by an ally; antagonist drops the mask; protagonist uses the antagonist's own weapon; a door opens on a person who should be dead or absent.
- Forbidden: slow establishing montage in scene 1; villain monologue explaining the whole plan; resolution by accident, weather or coincidence; characters withholding information for no reason; melodrama without a concrete physical stake; cliffhanger that negates the previous episode's payoff.

## ACT MAP

### Act 1 — The Bait (scenes 1-10)
Goal: Open a visceral question in the first 3 seconds, establish the protagonist's desire and wound, then detonate the inciting incident.
Must happen: Scene 1 poses an unanswered question or a visual contradiction (no slow establishing montage).; The protagonist wants something concrete and is denied it by someone with power.; The antagonist is introduced as reasonable and likable, never cartoonish.; Scene 10 reveals a secret object, document, witness or betrayal that changes the question.
Retention device: Open loop stacked on a second open loop; every scene ends on a partial answer that creates a new question.
Dopamine point: Scene 8-10: first small act of defiance from the protagonist.

### Act 2 — The Trap (scenes 11-20)
Goal: Tighten the trap: the antagonist uses the system, not violence. Humiliation and betrayal push the protagonist toward a forced choice.
Must happen: The protagonist's credibility or livelihood is threatened in public.; A trusted ally withholds information or signs something they should not.; The antagonist offers a deal the protagonist cannot easily refuse.; Scene 20 ends on a demand, a deadline or a public accusation.
Retention device: Countdown pressure (hearing, deadline, debt) plus dramatic irony: the audience learns the truth before the town does.
Dopamine point: Scene 17-18: a first piece of evidence lands in the protagonist's hands.

### Act 3 — The First Crack (scenes 21-30)
Goal: The protagonist stops reacting and starts investigating. A romance or loyalty beat raises the emotional stakes. A costly mistake keeps the antagonist ahead.
Must happen: The protagonist takes a concrete risk (break-in, trespass, public question, leaked file).; The audience gets a hard piece of proof the town does not yet believe.; A romance or intimacy beat complicates the alliance.; The antagonist counterattacks using the protagonist's own action against her/him.; Scene 30 ends on a temptation or a compromise that could destroy the case.
Retention device: Proof vs. believability: the protagonist has the truth but not the power to make anyone believe it.
Dopamine point: Scene 24-25: discovery of the physical evidence (ledger, recording, permit, logbook).

### Act 4 — The Dark Night (scenes 31-40)
Goal: Take everything away. The ally breaks, the institution turns, and the protagonist is isolated. The lowest point must be caused by a choice, not bad luck.
Must happen: The protagonist rejects the antagonist's deal and pays an immediate price.; The institution (court, trust, employer, town council) freezes or seizes something vital.; The ally's betrayal is explained by a credible threat, not villainy.; The protagonist loses the physical evidence or access to it.; Scene 40 ends with a new interpretation of an old object/place (the lighthouse, the house, the boathouse).
Retention device: All-is-lost engine: the audience wants to see how the protagonist climbs out, not whether she deserves to.
Dopamine point: Scene 35-36: a micro-revenge line or a quiet power move that costs the protagonist something.

### Act 5 — The Turn (scenes 41-50)
Goal: The protagonist turns the same system against the antagonist using the truth she already had. The confrontation begins in public. A final complication raises the price of winning.
Must happen: The protagonist converts a discarded detail into leverage (logbook, timestamp, witness, receipt).; The antagonist's power is shown to depend on the town's belief, which can be broken.; A public or semi-public confrontation forces the antagonist to drop the mask.; The ally earns a partial redemption through a costly action.; Scene 50 ends on the antagonist's last threat or a new piece of evidence that reframes the case.
Retention device: Power flip: the audience now knows the protagonist can win, but not at what cost.
Dopamine point: Scene 47-49: the protagonist says the line the audience has been waiting ten episodes for.

### Act 6 — The Payoff (scenes 51-60)
Goal: Deliver the public confrontation, the emotional payoff and the romantic resolution. End on a new open loop for the next episode.
Must happen: The truth is exposed in a public, irreversible way (hearing, broadcast, town meeting).; The antagonist loses the specific thing they used to control the protagonist.; The protagonist chooses what she keeps, not only what she destroys.; A romantic or familial payoff lands in one concrete gesture, not a speech.; Scene 59 or 60 plants the next-episode hook in a single line or object.
Retention device: Payoff + new question: close the season question and open a second, more personal mystery in the last 20 seconds.
Dopamine point: Scene 56-59: public humiliation of the antagonist and the protagonist's final refusal.

## FIRST-FRAME / VISUAL RULES

- Step 0 (once per episode): fill "visual_reference" for every main character. generators/02 exports chatgpt_reference_sheets.txt so the user can create one reference sheet per character BEFORE the frames and keep all of them attached in the same ChatGPT thread.
- One still per scene, 16:9, cinematic, photoreal. It must be the literal first frame of the clip.
- Start the prompt with "Cinematic still of the same woman as the reference image" (or "the same man...").
- Identity comes from the attached reference images: NEVER write age, name, eye color, skin tone or base hair color in the prompt. Describe only transient state: moment hairstyle, wet hair, flush, sweat, expression, gaze, wardrobe, pose, light, framing.
- Include framing, location, time of day, wardrobe, expression and one telling environmental detail.
- Center-weight the subject so a 9:16 crop still works. Keep the face unobstructed.
- 45-80 words per prompt. Do NOT include the global style suffix or negative prompt; they are appended automatically.
- No text, letters, logos, watermarks or captions inside the image.
- Global look (for your reference, not to repeat verbatim): prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette
- Allowed lighting: late-afternoon sun raking across the scene with long shadows; overcast storm light with a cold rim on faces; practical tungsten warmth inside against a blue dusk exterior; single hard window light with deep falloff; harbor floodlights and wet reflections at night; fireplace or lamp glow with visible falloff, never flat studio light
- Camera vocabulary: wide establishing shot with a human scale reference; medium shot, chest up, subject slightly off-center; tight close-up, eyes in sharp focus, background falling off; over-the-shoulder shot with the listener soft in foreground; low-angle hero shot for status flips; insert shot of the evidence object (hands only)

## AUDIO / VOICE RULES

- Native US English only. Conversational pace (~2.5 words/second).
- 18-30 words of dialogue TOTAL per scene across all speakers. 1-3 lines. Silence is allowed but rare.
- Subtext over exposition. Concrete nouns. No therapy-speak, no lectures, no villain monologues.
- The clip contains dialogue + diegetic ambience only. NO music, NO narrator, NO subtitles.
- Voice archetypes you may reference: {"protagonist": "warm mid-range American English, controlled, slightly breathy under pressure, never theatrical", "antagonist": "low, polished, unhurried American English, never shouts, smiles through threats", "ally": "grounded, plainspoken American English with a slight coastal New England softness", "love_interest": "quiet, low American English, careful diction, warmth held under restraint", "authority": "clipped, neutral American English, procedural calm, no drawl"}
- Delivery format: {speaker} ({delivery}): "{line}"

## CONTINUITY

{
  "wardrobe": "Lock one outfit per character per act; change it only at an act break with a story reason.",
  "props": "The evidence object must be visible or referenced in at least 4 scenes across different acts.",
  "time_of_day": "Acts 1-2 late afternoon to night; act 3 night; act 4 storm night; acts 5-6 next morning to dusk.",
  "locations": "Reuse 3-4 locations maximum so the audience learns the geography: the lighthouse, the harbor/boathouse, the town hall, the antagonist's house.",
  "identity": "Reference images define faces. Never describe age, eye color or base hair color in prompts; describe only transient state (hair style, wet hair, flush, sweat, expression, wardrobe)."
}

## TEASERS

Teasers: include all 3 (6 consecutive scenes each, 60 s each).
Each teaser is exactly 6 consecutive scenes (60 s), a 5-10 word hook_text (one CAPS word allowed),
and a caption of 2-4 short lines with one question and an honest CTA (follow/save/comment).
Do not promise DMs, downloads or links that do not exist.

## JSON SCHEMA (fields are mandatory unless marked optional)

```json
{
  "episode": {
    "slug": "the_ranch_maid_heiress",
    "title": "The Stable Girl",
    "series_title": "Series name",
    "episode_number": 1,
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
    "personaje_id": "emma_hayes",
    "cta": "Follow for Episode 2.",
    "hashtags": ["#shortdrama", "#novel", "#storytime", "#drama", "#episode1"],
    "ai_disclosure": true
  },
  "soundtrack": {"mood": "tense coastal romantic suspense", "bpm": 78, "notes": "Dialogue forward; music mixed in post."}
}
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

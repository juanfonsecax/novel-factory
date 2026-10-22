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
- Dialogue per scene: 20 words TOTAL across all speakers (hard cap). Target [6, 20]. Never exceed 20.
- Max 15 words per single line. At ~2.5 words/second that is <= 8.5 s of speech in a 10 s scene, leaving room for pauses.
- Internal cuts per scene: 1 to 4 shots built from the dialogue, not a fixed 0/3/7 grid. Shot 1 always starts at 0.0 in motion from the storyboard panel; when exactly two different characters speak, Shot 1 is a two-shot holding both lines. Otherwise each spoken line gets its own shot with the speaker on camera, face and mouth visible, facing the recipient. Silent inserts, reactions and object shots come after the dialogue, and a revelation insert gets its own centered silent shot of 2-3 s.
- Causal order is strict: consequences never precede their cause, clues are revealed once, and every location change needs a visible transition. Group 3-6 consecutive scenes per dramatic situation/location block.
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

## VIRAL STRUCTURE CATALOG (LATAM -> USA)

Use one of these six PROVEN LATAM -> USA structures as the skeleton of the episode.
Keep the structure, stakes and hook type; adapt names, locations and dialogue to the brief.

### 1. ranch_laundress_stolen_heirloom — The Ranch Laundress and the Stolen Heirloom (@novelasaa7, 831K views)
Genre: Ranch / Class Revenge | Setting: Texas or Montana ranch
Premise: A humble ranch laundress is publicly accused of stealing the family heirloom. The real thief is a wealthy family member, and the heir she loves is the only one willing to prove her innocence.
Hook: They accused the help. The thief wore the family name.
Structure: Public humiliation: the heirloom disappears during a family gathering and the laundress is accused. -> A physical detail contradicts the accusation: mud on the wrong boots, a broken clasp, a locked room. -> The heir investigates and discovers the planted evidence and the family cover-up. -> The laundress is forced to leave; the heir stops her at the gate with proof. -> Public reveal before the family and the town: the real thief is exposed. -> Payoff: the laundress is vindicated, the heir chooses her, and a new family secret opens.
USA adaptation: Texas or Montana ranch, county fair or ranch anniversary party, US English, land and class stakes, conservative family dynasty.

### 2. humiliated_vagabond_is_billionaire_owner — The Humiliated Vagabond Is the Billionaire Owner (@Mini_Dramas07, 658K views)
Genre: Hidden Billionaire / Revenge | Setting: Texas or Montana ranch
Premise: A humble ranch hand arrives at the property and is humiliated by the corrupt foreman and the family, never suspecting that he is the new billionaire owner who bought the entire ranch.
Hook: They threw out the man who owns the land.
Structure: Humiliation: the drifter is mocked, underpaid and thrown out of the ranch house. -> The heroine defends him and loses her job for it. -> The drifter returns as the anonymous billionaire owner and quietly changes the power dynamic. -> The corrupt foreman tries to cover up the abuse and frames the heroine. -> Public reveal: the owner identifies himself and exposes the foreman's fraud. -> Payoff: the heroine is chosen, the foreman faces the consequences, and a new threat appears.
USA adaptation: Texas or Montana cattle ranch, US English, ranch-hand class conflict, land ownership and public status reversal.

### 3. hidden_will_secret_daughter — The Hidden Will and the Secret Daughter (@Mini_Dramas07 & @TIEMPOCONLASABUELAS, 578K views)
Genre: Family Secret / Inheritance | Setting: Texas ranch or Montana estate
Premise: A young woman enters the ranch as a maid to find the true will hidden under the floorboards or in a secret drawer by the ambitious widow and the family lawyer.
Hook: The will named a daughter no one had ever met.
Structure: The maid arrives at the ranch and is treated as invisible by the widow and the lawyer. -> A loose floorboard or locked drawer reveals a second, older will. -> The widow accuses the maid of theft and forgery before the family. -> The maid finds a birth record, photograph or letter proving she is the secret daughter. -> Public hearing: the lawyer's forgery is exposed and the widow loses control. -> Payoff: the maid claims her name and inheritance, and a new family secret opens.
USA adaptation: Texas or Montana ranch estate, US English, probate hearing, legitimacy and family-dynasty stakes.

### 4. contract_marriage_proud_foreman — Contract Marriage with the Proud Foreman (@Mini_Dramas07, 185K views)
Genre: Contract Marriage / Romance | Setting: Texas or Wyoming ranch
Premise: To save her late father's ranch from bank ruin, the protagonist must marry her proud rival by contract. In secret, he protects her from an internal betrayal that wants to take the land.
Hook: She bought a husband for one year. He wanted the truth.
Structure: The bank deadline forces the contract marriage to be signed in public. -> Forced proximity reveals the foreman's secret debt and the heroine's collapsing ranch. -> Sabotage at the ranch puts the heroine in danger and the foreman protects her. -> The antagonist exposes the contract to humiliate them; the couple turns it into a real commitment. -> Public confrontation: the sabotage is traced to the antagonist. -> Payoff: the contract is torn up, a real proposal lands, and a new threat appears.
USA adaptation: Texas or Wyoming ranch, US English, bank foreclosure, blue-collar vs. landowner class tension.

### 5. untamable_champion_horse — The Untamable Champion Horse (@Mini_Dramas07, 122K views)
Genre: Horse Ranch / Forbidden Love | Setting: Kentucky horse farm or Texas ranch
Premise: A champion horse that nobody on the ranch can ride is tamed by the humblest worker on the property. The feat saves the ranch from ruin and awakens a forbidden love.
Hook: The horse that broke every rider chose the one nobody saw.
Structure: The untamable champion injures another rider and the ranch is threatened with foreclosure. -> The humblest worker is blamed and forbidden from entering the stable. -> A hidden injury or doped feed reveals the rival stable's sabotage. -> The worker bonds with the horse and proves the method works before the championship. -> Public race: the sabotage is exposed and the rival stable is disqualified. -> Payoff: the horse wins, the forbidden love is chosen, and a new race or threat opens.
USA adaptation: Kentucky or Texas horse country, US English, championship race, forbidden romance and animal stakes.

### 6. grandmas_buried_secret_betrayal — Grandma's Buried Secret and the Family Betrayal (@TIEMPOCONLASABUELAS & @Dramasquetocanelalma, +500K views)
Genre: Family Betrayal / Mystery | Setting: Texas ranch or Louisiana family estate
Premise: A grandmother despised by her ambitious children reveals a secret buried for decades and gives the inheritance to the only person who cared for her with nobility.
Hook: Grandma left a box in the ground and a warning on the lid.
Structure: At the family gathering, the despised grandmother announces a buried secret. -> The ambitious children deny it and threaten the protagonist's inheritance. -> A buried box, land deed or photograph proves the fortune was stolen from another branch. -> The family destroys evidence and tries to run the protagonist out of town. -> Public reveal at the family business or town meeting: the betrayal is exposed. -> Payoff: the inheritance goes to the noble caregiver, and a second grave or name opens the next mystery.
USA adaptation: Texas ranch or Louisiana family estate, US English, funeral and land-deed stakes, matriarch inheritance and family-business betrayal.




## NARRATIVE CONTINUITY ENGINE (MANDATORY)

The episode is 10 minute-blocks of 6 scenes. These rules are checked by the validator.

1. SINGLE DRIVING QUESTION PER BLOCK: every 6-scene block carries exactly ONE
   `driving_question` in the top-level `narrative_continuity.minute_blocks` array. No scene may
   open a second question inside the block; the block answers or complicates that one question.
2. STRICT CAUSE AND EFFECT CHAIN: every scene declares three strings:
   - `because_previous_ended_with`: copy VERBATIM the previous scene's `single_change_at_end`.
   - `this_scene_starts_with`: the concrete action already in motion that follows from it.
   - `single_change_at_end`: the ONE irreversible state change produced by this scene.
   Scene 1 uses `"The episode opens cold; there is no prior beat."` for the first field.
3. NO LOCATION PING-PONG: group 3-5 consecutive scenes in the same location. A-B-A is forbidden.
4. CANONICAL OBJECT LOCK: use one exact `key_object` name in the storyboard panel, in the
   Shot 1 action and in the Key Object list. Never switch to an alias.
5. DISORDER TEST: if the block is shuffled and the chain of consequences no longer makes sense,
   rewrite it. Mechanical placeholders (`hard cut...`, `the room falls quiet...`,
   `reacts as the line lands...`) are rejected by validation.

The three per-scene fields are mandatory from scene 2 to scene 60; scene 1 declares its opening
state and first change. Never repeat the same sentence in `this_scene_starts_with` and
`single_change_at_end`.


## FIRST-FRAME / VISUAL RULES

- Step 0 (once per episode): fill "visual_reference" for every main character. generators/02 exports chatgpt_reference_sheets.txt so the user can create one reference sheet per character BEFORE the frames and keep all of them attached in the same ChatGPT thread.
- One still per scene, 16:9, cinematic, photoreal. It must be the literal first frame of the clip.
- Open every prompt with the character name and the reference file: e.g. "Cinematic still of Nora Hale (the character in reference_nora.png), ...". Use the character's own id in the filename (lowercase, underscores).
- Identity comes from the attached reference images and the reference file. NEVER write age, eye color, skin tone or base hair color in the prompt. Describe only transient state: moment hairstyle, wet hair, flush, sweat, expression, gaze, wardrobe, pose, light, framing.
- Close the prompt with a one-line binding: "Keep <Name>'s face and wardrobe identical to reference_<id>.png."
- Include framing, location, time of day, wardrobe, expression and one telling environmental detail.
- Center-weight the subject so a 9:16 crop still works. Keep the face unobstructed.
- 45-80 words per prompt. Do NOT include the global style suffix or negative prompt; they are appended automatically.
- No text, letters, logos, watermarks or captions inside the image, except the exact "diegetic_text" word(s) declared for that scene (nothing else becomes legible).
- Global look (for your reference, not to repeat verbatim): prestige cinematic short-drama, photoreal, 35mm anamorphic glass, shallow depth of field, fine film grain, natural skin texture, muted teal-and-amber coastal palette
- Allowed lighting: late-afternoon sun raking across the scene with long shadows; overcast storm light with a cold rim on faces; practical tungsten warmth inside against a blue dusk exterior; single hard window light with deep falloff; harbor floodlights and wet reflections at night; fireplace or lamp glow with visible falloff, never flat studio light
- Camera vocabulary: wide establishing shot with a human scale reference; medium shot, chest up, subject slightly off-center; tight close-up, eyes in sharp focus, background falling off; over-the-shoulder shot with the listener soft in foreground; low-angle hero shot for status flips; insert shot of the evidence object (hands only)

## AUDIO / VOICE RULES

- Native US English only. Conversational pace (~2.5 words/second).
- 6-15 words of dialogue TOTAL per scene across all speakers (hard cap 15). 1-2 lines, max 15 words each. Finish before 8.5 s. Silence is allowed but rare.
- Every "speaker" MUST be the exact name of a character declared in "characters[].name". Never invent speakers (no CLERK, no NARRATOR, no unnamed roles).
- Subtext over exposition. Concrete nouns. No therapy-speak, no lectures, no villain monologues.
- The clip contains dialogue + diegetic ambience only. NO music, NO narrator, NO subtitles.
- Voice archetypes you may reference: {"protagonist": "warm mid-range American English, controlled, slightly breathy under pressure, never theatrical", "antagonist": "low, polished, unhurried American English, never shouts, smiles through threats", "ally": "grounded, plainspoken American English with a slight coastal New England softness", "love_interest": "quiet, low American English, careful diction, warmth held under restraint", "authority": "clipped, neutral American English, procedural calm, no drawl"}
- Delivery format: {speaker} ({delivery}): "{line}"

## SPEAKER-SHOT LOCK / OBJECT LOCK (MANDATORY)

1. ONE LINE = ONE SPOKEN SHOT. Whoever speaks is ON CAMERA with face and mouth visible for the whole line, facing the recipient; the recipient is in frame or over the shoulder, never hidden behind the speaker's back. Never put a line over an insert of hands, an object or an empty framing.
2. TWO-HANDER = SHOT 1. When exactly two different characters speak in the scene (one line each), Shot 1 is a two-shot that holds BOTH lines: both faces and mouths visible, each turned toward the other. Inside a two-hander, do not use single close-ups for the same two lines.
3. SILENT BEATS COME AFTER THE DIALOGUE. Inserts, reactions and object shots are silent and follow the spoken shots, except a revelation: the reveal goes in its own centered silent insert of 2-3 s between spoken shots, and the scene states when the dialogue ends.
4. MUZZLE THE MUTE. Every character present who does not speak is listed in "present_silent" and stays with the mouth closed for the whole scene. Never give a mute character a speaking verb or a quoted line.
5. NEVER SHOW THE INSIDE OF THE HIDING PLACE. If an object is hidden inside a bag, box, safe or drawer, the camera sees the container from outside, loosened but never gaping; the interior is only shown in the reveal scene, as the object being taken out.
6. OBJECT IN / OBJECT OUT. "object_start" and "object_end" name what the audience sees at the first and last second; both are physically visible in frame, not implied.
7. TEXT ON OBJECT. The only legible text in any frame is the exact word(s) declared in "diegetic_text"; documents, signs and screens stay illegible unless the plot declares them.

## CONTINUITY

{
  "wardrobe": "Lock one outfit per character per act; change it only at an act break with a story reason.",
  "props": "The evidence object must be visible or referenced in at least 4 scenes across different acts.",
  "time_of_day": "Acts 1-2 late afternoon to night; act 3 night; act 4 storm night; acts 5-6 next morning to dusk.",
  "locations": "Reuse 3-5 primary locations maximum so the audience learns the geography. Group 3-6 consecutive scenes in the same dramatic situation before changing location, and bridge every location change with a line, a visual transition or a travel beat.",
  "identity": "Reference images define faces. Every character in a scene must carry a cast-sheet position and a visible identity anchor: name, position number, stable descriptor and wardrobe. Never describe age, eye color or base hair color in prompts; describe only transient state (hair style, wet hair, flush, sweat, expression, wardrobe)."
}

- Write "continuity" in PRESENT tense only: current wardrobe, current props, current state of mind or body. NO spoilers.
- NEVER mention a future scene, act or event (no "returns in scene 40", "pays off later", "is revealed in act 5", "it is planted now"). The clip for this scene must not hint at scenes the viewer has not seen.

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
      "first_frame_prompt": "Cinematic still of Nora Hale (the character in reference_nora.png), wide establishing shot, at the Hale lighthouse cliff edge, storm dusk. Nora strides along the cliff edge, coat snapping in the wind, jaw set, eyes bright with contained anger. Wardrobe: charcoal wool coat over a dark sweater, dark jeans, rain-wet hair. Keep Nora Hale's face and wardrobe identical to reference_nora.png. Framing keeps the face unobstructed and centered for a 9:16 crop. 45-80 words, no style suffix (it is appended automatically), no text or logos.",
      "key_object": "brass key",
      "object_focus": "",
      "present_silent": ["cole"],
      "object_start": {"name": "brass key", "visible": "in Nora's fist, in frame from the first second"},
      "object_end": {"name": "brass key", "visible": "held up into the headlights, in frame at the end"},
      "object_hidden": false,
      "diegetic_text": [],
      "internal_cuts": [
        {"at": 0.0, "range": "00s-05s", "framing": "wide establishing shot, two-shot", "action": "Nora strides along the cliff edge with Cole behind her, the lighthouse dark, salt wind whipping her coat; both are on camera and facing each other as they speak.", "dialogue": true},
        {"at": 5.0, "range": "05s-07s", "framing": "close-up", "action": "Nora's hand closes around a brass key in her pocket; her jaw tightens.", "dialogue": false},
        {"at": 7.0, "range": "07s-10s", "framing": "tight close-up", "action": "Headlights sweep across the brass key as she raises it; she turns toward the road.", "dialogue": false}
      ],
      "dialogue": [
        {"speaker": "NORA", "line": "They said the lighthouse was empty for ten years.", "delivery": "cold, quiet", "shot": 0, "recipient": "COLE"},
        {"speaker": "COLE", "line": "So who left the light on?", "delivery": "low, suspicious", "shot": 0, "recipient": "NORA"}
      ],
      "sfx_ambience": "wind, distant surf, a gull, wet gravel underfoot",
      "continuity": "Act 1 wardrobe. She is holding the brass key; salt wind, wet gravel, cold hands. Present state only.",
      "because_previous_ended_with": "The episode opens cold; there is no prior beat.",
      "this_scene_starts_with": "Nora strides along the cliff edge, the brass key already closed in her fist.",
      "single_change_at_end": "Headlights find Nora on the cliff road, and she turns toward whoever is coming.",
      "block_driving_question": "Why did the lighthouse light turn on after ten years?"
    }
  ],
  "narrative_continuity": {
    "engine": "narrative_continuity_engine",
    "minute_blocks": [
      {"block": 1, "scenes": [1, 2, 3, 4, 5, 6], "driving_question": "Why did the lighthouse light turn on after ten years?"}
    ]
  },
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
- "internal_cuts": 1 to 4 items. Shot 1 is at 0.0 and starts in motion from the exact storyboard panel; the rest follow in chronological order with contiguous time ranges ("00s-06s", "06s-08s", ...). Each cut sets "dialogue": true when it carries a line and false when it is a silent insert/reaction/object shot. Silent shots never contain speech quotes or "says/whispers/tells".
- SPEAKER-SHOT LOCK: when exactly two different characters speak, Shot 1 is a two-shot holding both lines; otherwise each line is assigned to its own cut where the speaker is on camera, face and mouth visible, looking at the recipient. Never place dialogue on a hand insert, an object insert, a reaction-only shot or a shot from behind the speaker.
- "dialogue[].shot" is the 0-based index of the "internal_cuts" item that carries the line, and "dialogue[].recipient" names the person the line is spoken to (never the speaker).
- Silent shots come after the dialogue except a revelation insert, which gets its own centered silent shot of 2-3 s between spoken shots.
- "present_silent": characters present who do not speak in this scene (mouths closed the whole scene). Never list a speaker there.
- "key_object": the canonical name of the scene's story object, used in the panel, Shot 1 and the object shots. For a planting scene set "object_focus": "plant", "planted_object" (what is hidden), "planted_in" (the container, never a frame/view phrase) and "planted_by"; for a reveal set "object_focus": "reveal". "object_hidden": true when a container appears whose interior must never be shown.
- "diegetic_text": [] by default. Only when the plot REQUIRES the object itself to carry a legible word (e.g. "CONFESSION") list the exact uppercase word(s); the image prompt will allow exactly that text and nothing else.
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

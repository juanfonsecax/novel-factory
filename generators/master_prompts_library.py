#!/usr/bin/env python3
"""novel_factory master template library.

Contains the system's four complete, unabridged master prompts:

  PROMPT 000 — Viral story architect (China / USA micro-drama).
  PROMPT 001 — Cinematic storyboard generator (6 panels per image).
  PROMPT 002 — Master character sheet generator (single image).
  PROMPT 003 — Script + camera + sound + Muse AI command generator.

The placeholders the system fills automatically are exactly:

  {story_idea}          Base idea / narrative architecture for the project.
  {duration_minutes}    Total episode runtime in minutes.
  {total_scenes}        Total number of scenes in the project.
  {total_grid_images}   Number of 1-minute blocks (6 scenes each).
  {visual_style}        Locked visual look for the project.
  {aspect_ratio}        Master aspect ratio (16:9 by default).

Filling uses literal token replacement (not str.format), so braces in prompt
examples are never broken.
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

import nf_core as nf  # noqa: E402

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

NARRATIVE_CONTINUITY_RULE = """NARRATIVE CONTINUITY RULE (Single Through-Line + Cause-and-Effect Chain + Carried-State Ledger + Location Ping-Pong Ban + One Name per Key Object + Scramble Test + ReelShort/DramaBox Bridges and Pacing):
1. ONE DRIVING QUESTION PER 6-SCENE BLOCK: each minute has a single dramatic question; no scene opens a new question.
2. MANDATORY CAUSE-AND-EFFECT CHAIN: from scene 2 to the last scene, every scene declares `because_previous_ended_with` (literal copy of the previous scene's final change), `this_scene_starts_with` (concrete action already in motion that continues that consequence) and `single_change_at_end` (one irreversible state change).
3. ENTRY AND EXIT BRIDGES (OPENING AND CLOSING): every scene declares `entry_bridge` (micro-action or line <= 2 s that starts it because of the previous scene) and `exit_hook` (gesture, order, decision or question that ends it and pushes into the next one). exit_hook(N) feeds entry_bridge(N+1).
4. BLOCK PACING RULE (6 SCENES): 6 confrontation peaks in a row are FORBIDDEN. At least 1 non-confrontational beat per block (solo decision, discovery, plan, tender/vulnerable moment).
5. CLIFFHANGER ROTATION: rotate the type between blocks (identity -> emotion -> revelation). Repeating the same type in two consecutive blocks is forbidden.
6. LOCATION PING-PONG IS FORBIDDEN: group 3 to 5 consecutive scenes in the same location; the A-B-A pattern is forbidden.
7. ONE NAME PER KEY OBJECT: the same exact `key_object` appears in the storyboard panel, in the Shot 1 action and in the Key Object list; never use aliases.
8. SCRAMBLE TEST: if scrambling the block breaks the chain of consequences, rewrite it. The validator rejects mechanical placeholders and cuts without transitions.
"""


# ---------------------------------------------------------------------------
# PROMPT 00B — Proven source-story beat extractor (ReelShort/DramaBox)
# ---------------------------------------------------------------------------
PROMPT_00B_SOURCE_BEAT_EXTRACTOR = """🔍 PROMPT 00B — SOURCE-STORY BEAT AND BRIDGE EXTRACTOR (REELSHORT / DRAMABOX METHOD)
Act as an analytical Showrunner and Script Doctor specializing in high-retention micro-dramas (ReelShort, DramaBox).

GOAL:
Analyze the attached PROVEN SOURCE SCRIPT (or a viral-story transcript) and extract ONLY the dramatic skeleton and scene-by-scene bridges for every 10-second scene in the project, grouped into 1-minute blocks (6 scenes per block).

GOLDEN RULE (STRICT PROHIBITION):
COPYING DIALOGUE, NAMES, BRANDS OR ANY LITERAL TEXT FROM THE ORIGINAL IS COMPLETELY FORBIDDEN.
Extract only dramatic functions, power dynamics, turns, emotions and causal bridges. The full surface will be reinvented in idiomatic English in the next step.

FOR EACH SCENE EXTRACT:
1. scene_id: scene number (1 to the total declared by the project).
2. block: the 1-minute block it belongs to (1 to the total project blocks).
3. beat_function: one of the 6 key functions:
   - "hook" (grabs attention in the first 3-5 s)
   - "setup-stakes" (establishes what can be won or lost)
   - "reversal" (turn or power shift)
   - "escalation" (rising tension or conflict)
   - "crisis" (dilemma or critical moment)
   - "cliffhanger" (cut at the peak before the answer)
4. core_turn: what exactly changes in this scene (information revealed, power balance altered or irreversible state).
5. emotion: dominant emotional trajectory (anger -> surprise -> curiosity -> hope -> fear -> relief).
6. entry_bridge: the micro-action or line (max ~2 s) that starts the scene as a direct result of the previous one (an order being executed, someone chasing another, etc.). Never start "at the peak" without a bridge.
7. exit_hook: the gesture, order, decision or question that ends the scene and pushes into the next one.
8. non_confrontational: true/false. PACING RULE: every 6-scene block must have at least 1 NON-confrontational beat (solo decision, discovery, plan, tender/vulnerable moment).

SOURCE SCRIPT / SUMMARY:
{source_script}
"""


# ---------------------------------------------------------------------------
# PROMPT 000 — literal requested text (do not modify)
# ---------------------------------------------------------------------------
PROMPT_000_VIRAL_STORY_ARCHITECT = """🧠 PROMPT 000 — VIRAL STORY ARCHITECT (CHINA / USA MICRO-DRAMA SHOWRUNNER)
Act as a Showrunner with deep expertise in viral micro-dramas from the United States and China (ReelShort, DramaBox and AI-novel channels with 500,000+ views).

Your goal is to turn my base idea into a HIGH-RETENTION STORY built for the ENGLISH-language market (high RPM), mathematically structured for a runtime of {duration_minutes} minute(s) ({total_scenes} ten-second scenes, split into {total_grid_images} one-minute blocks / 6 scenes each).

BASE IDEA / SEED:
{story_idea}

GOLDEN DRAMATURGY AND RETENTION RULES YOU MUST APPLY:
1. EXPLOSIVE HOOK IN THE FIRST 10 SECONDS (SCENE 1): The story must never start slowly. Open in the middle of maximum tension: a public humiliation, a discovered betrayal, a millionaire secret, an extreme social-class gap or an unexpected contract.
2. MICRO-TURNS EVERY 30 SECONDS (EVERY 3 SCENES): Every 3 scenes there must be a revelation, an emotional conflict, a forbidden glance, a confrontation or an obstacle that prevents the viewer from closing the video.
3. CLIFFHANGER AT THE END OF EVERY MINUTE (SCENES 6, 12, 18...): The last scene of every 6-scene block must end at maximum dramatic tension.
4. CHARACTERS WITH IMMEDIATE VISUAL CONTRAST (MAXIMUM 3 TO 5 MAIN CHARACTERS): Design characters whose social status and personality are understood in 1 second through wardrobe alone (e.g. arrogant billionaire vs. humble worker with iron dignity; secret heiress vs. elitist villain).
5. LOCATION ECONOMY (MAXIMUM 3 TO 5 LOCATIONS): Concentrate the action in visually rich, contrasting locations to preserve perfect continuity. Group 3 to 6 consecutive scenes in the same dramatic situation before changing location.
6. STRICT CAUSALITY AND CHRONOLOGICAL ORDER: Every scene must be a consequence of the previous one and the cause of the next. Never show a consequence before its cause, reveal the same clue twice or teleport characters without a visible or spoken transition. Every act ends on a decision that forces the next one.
7. CATALOG OF 6 PROVEN VIRAL STRUCTURES (LATAM → USA, 500,000+ VIEWS): Use this catalog as a structure bank. Choose ONE as the story's backbone and adapt it to the US market in English. Do not copy names, brands or dialogue: preserve the emotional mechanics and beat order.
<<<VIRAL_TEMPLATES>>>

DELIVER THE RESULT IN THIS EXACT FORMAT (READY TO PASTE INTO PROMPT 001):
1. VIRAL TITLE IN ENGLISH (3 high-CTR options).
2. MAIN CAST (3 to 5 characters: Name, Age, Exact Physical Appearance, Fixed Signature Wardrobe and Voice Timbre in English).
3. INTENSE BLOCK-BY-BLOCK NARRATIVE SYNOPSIS (1 paragraph per story minute = 6 scenes per minute, describing opening, conflict, turns and outcome/cliffhanger)."""


# ---------------------------------------------------------------------------
# PROMPT 001 — cinematic storyboard generator (6 scenes per image)
# ---------------------------------------------------------------------------
PROMPT_001_STORYBOARD_GENERATOR = """🎬 PROMPT 001 — CINEMATIC STORYBOARD GENERATOR (6 SCENES PER IMAGE)
Act as a film director and create a visual storyboard for the story I am going to give you.

STORY DATA
Story:
{story_idea}

Runtime:
{duration_minutes} minute(s) ({total_scenes} ten-second scenes = {total_grid_images} storyboard image(s) with 6 panels each)

Visual style:
{visual_style}
(Options: Realistic cinematic 35mm / Realistic / 3D animation / 2D animation / Anime / Illustration)

STORYBOARD RULES
Every scene lasts exactly 10 seconds.
Automatically calculate the number of scenes from the runtime.
Every image must contain 6 scenes/panels (in a clean 3x2 grid: 6 panels numbered 1 to 6).
Therefore:
1 minute = 6 scenes = 1 image
2 minutes = 12 scenes = 2 images
3 minutes = 18 scenes = 3 images
4 minutes = 24 scenes = 4 images
5 minutes = 30 scenes = 5 images
{duration_minutes} minutes = {total_scenes} scenes = {total_grid_images} images
Every image represents exactly 1 minute of story.

EVERY PANEL
Every panel must visually show the corresponding story moment with professional cinematic framing (alternating establishing wide shots, dramatic medium shots and emotional close-ups).
Every panel is the literal FIRST FRAME of Shot 1 in its scene: same framing, same camera position, same blocking, same wardrobe, same lighting and same key object. Shot 1 starts in motion from that image; it is never a frozen frame.
It must include:
- Every character present in the scene, in their fixed Cast Sheet position.
- Location.
- Clear physical action already in motion.
- Intense emotion on the faces.
- The scene's key object visible or clearly implied.
- Cinematic composition and lighting.
100% VISUAL PANEL FORMAT (NO TEXT BOXES): The 6 photographic panels in a 3x2 grid must fill 100% of the 16:9 canvas, separated only by thin divider lines. Place ONLY the small number [1], [2], [3], [4], [5], [6] in the top-left corner of each panel. Drawing dark bottom bars, subtitles, text boxes or written descriptions inside the image is FORBIDDEN.

IMPORTANT:
Do not write dialogue or paragraphs inside the storyboard.

CONTINUITY
Keep the exact same character appearance throughout the storyboard.
Also preserve strict continuity of:
- Faces.
- Hair.
- Age.
- Build.
- Wardrobe.
- Locations.
- Period.
- Important objects (rings, contracts, vehicles, tools).
- Lighting.
- Atmosphere.
If a character changes clothes for narrative reasons, the change must be coherent.

VISUAL STYLE
Use exactly the selected visual style ({visual_style}).
Keep that style consistent across every image and every panel.
The storyboard must look professional and cinematic.

IMPORTANT
The result must be primarily visual.
Do not include:
- Dialogue.
- Extended narration.
- Subtitles.
- Paragraphs.
- Video prompts.
- Process explanations.
- Written descriptions, text boxes or bottom bars inside the image.

FINAL RESULT
From the provided story, runtime and style:
1. Calculate the total number of scenes ({total_scenes} scenes).
2. Every scene must last 10 seconds.
3. Divide the scenes into groups of 6.
4. Generate one image per group of 6 scenes.
5. Every image must contain 6 clearly divided panels.
6. Keep the numbering [1]-[6] in the top-left corner, with no additional text.
7. Preserve absolute continuity of characters and locations.
8. Tell the entire story visually from beginning to end."""


# ---------------------------------------------------------------------------
# PROMPT 002 — master character sheet in a single image
# ---------------------------------------------------------------------------
PROMPT_002_CHARACTER_SHEET_GENERATOR = """👤 PROMPT 002 — CHARACTER GENERATOR (MASTER SHEET IN A SINGLE IMAGE)
Act as a casting director and character designer.
We have already created the story's storyboard.
Now analyze that storyboard and identify the relevant main and secondary characters who appear in the story.
Your task is to generate A SINGLE IMAGE showing all identified characters together.

REFERENCE
Storyboard: the complete storyboard created in the previous step. The sheet must preserve exactly the faces, ages, ethnicities, wardrobes and accessories that appear in that storyboard.

MAIN RULE
Characters must be based directly on the storyboard.
You must preserve exactly their:
- Sex.
- Approximate age.
- Ethnicity and physical features.
- Face.
- Hair.
- Skin tone.
- Build.
- Main wardrobe.
- Important accessories.
- Visual style ({visual_style}).

If the storyboard has 2 characters, show all 2 in a single image.
If it has 3 characters, show all 3 in a single image.
If it has 4 characters, show all 4 in a single image.
And so on (prioritizing the 3 to 5 main characters of the plot).
Do not invent characters who are not relevant to the story.

IMAGE COMPOSITION
Generate a clean, professional character reference sheet.
All characters must appear:
- In a single image.
- Side by side.
- Clearly separated.
- Full body.
- Standing.
- Facing the camera.
- In a natural, neutral pose.
- Not covering each other.
- Not physically interacting with each other.
Each character's face and full body must be clearly visible.
Use a simple, neutral background (clean studio gray) so the characters are the protagonists of the image.

CONSISTENCY
This image will serve as the official character reference for subsequent image and video generations in Muse AI and Google Flow.
Therefore, faces and physical features must match the characters shown in the storyboard as closely as possible.
Do not redesign the characters.
The goal is to extract a clear, consistent visual reference for each character from the storyboard.

VISUAL STYLE
Use exactly the same visual style used in the storyboard ({visual_style}).
Do not change the story's visual style.

WARDROBE
Use each character's most representative or main wardrobe within the story.
Wardrobe must immediately help identify who each character is.

TEXT
Arrange the characters from left to right and place only the following below each one:
Position #N — CHARACTER NAME IN UPPERCASE
Example:
Position #1 (Far Left) — ELENA
Position #2 — SAM
Position #3 — MARGARET
Position #4 (Far Right) — ADRIAN
Every character always keeps the same position, the same face and the same wardrobe on the sheet and in every scene.
Do not include:
- Long descriptions.
- Dialogue.
- Biographies.
- Paragraphs.
- Scene information.
Text must be minimal to keep the image clean.

FINAL RESULT
Generate A SINGLE IMAGE containing all relevant characters in the story.
The image must work as a master character reference sheet that can later be used to keep the same character appearance across every scene and video.
Deliver only the character image."""


# ---------------------------------------------------------------------------
# PROMPT 003 — cinematic script + camera + sound + Muse AI command
# ---------------------------------------------------------------------------
PROMPT_003_SCRIPT_CAMERA_SOUND_GENERATOR = """🎬 PROMPT 003 — ENGLISH CINEMATIC SCRIPT GENERATOR + CAMERA CUTS + SOUND (OPTIMIZED FOR MUSE AI AND GOOGLE FLOW)
Act as a Hollywood screenwriter, cinematographer and sound designer.
We have already created the story's storyboard and the master character sheet. Now convert that storyboard into a complete cinematic, technical text script, respecting exactly the scenes shown in the storyboard, with all spoken dialogue in ENGLISH for international monetization.

PROJECT DATA
Storyboard:
The complete storyboard created in step 1: {total_grid_images} images with 6 panels, one per minute. Every scene must match its panel exactly.
Block runtime:
1 minute = 6 ten-second scenes (or the total number of scenes in the attached storyboard).

MAIN RULE
Every scene lasts exactly 10 seconds.
You must keep exactly the same number and order of scenes as the storyboard.
You must NOT add or remove scenes.
Every scene must correspond directly to its storyboard panel.

ENGLISH DIALOGUE (HARD RULE: MAXIMUM 15 WORDS PER SCENE)
All spoken dialogue must be in natural, dramatic, emotional ENGLISH.
- Maximum 15 words per scene and maximum 15 per turn.
- The voice must finish before 8.5 seconds; leave the rest for pauses, glances and reactions.
- Never cut a sentence for time: if an idea needs more, split it across scenes.
- Not every scene needs dialogue: use "No dialogue (Pure visual & sound tension)." when the image speaks better.

CAMERA DIRECTION: BETWEEN 1 AND 4 SHOTS PER 10s SCENE, BORN FROM THE DIALOGUE
1. GOLDEN RULE: ONE LINE = ONE SHOT OF THE SPEAKER:
   - Whoever speaks is ON CAMERA with face and mouth visible throughout their line, looking at the recipient. Putting dialogue over an insert, a reaction or someone's back is forbidden.
   - Shot 1: starts IN MOTION from the panel's exact frame. Same framing, same camera position, same blocking, same wardrobe, same lighting and same key object. Opening on a static frame is forbidden. If there are two speakers, Shot 1 is a two-shot showing both and holding their two lines.
   - Silent shots (insert, reaction, object detail) come AFTER the dialogue ends. Exception: the discovery/revelation goes in its own centered 2–3 second silent shot; declare at which second the dialogue ends ("Dialogue ends at second X").
   - Present characters who do not speak are listed as silent: once, with their mouth closed.
2. KEY OBJECT AND ON-SCREEN TEXT:
   - Every scene declares OBJECT AT START and OBJECT AT END visible on camera; the object insert shows it exactly as it is.
   - Never show the empty interior of a bag, safe or container where the object was hidden.
   - Only declared diegetic text (e.g. the word CONFESSION on the document) may be legible; all other papers and signs show no words.
3. IDENTITY AND POSITIONS:
   - Every present character is named as Name (Cast Sheet Pos #N: stable descriptor, wearing act wardrobe).
   - The Cast Sheet fixes positions from left to right; never insert that sheet as a shot between scenes.
3. SOUND DESIGN (SFX & AMBIENCE) AND VOICE:
   - Specify the speaker's constant voice timbre (e.g. "Warm emotional young female voice" / "Deep authoritative male baritone voice").
   - Specify realistic environmental sound effects (e.g. "Rain on window, footsteps on gravel, tense dramatic silence").
4. CAUSALITY AND LOCATION:
   - Every scene is a consequence of the previous one and the cause of the next. Revealing a consequence before its cause or repeating the same clue is forbidden.
   - Group 3 to 6 consecutive scenes in the same dramatic situation before changing location. Every location change needs a visible or spoken transition.

MANDATORY STRUCTURE FOR EVERY SCENE
Use exactly this structure for every scene:

SCENE [N] (Storyboard Panel #[N]) — [MM:SS–MM:SS]
- Location: [Exact location from the panel]
- Characters Present: [Name (Cast Sheet Pos #N), ...]
- Storyboard Panel (Shot 1 exact framing): [ panel framing + action + key object + everyone present ]
- Identity Anchors: [Name (Cast Sheet Pos #N: descriptor, wearing wardrobe), ...]
- Object In / Object Out: [OBJECT AT START visible → OBJECT AT END visible]
- Camera Cuts & Visual Action (10s, 1–4 shots):
  * [00s–..]: [Shot 1: exact panel framing + action already in motion; two-shot if two characters speak]
  * [..s–..s]: [SPEAKING SHOT: name (visible, looking at recipient) says exactly, only once: "line"] (one shot per spoken line)
  * [..s–..s]: [NO DIALOGUE: insert, reaction or object shot; the discovery is centered for 2–3 s]
- Silent: [PRESENT CHARACTERS WHO DO NOT SPEAK: name — mouth closed throughout the scene]
- Sound Design (SFX & Voice Tone): [Environmental sound effects + the character's fixed voice tone]
- Dialogue (English, max 15 words per line, finish before 8.5 s):
  [CHARACTER NAME]: "[Brief, concrete, complete English dialogue, max. 15 words]"

FINAL RESULT
Deliver only the scene block using the structure above and, at the end of the scenes, include this exact command ready to copy and paste together with the script into MUSE AI:

FINAL COMMAND TO PASTE INTO MUSE AI (TOGETHER WITH THE ATTACHED STORYBOARD AND CHARACTER SHEET):
"Make a realistic cinematic video of 10 seconds per scene, executing between 1 and 4 shots exactly as the script lists them (Shot 1 starts directly in motion from the exact framing of the corresponding storyboard panel without static frames; every spoken line gets its own shot with the speaker facing camera, face and mouth visible, never from behind the character; silent shots of inserts, reactions or objects come after the dialogue and never contain speech), keeping strictly the same race, face and wardrobe for each character according to their position in the attached Character Sheet, and join them into a single continuous video, never inserting the reference image between scenes. Format: {aspect_ratio}. Strict negative rules: no subtitles, no captions, no overlay text, no watermark, no background music, no groans or mouth noises before dialogue.\""""


TEMPLATES: Dict[str, Dict[str, str]] = {
    "prompt_000": {
        "key": "prompt_000",
        "code": "PROMPT 000",
        "signature": "PROMPT_000_VIRAL_STORY_ARCHITECT",
        "title": "Viral Story Architect (China / USA Micro-Drama)",
        "purpose": "Turns the base idea into a high-retention architecture with cast, locations and a block-by-block synopsis.",
        "text": PROMPT_000_VIRAL_STORY_ARCHITECT,
    },
    "prompt_001": {
        "key": "prompt_001",
        "code": "PROMPT 001",
        "signature": "PROMPT_001_STORYBOARD_GENERATOR",
        "title": "Cinematic Storyboard Generator (6 Scenes per Image)",
        "purpose": "Creates a visual storyboard in 6-panel grids (3x2), one image per minute of story.",
        "text": PROMPT_001_STORYBOARD_GENERATOR,
    },
    "prompt_002": {
        "key": "prompt_002",
        "code": "PROMPT 002",
        "signature": "PROMPT_002_CHARACTER_SHEET_GENERATOR",
        "title": "Master Character Sheet Generator (Single Image)",
        "purpose": "Extracts from the storyboard a master sheet with all relevant characters and their main wardrobe.",
        "text": PROMPT_002_CHARACTER_SHEET_GENERATOR,
    },
    "prompt_003": {
        "key": "prompt_003",
        "code": "PROMPT 003",
        "signature": "PROMPT_003_SCRIPT_CAMERA_SOUND_GENERATOR",
        "title": "Script + Camera + Sound + Muse AI Command Generator",
        "purpose": "Turns the storyboard into 10-second scenes with internal cuts, SFX, English dialogue and a final Muse AI command.",
        "text": PROMPT_003_SCRIPT_CAMERA_SOUND_GENERATOR,
    },
}


# ---------------------------------------------------------------------------
# Project values
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
    return idea or "(describe the base idea here: who wants what, who blocks them and what secret drives the story)"


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

    fallback_scenes = nf.scene_count_for_target(nf.DEFAULT_TARGET_MINUTES)
    total_scenes_raw = overrides.get("total_scenes") or episode.get("total_scenes") or len(scenes) or fallback_scenes
    try:
        total_scenes = int(total_scenes_raw)
    except (TypeError, ValueError):
        total_scenes = fallback_scenes
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
# Rendering and export
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
    valid = ", ".join(str(item.get("id") or "") for item in templates) or "(none)"
    raise KeyError(f"Unknown viral template: {template_id}. Valid: {valid}")


def render_viral_niche_block(template: Dict[str, Any]) -> str:
    template = template if isinstance(template, dict) else {}

    def text(key: str) -> str:
        return str(template.get(key) or "").strip()

    def bullets(key: str) -> List[str]:
        return [str(value).strip() for value in (template.get(key) or []) if str(value).strip()]

    lines: List[str] = [
        "USA MEGA-NICHE ARCHETYPE — USER SELECTION",
        "",
        f"- ID: {text('id')}",
        f"- Archetype: {text('label')}",
        f"- Category: {text('category')}",
        f"- Niche description (source): {text('description')}",
    ]
    audience = text("audience")
    if audience:
        lines.append(f"- Audience: {audience}")
    lines += [
        "",
        "ENGLISH SEED (US MARKET, en-US):",
        f"- Premise seed: {text('premise_seed')}",
        f"- Opening hook: {text('opening_hook')}",
        "",
        "MANDATORY BEATS:",
    ]
    lines += [f"- {item}" for item in bullets("must_include")] or ["- (no beats defined)"]
    lines += ["", "PRIMARY LOCATIONS:"]
    lines += [f"- {item}" for item in bullets("primary_locations")] or ["- (no locations defined)"]
    lines += ["", f"VISUAL SIGNATURE: {text('visual_signature')}"]
    series_hook = text("series_hook")
    if series_hook:
        lines.append(f"SERIES HOOK: {series_hook}")
    lines += [
        "",
        "ARCHETYPE USAGE RULES:",
        "- Use this archetype as the story's only engine; do not mix niches or plots from other archetypes.",
        "- Write titles, cast and synopsis in native US English (en-US).",
        "- Keep 3 to 5 main characters and 3 to 5 locations.",
        "- Preserve the runtime and scene count declared by the project, with a cliffhanger at the end of every minute.",
        "- The English seed is the canonical material; this selection overrides the base idea.",
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
        return ("(Catalog unavailable: use a LATAM -> USA micro-drama structure with "
                "a public hook, family secret and status reversal.)")
    lines: List[str] = []
    for index, item in enumerate(items, start=1):
        beats = " -> ".join(str(beat).strip() for beat in (item.get("structure") or []) if str(beat).strip())
        lines.extend([
            f"{index}. {item.get('name') or item.get('id')} (`{item.get('id')}`)",
            f"   Inspiration: {item.get('source') or 'LATAM viral'} · {item.get('views') or '+500K'} views · "
            f"{item.get('genre') or 'micro-drama'}.",
            f"   Premise: {item.get('premise') or ''}",
            f"   Hook: {item.get('hook') or ''}",
            f"   Beats: {beats}",
            f"   USA adaptation: {item.get('usa_adaptation') or ''}",
        ])
    return "\n".join(lines).strip()


def render_prompt(key: str, values: Dict[str, Any], niche: str = "") -> str:
    template = TEMPLATES.get(str(key))
    if not template:
        raise KeyError(f"Unknown template: {key}. Use: {', '.join(PROMPT_ORDER)}")
    text = template["text"]
    for placeholder in PLACEHOLDERS:
        token = "{" + placeholder + "}"
        text = text.replace(token, str(values.get(placeholder, token)))
    if str(key) == "prompt_000" and VIRAL_TEMPLATES_TOKEN in text:
        text = text.replace(VIRAL_TEMPLATES_TOKEN, render_viral_latam_block())
    if str(key) == "prompt_000" and str(niche or "").strip():
        selected = get_viral_template(niche)
        text = text.rstrip() + "\n\n" + render_viral_niche_block(selected)
    if str(key) in ("prompt_000", "prompt_001", "prompt_003"):
        text = text.rstrip() + "\n\n" + NARRATIVE_CONTINUITY_RULE
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
            "source_mode": master.get("source_mode", "proven_adaptation"),
        },
        "source_mode": master.get("source_mode", "proven_adaptation"),
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
        f"# MASTER PROMPTS — {project.get('title') or project.get('slug') or 'Episode'}",
        "",
        f"- Generated: {pack.get('generated_at')}",
        f"- Runtime: {values.get('duration_minutes')} minute(s)",
        f"- Scenes: {values.get('total_scenes')}",
        f"- 1-minute grids: {values.get('total_grid_images')}",
        f"- Aspect ratio: {values.get('aspect_ratio')}",
        f"- Visual style: {values.get('visual_style')}",
        "",
        "> All prompts are filled with the project data. Copy each complete block.",
    ]
    if pack.get("source_mode") == "original_unproven":
        lines += [
            "> ⚠️ **WARNING: source_mode is 'original_unproven' — script generated without a proven source.**",
        ]
    lines += [""]
    for prompt in pack.get("prompts") or []:
        lines += [
            "---",
            "",
            f"## {prompt['code']} — {prompt['title']}",
            "",
            f"_{prompt['purpose']}_",
            "",
            f"**{prompt['chars']:,} characters · {prompt['words']:,} words**",
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
        f"NOVEL FACTORY — MASTER PROMPTS — {project.get('title') or project.get('slug') or 'Episode'}",
        "=" * 78,
        f"Generated: {pack.get('generated_at')}",
        f"Runtime: {values.get('duration_minutes')} minute(s) · Scenes: {values.get('total_scenes')} · "
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
            str(prompt["text"]).rstrip(),
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
# 1-minute batches for Muse AI (6 scenes per block)
# ---------------------------------------------------------------------------
MUSE_FINAL_COMMAND_HEADER = (
    "FINAL COMMANDS TO PASTE INTO MUSE AI (CHOOSE BY CHANNEL):"
)
MUSE_FINAL_COMMAND_TEMPLATE = (
    "Make a realistic cinematic video of 10 seconds per scene, executing between 1 and 4 shots "
    "exactly as the script lists them: Shot 1 starts directly in motion from the exact framing of "
    "the corresponding storyboard panel, with no static frames (two-shot if two characters speak); "
    "every spoken line gets its own shot with the speaker facing camera, face and mouth visible, "
    "never from behind the character; silent shots (inserts, reactions, objects) come after the "
    "dialogue and never contain speech. Keep strictly the same race, face and wardrobe for each "
    "character according to their position in the attached Character Sheet, and join them into a "
    "single continuous video, never inserting the reference image between scenes. "
    "Format: {orientation} {aspect_ratio} {destination}. "
    "Strict negative rules: no subtitles, no captions, no overlay text, no watermark, "
    "no background music, no groans or mouth noises before dialogue."
)
MUSE_FINAL_COMMAND = MUSE_FINAL_COMMAND_TEMPLATE
MUSE_ATTACH_LINE = (
    "📎 ATTACH IN MUSE AI: REF_CAST_MASTER.png (Character Sheet) + "
    "REF_GRID_MIN_{batch:02d}.png (Minute {minute} Storyboard: Scenes {first}–{last})"
)


def _muse_final_command(batch_number: int, orientation: str, aspect: str, destination: str = "") -> str:
    return MUSE_FINAL_COMMAND_TEMPLATE.format(
        orientation=orientation,
        aspect_ratio=aspect,
        destination=destination.strip(),
    )


ROLE_LABELS = {
    "protagonist": "Protagonist",
    "love_interest": "Love interest",
    "antagonist": "Antagonist",
    "antagonist_heir": "Antagonist heir",
    "ally": "Ally",
    "mentor": "Mentor",
    "supporting": "Supporting",
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
    return "adult"


def _character_visual(character: Dict[str, Any]) -> str:
    visual = str(
        character.get("visual_reference")
        or character.get("description")
        or character.get("appearance")
        or ""
    ).strip()
    return visual or "features and build defined by the casting sheet"


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
    return "the main wardrobe described in the casting sheet"


def build_cast_sheet_prompt(master: Optional[Dict[str, Any]]) -> str:
    """Copy-ready prompt for REF_CAST_MASTER.png, with no attachments or brackets."""
    characters = project_characters(master)
    lines = [
        "Act as a casting director and character designer. Generate A SINGLE horizontal 16:9 IMAGE "
        "showing together, full body, standing, facing forward on a neutral studio gray "
        "background (#808080) and not touching each other, the following characters from our novel in "
        "Realistic Cinematic 35mm style:",
        "",
    ]
    for index, character in enumerate(characters, start=1):
        name = str(character.get("name") or character.get("id") or "CHARACTER").strip().upper()
        edge = " (Far Left)" if index == 1 else (" (Far Right)" if index == len(characters) else "")
        lines.append(
            f"Position #{index}{edge} — {name}. Role: {_character_role(character)}. "
            f"Age: {_character_age(character)}. "
            f"Physical features: {_character_visual(character)}. "
            f"Fixed wardrobe: {_character_wardrobe(character)}."
        )
    if not characters:
        lines.append(
            "1. THE PROJECT'S MAIN CHARACTERS — use exactly the names, roles, "
            "ages and wardrobes defined in story_brief.md and master_episode.json."
        )
    lines += [
        "",
        "Arrange the characters from left to right and place only the following below each one: "
        "'Position #N — NAME IN UPPERCASE'. Keep exactly the same positions, faces, "
        "hairstyles and wardrobes in every storyboard image and Muse AI batch. "
        "No additional text, no titles, no sentences, no logos, no watermarks; only the "
        "character image and their positions.",
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

    for raw in scene.get("characters_present") or scene.get("characters") or []:
        add(raw)
    if not names:
        for entry in nf.scene_dialogue_lines(scene):
            add(entry.get("speaker"))
    return names


def _muse_cut_rows(scene: Dict[str, Any]) -> List[Dict[str, str]]:
    import nf_core as nf

    cuts = [c for c in (scene.get("internal_cuts") or []) if isinstance(c, dict)]
    if not cuts:
        return [
            {"range": "00s–03s", "framing": "wide establishing shot",
             "action": "Shot 1 already in motion inside the exact storyboard framing."},
            {"range": "03s–07s", "framing": "close-up",
             "action": "Hard cut to a close-up or over-the-shoulder of the speaking character; lip-sync is clear."},
            {"range": "07s–10s", "framing": "tight close-up",
             "action": "Hard cut to a tight close-up, reaction or insert of the key object as the line lands."},
        ]
    total = float(scene.get("duration_s") or nf.SCENE_SECONDS)
    rows: List[Dict[str, str]] = []
    for idx, cut in enumerate(cuts):
        at = float(cut.get("at") or 0.0)
        end = float(cuts[idx + 1].get("at")) if idx + 1 < len(cuts) else total
        label = str(cut.get("range") or f"{int(at):02d}s–{int(end):02d}s").strip()
        framing = str(cut.get("framing") or "medium shot").strip()
        action = str(cut.get("action") or "").strip() or "the subject continues the motion from the previous beat."
        if cut.get("dialogue"):
            action += "  [SPEAKING SHOT: speaker on camera, face and mouth visible for the whole line.]"
        else:
            action += "  [SILENT SHOT: no dialogue, no speaking, mouths closed.]"
        rows.append({"range": label, "framing": framing, "action": action})
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
    panel = str(scene.get("storyboard_panel") or nf.build_storyboard_panel_description(scene, master)).strip()
    anchors = str(
        scene.get("character_anchors")
        or nf.format_character_anchors(scene, master.get("characters_locked") or master.get("characters") or [])
    ).strip()
    start_object = str((scene.get("object_start") or {}).get("name") or "").strip()
    end_object = str((scene.get("object_end") or {}).get("name") or "").strip()
    key_object = start_object or nf.extract_key_object(scene)
    diegetic = [str(text) for text in (scene.get("diegetic_text") or []) if str(text).strip()]
    silent_names = nf.scene_present_silent_names(scene, master)

    lines: List[str] = [
        f"SCENE {sid} (Storyboard Panel #{sid}) — {_muse_timecode(start)}–{_muse_timecode(end)}",
        f"- Location: {location}",
        f"- Characters Present: {', '.join(characters) if characters else 'the characters visible in the storyboard panel'}",
        f"- Storyboard Panel (Shot 1 exact framing): {panel}",
        f"- Identity Anchors: {anchors or 'use the cast sheet positions exactly as attached'}",
        f"- Key Object: {key_object or 'the central visual detail of the scene'}"
        + (f" → Object In / Object Out: {start_object} → {end_object or start_object}" if start_object else ""),
    ]
    if scene.get("object_hidden"):
        lines.append("- Object Rule: never show the container interior; it stays in shadow and out of frame.")
    if diegetic:
        lines.append(f"- On-Object Text (only legible text allowed in frame): \"{' / '.join(diegetic)}\"")
    if silent_names:
        lines.append(f"- Silent Present: {', '.join(silent_names)} — mouths closed for the whole scene, no lines.")
    lines.append("- Camera Cuts & Visual Action (10s):")
    for row in _muse_cut_rows(scene):
        lines.append(f"  * [{row['range']}]: {row['framing']} — {row['action']}")
    lines.append(f"- Sound Design (SFX & Voice Tone): {sfx}. Voice tone: {voice_text}")
    if dialogue_lines:
        lines.append("- Dialogue (English, max 15 words, finish before 8.5 s):")
        for entry in dialogue_lines:
            speaker = (entry.get("speaker") or "CHARACTER").upper()
            delivery = f" ({entry['delivery']})" if entry.get("delivery") else ""
            lines.append(f'  {speaker}{delivery}: "{entry["line"]}"')
    else:
        lines.append("- Dialogue (English, max 15 words, finish before 8.5 s):")
        lines.append("  No dialogue (Pure visual & sound tension).")
    return "\n".join(lines)


def build_muse_batches(
    master: Dict[str, Any],
    style: Optional[Dict[str, Any]] = None,
    aspect_ratio: str = "",
) -> List[Dict[str, Any]]:
    import nf_core as nf

    style = style if isinstance(style, dict) else {}
    scenes = nf.ordered_scenes(nf.prepare_master_locks_safe(master, style))
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
            batch_number, "horizontal", "16:9", "for YouTube"
        )
        command_916 = _muse_final_command(
            batch_number, "vertical", "9:16", "for Reels, TikTok and Shorts"
        )
        script = "\n\n".join(blocks)
        prompt_169 = "\n\n".join([
            script,
            "FINAL COMMAND (16:9 YouTube):",
            f"\"{command_169}\"",
        ])
        prompt_916 = "\n\n".join([
            script,
            "FINAL COMMAND (9:16 Reels/TikTok/Shorts):",
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
        f"NOVEL FACTORY — MUSE AI — 1-MINUTE BATCHES (6 SCENES) — {title}",
        "=" * 78,
        f"Scenes: {len(nf.ordered_scenes(master))} · Batches: {len(batches)} · 10 s per scene",
        "Each block includes the required attachments and TWO final commands: 16:9 (YouTube) and 9:16 (Reels).",
        "",
    ]
    for batch in batches:
        first = batch["scenes"][0] if batch.get("scenes") else 0
        last = batch["scenes"][-1] if batch.get("scenes") else 0
        lines += [
            "=" * 78,
            f"BLOCK {batch['batch_id']:02d} — MINUTE {batch['minute']:02d} — "
            f"SCENES {first}–{last} — {batch['start_timecode']}–{batch['end_timecode']}",
            "=" * 78,
            "",
            batch["attach"],
            "",
            "=== 16:9 COPY (YouTube) ===",
            batch["prompt_16x9_youtube"],
            "",
            "=== 9:16 COPY (Reels / TikTok / Shorts) ===",
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
    """Quick console render (useful for debugging the library)."""
    import argparse

    parser = argparse.ArgumentParser(description="Render the novel_factory master prompts.")
    parser.add_argument("prompt", nargs="?", default="all", choices=list(PROMPT_ORDER) + ["all"])
    parser.add_argument("--idea", default="", help="Base idea for the {story_idea} placeholder.")
    parser.add_argument("--project", default="", help="Existing project to take data from.")
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

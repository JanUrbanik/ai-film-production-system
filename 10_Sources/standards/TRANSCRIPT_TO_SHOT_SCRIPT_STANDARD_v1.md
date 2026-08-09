---
title: Transcript-to-Shot-Script Conversion Standard
type: knowledge / operating standard
version: 1.0
scope: Converts prose story transcripts into production-ready shot scripts for AI video generation
consumers: story agents, director agents, continuity agents, image-gen agents, video-gen agents
---

# Transcript-to-Shot-Script Conversion Standard

## 1. Purpose

This document defines the single authoritative method for converting a prose
story transcript into a shot-by-shot production script that AI image and video
generators can execute without visual drift.

Any agent that receives a story transcript and is asked to produce a shot list,
storyboard, asset bible, or generation prompts MUST follow this standard.

**Input:** a story transcript in prose, any person, any tense.
**Output:** four artifacts — Asset Bible, Continuity Ledger, Shot Script, Flags.

---

## 2. Core doctrine

Five principles. They override stylistic preference in every case.

### 2.1 The generator is a camera
Describe only what the camera sees and what the microphone hears. Interior
thought, backstory, motive, and narrative irony are invisible to a camera and
must never appear in a generation prompt. If an emotion matters, it must be
rendered as a visible physical fact: a jaw, a hand, a gaze direction, a
posture, a delay before speaking.

- Rejected: "Miranda is heartbroken and remembers everything."
- Accepted: "Miranda sits motionless, eyes fixed on the middle distance, one
  hand flat on the table beside an untouched cup. She does not blink."

### 2.2 Reference IDs never reach the model
Reference IDs (`[CHAR_001]`) are pipeline metadata. Image and video models do
not understand them and will tokenize them as noise, degrading output quality.

Every shot therefore carries **two separate text fields**:
- `REFS:` — machine-readable ID list, consumed by the pipeline to attach the
  correct reference images.
- `GEN_PROMPT:` — clean natural language, zero IDs, zero brackets, zero
  pipeline jargon. This is the only string sent to the generator.

This separation is non-negotiable. A single stray ID inside a GEN_PROMPT is a
defect.

### 2.3 Describe once, cite forever
Full physical descriptions live in the Asset Bible and nowhere else. Shots cite
IDs. Re-describing an asset in every shot guarantees drift, because each
re-description differs slightly from the last.

The one exception is inside `GEN_PROMPT`, which restates the subject in brief
(one clause) so the shot degrades gracefully if reference attachment fails.

### 2.4 Screen appearances, not word mentions
Reference sets are triggered by how often something is **seen**, not how often
it is **written**. A weapon named once but shown across four shots needs a
reference set. A dead relative named five times but never shown needs nothing.

### 2.5 Narration and visuals are separate tracks
The voice-over track and the visual track run in parallel and are not required
to match sentence-for-shot. Visuals must serve the meaning of the narration,
not illustrate its literal words. This decoupling is what allows long-form
runtimes without the result feeling like a slideshow of sentences.

---

## 3. ID scheme

### 3.1 Format
```
[TYPE_NNN]            base asset
[TYPE_NNN/STATE]      variant state of that asset
```
Zero-padded to three digits. Square brackets. One ID per token. Never nested
inside parentheses — nested and unbalanced parentheses break downstream
parsing.

### 3.2 Type prefixes
| Prefix  | Class            | Examples |
|---------|------------------|----------|
| `CHAR_` | Person           | protagonist, Miranda, the waiter |
| `LOC_`  | Location         | the alley, the coffee shop, the apartment |
| `WARD_` | Wardrobe item    | the red dress, his grey work shirt |
| `PROP_` | Object           | the ring, the letter, the coffee cup |
| `VEH_`  | Vehicle          | his sedan, the taxi |
| `ANI_`  | Animal           | the dog |
| `LOOK_` | Visual treatment | LOOK_PRESENT, LOOK_FLASHBACK, LOOK_DREAM |

Wardrobe is deliberately separated from props. Wardrobe binds to a character
state and changes across time; props generally do not. Wardrobe drift is the
most visible continuity failure in AI-generated film, so it is tracked
independently in the ledger.

### 3.3 Variant states — mandatory
A variant state is required whenever an asset **cannot share reference images**
with its base. Triggers:

- **Age or era change** — flashbacks, time jumps, youth versions
- **Major wardrobe change** — a character who changes outfit mid-story
- **Damage or transformation** — clean vs bloodied, intact vs broken
- **Time of day** — for locations
- **Weather** — for exterior locations

```
CHAR_002        Miranda — identity anchor (face structure, build, voice)
CHAR_002/A      present day, 38, shoulder-length dark hair, tired
CHAR_002/B      flashback five years, 33, long hair, animated
LOC_002/DAY     the coffee shop, daylight
LOC_002/DUSK    the coffee shop, evening practicals
PROP_004/CLEAN  the ring, before
PROP_004/BENT   the ring, after
```

The base ID carries identity. The state carries appearance. Failing to define
states is the single most common cause of flashback sequences that look like a
different person.

### 3.4 Aliases
If the transcript refers to the same physical thing under two names ("the
sedan", "his car", "the Volvo"), assign **one** ID and record the aliases in
the Asset Bible entry. Never issue a second ID for the same object.

---

## 4. Reference image rule

### 4.1 Trigger
An asset requires a reference set if **any** of the following is true:

- **(a)** It appears on screen in two or more shots.
- **(b)** It must visually match across a cut.
- **(c)** It carries plot weight even in a single appearance.

An asset that is mentioned in narration but never shown receives **no**
reference set and does not enter the Asset Bible as a visual asset.

### 4.2 Angle sets by asset class

**Characters — 5 images**
1. Front, neutral expression, arms at sides
2. Three-quarter left
3. Full profile
4. Back
5. Tight face plate, neutral expression, flat even light — *this is the identity
   lock and is the highest-value image in the set*

**Props, vehicles, wardrobe — 4 images**
1. Front
2. Three-quarter
3. Side
4. Rear

**Locations — 4 images, plus one per lighting state**
Locations are not photographed in 360°. They are photographed along the axes
you will actually shoot from.
1. Wide establishing
2. The reverse angle
3. Mid shot from the main coverage position
4. Texture / material detail plate

Then repeat image 1 for each lighting state in use (`/DAY`, `/DUSK`, `/NIGHT`,
`/RAIN`).

### 4.3 Reference image prompt rules
Each reference prompt is a standalone generation instruction and must specify:

- Subject, material, and **specific** colour values ("deep crimson", not "red")
- Age, condition, and wear
- Plain neutral mid-grey background
- Even flat lighting, no cast shadows, no rim light
- No props, no other subjects, no text
- Full subject inside frame with margin

Reference images are technical plates, not beauty shots. Dramatic lighting in a
reference image bakes that lighting into every downstream generation.

---

## 5. Shot construction rules

### 5.1 Duration
Maximum **8 seconds** per shot. This matches the generation window of current
video models. If an action requires a second camera position, it is a second
shot. A 60-second narration paragraph typically yields 8–12 shots.

### 5.2 Required fields
Every shot states framing, lens, camera move, lighting, subject action, and
screen direction. A shot missing any of these is incomplete.

### 5.3 Screen direction and the 180-degree rule
Every shot records which way the subject faces and which frame edge they exit.
The next shot in the scene must honour that direction. Models have no concept
of the axis of action; the script must enforce it. Violations produce cuts
where a character appears to teleport or reverse direction.

### 5.4 Dialogue and lip-sync
Mark `LIPSYNC: YES` only when a mouth is visible speaking on camera. Put the
exact spoken words in the `DIALOGUE` field, verbatim, with a delivery note
(pace, volume, emotional colour). Lip-sync shots route to a different
generation path than b-roll and must be identifiable by the pipeline without
parsing prose.

### 5.5 Negative prompts
Every shot carries a `NEGATIVE` field. Baseline for all shots:
`no text, no watermark, no extra people, no distorted hands, no modern
anachronisms`
Add scene-specific exclusions. Preventing drift is far cheaper than
regenerating.

### 5.6 Coverage discipline
Within a scene, vary framing across consecutive shots. Two consecutive shots at
the same framing and lens on the same subject read as an error, not a choice.

---

## 6. Output schema

The conversion produces exactly four parts, in this order.

### PART A — ASSET BIBLE
Ordered by class: CHAR, LOC, WARD, PROP, VEH, ANI, LOOK.

```
ID:
NAME:
ALIASES:
SCREEN APPEARANCES:      count + shot numbers
DESCRIPTION:             physical only. For people: age, build, height, hair
                         colour and cut, face shape, skin, eyes, distinguishing
                         marks, default posture and gait. For locations:
                         dimensions, materials, colour palette, light sources,
                         furnishing, era, condition, level of clutter.
                         Specific values only.
VARIANT STATES:          each state ID + exactly what differs from base
REFERENCE PROMPTS:       numbered, one per required angle
```

### PART B — CONTINUITY LEDGER
One row per shot. This table is the drift check and is read by the continuity
agent before any generation runs.

| SHOT | TIME | WEATHER | LOCATION | PRESENT | WEARING | EMOTIONAL STATE | CARRYING |
|------|------|---------|----------|---------|---------|-----------------|----------|

### PART C — SHOT SCRIPT
Grouped by scene. Each scene header carries: scene number, location ID, time,
look ID, and a one-line statement of dramatic purpose.

```
SHOT:              S01-005
DURATION:          6s
REFS:              [CHAR_001], [CHAR_002/A], [LOC_002/DUSK], [WARD_001]
FRAMING:           medium close-up
LENS:              85mm, shallow depth of field
CAMERA MOVE:       slow dolly out, 1.5m
LIGHT:             late afternoon, low sun from camera left, warm, window bloom
ACTION:            what the camera sees. Present tense. Physical only.
SCREEN DIRECTION:  subject faces frame right; exits frame right
DIALOGUE:          "exact line" — delivery: flat, barely above a whisper
LIPSYNC:           YES
VO SEGMENT:        which narration line runs under this shot, or NONE
AUDIO:             ambience plus specific SFX with timing
GEN_PROMPT:        one self-contained paragraph, natural language, no IDs,
                   no brackets, brief restatement of subject appearance
NEGATIVE:          baseline plus scene-specific exclusions
```

### PART D — FLAGS
Every ambiguity the transcript left open that had to be resolved: unstated
ages, unspecified times of day, unnamed characters, unclear geography, implied
but undescribed locations. State what was chosen and why.

**Do not invent plot. Do not add characters or events.** Flags record
interpretation, not authorship.

---

## 7. Invocation prompt

The following block is the operational instruction. Pass it, plus the
transcript, to the conversion agent.

```
You are a film director and continuity supervisor converting a prose story
transcript into a production-ready shot script for AI video generation. Your
output drives an automated pipeline. Precision and consistency matter more
than literary quality.

Follow the Transcript-to-Shot-Script Conversion Standard in full:

1. Describe only what the camera sees and the microphone hears. Never describe
   thought, motive, or backstory. Render emotion as visible physical fact.
2. Assign every recurring asset a typed, zero-padded, bracketed ID:
   CHAR_ LOC_ WARD_ PROP_ VEH_ ANI_ LOOK_. Add variant states with a slash
   whenever an asset cannot share reference images with its base — age change,
   wardrobe change, damage, time of day, weather.
3. An asset gets a reference set if it appears on screen in two or more shots,
   must match across a cut, or carries plot weight in a single appearance.
   Count screen appearances, not word mentions. Assets mentioned but never
   shown get nothing.
4. Reference angle sets: characters get front, three-quarter left, profile,
   back, plus a tight neutral face plate. Props, vehicles, and wardrobe get
   front, three-quarter, side, rear. Locations get wide establishing, reverse
   angle, mid from main coverage position, and a texture plate, plus a wide
   per lighting state. Reference prompts specify plain neutral background,
   flat even lighting, no props, no text, specific colour values.
5. Maximum 8 seconds per shot, one camera position, one continuous action.
   Every shot states framing, lens, camera move, lighting, action, and screen
   direction. Maintain the 180-degree rule across consecutive shots in a scene.
6. Mark LIPSYNC YES only when a mouth is visible speaking. Put exact spoken
   words in DIALOGUE with a delivery note.
7. Narration and visuals are separate tracks. Visuals serve the meaning of the
   narration, not its literal words.
8. Every shot has both a REFS field with IDs and a GEN_PROMPT with none. Never
   write an ID, bracket, or pipeline term inside GEN_PROMPT. Never leave a
   bracket unclosed. Never reuse an ID for a different asset. If one object
   appears under two names, assign one ID and record the aliases.

Output exactly four parts and nothing else:
PART A — ASSET BIBLE
PART B — CONTINUITY LEDGER
PART C — SHOT SCRIPT
PART D — FLAGS

No commentary, no preamble, no summary.

TRANSCRIPT:
<<<paste transcript here>>>
```

---

## 8. Worked example

**Source line (prose transcript):**

> Every day when I drive by this alley on my way home from work, I see my
> ex-wife Miranda sitting in that same coffee shop, wearing the same red dress
> she wore on the day I broke up with her.

**Converted output:**

```
SCENE 1 — [LOC_001/DUSK] — evening — [LOOK_PRESENT]
Purpose: establish the compulsion, the routine, the woman he cannot stop seeing.

SHOT:              S01-001
DURATION:          6s
REFS:              [VEH_001], [LOC_001/DUSK]
FRAMING:           extreme wide, aerial
LENS:              24mm
CAMERA MOVE:       FPV drone descends behind the car, closing distance
LIGHT:             dusk, sodium streetlights igniting, wet asphalt reflections
ACTION:            A silver sedan turns into a narrow brick alley between two
                   buildings and drives away from camera. No other traffic.
                   One pedestrian, back turned, near the far wall.
SCREEN DIRECTION:  car travels away from camera, drifting frame left
DIALOGUE:          none
LIPSYNC:           NO
VO SEGMENT:        "Every day when I drive home from work, I pass this alley."
AUDIO:             engine hum, tyres on wet stone, distant traffic
GEN_PROMPT:        Aerial FPV drone shot descending behind a silver four-door
                   sedan as it turns into a narrow brick alley at dusk. Wet
                   asphalt reflecting orange sodium streetlights. The car drives
                   away from camera. Empty alley, one pedestrian with back
                   turned. Cinematic, 24mm, motion blur on the passing walls.
NEGATIVE:          no text, no watermark, no other vehicles, no daylight

SHOT:              S01-002
DURATION:          5s
REFS:              [CHAR_001], [VEH_001]
FRAMING:           medium close-up through the windscreen
LENS:              85mm
CAMERA MOVE:       locked off; focus pull from full bokeh to sharp on his face
LIGHT:             streetlight raking across his face in intermittent bands
ACTION:            A man in his forties grips the wheel, eyes flicking to his
                   right, away from the road. Jaw set. He does not blink.
SCREEN DIRECTION:  he looks frame right
DIALOGUE:          none
LIPSYNC:           NO
VO SEGMENT:        continuous
AUDIO:             muffled interior engine, indicator tick
GEN_PROMPT:        Medium close-up through a car windscreen at dusk. A man in
                   his forties, short dark hair, stubble, grey shirt, grips the
                   steering wheel and looks off to his right, away from the
                   road. Streetlights sweep across his face in bands. Focus
                   pulls from heavy bokeh into sharp focus on his eyes. 85mm,
                   shallow depth of field, cinematic.
NEGATIVE:          no text, no watermark, no passengers, no phone

SHOT:              S01-003
DURATION:          8s
REFS:              [CHAR_002/A], [LOC_002/DUSK], [WARD_001]
FRAMING:           wide, through plate glass
LENS:              35mm
CAMERA MOVE:       slow dolly out, revealing the emptiness around her
LIGHT:             warm interior practicals against cold blue exterior
ACTION:            A woman in a red dress sits alone at a window table in a
                   large empty coffee shop. Every other chair is stacked on its
                   table. She does not look up. Camera retreats until she is a
                   small figure in a wide bright box.
SCREEN DIRECTION:  she faces frame left, toward the street
DIALOGUE:          none
LIPSYNC:           NO
VO SEGMENT:        "And every day, she is sitting there. In that same red dress."
AUDIO:             street ambience outside, glass-muffled interior, low hum
GEN_PROMPT:        Slow dolly-out wide shot through a plate glass window. A
                   woman in her late thirties, shoulder-length dark hair,
                   wearing a deep crimson dress, sits alone at a window table
                   in a large empty coffee shop at dusk. All other chairs are
                   stacked on tables. Warm interior lights against cold blue
                   evening outside. She stares at the street, motionless. 35mm,
                   cinematic, melancholic.
NEGATIVE:          no text, no watermark, no other customers, no staff
```

Note what the example does: three shots share one narration passage, the
reference IDs never appear in any GEN_PROMPT, the red dress is tracked as
wardrobe rather than a prop, and each shot commits to a specific screen
direction that the next shot must respect.

---

## 9. Anti-patterns

| Anti-pattern | Why it fails | Correction |
|---|---|---|
| IDs inside the generation prompt | Model tokenizes them as noise, degrading output | Keep REFS and GEN_PROMPT strictly separate |
| Nested or unbalanced parentheses around IDs | Breaks regex extraction downstream | Square brackets, one ID per token, never nested |
| One reference set for a character across a flashback | Age and hair differ; output looks like a different person | Define variant states |
| Wardrobe filed as a prop | Outfit drift goes untracked between shots | Separate WARD_ class plus ledger column |
| 360° coverage for a location | Wastes generations on angles never shot | Cover shooting axes plus lighting states |
| Reference plates with dramatic lighting | Bakes that lighting into every downstream shot | Flat even light, neutral background |
| Shots longer than 8 seconds | Exceeds model generation window | Split into separate shots |
| One shot per narration sentence | Produces a slideshow | Decouple the tracks, 8–12 shots per paragraph |
| Emotion stated rather than shown | Nothing for the camera to render | Convert to visible physical fact |
| Re-describing assets in every shot | Each restatement drifts from the last | Describe once in the bible, cite thereafter |
| Ignoring screen direction | Characters reverse or teleport across cuts | Record direction per shot, honour the axis |

---

## 10. Pre-generation QA checklist

Run before any image or video generation is dispatched.

- [ ] Every ID in every REFS field resolves to an Asset Bible entry
- [ ] No GEN_PROMPT contains a bracket, an underscore-prefixed ID, or a
      pipeline term
- [ ] No bracket anywhere is left unclosed
- [ ] No ID is used for two different assets
- [ ] Every asset meeting the reference trigger has a complete angle set
- [ ] Every variant state has its own complete angle set
- [ ] No shot exceeds 8 seconds
- [ ] Every shot has framing, lens, camera move, lighting, action, and screen
      direction
- [ ] Screen direction is consistent across every cut within each scene
- [ ] Continuity ledger has one row per shot with no blank cells
- [ ] Wardrobe column in the ledger changes only where the story changes it
- [ ] Every LIPSYNC:YES shot has verbatim dialogue and a delivery note
- [ ] Every shot has a NEGATIVE field including the baseline exclusions
- [ ] PART D contains no invented plot, characters, or events

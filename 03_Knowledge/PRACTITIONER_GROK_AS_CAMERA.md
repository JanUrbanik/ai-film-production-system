# Practitioner knowledge — Grok as camera / raw-footage engine

**Knowledge ID:** `K-PRAC-GROK-CAMERA-001`  
**Version:** 1.0  
**Source:** `PRAC-2026-001` → `10_Sources/practitioners/SOURCE_ZRtT-0SUw8M_ODYSSEY_GROK_CAMERA.md`  
**Video:** https://www.youtube.com/watch?v=ZRtT-0SUw8M  
**Status:** ACTIVE factory law (method), not hype  

---

## 1. Core thesis (Verified from transcript)

> Treat **Grok Imagine as a camera** and as a **raw footage generating machine** — not as an all-in-one finished film director.

Implications for this factory:

| Mindset | Factory meaning |
|---------|-----------------|
| Camera | Prompt subject action + camera move + continuity constraints |
| Raw footage engine | Multi-take bins; edit builds the piece |
| Not magic finish | PASS/FAIL QC + NLE still required |

This **reinforces** existing factory law (short clips, multi-take, edit hides sin, I2V priority). It does **not** replace Character/Env/Props bibles.

---

## 2. Extracted method (step chain)

### Phase A — Concept lock (pre-gen)

**Verified steps from speaker:**

1. Start with a **rough concept**.  
2. Materialize as **shot list** and/or **style template**.  
3. Purpose: keep **visual style consistent** across the whole piece.

**Factory mapping:**

| Speaker | Seat / artifact |
|---------|-----------------|
| Rough concept | R0/R1 brief |
| Shot list | R6 `03_shot_list/` |
| Style template | Style Contract + locked look language (`04_Bibles/templates/STYLE_CONTRACT.md`) |

### Phase B — Start frames before motion (critical)

**Verified:**

1. Generate **start frames**.  
2. Only when frames are **storyboard-worthy**, generate video from them.  
3. Often, generating video from a start frame lets Grok **use that frame’s context** (consumer “generate video” on still).  
4. If start frames are nailed, the **video model has a smaller job** — prompt only what should **happen** in the clip.

**Factory mapping:**

| Speaker | Factory |
|---------|---------|
| Start frame | LOCKED still / composed plate in `02_refs/` or shot still |
| Storyboard-worthy gate | R6 + R0/R9 still gate before R8 motion |
| Smaller video job | Mode **i2v**; motion prompt = camera + action only |
| API equivalent | `grok-imagine-video-1.5` + `image_url` / first-frame still |

**Label:** Consumer UI “click generate on frame” ≈ API **image-to-video** (**Assumed** product parity; API is contract for automation).

### Phase C — Motion prompt as camera orders

**Verified prompt pillars for each clip:**

1. **What is the subject doing?**  
2. **What is the camera doing?**  
3. **What must stay consistent** through the shot?

**Factory mapping:** Already in shot cards + `PROMPT_PACKET` + closed camera vocabulary. Elevate as mandatory R7 packet fields (not optional flavor).

### Phase D — Speech / performance shots

**Verified:**

1. For speech, **type the dialogue** the character should say.  
2. Add **emotion**, **pauses**, and **beats** the performance should hit.

**Factory mapping:**

- Packet `prompt.action` + `audio_note` + optional `dialogue` field on shot card  
- Skill: `06_Skills/generation/SPEECH_PERFORMANCE_PROMPT.md`  
- Native Imagine audio may carry lines (**Assumed** quality varies) → R11/R9 QC lips/clarity  
- Does **not** unlock arbitrary custom voice clone (see Imagine matrix restrictions)

### Phase E — Multi-take reality

**Verified:**

1. Take one is often not best.  
2. Do not expect perfection first try.  
3. You may need to **generate a clip** multiple times (transcript truncates here).

**Factory mapping:** R8 multi-take + R9 reject-heavy QC + `SHOT_FLEET_OPS` — already law; this source is practitioner confirmation.

---

## 3. Do / Don’t (operator card)

### Do

- Build style template + shot list before volume gen  
- Approve start frames as storyboard stills first  
- I2V from approved frames; motion prompt only deltas  
- Specify subject / camera / continuity every packet  
- For dialogue: words + emotion + pauses/beats  
- Budget multi-take; select in edit  

### Don’t

- Treat T2V-from-scratch as default for hero identity shots  
- Overload motion prompt with full re-description of face/world if frame already locks it  
- Ship take 1 without QC  
- Confuse “Grok as camera” with “skip bibles”  
- Claim the truncated transcript contains a full post pipeline  

---

## 4. Alignment with factory pipeline

```text
Concept + style template + shot list
        ↓
Start frames (image) → storyboard-worthy gate
        ↓
I2V / camera-style motion prompts (multi-take)
        ↓
QC (identity + motion + speech)
        ↓
Edit assembles raw footage into piece
```

Matches `CANONICAL_PIPELINE` generation priority: **I2V first**.

---

## 5. Seat ownership of this knowledge

| Seat | Must apply |
|------|------------|
| R1 Showrunner | Enforce start-frame gate before motion spend |
| R6 Shot Designer | Shot list + style-aware cards; mark speech shots |
| R7 Injector | Packet includes subject/camera/consistency; speech blocks |
| R8 Generator | I2V default from approved stills; multi-take |
| R9 Critic | Still-worthiness + take selection; speech clarity |
| R10 Editor | Treat PASS clips as raw footage library |
| R11 Sound | Performance intent vs native audio QC |

---

## 6. Open gaps (honest)

| Gap | Status |
|-----|--------|
| Transcript cuts mid-sentence after multi-take advice | Partial source |
| Exact Odyssey asset pipeline (counts, tools UI clicks) | Not in captured text |
| Creator on-camera identity | Assumed Heavy Pulp / heavypulp from external context |
| Whether style template = our Style Contract format | Assumed compatible |

When User supplies a longer transcript, revise this file to v1.1+ without deleting v1.0 decisions that still hold.

---

## 7. Related skills (call these)

1. `06_Skills/generation/GROK_AS_CAMERA.md`  
2. `06_Skills/generation/START_FRAME_FIRST.md`  
3. `06_Skills/generation/SPEECH_PERFORMANCE_PROMPT.md`  
4. `06_Skills/generation/I2V_PLATE_LOCK.md`  
5. `06_Skills/generation/SHOT_FLEET_OPS.md`  

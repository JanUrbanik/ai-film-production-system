# Skill — Imagine Image 2.0 (stills & edits)

**ID:** `IMAGINE_IMAGE_2_0`  
**As-of:** 2026-08-08  
**Surface default:** Consumer Quality Mode (`grok.com/imagine`, iOS/Android)  
**Ledger:** SuperGrok Heavy weekly pool first  
**Authority:** `10_Sources/research/GROK_IMAGINE_IMAGE_2_0_2026-08-08.md`  
**Does not replace:** `grok-imagine-video-1.5` motion path  

---

## When to use

| Job | Use Image 2.0? |
|-----|----------------|
| Bible master stills (char/env/prop) | **Yes — default** |
| Multi-view / expression / wardrobe stills | **Yes** |
| Start frames before I2V | **Yes — default** |
| Local fix (object, color, hand, logo) on a still | **Yes** (wand/seg before full regen) |
| Transparent cutout for composite / thumb | **Yes** (BG removal) |
| Match shot aspect without crude crop | **Yes** (Smart Resize) |
| Motion / dialogue / camera move | **No** → Video 1.5 + `GROK_AS_CAMERA` |
| Headless batch API while 2.0 API unreleased | **No** → `grok-imagine-image-quality` only if Director unlocked API |

---

## Tool map (consumer UI — Verified vendor)

| Tool | Film use |
|------|----------|
| **Quality Mode / Image 2.0** | Default still generator |
| **Magic Wand** | Local edit; protect locked face/wardrobe regions |
| **Segmentation** | Precise region select before edit |
| **Background removal** | Subject plate with alpha for boards/thumbs |
| **Multi-ref (≤5)** | Char+wardrobe+style or char+env+prop still composites |
| **Smart Resize** | Reflow plate to `16:9` / `9:16` / etc. without dumb crop |
| **Templates** | Speed only — still obey bible locks + consent |
| **Build a world for video** | Pre-I2V pack: character / locations / props same look |

---

## Factory procedure

### A. New bible master

1. Confirm LOCK intent + consent.  
2. Consumer Imagine → **Image 2.0 Quality**.  
3. Prompt: identity/style locked language; no crowd.  
4. Save `02_refs/.../master_vN.png`.  
5. Multi-ref or edit path for views (front / 3-4 / profile).  
6. Critic (R9) identity gate → LOCK.

### B. Start frame (Grok-as-camera)

1. Compose storyboard-worthy still (SUBJECT already correct).  
2. Image 2.0 generate or edit from bible refs (multi-ref OK).  
3. Smart Resize to shot `aspect` if needed.  
4. Run `START_FRAME_FIRST` gate.  
5. Only then I2V on Video 1.5 (`I2V_PLATE_LOCK`).

### C. Surgical still repair

1. Prefer Magic Wand / Segmentation over full regen.  
2. Re-run start-frame gate if used as I2V source.  
3. Never claim video identity fixed by still edit alone.

### D. World pack (pre-video)

1. Use “build a world for video” pattern: separate gens, one style.  
2. Store under `02_refs/characters|environments|props/`.  
3. Pin versions in bibles before volume motion.

---

## Prompt habits

- Still prompts: composition + light + materials + **what must not change**.  
- Edits: name the **region** and the **invariant** (“keep face and wardrobe; change only jacket color”).  
- Multi-ref: label roles in prompt (“person from image 1, room from image 2”).  
- After still lock, motion prompts stay SUBJECT + CAMERA + HOLD only.

---

## Logging

| Field | Example |
|-------|---------|
| `model_image` | `imagine-image-2.0-quality` (consumer) or API id when live |
| `surface` | `grok.com/imagine` |
| `ledger` | `supergrok_heavy_weekly` |
| `tools_used` | `wand\|seg\|bg_remove\|multi_ref\|smart_resize\|template` |

---

## Forbidden

- Skipping start-frame gate because “2.0 is better.”  
- Using templates to invent unlocked cast/IP.  
- Calling unreleased API model ids as Verified.  
- Burning API credits while Heavy weekly pool remains.

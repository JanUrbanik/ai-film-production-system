# Knowledge — Transcript-to-Shot-Script Conversion Standard

**Knowledge ID:** `K-SHOT-SCRIPT-001`  
**Version:** 1.0  
**Status:** ACTIVE (binding for prose → production conversion)  
**Full standard:** `10_Sources/standards/TRANSCRIPT_TO_SHOT_SCRIPT_STANDARD_v1.md`  
**Skill:** `06_Skills/generation/TRANSCRIPT_TO_SHOT_SCRIPT.md`  
**Workflow:** `05_Workflows/TRANSCRIPT_TO_SHOT_SCRIPT.md`  
**Pairs with:** `K-PRAC-GROK-CAMERA-001` (Grok-as-camera), Image 2.0 stills, Video 1.5 motion  

---

## 1. Purpose

Authoritative method to convert a **prose story transcript** into production artifacts that Imagine can execute **without visual drift**.

**Input:** prose transcript (any person/tense).  
**Output (exactly four parts):**

| Part | Artifact | Factory landing |
|------|----------|-----------------|
| A | Asset Bible | `01_bibles/` + ID map |
| B | Continuity Ledger | `09_qc_log/CONTINUITY_LEDGER.csv` |
| C | Shot Script | `03_shot_list/SHOT_SCRIPT.md` (+ cards) |
| D | Flags | `00_brief/FLAGS.md` |

Any seat asked for shot list / storyboard / asset bible / gen prompts from prose **must** follow this standard.

---

## 2. Five doctrines (non-negotiable)

1. **Generator is a camera** — only visible/audible facts; emotion = physical behavior.  
2. **Reference IDs never reach the model** — `REFS:` for pipeline; `GEN_PROMPT:` clean natural language only.  
3. **Describe once, cite forever** — full description in Asset Bible; shots cite IDs; GEN_PROMPT may restate subject in **one brief clause**.  
4. **Screen appearances, not word mentions** — refs by how often something is **seen**.  
5. **Narration ≠ visuals** — VO and picture are parallel tracks; serve meaning, not literal sentence slideshow.

---

## 3. ID scheme (pipeline metadata)

```text
[TYPE_NNN]         base
[TYPE_NNN/STATE]   variant that cannot share ref images
```

| Prefix | Class |
|--------|--------|
| `CHAR_` | Person |
| `LOC_` | Location |
| `WARD_` | Wardrobe (separate from props — drift killer) |
| `PROP_` | Object |
| `VEH_` | Vehicle |
| `ANI_` | Animal |
| `LOOK_` | Visual treatment (present / flashback / dream) |

**Variant states mandatory** when age/era, major wardrobe, damage, TOD, or weather prevent shared refs.

---

## 4. Reference image rules (Image 2.0 plates)

Trigger if: ≥2 screen shots, must match across cut, or single appearance with plot weight.

| Class | Angles |
|-------|--------|
| Characters | 5: front, ¾ L, profile, back, **tight neutral face plate** (identity lock) |
| Prop / veh / ward | 4: front, ¾, side, rear |
| Locations | 4 axes + one wide per lighting state |

Reference prompts: neutral mid-grey BG, **flat even light**, specific colours, no drama lighting, no text.

Factory default generator for these plates: **Imagine Image 2.0** Quality (`IMAGINE_IMAGE_2_0`).

---

## 5. Shot construction (aligns Grok-as-camera)

| Rule | Factory note |
|------|----------------|
| Max **8s** per shot (preferred) | API allows 15s; this standard caps **8s** for conversion output |
| One camera position, one continuous action | = one move + one action |
| Framing, lens, move, light, action, **screen direction** | required fields |
| 180° / screen direction continuity | Continuity ledger + R9 |
| `LIPSYNC: YES` only if mouth visible | routes speech path |
| `NEGATIVE` every shot | baseline + scene |
| Vary coverage | no two identical consecutive frames |

**GEN_PROMPT** must encode SUBJECT + CAMERA + HOLD in natural language **without IDs**.

---

## 6. Pre-generation QA (R7/R9 gate)

Before any Image 2.0 / Video 1.5 dispatch:

- Every REFS ID resolves in Asset Bible  
- No GEN_PROMPT contains brackets / IDs / pipeline jargon  
- Variant states have own angle sets  
- No shot > 8s (conversion path)  
- Screen direction consistent in scene  
- Ledger one row/shot, wardrobe column intentional  
- LIPSYNC rows have verbatim dialogue + delivery  
- PART D flags = interpretation only, **no invented plot**

---

## 7. Seat map

| Seat | Duty |
|------|------|
| R2 Story | Supply/freeze transcript; own FLAGS with R1 |
| R1 Showrunner | Order conversion; freeze shot script version |
| R3–R5 + WARD | Asset Bible → locked packs via Image 2.0 |
| R6 Shot Designer | Shot Script → cards; coverage + screen direction |
| R7 Injector | REFS → paths; GEN_PROMPT → `prompt.full_text` only |
| R8 Generator | Sends **only** GEN_PROMPT (+ attached refs); never IDs in model string |
| R9 Critic | Pre-gen QA checklist + take gates |
| R10 Editor | Respects VO vs visual tracks |

---

## 8. Relationship to existing law

| Existing | Integration |
|----------|-------------|
| Grok-as-camera | Doctrine 2.1 is the same camera mind; this standard adds ID/ledger discipline |
| Start-frame first | After shot script freeze: Image 2.0 stills per hero shot → gate → I2V |
| SUBJECT+CAMERA+HOLD | Lives inside GEN_PROMPT; REFS stay outside |
| SuperGrok Heavy first | All still/video gen stills draw weekly pool first |
| Schema packets | Extended fields: `refs`, `gen_prompt`, `screen_direction`, `lipsync`, … |

---

## Document control

| Ver | Date | Notes |
|-----|------|-------|
| 1.0 | 2026-08-09 | Ingest standard v1.0 from Director download |

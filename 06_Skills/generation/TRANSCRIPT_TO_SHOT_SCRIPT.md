# Skill — Transcript → Shot Script

**ID:** `TRANSCRIPT_TO_SHOT_SCRIPT`  
**Knowledge:** `K-SHOT-SCRIPT-001`  
**Full law:** `10_Sources/standards/TRANSCRIPT_TO_SHOT_SCRIPT_STANDARD_v1.md`  
**Seats:** R2 (input), R1 (order), R3–R6 (execute), R7 (packetize), R9 (QA)

---

## When to run

- User pastes a **prose transcript / story** and wants shot list, bibles, or gen prompts.  
- New project from narrative text (not already carded).  
- Episode beat expansion from locked prose.

**Do not skip** this skill for freeform “just write some prompts.”

---

## Output contract (exactly four parts)

Write under project slug:

| Part | Path |
|------|------|
| A Asset Bible | `01_bibles/ASSET_BIBLE.md` + per-ID notes |
| B Continuity Ledger | `09_qc_log/CONTINUITY_LEDGER.csv` |
| C Shot Script | `03_shot_list/SHOT_SCRIPT.md` |
| D Flags | `00_brief/FLAGS.md` |

Optional: `01_bibles/ID_MAP.md` (alias table).

Templates: `05_Workflows/templates/shot_script/`.

---

## Invocation (copy to conversion agent)

Use the invocation block in standard §7, or:

```text
You are a film director and continuity supervisor converting a prose story
transcript into a production-ready shot script for AI video generation.
Follow K-SHOT-SCRIPT-001 / TRANSCRIPT_TO_SHOT_SCRIPT_STANDARD_v1 in full.

Output exactly four parts and nothing else:
PART A — ASSET BIBLE
PART B — CONTINUITY LEDGER
PART C — SHOT SCRIPT
PART D — FLAGS

No commentary, no preamble, no summary.

TRANSCRIPT:
<<<paste>>>
```

Then **map** the four parts into factory paths above (do not leave only chat output).

---

## Hard checks while writing GEN_PROMPT

| Must | Must not |
|------|----------|
| Natural language only | `[CHAR_001]`, any brackets |
| Visible/audible facts | Thought, motive, backstory labels |
| Framing + move + light + action | Empty camera fields |
| Brief subject restatement | Full bible dump every shot |
| Screen direction stated | Ambiguous exits |
| NEGATIVE baseline + scene | Missing negatives |
| ≤ 8s duration | 9–15s on this conversion path |

Baseline NEGATIVE:
`no text, no watermark, no extra people, no distorted hands, no modern anachronisms`

---

## After conversion (hand-off chain)

```text
1. R1 freezes SHOT_SCRIPT version
2. R3–R5 (+WARD) generate Image 2.0 reference plates per bible angles
3. R9 bible gate
4. R6 ensures coverage + 180°
5. Hero start frames (Image 2.0) + START_FRAME_FIRST
6. R7 packets: refs[] from REFS; prompt.full_text = GEN_PROMPT only
7. R8 multi-take Video 1.5 — never paste IDs into model
8. R9 take gates using ledger
```

---

## Anti-patterns (instant FAIL)

- IDs inside GEN_PROMPT  
- Wardrobe tracked only as PROP_  
- One face set across flashback ages  
- Dramatic lighting on ref plates  
- One shot per narration sentence slideshow  
- Invented plot in FLAGS  

---

## Factory model binding

| Stage | Tool |
|-------|------|
| Ref plates + start frames | Imagine **Image 2.0** Quality |
| Motion | **Video 1.5** I2V preferred |
| Spend | SuperGrok Heavy weekly pool first |

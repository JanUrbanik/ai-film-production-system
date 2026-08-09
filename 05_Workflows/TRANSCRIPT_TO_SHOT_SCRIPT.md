# Workflow — Transcript → Shot Script → Gen

**Version:** 1.0  
**Date:** 2026-08-09  
**Knowledge:** `K-SHOT-SCRIPT-001`  
**Skill:** `TRANSCRIPT_TO_SHOT_SCRIPT`  
**Standard:** `10_Sources/standards/TRANSCRIPT_TO_SHOT_SCRIPT_STANDARD_v1.md`

---

## 0. When

Prose story / narration transcript must become executable Imagine work.  
Use **before** volume stills or I2V.

## 1. Bootstrap

```bash
cp -R 08_Projects/_template 08_Projects/<slug>
# optional copy templates
cp 05_Workflows/templates/shot_script/* 08_Projects/<slug>/ -n 2>/dev/null || true
```

Place source prose in `00_brief/TRANSCRIPT.md`.

## 2. Convert (R2 + R1 + conversion agent)

1. Load skill `TRANSCRIPT_TO_SHOT_SCRIPT` + full standard.  
2. Run invocation → four parts only.  
3. Write:
   - `01_bibles/ASSET_BIBLE.md`
   - `09_qc_log/CONTINUITY_LEDGER.csv`
   - `03_shot_list/SHOT_SCRIPT.md`
   - `00_brief/FLAGS.md`
4. Director reviews FLAGS (interpretations only).  
5. R1 freezes shot script version string.

## 3. Materialize bibles (R3–R5)

1. Expand Asset Bible IDs into factory bible files (char/env/props + **WARD_** notes).  
2. Generate reference plates on **Image 2.0** per angle rules (flat light).  
3. Store under `02_refs/{characters,environments,props,wardrobe}/<ID>/`.  
4. LOCK packs; R9 bible gate.

## 4. Cards + start frames (R6)

1. Emit shot cards from SHOT_SCRIPT (one card per SHOT).  
2. Enforce coverage variation + 180°.  
3. Hero shots: Image 2.0 start stills → `START_FRAME_FIRST`.

## 5. Inject (R7)

For each shot:

| Shot script field | Packet field |
|-------------------|--------------|
| `REFS` | `reference_images[]` + `bible_pins` (resolve paths; **never** into full_text) |
| `GEN_PROMPT` | `prompt.full_text` **exactly** (or SUBJECT/CAMERA/HOLD split derived from it) |
| `NEGATIVE` | `prompt.negatives` |
| `DURATION` | `duration_target` (≤8 on this path) |
| `LIPSYNC` / `DIALOGUE` | speech block / `lipsync` |
| `SCREEN DIRECTION` | `screen_direction` |
| `AUDIO` | `prompt.audio_note` |
| `VO SEGMENT` | `vo_segment` |

**Defect:** any `[CHAR_` or bracket inside `prompt.full_text`.

Validate `shot_packet.schema.json`.

## 6. Generate (R8)

1. SuperGrok Heavy pool first.  
2. Attach ref images by path from REFS.  
3. Send **GEN_PROMPT only** to model.  
4. Multi-take; download; never self-PASS.

## 7. QC (R9)

1. Pre-gen checklist (standard §10).  
2. Take gates vs ledger (wardrobe, location TOD, screen direction).  
3. FAIL → repair ladder; do not “fix” by stuffing IDs into prompts.

## 8. Edit (R10)

Assemble PASS bin; VO track independent of shot boundaries (doctrine 2.5).

---

## Definition of done

- [ ] Four parts on disk under slug  
- [ ] Ref plates complete for triggered assets  
- [ ] Packets pass schema + no-ID-in-prompt lint  
- [ ] At least hero path: start frame → I2V → QC row  

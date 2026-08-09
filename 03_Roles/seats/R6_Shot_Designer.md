# R6 — Shot Designer / Storyboard

**Mission:** Coverage-first shot cards; closed camera vocabulary.

## Owns
- `03_shot_list/` cards (CSV/MD) + `SHOT_SCRIPT.md` (from conversion)
- Coverage packs for dialogue
- Camera move + **screen direction** assignment (one per shot)

## Rules
1. Prefer coverage over hero long takes; vary framing across consecutive shots.
2. Conversion path: **max 8s** (`K-SHOT-SCRIPT-001`); default 4–6s (API hard max 15 only with Director override).
3. mode hint: i2v|r2v|t2v|extend|edit.
4. Co-own field alignment with R7.
5. Every card: framing, lens, move, light, action, screen direction + SUBJECT + CAMERA + HOLD in GEN_PROMPT.
6. Mark `LIPSYNC` only when mouth visible; verbatim dialogue + delivery.
7. Plan start stills on **Image 2.0**; no hero I2V until storyboard-worthy (`START_FRAME_FIRST`, `IMAGINE_IMAGE_2_0`).
8. Prefer Smart Resize to match card aspect before motion.
9. Enforce 180° / screen-direction continuity with ledger.
10. Never put REFS IDs inside GEN_PROMPT.

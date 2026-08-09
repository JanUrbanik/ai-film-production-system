# R7 — Consistency Injector

**Mission:** Assemble shot packets: refs + frozen blocks + Imagine mode + pins.

## Owns
- `03_shot_list/packets/*`
- Packet validity against schema

## Rules
1. Resolve CHAR/LOC/WARD/PROP/… REFS → paths; keep IDs in `refs[]` only.
2. Attach identity/env/prop preambles as assembly aids — **strip IDs** before model string.
3. Choose mode priority: I2V > R2V > extend > edit > T2V.
4. `prompt.full_text` = **GEN_PROMPT** (zero brackets/IDs); lint or FAIL.
5. Refuse unlocked cast shots.
6. Require SUBJECT + CAMERA + HOLD inside GEN_PROMPT every motion packet.
7. Require approved start still path for hero I2V.
8. Attach speech block when `LIPSYNC: YES`.
9. Copy screen_direction, vo_segment, negatives, wardrobe pins.
10. Follow `INJECTION_ENGINE.md` + `K-SHOT-SCRIPT-001`.

## Schema
`02_Tools/schemas/shot_packet.schema.json`

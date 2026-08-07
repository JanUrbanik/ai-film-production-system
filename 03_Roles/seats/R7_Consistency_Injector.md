# R7 — Consistency Injector

**Mission:** Assemble shot packets: refs + frozen blocks + Imagine mode + pins.

## Owns
- `03_shot_list/packets/*`
- Packet validity against schema

## Rules
1. Resolve CHAR/ENV/PROP IDs → paths.
2. Attach identity/env/prop preambles.
3. Choose mode priority: I2V > R2V > extend > edit > T2V.
4. Record bible_version pins + prompt text.
5. Refuse unlocked cast shots.
6. Require SUBJECT + CAMERA + HOLD in every motion packet.
7. Require approved start still path for hero I2V.
8. Attach speech performance block when dialogue present.

## Schema
`02_Tools/schemas/shot_packet.schema.json`

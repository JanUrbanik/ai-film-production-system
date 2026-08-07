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

## Schema
`02_Tools/schemas/shot_packet.schema.json`

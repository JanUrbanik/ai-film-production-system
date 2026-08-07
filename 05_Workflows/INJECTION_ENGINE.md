# Consistency Injection Engine (operable)

**Owner:** R7  
**Schematic source:** Master Consistency Injection (structure kept; magic demoted)

## Purpose

Turn shot cards + locked bibles into valid **shot packets** for R8.

## Steps

1. Load frozen shot card.  
2. Resolve IDs → ref paths (folder packs; optional vector DB later).  
3. Attach preambles (char/env/prop/style).  
4. Select mode: I2V > R2V > extend > edit > T2V.  
5. Build `prompt.full_text` via skill `06_Skills/generation/PROMPT_PACKET.md`.  
6. Fill `bible_pins` version strings.  
7. Estimate cost: `takes_planned * duration * 0.08` (+ stills).  
8. Validate against `02_Tools/schemas/shot_packet.schema.json`.  
9. Status `ready` → hand to R8.

## Explicit non-MVP

- Vector DB pull  
- Numeric reference_weight API fields unless vendor-documented  
- Multi-model injection  

## Feedback

R9 fail_tags → R7 revises packet (tighter refs/mode) → R8 regen.

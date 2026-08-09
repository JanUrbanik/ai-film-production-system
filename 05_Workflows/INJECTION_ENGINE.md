# Consistency Injection Engine (operable)

**Owner:** R7  
**Schematic source:** Master Consistency Injection (structure kept; magic demoted)

## Purpose

Turn shot cards + locked bibles into valid **shot packets** for R8.

## Steps

0. If source is prose transcript: require frozen `SHOT_SCRIPT` from `K-SHOT-SCRIPT-001` first (`TRANSCRIPT_TO_SHOT_SCRIPT`).  
1. Load frozen shot card / shot-script block.  
2. Resolve REFS IDs → ref paths (`CHAR_/LOC_/WARD_/PROP_/…` packs; optional vector DB later). Store IDs in packet `refs[]` only.  
3. Attach preambles for assembly aids — **strip all IDs/brackets before** any merge into model string.  
4. Select mode: I2V > R2V > extend > edit > T2V.  
4b. Hero cast/location: require storyboard-worthy start still before I2V (`START_FRAME_FIRST`).  
4c. Enforce SUBJECT + CAMERA + HOLD inside **GEN_PROMPT** (`GROK_AS_CAMERA` + shot standard).  
4d. Speech: `LIPSYNC` + verbatim `DIALOGUE` + delivery (`SPEECH_PERFORMANCE_PROMPT`).  
5. Set `prompt.full_text` = shot-script **GEN_PROMPT** (preferred) or assemble via `PROMPT_PACKET.md` with **zero** pipeline IDs.  
5b. Lint: reject if `full_text` matches `\[|CHAR_|LOC_|WARD_|PROP_|VEH_|ANI_|LOOK_`. Set `gen_prompt_lint`.  
6. Fill `bible_pins` (include `wardrobe[]`). Copy `screen_direction`, `vo_segment`, negatives.  
7. Duration: conversion path ≤8s (`duration_policy=standard_8s_cap`) unless Director overrides.  
8. Estimate cost: `takes_planned * duration * rate` (+ stills); ledger SuperGrok pool first.  
9. Validate against `02_Tools/schemas/shot_packet.schema.json`.  
10. Status `ready` → hand to R8.

## Explicit non-MVP

- Vector DB pull  
- Numeric reference_weight API fields unless vendor-documented  
- Multi-model injection  

## Feedback

R9 fail_tags → R7 revises packet (tighter refs/mode) → R8 regen.

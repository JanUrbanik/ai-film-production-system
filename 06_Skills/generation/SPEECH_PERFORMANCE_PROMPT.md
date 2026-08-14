# Skill: Speech / performance prompting

**Source:** `K-PRAC-GROK-CAMERA-001`  
**Seats:** R2 (dialogue lock), R6 (marks speech shots), R7/R8 (prompt), R9/R11 (QC)  

## When

Shot card includes spoken line or clear performance beat (speech, monologue, address-to-camera).

## Required prompt ingredients (Verified from practitioner)

1. **Exact words** (or locked paraphrase Director approved)  
2. **Emotion** (e.g. restrained grief, cold command)  
3. **Pauses and beats** (where they breathe, stop, land a word)  

## Template

```text
SPEECH: "{{dialogue_line}}"
PERFORMANCE: emotion={{...}}; pace={{slow|measured|urgent}};
BEATS: pause after "{{word}}"; land on "{{word}}"; eyes {{...}}
CAMERA: {{locked or slight push}}
HOLD: face and wardrobe from start frame/refs; no identity drift
```

## Factory notes

- Prefer **I2V** from a still that already has correct mouth-neutral or pre-speech face.  
- Spoken line → **`LIPSYNC:YES`**. Mouth **moves in-camera** on Video 1.5 (Director override 2026-08-13).  
- Native audio is in-pass. There is **no** post-hoc lip-sync / Higgsfield re-glue.  
- If lips fail QC: **re-take the same plate** with a tighter SPEECH / BEATS block. Do **not** default to hide-mouth OTS or picture-lock + ADR.  
- OTS / profile remain legal **coverage** (reaction, identity hide, or a line you *planned* to ADR). They are not the speech-FAIL default.  
- Preset `voice_id` only if account/policy allows (matrix `[U]`); not arbitrary clone.  
- One visible speaker per `LIPSYNC:YES` clip. Two-handers = more cards, not one gen.  

## Anti-patterns

- “He says something inspiring” without text  
- Emotion-only with no line  
- Complex walk + full speech + whip pan in one gen  

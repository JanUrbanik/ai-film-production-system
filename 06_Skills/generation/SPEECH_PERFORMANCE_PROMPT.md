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
- Native audio may include the line — **Assumed** variable sync; R9 checks intelligibility; R11 may replace with VO.  
- Preset `voice_id` only if account/policy allows (see Imagine matrix); not arbitrary clone.  
- If lips fail QC, keep take for picture and ADR, or prefer OTS/side angles (coverage).  

## Anti-patterns

- “He says something inspiring” without text  
- Emotion-only with no line  
- Complex walk + full speech + whip pan in one gen  

# Skill: Grok as camera (raw footage engine)

**Source:** `K-PRAC-GROK-CAMERA-001` / video `ZRtT-0SUw8M`  
**Seats:** R6, R7, R8, R9, R10  

## Intent

Prompt and operate Grok Imagine like a **camera department producing raw takes**, not like a one-click finished movie.

## Mandatory triple for every motion packet

Before R8 runs, packet must answer:

1. **SUBJECT:** what the character/object does (one primary action)  
2. **CAMERA:** what the camera does (one primary move from closed vocabulary)  
3. **HOLD:** what must not change (face/wardrobe/location/light pins)

## Prompt skeleton

```text
{{IDENTITY / HOLD from bible pins — short if I2V still carries likeness}}

SUBJECT: {{one action}}
CAMERA: {{one move}}, {{speed}}, {{framing}}
HOLD: match start frame / refs; no identity drift; no location morph
AUDIO: {{optional performance or ambience}}
```

## Operating rules

1. Prefer **I2V** when a storyboard-worthy start frame exists.  
2. Do not ask the video model to “reinvent” the frame — only animate ordered changes.  
3. Plan **multi-take**; take 1 is not sacred.  
4. Editor assembles raw footage; Generator does not “final cut.”  
5. Style consistency comes from **style template + start frames + bibles**, not vibes alone.

## Anti-patterns

- Novel-length prompts that re-spec the entire world every take  
- T2V hero close-ups with no refs/still when identity matters  
- Shipping without QC because “the trailer guy made it look easy”  

## Done-when

Packet has SUBJECT/CAMERA/HOLD; mode chosen; takes_planned ≥ 4 for hero shots unless Director waives.

# Shot Script — smoke_imagine_v1 (PART C)

**Version:** shot_script_smoke_v1  
**Standard:** K-SHOT-SCRIPT-001  
**Max duration:** 8s (this shot: 6s)  
**Freeze:** READY for consumer gen  

---

## SCENE 1 — [LOC_001/DUSK] — magic hour — [LOOK_001]

Purpose: prove Image 2.0 start frame → Video 1.5 I2V download path on SuperGrok Heavy.

```
SHOT:              S01-001
DURATION:          6s
REFS:              [LOC_001/DUSK], [LOOK_001]
FRAMING:           medium-wide, eye-level, doorway centered
LENS:              ~35mm equivalent, deep focus on still; shallow OK on motion hold
CAMERA MOVE:       very slow smooth push-in on locked axis (I2V only; still is lock-off)
LIGHT:             warm tungsten sconce camera-left; cool blue-hour through door; dust beam
ACTION:            Empty corridor and open dark-wood doorway. Dust motes drift in the beam.
                   A thin curtain at the door edge stirs once. No people. Architecture fixed.
SCREEN DIRECTION:  push-in toward doorway (deeper into frame center); no lateral exit
DIALOGUE:          none
LIPSYNC:           NO
VO SEGMENT:        NONE
AUDIO:             soft room tone; gentle air; no dialogue
GEN_PROMPT:        Photoreal cinematic image-to-video from the locked start frame. Same empty
                   narrow corridor and open dark-wood doorway; dust motes drift slowly in a warm
                   light beam; a thin curtain at the door edge stirs once in a faint breeze;
                   exterior dusk light stays consistent. Very slow smooth push-in toward the
                   doorway on a locked axis; no pan, no tilt, no handheld. Quiet atmosphere,
                   soft room tone, gentle air only; continuity with the start frame; do not
                   change architecture, furniture, or time of day. 16:9, 720p, six seconds.
NEGATIVE:          no text, no watermark, no extra people, no distorted hands, no modern
                   anachronisms; no faces; no animals; no handheld shake; no time-of-day jump
```

**Lint:** GEN_PROMPT contains no bracketed IDs.  
**Still prompt (Image 2.0):** see `STILL_PROMPT.md` (separate from motion GEN_PROMPT).  

# Skill: Image-to-video plate lock

**Reinforced by:** practitioner `K-PRAC-GROK-CAMERA-001` (start-frame first; smaller video job).  
**See also:** `START_FRAME_FIRST.md`, `GROK_AS_CAMERA.md`

## When

Hero framing already approved as **storyboard-worthy** still.

## Steps

1. Select LOCKED still (character+env composed or clean plate).  
2. Pass start-frame gate (`START_FRAME_FIRST.md`) before spending video seconds.  
3. Motion prompt describes **only** what changes (SUBJECT + CAMERA + HOLD).  
4. Do not re-describe a different face.  
5. `grok-imagine-video-1.5`, duration 4–10, res 720p (1080p hero).  
6. Multi-take; QC against still + bible (take 1 often not best).  

## Prompt pattern

```text
Animate this exact frame.
SUBJECT: she blinks and exhales.
CAMERA: slow push-in.
HOLD: identity, wardrobe, background layout from start frame.
AUDIO: subtle ambient city hum.
```

# Skill: Start-frame first (storyboard-worthy gate)

**Source:** `K-PRAC-GROK-CAMERA-001`  
**Seats:** R3–R6 (stills), R7 (packet), R8 (I2V), R9 (gate)  

## Rule

**No hero motion gen until start frame is storyboard-worthy.**

## Pipeline

```text
1. Concept + shot list + style template
2. Generate / lock start still via **Imagine Image 2.0** Quality (consumer default)
   — multi-ref / wand / seg / smart resize as needed (`IMAGINE_IMAGE_2_0`)
3. GATE: storyboard-worthy? (composition, identity, costume, readable story beat)
4. If NO → revise still on Image 2.0 (prefer wand/seg over full regen) — do not burn video seconds
5. If YES → I2V with motion-only prompt (Video 1.5)
6. Multi-take → QC → PASS bin
```

## Storyboard-worthy checklist (still)

- [ ] Matches shot card framing intent  
- [ ] Identity matches LOCKED bible (if cast)  
- [ ] Wardrobe/look ID correct  
- [ ] Location/light readable  
- [ ] Hero prop correct if required  
- [ ] No obvious deformity on faces/hands if those are hero  
- [ ] Style contract (grade/lens language) respected  
- [ ] Director or designated still-gate approver OK  

## Why (practitioner)

Nailing start frames gives the video model a **smaller job**: only animate what must happen.

## Factory mapping

| Still approved | Path |
|----------------|------|
| Generate still | Consumer **Image 2.0** Quality (`model_image` log: `imagine-image-2.0-quality`) |
| Yes | `mode: i2v`, `source_still` set, `grok-imagine-video-1.5` |
| No still / B-roll only | `t2v` allowed |
| New staging + identity | `r2v` with refs (still may not be frame 0) |
| API still overflow | `grok-imagine-image-quality` only after spend unlock; Image 2.0 API TBD |

## Naming

`02_refs/...` or `03_shot_list/stills/S07_start_v1.png`  
Motion takes: `04_gen/S07/S07_takeNN.mp4` must cite `start_v1` in packet.

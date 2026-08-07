# MVP Short Film Runbook (30–90s)

**Goal:** First consistent multi-clip piece on **Grok Imagine only**.  
**Timebox:** 1 focused session prepro + 1–2 gen/QC sessions + edit.

## 0. Preconditions

- [ ] Full deploy gate: `05_Workflows/DEPLOYMENT_CHECKLIST.md` sections **A–D** before video spend  
- [ ] `XAI_API_KEY` or SuperGrok consumer access  
- [ ] Read `02_Tools/GROK_IMAGINE_CAPABILITY_MATRIX.md`  
- [ ] Read `03_Knowledge/PRACTITIONER_GROK_AS_CAMERA.md` (Grok-as-camera)  
- [ ] Copy `08_Projects/_template` → `08_Projects/<slug>/`  
- [ ] Human Director available for PASS/FAIL  

## 1. Story lock (30–60 min)

Constraints:

- 1 location  
- ≤2 speaking characters  
- 1 look each  
- ≤1 hero prop  
- 3–7 story beats  

Write in `00_brief/`:

1. Logline (1–2 sentences)  
2. Beat list  
3. Consent note (original characters preferred)  

**Gate:** Director approves beats.

## 2. Style + bibles (60–120 min)

1. Fill `STYLE_CONTRACT.md` (closed camera vocab).  
2. Character bible(s) + generate ref packs via Imagine image.  
3. Environment bible + 2–4 plates.  
4. Props bible if needed.  
5. Mark bibles **LOCKED**.

**Gate:** No gen without LOCKED character pack.

## 3. Shot list (45–90 min)

1. Build 8–20 shot cards (coverage > hero long takes).  
2. Default `mode=i2v` when still exists; `r2v` for new staging.  
3. `duration_target` 4–6s typical.  
4. Freeze shot list version.  
5. Every card answers SUBJECT + CAMERA + HOLD (`03_Knowledge/PRACTITIONER_GROK_AS_CAMERA.md`).

## 3b. Start frames (before motion spend)

1. Generate start stills per hero shot (image quality).  
2. Run storyboard-worthy gate (`06_Skills/generation/START_FRAME_FIRST.md`).  
3. Do not spend video seconds until stills pass.  

## 4. Generate (batch)

Per shot_id:

1. Assemble prompt = SUBJECT + CAMERA + HOLD (+ speech block if dialogue).  
2. Prefer I2V from approved start frame.  
3. Fire `takes_planned` (start with 4–8; take 1 often not best).  
4. Download every result to `04_gen/<shot_id>/`.  
5. Name: `S07_take03.mp4`.

**Imagine defaults:**

- Model: `grok-imagine-video-1.5`  
- Res: 720p  
- Aspect: from style contract  
- Mindset: camera / raw footage engine — edit builds the piece  

## 5. QC (ruthless)

Use `05_Workflows/QC_RUBRICS.md`.

- PASS → copy to `05_pass/` (never overwrite)  
- FAIL → log reason; regen or change mode (edit/extend)  
- Expected keep rate: low; plan volume  

**Gate:** Every timeline shot has ≥1 PASS.

## 6. Assemble + audio

1. CapCut/DaVinci: story order, trim fail tails.  
2. Prefer cutaways over broken motion.  
3. Audio: keep usable native beds; ADR/VO if lips fail.  
4. Export master + optional silent picture lock.

## 7. Deliver

Package in `06_edit/delivery/`:

- Master mp4  
- PASS bin list  
- `09_qc_log/CONTINUITY_REPORT.md`  
- Bible versions used  

## 8. Definition of done

- [ ] 30–90s cut tells the beats  
- [ ] Same faces/wardrobe recognizable across cuts  
- [ ] No unexplained location jumps  
- [ ] QC log exists  
- [ ] Claims labeled if you write a postmortem  

## Anti-goals for MVP

- Multi-act  
- Crowds  
- Fight scenes  
- Four video vendors  
- Embedding databases  

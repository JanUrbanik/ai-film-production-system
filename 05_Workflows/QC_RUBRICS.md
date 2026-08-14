# QC rubrics (PASS/FAIL)

Do not claim these scores come from Grok Imagine. They are **operator rubrics**.

## Take gate — character

FAIL if any:

- [ ] Face ≠ bible (eyes/jaw/skin)  
- [ ] Hair style/color changed  
- [ ] Wardrobe color/pattern wrong  
- [ ] Age/body jumped  
- [ ] Grotesque teeth/eyes  
- [ ] Twin/extra identity appears  

## Take gate — motion

FAIL if any:

- [ ] Limbs melt/split/invert  
- [ ] Foot skate / moonwalk  
- [ ] Head morph mid-clip  
- [ ] Hands are hero of shot AND are blobs/extra fingers  
- [ ] Subject warps under camera move  
- [ ] Background chaos steals face  

## Take gate — world/prop

FAIL if any:

- [ ] Location landmarks wrong  
- [ ] Time-of-day/weather breaks continuity  
- [ ] Hero prop morphs or logo wrong  
- [ ] Scale absurd vs hands  

## Scene gate

Across shot_ids in same scene:

- [ ] Same look IDs  
- [ ] Same light setup family  
- [ ] Geography readable  
- [ ] No unexplained costume reset  

## Sequence / global gate

- [ ] Beats in order  
- [ ] Cast size still under budget  
- [ ] Style contract not abandoned  
- [ ] Audio cast consistent enough for cut  

## Repair ladder (Director 2026-08-13 — 7 steps)

Work top to bottom. Stop at the first fix that works. Identity fail first.

1. Trim to stable region  
2. Insert / OTS / coverage (not the speech-FAIL default)  
3. Local video **edit**  
4. **Extend** from last **good** frame (chain OFF unless junction = Continuous **and** prior PASS)  
5. Regen take — one defect + keep-list (fault note). Spoken line = in-camera re-take, not hide-mouth ADR  
6. **New start frame** if the still itself is the lie  
7. **New `/STATE` + new VDL** if the story actually changed (wet, night, damaged)

**Escalate:** two FAIL cycles on the same shot → Director. Do not burn the pool.  
**Never assemble around a hole.** Assembly reads `MANIFEST.csv` current rows only.

## Log format (`09_qc_log/takes.csv`)

```csv
shot_id,take,mode,request_id,result,fail_tags,notes
S07,03,i2v,uuid,pass,,
S07,04,i2v,uuid,fail,hands;warp,cut at 2.1s usable
```

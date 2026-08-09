# Phase B operator checklist — SuperGrok Heavy

**Do not use API.** Surface: https://grok.com/imagine  

## B1 Auth + usage

- [ ] Logged into SuperGrok Heavy account  
- [ ] Settings → Usage: note % used + reset → `09_qc_log/USAGE_BEFORE.md`  
- [ ] Confirm weekly pool has headroom  

## B2 Still (Image 2.0)

- [ ] Open Imagine → **Quality / Image 2.0**  
- [ ] Paste full prompt from `03_shot_list/STILL_PROMPT.md`  
- [ ] Download →  
  `08_Projects/smoke_imagine_v1/02_refs/start_frames/S01_start_v1.png`  
  (`.jpg` OK if UI exports jpeg)  

## B3 Start-frame gate

- [ ] Fill `03_shot_list/START_FRAME_GATE.md` → **PASS**  
- [ ] If FAIL: edit still on Image 2.0 (wand/seg) or regen; do not I2V  

## B4 I2V (Video 1.5)

- [ ] Upload `S01_start_v1` as start frame  
- [ ] Paste `03_shot_list/I2V_PROMPT.md` (or GEN_PROMPT from SHOT_SCRIPT)  
- [ ] Duration **4–6s**, **720p** if selectable  
- [ ] Download immediately →  
  `08_Projects/smoke_imagine_v1/04_gen/S01/S01_take01.mp4`  

## B5 QC + report

- [ ] Update `09_qc_log/takes.csv` gates  
- [ ] Optional: copy PASS → `05_pass/`  
- [ ] Usage after → `09_qc_log/USAGE_AFTER.md`  
- [ ] Tell agent: **assets landed**  

## Paths (absolute)

```text
/Users/generationalwealth/Desktop/ai-film-production-system/08_Projects/smoke_imagine_v1/02_refs/start_frames/S01_start_v1.png
/Users/generationalwealth/Desktop/ai-film-production-system/08_Projects/smoke_imagine_v1/04_gen/S01/S01_take01.mp4
```

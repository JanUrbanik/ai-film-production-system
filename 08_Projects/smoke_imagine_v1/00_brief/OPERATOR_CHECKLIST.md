# Phase B operator checklist — SuperGrok Heavy

**Do not use API.** Surface: https://grok.com/imagine  

## B1 Auth + usage

- [x] Agent opened Usage/Imagine URLs (2026-08-09)  
- [ ] Logged into SuperGrok Heavy account *(Director)*  
- [ ] Settings → Usage: note % used + reset → `09_qc_log/USAGE_BEFORE.md` *(Director)*  
- [ ] Confirm weekly pool has headroom *(Director)*  

## B2 Still (Image 2.0)

- [x] Still prompt on clipboard + `/tmp/smoke_still_prompt.txt` (agent)  
- [ ] Open Imagine → **Quality / Image 2.0** *(Director)*  
- [ ] Paste still prompt *(Director — clipboard ready)*  
- [ ] Download →  
  `08_Projects/smoke_imagine_v1/02_refs/start_frames/S01_start_v1.png`  
  (`.jpg` OK if UI exports jpeg)  

## B3 Start-frame gate

- [ ] Fill `03_shot_list/START_FRAME_GATE.md` → **PASS**  
- [ ] If FAIL: edit still on Image 2.0 (wand/seg) or regen; do not I2V  

## B4 I2V (Video 1.5)

- [x] I2V prompt staged `/tmp/smoke_i2v_prompt.txt` (agent)  
- [ ] Upload `S01_start_v1` as start frame  
- [ ] Paste `03_shot_list/I2V_PROMPT.md` (or GEN_PROMPT from SHOT_SCRIPT)  
- [ ] Duration **4–6s**, **720p** if selectable  
- [ ] Download immediately →  
  `08_Projects/smoke_imagine_v1/04_gen/S01/S01_take01.mp4`  

## B5 QC + report

- [x] Execution report written: `09_qc_log/OPERATOR_CHECKLIST_EXECUTION_20260809.md`  
- [ ] Update `09_qc_log/takes.csv` gates  
- [ ] Optional: copy PASS → `05_pass/`  
- [ ] Usage after → `09_qc_log/USAGE_AFTER.md`  
- [ ] Tell agent: **assets landed**  

**Agent result 2026-08-09:** B2–B5 blocked without interactive SuperGrok gens. API pixels not used.  

## Paths (absolute)

```text
/Users/generationalwealth/Desktop/ai-film-production-system/08_Projects/smoke_imagine_v1/02_refs/start_frames/S01_start_v1.png
/Users/generationalwealth/Desktop/ai-film-production-system/08_Projects/smoke_imagine_v1/04_gen/S01/S01_take01.mp4
```

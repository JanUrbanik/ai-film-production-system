# Phase B smoke — manual next steps (Director)

**As-of:** 2026-08-09  
**Status:** Pack frozen · agent checklist run · **blocked on consumer pixels**  
**Why blocked:** SuperGrok Heavy **consumer** Imagine is mandatory; agents cannot headless-generate stills/I2V without breaking spend law. API key in shell is **invalid (403)** and must **not** be used for smoke pixels anyway.

**Authoritative checklist:** `OPERATOR_CHECKLIST.md`  
**Execution log:** `../09_qc_log/OPERATOR_CHECKLIST_EXECUTION_20260809.md`  
**Smoke report:** `../../../07_Outputs/IMAGINE_SMOKE_20260809.md`

---

## Blockages (current)

| ID | Blockage | Owner | Unblock when |
|----|----------|-------|----------------|
| BLK-1 | No interactive SuperGrok session in agent | Director | You are logged into Heavy on grok.com |
| BLK-2 | Weekly Usage % not recorded | Director | Fill `09_qc_log/USAGE_BEFORE.md` |
| BLK-3 | No start still on disk | Director | Save `02_refs/start_frames/S01_start_v1.png` |
| BLK-4 | Start-frame gate not run | Director | PASS `03_shot_list/START_FRAME_GATE.md` |
| BLK-5 | No I2V mp4 on disk | Director | Save `04_gen/S01/S01_take01.mp4` |
| BLK-6 | QC/report not closable | Agent | After files land + you say **assets landed** |
| BLK-7 | Shell `XAI_API_KEY` → API 403 | Director (optional) | Ignore for smoke; fix console key only if later unlocking API |

**Do not:** run API image/video to “force” Phase B while Heavy weekly pool remains.

---

## Manual execution (order matters)

### 1. Usage (2 min)

1. Open https://grok.com → **Settings → Usage** (Heavy account).  
2. Fill `09_qc_log/USAGE_BEFORE.md` (% used, reset time).  
3. Confirm headroom for **1 still + 1× ~6s video**.

### 2. Still — Image 2.0 Quality (3–5 min)

1. Open https://grok.com/imagine  
2. Select **Quality / Imagine Image 2.0** (not speed-only if picker shows both).  
3. Paste prompt from either:
   - `03_shot_list/STILL_PROMPT.md` (fenced ```text``` block), or  
   - `/tmp/smoke_still_prompt.txt` if still present from agent run  
4. Download → save as:

```text
/Users/generationalwealth/Desktop/ai-film-production-system/08_Projects/smoke_imagine_v1/02_refs/start_frames/S01_start_v1.png
```

(`.jpg` OK; rename to `S01_start_v1.jpg` and note in gate.)

### 3. Gate (1 min)

1. Open `03_shot_list/START_FRAME_GATE.md`  
2. Check all rows; set **PASS**  
3. If FAIL → edit/regen still on Image 2.0; **do not I2V**

### 4. I2V — Video 1.5 (3–8 min)

1. Same Imagine surface → **image-to-video**  
2. Upload `S01_start_v1` as start frame  
3. Paste `03_shot_list/I2V_PROMPT.md` (or GEN_PROMPT from `SHOT_SCRIPT.md`)  
4. Duration **4–6 s**, **720p** if available  
5. Download immediately →  

```text
/Users/generationalwealth/Desktop/ai-film-production-system/08_Projects/smoke_imagine_v1/04_gen/S01/S01_take01.mp4
```

### 5. Close the loop (2 min)

1. Optionally set takes.csv `gate`/`qc` columns  
2. Fill `09_qc_log/USAGE_AFTER.md`  
3. In chat, reply exactly: **assets landed**  
4. Agent will finalize `07_Outputs/IMAGINE_SMOKE_20260809.md` → COMPLETE  

---

## Success criteria (Phase B exit)

- [ ] `S01_start_v1.png` (or .jpg) exists under `02_refs/start_frames/`  
- [ ] `START_FRAME_GATE.md` = PASS  
- [ ] `S01_take01.mp4` exists under `04_gen/S01/`  
- [ ] Ledger remains `supergrok_heavy_weekly`  
- [ ] API $ for this smoke = **0**  
- [ ] Smoke report status = **COMPLETE**  

---

## If something fails

| Failure | Action |
|---------|--------|
| Still ugly / wrong | Image 2.0 wand/seg or regen; re-gate |
| I2V drifts hard | New take `S01_take02.mp4`; do not overwrite PASS later |
| Weekly pool exhausted | Wait for reset **or** consumer Extra Credits; API only with explicit Director unlock line |
| Wrong account / no Image 2.0 | Confirm SuperGrok Heavy login; Quality Mode GA on consumer |

---

## Paths quick copy

| Role | Absolute path |
|------|----------------|
| Project root | `/Users/generationalwealth/Desktop/ai-film-production-system/08_Projects/smoke_imagine_v1` |
| Still out | `.../02_refs/start_frames/S01_start_v1.png` |
| Video out | `.../04_gen/S01/S01_take01.mp4` |
| Still prompt | `.../03_shot_list/STILL_PROMPT.md` |
| I2V prompt | `.../03_shot_list/I2V_PROMPT.md` |

# Imagine smoke — 2026-08-09 (Phase B)

**Status:** **BLOCKED** — pack frozen + agent checklist done; **manual SuperGrok Heavy gens required**  
**Project:** `08_Projects/smoke_imagine_v1`  
**Kit:** v1.2.4+ · `K-SHOT-SCRIPT-001` pack frozen  
**Spend:** `02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md`  
**Ledger:** `supergrok_heavy_weekly` (**not** xAI API)  
**Operator card:** `08_Projects/smoke_imagine_v1/00_brief/OPERATOR_CHECKLIST.md`  
**Manual next steps:** `08_Projects/smoke_imagine_v1/00_brief/MANUAL_NEXT_STEPS.md`  
**Execution log:** `08_Projects/smoke_imagine_v1/09_qc_log/OPERATOR_CHECKLIST_EXECUTION_20260809.md`

---

## Blockage summary

| ID | Blockage | Severity | Owner |
|----|----------|----------|-------|
| BLK-1 | Consumer Imagine not operable headless by agent | Hard | Director |
| BLK-2 | Weekly Usage % not written to `USAGE_BEFORE.md` | Hard | Director |
| BLK-3 | Start still missing (`S01_start_v1.*`) | Hard | Director |
| BLK-4 | Start-frame gate not PASS | Hard | Director |
| BLK-5 | I2V file missing (`S01_take01.mp4`) | Hard | Director |
| BLK-6 | Smoke report cannot close without assets | Dependent | Agent after handoff |
| BLK-7 | Env `XAI_API_KEY` unusable (403) — **not** used for pixels | Info | Optional later |

**Policy note:** API image/video generation is **out of scope** for this smoke while SuperGrok Heavy weekly pool is the required ledger.

---

## Pack freeze (agent-complete)

| Artifact | Path | Status |
|----------|------|--------|
| Brief | `00_brief/BRIEF.md` | OK |
| Consent | `00_brief/CONSENT.md` | OK |
| Flags | `00_brief/FLAGS.md` | OK |
| Operator checklist | `00_brief/OPERATOR_CHECKLIST.md` | OK |
| Style | `01_bibles/STYLE_CONTRACT.md` | LOCKED |
| Env bible | `01_bibles/ENVIRONMENT_BIBLE.md` | LOCKED |
| Asset Bible | `01_bibles/ASSET_BIBLE.md` | OK (LOC_001/DUSK) |
| Shot Script | `03_shot_list/SHOT_SCRIPT.md` | FROZEN |
| Still prompt | `03_shot_list/STILL_PROMPT.md` | OK Image 2.0 |
| I2V / GEN_PROMPT | `03_shot_list/I2V_PROMPT.md` + packet | OK no IDs |
| Packet | `03_shot_list/packets/S01.json` | `ready` · lint pass |
| Ledger | `09_qc_log/CONTINUITY_LEDGER.csv` | OK |
| Cost sketch | `03_shot_list/COST_SKETCH.md` | OK |
| Gate form | `03_shot_list/START_FRAME_GATE.md` | blank for Director |
| Drop zones | `02_refs/start_frames/`, `04_gen/S01/` | empty |

---

## B1 Auth

| Check | Result |
|-------|--------|
| SuperGrok Heavy | Director-confirmed (~€350) |
| Surface | `grok.com/imagine` |
| Image | **Imagine Image 2.0** Quality |
| Video | **1.5** I2V |
| Usage before | **BLOCKED** — Director must fill `USAGE_BEFORE.md` |
| Browser open Imagine/Usage | Attempted via `open` |
| API key in shell | Present but `/v1/models` → **403 bad-credentials** (not used for pixels) |
| API pixel calls | **NONE** |

## B2 Still

| Field | Value |
|-------|--------|
| Prompt file | `03_shot_list/STILL_PROMPT.md` |
| Model | `imagine-image-2.0-quality` |
| Prompt staged | clipboard + `/tmp/smoke_still_prompt.txt` |
| Target file | `02_refs/start_frames/S01_start_v1.png` |
| On disk | **NO** |

## B3 Start-frame gate

| Field | Value |
|-------|--------|
| Form | `03_shot_list/START_FRAME_GATE.md` |
| Decision | **NOT RUN** (no still) |

## B4 I2V

| Field | Value |
|-------|--------|
| GEN_PROMPT | packet / `I2V_PROMPT.md` / `/tmp/smoke_i2v_prompt.txt` |
| Duration / res | 6s / 720p |
| Target file | `04_gen/S01/S01_take01.mp4` |
| On disk | **NO** |

## B5 QC + cost

| Field | Value |
|-------|--------|
| takes.csv | still PENDING |
| usage_after | blank |
| API $ | **$0** |

## Exit gate

- [ ] Still on disk  
- [ ] Gate PASS  
- [ ] I2V mp4 on disk  
- [ ] takes.csv updated  
- [ ] This report marked COMPLETE  
- [x] No API spend  

---

## Next steps (manual — Director)

Follow in order (full text: `00_brief/MANUAL_NEXT_STEPS.md`):

1. **Usage** — Settings → Usage → fill `09_qc_log/USAGE_BEFORE.md` (clears BLK-2).  
2. **Still** — `grok.com/imagine` → **Image 2.0 Quality** → paste `STILL_PROMPT.md` → save  
   `02_refs/start_frames/S01_start_v1.png` (clears BLK-3).  
3. **Gate** — complete `START_FRAME_GATE.md` → **PASS** (clears BLK-4).  
4. **I2V** — upload still → paste `I2V_PROMPT.md` → 4–6s @ 720p → save  
   `04_gen/S01/S01_take01.mp4` (clears BLK-5).  
5. **Handoff** — optional `USAGE_AFTER.md` + takes.csv → chat: **assets landed** (clears BLK-6).  

**Agent will then:** verify files on disk, update takes/QC, mark this report **COMPLETE**.

**Do not:** use API Imagine to bypass SuperGrok Heavy pool for this smoke.

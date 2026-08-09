# Imagine smoke — 2026-08-09 (Phase B init)

**Status:** CHECKLIST EXECUTED (agent) — **BLOCKED on Director consumer pixels**  
**Execution log:** `08_Projects/smoke_imagine_v1/09_qc_log/OPERATOR_CHECKLIST_EXECUTION_20260809.md`  
**Project:** `08_Projects/smoke_imagine_v1`  
**Kit:** v1.2.4+ · `K-SHOT-SCRIPT-001` pack frozen  
**Spend:** `02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md`  
**Ledger:** `supergrok_heavy_weekly` (**not** xAI API)  
**Operator card:** `08_Projects/smoke_imagine_v1/00_brief/OPERATOR_CHECKLIST.md`

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

**Blocker:** Consumer SuperGrok Imagine requires interactive Director session. Agent cannot complete B2–B5 alone under spend policy.

**Director next:** paste clipboard still → Image 2.0 → download paths in checklist → reply **assets landed**.

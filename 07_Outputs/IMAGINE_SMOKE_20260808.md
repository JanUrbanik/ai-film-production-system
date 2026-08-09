# Imagine smoke — 2026-08-08

**Status:** SUPERSEDED by `IMAGINE_SMOKE_20260809.md` (Phase B pack init)  
**Project:** `08_Projects/smoke_imagine_v1`  
**Kit:** see 20260809 report  
**Spend policy:** `02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md`  
**Ledger:** `supergrok_heavy_weekly` (**not** xAI API)

---

## B1 Auth

| Check | Result |
|-------|--------|
| SuperGrok Heavy plan | Director-confirmed (~€350 tier) |
| Consumer surface | `grok.com/imagine` (required) |
| Image model | **Imagine Image 2.0** Quality Mode |
| Usage checked | _pending Director_ |
| API used | **NO** |

## B2 Still

| Field | Value |
|-------|--------|
| Prompt | `03_shot_list/STILL_PROMPT.md` |
| Model | `imagine-image-2.0-quality` (consumer) |
| File | `02_refs/start_frames/S01_start_v1.*` |
| On disk | PENDING |

## B3 Start-frame gate

| Field | Value |
|-------|--------|
| Form | `03_shot_list/START_FRAME_GATE.md` |
| Decision | PENDING |

## B4 I2V

| Field | Value |
|-------|--------|
| Prompt | `03_shot_list/I2V_PROMPT.md` |
| File | `04_gen/S01/S01_take01.mp4` |
| Duration / res | 4–6s / 720p target |
| On disk | PENDING |

## B5 QC + cost

| Field | Value |
|-------|--------|
| takes.csv | `09_qc_log/takes.csv` |
| usage_before | `09_qc_log/USAGE_BEFORE.md` |
| usage_after % | PENDING |
| QC | PENDING |
| API $ | **$0** (subscription path) |

## Exit gate

- [ ] Real non-`sim_` project has still + I2V on disk  
- [ ] Report ledger = supergrok_heavy_weekly  
- [ ] No unauthorized API spend  

**Next after PASS:** Director may scale takes or open real MVP slug; Phase C team scale still gated by this smoke.

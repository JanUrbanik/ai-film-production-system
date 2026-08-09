# smoke_imagine_v1 — Phase B live pixel smoke

**Mode:** Phase B proof only (not a narrative short)  
**Status:** **BLOCKED — manual SuperGrok Heavy gens required** (pack frozen; agent cannot finish pixels)  
**As-of:** 2026-08-09  
**Ledger (binding):** `supergrok_heavy_weekly` via **consumer** Imagine  
**Policy:** `02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md`  
**Shot law:** `K-SHOT-SCRIPT-001` (`03_shot_list/SHOT_SCRIPT.md`)  
**Do not use** `XAI_API_KEY` for this smoke unless Director unlocks after pool exhaustion.

## Goal

One **Image 2.0** start still → start-frame gate PASS → one **Video 1.5** I2V (4–6s, 720p) on disk → smoke report **COMPLETE**.

## Current blockages

| ID | Issue | Unblock |
|----|--------|--------|
| BLK-1 | No headless consumer Imagine for agents | Director logs into grok.com Heavy |
| BLK-2 | Usage % not filled | `09_qc_log/USAGE_BEFORE.md` |
| BLK-3 | No `S01_start_v1` still | Image 2.0 download to `02_refs/start_frames/` |
| BLK-4 | Gate not run | PASS `START_FRAME_GATE.md` |
| BLK-5 | No `S01_take01.mp4` | I2V download to `04_gen/S01/` |
| BLK-6 | Report not closable | Reply **assets landed** after files exist |
| BLK-7 | Shell API key 403 (if present) | Ignore for smoke; do **not** API-gen |

**Detail:** `00_brief/MANUAL_NEXT_STEPS.md` · `09_qc_log/OPERATOR_CHECKLIST_EXECUTION_20260809.md`

## Pack (agent-ready — frozen)

| Artifact | Path |
|----------|------|
| **Manual next steps** | `00_brief/MANUAL_NEXT_STEPS.md` |
| Operator checklist | `00_brief/OPERATOR_CHECKLIST.md` |
| Shot script | `03_shot_list/SHOT_SCRIPT.md` |
| Still prompt | `03_shot_list/STILL_PROMPT.md` |
| I2V / GEN_PROMPT | `03_shot_list/I2V_PROMPT.md` |
| Packet | `03_shot_list/packets/S01.json` (`ready`, lint pass) |
| Smoke report | `../../07_Outputs/IMAGINE_SMOKE_20260809.md` |

## Operator steps (you — SuperGrok Heavy)

1. Read **`00_brief/MANUAL_NEXT_STEPS.md`** (full procedure).  
2. Tick **`00_brief/OPERATOR_CHECKLIST.md`**.  
3. Summary: Usage → Image 2.0 still → gate PASS → I2V 6s/720p → save paths → **assets landed**.  

## Cost expectation

| Item | Ledger |
|------|--------|
| 1 quality still | SuperGrok Heavy weekly pool |
| 1× ~6s I2V | SuperGrok Heavy weekly pool |
| API | **not used** ($0 this smoke) |

## Related kit docs

- `05_Workflows/PRODUCTION_DEPLOY.md` §5  
- `06_Skills/generation/START_FRAME_FIRST.md`  
- `03_Knowledge/PRACTITIONER_GROK_AS_CAMERA.md`  
- `02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md`  

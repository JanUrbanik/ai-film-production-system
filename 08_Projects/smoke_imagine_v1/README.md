# smoke_imagine_v1 — Phase B live pixel smoke

**Mode:** Phase B proof only (not a narrative short)  
**Status:** **INITIALIZED** — pack frozen; waiting on Director pixels  
**Ledger (binding):** `supergrok_heavy_weekly` via **consumer** Imagine  
**Policy:** `02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md`  
**Shot law:** `K-SHOT-SCRIPT-001` (`03_shot_list/SHOT_SCRIPT.md`)  
**Do not use** `XAI_API_KEY` for this smoke unless Director unlocks after pool exhaustion.

## Goal

One **Image 2.0** start still → start-frame gate PASS → one **Video 1.5** I2V (4–6s, 720p) on disk → smoke report.

## Pack (agent-ready)

| Artifact | Path |
|----------|------|
| Operator checklist | `00_brief/OPERATOR_CHECKLIST.md` |
| Shot script | `03_shot_list/SHOT_SCRIPT.md` |
| Still prompt | `03_shot_list/STILL_PROMPT.md` |
| I2V / GEN_PROMPT | `03_shot_list/I2V_PROMPT.md` |
| Packet | `03_shot_list/packets/S01.json` |
| Smoke report | `../../07_Outputs/IMAGINE_SMOKE_20260809.md` |

## Operator steps (you — SuperGrok Heavy)

Follow **`00_brief/OPERATOR_CHECKLIST.md`** (authoritative). Summary:

1. **Usage** → `09_qc_log/USAGE_BEFORE.md`  
2. https://grok.com/imagine → **Image 2.0 Quality**  
3. Still from `STILL_PROMPT.md` → `02_refs/start_frames/S01_start_v1.png`  
4. Gate `START_FRAME_GATE.md` → PASS  
5. I2V from `I2V_PROMPT.md` → `04_gen/S01/S01_take01.mp4`  
6. Update `takes.csv` / usage after  
7. Reply **assets landed** — agent completes `07_Outputs/IMAGINE_SMOKE_20260809.md`  

## Cost expectation

| Item | Ledger |
|------|--------|
| 1 quality still | SuperGrok Heavy weekly pool |
| 1× ~6s I2V | SuperGrok Heavy weekly pool |
| API | **not used** |

## Related kit docs

- `05_Workflows/PRODUCTION_DEPLOY.md` §5  
- `06_Skills/generation/START_FRAME_FIRST.md`  
- `03_Knowledge/PRACTITIONER_GROK_AS_CAMERA.md`  

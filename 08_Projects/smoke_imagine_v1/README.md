# smoke_imagine_v1 — Phase B live pixel smoke

**Mode:** Phase B proof only (not a narrative short)  
**Ledger (binding):** `supergrok_heavy_weekly` via **consumer** Imagine  
**Policy:** `02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md`  
**Do not use** `XAI_API_KEY` for this smoke unless Director unlocks after pool exhaustion.

## Goal

One start still → start-frame gate PASS → one I2V clip (4–6s, 720p) on disk → smoke report.

## Operator steps (you — SuperGrok Heavy)

1. **Usage check** — grok.com → Settings → Usage  
   - Record % used + weekly reset in `09_qc_log/USAGE_BEFORE.md`
2. Open **https://grok.com/imagine** (logged into Heavy account)
3. **Still** — paste prompt from `03_shot_list/STILL_PROMPT.md`  
   - Use **Imagine Image 2.0** / Quality Mode (not legacy speed-only if picker shows both)  
   - Download → `02_refs/start_frames/S01_start_v1.png` (or .jpg)
4. **Gate** — fill `03_shot_list/START_FRAME_GATE.md` (PASS required)
5. **I2V** — upload start frame; paste motion prompt from `03_shot_list/I2V_PROMPT.md`  
   - Duration **4–6s**, resolution **720p** if selectable  
   - Download immediately → `04_gen/S01/S01_take01.mp4`
6. **QC** — fill `09_qc_log/takes.csv` + optional PASS copy to `05_pass/`
7. Tell the agent: *“assets landed”* — agent finalizes `07_Outputs/IMAGINE_SMOKE_20260808.md`

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

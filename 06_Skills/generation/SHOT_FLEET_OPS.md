# Skill: Shot fleet ops

## Meaning
Parallelism = multiple **R8 workers** or multiple jobs, not unique agent species.

## Worker IDs (Phase C)
- Format: `R8-01` … `R8-N` (zero-pad 2 digits).  
- Assigned by **R1b** (Episode/Feature) or R1 (MVP).  
- Log every take with `worker=R8-0x` in `takes.csv` notes or cost_ledger.

## Patterns
1. **Multi-take:** same packet, takes 01…K  
2. **Multi-shot:** different shot_ids after lock  
3. **Multi-edit branch:** concurrent edits from one source video  

## Naming
`04_gen/S07/S07_take03.mp4`  
Worker tag in log: `R8-02`  
Never two workers write the same `shot_id` directory concurrently.

## Defaults
| Mode | takes K | max concurrent jobs |
|------|---------|---------------------|
| MVP | 4–8 | 2–3 |
| Episode | 4–8 | 3 (Director may raise) |
| Feature | per R1b cap | per global ceiling |

Spend: SuperGrok Heavy weekly pool first; log ledger per batch.

## Cost
Row per take in `09_qc_log/cost_ledger.csv` (sequence, shot_id, take, ledger, model).

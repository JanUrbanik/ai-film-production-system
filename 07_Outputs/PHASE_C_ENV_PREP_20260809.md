# Phase C environment prep — 2026-08-09

**Context:** HANDOFF order A → **B** → **C**. Phase B smoke is still **BLOCKED** on Director consumer pixels.  
**Action taken:** Scaffold Phase C **docs/tooling only** so Episode scale can start immediately after B exit — without skipping B for pilots (Phase E).

## HANDOFF next-after-smoke

| Phase | Name | Status |
|-------|------|--------|
| B | Live pixel proof | BLOCKED — manual SuperGrok gens |
| **C** | Scale production team | **ENV PREPARED** (this note) |
| D | Advanced plugins | Wait for B (+ prefer C seats first) |
| E | Pilot productions | Must not start before B exit |

## Scaffolded artifacts

| Item | Path |
|------|------|
| R1b seat | `03_Roles/seats/R1b_Sequence_Manager.md` |
| Episode activation | `07_Prompts/FILM_TEAM_ACTIVATION_EPISODE.md` |
| Feature activation | `07_Prompts/FILM_TEAM_ACTIVATION_FEATURE.md` |
| Sequence board template | `05_Workflows/templates/SEQUENCE_BOARD.md` |
| Showrunner freeze checklist | `05_Workflows/templates/SHOWRUNNER_FREEZE_CHECKLIST.md` |
| Cost ledger template | `08_Projects/_template/09_qc_log/cost_ledger.csv` |
| Packet validator | `scripts/validate_packets.py` |
| R8 fleet skill bump | `06_Skills/generation/SHOT_FLEET_OPS.md` (if updated) |
| Sequence QC note | `05_Workflows/CONTINUITY_GATES.md` Gate 3 flesh |

## Verify commands (prep health)

```bash
export PATH="$HOME/.grok/bin:$PATH"
cd /Users/generationalwealth/Desktop/ai-film-production-system
./scripts/verify_plugin_stack.sh
python3 scripts/validate_packets.py 08_Projects/smoke_imagine_v1/03_shot_list/packets/
```

## Still required before Phase C “exit gate”

- [ ] Phase B smoke COMPLETE (still + I2V on disk)  
- [ ] Multi-sequence **dry-run** using R1b + ≥2 R8 workers + sequence QC log  
- [ ] Optional: tag release after C1 docs land  

## Do not

- Install exa/figma (Phase D) as substitute for C  
- Start real Episode pilot (E) before B  
- Unlock API Imagine while Heavy pool remains without Director line  

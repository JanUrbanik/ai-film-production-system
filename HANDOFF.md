# HANDOFF — AI Film Production System + CineAgent Studio

**Updated:** 2026-08-13 (Build Mode — post AGI audit fixes)  
**Supersedes:** 2026-08-10 “Phase B blocked / Studio not built” and any M0-only report.  
**GitHub Desktop clone:** still **behind** unless Jan synced. Live disk = this Build `demo-factory`.

## One-screen

| Layer | State |
|-------|--------|
| Factory laws | Production-ready + CineKit `[M]` (LAWs 4–6) |
| Phase A | CLOSED |
| Phase B smoke | **LANDED** — `S01_start_v1.png` + `S01_take01.mp4` |
| CineAgent Studio | Past M0 — Ingest, Generation, Manifest, Continuity Gate 1 |
| Packet status enum | includes `landed`, `regen_requested` + `additionalProperties` |
| Speech | `LIPSYNC:YES` in-camera; FAIL = re-take (not hide-mouth) |
| Repair ladder | **7 steps** + 2-FAIL escalate |
| FLAGS | `DIRECTOR_OK.md` required before plates / hero I2V |
| VDL | AWAITING until approved still; CHAR/PROP awaiting **blocks** hero I2V |
| Continuity | Gate 1 computed from disk; Gates 2–4 **pending** (not fake FAIL) |
| Masters | `readManifest` only — no `04_gen/` glob |
| First 60–90s film | Not started |

## Do not

- Rebuild Studio M0 or re-run Phase B from stale docs  
- Hide mouths on speech FAIL  
- Call Imagine API unless Director unlock  
- Push GitHub from a clone missing these files  
- Let AGI self-approve FLAGS  
- Assemble around a hole / glob rejects  

## Order

Transcript → Identify → Convert → **Director OK** → 3+1 plates → VDL from still → start frames → I2V → fault/re-take → MANIFEST `pass` → cut.

## Laws

K-SHOT-SCRIPT-001 (REFS ≠ GEN_PROMPT).  
LAW 4–6. Matrix wins vs CineKit if they fight. `[M]` = process, not verified Grok behavior.

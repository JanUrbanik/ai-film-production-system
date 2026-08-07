# AI Film Production System

**Status:** v1.0 production team kit (Imagine-first)  
**Date:** 2026-08-07  
**Root:** `/Users/generationalwealth/Desktop/ai-film-production-system`  
**Relationship:** Separate production factory. Master Builder Team is the optional **governance OS**, not the film runtime.

## What this is

A practical, honesty-labeled system for making **short-to-long AI narrative video** with:

1. Locked **Character / Environment / Props** bibles  
2. Shot cards + short-clip generation  
3. **Grok Imagine** as the default generation path (API + consumer surface)  
4. Human QC gates (not fake universal “consistency scores”)  
5. Edit/audio assembly as where the “movie” appears  

## What this is not

- Not a one-prompt feature film  
- Not a merge into Master Builder’s 16 seats  
- Not a guarantee of perfect face/motion lock  
- Not a claim that every model in old diagrams is required  

## Start here (operators)

| Order | Doc | Why |
|------:|-----|-----|
| 1 | `01_Architecture/ONE_PAGE_FACTORY_LAW.md` | Printable law |
| 2 | `03_Roles/PRODUCTION_TEAM.md` + `seats/` | Callable film team |
| 3 | `07_Prompts/FILM_TEAM_ACTIVATION.md` | Start a production session |
| 4 | `02_Tools/GROK_IMAGINE_CAPABILITY_MATRIX.md` | Imagine truth |
| 5 | `05_Workflows/MVP_SHORT_FILM_RUNBOOK.md` | MVP path |
| 6 | `05_Workflows/INJECTION_ENGINE.md` + engines/ | Bibles → packets |
| 7 | `09_Bridge/MASTER_BUILDER_HANDOFF.md` | Builder governance bridge |

## Modes

| Mode | Target | Default tools |
|------|--------|---------------|
| **MVP Short** | 30–90s multi-clip piece | Grok Imagine only + CapCut/DaVinci |
| **Episode** | 3–12 min | Imagine-first; optional adapters |
| **Feature factory** | Multi-act | Same architecture scaled; more QC, not more magic |

## Hard rules (print these)

1. Continuity is enforced **between** clips, not hoped for inside one long gen.  
2. No identity without reference images.  
3. Few faces, few outfits, few locations.  
4. Short clips (default 4–8s; API max 15s).  
5. One camera move + one action per gen.  
6. Reject more than you keep.  
7. Edit hides sin; audio sells continuity.  
8. Label every tool claim: **Verified / Assumed / Speculative**.  
9. Grok Imagine is default; other models are **adapters**, not requirements.  
10. Human Director owns final taste and PASS/FAIL.

## Folder map

```text
00_Epistemics/          claim labels, anti-hype
01_Architecture/        canonical pipeline + diagram corrections
02_Tools/               Imagine matrix + adapters + contracts
03_Roles/               production roles (not 16 Builder seats)
04_Bibles/              templates for char/env/props
05_Workflows/           MVP + feature + QC
06_Skills/              reusable prompt/ops skills
07_Prompts/             kickoff + shot templates
08_Projects/            real project worktrees
09_Bridge/              Master Builder handoff
10_Sources/             diagrams + research snapshots
```

## Relationship to Master Builder Team

| System | Owns |
|--------|------|
| `master-builder-team` | ADOPT A governance, research, tool rating, truth gates |
| `ai-film-production-system` | Film factory: bibles, shots, Imagine gen, QC, edit |

Bridge: charter a FULL job in Master Builder → deliver a film project brief → execute here → return masters + QC report.

## Sources integrated

- Desktop diagrams (`2flowd/`, `new vid systal/`) — corrected in architecture  
- `master-builder-team/01_Context/LONGFORM_AI_VIDEO_CONSISTENCY_WORKFLOW.md`  
- Official xAI Imagine docs (2026): video gen/edit/extend/reference-to-video, image gen/edit  

## Version

| Ver | Date | Notes |
|-----|------|-------|
| 0.1 | 2026-08-06 | Initial separate system + Imagine-first integration |
| 1.0 | 2026-08-07 | Master Builder FULL harden: seats, engines, schema, stress test |

# AI Film Production System

**Status:** v1.2.1 production-ready kit (Imagine-first + Grok-as-camera + marketplace plugins)  
**Date:** 2026-08-08  
**Release:** https://github.com/JanUrbanik/ai-film-production-system/releases  
**Deploy:** `05_Workflows/DEPLOYMENT_CHECKLIST.md` · **Status:** `PROJECT_STATUS.md` · **Changelog:** `CHANGELOG.md`  
**Plugins:** `02_Tools/plugins/` · `.grok/config.toml` · verify: `./scripts/verify_plugin_stack.sh`  
**Root:** `/Users/generationalwealth/Desktop/ai-film-production-system`  
**Relationship:** Separate production factory. Master Builder Team is the optional **governance OS**, not the film runtime.

## What this is

A practical, honesty-labeled system for making **short-to-long AI narrative video** with:

1. Locked **Character / Environment / Props** bibles  
2. Shot cards + short-clip generation  
3. **Grok Imagine** as the default generation path (API + consumer surface)  
4. **Grok-as-camera** method (start-frame first; SUBJECT + CAMERA + HOLD)  
5. Human QC gates (not fake universal “consistency scores”)  
6. Edit/audio assembly as where the “movie” appears  
7. Optional **Grok Build marketplace plugins** for research / verify / plan only  

## What this is not

- Not a one-prompt feature film  
- Not a merge into Master Builder’s 16 seats  
- Not a guarantee of perfect face/motion lock  
- Not a claim that every model in old diagrams is required  

## Start here (operators)

| Order | Doc | Why |
|------:|-----|-----|
| 1 | `PROJECT_STATUS.md` | What is final vs not |
| 2 | `05_Workflows/DEPLOYMENT_CHECKLIST.md` | Ship gate A–H |
| 3 | `01_Architecture/ONE_PAGE_FACTORY_LAW.md` | Printable law |
| 4 | `03_Roles/PRODUCTION_TEAM.md` + `seats/` | Callable film team |
| 5 | `07_Prompts/FILM_TEAM_ACTIVATION.md` | Start a production session |
| 6 | `02_Tools/GROK_IMAGINE_CAPABILITY_MATRIX.md` | Imagine truth |
| 6b | `02_Tools/plugins/GROK_MARKETPLACE_INTEGRATION.md` | Expandable Grok Build plugins |
| 7 | `05_Workflows/MVP_SHORT_FILM_RUNBOOK.md` | MVP path |
| 8 | `05_Workflows/INJECTION_ENGINE.md` + engines/ | Bibles → packets |
| 9 | `03_Knowledge/PRACTITIONER_GROK_AS_CAMERA.md` | Grok-as-camera method (Odyssey) |
| 10 | `09_Bridge/MASTER_BUILDER_HANDOFF.md` | Builder governance bridge |

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
11. Marketplace plugins never replace Imagine or bypass bible/start-frame gates.

## Grok toolkit marketplace integration

This factory is wired to the **xAI Grok Build Plugin Marketplace** (`xai-org/plugin-marketplace`). Plugins expand **research, verification, and planning** — they do **not** generate film pixels.

### Enabled stack (installed on operator machine)

| Plugin | Role in this factory |
|--------|----------------------|
| **superpowers** | Plans, verification-before-completion, systematic debugging |
| **firecrawl** | Scrape/crawl docs and public pages → `10_Sources/research/` |
| **tavily** | Structured web search with citations |
| **chrome-devtools** | Live browser checks when a claim depends on a web UI/page |

### Where it lives in the repo

| Path | Purpose |
|------|---------|
| `02_Tools/plugins/GROK_MARKETPLACE_INTEGRATION.md` | Full policy, catalog, seat map, forbidden uses |
| `02_Tools/plugins/INSTALLED_STACK.snapshot.json` | Snapshot of local installs (no secrets) |
| `02_Tools/plugins/README.md` | Plugins folder index |
| `.grok/config.toml` | Project plugin stack declaration |
| `.grok/rules.md` | Grok Build hard rules for this factory |
| `05_Workflows/PLUGIN_AUGMENTED_RESEARCH.md` | Optional research branch workflow |
| `06_Skills/ops/PLUGIN_STACK.md` | Operator skill card |
| `scripts/verify_plugin_stack.sh` | One-command health check |

### How it fits the production path

```text
Core MVP (pixels)
  deploy checklist → bibles → start frames → Imagine I2V → QC → edit

Optional plugin branch (expandable)
  tavily / firecrawl / chrome-devtools / superpowers
  → labeled notes in 10_Sources/research/
  → resume core path (no gate bypass)
```

### Verify marketplace integration

```bash
export PATH="$HOME/.grok/bin:$PATH"
cd /path/to/ai-film-production-system
./scripts/verify_plugin_stack.sh    # expect exit 0
grok mcp doctor                     # expect 0 failing when using MCP
```

Latest verify artifact: `07_Outputs/PLUGIN_STACK_VERIFY_20260808.md`  
Full E2E (post Tavily OAuth fix): `07_Outputs/E2E_PLUGIN_WORKFLOW_TEST_2026-08-08.md`

### Auth notes

- Tavily/Firecrawl use OAuth via Grok MCP credentials (`~/.grok/mcp_credentials.json`).  
- If `grok mcp doctor` shows Tavily failing: re-auth in Grok TUI (`/mcp`) or re-run OAuth.  
- Do not commit API keys or `auth.json`.

### Not enabled by default

Catalog-only until Director approves install: exa, figma, vercel, neon, mongodb, stripe, railway, cloudflare, sentry, axiom, tinyfish, …

## Folder map

```text
.grok/                  Grok Build project config + plugin stack
scripts/                verify_plugin_stack.sh and tooling
00_Epistemics/          claim labels, anti-hype
01_Architecture/        canonical pipeline + diagram corrections
02_Tools/               Imagine matrix + adapters + plugins/
03_Knowledge/           practitioner method briefs (always-on)
03_Roles/               production roles (not 16 Builder seats)
04_Bibles/              templates for char/env/props
05_Workflows/           MVP + feature + QC + plugin research
06_Skills/              reusable prompt/ops skills (incl. ops/)
07_Prompts/             kickoff + shot templates
07_Outputs/             verification reports (kit-level)
08_Projects/            real project worktrees
09_Bridge/              Master Builder handoff
10_Sources/             diagrams + research + practitioner transcripts
CHANGELOG.md            release history
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
- Practitioner: Odyssey / Grok-as-camera method — https://www.youtube.com/watch?v=ZRtT-0SUw8M (`10_Sources/practitioners/`, `03_Knowledge/PRACTITIONER_GROK_AS_CAMERA.md`)  
- Grok Build marketplace — https://github.com/xai-org/plugin-marketplace (`02_Tools/plugins/`)  

## Version

| Ver | Date | Notes |
|-----|------|-------|
| 0.1 | 2026-08-06 | Initial separate system + Imagine-first integration |
| 1.0 | 2026-08-07 | Master Builder FULL harden: seats, engines, schema, stress test |
| 1.1 | 2026-08-07 | Ingest PRAC-2026-001 Grok-as-camera / start-frame-first skills |
| 1.1-docs | 2026-08-07 | Deployment checklist + PROJECT_STATUS finalization |
| 1.2 | 2026-08-08 | Marketplace plugin stack integrated into factory workflows |
| 1.2.1 | 2026-08-08 | README marketplace docs; verify script + stack snapshot; release finalize |

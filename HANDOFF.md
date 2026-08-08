# HANDOFF — AI Film Production System

**For:** New agent chats / Human Director  
**Updated:** 2026-08-08  
**Kit version:** **v1.2.1** (tags `v1.2`, `v1.2.1` on `main`)  
**HEAD (at handoff write):** `7663f7c` — scale roadmap landed  
**Working tree expectation:** clean `main` == `origin/main` unless noted  

---

## 1. What this project is

| | |
|--|--|
| **Name** | AI Film Production System |
| **Root** | `/Users/generationalwealth/Desktop/ai-film-production-system` |
| **GitHub** | https://github.com/JanUrbanik/ai-film-production-system |
| **Role** | **Production factory** for short-to-long AI narrative video |
| **Not** | Master Builder’s 16 seats; not a finished feature film |

**Sister system (governance only):**  
`/Users/generationalwealth/Desktop/master-builder-team`  
- Pointer: `master-builder-team/01_Context/FILM_SYSTEM_POINTER.md`  
- Do **not** merge film seats into Builder `02_Agents/`.

---

## 2. Hard laws (non-negotiable)

1. **Imagine-first** pixels (`grok-imagine-image*`, `grok-imagine-video-1.5`).  
2. **Grok-as-camera:** start-frame first; prompt **SUBJECT + CAMERA + HOLD**; multi-take; edit assembles.  
3. **No identity without refs**; few faces/outfits/locations; short clips (API max 15s).  
4. **Human Director** = user — final PASS/FAIL, budget, consent, adapter/plugin spend.  
5. **Binary QC** — no fake native “92/100” consistency scores.  
6. **Multi-vendor video** (Kling/Veo/Seedance/…) = **adapter tier only**, never default fanout.  
7. **Marketplace plugins** = research / verify / plan only — **never** replace Imagine or bypass bible/start-frame gates.  
8. Claim labels: **Verified / Assumed / Speculative**.  
9. Prefer NordVPN **off** or **split-tunnel Warp** during long agent/MCP sessions.  

---

## 3. Current state (what’s done)

### 3.1 Kit capabilities

| Area | Status | Where |
|------|--------|--------|
| Constitution / one-page law | Done | `AGENTS.md`, `01_Architecture/ONE_PAGE_FACTORY_LAW.md` |
| Pipeline | Done | `01_Architecture/CANONICAL_PIPELINE.md` |
| Imagine matrix + adapters | Done | `02_Tools/GROK_IMAGINE_*`, `ADAPTER_POLICY.md` |
| Shot packet schema | Done | `02_Tools/schemas/shot_packet.schema.json` |
| Production seats R1–R12 | Done | `03_Roles/PRODUCTION_TEAM.md`, `seats/` |
| Bible engines + templates | Done | `04_Bibles/`, `05_Workflows/engines/` |
| MVP / feature / QC / injection | Done | `05_Workflows/*` |
| Deploy checklist | Done | `05_Workflows/DEPLOYMENT_CHECKLIST.md` |
| Grok-as-camera knowledge + skills | Done | `03_Knowledge/`, `06_Skills/generation/` |
| Marketplace core plugins | Done | superpowers, firecrawl, tavily, chrome-devtools |
| Plugin policy + verify script | Done | `02_Tools/plugins/`, `scripts/verify_plugin_stack.sh` |
| Activation prompts | Done | `07_Prompts/FILM_TEAM_ACTIVATION.md` |
| Scale roadmap | Done | `06_Roadmaps/ROADMAP_SCALE_TEAM_AND_ADVANCED_PLUGINS.md` |
| Releases | Done | GitHub Releases **v1.2**, **v1.2.1** |

### 3.2 Verification already run

| Test | Result | Path |
|------|--------|------|
| Plugin stack script | 16 PASS / 0 FAIL | `07_Outputs/PLUGIN_STACK_VERIFY_20260808.md` |
| Plugin E2E (post Tavily OAuth) | PASS, MCP 4/4 | `07_Outputs/E2E_PLUGIN_WORKFLOW_TEST_2026-08-08.md` |
| Final kit E2E (docs+sim+plugins) | PASS | `07_Outputs/FINAL_E2E_PRODUCTION_WORKFLOW_2026-08-08.md` |
| MVP dry-run sim | Packets/QC OK | `08_Projects/sim_mvp_deploy_v1/` |

### 3.3 Known environment notes

- **Tavily:** Was broken (expired OAuth); fixed via PKCE re-auth into `~/.grok/mcp_credentials.json`. May expire ~24h — re-auth via Grok TUI `/mcp` if doctor fails.  
- **Firecrawl / chrome-devtools / superpowers:** Were healthy at last verify.  
- **Grok CLI:** On PATH via `~/.grok/bin`.  
- **NordVPN:** Caused Warp agent drops when full-tunnel; keep off or split-tunnel Warp.  
- **`PROJECT_STATUS.md`** may still say “GitHub remote = local only” in one table row — **stale**; remote is live (fix when touching that file).  

---

## 4. Open / not done

| Item | Priority |
|------|----------|
| Live **Imagine still → I2V smoke** (real paid/API pixels) | **P0** before scaling spend |
| First **real** project slug (not `sim_*`) | **P0/P1** |
| Archive `08_Projects/sim_grok_camera_v1` + `sim_mvp_deploy_v1` → `11_Archive/simulations/` | **P1** hygiene |
| `05_Workflows/PRODUCTION_DEPLOY.md` | **P1** |
| R1b Sequence Manager as own seat + Episode activation prompts | **P1** (scale) |
| Advanced plugins (exa, figma, …) under admission control | **P2** after hygiene + smoke |
| Fuller Odyssey transcript → knowledge bump | **P3** |
| Multi-vendor adapters | **P3** only on named failure class |

---

## 5. Next development phase (roadmap pointer)

**Canonical plan:**  
`06_Roadmaps/ROADMAP_SCALE_TEAM_AND_ADVANCED_PLUGINS.md`

| Phase | Name | Intent |
|-------|------|--------|
| **A** | Hygiene & handoff | This file, archive sims, status fixes, PRODUCTION_DEPLOY |
| **B** | Live pixel proof | One real I2V clip + smoke report |
| **C** | Scale production team | R1b, Episode/Feature activation, R8 fleet, sequence QC, cost ledger |
| **D** | Advanced marketplace plugins | Admission control; exa/figma first; verify script updates |
| **E** | Pilot productions | Real MVP short → Episode slice → parallel R8 stress |
| **F** | Continuous improvement | Matrix re-verify, adapters, Builder charters as needed |

**Order rule:** A → B before heavy C/E. **Scale seats before scale plugins.** Never skip B before E.

### Advanced plugin candidates (not installed by default)

| Priority | Plugin | Use |
|----------|--------|-----|
| P1 | exa | Research A/B vs tavily |
| P1 | figma | Lookboards / still direction |
| P2 | tinyfish | Browse assist vs chrome-devtools |
| P2–P3 | neon/mongo, vercel/… | Only after real MVP exists |
| Skip | stripe | Unless commerce |

Every new plugin: Director charter → install → auth → config → seat map → verify script → pilot note → **no pixel-path bypass**.

---

## 6. How to operate (quick)

```bash
export PATH="$HOME/.grok/bin:$PATH"
cd /Users/generationalwealth/Desktop/ai-film-production-system
git pull origin main
./scripts/verify_plugin_stack.sh          # expect exit 0
# optional: grok mcp doctor
```

**Start a production session:** load `07_Prompts/FILM_TEAM_ACTIVATION.md`  
**MVP path:** `05_Workflows/MVP_SHORT_FILM_RUNBOOK.md`  
**Before video $:** `05_Workflows/DEPLOYMENT_CHECKLIST.md` sections **A–D**  
**New project:** `cp -R 08_Projects/_template 08_Projects/<slug>`  

---

## 7. Key paths (load order for new agents)

1. `HANDOFF.md` ← you are here  
2. `06_Roadmaps/ROADMAP_SCALE_TEAM_AND_ADVANCED_PLUGINS.md`  
3. `PROJECT_STATUS.md`  
4. `README.md`  
5. `01_Architecture/ONE_PAGE_FACTORY_LAW.md`  
6. `05_Workflows/DEPLOYMENT_CHECKLIST.md`  
7. `03_Knowledge/PRACTITIONER_GROK_AS_CAMERA.md`  
8. `02_Tools/plugins/GROK_MARKETPLACE_INTEGRATION.md`  
9. `07_Outputs/FINAL_E2E_PRODUCTION_WORKFLOW_2026-08-08.md`  
10. `03_Roles/PRODUCTION_TEAM.md`  

---

## 8. Starter prompt for a new chat

```text
Continue AI Film Production System.

Root: /Users/generationalwealth/Desktop/ai-film-production-system
Repo: https://github.com/JanUrbanik/ai-film-production-system
Branch: main (releases v1.2 / v1.2.1). Kit is production-ready docs+tooling; not a finished film.

Read FIRST and obey:
HANDOFF.md
06_Roadmaps/ROADMAP_SCALE_TEAM_AND_ADVANCED_PLUGINS.md
PROJECT_STATUS.md
README.md
05_Workflows/DEPLOYMENT_CHECKLIST.md
01_Architecture/ONE_PAGE_FACTORY_LAW.md
03_Knowledge/PRACTITIONER_GROK_AS_CAMERA.md
02_Tools/plugins/GROK_MARKETPLACE_INTEGRATION.md

Laws: Imagine-first; Grok-as-camera (start-frame first; SUBJECT+CAMERA+HOLD); plugins=research/verify/plan only; no multi-vendor default; separate from master-builder-team; Human Director=me; Verified/Assumed/Speculative labels.

Open work per HANDOFF: Phase A hygiene (archive sims, PRODUCTION_DEPLOY, status fix) → Phase B Imagine smoke → Phase C team scale → Phase D advanced plugins.

My next task: [Phase A | Phase B smoke | start real MVP slug ___ | install plugin ___]

Confirm reads in ≤10 bullets, then execute. Stop for approval before paid Imagine volume or new plugin installs.
```

---

## 9. Immediate recommended next tasks (pick one)

1. **Phase A:** Archive `sim_*`, add `PRODUCTION_DEPLOY.md`, fix `PROJECT_STATUS` GitHub row, commit/push.  
2. **Phase B:** Run one paid/API Imagine still→I2V smoke; write `07_Outputs/IMAGINE_SMOKE_*.md`.  
3. **Phase C start:** Author `R1b_Sequence_Manager.md` + Episode activation prompt.  
4. **Phase D start:** Director-charter + install **exa** or **figma** only after A/B.  

---

## 10. Document control

| Ver | Date | Notes |
|-----|------|-------|
| 1.0 | 2026-08-08 | Initial handoff for new-chat continuity at kit v1.2.1 + scale roadmap |

**Maintainer:** Update this file at the end of each major session (HEAD, open work, blockers).

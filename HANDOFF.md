# HANDOFF — AI Film Production System

**For:** New agent chats / Human Director  
**Updated:** 2026-08-08  
**Kit version:** **v1.2.3** (tags `v1.2`, `v1.2.1`, `v1.2.3` on `origin`)  
**HEAD (at handoff write):** `a356bc4` — `main` == `origin/main` @ tag `v1.2.3`  
**Working tree expectation:** clean unless mid-session edits  
**Verified this session:** 2026-08-08 — plugin verify 16/16 exit 0 after push; Phase A exit complete  

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

1. **Imagine-first** pixels — stills: **Image 2.0** consumer Quality; motion: `grok-imagine-video-1.5`.  
2. **Grok-as-camera:** start-frame first; prompt **SUBJECT + CAMERA + HOLD**; multi-take; edit assembles.  
3. **No identity without refs**; few faces/outfits/locations; short clips (API max 15s).  
4. **Human Director** = user — final PASS/FAIL, budget, consent, adapter/plugin spend.  
4b. **Spend:** **SuperGrok Heavy weekly pool first** (consumer Imagine); API credits only after pool/extras exhausted + Director OK — `02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md`.  
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
| Imagine matrix + adapters | Done + Image 2.0 | `02_Tools/GROK_IMAGINE_*`, `IMAGINE_IMAGE_2_0` skill, `ADAPTER_POLICY.md` |
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
| Handoff + Phase A hygiene | **Done** (pushed) | `HANDOFF.md`, `11_Archive/`, `PRODUCTION_DEPLOY.md` |
| SuperGrok-first + Image 2.0 stills | **Done** | `SPEND_POLICY_*`, `IMAGINE_IMAGE_2_0`, matrix |
| Releases | **Done** | GitHub **v1.2**, **v1.2.1**, **v1.2.3** |

### 3.2 Verification already run

| Test | Result | Path |
|------|--------|------|
| Plugin stack script | 16 PASS / 0 FAIL | `07_Outputs/PLUGIN_STACK_VERIFY_20260808.md` |
| Plugin E2E (post Tavily OAuth) | PASS, MCP 4/4 | `07_Outputs/E2E_PLUGIN_WORKFLOW_TEST_2026-08-08.md` |
| Final kit E2E (docs+sim+plugins) | PASS | `07_Outputs/FINAL_E2E_PRODUCTION_WORKFLOW_2026-08-08.md` |
| MVP dry-run sim | Packets/QC OK (archived) | `11_Archive/simulations/sim_mvp_deploy_v1/` |

### 3.3 Known environment notes

- **Tavily:** Was broken (expired OAuth); fixed via PKCE re-auth into `~/.grok/mcp_credentials.json`. May expire ~24h — re-auth via Grok TUI `/mcp` if doctor fails.  
- **Firecrawl / chrome-devtools / superpowers:** Were healthy at last verify.  
- **Grok CLI:** On PATH via `~/.grok/bin`.  
- **NordVPN:** Caused Warp agent drops when full-tunnel; keep off or split-tunnel Warp.  
- **`PROJECT_STATUS.md`:** GitHub remote documented as **live** (Phase A fix).  
- **`08_Projects/`:** `_template` + real slug `smoke_imagine_v1` (Phase B). Sims archived.  

---

## 4. Open / not done

### Phase A — CLOSED

| Item | Status |
|------|--------|
| A1 HANDOFF.md | Done on `main` |
| A2 Archive sims → `11_Archive/simulations/` | Done; `08_Projects/` = `_template` + real slugs only |
| A3 PROJECT_STATUS GitHub live | Done |
| A4 PRODUCTION_DEPLOY.md | Done |
| A5 .DS_Store / gitignore | Done (ignored; not tracked) |
| A6 Release tag | **v1.2.3** (supersedes optional v1.2.2 hygiene tag) |

### Still open (post–Phase A)

| Item | Priority |
|------|----------|
| Live **Imagine still → I2V smoke** via SuperGrok Heavy + **Image 2.0** (`smoke_imagine_v1`) | **P0** Phase B — pack ready; Director runs UI |
| API Imagine smoke | **Not default** — only after weekly pool/extras exhausted |
| R1b Sequence Manager + Episode activation | **P1** Phase C |
| Advanced plugins (exa, figma, …) | **P2** after smoke |
| Fuller Odyssey transcript | **P3** |
| Multi-vendor adapters | **P3** on named failure class only |
| Image 2.0 **API** model id | Track docs.x.ai — consumer-only for now |

---

## 5. Next development phase (roadmap pointer)

**Canonical plan:**  
`06_Roadmaps/ROADMAP_SCALE_TEAM_AND_ADVANCED_PLUGINS.md`

| Phase | Name | Intent |
|-------|------|--------|
| **A** | Hygiene & handoff | **CLOSED** on `v1.2.3` |
| **B** | Live pixel proof | **NEXT** — SuperGrok Heavy + Image 2.0 still → Video 1.5 I2V; pack `08_Projects/smoke_imagine_v1` |
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
6. `05_Workflows/PRODUCTION_DEPLOY.md`  
7. `05_Workflows/DEPLOYMENT_CHECKLIST.md`  
8. `03_Knowledge/PRACTITIONER_GROK_AS_CAMERA.md`  
9. `02_Tools/plugins/GROK_MARKETPLACE_INTEGRATION.md`  
10. `07_Outputs/FINAL_E2E_PRODUCTION_WORKFLOW_2026-08-08.md`  
11. `03_Roles/PRODUCTION_TEAM.md`  

---

## 8. Starter prompt for a new chat

```text
Continue AI Film Production System.

Root: /Users/generationalwealth/Desktop/ai-film-production-system
Repo: https://github.com/JanUrbanik/ai-film-production-system
Branch: main (releases v1.2 / v1.2.1 / v1.2.3). Kit is production-ready docs+tooling; not a finished film.

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

Open work per HANDOFF: Phase A DONE → Phase B Imagine smoke → Phase C team scale → Phase D advanced plugins.

My next task: [Phase B smoke | start real MVP slug ___ | Phase C R1b | install plugin ___]

Confirm reads in ≤10 bullets, then execute. Stop for approval before paid Imagine volume or new plugin installs.
```

---

## 9. Immediate recommended next tasks (pick one)

1. **Phase B smoke (P0):** SuperGrok Heavy + Image 2.0 still → Video 1.5 I2V per `08_Projects/smoke_imagine_v1/README.md`; reply *assets landed*.  
2. **Phase C start:** Author `R1b_Sequence_Manager.md` + Episode activation prompt (after B).  
3. **Phase D start:** Director-charter + install **exa** or **figma** only after B.  
4. **API path:** only if weekly pool + consumer extras exhausted and Director unlocks.  

---

## 10. Document control

| Ver | Date | Notes |
|-----|------|-------|
| 1.0 | 2026-08-08 | Initial handoff for new-chat continuity at kit v1.2.1 + scale roadmap |
| 1.1 | 2026-08-08 | Phase A work + SuperGrok-first + Image 2.0 → v1.2.3 |
| 1.2 | 2026-08-08 | Phase A formally CLOSED on origin; HANDOFF HEAD/tag accurate |

**Maintainer:** Update this file at the end of each major session (HEAD, open work, blockers).

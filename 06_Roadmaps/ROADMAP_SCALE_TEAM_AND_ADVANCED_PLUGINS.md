# Roadmap — Scale production team + advanced marketplace plugins

**Version:** 1.0  
**Date:** 2026-08-08  
**Baseline kit:** v1.2.1 (`main`, tags v1.2 / v1.2.1)  
**Repo:** https://github.com/JanUrbanik/ai-film-production-system  
**Audience:** New-chat agents + Human Director  

---

## 0. Baseline (do not rebuild)

| Already done | Evidence |
|--------------|----------|
| Imagine-first factory + seats R1–R12 | `03_Roles/`, runbooks |
| Grok-as-camera method | `03_Knowledge/PRACTITIONER_GROK_AS_CAMERA.md` |
| Core plugins enabled | superpowers, firecrawl, tavily, chrome-devtools |
| Plugin policy + verify script | `02_Tools/plugins/`, `scripts/verify_plugin_stack.sh` |
| E2E kit verification PASS | `07_Outputs/FINAL_E2E_*`, plugin E2E reports |

**North star for this phase:**  
Scale from “single-session MVP kit” → **multi-seat Episode/Feature operations** with **chartered advanced plugins**, without breaking Imagine-as-camera law.

---

## 1. Goals

1. **Team scale:** R1b Sequence Manager + clearer multi-worker R8 fleet + Episode/Feature activation matrices that actually run.  
2. **Advanced plugins:** Install and bind **selected** catalog plugins (exa, figma, tinyfish, optional deploy/obs) behind Director gates.  
3. **Ops maturity:** Archive sims, HANDOFF, production deploy guide, cost/ledger, parallel gen discipline.  
4. **Proof:** One live Imagine smoke + one real multi-scene MVP/Episode pilot—not more docs-only loops.

## 2. Non-goals

- Merging film seats into Master Builder 16  
- Default multi-vendor video fanout (Kling+Veo+Seedance always-on)  
- Mandatory vector DB / embedding QC  
- Stripe/payments, random infra plugins without a film use case  
- Claiming perfect identity lock  

## 3. Principles (binding)

1. Pixels = **Grok Imagine** + start-frame gate + SUBJECT/CAMERA/HOLD.  
2. Plugins = research / design-ref / verify / plan / optional publish—not the camera.  
3. **Scale seats before scale plugins.** A confused roster + more MCP = chaos.  
4. Every new plugin: install → auth → seat map → workflow hook → verify script update → labeled pilot.  
5. Episode/Feature modes activate standby seats; they don’t invent new governance.  
6. Cost and failure classes written down before parallel gen volume.  

---

## 4. Phased roadmap

### Phase A — Hygiene & handoff (prerequisite, 0.5–1 day)

**Why:** Clean production surface before scaling people/tools.

| # | Work item | Owner seat | Done-when |
|---|-----------|------------|-----------|
| A1 | Write root `HANDOFF.md` (state, laws, next actions) | R1 / docs | File on `main` |
| A2 | Archive `08_Projects/sim_*` → `11_Archive/simulations/` | R1 + exec | Only `_template` active under `08_Projects/` |
| A3 | Fix stale claims in `PROJECT_STATUS.md` (GitHub is live) | docs | No “local git only” |
| A4 | Add `05_Workflows/PRODUCTION_DEPLOY.md` | R1/R12 | Go-live checklist for real shoots |
| A5 | `git clean` `.DS_Store`; tighten gitignore if needed | exec | Clean tree |
| A6 | Optional tag **v1.2.2** hygiene | Director | Release notes |

**Exit gate A:** New chat can start from `HANDOFF.md` alone; active projects folder is production-clean.

---

### Phase B — Live pixel proof (1 day, before heavy scale)

**Why:** Scaling team/plugins is wasted if I2V path unproven on this account.

| # | Work item | Owner | Done-when |
|---|-----------|-------|-----------|
| B1 | Confirm SuperGrok and/or `XAI_API_KEY` | Director | Auth works |
| B2 | One LOCKED still (image-quality) | R3/R8 | File in real project refs |
| B3 | Start-frame gate PASS | R9/R0 | Gate log row |
| B4 | One I2V 4–6s @ 720p, download URL | R8 | Asset on disk |
| B5 | QC row + cost note | R9 | `07_Outputs/IMAGINE_SMOKE_YYYYMMDD.md` |

**Exit gate B:** At least one real Imagine clip exists under a non-`sim_` project.

---

### Phase C — Scale the production team (3–7 days)

**Focus:** Make Episode/Feature **operable**, not just tabulated.

#### C1 — Seat model upgrades

| Item | Detail |
|------|--------|
| **R1b Sequence Manager** | Promote from “section in Showrunner” → own seat file `R1b_Sequence_Manager.md` |
| **R8 fleet ops** | Standardize worker IDs `R8-01…N`, take naming, cost caps per sequence |
| **R9 tiered gates** | Explicit take → scene → sequence → global runbooks (already sketched; flesh Episode) |
| **R5/R11/R12** | Un-standby playbooks for Episode (props/sound/master) |
| **Collab graph v2** | Sequence-level review edges; no free debate mesh |

#### C2 — Activation & orchestration

| Item | Detail |
|------|--------|
| Episode activation prompt | `07_Prompts/FILM_TEAM_ACTIVATION_EPISODE.md` |
| Feature activation prompt | `07_Prompts/FILM_TEAM_ACTIVATION_FEATURE.md` |
| Stage board template | Per-sequence kanban in `03_shot_list/SEQUENCE_BOARD.md` |
| Parallelism rules | Max concurrent Imagine jobs; backoff; budget ceiling |

#### C3 — Artifacts & automation (light)

| Item | Detail |
|------|--------|
| Packet CLI | Validate `shot_packet.schema.json` in `scripts/validate_packets.py` |
| Cost ledger | `09_qc_log/cost_ledger.csv` template per project |
| Showrunner checklist | Freeze gates: story / bibles / stills / gen / cut |

**Exit gate C:** Run a **multi-sequence dry-run** (docs+packets, optional few live clips) with R1b + ≥2 R8 workers + sequence QC log.

---

### Phase D — Advanced marketplace plugins (parallel after A; careful after B)

**Current enabled:** superpowers · firecrawl · tavily · chrome-devtools  

**Candidates (catalog → chartered install):**

| Priority | Plugin | Film use case | Risk | Phase |
|----------|--------|---------------|------|-------|
| P1 | **exa** | Alt/faster research; A/B vs tavily | Auth/quota dual MCP | D1 |
| P1 | **figma** | Lookboards, frame comps, bible still direction | Design account; not pixels | D1 |
| P2 | **tinyfish** | Goal-driven browse when chrome-devtools insufficient | Overlap with chrome; auth | D2 |
| P2 | **neon** or **mongodb** | Optional asset/metadata index (paths, QC, versions) | Scope creep; secrets | D3 |
| P3 | **vercel/railway/cloudflare** | Only if publishing web review gallery | Infra distraction | D3 |
| P3 | **sentry/axiom** | Only if building internal tools/apps | Not film MVP | D3 |
| — | **stripe** | Out of scope unless commerce | Skip | — |

#### D0 — Plugin admission control (every advanced plugin)

1. Director charter: use case, cost, data sensitivity  
2. `grok plugin install <name> --trust`  
3. MCP OAuth / keys (never commit)  
4. Update `.grok/config.toml` `[plugins_stack]`  
5. Update `GROK_MARKETPLACE_INTEGRATION.md` seat map  
6. Extend `scripts/verify_plugin_stack.sh`  
7. Refresh `INSTALLED_STACK.snapshot.json`  
8. One labeled pilot note in `10_Sources/research/`  
9. **Forbidden check:** does not generate final picture; no gate bypass  

#### D1 — Research & design depth (recommended next plugins)

| Work | Done-when |
|------|-----------|
| Install **exa** OR keep tavily-only with documented choice | Doctor green; A/B note |
| Install **figma** if design workflow wanted | MCP OK; bible engine hook “import board → ref pack plan” |
| Skill: `06_Skills/ops/FIGMA_LOOKBOARD.md` (if figma) | Linked from R3/R4/R6 |
| Dual-research policy: tavily default, exa on failure/depth | Written in integration doc |

#### D2 — Automation assist

| Work | Done-when |
|------|-----------|
| Evaluate **tinyfish** vs chrome-devtools | One pilot; pick primary browser tool |
| Showrunner “research pack” automation via superpowers plans | Template under `05_Prompts/` or workflows |

#### D3 — Optional data/publish layer (only after real MVP short exists)

| Work | Done-when |
|------|-----------|
| Asset index (neon/mongo) **or** stay filesystem-only | Decision recorded |
| Review gallery deploy plugin **or** local folder delivery | Decision recorded |

**Exit gate D:** ≥1 advanced plugin beyond core four is installed, verified, seat-mapped, and used in a real preproduction beat—without touching pixel law.

---

### Phase E — Pilot productions (proves scale)

| Pilot | Shape | Success |
|-------|--------|---------|
| E1 | Real MVP short (30–90s), 1 loc, ≤2 cast | Checklist G sign-off |
| E2 | Episode slice (2–3 sequences), R1b active | Sequence QC + cost ledger |
| E3 | Stress: R8 fleet N=3–5 parallel takes | No ownership collisions; downloads reliable |

---

### Phase F — Continuous improvement

- Re-verify Imagine matrix before large spends (`docs.x.ai` via firecrawl/tavily)  
- Expand camera skills; fuller practitioner transcripts  
- Adapter registry only on named failure classes  
- Master Builder FULL charter only for governance-heavy jobs  

---

## 5. Suggested timeline

```text
Week 0:  Phase A hygiene + HANDOFF
Day 1:   Phase B Imagine smoke
Week 1:  Phase C team scale (R1b, Episode activation, packet validate script)
Week 1–2: Phase D1 advanced plugins (exa and/or figma)
Week 2–3: Phase E1–E2 pilots
Later:   D3 / Feature mode / adapters
```

Adjust to budget; **never skip B before E**.

---

## 6. Milestone checklist (copy into new chat)

### M0 — Ready to scale
- [ ] HANDOFF.md on main  
- [ ] Sims archived  
- [ ] verify_plugin_stack.sh green  
- [ ] Imagine smoke note exists  

### M1 — Team scale v1
- [ ] R1b seat file + Episode activation  
- [ ] R8 fleet naming + cost ledger template  
- [ ] Sequence QC path documented and dry-run  

### M2 — Advanced plugins v1
- [ ] Admission control followed for each new plugin  
- [ ] exa and/or figma live + seat-mapped  
- [ ] verify script covers new MCP  
- [ ] Pilot research/design note filed  

### M3 — Production proof
- [ ] Real MVP short delivered internally  
- [ ] Optional Episode slice  
- [ ] Postmortem with labeled claims  

---

## 7. Risks & mitigations

| Risk | Mitigation |
|------|------------|
| Plugin sprawl | Admission control; Director charter |
| OAuth expiry (tavily/etc.) | Doctor in deploy checklist; re-auth runbook |
| Parallel gen cost blowup | Cost ceiling per sequence; Showrunner freeze |
| Seat confusion at scale | R1b + exact name calls; no free debate |
| VPN/agent drops | Nord off or split-tunnel Warp |
| Scaling before pixels work | Gate B mandatory |

---

## 8. New-chat starter (scale phase)

```text
Continue AI Film Production System at v1.2.1.

Root: /Users/generationalwealth/Desktop/ai-film-production-system
Read: 06_Roadmaps/ROADMAP_SCALE_TEAM_AND_ADVANCED_PLUGINS.md
      PROJECT_STATUS.md, README.md, DEPLOYMENT_CHECKLIST.md,
      ONE_PAGE_FACTORY_LAW.md, GROK_MARKETPLACE_INTEGRATION.md

Laws: Imagine-first + Grok-as-camera; plugins ≠ camera; no multi-vendor default;
separate from master-builder-team; Director=me.

Execute Phase A (hygiene/handoff) unless I specify otherwise, then stop for approval
before Phase B paid Imagine smoke or Phase D plugin installs.
```

---

## 9. Document control

| Ver | Date | Notes |
|-----|------|-------|
| 1.0 | 2026-08-08 | Initial scale-team + advanced-plugins roadmap for chat handoff |

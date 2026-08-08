# Production deploy — real shoots

**Version:** 1.0  
**Date:** 2026-08-08  
**Kit:** ≥ v1.2.1  
**Audience:** Human Director + R1 Showrunner / R12 Mastering  
**Claim labels:** Steps below are **Verified** kit process unless marked otherwise.

This is the **go-live** guide for a **real** project (non-`sim_*` slug).  
It sits **on top of** `DEPLOYMENT_CHECKLIST.md` (gates A–G) and does not replace it.

---

## 0. When to use this doc

| Situation | Use |
|-----------|-----|
| First paid still / I2V on this account | This doc §1–4 + Phase B smoke |
| First real MVP short (30–90s) | Full doc + MVP runbook |
| Episode / Feature | This doc + scale roadmap Phase C activation prompts |
| Docs-only rehearsal | Prefer archived sims under `11_Archive/simulations/` — do not clutter `08_Projects/` |

**Order rule:** Hygiene (Phase A) → **one live smoke** (Phase B) → volume gen / multi-seat scale.

---

## 1. Pre-flight (same day as spend)

```bash
export PATH="$HOME/.grok/bin:$PATH"
cd /Users/generationalwealth/Desktop/ai-film-production-system   # or your clone
git pull origin main
./scripts/verify_plugin_stack.sh    # expect exit 0 if using plugins this session
# optional: grok mcp doctor
```

- [ ] On `main` (or intentional production branch); working tree understood  
- [ ] Read: `HANDOFF.md`, `ONE_PAGE_FACTORY_LAW.md`, `PRACTITIONER_GROK_AS_CAMERA.md`  
- [ ] Imagine access: **SuperGrok Heavy** login on `grok.com/imagine` (default)  
- [ ] Settings → Usage: weekly pool headroom noted (see `02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md`)  
- [ ] `XAI_API_KEY` **not** used unless Director unlocked API after pool/extras exhausted  
- [ ] NLE ready (CapCut or DaVinci); disk for multi-take downloads  
- [ ] NordVPN **off** or **split-tunnel Warp** (avoids agent/MCP drops)  
- [ ] Director available for PASS/FAIL and budget ceiling  

**Plugins:** research/verify/plan only — never replace Imagine or bypass start-frame gates  
(`02_Tools/plugins/GROK_MARKETPLACE_INTEGRATION.md`).

---

## 2. Open a real project slug

```bash
cp -R 08_Projects/_template 08_Projects/<slug>
# slug rules: no sim_ prefix; lowercase; e.g. mvp_doorway_v1, ep01_coldopen_v1
```

Active production surface must stay clean:

| Path | Allowed |
|------|---------|
| `08_Projects/_template/` | Scaffold only |
| `08_Projects/<slug>/` | Live or in-progress real projects |
| `11_Archive/simulations/` | Retired dry-runs only |

Fill in order (details: `MVP_SHORT_FILM_RUNBOOK.md`):

1. `00_brief/` — logline, 3–7 beats, consent  
2. Style Contract **LOCKED**  
3. Character / Environment / Props bibles + ref packs **LOCKED**  
4. Shot list frozen — every card: **SUBJECT + CAMERA + HOLD**  
5. Cost sketch: `takes × seconds × rate` (+ stills)

**Gate:** Director OK on beats + locked bibles before any hero still volume.

---

## 3. Checklist binding (do not skip)

Run **`05_Workflows/DEPLOYMENT_CHECKLIST.md`** and treat sections as hard stops:

| Section | Stop meaning |
|---------|----------------|
| **A–B** | Environment + session knowledge not loaded → no gen |
| **C** | Project bootstrap incomplete → no gen |
| **D** | Start-frame gate fail → **no I2V / motion spend** |
| **E–F** | Injection/QC/post incomplete → no “shipped” claim |
| **G** | Go-live acceptance incomplete → piece is draft only |

Sign the checklist’s deploy sign-off table when A–G are honestly complete.

---

## 4. Pixel path (Grok-as-camera)

**Default stack (Verified kit law):**

1. **Image 2.0 Quality** start still per hero shot (`IMAGINE_IMAGE_2_0`)  
2. Storyboard-worthy gate (`06_Skills/generation/START_FRAME_FIRST.md`)  
3. Packet validate vs `02_Tools/schemas/shot_packet.schema.json`  
4. Motion: **I2V > R2V > extend > edit > T2V**  
5. Model default: `grok-imagine-video-1.5` @ **720p** for iteration  
6. Multi-take (4–8 hero); download temp URLs **immediately** → `04_gen/<shot_id>/`  
7. Name `Sxx_takeNN.mp4`; never overwrite PASS  
8. R9 binary QC → only PASS copies to `05_pass/`  
9. R10 edits from PASS bin (raw-footage mindset)

**Forbidden by default:**

- Multi-vendor fanout (Kling/Veo/Seedance/…) without named failure class + Director spend OK  
- Identity without refs  
- Hero motion without start-frame PASS  
- Generators self-PASS  
- Plugins writing “final picture” or skipping bible/start-frame gates  

---

## 5. First paid smoke (Phase B — before volume)

Minimum proof on a **real** slug (can be tiny):

| Step | Done-when |
|------|-----------|
| B1 Auth | SuperGrok Heavy consumer login works; Usage pool checked |
| B2 Still | One LOCKED still via **consumer Imagine** on disk under project refs |
| B3 Gate | Start-frame gate row logged PASS |
| B4 I2V | One 4–6s @ 720p via **consumer Imagine** downloaded |
| B5 Report | `07_Outputs/IMAGINE_SMOKE_YYYYMMDD.md` with ledger=`supergrok_heavy_weekly` + QC note |
| B6 API | **Skip** unless Director unlocks after pool exhaustion |

**Exit:** At least one real Imagine clip exists under a non-`sim_` project.  
**Stop for Director** before scaling take count or opening Episode mode.

---

## 6. MVP short → ship package

Follow `05_Workflows/MVP_SHORT_FILM_RUNBOOK.md` end-to-end.

Delivery package (`06_edit/delivery/` or Director-chosen path):

- Master export  
- PASS bin list  
- `09_qc_log` continuity report  
- Bible version pins  
- Optional: AI disclosure note if publishing  

Do **not** call the piece shipped until checklist **G** is yes.

---

## 7. Episode / Feature (scale path)

Only after Phase B smoke and MVP discipline hold:

1. Read `06_Roadmaps/ROADMAP_SCALE_TEAM_AND_ADVANCED_PLUGINS.md` Phase C  
2. Activate Episode/Feature prompts when present (`07_Prompts/FILM_TEAM_ACTIVATION_*.md`)  
3. Use R1b Sequence Manager + R8 fleet naming when those seats exist  
4. Cost ceiling **per sequence**; Showrunner freeze gates before parallel gen  

Until Phase C files land, run multi-scene work as **multiple MVP-shaped sequences** under one slug with explicit sequence folders — do not invent free-debate multi-agent mesh.

---

## 8. Plugins during production

| Allowed | Forbidden |
|---------|-----------|
| Research packs → `10_Sources/research/` | Pixel generation |
| docs.x.ai re-verify before big spend | Bypassing start-frame / bible locks |
| Browser check of consumer Imagine UI state | Secret commit / raw OAuth dump |
| Plans / debug via superpowers | Claiming native “92/100 consistency” |

Re-auth Tavily (or other MCP) via Grok TUI `/mcp` if `grok mcp doctor` fails (~24h OAuth possible).

**Advanced plugins** (exa, figma, …): Director charter + admission control (roadmap Phase D) — not ad-hoc mid-shoot.

---

## 9. Failure ladder (before adapters)

1. Regen take (same packet)  
2. Tighten SUBJECT / CAMERA / HOLD or start still  
3. Mode shift on ladder (I2V→edit/extend etc.)  
4. Bible / ref pack repair  
5. **Only then:** named failure class → adapter tier (`02_Tools/ADAPTER_POLICY.md`) + spend OK  

Log every FAIL with `fail_tags` in `09_qc_log`.

---

## 10. Sister system boundary

| System | Role |
|--------|------|
| `ai-film-production-system` | Production runtime (this deploy) |
| `master-builder-team` | Optional governance OS only |

Do **not** merge film seats into Builder `02_Agents/`. Bridge docs: `09_Bridge/`.

---

## 11. Deploy sign-off (production)

| Field | Value |
|-------|--------|
| Operator | |
| Date | |
| Project slug | |
| Mode | MVP / Episode / Feature |
| Imagine surface | API / consumer UI / both |
| Checklist A–G | YES / NO |
| Phase B smoke on file? | YES / NO · path: |
| Budget ceiling | |
| Plugins used this shoot | none / list |
| Director sign-off | |

**Rule:** No volume video generation until checklist **A–D** are checked.  
**Rule:** No “factory proven on pixels” claim until Phase B smoke report exists.

---

## 12. Related paths

| Doc | Role |
|-----|------|
| `05_Workflows/DEPLOYMENT_CHECKLIST.md` | Gate list A–H |
| `05_Workflows/MVP_SHORT_FILM_RUNBOOK.md` | MVP execution |
| `05_Workflows/FEATURE_SCALE_WORKFLOW.md` | Longer form |
| `05_Workflows/QC_RUBRICS.md` / `CONTINUITY_GATES.md` | QC |
| `02_Tools/GROK_IMAGINE_CAPABILITY_MATRIX.md` | Tool truth |
| `06_Roadmaps/ROADMAP_SCALE_TEAM_AND_ADVANCED_PLUGINS.md` | A→F phases |
| `HANDOFF.md` | New-chat state |

---

## Document control

| Ver | Date | Notes |
|-----|------|-------|
| 1.0 | 2026-08-08 | Phase A4 — go-live guide for real shoots |

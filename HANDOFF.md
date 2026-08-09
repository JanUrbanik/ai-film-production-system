# HANDOFF — AI Film Production System

**For:** New agent chats / Human Director  
**Updated:** 2026-08-09  
**Kit version (docs):** **v1.2.5** (content on `main` after tag `v1.2.3`)  
**Git tags on origin:** `v1.2`, `v1.2.1`, `v1.2.3`  
**HEAD:** `d2e6f9e` — run `git pull && git log -1 --oneline` to confirm tip
**Working tree expectation:** clean after push  
**Sister engine:** `/Users/generationalwealth/Desktop/master-builder-team` (governance only — do **not** merge film seats into Builder `02_Agents/`)

---

## 0. One-screen status

| Layer | State |
|-------|--------|
| **Factory kit (docs/seats/workflows)** | **Production-ready** — operate from this repo |
| **Phase A hygiene** | **CLOSED** |
| **Phase B live pixels** | **BLOCKED** — pack ready; **no** still/mp4 on disk yet |
| **Phase C team scale** | **ENV PREPARED** (R1b, Ep/Feat activation, validator) — dry-run after B |
| **Phase D plugins** | Not started (exa/figma) |
| **Phase E pilots** | Not started — **never before B** |
| **CineAgent Studio UI** | Product brief only — build in Grok Build later |
| **Finished film** | Not a kit deliverable |

**P0 next:** Director finishes SuperGrok Heavy consumer smoke → reply **assets landed**.  
**Starter paste file:** `07_Outputs/NEXT_CHAT_STARTER_20260809.md`

---

## 1. What this project is

| | |
|--|--|
| **Name** | AI Film Production System |
| **Root** | `/Users/generationalwealth/Desktop/ai-film-production-system` |
| **GitHub** | https://github.com/JanUrbanik/ai-film-production-system |
| **Role** | Production **factory/kit** for short-to-long AI narrative video |
| **Not** | Master Builder’s 16 seats; not a finished feature film; not CineAgent app code yet |

**Pointer from Builder:** `master-builder-team/01_Context/FILM_SYSTEM_POINTER.md`

---

## 2. Hard laws (non-negotiable)

1. **Imagine-first** — stills **default** Image 2.0 consumer; motion **default** Video 1.5; both are **options** in a pluggable backend registry (`02_Tools/GENERATION_BACKEND_POLICY.md`).  
2. **Image 2.0 is NOT a video model** and is **not** locked as sole still tool — preferred default only.  
3. **Grok-as-camera:** start-frame first; **SUBJECT + CAMERA + HOLD**; multi-take; edit assembles (`K-PRAC-GROK-CAMERA-001`).  
4. **Transcript→shot-script:** `K-SHOT-SCRIPT-001` — four artifacts (Asset Bible, Continuity Ledger, Shot Script, Flags); **REFS never inside GEN_PROMPT**.  
5. **No identity without refs**; few faces/outfits/locations; short clips (conversion path ≤8s preferred; API max 15s).  
6. **Human Director** = user — PASS/FAIL, budget, consent, backend/adapter unlock.  
7. **Spend:** SuperGrok Heavy **weekly pool first** (consumer Imagine) before any `XAI_API_KEY` pixel spend (`02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md`).  
8. **Binary QC** — no fake native “92/100” (UI heuristics only if labeled **Assumed**).  
9. **Multi-vendor video** = adapter tier / Director picker — **never** default silent fanout.  
10. **Marketplace plugins** = research/verify/plan only — never replace Imagine or bypass gates.  
11. **Claim labels:** Verified / Assumed / Speculative.  
12. Prefer NordVPN **off** or **split-tunnel Warp** during long agent/MCP sessions.  
13. **CineAgent Studio** (planned) = visual shell over this repo — does **not** replace factory logic (`01_Architecture/CINEAGENT_STUDIO_PRODUCT_BRIEF.md`).

---

## 3. Session history (continuity thread 2026-08-08 → 2026-08-09)

Long chat resumed from prior handoff at context limit; work continued here.

| Step | What happened | Commit / artifact |
|------|----------------|-------------------|
| Resume | `git pull`; read HANDOFF; plugin verify 16/16 | pre-work |
| **Phase A** | Archive `sim_*` → `11_Archive/simulations/`; `PRODUCTION_DEPLOY.md`; status hygiene | `466cf30` |
| Spend law | SuperGrok Heavy weekly pool before API | `4dff04f` + `SPEND_POLICY_*` |
| Image 2.0 research | Stills default Quality Mode; API 2.0 “coming soon” | `a356bc4` **tag v1.2.3** |
| Phase A close docs | HANDOFF/roadmap A1–A6 CLOSED | `cbbe9db`… |
| **K-SHOT-SCRIPT-001** | Full transcript→shot standard integrated | `410e2a7` |
| Phase B pack | `smoke_imagine_v1` frozen pack + smoke report scaffold | `4dfa110` |
| Checklist exec | Opened UI URLs, staged prompts; **no pixels**; API models 403 | `101bd13` |
| Blockage docs | `MANUAL_NEXT_STEPS.md` BLK-1…7 | `468017c` |
| **Phase C prep** | R1b, Ep/Feat activation, sequence board, cost ledger, `validate_packets.py` | `c27d550` |
| **CineAgent + backends** | Pluggable registry; Studio product brief; mockup notes | `2cac274` |

### Key commits (newest first)

```text
2cac274 docs: pluggable gen backends + CineAgent Studio product brief
c27d550 feat(phase-c): prepare scale-team environment after smoke gate
468017c docs(phase-b): document smoke blockages and manual next steps
101bd13 docs(phase-b): record operator checklist execution — blocked on consumer UI
4dfa110 feat(phase-b): initialize smoke_imagine_v1 pack for SuperGrok Heavy
410e2a7 feat(knowledge): ingest transcript-to-shot-script standard K-SHOT-SCRIPT-001
a356bc4 (tag v1.2.3) feat(imagine): adopt Image 2.0 as default consumer stills path
4dff04f docs(spend): SuperGrok Heavy weekly pool first; Phase B consumer smoke pack
466cf30 chore(phase-a): archive sims, add PRODUCTION_DEPLOY, hygiene to v1.2.2
```

---

## 4. Environment facts (operator machine)

| Item | State |
|------|--------|
| Grok CLI | `~/.grok/bin/grok` on PATH (Build TUI — **not** Imagine camera CLI) |
| SuperGrok Heavy | Director ~€350 tier — **primary pixel budget** |
| `XAI_API_KEY` in shell | May be set but was **403 bad-credentials** on `/v1/models`; **do not** use for smoke while pool-first law holds |
| Grok OIDC `auth.json` | Was expired mid-session |
| Plugins | superpowers, firecrawl, tavily, chrome-devtools — `./scripts/verify_plugin_stack.sh` (MCP may need re-auth) |
| Smoke still | **Missing** `08_Projects/smoke_imagine_v1/02_refs/start_frames/S01_start_v1.*` |
| Smoke mp4 | **Missing** `08_Projects/smoke_imagine_v1/04_gen/S01/S01_take01.mp4` |

---

## 5. Kit inventory (done)

| Area | Where |
|------|--------|
| Law | `AGENTS.md`, `ONE_PAGE_FACTORY_LAW.md` |
| Pipeline | `CANONICAL_PIPELINE.md` |
| Imagine matrix | `02_Tools/GROK_IMAGINE_CAPABILITY_MATRIX.md` |
| Backend registry | `02_Tools/GENERATION_BACKEND_POLICY.md` |
| Spend | `02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md` |
| Adapters | `02_Tools/ADAPTER_POLICY.md` |
| Shot schema + validator | `schemas/shot_packet.schema.json`, `scripts/validate_packets.py` |
| Seats R1–R12 + R1b | `03_Roles/seats/` |
| Knowledge | `K-PRAC-GROK-CAMERA-001`, `K-SHOT-SCRIPT-001` |
| Shot standard full text | `10_Sources/standards/TRANSCRIPT_TO_SHOT_SCRIPT_STANDARD_v1.md` |
| Skills | `06_Skills/generation/*` incl. `IMAGINE_IMAGE_2_0`, `TRANSCRIPT_TO_SHOT_SCRIPT` |
| Deploy | `PRODUCTION_DEPLOY.md`, `DEPLOYMENT_CHECKLIST.md` |
| Activation | `FILM_TEAM_ACTIVATION.md` + `_EPISODE` + `_FEATURE` |
| CineAgent UI brief | `01_Architecture/CINEAGENT_STUDIO_PRODUCT_BRIEF.md` |
| Mockup notes | `10_Sources/ui_mockups/CINEAGENT_STUDIO_MOCKUP_NOTES.md` |
| Archive sims | `11_Archive/simulations/` |
| Active projects | `08_Projects/_template`, `08_Projects/smoke_imagine_v1` |
| Scale roadmap | `06_Roadmaps/ROADMAP_SCALE_TEAM_AND_ADVANCED_PLUGINS.md` |
| Next-chat starter | `07_Outputs/NEXT_CHAT_STARTER_20260809.md` |

---

## 6. Open work

### Phase B — P0 (blocking “factory proven on pixels”)

**Project:** `08_Projects/smoke_imagine_v1`  
**Manual guide:** `00_brief/MANUAL_NEXT_STEPS.md`  
**Checklist:** `00_brief/OPERATOR_CHECKLIST.md`  
**Exec log:** `09_qc_log/OPERATOR_CHECKLIST_EXECUTION_20260809.md`  
**Report:** `07_Outputs/IMAGINE_SMOKE_20260809.md` (status BLOCKED)

| BLK | Issue | Unblock |
|-----|--------|---------|
| 1 | No headless consumer Imagine | Director on grok.com Heavy |
| 2 | Usage % empty | `USAGE_BEFORE.md` |
| 3 | No start still | Image 2.0 → `S01_start_v1.png` |
| 4 | Gate not PASS | `START_FRAME_GATE.md` |
| 5 | No I2V | `S01_take01.mp4` 4–6s 720p |
| 6 | Report open | Chat: **assets landed** |
| 7 | API key 403 | Ignore for smoke |

**Ledger:** `supergrok_heavy_weekly` only. **No API pixels** unless Director unlocks after pool/extras.

### Phase C — after B

- Multi-sequence **dry-run** with R1b + ≥2 R8 + sequence board + `validate_packets.py`  
- Prep note: `07_Outputs/PHASE_C_ENV_PREP_20260809.md`

### Phase D / E / Studio

- D: exa/figma under admission control after B (prefer seats first)  
- E: real MVP/Episode pilots only after B  
- Studio: implement brief in Grok Build (M0–M5 in product brief)  

---

## 7. Operate (quick)

```bash
export PATH="$HOME/.grok/bin:$PATH"
cd /Users/generationalwealth/Desktop/ai-film-production-system
git pull origin main
./scripts/verify_plugin_stack.sh
python3 scripts/validate_packets.py 08_Projects/smoke_imagine_v1/03_shot_list/packets/
```

**Activation:** `07_Prompts/FILM_TEAM_ACTIVATION.md` (MVP) / `_EPISODE` / `_FEATURE`  
**New movie:** `cp -R 08_Projects/_template 08_Projects/<slug>`  
**Prose story:** `05_Workflows/TRANSCRIPT_TO_SHOT_SCRIPT.md`

---

## 8. Load order for new agents

1. `HANDOFF.md` ← you are here  
2. `07_Outputs/NEXT_CHAT_STARTER_20260809.md`  
3. `06_Roadmaps/ROADMAP_SCALE_TEAM_AND_ADVANCED_PLUGINS.md`  
4. `PROJECT_STATUS.md`  
5. `01_Architecture/ONE_PAGE_FACTORY_LAW.md`  
6. `02_Tools/GENERATION_BACKEND_POLICY.md`  
7. `02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md`  
8. `03_Knowledge/TRANSCRIPT_TO_SHOT_SCRIPT.md` + `PRACTITIONER_GROK_AS_CAMERA.md`  
9. `01_Architecture/CINEAGENT_STUDIO_PRODUCT_BRIEF.md` (if UI work)  
10. `08_Projects/smoke_imagine_v1/00_brief/MANUAL_NEXT_STEPS.md` (if pixels)  
11. `07_Outputs/IMAGINE_SMOKE_20260809.md`  

---

## 9. Immediate recommended next tasks

1. **Phase B (P0):** `MANUAL_NEXT_STEPS.md` → still + I2V → **assets landed**  
2. **Phase C:** multi-seq dry-run after B  
3. **CineAgent Studio M0** from product brief (Grok Build)  
4. **Phase D** plugins only after B (+ prefer C seats)  

---

## 10. Document control

| Ver | Date | Notes |
|-----|------|-------|
| 1.0 | 2026-08-08 | Initial handoff |
| 1.1–1.2 | 2026-08-08 | Phase A close |
| 2.0 | 2026-08-09 | Full continuity through CineAgent + backends + next-chat starter |

**Maintainer:** Rewrite this file at each major session end (HEAD, open work, blockers, commits).

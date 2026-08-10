# HANDOFF — AI Film Production System

**For:** Next agent chat / Human Director  
**Updated:** 2026-08-10  
**Kit docs version:** **v1.2.5** (on `main`; release tags include `v1.2.3`)  
**Git tags on origin:** `v1.2`, `v1.2.1`, `v1.2.3`  
**HEAD:** run `git pull origin main && git log -1 --oneline` (trust git tip)  
**Working tree:** expect clean after push  
**Factory root:** `/Users/generationalwealth/Desktop/ai-film-production-system`  
**GitHub:** https://github.com/JanUrbanik/ai-film-production-system  
**Sister (governance only):** `/Users/generationalwealth/Desktop/master-builder-team` — never merge film seats into Builder `02_Agents/`

**Paste pack for next chat:** `07_Outputs/NEXT_CHAT_STARTER_20260810.md`  
**Grok Build app prompt (full):** `07_Outputs/GROK_BUILD_CINEAGENT_STUDIO_PROMPT_FULL.md`

---

## 0. One-screen status

| Layer | State |
|-------|--------|
| Factory kit (docs/seats/workflows/tooling) | **Production-ready** |
| Phase A hygiene | **CLOSED** |
| Phase B live pixels (smoke) | **BLOCKED** — pack ready; **no** still/mp4 on disk |
| Phase C team scale | **ENV PREPARED** — dry-run after B |
| Phase D advanced plugins | Not started |
| Phase E pilots | Forbidden until B |
| CineAgent Studio app code | **Not built** — full Build prompt ready |
| Finished film | Not a kit deliverable |

**Director immediate forks:**
1. **Verify** anything questionable in factory docs (this chat was at context limit).  
2. **Phase B smoke** via SuperGrok Heavy consumer (`MANUAL_NEXT_STEPS.md`) → `assets landed`.  
3. **Start CineAgent Studio M0** in Grok Build using full prompt + 4 mockups.

---

## 1. What this is / is not

**Is:** Multi-agent **film production factory** — bibles, shot scripts/packets, Imagine generation discipline, QC, edit, handoffs.  
**Is not:** Finished movie; Master Builder 16-seat OS; shipping CineAgent binary yet.

---

## 2. Hard laws (do not dilute)

1. Imagine-first; Grok-as-camera: start-frame first; SUBJECT+CAMERA+HOLD; multi-take; edit assembles.  
2. **Stills default** = Imagine **Image 2.0** consumer Quality — **not a video model**, **not exclusive** (pluggable).  
3. **Motion default** (Grok path) = **Video 1.5** — pluggable; adapters only Director pick or named failure; **no silent multi-vendor fanout**.  
4. Registry: `02_Tools/GENERATION_BACKEND_POLICY.md`.  
5. **K-SHOT-SCRIPT-001**: prose → Asset Bible + Continuity Ledger + Shot Script + Flags; **REFS never in GEN_PROMPT**.  
6. SuperGrok Heavy **weekly pool first**; API pixels only after pool/extras exhausted + Director unlock (`SPEND_POLICY_SUPERGROK_FIRST.md`).  
7. Binary QC PASS/FAIL; mockup “92/100” = **Assumed** heuristic only if shown in UI.  
8. Plugins = research/verify/plan only.  
9. Labels: Verified / Assumed / Speculative.  
10. Human Director = user.  
11. CineAgent Studio = **UI shell** over this repo — does not replace seats/laws.  
12. NordVPN off or split-tunnel Warp for long agent sessions.

---

## 3. Full continuity timeline (prior chat → this thread)

| When | Work | Evidence |
|------|------|----------|
| Pre | Kit v1.2 / v1.2.1 plugins + E2E | tags, `07_Outputs/*E2E*` |
| Phase A | Archive sims → `11_Archive/simulations/`; `PRODUCTION_DEPLOY.md`; hygiene | `466cf30` |
| Spend | SuperGrok Heavy first | `4dff04f`, `SPEND_POLICY_*` |
| Image 2.0 | Stills default; not video | `a356bc4` **v1.2.3** |
| Shot standard | Full K-SHOT-SCRIPT-001 wire-up | `410e2a7` |
| Phase B pack | `smoke_imagine_v1` prompts/packet/checklist/report | `4dfa110` |
| B checklist | Agent opened UI, staged prompts; **no pixels**; API `/models` 403 | `101bd13` |
| B docs | `MANUAL_NEXT_STEPS.md` BLK-1..7 | `468017c` |
| Phase C | R1b, Ep/Feat activation, boards, cost ledger, `validate_packets.py` | `c27d550` |
| Studio + backends | CineAgent brief, mockup notes, backend policy | `2cac274` |
| Transfer pack | HANDOFF v2 + starters | `9165ada`… |
| Build prompt | Full Grok Build paste file | `78ebc83` |

### Important commits (newest relevant)

```text
78ebc83 docs: finalize full Grok Build prompt for CineAgent Studio
c97d0bf docs: handoff transfer pack — trust git tip after pull
2cac274 docs: pluggable gen backends + CineAgent Studio product brief
c27d550 feat(phase-c): prepare scale-team environment after smoke gate
468017c docs(phase-b): document smoke blockages and manual next steps
101bd13 docs(phase-b): record operator checklist execution — blocked on consumer UI
4dfa110 feat(phase-b): initialize smoke_imagine_v1 pack for SuperGrok Heavy
410e2a7 feat(knowledge): ingest transcript-to-shot-script standard K-SHOT-SCRIPT-001
a356bc4 (tag v1.2.3) feat(imagine): adopt Image 2.0 as default consumer stills path
4dff04f docs(spend): SuperGrok Heavy weekly pool first
466cf30 chore(phase-a): archive sims, add PRODUCTION_DEPLOY
```

---

## 4. Environment facts

| Item | State |
|------|--------|
| `main` | Should equal `origin/main` after pull |
| Grok CLI | `~/.grok/bin/grok` = Build TUI, not Imagine camera |
| SuperGrok Heavy | ~€350 — primary pixel ledger |
| API key | May exist in env but was **403** on models; do not use for smoke |
| Plugins | superpowers, firecrawl, tavily, chrome-devtools |
| Smoke still | **Missing** `S01_start_v1.png` |
| Smoke mp4 | **Missing** `S01_take01.mp4` |
| Packet S01 | Should `validate_packets` PASS |

---

## 5. Phase B smoke (P0) — exact paths

**Project:** `08_Projects/smoke_imagine_v1/`  

| Doc | Path |
|-----|------|
| Manual steps | `00_brief/MANUAL_NEXT_STEPS.md` |
| Checklist | `00_brief/OPERATOR_CHECKLIST.md` |
| Exec log | `09_qc_log/OPERATOR_CHECKLIST_EXECUTION_20260809.md` |
| Still prompt | `03_shot_list/STILL_PROMPT.md` (Image 2.0) |
| I2V prompt | `03_shot_list/I2V_PROMPT.md` (Video 1.5) |
| Shot script | `03_shot_list/SHOT_SCRIPT.md` |
| Packet | `03_shot_list/packets/S01.json` |
| Report | `07_Outputs/IMAGINE_SMOKE_20260809.md` |
| Still out | `02_refs/start_frames/S01_start_v1.png` |
| Video out | `04_gen/S01/S01_take01.mp4` |

**Ledger:** `supergrok_heavy_weekly` only until Director unlocks API.

---

## 6. Phase C prepared (not exited)

| Artifact | Path |
|----------|------|
| R1b seat | `03_Roles/seats/R1b_Sequence_Manager.md` |
| Episode activation | `07_Prompts/FILM_TEAM_ACTIVATION_EPISODE.md` |
| Feature activation | `07_Prompts/FILM_TEAM_ACTIVATION_FEATURE.md` |
| Sequence board | `05_Workflows/templates/SEQUENCE_BOARD.md` |
| Cost ledger template | `08_Projects/_template/09_qc_log/cost_ledger.csv` |
| Validator | `scripts/validate_packets.py` |
| Prep note | `07_Outputs/PHASE_C_ENV_PREP_20260809.md` |

Exit C still needs: B complete + multi-seq dry-run with R1b + ≥2 R8.

---

## 7. CineAgent Studio (app not coded)

| Artifact | Path |
|----------|------|
| Product brief | `01_Architecture/CINEAGENT_STUDIO_PRODUCT_BRIEF.md` |
| Mockup notes | `10_Sources/ui_mockups/CINEAGENT_STUDIO_MOCKUP_NOTES.md` |
| **Full Build prompt** | `07_Outputs/GROK_BUILD_CINEAGENT_STUDIO_PROMPT_FULL.md` |
| Preferred app dir | `~/Desktop/cineagent-studio` or `apps/cineagent-studio` |

**Build rules:** UI shell only; backend dropdowns; Image 2.0 = stills default; Video 1.5 = motion default; M0 hard stop; no fake 92/100; no API default.

**Director Build procedure:**
1. Open Grok Build with factory path access.  
2. Attach 4 mockup images.  
3. Paste **only** the ` ```text ` block inside `GROK_BUILD_CINEAGENT_STUDIO_PROMPT_FULL.md` (from `Build CineAgent Studio` through `Then stop for review`).  
4. Allow M0 only; review before M1.

---

## 8. Verification agenda for next chat (Director “saw mistakes”)

Next agent must help Director verify without losing state:

- [ ] `git pull` + clean `main` == `origin/main`  
- [ ] Image 2.0 **not** described as video generator anywhere critical  
- [ ] Backends pluggable in `GENERATION_BACKEND_POLICY.md`  
- [ ] Spend policy SuperGrok-first intact  
- [ ] K-SHOT-SCRIPT-001 REFS≠GEN_PROMPT intact  
- [ ] Smoke pack complete; pixels still missing  
- [ ] Phase C files present  
- [ ] Grok Build prompt fence intact (open/close, BEGIN M0)  
- [ ] CineAgent brief matches mockup notes (binary QC)  
- [ ] No secrets in repo  

After verification, Director may edit factory docs, then freeze Build starter messages.

---

## 9. Operate / verify commands

```bash
export PATH="$HOME/.grok/bin:$PATH"
cd /Users/generationalwealth/Desktop/ai-film-production-system
git pull origin main
git log -1 --oneline
git status -sb
./scripts/verify_plugin_stack.sh
python3 scripts/validate_packets.py 08_Projects/smoke_imagine_v1/03_shot_list/packets/
ls 08_Projects/smoke_imagine_v1/02_refs/start_frames/
ls 08_Projects/smoke_imagine_v1/04_gen/S01/
test -f 07_Outputs/GROK_BUILD_CINEAGENT_STUDIO_PROMPT_FULL.md && wc -l 07_Outputs/GROK_BUILD_CINEAGENT_STUDIO_PROMPT_FULL.md
```

---

## 10. Load order for new agents

1. `HANDOFF.md` (this file)  
2. `07_Outputs/NEXT_CHAT_STARTER_20260810.md`  
3. Roadmap + `PROJECT_STATUS.md`  
4. One-page law + backend + spend policies  
5. Shot-script + Grok-as-camera knowledge  
6. CineAgent brief + Build prompt (if app work)  
7. Smoke `MANUAL_NEXT_STEPS` + smoke report (if pixels)  

---

## 11. Document control

| Ver | Date | Notes |
|-----|------|-------|
| 2.0 | 2026-08-09 | Continuity through CineAgent brief |
| 3.0 | 2026-08-10 | Full transfer: verification agenda + Build prompt pointer + next starter |

**Maintainer:** Update HEAD/open work at each major session end. Trust `git log -1` over any stale SHA printed in prose.

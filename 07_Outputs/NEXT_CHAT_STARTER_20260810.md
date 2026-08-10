# Next chat starter — 2026-08-10

**You (Director):** copy ONLY the fenced `text` block below into a **new** agent chat as message 1.  
**Do not** summarize from memory. After paste, agent must `git pull` and read `HANDOFF.md`.

Also keep open for yourself:
- `HANDOFF.md`
- `07_Outputs/GROK_BUILD_CINEAGENT_STUDIO_PROMPT_FULL.md` (for Build later)
- Mockup images (attach when starting Grok Build)

---

```text
Continue AI Film Production System — FULL CONTINUITY (treat as unbroken session).

Root: /Users/generationalwealth/Desktop/ai-film-production-system
Repo: https://github.com/JanUrbanik/ai-film-production-system
Branch: main == origin/main after pull. Tags: v1.2, v1.2.1, v1.2.3. Docs ~v1.2.5.
Sister governance ONLY: /Users/generationalwealth/Desktop/master-builder-team
  — do NOT merge film seats into Builder 02_Agents/.

========================================
BOOTSTRAP (MANDATORY)
========================================
export PATH="$HOME/.grok/bin:$PATH"
cd /Users/generationalwealth/Desktop/ai-film-production-system
git pull origin main
git log -1 --oneline
git status -sb
# expect clean main

THEN READ IN ORDER (do not skip):
1) HANDOFF.md
2) 07_Outputs/NEXT_CHAT_STARTER_20260810.md
3) 06_Roadmaps/ROADMAP_SCALE_TEAM_AND_ADVANCED_PLUGINS.md
4) PROJECT_STATUS.md
5) AGENTS.md
6) 01_Architecture/ONE_PAGE_FACTORY_LAW.md
7) 02_Tools/GENERATION_BACKEND_POLICY.md
8) 02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md
9) 02_Tools/ADAPTER_POLICY.md
10) 03_Knowledge/TRANSCRIPT_TO_SHOT_SCRIPT.md
11) 03_Knowledge/PRACTITIONER_GROK_AS_CAMERA.md
12) 01_Architecture/CINEAGENT_STUDIO_PRODUCT_BRIEF.md
13) 10_Sources/ui_mockups/CINEAGENT_STUDIO_MOCKUP_NOTES.md
14) 07_Outputs/GROK_BUILD_CINEAGENT_STUDIO_PROMPT_FULL.md
15) 08_Projects/smoke_imagine_v1/00_brief/MANUAL_NEXT_STEPS.md
16) 07_Outputs/IMAGINE_SMOKE_20260809.md
17) 07_Outputs/PHASE_C_ENV_PREP_20260809.md

Verify:
./scripts/verify_plugin_stack.sh
python3 scripts/validate_packets.py 08_Projects/smoke_imagine_v1/03_shot_list/packets/
ls 08_Projects/smoke_imagine_v1/02_refs/start_frames/
ls 08_Projects/smoke_imagine_v1/04_gen/S01/
# expect no S01_start still and no mp4 unless I already landed assets

========================================
WHAT THIS IS
========================================
Production FACTORY/KIT for AI narrative video:
locked bibles, shot scripts/packets, Imagine generation, binary QC, edit.
NOT a finished film. NOT Master Builder 16 seats. NOT a shipped CineAgent app yet.

========================================
HARD LAWS (INTACT)
========================================
- Imagine-first; Grok-as-camera (start-frame first; SUBJECT+CAMERA+HOLD; multi-take; edit assembles).
- Stills DEFAULT = Grok Imagine Image 2.0 consumer Quality — NOT video; NOT exclusive lock (pluggable backends).
- Motion DEFAULT on Grok path = Video 1.5 — pluggable; adapters only with Director pick or named failure; NO silent multi-vendor fanout.
- Registry: 02_Tools/GENERATION_BACKEND_POLICY.md
- K-SHOT-SCRIPT-001: prose → Asset Bible + Continuity Ledger + Shot Script + Flags; REFS never inside GEN_PROMPT.
- SuperGrok Heavy WEEKLY POOL FIRST; XAI_API_KEY pixels only after pool/extras exhausted + my unlock.
- Binary QC PASS/FAIL; UI “92/100” only as Assumed heuristic if shown.
- Plugins (superpowers/firecrawl/tavily/chrome-devtools) = research/verify/plan only.
- Labels: Verified / Assumed / Speculative.
- Human Director = me.
- CineAgent Studio = future visual SHELL over this repo; does not replace agents/laws.

========================================
PHASE STATUS (DO NOT LOSE)
========================================
A CLOSED
- sims archived: 11_Archive/simulations/
- PRODUCTION_DEPLOY.md exists
- 08_Projects = _template + smoke_imagine_v1

B BLOCKED (P0)
- smoke PACK frozen (prompts, SHOT_SCRIPT, packet S01, checklists, report)
- NO still file, NO mp4 on disk yet
- Manual path ONLY: 08_Projects/smoke_imagine_v1/00_brief/MANUAL_NEXT_STEPS.md
- BLK-1..7 documented in that file + IMAGINE_SMOKE_20260809.md
- Agent cannot headless consumer Imagine; grok CLI is Build TUI not camera
- API key may 403 — do NOT API-gen smoke while pool-first law holds
- Still out: 02_refs/start_frames/S01_start_v1.png
- I2V out: 04_gen/S01/S01_take01.mp4
- Still prompt Image 2.0: 03_shot_list/STILL_PROMPT.md
- I2V prompt Video 1.5: 03_shot_list/I2V_PROMPT.md
- When files land I will say: assets landed

C ENV PREPARED (not exited)
- 03_Roles/seats/R1b_Sequence_Manager.md
- 07_Prompts/FILM_TEAM_ACTIVATION_EPISODE.md
- 07_Prompts/FILM_TEAM_ACTIVATION_FEATURE.md
- SEQUENCE_BOARD + cost_ledger templates
- scripts/validate_packets.py
- 07_Outputs/PHASE_C_ENV_PREP_20260809.md
- Exit C needs B complete + multi-seq dry-run (R1b + ≥2 R8)

D not started (exa/figma admission later)
E pilots FORBIDDEN until B
Studio app NOT coded — brief + FULL build prompt ready

========================================
CINEAGENT STUDIO (FOR LATER IN THIS OR BUILD CHAT)
========================================
Brief: 01_Architecture/CINEAGENT_STUDIO_PRODUCT_BRIEF.md
Mockups notes: 10_Sources/ui_mockups/CINEAGENT_STUDIO_MOCKUP_NOTES.md
FULL paste prompt for Grok Build:
  07_Outputs/GROK_BUILD_CINEAGENT_STUDIO_PROMPT_FULL.md
  → paste ONLY the ```text block (Build CineAgent… through Then stop for review)
  → attach 4 mockup images
  → M0 only first; app dir preferred ~/Desktop/cineagent-studio
Rules: shell not engine; backend dropdowns; Image 2.0 stills default; Video 1.5 motion default; no fake 92/100; SuperGrok pool first.

========================================
KEY HISTORY COMMITS
========================================
78ebc83 Grok Build CineAgent full prompt
2cac274 pluggable backends + CineAgent brief
c27d550 Phase C env prep
468017c Phase B MANUAL_NEXT_STEPS / blockages
101bd13 checklist exec blocked on consumer UI
4dfa110 smoke pack init
410e2a7 K-SHOT-SCRIPT-001
a356bc4 tag v1.2.3 Image 2.0 stills default
4dff04f SuperGrok-first spend
466cf30 Phase A archive + PRODUCTION_DEPLOY

========================================
THIS SESSION’S JOB
========================================
I left the previous chat at ~context limit. I need to VERIFY possible mistakes with you first, WITHOUT losing any state.

Your first response after bootstrap:
1) Confirm git tip + clean tree
2) Confirm all critical paths exist (list ≤20)
3) Confirm Image 2.0 is stills-default not video-lock
4) Confirm smoke still has no pixels
5) Confirm Build prompt file exists and fence/BEGIN M0 present
6) Then WAIT — I will ask verification questions / request corrected starter messages for:
   a) continuing factory work
   b) launching Grok Build CineAgent M0
Do NOT start large refactors, plugin installs, API pixel gen, or skip Phase B unless I explicitly order it.

My next task after verification (I will check one):
[ ] Finish Phase B smoke then say assets landed
[ ] Phase C dry-run after B
[ ] Launch CineAgent Studio M0 via GROK_BUILD_CINEAGENT_STUDIO_PROMPT_FULL.md + mockups
[ ] Fix specific docs mistakes I name
[ ] Other: ________
```

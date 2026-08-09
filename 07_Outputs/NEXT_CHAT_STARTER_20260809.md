# Next chat starter — copy everything below the line

---

```text
Continue AI Film Production System — full continuity handoff.

Root: /Users/generationalwealth/Desktop/ai-film-production-system
Repo: https://github.com/JanUrbanik/ai-film-production-system
Branch: main @ d2e6f9e (origin/main). Tags: v1.2, v1.2.1, v1.2.3. Docs kit ~v1.2.5. Confirm: git log -1 --oneline
Sister (governance only): /Users/generationalwealth/Desktop/master-builder-team — do NOT merge film seats into Builder 02_Agents/.

FIRST: git pull origin main
THEN read and obey in order:
1) HANDOFF.md  (complete state — do not skip)
2) 06_Roadmaps/ROADMAP_SCALE_TEAM_AND_ADVANCED_PLUGINS.md
3) PROJECT_STATUS.md
4) 01_Architecture/ONE_PAGE_FACTORY_LAW.md
5) 02_Tools/GENERATION_BACKEND_POLICY.md
6) 02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md
7) 03_Knowledge/TRANSCRIPT_TO_SHOT_SCRIPT.md
8) 03_Knowledge/PRACTITIONER_GROK_AS_CAMERA.md
9) 01_Architecture/CINEAGENT_STUDIO_PRODUCT_BRIEF.md
10) 08_Projects/smoke_imagine_v1/00_brief/MANUAL_NEXT_STEPS.md
11) 07_Outputs/IMAGINE_SMOKE_20260809.md
12) 07_Outputs/PHASE_C_ENV_PREP_20260809.md

=== WHAT THIS IS ===
Production FACTORY/KIT for AI narrative video (bibles, shot packets, Imagine, QC, edit).
NOT a finished film. NOT Master Builder 16 seats.

=== HARD LAWS ===
- Imagine-first; Grok-as-camera (start-frame first; SUBJECT+CAMERA+HOLD; multi-take; edit assembles).
- Stills DEFAULT = Grok Imagine Image 2.0 consumer Quality — NOT a video model; NOT exclusive (pluggable backends).
- Motion DEFAULT on Grok path = Video 1.5 — pluggable; adapters only with Director pick or named failure; NO silent multi-vendor fanout.
- K-SHOT-SCRIPT-001: prose → Asset Bible + Continuity Ledger + Shot Script + Flags; REFS never in GEN_PROMPT.
- SuperGrok Heavy WEEKLY POOL FIRST for consumer Imagine; XAI_API_KEY pixels only after pool/extras exhausted + Director unlock.
- Binary QC PASS/FAIL; no native “92/100” (UI scores = Assumed heuristic only).
- Plugins (superpowers/firecrawl/tavily/chrome-devtools) = research/verify/plan only.
- Labels: Verified / Assumed / Speculative.
- Human Director = me.
- CineAgent Studio = future visual shell over THIS repo (brief written); does not replace agents.

=== PHASE STATUS ===
A CLOSED — sims in 11_Archive/simulations/; PRODUCTION_DEPLOY.md; clean 08_Projects (_template + smoke_imagine_v1).
B BLOCKED — smoke PACK frozen; NO still/mp4 on disk. Manual only: smoke_imagine_v1/00_brief/MANUAL_NEXT_STEPS.md
   BLK-1..7 documented. Agent cannot headless-gen consumer Imagine. API key may 403 — do not API-gen for smoke.
C ENV PREPARED — R1b_Sequence_Manager.md; FILM_TEAM_ACTIVATION_EPISODE/FEATURE; SEQUENCE_BOARD; cost_ledger.csv; scripts/validate_packets.py.
   Exit C needs B complete + multi-seq dry-run.
D not started (exa/figma). E pilots FORBIDDEN until B. Studio app not coded yet.

=== KEY PATHS ===
Smoke project: 08_Projects/smoke_imagine_v1/
  Still target: 02_refs/start_frames/S01_start_v1.png
  I2V target:   04_gen/S01/S01_take01.mp4
  Prompts: STILL_PROMPT.md (Image 2.0), I2V_PROMPT.md (Video 1.5)
  Packet: 03_shot_list/packets/S01.json (validate_packets PASS)
Spend: 02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md
Backends: 02_Tools/GENERATION_BACKEND_POLICY.md
Shot standard full: 10_Sources/standards/TRANSCRIPT_TO_SHOT_SCRIPT_STANDARD_v1.md
Studio brief: 01_Architecture/CINEAGENT_STUDIO_PRODUCT_BRIEF.md
Mockups notes: 10_Sources/ui_mockups/CINEAGENT_STUDIO_MOCKUP_NOTES.md

=== RECENT COMMITS (do not lose) ===
d2e6f9e docs: align starter and HANDOFF to final tip SHA
0bad770 docs: finalize HANDOFF HEAD pin for GitHub push
16512bc docs: pin HANDOFF HEAD hash after continuity commit
9165ada docs: full continuity HANDOFF v2.0 + next-chat starter for context transfer
2cac274 docs: pluggable gen backends + CineAgent Studio product brief
c27d550 feat(phase-c): prepare scale-team environment after smoke gate
468017c docs(phase-b): document smoke blockages and manual next steps
101bd13 docs(phase-b): record operator checklist execution — blocked on consumer UI
4dfa110 feat(phase-b): initialize smoke_imagine_v1 pack for SuperGrok Heavy
410e2a7 feat(knowledge): ingest transcript-to-shot-script standard K-SHOT-SCRIPT-001
8144826 docs: stabilize HANDOFF HEAD note after Phase A close
9680140 docs: set HANDOFF HEAD to Phase A close tip

=== VERIFY ON START ===
export PATH="$HOME/.grok/bin:$PATH"
git pull origin main && git log -1 --oneline
./scripts/verify_plugin_stack.sh
python3 scripts/validate_packets.py 08_Projects/smoke_imagine_v1/03_shot_list/packets/
Confirm still=no mp4=no unless I say assets landed.

=== MY NEXT TASK ===
[ ] Phase B: I will run SuperGrok Image 2.0 still + I2V per MANUAL_NEXT_STEPS; then say "assets landed"
[ ] Phase C dry-run after B
[ ] Start CineAgent Studio M0 in Grok Build from product brief
[ ] Other: ________

Confirm reads in ≤12 bullets, then execute. Stop for approval before paid API Imagine volume, new plugin installs, or skipping Phase B for pilots.
```

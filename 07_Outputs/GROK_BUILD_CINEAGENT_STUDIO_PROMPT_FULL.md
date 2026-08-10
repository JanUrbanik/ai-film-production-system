# Grok Build — CineAgent Studio FULL PROMPT (finalize)

**Use:** Paste into Grok Build as the build brief. Attach the 4 CineAgent mockup images.  
**Operation root:** `/Users/generationalwealth/Desktop/ai-film-production-system`  
**Updated:** 2026-08-10  

Copy everything inside the single ```text block below.

---

```text
Build CineAgent Studio — visual control panel for the existing AI Film Production System.

========================================
0) MISSION
========================================
Build a dedicated desktop/web app: CineAgent Studio.
It is a CLEAN PROFESSIONAL FRONTEND over the factory already in this repo.
It does NOT replace agents, bibles, workflows, or generation law.
It DOES make Operation Projects + Movie Projects operable visually (storyboard-first).

I am attaching UI mockups. Match dark cinematic UI (black, purple/teal), storyboard-first layout, left rails, right agent/trinity/actions panels.

========================================
1) READ THESE FILES BEFORE ANY CODE
========================================
Absolute root:
/Users/generationalwealth/Desktop/ai-film-production-system

Read first:
HANDOFF.md
01_Architecture/CINEAGENT_STUDIO_PRODUCT_BRIEF.md
01_Architecture/ONE_PAGE_FACTORY_LAW.md
01_Architecture/CANONICAL_PIPELINE.md
01_Architecture/DIAGRAM_CORRECTIONS.md
02_Tools/GENERATION_BACKEND_POLICY.md
02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md
02_Tools/ADAPTER_POLICY.md
02_Tools/GROK_IMAGINE_CAPABILITY_MATRIX.md
02_Tools/adapters/GROK_IMAGINE_ADAPTER.md
02_Tools/schemas/shot_packet.schema.json
02_Tools/plugins/GROK_MARKETPLACE_INTEGRATION.md
03_Roles/PRODUCTION_TEAM.md
03_Knowledge/PRACTITIONER_GROK_AS_CAMERA.md
03_Knowledge/TRANSCRIPT_TO_SHOT_SCRIPT.md
10_Sources/ui_mockups/CINEAGENT_STUDIO_MOCKUP_NOTES.md
10_Sources/standards/TRANSCRIPT_TO_SHOT_SCRIPT_STANDARD_v1.md
AGENTS.md
PROJECT_STATUS.md
README.md

Also open all seat files:
03_Roles/seats/R1_Showrunner.md
03_Roles/seats/R1b_Sequence_Manager.md
03_Roles/seats/R2_Story.md
03_Roles/seats/R3_Character_Bible.md
03_Roles/seats/R4_Environment_Bible.md
03_Roles/seats/R5_Props_Bible.md
03_Roles/seats/R6_Shot_Designer.md
03_Roles/seats/R7_Consistency_Injector.md
03_Roles/seats/R8_Shot_Generator.md
03_Roles/seats/R9_Continuity_Critic.md
03_Roles/seats/R10_Editor.md
03_Roles/seats/R11_Sound.md
03_Roles/seats/R12_Mastering.md

Activation prompts:
07_Prompts/FILM_TEAM_ACTIVATION.md
07_Prompts/FILM_TEAM_ACTIVATION_EPISODE.md
07_Prompts/FILM_TEAM_ACTIVATION_FEATURE.md
07_Prompts/SHOT_GENERATOR.md
07_Prompts/PROJECT_KICKOFF.md

Workflows:
05_Workflows/PRODUCTION_DEPLOY.md
05_Workflows/DEPLOYMENT_CHECKLIST.md
05_Workflows/MVP_SHORT_FILM_RUNBOOK.md
05_Workflows/FEATURE_SCALE_WORKFLOW.md
05_Workflows/INJECTION_ENGINE.md
05_Workflows/CONTINUITY_GATES.md
05_Workflows/QC_RUBRICS.md
05_Workflows/TRANSCRIPT_TO_SHOT_SCRIPT.md
05_Workflows/PLUGIN_AUGMENTED_RESEARCH.md
05_Workflows/engines/CHARACTER_BIBLE_ENGINE.md
05_Workflows/engines/ENVIRONMENT_BIBLE_ENGINE.md
05_Workflows/engines/PROPS_BIBLE_ENGINE.md
05_Workflows/templates/SEQUENCE_BOARD.md
05_Workflows/templates/SHOWRUNNER_FREEZE_CHECKLIST.md
05_Workflows/templates/shot_script/ASSET_BIBLE.md
05_Workflows/templates/shot_script/SHOT_SCRIPT.md
05_Workflows/templates/shot_script/CONTINUITY_LEDGER.csv
05_Workflows/templates/shot_script/FLAGS.md

Skills:
06_Skills/generation/IMAGINE_IMAGE_2_0.md
06_Skills/generation/START_FRAME_FIRST.md
06_Skills/generation/GROK_AS_CAMERA.md
06_Skills/generation/PROMPT_PACKET.md
06_Skills/generation/TRANSCRIPT_TO_SHOT_SCRIPT.md
06_Skills/generation/SHOT_FLEET_OPS.md
06_Skills/generation/I2V_PLATE_LOCK.md
06_Skills/generation/SPEECH_PERFORMANCE_PROMPT.md
06_Skills/generation/WORLD_PACK_IMAGE_2_0.md
06_Skills/generation/EXTEND_CHAIN.md
06_Skills/generation/R2V_MULTI_REF.md
06_Skills/ops/PLUGIN_STACK.md

Scripts / config:
scripts/validate_packets.py
scripts/verify_plugin_stack.sh
.grok/config.toml
.grok/rules.md
02_Tools/plugins/INSTALLED_STACK.snapshot.json
02_Tools/plugins/README.md

Movie template + example project:
08_Projects/_template/README.md
08_Projects/_template/00_brief/
08_Projects/_template/01_bibles/
08_Projects/_template/02_refs/characters/
08_Projects/_template/02_refs/environments/
08_Projects/_template/02_refs/props/
08_Projects/_template/02_refs/wardrobe/
08_Projects/_template/03_shot_list/
08_Projects/_template/03_shot_list/sequences/
08_Projects/_template/04_gen/
08_Projects/_template/05_pass/
08_Projects/_template/06_edit/
08_Projects/_template/07_audio/
08_Projects/_template/08_thumb/
08_Projects/_template/09_qc_log/
08_Projects/_template/09_qc_log/cost_ledger.csv
08_Projects/_template/09_qc_log/CONTINUITY_LEDGER.csv
08_Projects/smoke_imagine_v1/README.md
08_Projects/smoke_imagine_v1/00_brief/MANUAL_NEXT_STEPS.md
08_Projects/smoke_imagine_v1/00_brief/OPERATOR_CHECKLIST.md
08_Projects/smoke_imagine_v1/03_shot_list/STILL_PROMPT.md
08_Projects/smoke_imagine_v1/03_shot_list/I2V_PROMPT.md
08_Projects/smoke_imagine_v1/03_shot_list/SHOT_SCRIPT.md
08_Projects/smoke_imagine_v1/03_shot_list/packets/S01.json
08_Projects/smoke_imagine_v1/09_qc_log/
04_Bibles/templates/ (including WARDROBE_BIBLE.md)
10_Sources/standards/TRANSCRIPT_TO_SHOT_SCRIPT_STANDARD_v1.md
10_Sources/research/GROK_IMAGINE_IMAGE_2_0_2026-08-08.md
07_Outputs/IMAGINE_SMOKE_20260809.md
07_Outputs/PHASE_C_ENV_PREP_20260809.md
09_Bridge/MASTER_BUILDER_HANDOFF.md

========================================
2) PRODUCT MODEL
========================================
Operation Project = factory root (this repo).
Movie Project = 08_Projects/<slug>/ from _template.

App must:
- import/link Operation Project folder
- create/open many Movie Projects
- keep engine vs film separate

========================================
3) MODULES
========================================
Dashboard | Storyboard | Bibles | Agents | Generation | Continuity | Masters | Import

Storyboard: Act→Sequence→Shot cards; timeline; thumb; camera meta; lock badges; sequence flow dependencies.
Bibles / Consistency Trinity: Character + Environment + Props (+ Wardrobe). Version pins, LOCK, multi-view refs.
Agents: map to R1–R12 + R1b; idle/active; one-click activation prompts.
Generation: queue, start-frame-first, multi-take, fleet R8-01…N.
Continuity: Gates 0–4 binary PASS/FAIL. Any numeric score = Assumed heuristic only (mockup 92/100 is NOT native truth).
Masters: assembly + export + continuity report.

========================================
4) GENERATION BACKENDS (CRITICAL)
========================================
REQUIRED dropdowns at project / sequence / shot level:

Still backends (default first):
- grok_imagine_image_2_0_consumer  (DEFAULT stills)
- grok_imagine_image_quality_api
- grok_imagine_image_standard_api
- adapter_still_*

Video backends (default first):
- grok_imagine_video_1_5_consumer  (DEFAULT motion on Grok path)
- grok_imagine_video_1_5_api
- grok_imagine_video_legacy_api
- adapter_video_kling / veo / seedance / *

RULES:
- Image 2.0 is NOT the video generator and NOT an exclusive lock.
- Video 1.5 is default option, not exclusive forever.
- No silent multi-vendor fanout.
- Backend change does NOT bypass bible lock, start-frame gate, or GEN_PROMPT lint.
- Spend banner: SuperGrok Heavy weekly pool first; API backends need Director unlock.
- See 02_Tools/GENERATION_BACKEND_POLICY.md + SPEND_POLICY_SUPERGROK_FIRST.md

Packet/GEN rules:
- Write/read 02_Tools/schemas/shot_packet.schema.json
- Validate via scripts/validate_packets.py
- prompt.full_text = GEN_PROMPT only — NEVER [CHAR_001] / LOC_ / WARD_ / PROP_ in model string
- REFS are metadata/paths only (K-SHOT-SCRIPT-001)

Workflow enforced by UI:
Bible LOCK → shot card → start still (still backend) → gate PASS → packet → video job (video backend) → multi-take → R9 PASS → 05_pass → edit

========================================
5) AGENT UI MAPPING
========================================
Showrunner → R1 (+ R1b sequences)
CharacterBible → R3
EnvironmentBible → R4
PropsBible → R5
ContinuityCritic → R9
DOP → R6
Injector → R7
Shot Generator fleet → R8-01…N
Editor / Sound / Master → R10 / R11 / R12

========================================
6) MOVIE FS CONTRACT
========================================
Create movie ≈ cp -R 08_Projects/_template 08_Projects/<slug>

Folders required:
00_brief/ 01_bibles/ 02_refs/{characters,environments,props,wardrobe}/
03_shot_list/{packets,sequences}/ 04_gen/ 05_pass/ 06_edit/ 07_audio/ 08_thumb/ 09_qc_log/

Key files:
00_brief/TRANSCRIPT.md, FLAGS.md
01_bibles/* + ASSET_BIBLE.md
03_shot_list/SHOT_SCRIPT.md, packets/*.json, SEQUENCE_BOARD
09_qc_log/takes.csv, cost_ledger.csv, CONTINUITY_LEDGER.csv
04_gen/<shot_id>/<shot_id>_takeNN.mp4
05_pass/ PASS only

========================================
7) DESIGN
========================================
Dark cinematic; purple/teal; storyboard-first; high density; mockups are visual source of truth.

========================================
8) TECH + WHERE TO PUT CODE
========================================
Preferred app location (do not dump node_modules into factory root carelessly):
/Users/generationalwealth/Desktop/cineagent-studio
OR
/Users/generationalwealth/Desktop/ai-film-production-system/apps/cineagent-studio

Stack default: Vite + React + TypeScript, local-first FS, no secrets in git.

========================================
9) MILESTONE GATES (HARD STOPS)
========================================
M0 — Shell + Operation import + Movie create/open + nav frames + README run instructions
    STOP for Director approval.
M1 — Storyboard read-only from project files
M2 — Bibles/Trinity locks + ref previews
M3 — Agents panel + activation loader
M4 — Generation queue + backend dropdowns + start-frame checklist + validate_packets
M5 — Continuity binary gates + masters export

========================================
10) FINAL BUILD INSTRUCTIONS (EXECUTE IN ORDER)
========================================
1. git-aware: factory is already on GitHub; do not rewrite history of the factory. App can be new folder/repo.
2. Read all listed law/brief/backend/seat files before scaffolding.
3. Scaffold M0 ONLY first.
4. Detect Operation Project by presence of e.g.:
   AGENTS.md, 03_Roles/seats/, 08_Projects/_template/, 02_Tools/schemas/shot_packet.schema.json, scripts/validate_packets.py
5. Implement Movie create from _template.
6. Wire nav: Dashboard, Storyboard, Bibles, Agents, Generation, Continuity, Masters (empty frames OK in M0).
7. After M0: provide
   - install/run commands
   - what factory files were detected
   - screenshots
   - known gaps
   Then STOP.
8. Do not claim pixel pipeline complete: smoke_imagine_v1 still has no real still/mp4 on disk unless Director added them.
9. Never enable API generation by default.
10. Never implement native 92/100 as truth.
11. Never hardcode Image 2.0 as sole backend or as video backend.
12. When generation UI exists, call validate_packets on packet save/queue.
13. Keep factory laws authoritative if UI mockups conflict (binary QC > vanity scores; pluggable backends > single vendor).

========================================
11) DEFINITION OF DONE (FULL APP — LATER)
========================================
- [ ] Import factory as Operation Project without rewriting seats
- [ ] Create/open Movie Projects under 08_Projects/
- [ ] Still/video backend pickers work; defaults Image 2.0 stills / Video 1.5 motion
- [ ] Can select non-default backends without code fork
- [ ] Start-frame gate blocks hero video queue until PASS
- [ ] validate_packets green on sample packets
- [ ] Continuity UI binary-first
- [ ] No secrets committed
- [ ] README + runbook for operators

========================================
12) FORBIDDEN
========================================
- Replacing the multi-agent factory with a chat-only toy
- Silent Kling+Veo+Grok fanout
- Bypassing bible lock / start-frame / GEN_PROMPT ID lint
- Committing API keys
- Faking Phase B pixel completion
- Mixing Master Builder 16 seats into film seats

========================================
13) BEGIN
========================================
BEGIN M0 NOW.
Create the app folder, scaffold shell, Operation import, Movie create/open, nav frames, README.
Then stop for review.
```

---

## Director use checklist

1. Open Grok Build with access to the factory path.  
2. Attach the 4 mockup images.  
3. Paste the ```text``` block from this file (or the whole fenced prompt).  
4. Allow only **M0**, then review.  
5. Factory engine stays in `ai-film-production-system`; app preferably in `~/Desktop/cineagent-studio`.

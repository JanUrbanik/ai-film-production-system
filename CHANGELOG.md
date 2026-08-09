# Changelog — AI Film Production System

## [1.2.5] — 2026-08-09

### Added
- `02_Tools/GENERATION_BACKEND_POLICY.md` — Image 2.0 = stills default only; video backends pluggable
- `01_Architecture/CINEAGENT_STUDIO_PRODUCT_BRIEF.md` — UI shell over this factory for Grok Build
- `10_Sources/ui_mockups/CINEAGENT_STUDIO_MOCKUP_NOTES.md` — mockup→factory map + 92/100 warning

### Clarified
- Image 2.0 is **not** locked as main video generator
- Studio must expose still/video backend pickers; no silent multi-vendor fanout
- Continuity UI scores = Assumed heuristics; binary QC remains law

## [1.2.4] — 2026-08-09

### Added
- **K-SHOT-SCRIPT-001** Transcript-to-Shot-Script Conversion Standard (full source + knowledge brief)
- Skill `TRANSCRIPT_TO_SHOT_SCRIPT` + workflow `05_Workflows/TRANSCRIPT_TO_SHOT_SCRIPT.md`
- Templates: Asset Bible, Continuity Ledger, Shot Script, Flags; `WARDROBE_BIBLE.md`
- Schema fields: `refs`, `screen_direction`, `lipsync`, `vo_segment`, `gen_prompt_lint`, `wardrobe` pins, 8s policy
- Project template: `TRANSCRIPT.md`, wardrobe refs, ledger CSV starter

### Changed
- Injection engine + PROMPT_PACKET: GEN_PROMPT-only model strings; ID lint
- Seats R1–R3, R6–R9 + activation: conversion path mandatory for prose
- One-page law §5c; AGENTS non-negotiable #8

### Notes
- Agents expand prose via four artifacts before Imagine volume; REFS never reach the model

## [1.2.3] — 2026-08-08

### Added
- Imagine **Image 2.0** research brief + skills `IMAGINE_IMAGE_2_0`, `WORLD_PACK_IMAGE_2_0`
- Matrix §2.0 consumer stills stack (wand/seg/BG remove/multi-ref≤5/smart resize/templates)
- Schema defaults: `model_image=imagine-image-2.0-quality`, `image_surface=consumer_imagine_2.0`

### Changed
- Default stills path: consumer Image 2.0 Quality (not API quality) under SuperGrok Heavy pool
- Bible engines, seats R3/R6/R8, start-frame skill, MVP runbook, one-page law
- Smoke pack stills explicitly Image 2.0 Quality Mode
- API Image 2.0 marked **coming soon** — no invented model ids

### Notes
- Motion remains `grok-imagine-video-1.5`; Image 2.0 upgrades stills that feed I2V

## [1.2.2] — 2026-08-08

### Added
- `05_Workflows/PRODUCTION_DEPLOY.md` — go-live guide for real shoots
- `11_Archive/` + `simulations/` — retired docs-only dry-runs
- `02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md` — SuperGrok Heavy weekly pool before API credits
- `08_Projects/smoke_imagine_v1/` — Phase B consumer Imagine smoke pack
- `07_Outputs/IMAGINE_SMOKE_20260808.md` — smoke report scaffold

### Changed
- Moved `08_Projects/sim_grok_camera_v1` and `sim_mvp_deploy_v1` → `11_Archive/simulations/`
- `08_Projects/` production-clean (`_template` + real slugs only)
- `PROJECT_STATUS.md` / `README.md` / deploy checklist paths updated for archive + live GitHub remote
- Factory law / AGENTS / adapter: consumer Heavy-first spend
- `HANDOFF.md` refreshed for Phase A exit → Phase B consumer smoke

### Notes
- Optional release tag `v1.2.2` when Director approves push
- Pixel smoke completes when Director downloads still+I2V from grok.com/imagine into smoke project

## [1.2.1] — 2026-08-08

### Added
- Full **README** section documenting marketplace integration, verify command, auth notes
- `scripts/verify_plugin_stack.sh` one-command health check
- `02_Tools/plugins/INSTALLED_STACK.snapshot.json` + plugins `README.md`
- Verify artifact `07_Outputs/PLUGIN_STACK_VERIFY_20260808.md`

### Verified
- `./scripts/verify_plugin_stack.sh` → 16 PASS / 0 FAIL
- Live tavily search + firecrawl scrape PASS; MCP doctor 4 healthy / 0 failing

## [1.2] — 2026-08-08

### Added
- Grok Build marketplace integration (`02_Tools/plugins/GROK_MARKETPLACE_INTEGRATION.md`)
- Project `.grok/config.toml` + rules for plugin stack (superpowers, firecrawl, tavily, chrome-devtools)
- Plugin-augmented research workflow + `06_Skills/ops/PLUGIN_STACK.md`
- E2E plugin test reports and research notes under `07_Outputs/` and `10_Sources/research/`

### Fixed
- Tavily MCP OAuth: cleared expired tokens, completed PKCE re-auth
- `grok mcp doctor`: 4 healthy / 0 failing after fix

### Verified
- Full expandable research path: tavily + firecrawl + chrome-devtools + superpowers checklist
- Policy held: plugins do not replace Grok Imagine / Grok-as-camera pixel path

## [1.1] — 2026-08-07

### Added
- Odyssey practitioner method (Grok-as-camera): knowledge + skills
- Start-frame-first gate, speech performance prompting
- Deployment checklist + `PROJECT_STATUS.md`
- MVP dry-run `sim_mvp_deploy_v1` checklist verification

## [1.0] — 2026-08-07

### Added
- Production team seats R1–R12, bible engines, injection schema
- Imagine capability matrix, adapter policy, continuity gates
- Master Builder bridge; GitHub repo bootstrap

## Notes
- Live Imagine smoke / finished film renders remain operator production steps, not kit blockers.
- Keep NordVPN off or split-tunnel Warp during long agent/MCP sessions.

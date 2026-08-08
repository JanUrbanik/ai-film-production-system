# Deployment checklist — Grok-as-camera factory

**Version:** 1.1  
**Date:** 2026-08-07  
**Applies to:** `ai-film-production-system` @ main ≥ v1.1  
**Mode default:** MVP Short (Imagine-only)

Use this before the first real production run and again before any paid gen campaign.

---

## A. Environment

- [ ] Factory root available and current: `ai-film-production-system`
- [ ] Git on `main`; confirm Grok-as-camera ingest present  
  `git log --oneline -5` includes v1.1 practitioner method (or later)
- [ ] Read once:  
  - `01_Architecture/ONE_PAGE_FACTORY_LAW.md`  
  - `03_Knowledge/PRACTITIONER_GROK_AS_CAMERA.md`  
  - `02_Tools/GROK_IMAGINE_CAPABILITY_MATRIX.md`
- [ ] Generation access ready: **SuperGrok Heavy** → `grok.com/imagine` (weekly pool first)
- [ ] Settings → Usage checked; API key path only if Director unlocked after pool/extras exhausted (`02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md`)
- [ ] NLE installed (CapCut or DaVinci)
- [ ] Disk space for stills + multi-take video downloads
- [ ] Optional plugins (Grok Build): `./scripts/verify_plugin_stack.sh` exits 0
- [ ] Optional: `grok plugin list` shows superpowers/firecrawl/tavily/chrome-devtools
- [ ] Optional: `grok mcp doctor` healthy if using research/browser MCP this session
- [ ] Read `02_Tools/plugins/GROK_MARKETPLACE_INTEGRATION.md` if using plugins
- [ ] Optional: Master Builder only if running a governed charter

---

## B. Session knowledge load

- [ ] Load `07_Prompts/FILM_TEAM_ACTIVATION.md` into the agent/session
- [ ] Confirm activation references practitioner method (Grok = camera / start-frame first)
- [ ] Skills resolvable:  
  `GROK_AS_CAMERA` · `START_FRAME_FIRST` · `SPEECH_PERFORMANCE_PROMPT` · `I2V_PLATE_LOCK` · `SHOT_FLEET_OPS`
- [ ] Adapter policy understood: Imagine default; no multi-vendor fanout unless Director approves a named failure class
- [ ] Claim labels required: Verified / Assumed / Speculative

---

## C. Project bootstrap

- [ ] `cp -R 08_Projects/_template 08_Projects/<slug>`
- [ ] `00_brief/`: logline, beats (3–7 MVP), consent
- [ ] Director OK on beats
- [ ] Style Contract LOCKED (closed camera vocabulary)
- [ ] Character bible + ref pack LOCKED (if cast on camera)
- [ ] Environment bible + plates LOCKED
- [ ] Props bible LOCKED only if hero prop exists (else R5 standby)
- [ ] Shot list frozen; every card has **SUBJECT + CAMERA + HOLD**
- [ ] Speech shots marked for performance blocks

---

## D. Start-frame gate (before video spend)

- [ ] Start still generated per hero shot (image quality model)
- [ ] Storyboard-worthy checklist passed (`06_Skills/generation/START_FRAME_FIRST.md`)
- [ ] Still-gate approver (Director or designee) signed off
- [ ] Still paths recorded for injector (`source_still` / still id)
- [ ] **No** hero `i2v` jobs launched before gate pass

---

## E. Injection + generation

- [ ] R7 packets validate against `02_Tools/schemas/shot_packet.schema.json`
- [ ] Each motion packet includes SUBJECT + CAMERA + HOLD
- [ ] Speech packets include dialogue + emotion + pauses/beats
- [ ] Mode priority respected: **I2V > R2V > extend > edit > T2V**
- [ ] Cost sketch written: `takes × seconds × rate` (+ stills)
- [ ] Working res 720p for iteration; 1080p only for hero finals when needed
- [ ] R8 multi-take plan (default 4–8 for hero shots)
- [ ] Temporary Imagine URLs downloaded immediately into `04_gen/<shot_id>/`
- [ ] Naming: `Sxx_takeNN.mp4`; never overwrite PASS
- [ ] Generators never self-PASS

---

## F. QC + post

- [ ] R9 runs take/scene gates (`QC_RUBRICS.md`, `CONTINUITY_GATES.md`)
- [ ] FAIL logged with `fail_tags`; repair ladder before adapter spend
- [ ] PASS copied only to `05_pass/`
- [ ] R10 assembles from PASS bin (raw-footage mindset)
- [ ] R11 checks native audio / ADR path if lips weak
- [ ] Delivery package:  
  - master export  
  - PASS list  
  - `09_qc_log` continuity report  
  - bible version pins used

---

## G. Go-live acceptance (first shipped piece)

- [ ] Every cast shot used locked character refs / approved start frames
- [ ] No hero motion without start-frame gate
- [ ] Every packet had SUBJECT + CAMERA + HOLD
- [ ] Multi-take evidence exists under `04_gen/`
- [ ] QC log complete; approximate keep rate noted
- [ ] Cut (30–90s MVP) lands beats without identity/location teleport
- [ ] AI disclosure handled if publishing
- [ ] Postmortem claims labeled if written

---

## H. Optional hardening (not required for first deploy)

- [ ] Review archived docs-only dry-runs under `11_Archive/simulations/` (reference only)
- [ ] Minimal paid smoke: 1 still → 1 I2V → download → QC note (`PRODUCTION_DEPLOY.md` §5)
- [ ] Backup off-machine (GitHub remote is live)
- [ ] Fuller Odyssey transcript → bump `K-PRAC-GROK-CAMERA-001`
- [ ] Re-verify docs.x.ai duration/pricing before large campaigns
- [ ] Read go-live guide: `05_Workflows/PRODUCTION_DEPLOY.md`

---

## Deploy sign-off

| Field | Value |
|-------|--------|
| Operator | |
| Date | |
| Project slug | |
| Mode | MVP / Episode / Feature |
| Imagine surface | API / consumer UI / both |
| A–G complete? | YES / NO |
| Notes | |

**Rule:** Do not start volume video generation until sections **A–D** are checked.

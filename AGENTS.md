# AGENTS.md — AI Film Production System

## Mission

Produce short-to-long AI narrative video with locked bibles, Grok Imagine generation, ruthless QC, and honest epistemics.

## Non-negotiables

1. **Imagine-first** default (`02_Tools/`) — stills default **Image 2.0** consumer; motion default Video **1.5**; both are **options** in a pluggable backend registry (not exclusive locks).  
2. **Claim labels** on capabilities (`00_Epistemics/`).  
3. **Human Director** final taste.  
4. **No identity without refs.**  
5. **Short clips + edit**, not one-shot features.  
6. **Separate from Master Builder seats** — bridge only.  
7. **SuperGrok Heavy weekly pool first** — consumer Imagine before any `XAI_API_KEY` spend (`02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md`).  
8. **Prose → shot script standard** — Asset Bible + ledger + shot script + flags; REFS never in GEN_PROMPT (`K-SHOT-SCRIPT-001`).  
9. **LAW 4 — Description follows the image** `[M]` — VDL is written from the approved still, never from the script (`10_Sources/method/CINEKIT_METHOD_LAYER.md`).  
10. **LAW 5 — The asset wins** `[M]` — approved asset overrides contradictory script; escalate only if narrative-critical.  
11. **LAW 6 — One attachment convention per project** `[M]` — ref injection order is locked project-wide, never improvised per shot.  
12. **Epistemic `[M]`** — imported method is process, not verified Grok behavior. Matrix + K-SHOT-SCRIPT-001 win conflicts.  

## Runtime preference

- **Pixels default:** SuperGrok Heavy consumer Imagine (`grok.com/imagine` / apps) — subscription weekly pool  
- **API Imagine:** last resort only after weekly pool (+ optional consumer Extra Credits) exhausted and Director unlocks  
- Grok Build interactive sessions may use account pool; Build-with-API-key is a separate API ledger  
- Master Builder FULL charter optional for governance-heavy jobs  
- Marketplace plugins (superpowers, firecrawl, tavily, chrome-devtools): research/verify/planning only — see `02_Tools/plugins/GROK_MARKETPLACE_INTEGRATION.md`  

## When unsure

Re-read capability matrix and re-verify docs.x.ai before expanding tool claims. Prefer installed plugins over reinventing research tools; never let plugins bypass bible/start-frame gates.

# Research note — plugin stack workflow test

**Date:** 2026-08-08  
**Workflow:** `05_Workflows/PLUGIN_AUGMENTED_RESEARCH.md`  
**Project:** ai-film-production-system (factory plugin integration test)  
**Live Imagine pixels:** not in scope  

## Question

Do the installed Grok marketplace expandable plugins function end-to-end for film-factory research/verify/plan stages without replacing Imagine generation?

## Environment (Verified)

| Check | Result |
|-------|--------|
| `grok` CLI | 0.2.117 |
| Plugins installed | superpowers, firecrawl, tavily, chrome-devtools |
| MCP doctor chrome-devtools | healthy (29 tools) |
| MCP doctor firecrawl | healthy (26 tools) |
| MCP doctor tavily | **failing** — OAuth authorization required |
| grok.com cloud auth | skipped (auth expired — `grok login` recommended) |
| Factory policy doc | `02_Tools/plugins/GROK_MARKETPLACE_INTEGRATION.md` present |

## Findings

### superpowers — PASS (inventory)

**Verified:** Skills present on disk under installed plugin package, including:

- writing-plans, executing-plans  
- verification-before-completion  
- systematic-debugging  
- test-driven-development  
- brainstorming, subagent-driven-development, …

**Assumed:** Skills load in interactive Grok Build TUI when project `.grok/` is present.  
**Action:** Use for stage plans before volume gen (R1), not for pixels.

### firecrawl — PASS (live scrape)

**Verified from scrape** of https://docs.x.ai/developers/model-capabilities/video/generation :

- Max duration: **1–15 seconds**  
- Resolutions: **480p / 720p / 1080p** (1080p on grok-imagine-video-1.5 for T2V/I2V; R2V cap 720p)  
- Model ID: **grok-imagine-video-1.5** documented  
- Generation is **asynchronous** (request_id + poll)

**Factory impact:** Aligns with existing `GROK_IMAGINE_CAPABILITY_MATRIX.md` — **no matrix change required**.

### chrome-devtools — PASS (live browser)

**Verified:**

- Opened docs page successfully  
- Title: **Video Generation | SpaceXAI Docs**  
- Page text includes **duration** and **15 seconds**

**Factory impact:** Suitable for UI/doc claim verification branch (R9 web claims only).

### tavily — FAIL (auth)

**Verified failure mode:**

- MCP handshake: OAuth authorization required  
- No tavily_* tools exposed while unhealthy  
- Matches policy: escalate auth to Director/User — do not invent search results

**Fix:** Re-auth Tavily MCP in Grok (`/mcp` or provider OAuth). Optional: `grok login` if grok.com source also expired.

## Workflow path exercised

```text
Trigger: tool-truth check before spend
  → firecrawl scrape primary docs (PASS)
  → chrome-devtools corroborate page (PASS)
  → tavily search (FAIL auth — logged)
  → superpowers inventory (PASS)
  → labeled note filed (this file)
  → core Imagine path NOT invoked (correct)
```

## Seat map check

| Seat guidance | Observed |
|---------------|----------|
| Plugins ≠ camera | Honored — no I2V attempted |
| Research → 10_Sources/research | This note |
| Escalate MCP auth fail | Tavily FAIL recorded |

## Verdict

| Component | Status |
|-----------|--------|
| Plugin **install** surface | PASS |
| firecrawl functional | PASS |
| chrome-devtools functional | PASS |
| superpowers skills present | PASS |
| tavily functional | **FAIL — re-auth needed** |
| Policy integration (no pixel bypass) | PASS |
| Overall expandable research branch | **PARTIAL PASS** (3/4 runtimes green) |

## Actions for Director

1. **Required for full green:** Re-authorize Tavily MCP; optional `grok login`.  
2. **No change** to Imagine matrix from this scrape (already consistent).  
3. Safe to use firecrawl + chrome-devtools + superpowers on research branch now.  
4. Keep Nord off / split-tunnel during long Grok MCP sessions.

## Labels legend

- **Verified** — observed this run  
- **Assumed** — reasonable, not re-proven in TUI  
- **Speculative** — none claimed here  

# Plugin stack workflow test report

**Date:** 2026-08-08  
**Factory version:** 1.2  
**Detailed note:** `10_Sources/research/NOTE_20260808_plugin_stack_workflow_test.md`

## Summary

| Plugin | Role | Test | Result |
|--------|------|------|--------|
| superpowers | planning/verify skills | skill inventory on disk | **PASS** |
| firecrawl | scrape primary docs | live scrape docs.x.ai video generation | **PASS** |
| chrome-devtools | browser verify | open docs page, title + duration text | **PASS** |
| tavily | structured search | MCP search | **FAIL** (OAuth required) |

**MCP doctor:** 2 healthy · 1 failing (tavily)  
**Imagine pixels:** not run (correct per policy)

## Score

- Runtime expandable path: **PARTIAL PASS (3/4)**  
- Policy compliance: **PASS**  
- Blocks MVP pixels: **NO** (plugins optional for MVP)

## Operator fix for full PASS

```bash
export PATH="$HOME/.grok/bin:$PATH"
grok login          # if grok.com auth expired
# then open Grok TUI in factory dir → /mcp → authorize tavily
grok mcp doctor     # expect 3 healthy
```

## Evidence highlights (Verified)

Firecrawl scrape confirmed video duration 1–15s, resolutions 480p/720p/1080p, model `grok-imagine-video-1.5`, async polling — consistent with factory matrix.

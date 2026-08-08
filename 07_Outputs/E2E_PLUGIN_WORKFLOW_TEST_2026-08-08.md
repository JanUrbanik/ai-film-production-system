# E2E plugin + factory workflow test

**Date:** 2026-08-08  
**Factory:** ai-film-production-system v1.2+  
**Goal:** Fix Tavily OAuth + full expandable research path + confirm camera path untouched

## 1. Tavily OAuth fix (Verified)

| Step | Result |
|------|--------|
| Root cause | Tokens from 2026-07-30 expired (`expires_in` 86400); refresh grant failed |
| Action | Removed stale `tavily:https://mcp.tavily.com/mcp` from `~/.grok/mcp_credentials.json` (firecrawl kept); backup saved |
| Re-auth | OAuth PKCE + dynamic client registration + local callback `127.0.0.1:8765` |
| New tokens | Bearer, `expires_in` 86400, refresh_token present |
| `grok mcp doctor` | **4 healthy / 0 failing** (chrome-devtools, tavily, firecrawl, grok_com_github) |

## 2. MCP doctor snapshot (this run)

```

MCP Doctor

  Config sources
    ~/.grok/config.toml                      0 servers
    /Users/generationalwealth/Desktop/ai-film-production-system/.grok/config.toml 0 servers
    plugin: firecrawl                        1 server
    plugin: chrome-devtools-mcp              1 server
    plugin: tavily                           1 server
    ~/.claude.json                           0 servers
    .mcp.json                                not found
    grok.com                                 1 server

  chrome-devtools (stdio: npx chrome-devtools-mcp@1.6.0)
    ✓ command found (/Users/generationalwealth/.nvm/versions/node/v24.18.1/bin/npx)
    ✓ server started (0.0s)
    ✓ handshake OK (protocol 2025-06-18)
    ✓ 29 tools discovered

  grok_com_github (http: https://api.githubcopilot.com/mcp/x/all)
    ✓ server started (0.0s)
    ✓ handshake OK (protocol 2025-06-18)
    ✓ 90 tools discovered

  tavily (http: https://mcp.tavily.com/mcp)
    ✓ server started (1.0s)
    ✓ handshake OK (protocol 2025-06-18)
    ✓ 5 tools discovered

  firecrawl (http: https://mcp.firecrawl.dev/v2/mcp)
    ✓ server started (1.0s)
    ✓ handshake OK (protocol 2025-06-18)
    ✓ 26 tools discovered

Found 4 healthy, 0 failing.
```

## 3. Plugin functional results

| Plugin | Test | Result |
|--------|------|--------|
| tavily | search `grok imagine video 1.5 duration site:docs.x.ai` | **PASS** — docs hits returned |
| firecrawl | scrape video generation docs | **PASS** — duration 1–15s, res 480/720/1080 |
| chrome-devtools | open docs URL, title contains Video | **PASS** |
| superpowers | verification-before-completion checklist in E2E note | **PASS** (process) |

## 4. Factory integration artifacts

| Artifact | Status |
|----------|--------|
| `10_Sources/research/NOTE_20260808_e2e_plugin_full.md` | Written by E2E agent |
| Prior note `NOTE_20260808_plugin_stack_workflow_test.md` | Historical partial (pre-fix) |
| Camera MVP sim packets (`sim_mvp_deploy_v1`) | Still present; SUBJECT/CAMERA/HOLD intact |
| Imagine pixel generation | **Not run** (policy correct) |

## 5. End-to-end path verified

```text
Trigger research branch
  → tavily search (PASS)
  → firecrawl scrape (PASS)
  → chrome-devtools verify (PASS)
  → superpowers verification checklist (PASS)
  → labeled note in 10_Sources/research/
  → no I2V / no bible bypass
  → core Grok-as-camera path remains available
```

## 6. Verdict

| Gate | Result |
|------|--------|
| Tavily OAuth | **FIXED** |
| All enabled MCPs healthy | **PASS (4/4 doctor)** |
| Plugin research E2E | **PASS** |
| Policy (plugins ≠ camera) | **PASS** |
| Full live film render | **N/A** (not requested; separate smoke) |

**Overall: PASS** for integrated expandable workflow after Tavily fix.

## 7. Operator maintenance

- When Tavily fails again after ~24h: re-run OAuth or complete browser auth via Grok TUI `/mcp`.
- Prefer keeping Nord off / split-tunnel Warp during MCP OAuth and long agent runs.
- Optional: `grok login` if grok.com features needed beyond plugins.

# Plugin stack verify run

**Date:** 2026-08-08T01:36:14Z
**Script exit:** 0

## script output
```
=== AI Film Production System — plugin stack verify ===
root: /Users/generationalwealth/Desktop/ai-film-production-system

PASS  repo file 02_Tools/plugins/GROK_MARKETPLACE_INTEGRATION.md
PASS  repo file 02_Tools/plugins/INSTALLED_STACK.snapshot.json
PASS  repo file 05_Workflows/PLUGIN_AUGMENTED_RESEARCH.md
PASS  repo file 06_Skills/ops/PLUGIN_STACK.md
PASS  repo file .grok/config.toml
PASS  repo file .grok/rules.md
PASS  .grok/config.toml declares plugin stack
PASS  grok CLI: grok 1.0.0 (3cd0d0cbcebe) [stable]
PASS  plugin installed: superpowers
PASS  plugin installed: firecrawl
PASS  plugin installed: tavily
PASS  plugin installed: chrome-devtools

MCP Doctor

  Config sources
    ~/.grok/config.toml                      0 servers
    /Users/generationalwealth/Desktop/ai-film-production-system/.grok/config.toml 0 servers
    plugin: chrome-devtools-mcp              1 server
    plugin: firecrawl                        1 server
    plugin: tavily                           1 server
    ~/.claude.json                           0 servers
    .mcp.json                                not found
    grok.com                                 1 server

  chrome-devtools (stdio: npx chrome-devtools-mcp@1.6.0)
    ✓ command found (/Users/generationalwealth/.nvm/versions/node/v24.18.1/bin/npx)
    ✓ server started (0.0s)
    ✓ handshake OK (protocol 2025-06-18)
    ✓ 29 tools discovered

  tavily (http: https://mcp.tavily.com/mcp)
    ✓ server started (0.8s)
    ✓ handshake OK (protocol 2025-06-18)
    ✓ 5 tools discovered

  firecrawl (http: https://mcp.firecrawl.dev/v2/mcp)
    ✓ server started (0.8s)
    ✓ handshake OK (protocol 2025-06-18)
    ✓ 26 tools discovered

  grok_com_github (http: https://api.githubcopilot.com/mcp/x/all)
    ✓ server started (0.0s)
    ✓ handshake OK (protocol 2025-06-18)
    ✓ 90 tools discovered

Found 4 healthy, 0 failing.
PASS  mcp doctor: 0 failing
PASS  mcp healthy: tavily
PASS  mcp healthy: firecrawl
PASS  mcp present: chrome-devtools

SUMMARY pass=16 fail=0 warn=0
```


## Live functional (same session)

- tavily_search: PASS (docs.x.ai hit)
- firecrawl scrape: PASS (max duration 15 seconds)
- Imagine pixel gen: not run (policy)

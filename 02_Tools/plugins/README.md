# Grok toolkit marketplace (factory)

## Purpose

Wire **xAI Grok Build plugin marketplace** expandable components into this film factory **without** replacing Grok Imagine as the camera.

## Files

| File | Role |
|------|------|
| `GROK_MARKETPLACE_INTEGRATION.md` | Policy, catalog, seat map, forbidden uses |
| `INSTALLED_STACK.snapshot.json` | Pinned snapshot of local installs (no secrets) |
| `README.md` | This index |

## Enabled stack

- **superpowers** — plans / verification  
- **firecrawl** — scrape/crawl  
- **tavily** — structured search  
- **chrome-devtools** — live browser verify  

## Workflows / skills

- `05_Workflows/PLUGIN_AUGMENTED_RESEARCH.md`  
- `06_Skills/ops/PLUGIN_STACK.md`  
- Project config: `.grok/config.toml`, `.grok/rules.md`

## Verify

```bash
./scripts/verify_plugin_stack.sh
# optional live research E2E (uses MCP quota):
# grok -p "..."  # see 07_Outputs/E2E_PLUGIN_WORKFLOW_TEST_*.md
```

## Law

Plugins = research / verify / plan only.  
Pixels = Grok Imagine + Grok-as-camera path.

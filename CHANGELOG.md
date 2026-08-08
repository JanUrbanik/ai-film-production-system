# Changelog — AI Film Production System

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

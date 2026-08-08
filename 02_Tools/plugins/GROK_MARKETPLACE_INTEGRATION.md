# Grok toolkit marketplace — analysis & film-factory integration

**Status:** v1.0 integrated  
**Date:** 2026-08-08  
**Marketplace:** `xai-org/plugin-marketplace` (`https://github.com/xai-org/plugin-marketplace.git`)  
**Local cache:** `~/.grok/marketplace-cache/`  
**Install registry:** `~/.grok/installed-plugins/registry.json`

---

## 1. What the “marketplace folder” is

Not a Desktop folder. On this machine it is the **user-level Grok Build plugin system**:

| Location | Role |
|----------|------|
| `~/.grok/marketplace-cache/<id>/` | Cloned catalog (README + `.grok-plugin/marketplace.json`) |
| `~/.grok/installed-plugins/` | Installed expandable plugin packages (skills + MCP) |
| `master-builder-team/.grok/config.toml` | Project declaration of plugin stack (Builder) |
| `ai-film-production-system/.grok/config.toml` | Project declaration for **this factory** (added) |

Plugins expand Grok Build with **skills**, **commands**, **MCP servers**, hooks — without changing the film seat roster.

---

## 2. Catalog snapshot (expandable components)

From marketplace.json (official index):

| Plugin | Category (approx) | Film factory default |
|--------|-------------------|----------------------|
| **superpowers** | Planning / execution discipline | **Enabled** |
| **firecrawl** | Web scrape/crawl/extract | **Enabled** (research) |
| **tavily** | Structured web research MCP | **Enabled** (research default) |
| **chrome-devtools** | Live browser verify MCP | **Enabled** (verify) |
| exa | Alt research MCP | Optional swap for tavily |
| figma | Design-to-code | Optional (art direction stills) |
| vercel / railway / cloudflare | Deploy platforms | Optional (web delivery only) |
| sentry / axiom | Observability | Optional (app backends) |
| mongodb / neon | Data stores | Optional (asset DB later) |
| stripe | Payments | Out of scope MVP |
| tinyfish | Browser automation/search | Optional |

---

## 3. Installed stack (Verified on this machine)

| Plugin | Version (registry) | Primary film use |
|--------|--------------------|------------------|
| superpowers | 6.2.0 | Plans, verification-before-completion, systematic debug of pipeline docs/scripts |
| firecrawl | 1.1.0 | Scrape Imagine docs, competitor method pages, transcript-adjacent pages |
| tavily | 1.0.0 | Cited research for tool limits, market refs, practitioner methods |
| chrome-devtools | 1.6.0 | Verify live grok.com/imagine UI claims, console errors, screenshots |

**Skill highlights:**

- **superpowers:** `writing-plans`, `executing-plans`, `verification-before-completion`, `systematic-debugging`, `test-driven-development`, `brainstorming`, …
- **firecrawl:** `firecrawl-scrape`, `firecrawl-search`, `firecrawl-crawl`, `firecrawl-map`, `firecrawl-parse`, …
- **tavily:** `tavily-web`, `tavily-best-practices`, domain research skills
- **chrome-devtools:** `chrome-devtools`, performance/a11y/debug skills

---

## 4. Integration law (film factory)

### 4.1 What plugins may do

| Stage | Allowed plugin use |
|-------|--------------------|
| Preproduction research | tavily / firecrawl / exa for **docs & methods** (label claims) |
| Tool truth checks | firecrawl scrape `docs.x.ai`; chrome-devtools on public Imagine UI |
| Pipeline/docs work | superpowers planning + verification |
| Production gen | **Grok Imagine** remains pixel path — plugins do **not** replace I2V |
| QC of web claims | chrome-devtools screenshots/console when claim depends on live page |
| Post | NLE local; plugins only if publishing web page |

### 4.2 What plugins must not do

1. Bypass start-frame gate or bible locks.  
2. Invent Imagine capabilities from plugin marketing.  
3. Auto-enable multi-vendor video adapters.  
4. Store secrets in git.  
5. Run browser automation against private accounts without Director OK.  
6. Treat MCP failure as silent success — escalate.

### 4.3 Runtime locus

| Surface | Plugins |
|---------|---------|
| **Grok Build** in this repo | Full stack when MCP healthy |
| **Warp/Oz** | May use parallel tools (web, shell); still follow same policy labels |
| **Consumer Imagine UI only** | Plugins N/A — camera method still applies |

Verify: `grok plugin list` · `grok mcp doctor` (from project dir after `grok` auth).

---

## 5. Seat → plugin map

| Film seat | Plugin | When |
|-----------|--------|------|
| R1 Showrunner | superpowers | Stage plans, verification before “gen volume” |
| R2 Story | tavily (optional) | Period/setting research with citations |
| R3–R5 Bible leads | firecrawl (optional) | Reference boards from allowed public sources |
| R6 Shot Designer | — | Camera skills in-repo first |
| R7 Injector | — | Schema + packets; no MCP required |
| R8 Generator | — | Imagine API/UI only |
| R9 Continuity Critic | chrome-devtools (optional) | Only if QC depends on **web page** truth, not frame pixels |
| R10–R12 Post | — | Local NLE/audio |
| Governance (Builder bridge) | full stack | FULL charters, tool rating |

---

## 6. Workflow hooks (expandable steps)

Inserted into existing workflows as **optional branches**:

```text
MVP path (unchanged core)
  A–D deploy gates
  brief → bibles → start frames → packets → Imagine → QC → edit

Expandable research branch (plugins)
  before bible lock OR when tool claims uncertain:
    tavily/firecrawl → cited notes in 10_Sources/research/
    chrome-devtools → screenshot proof if UI-dependent
    label Verified/Assumed/Speculative
    then resume core path
```

See: `05_Workflows/PLUGIN_AUGMENTED_RESEARCH.md`  
Skill: `06_Skills/ops/PLUGIN_STACK.md`

---

## 7. Not installed (do not assume)

exa, figma, vercel, neon, mongodb, stripe, railway, cloudflare, sentry, axiom, tinyfish — **catalog only** until Director approves install.

To expand later:

```bash
grok plugin marketplace add xai-org/plugin-marketplace   # if needed
grok plugin install <name> --trust
# authorize MCP in TUI: /mcp
```

---

## 8. Relationship to Master Builder

Builder already declares the same four plugins in `.grok/config.toml` + KB ENTRY-009.  
This factory **mirrors** that stack for production research/verify — it does **not** merge Builder seats.

---

## 9. Re-verify commands

```bash
export PATH="$HOME/.grok/bin:$PATH"
cd /path/to/ai-film-production-system
./scripts/verify_plugin_stack.sh
# equivalent manual:
grok plugin list
grok mcp doctor
```

Snapshot of installs (no secrets): `INSTALLED_STACK.snapshot.json`  
Last full E2E report: `07_Outputs/E2E_PLUGIN_WORKFLOW_TEST_2026-08-08.md`

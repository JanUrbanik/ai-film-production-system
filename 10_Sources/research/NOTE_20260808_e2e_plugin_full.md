# Research note — E2E plugin-augmented path (full)

**Date:** 2026-08-08  
**Scope:** Plugin research/verify path only  
**Live Imagine pixels:** not invoked  

## Question

What are the documented maximum duration and resolutions for `grok-imagine-video-1.5`, and do the marketplace plugins (tavily, firecrawl, chrome-devtools, superpowers) complete an end-to-end research path without calling Imagine generation?

## Sources

| # | Source | How used |
|---|--------|----------|
| 1 | Tavily search: `grok-imagine-video-1.5 maximum duration site:docs.x.ai` | Discovery + snippets from docs.x.ai |
| 2 | https://docs.x.ai/developers/model-capabilities/video/generation | Firecrawl scrape (markdown + JSON extract: max duration, resolutions) |
| 3 | Same URL via Chrome DevTools | Live page open + `document.title` check |
| 4 | https://docs.x.ai/developers/model-capabilities/video/reference-to-video | Tavily hit (R2V max duration / resolution caps) |

## Findings

### Max duration — **Verified**

- Allowed `duration` range on video generation: **1–15 seconds** (docs Configuration → Duration).
- Example SDK calls use `duration=15` with model `grok-imagine-video-1.5`.
- Tavily hit on reference-to-video: on `grok-imagine-video-1.5`, max duration is **15 seconds**.
- Video **editing** does not take custom duration; edited output capped at **8.7 seconds** of original (mode-specific; not T2V max).

### Resolutions — **Verified**

| Resolution | Notes |
|------------|--------|
| `480p` | Standard definition; **default**; faster processing |
| `720p` | HD |
| `1080p` | Full HD; supported on `grok-imagine-video-1.5` for **text-to-video** and **image-to-video** |

- **Reference-to-video** is capped at **720p** (docs note; also Tavily R2V page).
- Video **editing** does not support custom resolution; output matches input, capped at 720p.

### Page title corroboration — **Verified**

- Chrome DevTools title: **`Video Generation | SpaceXAI Docs`**
- `document.title.includes('Video')` → **true**

### Epistemic labels

| Claim | Label |
|-------|--------|
| Duration 1–15s for generation | **Verified** (primary docs scrape + config section) |
| Resolutions 480p / 720p / 1080p | **Verified** (primary docs resolution table) |
| 1080p T2V/I2V on grok-imagine-video-1.5 | **Verified** |
| R2V max 720p / max 15s | **Verified** (docs note / Tavily R2V page) |
| Factory matrix still aligned | **Assumed** until capability matrix re-diffed in-repo |
| No pixel spend this run | **Verified** (no Imagine video tool calls) |

## Factory action

1. Keep clip length planning within **1–15s** per generation request; compose longer narratives via short clips + edit (factory non-negotiable).
2. Prefer **720p** for production drafts; use **1080p** only when T2V/I2V quality budget justifies cost/latency.
3. Do not request 1080p for **reference-to-video** (cap 720p).
4. No capability-matrix change required from this E2E unless an internal doc still claims a lower max duration.
5. Plugins stay on research/verify branch only — never bypass bible/start-frame gates for pixels.

## Plugin results table

| Plugin | Role this run | Result | Evidence |
|--------|---------------|--------|----------|
| **tavily** | Search `grok-imagine-video-1.5 maximum duration site:docs.x.ai` | **PASS** | Returned docs.x.ai hits including Video Generation, Reference-to-Video (max 15s), Image-to-Video, Extension |
| **firecrawl** | Scrape generation docs; extract max duration + resolutions only | **PASS** | JSON extract: `max_duration` = 15 seconds, `duration_range` = 1–15 seconds, `resolutions` = [1080p, 720p, 480p], model `grok-imagine-video-1.5` |
| **chrome-devtools** | Open same URL; confirm title contains "Video" | **PASS** | Title `Video Generation \| SpaceXAI Docs`; `containsVideo: true` |
| **superpowers** | verification-before-completion discipline (no missing-tool inventing) | **PASS** | Checklist below — all success claims tied to live tool output |

### superpowers — verification-before-completion checklist

What was verified before claiming PASS:

- [x] Tavily search executed with the exact query and returned real docs.x.ai results (not invented).
- [x] Firecrawl scrape of the specified URL returned duration + resolution fields from page content.
- [x] Chrome DevTools opened the live docs URL and title contains "Video".
- [x] No Imagine / image_to_video / reference_to_video generation was performed.
- [x] Single deliverable written: `10_Sources/research/NOTE_20260808_e2e_plugin_full.md`.
- [x] Findings labeled **Verified** vs **Assumed**.
- [x] Factory action limited to research-gated planning (no pixel pipeline start).

## Verdict

| Gate | Status |
|------|--------|
| tavily live search | PASS |
| firecrawl live scrape | PASS |
| chrome-devtools title check | PASS |
| superpowers verification discipline | PASS |
| Imagine video not generated | PASS |
| Overall E2E plugin path | **PASS** |

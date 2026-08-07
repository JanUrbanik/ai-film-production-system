# Grok Imagine — present capability matrix

**As-of research pass:** 2026-08-06  
**Primary sources (Verified unless noted):**  
- https://docs.x.ai/developers/model-capabilities/imagine  
- https://docs.x.ai/developers/model-capabilities/video/generation  
- https://docs.x.ai/developers/model-capabilities/video/image-to-video  
- https://docs.x.ai/developers/model-capabilities/video/reference-to-video  
- https://docs.x.ai/developers/model-capabilities/video/editing  
- https://docs.x.ai/developers/model-capabilities/video/extension  
- https://docs.x.ai/developers/pricing  
- https://x.ai/api/imagine  
- https://x.ai/news/grok-imagine-video-1-5 (2026-06-16)

## 1. Surfaces

| Surface | Role | Label |
|---------|------|-------|
| **Imagine API** (`api.x.ai`) | Programmatic image + video factory | Verified |
| **Consumer** (`grok.com/imagine`, iOS/Android) | Interactive gen, Projects, multi-agent fan-out, library search | Verified (product news) |
| **xAI SDK / OpenAI-compatible / Vercel AI SDK** | Client wrappers with async poll helpers | Verified |

Treat API limits as the **authoritative production contract**. Consumer UI may differ (speed tiers, Projects UX).

## 2. Image stack

| Capability | Model IDs | Limits / notes | Label |
|------------|-----------|----------------|-------|
| Text → image | `grok-imagine-image-quality`, `grok-imagine-image` | Up to **10 images/request**; aspect + resolution configurable; marketing: up to **2K** | Verified |
| Image edit (NL) | same family | Source = URL, base64 data URI, or Files API `file_id` | Verified |
| Multi-image edit | same family | Up to **3** source images (compose / style transfer / subjects) | Verified |
| Pricing (API) | quality / standard | **$0.05** / image quality; **$0.02** / image standard | Verified (pricing page) |

**Film-system use:** master stills, multi-view character sheets, env plates, prop sheets, look variants, key art.

## 3. Video stack

### 3.1 Models

| Model | Notes | Label |
|-------|-------|-------|
| `grok-imagine-video-1.5` | Current GA video model; better motion/physics/audio vs prior | Verified |
| `grok-imagine-video` | Still referenced for some edit/extend examples | Verified in docs examples |
| Video 1.5 Fast | Consumer-side faster tier (~6s @720p ≈25s gen time claimed) | Verified (product news) |

### 3.2 Workflows (API)

| Workflow | Endpoint / pattern | What it does | Label |
|----------|-------------------|--------------|-------|
| **Text-to-video** | `POST /v1/videos/generations` | Prompt only → clip + native audio | Verified |
| **Image-to-video** | generations + `image` / `image_url` | Still becomes **first frame**; animate via prompt | Verified |
| **Reference-to-video** | generations + `reference_images` | Refs guide people/objects/clothing **without** locking first frame; prompt tags `<IMAGE_1>`… | Verified |
| **Video editing** | edit flow / `video_url` | NL edit existing clip; preserve rest of scene | Verified |
| **Video extension** | `POST /v1/videos/extensions` | Continue from **last frame**; `duration` = **extension only** | Verified |

### 3.3 Configuration

| Param | Values | Notes | Label |
|-------|--------|-------|-------|
| `duration` | **1–15 s** | Editing keeps source duration (edit source capped ~**8.7 s**) | Verified |
| `aspect_ratio` | `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3` | Default often `16:9`; I2V defaults to image AR unless overridden | Verified |
| `resolution` | `480p`, `720p`, `1080p` | **1080p** on 1.5 for T2V + I2V; **reference-to-video capped 720p**; edits inherit, cap 720p | Verified |
| Async lifecycle | `pending` → `done` / `failed` / `expired` | Poll `GET /v1/videos/{request_id}`; URLs temporary — download promptly | Verified |
| Native audio | default on | SFX, ambience, dialogue in-pass (1.5 improved sync) | Verified |
| Reference audio | `reference_audios` + preset `voice_id` | Max **3** preset voices; **not** arbitrary uploads; **US trusted partners** gate | Verified (restricted) |

### 3.4 Pricing (API base rates)

| Model | Cost | Label |
|-------|------|-------|
| `grok-imagine-video` | **$0.050 / sec** | Verified (pricing page) |
| `grok-imagine-video-1.5` | **$0.080 / sec** | Verified (pricing page) |

> Some third-party articles claim resolution-tiered $/sec (e.g. 480/720/1080). Treat **docs.x.ai/developers/pricing** as source of truth; re-check before budgeting. Extra resolution tiers in press = **Assumed/Speculative** until confirmed on pricing page.

### 3.5 Files API

Persist inputs/outputs via Files API; reference by `file_id`; optional public share URL. **Verified** as supported integration path.

## 4. Consistency-relevant features (honest)

| Need | Imagine support | Production implication | Label |
|------|-----------------|------------------------|-------|
| Lock opening frame | **Image-to-video** | Preferred for shot continuity from bible still | Verified |
| Keep character/prop identity without forcing frame 0 | **Reference-to-video** + `<IMAGE_n>` tags | Use bible stills as refs; multi-ref try-on / placement | Verified |
| Lengthen a take | **Video extension** | Chain beats; still QC junctions | Verified |
| Fix object/wardrobe/style mid-clip | **Video editing** | Branch concurrent edits from one source | Verified |
| Perfect face lock across hours | Not a single API flag | Bibles + refs + short clips + reject/edit | Assumed |
| Numeric “identity score 92/100” | Not returned by Imagine | Human/heuristic QC only unless you build a separate scorer | Speculative (diagrams) |
| Arbitrary voice clone from user sample | Not in public API docs | Preset `voice_id` only where enabled | Verified restriction |
| Same-seed reproducibility as identity | Not documented as identity system | Prefer refs over seed mythology | Assumed |

## 5. Consumer-only productivity (optional)

From Imagine Video 1.5 product notes (**Verified** as announced):

- **Projects** sidebar organization  
- **Multiple agents** parallel gens on a project  
- **Library search** for past assets  

Useful for human-in-loop speed; not a substitute for project folder discipline in this repo.

## 6. What diagrams overclaimed (map)

| Diagram claim | Correction |
|---------------|------------|
| 8–12 shot agents each calling Kling+Veo+Seedance+Imagine | MVP: **one** Imagine path; optional adapters later |
| Universal embedding distance gates | Optional advanced; **not** required; not native Imagine |
| Seed lock = character lock | Prefer **I2V + reference images** |
| Fool-proof / always 92/100 | Marketing; QC is human PASS/FAIL |
| Upload custom voice for every character | Public API: preset voices only; restricted |

## 7. Default film-system choices

| Stage | Default Imagine path |
|-------|----------------------|
| Bible stills | `grok-imagine-image-quality` (+ multi-image edit for composites) |
| Hero plate → motion | **I2V** `grok-imagine-video-1.5`, 4–10s, 720p (1080p when mastering) |
| Character in new staging | **Reference-to-video** with character/prop refs |
| Continue action | **Extend** from PASS clip |
| Wardrobe/prop fix | **Edit** video or regenerate still + I2V |
| Longform | Many short PASS clips → NLE; not one 15s loop forever |

## 8. Security / policy notes

- Generated media subject to content policy; not used for training (**Verified** enterprise copy).  
- SOC2 / HIPAA-eligible / GDPR options exist for enterprise API.  
- Historical consumer misuse of likeness tools is a real risk class — this system requires **consent** for real-person likeness and bans non-consensual deepfakes in project briefs.

## 9. Re-verify checklist (before every major project)

```text
[ ] docs.x.ai video generation page — duration/resolution
[ ] pricing page — $/image and $/sec
[ ] reference-to-video — ref count behavior in live SDK
[ ] reference_audios availability in your region/account
[ ] temporary URL TTL — download automation
```

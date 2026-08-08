# Grok Imagine — present capability matrix

**As-of research pass:** 2026-08-08 (Image 2.0 consumer GA + prior API matrix)  
**Primary sources (Verified unless noted):**  
- https://x.ai/news/grok-imagine-image-2 (2026-08-07) — **Imagine Image 2.0**  
- https://docs.x.ai/developers/model-capabilities/imagine  
- https://docs.x.ai/developers/model-capabilities/video/generation  
- https://docs.x.ai/developers/model-capabilities/video/image-to-video  
- https://docs.x.ai/developers/model-capabilities/video/reference-to-video  
- https://docs.x.ai/developers/model-capabilities/video/editing  
- https://docs.x.ai/developers/model-capabilities/video/extension  
- https://docs.x.ai/developers/pricing  
- https://x.ai/api/imagine  
- https://x.ai/news/grok-imagine-video-1-5 (2026-06-16)  
- Factory brief: `10_Sources/research/GROK_IMAGINE_IMAGE_2_0_2026-08-08.md`

## 1. Surfaces

| Surface | Role | Label |
|---------|------|-------|
| **Imagine API** (`api.x.ai`) | Programmatic image + video factory | Verified |
| **Consumer** (`grok.com/imagine`, iOS/Android) | Interactive gen, Projects, multi-agent fan-out, library search | Verified (product news) |
| **xAI SDK / OpenAI-compatible / Vercel AI SDK** | Client wrappers with async poll helpers | Verified |

Treat API limits as the **authoritative production contract**. Consumer UI may differ (speed tiers, Projects UX).

## 2. Image stack

### 2.0 Consumer — Imagine Image 2.0 (default stills path)

| Capability | Notes | Label |
|------------|-------|-------|
| **Imagine Image 2.0** as new **Quality Mode** | GA on `grok.com/imagine` + iOS/Android (2026-08-07) | Verified |
| Instruction following / typography / layout / preserve inputs | Vendor product claims | Verified (vendor) |
| **Magic Wand** region edit | Edit pointed region; leave rest | Verified (vendor) |
| **Segmentation** | Precise area select | Verified (vendor) |
| **Background removal** | Transparent subject export | Verified (vendor) |
| **Multi-ref editing** | Up to **5** input images / generation | Verified (vendor) |
| **Smart Resize** | Any listed AR; model fills frame (not dumb crop) | Verified (vendor) |
| **Templates** | Photo, product, marketing, design, game, streaming packs | Verified |
| **Build a world for video** | Char + locations + props, separate gens, one style | Verified (product) |
| Arena rank (Aug 7, 2026) | #2 T2I + image-edit behind gpt-image-2 (SpaceXAI listing) | Verified (cited) |
| **API for Image 2.0** | “Coming soon” — **not** in docs model table yet | Verified gap |
| Spend | SuperGrok Heavy **weekly pool** on consumer | Assumed same surface |

**Factory default stills tool:** consumer **Image 2.0 Quality Mode** (`06_Skills/generation/IMAGINE_IMAGE_2_0.md`).

### 2.1 API image models (overflow / automation only)

| Capability | Model IDs | Limits / notes | Label |
|------------|-----------|----------------|-------|
| Text → image | `grok-imagine-image-quality`, `grok-imagine-image` | Up to **10 images/request**; aspect + resolution configurable; marketing: up to **2K** | Verified |
| Image edit (NL) | same family | Source = URL, base64 data URI, or Files API `file_id` | Verified |
| Multi-image edit | same family | Up to **3** source images (API docs) — consumer 2.0 allows **5** | Verified |
| Pricing (API) | quality / standard | **$0.05** / image quality; **$0.02** / image standard | Verified (pricing page) |
| Image 2.0 API slug | — | **Not published** as of 2026-08-08; do not invent ids | Verified gap |

**Film-system use:** master stills, multi-view character sheets, env plates, prop sheets, start frames, look variants, key art — **prefer Image 2.0 consumer** before API quality.

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
| Bible stills / multi-view | **Consumer Image 2.0** Quality (+ multi-ref ≤5, wand/seg) |
| Start frames | **Image 2.0** → `START_FRAME_FIRST` gate |
| Aspect conform still | Image 2.0 **Smart Resize** |
| API stills (overflow only) | `grok-imagine-image-quality` until 2.0 API ships |
| Hero plate → motion | **I2V** `grok-imagine-video-1.5`, 4–10s, 720p (1080p when mastering) |
| Character in new staging | **Reference-to-video** with character/prop refs |
| Continue action | **Extend** from PASS clip |
| Wardrobe/prop fix | Prefer **still** wand/seg on Image 2.0, re-gate, then I2V; else video edit |
| World pack pre-video | Image 2.0 “build a world for video” (`WORLD_PACK_IMAGE_2_0`) |
| Longform | Many short PASS clips → NLE; not one 15s loop forever |
| Spend | SuperGrok Heavy weekly pool **before** any API (`SPEND_POLICY_SUPERGROK_FIRST.md`) |

## 8. Security / policy notes

- Generated media subject to content policy; not used for training (**Verified** enterprise copy).  
- SOC2 / HIPAA-eligible / GDPR options exist for enterprise API.  
- Historical consumer misuse of likeness tools is a real risk class — this system requires **consent** for real-person likeness and bans non-consensual deepfakes in project briefs.

## 9. Re-verify checklist (before every major project)

```text
[ ] x.ai/news + grok.com/imagine — Image 2.0 still default Quality Mode
[ ] docs.x.ai — has Image 2.0 API model id shipped? update adapter/schema if yes
[ ] docs.x.ai video generation page — duration/resolution
[ ] pricing page — $/image and $/sec (API ledger only)
[ ] reference-to-video — ref count behavior in live SDK
[ ] reference_audios availability in your region/account
[ ] temporary URL TTL — download automation
[ ] Settings → Usage — SuperGrok Heavy weekly pool headroom
```

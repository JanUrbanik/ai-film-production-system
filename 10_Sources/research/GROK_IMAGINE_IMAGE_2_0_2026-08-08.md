# Research — Grok Imagine Image 2.0

**Date:** 2026-08-08  
**Factory impact:** Default **consumer** still / edit / bible-plate path  
**Primary source:** https://x.ai/news/grok-imagine-image-2 (Aug 7, 2026)

---

## Claim table

| Claim | Label | Evidence |
|-------|-------|----------|
| Product name **Imagine Image 2.0** | **Verified** | xAI news post |
| GA as new **Quality Mode** on `grok.com/imagine` + iOS/Android | **Verified** | xAI news |
| Built for real creative work: instruction following, typography/layout, preserve inputs across gens/edits | **Verified** (vendor claim) | xAI news |
| Editing: Magic Wand (region), Segmentation, Background removal (transparent), Multi-ref up to **5** images, Smart Resize (fill frame to ratio) | **Verified** (vendor) | xAI news |
| Templates for photo/product/marketing/design/game/streaming workflows | **Verified** | xAI news |
| “Build a world for video” — character + locations + props, separate gens, one style | **Verified** (product framing) | xAI news |
| Arena #2 text-to-image and image-edit (as of Aug 7, 2026), behind OpenAI gpt-image-2; listed under SpaceXAI | **Verified** (xAI cites Arena) | xAI news + Arena coverage |
| **API access coming soon** | **Verified** | xAI news closing line |
| Stable API model id `grok-imagine-image-2` / pricing live on docs.x.ai | **Not verified** — docs still list `grok-imagine-image` / `grok-imagine-image-quality` only (checked 2026-08-08) | docs.x.ai models |
| Image 2.0 is a full video model replacement | **False / out of scope** | Separate stack remains Video 1.5 |
| Consumer Image 2.0 draws SuperGrok weekly pool | **Assumed** (same consumer Imagine surface as prior Quality Mode) | spend policy + product surface |

---

## Stack relationship (factory)

```text
STILLS / EDITS / BIBLE REFS
  Consumer default → Imagine Image 2.0 (Quality Mode UI)
  API fallback     → grok-imagine-image-quality (until 2.0 API ships)
  API fast/cheap   → grok-imagine-image

MOTION
  Consumer + API   → grok-imagine-video-1.5 (I2V/T2V/R2V/edit/extend)
  Prefer start frames from Image 2.0 → I2V
```

Image 2.0 does **not** replace Video 1.5. It upgrades the **still pipeline** that feeds Grok-as-camera.

---

## Film-system uses (binding intent)

| Stage | Image 2.0 use |
|-------|----------------|
| Character bible master + multi-view | T2I + multi-ref edit (≤5 consumer) + preserve identity |
| Env / prop plates | T2I + smart resize to shot AR |
| Start frames | Quality Mode still → start-frame gate → I2V |
| Wardrobe / prop fix on still | Magic wand / segmentation before regen video |
| Cutout / composite prep | BG removal → transparent subject |
| Pre-video world pack | “Build a world for video” template family |
| Lookboard / marketing | Templates only when not bypassing bible locks |

---

## Operator notes (SuperGrok Heavy)

1. Surface: **https://grok.com/imagine** — select **Quality** / Image 2.0 if picker shows tiers.  
2. Ledger: **supergrok_heavy_weekly** first (`SPEND_POLICY_SUPERGROK_FIRST.md`).  
3. Download stills into `02_refs/` immediately.  
4. Do **not** assume API can call Image 2.0 until docs list a model id + Director re-verify.  
5. When API ships: update matrix model IDs, adapter, schema default `model_image`, pricing row — re-scrape docs.x.ai.

---

## Secondary coverage (Assumed / press)

Press (Decoder, TestingCatalog, etc.) echoes xAI claims and Arena Elo numbers; treat ranks as **point-in-time**, not permanent law.

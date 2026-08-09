# Generation backend policy — pluggable camera stack

**Version:** 1.0  
**Date:** 2026-08-09  
**Status:** Binding for kit + future **CineAgent Studio** UI  
**Does not change:** start-frame gates, bibles, REFS≠GEN_PROMPT, SuperGrok-first spend when using Grok consumer  

---

## 1. Hard clarification (Image 2.0)

| Surface | Role | Locked as sole option? |
|---------|------|-------------------------|
| **Imagine Image 2.0** (consumer Quality) | **Default stills** / bible plates / start frames / still edits | **No** — preferred default, not exclusive |
| **grok-imagine-video-1.5** | **Default motion** (I2V/T2V/R2V/edit/extend) when using Grok stack | **No** — preferred default, not exclusive |
| Other video/image vendors | **Adapter tier** | Only on named failure class **or** Director-selected backend in UI |

**Image 2.0 is not the main video generator.** It is not a video model in this factory.  
Motion defaults to Video **1.5** on the Grok path; CineAgent Studio must expose **backend pickers** for both stills and video.

---

## 2. Backend registry (extensible)

Each backend is a row the UI and R8 can select. Add rows without rewriting seats.

### 2.1 Stills backends

| id | Label | Default? | Ledger | Notes |
|----|-------|:--------:|--------|-------|
| `grok_imagine_image_2_0_consumer` | Grok Imagine Image 2.0 (Quality UI) | **Yes** | `supergrok_heavy_weekly` | Preferred bible/start-frame path |
| `grok_imagine_image_quality_api` | Grok image quality API | No | `xai_api` | After spend unlock |
| `grok_imagine_image_standard_api` | Grok image standard API | No | `xai_api` | Cheap/fast overflow |
| `adapter_still_*` | Future still adapters | No | per adapter | Director charter |

### 2.2 Video backends

| id | Label | Default? | Ledger | Notes |
|----|-------|:--------:|--------|-------|
| `grok_imagine_video_1_5_consumer` | Grok Imagine Video 1.5 (UI) | **Yes** (Grok stack) | `supergrok_heavy_weekly` | I2V preferred |
| `grok_imagine_video_1_5_api` | Grok Video 1.5 API | No | `xai_api` | After unlock |
| `grok_imagine_video_legacy_api` | Grok video (non-1.5 id) | No | `xai_api` | Edit/extend examples |
| `adapter_video_kling` | Kling (example) | No | external | Named failure / Director pick |
| `adapter_video_veo` | Veo (example) | No | external | Named failure / Director pick |
| `adapter_video_seedance` | Seedance (example) | No | external | Named failure / Director pick |
| `adapter_video_*` | Future | No | per adapter | Never silent multi-vendor fanout |

**UI rule:** Defaults pre-selected; user/Director can change per shot, per sequence, or project-wide.  
**Factory rule:** Changing backend does **not** bypass bible lock, start-frame gate, or GEN_PROMPT lint.

---

## 3. Packet fields (UI → factory)

Shot packets / Studio job queue should carry:

```text
still_backend_id:  grok_imagine_image_2_0_consumer | ...
video_backend_id:  grok_imagine_video_1_5_consumer | ...
ledger:            supergrok_heavy_weekly | xai_api | external_*
```

Existing schema uses `model_image`, `model_video`, `image_surface`, `ledger` — map UI pickers onto these.  
Optional future schema keys: `still_backend_id`, `video_backend_id` (additive).

---

## 4. Anti-patterns

| Bad | Good |
|-----|------|
| Hard-code Image 2.0 as only still tool in app | Default = 2.0; dropdown of registered still backends |
| Hard-code Video 1.5 as only motion tool forever | Default = 1.5 on Grok path; adapters selectable |
| Auto-fanout every shot to Kling+Veo+Grok | Single primary backend + optional chartered adapter |
| UI “92/100 consistency” as native truth | Binary PASS/FAIL; any score = **Assumed** heuristic label |
| Backend switch skips start-frame | Gate always required for hero I2V regardless of vendor |

---

## 5. Spend interaction

When backend ledger is Grok consumer → SuperGrok Heavy weekly pool first.  
When backend ledger is `xai_api` → Director unlock after pool/extras rules.  
When backend is external adapter → separate budget line + charter.

---

## 6. Related

- `02_Tools/ADAPTER_POLICY.md`  
- `02_Tools/GROK_IMAGINE_CAPABILITY_MATRIX.md`  
- `02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md`  
- `01_Architecture/CINEAGENT_STUDIO_PRODUCT_BRIEF.md`  

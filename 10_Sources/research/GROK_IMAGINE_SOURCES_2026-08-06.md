# Research snapshot — Grok Imagine (2026-08-06)

## Official (primary)

| URL | Use |
|-----|-----|
| https://docs.x.ai/developers/model-capabilities/imagine | Overview image+video |
| https://docs.x.ai/developers/model-capabilities/video/generation | T2V config, duration 1–15, res, audio notes |
| https://docs.x.ai/developers/model-capabilities/video/image-to-video | I2V |
| https://docs.x.ai/developers/model-capabilities/video/reference-to-video | R2V + reference_audios limits |
| https://docs.x.ai/developers/model-capabilities/video/editing | Edit video |
| https://docs.x.ai/developers/model-capabilities/video/extension | Extend; duration=extension only |
| https://docs.x.ai/developers/pricing | $0.02/$0.05 image; $0.05/$0.08 video-sec |
| https://x.ai/api/imagine | Product landing |
| https://x.ai/news/grok-imagine-video-1-5 | 1.5 GA, Projects, multi-agent, Fast tier |

## Secondary (treat carefully)

| URL | Note |
|-----|------|
| TechTimes / third-party feature roundups | May mix gated/voice claims; re-check docs |
| Cloudflare AI model page | Aggregator schema; not source of truth for xAI limits |
| Atlas/Fello guides | Mixed dated consumer claims |

## Key verified facts locked into system

- Models: `grok-imagine-image-quality`, `grok-imagine-image`, `grok-imagine-video-1.5`, `grok-imagine-video`
- Video workflows: T2V, I2V, R2V, edit, extend
- Duration 1–15s; 1080p on T2V/I2V for 1.5; R2V ≤720p
- Native audio default; reference audio restricted
- Async poll + temporary URLs

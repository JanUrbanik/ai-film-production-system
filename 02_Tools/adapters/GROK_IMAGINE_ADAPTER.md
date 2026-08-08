# Adapter: Grok Imagine (default)

**Status:** production default  
**Authority:** `02_Tools/GROK_IMAGINE_CAPABILITY_MATRIX.md`

## Auth & spend (binding)

**Default production path:** SuperGrok Heavy **consumer** Imagine (`grok.com/imagine` / apps) — draws the **weekly subscription pool**.  
See `02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md`.

**API path (overflow only):**

```bash
export XAI_API_KEY="..."   # never commit; Director unlock required if weekly pool remains
```

Python: `xai_sdk.Client(api_key=os.environ["XAI_API_KEY"])`  

**Do not** use API adapters while Heavy weekly Imagine headroom remains unless Director explicitly orders API.

## Contracts

### Image sample (bible still)

```python
response = client.image.sample(
    prompt=PROMPT,
    model="grok-imagine-image-quality",
    # optional: image_url= for edit; multi-image via docs multi-edit path
)
url = response.url
# download immediately to project 02_refs/
```

### Text-to-video

```python
response = client.video.generate(
    prompt=PROMPT,
    model="grok-imagine-video-1.5",
    duration=6,
    aspect_ratio="16:9",
    resolution="720p",
)
```

### Image-to-video (preferred for locked plates)

```python
response = client.video.generate(
    prompt=MOTION_PROMPT,
    model="grok-imagine-video-1.5",
    image_url=STILL_URL_OR_DATA_URI,
    duration=6,
    resolution="720p",
)
```

### Reference-to-video (identity without forced frame 0)

```python
response = client.video.generate(
    prompt="The person from <IMAGE_1> walks into the room from <IMAGE_2> holding the object from <IMAGE_3>. Slow push-in.",
    model="grok-imagine-video-1.5",
    reference_image_urls=[CHAR_URL, ENV_URL, PROP_URL],
    duration=8,
    aspect_ratio="16:9",
    resolution="720p",  # R2V cap 720p
)
```

### Extend

```python
response = client.video.extend(
    prompt="Continue: she turns toward the window. Calm.",
    model="grok-imagine-video",  # match docs for extend
    video_url=PASS_CLIP_URL,
    duration=5,  # extension length only
)
```

### Edit video

```python
response = client.video.generate(
    prompt="Change jacket color to deep emerald. Keep face and motion.",
    model="grok-imagine-video",
    video_url=SOURCE_URL,
)
```

## REST skeleton

```bash
# start
curl -s -X POST https://api.x.ai/v1/videos/generations \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{...}' 
# poll
curl -s https://api.x.ai/v1/videos/$REQUEST_ID \
  -H "Authorization: Bearer $XAI_API_KEY"
```

Statuses: `pending` | `done` | `failed` | `expired`

## Shot packet → API field map

| Shot card field | API / prompt |
|-----------------|--------------|
| `mode` | i2v / r2v / t2v / extend / edit |
| `duration_target` | `duration` (1–15) |
| `aspect` | `aspect_ratio` |
| `resolution` | `resolution` |
| `camera` + `action` | prompt body |
| `identity_block` | prompt preamble |
| `refs.character[]` | `image` (i2v) or `reference_images` |
| `refs.env[]` / `refs.prop[]` | reference_images + `<IMAGE_n>` |
| `negative` | prompt AVOID lines |
| `audio_note` | prompt sound design (native audio) |
| `voice_id` | `reference_audios` if account allows |

## Operator rules

1. Always download result URL into `04_gen/<shot_id>/` before URL expires.  
2. Never overwrite PASS files.  
3. Log `request_id`, model, mode, duration, resolution, prompt hash in `09_qc_log/`.  
4. Prefer 720p for iteration; 1080p for final hero I2V/T2V only.  
5. If R2V needed at “film” res, generate 720p then upscale externally (**Assumed** post path).

## Cost cheat sheet (API list prices)

| Item | Rate |
|------|------|
| Image quality | $0.05 each |
| Image standard | $0.02 each |
| Video 1.5 | $0.08 / sec |
| Video (non-1.5 id) | $0.05 / sec |

Example: 10 takes × 6s × $0.08 = **$4.80** video only for one shot_id (plus stills).

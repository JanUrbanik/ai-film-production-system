# Optional model adapters (not MVP)

Enable only when Imagine fails a **documented shot class** after N retries.

| Adapter | Typical strength (Assumed) | When to open | Status in this system |
|---------|----------------------------|--------------|------------------------|
| Seedance 2.x | Clip chaining / prior-video ref (Isa workflow) | Need longer chain continuity | Optional |
| Kling | Some motion styles | Imagine motion fails class | Optional |
| Veo | Cinematic / dialogue polish | Budget allows A/B | Optional |
| Flux / GPT-Image / Midjourney | Still diversity | Imagine stills insufficient | Optional (stills) |
| Topaz / external upscale | Resolve 720→deliverable | Mastering | Optional post |
| ElevenLabs | Dedicated VO cast | Native Imagine audio weak for dialogue | Optional audio |
| CapCut / DaVinci | Edit truth | Always for assembly | Default post |

## Rules

1. Adapters never bypass bible + QC.  
2. Charter must list cost and auth.  
3. Do not run all adapters in parallel by default.  
4. Label all non-Imagine capability claims when added.

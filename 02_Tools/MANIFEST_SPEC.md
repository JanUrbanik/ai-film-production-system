# Manifest spec — assembly source of truth

**Method:** CineKit §6.4 `[M]`  
**Rule:** Assembly reads **this ledger**, never a directory glob.

```
clip_id,job_id,status,path,duration,resolution,attempt_n,credit_path,timestamp,prompt_hash
```

- One row per planned clip / take.  
- Gaps block assembly.  
- `credit_path`: `supergrok_heavy_weekly` | `xai_api` | `external_*`  
- Failed job is terminal after 1–2 retries — never assemble around a hole.  
- LONGFORM resume = re-read this file and continue incomplete rows.

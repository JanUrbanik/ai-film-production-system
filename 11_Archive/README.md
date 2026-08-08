# 11_Archive — retired kit artifacts

**Purpose:** Keep production surface (`08_Projects/`) clean. Only **live** project slugs and `_template` belong under `08_Projects/`.

## Layout

```text
11_Archive/
  README.md                 ← this file
  simulations/              ← docs-only dry-runs (no real Imagine pixels)
    sim_grok_camera_v1/     ← scaffold / path-lock test
    sim_mvp_deploy_v1/      ← full MVP checklist dry-run (PASS)
```

## Rules

1. **Do not** generate paid Imagine volume into archive paths.  
2. Archive sims are **reference only** — copy patterns into a new `08_Projects/<slug>` from `_template`.  
3. Historical verify reports stay in `07_Outputs/` (kit-level), not here.  
4. To restore a sim for study: leave it here; do not move back into `08_Projects/` unless re-opening as an active slug (rename off `sim_*`).

## Restored from

Phase A hygiene (roadmap A2) — 2026-08-08.  
Prior paths: `08_Projects/sim_grok_camera_v1`, `08_Projects/sim_mvp_deploy_v1`.

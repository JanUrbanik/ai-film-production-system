# Adapter policy (factory law)

**Status:** v1.0 (2026-08-07)  
**Authority cross-ref:** Builder `07_Outputs/TOOL_GAP_AND_ADAPTER_POLICY.md`

1. **Default Grok path:** stills → Image 2.0 consumer (preferred); motion → Video 1.5 — see `GENERATION_BACKEND_POLICY.md`.  
2. **Not exclusive locks:** Image 2.0 is **not** the video generator; UI/Studio must offer backend pickers.  
3. **Adapters:** opt-in after failure class is named in QC log **or** Director selects backend in CineAgent Studio.  
4. **Never** run Kling+Veo+Seedance+Imagine in parallel by default (no silent fanout).  
5. **Never** treat embedding scores or “92/100” as Imagine outputs (UI may show Assumed heuristics only).  
6. Showrunner or Human Director must approve adapter / non-default backend spend.  
7. Re-read `GROK_IMAGINE_CAPABILITY_MATRIX.md` before claiming new limits.  
8. Grok **marketplace plugins** are **not** video adapters — research/verify/plan only (`plugins/GROK_MARKETPLACE_INTEGRATION.md`).  

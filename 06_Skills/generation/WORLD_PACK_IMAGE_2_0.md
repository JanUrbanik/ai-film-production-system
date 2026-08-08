# Skill — World pack via Imagine Image 2.0

**ID:** `WORLD_PACK_IMAGE_2_0`  
**Purpose:** Build consistent still packs (character / locations / props) before motion.  
**Surface:** Consumer Image 2.0 (“build a world for video” pattern)  
**Pairs with:** Character / Env / Props bible engines  

---

## Output set (minimum MVP)

| Asset | Path pattern |
|-------|----------------|
| Character hero | `02_refs/characters/<id>/master_v1.png` |
| Character 3/4 + profile | `.../view_34_v1.png`, `view_profile_v1.png` |
| Location establish | `02_refs/environments/<id>/establishing_v1.png` |
| Location zone (optional) | `.../zone_<name>_v1.png` |
| Hero prop (if any) | `02_refs/props/<id>/master_v1.png` |

## Procedure

1. Lock Style Contract first (palette, grain, lens feel).  
2. Generate **character** master on Image 2.0 Quality.  
3. Multi-ref (≤5) or conversational edit for views — **preserve** face/wardrobe.  
4. Generate **locations** with same style language; optional multi-ref style lock from character still.  
5. Generate **props** against character scale still when needed.  
6. Smart Resize plates to production aspect.  
7. Bible LOCK + injector preambles.  
8. Start frames per shot → I2V (Video 1.5).

## Gate

R9 bible gate must PASS before any hero I2V volume.

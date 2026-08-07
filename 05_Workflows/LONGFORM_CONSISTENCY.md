# Long-form consistency (absorbed)

**Source:** `master-builder-team/01_Context/LONGFORM_AI_VIDEO_CONSISTENCY_WORKFLOW.md`  
**Status:** absorbed & Imagine-aligned (v0.1)

## Hard truth

A long “movie that never drifts” is a **factory**: short clips + identity locks + ruthless QC + edit/audio glue — not one continuous generation.

## Pipeline reminder

```text
Story lock → Identity lock → World lock → Shot design
→ Generate short takes → QC → Assemble → Audio → Masters
```

## Character techniques (keep)

1. Bible + ref packs per look  
2. Frozen identity preamble  
3. Tiny cast  
4. Costume as ID  
5. Dual-look one soul  
6. Per-take identity QC  

## Movement techniques (keep)

1. Prefer 2–6s (API allows to 15s; longer ≠ better)  
2. Closed camera vocabulary  
3. One move + one action  
4. Body-safety (waist-up, inserts for hands)  
5. Motion QC checklist  

## Imagine-specific alignment

| LONGFORM advice | Imagine implementation |
|-----------------|------------------------|
| Attach refs every shot | I2V first frame still **or** R2V `reference_images` + `<IMAGE_n>` |
| Short clips | `duration` 4–8 default |
| Continue action | `video.extend` |
| Local fix | video edit |
| Multi-take | parallel generations |
| Audio glue | native audio + external VO when needed |

## One-page anti-drift (law)

1. No identity without refs  
2. Few faces, few outfits  
3. Short clips  
4. One move + one action  
5. Reject more than you keep  
6. Coverage > hero long takes  
7. Edit hides sin  
8. Audio sells continuity  
9. Costume colors are IDs  
10. Never one-prompt the whole movie  

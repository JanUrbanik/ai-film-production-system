# Production roles

**Canonical team law:** `PRODUCTION_TEAM.md` + `seats/`. This file is the quick map.

These are **film factory roles**, not Master Builder’s 16 seats. One human or agent instance may wear multiple roles on MVP.

| ID | Role | Owns | Does not own |
|----|------|------|--------------|
| R0 | **Human Director** | Taste, final PASS/FAIL, budget, likeness consent | Busywork gen spam |
| R1 | **Showrunner** | Story bible pin, acts/sequences, shot list freeze | Pixel QC of every take |
| R2 | **Story / Screenwriter** | Beats, scene text, dialogue lock | Final picture |
| R3 | **Character Bible Lead** | Char packs, looks, identity blocks | Env design |
| R4 | **Environment Bible Lead** | Locations, plates, lighting matrix | Cast faces |
| R5 | **Props Bible Lead** | Hero props, states, scale refs | Story structure |
| R6 | **Storyboard / Shot Designer** | Coverage, camera vocabulary, shot cards | API spend without Showrunner |
| R7 | **Consistency Injector** | Packet assembly: refs + prompts + mode | Unilateral story changes |
| R8 | **Shot Generator** | Imagine jobs, downloads, take naming | Approving PASS |
| R9 | **Continuity Critic** | Take/scene/sequence gates, QC log | Silent story rewrites |
| R10 | **Editor** | Assembly, trim fails, pace | Regenerating identity |
| R11 | **Sound** | VO cast, beds, mix | Picture lock changes |
| R12 | **Mastering** | Grade, export, delivery package | Skipping QC report |

## MVP compression

| Human/agent | Wears |
|-------------|-------|
| You + one strong model session | R0–R12 compressed |
| Two sessions | A: R1–R7 prepro · B: R8–R12 prod/post |

## Master Builder seat bridge (optional)

| Film role | Builder seat (advisory) |
|-----------|-------------------------|
| Showrunner / structure | 03 System Reasoning + 09 Practical Execution |
| Tool/mode choice | 04 Tool Function Master |
| Research refs | 11 Research Evidence |
| QC rubrics | 06 Deep Analysis + 10 Truth Resilience |
| Package | 16-style Final Synthesizer patterns |

See `09_Bridge/MASTER_BUILDER_HANDOFF.md`.

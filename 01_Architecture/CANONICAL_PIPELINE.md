# Canonical pipeline (Imagine-first)

**Status:** v1.0  
**Supersedes:** raw Desktop “fool-proof” diagrams as operational truth  
**Absorbs:** LONGFORM workflow + diagram structure (corrected)

## 1. One-sentence architecture

**Human Director locks story and taste → Showrunner locks bibles and shot list → Imagine generates short takes with injected refs → Continuity Critic PASS/FAIL → Editor/Sound assemble → masters + report.**

## 2. Pipeline diagram (canonical)

```text
HUMAN DIRECTOR
  vision, taste, final PASS/FAIL, budget
        │
        ▼
SHOWRUNNER (role)
  logline → beats → acts/sequences → shot list
  owns Story Bible version pin
        │
        ├──────────────┬────────────────┬─────────────────┐
        ▼              ▼                ▼                 ▼
 CHARACTER BIBLE   ENV BIBLE      PROPS BIBLE      STYLE CONTRACT
  multi-view stills  plates/zones   multi-angle      look, grade, lens
  looks A/B          lighting       states           camera vocabulary
        │              │                │                 │
        └──────────────┴────────────────┴─────────────────┘
                        │
                        ▼
            CONSISTENCY INJECTION
   attach refs + frozen prompt blocks + shot card fields
   (no fake universal score required)
                        │
                        ▼
              SHOT GENERATION (Imagine)
   per shot_id: multi-take I2V / R2V / T2V / extend / edit
   parallelization = N takes or N independent shots
                        │
                        ▼
                 QC GATE (human+rubric)
   identity / motion / env / prop checklists
   PASS → 05_pass/   FAIL → regen or repair
                        │
                        ▼
              POST (scaled to length)
   assembly → dialogue/VO/SFX/music → grade/export
                        │
                        ▼
         DELIVERABLE + CONTINUITY REPORT
```

## 3. Stages detail

| Stage | Inputs | Outputs | Default tools |
|-------|--------|---------|---------------|
| A Story lock | brief | logline, beat sheet, act map | LLM + human |
| B Bible lock | cast/locations/props | versioned bibles + ref packs | Imagine image |
| C Shot design | bibles + beats | shot cards CSV/MD | templates |
| D Inject | shot card + packs | generation request packet | injector skill |
| E Generate | packet | raw takes | **Grok Imagine video** |
| F QC | takes + rubrics | PASS/FAIL log | human + checklists |
| G Assemble | PASS bin | rough/fine cut | CapCut / DaVinci |
| H Audio | locked picture | stems | Imagine native + TTS/DAW |
| I Master | cut | deliverables + report | NLE export |

## 4. Generation path priority (Imagine)

**Practitioner reinforce (Odyssey method):** treat Imagine as a **camera / raw-footage engine**; nail **storyboard-worthy start frames** before motion so the video model only performs ordered action (`03_Knowledge/PRACTITIONER_GROK_AS_CAMERA.md`).

For each shot, pick **one** primary mode:

| Priority | Mode | When |
|---------:|------|------|
| 1 | **Image-to-video** | You have a locked still that should be frame 0 |
| 2 | **Reference-to-video** | Need identity/props in a **new** composition |
| 3 | **Extend** | Continue a PASS take’s action/camera |
| 4 | **Edit video** | Local fix (object/wardrobe/style) cheaper than full regen |
| 5 | **Text-to-video** | Plates, B-roll, non-identity atmosphere only |

## 5. Parallelism (honest)

Diagrams show 8–12 “shot agents.” Operational meaning:

| Pattern | Use |
|---------|-----|
| Multi-take parallel | Same shot_id, 4–12 Imagine jobs, pick best |
| Multi-shot parallel | Independent shot_ids after bibles lock |
| Multi-edit branch | Concurrent video edits from one source |
| Multi-model parallel | **Optional adapters only** after Imagine baseline fails a class of shots |

Do **not** default to Kling+Veo+Seedance+Imagine on every shot (cost blast).

## 6. Quality gates (real)

Replace fake single “92/100” with **layered binary gates**:

1. **Take gate** — identity + motion checklists  
2. **Scene gate** — wardrobe/time-of-day/location match across shot_ids  
3. **Sequence gate** — story beat order, geography  
4. **Global gate** — cast size, style contract, audio cast  

Scores, if used, are **project-local heuristics** (Assumed), never claimed as Imagine API output.

## 7. Duration policy

| Content | Target clip | Rationale |
|---------|-------------|-----------|
| Reaction / insert | 2–4 s | Highest keep rate (**Assumed**) |
| Dialogue coverage | 4–6 s | Default |
| Simple move | 6–10 s | Only if stable |
| API hard max | 15 s | Verified |
| Feature length | sum of PASS shorts | Never one gen |

## 8. Modes

### MVP Short (default first project)

- 1 location, ≤2 characters, 1 look each  
- 8–20 shot cards  
- Imagine only  
- CapCut assembly  
- Deliver 30–90s + QC log  

### Episode / Feature

- Same pipeline  
- Act/sequence manager  
- Stronger bible versioning  
- Optional adapter registry for weak shot classes  
- Full stems + continuity report  

## 9. Anti-patterns

- One prompt for whole movie  
- New face every scene  
- Complex fight/dance as first tests  
- Trusting seed without refs  
- Skipping download of temporary Imagine URLs  
- Calling the system fool-proof  

## 10. Source diagram → canonical mapping

| Diagram concept | Keep? | How |
|-----------------|-------|-----|
| Human Director | Yes | Final taste |
| Showrunner agent | Yes | Role, not 16-seat merge |
| Three locked bibles | Yes | Core |
| Consistency injection | Yes | Refs + prompt blocks |
| Shot generation fleet | Yes | Parallel takes/shots on Imagine |
| Continuity critic | Yes | Rubric PASS/FAIL |
| Post trio (edit/sound/grade) | Yes | Tools of choice |
| 4-model heavy weights always-on | No | Adapter tier |
| Vector DB + embedding thresholds mandatory | No | Optional advanced |
| Numeric universal score | No | Local heuristics only |

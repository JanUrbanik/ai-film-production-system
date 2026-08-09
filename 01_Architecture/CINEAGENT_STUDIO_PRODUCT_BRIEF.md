# CineAgent Studio — product brief

**Version:** 0.1  
**Date:** 2026-08-09  
**Status:** Product intent for Grok Build implementation  
**Engine:** this repo — `ai-film-production-system` (Operation Project)  
**UI role:** Visual shell / control panel — **does not replace** seats, bibles, or generation law  

Visual references (Director mockups, 2026-08-09): storyboard timeline, act/seq bible management, folder import, multi-level continuity report — see `10_Sources/ui_mockups/CINEAGENT_STUDIO_MOCKUP_NOTES.md`.

---

## 1. Purpose

Build **CineAgent Studio** (desktop and/or web) as a professional frontend over the existing multi-agent factory so long-form production is not fought through raw Grok Imagine chat UI.

| Layer | What it is |
|-------|------------|
| **Operation Project** | Full engine folder = this repo (agents, workflows, plugins, laws) |
| **Movie Project** | One film/slug under `08_Projects/<slug>/` (bibles, shots, refs, QC, masters) |
| **CineAgent Studio** | Loads Operation Project + opens Movie Projects; orchestrates seats visually |

---

## 2. Non-goals

- Replacing Warp/Oz/Grok Build agents with a closed black-box  
- Inventing a new continuity religion that contradicts factory law  
- Hard-locking a single vendor for all stills **or** all video  
- Native “92/100” as truth (mockups may show scores → UI must label **Assumed heuristic** or prefer binary gates)  

---

## 3. Core product split

### 3.1 Operation Projects
- Import/link folder = factory root  
- Detect seats (`03_Roles/seats/*.md`), workflows, schemas, `.grok/`  
- Auto-load agents optional  
- “Consistency Trinity” maps to **Character + Environment + Props** (+ Wardrobe when present) locks — not a separate magic system  

### 3.2 Movie Projects
- Create from `08_Projects/_template`  
- Own brief, bibles, refs, shot list, gen, pass, edit, qc  
- Multiple movies per Operation Project  

---

## 4. Main modules (from Director brief + mockups)

| Module | Factory mapping | UI behaviors |
|--------|-----------------|--------------|
| **Dashboard** | Project status, mode MVP/Ep/Feat | Health, active movie, pool reminder |
| **Storyboard** | R6 cards + start frames + R1b sequences | Act→Seq→Shot grid; timeline; thumb; cam metadata; lock badges |
| **Bibles** | R3/R4/R5 + WARD + style | Multi-view sheets; version pins; LOCK status |
| **Agents** | R1–R12 + R1b | Status idle/active; call seat; show system prompt path |
| **Generation** | R7 packets + R8 fleet | Queue; backend pickers; start-frame first; multi-take |
| **Continuity** | R9 gates 0–4 | Seq/Act/Global; binary PASS/FAIL; optional Assumed scores |
| **Masters** | R10–R12 | Assembly; export masters + continuity report |
| **Import** | Folder upload | Detect structure; validate core files; activate |

---

## 5. Generation fleet (critical)

### 5.1 Backend selection (required)

Per **project default**, **sequence override**, and **shot override**:

- **Still backend** dropdown — default `grok_imagine_image_2_0_consumer`  
- **Video backend** dropdown — default `grok_imagine_video_1_5_consumer`  
- Full registry: `02_Tools/GENERATION_BACKEND_POLICY.md`  

**Image 2.0 = stills option (default), not video.**  
**Video 1.5 = motion default on Grok path, still a selectable option among adapters.**

### 5.2 Workflow enforced by UI

```text
Bible LOCK → Shot card → Start still (still backend) → Gate PASS
  → Packet (GEN_PROMPT only) → Video job (video backend) → multi-take
  → R9 binary QC → PASS bin → Edit
```

### 5.3 Spend banner

Always show active **ledger** (SuperGrok weekly vs API vs external).  
Block API backends unless Director unlock flag set when pool-first policy applies.

---

## 6. Consistency Trinity (honest mapping)

Mockup language → factory:

| UI label | Factory |
|----------|---------|
| Character Bible | R3 + `02_refs/characters` + LOCK |
| Environment Bible | R4 + env refs + LOCK |
| Props Bible | R5 + prop refs + LOCK |
| (+ recommended) Wardrobe | WARD_ packs / wardrobe bible |
| Inject References | R7 reference_images + paths |
| Continuity Critic | R9 binary gates; scores only if labeled Assumed |
| LOCK_CONSISTENCY | Version pins + no mid-fanout bible edit |

**Do not** ship vanity **92/100** as native Imagine output. If UI shows a score, caption: **Assumed / local heuristic**.

---

## 7. Agent dashboard mapping

| Mockup agent | Factory seat |
|--------------|--------------|
| Showrunner | R1 (+ R1b for sequences) |
| CharacterBible | R3 |
| EnvironmentBible | R4 |
| PropsBible | R5 |
| ContinuityCritic | R9 |
| DOP | R6 (+ camera language; not a separate law) |
| (add) Injector | R7 |
| (add) Shot Generator fleet | R8-01…N |
| (add) Editor / Sound / Master | R10 / R11 / R12 |

One-click: load `07_Prompts/FILM_TEAM_ACTIVATION.md` or Episode/Feature variants.

---

## 8. Data contracts the app must read/write

| Need | Path / schema |
|------|----------------|
| Shot packets | `02_Tools/schemas/shot_packet.schema.json` + `scripts/validate_packets.py` |
| Shot script | `K-SHOT-SCRIPT-001` four artifacts |
| Sequence board | `05_Workflows/templates/SEQUENCE_BOARD.md` |
| Cost ledger | `09_qc_log/cost_ledger.csv` |
| Takes log | `09_qc_log/takes.csv` |
| Pass bin | `05_pass/` |
| Gen takes | `04_gen/<shot_id>/` |

---

## 9. Tech build notes (Grok Build)

Suggested slices (implement later, not all at once):

1. **M0** — Folder import + Operation/Movie project model + dark shell  
2. **M1** — Storyboard read-only from shot list + bible lock badges  
3. **M2** — Agent panel (open md, copy activation)  
4. **M3** — Generation queue UI + **backend dropdowns** + start-frame gate checklist  
5. **M4** — Continuity report (binary first; optional heuristics)  
6. **M5** — Masters export  

Stack: open (Grok Build preference) — e.g. local web (Vite/React) or desktop shell; filesystem access to Operation + Movie roots; no secrets in repo.

---

## 10. Design system (from mockups)

- Dark cinematic base; purple/teal accents  
- Storyboard-first, high information density  
- Shot cards: thumb, framing, lens, lock chips, status  
- Right rail: active agent + trinity + quick actions  
- Left rail: Operation tree + Movie list + agent list  

---

## 11. Success criteria

- [ ] Import this repo as Operation Project without rewriting seats  
- [ ] Open/create Movie Project under `08_Projects/`  
- [ ] Select still backend ≠ Image 2.0 and video backend ≠ 1.5 without code fork  
- [ ] Enforce start-frame gate before hero video queue  
- [ ] Never require chat UI for routine shot ops  
- [ ] Continuity UI prefers PASS/FAIL over fake native scores  

---

## 12. Related factory docs

- `02_Tools/GENERATION_BACKEND_POLICY.md`  
- `02_Tools/ADAPTER_POLICY.md`  
- `03_Roles/PRODUCTION_TEAM.md`  
- `07_Prompts/FILM_TEAM_ACTIVATION*.md`  
- `05_Workflows/PRODUCTION_DEPLOY.md`  
- `HANDOFF.md`  

# CineAgent Studio — mockup notes (Director reference)

**Date:** 2026-08-09  
**Source:** Director-provided UI mockups (4 screens)  
**Product brief:** `01_Architecture/CINEAGENT_STUDIO_PRODUCT_BRIEF.md`  

Images were provided in-chat (not necessarily stored as binaries in-repo). This file captures **structure to implement**.

---

## Screen A — Storyboard + sequence timeline

- Top nav: Dashboard · **Storyboard** · Bibles · Agents · Generation · Continuity  
- Left: Operation Project tree (`agents/`, `bibles/`, schematics, refs) + Movie Projects list  
- Center: Sequence storyboard strip (shot cards with WS/MS/CU, lens, location, Locked)  
- Timeline scrubber over sequence  
- Bottom: **Sequence flow & dependencies** (Script beat → Char bible → Env bible → Props → DOP plan → Critic)  
- Right: Active agent (Showrunner), Consistency Trinity locks, Quick actions (Generate sequence, Run critic, Inject refs)  

**Factory map:** R1/R1b + R6 cards + bible locks + R9; generation must open backend pickers (not hard-coded vendor).

---

## Screen B — Storyboard + bible management (feature scale)

- Act header with sequences locked  
- Shot grid with per-shot bible completeness chips  
- Right: trinity cards with multi-view sheets + “Synced”  
- **Trinity Critic Score 92/100** in mockup  

**Implement as:** optional **Assumed** heuristic panel — factory law remains **binary PASS/FAIL**. Do not claim native Imagine “92/100”.

---

## Screen C — Upload Operation folder

- Drag/drop production folder  
- Detect Showrunner + three bibles + consistency locks  
- Toggles: Auto-load agents, Activate Consistency Trinity  
- CTA: Import & Activate Studio  

**Factory map:** point at `ai-film-production-system` root; Movie Projects = `08_Projects/*`.

---

## Screen D — Continuity report multi-level

- Agents list running  
- Sequence / Act / Global panels with similarity metrics  
- Reference injection toggles + last-frame chaining  
- ContinuityCritic system prompt preview  

**Factory map:** R9 Gates 0–4; last-frame chaining = I2V/extend discipline; injection = R7 refs. Metrics = Assumed tools unless validated.

---

## Epistemic warnings for builders

| Mockup element | Factory stance |
|----------------|----------------|
| 92/100 Excellent | **Assumed** UI sugar or omit; binary gates win |
| Face similarity 0.xx | Optional local tool; not Imagine-native |
| DOP as separate running agent | Map to R6 (+ R8 camera execution) |
| Single-vendor implied | **Wrong** — backends pluggable (`GENERATION_BACKEND_POLICY.md`) |
| Image 2.0 as only generator | **Wrong** — stills default only; video separate |

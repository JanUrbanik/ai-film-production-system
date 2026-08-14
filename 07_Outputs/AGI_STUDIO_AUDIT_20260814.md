# AGI × CineAgent Studio — operational audit

**Date:** 2026-08-14  
**Auditor:** factory-side agent (Desktop clone)  
**Handoff authority:** Director note 2026-08-13 (supersedes factory `HANDOFF.md`, `CINEAGENT_M0_REPORT.md`, “Phase B blocked / Studio is M0”)  
**Scope:** How strong is movie production when Jan’s AGI producer operates Studio as the visual panel over the factory.  
**Epistemic:** Desktop and GitHub inspected. Live Studio source was **not** on this machine. An Aug 11 Grok workspace zip exists and is treated as **stale M0**, not current Build.  
**GitHub:** **not pushed.** Audit is not clean for a “latest” factory update. Required method files are **missing** on this clone.

---

## Verdict (blunt)

The **design** is strong enough for an AGI producer **if** it is locked to **one disk of record** (the Build-bundled factory / movie folder) and Jan stays in the SuperGrok Heavy pixel loop.

The **Desktop + GitHub factory clone is not that disk.** It is still v1.2.5-era (`e627e34`, 2026-08-10). It does not contain CineKit LAWs 4–6, MANIFEST, junction/chain packet fields, ingest extras, `porch_letter`, or smoke pixels. An AGI pointed at Desktop will **fight** the live app: hide mouths, skip VDL, glob `04_gen/`, treat mock Continuity as real, and write packets the live Studio will not recognize.

**Do not treat this clone as the operator brain until Jan syncs Build → Desktop.**

Studio as described (Ingest → per-asset bibles → sequence line → click-to-reject → fault brief) is a real control panel. It is **not** yet a closed-loop camera. That is acceptable **if** AGI is forbidden from inventing pixels or passing mock gates.

---

## What was actually on Desktop (2026-08-14)

| Claim in 2026-08-13 handoff | Desktop factory (`ai-film-production-system`) |
|-----------------------------|-----------------------------------------------|
| `10_Sources/method/CINEKIT_METHOD_LAYER.md` | **MISS** |
| `02_Tools/MANIFEST_SPEC.md` | **MISS** |
| Schema: fov, junction, chain, master_prompt, regen_requested | **MISS** — packet schema has none of these |
| `AGENTS.md` LAWs 4–6 | **MISS** — still 8 non-negotiables, ends at K-SHOT |
| VDL / 3+1 / stage map templates | **MISS** |
| Smoke `S01_start_v1.png` / `S01_take01.mp4` | **MISS** (dirs have `.gitkeep` + README only) |
| Movies `porch_letter`, `m0_review_short` | **MISS** — only `_template` + `smoke_imagine_v1` |
| `~/Desktop/cineagent-studio` | **MISS** |
| `CineAgent 13 aug/` | empty folder |
| `CineAgent Studio vana/` | empty `hithubrecovery/` + zip dated **2026-08-11** (M0 shell; `CINEAGENT_M0_REPORT.md`; `.github_repo` = `JanUrbanik/AiMovieProductionInterface`) |

Factory git: `main` == `origin/main` @ `e627e34`. Untracked only: `07_Outputs/LIPSYNC_DIALOGUE_QA_20260813.md` (this session) + this audit. Smoke packet `S01.json` still **validate PASS**, status `ready`, `phase_b.*` still `pending_download`.

Per Director: pixels **landed in Build demo-factory**. This audit **does not** call Phase B failed. It **does** say: **this clone cannot see them.**

---

## Strengths (when AGI is plugged into the *live* app + factory laws)

1. **Folder contract is the right primitive.** Seats, bibles, packets, `04_gen/`, `05_pass/`, `09_qc_log/` beat chat memory. Product intent matches: disk is the film of record.
2. **K-SHOT-SCRIPT-001 is executable.** Four-part conversion, REFS ≠ GEN_PROMPT, screen appearances ≠ word mentions, ID lint in `scripts/validate_packets.py`. Ingest as described writes the right class of files.
3. **Imagine-as-camera is coherent.** Start-frame first, Image 2.0 stills / Video 1.5 motion, Heavy pool first, no silent multi-vendor fanout, no 92/100 as native truth.
4. **CineKit `[M]` import is correctly ranked** *if* written as handoff states: matrix + K-SHOT win conflicts; VDL write-lock from approved still (LAW 4) is the right identity rule.
5. **Generation UX as described is AGI-operable:** script-order stack, junction vs hard-cut, click-reject → archive + fault note + `regen_requested` **without** silent API fire. That is the correct spend law.
6. **Coverage + short clips + multi-take** already exist as factory law. A 60–90s short does not need Masters-module completeness if `05_pass/` + NLE exist.
7. **Speech correction (in-camera `LIPSYNC:YES`, re-take not Higgsfield)** matches the matrix: native audio is in-pass; no public re-glue. (Factory *docs on this clone* still say the opposite — see issues.)

---

## Issues (Issue / Where / Why for AGI / Fix)

Known gaps from the handoff are marked **[KNOWN]**. New or worse-than-stated items are **[NEW]** or **[WORSE]**.

### I-01 — Split-brain: Desktop/GitHub factory ≠ live Studio disk  **[NEW] [BLOCKING]**

- **Where:** `/Users/generationalwealth/Desktop/ai-film-production-system` @ `e627e34` vs Grok Build bundled `demo-factory` + live `src/`.
- **Why it matters:** AGI will open the wrong root, apply stale HANDOFF (“Phase B blocked”, “Studio not built”), skip CineKit, and write artifacts Studio already emits (or fail to read Studio artifacts). Chat-forget is solved only if **one** folder is canonical.
- **Fix:** Jan exports Build workspace (or `demo-factory` + Studio `src/`) onto Desktop. Pick **one** Operation path. Then rewrite factory `HANDOFF.md` / `PROJECT_STATUS.md` from the 2026-08-13 note. Do not push GitHub until that copy exists.

### I-02 — Speech law conflict: hide-mouth / ADR vs in-camera re-take  **[WORSE] [BLOCKING for AGI policy]**

- **Where:** `06_Skills/generation/SPEECH_PERFORMANCE_PROMPT.md` (“prefer OTS/side”; “R11 may replace with VO”); `05_Workflows/MVP_SHORT_FILM_RUNBOOK.md` §6; `03_Roles/seats/R11_Sound.md`; `05_Workflows/QC_RUBRICS.md` repair step 2 “Replace with insert / OTS”; `07_Outputs/LIPSYNC_DIALOGUE_QA_20260813.md` (kit-only Q&A, now **policy-stale** on repair).
- **Why it matters:** AGI that loads factory skills will **hide the mouth** or picture-lock + ADR on speech FAIL. Director law: spoken line → `LIPSYNC:YES`; mouth moves in-camera; FAIL = **re-take**; no Higgsfield port. That is a production-behavior fork, not a comment nit.
- **Fix:** Patch factory speech skill, R6, R11, QC ladder, and the lip-sync Q&A with an explicit **Director override 2026-08-13**. Keep kit matrix facts (`[U]` on `voice_id`, two-speaker, verbatim). Coverage OTS remains valid for **non-speech** or **hide identity**, not as the speech-fail default.

### I-03 — Repair ladder length/order mismatch  **[WORSE]**

- **Where:** Factory `QC_RUBRICS.md` / `CONTINUITY_GATES.md` = 6 steps (ends adapter). Director checklist = 7 steps (adds **new start frame** and **new `/STATE` + VDL**); “identity fail first; two FAIL cycles → escalate; do not assemble around a hole.”
- **Why it matters:** AGI will stop at regen/adapter and never mint a new VDL state. It may also assemble a hole if mock Continuity is ignored.
- **Fix:** Replace factory ladder with Director 7-step list. Encode “2 FAIL → escalate” in R9 + fault UI. Studio Continuity must not allow Masters/assembly while a timeline shot has zero PASS.

### I-04 — Continuity module is a mock  **[KNOWN] [BLOCKING for unsupervised AGI]**

- **Where:** Studio Continuity (live Build). Factory `05_Workflows/CONTINUITY_GATES.md` is **docs only** — no compute. Aug 11 M0 already admitted gates are FAIL scaffolding.
- **Why it matters:** If every gate shows FAIL, AGI either (a) treats FAIL as noise and ships junk, or (b) deadlocks and never cuts. Unsupervised AGI will do (a).
- **Fix (thinnest real R9):** Compute Gate 1 from disk only: `takes.csv` + file exists in `04_gen/` + optional `05_pass/` copy. Binary. Leave Gates 2–4 human until later. Never display FAIL as default decoration.

### I-05 — No MANIFEST spec or file on the operator clone  **[KNOWN on Build / NEW as factory gap]**

- **Where:** Handoff claims `09_qc_log/MANIFEST.csv` + `02_Tools/MANIFEST_SPEC.md`. Neither exists on Desktop. Smoke has `takes.csv` only. Template has neither `takes.csv` nor `MANIFEST.csv`.
- **Why it matters:** Without a spec, AGI **will glob** `04_gen/**/*.mp4` (including `rejects/`). Resume after crash becomes “newest mtime wins.” Assembly order drifts from script order.
- **Fix:** Land `MANIFEST_SPEC.md` + template CSV. Columns at minimum: `shot_id,take,role(still|video),path,status(PASS|FAIL|REJECT),junction,chain,created_at`. Studio and AGI **must** append; glob only as a recovery auditor that never promotes rejects.

### I-06 — Packet schema cannot express live Studio packets  **[NEW] [BLOCKING if Desktop validator is used]**

- **Where:** `02_Tools/schemas/shot_packet.schema.json`. Missing `fov`, `junction`, `chain`, `master_prompt`, `regen_requested`. `status` enum = `draft|ready|gen|qc|pass|fail` only. Smoke packet extra keys (`ledger`, `phase_b`) already sit outside the documented contract.
- **Why it matters:** If Studio writes `status: regen_requested`, `scripts/validate_packets.py` **fails** that packet. AGI “fixing” validation will strip junction/chain. Next I2V may **chain a hard cut**.
- **Fix:** Additive schema fields. Add `regen_requested` to status enum (or a sibling flag). Validator: lint GEN_PROMPT IDs; **do not** reject unknown additive keys. Junction enum: `continuous | scene_change | ellipsis` (or whatever Studio actually writes — copy from Build, do not invent).

### I-07 — Junction/chain not factory-law on this clone  **[NEW]**

- **Where:** Studio (handoff): continuous = green link / last-frame chain; `scene_change` / `ellipsis` = chain OFF. Factory only has `06_Skills/generation/EXTEND_CHAIN.md` (extend from PASS) and mockup note “last-frame chaining.” No packet field.
- **Why it matters:** AGI using factory EXTEND skill on an ellipsis will **morph a cut**. That is the exact failure Director forbade.
- **Fix:** Promote junction to factory law (one-pager + R6 + R8). Default chain = OFF unless junction = `continuous` **and** previous take is PASS.

### I-08 — VDL / plates are prompts only; no approved-image lock on Desktop  **[KNOWN]**

- **Where:** Handoff: VDL = `AWAITING_APPROVED_IMAGE`; 3+1 / angles written under `02_refs/_prompts/`. Factory `_template` has no `_prompts/`, no per-asset `01_bibles/assets/`, no VDL field on `CHARACTER_BIBLE.md`.
- **Why it matters:** AGI will generate volume I2V from **script description** (LAW 4 violation) or treat prompt markdown as if it were a locked plate.
- **Fix:** Keep VDL non-auto (correct). Gate R8: refuse hero I2V if any on-camera CHAR/LOC/PROP VDL ≠ approved. UI badge is not enough — hard stop in packet status.

### I-09 — Fault loop is not a camera  **[KNOWN] — acceptable if enforced**

- **Where:** Studio fault textarea → `04_gen/<id>/rejects/` + `09_qc_log/faults/` + `REGEN_BRIEF.md` + takes FAIL. Does **not** call Imagine. Factory R8 adapter is API-shaped and spend-locked.
- **Why it matters:** Closed-loop AGI will either stall (“queued”) or **break spend law** by curling `XAI_API_KEY`. The loop is enough for **human-in-the-loop** Heavy UI. It is **not** enough for unattended 400-clip nights.
- **Fix:** Do **not** add a silent API hook. Add an explicit operator state: `AWAITING_HUMAN_IMAGINE` with the exact consumer prompt + start-frame path. AGI’s job = write brief + open that card. Optional later: Director-unlock API adapter.

### I-10 — Deterministic Ingest ≠ literary director  **[KNOWN]**

- **Where:** Studio converter vs `05_Workflows/TRANSCRIPT_TO_SHOT_SCRIPT.md` (expects R2 + FLAGS review). Factory conversion writes 4 parts; Studio writes many more (STORY_BIBLE, per-asset files, ATTACHMENT_CONVENTION, MANIFEST).
- **Why it matters:** AGI will trust FLAGS and IDs as locked story. Screen-appearance counts from a dumb converter will be wrong; volume gen will lock the wrong cast.
- **Fix:** Hard stop after Convert: `FLAGS.md` + element confirm must be `Director OK` before any Image 2.0. Do not let AGI self-approve FLAGS.

### I-11 — Masters / 60–90s film not producible inside the app  **[KNOWN]**

- **Where:** Studio Masters = frame. Factory Stage G/H is CapCut/DaVinci + `05_pass/`.
- **Why it matters:** AGI cannot “export the movie” from Studio. It can only stack takes. Fine — if `05_pass/` + MANIFEST exist. Today Desktop smoke has no PASS bin media.
- **Fix:** Thinnest path: Play-in-order (already in Studio) + copy PASS files to `05_pass/` + `06_edit/` EDL or concat list. Real NLE stays outside. Do not block first short on a Masters module.

### I-12 — Stale factory operator docs will gaslight AGI  **[NEW]**

- **Where:** `HANDOFF.md` v3.0, `PROJECT_STATUS.md`, `07_Outputs/IMAGINE_SMOKE_20260809.md` (BLOCKED), `CINEAGENT_STUDIO_PRODUCT_BRIEF.md` (app not coded), Build prompt “M0 only.”
- **Why it matters:** First thing a new AGI chat reads is “no pixels, Studio not built.” It will re-scaffold M0 or re-run Phase B.
- **Fix:** After Jan syncs files, rewrite HANDOFF from the 2026-08-13 note. Stamp smoke report COMPLETE only if png/mp4 are **on that clone**.

### I-13 — CineKit method file absent; `[M]` vs Verified unlabeled on clone  **[KNOWN as import / NEW as missing file]**

- **Where:** `10_Sources/method/CINEKIT_METHOD_LAYER.md` missing. `00_Epistemics/` has claim labels but no `[M]`.
- **Why it matters:** AGI will treat CineKit process (3+1, VDL, attachment convention) as **Verified Grok behavior** or ignore it entirely.
- **Fix:** Land the method file with `[M]` banner and a conflict table: K-SHOT + matrix win.

### I-14 — Two GitHub identities; Studio src not in factory repo  **[NEW / hygiene]**

- **Where:** Factory remote = `JanUrbanik/ai-film-production-system`. Aug 11 zip `.github_repo` = `JanUrbanik/AiMovieProductionInterface`. No `src/` on Desktop factory.
- **Why it matters:** Pushing factory `main` cannot publish live Studio. Pushing the old zip would **regress** past-M0 Build to M0.
- **Fix:** Factory repo = laws/seats/schemas/movies. Studio app = Build export or the interface repo **after** Jan dumps current source. Never commit the Aug 11 zip as current.

### I-15 — `voice_id` / two-speaker / negatives still `[U]`  **[KNOWN]**

- **Where:** Matrix + `07_Outputs/LIPSYNC_DIALOGUE_QA_20260813.md` Q2, Q3, Q6, Q9. CineKit T1–T9 (not on this disk).
- **Why it matters:** AGI will invent a voice bible from `CHARACTER_BIBLE` “voice intent” or pack two speakers into one gen because a master prompt showed HARD CUT.
- **Fix:** Leave `[U]`. Factory default remains: one speaker visible per `LIPSYNC:YES` clip; no user-WAV visemes; coverage for two-handers. Do not “complete” T1–T9 in prose.

---

## Answers to Director audit questions

### 1. Can AGI drive Ingest → bible → packets without chat memory?

**On live Studio (as described): mostly yes, after FLAGS confirm.** Writes land on the movie folder.  
**On this Desktop clone: no.** Converter extras (STORY_BIBLE, assets/, `_prompts/`, ATTACHMENT_CONVENTION, MANIFEST) are not in `_template` or workflows. AGI would emit the old 4-part set and think it was done.

### 2. Where can it silently drift?

- No VDL approved → gen from script text (LAW 4 break).
- Mock Continuity all-FAIL → ignore gates.
- No auto plates → skip refs, I2V anyway.
- Glob `04_gen/` including `rejects/`.
- Chain extend across `scene_change` / ellipsis.
- Speech FAIL → OTS/ADR instead of re-take (factory skill).
- Self-approve FLAGS.
- Read Desktop HANDOFF and restart M0 / Phase B.

### 3. Is MANIFEST enough, or will AGI glob `04_gen/`?

**MANIFEST is not on this clone, so AGI will glob.** Even with a MANIFEST, AGI globs unless the spec is law and Play-in-order / Masters read **only** MANIFEST+PASS rows. Treat glob as forensic, never as the edit list.

### 4. Can it obey junction/chain so it doesn’t morph cuts?

**Only if it uses Studio packet fields that do not exist in the factory schema/skills here.** Factory EXTEND_CHAIN will happily continue an ellipsis. This is a real morph risk.

### 5. Is the fault-note loop enough for closed-loop repair?

**Enough for Director-in-the-loop. Not enough for unattended AGI.** Next pixels are SuperGrok Heavy UI. Do not add an Imagine API hook to close the loop. Add `AWAITING_HUMAN_IMAGINE` so AGI does not stall or cheat.

### 6. Thinnest missing piece before a 60–90s short is producible end-to-end?

Not Masters. Not full R9. Not auto Image 2.0.

**Thinnest stack:**

1. **One synced movie folder** (Build demo-factory → Desktop, or AGI lives only in Build).
2. **Junction + MANIFEST on disk** (so assembly order is not a guess).
3. **Human Heavy loop** for approved stills + I2V takes (already the spend law).
4. **Take-level PASS copy into `05_pass/`** (binary, no mock).
5. **Play-in-order or NLE** from PASS+MANIFEST.

A 60–90s env+1-cast piece is then a **production** job, not an app feature. Auto plates, real Gates 2–4, and Masters export can wait.

### 7. Any law conflict (K-SHOT vs CineKit vs Studio defaults)?

| Conflict | Winner if handoff is law | What this clone currently does |
|----------|--------------------------|--------------------------------|
| CineKit vs K-SHOT REFS/GEN_PROMPT | K-SHOT | K-SHOT (good) |
| CineKit vs Imagine matrix (`voice_id`, etc.) | Matrix | Matrix (good) |
| VDL vs script-as-identity | LAW 4 (CineKit `[M]`) | No VDL — script/bible text wins by omission |
| Speech fail = OTS/ADR vs in-camera re-take | **Director 2026-08-13** | Factory skills = hide/ADR |
| Repair 6-step vs 7-step + VDL | Director checklist | 6-step, no VDL |
| WARD plates vs ledger-only | Handoff WARD ledger-only | Template still has wardrobe ref folders |
| Deterministic Ingest vs R2 literary conversion | Studio converter + FLAGS review | Workflow still says R2 four-part only |

No conflict found that says Image 2.0 is video. Backends remain pluggable on paper.

### 8. Git hygiene — what can actually be committed from Desktop?

**Can commit now (and should not, as “latest”):**
- `07_Outputs/LIPSYNC_DIALOGUE_QA_20260813.md` — useful kit Q&A, **stale on speech repair policy**
- `07_Outputs/AGI_STUDIO_AUDIT_20260814.md` — this file

**Cannot commit (files not on disk):**
- `10_Sources/method/CINEKIT_METHOD_LAYER.md`
- `02_Tools/MANIFEST_SPEC.md`
- schema extras (fov/junction/chain/master_prompt)
- VDL / 3+1 template upgrades
- LAW 4–6 in `AGENTS.md`
- rewritten `HANDOFF.md` / `PROJECT_STATUS.md` matching live Studio (**must not invent**)
- smoke png/mp4
- `porch_letter`, Studio `src/`

**Must not:**
- Push the Aug 11 zip as current Studio
- Force-push
- Claim `AiMovieProductionInterface` is in sync (not inspected live; zip is M0)

---

## GitHub decision (step 5)

**No push.**

> Desktop factory is behind this note. CineKit method, MANIFEST spec, schema extras, LAW 4–6, ingest templates, `porch_letter`, and smoke pixels are **not** on this clone. Live CineAgent Studio source is still **Grok Build** (plus a stale 2026-08-11 M0 zip that must not be published as current).  
> GitHub factory updated (method + templates) — **not done**. Needs an explicit sync/export from Jan before any “latest” push.

---

## Relay pack for Build Mode (copy this list)

1. **I-01 BLOCKING** — Split-brain Desktop vs Build disk. Sync before AGI operates.  
2. **I-02 BLOCKING policy** — Factory speech skill still says hide-mouth/ADR; override to in-camera re-take.  
3. **I-03** — Align repair ladder to Director 7 steps + 2-FAIL escalate.  
4. **I-04 KNOWN** — Continuity mock. Ship take-level disk PASS/FAIL only.  
5. **I-05** — MANIFEST spec + forbid glob-as-edit.  
6. **I-06 BLOCKING if shared validator** — Add junction/chain/fov/master_prompt/`regen_requested`.  
7. **I-07** — Chain default OFF except `continuous` + prior PASS.  
8. **I-08 KNOWN** — Hard-stop I2V without approved VDL.  
9. **I-09 KNOWN** — Fault loop stays human-Imagine; state `AWAITING_HUMAN_IMAGINE`.  
10. **I-10 KNOWN** — FLAGS Director OK before plates.  
11. **I-11 KNOWN** — First short via `05_pass/` + Play-in-order/NLE, not Masters module.  
12. **I-12** — Stale HANDOFF/status will make AGI rebuild M0.  
13. **I-13** — Land CineKit method file with `[M]`.  
14. **I-14** — Do not publish Aug 11 M0 zip.  
15. **I-15 KNOWN** — Keep voice/two-speaker `[U]`.

**AGI operating rule until sync:** Operate **only** the Build movie folder. Do not trust Desktop `HANDOFF.md`. Do not call Imagine API. Do not pass mock Continuity. Do not hide mouths on speech FAIL.

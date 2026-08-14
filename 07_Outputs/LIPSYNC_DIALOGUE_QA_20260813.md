# Lip-sync / dialogue Q&A — kit-only

**Date:** 2026-08-13  
**Source session:** AI Film Production System continuity chat (post-bootstrap; Showrunner open on `smoke_imagine_v1`; Director research order — no production work).  
**Epistemic rule:** **Kit-only.** Claims labeled **Verified** / **Assumed** / **Speculative** / **Unknown in kit**. No invented platform claims. Matrix as-of **2026-08-08**. This file did **not** re-query `docs.x.ai` or the live SuperGrok UI.

**Showrunner assignment (that session):** Research-only. Tools/Imagine matrix first (`02_Tools/GROK_IMAGINE_CAPABILITY_MATRIX.md`), then adapter + spend + speech skill + R6/R11/R9 factory rules. No dedicated Tools seat — matrix is law; R8 executes gen, R11 owns voice/ADR, R6 marks `LIPSYNC`, R9 gates speech.

---

### 1. Native vs separate lip-sync pass

**Verified**
- T2V returns **clip + native audio** in one generation call. `02_Tools/GROK_IMAGINE_CAPABILITY_MATRIX.md` §3.2–3.3.
- Native audio is **default on**; kit lists “SFX, ambience, **dialogue in-pass** (1.5 improved sync).” Same file §3.3.
- Documented video workflows are only T2V / I2V / R2V / edit / extend. **None is a separate lip-sync or ADR stage.**
- Practitioner method: type the dialogue the character should say. `03_Knowledge/PRACTITIONER_GROK_AS_CAMERA.md` Phase D.

**Assumed**
- Putting a line in the prompt is meant to produce **mouth motion and voice in that same clip**, not a later speech pass. Skill: “Native audio may include the line.” `06_Skills/generation/SPEECH_PERFORMANCE_PROMPT.md`.

**Unknown in kit**
- Whether consumer UI can generate picture first, then add speech.
- Whether native audio can be turned off.
- How reliably mouth + voice lock when dialogue is in the prompt (kit only says 1.5 “improved sync”; skill calls quality **variable**).

**Re-check:** `docs.x.ai` video generation (audio default / disable); live Imagine UI; a speech smoke (not Phase B S01 — that shot is `LIPSYNC: NO`).

---

### 2. Own WAV / TTS driving lip-sync

**Verified restriction**
- Public API: `reference_audios` + **preset `voice_id`**. Max **3** preset voices. **Not arbitrary uploads.** **US trusted partners** gate. Matrix §3.3, §4, §6.
- “Arbitrary voice clone from user sample” = **not in public API docs.** Matrix §4.
- Adapter maps packet `voice_id` → `reference_audios` **if account allows.** `02_Tools/adapters/GROK_IMAGINE_ADAPTER.md`.
- R11: preset `voice_id` only if allowed; else external. `03_Roles/seats/R11_Sound.md`.

**Unknown in kit**
- Any consumer path that accepts a **user WAV** and drives visemes from it.
- Whether `reference_audios` is file-upload of presets or ID-only.
- Whether this SuperGrok Heavy account is inside the US-partners gate.

**Re-check:** `docs.x.ai` reference-to-video / `reference_audios`; live Imagine upload UI; account entitlement.

---

### 3. Voice lock across clips

**Verified**
- Face lock is **visual refs / I2V first frame / R2V images** — not a voice system. Matrix §4.
- No public **user voice clone**. Preset `voice_id` only, max **3**, gated. Matrix §3.3, §4, §6; `01_Architecture/DIAGRAM_CORRECTIONS.md`.
- Character bible field is **“Voice intent (cast later; preset voice_id if any)”** — a factory note, not a platform lock. `04_Bibles/templates/CHARACTER_BIBLE.md`.

**Assumed (factory workaround, not Imagine guarantee)**
- R11: “One voice profile per character **when possible**.”
- If native voice is weak: **ADR / VO / optional ElevenLabs.** `02_Tools/adapters/OPTIONAL_MODEL_ADAPTERS.md`, `06_Skills/generation/SPEECH_PERFORMANCE_PROMPT.md`, `05_Workflows/MVP_SHORT_FILM_RUNBOOK.md` §6, `05_Workflows/LONGFORM_CONSISTENCY.md` (“audio glue”).
- Seed is **not** documented as an identity/voice system. Matrix §4.

**Unknown in kit**
- Whether the same face + same prompt reuses a voice across takes.
- Any character-bound voice ID, sample store, or seed that survives ~400 clips.

**Re-check:** `reference_audios` availability on this account (matrix re-verify list); live multi-clip same-character test; docs for any new voice-lock field.

---

### 4. Hard limits per clip (words / too-long line)

**Verified**
- API duration **1–15 s**. Matrix §3.3; `01_Architecture/CANONICAL_PIPELINE.md` §7.
- Conversion path **caps 8 s** unless Director overrides. `K-SHOT-SCRIPT-001` (`03_Knowledge/TRANSCRIPT_TO_SHOT_SCRIPT.md`, `10_Sources/standards/TRANSCRIPT_TO_SHOT_SCRIPT_STANDARD_v1.md`); packet `duration_policy` in `02_Tools/schemas/shot_packet.schema.json`.
- Factory **dialogue coverage target: 4–6 s.** Pipeline §7.
- One shot = **one camera position, one continuous action.** `10_Sources/standards/TRANSCRIPT_TO_SHOT_SCRIPT_STANDARD_v1.md` §5.1.

**Unknown in kit**
- Max spoken **words**.
- What happens if the line is longer than the clip: truncate, rush, or fail. **Not stated.**

**Re-check:** `docs.x.ai` generation page; timed smoke with a line that cannot fit N seconds.

---

### 5. Framing required for lip-sync

**Verified (factory marking rule — not a measured model limit)**
- Mark `LIPSYNC: YES` **only when a mouth is visible speaking.** Standard §5.4; `03_Roles/seats/R6_Shot_Designer.md`; `03_Knowledge/TRANSCRIPT_TO_SHOT_SCRIPT.md` §5.

**Assumed**
- Prefer I2V from a **mouth-neutral / pre-speech** start still. `06_Skills/generation/SPEECH_PERFORMANCE_PROMPT.md`.
- If lips fail: keep picture + ADR, **or prefer OTS / side.** Same skill. That implies frontal/mouth-visible is the intended lip-sync framing, and OTS is the hide-mouth path.

**Unknown in kit**
- Whether profile, OTS, wide, or low light **degrades or breaks** platform lip-sync. No measurements.

**Re-check:** controlled stills (CU frontal vs profile vs OTS vs WS) on Video 1.5.

---

### 6. Two speakers in one clip

**Verified (how *this factory* cuts two-handers)**
- Dialogue coverage pack is **split shots**: wide, two-shot, OTS A/B, CU A, CU B. `04_Bibles/templates/SHOT_CARD_SCHEMA.md`.
- One shot = one camera + one action; **≤8 s** on conversion path.
- Speech anti-pattern: “complex walk + full speech + whip pan in one gen.” `06_Skills/generation/SPEECH_PERFORMANCE_PROMPT.md`.

**Unknown in kit**
- Whether Imagine **tracks two mouths / two voices** in one generation.
- Speaker count or line-swap limit.
- The **HARD CUT two-character exchange** example is **not in this repo** (not in matrix, shot standard, CineAgent brief, or smoke). Do not interpret an external master prompt as kit fact.

**Re-check:** live two-shot with alternating lines; `docs.x.ai`; that external prompt vs current UI.

---

### 7. Cost: native-audio vs silent

**Verified**
- **API** Video 1.5: **$0.080 / sec**. Legacy video id: **$0.050 / sec**. Matrix §3.4; `02_Tools/adapters/GROK_IMAGINE_ADAPTER.md` cheat sheet. **No silent vs dialogue split.**
- Native audio is **default on** (matrix §3.3), so the kit does not describe a cheaper silent SKU.
- **Consumer** SuperGrok Heavy: shared **weekly pool**, “compute-weighted, not 1:1 seconds.” `02_Tools/SPEND_POLICY_SUPERGROK_FIRST.md`. Production smoke ledger is that pool, not API $/sec.

**Unknown in kit**
- Any credits-per-second delta for talking vs silent clips (API or consumer).

**Re-check:** `docs.x.ai/developers/pricing`; SuperGrok Settings → Usage after one silent and one dialogue take of equal duration/res.

---

### 8. Repair if picture is good, lips are wrong

**Verified**
- Named Imagine repair modes: **video edit** (NL edit; “preserve rest of scene”) and **extend**. Matrix §3.2. Edit source duration cap ~**8.7 s**.
- Kit examples of edit: **object / wardrobe / style** (e.g. jacket color). Not audio-only. Pipeline §4; adapter.
- Factory QC ladder: trim → insert/OTS → video edit → extend → **full regen** → chartered adapter. `05_Workflows/QC_RUBRICS.md`; `05_Workflows/CONTINUITY_GATES.md`.
- Factory speech repair: **keep picture + ADR**, or change coverage. Speech skill; MVP runbook §6; R11.

**Unknown in kit**
- Terms **“Clip Patch”** and **“Clip Regen”** — **not used** in this factory.
- Whether video edit can change **audio only** or lips only, and whether that costs less than a new generation.

**Re-check:** `docs.x.ai` video editing (audio-only / mute / replace speech); live edit-vs-regen Usage; do not treat those product names as law until they appear in docs or UI.

---

### 9. Languages (Spanish / English) and verbatim

**Verified (what we *send*, not what the model *does*)**
- Factory requires **verbatim** locked line in `DIALOGUE` + delivery; `LIPSYNC: YES` only if mouth visible. Standard §5.4; `05_Workflows/INJECTION_ENGINE.md` 4d.
- Prompt recipe: **exact words** (or Director-approved locked paraphrase) + emotion + pauses. Speech skill; practitioner Phase D.

**Unknown in kit**
- Which languages get accurate mouth shapes. **Spanish and English are not tested or listed.**
- Whether Video 1.5 speaks the quoted line **verbatim** or paraphrases.

**Re-check:** official language list on `docs.x.ai` / Imagine help; paired EN/ES smokes with a locked quote vs output transcript.

---

### 10. Post-hoc dub: replace generated audio

**Verified (factory path exists)**
- Post is **locked picture → stems**. Tools: “Imagine native + TTS/DAW.” `01_Architecture/CANONICAL_PIPELINE.md` Stage H.
- If lips fail: keep native beds where usable; **ADR/VO**; optional **silent picture lock.** MVP §6; R11; longform “audio sells continuity.”
- Nothing in kit exports visemes, viseme tracks, or a re-time contract.

**Assumed**
- Swap on a **mouth-visible** take will show the original mouth against the new track unless you hide the mouth (OTS/wide/insert) or match timing by hand.
- Swap on **mouth-not-visible** coverage is the designed hide.

**Unknown in kit**
- Whether *anything* besides the baked picture “survives” a swap.
- That a swap **always** “guarantees visible desync” — not measured. Depends on framing (see Q5).

**Re-check:** one picture-lock + external WAV align on CU vs OTS.

---

## What this decides for production (Verified + Assumed only)

**Voice across ~400 clips is not locked like a face.** Public Imagine gives **in-pass native audio** (one gen, default on). **Your WAV cannot drive lips** on the documented API. The only platform voice control in-kit is **gated preset `voice_id` (max 3)** — unknown on this account. The factory’s written path for a stable cast voice is **picture PASS + external VO/ADR** (optional ElevenLabs), not Imagine character-voice IDs. Treat native dialogue as a **bonus take**, not the voice bible.

**Dialogue cost is take volume + ADR, not a documented cheap audio patch.** There is **no kit “Clip Patch = audio only.”** Video edit is a visual local fix; speech fail → keep picture and ADR, or regen. **No silent-vs-talking rate** is documented; API is flat **$/sec**; consumer is the **weekly pool**.

**Confrontation scenes should be coverage, not one HARD-CUT two-hander gen.** Kit law is **one move + one action**, **4–6 s dialogue clips**, **`LIPSYNC` only on mouth-visible singles**, two-handers split **CU/OTS**. Two-speaker tracking, line-swap limits, word caps, and too-long-line behavior are **not in the kit** — do not plan clip count on a two-person-in-one-gen bet until a live test says otherwise.

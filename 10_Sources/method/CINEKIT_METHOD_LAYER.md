# CineKit Method Layer v1.1 — integration (Grok-native)

**Type:** Additive method. Does **not** replace `K-SHOT-SCRIPT-001`.  
**Source:** `CINEKIT_UPGRADE_PACK_v1.1.md` (Higgsfield method → Grok/xAI only).  
**Date:** 2026-08-13  
**Conflict rule:** Capability matrix + K-SHOT-SCRIPT-001 win. This file is `[M]` process.

## Epistemic

Imported practice = **`[M] Method`**. Safe as workflow. Not verified Grok-model behavior.

## Three new root laws

**LAW 4 — DESCRIPTION FOLLOWS THE IMAGE.** `[M]`  
Canonical look is written **from the approved reference still**, never from the script.  
VDL is authored **after** plate approval.

**LAW 5 — THE ASSET WINS.** `[M]`  
If script and approved asset disagree, amend the script. Escalate only if narrative-critical.

**LAW 6 — ONE ATTACHMENT CONVENTION, PROJECT-WIDE.** `[M]`/`[A]`  
How refs attach to Imagine is locked once per movie. Never improvised shot-to-shot.

## Production order (Studio Ingest)

```
1 Transcript
2 Identify key elements (screen appearances, not word count)
3 Convert → bible + ledger + shot script + flags + packets + manifest row stubs
4 3+1 ref plates (Image 2.0, separate calls) → Director picks winner
5 VDL written FROM the approved image (Law 4)
6 LOCK packs
7 Start frames (cinematic stills — not the flat refs)
8 Gate → I2V Video 1.5
9 Assembly reads MANIFEST only
```

## Reference counts (unchanged kit law)

| Class | Plates | Notes |
|---|---|---|
| CHAR | 5 | front, ¾ L, profile, back, tight face |
| PROP / VEH | 4 | front, ¾, side, rear |
| LOC | 4 + 1 wide per lighting state | |
| WARD | **ledger only** unless face cannot match (`CHAR_00N/B`) | §2.4 costume policy |
| LOOK | 0 photos | grade note |

3+1: three **separate** variant calls, pick one, then shoot the angle set from the winner.

## Dialogue inversion `[A]`

No documented Grok post-hoc lip-sync. Replaceable lines = **mouth-hidden** (OTS, profile, wide, insert).  
`LIPSYNC: YES` is a deliberate exception.

## Do not port

soul_cast, `<<<element_id>>>`, Higgsfield lipsync/credits/concurrency, Clip Patch names, 16:9 hardcode, variant-state regression.

## Studio files written on convert

- `01_bibles/STORY_BIBLE.md` — index of every element
- `01_bibles/assets/<ID>.md` — description, ref prompts, VDL stub, invariants / stage map
- `02_refs/_prompts/<ID>_REF_PROMPTS.md` — 3+1 + angle prompts
- `09_qc_log/MANIFEST.csv` — append-only clip ledger
- `00_brief/ATTACHMENT_CONVENTION.md` — project lock

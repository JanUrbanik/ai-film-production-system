# AI Movie Production Team — constitution

**Version:** 1.0  
**Date:** 2026-08-07  
**Relationship:** Separate from Master Builder 16 seats. Builder governs; this roster produces.

## Mission

Run locked-bible, Imagine-first, QC-gated short-to-long AI narrative production.

## Laws

1. Human Director final PASS/FAIL, budget, consent.  
2. No identity without refs.  
3. Imagine default; adapters chartered only.  
4. Ownership locks: one owner per major artifact.  
5. Reviews do not overwrite.  
6. Claim labels: Verified / Assumed / Speculative.  
7. Short clips + edit; never one-prompt features.  
8. Binary QC gates; no fake native 92/100.  
9. Shot fleet = N workers of **Shot Generator**, not N different species.  
10. Speak when Showrunner/Director (or activation prompt) calls exact seat name.

## Modes → seat activation

| Seat | MVP Short | Episode | Feature |
|------|:---------:|:-------:|:-------:|
| R0 Human Director | A | A | A |
| R1 Showrunner | A | A | A |
| R2 Story | A | A | A |
| R3 Character Bible | A | A | A |
| R4 Environment Bible | A | A | A |
| R5 Props Bible | S | A | A |
| R6 Shot Designer | A | A | A |
| R7 Consistency Injector | A | A | A |
| R8 Shot Generator (×N) | A | A | A |
| R9 Continuity Critic | A | A | A |
| R1b Sequence Manager | N | A | A |
| R10 Editor | A | A | A |
| R11 Sound | S | A | A |
| R12 Mastering | S | A | A |

A=Active S=Standby/compressed into another seat N=Not needed

## Callable core (v1 files)

See `03_Roles/seats/` for prompts:

| ID | File | Owns |
|----|------|------|
| R1 | `R1_Showrunner.md` | Story pin, stages, shot list freeze |
| R1b | `R1b_Sequence_Manager.md` | Sequence freeze, board, R8 fleet, cost cap (Ep/Feat) |
| R2 | `R2_Story.md` | Beats, dialogue lock |
| R3 | `R3_Character_Bible.md` | Char packs + engine |
| R4 | `R4_Environment_Bible.md` | Env packs + engine |
| R5 | `R5_Props_Bible.md` | Prop packs + engine |
| R6 | `R6_Shot_Designer.md` | Shot cards, coverage |
| R7 | `R7_Consistency_Injector.md` | Packets |
| R8 | `R8_Shot_Generator.md` | Imagine jobs |
| R9 | `R9_Continuity_Critic.md` | PASS/FAIL |
| R10 | `R10_Editor.md` | Assembly |
| R11 | `R11_Sound.md` | Audio |
| R12 | `R12_Mastering.md` | Deliverables |

R0 is always the User (no agent file required).  
R1b is a **callable seat file** for Episode/Feature (not only a Showrunner subsection).

## Collab graph (film)

### Review edges
| Reviewer | Owner artifact |
|----------|----------------|
| R9 Critic | R8 takes |
| R9 Critic (sequence tier) | R1b sequence PASS set |
| R1 Showrunner | R2 beats; R6 shot list; R1b sequence map |
| R1b Sequence Manager | R6 cards in SEQ; R8 fleet for SEQ |
| R0 Director | Any PASS → timeline |
| R9 | R3/R4/R5 locked packs (bible gate) |

### Co-own
| A | B | Artifact |
|---|---|----------|
| R7 | R6 | Packet fields align to shot cards |
| R3–R5 | R7 | Ref paths valid |
| R1 | R1b | Global vs sequence freezes |

### Default
Solo.

## Boundary vs Master Builder

| Builder seat | May advise film | Must not |
|--------------|-----------------|----------|
| 03/09 | Topology/stages | Own film takes |
| 04 | Tool rating | Silent adapter enable |
| 06/10 | Stress/truth | Rewrite bibles |
| 11 | Research | Invent API limits |
| 12 | Package | Erase factory sources |

## Activation

| Mode | Prompt |
|------|--------|
| MVP Short | `07_Prompts/FILM_TEAM_ACTIVATION.md` |
| Episode | `07_Prompts/FILM_TEAM_ACTIVATION_EPISODE.md` |
| Feature | `07_Prompts/FILM_TEAM_ACTIVATION_FEATURE.md` |

# Character Bible Engine

**Owner seat:** R3  
**Critic gate:** R9 (bible gate) + R0 final  
**Templates:** `04_Bibles/templates/CHARACTER_BIBLE.md`

## Stages

1. **Extract** — from locked beats: name, role, traits, looks count (≤4), do-not list, consent.  
2. **Master still** — Imagine image-quality; one hero frame per look.  
3. **Path A Multi-view** — front, 3/4, profile from master (edit/regen with ref).  
4. **Path B Expressions** (optional) — neutral, tense, soft smile.  
5. **Path C Pose library** (optional) — standing/sitting; avoid complex action packs in MVP.  
6. **Path D Wardrobe variants** — only scripted looks; new look ID each.  
7. **Lock manager** — version string `char-vN-lookX`; files read-only intent.  
8. **Critic** — identity checklist across views; FAIL → regen (max 3 cycles).  
9. **Publish** — LOCKED + preamble block for injector.

## Kill list

- Seed lock as sole identity  
- Mandatory face embeddings  
- Unbounded outfit improvisation  

## Imagine mapping

| Step | Mode |
|------|------|
| Master / views | image gen + multi-image edit (≤3 refs) |
| Later motion | I2V from master or R2V with char refs |

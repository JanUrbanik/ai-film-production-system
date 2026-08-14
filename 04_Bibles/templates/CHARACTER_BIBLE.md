# Character Bible — `{{CHAR_ID}}`

**Version:** 0.1  
**Lock status:** DRAFT | LOCKED  
**Consent:** original character | licensed | real person w/ written consent  

## Identity

| Field | Value |
|-------|-------|
| Name | |
| Role (1 sentence) | |
| Age range | |
| Body / height language | |
| Face anchors | eyes, skin, hair, facial hair, scars |
| Voice intent | (cast later; preset voice_id if any) |
| Do-not list | |

## Looks (max 2–4)

### Look `A` — name
- Wardrobe exact:
- Palette:
- Props worn:
- Ref folder: `02_refs/characters/{{CHAR_ID}}/look_A/`

### Look `B` — name (optional)
- …

## Frozen identity preamble (paste every shot)

```text
CHARACTER LOCK — {{NAME}}: {{face}}, {{hair}}, {{skin}}, {{body}}.
LOOK {{LOOK_ID}}: {{wardrobe exact}}.
NEGATIVE: identity drift, face morph, age change, different person, extra fingers, warped hands.
REF: match attached reference images exactly for face and wardrobe.
```

## Multi-view pack checklist

- [ ] Hero master still  
- [ ] Front  
- [ ] 3/4 L + R  
- [ ] Profile  
- [ ] Expression set (neutral, tense, soft smile) — optional  
- [ ] Full body once per look  

## Imagine path for pack

1. Generate master with `grok-imagine-image-quality`  
2. Multi-image edit or controlled regen for angles **from master**  
3. Lock files; no silent replacements after LOCKED  

## Voice record (register before production)

| Field | Value |
|-------|-------|
| Voice source | native bonus take / external ADR / preset voice_id |
| Identifier | |
| Sample ref | |
| Doctrine | Native dialogue is a bonus take, not the voice bible |

## VDL — Visual Description Lock `[M]` LAW 4

**Status:** AWAITING_APPROVED_IMAGE  

Write **after** the 3+1 winner still is approved. Look at the image. If the image disagrees with DESCRIPTION, the image wins (LAW 5) and DESCRIPTION is corrected.

```
VDL {{CHAR_ID}}:
  <1–2 sentences from the approved still>
  - wardrobe / surface that must not drift
  - 1–2 hook features actually visible
  - explicit negations (no hat, no tie, …)
```

## Invariants `[M]`

```
INV {{CHAR_ID}}:
  1. <permanent physical fact>
  2. <state rule>
  3. <conditional rule>
```

## 3+1 plate workflow

1. Three **separate** Image 2.0 variant calls (never one batch of 3)
2. Director selects winner
3. Shoot 5-angle set from winner (front, ¾ L, profile, back, tight face)
4. Dual channel: adapter ref-set id **and** file path
5. Then write VDL from the image

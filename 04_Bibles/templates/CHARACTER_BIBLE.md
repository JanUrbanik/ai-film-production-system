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

## Dual-identity note (if any)

- Soul ID = same face geometry  
- Looks only swap wardrobe  
- Reveal scenes must use soul refs + look B wardrobe only  

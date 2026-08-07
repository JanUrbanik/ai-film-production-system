# Environment Bible — `{{LOC_ID}}`

**Version:** 0.1  
**Lock status:** DRAFT | LOCKED  

## Core

| Field | Value |
|-------|-------|
| Name | |
| Interior / exterior | |
| Time of day default | |
| Weather / season | |
| Palette / materials | |
| Key landmarks | |
| Continuity rules | (e.g. always wet street, neon left) |
| Do-not list | |

## Zones

| Zone ID | Description | Ref stills |
|---------|-------------|------------|
| Z1 | | `02_refs/environments/{{LOC_ID}}/Z1/` |
| Z2 | | |

## Lighting matrix

| Setup | Description | When used |
|-------|-------------|-----------|
| L_day | | |
| L_magic | | |
| L_night | | |

## Establishing pack checklist

- [ ] Wide master  
- [ ] Opposite angle  
- [ ] Detail / texture plate  
- [ ] Empty plate for coverage  

## Frozen env preamble

```text
LOCATION LOCK — {{LOC_NAME}}: {{landmarks}}, {{materials}}, {{time}}, {{light}}.
NEGATIVE: location teleport, architecture morph, random weather change, extra buildings.
REF: match environment reference plates.
```

## Imagine path

1. T2I master plates (`grok-imagine-image-quality`)  
2. Edit for alternate angles from master when possible  
3. I2V only for living atmosphere B-roll; characters via R2V/I2V with char refs  

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

## Stage Map `[M]` — write from approved location image

```
STAGE_MAP {{LOC_ID}}:
  anchor_object:
  landmarks:     relative to the anchor only
  zones:
  entrances_exits:
  light_sources: direction + practicals
```

All blocking uses only these landmarks. No "left third of frame."

## VDL `[M]` LAW 4

**Status:** AWAITING_APPROVED_IMAGE  

```
VDL {{LOC_ID}}:
  <1–2 sentences from the approved still>
  - materials / palette that must not drift
  - hook landmarks visible in the still
  - explicit negations
```

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

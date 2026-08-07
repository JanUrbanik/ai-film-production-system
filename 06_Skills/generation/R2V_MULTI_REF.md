# Skill: Reference-to-video multi-ref

## When

Need character/prop/env identity in a **new** shot that should not force a specific first frame.

## Rules

1. Order refs deliberately; tag in prompt as `<IMAGE_1>`, `<IMAGE_2>`, …  
2. Cap resolution at **720p** (API).  
3. Prefer ≤3 strong refs for MVP (character, wardrobe/prop, environment).  
4. Still run identity QC — refs guide, they do not guarantee.  

## Pattern

```text
Wide shot of the alley from <IMAGE_3>. The woman from <IMAGE_1> enters holding the envelope from <IMAGE_2>.
CAMERA: locked-off then slight tilt down. ACTION: she stops and looks up.
Photoreal, match faces and prop details from references.
```

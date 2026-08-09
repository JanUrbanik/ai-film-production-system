# Shot Script — PART C

**Project:**  
**Version:**  
**Standard:** K-SHOT-SCRIPT-001  
**Max duration per shot:** 8s  

---

## Scene header template

```
SCENE N — [LOC_xxx/STATE] — time — [LOOK_xxx]
Purpose: one-line dramatic purpose
```

## Shot block template

```
SHOT:              S01-001
DURATION:          6s
REFS:              [CHAR_001], [LOC_001/DUSK]
FRAMING:
LENS:
CAMERA MOVE:
LIGHT:
ACTION:            present tense, physical only
SCREEN DIRECTION:
DIALOGUE:          none | "exact line" — delivery: ...
LIPSYNC:           YES | NO
VO SEGMENT:        line or NONE
AUDIO:
GEN_PROMPT:        natural language only — NO IDs, NO brackets
NEGATIVE:          no text, no watermark, no extra people, no distorted hands, no modern anachronisms; ...
```

**Lint:** If `GEN_PROMPT` contains `[` or `CHAR_` / `LOC_` / `PROP_` tokens → REJECT.

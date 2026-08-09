# Skill: Prompt packet assembler

## Purpose

Turn a shot card + locked bibles into one Imagine request.

**Preferred path:** If `SHOT_SCRIPT` exists, set `prompt.full_text` = **GEN_PROMPT** verbatim (already camera-clean). Do not re-author and do not inject IDs.

**Law:** `K-SHOT-SCRIPT-001` — REFS never enter the model string.

## Template (only when assembling without a frozen GEN_PROMPT)

```text
{{brief natural subject restatement — no IDs}}
FRAMING: {{framing}}. LENS: {{lens}}.
SUBJECT: {{one visible action}}.
CAMERA: {{one move}}, {{speed}}.
HOLD: match start frame and locked look; {{continuity in plain words}}.
LIGHT: {{light}}.
AUDIO: {{audio_note}}.
{{SPEECH_BLOCK if LIPSYNC — see SPEECH_PERFORMANCE_PROMPT}}
STYLE: {{grade/tone from style contract}}.

Practitioner mandatory triple: SUBJECT + CAMERA + HOLD (`GROK_AS_CAMERA`).

AVOID: {{NEGATIVE baseline + scene}}; identity drift; extra limbs; location morph.
```

## Lint (mandatory)

FAIL packet if `full_text` contains: `[` `]` or tokens `CHAR_` `LOC_` `WARD_` `PROP_` `VEH_` `ANI_` `LOOK_`.

## Mode picker

| Condition | Mode |
|-----------|------|
| Locked still must be frame 0 | i2v |
| New composition, keep IDs | r2v |
| Continue PASS tail | extend |
| Local object/wardrobe fix | edit |
| No identity (B-roll) | t2v |

## Output artifact

`03_shot_list/packets/Sxx.md` including mode, model, duration, res, ref paths, full prompt.

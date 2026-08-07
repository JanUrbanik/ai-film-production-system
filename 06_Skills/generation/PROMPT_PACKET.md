# Skill: Prompt packet assembler

## Purpose

Turn a shot card + locked bibles into one Imagine request.

## Template

```text
{{IDENTITY_BLOCK}}
{{ENV_BLOCK}}
{{PROP_BLOCK}}

FRAMING: {{framing}}. LENS: {{lens from style}}.
SUBJECT: {{one verb phrase}}.
CAMERA: {{one move}}, {{speed}}, stable subject.
HOLD: match start frame/refs; {{continuity pins}}.
AUDIO: {{audio_note}}.
{{SPEECH_BLOCK if any — see SPEECH_PERFORMANCE_PROMPT}}
STYLE: {{grade/tone from style contract}}.

Practitioner mandatory triple: SUBJECT + CAMERA + HOLD (`GROK_AS_CAMERA`).

AVOID: {{project negatives}}; identity drift; extra limbs; location morph.
```

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

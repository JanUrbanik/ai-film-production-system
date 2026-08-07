# Shot card schema

## Fields

| Field | Required | Example |
|-------|----------|---------|
| `shot_id` | yes | S07 |
| `sequence` | yes | SEQ1 |
| `beat` | yes | Offer cash |
| `location` | yes | street_curb_day |
| `zone` | no | Z1 |
| `characters` | yes | HERO:A, RIVAL:A |
| `props` | no | P01:clean |
| `framing` | yes | MCU |
| `camera` | yes | slow push-in |
| `action` | yes | she extends hand with cash |
| `dialogue` | no | "Take it." |
| `audio_note` | no | soft city bed, no score hit |
| `duration_target` | yes | 5 |
| `aspect` | yes | 16:9 |
| `resolution` | yes | 720p |
| `mode` | yes | i2v \| r2v \| t2v \| extend \| edit |
| `source_still` | i2v/edit | path or URL |
| `source_video` | extend/edit | path or URL |
| `refs` | yes if identity | paths |
| `identity_block` | yes if cast | frozen text |
| `prompt_body` | yes | assembled |
| `takes_planned` | yes | 6 |
| `status` | yes | todo/gen/pass/fail |
| `fail_reason` | if fail | hands |

## CSV header

```csv
shot_id,sequence,beat,location,characters,framing,camera,action,dialogue,duration_target,aspect,resolution,mode,status
```

## Coverage pack (dialogue beat)

For each dialogue beat, prefer:

1. Wide establish (static)  
2. Medium two-shot  
3. OTS A→B  
4. OTS B→A  
5. CU A  
6. CU B  
7. Insert if needed  

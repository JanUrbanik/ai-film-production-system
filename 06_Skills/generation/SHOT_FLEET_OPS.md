# Skill: Shot fleet ops

## Meaning
Parallelism = multiple **R8 workers** or multiple jobs, not unique agent species.

## Patterns
1. **Multi-take:** same packet, takes 01…K  
2. **Multi-shot:** different shot_ids after lock  
3. **Multi-edit branch:** concurrent edits from one source video  

## Naming
`04_gen/S07/S07_take03.mp4`  
Worker tag in log: `R8-02`

## Defaults
K=4–8 MVP; raise only if keep rate known low.

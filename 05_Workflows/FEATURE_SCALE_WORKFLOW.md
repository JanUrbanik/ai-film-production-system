# Feature / multi-act scale

Same factory as MVP. Scale **process**, not magic.

## Act structure

```text
ACT1 setup → ACT2 confrontation → ACT3 resolution
  sequences 1.n     sequences 2.n      sequences 3.n
```

Showrunner owns:

- Act goals  
- Sequence list  
- Bible version pins per sequence (look changes only when scripted)  
- Feedback loops: sequence critic → act critic → global critic  

## Parallelization rules

| Allowed | Forbidden by default |
|---------|----------------------|
| Parallel takes per shot | 4 vendors per take |
| Parallel independent shots after lock | Unlocked bible edits mid-fanout |
| Parallel video edits from one source | Silent identity changes |

## Continuity injection (operational)

For each shot packet:

1. Resolve CHAR/ENV/PROP IDs → file paths  
2. Attach frozen preambles  
3. Choose Imagine mode (I2V > R2V > extend > edit > T2V)  
4. Write packet JSON/MD beside shot card  
5. Generate → QC → only PASS enters edit bins by sequence  

## Optional advanced (not required)

- Vector DB / embeddings for ref retrieval  
- Automated visual diff  
- Multi-model routing matrix  

If added, label **Assumed/Speculative** until validated on your footage.

## Post scaled

- Assembly by sequence then act  
- Dialogue edit + beds + foley  
- Consistent grade / LUT across hours  
- Delivery: picture master, stems, full continuity report  

## Absorbed LONGFORM rules

Ported from Master Builder `LONGFORM_AI_VIDEO_CONSISTENCY_WORKFLOW.md`:

- Short clips, coverage packs, reject-heavy QC  
- Audio as continuity multiplier  
- Edit hides sin  
- One-page anti-drift rules remain law  

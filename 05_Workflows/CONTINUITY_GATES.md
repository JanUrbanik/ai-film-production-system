# Continuity gates

**Owner:** R9  
**Law:** Binary PASS/FAIL. Native “92/100” is not an Imagine output (Deprecated diagram claim).

## Gate 0 — Bible lock
- Character packs LOCKED if cast on camera  
- Env LOCKED if location established  
- Props LOCKED if hero prop on camera  
- Style contract LOCKED  

## Gate 1 — Take
Use `QC_RUBRICS.md` character/motion/world lists.

## Gate 2 — Scene
Same look IDs, light family, geography, no wardrobe teleport.

## Gate 3 — Sequence (Episode/Feature)
**Owner path:** R1b board + R9 sequence decision (`SEQUENCE_BOARD.md`).

- [ ] All timeline shots in SEQ have ≥1 PASS in `05_pass/` (or seq pass bin)  
- [ ] Beat order matches frozen sequence purpose  
- [ ] Geography continuous across scenes in SEQ  
- [ ] Look / wardrobe transitions only if scripted (ledger WEARING)  
- [ ] Screen direction / 180° holds across scene joins  
- [ ] Cost under sequence cap (`cost_ledger.csv`)  
- [ ] No unresolved FAIL with open repair  

**Binary:** Sequence PASS / FAIL. FAIL → R1b one repair cycle → escalate R1.

## Gate 4 — Global
Cast size, style contract, audio cast, Director taste.  
Feature adds **act gate** between sequence and global (R1 + R9): act goals met, look pins stable.

## Repair ladder (Director 2026-08-13 — 7 steps)

Work top to bottom. Stop at the first fix. Identity fail first.

1. Trim / cut around it  
2. Insert / OTS / coverage (only if the hero take’s face is already good)  
3. Local video edit  
4. Extend from last **good** frame  
5. Regen take (fault note: one defect + keep-list)  
6. **New start frame** (the still itself is the lie)  
7. **New `/STATE` + new VDL from the new still** (story actually changed)

**Stop rules:** two FAIL cycles on the same shot → escalate. Do not assemble around a hole.  
Adapter (chartered) is **not** a default step.

## Extend junction extra checks
- Seam morph  
- Wardrobe continuity across seam  
- Light pop  

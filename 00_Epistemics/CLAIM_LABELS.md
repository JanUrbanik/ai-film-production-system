# Claim labels (mandatory)

Every capability, score, or process claim in this system must carry one label.

| Label | Meaning | Operator action |
|-------|---------|-----------------|
| **Verified** | Confirmed from official docs, live API/console behavior, or observed project output | Safe to depend on in runbooks |
| **Assumed** | Standard production practice; fits tools but not re-proven this session | Use with QC; do not market as guaranteed |
| **Speculative** | Plausible marketing, diagram hype, or third-party rumor | Do not build gates or budgets on it |
| **Deprecated diagram claim** | Appeared in Desktop diagrams but contradicted by docs or practice | Keep only as historical note |

## Forbidden without labels

- Universal “consistency score 0–100” as if the model returns it  
- “Fool-proof” / “never drifts”  
- Claiming seed lock alone equals identity lock  
- Requiring 8–12 parallel video vendors for MVP  
- Face embeddings / vector DB as required infrastructure (optional advanced only)

## Default honesty posture

Prefer **fewer verified tools + ruthless QC** over a large aspirational model zoo.

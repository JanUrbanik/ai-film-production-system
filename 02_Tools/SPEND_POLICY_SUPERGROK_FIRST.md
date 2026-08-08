# Spend policy — SuperGrok Heavy first

**Version:** 1.0  
**Date:** 2026-08-08  
**Status:** Binding factory law (Director order)  
**Account:** Human Director — **SuperGrok Heavy** (highest consumer tier / weekly pool)

---

## 1. Hard rule

| Priority | Ledger | When to use |
|---------:|--------|-------------|
| **1 (always first)** | **SuperGrok Heavy weekly subscription pool** via consumer surfaces (`grok.com/imagine`, Grok iOS/Android Imagine) | Default for **all** stills + video while weekly pool remains |
| **2** | SuperGrok **Extra Usage Credits** / Auto Top-up on the **consumer** side (if Director enables) | Only after weekly pool is exhausted; still **not** API |
| **3 (last resort)** | **xAI API** (`XAI_API_KEY` / `api.x.ai` Imagine endpoints) | Only when Director confirms weekly pool **and** consumer Extra Credits path are exhausted or unavailable for the job |

**Never** burn API prepaid/invoice credits while SuperGrok Heavy weekly Imagine allowance remains.

---

## 2. Why (Verified product boundary)

From xAI consumer FAQ / pricing structure (**Verified** product docs as-of 2026):

1. Paid Grok plans use a **shared weekly usage pool** across Chat, Imagine, Voice, Build, etc.  
2. **Imagine on subscription** draws that pool (consumer login — not an API key).  
3. **API billing is a separate ledger.** A SuperGrok / SuperGrok Heavy subscription does **not** fund `XAI_API_KEY` Imagine calls.  
4. After the weekly pool is hit, consumer options include **Extra Usage Credits**, upgrade (N/A — already Heavy), or wait for reset — **not** silent failover to API.

**Assumed for this factory:** Director’s ~€350 SuperGrok Heavy plan is the primary Imagine budget; API is automation overflow only.

---

## 3. Operator checklist (every gen session)

Before any still or video:

- [ ] Open **Settings → Usage** on grok.com (or app) while logged into the Heavy account  
- [ ] Note **% weekly pool used**, **reset time**, product breakdown (Imagine share)  
- [ ] Confirm pool has headroom for planned takes (`takes × duration` cost intuition — pool is compute-weighted, not 1:1 seconds)  
- [ ] Set session surface = **Consumer Imagine** unless Director explicitly authorizes API  

If weekly pool is exhausted:

- [ ] Prefer wait-for-reset **or** Director-approved **Extra Usage Credits** on consumer  
- [ ] API only with explicit Director line: *“Weekly + consumer extras exhausted — API OK for this job”*  
- [ ] Log API spend separately in `09_qc_log/cost_ledger` / smoke report  

---

## 4. Surface map

| Work | Default surface | Auth | Bills |
|------|-----------------|------|-------|
| Bible stills / start frames / still edits | `grok.com/imagine` **Image 2.0 Quality** | SuperGrok Heavy login | Weekly pool |
| I2V / T2V / edit / extend | `grok.com/imagine` (video 1.5) | SuperGrok Heavy login | Weekly pool |
| Batch automation / CI / headless | API `api.x.ai` | `XAI_API_KEY` | **API credits only** |
| Grok Build agents (interactive) | Grok Build account session | Heavy login | Weekly pool (eligible Build) |
| Grok Build with API key | CLI + key | `XAI_API_KEY` | API ledger |

**Credential test:**  
- Browser/app session → consumer pool.  
- `Authorization: Bearer $XAI_API_KEY` → API ledger.  
Do not confuse a Usage tab label that says “API” with console API credits.

---

## 5. Agent / seat obligations

| Seat | Must |
|------|------|
| **R0 Director** | Own Usage checks; authorize any API spillover in writing |
| **R1 Showrunner** | Plan take counts against weekly pool; freeze gen if pool critical |
| **R8 Shot Generator** | Consumer Imagine default; no API client unless R0 unlock |
| **R9 Critic** | Reject “we used API because it was easier” without R0 note |
| **R12 Mastering** | Delivery notes list surface + ledger used |

Automation agents (Warp/Oz/Grok Build): **must not** call Imagine API by default. Prefer:

1. Produce packets + prompts + gate docs  
2. Human Director (or supervised session) runs gen in **consumer Imagine**  
3. Download assets into `08_Projects/<slug>/04_gen/`  
4. Resume QC/edit in-repo  

---

## 6. Phase B smoke implication

Phase B live pixel proof **must** prefer:

1. Real slug under `08_Projects/` (not `sim_*`)  
2. One start still via **consumer Imagine**  
3. One I2V 4–6s @ 720p via **consumer Imagine**  
4. Download to disk + `07_Outputs/IMAGINE_SMOKE_*.md`  

API smoke is **optional secondary** proof only if Director orders API path after pool exhaustion — not a substitute for subscription-first law.

---

## 7. Cost logging fields

Record per session in project `09_qc_log/` or kit `07_Outputs/`:

| Field | Example |
|-------|---------|
| `ledger` | `supergrok_heavy_weekly` \| `consumer_extra_credits` \| `xai_api` |
| `surface` | `grok.com/imagine` \| `ios` \| `android` \| `api.x.ai` |
| `usage_before_pct` | 42 |
| `usage_after_pct` | 55 |
| `reset_at` | ISO time from Settings → Usage |
| `api_authorized_by` | empty unless ledger=`xai_api` |

---

## 8. Forbidden

- Defaulting scripts to `XAI_API_KEY` “because agents can curl”  
- Claiming SuperGrok Heavy “includes API Imagine”  
- Mixing ledgers in one cost line without labels  
- Continuing volume gen when Usage shows pool exhausted without Director choice (wait / extras / API)

---

## 9. Related

- `01_Architecture/ONE_PAGE_FACTORY_LAW.md`  
- `02_Tools/adapters/GROK_IMAGINE_ADAPTER.md`  
- `02_Tools/GROK_IMAGINE_CAPABILITY_MATRIX.md`  
- `05_Workflows/PRODUCTION_DEPLOY.md`  
- `HANDOFF.md`  
- Consumer Usage FAQ: https://docs.x.ai/grok/faq  
- Pricing surfaces: https://x.ai/pricing  

---

## Document control

| Ver | Date | Notes |
|-----|------|-------|
| 1.0 | 2026-08-08 | Director order: Heavy weekly pool first; API last resort |

# Store Leads — Keep-List (strong-store monitor feed)

**Purpose (Marina, S2→S3):** accumulate the STRONG / borderline stores we find (65+, 55–64, and
genuinely-interesting browse picks) so we can later load them into a **"newest-products-first" monitor**
(ShopHunter OR another service) and check every 2–3 days what NEW products these proven operators launch
→ catch future winners early. **Store Leads = the store-supplier for that monitor.**

**Mechanism:** the master record (`logs/storeleads/processed_domains.json` on the VPS) carries a `monitor: true`
flag per store. `sl_mark_processed.py` sets it (proxy-score gate); the main agent confirms/edits it at the
checkpoint (a founder-Watchlist or a real borderline → `monitor: true`). This file is the human-readable
running export of those flagged stores. The monitor JOB itself is DEFERRED (lives in ShopHunter, parked) —
here we only FEED the list.

**Discipline:** add a store here when it's a genuine strong/borderline find (not trade/commodity filler).
Dedupe by domain. Note WHY in 4–5 words. Keep clickable.

---

## Monitored stores

| Date | Store | Score | Class | Why keep (monitor for new launches) |
|---|---|---|---|---|
| 2026-06-01 | [muravai.co](https://muravai.co) | 77 | filtered showerhead (Beauty) | Consider; proven filter-niche, hair angle open — watch what they launch next |
| 2026-06-01 | [us.thecoldpod.com](https://us.thecoldpod.com) | 64 | ice bath (Fitness) | Consider; study; single-product DTC — watch their next drops |

---

## How to add
One row per kept store: `Date · [domain](https://domain) · score · product_class · why (4–5 words)`.
Also set `monitor: true` in `processed_domains.json` (via `sl_mark_processed.py --monitor-min` or by hand at checkpoint).

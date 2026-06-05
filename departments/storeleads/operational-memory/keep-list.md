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
| 2026-06-01 | [muravai.co](https://muravai.co) | 77 | filtered showerhead (Beauty) | Watchlist; proven filter-niche, hair angle open — watch what they launch next |
| 2026-06-01 | [us.thecoldpod.com](https://us.thecoldpod.com) | 64 | ice bath (Fitness) | Watchlist; study (premium-look/low-price) — watch their next drops |
| 2026-06-01 | [izimini.com](https://www.izimini.com) | 57 | outdoor baby chair (Kids) | Consider; stylish + strong seasonal hook — watch new outdoor SKUs |
| 2026-06-01 | [dingledanglebaby.com](https://www.dingledanglebaby.com) | 60 | diaper-change distractor (Kids) | Consider; fun/novel family-bonding — Shark Tank brand, watch new toys |
| 2026-06-01 | [joseat.com](https://joseat.com) | 68 | cart/high-chair cover (Kids) | Consider; clear hygiene pain — watch new covers/accessories |
| 2026-06-01 | [wildridecarrier.com](https://wildridecarrier.com) | 70 | toddler hip carrier (Kids) | Watchlist; beautiful design brand in saturated niche — watch their drops |
| 2026-06-01 | [waterlandbaby.com](https://www.waterlandbaby.com) | 72 | water+land carrier (Kids) | Watchlist; clever water positioning — watch how they extend the line |
| 2026-06-01 | [petiteisland.com](https://www.petiteisland.com) | 77 | pocket fetal doppler (Health) | S4 winner; doppler convergence w/ approved WellnessBaby (83); watch new SKUs |
| 2026-06-01 | [kindersensebaby.com](https://kindersensebaby.com) | 73 | crib safety tent (Kids) | S4 winner; real safety-pain solver; watch their next launches |
| 2026-06-05 | [yogorgeous.com.au](https://yogorgeous.com.au) | 53 | anti-roll changing mat (Kids) | S8 founder-kept Watchlist; WriggleBum-category diaper-change pain — study |
| 2026-06-05 | [babymarstore.com](https://babymarstore.com) | 60 | RockaBaby stroller rocker (Kids) | S8 convergence → Rockit SL2; watch deep-tail clones of proven mechanism |

---

## How to add
One row per kept store: `Date · [domain](https://domain) · score · product_class · why (4–5 words)`.
Also set `monitor: true` in `processed_domains.json` (via `sl_mark_processed.py --monitor-min` or by hand at checkpoint).

# Hypothesis — Niche store-first discovery at scale (Store Leads)

> **STATUS: ACTIVE (the founding direction).** Pilot-validated chain 2026-05-30; still calibrating.

## Idea (Marina, 2026-05-30)
Replicate the ShopHunter system, but on Store Leads' much larger universe (~2.88M active Shopify):
pick a niche → set WIDE filters that don't over-cut → dump all matching stores → analyse EVERY store
(nothing lost) with a live site visit for finalists → score → report 65+ / 55–64 / interesting links.
Goal of the first month = build + harden the chain on real niches, not chase a specific winner.

## Locked starting filters (Marina-approved 2026-05-30)
- Platform = Shopify · Status = Active
- Country ∈ US, UK, DE, CA, AU, NZ (query per-country, merge — multi-cc AND bug)
- Created ≥ 2020 (a store made years ago may only now be testing a product — don't lose it)
- Avg product price $0–350 (wide; confirm real hero price on the site)
- Avg product weight ≤ ~1.5 kg (cut bulky — when the weight filter is wired server-side)
- Est. revenue $0–$1M/month (from zero — catch emerging $10k stores)
- FB-Pixel filter OFF for now (data incomplete; try later to see how much it cuts)
- Exclude niches we won't sell (apparel/clothing; others TBD)

## To calibrate / build next
- Crack **sort** (Created↓ / Est Sales↑) to fish emerging white-label instead of rank-top brands.
- Crack server-side **range filters** (price / weight / created / revenue band `erb`).
- Multi-country merge in the dumper.
- Stage-1 **table / fields** design with Marina (on the 200 pilot).
- **Saved Lists + weekly-email** monitoring of new stores/products on a saved filter.
- Optional **ShopHunter** enrichment for top finalists (per-product revenue) — validate hit-rate first.
- Niche rotation; record niche-yield facts (like ShopHunter) without closing niches.

## Open questions to test
1. Exact "search" accounting vs the ~2000–4000/mo quota (per query vs per page) — check the in-app counter.
2. How deep can we paginate within the 25k/query ceiling, and best segmentation for >25k niches.
3. Revenue-estimate accuracy: Store Leads `erf` vs live reality vs ShopHunter.
4. Which sort surfaces the best white-label pool (Created vs Est-Sales-asc vs social-growth).

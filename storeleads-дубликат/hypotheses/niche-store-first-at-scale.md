# Hypothesis — Niche store-first discovery at scale (Store Leads)

> **STATUS: ACTIVE (the founding direction).** Pilot-validated chain 2026-05-30; still calibrating.

## Idea (Marina, 2026-05-30)
Replicate the ShopHunter system, but on Store Leads' much larger universe (~2.85M active Shopify):
pick a niche → set WIDE filters that don't over-cut → dump all matching stores → analyse EVERY store
(nothing lost) with a live site visit for finalists → score → report 65+ / 55–64 / interesting links.
Goal of the first month = build + harden the chain on real niches, not chase a specific winner.

## Locked starting filters (Marina-approved 2026-05-30)
- Platform = Shopify · Status = Active
- Country ∈ US, UK, DE, CA, AU, NZ (query per-country, merge — multi-cc AND bug)
- Created ≥ 2020 (a store made years ago may only now be testing a product — don't lose it)
- Avg product price $0–350 (wide STORE-LEVEL filter — keep the box; not the same as the PRODUCT band below)
- Avg product weight ≤ ~1.5 kg (cut bulky — when the weight filter is wired server-side)
- Est. revenue $0–$1M/month (from zero — catch emerging $10k stores)
- FB-Pixel filter OFF — and demoted to CONTEXT, not a selection criterion (data not always correct; Marina S2)

> **Two different price numbers — don't confuse them (S2 clarification):** the **$0–350 above** is the *store's
> average* product price, a WIDE Stage-1 filter just to keep the box in play. The **product RETAIL band** we
> actually score against is **preferred $45–79 / acceptable $39–100 / premium $100–170 (margin-penalty) / >$170 = out**
> (`core/scoring-system.md` + `methods/subagent-spec.md`). A $300-avg store can still hold a $69 golden product.
- Exclude niches we won't sell (apparel/clothing; others TBD)

## To calibrate / build next
- ✅ DONE (2026-05-31): advanced **`bq`** query — Created≥2020 server-side + multi-category OR +
  25k-ceiling bypass via created windows (no server sort needed; client-sort by Est Visits).
- ✅ DONE: category census + green shortlist; Stage-1 **table / fields** agreed with Marina + live-verified.
- Multi-country merge in the dumper (pilot is US-only for now).
- **Saved Lists + weekly-email** monitoring of new stores/products on a saved filter.
- Optional **ShopHunter** enrichment for top finalists (per-product revenue) — validate hit-rate first.
- Niche rotation; record niche-yield facts (like ShopHunter) without closing niches.

## Open questions to test
1. Exact "search" accounting vs the ~2000–4000/mo quota (per query vs per page) — check the in-app counter.
2. ✅ Answered: >25k niches segmented via `bq` created windows (each <25k), paginate+merge (HI 27,052 exact).
3. Revenue-estimate accuracy: Store Leads `erf` vs live reality vs ShopHunter.
4. Which sort surfaces the best white-label pool (Created vs Est-Sales-asc vs social-growth).

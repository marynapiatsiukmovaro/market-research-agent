# Hypothesis — Store Leads as a BREADTH store-source ($75) feeding our funnel

> **STATUS: HYPOTHESIS — UNTESTED. To validate in a future session.** NOT a committed strategy, NOT a pivot,
> NOT a rule. Recorded so the idea is not "new" when Marina raises it. Discussed SH-10 wrap (2026-05-27);
> builds directly on the **SH-8 breadth-tool idea** (learnings.md SH-8: "bottleneck #1 = traction-biased tracked
> subset misses emerging stores → fix = a breadth tool ~millions of stores; pair it with ShopHunter as the deep layer").

## Core idea
Use **Store Leads (storeleads.app) Premium = $75/mo** as a new STORE-SOURCE (the "universe") and run our
**existing source-agnostic funnel** on the stores it returns. Either **paired with ShopHunter** or **standalone**.

**Why:** ShopHunter's ~800/category is its TRACKED inventory-depletion subset → misses emerging/early-window stores.
Store Leads indexes the whole Shopify(+1 platform) universe, filterable by category / rank / price / growth.

## Method = SAME as ShopHunter; only Stage-0 (the source) changes
Our funnel is platform-agnostic: `dump → conservative cut → ENRICH from the LIVE site (real catalog/price) → deep-score`.
The live-enrich step (sh_enrich_final.py) already exists and only needs a **store domain** — which any source provides.
- **NEW Stage-0** = harvest a filtered store list from the Store Leads UI (scrape like sh_cat_dump.py — export NOT needed).
- Everything downstream (cut → live enrich → 100-pt deep-score + Marina Veto) is **reused as-is.**

**Store Leads filters to use (stronger than ShopHunter's):** Platform=Shopify → Category → Country=US/target →
Active/Rank → **Average Product Price** band ($45–79) → **Average Product Weight** (cut bulky) →
**Followers growth 30d** + **Creation Date (weekly)** + **Last Plan Change** (= emerging / fast-rising = early window).
The video example (category → ~13K stores → +Shopify → +Active → ~4K) = exactly this Stage-0 pre-qualification.

## Two modes
- **PAIRED with ShopHunter (preferred, = the SH-8 vision):** Store Leads finds the quality/growing stores →
  load them into ShopHunter (tracked collections) → ShopHunter adds what Store Leads-$75 lacks: per-product
  revenue (Top Products) + **Newest-First new-launch monitoring**. On a CURATED quality base, Newest-First finally
  becomes high-ROI (it was low-ROI on ShopHunter's mediocre default set).
- **STANDALONE (also viable):** run the funnel directly on Store Leads domains. Live-enrich gives real catalog +
  price; the only gap = the "which product is the hero" revenue signal (Store Leads **Product Search = Elite $450 only**)
  → derive hero from live-catalog signals (featured / best-seller collection / product order / review count) OR get it
  from Dropship.io / WinningHunter (they have per-product sales).

## Cost logic (Marina, SH-10)
$75 Premium is enough — export ($250 Pro) replaced by our scraper; "2000 searches/mo" is plenty (~50/page, paginated).
**$75 Store Leads + ~$50 ShopHunter = $125/mo = acceptable**; $450 Elite = too much for now. Upgrade only if June ROAS pays back.
**Cheapest validation FIRST:** Dropship.io **7-day free trial** (export included + per-product sales + FB ad-spend) to test the
multi-source model at $0 before paying $75.

## Honest trade-offs / risks
- Store Leads-$75 has **no per-product revenue** → "which product is the winner" signal weaker than ShopHunter (hence the pairing).
- Revenue filtering is via **Rank / Platform Rank + Avg Price** (no direct $ slider); estimated_sales exists as a field (sort post-harvest).
- **ToS/ban risk = LOW, not legal:** scraping the UI on a no-export tier can breach ToS → at most account suspension if detected;
  mitigate with gentle human-pace + own account + internal-use-only (same discipline as ShopHunter). A 3rd-party "Storeleads Scraper"
  exists on Apify → it's a known pattern (they may rate-limit) → stay gentle.

## Open questions to TEST (before committing)
1. Store Leads Premium UI — are result lists FULL (not a capped preview)? How deep can we paginate/harvest?
2. What exactly counts as a "search" toward the 2000/mo quota (1 query vs 1 page)?
3. ShopHunter "Add Shop" capacity — can we load thousands of Store-Leads stores into tracked collections, and how fast do data populate?
4. Is STANDALONE enough, or is the ShopHunter pairing materially better (hero/newest signal)?
5. Revenue-estimate accuracy: Store Leads vs ShopHunter vs live reality.

## Next step when activated
Dropship.io 7-day trial (validate model, $0) → Store Leads $75 1-day harvest verification → if good, June = full breadth run + product launches → July decide scale.

> Review/expire: revisit when Marina activates a Store Leads (or Dropship.io) trial. Until tested, treat as a directional hypothesis only.

# RESEARCH SOURCES

> **What this file is:** a channel-agnostic reference for how to READ each signal type.
> It does NOT set which sources to scan — **active discovery is per-department** (FB Ads
> Library keyword scan in `departments/facebook-ads-library/`; ShopHunter store-first in
> `departments/shophunter/`). Read your department's `workflow.md` for the live pipeline.

## Department primary surfaces
- **Facebook/Meta Ads Library** — competitor ad spend = market validation (FB dept's surface)
- **ShopHunter** — Shopify store revenue / longevity / multi-store demand (ShopHunter dept's surface)

## Other signal types (corroboration — what each one means)
- TikTok Ads Library — active ad spend = market validation signal
- Amazon Movers & Shakers — real demand signal, rank velocity
- AliExpress Trending / New Arrivals — sourcing + demand overlap
- TikTok Organic — #tiktokmademebuyit, trending products, viral demos
- Instagram Reels trending — cross-platform demand signal
- Alibaba — sourcing verification, supplier count, MOQ
- Temu trending — early commodity signal (if on Temu, margin is squeezed)
- Pinterest trending — lifestyle product signals
- Reddit (r/shutupandtakemymoney, r/BuyItForLife) — genuine consumer demand
- Etsy trending — handmade/custom product ideas that can be industrialized

## Supplementary Tools
- Google Trends — saturation and longevity check
- AdSpy — paid ad intelligence (if access available)
- Viral product trackers (Ecomhunt, Dropispy) — if access available

## Signal Evaluation Logic (channel-agnostic)

*Active source priority is determined by the department workflow, not globally — see `departments/{dept}/workflow.md`. This section evaluates what each signal type means, not which sources to scan first.*

1. Active ads on Meta/TikTok = someone is spending money = market exists
2. Amazon momentum = real demand beyond ad-driven
3. TikTok organic = early signal before saturation
4. AliExpress volume = sourcing feasibility confirmed

---

## Facebook Ads Library — Keyword Strategy

### Good keywords (yield direct brand advertisers)
- Category-specific: "travel pillow", "car organizer", "posture corrector", "massage gun"
- Product-specific: "neck massager", "desk organizer", "compression sleeve"
- Feature-specific: "wireless", "portable", "foldable", "waterproof"
- Problem-specific (product-level): "neck pain relief", "back support", "car clutter"

### Bad keywords for WebSearch-based discovery
- Broad emotional phrases: "struggling with", "tired of", "finally", "sick of"
- Via WebSearch these attract: debt programs, weight loss apps, clinical studies, online courses
- For WebSearch: avoid unless combined with a product word (e.g. "tired of neck pain" instead of "tired of")

**Note — FB Ads Library VPS:** In direct FB scraping these phrases were tested as "performance advertising signal keywords" (filter by advertiser TYPE, not topic). **Verdict after Sessions 15–20:** broad performance/emotional phrases mostly produced noise — current approach favors product-specific / concrete-object keywords. Full keyword verdicts + Meta Rules: `departments/facebook-ads-library/operational-memory/keyword-map.md` (Scorecard). The closed broad-horizontal queue is archived in `archive/keyword-map-archived-S15-20-queue.md`.

### Amazon Affiliate Ads — New Rule (updated 2026-05-13)
Two types of Amazon affiliate ads — treat differently:

SKIP (pure noise):
- Ad copy contains "comment [WORD] and I'll DM/send you the link"
- Advertiser name contains "with Amazon.com" / "with Amazon Associates"
- Store URL is markable.ai or amzlink.to

KEEP and EXTRACT (product signal):
- Ad shows a SPECIFIC named product or feature ("This corn stripper removes kernels in 3 seconds")
- Someone is paying for Facebook ads to promote it → product converts on Amazon
- Extract product name → search Amazon → check price + reviews → evaluate as candidate
- Amazon is just a sales platform — if it sells there, it can sell on your Shopify too

### Facebook Ads Library URL Filters
Available parameters to combine with keywords:

| Parameter | Usage | Effect |
|-----------|-------|--------|
| `country=US` | Always | US market only |
| `active_status=active` | Always | Running ads only |
| `media_type=video` | Optional | Video ads only — better for demo products |
| `start_date[min]=2026-01-01` | Recommended | Only new entrants — less saturated |

Usage: add --since=2026-01-01 to scraper command to filter fresh ads only.

### Scraper Modes (Facebook Ads Library VPS — current)
- Standard: **500 ads/keyword** target, hard cap 600 — never exceed (see op-rules.md RULE 5)
- Scale by adding more keywords (breadth), not going deeper on one keyword
- Early abort: if initial batches show 70%+ services/apps with 0 physical products → replace keyword

*Pre-VPS historical reference (Sessions 1–6, now obsolete): Wide = 3–6 keywords × 25 ads; Deep = 150–200 ads/keyword.*

---

## Current operational notes (retained from archived capability map)

- **Marina's core rule (ad longevity = market proof):** "Если реклама работает 2 недели подряд — продукт КОНВЕРТИТ." An ad running 14+ days straight = someone is profiting = market validated by another advertiser's budget. ≥7 days = interesting, ≥14 = strong.
- **Store-link check before reporting (mandatory):** always WebFetch the store URL before reporting. Opens cleanly → OK. Redirect/error → verify manually. Chrome Safe-Browsing "dangerous site" flag → REJECT immediately (lesson: beambo.com).
- **Meta Ads Library access:** via VPS scraper (Mikhail Piatsiuk session) — full setup in `departments/facebook-ads-library/operational-memory/op-rules.md`.

> Full legacy capability maps (Minea / WebSearch / WebFetch / TikTok / Amazon detailed specs, Session-2 evaluation, pre-FB backlog) archived to `archive/sources-overview-capability-map.md` (S30 cleanup; see the Minea verdict note there — do not return). Discovery is per-department (FB Ads Library + ShopHunter); those tools are not in the current pipeline.

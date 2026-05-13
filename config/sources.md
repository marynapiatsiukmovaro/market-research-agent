# RESEARCH SOURCES

## Primary Sources (check daily)
- TikTok Ads Library — active ad spend = market validation signal
- Facebook/Meta Ads Library — competitor spend confirmation
- Amazon Movers & Shakers — real demand signal, rank velocity
- AliExpress Trending / New Arrivals — sourcing + demand overlap
- TikTok Organic — #tiktokmademebuyit, trending products, viral demos
- Instagram Reels trending — cross-platform demand signal

## Secondary Sources (check when needed)
- Alibaba — sourcing verification, supplier count, MOQ
- Temu trending — early commodity signal (if on Temu, margin is squeezed)
- Pinterest trending — lifestyle product signals
- Reddit (r/shutupandtakemymoney, r/BuyItForLife) — genuine consumer demand
- Etsy trending — handmade/custom product ideas that can be industrialized
- ShopHunter — Shopify store revenue validation

## Supplementary Tools
- Google Trends — saturation and longevity check
- Minea / AdSpy — paid ad intelligence (if access available)
- Viral product trackers (Ecomhunt, Dropispy) — if access available

## Source Priority Logic
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

### Bad keywords (yield services, apps, supplements — not physical products)
- Broad emotional phrases: "struggling with", "tired of", "finally", "sick of"
- These attract: debt programs, weight loss apps, clinical studies, online courses
- Avoid unless combined with a product word (e.g. "tired of neck pain" instead of "tired of")

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

### Scraper Modes
- Default (Wide): 3-6 keywords × 25 ads = broad category discovery
- Deep mode (--deep): 1-2 keywords × 150-200 ads = full category map
  - Use Deep when: category already identified as hot (e.g. travel pillow had 7 brands)
  - Use Wide when: exploring new session, unknown categories

# Store Leads — Capabilities

## Part 1 — What we already do (inherited from core/ + shared/)
Score a product 0–100 + Marina Veto (`core/scoring-system.md`) · hard-reject (`core/mandatory-filters.md`) ·
founder bar (`core/founder.md` + `shared/founder-taste.md`) · deep-validate 85+ (`shared/product-validation.md`) ·
report to Notion + logs (`shared/notion-workflow.md`, `shared/reported-products.md`, `shared/rejected-products.md`) ·
analysis skills (`shared/skills/`). The moment we SEE a product, we can filter, score, validate, report it.

## Part 2 — What Store Leads exposes (mapped 2026-05-30)
**Universe:** ~3.63M domains; ~2.88M **active Shopify** (our pool). Weekly DB refresh.

**Discovery = internal JSON API** (`/json/auth/domains`), driven via the logged-in session
(see `methods/interface-guide.md`). 50/page, cursor pagination, 25k results/query ceiling.

**Store-level data IN the search result (no site visit needed for Stage-1):**
domain · merchant · title · meta-desc · category (Google taxonomy) · country/region/city ·
**est. revenue $/month + $/year** · **avg / min / max product price** · product count ·
**store created date** · Shopify plan tier · reviews (count + rating, TrustPilot) ·
**most-recent published product (image + date)** · installed apps · tech stack (incl. **Facebook
Pixel**) · features · social links (FB/IG/TikTok) · social followers + 30-day growth · employees · rank.

**Filters (facets):** category (cat/cat1) · country · **est-revenue band** (`erb`: <$50k … $5m+/mo) ·
**created date** (month/week — emerging stores) · Shopify plan · **installed apps** · **technologies**
(e.g. Facebook Pixel = advertises) · features · language · currency · region/city · employees · TLD ·
theme · sales channels · ships-to · **avg product price** · **avg product weight** (cut bulky).

**Sort:** Estimated Sales · Avg Product Price (USD) · Created · Product Count · Est Visits/PageViews ·
Rank · Platform Rank · TikTok/Instagram/Pinterest/YouTube followers + 30d % · TrustPilot · Monthly App
Spend · Last Plan Change · Employees · Theme Cost. *(Filter/sort param encoding partly cracked — see interface-guide.)*

**Saved Lists + weekly email** on a saved filter = the monitoring layer (to wire later).

## vs ShopHunter (key differences)
| | ShopHunter | Store Leads (Premium $75) |
|---|---|---|
| Universe | ~800/category tracked subset | ~2.88M active Shopify, filterable |
| Data in result | open every store | almost all store-level data in the dump |
| Revenue | per-PRODUCT (Top Products) | per-STORE ($/mo + $/yr); **no per-product** |
| Filters | category + basic | revenue band, created, avg price/weight, apps, tech, social-growth |
| Emerging stores | weak (mature subset) | strong (Created + social-growth sorts) |
| Hero product | given (Top Products) | derive from live catalog (best-selling collection) |

## Gaps / limits (Premium $75)
No per-PRODUCT revenue (= Elite $450 Product Search) → hero via live catalog. No CSV export / API /
workflow (Pro+) → internal session-API, stay gentle. ~2000–4000 searches/mo. 25k results/query ceiling.
Multi-country must be queried per-country (AND bug). Sort/range-filter encoding still being cracked.

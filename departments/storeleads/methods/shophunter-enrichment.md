# Store Leads — Optional ShopHunter Enrichment (cross-department resource)

> **What this is:** ShopHunter used as an OPTIONAL external enrichment for Store Leads **finalists** — it adds
> per-PRODUCT revenue + a competitor landscape that Store Leads (per-STORE only) cannot give. **Not a gate, not a
> routine step** (Marina: "вернёмся, продумаем как встроить"). Run it on a small finalist set when useful.
>
> **Isolation:** we read ShopHunter's **methods** (this lookup mechanic) as a resource ONLY. We do NOT read
> ShopHunter's operational-memory (its learnings / founder-feedback). Mapped during the 2026-05-31 Store Leads session.

## Access
- ShopHunter on the VPS: `cookies/shophunter.creds` (gitignored, set via `scripts/set_shophunter_creds.py`,
  interactive getpass — never in chat) + persistent profile `cookies/shophunter_profile`. Login: `scripts/shophunter_login.py`.
- For a NEW account: back up + remove the old `shophunter_profile` so login is clean (don't inherit the old session).

## The lookup mechanic (cracked 2026-05-31 — `scripts/sh_store_lookup2.py`)
Two non-obvious traps — both must be handled or you get false matches:
1. **Type, don't fill.** `inp.fill()` does NOT trigger the SPA's reactive search. Use `click → type(delay) → wait →
   Enter` on the **visible** "Search Shops" input (there are 2 inputs; one is hidden).
2. **Verify the domain.** The Explore page keeps a **default shop card** (e.g. zentrumflow) when a search returns
   nothing → grabbing the first `/shops/{id}` link gives a FALSE match. **Open the result and confirm its shown
   domain contains the query core** before accepting (RULE 3 — no coverage claims from "not found").
- **Search terms that work:** brand-words (`stoov`) and bare domain (`stoov.com`). A **full URL** (`https://www.…`)
  returns only the junk default set — don't use it.
- Ladder per finalist: `brandwords → bare domain`; verify each opened shop's domain; else NOT_FOUND.

## Hit-rate reality (measured)
On the first 16 Store Leads finalists: **4/16 found (25%).** ShopHunter tracks an established subset — most emerging
Store Leads gems are NOT in it (this is exactly why Store Leads exists). So: enrich the ones SH covers; absence in SH
is NOT a negative signal about the store.

## What to pull (the SH columns worth adding)
From `/shops/{id}`: Revenue **Day/Week/Month + trend %** · Store Creation Date · SKU count · Tracked-by-N ·
**Top Revenue Producers (per-PRODUCT revenue — the real hero + $)** · Top Advertised Products · **Competitor Analysis**
(rival stores + their revenue = free niche landscape; this is where convergence clusters surface, e.g. composting-toilet
players each ~$1M/mo). Always treat revenue as an ESTIMATE — corroborate (cross-check vs Store Leads `erf`; they
matched for Stoov $314k≈$332k but diverged for CompoCloset $344k vs $1M).

## Notion (when a finalist WAS found in ShopHunter)
Fill the existing **SH fields** for that product: `SH Link` · `SH Store Created` · `SH Rev W/M` · `SH SKU/Country`
(these columns exist in Product Tracker). Leave blank when not found. (These are the same fields the ShopHunter
department uses — cross-dept reuse for an SL product we enriched via SH is fine; flag it in Notes.)

# Store Leads — Session Learnings

Short-lived tactical discoveries. Read at session start. Permanent rules → op-rules (once it
exists); company logic stays in core/. Append with expiry; archive expired (never delete) per RULE-15.

---

## HANDOFF → NEXT SESSION (read first)

**✅ DAY 1 DONE (2026-05-30) — department bootstrapped + full chain validated end-to-end on a 200-store pilot (US Kitchen & Dining).**

**State:**
- **Access solved:** passwordless email-code login → `cookies/storeleads_state.json` + `storeleads_profile` on VPS. Re-login: `scripts/sl_email_login.py` (Marina enters email + emailed code). Verify: `sl_check_login.py`. Plan = Premium $75 (2 platforms, ~2–4k searches/mo, no export/API).
- **API mapped + filters cracked:** POST `/json/auth/domains`, `f:<field>` filters (p=platform, ds=status, cc=country, cat/cat1=category), pagination key `cursor`, 25k/query ceiling. ⚠️ multi-country comma = 0 (AND bug) → one country/query + merge. Sort + range-filter encoding NOT yet cracked.
- **Chain ran:** `sl_dump.py` (13,335 US K&D → client-filtered to 200 survivors: created≥2020, rev≤$1M/mo, price≤$350) → `sl_enrich2.py` (200, 196 reachable, real hero from best-selling collection) → real Stage-3 deep-score (read all, hero-confirm via WebFetch, 100-pt + Veto).
- **Pilot yield (modest, as expected):** 1 report-worthy ~70 = **Rolling Knife Sharpener TYPE** (tumblerware.com; branded/premium → white-label the type). Borderline 55–64: GrillGun torch (grillblazer, ad-policy risk), Anytongs (Shark Tank), self-heating mugs Nextmug+OHOM (×2 convergence but везде), Matsato knife. **Nothing written to Notion** (awaiting Marina; honest near-0 winner pass — normal store-first result + chain-training run).
- VPS outputs: `logs/storeleads/` — `kd_us_raw.json`, `kd_us_survivors.json`, `kd_us_enriched2.json`, sentinels, screenshots, `full_*.json` (API captures).

**KEY LEARNINGS (see Active Learnings below):** (1) Stage-3 must be real (no eyeballing proxy tiers); (2) rank-sort surfaces biggest=brands → sort by Created↓/EstSales↑ to fish white-label; (3) hero must be confirmed on live site; (4) K&D @ this band = brand/catalog-heavy.

**NEXT SESSION (Marina returns to this chat):** continue building — (a) crack **sort param** (Created↓ / Est Sales↑) + range filters; (b) calibrate the **Stage-1 table / fields** with Marina on this 200; (c) re-run a deeper pull (emerging white-label); (d) decide table structure; later: saved-filter weekly monitoring, optional ShopHunter enrichment, then compact + register department in CLAUDE.md/README. Department NOT yet registered in CLAUDE.md (intentional — finalize structure first).

---

## Active Learnings

### [2026-05-30] DAY 1 — Store Leads = clean internal JSON API behind a Shadow-DOM SPA
**Type:** Tactical / Pattern | **Severity:** HIGH | **Confidence:** HIGH (live)
**Observation:** Dashboard text is empty (Vaadin shadow DOM) — judge screenshots. But `/json/auth/domains`
returns rich store-level data (revenue/price/created/reviews/FB-pixel/newest-product) per result → Stage-1
needs NO site visit; only finalists get a live hero-confirmation. Filters = `f:<field>`; pagination `cursor`;
25k/query ceiling; multi-country = AND bug (query per country). **Applies to:** every run. **Expires:** Never → op-rules.

### [2026-05-30] DAY 1 — Stage-3 discipline: never eyeball the proxy A/B/C tier
**Type:** Warning / Correction | **Severity:** HIGH | **Confidence:** HIGH (Marina caught it)
**Observation:** First Stage-3 attempt read the enricher's A/B/C revenue-tier and editorialised scores →
unreliable "no winner". The enricher tier is a revenue/price SORT-AID, not quality. Real Stage-3 = read ALL,
confirm the hero on the live site (enricher mis-picks: bundles; SUSTEAS list implied a grill but the bestseller
was a $33 grater), run 100-pt + Marina Veto, lead with WOW/taste. **Applies to:** every Stage-3. **Expires:** Never → op-rules.

### [2026-05-30] DAY 1 — Pool/sort + niche-yield (Kitchen & Dining)
**Type:** Pattern / Yield fact | **Severity:** MEDIUM | **Confidence:** MEDIUM (1 niche, 1 run)
**Observation:** Default **rank sort surfaces the BIGGEST stores = established brands** → emerging white-label
sits deeper and was under-represented in the first 200. K&D @ rank-sort + $100k–1M = cookware/dinnerware/glass/
knife-collector/decor/food brands + catalog stores dominate; few impulse white-label gadgets, those branded/premium/
saturated (self-heating mug ×2 = convergence but везде). **Fix:** sort by Created↓ / Est Sales↑ (crack the param).
Tier-1 yield fact — do NOT close the niche or add a filter; keep scoring as-is. **Applies to:** niche selection + sort.
**Expires after:** revisit once sort is cracked + a Created-sorted pull is run.

---

## Expired / Promoted
(none yet)

## How to add a learning
```
### [YYYY-MM-DD] Session — [Title]
**Type:** Pattern / Warning / Signal / Tactical | **Severity:** … | **Confidence:** …
**Observation:** … **Applies to:** … **Expires after:** Session N (or "Never" → op-rules)
```

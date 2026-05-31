# Store Leads — Session Learnings

Short-lived tactical discoveries. Read at session start. Permanent rules → op-rules (once it
exists); company logic stays in core/. Append with expiry; archive expired (never delete) per RULE-15.

---

## HANDOFF → NEXT SESSION (read first)

**▶ DAY 2 (2026-05-31) — STRATEGY / SYSTEM-BUILD session (in progress).**
- **Filter architecture LOCKED (Marina-agreed):** server-side = MINIMAL term filters only — **Platform=Shopify, Status=Active, Category, Created≥2020**. Everything else (price, revenue, weight, Est Visits/PageViews, sort, ranking) = **CLIENT-SIDE** on the dumped rows. **Why:** any field-filter silently drops stores with no data (proven: 400,222 / 2.85M active Shopify have category=None → category filter alone drops ~14%; sparse fields drop far more). Marina confirmed the same effect in the UI.
- **25k-results/query ceiling** beaten by segmentation: `f:cratyyyymm="YYYY-MM"` (exact month) WORKS → dump month-by-month for big subs; or created-window via `bq` (below). For counting, the cratyyyymm FACET returns ALL 114 months (other=0) → exact ≥2020 sums.
- **CENSUS DONE (validated vs live UI: K&D = 29,150 exact match).** GREEN shortlist = 12 subcats, **≈196k naive / ~180k unique ≥2020**: HG Kitchen&Dining 29,150 · Home Improvement 27,052 · Bed&Bath 19,088 · Gardening 15,727 · Home Appliances 15,038 · Nursery&Playroom 6,729 · Cleaning 5,868 · Home Safety&Security 991 · Pets PetFood&Supplies 42,610 · Dogs 21,909 · Cats 4,569 · Health Oral&Dental 7,390. YELLOW subs deferred (Marina marked them for later). Census scripts (active): `sl_subtree.py` (full L2 tree) + `sl_count.py` (exact ≥2020 per sub).
- **`bq` FULLY CRACKED (2026-05-31) — it is a Bleve query DSL, passed as a JSON *string* in the POST body key `bq`.** Server error confirmed type=string ("unmarshal object into ...bq of type string"). Format validated to-the-store vs live UI (K&D=29,150; HI=27,052):
  - Container: `bq = json.dumps({"must":{"conjuncts":[ ...query objects... ]}})` (NOT `operator/value` — that was wrong).
  - Platform: `{"field":"p","term":"1"}` · Status: `{"field":"ds","term":"1"}` (term, ids as strings).
  - Category EXACT: `{"field":"cat","match":"<full path>"}` — **`match`, not `term`** (term→0). Path e.g. `/Home & Garden/Kitchen & Dining`.
  - Multi-category **OR** (= the "Show more" checklist / Operation:Or): wrap a disjunction as one conjunct → `{"disjuncts":[{"field":"cat","match":A},{"field":"cat","match":B}]}`. Verified (K&D+HI≥2020 = 55,993).
  - **Created ≥2020** (range): Bleve **TermRange on `cratyyyymm`** → `{"field":"cratyyyymm","min":"2020-01","inclusive_min":true}` = **29,150 exact**. (createdAt/crat as RFC3339 = ignored or 0; only cratyyyymm string-range works.)
  - **25k-ceiling bypass via created WINDOWS**: add `"max":"YYYY-MM","inclusive_max":true` → split a big sub into windows each <25k, paginate each, merge. Verified sums exact: K&D 2020-01..2022-12=7,337 + 2023-01..now=21,813 = 29,150; HI 6,969+20,083=27,052. (Good split point: pre-2023 vs 2023+.)
  - bq does NOT re-trigger from the URL on a programmatic `goto` (SPA ignores it) — must send in the POST body. reCAPTCHA `rct` NOT required for these body queries (200 OK without it). Crack scripts: `sl_crack_bq.py`..`sl_crack_bq5.py`.
  - SORT still not needed: collect full window-merged set, then sort CLIENT-SIDE by Est Visits (mvis). Server-side sort param still uncracked but unnecessary now.
- **EXPORT TABLE FIELDS — FINALIZED (Marina-agreed 2026-05-31):** Domain · Merchant Name · Country · Location · Language · Created · **Est Visits/mo (`mvis`)** · Est PageViews/mo (`mpv`) · Est Sales/mo (`erf`) · Avg/Min/Max Product Price (`apf/minpf/maxpf`) · **Average Product Weight** (cut bulky — logistics) · **Product count / Variants** (hero vs catalog flag) · Products Created 30d · App Spend (`masf`) · Rank/Platform Rank · Status · Platform · Categories · **Theme / Last Theme** (KEEP — site-quality ref for the launch dept) · Meta Description · **Combined Store Reviews (#/rating)** + TrustPilot Reviews/Rating · social ACCOUNTS **Facebook/Instagram/TikTok/Pinterest** (from `identifiers`, matched by URL). **DROP Meta Keywords. DROP social Followers+30d-growth** (Marina 2026-05-31 — NOT in the domains API response; the cryptic tsss/stcs/shcs turned out to be ships-to/shipper data, not followers — removed to avoid clutter; revisit only if a social-stats endpoint is found). **Field codes (live-verified, coverage% on HI≥2020 n=300):** domain=name · merchant=merchantName(100) · country=countryCode · loc=loc(98) · lang=langn · created=createdAt · visits=mvis(100) · pageviews=mpv(100) · sales=erf(100) · price=apf/minpf/maxpf(96) · weight=apw(86) · products=pc(100) · variants=varc(97) · app_spend=masf(77) · rank=rank/prank(100) · theme=themeName(100)/ltheme(87) · meta=md(99) · reviews=combrs(45)/tprs(27) · social=identifiers FB(75)/IG(81)/TikTok(22)/Pinterest(32). Est Visits = primary analysis-ranking signal (start >1000 visits, don't exclude lower). NOTE: we extract via API so we can include any field regardless of UI column checks; Notion gets the useful subset + social links auto-filled.
- **FULL DUMP DONE (Home Improvement ≥2020):** `sl_dump_full.py` collected **27,052 unique = exact server sum** (windows 2020-01..2022-12=6,969 + 2023-01..now=20,083), **no 25k-ceiling hit** — windowing works. ⚠️ **page size `ps` caps at 50** (server ignores ps=200) → ~540 page requests, ~21 min for 27k at 0.5s/page. Outputs on VPS: `home_improvement_full.json` (19MB) + `home_improvement_table.html` (14MB). Light preview via `sl_html_top.py <slug> <N>` → top-N HTML (366KB for 500). HTML = clickable domain + FB/IG/TT/Pin links, sorted by Est Visits. Top-by-visits = big brands (Hunter Fan/Honeywell/Grohe/Lasko); white-label gems mid-list (getcanopy/dreo/horow/forgenflame) — confirms Day-1 sort calibration.
- **NEXT:** Marina reviews the HTML → then pull **batch 200** (top by visits, or a chosen band) → funnel: live site-visit hero-confirm → real Stage-3 deep-score (100pt+Veto, no eyeballing) → checkpoint → Notion. Active dumpers in `scripts/`: `sl_dump_full.py` (full windowed) / `sl_dump3.py` (sample) / `sl_html_top.py` (preview). The one-off `bq`-crack series + early dumps/probes are in `archive/storeleads-discovery-2026-05/` (provenance only; the cracked format lives in `methods/interface-guide.md`).

---

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

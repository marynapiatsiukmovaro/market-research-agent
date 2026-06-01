# Store Leads Department

Third sourcing department. **Store-first discovery** at SCALE via storeleads.app (~2.85M
active Shopify stores; ~3.59M Shopify all-status), using its internal JSON API as the funnel's Stage-0 source.

> **Status: SYSTEM-BUILD / in active development (started 2026-05-30).** Access solved; internal
> data-API fully mapped incl. the advanced **`bq` (Bleve) query** — created≥2020, multi-category OR,
> and the 25k-ceiling bypass via created windows (all validated to-the-store). Category census done;
> green-shortlist subcategories fixed; export-table fields agreed + live-verified. First full clean
> dump done (Home Improvement ≥2020 = 27,052). Funnel runs end-to-end on the **product-centric enricher v4**
> (`sl_enrich4.py` — product_class/store_type/self-check); 5 HI batches done (1000 stores; HI = structurally
> "heavy"/trade, low white-label yield); master record + keep-list monitor wired (RULE 19/20); stage artifacts
> (HTML+PNG) delivered to Marina's Desktop each batch. NEXT = batches 6–7 to finish the HI band, then likely
> switch to a consumer subcategory. Built iteratively like ShopHunter / FB matured. Human-in-loop; autonomous NOT earned.

## Why this department exists
ShopHunter's universe is its ~800/category *tracked* subset — emerging/early-window stores
are missed. Store Leads indexes the whole Shopify universe (~2.88M active), richly filterable
(revenue band, created date, avg price/weight, category, country, installed apps, tech) and —
crucially — returns most store-level data **inside the search result** (revenue, price range,
created date, reviews, FB-pixel, newest product), so the first cut is cheap and only finalists
need a live site visit. Bigger top-of-funnel, lower cost per store.

## Relationship to other departments
**Fully isolated** (Marina, 2026-05-30). NOT a breadth-feeder for ShopHunter — an independent
department, like FB and ShopHunter are to each other. ShopHunter MAY later be used as an
*optional external enrichment resource* for top finalists (per-product revenue), but the two
departments do not couple. Never read another department's operational memory.
FB / ShopHunter are **maturity references for SHAPE, not content** — copy the discipline
(permanent rules vs expiring learnings, founder calibration before scoring, end-of-session
memory, no gut top-N, checkpoint-before-Notion), NOT their mechanics.

## What it inherits (read-only — never modify from a Store Leads session)
`core/` (scoring + Marina Veto, mandatory-filters, founder, product-requirements, operating /
session-health rules, identity, mindset) + `shared/` (reported/rejected logs, Notion schema +
workflow, founder-taste, product-validation, analysis skills).

## Access model
- Runs on the shared VPS (`5.78.217.133`), headless Chromium (Playwright 1.59) + iProyal proxy.
- **storeleads.app login is passwordless** (email code — NOT Google/password). Marina enters
  email + the emailed code via `scripts/sl_email_login.py` (ssh -t). Session persists in
  `cookies/storeleads_state.json` + `cookies/storeleads_profile` (gitignored). Re-login with a
  fresh code when it expires. Verify with `scripts/sl_check_login.py`.
- Plan = **Premium $75**: 2 platforms (Shopify selected), ~2000–4000 searches/mo, **NO export /
  API / workflow** (Pro+ only) → we use the internal session-API the UI itself calls. Stay gentle.

## Entry points
- `workflow.md` — session entry point (thin → methods/). Load order: op-rules → founder-feedback → learnings.
- `operational-memory/op-rules.md` — **PERMANENT rules (read FIRST every session)** — the department's discipline.
- `capabilities.md` — what Store Leads exposes + what we inherit.
- `methods/interface-guide.md` — the JSON-API mechanics (login, endpoints, `bq`, filter format, fields, limits).
- `methods/discovery-funnel.md` — the chain (Stage 0–3): Stage-1 = `sl_select_all` (RULE 24 — NO field filters, analyse every unprocessed store; conservative-cut RETIRED) + data-trust map + discipline.
- `methods/subagent-spec.md` — the Stage-2 enricher's exact job spec (fields, `desc` rule, what NOT to write).
- `methods/shophunter-enrichment.md` — OPTIONAL cross-dept enrichment of finalists via ShopHunter.
- `reference/cross-dept-patterns.md` — patterns observed in SH/FB, not adopted yet (reference / archivable).
- `operational-memory/learnings.md` — HANDOFF (read first) + session learnings.
- `operational-memory/founder-feedback.md` — Marina's product decisions for this channel.
- `hypotheses/_active.md` — current research direction.

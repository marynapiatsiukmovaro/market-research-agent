# Active Hypothesis — Store Leads

**ACTIVE:** `niche-store-first-at-scale.md` — pick a niche → dump with **only 3 server-side filters
(Shopify + Active + Created≥2020)** → **`sl_select_all.py` (RULE 24: NO field filters; visits = order only;
analyse EVERY unprocessed store)** → live-enrich heroes + open EVERY needs_live → 100-pt + Veto →
65+/55–64/browse. Pilot 2026-05-30 (K&D 200) validated the chain; S4 (Nursery, 1000 stores) confirmed RULE-24
no-gate catches deep-tail winners the old band-filter would lose.

---

## ⭐ ARCHITECTURE v2 — PRODUCT-CENTRIC (Marina-agreed 2026-05-31, S2)

> **STATUS (S3, 2026-06-01): IMPLEMENTED & LIVE in `sl_enrich4.py`.** Everything in the "What v2 builds NOW" list
> below is coded; v4 added product_class/store_type, homepage-hero + desc self-check (RULE 22), new_products_30d,
> subdomain-collapsed convergence, class-aware ABC, and the master-record + keep-list (RULE 20). This block is now
> the design rationale, not a to-do.

The founding chain stands; v2 sharpens its SOUL. Distilled from FB + ShopHunter discipline, but built to
**surpass** them on the one thing only Store Leads can do.

**Department philosophy — why we can be the strongest department:**
> We see the WHOLE Shopify universe (~2.85M active). So we win on TWO fronts FB and ShopHunter can't cover:
> 1. **Earlier** — we catch winner-PRODUCTS in young/emerging stores BEFORE they hit ads (FB) or accrue the
>    revenue ShopHunter ranks by.
> 2. **Wider (Marina S2)** — we also surface **ESTABLISHED, proven stores that are simply NOT visible** in
>    ShopHunter (not in its ~800 tracked subset) and weren't caught in FB. A proven product hiding off-radar
>    is a winner we can take TODAY — no need to only chase emerging. **`established` ≠ reject.**
>
> **The unit of the hunt is the PRODUCT, not the store.** A store is just a box; we pull its 1–2 golden products.
> **Revenue is NOT our main signal** — an early winner has none yet (a 2-week-old store may show $0 or wrong/
> foreign-currency revenue). We judge by EARLY SIGNALS + the LIVE SITE as the source of truth. **Accuracy now,
> cheap-at-scale later** (harden first, then cheapen what already works — never the reverse).

**What v2 builds in the scraper NOW (Marina-locked S2):**
1. **Open-ladder (kills the silent-DROP bug):** try `best-selling`→`frontpage`→`featured`→`/products.json`
   →**homepage HTML**. If still nothing → mark **"needs manual look" + reason**, NEVER a silent DROP.
   (S2 proof: 17/18 "unreachable" stores were actually alive — products.json just disabled.)
2. **TOP-3 product candidates per store** (not 1 guessed hero): scan the whole top-catalog, return the 3
   best, each with desc + REAL price (USD) + type. (Fixes "1 random hero = a spare part" + "is the info
   enough" — answer was no; 3 with full info = yes.)
3. **Early signals per PRODUCT (NOW):**
   - **Storefront position** — order in best-selling/featured = the merchant saying "THIS is my main one"
     (works even for a 2-week-old store, no revenue needed).
   - **Investment** — description length / #images / #variants / badges (Bestseller, As-seen-on) =
     effort put in ≠ filler.
   - **Convergence WITHIN the subcategory** (Marina S2: this scope is fine NOW — it's ~27k stores in one
     subcategory, NOT hundreds of thousands across the universe, so it's cheap). Same product-type across N
     stores of the dumped subcategory = demand WITHOUT revenue. **Dedupe geo-mirrors** (7 country-mirrors of
     one domain ≠ ×7 — S2 lesson, fullmoonloom).
4. **Currency normalization** (AUD/ZAR → USD — the #1 enricher error; price is the #1 unreliable field).
5. **Pre-flight 5 checks** before every run (from FB): VPS up · login valid · no duplicate worker · proxy
   healthy · quota OK. (Directly fixes the S2-start reliability mess.) **Follow FB RULE 4c exactly:** minimal
   one-line `nohup` launch · detect done by sentinel/log marker not process · never `pgrep -f` (self-match) use
   `[s]l_enrich2` · bracket-kill standalone · NEVER add `-o` ssh flags (breaks the allowlist → permission prompts).
6. **`desc_confidence` flag** (Marina S2 — we do what ShopHunter only PLANNED at SH-8 but never coded → we go
   first/stronger): the enricher tags each candidate's description `ok` / `empty` / `mismatched`, so the main
   agent KNOWS which to live-verify. Kills the "winner buried by a bad description" risk (SH-7 SlotPro 52→66).

**What I (main agent) do at deep-score:** LIVE SITE = source of truth; empty/mismatched desc → open the
page before scoring; 100-pt + Marina Veto on the confirmed product; no gut top-N (FB RULE 8).
- **Loss-measurement (Marina S2):** every batch, hand-check a RANDOM sample of the definite-no/dropped pile →
  report the loss number ("checked N dropped, 0 winners → cut is sound"). Turns "0% loss" from faith into a measured fact.
- **Keep-list for monitoring (Marina S2 — START NOW):** flag interesting/high-potential stores into a keep-list
  every batch (zero extra work — I see them anyway). When it grows → feed them into the ShopHunter
  newest-first monitor (ShopHunter's PARKED `collection-newest-first-monitor` hypothesis). **Store Leads = the
  store-supplier for that monitor** — we comb the universe, the monitor watches what those operators launch next.

**DEFERRED (Marina, NOT now):**
- **Fresh-product / new-arrival monitoring JOB itself** — the check-up job lives in ShopHunter (parked); we only
  FEED it the keep-list now, don't build the job here.
- **FB-Pixel / ads** — demoted to CONTEXT, not a selection criterion (data not always correct).
- **ShopHunter enrichment of finalists** — **PROVISIONAL (S3):** tested S3 = 2/12 found (both already-known weak),
  most SL stores are SL-unique → SH adds little so far. **Decide after batch 6** whether it earns its paid sub; if
  not, we drop it. Not a standard step.

Archived: (none yet)

See `niche-store-first-at-scale.md` for the founding detail, `methods/discovery-funnel.md` for the procedure,
and `methods/subagent-spec.md` for the scraper's exact output contract (v2).

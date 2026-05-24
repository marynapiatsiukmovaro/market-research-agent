# ShopHunter — Session Learnings

Short-lived tactical discoveries from recent sessions. Read at session start.
Does NOT contain permanent rules (those go to `op-rules.md` once it exists) or
company-level logic (that stays in `core/`).

Discipline mirrors the FB department: append new entries with an expiry; archive
expired entries; never delete — move to the Expired section. A pattern confirmed
across 3 sessions OR explicitly approved by Marina may be promoted to a permanent
rule via `review/promotion-queue.md`.

---

## HANDOFF → SH-3 (read first)

**Done in SH-2 (2026-05-24):** mapped shop-page data live; added 4 ShopHunter-only Notion fields
(SH Link, **SH Store Created [now TEXT]**, SH Rev W/M, SH SKU/Country) shown in the main Table view after
Store Link; enriched ALL 47 Product-Tracker rows (**29 with data, 18 marked "-"**). Fixed the search
over-stripping bug → recovered **seattosleep (61584507067), nuface (7425785), camp snap (74473832752 —
matched by NAME; its SH domain ≠ campsnapcamera.com)**. N/A handling DONE (Marina option a): SH Store
Created converted date→TEXT (existing dates preserved as date-mentions), literal "N/A" written to the 14 N/A rows.

**Open / do next:**
1. **9 confirmed ABSENT** even via full URL + brand name (all 12 misses now RESOLVED; these keep "-"):
   travelerpillow, puredailycare, luncheaze, itakico, glenbrookhome, toucanbaby, desknest, ergopurrch, kaizenkidz.
2. **9 not found via domain+name — cause UNKNOWN, do NOT infer coverage.** Of the 12 misses, 3 were
   search-bug false-negatives (seattosleep, nuface, camp snap); 9 were not found (travelerpillow,
   puredailycare, luncheaze, itakico, glenbrookhome, toucanbaby, desknest, ergopurrch, kaizenkidz). We have
   NOT inspected what those 9 are — could be established brands under a different stored domain/name we didn't
   guess, or genuinely absent. 9 links say NOTHING about ShopHunter coverage (tens of thousands of stores).
   NEXT: open/inspect the 9 directly before any coverage statement. Method lesson: a store's SH-stored domain
   can differ from our Store Link → **brand-NAME search is the essential fallback** (camp snap matched by name).
3. **Begin ShopHunter store-first DISCOVERY** (the original "tomorrow" goal).

**Watch:** revenue = estimate (corroborate); mono-brand (2–9 SKU) vs catalog/dropship (100+ SKU);
competitor multi-geo domains; VPS background-SSH drops (poll `pgrep`, don't relaunch).

---

## Active Learnings

### [2026-05-24] Session SH-1 — Explore Shops search needs the BARE DOMAIN, not the full product URL
**Type:** Tactical / Warning
**Severity:** MEDIUM
**Confidence:** HIGH (confirmed live with renpho.com)
**Observation:** In Explore → Shops, the "Search Shops" box matches a store by its
domain/handle, NOT a full product path. Searching `renpho.com/collections/eye-massager`
did NOT surface the store; stripping to `renpho.com` returned the shop (id 8346304597).
Rule: when taking a Store Link from our records/Notion, strip it to the bare domain
(everything up to the first slash after .com) before searching.
The shop page then exposes: store revenue (Day/Week/Month + trend), **Store Creation Date**,
**SKU count**, **tracked-by-N-users**, **Competitor Analysis** (rival stores + their revenue +
top products), and a **"View on Facebook Ads Archive"** link (built-in FB cross-reference).
**Applies to:** every Explore Shops lookup that starts from a known store link
**Expires after:** Never → promote to `op-rules.md` when that file is created (permanent operational fact)
**⚠ REFINED in SH-2 (below): bare domain ALONE is INSUFFICIENT — strip only the PATH, then try full URL / www / bare / name.**

---

### [2026-05-24] Session SH-2 — [CORRECTED] Search by FULL URL — bare domain alone is NOT enough (refines SH-1)
**Type:** Warning / Correction (supersedes the SH-1 bare-domain rule)
**Severity:** HIGH (this bug caused ~12 false "not in index" results in SH-2)
**Confidence:** HIGH (Marina confirmed live + diagnostic)
**Observation:** "Search Shops" is a RELEVANCE search. Bare domain matches only stores whose canonical
domain is stored WITHOUT www (renpho.com, nuvebrand.com). It FAILS (0 results) for stores stored WITH
www: `seattosleep.co.uk` → 0, but `https://www.seattosleep.co.uk` (full URL, as Marina pasted) → found
(id 61584507067); the name with spaces "seat to sleep" also found it. A product PATH still breaks it
(SH-1: renpho.com/collections/… → 0).
**Rule (corrected):** strip only the PATH after the domain; then try IN ORDER until a hit:
(1) full Store Link URL as-is (https://www.…), (2) https://www.+domain, (3) bare domain,
(4) brand NAME as words (de-concatenate: seattosleep→"seat to sleep"). ALWAYS open the result and
confirm the shop's shown domain matches before trusting — search returns multiple relevance matches,
the right store may not be first, and a store's canonical domain may differ from our saved Store Link
(e.g. Camp Snap may be campsnap.com, not campsnapcamera.com).
**Applies to:** every Explore Shops lookup.
**Expires after:** Never → op-rules.md.

### [2026-05-24] Session SH-2 — "Not in index" came from a SEARCH BUG; the 9 unfound stores are UNEXPLAINED (no coverage claim)
**Type:** Warning / Open question
**Severity:** HIGH
**Confidence:** MEDIUM
**Observation:** The over-stripping bug made SH-2 mark ~12 stores "-"/"not found". After the corrected
search (full URL + brand name), 3 were recovered — seattosleep (id 61584507067), nuface (id 7425785,
$2M/mo, branded ref), camp snap (id 74473832752 — matched by NAME; its SH domain ≠ campsnapcamera.com).
9 were still not found via domain+name: travelerpillow, puredailycare, luncheaze, itakico, glenbrookhome,
toucanbaby, desknest, ergopurrch, kaizenkidz. ⚠ Do NOT conclude anything about ShopHunter's coverage from
this — we have NOT inspected those 9 (they may be established brands under a different stored domain/name,
or genuinely absent), and 9 links is no sample for a tool with tens of thousands of stores (Marina's
correction — avoid overgeneralizing from a tiny sample). NEXT: open/inspect the 9 directly (correct stored
domain? on Shopify? real size) BEFORE any coverage statement.
**Applies to:** the 9 "-" rows; keep any unverified coverage claim OUT of strategy.
**Expires after:** Session SH-4.

### [2026-05-24] Session SH-2 — Notion: the 4 SH fields are ShopHunter-DEPARTMENT-ONLY
**Type:** Pattern / Rule (Marina-approved)
**Severity:** MEDIUM
**Confidence:** HIGH
**Observation:** Added to the shared Product Tracker: **SH Link** (url), **SH Store Created** (text — converted
from date in SH-2; description was lost on conversion, re-add if wanted), **SH Rev W/M** (text "week / month"),
**SH SKU/Country** (text "N / US"). The other 3 field descriptions say "ShopHunter dept only — FB Ads agent
leaves blank" → the FB-department agent must NOT fill these.
Provenance decision (Marina): do NOT add a separate "Department" field — instead add value **"ShopHunter"**
to the existing **Source** field for FUTURE ShopHunter-discovered products; NEVER rewrite existing Source
values (TikTok/WebSearch/Facebook/Amazon are accurate — today's enrichment did NOT change Source).
For a store not found, put **"-"** in SH Link (visible "checked, absent"). **Notes** may now hold
store/infrastructure observations (multi-geo domains, store-name≠product, price discrepancies), not only product notes.
**Applies to:** every Notion write from ShopHunter.
**Expires after:** Never → op-rules.md.

### [2026-05-24] Session SH-2 — Shop-data semantics (what the numbers mean)
**Type:** Signal
**Severity:** LOW
**Confidence:** HIGH
**Observation:** (1) Revenue = ESTIMATE — corroborate before calling a winner. (2) Store Created: ~half
show N/A; when present, dates are varied/plausible (2016–2025) → field usable for mature-vs-fresh; the
9/2/2022 shared by renpho+nuve was isolated. N/A handling RESOLVED in SH-2 (Marina opt a): SH Store Created
converted to TEXT, literal "N/A" written to the 14 N/A rows, existing dates preserved as date-mentions. (3) SKU count
reveals store TYPE: mono-brand hero (2–9 SKU: Hoppie, Rhona, WagWells) vs big catalog/dropship
(KittySpout 481, Cherrypick 216, Levide 147) — high SKU = product is one of many, weaker as a hero-brand.
(4) Competitor Analysis = free convergence/saturation map per store, incl. multi-geo same-brand variants
(renpho.eu/IE, renpho.uk/GB) → record in Notes. (5) Shopify Apps can flag white-label supplier (Nuvé uses
"SUPLIFUL: White Label Products"). (6) Store NAME ≠ our product name (Rhona store = "Rhona's FloatSeat+™").
**Applies to:** reading any shop page.
**Expires after:** Never → op-rules.md.

### [2026-05-24] Session SH-2 — VPS scraping ops (reliability)
**Type:** Tactical
**Severity:** MEDIUM
**Confidence:** HIGH
**Observation:** (1) A `run_in_background` SSH to the VPS DROPPED (exit 255) but the remote python KEPT
RUNNING — DO NOT relaunch (parallel runs fight over the single browser-profile lock + burn credits);
instead poll `pgrep -f` and read the incremental JSON. (2) A wait-loop using `pgrep -f "sh_batch.py"`
matches ITS OWN command line → never exits; use a distinct marker. (3) Scripts MUST save results
incrementally (per store), not only at loop end. (4) Under headless-Chromium load, VPS sshd briefly
returns "banner exchange: invalid format" — transient, retry. (5) Foreground SSH runs were reliable;
background ones dropped. Helper scripts: sh_batch.py (compact extractor), sh_recheck.py (name/URL retry),
sh_diag.py (search diagnostic) in /opt/market-research-agent/scripts/.
**Applies to:** all VPS ShopHunter scripts.
**Expires after:** Never → op-rules.md.

---

## Expired / Promoted

_Empty._

---

## How to add a learning

```
### [YYYY-MM-DD] Session N — [Short Title]
**Type:** Pattern / Warning / Signal / Tactical
**Severity:** LOW / MEDIUM / HIGH / CRITICAL
**Confidence:** LOW (1 case) / MEDIUM (2–3) / HIGH (multiple or founder-confirmed)
**Observation:** what was found (2–5 lines)
**Applies to:** [store type / category / discovery path]
**Expires after:** Session [N+7]   (use "Never" → promote to op-rules.md instead)
```

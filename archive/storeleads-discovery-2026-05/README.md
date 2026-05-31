# Store Leads — discovery scripts (archived 2026-05-31)

One-off scripts from bootstrapping the Store Leads department (Day 1–2, 2026-05-30/31).
They served their purpose; the **knowledge they produced lives in**
`departments/storeleads/methods/interface-guide.md` + `operational-memory/learnings.md`.
Kept for provenance (HOW we cracked the API), not for re-running.

- `sl_recon.py` / `sl_login_recon.py` / `sl_iface_shots.py` — early UI/login screenshots.
- `sl_net.py` / `sl_api.py` — captured the SPA's API calls + request bodies.
- `sl_decode.py` / `sl_decode2.py` — digested plans / facets / field codes.
- `sl_cats.py` / `sl_query.py` — first category-tree + `f:` filter probes.
- `sl_census.py` / `sl_subcensus.py` — early category census (superseded by `sl_count.py` + `sl_subtree.py`).
- `sl_probe.py` — foundation probe (sort / created filter / filter-drop evidence).
- `sl_crack_bq.py` … `sl_crack_bq5.py` — the `bq` cracking series → final Bleve format
  (`{"field":"cat","match":..}`, `cratyyyymm` TermRange for created≥2020, disjuncts for OR,
  date-window split to beat the 25k ceiling). Validated to-the-store (K&D=29,150).
- `sl_dump.py` / `sl_dump2.py` — pre-`bq` dumps (client-side created filter). Replaced by
  `sl_dump_full.py` (server-side `bq`, windowed).
- `sl_shots.py` / `sl_shots2.py` — early screenshot attempts (replaced by `sl_shots3.py`,
  which renders the Advanced view by putting the Bleve `bq` in the URL path).

Active tooling remains in repo `scripts/`.

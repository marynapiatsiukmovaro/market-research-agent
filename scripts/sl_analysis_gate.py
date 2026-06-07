#!/usr/bin/env python3
"""sl_analysis_gate.py — ANALYSIS-stage self-verification gate (Store Leads, S6 hardening; S13 contract).

The analysis-side twin of sl_qa.py (which guards Stage-2 DATA). This guards the ANALYSIS STEPS:
it proves — from artifacts, not the agent's word — that (1) every needs_live + unreachable store was
hand-opened, (2) every device-class in-range candidate got an explicit verdict, (3) the BROWSE-POOL
meets the floor of 7 (Marina S13 — browse is her window into the niche; 7 = floor, NOT a target/cap),
and it emits the browse-pool. Auto-STOP on any gap → this is the "external controller" that lets
analysis run faster safely (it self-stops; the agent cannot proceed past a gap).

Inputs:
  <enriched.json>   the Stage-2 enriched batch (source of truth for flags + candidate universe)
  <opens.jsonl>     one JSON/line for every hand-opened store:  {"domain":..., "verdict":"<short>"}
  <scores.jsonl>    one JSON/line per deep-scored candidate:
                    {"domain":..,"hero":..,"price":..,"score":N,"bucket":"winner|borderline|reject|browse","note":""}
Usage: python3 sl_analysis_gate.py <enriched.json> <opens.jsonl> <scores.jsonl>
"""
import json, sys

DEVICE_CLASSES = {"consumer-gadget", "appliance", "kitchen"}            # MUST have an explicit verdict
BROWSE_CLASSES = {"consumer-gadget", "appliance", "kitchen"}            # auto-browse classes (decor dropped — pulls mis-tagged decals/boards)
OFFMODEL_KIND = {"apparel", "ingestible", "skincare"}
BROWSE_FLOOR = 7   # Marina S13 (2026-06-07): minimum 7 browse links per batch, even in the tail. No ceiling.

def load_jsonl(p):
    out = []
    try:
        for ln in open(p):
            ln = ln.strip()
            if ln: out.append(json.loads(ln))
    except FileNotFoundError:
        pass
    return out

def any_in_range(r):
    return bool(r.get("in_range")) or any(t.get("in_range") for t in (r.get("tops3") or []))

enr = json.load(open(sys.argv[1]))
opens = load_jsonl(sys.argv[2])
scores = load_jsonl(sys.argv[3])
by = {r.get("domain"): r for r in enr}
opened = {o["domain"] for o in opens}
scored = {s["domain"] for s in scores}
reviewed = opened | scored

# ---- GATE 1: every flag (needs_live + unreachable) was hand-opened ----
flags = {r.get("domain") for r in enr if r.get("needs_live") or not r.get("reachable")}
missing_flags = sorted(flags - opened)

# ---- GATE 2: every device-class in-range store has an explicit verdict (scored or opened) ----
must_review = {r.get("domain") for r in enr
               if r.get("reachable") and any_in_range(r)
               and (r.get("product_class") in DEVICE_CLASSES)
               and not r.get("pust") and (r.get("kind") not in OFFMODEL_KIND)}
missing_review = sorted(must_review - reviewed)

# ---- BROWSE-POOL: device-class residue ∪ my explicit browse judgment (tags + bucket='browse') ----
win = {s["domain"] for s in scores if s.get("bucket") == "winner"}
bord = {s["domain"] for s in scores if s.get("bucket") == "borderline"}
rejected = {s["domain"] for s in scores if s.get("bucket") == "reject"}
browse_scored = {s["domain"] for s in scores if s.get("bucket") == "browse"}        # explicit browse in scorecard
browse_tagged = {o["domain"] for o in opens if "browse" in (o.get("verdict", "").lower())}
explicit_browse = browse_scored | browse_tagged                                     # my judgment — always survives
opened_offmodel = opened - browse_tagged          # hand-opened & judged off-model → never in browse
# my explicit browse overrides the off-model / proxy-class exclusion (Marina S13: when unsure, INCLUDE):
exclude = (win | bord | rejected | opened_offmodel) - explicit_browse
auto = {r.get("domain") for r in enr
        if r.get("reachable") and any_in_range(r)
        and (r.get("product_class") in BROWSE_CLASSES)
        and not r.get("pust") and (r.get("kind") not in OFFMODEL_KIND)}
browse = sorted((auto | explicit_browse) - exclude)
browse_short = len(browse) < BROWSE_FLOOR

# ---- counts ----
n = len(enr)
consumer_other = sum(1 for r in enr if r.get("product_class") == "consumer-other")
ok = not missing_flags and not missing_review and not browse_short

print("=" * 76)
print("ANALYSIS ACCEPTANCE GATE")
print("=" * 76)
print(f"  stores (read universe)      : {n}")
print(f"  flags (needs_live+unreach)  : {len(flags)}  | hand-opened: {len(flags & opened)}  | MISSING: {len(missing_flags)}")
print(f"  device-class must-review    : {len(must_review)} | reviewed: {len(must_review & reviewed)} | MISSING: {len(missing_review)}")
print(f"  deep-scored (scorecard)     : {len(scores)}  -> winners {len(win)} · borderline {len(bord)} · reject {len(rejected)} · browse {len(browse_scored)}")
print(f"  BROWSE-POOL                 : {len(browse)}  (floor {BROWSE_FLOOR}; device-class ∪ my browse-tags; not winner/borderline/reject) {'⛔ BELOW FLOOR' if browse_short else 'OK'}")
print(f"  consumer-other (card-judged, not individually logged — transparency, RULE 1): {consumer_other}")
if missing_flags:
    print("\n  ⛔ UNOPENED FLAGS (RULE 23 breach):", missing_flags)
if missing_review:
    print("\n  ⛔ UNREVIEWED DEVICE CANDIDATES:", missing_review)
if browse_short:
    print(f"\n  ⛔ BROWSE BELOW FLOOR: {len(browse)} < {BROWSE_FLOOR} — tag more interesting stores (bucket='browse' or verdict~'browse'). Tail counts; when unsure, INCLUDE.")
print("\n  BROWSE candidates:", browse)
# RULE 31 contract — printed ABOVE the verdict (S13b fix): the GATE line you MUST paste is now the LAST line,
# so the contract can't be truncated away without also losing the PASS line. (The b12/b13 drift was `sed`-truncating
# the tail → PASS seen, contract cut. Co-locating + putting the verdict last makes that physically impossible.)
print("\n  REPORT CONTRACT (RULE 31) — the checkpoint MUST contain EVERY section (no shrinking, any rhythm):")
print("    [ ] WINNERS 65+   [ ] BORDERLINE 55-64   [ ] BROWSE (>=7, RULE 32)   [ ] FUNNEL + ABC   [ ] LOSS-AUDIT")
print("    [ ] 1-2-line plain-language description per candidate (Marina reads it instead of opening the site)")
print("    ⚠ Run the gate WITHOUT truncating output; paste from this CONTRACT block through the GATE line below.")
# GATE verdict = the LAST line, carrying the section counts so pasting it inherently states W/BL/BR + coverage:
verdict = "✅ PASS" if ok else "⛔ STOP — fill the gaps above before checkpoint"
print(f"\n  GATE: {verdict} · W{len(win)} · BL{len(bord)} · BR{len(browse)}/{BROWSE_FLOOR}+ · "
      f"flags{len(flags & opened)}/{len(flags)} · dev{len(must_review & reviewed)}/{len(must_review)} · read{n}  [paste THIS line + the CONTRACT above]")
sys.exit(0 if ok else 1)

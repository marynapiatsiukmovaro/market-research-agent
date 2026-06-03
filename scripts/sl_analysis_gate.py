#!/usr/bin/env python3
"""sl_analysis_gate.py — ANALYSIS-stage self-verification gate (Store Leads, S6 hardening).

The analysis-side twin of sl_qa.py (which guards Stage-2 DATA). This guards the ANALYSIS STEPS:
it proves — from artifacts, not the agent's word — that (1) every needs_live + unreachable store was
hand-opened, (2) every device-class in-range candidate got an explicit verdict, and it (3) emits the
deterministic BROWSE-POOL by a fixed rule (count varies by niche, selection is reproducible).
Auto-STOP on any gap → this is what lets analysis run faster safely (it self-stops).

Inputs:
  <enriched.json>   the Stage-2 enriched batch (source of truth for flags + candidate universe)
  <opens.jsonl>     one JSON/line for every hand-opened store:  {"domain":..., "verdict":"<short>"}
  <scores.jsonl>    one JSON/line per deep-scored candidate:
                    {"domain":..,"hero":..,"price":..,"cur":..,"problem":N,"wow":N,"emotion":N,
                     "margin":N,"market":N,"veto":false,"veto_reason":"","score":N,"bucket":"winner|borderline|reject","note":""}
Usage: python3 sl_analysis_gate.py <enriched.json> <opens.jsonl> <scores.jsonl>
"""
import json, sys

DEVICE_CLASSES = {"consumer-gadget", "appliance", "kitchen"}            # MUST have an explicit verdict
BROWSE_CLASSES = {"consumer-gadget", "appliance", "kitchen"}            # auto-browse classes (decor dropped — pulls mis-tagged decals/boards)
OFFMODEL_KIND = {"apparel", "ingestible", "skincare"}

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

# ---- BROWSE-POOL: deterministic rule (selection fixed; count varies by niche) ----
win = {s["domain"] for s in scores if s.get("bucket") == "winner"}
bord = {s["domain"] for s in scores if s.get("bucket") == "borderline"}
rejected = {s["domain"] for s in scores if s.get("bucket") == "reject"}
browse_tagged = {o["domain"] for o in opens if "browse" in (o.get("verdict", "").lower())}
opened_offmodel = opened - browse_tagged          # hand-opened & judged off-model → never in browse
exclude = win | bord | rejected | opened_offmodel
# auto = device-class in-range residue; browse_tagged = my explicit judgment (overrides proxy class/in_range)
auto = {r.get("domain") for r in enr
        if r.get("reachable") and any_in_range(r)
        and (r.get("product_class") in BROWSE_CLASSES)
        and not r.get("pust") and (r.get("kind") not in OFFMODEL_KIND)}
browse = sorted((auto | browse_tagged) - exclude)

# ---- counts ----
n = len(enr)
consumer_other = sum(1 for r in enr if r.get("product_class") == "consumer-other")
ok = not missing_flags and not missing_review

print("=" * 76)
print("ANALYSIS ACCEPTANCE GATE")
print("=" * 76)
print(f"  stores (read universe)      : {n}")
print(f"  flags (needs_live+unreach)  : {len(flags)}  | hand-opened: {len(flags & opened)}  | MISSING: {len(missing_flags)}")
print(f"  device-class must-review    : {len(must_review)} | reviewed: {len(must_review & reviewed)} | MISSING: {len(missing_review)}")
print(f"  deep-scored (scorecard)     : {len(scores)}  -> winners {len(win)} · borderline {len(bord)} · reject {len(rejected)}")
print(f"  BROWSE-POOL (rule-derived)  : {len(browse)}  (consumer-class in-range, not winner/borderline/reject, deduped)")
print(f"  consumer-other (card-judged, not individually logged — transparency, RULE 1): {consumer_other}")
if missing_flags:
    print("\n  ⛔ UNOPENED FLAGS (RULE 23 breach):", missing_flags)
if missing_review:
    print("\n  ⛔ UNREVIEWED DEVICE CANDIDATES:", missing_review)
print("\n  BROWSE candidates:", browse)
print("\n  GATE:", "✅ PASS — every flag opened + every device candidate verdicted" if ok else "⛔ STOP — fill the gaps above before checkpoint")
sys.exit(0 if ok else 1)

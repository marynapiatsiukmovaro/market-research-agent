#!/usr/bin/env python3
"""
sl_winner_crossref.py — GUARD PROTOTYPE v0.1 (Store Leads, S16 2026-06-27)

WHY (Marina S16): the S15 failure = winners that matched things we'd already found
(nursery products sitting INSIDE the Home & Garden dump: The Wriggler / Rockit / SnoofyBee)
were silently browse-dumped. The gates checked COVERAGE, never JUDGMENT. This guard makes
"have we seen this winner-TYPE before?" a structural check, so a match CANNOT be silently browsed.

CORE IDEA (Marina's steer): the winner ignores our category label. We open the niche as
Home & Garden, but the winner may be a product from a COMPLETELY DIFFERENT category sitting inside
it (Store Leads cross-files constantly). So we cross-reference EVERY store against known winning
TYPES from ALL niches, plus exact known domains. A hit = MUST get an explicit score
(winner/borderline/reject with a PRODUCT reason) — never browse-only, never dismissed by category.

⚠ CATEGORY-NEUTRAL BY DESIGN (Marina S16): NO category is privileged. The registry below has more
nursery entries ONLY because Nursery is the niche we've mined most so far — that is a fact about OUR
PAST WORK, never a hint about where winners live. This is a SAFETY net ("seen this win before? don't
dismiss it"), NEVER a priority lens — the READ (RULE 6: read ALL, judge each on merit) stays fully
category-neutral and is the real net. The registry GROWS evenly as we analyse new categories.

STATUS: PROTOTYPE. Refine on b2+ (Marina: "guard is not final truth; watch how it works, tune it").
This v0.1 PRINTS a must-score worklist + writes <enriched>_crossref.jsonl. It does NOT yet hard-block
the gate (v0.2 candidate after we see it run). Floor, not cage — it never forbids opening extras.

LESSON BAKED IN FROM b1: match on EXACT domain + WHOLE-WORD type keywords, NOT loose substrings
(b1 false positives: "boba" matched "Mam-boba-by"; a brand co-occurrence ≠ same product).

Usage:  python3 scripts/sl_winner_crossref.py <enriched.json> [out_crossref.jsonl]
"""
import json, sys, re, os

# ── Known winning TYPES from EVERY niche we've analysed so far — a FLAT, EQUAL list, NO category
# privileged. It records only WHAT we've already mined (mostly Nursery to date, since that's the niche
# we've worked most) — NOT what matters most and NOT where to look. The winner can be in ANY category.
# Grouped below ONLY for human readability; every group carries equal weight. Each: label -> (keywords, context).
WINNER_TYPES = {
  # ---- types first found in Nursery (the niche mined most so far — no special weight) ----
  "baby carrier/wrap/sling":      (["baby carrier","baby wrap","baby sling","ergonomic carrier","hip carrier","ring sling"], "Nursery: WaterLand 72 / Omni 66 / Wildride 70 (carriers reviewed; judge, don't auto-browse)"),
  "fetal doppler":                (["fetal doppler","baby doppler","heartbeat monitor","prenatal doppler"], "Nursery: WellnessBaby 83 APPROVED / WonderBee 77 — top winner type; ⚠ liability"),
  "baby video/audio monitor":     (["baby monitor","video monitor","baby camera"], "Nursery: Roar 69"),
  "swaddle / sleep sack":         (["swaddle","sleep sack","sleeping bag","sleep bag"], "Nursery: Kaiya 72 / Dreamland 70 (apparel-ish — judge tactile differentiator)"),
  "changing mat/pad (anti-roll)": (["changing mat","changing pad","anti-roll","anti roll","diaper change"], "Nursery: Yogorgeous Watchlist + WriggleBum Consider (THE S15 MISS — The Wriggler/SnoofyBee)"),
  "nappy/diaper-change harness":  (["nappy change","diaper harness","changing harness"], "Nursery: WriggleBum 68 Consider"),
  "nursing light / feeding":      (["nursing light","nursing nightlight","wearable light"], "Nursery: LatchLight 76 Consider"),
  "crib safety tent/rail":        (["crib tent","crib safety","bed rail","safety tent"], "Nursery: KinderSense 73 / Crib Tent 73"),
  "stroller rocker":              (["stroller rocker","pram rocker","auto rocker","baby rocker"], "Nursery: Rockit 74 Consider (THE S15 MISS — rockitsleep.com)"),
  "baby bottle warmer/dryer":     (["bottle warmer","baby dryer","bottle dryer"], "Nursery: UpPro 67 / BuddyBottle 68"),
  "baby gate/stability":          (["baby gate","retractable gate","stair gate","stability pouch"], "Nursery: BabyBond 66 / Kanga 67"),
  "high-chair / seat cover":      (["high chair cover","cart cover","high-chair cover","shopping cart cover"], "Nursery: JoSeat 68"),
  # ---- pet (mostly closed, but a real-mechanism pet-care product still scores) ----
  "litter health monitor":        (["litter monitor","health litter","litter health","color-changing litter"], "Cats: SiiPet LitterLens 74"),
  # ---- home / wellness (types we've actually scored) ----
  "couch console / cup holder":   (["couch console","sofa console","cup holder console","couch cupholder"], "H&G S16: CouchConsole 73"),
  "peel&stick countertop wrap":   (["peel and stick countertop","countertop wrap","faux granite wrap","counter top wrap"], "H&G S16: EzFauxDecor 61"),
  "shower/water filter":          (["shower filter","showerhead filter","filtered showerhead","water filter pitcher"], "HI: Muravai 77 Watchlist (hair-angle open)"),
  "posture corrector":            (["posture corrector"], "FB: Smart Posture Corrector 75 Approved"),
  "eye massager":                 (["eye massager"], "FB: Eye Massager 84 Approved"),
  "heated cushion / sauna":       (["heated cushion","infrared cushion","sauna blanket","cold plunge","ice bath"], "HI: Stoov 73 / Cold Pod 64 Watchlist (⚠ bulky/high-ticket)"),
}

def norm(s):
    return re.sub(r"[^a-z0-9 ]+"," ", (s or "").lower())

def has_kw(text, kw):
    # whole-phrase, word-boundary match — NOT a loose substring (b1 lesson: boba != Mambobaby)
    return re.search(r"(?<![a-z])" + re.escape(kw.lower()) + r"(?![a-z])", text) is not None

def load_known_domains():
    """Exact domains we've already found/kept (re-appearance catch). Best-effort parse of keep-list."""
    doms = set()
    base = os.path.join(os.path.dirname(__file__), "..", "departments", "storeleads", "operational-memory", "keep-list.md")
    try:
        txt = open(base, encoding="utf-8").read()
        for m in re.finditer(r"([a-z0-9][a-z0-9\-]+\.[a-z][a-z0-9\.\-]+)", txt.lower()):
            doms.add(m.group(1).lstrip("www."))
    except Exception:
        pass
    return doms

def store_text(r):
    parts = [r.get("domain",""), r.get("home_pitch","")]
    for p in (r.get("tops3") or []):
        parts.append(p.get("t","")); parts.append(p.get("desc",""))
    return norm(" ".join(parts))

def main():
    if len(sys.argv) < 2:
        print("usage: sl_winner_crossref.py <enriched.json> [out.jsonl]"); sys.exit(2)
    path = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    data = json.load(open(path, encoding="utf-8"))
    known = load_known_domains()

    hits = []
    for r in data:
        dom = (r.get("domain","") or "").lower().lstrip("www.")
        text = store_text(r)
        reasons = []
        if dom in known:
            reasons.append(("KNOWN-DOMAIN", "already in keep-list — re-confirm decision"))
        for label,(kws,ctx) in WINNER_TYPES.items():
            if any(has_kw(text, k) for k in kws):
                reasons.append(("TYPE:"+label, ctx));
        if reasons:
            hits.append({"domain": r.get("domain"), "reasons": reasons})

    print("="*78)
    print("WINNER CROSS-REF GUARD v0.1  (PROTOTYPE — tune on b2)")
    print(f"  file: {os.path.basename(path)}   stores: {len(data)}   must-score hits: {len(hits)}")
    print("  RULE: every store below MUST get an EXPLICIT score (winner/borderline/reject w/ a PRODUCT")
    print("        reason) — it CANNOT be browse-only or dismissed by category. (CREED #3/#6)")
    print("="*78)
    for h in hits:
        print(f"\n  ▶ {h['domain']}")
        for tag,ctx in h["reasons"]:
            print(f"      [{tag}]  {ctx}")
    if not hits:
        print("\n  (no known-type / known-domain matches this batch — still judge every store on merit)")
    if out:
        with open(out,"w",encoding="utf-8") as f:
            for h in hits: f.write(json.dumps(h,ensure_ascii=False)+"\n")
        print(f"\n  wrote worklist -> {out}")

if __name__ == "__main__":
    main()

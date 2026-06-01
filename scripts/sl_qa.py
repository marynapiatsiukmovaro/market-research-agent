import json, sys
def pct(a, b): return round(100*a/b, 1) if b else 0.0
def audit(path):
    d = json.load(open(path))
    n = len(d); reach = sum(1 for r in d if r.get("reachable"))
    cand = sum(1 for r in d if r.get("candidate"))
    withprice = sum(1 for r in d if isinstance(r.get("price"), (int, float)) and r.get("price") > 0)
    curnull = sum(1 for r in d if (isinstance(r.get("price"), (int, float)) and r.get("price") > 0) and not r.get("currency"))
    tops = [len(r.get("tops3") or []) for r in d]
    withtops = sum(1 for t in tops if t > 0)
    avgtops = round(sum(tops)/n, 2) if n else 0
    empty_tops_reach = sum(1 for r in d if r.get("reachable") and not (r.get("tops3") or []))
    descok = sum(1 for r in d if r.get("desc_confidence") == "ok")
    pitch = sum(1 for r in d if r.get("home_pitch"))
    nl = sum(1 for r in d if r.get("needs_live"))
    name = path.split("/")[-1]
    print("%-24s n=%d reach=%d(%.1f%%) cand=%.1f%% price=%.1f%% cur_null=%d tops_cov=%.1f%% avgtops=%.2f desc_ok=%.1f%% pitch=%.1f%% needs_live=%d(%.1f%%) empty_tops_reach=%.1f%%" % (
        name, n, reach, pct(reach, n), pct(cand, n), pct(withprice, cand), curnull, pct(withtops, n), avgtops, pct(descok, cand), pct(pitch, n), nl, pct(nl, n), pct(empty_tops_reach, reach)))
    flags = []
    if pct(reach, n) < 90: flags.append("reach<90")
    if pct(cand, n) < 95: flags.append("cand<95")
    if pct(withprice, cand) < 95: flags.append("price<95")
    if curnull > 0: flags.append("cur_null=%d" % curnull)
    if pct(empty_tops_reach, reach) > 5: flags.append("empty_tops>5")
    if avgtops < 2: flags.append("avgtops<2")
    print("%-24s GATE: %s" % ("", "PASS" if not flags else "FLAG -> " + ",".join(flags)))
for p in sys.argv[1:]:
    audit(p)

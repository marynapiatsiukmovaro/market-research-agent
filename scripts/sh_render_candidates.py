# Compact candidate-sheet renderer for deep-score (reads enriched.json, prints ALL A+B+C).
# Usage: sh_render_candidates.py <enriched_file>
import json, sys, re
OUT = "/opt/market-research-agent/logs/shophunter"
d = json.load(open(OUT + "/" + sys.argv[1]))
order = {"A": 0, "B": 1, "C": 2}
d.sort(key=lambda x: (order.get(x.get("tier", "C"), 3), -int(x.get("score", 0) or 0)))
def cl(s, n):
    return re.sub(r"\s+", " ", (s or "").strip())[:n]
print("TOTAL", len(d), "| reachable", sum(1 for x in d if x.get("reachable")), "| in_range", sum(1 for x in d if x.get("in_range")))
for x in d:
    rng = "IN" if x.get("in_range") else "OUT"
    pu = " PUST" if x.get("pust") else ""
    cb = x.get("conv_batch") or 0
    ck = x.get("conv_known") or ""
    conv = ("cB%d" % cb) + (("/" + str(ck)) if ck else "")
    rch = "" if x.get("reachable") else " UNREACH"
    fl = ",".join(f for f in (x.get("flags") or []) if not f.startswith("CONV"))
    fl = (" {" + fl + "}") if fl else ""
    print("[%s|%s] $%s %s %s %s%s%s%s | %s | %s" % (
        x.get("tier", "?"), x.get("score", "?"), x.get("price", "?"), rng,
        cl(x.get("niche", ""), 10), conv, pu, rch, fl,
        cl(x.get("candidate", ""), 46), x.get("domain", "")))
    print("     ::", cl(x.get("desc", ""), 150))

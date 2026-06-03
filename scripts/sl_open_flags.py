#!/usr/bin/env python3
"""sl_open_flags.py — P1+P3 (S7 hypothesis): auto-log opener for needs_live+unreachable.
Reads the enriched batch, derives the FULL flag-list itself, opens each (with 503/timeout
RETRY then nothing-left=dead), and WRITES a pre-seeded opens.jsonl with one line per flag:
  {"domain":..,"status":..,"title":..,"prices":[..],"verdict":""}
The agent only fills "verdict". Opened-but-not-logged becomes impossible (RULE 23 enforced
by the tool, not memory). Device-class in-range stores are ALSO seeded so the analysis-gate
must-review set is covered too.
Usage: python3 sl_open_flags.py <enriched.json> <out_opens.jsonl>
"""
import sys, json, ssl, re, time, urllib.request
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
DEV = {"consumer-gadget", "appliance", "kitchen"}


def grab(dom, tries=2):
    url = dom if dom.startswith("http") else "https://" + dom
    last = ""
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
            h = urllib.request.urlopen(req, timeout=15, context=ctx)
            html = h.read(60000).decode("utf-8", "ignore")
            title = (re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I) or [None, ""])[1].strip()[:120]
            prices = re.findall(r"[$£€]\s?([0-9]{1,4}(?:\.[0-9]{2})?)", html)[:6]
            return {"status": h.getcode(), "title": title, "prices": prices, "retried": i > 0}
        except Exception as e:
            last = str(e)[:80]
            if i + 1 < tries:
                time.sleep(4)   # P3: retry transient 503/timeout once before declaring dead
    return {"status": "ERR", "title": "", "prices": [], "err": last, "retried": tries > 1}


d = json.load(open(sys.argv[1]))
flags = [r for r in d if r.get("needs_live") or not r.get("reachable")]
dev = [r for r in d if r.get("reachable") and (r.get("product_class") in DEV)
       and any(p.get("in_range") for p in (r.get("tops3") or []))]
seen = set(); rows = []
for r in flags + dev:
    dom = r.get("domain")
    if dom in seen:
        continue
    seen.add(dom)
    kind = "FLAG" if (r.get("needs_live") or not r.get("reachable")) else "DEVICE"
    info = grab(dom)
    rows.append({"domain": dom, "_seed": kind, "status": info.get("status"), "title": info.get("title"),
                 "prices": info.get("prices"), "retried": info.get("retried"), "verdict": ""})
with open(sys.argv[2], "w") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
nflag = sum(1 for r in rows if r["_seed"] == "FLAG")
ndev = sum(1 for r in rows if r["_seed"] == "DEVICE")
nretry = sum(1 for r in rows if r.get("retried"))
print(f"SEEDED {len(rows)} rows -> {sys.argv[2]}  (flags {nflag} | device {ndev} | retried {nretry})")

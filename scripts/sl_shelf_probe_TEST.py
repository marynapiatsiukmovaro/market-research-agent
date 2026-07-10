#!/usr/bin/env python3
"""Does the robot see what a human sees? (S20 probe, Marina's question)

For each domain, fetch three orderings of the SAME store and put them side by side:
  1. what the ENRICHER reads        -> /products.json?limit=50   (or the collection it fell back to)
  2. what a HUMAN sees on the shelf -> /collections/all  (HTML, the merchant's own manual order)
  3. what a HUMAN sees first        -> the homepage      (HTML, whatever the merchant put up front)

If (1) and (2) disagree, then for the 163 of 250 stores that have no best-selling collection the card's
"top-3 products" are three arbitrary items, not the store's front row — which is exactly what the 30/250
day-to-day drift measured.

Usage: sl_shelf_probe_TEST.py <domain> [<domain> ...]
"""
import json, re, sys, time
from playwright.sync_api import sync_playwright

creds = {}
for line in open("/opt/market-research-agent/cookies/proxy.creds"):
    if "=" in line:
        k, v = line.strip().split("=", 1); creds[k] = v
PROXY = {"server": "http://%s:%s" % (creds["PROXY_HOST"], creds["PROXY_PORT"]),
         "username": creds["PROXY_USER"], "password": creds["PROXY_PASS"]}
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/123.0.0.0 Safari/537.36")


def get(pg, url, tries=2):
    for a in range(tries):
        try:
            pg.goto(url, wait_until="domcontentloaded", timeout=20000)
            return pg.content(), pg.inner_text("body")
        except Exception:
            time.sleep(1.5)
    return "", ""


def handles(html, n=6):
    out = []
    for h in re.findall(r"/products/([a-z0-9][a-z0-9\-]{1,80})", html or ""):
        if h not in out:
            out.append(h)
        if len(out) >= n:
            break
    return out


with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=["--no-sandbox"], proxy=PROXY)
    pg = b.new_context(user_agent=UA, viewport={"width": 1400, "height": 1600}).new_page()
    for dom in sys.argv[1:]:
        print("=" * 100)
        print(dom)
        _, body = get(pg, f"https://{dom}/products.json?limit=6")
        try:
            js = json.loads(body) if body.strip().startswith("{") else {"products": []}
            robot = [(x["title"][:52], x.get("handle")) for x in js.get("products", [])[:6]]
        except Exception:
            robot = []
        print("  1. РОБОТ читает /products.json:")
        for i, (t, h) in enumerate(robot):
            print(f"       {i}. {t}")
        if not robot:
            print("       (пусто)")

        html, _ = get(pg, f"https://{dom}/collections/all")
        hh = handles(html)
        print("  2. ЧЕЛОВЕК видит на витрине /collections/all:")
        for i, h in enumerate(hh):
            print(f"       {i}. {h}")
        if not hh:
            print("       (не открылось / нет такой коллекции)")

        html2, _ = get(pg, f"https://{dom}/")
        hh2 = handles(html2)
        print("  3. ЧЕЛОВЕК видит на ГЛАВНОЙ:")
        for i, h in enumerate(hh2):
            print(f"       {i}. {h}")

        rset = {h for _, h in robot if h}
        print(f"  → совпадение робот∩витрина: {len(rset & set(hh))}/6 · робот∩главная: {len(rset & set(hh2))}/6")
    b.close()

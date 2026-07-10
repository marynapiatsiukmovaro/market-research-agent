#!/usr/bin/env python3
"""sl_hand_fetch.py — a dumb pipe, not a scraper.

WHY IT EXISTS (S21, Marina-directed). To compare the robot's card against a hand-made one, the two must
be read through the SAME channel. Reading from the Mac (WebFetch) is a different IP, a different browser,
and — worst — a summarising model between the agent and the page: it renamed £29.99 to "$29.99" and
counted 92 collections where the list held 76. A hand-made card built on that is not an etalon, it is a
second error to compare with the first.

So: same proxy, same Playwright, same user-agent as `sl_enrich4.py`. This tool FETCHES and PRINTS.
It never picks a shelf, never picks a product, never assigns a class, never converts a price.
Every judgement stays with the agent — that is the whole point of the exercise.

Usage:
    python3 scripts/sl_hand_fetch.py <url> [<url> ...]        # prints RAW body of each
    python3 scripts/sl_hand_fetch.py --html <url>             # prints page HTML instead of body text
"""
import sys
from playwright.sync_api import sync_playwright

creds = {}
for line in open("/opt/market-research-agent/cookies/proxy.creds"):
    if "=" in line:
        k, v = line.strip().split("=", 1)
        creds[k] = v
PROXY = {"server": "http://%s:%s" % (creds["PROXY_HOST"], creds["PROXY_PORT"]),
         "username": creds["PROXY_USER"], "password": creds["PROXY_PASS"]}
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")

args = [a for a in sys.argv[1:] if not a.startswith("--")]
WANT_HTML = "--html" in sys.argv

with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=["--no-sandbox"], proxy=PROXY)
    pg = b.new_context(user_agent=UA, viewport={"width": 1400, "height": 1600}).new_page()
    for url in args:
        print("\n===== %s =====" % url)
        try:
            pg.goto(url, wait_until="domcontentloaded", timeout=18000)
            print(pg.content() if WANT_HTML else pg.inner_text("body"))
        except Exception as e:
            print("FETCH-FAILED: %s: %s" % (type(e).__name__, e))
    b.close()

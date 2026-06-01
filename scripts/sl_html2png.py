#!/usr/bin/env python3
"""sl_html2png.py — render a local HTML file to a full-page PNG (headless chromium).
Reusable for stage screenshots Marina wants on her Desktop.
Usage: python3 sl_html2png.py <input.html> <output.png>
"""
import sys, os
from playwright.sync_api import sync_playwright

inp, outp = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
with sync_playwright() as p:
    b = p.chromium.launch(args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 1280, "height": 1000}, device_scale_factor=2)
    pg.goto("file://" + inp)
    pg.wait_for_timeout(400)
    pg.screenshot(path=outp, full_page=True)
    b.close()
print("PNG written:", outp)

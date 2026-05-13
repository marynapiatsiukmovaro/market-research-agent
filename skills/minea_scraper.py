#!/usr/bin/env python3
"""
Minea Scraper — grabs winning product data from Minea.com Meta Ads Library
Outputs JSON list of products for Claude to analyze.
"""

import json
import re
import os
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout


def load_env():
    env_path = Path(__file__).parent.parent / ".env"
    env = {}
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    for key in ["MINEA_EMAIL", "MINEA_PASSWORD"]:
        if key in os.environ:
            env[key] = os.environ[key]
    return env


def save_screenshot(page, name):
    screenshots_dir = Path("/opt/market-research-agent/logs/screenshots")
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    path = screenshots_dir / f"{name}.png"
    page.screenshot(path=str(path))
    print(f"[DEBUG] Screenshot: {path}", flush=True)


def login(page, email, password):
    page.goto("https://app.minea.com/login", wait_until="networkidle", timeout=30000)
    page.locator('input[type="email"]').first.fill(email)
    page.locator('input[type="password"]').first.fill(password)
    save_screenshot(page, "01_credentials_filled")
    page.locator('button[type="submit"]').first.click()

    try:
        page.wait_for_url(lambda url: "login" not in url, timeout=15000)
    except PlaywrightTimeout:
        pass

    page.wait_for_load_state("networkidle", timeout=15000)
    time.sleep(3)

    current_url = page.url
    print(f"[INFO] Post-login URL: {current_url}", flush=True)
    if "login" in current_url.lower():
        print("[ERROR] Login failed — still on login page", flush=True)
        save_screenshot(page, "login_failed")
        sys.exit(1)

    print("[OK] Login successful", flush=True)
    save_screenshot(page, "02_dashboard")


def scrape_minea(max_products=20):
    env = load_env()
    email = env.get("MINEA_EMAIL", "")
    password = env.get("MINEA_PASSWORD", "")

    if not email or not password:
        print("[ERROR] MINEA_EMAIL or MINEA_PASSWORD not set", flush=True)
        sys.exit(1)

    products = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
        )
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        try:
            # ── Step 1: Login ──────────────────────────────────────────
            print("[1/4] Logging in to Minea...", flush=True)
            login(page, email, password)

            # ── Step 2: Navigate to Meta Ads Library ───────────────────
            print("[2/4] Opening Meta Ads Library...", flush=True)
            # Sort by publication date (most recent active ads)
            page.goto(
                "https://app.minea.com/en/ads/meta-library?sort_by=-publication_date",
                wait_until="networkidle",
                timeout=30000
            )
            time.sleep(5)
            save_screenshot(page, "03_meta_ads")
            print(f"[INFO] Ads page URL: {page.url}", flush=True)

            # ── Step 3: Scroll to load more cards ─────────────────────
            print("[3/4] Loading product cards...", flush=True)
            for _ in range(4):
                page.keyboard.press("End")
                time.sleep(2)

            save_screenshot(page, "04_after_scroll")

            # ── Step 4: Extract card data ──────────────────────────────
            print("[4/4] Extracting product data...", flush=True)
            cards = page.locator(".virtuoso-grid-item").all()
            print(f"[INFO] Found {len(cards)} ad cards", flush=True)

            if not cards:
                # Fallback: try articles or generic containers
                cards = page.locator("article, [class*='AdCard'], [class*='ad-card']").all()
                print(f"[INFO] Fallback: {len(cards)} cards", flush=True)

            for i, card in enumerate(cards[:max_products]):
                try:
                    raw = card.inner_text().strip()
                    if len(raw) < 10:
                        continue

                    product = {"raw_text": raw[:800], "source": "Minea Meta Ads"}

                    # Store/product link — extract from raw text (Minea wraps in JS)
                    url_matches = [u for u in re.findall(r'https?://[^\s\n<]+', raw) if 'minea.com' not in u]
                    if url_matches:
                        product["store_url"] = url_matches[0]

                    # Brand / store name (first non-empty text line)
                    lines = [ln.strip() for ln in raw.split("\n") if ln.strip()]
                    product["brand"] = lines[0] if lines else ""

                    # Active ads count signal
                    for line in lines:
                        if "active ads" in line.lower():
                            product["active_ads_signal"] = line
                            break

                    # Impression count
                    for line in lines:
                        if any(x in line for x in ["k", "M"]) and any(c.isdigit() for c in line):
                            product["impressions"] = line
                            break

                    products.append(product)
                    print(f"  [{i+1}] {product.get('brand', 'no-name')[:50]} | ads: {product.get('active_ads_signal', '?')} | url: {product.get('store_url', 'N/A')[:60]}", flush=True)

                except Exception as e:
                    print(f"  [{i+1}] Error: {e}", flush=True)
                    continue

        except PlaywrightTimeout as e:
            print(f"[ERROR] Timeout: {e}", flush=True)
            save_screenshot(page, "error_timeout")
        except Exception as e:
            print(f"[ERROR] {e}", flush=True)
            save_screenshot(page, "error_unexpected")
        finally:
            browser.close()

    return products


if __name__ == "__main__":
    print("=== Minea Scraper v2 ===", flush=True)
    results = scrape_minea(max_products=20)

    output_path = Path("/opt/market-research-agent/logs/minea_results.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(results, ensure_ascii=False, indent=2))

    print(f"\n=== Done: {len(results)} products ===", flush=True)
    print(f"Saved to: {output_path}", flush=True)

    if results:
        print("\n=== PRODUCTS FOR CLAUDE ===", flush=True)
        for i, p in enumerate(results, 1):
            print(f"\n[{i}] Brand: {p.get('brand', '?')}", flush=True)
            print(f"     Active ads: {p.get('active_ads_signal', '?')}", flush=True)
            print(f"     Impressions: {p.get('impressions', '?')}", flush=True)
            print(f"     Store: {p.get('store_url', 'N/A')}", flush=True)
            print(f"     Raw: {p.get('raw_text', '')[:200]}", flush=True)
    else:
        print("[!] No products — check logs/screenshots/", flush=True)

#!/usr/bin/env python3
"""
Minea Scraper v3 — Meta Ads Library with Health/Beauty + US filters
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


def try_click(page, selectors, label):
    """Try each selector in order; return True if any succeeded."""
    for sel in selectors:
        try:
            el = page.locator(sel).first
            if el.is_visible(timeout=2000):
                el.click()
                time.sleep(1)
                print(f"[FILTER] {label}: clicked '{sel}'", flush=True)
                return True
        except Exception:
            continue
    print(f"[FILTER] {label}: no selector matched — skipping", flush=True)
    return False


def apply_filters(page):
    """Apply Health/Beauty category + US country filter via Minea UI.
    Fault-tolerant: if UI structure doesn't match, scraping continues unfilitered.
    """
    save_screenshot(page, "03_before_filters")

    # ── Category filter ──────────────────────────────────────────────────────
    category_opened = try_click(page, [
        'button:has-text("Category")',
        'button:has-text("Niche")',
        'button:has-text("Industry")',
        '[data-testid="category-filter"]',
        '[aria-label*="category" i]',
        '[aria-label*="niche" i]',
        # Minea sometimes uses a FilterChip or Chip component
        'div[class*="filter" i]:has-text("Category")',
        'div[class*="niche" i]',
    ], "open category dropdown")

    if category_opened:
        time.sleep(1)
        try_click(page, [
            'li:has-text("Health & Beauty")',
            'li:has-text("Health and Beauty")',
            'option:has-text("Health & Beauty")',
            '[data-value="health-beauty"]',
            '[data-value="beauty"]',
            'span:has-text("Health & Beauty")',
            'div:has-text("Health & Beauty")',
            'li:has-text("Beauty")',
            'li:has-text("Health")',
        ], "select Health & Beauty")
        time.sleep(1)

        # Apply or close
        applied = try_click(page, [
            'button:has-text("Apply")',
            'button:has-text("OK")',
            'button:has-text("Confirm")',
        ], "apply category")
        if not applied:
            page.keyboard.press("Escape")
            time.sleep(1)

    save_screenshot(page, "04_after_category_filter")

    # ── Country filter ───────────────────────────────────────────────────────
    country_opened = try_click(page, [
        'button:has-text("Country")',
        'button:has-text("Location")',
        'button:has-text("Region")',
        'button:has-text("Market")',
        '[data-testid="country-filter"]',
        '[aria-label*="country" i]',
        'div[class*="filter" i]:has-text("Country")',
        'div[class*="country" i]',
    ], "open country dropdown")

    if country_opened:
        time.sleep(1)
        # Look for a search input inside the dropdown and type "United States"
        try:
            search_input = page.locator('input[placeholder*="Search" i], input[placeholder*="search" i]').first
            if search_input.is_visible(timeout=2000):
                search_input.fill("United States")
                time.sleep(1)
        except Exception:
            pass

        try_click(page, [
            'li:has-text("United States")',
            'option:has-text("United States")',
            '[data-value="US"]',
            '[data-value="us"]',
            'span:has-text("United States")',
            'div:has-text("United States")',
            'li:has-text("USA")',
        ], "select United States")
        time.sleep(1)

        applied = try_click(page, [
            'button:has-text("Apply")',
            'button:has-text("OK")',
            'button:has-text("Confirm")',
        ], "apply country")
        if not applied:
            page.keyboard.press("Escape")
            time.sleep(1)

    save_screenshot(page, "05_after_country_filter")
    page.wait_for_load_state("networkidle", timeout=10000)
    time.sleep(3)
    print("[FILTER] Filters applied (check screenshots to verify)", flush=True)


def parse_active_days(raw_text):
    """Extract 'Xd Active' from raw card text → return int days or None."""
    match = re.search(r'(\d+)d\s+[Aa]ctive', raw_text)
    if match:
        return int(match.group(1))
    # Also handle "Active" without day count (just started today)
    if re.search(r'\bActive\b', raw_text):
        return 1
    return None


def parse_active_ads_count(raw_text):
    """Extract numeric count from 'X active ads' or 'X active ad'."""
    match = re.search(r'(\d+)\s+active\s+ads?', raw_text, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None


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
            print("[1/5] Logging in to Minea...", flush=True)
            login(page, email, password)

            # ── Step 2: Navigate to Meta Ads Library ───────────────────
            print("[2/5] Opening Meta Ads Library...", flush=True)
            page.goto(
                "https://app.minea.com/en/ads/meta-library?sort_by=-publication_date",
                wait_until="networkidle",
                timeout=30000
            )
            time.sleep(5)
            print(f"[INFO] Ads page URL: {page.url}", flush=True)

            # ── Step 3: Apply category + country filters ───────────────
            print("[3/5] Applying filters (Health/Beauty + US)...", flush=True)
            apply_filters(page)

            # ── Step 4: Scroll to load 20+ cards ──────────────────────
            print("[4/5] Scrolling to load 20+ cards...", flush=True)
            for scroll_i in range(10):
                page.keyboard.press("End")
                time.sleep(2)
                cards_now = page.locator(".virtuoso-grid-item").count()
                print(f"  scroll {scroll_i+1}/10 — cards visible: {cards_now}", flush=True)
                if cards_now >= max_products:
                    break

            save_screenshot(page, "06_after_scroll")

            # ── Step 5: Extract card data ──────────────────────────────
            print("[5/5] Extracting product data...", flush=True)
            cards = page.locator(".virtuoso-grid-item").all()
            print(f"[INFO] Found {len(cards)} ad cards", flush=True)

            if not cards:
                cards = page.locator("article, [class*='AdCard'], [class*='ad-card']").all()
                print(f"[INFO] Fallback: {len(cards)} cards", flush=True)

            for i, card in enumerate(cards[:max_products]):
                try:
                    raw = card.inner_text().strip()
                    if len(raw) < 10:
                        continue

                    product = {"raw_text": raw[:800], "source": "Minea Meta Ads"}

                    # Store link
                    url_matches = [u for u in re.findall(r'https?://[^\s\n<]+', raw) if 'minea.com' not in u]
                    if url_matches:
                        product["store_url"] = url_matches[0]

                    # Brand name (first non-empty line)
                    lines = [ln.strip() for ln in raw.split("\n") if ln.strip()]
                    product["brand"] = lines[0] if lines else ""

                    # Active ads count (raw signal line + parsed int)
                    for line in lines:
                        if "active ads" in line.lower() or "active ad" in line.lower():
                            product["active_ads_signal"] = line
                            break
                    product["active_ads_count"] = parse_active_ads_count(raw)

                    # Days running
                    product["active_days"] = parse_active_days(raw)

                    # Impressions
                    for line in lines:
                        if any(x in line for x in ["k", "M"]) and any(c.isdigit() for c in line):
                            product["impressions"] = line
                            break

                    # Marina filter pre-screen: 5-30 active ads + ≥7 days = flag as strong
                    ads_count = product.get("active_ads_count")
                    days = product.get("active_days")
                    if ads_count is not None and days is not None:
                        if 5 <= ads_count <= 30 and days >= 7:
                            product["marina_signal"] = "STRONG — sweet spot (5-30 ads, 7+ days)"
                        elif 5 <= ads_count <= 30 and days >= 14:
                            product["marina_signal"] = "VERY STRONG — 14+ days continuous"
                        elif ads_count > 30:
                            product["marina_signal"] = "CAUTION — 30+ ads, saturation risk"
                        elif ads_count < 5:
                            product["marina_signal"] = "WATCH — <5 ads, not yet proven"

                    products.append(product)
                    print(
                        f"  [{i+1}] {product.get('brand', 'no-name')[:40]} | "
                        f"ads: {product.get('active_ads_count', '?')} | "
                        f"days: {product.get('active_days', '?')}d | "
                        f"signal: {product.get('marina_signal', '-')} | "
                        f"url: {product.get('store_url', 'N/A')[:50]}",
                        flush=True
                    )

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
    print("=== Minea Scraper v3 ===", flush=True)
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
            print(f"     Active ads: {p.get('active_ads_count', '?')} ({p.get('active_ads_signal', '?')})", flush=True)
            print(f"     Days running: {p.get('active_days', '?')}", flush=True)
            print(f"     Marina signal: {p.get('marina_signal', 'unknown')}", flush=True)
            print(f"     Impressions: {p.get('impressions', '?')}", flush=True)
            print(f"     Store: {p.get('store_url', 'N/A')}", flush=True)
            print(f"     Raw: {p.get('raw_text', '')[:200]}", flush=True)
    else:
        print("[!] No products — check logs/screenshots/", flush=True)

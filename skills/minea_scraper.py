#!/usr/bin/env python3
"""
Minea Scraper — grabs winning product data from Minea.com
Outputs JSON list of products for Claude to analyze.
"""

import json
import os
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

# Load credentials
def load_env():
    env_path = Path(__file__).parent.parent / ".env"
    env = {}
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    # Also check environment variables (override .env)
    for key in ["MINEA_EMAIL", "MINEA_PASSWORD"]:
        if key in os.environ:
            env[key] = os.environ[key]
    return env

def save_debug_screenshot(page, name):
    screenshots_dir = Path("/opt/market-research-agent/logs/screenshots")
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    path = screenshots_dir / f"{name}.png"
    page.screenshot(path=str(path))
    print(f"[DEBUG] Screenshot saved: {path}", flush=True)

def scrape_minea(max_products=20, category="health", market="US"):
    env = load_env()
    email = env.get("MINEA_EMAIL", "")
    password = env.get("MINEA_PASSWORD", "")

    if not email or not password:
        print("[ERROR] MINEA_EMAIL or MINEA_PASSWORD not found in .env", flush=True)
        sys.exit(1)

    products = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
        )
        context = browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        try:
            # ── Step 1: Login ──────────────────────────────────────────────
            print("[1/5] Navigating to Minea login...", flush=True)
            page.goto("https://app.minea.com/login", wait_until="networkidle", timeout=30000)
            save_debug_screenshot(page, "01_login_page")

            # Fill email
            page.wait_for_selector('input[type="email"], input[name="email"], input[placeholder*="mail"]', timeout=10000)
            email_input = page.locator('input[type="email"], input[name="email"], input[placeholder*="mail"]').first
            email_input.fill(email)
            time.sleep(0.5)

            # Fill password
            password_input = page.locator('input[type="password"]').first
            password_input.fill(password)
            time.sleep(0.5)

            save_debug_screenshot(page, "02_credentials_filled")

            # Submit
            submit_btn = page.locator('button[type="submit"], button:has-text("Login"), button:has-text("Sign in"), button:has-text("Se connecter")').first
            submit_btn.click()

            print("[2/5] Logging in...", flush=True)
            page.wait_for_load_state("networkidle", timeout=20000)
            time.sleep(2)
            save_debug_screenshot(page, "03_after_login")

            current_url = page.url
            print(f"[INFO] After login URL: {current_url}", flush=True)

            if "login" in current_url.lower():
                print("[ERROR] Still on login page — check credentials or CAPTCHA", flush=True)
                save_debug_screenshot(page, "03_login_failed")
                sys.exit(1)

            # ── Step 2: Navigate to Facebook Ads / Products ───────────────
            print("[3/5] Navigating to winning products...", flush=True)

            # Try Facebook ads section (most ad data)
            try:
                page.goto("https://app.minea.com/facebook-ads", wait_until="networkidle", timeout=20000)
            except PlaywrightTimeout:
                page.goto("https://app.minea.com/products", wait_until="networkidle", timeout=20000)

            time.sleep(2)
            save_debug_screenshot(page, "04_products_page")
            print(f"[INFO] Products page URL: {page.url}", flush=True)

            # ── Step 3: Apply filters ─────────────────────────────────────
            print("[4/5] Applying filters...", flush=True)

            # Try to set market to US
            try:
                country_filter = page.locator('[data-testid="country-filter"], button:has-text("Country"), select[name="country"]').first
                if country_filter.is_visible(timeout=3000):
                    country_filter.click()
                    time.sleep(1)
                    us_option = page.locator('li:has-text("United States"), option[value="US"], [data-value="US"]').first
                    if us_option.is_visible(timeout=3000):
                        us_option.click()
                        time.sleep(1)
            except Exception:
                print("[INFO] Country filter not found or already set", flush=True)

            # Sort by most recent or trending
            try:
                sort_btn = page.locator('button:has-text("Sort"), button:has-text("Trier"), [data-testid="sort"]').first
                if sort_btn.is_visible(timeout=3000):
                    sort_btn.click()
                    time.sleep(0.5)
                    trending = page.locator('li:has-text("Trending"), li:has-text("Popular"), li:has-text("Recent")').first
                    if trending.is_visible(timeout=2000):
                        trending.click()
                        time.sleep(1)
            except Exception:
                print("[INFO] Sort filter not found, using default order", flush=True)

            save_debug_screenshot(page, "05_filters_applied")
            page.wait_for_load_state("networkidle", timeout=10000)

            # ── Step 4: Scrape products ───────────────────────────────────
            print("[5/5] Scraping product cards...", flush=True)
            time.sleep(2)

            # Try multiple possible card selectors
            card_selectors = [
                ".product-card",
                "[data-testid='product-card']",
                ".ad-card",
                ".product-item",
                "[class*='ProductCard']",
                "[class*='product-card']",
                "[class*='AdCard']",
                "article",
            ]

            cards = []
            for selector in card_selectors:
                found = page.locator(selector).all()
                if found:
                    cards = found
                    print(f"[INFO] Found {len(cards)} cards with selector: {selector}", flush=True)
                    break

            if not cards:
                print("[WARN] No product cards found — saving full page HTML for debug", flush=True)
                html_path = Path("/opt/market-research-agent/logs/minea_page.html")
                html_path.write_text(page.content())
                save_debug_screenshot(page, "06_no_cards_found")
                browser.close()
                return []

            for i, card in enumerate(cards[:max_products]):
                try:
                    product = {}

                    # Product name / title
                    title_el = card.locator("h2, h3, h4, [class*='title'], [class*='name'], [class*='Title']").first
                    product["name"] = title_el.inner_text().strip() if title_el.count() > 0 else ""

                    # Price
                    price_el = card.locator("[class*='price'], [class*='Price'], span:has-text('$')").first
                    product["price"] = price_el.inner_text().strip() if price_el.count() > 0 else ""

                    # Ad metrics (likes, shares, views)
                    metrics_text = card.inner_text()
                    product["raw_text"] = metrics_text[:500]  # first 500 chars for Claude analysis

                    # Store/brand link
                    link_el = card.locator("a").first
                    product["link"] = link_el.get_attribute("href") if link_el.count() > 0 else ""

                    # Image
                    img_el = card.locator("img").first
                    product["image"] = img_el.get_attribute("src") if img_el.count() > 0 else ""

                    if product.get("name") or product.get("raw_text"):
                        products.append(product)
                        print(f"  [{i+1}] Scraped: {product.get('name', 'no-name')[:50]}", flush=True)

                except Exception as e:
                    print(f"  [{i+1}] Error scraping card: {e}", flush=True)
                    continue

        except PlaywrightTimeout as e:
            print(f"[ERROR] Timeout: {e}", flush=True)
            save_debug_screenshot(page, "error_timeout")
        except Exception as e:
            print(f"[ERROR] Unexpected error: {e}", flush=True)
            save_debug_screenshot(page, "error_unexpected")
        finally:
            browser.close()

    return products


if __name__ == "__main__":
    print("=== Minea Scraper ===", flush=True)
    results = scrape_minea(max_products=20)

    output_path = Path("/opt/market-research-agent/logs/minea_results.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(results, ensure_ascii=False, indent=2))

    print(f"\n=== Done: {len(results)} products scraped ===", flush=True)
    print(f"Results saved to: {output_path}", flush=True)

    # Print summary for Claude to read
    if results:
        print("\n=== PRODUCT LIST FOR CLAUDE ANALYSIS ===", flush=True)
        for i, p in enumerate(results, 1):
            print(f"\n[{i}] {p.get('name', 'Unknown')}", flush=True)
            print(f"    Price: {p.get('price', 'N/A')}", flush=True)
            print(f"    Link: {p.get('link', 'N/A')}", flush=True)
            print(f"    Data: {p.get('raw_text', '')[:200]}", flush=True)
    else:
        print("\n[!] No products found — check screenshots in logs/screenshots/", flush=True)

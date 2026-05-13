#!/usr/bin/env python3
"""
Facebook Ads Library Scraper — stealth browser automation
Searches for active ads by keyword, country=US, status=active.
Outputs JSON list of advertisers + ad data for Claude to analyze.
"""

import json
import re
import os
import sys
import time
import random
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout


# ── Helpers ───────────────────────────────────────────────────────────────────

def load_env():
    env_path = Path(__file__).parent.parent / ".env"
    env = {}
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env


def save_screenshot(page, name):
    path = Path("/opt/market-research-agent/logs/screenshots") / f"{name}.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(path))
    print(f"[DEBUG] Screenshot: {path}", flush=True)


def human_delay(min_s=0.8, max_s=2.5):
    """Random human-like pause between actions."""
    time.sleep(random.uniform(min_s, max_s))


def human_scroll(page, steps=5):
    """Scroll down incrementally like a human, not jump to bottom."""
    for _ in range(steps):
        scroll_amount = random.randint(300, 700)
        page.mouse.wheel(0, scroll_amount)
        time.sleep(random.uniform(0.4, 1.2))


def accept_cookies(page):
    """Dismiss cookie/consent banners if present."""
    cookie_selectors = [
        'button:has-text("Allow all cookies")',
        'button:has-text("Accept all")',
        'button:has-text("Accept")',
        '[data-cookiebanner="accept_button"]',
        'button[title="Accept all"]',
    ]
    for sel in cookie_selectors:
        try:
            btn = page.locator(sel).first
            if btn.is_visible(timeout=2000):
                btn.click()
                print(f"[COOKIES] Accepted via: {sel}", flush=True)
                human_delay(1, 2)
                return
        except Exception:
            continue


def build_search_url(keyword: str, country: str = "US", active_only: bool = True) -> str:
    active_status = "active" if active_only else "all"
    keyword_encoded = keyword.replace(" ", "+")
    return (
        f"https://www.facebook.com/ads/library/"
        f"?active_status={active_status}"
        f"&ad_type=all"
        f"&country={country}"
        f"&q={keyword_encoded}"
        f"&search_type=keyword_search"
        f"&media_type=all"
    )


# ── Core scraping ──────────────────────────────────────────────────────────────

def parse_ad_cards(page) -> list[dict]:
    """Extract structured data from visible ad cards."""
    ads = []

    # Primary selector used by Facebook Ads Library (as of 2026)
    card_selectors = [
        '[data-testid="ad_archive_results"] > div',
        'div[class*="AdLibraryResultsItem"]',
        'div[class*="x1lliihq"]',  # common FB class pattern
        'div[data-ad-preview]',
    ]

    cards = []
    for sel in card_selectors:
        cards = page.locator(sel).all()
        if cards:
            print(f"[PARSE] Found {len(cards)} cards via: {sel}", flush=True)
            break

    if not cards:
        # Fallback: grab all large divs that contain ad metadata text
        raw_text = page.inner_text("body")
        print(f"[PARSE] No card selector matched. Page text length: {len(raw_text)}", flush=True)
        return []

    for i, card in enumerate(cards[:25]):
        try:
            raw = card.inner_text().strip()
            if len(raw) < 20:
                continue

            ad = {
                "raw_text": raw[:1000],
                "source": "Facebook Ads Library",
                "search_url": page.url,
            }

            lines = [ln.strip() for ln in raw.split("\n") if ln.strip()]

            # Advertiser name (usually first non-empty line)
            ad["advertiser"] = lines[0] if lines else ""

            # Start date — "Started running on DD Month YYYY"
            date_match = re.search(
                r"[Ss]tarted running on\s+(\d{1,2}\s+\w+\s+\d{4})", raw
            )
            if date_match:
                ad["started_running"] = date_match.group(1)

            # Active status
            ad["is_active"] = "Active" in raw or "active" in raw.lower()

            # Platforms
            platforms = []
            for platform in ["Facebook", "Instagram", "Messenger", "Audience Network"]:
                if platform.lower() in raw.lower():
                    platforms.append(platform)
            ad["platforms"] = platforms

            # Number of active ads by this advertiser
            count_match = re.search(r"(\d+)\s+ads?\s+use this", raw, re.IGNORECASE)
            if not count_match:
                count_match = re.search(r"(\d+)\s+active ads?", raw, re.IGNORECASE)
            if count_match:
                ad["active_ads_count"] = int(count_match.group(1))

            # Country signals in ad text
            for country in ["United States", "United Kingdom", "Canada", "Australia"]:
                if country in raw:
                    ad["country_signal"] = country
                    break

            # Ad copy snippet (look for "free shipping" or offer language)
            ad_copy_match = re.search(
                r"(free shipping|get \d+% off|limited time|buy now|shop now)[^\n]{0,120}",
                raw, re.IGNORECASE
            )
            if ad_copy_match:
                ad["offer_text"] = ad_copy_match.group(0).strip()

            # Store URL from card links
            try:
                links = card.locator("a[href]").all()
                for link in links:
                    href = link.get_attribute("href") or ""
                    if href and "facebook.com" not in href and href.startswith("http"):
                        ad["store_url"] = href
                        break
            except Exception:
                pass

            # Running duration signal
            run_match = re.search(
                r"(\d+)\s+(day|week|month)s?\s+ago", raw, re.IGNORECASE
            )
            if run_match:
                ad["running_since"] = f"{run_match.group(1)} {run_match.group(2)}(s) ago"

            ads.append(ad)
            print(
                f"  [{i+1}] {ad.get('advertiser', 'unknown')[:40]} | "
                f"active_ads: {ad.get('active_ads_count', '?')} | "
                f"started: {ad.get('started_running', '?')} | "
                f"platforms: {ad.get('platforms', [])}",
                flush=True,
            )

        except Exception as e:
            print(f"  [{i+1}] Parse error: {e}", flush=True)
            continue

    return ads


# ── Main scrape flow ───────────────────────────────────────────────────────────

def scrape_facebook_ads(
    keywords: list[str],
    country: str = "US",
    max_per_keyword: int = 20,
) -> list[dict]:
    """
    Scrape Facebook Ads Library for each keyword.
    Returns combined list of ad records.
    """
    all_ads = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
                "--disable-blink-features=AutomationControlled",  # key stealth flag
                "--disable-web-security",
                "--disable-features=IsolateOrigins,site-per-process",
                "--window-size=1440,900",
            ],
        )

        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            locale="en-US",
            timezone_id="America/New_York",
            # Pretend to be a real browser with common headers
            extra_http_headers={
                "Accept-Language": "en-US,en;q=0.9",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            },
        )

        # Remove webdriver traces — key stealth patch
        context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
            Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3] });
            Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
            window.chrome = { runtime: {} };
        """)

        page = context.new_page()

        for keyword in keywords:
            print(f"\n[KEYWORD] Searching: '{keyword}' | country={country}", flush=True)
            url = build_search_url(keyword, country=country, active_only=True)
            print(f"[URL] {url}", flush=True)

            try:
                # Navigate with realistic timeout
                page.goto(url, wait_until="domcontentloaded", timeout=30000)
                human_delay(2, 4)

                # Accept cookies on first visit
                accept_cookies(page)
                save_screenshot(page, f"01_loaded_{keyword.replace(' ', '_')[:20]}")

                # Check for blocking / login wall
                page_text = page.inner_text("body")
                if "log in" in page_text.lower() and len(page_text) < 1000:
                    print("[WARN] Login wall detected — results may be limited", flush=True)
                    save_screenshot(page, "blocked_login_wall")

                # Human-like scroll to load more cards
                human_scroll(page, steps=random.randint(4, 7))
                human_delay(1.5, 3)
                save_screenshot(page, f"02_scrolled_{keyword.replace(' ', '_')[:20]}")

                # Parse cards
                ads = parse_ad_cards(page)
                print(f"[RESULT] {len(ads)} ads found for '{keyword}'", flush=True)

                # Tag with keyword
                for ad in ads:
                    ad["keyword"] = keyword

                all_ads.extend(ads[:max_per_keyword])

                # Human-like pause between keywords
                if keyword != keywords[-1]:
                    human_delay(3, 6)

            except PlaywrightTimeout as e:
                print(f"[ERROR] Timeout on '{keyword}': {e}", flush=True)
                save_screenshot(page, f"error_timeout_{keyword[:15]}")
            except Exception as e:
                print(f"[ERROR] '{keyword}': {e}", flush=True)
                save_screenshot(page, f"error_{keyword[:15]}")
                continue

        browser.close()

    return all_ads


# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Keywords to search — passed as CLI args or use defaults
    if len(sys.argv) > 1:
        keywords = sys.argv[1:]
    else:
        keywords = ["free shipping"]  # default first query

    print(f"=== Facebook Ads Library Scraper ===", flush=True)
    print(f"Keywords: {keywords}", flush=True)
    print(f"Country: US | Status: Active only", flush=True)

    results = scrape_facebook_ads(keywords=keywords, country="US", max_per_keyword=20)

    output_path = Path("/opt/market-research-agent/logs/facebook_ads_results.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(results, ensure_ascii=False, indent=2))

    print(f"\n=== Done: {len(results)} ads total ===", flush=True)
    print(f"Saved to: {output_path}", flush=True)

    if results:
        print("\n=== ADS FOR CLAUDE ===", flush=True)
        for i, ad in enumerate(results, 1):
            print(f"\n[{i}] Advertiser: {ad.get('advertiser', '?')}", flush=True)
            print(f"     Keyword: {ad.get('keyword', '?')}", flush=True)
            print(f"     Started: {ad.get('started_running', '?')}", flush=True)
            print(f"     Active ads: {ad.get('active_ads_count', '?')}", flush=True)
            print(f"     Platforms: {ad.get('platforms', [])}", flush=True)
            print(f"     Offer: {ad.get('offer_text', 'N/A')}", flush=True)
            print(f"     Store: {ad.get('store_url', 'N/A')}", flush=True)
    else:
        print("[!] No ads found — check logs/screenshots/", flush=True)

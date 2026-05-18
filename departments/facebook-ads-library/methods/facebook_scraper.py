#!/usr/bin/env python3
"""
Facebook Ads Library Scraper — stealth browser automation
Searches for active ads by keyword, country=US, status=active.
Outputs JSON list of advertisers + ad data for Claude to analyze.

CLI flags:
  --since=YYYY-MM-DD    Only ads started on or after this date (fresher brands)
  --deep                Scroll to ~500-580 ads/keyword (target 500, hard cap 600)
  --seen=FILE           Path to seen-advertisers.md — skip already-analyzed store domains
  --video               Only video ads (better for demo products)
  --sort=recent         Sort by "Most recent" (newest launches first)
  --sort=impressions    Sort by "Impressions: high to low" (proven winners)
  --output=PATH         Save JSON output to this path (default: logs/facebook_ads_TIMESTAMP.json)
  (default: no sort click = FB default which is "Impressions: high to low")

Sort option UI labels verified on live FB Ads Library 2026-05-15:
  "Most recent"            → newest ad launches first (catches fresh 2026 DTC entrants)
  "Impressions: high to low" → highest impression count first (proven winners, longest running)
If UI labels have changed — scraper will print a warning and proceed without sorting.

Examples:
  python3 skills/facebook_scraper.py "travel pillow" "car organizer"
  python3 skills/facebook_scraper.py --deep "travel pillow"
  python3 skills/facebook_scraper.py --since=2026-01-01 --seen=memory/seen-advertisers.md "desk organizer"
  python3 skills/facebook_scraper.py --deep --sort=recent --since=2026-01-01 "baby"
  python3 skills/facebook_scraper.py --deep --output=/tmp/results.json "baby carrier"
"""

import json
import re
import sys
import time
import random
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout


# ── Affiliate noise detection ──────────────────────────────────────────────────

# Patterns that identify pure affiliate noise (no product to extract)
AFFILIATE_NOISE_PATTERNS = [
    r"comment\s+[\"']?\w+[\"']?\s+and\s+(i'?ll|i will)\s+(send|dm|message)\s+you",
    r"comment\s+[\"']?\w+[\"']?\s+and\s+i'?ll\s+send",
    r"drop\s+[\"']?\w+[\"']?\s+and\s+i'?ll\s+(send|dm)",
]

# Advertiser name suffixes that identify Amazon affiliate accounts
AFFILIATE_ADVERTISER_SUFFIXES = [
    "with amazon.com",
    "with amazon associates",
    "with amazon home",
    "with markable creators",
    "with markable",
    "with shoptemu",
    "with ftl",
]


def is_affiliate_noise(ad: dict) -> tuple[bool, str]:
    """
    Detect pure affiliate noise vs. real product ads.
    Returns (is_noise, reason).

    Rule: skip if it's a comment-for-link affiliate AND has no extractable product.
    Keep if the ad shows a specific product even if sold on Amazon.
    """
    advertiser = (ad.get("advertiser") or "").lower().strip()
    ad_copy = (ad.get("ad_copy") or "").lower()
    store_url = (ad.get("store_url") or "").lower()

    # Check for Amazon affiliate account name pattern
    for suffix in AFFILIATE_ADVERTISER_SUFFIXES:
        if advertiser.endswith(suffix):
            # Still keep if specific product is visible in copy (not just "comment for link")
            has_comment_pattern = any(
                re.search(p, ad_copy) for p in AFFILIATE_NOISE_PATTERNS
            )
            if has_comment_pattern:
                return True, f"affiliate noise: '{suffix}' + comment-for-link pattern"
            else:
                # Amazon affiliate but shows a specific product — keep it
                return False, ""

    # Pure comment-for-link without product context
    for pattern in AFFILIATE_NOISE_PATTERNS:
        if re.search(pattern, ad_copy):
            if "amazon.com" in store_url or "amzlink" in store_url or "markable" in store_url:
                return True, "comment-for-link affiliate with Amazon store"

    return False, ""


# ── Seen advertisers filter ────────────────────────────────────────────────────

def load_seen_domains(filepath: str) -> set:
    """Load previously-analyzed store domains from seen-advertisers.md."""
    seen = set()
    try:
        with open(filepath) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or line.startswith("Format:") or line.startswith("---") or line.startswith("##") or line.startswith("Pass") or line.startswith("Scraper"):
                    continue
                domain = line.split("|")[0].strip().lower()
                if domain and "." in domain:
                    seen.add(domain)
        print(f"[SEEN] Loaded {len(seen)} known domains to skip", flush=True)
    except FileNotFoundError:
        print(f"[SEEN] File not found: {filepath} — running without seen filter", flush=True)
    return seen


def is_seen(ad: dict, seen_domains: set) -> bool:
    """Check if this ad's store domain was already analyzed."""
    store_url = (ad.get("store_url") or "").lower()
    store_domain = (ad.get("store_domain") or "").lower()
    for domain in seen_domains:
        if domain in store_url or domain in store_domain:
            return True
    return False


def apply_sort(page, sort_mode: str):
    """
    Click the FB Ads Library 'Sort by' dropdown and select a sort option.
    sort_mode: 'recent' → 'Most recent' | 'impressions' → 'Impressions: high to low'
    Verified UI labels: 2026-05-15. If labels changed, logs warning and skips.
    """
    SORT_LABELS = {
        "recent": "Most recent",
        "impressions": "Impressions: high to low",
    }
    target_label = SORT_LABELS.get(sort_mode)
    if not target_label:
        print(f"[SORT] Unknown sort mode '{sort_mode}' — skipping", flush=True)
        return

    try:
        # Find Sort by button (must be in top-right of results area)
        sort_btn = None
        elements = page.locator('div:text-is("Sort by")').all()
        for el in elements:
            bb = el.bounding_box()
            if bb and bb['x'] > 900 and bb['y'] < 400:
                sort_btn = el
                break

        if not sort_btn:
            print(f"[SORT] 'Sort by' button not found — proceeding without sort", flush=True)
            return

        sort_btn.click()
        time.sleep(1.5)

        # Click the target sort option
        option = page.locator(f'text="{target_label}"').first
        if option.is_visible(timeout=3000):
            option.click()
            time.sleep(2)
            print(f"[SORT] Applied: '{target_label}'", flush=True)
        else:
            # UI labels may have changed
            print(f"[SORT] WARNING: Option '{target_label}' not found in dropdown.", flush=True)
            print(f"[SORT] UI labels may have changed — screenshot saved, proceeding without sort.", flush=True)
            save_screenshot(page, "sort_label_changed")
            # Close dropdown by pressing Escape
            page.keyboard.press("Escape")

    except Exception as e:
        print(f"[SORT] Error applying sort: {e} — proceeding without sort", flush=True)


def save_screenshot(page, name):
    path = Path("/opt/market-research-agent/logs/screenshots") / f"{name}.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(path))
    print(f"[DEBUG] Screenshot: {path}", flush=True)


def human_delay(min_s=0.8, max_s=2.5):
    """Random human-like pause between actions."""
    time.sleep(random.uniform(min_s, max_s))


def human_scroll(page, steps=5, deep=False):
    """Scroll down using JS window.scrollBy — triggers FB lazy-load unlike mouse.wheel.
    Deep mode: 20-30 steps; normal: steps param.
    """
    actual_steps = random.randint(20, 30) if deep else steps
    for i in range(actual_steps):
        scroll_amount = random.randint(600, 1000)
        page.evaluate(f"window.scrollBy(0, {scroll_amount})")
        pause = random.uniform(0.8, 1.8) if deep else random.uniform(0.5, 1.2)
        time.sleep(pause)
        if deep and (i + 1) % 5 == 0:
            time.sleep(random.uniform(1.2, 2.0))


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


def build_search_url(keyword: str, country: str = "US", active_only: bool = True,
                     since_date: str = "", video_only: bool = False) -> str:
    active_status = "active" if active_only else "all"
    keyword_encoded = keyword.replace(" ", "+")
    media_type = "video" if video_only else "all"
    url = (
        f"https://www.facebook.com/ads/library/"
        f"?active_status={active_status}"
        f"&ad_type=all"
        f"&country={country}"
        f"&q={keyword_encoded}"
        f"&search_type=keyword_search"
        f"&media_type={media_type}"
    )
    if since_date:
        url += f"&start_date[min]={since_date}"
    return url


# ── Core scraping ──────────────────────────────────────────────────────────────

def parse_ad_cards(page) -> list[dict]:
    """
    Extract structured data from visible ad cards using JS DOM traversal.
    Facebook uses auto-generated CSS classes that change — content-based extraction is reliable.
    Strategy: find all 'Library ID:' text nodes, walk up DOM to the card container,
    extract full card text.
    """
    ads = []

    # JS: find each 'Library ID:' span, walk up until we find the card root
    # (identified by also containing 'See ad details' or 'See summary details')
    raw_cards = page.evaluate("""
        () => {
            const results = [];
            const spans = Array.from(document.querySelectorAll('span, div'));
            const libSpans = spans.filter(el =>
                el.childNodes.length === 1 &&
                el.childNodes[0].nodeType === Node.TEXT_NODE &&
                el.textContent.trim().startsWith('Library ID:')
            );

            for (const span of libSpans) {
                let el = span;
                let card = null;
                for (let i = 0; i < 25; i++) {
                    el = el.parentElement;
                    if (!el || el === document.body) break;
                    const txt = el.innerText || '';
                    if (txt.includes('See ad details') || txt.includes('See summary details')) {
                        card = el;
                        break;
                    }
                }
                if (card) {
                    // Get store links from within the card
                    const links = Array.from(card.querySelectorAll('a[href]'))
                        .map(a => a.href)
                        .filter(h => h && !h.includes('facebook.com') && h.startsWith('http'));
                    results.push({
                        text: (card.innerText || '').substring(0, 1200),
                        links: links.slice(0, 3)
                    });
                }
            }
            return results;
        }
    """)

    print(f"[PARSE] JS extracted {len(raw_cards)} ad cards", flush=True)

    if not raw_cards:
        print("[PARSE] No cards found — check screenshot for page state", flush=True)
        return []

    for i, card_data in enumerate(raw_cards):
        try:
            raw = card_data.get("text", "").strip()
            if len(raw) < 30:
                continue

            ad = {
                "raw_text": raw[:1000],
                "source": "Facebook Ads Library",
                "search_url": page.url,
                "store_links": card_data.get("links", []),
            }

            lines = [ln.strip() for ln in raw.split("\n") if ln.strip()]

            # Card structure (confirmed from DOM inspection 2026-05-15):
            # Active → Library ID → Started running → Platforms → See ad details
            # → ADVERTISER NAME → Sponsored → AD COPY → DOMAIN.COM → Shop now

            # Advertiser: first non-empty line after "See ad details" / "See summary details"
            advertiser = ""
            ad_copy = ""
            store_domain = ""
            found_details = False
            found_sponsored = False
            copy_lines = []

            for line in lines:
                if line in ("See ad details", "See summary details"):
                    found_details = True
                    continue
                if found_details and not advertiser:
                    advertiser = line
                    continue
                if found_details and advertiser and line == "Sponsored":
                    found_sponsored = True
                    continue
                if found_sponsored:
                    # Store domain: ALL-CAPS line that looks like a domain
                    if line.isupper() and "." in line and len(line) < 40:
                        store_domain = line
                        break
                    # Skip UI buttons
                    if line in ("Shop now", "Shop Now", "Learn more", "Get offer", "Sign up"):
                        continue
                    copy_lines.append(line)

            ad["advertiser"] = advertiser
            ad["ad_copy"] = " ".join(copy_lines)[:300]
            ad["store_domain"] = store_domain
            ad["store_url"] = f"https://{store_domain.lower()}" if store_domain else "Not found"

            # Start date — FB format: "Jun 12, 2024" (Mon DD, YYYY)
            date_match = re.search(
                r"[Ss]tarted running on\s+(\w{3,9}\s+\d{1,2},\s+\d{4})", raw
            )
            if not date_match:
                # Fallback: "12 Jun 2024" format (DD Mon YYYY)
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

            # Number of ads using this creative: "2 ads use this creative" or "1 ad uses this"
            count_match = re.search(r"(\d+)\s+ad[s]?\s+uses?\s+this", raw, re.IGNORECASE)
            if not count_match:
                count_match = re.search(r"(\d+)\s+active ads?", raw, re.IGNORECASE)
            if count_match:
                ad["active_ads_count"] = int(count_match.group(1))
            elif re.search(r"this ad has multiple versions", raw, re.IGNORECASE):
                ad["active_ads_count"] = "2+"
            elif "See ad details" in raw and "See summary details" not in raw:
                ad["active_ads_count"] = 1  # single-version ad

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

            # Store URL: prefer JS-extracted href links, fallback to domain text from ad copy
            store_links = ad.get("store_links", [])
            if store_links:
                ad["store_url"] = store_links[0]
            elif ad.get("store_domain"):
                ad["store_url"] = f"https://{ad['store_domain'].lower()}"
            # else: store_url already set in parsing block above

            # Running duration signal
            run_match = re.search(
                r"(\d+)\s+(day|week|month)s?\s+ago", raw, re.IGNORECASE
            )
            if run_match:
                ad["running_since"] = f"{run_match.group(1)} {run_match.group(2)}(s) ago"

            ads.append(ad)
            print(
                f"  [{i+1}] {ad.get('advertiser', '?')[:35]} | "
                f"started: {ad.get('started_running', '?')} | "
                f"active_ads: {ad.get('active_ads_count', '?')} | "
                f"domain: {ad.get('store_domain', '?')}",
                flush=True,
            )

        except Exception as e:
            print(f"  [{i+1}] Parse error: {e}", flush=True)
            continue

    return ads


# ── Incremental scroll + collect (handles FB virtual DOM recycling) ────────────

def incremental_scroll_collect(page, target: int = 500, deep: bool = False) -> list[dict]:
    """
    Scroll and parse in batches. FB removes old cards from DOM as you scroll down —
    parsing only at the end loses them. This captures every card before it disappears.
    Returns deduplicated list of ad dicts (keyed by Library ID).
    """
    collected = {}          # library_id (or fallback key) → ad dict
    batch_size = 5          # scroll steps between each parse
    max_batches = 60 if deep else 12   # deep → up to 300 scroll steps; normal → 60
    no_new_streak = 0

    for batch in range(max_batches):
        # Scroll one batch of steps using JS (triggers FB lazy-load; mouse.wheel does not)
        for _ in range(batch_size):
            scroll_amount = random.randint(600, 1000)
            page.evaluate(f"window.scrollBy(0, {scroll_amount})")
            time.sleep(random.uniform(0.8, 1.8) if deep else random.uniform(0.5, 1.2))

        # Extra pause every 3 batches so FB can lazy-load more content
        if (batch + 1) % 3 == 0:
            time.sleep(random.uniform(1.5, 2.5))

        # Parse whatever is currently in the DOM
        batch_ads = parse_ad_cards(page)
        new_count = 0
        for ad in batch_ads:
            raw = ad.get("raw_text", "")
            lib_match = re.search(r"Library ID:\s*(\d+)", raw)
            key = lib_match.group(1) if lib_match else (ad.get("advertiser", "") + f"_b{batch}")
            if key and key not in collected:
                collected[key] = ad
                new_count += 1

        total = len(collected)
        print(
            f"[SCROLL] Batch {batch + 1}/{max_batches}: +{new_count} new → {total} unique ads",
            flush=True,
        )

        if new_count == 0:
            no_new_streak += 1
            if no_new_streak >= 5:
                print(f"[SCROLL] No new cards in 5 consecutive batches — stopping at {total}", flush=True)
                break
        else:
            no_new_streak = 0

        if total >= target:
            print(f"[SCROLL] Target {target} reached — stopping", flush=True)
            break

    return list(collected.values())


# ── Main scrape flow ───────────────────────────────────────────────────────────

def deduplicate(ads: list[dict]) -> list[dict]:
    """Remove duplicate advertisers across keywords — keep the one with more data."""
    seen = {}
    for ad in ads:
        key = (ad.get("advertiser", "").lower().strip() or
               ad.get("store_domain", "").lower().strip())
        if not key or key in ("?", ""):
            continue
        if key not in seen:
            seen[key] = ad
        else:
            existing = seen[key]
            # Keep whichever has more fields filled
            if len([v for v in ad.values() if v]) > len([v for v in existing.values() if v]):
                seen[key] = ad
    unique = list(seen.values())
    print(f"[DEDUP] {len(ads)} ads → {len(unique)} unique advertisers", flush=True)
    return unique


def scrape_facebook_ads(
    keywords: list[str],
    country: str = "US",
    max_per_keyword: int = 20,
    since_date: str = "",
    deep: bool = False,
    seen_domains: set = None,
    video_only: bool = False,
    sort_mode: str = "",
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

        # Load saved FB session if available (enables full 500+ ad access)
        session_file = Path("/opt/market-research-agent/cookies/fb_session.json")
        session_kwargs = {"storage_state": str(session_file)} if session_file.exists() else {}
        if session_file.exists():
            print(f"[SESSION] Loaded FB session from {session_file}", flush=True)
        else:
            print("[SESSION] No session file — running without login (limited to ~28 ads)", flush=True)

        context = browser.new_context(
            **session_kwargs,
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

        seen_domains = seen_domains or set()

        for keyword in keywords:
            print(f"\n[KEYWORD] Searching: '{keyword}' | country={country} | deep={deep}", flush=True)
            url = build_search_url(keyword, country=country, active_only=True,
                                   since_date=since_date, video_only=video_only)
            print(f"[URL] {url}", flush=True)
            try:
                # Navigate with realistic timeout
                page.goto(url, wait_until="domcontentloaded", timeout=30000)
                human_delay(2, 4)

                # Accept cookies on first visit
                accept_cookies(page)

                # Dismiss "automated behavior" warning if Facebook shows it
                try:
                    dismiss_btn = page.locator('div[role="button"]:has-text("Dismiss")')
                    if dismiss_btn.count() > 0:
                        dismiss_btn.first.click()
                        print("[SESSION] Dismissed automated behavior warning", flush=True)
                        human_delay(1, 2)
                except Exception:
                    pass

                save_screenshot(page, f"01_loaded_{keyword.replace(' ', '_')[:20]}")

                # Apply sort if requested (after page load, before scrolling)
                if sort_mode:
                    apply_sort(page, sort_mode)
                    human_delay(1, 2)

                # Check for blocking / login wall
                page_text = page.inner_text("body")
                if "log in" in page_text.lower() and len(page_text) < 1000:
                    print("[WARN] Login wall detected — results may be limited", flush=True)
                    save_screenshot(page, "blocked_login_wall")

                # Warm-up: FB React renders cards lazily — scroll down 3 steps then back
                # to top before main loop, so first batch always finds loaded cards.
                print("[SCROLL] Warm-up: triggering FB initial card render...", flush=True)
                for _ in range(3):
                    page.evaluate("window.scrollBy(0, 800)")
                    time.sleep(1.5)
                page.evaluate("window.scroll(0, 0)")
                time.sleep(3)

                # Scroll incrementally and collect cards before FB virtual DOM removes them
                target_ads = 500 if deep else 50
                ads = incremental_scroll_collect(page, target=target_ads, deep=deep)
                save_screenshot(page, f"02_scrolled_{keyword.replace(' ', '_')[:20]}")
                print(f"[RESULT] {len(ads)} raw ads found for '{keyword}'", flush=True)

                # Apply filters: seen domains + affiliate noise
                filtered = []
                skipped_seen = 0
                skipped_affiliate = 0
                for ad in ads:
                    ad["keyword"] = keyword

                    # Skip already-seen advertisers
                    if seen_domains and is_seen(ad, seen_domains):
                        skipped_seen += 1
                        continue

                    # Skip pure affiliate noise (but keep Amazon ads with real products)
                    noise, reason = is_affiliate_noise(ad)
                    if noise:
                        skipped_affiliate += 1
                        print(f"  [SKIP affiliate] {ad.get('advertiser', '?')[:30]} — {reason}", flush=True)
                        continue

                    filtered.append(ad)

                print(f"[FILTER] Skipped {skipped_seen} seen + {skipped_affiliate} affiliate noise "
                      f"→ {len(filtered)} remain for '{keyword}'", flush=True)

                all_ads.extend(filtered[:max_per_keyword])

                # Anti-detection pause between keywords: 30-60s (was 3-6s)
                if keyword != keywords[-1]:
                    pause = random.uniform(30, 60)
                    print(f"[PAUSE] {pause:.0f}s between keywords (anti-detection)...", flush=True)
                    time.sleep(pause)

            except PlaywrightTimeout as e:
                print(f"[ERROR] Timeout on '{keyword}': {e}", flush=True)
                save_screenshot(page, f"error_timeout_{keyword[:15]}")
            except Exception as e:
                print(f"[ERROR] '{keyword}': {e}", flush=True)
                save_screenshot(page, f"error_{keyword[:15]}")
                continue

        browser.close()

    return deduplicate(all_ads)


# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Parse CLI flags before keywords
    since_date = ""
    deep = False
    seen_file = ""
    video_only = False
    sort_mode = ""
    output_file = ""
    args = sys.argv[1:]

    remaining = []
    for arg in args:
        if arg.startswith("--since="):
            since_date = arg.split("=", 1)[1]
        elif arg == "--deep":
            deep = True
        elif arg.startswith("--seen="):
            seen_file = arg.split("=", 1)[1]
        elif arg == "--video":
            video_only = True
        elif arg.startswith("--sort="):
            sort_mode = arg.split("=", 1)[1]
        elif arg.startswith("--output="):
            output_file = arg.split("=", 1)[1]
        else:
            remaining.append(arg)

    keywords = remaining if remaining else ["free shipping"]

    # Load seen domains if file provided
    seen_domains = load_seen_domains(seen_file) if seen_file else set()

    print(f"=== Facebook Ads Library Scraper ===", flush=True)
    print(f"Keywords: {keywords}", flush=True)
    print(f"Country: US | Status: Active only | Since: {since_date or 'all time'}", flush=True)
    print(f"Mode: {'DEEP (target 500, ~500-580 ads/keyword)' if deep else 'Normal (~25-50 ads/keyword)'}", flush=True)
    print(f"Sort: {sort_mode or 'default (FB default = Impressions: high to low)'}", flush=True)
    print(f"Seen filter: {f'{len(seen_domains)} domains' if seen_domains else 'off'}", flush=True)
    print(f"Video only: {video_only}", flush=True)

    start_time = time.time()
    results = scrape_facebook_ads(
        keywords=keywords,
        country="US",
        max_per_keyword=600 if deep else 50,
        since_date=since_date,
        deep=deep,
        seen_domains=seen_domains,
        video_only=video_only,
        sort_mode=sort_mode,
    )
    runtime = int(time.time() - start_time)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    output_path = Path(output_file) if output_file else Path(f"/opt/market-research-agent/logs/facebook_ads_{timestamp}.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    output_data = {
        "meta": {
            "keywords": keywords,
            "run_at": datetime.now().isoformat(),
            "total_unique_advertisers": len(results),
            "runtime_seconds": runtime,
            "mode": "deep" if deep else "normal",
            "sort": sort_mode or "default",
            "since_date": since_date or "all time",
            "target_ads_per_keyword": 500 if deep else 50,
        },
        "advertisers": results,
    }
    output_path.write_text(json.dumps(output_data, ensure_ascii=False, indent=2))

    print(f"\n=== Done: {len(results)} unique ads total ===", flush=True)
    print(f"Runtime: {runtime}s", flush=True)
    print(f"Saved to: {output_path}", flush=True)

    if results:
        print("\n=== ADS FOR CLAUDE ===", flush=True)
        for i, ad in enumerate(results, 1):
            print(f"\n[{i}] Advertiser: {ad.get('advertiser', '?')}", flush=True)
            print(f"     Keyword:   {ad.get('keyword', '?')}", flush=True)
            print(f"     Started:   {ad.get('started_running', '?')}", flush=True)
            print(f"     Active ads:{ad.get('active_ads_count', '?')}", flush=True)
            print(f"     Store:     {ad.get('store_url', 'N/A')}", flush=True)
            print(f"     Ad copy:   {ad.get('ad_copy', 'N/A')[:120]}", flush=True)
    else:
        print("[!] No ads found — check logs/screenshots/", flush=True)

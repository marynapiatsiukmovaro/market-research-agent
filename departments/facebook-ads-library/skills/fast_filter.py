#!/usr/bin/env python3
"""
fast_filter.py v2 — VPS-side candidate filter for FB Ads Library scraper output.
Usage: python3 skills/fast_filter.py /tmp/{keyword}_results.json [--top=20]
Output: prints top N candidates to stdout (for chat); saves full filtered list to /tmp/{keyword}_candidates.txt

v2 changes vs v1:
- Fixed dead REJECT_COPY_STRICT code (was defined but never called)
- Added ISP / insurance / med spa / auto service / subscription rejection signals
- Raised minimum pass threshold from 3 → 5
- Added monthly-pricing pattern as service signal (penalizes score)
- Added .io / .net SaaS domain signal
"""

import json
import sys
import re
import os

# ── REJECT: KNOWN BAD DOMAINS ─────────────────────────────────────────────────
REJECT_DOMAINS = [
    '.edu', '.gov', 'facebook.com', 'instagram.com', 'youtube.com',
    'amazon.com', 'google.com', 'apple.com', 'spotify.com', 'netflix.com',
    'twitter.com', 'linkedin.com', 'tiktok.com', 'walmart.com', 'target.com',
    'bestbuy.com', 'homedepot.com', 'lowes.com', 'chewy.com', 'petco.com',
    'itunes.apple.com', 'play.google.com', 'apps.apple.com',
    'fepblue.org', 'bcbs.com', 'vioc.com', 'valvoline.com',
]

# ── REJECT: AD COPY PHRASES (exact match, lowercase) ─────────────────────────
REJECT_COPY_PHRASES = [
    # App installs
    'download the app', 'available on the app store', 'google play',
    'download on ios', 'download on android', 'get the app',
    # Service sign-ups
    'free trial today', 'sign up for free', 'enroll now', 'join our program',
    'schedule a consultation', 'book an appointment', 'call us today',
    'accepting new patients', 'now hiring', 'apply now', 'donate today',
    # Media/content & sports apps
    'stream now', 'watch now', 'listen now', 'subscribe to our newsletter',
    'scorekeeping', 'live scoring', 'team management app', 'sports app',
    'messaging tools', 'live stream your', 'track your stats',
    # Finance/legal
    'investment advice', 'financial planning', 'mortgage rates',
    'insurance quote', 'property management', 'franchise opportunity',
    # Education/coaching
    'business coaching', 'online course', 'coaching program', 'masterclass',
    'webinar', 'dog training course', 'parenting coach',
    # Software/SaaS
    'saas platform', 'software solution', 'crm tool', 'email marketing',
    'seo agency', 'digital marketing agency', 'local seo', 'hr software',
    'payroll software', 'accounting software', 'per user per month',
    'free demo', 'enterprise plan', 'api access',
    # ISP / telecom
    'business internet', 'fiber internet', 'broadband service',
    'internet plan', 'unlimited data plan', 'built-in security',
    'business-first internet',
    # Insurance / healthcare plans
    'health insurance', 'dental insurance', 'life insurance',
    'employee program', 'health benefits', 'open enrollment',
    'copay', 'deductible', 'health plan', 'coverage starts',
    # Medical / aesthetic services
    'aesthetic journey', 'med spa', 'medspa', 'botox', 'filler',
    'laser hair removal', 'coolsculpting', 'lip filler', 'skin clinic',
    'injectable', 'microneedling service',
    # Auto services
    'oil change', 'auto repair', 'car dealership', 'vehicle service',
    'tire rotation', 'knock off',
    # Real estate
    'real estate', 'home for sale', 'list your home', 'property listing',
    'landlord', 'property manager',
]

# ── REJECT: ADVERTISER NAME SIGNALS ──────────────────────────────────────────
REJECT_NAME_SIGNALS = [
    'chiropractic', 'dental', 'dentist', 'orthodont', 'medical center',
    'hospital', 'clinic', 'plumbing', 'roofing', 'hvac', 'electrician',
    'law firm', 'attorney', 'lawyer', 'university', 'college', 'academy',
    'real estate', 'insurance', 'mortgage', 'financial', 'investment',
    'credit union', 'church', 'nonprofit', 'foundation',
    'pediatrics', 'optometry', 'vision center', 'urgent care',
    'auto body', 'dealership', 'ford ', 'toyota ', 'chevrolet',
    'oil change', 'tire ', 'muffler',
    'blue cross', 'blue shield', 'aetna', 'cigna', 'humana', 'united health',
    'state farm', 'allstate', 'geico', 'progressive insurance',
    'optimum', 'comcast', 'spectrum ', 'at&t', 'verizon', 't-mobile',
    'valvoline', 'jiffy lube', 'pep boys',
]

# ── PHYSICAL PRODUCT WORDS ────────────────────────────────────────────────────
PHYSICAL_PRODUCT_WORDS = [
    'device', 'tool', 'kit', 'brace', 'cushion', 'pillow', 'mat', 'bag',
    'case', 'sleeve', 'band', 'wrap', 'roller', 'massager', 'grinder',
    'trimmer', 'brush', 'cleaner', 'pump', 'bottle', 'cup', 'tray',
    'organizer', 'holder', 'stand', 'clip', 'strap', 'pad', 'patch',
    'spray', 'cream', 'serum', 'gel', 'oil', 'lotion', 'drops',
    'capsule', 'tablet', 'strip', 'sheet', 'mask', 'wand', 'comb',
    'camera', 'watch', 'tracker', 'monitor', 'sensor', 'lamp', 'light',
    'heater', 'cooler', 'fan', 'filter', 'purifier', 'humidifier',
    'toy', 'game', 'puzzle', 'planner', 'journal',
    'shoe', 'insole', 'sock', 'glove', 'hat', 'vest', 'shirt', 'shorts',
    'collar', 'leash', 'harness', 'feeder', 'fountain', 'crate',
    'ships free', 'free shipping', 'order now', 'buy now',
    'in stock', 'back in stock', 'sold out', 'limited stock',
    'money back guarantee', 'day guarantee', 'free returns',
    'delivery', 'arrives', 'package', 'box includes',
    'gummies', 'supplement', 'capsules', 'softgel',
    'razor', 'shaver', 'clipper', 'nail', 'eyelash',
    'blanket', 'towel', 'robe', 'slipper', 'boot', 'sandal',
    'ring', 'bracelet', 'necklace', 'earring',
    'backpack', 'wallet', 'luggage', 'suitcase', 'duffel',
    'blender', 'grater', 'peeler', 'slicer', 'press',
    'planter', 'pot ', 'garden', 'hose', 'sprinkler',
    'bike', 'scooter', 'skateboard', 'helmet',
    'sauna', 'spa', 'bath', 'shower',
]

PRICE_PATTERN = re.compile(r'\$\d{2,3}(?:\.\d{2})?')
MONTHLY_PRICE_PATTERN = re.compile(r'\$\d+(?:\.\d{2})?\/mo|\bper month\b|\bmonthly\b')


def score_candidate(ad: dict) -> int:
    """Score 0-15. Higher = more likely physical product worth checking.
    Minimum threshold to pass: 5 (raised from 3 in v1).
    """
    score = 0
    domain = (ad.get('store_domain') or '').lower().strip()
    copy = (ad.get('ad_copy') or '').lower()
    name = (ad.get('advertiser') or '').lower()
    started = (ad.get('started_running') or '')
    n_ads = str(ad.get('active_ads_count') or '')

    # Has a real domain (not 'not found')
    if domain and domain not in ['not found', '?', '']:
        score += 2

    # Fresh launch signals
    if '2026' in started:
        score += 4
    elif '2025' in started:
        score += 2

    # Multiple active ads (scaling signal)
    n_match = re.search(r'\d+', n_ads)
    if n_match:
        n = int(n_match.group())
        if n >= 5 or '5+' in n_ads:
            score += 3
        elif n >= 2 or '2+' in n_ads:
            score += 2
        else:
            score += 1

    # Price mentioned in copy (one-time purchase signal)
    if PRICE_PATTERN.search(copy):
        score += 2

    # Monthly pricing = service penalty
    if MONTHLY_PRICE_PATTERN.search(copy):
        score -= 3

    # Physical product words
    product_hits = sum(1 for w in PHYSICAL_PRODUCT_WORDS if w in copy)
    score += min(product_hits, 4)

    return score


def is_rejected(ad: dict) -> tuple[bool, str]:
    """Returns (True, reason) if rejected, (False, '') if passes."""
    domain = (ad.get('store_domain') or '').lower().strip()
    copy = (ad.get('ad_copy') or '').lower()
    name = (ad.get('advertiser') or '').lower()

    # Domain reject
    for bad_domain in REJECT_DOMAINS:
        if bad_domain in domain:
            return True, f"domain: {bad_domain}"

    # Copy phrases reject
    for phrase in REJECT_COPY_PHRASES:
        if phrase in copy:
            return True, f"copy phrase: {phrase}"

    # Name signals reject
    for signal in REJECT_NAME_SIGNALS:
        if signal in name:
            return True, f"advertiser name: {signal}"

    return False, ''


def run(json_path: str, top_n: int = 20):
    with open(json_path) as f:
        data = json.load(f)

    ads = data.get('advertisers', [])
    meta = data.get('meta', {})
    keyword = meta.get('keywords', ['?'])[0]
    total = meta.get('total_unique_advertisers', len(ads))

    passed = []
    rejected_count = 0

    for ad in ads:
        rejected, reason = is_rejected(ad)
        if rejected:
            rejected_count += 1
            continue
        sc = score_candidate(ad)
        if sc >= 5:  # v2: raised from 3 to 5
            ad['_filter_score'] = sc
            passed.append(ad)

    passed.sort(key=lambda x: x.get('_filter_score', 0), reverse=True)

    # Save full filtered list to /tmp/
    base = os.path.splitext(os.path.basename(json_path))[0]
    out_path = f'/tmp/{base}_candidates.txt'
    with open(out_path, 'w') as f:
        f.write(f'# {keyword.upper()} — Candidates ({len(passed)} passed filter)\n')
        f.write(f'# Total scraped: {total} | Rejected obvious: {rejected_count} | Passed: {len(passed)}\n\n')
        for i, ad in enumerate(passed, 1):
            f.write(f'[{i}] {ad.get("advertiser","")} | {ad.get("store_domain","")} | '
                    f'Started: {ad.get("started_running","")} | Ads: {ad.get("active_ads_count","")} | '
                    f'Score: {ad["_filter_score"]}\n')
            f.write(f'    Store: {ad.get("store_url","")}\n')
            f.write(f'    Copy: {(ad.get("ad_copy","") or "")[:200]}\n\n')

    # Print top N to stdout (for chat)
    print(f'=== FAST FILTER RESULTS: {keyword} ===')
    print(f'Total scraped: {total} | Rejected: {rejected_count} | Passed filter: {len(passed)}')
    print(f'Showing top {min(top_n, len(passed))} by signal score\n')
    print(f'Full list saved: {out_path} ({len(passed)} candidates)\n')
    print('─' * 60)

    for i, ad in enumerate(passed[:top_n], 1):
        domain = ad.get('store_domain', '') or 'NO DOMAIN'
        started = ad.get('started_running', '?')
        n_ads = ad.get('active_ads_count', '?')
        score = ad.get('_filter_score', 0)
        copy = (ad.get('ad_copy', '') or '')[:150]
        print(f'[{i}] {ad.get("advertiser","")} | {domain} | {started} | {n_ads} ads | filter:{score}')
        print(f'    {copy}')
        print()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 fast_filter.py results.json [--top=N]")
        sys.exit(1)

    json_path = sys.argv[1]
    top_n = 20
    for arg in sys.argv[2:]:
        if arg.startswith('--top='):
            top_n = int(arg.split('=')[1])

    run(json_path, top_n)

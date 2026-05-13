# SEEN ADVERTISERS LOG

Brands already analyzed in previous sessions. Skip in future scraping runs.
Scraper reads this file when called with --seen=memory/seen-advertisers.md

Format: domain | reason_skipped | date_seen
One domain per line (lines starting with # are comments).

---

## REJECTED — Price too high (above $79)

nobltravel.com | carry-on bags $279-799 | 2026-05-13
chefpreserve.com | vacuum sealer $159 main product | 2026-05-13
condition1.com | professional hard cases $170-510 | 2026-05-13
comfysleepers.com | cooling blanket $107 | 2026-05-13
sondurtravel.com | travel cushions $112-182 (only $55 lumbar variant in range) | 2026-05-13
noreceptionclub.com | travel duffel $235 | 2026-05-13

## REJECTED — Price too low (below $39)

lakany.com | car accessories $8-36 | 2026-05-13
bagail.com | packing cubes ~$20-35 | 2026-05-13
farandwideofficial.com | passport holder ~$25 | 2026-05-13
woodencrew.store | travel accessories $28-45, no strong signal | 2026-05-13
flyhugz.com | travel pillow category already covered, $39-50 | 2026-05-13

## REJECTED — Wrong store / mismatch

livena-shop.com | car accessories store, trunk organizer not main product | 2026-05-13
amhomey.com | general dropship store, products don't match ads | 2026-05-13

## REJECTED — Wrong category / niche

hackmotion.com | golf wrist sensor, niche sport | 2026-05-13
pockt.co | TENS device $23-130, below price floor or above | 2026-05-13
kilosgear.com | camping sleeping bag, seasonal | 2026-05-13
agedandore.com | travel spirits/whisky kit, niche | 2026-05-13

## ACCEPTED — Already in Notion (do not re-add)

the8thstreet.com | ACCEPTED score 73 | 2026-05-13
wander-plus.com | ACCEPTED score 72 | 2026-05-13
travelerpillow.com | ACCEPTED score 67 | 2026-05-13

---

## How to Use

Pass to scraper:
  python3 skills/facebook_scraper.py --seen=memory/seen-advertisers.md "keyword1" "keyword2"

Scraper will skip any ad whose store_domain matches an entry in this file.
Add new entries at the end of each session.

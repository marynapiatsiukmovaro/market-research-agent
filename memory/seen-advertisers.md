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

## Session 4 — 2026-05-14

### ACCEPTED — Already in Notion (do not re-add)
kittyspout.com | ACCEPTED score 77 — cat water fountain, stainless steel wireless | 2026-05-14

### REJECTED — Price too low (below $49)
uprootclean.com | pet hair remover $16.99 hero product | 2026-05-14
purepathshop.ca | pet hair glove $24.99 | 2026-05-14
north-alpine.com | men compression tank $29.90 | 2026-05-14

### REJECTED — Price too high (above $99)
enjuvie.com | magnetic lashes $120-235 | 2026-05-14

### REJECTED — Wrong category / noise
coregadgetry.com | general dropship store, multiple unrelated gadgets | 2026-05-14
trovetraders.com | general dropship store, multiple categories | 2026-05-14
shoplarke.com | general dropship store $12-30 items | 2026-05-14
copenrain.com | general dropship store | 2026-05-14
livowish.com | redirects to shoplarke, dropship | 2026-05-14

### REJECTED — Established brand / saturated
jolieskinco.com | shower filter 650K customers — too established | 2026-05-14
everstridesocks.com | compression socks since 2024, established | 2026-05-14
koprez.com | plantar fasciitis sleeve 200K customers, established | 2026-05-14

### REJECTED — Unverifiable result / пустышка
comfrt.com | weighted hoodie — "not proven in clinical trials" disclaimer | 2026-05-14
auroraskin.us | LED facial sculptor — Marina rejected LED face devices as "везде" | 2026-05-14

---

## Session 5 — 2026-05-14 (Pet Tech Vertical Deep Dive)

### REJECTED — Price too high (above ceiling)
neakasa.com | pet grooming vacuum $84-200 | 2026-05-14
penthousepaws.com | smart HD feeder $138 | 2026-05-14
petpivot.com | self-cleaning litter box $179 | 2026-05-14
getbistrocat.com | BistroCat feeder $95+subscription | 2026-05-14

### REJECTED — Price too low (below floor)
pawspik.com | interactive cat toy $29.99 | 2026-05-14
potaroma.com | smart sensor cat laser toy $29.99 | 2026-05-14
getfurlife.com | pheromone calming collar $29.99 | 2026-05-14

### REJECTED — Established brand / pre-2024
goifetch.com | iFetch ball launcher — legacy brand 10+ years | 2026-05-14
rellaty.com | pet water fountain — founded 2019, too established | 2026-05-14
bellanpal.com | multi-category pet store — founded 2021 | 2026-05-14
sphinxcatfeeder.com | Kickstarter only, not shipped | 2026-05-14
oneisall.com | automatic feeder — Amazon/retail distributed, not fresh DTC FB | 2026-05-14

### REJECTED — Subscription model / wrong structure
tractive.com | GPS tracker — subscription $6-10/mo | 2026-05-14
fitbark.com | activity tracker — subscription | 2026-05-14
maven.pet | dog health tracker — subscription | 2026-05-14
linkmypet.com | smart collar — subscription | 2026-05-14

### NOTED — Confirmed mechanism, not reportable
heusom.com | nail grinder $39.95/$66.60 — "validated mechanism, commoditized execution"; flashy ads confirmed but same product $20-39 on Amazon | 2026-05-14

## How to Use

Pass to scraper:
  python3 skills/facebook_scraper.py --seen=memory/seen-advertisers.md "keyword1" "keyword2"

Scraper will skip any ad whose store_domain matches an entry in this file.
Add new entries at the end of each session.

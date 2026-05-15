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

## Session 6 — 2026-05-14 (Dog Fountain + Smart Feeder)

### CANDIDATE — Needs FB verification
trywagwells.com | CANDIDATE score 76 — dog water fountain, stainless, $74.95, CET operator, April 2026 Amazon | 2026-05-14

### REJECTED — Too established (pre-2025)
uahpet.com | founded 2019, Amazon + Chewy distributed | 2026-05-14
petmarvel.com | founded 2019, Chewy + Amazon, misleading ads | 2026-05-14
voluas.com | founded 2021, Chewy distributed | 2026-05-14
homerunpet.com | founded 2015, Amazon native | 2026-05-14

### REJECTED — Amazon-native only / no DTC site
pokpet.com | Amazon + Chewy only, no DTC FB presence | 2026-05-14
arfpets.com | multi-category pet store, not specialist DTC feeder | 2026-05-14

### REJECTED — Wrong market / fake signals
tryhydropaws.com | AUD pricing = Australia market; 37K reviews > 24K customers = inflated | 2026-05-14
sgsmartpaw.com | .sg domain + +65 phone = Singapore market; suspicious review count | 2026-05-14

### REJECTED — Branded (can't white-label)
cheerble.com | Elfin D1 Pro dog fountain $95.99 — confirmed FB advertiser but branded product; useful as category signal only | 2026-05-14

### NOTED — Minimal signal, white-label candidate
shophydrapaw.com | dog fountain $69.95 — no founding date, no FB signal, white-label pattern; resold by third parties | 2026-05-14

## Session 7 — 2026-05-15 (Home/Kitchen Vertical)

### REJECTED — Too established (pre-2025)
dovety.com | electric spin scrubber $59.99 — B0C ASIN = 2023 launch, 3 years old | 2026-05-15
leebein.com | electric spin scrubber — founded 2020, 10M+ families, too established | 2026-05-15
gladwellclean.com | cordless electric mop — B08 ASIN = 2020, 6 years old | 2026-05-15

### REJECTED — Retail-distributed (not DTC-first)
hombrand.com | electric spin scrubber $54.99 — sold at Best Buy, Target, Home Depot | 2026-05-15
foodsaver.com | handheld vacuum sealer $100-170 — retail giant (Newell Brands) | 2026-05-15

### REJECTED — Site credibility / broken
sonixpack.com | handheld vacuum sealer $79.99 — HTTP 402 error on main page | 2026-05-15
technoant.co | self-wringing mop — trust score 10/100, WHOIS hidden, dropship store pattern | 2026-05-15

### REJECTED — Amazon-only (no DTC site)
grazie-mop (no domain confirmed) | spin mop — B0FX ASIN (fresh 2025) but no DTC site found | 2026-05-15

## Session 8 — 2026-05-15 (Kids Vertical, Keyword-First Deep Scan)

### ACCEPTED — Category validators (do not re-add to Notion, use as market signals)
bamboraco.com | ACCEPTED score 73 — baby ring sling carrier, $59, 13+ active FB ad units; Category Validator | 2026-05-15
hoppie.kids | ACCEPTED score 65 — stroller hammock seat for 2nd child, $79, 1032 reviews; Category Validator | 2026-05-15

### REJECTED — Legacy / retail-distributed
potterybarnkids.com | retail brand, luxury baby items $200+ | 2026-05-15
uppababy.com | luxury stroller brand $600-1200 — retail | 2026-05-15
doona.com | car seat + stroller combo $500+ — retail brand | 2026-05-15
lovevery.com | premium play kits $36-120/month — subscription; established brand | 2026-05-15
babylist.com | baby registry platform — service, not physical product | 2026-05-15
owletcare.com | baby monitor — established brand, FDA-cleared, $100-350 | 2026-05-15
cradlewise.com | smart baby bed $1000+ — above ceiling | 2026-05-15
boppy.com | nursing pillow — retail giant (Walmart), established brand | 2026-05-15
nuk-usa.com | pacifiers/baby gear — established FMCG brand | 2026-05-15
momcozy.com | nursing/maternity brand — established, retail distributed | 2026-05-15

### REJECTED — Wrong category / noise
wildbird.co | ring sling $69 — NOW IN TARGET RETAIL, DTC play over | 2026-05-15
totesbabies.com | stroller bag add-on — founded 2021, too established | 2026-05-15
mama-roo.com | baby carrier quiz site — founded 2023, low signal | 2026-05-15
austlen.com | premium multi-child stroller $500+ — above ceiling | 2026-05-15
stroleebaby.com | lightweight stroller — started Jul 2025, price unconfirmed (likely $200+) | 2026-05-15
emmafy.com | mom crossbody bag — started Sep 2025, BUY 1 GET 1 (price TBD, possibly below floor) | 2026-05-15
minabaie.com | diaper bag — started Mar 2026, price TBD | 2026-05-15
tacticalbabygear.com | tactical/military-style dad gear — niche, contest-based ads | 2026-05-15
kiddofinds.com | general baby product aggregator — affiliate/curator | 2026-05-15
butterr.co | natural nursing pillow — founded 2023, too established | 2026-05-15
designdua.com | multi-category baby/home brand — founded 2022 | 2026-05-15
kinderpack.com | USA-made ergonomic carrier — founded 2022, retail | 2026-05-15
zoberloco.com | baby carrier — founded 2023, too established | 2026-05-15
mykinderpack.com | USA-made carrier — founded 2022 | 2026-05-15
hoppie.kids | ACCEPTED score 65 — already logged above | 2026-05-15

### NOTED — Needs follow-up verification
babybub.com | multi-product brand (pregnancy + nursing $49-75); weak signal, needs domain check | 2026-05-15
skaldoandmalin.com | baby arm feeding pillow + general baby accessories $9-45 — low prices for most items | 2026-05-15

## Session 9 — 2026-05-15 (Kids Vertical: baby, toddler, sleep baby keywords)

### ACCEPTED — Already in Notion (do not re-add)
toucanbaby.com | ACCEPTED score 67 — sleep sack with self-soothing lovey, $44-85, Dec 2025 DTC | 2026-05-15
buymamacoco.com | ACCEPTED score 66 — fastener-free cocoon swaddle, $44, 656 reviews, March 2026 | 2026-05-15

### REJECTED — Price too low (below $39)
upairy.com | potty training underwear $7/pair, 100K+ parents = established | 2026-05-15
kidconfident.co | potty training pants $7/pair — below price floor | 2026-05-15
floatbuds.shop | swim floatsuit $37 sale / $44 regular — seasonal + below floor effective price | 2026-05-15

### REJECTED — Established brand / branded product
us.mycarrypotty.com | UK brand since ~2014, "1M+ families", patented leakproof seal — not white-label | 2026-05-15
lovetodream.com | baby sleep bags — Australian brand since 2007, established retail | 2026-05-15
nestedbean.com | Zen Swaddle — established since 2015, branded "weighted chest" tech | 2026-05-15
woolino.com | premium wool sleep bag — Canadian brand ~2013, established | 2026-05-15

### REJECTED — Price borderline / regulatory risk
copacalmer.com | teething roller with essential oils — safety risk (EOs on infant skin), price not disclosed | 2026-05-15
aed.us | LifeVac anti-choking device — under $40, primarily B2B/professional channel | 2026-05-15

### REJECTED — Wrong category / noise
top5methods.com | AirwayClear anti-choking device — under $40, borderline price | 2026-05-15
cradle-cuties.com | BabyHug pillow — dropship pattern signals, 404 on product page, suspicious social proof | 2026-05-15

## Session 9 Post-Compact — Rounds 4-6 (2026-05-15)

### REJECTED — Price too low / below floor
getfootstr.com | kids orthotics insoles $34.99 (on sale) — below $39 floor + branded Footstr™ | 2026-05-15

### REJECTED — Price borderline + white-label impossible (patented)
kaizenkidz.com | ACCEPTED score 65 — 3-2-1 Swim Pack $99.99, patent on mechanism (not concept), Needs Verification | 2026-05-15

### REJECTED — Established brand (1M+ customers / too large)
natpat.com | BuzzPatch/SleepyPatch essential oil patches — 1M+ customers, Australian brand, AromaWeave™ technology | 2026-05-15

### REJECTED — Price too low / wrong structure
mimibelt.com | pregnancy seatbelt adapter $35.99 — below $39 floor, branded, 1,472 reviews | 2026-05-15
cocoseat.com | portable baby seat cover $44 — commoditized mechanism (shopping cart covers $15-30 on Amazon), score ~62 below threshold | 2026-05-15

### REJECTED — Multi-product / wide price range
mammabump.com | maternity recovery brand $19-330 — multi-product, too wide range, Momcozy competition | 2026-05-15

### REJECTED — Anti-choking category (regulatory/patent risk)
rescueseal.store | RescueSeal emergency kit $59 — anti-choking category, patented competitor (LifeVac) | 2026-05-15
freevair.com | Freevair anti-choking device — same category, price not disclosed | 2026-05-15

### REJECTED — Wrong market (UK brand / GBP pricing)
safehero.us | SafeHero emergency tools £19-79 — UK brand (GBP pricing), 150K+ families too established | 2026-05-15

## How to Use

Pass to scraper:
  python3 skills/facebook_scraper.py --seen=memory/seen-advertisers.md "keyword1" "keyword2"

Scraper will skip any ad whose store_domain matches an entry in this file.
Add new entries at the end of each session.

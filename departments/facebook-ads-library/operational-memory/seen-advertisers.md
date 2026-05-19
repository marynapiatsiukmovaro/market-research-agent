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

## Session 9 — Rounds 7-8 (2026-05-15, post-compact)

### KEYWORD: "Montessori toy" — 81 unique advertisers, scroll stall at 253 raw

#### REJECTED — Dropship network (same "Montessori Fishing Set" copy, different domains)
formerline.com | dropship clone — Montessori Fishing Set | 2026-05-15
terrificaday.com | dropship clone — Montessori Fishing Set | 2026-05-15
circumstancen.com | dropship clone — Montessori Fishing Set | 2026-05-15
undertakely.com | dropship clone — Montessori Fishing Set | 2026-05-15
extensiveh.com | dropship clone — Montessori Fishing Set | 2026-05-15
circulatem.com | dropship clone — Montessori Fishing Set | 2026-05-15
reinforcea.com | dropship clone — Montessori Caterpillar / Fishing Set network | 2026-05-15

#### REJECTED — Established brands / retail-distributed
leyadoll.com | personalized dolls — founded 2018, 100K+ customers | 2026-05-15
montessoriparadise.com | multi-product Montessori store | 2026-05-15
montessorikidsmart.com | multi-product Montessori store | 2026-05-15
robud.com | play kitchen — multi-product, appears in multiple keywords | 2026-05-15
sarahssilks.com | premium Montessori silks — established retail brand | 2026-05-15

#### REJECTED — Non-US market
bycubby.com | personalised busy books — UK brand (British spelling "Personalised") | 2026-05-15
toddla.co | Montessori busy board — AUD pricing / AEDT support hours = Australian brand | 2026-05-15
vivatrend.no | Norwegian domain (.no) | 2026-05-15

#### REJECTED — Demo site / fake store
bloomellokids.com | "© 2026 Bloomello Kids Demo" — template demo site, not real brand | 2026-05-15

#### REJECTED — Dropship general store
itemmatter.com | general gadget store (cable clips, ice ball maker, rings) — domain mismatches ads | 2026-05-15
passioninbuy.com | Montessori Busy Board — dropship store, same copy as multiple others | 2026-05-15
hicooo.com | general educational toys dropship | 2026-05-15
alppibaby.com | general baby toy dropship | 2026-05-15
yourbabyshop.store | general baby store dropship | 2026-05-15
kiddie-corner.com | general Montessori toy dropship | 2026-05-15
briefconcise.com | square busy board — generic dropship | 2026-05-15
endeavoried.com | screw-tightening busy board — dropship | 2026-05-15
swiftzenx.com | MagicBook — dropship | 2026-05-15
crishine.com | same busy board copy as tibatoes — dropship | 2026-05-15
formerline.com | Montessori Fishing Set clone | 2026-05-15

#### REJECTED — Unverifiable / suspicious
tibatoes.com | trust score 39/100, dropship signals, UK couple, "junk from China" complaints | 2026-05-15
minilabbies.com | Digiscope™ $78 — DIGISCOPE trademark (USPTO 99491168) blocks white-label; fake reviews suspected; China shipping delays | 2026-05-15
toddsiq.com | Drawing Robot — no web presence found | 2026-05-15
toddleready.com | speech therapist toy — no price or founding date found, weak signal | 2026-05-15
playnesttoys.com | multi-category toy retailer — parent co. Jewelias est. 2019 | 2026-05-15
sundaymom.com | faith-based content, not product brand | 2026-05-15

### KEYWORD: "sensory toy" — 198 unique advertisers, 515 raw ads

#### REJECTED — Adult stress relief, not kids (dominant category in this keyword)
itsblossom.com | adult sensory cube + squishy hamster stress toys | 2026-05-15
ancienflow.com | adult stress ice cream squeeze toy | 2026-05-15
sangboxs.com | magnetic exploding stress-relief spinner — adult | 2026-05-15
owlandgoosegifts.com | squishy toys — general gift store | 2026-05-15
hooktasy.com | digital crochet patterns, not physical toy brand | 2026-05-15
doldols.com | 3D-printed D20 squishy fidget — adult/gaming niche | 2026-05-15
reshline.com | Lava Squish Flow Toy — adult | 2026-05-15
moonycozy.com | lava squish + squishy ice cubes — adult stress | 2026-05-15

#### REJECTED — Dropship networks (each group = same product, many domains)
frequentlyk.com | jelly squishes network node | 2026-05-15
graciousk.com | jelly squishes network node | 2026-05-15
blstdispse.com | jelly squishes network node | 2026-05-15
clockwisei.com | jelly squishes network node | 2026-05-15
accurateg.com | jelly squishes network node | 2026-05-15
whenevertime.com | jelly squishes network node | 2026-05-15
interferek.com | jelly squishes network node | 2026-05-15
nifyanifest.com | jelly squishes network node | 2026-05-15
nominateh.com | jelly squishes network node | 2026-05-15
admissioni.com | jelly squishes network node | 2026-05-15
coincidem.com | jelly squishes network node | 2026-05-15
freedomty.com | jelly squishes network node | 2026-05-15
enjoyaitlife.com | jelly squishes network node | 2026-05-15
forttender.com | Easter squishy bundle network node | 2026-05-15
foundatioy.com | Easter squishy bundle network node | 2026-05-15
northwestl.com | Easter squishy bundle network node | 2026-05-15
reflexionm.com | Easter squishy bundle network node | 2026-05-15
professionay.com | Easter squishy bundle network node | 2026-05-15
flowarmth.com | Kids Phonograph 99 Cards network node | 2026-05-15
transferk.com | Kids Phonograph 99 Cards network node | 2026-05-15
howeveryet.com | stroller hanging sensory toy — dropship network | 2026-05-15
afterdoubt.com | stroller hanging sensory toy — dropship network | 2026-05-15
idealbless.com | stroller hanging sensory toy — dropship network | 2026-05-15
doneforth.com | "Interactive Sensory Garden Baby Toy Set" — used by doneforth + ampleidea = dropship | 2026-05-15
ampleidea.com | same Sensory Garden copy as doneforth = dropship clone | 2026-05-15
naivetu.com | lava flow toy dropship | 2026-05-15
convergeas.com | interactive music plush network node | 2026-05-15
inlikewise.com | interactive music plush network node | 2026-05-15
tyiiplus.com | interactive music plush network node | 2026-05-15

#### REJECTED — Non-US market
laylaylabels.com | AUD pricing = Australian brand | 2026-05-15
wrapango.com | based in Bulgaria, hero product $17.99 | 2026-05-15
tiny-dreams.uk | UK domain | 2026-05-15
chillzones.co.uk | UK domain | 2026-05-15
sunnyo.com.au | Australian domain | 2026-05-15

#### REJECTED — Wrong price or category
brainrichkids.com | climbing play gym $1499-2399, ~10 years old | 2026-05-15
junglejumparoo.com | jumping toy $449-498 — above ceiling, established brand | 2026-05-15
pandadrum.com | Panda Drum® $89-259 — trademarked, not white-label | 2026-05-15
thelovingegg.com | silicone Easter eggs — seasonal product | 2026-05-15
123babybox.com | subscription baby box — service model | 2026-05-15
sensorytheraplaybox.com | subscription sensory box — service model | 2026-05-15

#### NOTED — Insufficient signal, not recommended
blemory.com | mibbo musical plush toy $39.95 — touch-activated music concept interesting; sold out, no reviews visible, 404 on product page, zero external presence — too fragile | 2026-05-15

## Session 16 — 2026-05-18 (Broad Horizontal Discovery: Promo-phrase Keywords)

### KEYWORD: "50% off today" — 69 advertisers, 0 reportable

#### REJECTED — Overheated / commodity
hugterra.com | hugging pillow $39.99 — Amazon saturated; no DTC angle; established category | 2026-05-18
revoget.com | knee pillow $29.99 — below price floor + commodity | 2026-05-18
treatmedy.com | bunion device — retargeting ad ("forgot to checkout"), not cold traffic signal + пустышки risk | 2026-05-18

#### REJECTED — Wrong market
basedco.ca | Canadian grooming brand — .ca domain, USD price unverifiable | 2026-05-18

### KEYWORD: "buy 1 get 1 free" — 164 advertisers, 0 reportable

#### NOTED — Category signal, below threshold
blumibaby.com | kids swim goggles $39.99 — 25 active FB ads, 12K reviews 4.83★; score ~62 (below 65); late entry window + price floor + seasonal; Blumi Baby = established brand | 2026-05-18

#### REJECTED — Late entry / established
peakfootwear.com | barefoot shoes $59-89 — 17 active ads, strong brand, but niche athletic footwear; established market | 2026-05-18
magicbrush.com | horse grooming brush — equestrian niche, B2B/hobby, mass market too small | 2026-05-18
spotminders.com | mole/skin spot tracker app — digital service, not physical product | 2026-05-18

### KEYWORD: "half off" — 357 advertisers, 0 reportable (tested as proxy for "50% off")

#### REJECTED — Price too high (above ceiling)
anleolife.com | raised garden beds $129-$1503 — above $99 ceiling | 2026-05-18

#### REJECTED — Professional niche / wrong audience
tpobusa.com | "Pissed Off Barber" professional clippers — barber B2B niche, not mass consumer cold traffic | 2026-05-18

#### REJECTED — Пустышки risk
sinuvox.com | red light sinus device — "clinically studied" claim based on self-reported survey; red light category overheated + unverifiable mechanism | 2026-05-18

#### REJECTED — Price too low / general store
aneedfamily.com | vacuum storage bags $14.99 — below price floor; multi-category general dropship store | 2026-05-18

## Session 22 — 2026-05-19 (Situation Keywords: Worker Context + Sensation)

### KEYWORDS: night shift / desk setup / ergonomic / meal prep / desk job / cold office / on your feet all day
### Result: 1 product (cold office → heated desk mat 66, whisperheat.com)

### REJECTED — Price too high (above $170)
suvie.com | Kitchen Robot appliance $649 — automated meal prep machine, way above range | 2026-05-19
topjob.co | ergonomic furniture $214-999 — AnyDesk Hub/Fold, BISKIT Chair; all above range | 2026-05-19
snibbs.co | work shoes $99-185 — ultra-comfy slip-resistant; logistics complex + above range | 2026-05-19

### REJECTED — Wrong category / not white-label
masongenie.com | vacuum jar sealer DTC — "only at masongenie.com", proprietary design; 1 FB ad only | 2026-05-19
oldbonestherapy.com | knee compression sleeves $40-60 — mechanism veto (pain relief unprovable on camera) + athlete niche | 2026-05-19
peepclub.com | Heated Eye Wand LED+ $120 — eye care category already closed (Eye Massager S1 score 84); UK brand | 2026-05-19

### ACCEPTED — Already in Notion
whisperheat.com | ACCEPTED score 66 — electric heated under-desk mat; cold office keyword; seasonal Oct-Apr | 2026-05-19

---

## How to Use

Pass to scraper:
  python3 skills/facebook_scraper.py --seen=memory/seen-advertisers.md "keyword1" "keyword2"

Scraper will skip any ad whose store_domain matches an entry in this file.
Add new entries at the end of each session.

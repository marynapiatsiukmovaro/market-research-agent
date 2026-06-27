# Store Leads — Keep-List (strong-store monitor feed)

**Purpose (Marina, S2→S3):** accumulate the STRONG / borderline stores we find (65+, 55–64, and
genuinely-interesting browse picks) so we can later load them into a **"newest-products-first" monitor**
(ShopHunter OR another service) and check every 2–3 days what NEW products these proven operators launch
→ catch future winners early. **Store Leads = the store-supplier for that monitor.**

**Mechanism:** the master record (`logs/storeleads/processed_domains.json` on the VPS) carries a `monitor: true`
flag per store. `sl_mark_processed.py` sets it (proxy-score gate); the main agent confirms/edits it at the
checkpoint (a founder-Watchlist or a real borderline → `monitor: true`). This file is the human-readable
running export of those flagged stores. The monitor JOB itself is DEFERRED (lives in ShopHunter, parked) —
here we only FEED the list.

**Discipline:** add a store here when it's a genuine strong/borderline find (not trade/commodity filler).
Dedupe by domain. Note WHY in 4–5 words. Keep clickable.

---

## Monitored stores

| Date | Store | Score | Class | Why keep (monitor for new launches) |
|---|---|---|---|---|
| 2026-06-01 | [muravai.co](https://muravai.co) | 77 | filtered showerhead (Beauty) | Watchlist; proven filter-niche, hair angle open — watch what they launch next |
| 2026-06-01 | [us.thecoldpod.com](https://us.thecoldpod.com) | 64 | ice bath (Fitness) | Watchlist; study (premium-look/low-price) — watch their next drops |
| 2026-06-01 | [izimini.com](https://www.izimini.com) | 57 | outdoor baby chair (Kids) | Consider; stylish + strong seasonal hook — watch new outdoor SKUs |
| 2026-06-01 | [dingledanglebaby.com](https://www.dingledanglebaby.com) | 60 | diaper-change distractor (Kids) | Consider; fun/novel family-bonding — Shark Tank brand, watch new toys |
| 2026-06-01 | [joseat.com](https://joseat.com) | 68 | cart/high-chair cover (Kids) | Consider; clear hygiene pain — watch new covers/accessories |
| 2026-06-01 | [wildridecarrier.com](https://wildridecarrier.com) | 70 | toddler hip carrier (Kids) | Watchlist; beautiful design brand in saturated niche — watch their drops |
| 2026-06-01 | [waterlandbaby.com](https://www.waterlandbaby.com) | 72 | water+land carrier (Kids) | Watchlist; clever water positioning — watch how they extend the line |
| 2026-06-01 | [petiteisland.com](https://www.petiteisland.com) | 77 | pocket fetal doppler (Health) | S4 winner; doppler convergence w/ approved WellnessBaby (83); watch new SKUs |
| 2026-06-01 | [kindersensebaby.com](https://kindersensebaby.com) | 73 | crib safety tent (Kids) | S4 winner; real safety-pain solver; watch their next launches |
| 2026-06-05 | [yogorgeous.com.au](https://yogorgeous.com.au) | 53 | anti-roll changing mat (Kids) | S8 founder-kept Watchlist; WriggleBum-category diaper-change pain — study |
| 2026-06-05 | [babymarstore.com](https://babymarstore.com) | 60 | RockaBaby stroller rocker (Kids) | S8 convergence → Rockit SL2; watch deep-tail clones of proven mechanism |
| 2026-06-07 | [petarro.com](https://petarro.com) | 64 | cat exercise wheel (Cats) | S12 borderline; viral-UGC wheel but bulky/$150 (RULE10); wheel-convergence ×4 (meowza/PawSquad/FelineFit) — watch if a non-bulky version appears |
| 2026-06-07 | [bxsdesigns.com](https://www.bxsdesigns.com) | 61 | patented sifting litter box (Cats) | S12 borderline; real daily-scoop pain, "6-second" angle vs $300 auto-boxes; patented (can't white-label) — watch the category |
| 2026-06-07 | [thegerty.com](https://thegerty.com) | 65 | inflatable anxiety friend (Dogs) | S13 WINNER → Notion + queue/study; Shark Tank, viral-shaped; watch efficacy/clones |
| 2026-06-07 | [teamk9.com](https://teamk9.com) | 60 | backseat cooling fans (Dogs) | S13 borderline → Notion/queue; whole store = idea-asset (car hammock $169, tactical harness $90) — watch new drops |
| 2026-06-07 | [coolbowl.shop](https://coolbowl.shop) | 61 | refrigerated water bowl (Dogs) | S13 borderline; "first ever" Peltier-cooled bowl, novel — $99 + plug-dependent; watch for a cheaper/portable version |
| 2026-06-07 | [drpfoten.de](https://drpfoten.de) | 60 | quiet nail trimmer PawTrim (Dogs) | S13 borderline; real nail-trim-anxiety pain, "quiet" differentiator; grinder category saturated — watch angle |
| 2026-06-07 | [snugglepuppy.com](https://snugglepuppy.com) | 58 | heartbeat anxiety toy (Dogs) | S13 borderline; 25yr category-definer (separation anxiety), proven but saturated — watch white-label gap |
| 2026-06-07 | [dickybag.com](https://www.dickybag.com) | 56 | odour-proof waste carrier (Dogs) | S13 borderline; real "dangling poo-bag" pain, award-winning UK — watch if a viral version appears |
| 2026-06-07 | [getrenu.com](https://getrenu.com) | 60 | waterless grooming brush+mist (Dogs) | S13 b6 borderline; ultrasonic-mist 3-min refresh, 45k+ customers — but me-too multi-seller + mixed Trustpilot; watch quality fix |
| 2026-06-07 | [dogloc.com](https://dogloc.com) | 55 | anti-theft lockable leash (Dogs) | S13 b8 borderline; patented lock vs dog-theft fear; convergence w/ lock-dog.com — watch for cheaper white-label |
| 2026-06-07 | [checkpup.com](https://checkpup.com) | 54 | at-home dog wellness/urine test (Dogs) | S13 b11 browse; echoes Cats health-vein (vetpointbio) — only "fresh" vector in Dogs; watch diagnostics trend |
| 2026-06-07 | [warmwalksinc.com](https://www.warmwalksinc.com) | 60 | heated dog leash 3-in-1 (Dogs) | S13b b14 borderline (NOT Notion, Marina); heat-handle + power-bank + LED $54.95, novel/demoable — but seasonal + electronics return/QC + narrow market; watch a non-seasonal version |
| 2026-06-08 | [ergodog.com](https://ergodog.com) | 58 | no-pull leverage leash "Shrink Ray" (Dogs) | S14 Dogs b21 borderline (NOT Notion); genuine ergonomic handlebar mechanism for heavy pullers + 30d guarantee — but $90, narrow audience, weak visual wow; watch for a cheaper/visual version |
| 2026-06-08 | [snappyshoerivets.com](https://snappyshoerivets.com) | 52 | Croc/clog repair rivets (HI b6) | S14 HI browse; tiny novel impulse ($13, glow-in-dark) for a broken Croc strap — cheap COGS + UGC-able but micro-TAM; watch if a viral version appears |
| 2026-06-08 | [boundri.com](https://boundri.com) | 52 | personalized kids' farm play rug (HI b6) | S14 HI browse; custom photo/map play rug — emotional FB-gift angle (off-HI); watch the personalized-gift vector |
| 2026-06-08 | [paintwithnumber.com](https://paintwithnumber.com) | 57 | custom paint-by-numbers from photo (HI b1) | S14 HI borderline; proven FB-gift category — appeared ×4 across HI (schilderopnr/brushme/lilpaintshop); off-HI-niche but a recurring impulse-gift signal worth watching |
| 2026-06-27 | [luvlink.com.au](https://www.luvlink.com.au) | 63 | friendship/touch lamp (H&G b5) | S16 borderline; tap-to-light paired lamp worldwide, strong emotion ("thinking of you") but ~$120 premium + saturated (Filimin) — watch for a cheaper version |
| 2026-06-27 | [chickcozy.com](https://chickcozy.com) | 63 | solar auto chicken-coop door (H&G b5) | S16 borderline; real pain (predator-safety/convenience) + demo, but $159 premium + niche (chicken keepers, growing trend) — watch the backyard-chicken vector |
| 2026-06-27 | [claymoreoutdoor.com](https://claymoreoutdoor.com) | ~50 | portable outdoor fan V600+ (H&G b5) | S16 browse — found by LIVE-OPENING an "unreachable" store (title hid it!); Red Dot fan $64.95 in-range but branded/commodity-adjacent — proof that opening unreachable matters |

---

## How to add
One row per kept store: `Date · [domain](https://domain) · score · product_class · why (4–5 words)`.
Also set `monitor: true` in `processed_domains.json` (via `sl_mark_processed.py --monitor-min` or by hand at checkpoint).

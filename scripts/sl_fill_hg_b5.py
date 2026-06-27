#!/usr/bin/env python3
"""S16 b5 verdict+score filler. Written locally + scp per no-heredoc rule.
b5 = the LIVE-OPEN-restored batch (9 stores WebFetched in chat). Fills opens verdicts (RULE 23)
+ scores.jsonl: 2 winners (The Wriggler 68 = S15-miss redeemed by guard+live-open · OtterSpace 66),
2 borderline (LuvLink 63 · ChickCozy 63), rejects (guard hits + Flawless above-ceiling), browse."""
import json
D = "logs/storeleads/niches/home-and-garden"
OPENS = f"{D}/np_b5_opens.jsonl"; SCORES = f"{D}/np_b5_scores.jsonl"

V = {
 "inotterspace.com": "WINNER (live-opened): OtterSpace blackout curtain kit $129 — see scores (66)",
 "ournewbabyinc.com": "reject: Copper Pearl reseller, below-floor knit headbands/swaddle (apparel) [guard hit]",
 "createacastle.com": "browse: Shark Tank castle play molds (kids sand/snow), genuine consumer ~$40-60",
 "eu.beatbot.com": "off-model: robotic pool cleaner $2050+, above ceiling/high-ticket",
 "utihamono.com": "off-model: Japanese forged knives, branded/premium",
 "www.shoptchotchke.com": "off-model: artisan Judaica/ketubahs decor",
 "aonoki.shop": "off-model: live houseplants (JP)",
 "enjuvie.com": "off-model: magnetic lash kit (beauty, desc-empty), $49-59",
 "offthebeatenpathnursery.com": "off-model: live fig trees / plant nursery",
 "lemonsonfire.com": "off-model: apparel tanks + art, $20-50",
 "www.havai.in": "off-model: commercial BLDC desert coolers, trade/bulky",
 "www.worldlygoodstoo.com": "off-model: decorative glass balls/arrangements (custom)",
 "elizabethstuart.com": "off-model: decor vases / garden books, design brand",
 "babinskis.com": "off-model: branded baby-gear retailer (UPPAbaby/Nuna), prices 0",
 "waxbuffalo.com": "off-model: soy candles, commodity decor",
 "yourothercloset.com": "off-model: consignment/resale mixed goods",
 "www.greenflow.hk": "off-model: handmade pottery plant pots (HK), $112-189",
 "beatlas.com": "off-model: space heaters catalog, commodity, below/at floor",
 "www.bendigopottery.com.au": "off-model: ceramics/stoneware (AU), clearance",
 "lightmyfire.com": "off-model: Swedish outdoor/camping commodity, below floor",
 "www.rubiomonocoat.nl": "off-model: wood-oil/finish (NL), trade/consumable",
 "yardbarandgrill.com": "off-model: vegan burger food orders",
 "globalturf.com": "off-model: used golf-turf equipment $14k, trade",
 "evivenutrition.com": "off-model: frozen smoothie food, ingestible",
 "wildehousepaper.com": "off-model: journaling course/paper goods, $0.01 digital",
 "furnishit.com": "off-model: reclining sofas/furniture $1499+, bulky",
 "shop.piaule.com": "off-model: premium homeware sheets/vessels $149-349",
 "www.paulschneiderceramics.com": "off-model: ceramic lamps $2045-2940, high-ticket",
 "inhouuse.com": "off-model: acrylic organizers/mugs (EG), regional",
 "abejareina.cl": "off-model: handmade furniture/decor (CL), high-ticket",
 "muskokaliving.com": "off-model: outdoor furniture $995-2155, bulky",
 "www.ukbumpkeys.com": "off-model: lock-pick tools/vices, pro-tool/niche",
 "readyelectricsupply.com": "off-model: LED bulbs/electrical wholesale, trade",
 "honeywellsmartlighting.com": "off-model: floor lamps $799-999, branded/above",
 "coastwoodfurniture.co.nz": "off-model: NZ-made furniture $487-1097, bulky",
 "ruwag.co.za": "off-model: drill bits/fasteners trade (ZA), price-unknown",
 "www.riverridgehome.com": "off-model: kids wall shelves/cabinets, furniture (price-unknown)",
 "www.carlisleco.com": "off-model: wallcoverings/wallpaper, trade (price-unknown)",
 "parkayfloors.com": "off-model: waterproof flooring, material/trade",
 "www.swingcushionsusa.com": "off-model: patio-swing replacement cushions/canopies (price-unknown)",
 "lifetimekidsrooms.com": "off-model: kids beds/furniture (DK), bulky (price-unknown)",
 "universalstatues-us.com": "off-model: fiberglass statues, decor/bulky",
 "cameronmarks.com": "off-model: boutique decor/gifts, mixed",
 "twincitiescrickets.com": "off-model: live feeder crickets (reptile food)",
 "bycocoon.com": "off-model: architectural bathroom design, trade/high-ticket",
 "www.bastbrothers.com": "off-model: garden-center plants/decor",
 "faroslinen.com": "off-model: linen summer shirts (apparel)",
 "www.furnitureworldlv.com": "off-model: liquidation furniture, bulky",
 "www.sparklebarn.com": "off-model: vintage furniture (Seattle), bulky",
 "firealarmdepot.com": "off-model: fire-alarm parts, trade",
 "villagecraftandcandle.com": "off-model: candle-making supplies, DIY/craft",
 "claymoreoutdoor.com": "browse: Claymore outdoor LED lanterns/fans (KR brand), genuine gadget — check range",
 "dinerdrip.com": "off-model: Denny's branded merch/apparel",
 "clock.pe": "off-model: branded watches retailer (PE)",
 "loandcointeriors.com.au": "off-model: luxury cabinetry hardware/handles, trade ($300)",
 "architecturalheritage.com": "off-model: antique architectural salvage/decor, high-ticket",
 "www.everdrop.it": "off-model: eco cleaning tabs/consumable (IT)",
 "onlineshop.ozaki-flowerpark.co.jp": "off-model: flower-park plants/garden (JP)",
}
rows = []
for l in open(OPENS):
    l = l.strip()
    if not l: continue
    d = json.loads(l); d["verdict"] = V.get(d.get("domain", ""),
        "off-model: trade/decor/furniture/plants, not white-label impulse"); rows.append(d)
open(OPENS, "w").write("".join(json.dumps(d, ensure_ascii=False)+"\n" for d in rows))
print("opens: filled", len(rows), "verdicts (all flags, RULE 23)")

def sc(domain, hero, price, problem, wow, emotion, margin, market, veto, score, bucket):
    return {"domain": domain, "hero": hero, "price": price, "problem": problem, "wow": wow,
            "emotion": emotion, "margin": margin, "market": market, "veto": veto,
            "score": score, "bucket": bucket}
SC = [
 # WINNERS (live-opened) —
 sc("thewriggler.com", "The Wriggler Anti-Roll Changing Mat (patented kneepad)", 43.0,
    15, 12, 7, 8, 5, "patented (white-label-exact=no); convergence Yogorgeous(WL)+WriggleBum(Consider) — THE S15 MISS", 68, "winner"),
 sc("inotterspace.com", "OtterSpace Total Blackout Curtain Kit (magnetic, portable)", 129.0,
    15, 13, 7, 5, 5, "Premium $129 (margin cap 5); neuroscientist single-product DT, real sleep pain + demoable", 66, "winner"),
 # BORDERLINE (live-opened) —
 sc("www.luvlink.com.au", "LuvLink Friendship Lamp (tap-to-light paired lamp)", 120.0,
    12, 13, 9, 5, 4, "Premium ~$120; strong emotion but friendship-lamp category saturated (Filimin etc.)", 63, "borderline"),
 sc("chickcozy.com", "ChickCozy Solar Automatic Chicken Coop Door", 159.0,
    15, 12, 7, 5, 3, "Premium $159; real pain+demo but niche market (chicken keepers), branded", 63, "borderline"),
 # REJECTS (explicit, product-level) —
 sc("flawlessfacepillow.com", "Flawless Face Pillow Cloud (anti-wrinkle)", 209.0,
    10, 10, 6, 1, 4, "ABOVE $170 ceiling ($209) + 100k reviews saturated + wrinkle-claim пустышка-lean", 40, "reject"),
 sc("clementinekids.com", "Clementine Kids muslin swaddle / crib bundles", 25.0,
    7, 5, 4, 4, 4, "plain muslin swaddle = apparel, off-model (no functional/tactile differentiator) [guard hit]", 38, "reject"),
 sc("babyboxy.com", "Baby Boxy curated baby gift boxes", 95.0,
    6, 5, 4, 4, 3, "curated gift-box assembly, not a single white-label product [guard hit]", 36, "reject"),
 sc("www.omnitub.co.uk", "Omnitub deep soaking bathtubs", 882.0,
    10, 6, 4, 1, 4, "bathtubs $882-5708 = bulky/high-ticket (RULE 10) [guard false-positive — desired cost]", 30, "reject"),
 # BROWSE — genuine consumer products (Marina's window); bias INCLUDE —
 sc("mywaterfilter.com.au", "Sprite Bath Ball Water Filter $65.99 (+cartridges)", 65.99,
    11, 7, 4, 6, 4, "Muravai-Watchlist-type filter (skin/hair) but multi-product retailer not a hero brand", 52, "browse"),
 sc("www.whallstore.com", "WHALL 4-in-1 UV Mattress Vacuum (anti-mite)", 179.99,
    13, 10, 5, 3, 4, "real anti-dust-mite gadget but $179.99 above range + branded", 50, "browse"),
 sc("www.simplicomfy.com", "Simpli Comfy EZ Bed self-inflating air mattress", 84.0,
    11, 8, 4, 6, 4, "auto-refill ConstantComfort pump (real diff) but bulky/commodity-adjacent, low camera-wow", 49, "browse"),
 sc("grandiogreenhouses.com", "Grandio Automatic Roof Vent Opener (no-power)", 89.0,
    12, 8, 4, 6, 4, "clever passive auto-vent gadget but niche (greenhouse owners)", 48, "browse"),
 sc("createacastle.com", "Create A Castle play molds (Shark Tank, sand/snow)", 50.0,
    9, 9, 5, 5, 4, "genuine Shark Tank kids product, demoable but seasonal/toy", 50, "browse"),
 sc("doorfoto.com", "DoorFoto custom door covers", 59.99,
    7, 7, 4, 6, 4, "novelty seasonal door decor, single-angle", 45, "browse"),
 sc("broview.net", "Broview stackable storage bins", 49.99,
    9, 6, 3, 6, 4, "large stackable storage (200Gal) in-range but bulky/commodity", 44, "browse"),
 sc("www.redcandy.co.uk", "Red Candy quirky homeware/gifts", 32.0,
    6, 7, 4, 4, 4, "quirky-gift multi-product (key bottle opener etc.), mostly below floor", 42, "browse"),
]
open(SCORES, "w").write("".join(json.dumps(s, ensure_ascii=False)+"\n" for s in SC))
w = sum(1 for s in SC if s["bucket"] == "winner"); b = sum(1 for s in SC if s["bucket"] == "borderline")
br = sum(1 for s in SC if s["bucket"] == "browse")
print(f"scores: wrote {len(SC)} -> {w} winners · {b} borderline · {br} browse · rejects {len(SC)-w-b-br}")

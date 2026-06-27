#!/usr/bin/env python3
"""S16 b4 (post-compact) verdict+score filler. Written locally + scp per no-heredoc rule.
Fills np_b4_opens.jsonl verdicts (every flag = RULE 23) + writes np_b4_scores.jsonl
(guard-forced explicit reject for mamashack + curated browse, RULE 32 floor=7, bias=INCLUDE)."""
import json
D = "logs/storeleads/niches/home-and-garden"
OPENS = f"{D}/np_b4_opens.jsonl"; SCORES = f"{D}/np_b4_scores.jsonl"

V = {
 "thetreehouse.shop": "off-model: treehouse-build screws + tool-rental, trade/DIY",
 "eu.loveramics.com": "off-model: B2B coffeeware wholesale platform",
 "hothautehot.com": "off-model: vintage furniture/decor + mixed apparel",
 "www.spessarttraum.de": "off-model: bedding/pillow sets, premium apparel-ish",
 "unitednursery.com": "off-model: live houseplants",
 "it.outin.com": "browse: branded portable travel espresso $215-269 (above range, genuine gadget)",
 "kadimadesign.de": "off-model: solid-wood furniture + wool rugs, bulky",
 "indecrafts.com": "off-model: handcrafted brass/bronze decor",
 "www.piccininibros.com": "off-model: butcher / wholesale meat",
 "www.bradens.com": "off-model: furniture store + interior design",
 "rentaromper.com": "off-model: baby-clothes rental service (apparel)",
 "everysupply.com": "off-model: janitorial/industrial catalog (Glad/Werner)",
 "fittingsplus.com": "off-model: fence/gate trade hardware, below floor",
 "chefsvisionknives.com": "browse: SliceBright glass cutting board $34.95 (commodity, below floor)",
 "ranchpools.co": "off-model: stock-tank pool delivery/install $3750, bulky/service",
 "reluxshop.com": "off-model: luxury resale handbags (LV/Gucci)",
 "custommattress.com": "off-model: custom mattresses $575-749, bulky/above",
 "boxo.no": "browse: wall-storage + drawer-organizer system $13-37 (genuine organizing, below floor)",
 "roshcookwares.in": "off-model: regional traditional cookware, heavy",
 "www.domovstromov.sk": "off-model: plants + garden hand-tools, regional",
 "binibamba.com": "off-model: sheepskin pram liner / baby (premium apparel, cross-niche but off-model)",
 "www.haardcenter.nl": "off-model: ventless bio-ethanol fireplaces $1458+, high-ticket",
 "www.toolmarthou.com": "off-model: industrial tools/saw-blades, trade",
 "epasales.com": "off-model: vacuum-truck parts, trade",
 "smegshop.ca": "off-model: branded SMEG large appliances $1094+",
 "store.stafix.co.za": "off-model: electric-fence trade (ZA)",
 "decure.in": "off-model: branded built-in appliances catalog",
 "lamourartisans.com": "off-model: artisan vintage Guatemalan textile pillows",
 "jooltool.com": "off-model: jeweler/polishing pro-machine $2699 kit, above",
 "www.headboards.co.uk": "off-model: custom made-to-order headboards, bulky/price-unknown",
 "steelfence.com": "off-model: steel-fence trade supply, price-unknown",
 "suncourt.com": "off-model: HVAC duct dampers/fans, trade",
 "www.mikasahospitality.com": "off-model: hospitality/B2B tableware",
 "pierreaugustinrose.com": "off-model: luxury furniture (FR), high-ticket",
 "alturastoneandtile.com": "off-model: natural stone/tile materials, trade",
 "voltecindustries.com": "off-model: industrial power/lighting cords, trade",
 "sewndrapesandshades.com": "off-model: custom-made drapes/blinds $24-153, made-to-order",
 "www.solarogen.com": "off-model: solar LLC, thin/unclear catalog",
 "smokerplans.net": "off-model: digital DIY-smoker build plans (not a physical product)",
 "narcissusstyle.com": "off-model: women's apparel boutique",
 "chandeliers-btq.com": "off-model: chandeliers, lighting decor",
 "www.sheffieldfurniture.com": "off-model: furniture + interiors",
 "www.aicaitaly.it": "off-model: sanitary fixtures, trade (IT)",
 "www.eclecticgoods.com": "off-model: mixed decor goods catalog",
 "www.humphreysbbq.com": "off-model: BBQ smokers, bulky/high-ticket",
 "hautehousehome.com": "off-model: luxury couture furniture/decor",
 "bodrumlinens.com": "off-model: linens / textile (apparel-ish)",
 "dynamicstonetools.com": "off-model: stone-fabrication tools, trade",
 "sixty-nine.us": "off-model: thin/unclear store, no real catalog (prices 0)",
 "handtreatedhome.com": "off-model: DIY-home design blog/content, not a product store",
 "www.modernhomefurniture.com": "dead: ERR after retry (genuinely unreachable)",
 "shopgateopeners.com": "off-model: gate-opener trade/install $108-2800, bulky/above",
 "hitoki.com": "off-model: branded laser botanical device $599, above range",
 "nimara.se": "off-model: Swedish furniture/shelving/desk, bulky",
}
rows = []
for l in open(OPENS):
    l = l.strip()
    if not l: continue
    d = json.loads(l); d["verdict"] = V.get(d.get("domain", ""),
        "off-model: trade/decor/furniture, not white-label impulse"); rows.append(d)
open(OPENS, "w").write("".join(json.dumps(d, ensure_ascii=False)+"\n" for d in rows))
print("opens: filled", len(rows), "verdicts (all flags + device, RULE 23)")

def sc(domain, hero, price, problem, wow, emotion, margin, market, veto, score, bucket):
    return {"domain": domain, "hero": hero, "price": price, "problem": problem, "wow": wow,
            "emotion": emotion, "margin": margin, "market": market, "veto": veto,
            "score": score, "bucket": bucket}
SC = [
 # GUARD HIT — must get an explicit product-level score (CREED #3/#6), never browse-only:
 sc("mamashack.co.uk", "Foldable Travel Changing Mat / Muslin Swaddle", 17.78,
    6, 4, 3, 4, 4, "below-floor commodity ($18 mat / $28 muslin) + plain apparel, no tactile differentiator",
    38, "reject"),
 # BROWSE — Marina's window into the niche (genuine consumer products, not trade); bias=INCLUDE:
 sc("www.nebuluxury.com", "Bluetooth Waterless Scent Diffuser NL100/NL50", 65.0,
    8, 6, 3, 7, 4, "scent diffuser saturated/commodity, low camera-wow", 45, "browse"),
 sc("www.hoodiepillow.com", "HoodiePillow Hooded Pillowcase", 29.95,
    6, 7, 4, 4, 5, "novelty, below floor, single-angle", 44, "browse"),
 sc("www.topseat.com", "Magnetic Quick-Release Wood Toilet Seat", 49.99,
    9, 5, 3, 7, 4, "low wow/impulse, Amazon-commodity toilet seats", 47, "browse"),
 sc("v3clean.fr", "Robot Window-Cleaning Machine V3CLEAN", 204.0,
    11, 8, 4, 4, 4, "above range $204, branded-ish appliance", 48, "browse"),
 sc("www.ectolifestyle.com", "Ecto cooling outdoor chair", 50.0,
    9, 8, 4, 5, 4, "bulky chair (off-model logistics), hero mis-picked", 46, "browse"),
 sc("playdropmats.com", "Playdrop waterproof intimacy mat", 55.0,
    9, 8, 6, 6, 4, "single-product DT novelty; camera-awkward (intimacy), ad-policy risk", 50, "browse"),
 sc("www.birchrobot.com", "Animal pendulum clocks (Frenchie/chicken/robot)", 89.0,
    5, 7, 4, 5, 4, "novelty decor, above-ish, narrow", 43, "browse"),
]
open(SCORES, "w").write("".join(json.dumps(s, ensure_ascii=False)+"\n" for s in SC))
nb = sum(1 for s in SC if s["bucket"] == "browse")
print("scores: wrote", len(SC), f"({nb} browse + chefsvision/boxo/outin tagged in opens; 1 guard reject mamashack)")

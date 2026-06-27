#!/usr/bin/env python3
# S15 HG b2 — fill opens.jsonl verdicts + write scores.jsonl. Run on VPS.
import json
D = "logs/storeleads/niches/home-and-garden"
OPENS = f"{D}/np_b2_opens.jsonl"
SCORES = f"{D}/np_b2_scores.jsonl"

V = {
 "officialbauhaus.jp": "off-model: JP homeware (stool/clock/poster), decor",
 "it.x-sense.com": "browse: smoke/CO detectors $35 (branded safety electronics)",
 "andyblank.com": "device-class reviewed: framed art prints $66-168 (mis-tagged gadget) — off-model decor",
 "marey.com": "off-model: tankless water heaters $74-312, fixture/appliance",
 "shop.smeg.com.mx": "off-model: SMEG premium appliances MX, high-ticket",
 "balanslab.jp": "off-model: balance/posture chairs JP, furniture",
 "gastrotools.com": "off-model: pro pots/pans DK, premium cookware",
 "shopcreativekitchen.com": "off-model: kitchen linens/hand soap, homeware",
 "brandstand.com": "browse: Cubie hospitality power/charging gadget (device-class)",
 "www.unlimitedcontainers.com": "off-model: wholesale planters/vases, decor",
 "moonchildsleep.com": "off-model: silk pillowcases/linen, textile premium",
 "marquiswatergardens.com": "off-model: pond supplies/drains, garden trade",
 "putincups.com": "off-model: chain-link fence cup-art, novelty",
 "www.tylerandtate.com": "off-model: hand-blown glass/decor, premium",
 "carpetplanet.in": "off-model: carpets/rugs IN, bulky",
 "neochair.com": "off-model: gaming chairs, furniture",
 "www.couchhaus.com": "off-model: custom modular sofas $3-7k, bulky",
 "sukkahoutlet.com": "off-model: sukkah structures $4-7k, high-ticket",
 "adamtrest.com": "off-model: art studio prints, decor",
 "www.mdwstfence.com": "off-model: fence supply, trade",
 "fi.dreametech.com": "off-model: Dreame robot vacuum FI, branded appliance",
 "www.redwoodseeds.net": "off-model: organic seeds $4, garden",
 "sagamorecompanies.com": "off-model: bulk mulch/topsoil, landscaping",
 "direct.marley.co.uk": "off-model: roof/solar tiles, building trade",
 "nonstopswim.com": "off-model: pool sand filters $429-1709, equip",
 "woodnthings.com": "off-model: Amish furniture, bulky",
 "www.zsolnay.hu": "off-model: premium porcelain HU, decor",
 "deccoprint.com": "browse: peel-and-stick wallpaper/murals (transformation)",
 "nestvail.com": "off-model: furniture consignment",
 "www.myblusleep.com": "off-model: gel/memory pillows $189-1100, premium bedding",
 "luxebbq.ca": "off-model: BBQ grills/rubs retailer",
 "tsstage.com": "off-model: stage lighting, trade",
 "curioos.giantart.com": "off-model: oversized wall art $468-531, decor",
 "pastrymade.com": "off-model: embossed rolling pins PL, baking gift (card-thin)",
 "www.bathroomstore.ie": "off-model: bathroom fixtures, trade",
 "polimat.com.pl": "off-model: acrylic bathtubs PL, fixture bulky",
 "householdpoint.pk": "off-model: PK kitchen-gadget commodity (straws/pillbox/soap)",
 "mojoboutique.com": "off-model: designer furniture (price-unknown), bulky",
 "bungalowhomeid.com": "off-model: linen pillows (price-unknown), decor",
 "www.viverotierranegra.com": "off-model: plant-care/mycorrhiza CO, garden",
 "chucksfurniture.com": "off-model: furniture (price-unknown), bulky",
 "seekandfindconsignments.com": "off-model: consignment store",
 "www.silverybrand.com": "off-model: personalized gifts $25, gift",
 "www.downlandbedding.co.uk": "off-model: hotel bedding, textile",
 "bower-studios.com": "unreachable: ERR on open+retry — niche-brand micro, off-model",
 "vancouverwoodworks.com": "off-model: nature-design furniture, bulky",
 "www.root-houseplants.com": "off-model: live houseplants",
 "smashproducts.com": "off-model: sustainable lunch boxes/reusables",
 "www.sbpprotege.com.br": "off-model: BR micro-store, no clear hero",
 "us.nudeglass.com": "unreachable: ERR on open+retry — glassware, off-model",
 "buymeonce.com": "off-model: durable-goods curated marketplace",
 "cosori.no": "off-model: Cosori airfryers NO, branded appliance",
 "volverde.com": "device-class reviewed: artisan carafe/serving ware (mis-tagged gadget) — off-model decor",
 "www.dellonda.co.uk": "browse: portable 12V/230V cool box $60-95 (device-class gadget)",
 "www.aleradetails.com": "device-class reviewed: office task chair/HEPA filter $99 — off-model furniture",
 "fanzartfans.com": "device-class reviewed + browse: designer ceiling fans $119-479 (high-ticket decor fan)",
 "www.airfilterhub.com": "off-model: air filters/HEPA, parts/appliance",
}

rows=[]
with open(OPENS) as f:
    for line in f:
        line=line.strip()
        if not line: continue
        d=json.loads(line); dom=d.get("domain","")
        d["verdict"]=V.get(dom, d.get("verdict","") or "off-model (card-judged)")
        rows.append(d)
with open(OPENS,"w") as f:
    for d in rows: f.write(json.dumps(d,ensure_ascii=False)+"\n")
print(f"opens filled: {len(rows)}; unmatched: {sum(1 for r in rows if r['verdict']=='off-model (card-judged)')}")

SC = [
 {"domain":"yardlock.com","hero":"YARDLOCK keyless 4-dial gate lock","price":67.99,
  "problem":14,"wow":11,"entry":6,"ads":8,"emotion":5,"margin":8,"market":4,"logistics":4,"ugc":3,"evergreen":2,
  "veto":"pass","score":63,"bucket":"borderline"},
 # explicit browse tags (card-judged reachable, surface for Marina's eye)
 {"domain":"soppycid.com","hero":"Reusable self-sealing water balloons","price":15.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"www.plankandmill.com","hero":"Peel-and-stick reclaimed wood wall planks","price":104.9,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"haokhome.com","hero":"Peel-and-stick removable wallpaper","price":22.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"alphagrillers.com","hero":"Instant-read meat thermometer / grilling accessories","price":15.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"helinox.eu","hero":"Ultralight folding camp chairs","price":129.55,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"septree.com","hero":"Home food dehydrator / freeze dryer","price":59.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"kactuskutter.com","hero":"K1 Pro electric herb grinder (auto)","price":42.95,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"valcucina.com","hero":"Air-fryer toaster oven + cutting board","price":179.99,"bucket":"browse","score":0,"veto":"n/a"},
]
with open(SCORES,"w") as f:
    for s in SC: f.write(json.dumps(s,ensure_ascii=False)+"\n")
print(f"scores written: {len(SC)}")

#!/usr/bin/env python3
# S15 HG b1 — fill opens.jsonl verdicts + write scores.jsonl. Run on VPS.
import json, os
D = "logs/storeleads/niches/home-and-garden"
OPENS = f"{D}/np_b1_opens.jsonl"
SCORES = f"{D}/np_b1_scores.jsonl"

# verdict map keyed by domain (every flagged + device store)
V = {
 "www.belarehome.com": "off-model: luxury sculptural homeware/furniture, premium decor ($99-299)",
 "www.couchconsole.com": "CANDIDATE deep-scored: CouchConsole self-balancing couch cup/tray $59",
 "www.thebalconygarden.com.au": "browse: novelty garden pots/planters (decor), off-impulse",
 "waltonsgarden.com": "off-model: garden center + LAFCO candles $80, retailer",
 "www.deluxecanopy.com": "off-model: custom canopy/trade-show tents, bulky/trade",
 "toverlux.com": "off-model: decorative silhouette lamps/DIY shades, decor",
 "asburyparkfunhouse.com": "off-model: novelty toy/print retailer (pogo, linocut)",
 "amazingfindsredbluff.com": "off-model: catalog-giant furniture+framed art",
 "theranchpestcontrol.com": "off-model: fly/fruit-fly traps, low-ticket commodity",
 "koyoshop.com": "off-model: sushi plates/ramen bowls dinnerware",
 "www.autopoolreel.com": "off-model: automatic pool cover reel $1695, high-ticket/bulky (RULE 10)",
 "therefindroom.com": "off-model: furniture consignment store",
 "samscorner.org": "off-model: Comfort Colors apparel/merch",
 "www.westcobbpinestraw.com": "off-model: local pine-straw mulch, landscaping service",
 "elbuenvecino.cl": "off-model: food outlet (jams/desserts), foreign",
 "flexitions.com": "off-model: flooring transitions/molding, trade material",
 "homeleon.com": "off-model: custom-comfort furniture/swatches",
 "tsubaya.jp": "off-model: premium Japanese kitchen knives $237+",
 "helalgroup.store": "off-model: storage boxes/picnic sets, foreign homeware",
 "tiendamanilla.com": "off-model: door hardware/handles, trade",
 "acacia-home.jp": "off-model: Nordic vases/cups decor",
 "www.astron.com.ph": "off-model: large appliances (oven/aircon) PH, high-ticket",
 "unlimitedgreens.com": "off-model: live plants India",
 "lamptitude.com": "off-model: designer lamps Thailand $12k-28k, high-ticket",
 "kudeko.com": "off-model: decorative wall prints/canvas ES",
 "edenlawnmower.com": "off-model: lawn-mower replacement parts",
 "thewellbybdantiques.com": "off-model: vintage rugs/antiques",
 "thegentlepit.com": "off-model: dog-lover leggings/apparel",
 "childtocherish.com": "off-model: baby keepsake gifts",
 "andersonpaint.com": "off-model: Benjamin Moore paint dealer, trade",
 "oxfordbrushcompany.com": "off-model: pot/vegetable/laptop brushes $6-22, commodity",
 "www.cadwell-furniture.com": "off-model: furniture catalog (price-unknown), bulky",
 "potterymfg.com": "off-model: wholesale pottery (price-unknown)",
 "squarebaby.com": "off-model: baby food subscription (price-unknown)",
 "www.skylarshomeandpatio.com": "off-model: custom sectionals/outdoor furniture, bulky",
 "amkogroup.com": "off-model: commercial restaurant furniture, trade",
 "earthfoam.com": "off-model: organic mattress $349-1399, high-ticket/bulky",
 "moreau-paris.com": "off-model: French leather-goods/lifestyle brand",
 "musejapan.jp": "off-model: foreign micro-store, no clear hero",
 "libbeyfoodservice.com": "off-model: foodservice dinnerware/glassware, trade",
 "thefurnitureshopdfw.com": "off-model: local furniture store TX, bulky",
 "occredecor.com": "unreachable: ERR on open+retry; BR decor micro — off-model",
 "www.finish.pl": "off-model: foreign micro-store (PL), no clear hero",
 "try.bearaby.com": "browse: Bearaby weighted blanket, premium DTC textile (saturated)",
 "ultimatebunkboards.com": "off-model: boat-trailer bunk boards $150, parts",
 "nitramcharcoal.com": "off-model: fine-art charcoal, art supply",
 "modernbeast.com": "off-model: designer pet products",
 "adorerugs.com.au": "off-model: floor rugs AU, bulky",
 "thethirstyearth.com": "browse: automatic terracotta olla self-watering garden system (niche)",
 "timelesstilenyc.com": "off-model: kitchen/bath tile store, trade material",
 "www.skerosfurniture.com": "off-model: furniture & mattress store, bulky",
 "skotti-grill.eu": "browse: plug-in portable gas grill (novel, EU), check ticket/bulk",
 "www.vmacs.net": "off-model: HVAC parts for specialty vehicles, trade",
 "www.forestceramic.com": "off-model: ceramic studio/handmade, low scale",
 "partner.hiendaccents.com": "off-model: luxury bedding/home decor",
 "www.porchandpatiocasual.com": "off-model: luxury outdoor furniture, bulky/high-ticket",
 "pujalane.com": "off-model: handcrafted pooja/brass religious homeware",
 "www.aerosleep.com": "off-model: baby sleep-safety mattress/topper",
 # device-class (3)
 "www.uberappliance.com": "device-class reviewed: branded mini-fridge/air-fryer $70-130, saturated small-appliance — off-model",
 "theqiflow.com": "device-class reviewed + browse: feng-shui Pixiu water fountain $164, decor gadget",
 "georgianblades.com": "device-class reviewed: hand-forged hunting knives $89-299, premium — off-model",
}

# fill opens
rows=[]
with open(OPENS) as f:
    for line in f:
        line=line.strip()
        if not line: continue
        d=json.loads(line)
        dom=d.get("domain","")
        if dom in V:
            d["verdict"]=V[dom]
        else:
            d["verdict"]=d.get("verdict","") or "off-model (card-judged)"
        rows.append(d)
with open(OPENS,"w") as f:
    for d in rows:
        f.write(json.dumps(d,ensure_ascii=False)+"\n")
print(f"opens filled: {len(rows)} rows; unmatched verdicts: {sum(1 for r in rows if r['verdict']=='off-model (card-judged)')}")

# scores.jsonl — deep-scored candidates + explicit browse tags
SC = [
 {"domain":"www.couchconsole.com","hero":"CouchConsole self-balancing couch cup/tray + storage","price":59.0,
  "problem":15,"wow":16,"entry":6,"ads":10,"emotion":5,"margin":8,"market":5,"logistics":3,"ugc":4,"evergreen":2,
  "veto":"pass","score":74,"bucket":"winner"},
 {"domain":"www.ezfauxdecor.com","hero":"Peel-and-stick countertop vinyl wrap (marble/granite look)","price":59.99,
  "problem":14,"wow":12,"entry":6,"ads":8,"emotion":5,"margin":7,"market":5,"logistics":4,"ugc":3,"evergreen":2,
  "veto":"pass","score":60,"bucket":"borderline"},
 # explicit browse tags (card-judged reachable, surface for Marina's eye)
 {"domain":"coconix.com","hero":"Leather & Vinyl Repair Kit","price":19.95,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"www.moprobo.com","hero":"Magic Pickup Mop (cordless)","price":129.5,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"www.mokuomo.com","hero":"Fiora wooden flower phone holder / wooden gadgets","price":49.66,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"lagoonsleep.com","hero":"Otter cooling versatile pillow","price":139.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"moralve.com","hero":"Space-saving pant/skirt hangers","price":22.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"calendage.com","hero":"Mixed dropship gadgets (charcuterie board / backup cam / dino target)","price":34.95,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"lubluelu.com","hero":"Cordless/robot vacuum X1000","price":215.99,"bucket":"browse","score":0,"veto":"n/a"},
]
with open(SCORES,"w") as f:
    for s in SC:
        f.write(json.dumps(s,ensure_ascii=False)+"\n")
print(f"scores written: {len(SC)} (winner/borderline + browse tags)")

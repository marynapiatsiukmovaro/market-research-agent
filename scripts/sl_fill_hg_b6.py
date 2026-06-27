#!/usr/bin/env python3
import json
D="logs/storeleads/niches/home-and-garden"; OPENS=f"{D}/np_b6_opens.jsonl"; SCORES=f"{D}/np_b6_scores.jsonl"
BROWSE={"getpottd.com.au":"browse: at-home pottery kit (geo-mirror/convergence of b3 getpottd.co.uk)",
 "eu.dryrobe.com":"device-class reviewed + browse: dryrobe towel changing robe $75 (known brand, functional)",
 "www.opolar.com":"device-class reviewed + browse: wall-mount fan w/ remote $59 (small appliance)",
 "germstar.com":"device-class reviewed: touchless hand-sanitizer dispenser $42 (commercial) — off-model",
 "www.awesomewaterfilters.com.au":"device-class reviewed: inline water filters / coolers — off-model trade",
 "thelittlegreenbean.com":"device-class reviewed: embroidery/cross-stitch stands — off-model hobby",
 "www.thehomelightingcentre.co.uk":"device-class reviewed: Anglepoise designer desk lamps $109+ — off-model lighting",
 "stonehousedahlias.com":"off-model: dahlia tubers (mis-tagged gadget)"}
OFF="off-model (card-judged: decor/lamps/furniture/bedding/plants/candles/baby/flooring/cookware/foreign micro)"
rows=[]
for l in open(OPENS):
    l=l.strip()
    if not l: continue
    d=json.loads(l); d["verdict"]=BROWSE.get(d.get("domain",""),OFF); rows.append(d)
open(OPENS,"w").write("".join(json.dumps(d,ensure_ascii=False)+"\n" for d in rows))
print("opens:",len(rows))
SC=[
 {"domain":"iceblankets.com","hero":"FreezeCore cooling blanket","price":279.0,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"shop.geme.bio","hero":"GEME electric home bio-waste composter","price":599.0,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"laceanchors.com","hero":"Lace Anchors no-tie shoelace system","price":15.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"www.gleener.com","hero":"Gleener 4-in-1 fabric shaver / de-piller","price":19.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"www.opolar.com","hero":"Opolar wall-mount fan w/ remote","price":59.0,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"eu.dryrobe.com","hero":"Dryrobe organic towel changing robe","price":75.6,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"imaginariumandco.com","hero":"Dream Plush adjustable wedge pillow","price":45.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"getpottd.com.au","hero":"At-home air-dry pottery kit (geo-mirror)","price":58.74,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"www.elecwish.com","hero":"4-in-1 evaporative air cooler / solar umbrella","price":99.99,"bucket":"browse","score":0,"veto":"n/a"},
]
open(SCORES,"w").write("".join(json.dumps(s,ensure_ascii=False)+"\n" for s in SC))
print("scores:",len(SC))

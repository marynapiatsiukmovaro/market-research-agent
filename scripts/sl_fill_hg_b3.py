#!/usr/bin/env python3
import json
D="logs/storeleads/niches/home-and-garden"; OPENS=f"{D}/np_b3_opens.jsonl"; SCORES=f"{D}/np_b3_scores.jsonl"
BROWSE={"e-foldimate.com":"browse: FOLDIMATE laundry-folding machine $319 (viral gadget, high-ticket)",
 "snapbuy.us":"browse: mini projector / wet-dry vac (dropship gadget)"}
OFF="off-model (card-judged: garden/woodwork/knives/furniture/plants/pool/parts/foreign micro)"
rows=[]
for l in open(OPENS):
    l=l.strip()
    if not l: continue
    d=json.loads(l); dom=d.get("domain","")
    d["verdict"]=BROWSE.get(dom, OFF)
    rows.append(d)
open(OPENS,"w").write("".join(json.dumps(d,ensure_ascii=False)+"\n" for d in rows))
print("opens filled:",len(rows))
SC=[
 {"domain":"e-foldimate.com","hero":"FOLDIMATE automatic laundry folder","price":319.68,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"snapbuy.us","hero":"Mini projector / wet-dry vac (dropship)","price":79.9,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"getpottd.co.uk","hero":"At-home air-dry pottery kit","price":55.88,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"glidelok.com","hero":"GlideLok child-safety door lock","price":27.97,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"turbotrusser.com","hero":"Turbo Trusser BBQ poultry trusser","price":19.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"vinturi.com","hero":"Vinturi wine aerator","price":49.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"stooly.fr","hero":"Foldable stool (as-seen-on-TV)","price":73.44,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"heatsbox.com","hero":"HeatsBox heated lunchbox","price":144.48,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"checkout.everdrop.de","hero":"Everdrop refill cleaning tabs","price":8.63,"bucket":"browse","score":0,"veto":"n/a"},
]
open(SCORES,"w").write("".join(json.dumps(s,ensure_ascii=False)+"\n" for s in SC))
print("scores:",len(SC))

#!/usr/bin/env python3
import json
D="logs/storeleads/niches/home-and-garden"; OPENS=f"{D}/np_b7_opens.jsonl"; SCORES=f"{D}/np_b7_scores.jsonl"
BROWSE={"www.mydepot.com":"device-class reviewed + browse: bladeless tower fan $55-139 (small appliance)",
 "uk.squishable.com":"device-class reviewed: Squishable plush / blind-box $26-57 (novelty toy) — off-model",
 "www.lapetitemaison.us":"device-class reviewed: luxury robe/throws (mis-tagged) — off-model textile"}
OFF="off-model (card-judged: furniture/decor/bedding/plants/lighting/cookware/baby/trade/foreign micro)"
rows=[]
for l in open(OPENS):
    l=l.strip()
    if not l: continue
    d=json.loads(l); d["verdict"]=BROWSE.get(d.get("domain",""),OFF); rows.append(d)
open(OPENS,"w").write("".join(json.dumps(d,ensure_ascii=False)+"\n" for d in rows))
print("opens:",len(rows))
SC=[
 {"domain":"refreshedshoecleaner.com","hero":"Refreshed shoe-cleaning care kit","price":39.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"naipo.de","hero":"Naipo shiatsu neck massager w/ heat","price":64.79,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"rockitsleep.com","hero":"Rockit portable stroller rocker (CONVERGENCE w/ Nursery winner)","price":59.95,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"therumblejar.com","hero":"Rumble Go portable cold-brew maker","price":44.0,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"www.mydepot.com","hero":"Bladeless tower fan","price":55.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"jerryrigknife.com","hero":"JerryRig utility tool / razor knife","price":14.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"streamlinenyc.com","hero":"Capybara color-changing LED tap light","price":9.0,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"www.boxblayde.com","hero":"BoxBlayde electric box cutter","price":69.0,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"snoofybee.com","hero":"Playtime changing pad / Queen Bee diaper bag","price":38.24,"bucket":"browse","score":0,"veto":"n/a"},
]
open(SCORES,"w").write("".join(json.dumps(s,ensure_ascii=False)+"\n" for s in SC))
print("scores:",len(SC))

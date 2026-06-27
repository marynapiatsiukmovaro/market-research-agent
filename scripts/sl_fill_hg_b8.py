#!/usr/bin/env python3
import json
D="logs/storeleads/niches/home-and-garden"; OPENS=f"{D}/np_b8_opens.jsonl"; SCORES=f"{D}/np_b8_scores.jsonl"
BROWSE={"jp.morus.com":"browse: adsorption clothes steamer / 3-sec instant hot-water pot $51-84 (gadget)",
 "www.insightcordlesslighting.com":"device-class reviewed + browse: cordless rechargeable table lamps $85 (no-wiring)"}
OFF="off-model (card-judged: furniture/decor/bedding/lighting/plants/garden/trade/flooring/foreign micro)"
rows=[]
for l in open(OPENS):
    l=l.strip()
    if not l: continue
    d=json.loads(l); d["verdict"]=BROWSE.get(d.get("domain",""),OFF); rows.append(d)
open(OPENS,"w").write("".join(json.dumps(d,ensure_ascii=False)+"\n" for d in rows))
print("opens:",len(rows))
SC=[
 {"domain":"sofascratcher.com","hero":"Sofa-Scratcher cat couch-corner scratch protector","price":54.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"mrbinhome.com","hero":"Motion-sensor butterfly-lid bathroom trash can","price":89.0,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"www.dustopper.com","hero":"Dustopper cyclone dust separator","price":25.0,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"jp.morus.com","hero":"Morus adsorption clothes steamer / instant hot-water pot","price":84.48,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"www.insightcordlesslighting.com","hero":"Cordless rechargeable table lamps","price":85.09,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"inspiraspark.com","hero":"Little Balance Box adjustable push-walker","price":129.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"www.vipek.com","hero":"VIPEK heavy-duty rolling clothes rack","price":119.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"lighterbro.com","hero":"LighterBro lighter-holder multi-tool case","price":19.99,"bucket":"browse","score":0,"veto":"n/a"},
 {"domain":"getbrickshield.com","hero":"BrickShield temporary Lego glue spray","price":15.99,"bucket":"browse","score":0,"veto":"n/a"},
]
open(SCORES,"w").write("".join(json.dumps(s,ensure_ascii=False)+"\n" for s in SC))
print("scores:",len(SC))

# Export all tracked-shop collections grouped by niche: NAME · domain · SH-link.
# Joins each niche's seed shop_ids (from seed files / add-logs) against its category dump.
import json, re, os
OUT = "/opt/market-research-agent/logs/shophunter"

def ids_from_addlog(path):
    ids = []
    if not os.path.exists(path):
        return ids
    for ln in open(path):
        m = re.search(r"\bADDED\s+(\d+)", ln)
        if m:
            ids.append(m.group(1))
    return ids

def ids_from_txt(path):
    if not os.path.exists(path):
        return []
    return re.findall(r"\d+", open(path).read())

def ids_from_jsonlist(path):
    if not os.path.exists(path):
        return []
    return [str(x) for x in json.load(open(path))]

def load_dump(path):
    d = {}
    if not os.path.exists(path):
        return d
    for r in json.load(open(path)):
        d[str(r.get("shop_id"))] = (r.get("name", ""), r.get("domain", ""))
    return d

NICHES = [
    ("Home & Garden", ids_from_addlog("/tmp/hg_addcoll.log"), OUT + "/hg_shops_1000.json"),
    ("Baby & Toddler", ids_from_jsonlist(OUT + "/bt_collection_final.json"), OUT + "/baby_toddler_shops.json"),
    ("Arts & Entertainment", ids_from_addlog("/tmp/ae_coll_aen.log") or ids_from_addlog("/tmp/ae_coll_shops.log"), OUT + "/arts_entertainment_shops.json"),
    ("Animals & Pet Supplies", ids_from_txt(OUT + "/ap_seed_ids.txt"), OUT + "/animals_pet_supplies_shops.json"),
]

for name, ids, dumppath in NICHES:
    seen = []
    for i in ids:
        if i not in seen:
            seen.append(i)
    dump = load_dump(dumppath)
    print("\n=== %s — %d shops ===" % (name, len(seen)))
    for sid in seen:
        nm, dom = dump.get(sid, ("(not in dump)", ""))
        print("%s\t%s\thttps://app.shophunter.io/shops/%s" % (nm[:34], dom, sid))

# --- TSV emitter (SH-10 add) ---
import sys
if "--tsv" in sys.argv:
    rows = []
    for name, ids, dumppath in NICHES:
        seen = []
        for i in ids:
            if i not in seen:
                seen.append(i)
        dump = load_dump(dumppath)
        for sid in seen:
            nm, dom = dump.get(sid, ("(not in dump)", ""))
            rows.append((name, nm.replace("\t"," ").strip(), dom, sid, "https://app.shophunter.io/shops/%s" % sid))
    with open(OUT + "/tracked_shops_export.tsv", "w") as f:
        f.write("niche\tname\tdomain\tshop_id\tsh_link\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    print("TSV written:", OUT + "/tracked_shops_export.tsv", "| rows:", len(rows))

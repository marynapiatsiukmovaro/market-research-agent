#!/usr/bin/env python3
# OBSERVATION ONLY (does not touch funnel): classify each store of a batch into a sub-niche
# by keyword-matching title + top-product names. Priority order = first match wins.
import json, sys, collections, re

BUCKETS = [
 ("furniture",      ["sofa","sectional","couch","armchair","recliner","nightstand","dresser","credenza","sideboard","wardrobe","bookcase","coffee table","dining table","desk","bed frame","bunk","headboard","ottoman","bar stool","barstool","loveseat","chaise","cabinet","furniture","console table","tallboy","chest of drawer"]),
 ("mattress/sleep", ["mattress","memory foam","topper","box spring","adjustable bed","sleep "]),
 ("bedding/textile",["bedding","duvet","bed sheet","sheet set","fitted sheet","pillowcase","linen","quilt","comforter","throw blanket","blanket","towel","bathrobe","cushion cover","draught","curtain","drape"]),
 ("decor/art",      ["wall art","wall decor","canvas","poster","print","tapestry","sculpture","figurine","ornament","photo frame","picture frame","vase","artificial","faux flower","faux plant","decorative","home decor","wall hanging","mirror"]),
 ("candle/fragrance",["candle","fragrance","diffuser","scented","soy wax","reed diffuser","incense","perfume","room spray","wax melt"]),
 ("rug/carpet",     ["rug","carpet","area rug","runner"]),
 ("kitchen/cookware",["knife","cookware","frying pan","saucepan","skillet","cutlery","dinnerware","tableware","porcelain","ceramic plate","cooking","utensil","spatula","cutting board","wok","kettle","coffee","espresso","barista","grinder","baking","rolling pin","mug","drinkware","tumbler","glassware","pottery"]),
 ("bbq/outdoor-cook",["bbq","grill","smoker","fire pit","firepit","pizza oven","kamado","charcoal","griddle","cooler","fire kettle"]),
 ("garden/plants",  ["plant","garden","seed","nursery","dahlia","bonsai","succulent","orchid","palm","tree","mulch","soil","lawn","planter","flower","fertilizer","greenhouse","compost","terrarium","cacti","cactus","bulb","shrub","fruit tree"]),
 ("lighting",       ["lamp","chandelier","sconce","pendant light","lighting","light fixture","led light","floor lamp","table lamp","wall light","desk lamp"]),
 ("bath/fixture",   ["bath","shower","toilet","sink","faucet","vanity","tile","tap","drain","bidet","tub","wainscot","mirror cabinet"]),
 ("tools/trade/parts",["tool","drill","saw","hardware","fence","lumber","paint","flooring","parts","supply","filter","pump","battery","lock","hinge","screw","wire","fastener","lock pick","window hardware","door hardware","caulk","sealer","grout","adhesive","stone","gravel","paver"]),
 ("appliance/gadget",["vacuum","robot","air cooler","air purifier","dehumidifier","air fryer","fryer","blender","heater","fridge","freezer","refrigerator","microwave","fan ","ceiling fan","sanitizer","projector","humidifier","mower","dishwasher","washing machine","sterilizer","ice maker","espresso machine"]),
 ("baby/kids",      ["baby","toddler","nursery","swaddle","diaper","stroller","crib","newborn","infant","kids bed","playmat","play mat","teether","pacifier","incubator"]),
 ("pet",            ["pet","dog","cat ","puppy","kitten","aquarium"]),
 ("food/ingestible",["coffee bean","tea ","spice","seasoning","rub","sauce","jam","chocolate","snack","syrup","honey","food hall","gourmet","smoothie","formula"]),
 ("apparel/accessory",["apparel","clothing","t-shirt","shirt","hat","cap ","sandal","sneaker","shoe","legging","jumper","sweater","scarf","bag","tote","sleepwear","robe","sock","dress","bikini","swimsuit"]),
 ("cleaning/laundry",["cleaning","detergent","cleaner","laundry","refuse","bin liner","mop","microfiber","stain remover","fabric shaver","wipe"]),
 ("pool/spa",       ["pool","spa","sauna","hot tub","cold plunge","jacuzzi"]),
]

def classify(text):
    t = text.lower()
    for name, kws in BUCKETS:
        for kw in kws:
            if kw in t:
                return name
    return "other/consumer"

def blob(store):
    parts=[store.get("title","") or "", store.get("home_pitch","") or "", store.get("product_class","") or ""]
    for tp in (store.get("tops") or store.get("candidates") or []):
        if isinstance(tp,dict):
            parts.append(tp.get("title","") or tp.get("name","") or "")
    return " ".join(parts)

D="logs/storeleads/niches/home-and-garden"
overall=collections.Counter()
print(f"{'batch':6} " + "sub-niche profile (top buckets)")
for b in sys.argv[1:]:
    s=json.load(open(f"{D}/hg_{b}_enriched.json"))
    c=collections.Counter()
    cat_giant=0
    for x in s:
        if x.get("store_type")=="catalog-giant": cat_giant+=1
        c[classify(blob(x))]+=1
        overall[classify(blob(x))]+=1
    top=", ".join(f"{k} {v}" for k,v in c.most_common(8))
    print(f"{b:6} catalog-giant={cat_giant:3} | {top}")
print("="*70)
print("TOTAL b3-b6:", ", ".join(f"{k} {v}" for k,v in overall.most_common(14)))

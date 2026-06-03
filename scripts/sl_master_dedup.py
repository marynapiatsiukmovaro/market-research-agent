#!/usr/bin/env python3
"""Store Leads — cross-niche MASTER dedup (S8, Marina-approved 2026-06-03).

One master registry of every domain we already have (any niche, analysed or just dumped).
Every NEW niche dump is checked against it: overlapping (multi-category) stores are removed
so we never enrich/analyse the same store twice. The master GROWS niche by niche.

Why: a Store Leads card is tagged with MULTIPLE categories, so one store surfaces in several
niche dumps. processed_domains.json only excludes ALREADY-ANALYSED stores; this also catches
stores sitting in another niche's reservoir / a sibling dump. (RULE 19 generalised cross-niche.)

Domain match form (Marina-confirmed): lowercase + strip scheme/path + strip a leading "www.".
Subdomains are kept distinct (my.x.com != x.com — they ARE different stores in Store Leads);
www. is the only safe strip so a formatting diff never reads as two different stores.

USAGE
  Seed / extend the master from existing pools (each <file> <label> pair):
    sl_master_dedup.py seed  <master.json> <file1> <label1> [<file2> <label2> ...]
  Dedup a fresh niche dump against the master (dry-run by default):
    sl_master_dedup.py dedup <master.json> <new_full.json> <niche_label> [--apply]
      --apply  : write <new_full>_dedup.json (records minus overlap) AND add the unique
                 domains into the master under <niche_label>.

A *_full.json is a list of records (domain field); processed_domains.json is a dict keyed by
domain. Both are auto-detected.
"""
import json, sys, os, datetime


def norm(d):
    d = str(d).strip().lower()
    for p in ("http://", "https://"):
        if d.startswith(p):
            d = d[len(p):]
    d = d.split("/")[0].split("?")[0]
    if d.startswith("www."):
        d = d[4:]
    return d.rstrip(".")


def domains_of(path):
    """Extract the normalized domain set from a *_full.json (list) or a domain-keyed dict."""
    d = json.load(open(path))
    out = []
    if isinstance(d, dict) and isinstance(d.get("domains"), (list, dict)):
        d = d["domains"]
    if isinstance(d, list):
        for r in d:
            if isinstance(r, dict):
                v = r.get("domain") or r.get("tld1") or r.get("merchant")
                if v:
                    out.append(norm(v))
            elif r:
                out.append(norm(r))
    elif isinstance(d, dict):
        out = [norm(k) for k in d.keys()]
    return out


def load_master(path):
    if os.path.exists(path):
        m = json.load(open(path))
        m.setdefault("domains", {})
        m.setdefault("_meta", {"niches": {}})
        return m
    return {"_meta": {"niches": {}}, "domains": {}}


def save_master(path, m):
    json.dump(m, open(path, "w"), ensure_ascii=False, indent=0)


def today():
    return datetime.date.today().isoformat()


def cmd_seed(master_path, pairs):
    if len(pairs) % 2:
        sys.exit("seed needs <file> <label> pairs")
    m = load_master(master_path)
    for i in range(0, len(pairs), 2):
        f, label = pairs[i], pairs[i + 1]
        doms = domains_of(f)
        added = 0
        for dom in doms:
            if dom and dom not in m["domains"]:
                m["domains"][dom] = label
                added += 1
        m["_meta"]["niches"][label] = m["_meta"]["niches"].get(label, 0) + added
        print(f"  + {label:24} {f}: {len(doms)} domains read, {added} new added")
    m["_meta"]["seeded"] = today()
    save_master(master_path, m)
    print(f"MASTER now holds {len(m['domains'])} unique domains across "
          f"{len(m['_meta']['niches'])} labels  ->  {master_path}")


def cmd_dedup(master_path, new_path, niche, apply):
    m = load_master(master_path)
    raw = json.load(open(new_path))
    records = raw["domains"] if isinstance(raw, dict) and isinstance(raw.get("domains"), list) else raw
    if not isinstance(records, list):
        sys.exit("dedup expects a *_full.json that is a list of store records")

    seen_master = m["domains"]
    overlap_by_label, kept, removed = {}, [], 0
    seen_in_this_dump = set()
    for r in records:
        dom = norm(r.get("domain") or r.get("tld1") or r.get("merchant") or "")
        if not dom:
            continue
        if dom in seen_master:                      # already ours (another niche / processed)
            lbl = seen_master[dom]
            overlap_by_label[lbl] = overlap_by_label.get(lbl, 0) + 1
            removed += 1
            continue
        if dom in seen_in_this_dump:                # intra-dump duplicate
            removed += 1
            continue
        seen_in_this_dump.add(dom)
        kept.append(r)

    print(f"\n=== MASTER DEDUP — {niche} ===")
    print(f"dumped (records)      : {len(records)}")
    print(f"removed (overlap+dup) : {removed}")
    if overlap_by_label:
        for lbl, n in sorted(overlap_by_label.items(), key=lambda x: -x[1]):
            print(f"   - already in '{lbl}': {n}")
    print(f"UNIQUE kept           : {len(kept)}")
    print(f"master size (before)  : {len(seen_master)}")

    if apply:
        out = os.path.splitext(new_path)[0] + "_dedup.json"
        json.dump(kept, open(out, "w"), ensure_ascii=False)
        for r in kept:
            dom = norm(r.get("domain") or r.get("tld1") or r.get("merchant") or "")
            if dom:
                m["domains"][dom] = niche
        m["_meta"]["niches"][niche] = m["_meta"]["niches"].get(niche, 0) + len(kept)
        save_master(master_path, m)
        print(f"--apply: wrote {out} ({len(kept)} unique records)")
        print(f"master size (after)   : {len(m['domains'])}")
    else:
        print("(dry-run — pass --apply to write the deduped file + grow the master)")


def main():
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    cmd = a[0]
    if cmd == "seed":
        cmd_seed(a[1], a[2:])
    elif cmd == "dedup":
        apply = "--apply" in a
        rest = [x for x in a[2:] if x != "--apply"]
        cmd_dedup(a[1], rest[0], rest[1], apply)
    else:
        sys.exit(f"unknown cmd '{cmd}' (use seed|dedup)")


if __name__ == "__main__":
    main()

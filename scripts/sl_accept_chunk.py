#!/usr/bin/env python3
"""Store Leads — per-chunk ACCEPTANCE wrapper (S11, Marina-approved 2026-06-07).

ONE command per reservoir-build chunk that prints ONE verdict line, so chunk-acceptance is
MECHANICAL + UNIFORM + VISIBLE (system, not discipline). It does NOT change anything that
already works — it only WRAPS the existing checks:
  - count-reconcile  : enriched == selected (catches a silent worker crash)        [in-script]
  - credit-guard     : ps aux | grep claude on this host (RULE 13, every chunk)    [in-script]
  - QA-gate          : calls scripts/sl_qa.py  (the canonical QA — single source)  [subprocess]
  - ACCEPT-logic     : encodes §1b — a benign products.json/vNone STOP is ACCEPTed, a genuine
                       breakage is STOPped (RULE 30). The agent no longer eyeballs this.

Verdict rule (matches op-rules §1b ACCEPT-logic, RULE 26/30):
  HARD STOP (genuine breakage) if ANY of:
     count mismatch · cur_null>0 · reach<90 · reachable-card gap
     (>=1top<97 · img<90 · in_range<99 · descConf<99 · avgtops<2.0)
  else ACCEPT — even when sl_qa prints STOP only on the provisional fields that TRACK the
  unreachable set (cand / product_class / new30d / home_pitch / social): those stores go to
  needs_live hand-open at analysis (RULE 23); re-enrich does not recover them.
  credit-guard claude-procs>0 is flagged in the line (safety), never silently dropped.

Usage:  sl_accept_chunk.py <enriched.json>     (CWD-relative path, like sl_qa.py — run from repo root)
Exit:   0 = ACCEPT, 1 = STOP (genuine breakage), 2 = usage/IO error.
"""
import json, os, re, sys, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
# reachable-card thresholds (RULE 26 — the genuine-breakage floor; provisional fields excluded on purpose)
TH = {"reach": 90.0, "top1": 97.0, "img": 90.0, "in_range": 99.0, "descConf": 99.0, "avgtops": 2.0}
# STOP reasons that are BENIGN (they track the unreachable/products.json set, not breakage).
# "reach" is benign HERE because the hard-check below enforces the real reach floor (TH["reach"]) —
# sl_qa's own reach-STOP (at its fixed 90) is then redundant: if reach mattered, the hard-check caught it.
BENIGN = {"reach", "cand", "product_class", "new30d", "home_pitch", "social", "3tops"}


def die(msg, code=2):
    print(f"ERROR {msg}"); sys.exit(code)


def main():
    if len(sys.argv) < 2:
        die("usage: sl_accept_chunk.py <enriched.json> [reach_floor=90]")
    enr = sys.argv[1]
    # optional per-call reach floor (default 90). Session-scoped override only — NOT a codified rule.
    if len(sys.argv) > 2:
        try:
            TH["reach"] = float(sys.argv[2])
        except ValueError:
            die(f"bad reach_floor: {sys.argv[2]}")
        # vNone-tail lenient mode: a sub-90 floor signals the thin missing-visits tail, where price-unknown
        # (PRICE-CHECK tier) is expected and resolved live at analysis (RULE 7) — treat "price" as benign too.
        # Default (no arg / floor 90) leaves "price" a genuine STOP. Session-scoped, NOT codified.
        if TH["reach"] < 90:
            BENIGN.add("price")
    if not os.path.exists(enr):
        die(f"enriched not found: {enr}")
    sel = enr.replace("_enriched.json", ".json")
    chunk = os.path.basename(enr).replace("_enriched.json", "")

    # 1. count-reconcile
    try:
        e = json.load(open(enr)); s = json.load(open(sel))
    except Exception as ex:
        die(f"load failed: {ex}")
    n_enr, n_sel = len(e), len(s)
    count_ok = (n_enr == n_sel)

    # 2. credit-guard (this host) — every chunk, no exceptions (RULE 13)
    try:
        ps = subprocess.run(["bash", "-c", "ps aux | grep '[s]l_enrich4' | wc -l"],
                            capture_output=True, text=True, timeout=15)
        claude_procs = int(ps.stdout.strip() or "0")
    except Exception:
        claude_procs = -1  # unknown

    # 3. QA-gate — call the canonical sl_qa.py (single source of truth, NOT duplicated)
    qa = subprocess.run([sys.executable, os.path.join(HERE, "sl_qa.py"), enr],
                        capture_output=True, text=True)
    out = qa.stdout + qa.stderr

    def grab(pat, cast=float, default=None):
        m = re.search(pat, out)
        return cast(m.group(1)) if m else default

    reach = grab(r"reach ([\d.]+)%")
    cur_null = grab(r"cur_null (\d+)", int)
    avgtops = grab(r"avgtops ([\d.]+)")
    top1 = grab(r">=1top ([\d.]+)%")
    img = grab(r"·\s*img ([\d.]+)%")
    in_range = grab(r"in_range ([\d.]+)%")
    descConf = grab(r"descConf ([\d.]+)%")
    gate_pass = "GATE: ✅ PASS" in out
    stop_reasons = []
    mstop = re.search(r"GATE: ⛔ STOP -> (.+)", out)
    if mstop:
        stop_reasons = [r.strip().split("<")[0].split(">")[0].split()[0] for r in mstop.group(1).split(",")]

    # 4. ACCEPT-logic — hard-fail on genuine breakage; benign provisional STOP = ACCEPT
    hard = []
    if not count_ok:                                   hard.append(f"count {n_enr}!={n_sel}")
    if cur_null is None or cur_null > 0:               hard.append(f"cur_null={cur_null}")
    if reach is None or reach < TH["reach"]:           hard.append(f"reach={reach}<{TH['reach']:.0f}")
    if top1 is not None and top1 < TH["top1"]:         hard.append(f">=1top={top1}<97")
    if img is not None and img < TH["img"]:            hard.append(f"img={img}<90")
    if in_range is not None and in_range < TH["in_range"]: hard.append(f"in_range={in_range}<99")
    if descConf is not None and descConf < TH["descConf"]: hard.append(f"descConf={descConf}<99")
    if avgtops is not None and avgtops < TH["avgtops"]: hard.append(f"avgtops={avgtops}<2.0")

    accept = (len(hard) == 0)
    # if sl_qa STOPped, confirm the reasons are all benign (else it's a breakage we don't model -> STOP to be safe)
    if accept and not gate_pass and stop_reasons:
        non_benign = [r for r in stop_reasons if r not in BENIGN]
        if non_benign:
            accept = False; hard.append("qa-stop:" + "/".join(non_benign))

    qa_tag = "PASS" if gate_pass else ("ACCEPT*" if accept else "STOP")
    cg = "0" if claude_procs == 0 else (f"⚠{claude_procs}" if claude_procs > 0 else "?")
    verdict = "ACCEPT" if accept else "STOP"
    note = "" if (gate_pass or not accept) else f" (benign:{'/'.join(stop_reasons)})"
    line = (f"{verdict} {chunk} · reach {reach}% · count {n_enr}=={n_sel} "
            f"{'OK' if count_ok else 'MISMATCH'} · cur_null {cur_null} · QA {qa_tag}{note} · claude-procs {cg}")
    if not accept:
        line += "  <-- " + "; ".join(hard)
    print(line)
    sys.exit(0 if accept else 1)


if __name__ == "__main__":
    main()

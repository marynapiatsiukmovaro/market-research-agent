#!/usr/bin/env python3
"""sl_card_parity.py — do the founder and the agent see the SAME card? (S18, Marina-approved)

WHY THIS EXISTS — the failure it makes impossible:
  For 27 batches the founder read a rich HTML card while the agent read a text projection that had
  silently dropped `home_hero` (the homepage-banner product — added to the enricher precisely because
  the best-seller auto-pick misfires), `bullets`, `desc_confidence`, `pust`, `kind`, and the unreachable
  reason. Nobody noticed, because **the absence of a field has no symptom**: the text looked complete —
  rows, domains, three products, prices. You cannot see a field that was never printed.
  Nothing in the system had ever asked the one question: "do these two surfaces show the same thing?"
  (The HTML was not innocent either — it rendered neither `pust` nor `kind`, both Marina-Veto inputs.)

WHAT IT DOES (counts, never judges):
  Runs both canonical renderers on the same enriched file, reads the machine-readable `CERT` line each
  prints, and compares: stores · products · banner-heroes · the CONTRACT FIELD LIST. Any divergence = STOP,
  because it means one of us is judging on less than the other.

Usage: python3 sl_card_parity.py <enriched.json>
Exit:  0 = surfaces agree, 1 = they diverge, 2 = a renderer failed / no CERT line.
"""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def cert_of(cmd):
    """Run a renderer, return its CERT line parsed into a dict."""
    p = subprocess.run(cmd, capture_output=True, text=True)
    for ln in (p.stdout + p.stderr).splitlines():
        if ln.startswith("CERT "):
            d = {}
            for kv in ln[5:].split():
                k, _, v = kv.partition("=")
                d[k] = v
            return d
    print(f"⛔ no CERT line from: {' '.join(cmd)}")
    if p.returncode:
        print((p.stdout + p.stderr)[-400:])
    return None


def main():
    if len(sys.argv) < 2:
        print("usage: sl_card_parity.py <enriched.json>")
        sys.exit(2)
    enr = sys.argv[1]
    if not os.path.exists(enr):
        print(f"ERROR enriched not found: {enr}")
        sys.exit(2)

    with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as tmp:
        html_out = tmp.name
    try:
        agent = cert_of([sys.executable, os.path.join(HERE, "sl_project_any.py"), enr])
        founder = cert_of([sys.executable, os.path.join(HERE, "sl_stage2_table.py"),
                           enr, html_out, "parity-check", ""])
    finally:
        if os.path.exists(html_out):
            os.unlink(html_out)

    if not agent or not founder:
        sys.exit(2)

    print("=" * 74)
    print("CARD PARITY — видит ли агент то же, что founder?")
    print("=" * 74)

    diffs = []
    for k in ("stores", "products", "banners"):
        a, f = agent.get(k), founder.get(k)
        mark = "✅" if a == f else "⛔"
        if a != f:
            diffs.append(f"{k}: agent={a} founder={f}")
        print(f"  {mark} {k:<10} agent {a:>6}   founder {f:>6}")

    fa = set(filter(None, agent.get("fields", "").split(",")))
    ff = set(filter(None, founder.get("fields", "").split(",")))
    only_a, only_f = sorted(fa - ff), sorted(ff - fa)
    if only_a or only_f:
        diffs.append(f"fields diverge: only-agent={only_a} only-founder={only_f}")
    print(f"  {'✅' if not (only_a or only_f) else '⛔'} fields     {len(fa)} contract fields, identical on both surfaces"
          if not (only_a or only_f) else
          f"  ⛔ fields     only-agent={only_a} · only-founder={only_f}")

    print()
    if diffs:
        print("⛔ PARITY STOP — поверхности расходятся. Один из нас судит по меньшему:")
        for d in diffs:
            print("     -", d)
        print("   Не анализировать, пока не сойдутся (RULE 25).")
        sys.exit(1)
    print(f"✅ PARITY PASS — обе поверхности показывают одну карточку: "
          f"{agent['stores']} магазинов · {agent['products']} товаров · {agent['banners']} баннер-героев · "
          f"{len(fa)} полей контракта.")
    sys.exit(0)


if __name__ == "__main__":
    main()

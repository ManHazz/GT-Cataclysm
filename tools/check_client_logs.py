#!/usr/bin/env python3
"""Scan a client game dir's logs for content errors (Patchouli, GuideME, KubeJS, Ponder, crashes)."""
import argparse, glob, os, re, sys

# (category, regex) - matched per line, case-insensitive; first match wins
RULES = [
    ("patchouli", re.compile(r"/(ERROR|FATAL)\].*patchouli|patchouli.*(failed to load|error loading|could not load|invalid book|exception)", re.I)),
    ("guideme", re.compile(r"references an unknown item|malformed item_ids|Failed to parse GuideME page|Cannot validate guide|/(ERROR|FATAL)\].*guideme|guideme.*(validation failed|exception)", re.I)),
    ("ponder", re.compile(r"/(ERROR|FATAL)\].*ponder|ponder(js)?.*(failed|exception|error)", re.I)),
    ("kubejs", re.compile(r"/(ERROR|FATAL)\].*kubejs|Error loading KubeJS script|Failed to (load|run) script", re.I)),
    ("generic", re.compile(r"Exception caught during firing event|Encountered an unexpected exception", re.I)),
]
KJS_SUMMARY = re.compile(r"Loaded (\d+)/(\d+) KubeJS client scripts.*? with (\d+) errors", re.I)


def read(p):
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read().splitlines()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("game_dir", nargs="?", default="run", help="game directory (default: run)")
    ap.add_argument("--ignore", action="append", default=[], help="regex of lines to ignore (repeatable)")
    ap.add_argument("--no-require-kubejs", action="store_true", help="do not fail if KubeJS client.log is missing")
    ap.add_argument("--max-lines", type=int, default=15, help="max lines printed per category")
    a = ap.parse_args()
    ign = [re.compile(x) for x in a.ignore]
    g = a.game_dir
    findings, fails = {}, []

    latest = os.path.join(g, "logs", "latest.log")
    if not os.path.isfile(latest):
        fails.append("logs/latest.log missing: game never started")
    for p in (latest, os.path.join(g, "logs", "debug.log")):
        if not os.path.isfile(p):
            continue
        for i, line in enumerate(read(p), 1):
            if any(r.search(line) for r in ign):
                continue
            for cat, rx in RULES:
                if rx.search(line):
                    findings.setdefault(cat, []).append(f"{os.path.basename(p)}:{i}: {line.strip()[:300]}")
                    break

    kjs = [p for p in (os.path.join(g, "kubejs", "logs", "client.log"), os.path.join(g, "logs", "kubejs", "client.log")) if os.path.isfile(p)]
    if not kjs and not a.no_require_kubejs:
        fails.append("KubeJS client.log not found (kubejs/logs or logs/kubejs)")
    for p in kjs:
        lines = read(p)
        summ = [m for m in (KJS_SUMMARY.search(l) for l in lines) if m]
        if not summ:
            fails.append(f"{p}: no 'Loaded N/M KubeJS client scripts ... with K errors' line")
        elif int(summ[-1].group(3)) != 0:
            fails.append(f"{p}: {summ[-1].group(0)}")
        for i, l in enumerate(lines, 1):
            if re.search(r"\[ERROR\]|/ERROR\]", l) and not any(r.search(l) for r in ign):
                findings.setdefault("kubejs", []).append(f"client.log:{i}: {l.strip()[:300]}")

    for c in sorted(glob.glob(os.path.join(g, "crash-reports", "*.txt"))):
        fails.append(f"crash report: {c}")
        findings.setdefault("crash", []).extend(read(c)[:12])

    for cat, ls in findings.items():
        fails.append(f"{len(ls)} {cat} problem line(s)")
    print("=== client log check ===")
    for cat, ls in findings.items():
        print(f"\n[{cat}] {len(ls)} line(s)")
        for l in ls[: a.max_lines]:
            print("  " + l)
        if len(ls) > a.max_lines:
            print(f"  ... {len(ls) - a.max_lines} more")
    if fails:
        print("\nFAILED:")
        for f in fails:
            print("  - " + f)
            print(f"::error::{f}")
        return 1
    print("OK: no client content errors")
    return 0


if __name__ == "__main__":
    sys.exit(main())

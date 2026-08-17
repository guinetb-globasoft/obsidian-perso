#!/usr/bin/env python3
"""Overlaps mod-contre-mod + verification des dependances de masters."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "crossref.json"), encoding="utf-8"))
VANILLA = {"skyrim.esm", "update.esm", "dawnguard.esm",
           "hearthfires.esm", "dragonborn.esm"}
order = d["order_mtime"]
rank = {n: i for i, n in enumerate(order)}

print("### Dependances de masters — un master doit charger AVANT son dependant")
problems = 0
for name, info in d["counts"].items():
    for m in info["masters"]:
        if m.lower() in VANILLA:
            continue
        real = next((n for n in rank if n.lower() == m.lower()), None)
        if real is None:
            print(f"  !! {name} exige {m} — ABSENT / inactif")
            problems += 1
        elif rank[real] > rank[name]:
            print(f"  !! {name} (#{rank[name]}) charge AVANT son master "
                  f"{real} (#{rank[real]})")
            problems += 1
        else:
            print(f"  ok {name} (#{rank[name]}) apres {real} (#{rank[real]})")
if not problems:
    print("  (rien d'anormal)")

print()
print("### Paires de mods qui se disputent le meme record")
pairs = {}
for key, entries in d["index"].items():
    mods = sorted({e["plugin"] for e in entries
                   if e["plugin"].lower() not in VANILLA})
    if len(mods) < 2:
        continue
    for i in range(len(mods)):
        for j in range(i + 1, len(mods)):
            pk = (mods[i], mods[j])
            pairs.setdefault(pk, []).append((key, entries[0]["sig"]))

if not pairs:
    print("  (aucune)")
for (a, b), items in sorted(pairs.items(), key=lambda kv: -len(kv[1])):
    win = a if rank[a] > rank[b] else b
    lose = b if win == a else a
    print(f"\n  {a} (#{rank[a]})  vs  {b} (#{rank[b]})  — {len(items)} records")
    print(f"     gagnant : {win}   (perdant : {lose})")
    sigs = {}
    for _, s in items:
        sigs[s] = sigs.get(s, 0) + 1
    print(f"     types   : {sigs}")

print()
print("### Mods touchant ALCH/INGR/COBJ sans conflit (surcharges solo)")
for name, info in d["counts"].items():
    if name.lower() in VANILLA:
        continue
    touched = {s: c for s, c in info["counts"].items()
               if s in ("ALCH", "INGR", "COBJ")}
    if touched:
        ovr = {s: info["overrides"].get(s, 0) for s in touched}
        print(f"  #{rank[name]:<3d} {name:42s} total={touched} surcharges={ovr}")

#!/usr/bin/env python3
"""Rapporte les conflits ALCH/INGR/COBJ et qui gagne selon l'ordre de chargement."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(HERE, "crossref.json"), encoding="utf-8"))

VANILLA = {"skyrim.esm", "update.esm", "dawnguard.esm",
           "hearthfires.esm", "dragonborn.esm"}

index = data["index"]
order_mtime = data["order_mtime"]
order_txt = data["order_txt"]

print("=" * 78)
print("ORDRE DE CHARGEMENT REEL (date de fichier — regle Skyrim LE)")
print("=" * 78)
for i, n in enumerate(order_mtime):
    mark = "" if n.lower() in VANILLA else "  "
    print(f"{i:3d}  {mark}{n}")

print()
print("Ecarts avec l'ordre du fichier plugins.txt :")
diffs = 0
for n in order_mtime:
    a, b = order_mtime.index(n), order_txt.index(n)
    if a != b:
        print(f"   {n:42s} disque #{a:2d}   plugins.txt #{b:2d}")
        diffs += 1
if not diffs:
    print("   (aucun)")

print()
print("Plugins presents sur le disque mais INACTIFS (ne chargent pas) :")
for n in data["inactive"]:
    print(f"   {n}")

# ---------------------------------------------------------------- conflits
print()
print("=" * 78)
print("CONFLITS — records ALCH/INGR/COBJ touches par plus d'un plugin")
print("=" * 78)

conflicts = []
for key, entries in index.items():
    plugins = {e["plugin"] for e in entries}
    mods = {p for p in plugins if p.lower() not in VANILLA}
    if len(plugins) < 2 or not mods:
        continue
    conflicts.append((key, entries))


def label(entries):
    for e in entries:
        if e["name"] and e["name"] != "<localise>":
            return e["name"]
    for e in entries:
        if e["edid"]:
            return e["edid"]
    return "?"


def sig_of(entries):
    return entries[0]["sig"]


by_sig = {}
for key, entries in conflicts:
    by_sig.setdefault(sig_of(entries), []).append((key, entries))

summary = {}
for sig in ("ALCH", "INGR", "COBJ"):
    items = by_sig.get(sig, [])
    if not items:
        continue
    print()
    print("-" * 78)
    print(f"### {sig}  —  {len(items)} records en conflit")
    print("-" * 78)
    for key, entries in sorted(items, key=lambda kv: label(kv[1]).lower()):
        ordered = sorted(entries, key=lambda e: e["rank_mtime"])
        winner = ordered[-1]
        w_txt = sorted(entries, key=lambda e: e["rank_txt"])[-1]
        kind = winner["kind"]
        print(f"\n  {label(entries)}   [{key}]  ({kind})")
        for e in ordered:
            flag = ">>" if e is winner else "  "
            bits = []
            if e["value"] is not None:
                bits.append(f"valeur={e['value']}")
            if e["weight"] is not None:
                bits.append(f"poids={e['weight']:g}")
            if e["effects"]:
                bits.append(f"{e['effects']} effets")
            if e["components"]:
                bits.append(f"{e['components']} composants")
            print(f"   {flag} #{e['rank_mtime']:<3d} {e['plugin']:42s} "
                  f"{'  '.join(bits)}")
        if w_txt["plugin"] != winner["plugin"]:
            print(f"      !! selon plugins.txt le gagnant serait "
                  f"{w_txt['plugin']} — divergence")
        summary.setdefault(winner["plugin"], {}).setdefault(sig, 0)
        summary[winner["plugin"]][sig] += 1

print()
print("=" * 78)
print("QUI GAGNE — nombre de records remportes par plugin")
print("=" * 78)
for plug in sorted(summary, key=lambda p: -sum(summary[p].values())):
    tot = sum(summary[plug].values())
    detail = "  ".join(f"{s}={c}" for s, c in sorted(summary[plug].items()))
    print(f"  {plug:42s} {tot:4d}   ({detail})")

print()
print(f"Total records en conflit : {len(conflicts)}")

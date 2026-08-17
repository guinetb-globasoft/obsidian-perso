import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "cuisine.json"), encoding="utf-8"))
r = d["recettes"]

by_station = {}
for x in r:
    by_station.setdefault(x["station"], []).append(x)

for st, items in sorted(by_station.items(), key=lambda kv: -len(kv[1])):
    print(f"\n{'=' * 74}\n{st}  —  {len(items)} recettes\n{'=' * 74}")
    for x in sorted(items, key=lambda y: (y["plugin"], y["produit"])):
        ing = ", ".join(f"{n}x {lab}" if n > 1 else lab
                        for lab, n in x["ingredients"]) or "(aucun)"
        cnt = f" x{x['count']}" if x["count"] > 1 else ""
        print(f"  {x['produit']}{cnt}")
        print(f"      <- {ing}")
        print(f"      [{x['plugin']} | {x['edid']}]")

print(f"\n\nTotal : {len(r)} recettes de cuisine")
print("Par plugin :")
byp = {}
for x in r:
    byp[x["plugin"]] = byp.get(x["plugin"], 0) + 1
for p, c in sorted(byp.items(), key=lambda kv: -kv[1]):
    print(f"  {p:30s} {c}")

#!/usr/bin/env python3
"""Compare finement vanilla / lightingredients / de rerum dirennis sur les INGR."""
import os
import sys

sys.path.insert(0, r"C:\Users\Shadow\Downloads")
import skyrim_plugin_scan as sps

DATA = r"C:\Program Files (x86)\Steam\steamapps\common\Skyrim\Data"
TARGETS = ["Skyrim.esm", "lightingredients.esp", "de rerum dirennis.esp"]


def collect(name):
    res = sps.scan_plugin(os.path.join(DATA, name), {"INGR"})
    masters = res["meta"]["masters"]
    out = {}
    for i in res["details"]:
        hi = i["formid"] >> 24
        origin = masters[hi] if hi < len(masters) else name
        out[f"{origin.lower()}:{i['formid'] & 0xFFFFFF:06X}"] = i
    return out


van, light, drd = (collect(n) for n in TARGETS)

shared = sorted(set(light) & set(drd))
print(f"INGR communs lightingredients / de rerum dirennis : {len(shared)}\n")

same_weight = same_value = same_eff = 0
drd_eff_differs_from_vanilla = 0
examples = []

for k in shared:
    l, d = light[k], drd[k]
    v = van.get(k)
    if l["weight"] == d["weight"]:
        same_weight += 1
    if l["value"] == d["value"]:
        same_value += 1
    le = [(e["mgef"], round(e["magnitude"], 3), e["duration"]) for e in l["effects"]]
    de = [(e["mgef"], round(e["magnitude"], 3), e["duration"]) for e in d["effects"]]
    if le == de:
        same_eff += 1
    if v:
        ve = [(e["mgef"], round(e["magnitude"], 3), e["duration"]) for e in v["effects"]]
        if de != ve:
            drd_eff_differs_from_vanilla += 1
            if len(examples) < 4:
                examples.append((d["edid"] or d["name"], ve, de, le))

n = len(shared)
print(f"  poids identiques (light vs drd)   : {same_weight}/{n}")
print(f"  valeurs identiques (light vs drd) : {same_value}/{n}")
print(f"  effets identiques (light vs drd)  : {same_eff}/{n}")
print(f"  effets DRD differents du vanilla  : {drd_eff_differs_from_vanilla}/{n}")

print("\n  Exemples (mgef, magnitude, duree) :")
for edid, ve, de, le in examples:
    print(f"\n   {edid}")
    print(f"     vanilla : {[(f'{m:08X}', mg, du) for m, mg, du in ve]}")
    print(f"     drd     : {[(f'{m:08X}', mg, du) for m, mg, du in de]}")
    print(f"     light   : {[(f'{m:08X}', mg, du) for m, mg, du in le]}")

# poids : que valent-ils reellement ?
wl = {l["weight"] for l in light.values()}
wd = {drd[k]["weight"] for k in shared}
print(f"\n  poids distincts dans lightingredients : {sorted(wl)}")
print(f"  poids distincts dans drd (sur communs) : {sorted(wd)}")

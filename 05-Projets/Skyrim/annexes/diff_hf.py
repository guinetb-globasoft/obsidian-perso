#!/usr/bin/env python3
"""HearthFires surcharge des plats vanilla : change-t-il leurs effets ?"""
import os
import struct
import sys

sys.path.insert(0, r"C:\Users\Shadow\Downloads")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import skyrim_plugin_scan as sps
from cuisine import load_strings_for, walk, DATA


def grab(plugin):
    table = load_strings_for(plugin)
    out = {}
    for sig, formid, body, meta in walk(os.path.join(DATA, plugin), {"ALCH"}):
        masters = meta["masters"]
        hi = formid >> 24
        origin = masters[hi] if hi < len(masters) else plugin
        cid = f"{origin.lower()}:{formid & 0xFFFFFF:06X}"
        edid = full = None
        value = weight = None
        effects = []
        pending = None
        for ssig, blob in sps.iter_subrecords(body):
            if ssig == "EDID":
                edid = sps.zstring(blob)
            elif ssig == "FULL" and len(blob) >= 4:
                (sid,) = struct.unpack_from("<I", blob, 0)
                full = table.get(sid)
            elif ssig == "DATA" and len(blob) >= 4:
                (weight,) = struct.unpack_from("<f", blob, 0)
            elif ssig == "ENIT" and len(blob) >= 8:
                value, _f = struct.unpack_from("<Ii", blob, 0)
            elif ssig == "EFID" and len(blob) >= 4:
                (pending,) = struct.unpack_from("<I", blob, 0)
            elif ssig == "EFIT" and len(blob) >= 12:
                mag, _a, dur = struct.unpack_from("<fII", blob, 0)
                effects.append((pending & 0xFFFFFF, round(mag, 3), dur))
                pending = None
        out[cid] = {"edid": edid, "name": full, "value": value,
                    "weight": weight, "effects": effects}
    return out


sky = grab("Skyrim.esm")
hf = grab("HearthFires.esm")

shared = sorted(set(sky) & set(hf))
print(f"Plats vanilla surcharges par HearthFires : {len(shared)}\n")

changed = []
for cid in shared:
    a, b = sky[cid], hf[cid]
    diffs = []
    if a["effects"] != b["effects"]:
        diffs.append(f"effets {a['effects']} -> {b['effects']}")
    if a["value"] != b["value"]:
        diffs.append(f"valeur {a['value']} -> {b['value']}")
    if a["weight"] != b["weight"]:
        diffs.append(f"poids {a['weight']} -> {b['weight']}")
    if diffs:
        changed.append((b["name"] or b["edid"], diffs))

if not changed:
    print("  Aucun changement : HearthFires recopie les valeurs vanilla a l'identique.")
else:
    print(f"  {len(changed)} plats reellement modifies :")
    for name, diffs in changed:
        print(f"   {name}")
        for d in diffs:
            print(f"      {d}")

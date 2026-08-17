#!/usr/bin/env python3
"""Pour chaque recette de cuisine, ce que le plat apporte reellement.

Joint COBJ (recette) -> ALCH (plat produit) -> MGEF (effet magique),
en resolvant les noms via les tables .STRINGS propres a chaque plugin
et en tranchant les surcharges selon l'ordre de chargement.
"""
import json
import os
import struct
import sys

sys.path.insert(0, r"C:\Users\Shadow\Downloads")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import skyrim_plugin_scan as sps
from cuisine import load_strings_for, walk, DATA, PLUGINS_TXT, VANILLA_ORDER, IMPLICIT

HERE = os.path.dirname(os.path.abspath(__file__))
WANT = {"KYWD", "COBJ", "ALCH", "MGEF"}

ENIT_FOOD = 0x00000002
ENIT_MEDICINE = 0x00010000
ENIT_POISON = 0x00020000


def active_order():
    listed = []
    with open(PLUGINS_TXT, encoding="cp1252") as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#"):
                listed.append(line.lstrip("*").strip())
    on_disk = {f.lower(): f for f in os.listdir(DATA)}
    out = []
    for e in IMPLICIT + listed:
        real = on_disk.get(e.lower())
        if real and real not in out:
            out.append(real)

    def key(n):
        low = n.lower()
        if low in VANILLA_ORDER:
            return (0, VANILLA_ORDER.index(low), 0.0)
        is_esm = open(os.path.join(DATA, n), "rb").read(9)[8] & 0x01
        return (0 if is_esm else 1, 99, os.path.getmtime(os.path.join(DATA, n)))

    out.sort(key=key)
    return out


def main():
    active = active_order()
    tables = {p: load_strings_for(p) for p in active}

    names, edids, keywords = {}, {}, {}
    alch, mgef, cobj = {}, {}, {}

    def canon(formid, masters, plugin):
        hi = formid >> 24
        origin = masters[hi] if hi < len(masters) else plugin
        return f"{origin.lower()}:{formid & 0xFFFFFF:06X}"

    for plugin in active:
        table = tables[plugin]
        for sig, formid, body, meta in walk(os.path.join(DATA, plugin), WANT):
            masters = meta["masters"]
            cid = canon(formid, masters, plugin)
            edid = full = None
            value = weight = flags = None
            bench = result = rcount = None
            comps, effects = [], []
            pending = None
            for ssig, blob in sps.iter_subrecords(body):
                if ssig == "EDID":
                    edid = sps.zstring(blob)
                elif ssig == "FULL":
                    if meta["localized"] and len(blob) >= 4:
                        (sid,) = struct.unpack_from("<I", blob, 0)
                        full = table.get(sid)
                    else:
                        full = sps.zstring(blob)
                elif ssig == "EFID" and len(blob) >= 4:
                    (pending,) = struct.unpack_from("<I", blob, 0)
                elif ssig == "EFIT" and len(blob) >= 12:
                    mag, area, dur = struct.unpack_from("<fII", blob, 0)
                    effects.append({"mgef": canon(pending, masters, plugin),
                                    "mag": mag, "dur": dur})
                    pending = None
                elif sig == "ALCH":
                    if ssig == "DATA" and len(blob) >= 4:
                        (weight,) = struct.unpack_from("<f", blob, 0)
                    elif ssig == "ENIT" and len(blob) >= 8:
                        value, flags = struct.unpack_from("<Ii", blob, 0)
                elif sig == "COBJ":
                    if ssig == "BNAM" and len(blob) >= 4:
                        (bench,) = struct.unpack_from("<I", blob, 0)
                    elif ssig == "CNAM" and len(blob) >= 4:
                        (result,) = struct.unpack_from("<I", blob, 0)
                    elif ssig == "NAM1" and len(blob) >= 2:
                        (rcount,) = struct.unpack_from("<H", blob, 0)
                    elif ssig == "CNTO" and len(blob) >= 8:
                        item, cnt = struct.unpack_from("<II", blob, 0)
                        comps.append((canon(item, masters, plugin), cnt))
            if edid:
                edids[cid] = edid
            if full:
                names[cid] = full
            if sig == "KYWD" and edid:
                keywords[edid] = cid
            elif sig == "MGEF":
                mgef[cid] = {"edid": edid, "name": full, "plugin": plugin}
            elif sig == "ALCH":
                # surcharge : le dernier charge ecrase
                alch[cid] = {"edid": edid, "name": full, "value": value,
                             "weight": weight, "flags": flags,
                             "effects": effects, "plugin": plugin}
            elif sig == "COBJ" and bench is not None:
                cobj[cid] = {"edid": edid, "bench": canon(bench, masters, plugin),
                             "result": canon(result, masters, plugin) if result else None,
                             "count": rcount or 1, "components": comps,
                             "plugin": plugin}
        print(f"  lu : {plugin}", file=sys.stderr)

    cook_kw = {v: k for k, v in keywords.items()
               if any(t in k.lower() for t in ("cookpot", "oven"))
               and "building" not in k.lower()}

    def label(cid):
        return names.get(cid) or edids.get(cid) or cid

    rows = []
    for cid, r in cobj.items():
        if r["bench"] not in cook_kw:
            continue
        dish = alch.get(r["result"])
        eff = []
        if dish:
            for e in dish["effects"]:
                m = mgef.get(e["mgef"], {})
                eff.append({
                    "effet": m.get("name") or m.get("edid") or e["mgef"],
                    "edid": m.get("edid", ""),
                    "mag": e["mag"],
                    "dur": e["dur"],
                })
        kind = "?"
        if dish and dish["flags"] is not None:
            f = dish["flags"]
            kind = ("nourriture" if f & ENIT_FOOD else
                    "poison" if f & ENIT_POISON else
                    "medicament" if f & ENIT_MEDICINE else "potion")
        rows.append({
            "station": cook_kw[r["bench"]],
            "plat": label(r["result"]) if r["result"] else "?",
            "edid_recette": r["edid"],
            "count": r["count"],
            "source": r["plugin"],
            "source_plat": dish["plugin"] if dish else None,
            "type": kind,
            "valeur": dish["value"] if dish else None,
            "poids": dish["weight"] if dish else None,
            "effets": eff,
            "ingredients": [[label(c), n] for c, n in r["components"]],
        })

    rows.sort(key=lambda x: (x["station"], x["plat"]))
    with open(os.path.join(HERE, "bonus.json"), "w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=1, ensure_ascii=False)

    for st in sorted({r["station"] for r in rows}):
        print(f"\n{'=' * 76}\n{st}\n{'=' * 76}")
        for r in [x for x in rows if x["station"] == st]:
            cnt = f" x{r['count']}" if r["count"] > 1 else ""
            print(f"\n  {r['plat']}{cnt}   [{r['type']}] "
                  f"valeur={r['valeur']} poids={r['poids']:g}"
                  if r["poids"] is not None else f"\n  {r['plat']}{cnt}")
            if not r["effets"]:
                print("      (aucun effet)")
            for e in r["effets"]:
                d = f" pendant {e['dur']}s" if e["dur"] else ""
                print(f"      {e['effet']}  {e['mag']:g}{d}   <{e['edid']}>")
    print(f"\n\n{len(rows)} plats")


if __name__ == "__main__":
    main()

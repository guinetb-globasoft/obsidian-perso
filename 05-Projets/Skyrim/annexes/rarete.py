#!/usr/bin/env python3
"""Rarete reelle des ingredients de cuisine.

Mesure, sur tout l'ordre de chargement actif :
  - REFR : nombre d'exemplaires poses dans le monde
  - FLOR/TREE : plantes recoltables qui produisent l'ingredient (+ leurs REFR)
  - CONT : nombre de types de conteneurs qui en contiennent
  - LVLI : nombre de listes de butin qui peuvent en faire apparaitre
"""
import json
import os
import struct
import sys

sys.path.insert(0, r"C:\Users\Shadow\Downloads")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import skyrim_plugin_scan as sps
from cuisine import load_strings_for, DATA, PLUGINS_TXT, VANILLA_ORDER, IMPLICIT

HERE = os.path.dirname(os.path.abspath(__file__))
WANT = {"REFR", "FLOR", "TREE", "CONT", "LVLI", "ALCH", "INGR", "MISC", "COBJ",
        "KYWD"}


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

    names, edids = {}, {}
    refr_count = {}     # cid objet de base -> nb de placements
    produce = {}        # cid FLOR/TREE -> cid ingredient produit
    cont_count = {}     # cid -> nb de types de conteneurs
    lvli_count = {}     # cid -> nb de listes de butin
    keywords = {}
    recipes = []

    for plugin in active:
        table = tables[plugin]
        path = os.path.join(DATA, plugin)
        with open(path, "rb") as fh:
            meta = sps.parse_tes4(fh)
            masters = meta["masters"]
            localized = meta["localized"]

            def canon(formid):
                hi = formid >> 24
                origin = masters[hi] if hi < len(masters) else plugin
                return f"{origin.lower()}:{formid & 0xFFFFFF:06X}"

            while True:
                head = fh.read(sps.REC_HEADER)
                if len(head) < sps.REC_HEADER:
                    break
                sig = head[0:4].decode("ascii", "replace")
                if sig == "GRUP":
                    continue
                size, flags, formid = struct.unpack_from("<III", head, 4)
                body = sps.read_record_body(fh, size, flags)
                if sig not in WANT:
                    continue
                cid = canon(formid)

                if sig == "REFR":
                    for ssig, blob in sps.iter_subrecords(body):
                        if ssig == "NAME" and len(blob) >= 4:
                            (base,) = struct.unpack_from("<I", blob, 0)
                            b = canon(base)
                            refr_count[b] = refr_count.get(b, 0) + 1
                            break
                    continue

                edid = full = None
                bench = result = None
                comps = []
                for ssig, blob in sps.iter_subrecords(body):
                    if ssig == "EDID":
                        edid = sps.zstring(blob)
                    elif ssig == "FULL":
                        if localized and len(blob) >= 4:
                            (sid,) = struct.unpack_from("<I", blob, 0)
                            full = table.get(sid)
                        else:
                            full = sps.zstring(blob)
                    elif sig in ("FLOR", "TREE") and ssig == "PFIG" \
                            and len(blob) >= 4:
                        (ing,) = struct.unpack_from("<I", blob, 0)
                        produce[cid] = canon(ing)
                    elif sig == "CONT" and ssig == "CNTO" and len(blob) >= 8:
                        item, _cnt = struct.unpack_from("<II", blob, 0)
                        k = canon(item)
                        cont_count[k] = cont_count.get(k, 0) + 1
                    elif sig == "LVLI" and ssig == "LVLO" and len(blob) >= 12:
                        _lvl, _u, item, _c, _u2 = struct.unpack_from(
                            "<HHIHH", blob, 0)
                        k = canon(item)
                        lvli_count[k] = lvli_count.get(k, 0) + 1
                    elif sig == "COBJ":
                        if ssig == "BNAM" and len(blob) >= 4:
                            (bench,) = struct.unpack_from("<I", blob, 0)
                        elif ssig == "CNAM" and len(blob) >= 4:
                            (result,) = struct.unpack_from("<I", blob, 0)
                        elif ssig == "CNTO" and len(blob) >= 8:
                            item, cnt = struct.unpack_from("<II", blob, 0)
                            comps.append((canon(item), cnt))
                if edid:
                    edids[cid] = edid
                if full:
                    names[cid] = full
                if sig == "KYWD" and edid:
                    keywords[edid] = cid
                if sig == "COBJ" and bench is not None:
                    recipes.append({"cid": cid, "bench": canon(bench),
                                    "result": canon(result) if result else None,
                                    "components": comps})
        print(f"  lu : {plugin}", file=sys.stderr)

    cook_kw = {v for k, v in keywords.items()
               if any(t in k.lower() for t in ("cookpot", "oven"))
               and "building" not in k.lower()}
    cooking = {r["cid"]: r for r in recipes if r["bench"] in cook_kw}

    # ingredients utilises + nb de recettes qui les demandent
    used = {}
    for r in cooking.values():
        for c, n in r["components"]:
            used.setdefault(c, {"recettes": 0, "qte_max": 0})
            used[c]["recettes"] += 1
            used[c]["qte_max"] = max(used[c]["qte_max"], n)

    # plantes recoltables : REFR de la plante -> ingredient produit
    harvest = {}
    for flor_cid, ing_cid in produce.items():
        if ing_cid in used:
            harvest[ing_cid] = harvest.get(ing_cid, 0) + refr_count.get(flor_cid, 0)

    rows = []
    for cid, info in used.items():
        direct = refr_count.get(cid, 0)
        plants = harvest.get(cid, 0)
        rows.append({
            "cid": cid,
            "nom": names.get(cid) or edids.get(cid) or cid,
            "edid": edids.get(cid, ""),
            "poses": direct,
            "plantes": plants,
            "total": direct + plants,
            "conteneurs": cont_count.get(cid, 0),
            "listes_butin": lvli_count.get(cid, 0),
            "recettes": info["recettes"],
            "qte_max": info["qte_max"],
        })
    rows.sort(key=lambda r: (r["total"], r["listes_butin"]))

    with open(os.path.join(HERE, "rarete.json"), "w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=1, ensure_ascii=False)

    print(f"\n{'ingredient':26s}{'posés':>7}{'plantes':>9}{'TOTAL':>8}"
          f"{'conten.':>9}{'butin':>7}{'recettes':>10}")
    print("-" * 76)
    for r in rows:
        print(f"{r['nom'][:25]:26s}{r['poses']:>7}{r['plantes']:>9}"
              f"{r['total']:>8}{r['conteneurs']:>9}{r['listes_butin']:>7}"
              f"{r['recettes']:>10}")
    print(f"\n{len(rows)} ingredients distincts dans les recettes de cuisine")


if __name__ == "__main__":
    main()

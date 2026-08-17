#!/usr/bin/env python3
"""D'ou viennent concretement les ingredients rares ?

Trace, pour chaque ingredient cible : listes de butin (y compris imbriquees),
conteneurs, plantes recoltables, et PNJ qui le laissent en depouille.
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
WANT = {"LVLI", "CONT", "NPC_", "FLOR", "TREE", "ALCH", "INGR", "MISC"}

CIBLES = ["Mudcrab Legs", "Butter", "Jug of Milk", "Sack of Flour",
          "Chicken Breast", "Mammoth Snout", "Moon Sugar", "Horse Meat",
          "Leg of Goat", "Eidar Cheese Wheel", "Raw Beef", "Horker Meat",
          "Chicken's Egg", "Ale", "Venison"]


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
    lvli = {}       # cid -> [item cids]
    cont = {}       # cid -> [item cids]
    npc_death = {}  # lvli cid -> [noms de PNJ]
    produce = {}    # flor cid -> ingredient cid

    for plugin in active:
        table = tables[plugin]
        with open(os.path.join(DATA, plugin), "rb") as fh:
            meta = sps.parse_tes4(fh)
            masters, localized = meta["masters"], meta["localized"]

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
                edid = full = death = None
                items = []
                for ssig, blob in sps.iter_subrecords(body):
                    if ssig == "EDID":
                        edid = sps.zstring(blob)
                    elif ssig == "FULL":
                        if localized and len(blob) >= 4:
                            (sid,) = struct.unpack_from("<I", blob, 0)
                            full = table.get(sid)
                        else:
                            full = sps.zstring(blob)
                    elif sig == "LVLI" and ssig == "LVLO" and len(blob) >= 12:
                        _l, _u, item, _c, _u2 = struct.unpack_from("<HHIHH", blob, 0)
                        items.append(canon(item))
                    elif sig == "CONT" and ssig == "CNTO" and len(blob) >= 8:
                        item, _c = struct.unpack_from("<II", blob, 0)
                        items.append(canon(item))
                    elif sig == "NPC_" and ssig == "INAM" and len(blob) >= 4:
                        (d,) = struct.unpack_from("<I", blob, 0)
                        death = canon(d)
                    elif sig in ("FLOR", "TREE") and ssig == "PFIG" and len(blob) >= 4:
                        (ing,) = struct.unpack_from("<I", blob, 0)
                        produce[cid] = canon(ing)
                if edid:
                    edids[cid] = edid
                if full:
                    names[cid] = full
                if sig == "LVLI":
                    lvli[cid] = items
                elif sig == "CONT":
                    cont[cid] = items
                elif sig == "NPC_" and death:
                    npc_death.setdefault(death, []).append(full or edid or cid)
        print(f"  lu : {plugin}", file=sys.stderr)

    def label(cid):
        return names.get(cid) or edids.get(cid) or cid

    by_name = {}
    for cid in list(names) + list(edids):
        by_name.setdefault(label(cid), cid)

    # index inverse : item -> listes qui le contiennent (transitif)
    parents = {}
    for lid, items in lvli.items():
        for it in items:
            parents.setdefault(it, set()).add(lid)

    def all_lists(target, seen=None):
        """Remonte la chaine des listes imbriquees."""
        if seen is None:
            seen = set()
        out = set()
        for p in parents.get(target, ()):
            if p in seen:
                continue
            seen.add(p)
            out.add(p)
            out |= all_lists(p, seen)
        return out

    report = {}
    for nom in CIBLES:
        cid = by_name.get(nom)
        if not cid:
            print(f"!! introuvable : {nom}", file=sys.stderr)
            continue
        lists = all_lists(cid)
        conts = [label(c) for c, items in cont.items() if cid in items]
        plants = [label(f) for f, ing in produce.items() if ing == cid]
        npcs = set()
        for lid in lists:
            for n in npc_death.get(lid, ()):
                npcs.add(n)
        report[nom] = {
            "listes": sorted(edids.get(x, x) for x in lists),
            "conteneurs": sorted(set(conts)),
            "plantes": sorted(set(plants)),
            "depouilles": sorted(npcs),
        }
        print(f"\n{'=' * 72}\n{nom}\n{'=' * 72}")
        print(f"  plantes/récoltables : {', '.join(sorted(set(plants))) or '—'}")
        print(f"  dépouilles de PNJ   : {', '.join(sorted(npcs)) or '—'}")
        print(f"  conteneurs types    : {', '.join(sorted(set(conts))[:8]) or '—'}")
        ll = sorted(edids.get(x, x) for x in lists)
        print(f"  listes de butin ({len(ll)}) : {', '.join(ll[:12]) or '—'}")

    with open(os.path.join(HERE, "sources.json"), "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()

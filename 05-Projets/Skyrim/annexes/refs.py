#!/usr/bin/env python3
"""Recherche exhaustive : quels records citent un FormID donne ?

Balaye TOUS les records de TOUS les plugins actifs et signale ceux dont le
corps contient le FormID cible. Evite de conclure a tort qu'un objet n'a
aucune source parce qu'on n'a regarde que LVLI/CONT.
"""
import os
import struct
import sys
from collections import Counter

sys.path.insert(0, r"C:\Users\Shadow\Downloads")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import skyrim_plugin_scan as sps
from cuisine import load_strings_for, DATA, PLUGINS_TXT, VANILLA_ORDER, IMPLICIT

CIBLES = {          # nom -> (plugin d'origine, id local) — releves sur rarete.json
    "Butter":             ("HearthFires.esm", 0x00353C),
    "Jug of Milk":        ("HearthFires.esm", 0x003534),
    "Sack of Flour":      ("HearthFires.esm", 0x003538),
    "Mudcrab Legs":       ("HearthFires.esm", 0x003540),
    "Eidar Cheese Wheel": ("Skyrim.esm",      0x064B34),
    "Mammoth Snout":      ("Skyrim.esm",      0x0669A4),
}


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
    # resout le vrai FormID a chercher, en cherchant l'EDID attendu
    active = active_order()
    hits = {n: [] for n in CIBLES}
    counts = {n: Counter() for n in CIBLES}

    for plugin in active:
        with open(os.path.join(DATA, plugin), "rb") as fh:
            meta = sps.parse_tes4(fh)
            masters = meta["masters"]
            # FormID local tel qu'il apparait DANS ce plugin
            targets = {}
            for nom, (origin, local) in CIBLES.items():
                idx = None
                if origin.lower() == plugin.lower():
                    idx = len(masters)
                else:
                    for i, m in enumerate(masters):
                        if m.lower() == origin.lower():
                            idx = i
                            break
                if idx is not None:
                    targets[struct.pack("<I", (idx << 24) | local)] = nom
            if not targets:
                continue

            while True:
                head = fh.read(sps.REC_HEADER)
                if len(head) < sps.REC_HEADER:
                    break
                sig = head[0:4].decode("ascii", "replace")
                if sig == "GRUP":
                    continue
                size, flags, formid = struct.unpack_from("<III", head, 4)
                body = sps.read_record_body(fh, size, flags)
                for pat, nom in targets.items():
                    if pat in body:
                        edid = None
                        for ssig, blob in sps.iter_subrecords(body):
                            if ssig == "EDID":
                                edid = sps.zstring(blob)
                                break
                        counts[nom][sig] += 1
                        if len(hits[nom]) < 4000:
                            hits[nom].append((plugin, sig, edid or f"{formid:08X}"))
        print(f"  lu : {plugin}", file=sys.stderr)

    for nom in CIBLES:
        print(f"\n{'=' * 72}\n{nom}\n{'=' * 72}")
        print(f"  par type de record : {dict(counts[nom])}")
        interesting = [h for h in hits[nom] if h[1] not in ("REFR",)]
        print(f"  records non-REFR qui le citent ({len(interesting)}) :")
        for plugin, sig, edid in interesting[:40]:
            print(f"     {sig}  {edid}   [{plugin}]")


if __name__ == "__main__":
    main()

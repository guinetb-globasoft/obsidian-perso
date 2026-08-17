#!/usr/bin/env python3
"""MGEF de magie : archetype corrige + description DNAM (source de verite).

L'enumeration d'archetypes precedente omettait Darkness (13) et NightEye (14),
ce qui decalait tout de 2 a partir de Lock. La description DNAM, ecrite pour
le joueur, permet de valider l'interpretation sans dependre de l'enum.
"""
import os
import struct
import sys

sys.path.insert(0, r"C:\Users\Shadow\Downloads")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bsa
import skyrim_plugin_scan as sps
from cuisine import walk, DATA, STRINGS

ARCH = [
    "Value Modifier", "Script", "Dispel", "Cure Disease", "Absorb",
    "Dual Value Modifier", "Calm", "Demoralize", "Frenzy", "Disarm",
    "Command Summoned", "Invisibility", "Light", "Darkness", "Night Eye",
    "Lock", "Open", "Bound Weapon", "Summon Creature", "Detect Life",
    "Telekinesis", "Paralysis", "Reanimate", "Soul Trap", "Turn Undead",
    "Guide", "Werewolf Feed", "Cure Paralysis", "Cure Addiction",
    "Cure Poison", "Concussion", "Value and Parts", "Accumulate Magnitude",
    "Stagger", "Peak Value Modifier", "Cloak", "Werewolf", "Slow Time",
    "Rally", "Enhance Weapon", "Spawn Hazard", "Etherealize", "Banish",
    "Spawn Scripted Ref", "Disguise", "Grab Actor", "Vampire Lord",
]

AV = {24: "Health", 25: "Magicka", 26: "Stamina",
      27: "HealRate", 28: "MagickaRate", 29: "StaminaRate",
      155: "AV-155", 156: "AV-156"}


def parse_dlstrings(blob):
    """DLSTRINGS/ILSTRINGS : chaque entree est prefixee de sa longueur."""
    count, _size = struct.unpack_from("<II", blob, 0)
    end = 8 + count * 8
    out = {}
    for i in range(count):
        sid, off = struct.unpack_from("<II", blob, 8 + i * 8)
        start = end + off
        (ln,) = struct.unpack_from("<I", blob, start)
        out[sid] = blob[start + 4:start + 4 + ln].rstrip(b"\x00") \
            .decode("cp1252", "replace")
    return out


def main():
    path = os.path.join(STRINGS, "Skyrim_English.DLSTRINGS")
    with open(path, "rb") as fh:
        dl = parse_dlstrings(fh.read())
    with open(os.path.join(STRINGS, "Skyrim_English.STRINGS"), "rb") as fh:
        blob = fh.read()
    count, _ = struct.unpack_from("<II", blob, 0)
    dend = 8 + count * 8
    st = {}
    for i in range(count):
        sid, off = struct.unpack_from("<II", blob, 8 + i * 8)
        s = dend + off
        st[sid] = blob[s:blob.find(b"\x00", s)].decode("cp1252", "replace")

    rows = []
    for sig, fid, body, meta in walk(os.path.join(DATA, "Skyrim.esm"), {"MGEF"}):
        edid = name = desc = None
        arch = pav = None
        for ss, b in sps.iter_subrecords(body):
            if ss == "EDID":
                edid = sps.zstring(b)
            elif ss == "FULL" and len(b) >= 4:
                (sid,) = struct.unpack_from("<I", b, 0)
                name = st.get(sid)
            elif ss == "DNAM" and len(b) >= 4:
                (sid,) = struct.unpack_from("<I", b, 0)
                desc = dl.get(sid)
            elif ss == "DATA" and len(b) >= 92:
                (arch,) = struct.unpack_from("<I", b, 64)
                (pav,) = struct.unpack_from("<i", b, 68)
        rows.append((fid & 0xFFFFFF, edid, name, desc, arch, pav))

    print("=== Effets candidats : regeneration de magie ===\n")
    for fid, edid, name, desc, arch, pav in rows:
        if not edid:
            continue
        if edid in ("FoodRestoreMagickaDuration", "FoodRestoreHealthDuration",
                    "FoodRestoreStaminaDuration", "FoodFortifyMagickaRate",
                    "FoodFortifyMagicka", "AlchRestoreMagicka",
                    "AbFortifyMagickaRate"):
            a = ARCH[arch] if arch is not None and arch < len(ARCH) else arch
            print(f"  {edid}")
            print(f"     FormID    : {fid:08X}")
            print(f"     nom       : {name}")
            print(f"     archétype : {a}   AV={AV.get(pav, pav)}")
            print(f"     descr.    : {desc}\n")

    print("\n=== Tous les MGEF 'Restore/Regenerate' sur Magicka ===")
    for fid, edid, name, desc, arch, pav in sorted(rows, key=lambda r: r[1] or ""):
        if pav not in (25, 28) or not edid:
            continue
        a = ARCH[arch] if arch is not None and arch < len(ARCH) else arch
        if a not in ("Value Modifier", "Peak Value Modifier"):
            continue
        if not desc or ("estore" not in desc and "egenerat" not in desc):
            continue
        print(f"  {fid:08X}  {edid:34s}{a:22s}{AV.get(pav, pav):12s}{desc}")


if __name__ == "__main__":
    main()

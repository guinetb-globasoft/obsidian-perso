#!/usr/bin/env python3
"""MGEF de Skyrim.esm touchant la magie : archetype, valeur d'acteur, usage.

Le sous-record DATA d'un MGEF fait ~152 octets ; l'archetype est a l'offset
64 et la valeur d'acteur primaire a l'offset 68.
"""
import os
import struct
import sys

sys.path.insert(0, r"C:\Users\Shadow\Downloads")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import skyrim_plugin_scan as sps
from cuisine import load_strings_for, walk, DATA

ARCHETYPES = {
    0: "Value Modifier", 1: "Script", 2: "Dispel", 3: "Cure Disease",
    4: "Absorb", 5: "Dual Value Modifier", 6: "Calm", 7: "Demoralize",
    8: "Frenzy", 9: "Disarm", 10: "Command Summoned", 11: "Invisibility",
    12: "Light", 13: "Lock", 14: "Open", 15: "Bound Weapon",
    16: "Summon Creature", 17: "Detect Life", 18: "Telekinesis",
    19: "Paralysis", 20: "Reanimate", 21: "Soul Trap", 22: "Turn Undead",
    23: "Guide", 24: "Werewolf Feed", 25: "Cure Paralysis",
    26: "Cure Addiction", 27: "Cure Poison", 28: "Concussion",
    29: "Value and Parts", 30: "Accumulate Magnitude", 31: "Stagger",
    32: "Peak Value Modifier", 33: "Cloak", 34: "Werewolf", 35: "Slow Time",
    36: "Rally", 37: "Enhance Weapon", 38: "Spawn Hazard", 39: "Etherealize",
    40: "Banish", 41: "Spawn Scripted Ref", 42: "Disguise", 43: "Grab Actor",
    44: "Vampire Lord",
}

AV = {
    6: "OneHanded", 7: "TwoHanded", 8: "Marksman", 9: "Block", 10: "Smithing",
    11: "HeavyArmor", 12: "LightArmor", 13: "Pickpocket", 14: "Lockpicking",
    15: "Sneak", 16: "Alchemy", 17: "Speechcraft", 18: "Alteration",
    19: "Conjuration", 20: "Destruction", 21: "Illusion", 22: "Restoration",
    23: "Enchanting", 24: "Health", 25: "Magicka", 26: "Stamina",
    27: "HealRate", 28: "MagickaRate", 29: "StaminaRate",
    30: "SpeedMult", 31: "InventoryWeight", 32: "CarryWeight",
    33: "CritChance", 34: "MeleeDamage", 35: "UnarmedDamage",
    36: "Mass", 37: "VoicePoints", 38: "VoiceRate",
    40: "DamageResist", 41: "PoisonResist", 42: "ResistFire",
    43: "ResistShock", 44: "ResistFrost", 45: "ResistMagic",
    46: "ResistDisease",
    52: "HealRateMult", 53: "MagickaRateMult", 54: "StaminaRateMult",
}

# drapeaux MGEF utiles
FLAG_HOSTILE = 0x00000001
FLAG_RECOVER = 0x00000004
FLAG_DETRIMENTAL = 0x00000008
FLAG_NO_DURATION = 0x00000200
FLAG_NO_MAGNITUDE = 0x00000400
FLAG_POWER_AFFECTS_MAG = 0x00200000
FLAG_POWER_AFFECTS_DUR = 0x00400000


def main():
    plugin = "Skyrim.esm"
    table = load_strings_for(plugin)
    rows = {}
    for sig, fid, body, meta in walk(os.path.join(DATA, plugin), {"MGEF"}):
        edid = full = None
        arch = pav = sav = flags = None
        for ss, b in sps.iter_subrecords(body):
            if ss == "EDID":
                edid = sps.zstring(b)
            elif ss == "FULL" and len(b) >= 4:
                (sid,) = struct.unpack_from("<I", b, 0)
                full = table.get(sid)
            elif ss == "DATA" and len(b) >= 92:
                (flags,) = struct.unpack_from("<I", b, 0)
                (arch,) = struct.unpack_from("<I", b, 64)
                (pav,) = struct.unpack_from("<i", b, 68)
                (sav,) = struct.unpack_from("<i", b, 88)
        rows[fid & 0xFFFFFF] = {
            "edid": edid, "nom": full, "arch": arch, "pav": pav,
            "sav": sav, "flags": flags,
        }

    print(f"{len(rows)} MGEF dans Skyrim.esm\n")

    # controle de coherence sur des effets connus
    print("--- controle des offsets (effets connus) ---")
    for want in ("FoodRestoreHealthDuration", "FoodRestoreStaminaDuration",
                 "FoodFortifyMagickaRate", "FoodFortifyMagicka",
                 "AlchRestoreMagicka"):
        for fid, r in rows.items():
            if r["edid"] == want:
                print(f"  {want:28s} arch={ARCHETYPES.get(r['arch'], r['arch'])!r:24s} "
                      f"AV={AV.get(r['pav'], r['pav'])}")
                break
        else:
            print(f"  {want:28s} ABSENT")

    magicka = {fid: r for fid, r in rows.items()
               if r["pav"] in (25, 28, 53) or r["sav"] in (25, 28, 53)}
    print(f"\n--- MGEF touchant Magicka / MagickaRate : {len(magicka)} ---")
    print(f"{'FormID':>10}  {'EditorID':34s}{'archetype':24s}{'AV':14s}"
          f"{'durée?':8s}{'nom'}")
    for fid, r in sorted(magicka.items(), key=lambda kv: (kv[1]["pav"], kv[1]["edid"] or "")):
        dur = "non" if (r["flags"] or 0) & FLAG_NO_DURATION else "oui"
        print(f"  {fid:08X}  {(r['edid'] or '')[:33]:34s}"
              f"{ARCHETYPES.get(r['arch'], str(r['arch']))[:23]:24s}"
              f"{AV.get(r['pav'], str(r['pav']))[:13]:14s}{dur:8s}{r['nom'] or ''}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Extrait les recettes de cuisine (COBJ dont le plan de travail est un
poste de cuisine) sur tout l'ordre de chargement actif, et resout les noms
via les fichiers .STRINGS.

Le scanner d'origine lit bien BNAM dans out["bench"] mais ne l'imprime
jamais : on refait donc la passe nous-memes.
"""
import json
import os
import struct
import sys
import zlib

sys.path.insert(0, r"C:\Users\Shadow\Downloads")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bsa
import skyrim_plugin_scan as sps

DATA = r"C:\Program Files (x86)\Steam\steamapps\common\Skyrim\Data"
STRINGS = os.path.join(DATA, "Strings")
HERE = os.path.dirname(os.path.abspath(__file__))
PLUGINS_TXT = r"C:\Users\Shadow\AppData\Local\Skyrim\plugins.txt"

VANILLA_ORDER = ["skyrim.esm", "update.esm", "dawnguard.esm",
                 "hearthfires.esm", "dragonborn.esm"]
IMPLICIT = ["Skyrim.esm", "Update.esm"]

# Types portant un nom affichable qu'on veut resoudre
NAMED = {"ALCH", "INGR", "MISC", "FOOD", "WEAP", "ARMO", "KYWD", "COBJ",
         "SLGM", "AMMO", "BOOK", "SCRL"}


# ------------------------------------------------------------------ STRINGS

def parse_strings(blob):
    """Decode un blob .STRINGS (chaines nul-terminees)."""
    count, _data_size = struct.unpack_from("<II", blob, 0)
    directory_end = 8 + count * 8
    out = {}
    for i in range(count):
        sid, offset = struct.unpack_from("<II", blob, 8 + i * 8)
        start = directory_end + offset
        end = blob.find(b"\x00", start)
        out[sid] = blob[start:end].decode("cp1252", "replace")
    return out


def load_strings_for(plugin):
    """Table de chaines propre a UN plugin.

    Les identifiants FULL sont locaux au fichier qui les porte : melanger
    les tables donne des noms faux (c'est ce qui produisait des ingredients
    du genre << Orcish Shield of Dwindling Fire >> dans une chaudree).
    Les DLC n'ont pas leurs .STRINGS dans Data\\Strings : ils sont dans le .bsa.
    """
    stem = os.path.splitext(plugin)[0]
    loose = os.path.join(STRINGS, f"{stem}_English.STRINGS")
    if os.path.exists(loose):
        with open(loose, "rb") as fh:
            return parse_strings(fh.read())
    bsa_path = os.path.join(DATA, f"{stem}.bsa")
    if os.path.exists(bsa_path):
        try:
            files = bsa.read_bsa_strings(bsa_path)
        except (ValueError, zlib.error, struct.error) as exc:
            print(f"  !! BSA illisible pour {plugin} : {exc}", file=sys.stderr)
            return {}
        blob = files.get(f"{stem.lower()}_english.strings")
        if blob:
            return parse_strings(blob)
    return {}


# ------------------------------------------------------------------ parsing

def walk(path, want_sigs):
    """Parcourt un plugin et rend (sig, formid, subrecords dict-like)."""
    with open(path, "rb") as fh:
        meta = sps.parse_tes4(fh)
        while True:
            head = fh.read(sps.REC_HEADER)
            if len(head) < sps.REC_HEADER:
                break
            sig = head[0:4].decode("ascii", "replace")
            if sig == "GRUP":
                continue
            size, flags, formid = struct.unpack_from("<III", head, 4)
            body = sps.read_record_body(fh, size, flags)
            if sig in want_sigs:
                yield sig, formid, body, meta


def main():
    # --- ordre de chargement actif (regle Skyrim LE : date de fichier) ---
    listed = []
    with open(PLUGINS_TXT, encoding="cp1252") as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#"):
                listed.append(line.lstrip("*").strip())
    on_disk = {f.lower(): f for f in os.listdir(DATA)}
    active = []
    for e in IMPLICIT + listed:
        real = on_disk.get(e.lower())
        if real and real not in active:
            active.append(real)

    def key(n):
        low = n.lower()
        if low in VANILLA_ORDER:
            return (0, VANILLA_ORDER.index(low), 0.0)
        is_esm = open(os.path.join(DATA, n), "rb").read(9)[8] & 0x01
        return (0 if is_esm else 1, 99, os.path.getmtime(os.path.join(DATA, n)))

    active.sort(key=key)

    # une table par plugin, jamais fusionnee
    tables = {}
    for p in active:
        t = load_strings_for(p)
        tables[p] = t
        if t:
            print(f"  strings {p}: {len(t)} entrees", file=sys.stderr)

    # --- passe 1 : noms, EDID, mots-cles ---------------------------------
    names = {}      # formid canonique -> nom affichable
    edids = {}      # formid canonique -> EditorID
    keywords = {}   # EditorID -> formid canonique

    def canon(formid, masters, plugin):
        hi = formid >> 24
        origin = masters[hi] if hi < len(masters) else plugin
        return f"{origin.lower()}:{formid & 0xFFFFFF:06X}"

    recipes = []

    for plugin in active:
        path = os.path.join(DATA, plugin)
        for sig, formid, body, meta in walk(path, NAMED):
            masters = meta["masters"]
            cid = canon(formid, masters, plugin)
            edid = full = None
            bench = result = result_count = None
            comps = []
            for ssig, blob in sps.iter_subrecords(body):
                if ssig == "EDID":
                    edid = sps.zstring(blob)
                elif ssig == "FULL":
                    if meta["localized"] and len(blob) >= 4:
                        (sid,) = struct.unpack_from("<I", blob, 0)
                        full = tables[plugin].get(sid)
                    else:
                        full = sps.zstring(blob)
                elif sig == "COBJ":
                    if ssig == "BNAM" and len(blob) >= 4:
                        (bench,) = struct.unpack_from("<I", blob, 0)
                    elif ssig == "CNAM" and len(blob) >= 4:
                        (result,) = struct.unpack_from("<I", blob, 0)
                    elif ssig == "NAM1" and len(blob) >= 2:
                        (result_count,) = struct.unpack_from("<H", blob, 0)
                    elif ssig == "CNTO" and len(blob) >= 8:
                        item, cnt = struct.unpack_from("<II", blob, 0)
                        comps.append((canon(item, masters, plugin), cnt))
            if edid:
                edids[cid] = edid
            if full:
                names[cid] = full
            if sig == "KYWD" and edid:
                keywords[edid] = cid
            if sig == "COBJ" and bench is not None:
                recipes.append({
                    "plugin": plugin,
                    "cid": cid,
                    "edid": edid,
                    "bench": canon(bench, masters, plugin),
                    "result": canon(result, masters, plugin) if result else None,
                    "count": result_count or 1,
                    "components": comps,
                })
        print(f"  lu : {plugin}", file=sys.stderr)

    # --- reperage des postes de cuisine ----------------------------------
    cook_kw = {v: k for k, v in keywords.items()
               if any(t in k.lower() for t in ("cookpot", "cooking", "oven", "spit"))}
    print("\nMots-cles de cuisine trouves :", file=sys.stderr)
    for cid, name in cook_kw.items():
        print(f"   {name}  [{cid}]", file=sys.stderr)

    cooking = [r for r in recipes if r["bench"] in cook_kw]

    # Une recette surchargee existe en plusieurs exemplaires (un par plugin qui
    # la touche). Le moteur ne garde que le dernier charge : on fait pareil.
    # `active` est deja trie dans l'ordre de chargement, donc le dernier vu gagne.
    winner = {}
    touched_by = {}
    for r in cooking:
        touched_by.setdefault(r["cid"], []).append(r["plugin"])
        winner[r["cid"]] = r          # ecrase : le dernier charge l'emporte
    for cid, plugs in touched_by.items():
        if len(plugs) > 1:
            print(f"  surcharge : {edids.get(cid, cid)} touche par {plugs} "
                  f"-> {plugs[-1]} gagne", file=sys.stderr)
    cooking = list(winner.values())

    def label(cid):
        return names.get(cid) or edids.get(cid) or cid

    payload = []
    for r in cooking:
        payload.append({
            "plugin": r["plugin"],
            "station": cook_kw[r["bench"]],
            "edid": r["edid"],
            "produit": label(r["result"]) if r["result"] else "?",
            "produit_edid": edids.get(r["result"], ""),
            "count": r["count"],
            "ingredients": [[label(c), n] for c, n in r["components"]],
        })

    with open(os.path.join(HERE, "cuisine.json"), "w", encoding="utf-8") as fh:
        json.dump({"recettes": payload,
                   "total_cobj": len(recipes),
                   "ordre": active}, fh, indent=1, ensure_ascii=False)

    print(f"\nCOBJ total (toutes stations) : {len(recipes)}")
    print(f"Recettes de cuisine          : {len(cooking)}")


if __name__ == "__main__":
    main()

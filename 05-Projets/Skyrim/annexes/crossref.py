#!/usr/bin/env python3
"""Croise le scan de plugins avec l'ordre de chargement reel.

Reutilise le parseur de skyrim_plugin_scan.py, mais resout chaque record
en cle canonique (master d'origine, id local) pour pouvoir comparer des
plugins qui n'ont pas la meme liste de masters.
"""
import json
import os
import sys

sys.path.insert(0, r"C:\Users\Shadow\Downloads")
import skyrim_plugin_scan as sps

DATA = r"C:\Program Files (x86)\Steam\steamapps\common\Skyrim\Data"
PLUGINS_TXT = r"C:\Users\Shadow\AppData\Local\Skyrim\plugins.txt"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "crossref.json")

# Skyrim LE : Skyrim.esm et Update.esm sont actifs implicitement, jamais listes.
IMPLICIT = ["Skyrim.esm", "Update.esm"]
# Ordre canonique impose par le moteur pour les masters officiels.
VANILLA_ORDER = ["skyrim.esm", "update.esm", "dawnguard.esm",
                 "hearthfires.esm", "dragonborn.esm"]

DETAIL = {"ALCH", "INGR", "COBJ"}


def read_plugins_txt(path):
    out = []
    with open(path, "r", encoding="cp1252") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            out.append(line.lstrip("*").strip())
    return out


def real_name(entry):
    """Retrouve le nom tel qu'il est sur le disque (casse exacte)."""
    for f in os.listdir(DATA):
        if f.lower() == entry.lower():
            return f
    return None


def load_order_key(name, is_esm, mtime):
    """Skyrim LE : les ESM passent avant les ESP, puis tri par date de fichier."""
    low = name.lower()
    if low in VANILLA_ORDER:
        return (0, VANILLA_ORDER.index(low), 0.0, low)
    return (0 if is_esm else 1, 99, mtime, low)


def main():
    listed = read_plugins_txt(PLUGINS_TXT)
    active = []
    for entry in IMPLICIT + listed:
        rn = real_name(entry)
        if rn is None:
            print(f"!! actif mais absent du dossier Data : {entry}")
            continue
        if rn not in active:
            active.append(rn)

    on_disk = [f for f in sorted(os.listdir(DATA))
               if f.lower().endswith((".esp", ".esm", ".esl"))]
    inactive = [f for f in on_disk
                if f.lower() not in {a.lower() for a in active}]

    scanned = {}
    for name in active:
        path = os.path.join(DATA, name)
        try:
            res = sps.scan_plugin(path, DETAIL)
        except (sps.PluginError, OSError) as exc:
            print(f"!! echec {name} : {exc}")
            continue
        res["mtime"] = os.path.getmtime(path)
        scanned[name] = res
        print(f"ok {name}: {len(res['details'])} records detailles")

    # --- ordre de chargement ---------------------------------------------
    by_mtime = sorted(scanned, key=lambda n: load_order_key(
        n, scanned[n]["meta"]["is_esm"], scanned[n]["mtime"]))

    # ordre tel qu'il apparait dans plugins.txt (pour comparaison)
    txt_rank = {}
    for i, entry in enumerate(IMPLICIT + listed):
        txt_rank[entry.lower()] = i
    by_txt = sorted(scanned, key=lambda n: (
        0 if n.lower() in VANILLA_ORDER else 1,
        VANILLA_ORDER.index(n.lower()) if n.lower() in VANILLA_ORDER else 0,
        txt_rank.get(n.lower(), 999)))

    rank_mtime = {n: i for i, n in enumerate(by_mtime)}
    rank_txt = {n: i for i, n in enumerate(by_txt)}

    # --- indexation canonique --------------------------------------------
    # cle = "master_d_origine:idlocal" -> liste de (plugin, info)
    index = {}
    for name, res in scanned.items():
        masters = res["meta"]["masters"]
        for info in res["details"]:
            hi = info["formid"] >> 24
            local = info["formid"] & 0x00FFFFFF
            if hi < len(masters):
                origin = masters[hi]
            else:
                origin = name  # record cree par ce plugin
            key = f"{origin.lower()}:{local:06X}"
            index.setdefault(key, []).append({
                "plugin": name,
                "origin": origin,
                "local": local,
                "sig": info["signature"],
                "edid": info["edid"],
                "name": info["name"],
                "kind": info["kind"],
                "weight": info["weight"] if "weight" in info else None,
                "value": info["value"] if "value" in info else None,
                "override": info["override"],
                "effects": len(info.get("effects", [])),
                "components": len(info.get("components", [])),
                "rank_mtime": rank_mtime[name],
                "rank_txt": rank_txt[name],
            })

    payload = {
        "active": active,
        "inactive": inactive,
        "order_mtime": by_mtime,
        "order_txt": by_txt,
        "index": index,
        "counts": {n: {"details": len(r["details"]),
                       "counts": r["counts"],
                       "overrides": r["overrides"],
                       "masters": r["meta"]["masters"]}
                   for n, r in scanned.items()},
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1)
    print(f"\necrit : {OUT}")
    print(f"cles indexees : {len(index)}")


if __name__ == "__main__":
    main()

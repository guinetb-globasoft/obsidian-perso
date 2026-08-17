---
tags: ["skyrim", "modding", "outil", "python"]
created: 2026-07-28
---

---
projet: Skyrim
type: outil
tags: ["skyrim", "modding", "outil", "python"]
created: 2026-07-27
version: 2
---

# skyrim_plugin_scan.py — v2

> Parseur TES4/TES5 sans dépendance. Inventorie les records de chaque plugin et distingue **surcharges** (conflits potentiels) et **ajouts** (inoffensifs).

## Ce qui change depuis la v1

La v1 avait un défaut relevé lors du premier croisement : `scan_plugin()` calculait bien le master d'origine de chaque record dans `info["source"]`, mais `format_details()` ne l'imprimait jamais. Les FormID affichés étaient donc **relatifs à la liste de masters de chaque plugin**, donc incomparables entre eux — il fallait reconstruire les clés canoniques à la main.

**Corrigé.** La v2 imprime `master_origine:id_local` :

- sur la ligne de chaque record, avec le FormID brut conservé entre crochets ;
- sur les **effets** (`EFID`) ;
- sur les **composants** et le **produit** des recettes `COBJ` ;
- sur l'**établi** (`BNAM`), nouvellement affiché.

Deux records portant la même clé canonique dans deux plugins différents sont le même record. C'est le critère de conflit, directement lisible.

> [!note] Limite assumée
> `--skip-vanilla` exclut volontairement les `.esm` officiels. Pour disposer des valeurs de référence, les scanner à part (sans le drapeau) et comparer.

## Utilisation

```
python skyrim_plugin_scan.py "C:\Program Files (x86)\Steam\steamapps\common\Skyrim\Data" --skip-vanilla --details ALCH,INGR,COBJ
```

| Option | Effet |
|---|---|
| `--details TYPE,TYPE` | détaille les records de ces types (`ALCH`, `INGR`, `COBJ`, `MISC`) |
| `--only texte` | ne traite que les plugins dont le nom contient `texte` |
| `--skip-vanilla` | ignore `Skyrim.esm`, `Update.esm` et les DLC officiels |
| `--csv fichier.csv` | écrit aussi un tableau récapitulatif |

Python 3.8+, aucune dépendance externe.

## Exemple de sortie

```
  [SURCHARGE] ALCH Skyrim.esm:064B33  Bread  (nourriture)    [brut 00064B33]
              EditorID : FoodBread
              poids=0.25  valeur=2
              effet Skyrim.esm:03EB07 : magnitude=10 duree=5s
  [nouveau  ] COBJ (ce plugin):000801  RecipeHoneyPie  (recette)
              composant Skyrim.esm:064B33 x1
              produit (ce plugin):000800 x1
              etabli Skyrim.esm:0A5CB3
```

## Source

```python
#!/usr/bin/env python3
"""
skyrim_plugin_scan.py - Analyse les plugins Skyrim (.esp / .esm / .esl)
et rapporte exactement quels records chaque mod touche.

Format TES4/TES5 (Bethesda). Aucune dependance externe : Python 3.8+ suffit.

Usage:
    python skyrim_plugin_scan.py "C:/.../Skyrim/Data"
    python skyrim_plugin_scan.py "C:/.../Data" --details ALCH,INGR,COBJ
    python skyrim_plugin_scan.py "C:/.../Data" --csv rapport.csv
"""

import argparse
import os
import struct
import sys
import zlib

# ---------------------------------------------------------------- constantes

REC_HEADER = 24          # taille d'un en-tete de record ET de GRUP
FLAG_MASTER = 0x00000001  # le plugin est un ESM
FLAG_LOCALIZED = 0x00000080  # chaines externalisees (fichiers .STRINGS)
FLAG_COMPRESSED = 0x00040000  # donnees du record compressees en zlib

# Types de records dont on sait extraire le detail
DETAILABLE = {"ALCH", "INGR", "COBJ", "MISC", "FOOD"}

# Drapeaux ENIT pour les ALCH (ingestibles)
ENIT_NO_AUTOCALC = 0x00000001
ENIT_FOOD_ITEM = 0x00000002
ENIT_MEDICINE = 0x00010000
ENIT_POISON = 0x00020000


class PluginError(Exception):
    pass


# ---------------------------------------------------------------- bas niveau

def iter_subrecords(data):
    """Parcourt les sous-records d'un blob de donnees de record.

    Gere XXXX, qui porte la taille reelle quand elle depasse 65535.
    Rend des tuples (signature, contenu).
    """
    pos = 0
    end = len(data)
    override_size = None
    while pos + 6 <= end:
        sig = data[pos:pos + 4].decode("ascii", "replace")
        (size,) = struct.unpack_from("<H", data, pos + 4)
        pos += 6
        if sig == "XXXX":
            (override_size,) = struct.unpack_from("<I", data, pos)
            pos += size
            continue
        if override_size is not None:
            size = override_size
            override_size = None
        yield sig, data[pos:pos + size]
        pos += size


def zstring(blob):
    """Chaine terminee par un octet nul, encodage cp1252 (usage Bethesda)."""
    return blob.split(b"\x00", 1)[0].decode("cp1252", "replace")


def read_record_body(fh, size, flags):
    """Lit le corps d'un record, en decompressant si necessaire."""
    raw = fh.read(size)
    if flags & FLAG_COMPRESSED:
        if len(raw) < 4:
            raise PluginError("record compresse tronque")
        (decompressed_size,) = struct.unpack_from("<I", raw, 0)
        try:
            raw = zlib.decompress(raw[4:])
        except zlib.error as exc:
            raise PluginError(f"echec zlib : {exc}") from exc
        if len(raw) != decompressed_size:
            # Non bloquant : certains outils ecrivent une taille approximative.
            pass
    return raw


# ---------------------------------------------------------------- en-tete

def parse_tes4(fh):
    """Lit l'enregistrement TES4 en tete de fichier et retourne ses metadonnees."""
    header = fh.read(REC_HEADER)
    if len(header) < REC_HEADER:
        raise PluginError("fichier trop court")
    sig = header[0:4].decode("ascii", "replace")
    if sig != "TES4":
        raise PluginError(f"signature inattendue : {sig!r} (attendu TES4)")

    size, flags = struct.unpack_from("<II", header, 4)
    body = read_record_body(fh, size, flags)

    masters = []
    author = ""
    description = ""
    num_records = None

    for sub_sig, blob in iter_subrecords(body):
        if sub_sig == "MAST":
            masters.append(zstring(blob))
        elif sub_sig == "CNAM":
            author = zstring(blob)
        elif sub_sig == "SNAM":
            description = zstring(blob)
        elif sub_sig == "HEDR" and len(blob) >= 8:
            (num_records,) = struct.unpack_from("<I", blob, 4)

    return {
        "masters": masters,
        "author": author,
        "description": description,
        "declared_records": num_records,
        "is_esm": bool(flags & FLAG_MASTER),
        "localized": bool(flags & FLAG_LOCALIZED),
    }


# ---------------------------------------------------------------- detail

def describe_alch(body, localized):
    """Extrait les champs utiles d'un ingestible (potion ou nourriture)."""
    out = {"edid": "", "name": "", "weight": None, "value": None,
           "kind": "potion", "effects": []}
    pending_effect = None

    for sig, blob in iter_subrecords(body):
        if sig == "EDID":
            out["edid"] = zstring(blob)
        elif sig == "FULL":
            out["name"] = "<localise>" if localized else zstring(blob)
        elif sig == "DATA" and len(blob) >= 4:
            (out["weight"],) = struct.unpack_from("<f", blob, 0)
        elif sig == "ENIT" and len(blob) >= 8:
            value, enit_flags = struct.unpack_from("<Ii", blob, 0)
            out["value"] = value
            if enit_flags & ENIT_FOOD_ITEM:
                out["kind"] = "nourriture"
            elif enit_flags & ENIT_POISON:
                out["kind"] = "poison"
            elif enit_flags & ENIT_MEDICINE:
                out["kind"] = "medicament"
        elif sig == "EFID" and len(blob) >= 4:
            (pending_effect,) = struct.unpack_from("<I", blob, 0)
        elif sig == "EFIT" and len(blob) >= 12:
            magnitude, area, duration = struct.unpack_from("<fII", blob, 0)
            out["effects"].append({
                "mgef": pending_effect,
                "magnitude": magnitude,
                "area": area,
                "duration": duration,
            })
            pending_effect = None
    return out


def describe_ingr(body, localized):
    """Extrait les champs utiles d'un ingredient d'alchimie."""
    out = {"edid": "", "name": "", "weight": None, "value": None,
           "kind": "ingredient", "effects": []}
    pending_effect = None

    for sig, blob in iter_subrecords(body):
        if sig == "EDID":
            out["edid"] = zstring(blob)
        elif sig == "FULL":
            out["name"] = "<localise>" if localized else zstring(blob)
        elif sig == "DATA" and len(blob) >= 8:
            value, weight = struct.unpack_from("<if", blob, 0)
            out["value"] = value
            out["weight"] = weight
        elif sig == "EFID" and len(blob) >= 4:
            (pending_effect,) = struct.unpack_from("<I", blob, 0)
        elif sig == "EFIT" and len(blob) >= 12:
            magnitude, area, duration = struct.unpack_from("<fII", blob, 0)
            out["effects"].append({
                "mgef": pending_effect,
                "magnitude": magnitude,
                "area": area,
                "duration": duration,
            })
            pending_effect = None
    return out


def describe_cobj(body, localized):
    """Extrait les champs utiles d'une recette (Constructible Object)."""
    out = {"edid": "", "name": "", "components": [], "result": None,
           "result_count": None, "bench": None, "kind": "recette"}

    pending_item = None
    for sig, blob in iter_subrecords(body):
        if sig == "EDID":
            out["edid"] = zstring(blob)
        elif sig == "CNTO" and len(blob) >= 8:
            item, count = struct.unpack_from("<II", blob, 0)
            out["components"].append({"item": item, "count": count})
        elif sig == "CNAM" and len(blob) >= 4:
            (out["result"],) = struct.unpack_from("<I", blob, 0)
        elif sig == "BNAM" and len(blob) >= 4:
            (out["bench"],) = struct.unpack_from("<I", blob, 0)
        elif sig == "NAM1" and len(blob) >= 2:
            (out["result_count"],) = struct.unpack_from("<H", blob, 0)
    return out


def describe_misc(body, localized):
    out = {"edid": "", "name": "", "weight": None, "value": None,
           "kind": "objet divers", "effects": []}
    for sig, blob in iter_subrecords(body):
        if sig == "EDID":
            out["edid"] = zstring(blob)
        elif sig == "FULL":
            out["name"] = "<localise>" if localized else zstring(blob)
        elif sig == "DATA" and len(blob) >= 8:
            value, weight = struct.unpack_from("<if", blob, 0)
            out["value"] = value
            out["weight"] = weight
    return out


DESCRIBERS = {
    "ALCH": describe_alch,
    "INGR": describe_ingr,
    "COBJ": describe_cobj,
    "MISC": describe_misc,
}


# ---------------------------------------------------------------- parcours

def scan_plugin(path, detail_types=frozenset()):
    """Parcourt un plugin et retourne ses metadonnees + inventaire des records."""
    size_on_disk = os.path.getsize(path)
    with open(path, "rb") as fh:
        meta = parse_tes4(fh)
        localized = meta["localized"]
        masters = meta["masters"]

        # Index du plugin lui-meme dans sa propre liste de masters
        own_index = len(masters)

        counts = {}
        overrides = {}
        details = []

        while True:
            head = fh.read(REC_HEADER)
            if len(head) < REC_HEADER:
                break
            sig = head[0:4].decode("ascii", "replace")

            if sig == "GRUP":
                # On descend dedans : on ne saute que l'en-tete.
                continue

            rec_size, rec_flags, form_id = struct.unpack_from("<III", head, 4)
            body = read_record_body(fh, rec_size, rec_flags)

            counts[sig] = counts.get(sig, 0) + 1

            # L'octet de poids fort du FormID designe le master d'origine.
            master_index = form_id >> 24
            is_override = master_index < own_index
            if is_override:
                overrides[sig] = overrides.get(sig, 0) + 1

            if sig in detail_types and sig in DESCRIBERS:
                info = DESCRIBERS[sig](body, localized)
                info["formid"] = form_id
                info["signature"] = sig
                info["override"] = is_override
                info["source"] = (masters[master_index]
                                  if master_index < len(masters) else "(ce plugin)")
                info["_masters"] = masters
                details.append(info)

    return {
        "path": path,
        "name": os.path.basename(path),
        "size": size_on_disk,
        "meta": meta,
        "counts": counts,
        "overrides": overrides,
        "details": details,
    }


# ---------------------------------------------------------------- rendu

def format_plugin_summary(result):
    meta = result["meta"]
    lines = []
    lines.append("=" * 78)
    lines.append(f"{result['name']}   ({result['size']:,} octets)".replace(",", " "))
    lines.append("=" * 78)

    if meta["author"]:
        lines.append(f"  Auteur      : {meta['author']}")
    if meta["description"]:
        lines.append(f"  Description : {meta['description'][:200]}")
    lines.append(f"  Masters     : {', '.join(meta['masters']) or '(aucun)'}")
    lines.append(f"  Type        : {'ESM' if meta['is_esm'] else 'ESP'}"
                 f"{' / chaines localisees' if meta['localized'] else ''}")

    counts = result["counts"]
    overrides = result["overrides"]
    if not counts:
        lines.append("  Aucun record.")
        return "\n".join(lines)

    total = sum(counts.values())
    total_ovr = sum(overrides.values())
    lines.append(f"  Records     : {total} dont {total_ovr} en surcharge de records existants")
    lines.append("")
    lines.append(f"  {'TYPE':<8}{'TOTAL':>8}{'SURCHARGES':>13}{'NOUVEAUX':>11}")
    lines.append(f"  {'-' * 40}")
    for sig in sorted(counts, key=lambda s: -counts[s]):
        ovr = overrides.get(sig, 0)
        lines.append(f"  {sig:<8}{counts[sig]:>8}{ovr:>13}{counts[sig] - ovr:>11}")

    return "\n".join(lines)


def format_details(result):
    if not result["details"]:
        return ""
    lines = ["", "  --- detail des records demandes ---"]
    for info in result["details"]:
        tag = "SURCHARGE" if info["override"] else "nouveau  "
        label = info.get("name") or info.get("edid") or "?"
        # Cle canonique : le FormID brut n'est PAS comparable d'un plugin a
        # l'autre (son octet de poids fort est un index dans la liste de
        # masters propre au plugin). On imprime master_origine:id_local, qui
        # designe le meme record quel que soit le plugin qui le porte.
        canonical = f"{info['source']}:{info['formid'] & 0xFFFFFF:06X}"
        head = (f"  [{tag}] {info['signature']} {canonical}  "
                f"{label}  ({info['kind']})")
        lines.append(f"{head}    [brut {info['formid']:08X}]")
        if info.get("edid") and info.get("name"):
            lines.append(f"              EditorID : {info['edid']}")
        bits = []
        if info.get("weight") is not None:
            bits.append(f"poids={info['weight']:g}")
        if info.get("value") is not None:
            bits.append(f"valeur={info['value']}")
        if bits:
            lines.append(f"              {'  '.join(bits)}")

        masters = info.get("_masters", [])

        def canon(form_id):
            """Resout un FormID reference vers master_origine:id_local."""
            idx = form_id >> 24
            origin = masters[idx] if idx < len(masters) else "(ce plugin)"
            return f"{origin}:{form_id & 0xFFFFFF:06X}"

        for eff in info.get("effects", []):
            lines.append(f"              effet {canon(eff['mgef'])} : "
                         f"magnitude={eff['magnitude']:g} duree={eff['duration']}s")
        for comp in info.get("components", []):
            lines.append(f"              composant {canon(comp['item'])} x{comp['count']}")
        if info.get("result") is not None:
            lines.append(f"              produit {canon(info['result'])} "
                         f"x{info.get('result_count') or 1}")
        if info.get("bench") is not None:
            lines.append(f"              etabli {canon(info['bench'])}")
    return "\n".join(lines)


def write_csv(results, csv_path):
    import csv as _csv
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        writer = _csv.writer(fh, delimiter=";")
        writer.writerow(["plugin", "type_record", "total", "surcharges", "nouveaux"])
        for res in results:
            for sig, count in sorted(res["counts"].items()):
                ovr = res["overrides"].get(sig, 0)
                writer.writerow([res["name"], sig, count, ovr, count - ovr])


# ---------------------------------------------------------------- entree

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Analyse les plugins Skyrim et rapporte les records touches.")
    parser.add_argument("data_dir", help="dossier Data de Skyrim")
    parser.add_argument("--details", default="",
                        help="types a detailler, separes par des virgules "
                             "(ex: ALCH,INGR,COBJ)")
    parser.add_argument("--only", default="",
                        help="n'analyser que les plugins dont le nom contient ce texte")
    parser.add_argument("--csv", default="", help="ecrire aussi un rapport CSV")
    parser.add_argument("--skip-vanilla", action="store_true",
                        help="ignorer Skyrim.esm, Update.esm et les DLC officiels")
    args = parser.parse_args(argv)

    detail_types = {t.strip().upper() for t in args.details.split(",") if t.strip()}

    vanilla = {"skyrim.esm", "update.esm", "dawnguard.esm",
               "hearthfires.esm", "dragonborn.esm"}

    candidates = []
    for entry in sorted(os.listdir(args.data_dir)):
        if not entry.lower().endswith((".esp", ".esm", ".esl")):
            continue
        if args.only and args.only.lower() not in entry.lower():
            continue
        if args.skip_vanilla and entry.lower() in vanilla:
            continue
        candidates.append(os.path.join(args.data_dir, entry))

    if not candidates:
        print("Aucun plugin trouve.", file=sys.stderr)
        return 1

    results = []
    for path in candidates:
        try:
            res = scan_plugin(path, detail_types)
        except (PluginError, OSError, struct.error) as exc:
            print("=" * 78)
            print(f"{os.path.basename(path)} : ECHEC DE LECTURE — {exc}")
            continue
        results.append(res)
        print(format_plugin_summary(res))
        detail_block = format_details(res)
        if detail_block:
            print(detail_block)
        print()

    if args.csv and results:
        write_csv(results, args.csv)
        print(f"Rapport CSV ecrit : {args.csv}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
```

---

Voir [[00-Index]] · [[01-Conflits-Nourriture-Ingredients]] · [[02-Brief-Mod-Nourriture]]

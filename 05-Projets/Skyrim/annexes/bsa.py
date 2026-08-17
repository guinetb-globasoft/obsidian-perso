#!/usr/bin/env python3
"""Lecteur minimal d'archives BSA Skyrim LE (version 104).

Sert uniquement a recuperer les tables .STRINGS des DLC, qui ne sont pas
posees dans Data\\Strings mais empaquetees dans le .bsa.
"""
import struct
import zlib

FLAG_DIR_NAMES = 0x0001
FLAG_FILE_NAMES = 0x0002
FLAG_COMPRESSED = 0x0004
FLAG_EMBED_NAMES = 0x0100

SIZE_COMPRESS_TOGGLE = 0x40000000


def read_bsa_strings(path):
    """Rend {nom_de_fichier_minuscule: octets} pour les entrees du dossier strings."""
    with open(path, "rb") as fh:
        blob = fh.read()

    magic, version, folder_offset, arch_flags, folder_count, file_count, \
        total_folder_name_len, total_file_name_len, file_flags = \
        struct.unpack_from("<4sIIIIIIII", blob, 0)

    if magic != b"BSA\x00":
        raise ValueError(f"{path}: signature {magic!r} inattendue")
    if version not in (103, 104, 105):
        raise ValueError(f"{path}: version BSA {version} non geree")

    # --- enregistrements de dossiers ---
    folders = []
    pos = folder_offset
    for _ in range(folder_count):
        if version == 105:
            _hash, count, _pad, offset = struct.unpack_from("<QIIQ", blob, pos)
            pos += 24
        else:
            _hash, count, offset = struct.unpack_from("<QII", blob, pos)
            pos += 16
        folders.append({"count": count, "offset": offset})

    # --- noms de dossiers + enregistrements de fichiers ---
    entries = []          # (dossier, taille, offset, compresse)
    for fold in folders:
        pos = fold["offset"] - total_file_name_len
        name = ""
        if arch_flags & FLAG_DIR_NAMES:
            (ln,) = struct.unpack_from("<B", blob, pos)
            pos += 1
            name = blob[pos:pos + ln - 1].decode("cp1252", "replace")
            pos += ln
        for _ in range(fold["count"]):
            _h, size, offset = struct.unpack_from("<QII", blob, pos)
            pos += 16
            compressed = bool(arch_flags & FLAG_COMPRESSED)
            if size & SIZE_COMPRESS_TOGGLE:
                compressed = not compressed
                size &= ~SIZE_COMPRESS_TOGGLE
            entries.append([name, size, offset, compressed, None])

    # --- bloc des noms de fichiers (concatenes, dans l'ordre) ---
    if arch_flags & FLAG_FILE_NAMES:
        pos = folder_offset + folder_count * (24 if version == 105 else 16)
        pos += total_folder_name_len + folder_count  # noms + octets de longueur
        pos += file_count * 16                       # enregistrements fichiers
        names_blob = blob[pos:pos + total_file_name_len]
        names = names_blob.split(b"\x00")
        for i, ent in enumerate(entries):
            if i < len(names):
                ent[4] = names[i].decode("cp1252", "replace")

    # --- extraction des seuls fichiers du dossier strings ---
    out = {}
    for folder, size, offset, compressed, fname in entries:
        if "strings" not in folder.lower():
            continue
        if not fname:
            continue
        p = offset
        if arch_flags & FLAG_EMBED_NAMES:
            (ln,) = struct.unpack_from("<B", blob, p)
            p += 1 + ln
        if compressed:
            (orig,) = struct.unpack_from("<I", blob, p)
            p += 4
            data = zlib.decompress(blob[p:p + size])
            if len(data) != orig:
                data = data[:orig]
        else:
            data = blob[p:p + size]
        out[fname.lower()] = data
    return out


if __name__ == "__main__":
    import sys
    for f in read_bsa_strings(sys.argv[1]):
        print(f)

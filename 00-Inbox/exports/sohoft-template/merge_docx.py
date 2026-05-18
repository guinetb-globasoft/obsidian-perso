"""
Fusionne le body Pandoc dans le docx SoHoft en préservant :
- page de garde (avant le 1er pagebreak)
- sommaire SoHoft
- headers / footers / fonts / theme / styles / images

Produit : Propale_Sohoft_CA_Immobilier_v1.docx
"""
import re, shutil, zipfile
from pathlib import Path
from lxml import etree

EXPORTS = Path(r'C:/Users/Shadow/Documents/vault-prive/00-Inbox/exports')
# On utilise sohoft-reference.docx (SoHoft + styleIds Heading1/2/3/Title/SourceCode standards)
SOHOFT = EXPORTS / 'sohoft-template' / 'sohoft-reference.docx'
BODY = EXPORTS / '_body_raw.docx'
OUT = EXPORTS / 'Propale_Sohoft_CA_Immobilier_v1.docx'

NS = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'rel': 'http://schemas.openxmlformats.org/package/2006/relationships',
    'w14': 'http://schemas.microsoft.com/office/word/2010/wordml',
    'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
    'mc': 'http://schemas.openxmlformats.org/markup-compatibility/2006',
}

# ------ Lecture des sources ------

def read_zip_member(z, name):
    return z.read(name)

with zipfile.ZipFile(SOHOFT) as z_sohoft:
    sohoft_doc = z_sohoft.read('word/document.xml').decode('utf-8')
    sohoft_rels = z_sohoft.read('word/_rels/document.xml.rels').decode('utf-8')
    sohoft_numbering = z_sohoft.read('word/numbering.xml').decode('utf-8') if 'word/numbering.xml' in z_sohoft.namelist() else None

with zipfile.ZipFile(BODY) as z_body:
    body_doc = z_body.read('word/document.xml').decode('utf-8')
    body_rels = z_body.read('word/_rels/document.xml.rels').decode('utf-8')
    body_numbering = z_body.read('word/numbering.xml').decode('utf-8') if 'word/numbering.xml' in z_body.namelist() else None
    body_files = z_body.namelist()

# ------ Extraction du body Pandoc (sans sectPr) ------

body_start = body_doc.find('<w:body>') + len('<w:body>')
body_end = body_doc.rfind('</w:body>')
body_inner = body_doc[body_start:body_end]

# retirer le sectPr final du body Pandoc
body_inner = re.sub(r'<w:sectPr[^>]*>.*?</w:sectPr>', '', body_inner, flags=re.DOTALL)
print(f'[1] Body Pandoc extrait : {len(body_inner)} caracteres')

# ------ Extraction de la page de garde SoHoft (jusqu'au 1er pagebreak inclus) ------

# Trouver le 1er w:br w:type="page"
m = re.search(r'<w:br[^/]*w:type="page"[^/]*/>', sohoft_doc)
if not m:
    raise SystemExit('Pas de saut de page dans SoHoft')
break_pos = m.end()

# Trouver la fin du paragraphe w:p qui contient ce pagebreak
close_p = sohoft_doc.find('</w:p>', break_pos) + len('</w:p>')

# La page de garde SoHoft = body_start_sohoft .. close_p
sohoft_body_start = sohoft_doc.find('<w:body>') + len('<w:body>')
cover = sohoft_doc[sohoft_body_start:close_p]
print(f'[2] Page de garde SoHoft : {len(cover)} caracteres')

# ------ Extraction du sectPr SoHoft (pour bornes de section finales) ------

sohoft_body_end = sohoft_doc.rfind('</w:body>')
sect_match = re.search(r'<w:sectPr[^>]*>.*?</w:sectPr>', sohoft_doc[:sohoft_body_end], re.DOTALL)
if sect_match:
    last_sect = sect_match.group(0)
    # On prend le dernier sectPr (celui de fin de document)
    all_sects = list(re.finditer(r'<w:sectPr[^>]*>.*?</w:sectPr>', sohoft_doc, re.DOTALL))
    last_sect = all_sects[-1].group(0) if all_sects else ''
    print(f'[3] sectPr final : {len(last_sect)} caracteres')
else:
    last_sect = ''

# ------ Gestion des rIds : renuméroter ceux du body Pandoc pour éviter collision ------

# Parser les rels du SoHoft et du Body
def parse_rels(rels_xml):
    r = etree.fromstring(rels_xml.encode('utf-8'))
    result = {}
    for rel in r.findall('rel:Relationship', NS):
        result[rel.get('Id')] = {
            'Type': rel.get('Type'),
            'Target': rel.get('Target'),
            'TargetMode': rel.get('TargetMode'),
        }
    return result

sohoft_rel_dict = parse_rels(sohoft_rels)
body_rel_dict = parse_rels(body_rels)

# trouver un rId libre de base
max_id = 0
for k in sohoft_rel_dict:
    mm = re.match(r'rId(\d+)', k)
    if mm:
        max_id = max(max_id, int(mm.group(1)))
offset = max_id + 100  # marge de sécurité
print(f'[4] Offset rId : +{offset} (max SoHoft = rId{max_id})')

# renuméroter les rId du body
id_map = {}
for old_id in body_rel_dict.keys():
    mm = re.match(r'rId(\d+)', old_id)
    if mm:
        new_id = f'rId{int(mm.group(1)) + offset}'
        id_map[old_id] = new_id
    else:
        id_map[old_id] = old_id

# Appliquer la renumérotation sur body_inner (attributs r:id="rIdN" et r:embed="rIdN")
def remap_ids(text, id_map):
    def sub(match):
        val = match.group(2)
        return f'{match.group(1)}="{id_map.get(val, val)}"'
    return re.sub(r'(r:id|r:embed|r:link)="(rId\d+)"', sub, text)

body_inner_remapped = remap_ids(body_inner, id_map)
print(f'[5] rId remappes dans body_inner')

# ------ Construction du nouveau document.xml ------

# header de document.xml d'origine (jusqu'à <w:body>)
doc_header = sohoft_doc[:sohoft_body_start]
doc_footer = '</w:body></w:document>'

new_body = cover + body_inner_remapped + last_sect

# On concatène
new_doc = doc_header + new_body + doc_footer
print(f'[6] Nouveau document.xml : {len(new_doc)} caracteres (vs SoHoft orig {len(sohoft_doc)})')

# ------ Fusion des rels ------

# Garder uniquement les rels du body effectivement référencées dans body_inner_remapped
# (les autres — styles, fonts, settings, theme — sont déjà fournies par SoHoft)
used_ids = set(re.findall(r'(?:r:id|r:embed|r:link)="(rId\d+)"', body_inner_remapped))
print(f'[6b] rId reference dans body_inner : {len(used_ids)}')

r_sohoft_root = etree.fromstring(sohoft_rels.encode('utf-8'))
added = skipped = 0
for old_id, props in body_rel_dict.items():
    new_id = id_map[old_id]
    if new_id not in used_ids:
        skipped += 1
        continue
    if any(rel.get('Id') == new_id for rel in r_sohoft_root):
        continue
    attrs = {'Id': new_id, 'Type': props['Type'], 'Target': props['Target']}
    if props['TargetMode']:
        attrs['TargetMode'] = props['TargetMode']
    etree.SubElement(r_sohoft_root, '{http://schemas.openxmlformats.org/package/2006/relationships}Relationship', attrs)
    added += 1
new_rels = etree.tostring(r_sohoft_root, xml_declaration=True, encoding='UTF-8', standalone=True).decode('utf-8')
print(f'[7] +{added} relations ajoutees ({skipped} orphelines filtrees)')

# ------ Fusion de numbering.xml (si Pandoc en a ajouté) ------

new_numbering = sohoft_numbering
if body_numbering and sohoft_numbering:
    s_num = etree.fromstring(sohoft_numbering.encode('utf-8'))
    b_num = etree.fromstring(body_numbering.encode('utf-8'))
    W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    existing_abs = {a.get(W + 'abstractNumId') for a in s_num.findall(W + 'abstractNum')}
    existing_num = {n.get(W + 'numId') for n in s_num.findall(W + 'num')}
    add_ab = 0
    for abn in b_num.findall(W + 'abstractNum'):
        if abn.get(W + 'abstractNumId') not in existing_abs:
            s_num.append(abn)
            add_ab += 1
    add_n = 0
    for nn in b_num.findall(W + 'num'):
        if nn.get(W + 'numId') not in existing_num:
            s_num.append(nn)
            add_n += 1
    new_numbering = etree.tostring(s_num, xml_declaration=True, encoding='UTF-8', standalone=True).decode('utf-8')
    print(f'[8] numbering fusionne (+{add_ab} abstractNum, +{add_n} num)')

# ------ Ecriture du zip final ------

with zipfile.ZipFile(SOHOFT, 'r') as zin:
    with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.namelist():
            data = zin.read(item)
            if item == 'word/document.xml':
                data = new_doc.encode('utf-8')
            elif item == 'word/_rels/document.xml.rels':
                data = new_rels.encode('utf-8')
            elif item == 'word/numbering.xml' and new_numbering:
                data = new_numbering.encode('utf-8')
            zout.writestr(item, data)

print(f'\n[OK] Livrable : {OUT}')
print(f'     Taille : {OUT.stat().st_size:,} bytes')

"""Créer sohoft-reference.docx : SoHoft docx + styles Heading1/2/3 standards basés sur les styles SoHoft."""
import shutil, zipfile, os, re
from pathlib import Path

WORK = Path(r'C:/Users/Shadow/Documents/vault-prive/00-Inbox/exports/sohoft-template')
SRC = WORK / 'sohoft-source.docx'
DST = WORK / 'sohoft-reference.docx'

W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

shutil.copy(SRC, DST)

# Nouveaux styles à injecter (basedOn les styles SoHoft existants)
extra_styles = '''<w:style w:type="paragraph" w:styleId="Heading1" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:name w:val="heading 1"/>
  <w:basedOn w:val="Heading1-left"/>
  <w:next w:val="Normal"/>
  <w:link w:val="Heading1-left"/>
  <w:uiPriority w:val="9"/>
  <w:qFormat/>
  <w:pPr>
    <w:outlineLvl w:val="0"/>
  </w:pPr>
</w:style>
<w:style w:type="paragraph" w:styleId="Heading2">
  <w:name w:val="heading 2"/>
  <w:basedOn w:val="Heading2-left"/>
  <w:next w:val="Normal"/>
  <w:uiPriority w:val="9"/>
  <w:unhideWhenUsed/>
  <w:qFormat/>
  <w:pPr>
    <w:outlineLvl w:val="1"/>
  </w:pPr>
</w:style>
<w:style w:type="paragraph" w:styleId="Heading3">
  <w:name w:val="heading 3"/>
  <w:basedOn w:val="Heading3-left"/>
  <w:next w:val="Normal"/>
  <w:uiPriority w:val="9"/>
  <w:unhideWhenUsed/>
  <w:qFormat/>
  <w:pPr>
    <w:outlineLvl w:val="2"/>
  </w:pPr>
</w:style>
<w:style w:type="paragraph" w:styleId="Heading4">
  <w:name w:val="heading 4"/>
  <w:basedOn w:val="Heading3-left"/>
  <w:next w:val="Normal"/>
  <w:uiPriority w:val="9"/>
  <w:unhideWhenUsed/>
  <w:qFormat/>
  <w:pPr>
    <w:outlineLvl w:val="3"/>
  </w:pPr>
  <w:rPr><w:sz w:val="28"/></w:rPr>
</w:style>
<w:style w:type="paragraph" w:styleId="Heading5">
  <w:name w:val="heading 5"/>
  <w:basedOn w:val="Heading3-left"/>
  <w:next w:val="Normal"/>
  <w:uiPriority w:val="9"/>
  <w:unhideWhenUsed/>
  <w:qFormat/>
  <w:pPr>
    <w:outlineLvl w:val="4"/>
  </w:pPr>
  <w:rPr><w:sz w:val="24"/></w:rPr>
</w:style>
<w:style w:type="paragraph" w:styleId="Heading6">
  <w:name w:val="heading 6"/>
  <w:basedOn w:val="Heading3-left"/>
  <w:next w:val="Normal"/>
  <w:uiPriority w:val="9"/>
  <w:unhideWhenUsed/>
  <w:qFormat/>
  <w:pPr>
    <w:outlineLvl w:val="5"/>
  </w:pPr>
  <w:rPr><w:sz w:val="22"/><w:i/></w:rPr>
</w:style>
<w:style w:type="paragraph" w:styleId="Title">
  <w:name w:val="Title"/>
  <w:basedOn w:val="Title1"/>
  <w:next w:val="Normal"/>
  <w:uiPriority w:val="10"/>
  <w:qFormat/>
</w:style>
<w:style w:type="paragraph" w:styleId="Author">
  <w:name w:val="Author"/>
  <w:basedOn w:val="Normal"/>
  <w:next w:val="Normal"/>
  <w:qFormat/>
  <w:pPr>
    <w:jc w:val="center"/>
  </w:pPr>
</w:style>
<w:style w:type="paragraph" w:styleId="SourceCode">
  <w:name w:val="Source Code"/>
  <w:basedOn w:val="Normal"/>
  <w:next w:val="Normal"/>
  <w:uiPriority w:val="99"/>
  <w:unhideWhenUsed/>
  <w:pPr>
    <w:shd w:val="clear" w:color="auto" w:fill="F2F2F2"/>
    <w:spacing w:after="0" w:line="240" w:lineRule="auto"/>
  </w:pPr>
  <w:rPr>
    <w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" w:cs="Consolas"/>
    <w:sz w:val="18"/>
  </w:rPr>
</w:style>
<w:style w:type="character" w:styleId="VerbatimChar">
  <w:name w:val="Verbatim Char"/>
  <w:basedOn w:val="DefaultParagraphFont"/>
  <w:uiPriority w:val="99"/>
  <w:rPr>
    <w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" w:cs="Consolas"/>
    <w:sz w:val="18"/>
  </w:rPr>
</w:style>
<w:style w:type="table" w:styleId="Table">
  <w:name w:val="Table"/>
  <w:basedOn w:val="TableNormal"/>
  <w:uiPriority w:val="39"/>
  <w:tblPr>
    <w:tblInd w:w="0" w:type="dxa"/>
    <w:tblBorders>
      <w:top w:val="single" w:sz="4" w:space="0" w:color="auto"/>
      <w:left w:val="single" w:sz="4" w:space="0" w:color="auto"/>
      <w:bottom w:val="single" w:sz="4" w:space="0" w:color="auto"/>
      <w:right w:val="single" w:sz="4" w:space="0" w:color="auto"/>
      <w:insideH w:val="single" w:sz="4" w:space="0" w:color="auto"/>
      <w:insideV w:val="single" w:sz="4" w:space="0" w:color="auto"/>
    </w:tblBorders>
  </w:tblPr>
</w:style>
<w:style w:type="paragraph" w:styleId="TOCHeading">
  <w:name w:val="TOC Heading"/>
  <w:basedOn w:val="Heading1-left"/>
  <w:next w:val="Normal"/>
  <w:uiPriority w:val="39"/>
  <w:qFormat/>
</w:style>'''

# Remove default namespace prefix in extras — already scoped via xmlns on root
extra_styles_clean = re.sub(r' xmlns:w="[^"]*"', '', extra_styles)

# Lecture + modification du styles.xml dans le zip
tmp = WORK / 'sohoft-reference-tmp.docx'
with zipfile.ZipFile(DST, 'r') as zin:
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.namelist():
            data = zin.read(item)
            if item == 'word/styles.xml':
                text = data.decode('utf-8')
                # insérer les nouveaux styles juste avant </w:styles>
                if 'Heading1' not in re.findall(r'w:styleId="([^"]+)"', text) or True:
                    text = text.replace('</w:styles>', extra_styles_clean + '</w:styles>')
                data = text.encode('utf-8')
            zout.writestr(item, data)

shutil.move(tmp, DST)
print(f'OK: {DST}')
print(f'Taille: {os.path.getsize(DST)} bytes')

from pathlib import Path
from pypdf import PdfReader
from PIL import Image
import hashlib, json
root=Path(__file__).resolve().parents[1]
pdf=root/'docs/mytech-eps-pcb-handbook.pdf'
r=PdfReader(pdf)
assert len(r.pages)==58, len(r.pages)
for n,p in enumerate(r.pages,1):
    text=p.extract_text() or ''
    assert len(text)>60, ('missing page content',n)
    if n<=54: assert f'{n:02}' in text[:350], ('page label mismatch',n)
for item in json.loads((root/'research/asset-manifest.json').read_text(encoding='utf8')):
    path=root/item['path']
    assert hashlib.sha256(path.read_bytes()).hexdigest()==item['sha256'], ('asset mismatch',path)
    with Image.open(path) as im: im.verify()
a=PdfReader(root/'source-documents/Author_and_Acknowledgements.pdf')
assert len(a.pages)==4
for n,p in enumerate(a.pages): assert p.extract_text()==r.pages[54+n].extract_text(), ('appendix changed',n)
record=json.loads((root/'research/acknowledgements-source.json').read_text(encoding='utf8'))
assert hashlib.sha256((root/record['path']).read_bytes()).hexdigest()==record['sha256']
print('Validated: 58 pages; unchanged author appendix; source hashes and original page labels.')

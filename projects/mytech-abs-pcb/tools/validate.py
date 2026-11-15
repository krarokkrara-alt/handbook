"""Validate the ABS publication and relative Markdown links."""
from pathlib import Path
from zipfile import ZipFile
from urllib.parse import unquote
import hashlib,json,re,sys

ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'publication_manifest.json').read_text(encoding='utf-8'))
errors=[]
for item in manifest['files']:
    p=ROOT/item['path']
    if not p.is_file():errors.append('Missing '+item['path']);continue
    b=p.read_bytes()
    if len(b)!=item['bytes'] or hashlib.sha256(b).hexdigest()!=item['sha256']:errors.append('Hash mismatch '+item['path'])
    if p.suffix=='.docx':
        with ZipFile(p) as z:
            if z.testzip():errors.append('Invalid DOCX '+item['path'])
for p in ROOT.rglob('*.md'):
    for link in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',link) or link.startswith('#'):continue
        path=unquote(link.split('#',1)[0].strip('<>'))
        if not (p.parent/path).exists():errors.append('Broken link '+str(p.relative_to(ROOT))+': '+link)
try:
    from pypdf import PdfReader
    for p,n in [(ROOT/'books/ABS-MyTech-Real-PCB.pdf',59),(ROOT/'source-documents/Author_and_Acknowledgements.pdf',4)]:
        if len(PdfReader(p).pages)!=n:errors.append('Page count '+p.name)
except ImportError:
    print('pypdf not installed; PDF page-count check skipped.')
if errors:
    print('\n'.join(errors));sys.exit(1)
print('PASS: publication hashes, DOCX integrity, relative links and available PDF checks.')

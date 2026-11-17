from pathlib import Path
import re,json,hashlib
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1]
report=json.loads((R/'BUILD_REPORT.json').read_text(encoding='utf-8'))
r=PdfReader(R/'books/BCM-MyTech-Handbook.pdf')
assert len(r.pages)==report['total_pages']
assert report['author_pages']==4
assert not report['out_of_bounds']
s=(R/'manuscript.md').read_text(encoding='utf-8')
for n in range(1,16):assert re.search(r'## บท(?:ที่)?\s*'+str(n)+r'\s',s),n
assert len(r.outline)>=18
for path in re.findall(r'<img src="([^"]+)"',(R/'books/BCM-MyTech-Handbook.html').read_text(encoding='utf-8')):
    assert (R/'books'/path).resolve().is_file(),path
author=PdfReader(R/'source-documents/Author_and_Acknowledgements.pdf')
for a,b in zip(r.pages[-4:],author.pages):
    assert a.get_contents().get_data()==b.get_contents().get_data()
assert all((R/f).is_file() for f in ['README.md','CLAUDE_HANDOFF.md','VISUAL_SOURCES.md','QA_REPORT.md'])
print('PASS:',len(r.pages),'pages, 15 chapters, 4 unchanged author pages, HTML images and bounds')

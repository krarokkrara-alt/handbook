from pathlib import Path
import re,json,hashlib
from pypdf import PdfReader
R=Path(__file__).absolute().parents[1]
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
for a,b in zip(r.pages[1:5],author.pages):
    assert a.get_contents().get_data()==b.get_contents().get_data()
assert all((R/f).is_file() for f in ['README.md','CLAUDE_HANDOFF.md','VISUAL_SOURCES.md','QA_REPORT.md'])
assert report['author_location']==[2,5]
destinations={d.title:r.get_destination_page_number(d)+1 for d in r.outline if not isinstance(d,list)}
for title,page in report['chapters']:assert destinations[title]==page,(title,page)
assert '<table>' in (R/'books/BCM-MyTech-Handbook.html').read_text(encoding='utf-8')
import sys;sys.path.insert(0,str(R/'tools'))
from compare_data import compare
_c=compare(b'\x00'*8,b'\x00'*3+b'\x01\x02'+b'\x00'*3,'read_repeat')
assert _c['different_byte_positions']==2 and _c['different_ranges_inclusive']==[{'start_hex':'0x3','end_hex':'0x4','length':2}],_c
assert compare(b'ab',b'abc')['different_byte_positions']==1
assert '\\x01' not in json.dumps(_c) and 'หยุดงาน' in _c['verdict_th']
def has_watermark(page):
    gs=(page.get('/Resources') or {}).get('/ExtGState') or {}
    return any(abs(float(v.get_object().get('/ca',1))-0.09)<1e-6 for v in gs.values())
wm=report.get('watermark') or {}
assert wm.get('text') and wm.get('from_page')==6,'watermark missing from BUILD_REPORT.json'
assert not any(has_watermark(p) for p in r.pages[:5]),'cover/author pages must not be watermarked'
missing=[i for i,p in enumerate(r.pages,1) if i>=6 and not has_watermark(p)]
assert not missing,('watermark missing on pages',missing)
assert 'class="watermark"' in (R/'books/BCM-MyTech-Handbook.html').read_text(encoding='utf-8')
print('PASS:',len(r.pages),'pages, 15 chapters plus detailed supplement, author pages 2-5, HTML images and bounds, watermark pages 6-'+str(len(r.pages)))

from pypdf import PdfReader,PdfWriter
from pathlib import Path
import json
r=PdfReader('tmp/pdfs/mytech-eps-pcb-raw.pdf');assert len(r.pages)==42
order=[0,41]+list(range(20,41))+list(range(1,20));assert sorted(order)==list(range(42))
w=PdfWriter()
for i in order:w.add_page(r.pages[i])
w.add_metadata({'/Title':'คู่มือซ่อมพวงมาลัยไฟฟ้า by mytech - เน้น PCB','/Author':'mytech'})
for name,page in [('เปิดเล่ม',1),('ภาค PCB และอุปกรณ์',2),('PCB จริงหลายยี่ห้อ',13),('Schematic ตัวอย่างผู้ผลิต',18),('ภาคผนวก Honda Z51',23)]:w.add_outline_item(name,page)
p=Path('output/pdf/mytech-eps-pcb-handbook.pdf');p.parent.mkdir(parents=True,exist_ok=True);w.write(p)
raw=json.loads(Path('output/book-v2-raw-index.json').read_text(encoding='utf8'))
Path('output/mytech-book-index.json').write_text(json.dumps([{'page':n+1,'title':raw[i][1]} for n,i in enumerate(order)],ensure_ascii=False,indent=2),encoding='utf8')
print('Final pages',len(w.pages),'MB',round(p.stat().st_size/1048576,2))

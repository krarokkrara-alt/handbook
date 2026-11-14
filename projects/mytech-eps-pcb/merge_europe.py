from pypdf import PdfReader,PdfWriter
from pathlib import Path
from io import BytesIO
from reportlab.pdfgen import canvas
b=PdfReader('output/pdf/mytech-eps-pcb-handbook.pdf');e=PdfReader('tmp/pdfs/mytech-europe-pages.pdf');assert len(b.pages)==42 and len(e.pages)==13
w=PdfWriter();w.add_page(e.pages[0])
overlay=BytesIO();cc=canvas.Canvas(overlay,pagesize=(595.28,841.89));cc.setFont('Helvetica-Bold',9);cc.setFillColorRGB(0,0.49,0.53);cc.drawString(36,60,'EUROPE PCB CASES: pages 43-54');cc.save();overlay.seek(0);b.pages[1].merge_page(PdfReader(overlay).pages[0])
for p in b.pages[1:]:w.add_page(p)
for p in e.pages[1:]:w.add_page(p)
w.add_metadata({'/Title':'คู่มือซ่อมพวงมาลัยไฟฟ้า by mytech - PCB ญี่ปุ่น เกาหลี ยุโรป','/Author':'mytech'})
for title,page in [('เปิดเล่ม / สารบัญ',1),('ภาค PCB และอุปกรณ์',2),('PCB จริงหลายยี่ห้อ',13),('Schematic ผู้ผลิตชิป',18),('ภาคผนวก Honda Z51',23),('ภาคยุโรป',42),('Fiat / Opel',43),('MINI',45),('Volkswagen / Audi',47),('Renault',49),('แหล่งข้อมูลยุโรป',53)]:w.add_outline_item(title,page)
p=Path('output/pdf/mytech-eps-pcb-handbook-europe.pdf');w.write(p);print('Merged',len(w.pages),'pages',round(p.stat().st_size/1048576,2),'MB')

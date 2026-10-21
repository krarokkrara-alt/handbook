"""Map printed headings to actual PDF pages; create contents and PDF bookmarks."""
from pathlib import Path
import json,re,html,hashlib
import pypdfium2 as pdfium
from pypdf import PdfReader,PdfWriter
from reportlab.pdfgen import canvas
from io import BytesIO
P=Path(__file__).resolve().parents[1];O=P/'production'
def norm(s):return re.sub(r'\s+','',s).replace('**','')
def prepare():
 pdf=pdfium.PdfDocument(O/'P0093_Prototype.pdf')
 texts=[norm(p.get_textpage().get_text_range()) for p in pdf]
 reader=PdfReader(O/'P0093_Prototype.pdf')
 destinations={}
 def walk(items):
  for item in items:
   if isinstance(item,list):walk(item)
   else:destinations[norm(item.title)]=reader.get_destination_page_number(item)+1
 walk(reader.outline)
 manifest=json.loads((P/'circuits/print_manifest.json').read_text(encoding='utf8'))
 entries=[]
 for d in manifest['diagrams']:
  entries.append({'label':'ภาพ '+d['id']+' '+d['title_th'],'page':int(d['id'])+1,'kind':'plate'})
 for line in (P/'manuscript/MASTER_DRAFT.md').read_text(encoding='utf8').splitlines():
  if not line.startswith('## '):continue
  title=line[3:]
  if title.startswith(('วงจรการทำงาน','ภาคหนึ่ง')):continue
  hits=[destinations[norm(title)]] if norm(title) in destinations else [i+1 for i,t in enumerate(texts) if norm(title) in t]
  if not hits:raise ValueError('Heading not located: '+title)
  entries.append({'label':title,'page':hits[0],'kind':'section'})
 for e in entries:e['final_page']=e['page']+1
 (O/'navigation_map.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2),encoding='utf8')
 rows=''.join('<tr><td>'+html.escape(e['label'])+'</td><td>'+str(e['final_page'])+'</td></tr>' for e in entries)
 (O/'contents.html').write_text('<!doctype html><meta charset="utf-8"><style>@page{size:A4;margin:16mm 18mm}body{font-family:"Leelawadee UI",Tahoma;font-size:10.5pt;color:black}h1{font-size:23pt;margin:0 0 4mm}p{line-height:1.4}table{width:100%;border-collapse:collapse}td{padding:1.5mm 0;border-bottom:1px solid #ddd}td:last-child{text-align:right;width:13mm}small{font-size:9pt}</style><h1>สารบัญ</h1><p>เริ่มจากภาพรวมทางน้ำมัน แล้วตามวงจรควบคุมไปสู่การแยกสาเหตุ การซ่อม และการยืนยันผล เลขหน้าอ้างฉบับ PDF นี้</p><table>'+rows+'</table><p><small>ภาพหลักการใช้เรียนรู้หน้าที่ ส่วนเลขขาและค่าทดสอบเฉพาะเอกสารต้องตรวจรุ่น ตลาด และชุดอุปกรณ์ก่อนใช้กับรถจริง เคส A–H เป็นกรณีจำลอง</small></p>',encoding='utf8')
 print('Contents entries',len(entries))
def merge():
 base=PdfReader(O/'P0093_Prototype.pdf');toc=PdfReader(O/'contents.pdf')
 assert len(toc.pages)==1,'Contents must fit one page'
 w=PdfWriter();w.add_page(base.pages[0]);w.add_page(toc.pages[0])
 for p in base.pages[1:]:w.add_page(p)
 for index,page in enumerate(w.pages):
  width,height=float(page.mediabox.width),float(page.mediabox.height)
  overlay=BytesIO();c=canvas.Canvas(overlay,pagesize=(width,height))
  c.setFillColorRGB(1,1,1);c.rect(0,0,width,27,fill=1,stroke=0)
  c.setFillColorRGB(.3,.3,.3);c.setFont('Helvetica',8)
  c.drawCentredString(width/2,12,f'P0093 | BOOK | {index+1} / {len(w.pages)}')
  c.save();overlay.seek(0);page.merge_page(PdfReader(overlay).pages[0])
 entries=json.loads((O/'navigation_map.json').read_text(encoding='utf8'))
 w.add_outline_item('สารบัญ',1)
 for e in entries:w.add_outline_item(e['label'],e['final_page']-1)
 # Bookmarks provide navigation; the printed contents rows are plain text.
 w.add_metadata({'/Title':'P0093 Toyota 1KD และ 2KD วงจรและการวินิจฉัย','/Author':'กองบรรณาธิการโครงการ'})
 target=O/'P0093_ReadingProof.pdf'
 with target.open('wb') as f:w.write(f)
 print('Reading proof pages',len(w.pages),'SHA256',hashlib.sha256(target.read_bytes()).hexdigest())
if __name__=='__main__':
 import sys
 merge() if '--merge' in sys.argv else prepare()

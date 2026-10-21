"""Create a short course companion from reviewed plates/forms and original learning guide."""
from pathlib import Path
import re,json,html,hashlib
from io import BytesIO
from pypdf import PdfReader,PdfWriter
from reportlab.pdfgen import canvas
P=Path(__file__).resolve().parents[1];O=P/'production'
def inline(s):
 s=html.escape(s)
 s=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',s)
 return s
def prepare():
 source=(P/'manuscript/COURSE_GUIDE.md').read_text(encoding='utf8')
 parts=source.split('<!-- pagebreak -->');assert len(parts)==2
 sections=[]
 for part in parts:
  body=[];table=[]
  def flush_table():
   if not table:return
   rows=[[c.strip() for c in line.strip('|').split('|')] for line in table if not re.match(r'^\|?\s*:?-{2,}',line)]
   body.append('<table>'+''.join('<tr>'+''.join(('<th>' if i==0 else '<td>')+inline(c)+('</th>' if i==0 else '</td>') for c in row)+'</tr>' for i,row in enumerate(rows))+'</table>');table.clear()
  for text in part.splitlines():
   text=text.strip()
   if not text:continue
   if text.startswith('|'):table.append(text);continue
   flush_table()
   m=re.match(r'^(#{1,4})\s+(.*)',text)
   if m:body.append('<h'+str(len(m[1]))+'>'+inline(m[2])+'</h'+str(len(m[1]))+'>')
   elif text.startswith('>'):body.append('<blockquote>'+inline(text.lstrip('> '))+'</blockquote>')
   else:body.append('<p'+(' class="highlight"' if text.startswith('**ไฮไลต์') else '')+'>'+inline(text)+'</p>')
  flush_table()
  sections.append('<section>'+''.join(body)+'</section>')
 registry=json.loads((P/'research/claim_ledger.json').read_text(encoding='utf8'))['source_registry']
 refs=(P/'research/READER_REFERENCES.md').read_text(encoding='utf8')
 names={}
 for m in re.finditer(r'^### ([A-Z]\d+(?: / [A-Z]\d+)*) — (.+)$',refs,re.M):
  for key in m[1].split(' / '):names[key]=m[2]
 rows=''.join('<tr><td>'+key+'</td><td><a href="'+html.escape(url)+'">'+inline(names.get(key,key))+'</a></td></tr>' for key,url in registry.items())
 sections.append('<section><h1>แหล่งอ้างอิงสำหรับคอร์ส</h1><p>เอกสารย่อนี้ใช้ร่วมกับหนังสือ P0093 Toyota 1KD และ 2KD ฉบับเต็ม ชื่อเครื่องยนต์อย่างเดียวไม่ยืนยันว่าเลขขา ค่าตรวจ หรือวิธีซ่อมใช้กับรถคันนั้นได้ เปิดแหล่งด้านล่างเพื่อตรวจขอบเขตรุ่นเอกสารและตลาด</p><table>'+rows+'</table><blockquote>ห้ามคลายท่อ common rail ขณะเครื่องทำงาน ห้ามปิดระบบป้องกันหรืออุดทางระบาย การเปิดระบบต้องทำตามวิธีลดแรงดันตกค้างของคู่มือตรงรถ</blockquote><p>เคส A–H ในเล่มเต็มเป็นกรณีจำลอง ภาพวงจรเป็นภาพวาดใหม่ ภาพ 11–12 ที่ไม่ได้คัดมาในเอกสารย่อเป็นตัวอย่างต่อสายเฉพาะ DR201E ไม่ใช่เลขขาสากล</p><p>ภาพอุปกรณ์จริงยังไม่มีชุดที่ผ่านสิทธิ์ฝังและยืนยันตรง application เอกสารนี้จึงไม่แสดงภาพวาดว่าเป็นภาพถ่ายจริง รายละเอียดข้อจำกัดและแหล่งเพิ่มเติมอยู่ในเล่มเต็ม</p></section>')
 css='@page{size:A4;margin:17mm 18mm 19mm}body{font-family:"Leelawadee UI",Tahoma;color:#000;font-size:11pt;line-height:1.36;margin:0}section{break-after:page}section:last-child{break-after:auto}h1{font-size:23pt;margin:0 0 5mm}h2{font-size:17pt;margin:5mm 0 3mm}h3,h4{font-size:13pt;margin:4mm 0 2mm}h1,h2,h3,h4{break-after:avoid}p{margin:0 0 3mm;orphans:3;widows:3}blockquote{background:#fff2cc;padding:3mm;margin:3mm 0;break-inside:avoid}table{border-collapse:collapse;width:100%;font-size:10pt}td{padding:1.5mm;border-bottom:1px solid #ddd}a{color:#155889}'
 css+=' .highlight{background:#fff2cc;padding:1.5mm;margin:1mm 0}th{background:#eee;text-align:left;padding:1.5mm;border:1px solid #ccc}td{vertical-align:top}tr{break-inside:avoid}'
 (O/'course_guide.html').write_text('<!doctype html><meta charset="utf-8"><style>'+css+'</style>'+''.join(sections),encoding='utf8')
def merge():
 base=PdfReader(O/'P0093_Prototype.pdf');guide=PdfReader(O/'course_guide.pdf')
 assert len(guide.pages)==3,'Guide must be exactly 2 teaching pages and 1 reference page'
 destinations={}
 def walk(items):
  for item in items:
   if isinstance(item,list):walk(item)
   else:destinations[item.title]=base.get_destination_page_number(item)
 walk(base.outline)
 w=PdfWriter();mapping=[]
 for i in range(2):w.add_page(guide.pages[i])
 for number in [1,2,3,4,5,16]:
  page=number # Base cover page is index 0, plates start at index 1.
  w.add_page(base.pages[page]);mapping.append({'label':'ภาพ '+str(number).zfill(2),'base_page':page+1,'course_page':len(w.pages)})
 for number in range(1,7):
  matches=[(title,index) for title,index in destinations.items() if title.startswith('แบบ'+str(number).zfill(2))]
  assert len(matches)==1,matches
  title,index=matches[0];w.add_page(base.pages[index]);mapping.append({'label':title,'base_page':index+1,'course_page':len(w.pages)})
 w.add_page(guide.pages[2]);assert len(w.pages)==15
 for i,page in enumerate(w.pages):
  width,height=float(page.mediabox.width),float(page.mediabox.height)
  stream=BytesIO();c=canvas.Canvas(stream,pagesize=(width,height));c.setFont('Helvetica',8);c.setFillColorRGB(.3,.3,.3)
  c.drawCentredString(width/2,12,f'P0093 | COURSE | {i+1} / {len(w.pages)}');c.save();stream.seek(0)
  page.merge_page(PdfReader(stream).pages[0])
 w.add_outline_item('แนวทางเรียน',0);w.add_outline_item('กิจกรรมฝึก',1)
 for item in mapping:w.add_outline_item(item['label'],item['course_page']-1)
 w.add_outline_item('แหล่งอ้างอิง',14)
 target=O/'P0093_CourseProof.pdf'
 with target.open('wb') as f:w.write(f)
 (O/'course_page_map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2),encoding='utf8')
 print('Course pages',len(w.pages),'SHA256',hashlib.sha256(target.read_bytes()).hexdigest())
if __name__=='__main__':
 import sys
 merge() if '--merge' in sys.argv else prepare()

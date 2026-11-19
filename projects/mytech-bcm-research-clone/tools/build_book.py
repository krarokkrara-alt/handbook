"""Build the Thai BCM handbook offline from checked-in text and images."""
from pathlib import Path
import re, json, os, unicodedata, hashlib
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader, PdfWriter

ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'assets'; BOOKS=ROOT/'books'; BOOKS.mkdir(exist_ok=True)
REG=os.environ.get('MYTECH_FONT_REGULAR',r'C:\Windows\Fonts\tahoma.ttf')
BOLD=os.environ.get('MYTECH_FONT_BOLD',r'C:\Windows\Fonts\tahomabd.ttf')
pdfmetrics.registerFont(TTFont('Thai',REG));pdfmetrics.registerFont(TTFont('ThaiB',BOLD))

def diagram(name,title,kind):
    im=Image.new('RGB',(1600,900),'white');d=ImageDraw.Draw(im)
    f=ImageFont.truetype(REG,28); small=ImageFont.truetype(REG,23);big=ImageFont.truetype(BOLD,38)
    ink='#173b4b';teal='#007d87';gold='#94621c'
    d.text((55,35),title,font=big,fill=ink)
    def box(x,y,w,h,label):
        d.rounded_rectangle((x,y,x+w,y+h),radius=12,fill='#eef5f6',outline=ink,width=3)
        for j,s in enumerate(label.split('\n')):d.text((x+18,y+20+j*38),s,font=f,fill=ink)
    def line(a,b,label=''):
        d.line((a,b),fill=teal,width=4)
        if label:d.text(((a[0]+b[0])//2,(a[1]+b[1])//2-35),label,font=small,fill=gold)
    if kind=='can':
        box(70,240,280,330,'MCU\nTX output\nRX input\nSTB control')
        box(550,200,470,430,'TCAN1042V-Q1\n1 TXD     8 STB\n2 GND     7 CANH\n3 VCC     6 CANL\n4 RXD     5 VIO')
        line((350,310),(550,310),'TXD');line((350,410),(550,410),'RXD');line((350,510),(550,510),'STB')
        line((1020,330),(1480,330),'CANH');line((1020,470),(1480,470),'CANL')
        d.text((1080,600),'VCC = 5 V supply',font=f,fill=ink)
        d.text((1080,645),'VIO is a supply INPUT',font=f,fill=ink)
        d.text((70,730),'Signal map only. Protection, decoupling and termination omitted.',font=f,fill=ink)
        d.text((70,775),'VIO must match supported MCU logic voltage. Base pin 5 = NC.',font=f,fill=ink)
    elif kind=='lin':
        box(65,240,300,350,'MCU\nRX input\nTX output\nSleep control')
        box(570,180,440,470,'TJA1021 SO8\n1 RXD       8 INH\n2 SLP_N   7 VBAT\n3 WAKE_N  6 LIN\n4 TXD       5 GND')
        line((365,310),(570,310),'RXD');line((365,430),(570,430),'TXD');line((365,550),(570,550),'SLP_N')
        line((1010,420),(1490,420),'LIN BUS');line((1010,290),(1460,290),'INH -> regulator')
        d.text((70,730),'RXD is open-drain: use the pull-up specified for the logic interface.',font=f,fill=ink)
        d.text((70,775),'Commander pull-up/diode and local-wake network are not shown.',font=f,fill=ink)
    elif kind=='spi':
        box(70,230,300,370,'Programmer\nSelect exact device\nCheck VCC + logic\nRead first')
        box(600,200,440,430,'M95640-A125/A145\nSO8\n1 S#       8 VCC\n2 Q         7 HOLD#\n3 W#       6 C\n4 VSS      5 D')
        for y,label in [(295,'CS -> S#'),(385,'MISO <- Q'),(475,'SCK -> C'),(565,'MOSI -> D')]:line((370,y),(600,y),label)
        d.text((1100,310),'64 Kbit',font=big,fill=teal);d.text((1100,370),'8192 bytes',font=f,fill=ink)
        d.text((1100,450),'Main array only',font=f,fill=ink)
        d.text((70,730),'Conceptual signal map, not an in-circuit connection guide.',font=f,fill=ink)
        d.text((70,775),'Check package, write protection and identification page separately.',font=f,fill=ink)
    elif kind=='power':
        labels=['BATTERY\nConfirmed pins','Protection\n+ filter','Pre-boost\nif fitted','Buck / LDO\nregulated rails']
        for i,l in enumerate(labels):
            box(50+i*390,200,320,170,l)
            if i<3:line((370+i*390,285),(440+i*390,285))
        for i,l in enumerate(['A: input under load','B: voltage drop','C: enable + switch','D: rail + reset']):d.text((50+i*390,440),l,font=small,fill=ink)
        d.text((65,610),'Measure input and output in the same operating state.',font=f,fill=ink)
        d.text((65,675),'A low rail can be caused by the regulator OR a downstream load.',font=f,fill=ink)
        d.text((65,750),'Functional redraw based on TI BCM reference designs; not vehicle pinout.',font=f,fill=ink)
    elif kind=='transfer':
        for i,l in enumerate(['IDENTIFY\nModule + chip','BACK UP\nRepeat + compare','CHECK\nCompatibility','TRANSFER\nApproved region']):
            box(50+i*390,200,320,170,l)
            if i<3:line((370+i*390,285),(440+i*390,285))
        box(300,500,1000,160,'READ BACK -> VEHICLE SETUP -> FUNCTION TEST\nChip verify does not prove complete vehicle operation')
    if kind in ('can','lin','spi'):d.text((70,835),'Lines show signal relationships, NOT physical pin positions.',font=small,fill=gold)
    im.save(ASSETS/(name+'.png'))

for args in [('power-map','Power circuit diagnosis','power'),('can-map','CAN transceiver signal map','can'),('lin-map','LIN transceiver signal map','lin'),('spi-map','SPI EEPROM signal map','spi'),('transfer-map','Chip and data transfer workflow','transfer')]:diagram(*args)

W,H=595.28,841.89
manuscript=(ROOT/'manuscript.md').read_text(encoding='utf-8')
if (ROOT/'supplement-v2.md').exists():manuscript+='\n'+(ROOT/'supplement-v2.md').read_text(encoding='utf-8')
TOC_PAGES=(sum(1 for l in manuscript.splitlines() if l.startswith('## '))+3+23)//24
def physical(p):return p if p==1 else p+4 if p==2 else p+4+TOC_PAGES
c=canvas.Canvas(str(BOOKS/'BCM-MyTech-body.pdf'),pagesize=(W,H));c.setAuthor('MyTech | Supunya Pharaphong');c.setTitle('BCM วงจรบอร์ด การย้ายชิป และการย้ายข้อมูล')
page=0;y=0;pages=[];toc=[];bounds=[]
def newpage(title='BCM | MyTech'):
    global page,y
    if page:c.showPage()
    page+=1;y=770;pages.append({'page':page,'title':title})
    c.setFillColor(HexColor('#007d87'));c.rect(36,796,523,3,fill=1,stroke=0)
    c.setFont('Thai',8);c.setFillColor(HexColor('#325765'));c.drawString(36,808,'BCM | วงจรบอร์ด การย้ายชิป และการย้ายข้อมูล')
    c.drawRightString(559,808,'แจกฟรี | แต่งโดย MyTech')
    c.setFont('Thai',8);c.drawString(36,27,'ฉบับขยายวงจรและโปรแกรม | 17 พฤศจิกายน 2569');c.drawRightString(559,27,str(physical(page)))
def clusters(s):
    out=[]
    for ch in s:
        if out and (unicodedata.combining(ch) or ch in '\u0e31\u0e34\u0e35\u0e36\u0e37\u0e38\u0e39\u0e47\u0e48\u0e49\u0e4a\u0e4b\u0e4c\u0e4d\u0e4e'):out[-1]+=ch
        else:out.append(ch)
    return out
def wrap(s,font,size,width):
    out=[];cur=''
    for token in clusters(s):
        if cur and pdfmetrics.stringWidth(cur+token,font,size)>width:
            # Prefer a recent word boundary, otherwise preserve Thai grapheme clusters.
            k=cur.rfind(' ')
            if k>len(cur)*.65:out.append(cur[:k]);cur=cur[k+1:]+token
            else:out.append(cur);cur=token
        else:cur+=token
    if cur:out.append(cur)
    return out
def text(s,size=10.5,bold=False,indent=0):
    global y
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1 (\2)',s).replace('**','').replace('`','')
    font='ThaiB' if bold else 'Thai';leading=size*1.5
    for ln in wrap(s,font,size,523-indent):
        if y-leading<55:newpage()
        c.setFont(font,size);c.setFillColor(HexColor('#172c36'));c.drawString(36+indent,y,ln)
        bounds.append({'page':page,'y':round(y,1),'right':round(36+indent+pdfmetrics.stringWidth(ln,font,size),1)})
        y-=leading
    y-=7
def picture(path,caption,maxheight=330):
    global y
    im=Image.open(path);iw,ih=im.size;dh=min(maxheight,523*ih/iw);dw=dh*iw/ih
    if y-dh-80<55:newpage()
    c.drawImage(str(path),36+(523-dw)/2,y-dh,width=dw,height=dh,mask='auto');y-=dh+17
    text(caption,9)
def heading(s):
    global y
    newpage(s);toc.append((s,page));text(s,17,True);y-=8

def table(rows):
    global y
    if not rows:return
    n=len(rows[0]);widths=([130,393] if n==2 else [120,190,213] if n==3 else [85,130,158,150] if n==4 else [523/n]*n)
    header=rows[0]
    def row(cells,isheader=False):
        global y
        font='ThaiB' if isheader else 'Thai';fs=8.5;lead=13
        wrapped=[wrap(re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',v).replace('**',''),font,fs,w-14) for v,w in zip(cells,widths)]
        h=max(len(ls) for ls in wrapped)*lead+16
        if y-h<55:
            newpage()
            if not isheader:row(header,True)
        x=36
        for w,ls in zip(widths,wrapped):
            c.setFillColor(HexColor('#deedf0' if isheader else '#ffffff'));c.setStrokeColor(HexColor('#c9d8de'));c.rect(x,y-h,w,h,fill=1,stroke=1)
            c.setFillColor(HexColor('#172c36'));c.setFont(font,fs)
            for j,l in enumerate(ls):c.drawString(x+7,y-12-j*lead,l)
            x+=w
        y-=h
    for i,r in enumerate(rows):row(r,i==0)
    y-=14

# Full bleed cover is a designed illustration, not documentary evidence.
_toc_titles=[l[3:].split(':')[0] for l in manuscript.splitlines() if l.startswith('## ') and not l[3:].startswith('ทะเบียนภาพ')]+['ภาพถ่ายบอร์ดและขอบเขตการใช้หลักฐาน','แบบบันทึกงานสำหรับใช้งานจริง']
TOC_PAGES=1;_ty=740
for _title in _toc_titles:
    if _ty<80:TOC_PAGES+=1;_ty=740
    _ty-=18*len(wrap(_title,'Thai',10,465))+10
newpage('ปก');c.drawImage(str(ASSETS/'cover.png'),0,0,width=W,height=H)
heading('อ่านหนังสือเล่มนี้อย่างไร')
text('หนังสือ BCM สำหรับช่างที่ต้องการอ่านวงจรภายในบอร์ด แยกภาคเสีย และจัดการงานย้ายชิปหรือข้อมูลอย่างมีหลักฐาน ครอบคลุมกรณีญี่ปุ่น ยุโรป และอเมริกาตามเอกสารที่ตรวจพบ เน้นลำดับตรวจที่ทำซ้ำได้และการบันทึกผลให้คนอื่นรับช่วงงานได้')
text('ข้อมูลผู้แต่งและกิตติกรรมประกาศเดิมอยู่หลังปกหน้า 2-5 ข้อความขอบคุณในเอกสารเดิมไม่ใช้ยืนยันว่า Claude หรือบุคคลที่กล่าวถึงได้ตรวจหนังสือ BCM ฉบับนี้ ภาพปกเป็นภาพประกอบสร้างด้วย AI')
text('ค่าจุดวัด ขาปลั๊ก แรงดันเขียน และจุดต่อเครื่องโปรแกรมต้องตรงกับหมายเลขกล่อง ชิป และ package จริง ภาพวาดในเล่มแสดงความสัมพันธ์ของสัญญาณหรือกระบวนการ ไม่ใช้แทนคู่มือเชื่อมต่อเฉพาะกล่อง')
text('คำว่า รองรับการอ่านเขียน หมายถึงรายการความสามารถในเอกสารที่อ้าง ไม่เท่ากับ full clone หรือการทำงานสมบูรณ์บนรถ การตรวจ read-back และ verify เป็นเพียงส่วนหนึ่งของการตรวจหลังงาน')
text('วิธีใช้: อ่านบท 1-7 เพื่อวางแผนตรวจบอร์ด ต่อด้วยบท 8-10 เมื่อมีเหตุผลต้องย้ายชิปหรือข้อมูล ใช้บท 11-14 ตรวจเอกสารกรณีและเครื่องมือ แล้วกรอกใบงานบท 15 ก่อนส่งงาน')
picture(ASSETS/'transfer-map.png','ภาพวาดอธิบายลำดับงานของผู้เรียบเรียง ไม่ใช่เมนูของเครื่องมือรุ่นใด')

visuals={3:('power-map','ภาพวาดหน้าที่จาก TI TIDA-00745 ต้องตรวจวงจรและรุ่นจริงก่อนใช้'),6:('can-map','ผังสัญญาณวาดใหม่ อ้าง TI TCAN1042-Q1 Rev D หน้า 5; แสดงรุ่น V ที่มี VIO'),7:('spi-map','ผังสัญญาณวาดใหม่ อ้าง ST M95640 DS8799; ไม่ใช่จุดต่ออ่านในวงจร'),10:('transfer-map','ภาพวาดอธิบายกระบวนการ ไม่รับรองความเข้ากันได้ของกล่อง')}
skip=False;in_table=False
table_rows=[]
for ln in manuscript.splitlines():
    ln=ln.strip()
    if ln.startswith('|'):
        cells=[x.strip() for x in ln.strip('|').split('|')]
        if not all(re.fullmatch(r'[-: ]+',x) for x in cells):table_rows.append(cells)
        continue
    if table_rows:table(table_rows);table_rows=[]
    if ln.startswith('# '):continue
    if ln.startswith('## '):
        title=ln[3:];skip=title.startswith('ทะเบียนภาพ')
        if skip:continue
        heading(title)
        match=re.search(r'บท(?:ที่)?\s*(\d+)',title)
        n=int(match.group(1)) if match else 0
        if n in visuals:
            name,cap=visuals[n];picture(ASSETS/(name+'.png'),cap,270)
        if n==6:picture(ASSETS/'lin-map.png','ผังสัญญาณวาดใหม่ อ้าง NXP TJA1021 Rev 9 หน้า 4; ไม่ใช่วงจร application ครบชุด',270)
        continue
    if skip or not ln:continue
    if ln.startswith('!['):
        m=re.match(r'!\[([^]]*)\]\(([^)]+)\)',ln)
        if m and (ROOT/m.group(2)).exists():picture(ROOT/m.group(2),m.group(1),420)
        continue
    if ln.startswith('### '):
        if y<130:newpage()
        text(ln[4:],12,True);continue
    if ln.startswith('|'):
        cells=[x.strip() for x in ln.strip('|').split('|')]
        if all(re.fullmatch(r'[-: ]+',x) for x in cells):continue
        text(' | '.join(cells),9.5,indent=8);continue
    text(ln)
if table_rows:table(table_rows)

heading('ภาพถ่ายบอร์ดและขอบเขตการใช้หลักฐาน')
vfile=ROOT/'VISUAL_SOURCES.md'
if vfile.exists():
    for ln in vfile.read_text(encoding='utf-8').splitlines():
        if ln.startswith('!['):
            m=re.match(r'!\[([^]]*)\]\(([^)]+)\)',ln)
            if m and (ROOT/m.group(2)).exists():picture(ROOT/m.group(2),m.group(1))
        elif ln and not ln.startswith('#'):
            if ln.startswith('cover.png'):ln='cover.png เป็นภาพปกสร้างด้วย AI ใช้แสดงแนวคิด BCM หลายรูปแบบ ไม่ยืนยันรุ่นรถจริง'
            text(ln,9.5)
else:text('ภาพถ่ายบอร์ดอยู่ระหว่างตรวจแหล่งต้นทาง ภาพวาดในบทวงจรใช้แทนคำอธิบายหน้าที่ได้ แต่ไม่ยืนยันตำแหน่งอุปกรณ์บน BCM รถแต่ละรุ่น')

heading('แบบบันทึกงานสำหรับใช้งานจริง')
for label in ['เลขงาน / วันที่ / ผู้ปฏิบัติงาน','รุ่นรถ / รุ่นปี / อาการที่ยืนยัน','หมายเลขกล่อง / HW / SW / PCB','รหัส MCU / EEPROM / package','เอกสารขาปลั๊กและวงจรที่ใช้','สภาวะวัด / จุดอ้างอิงกราวด์','เครื่องมือ / เวอร์ชัน / อะแดปเตอร์','ไฟล์ต้นฉบับ / ขนาด / SHA-256','ผลอ่านซ้ำ / การเปรียบเทียบ','งานที่ทำ / ชิ้นส่วนหรือพื้นที่ข้อมูล','ผลอ่านกลับ / verify / รูปหลังบัดกรี','ผลทดสอบบนรถ / ฟังก์ชันที่ยังไม่ได้ทดสอบ']:
    text(label,10.5,True);text('........................................................................................................................',10)
c.save()
body=PdfReader(BOOKS/'BCM-MyTech-body.pdf')
tc=canvas.Canvas(str(BOOKS/'toc.pdf'),pagesize=(W,H));tc.setFont('ThaiB',21);tc.drawString(36,780,'สารบัญ');ty=740
for title,p in toc:
    if title=='อ่านหนังสือเล่มนี้อย่างไร':continue
    if ty<80:tc.showPage();tc.setFont('ThaiB',21);tc.drawString(36,780,'สารบัญ ต่อ');ty=740
    title=title.split(':')[0]
    tc.setFont('Thai',10)
    for l in wrap(title,'Thai',10,465):tc.drawString(36,ty,l);ty-=18
    tc.drawRightString(555,ty+18,str(physical(p)));ty-=10
tc.setFont('Thai',8);tc.drawString(36,35,'PDF มี bookmarks สำหรับเปิดแต่ละบท | เลขหน้าอ้างอิงลำดับหน้า PDF');tc.save()
tocpdf=PdfReader(BOOKS/'toc.pdf')
assert len(tocpdf.pages)==TOC_PAGES,(len(tocpdf.pages),TOC_PAGES)
writer=PdfWriter();writer.append(body,pages=(0,1))
author=PdfReader(ROOT/'source-documents/Author_and_Acknowledgements.pdf');writer.append(author)
writer.append(body,pages=(1,2));writer.append(tocpdf);writer.append(body,pages=(2,len(body.pages)))
writer.add_outline_item('เกี่ยวกับผู้แต่งและกิตติกรรมประกาศเดิม',1);writer.add_outline_item('สารบัญ',6)
for title,p in toc:writer.add_outline_item(title,physical(p)-1)
writer.add_metadata({'/Title':'BCM วงจรบอร์ด การย้ายชิป และการย้ายข้อมูล','/Author':'MyTech | Supunya Pharaphong'})
with open(BOOKS/'BCM-MyTech-Handbook.pdf','wb') as f:writer.write(f)
(BOOKS/'BCM-MyTech-body.pdf').unlink()
(BOOKS/'toc.pdf').unlink()
(ROOT/'BUILD_REPORT.json').write_text(json.dumps({'edition':2,'body_pages':len(body.pages),'author_pages':len(author.pages),'author_location':[2,5],'toc_pages':TOC_PAGES,'total_pages':len(writer.pages),'chapters':[(t,physical(p)) for t,p in toc],'out_of_bounds':[x for x in bounds if x['y']<50 or x['right']>560]},ensure_ascii=False,indent=2),encoding='utf-8')
print('Built',len(writer.pages),'pages; bounds issues:',len([x for x in bounds if x['y']<50 or x['right']>560]))

# Editable offline HTML: original source is manuscript.md.
def inline(s):
    s=escape(s)
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
    return s
html=['<!doctype html><html lang="th"><meta charset="utf-8"><title>BCM แต่งโดย MyTech</title>',
      '<style>body{font:18px/1.8 Tahoma,sans-serif;color:#172c36;max-width:900px;margin:32px auto;padding:0 24px}h1,h2{line-height:1.5}h2{margin-top:60px;border-bottom:2px solid #007d87}img{max-width:100%;max-height:800px;display:block;margin:24px auto}table{border-collapse:collapse;font-size:15px}td,th{border:1px solid #ccc;padding:10px}a{overflow-wrap:anywhere}figure{break-inside:avoid}figcaption{font-size:14px}@media print{body{font-size:11pt;max-width:none}h2{break-before:page}img{max-height:210mm}} </style>',
      '<body><img src="../assets/cover.png" alt="ปกหนังสือ BCM"><h1>BCM วงจรบอร์ด การย้ายชิป และการย้ายข้อมูล</h1><p>แจกฟรี | แต่งโดย MyTech | Supunya Pharaphong</p>',
      '<p>ฉบับอ้างอิงงานช่าง ไม่มีผลทดสอบโคลนสำเร็จของรถทุกกรณี ภาพปกเป็นภาพสร้าง ส่วนภาพบอร์ดจริงระบุเจ้าของภาพแยกไว้</p>']
authorhtml='<h2>เกี่ยวกับผู้แต่งและกิตติกรรมประกาศเดิม</h2><p>ข้อความเดิมไม่ใช่การรับรองผลตรวจหนังสือ BCM ฉบับนี้</p>'+''.join('<img src="../assets/author/'+p.name+'" alt="เอกสารผู้แต่งเดิม">' for p in sorted((ASSETS/'author').glob('page-*.png')))
html=[s.replace('<h1>',authorhtml+'<h1>',1) if 'assets/cover.png' in s else s for s in html]
htmltable=[]
def flushhtml():
    if not htmltable:return
    html.append('<table>')
    for i,r in enumerate(htmltable):
        tag='th' if i==0 else 'td';html.append('<tr>'+''.join('<'+tag+'>'+inline(v)+'</'+tag+'>' for v in r)+'</tr>')
    html.append('</table>');htmltable.clear()
for ln in manuscript.splitlines():
    ln=ln.strip()
    if ln.startswith('|'):
        cells=[x.strip() for x in ln.strip('|').split('|')]
        if not all(re.fullmatch(r'[-: ]+',x) for x in cells):htmltable.append(cells)
        continue
    flushhtml()
    if not ln or ln.startswith('# '):continue
    if ln.startswith('## '):
        html.append('<h2>'+inline(ln[3:])+'</h2>')
        match=re.search(r'บท(?:ที่)?\s*(\d+)',ln)
        n=int(match.group(1)) if match else 0
        if n in visuals:html.append('<figure><img src="../assets/'+visuals[n][0]+'.png"><figcaption>'+inline(visuals[n][1])+'</figcaption></figure>')
        if n==6:html.append('<figure><img src="../assets/lin-map.png"><figcaption>ผังสัญญาณ TJA1021 SO8 ไม่ใช่ตำแหน่งต่อเครื่องมือจริง</figcaption></figure>')
    elif ln.startswith('!['):
        m=re.match(r'!\[([^]]*)\]\(([^)]+)\)',ln)
        if m:html.append('<figure><img src="../'+m.group(2)+'"><figcaption>'+inline(m.group(1))+'</figcaption></figure>')
    else:html.append('<p>'+inline(ln)+'</p>')
html.append('<h2>ภาพถ่ายบอร์ดและแหล่งที่มา</h2>')
for ln in vfile.read_text(encoding='utf-8').splitlines():
    if ln.startswith('!['):
        m=re.match(r'!\[([^]]*)\]\(([^)]+)\)',ln)
        if m:html.append('<figure><img src="../'+m.group(2)+'"><figcaption>'+inline(m.group(1))+'</figcaption></figure>')
    elif ln.startswith('## '):html.append('<h3>'+inline(ln[3:])+'</h3>')
    elif ln and not ln.startswith('#'):html.append('<p>'+inline(ln)+'</p>')
html.append('</body></html>');(BOOKS/'BCM-MyTech-Handbook.html').write_text('\n'.join(html),encoding='utf-8')

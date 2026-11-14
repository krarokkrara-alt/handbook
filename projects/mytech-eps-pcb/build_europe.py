from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from PIL import Image
from pathlib import Path
import os
import json
pdfmetrics.registerFont(TTFont('T',os.environ.get('MYTECH_FONT_REGULAR',r'C:\Windows\Fonts\tahoma.ttf')))
pdfmetrics.registerFont(TTFont('B',os.environ.get('MYTECH_FONT_BOLD',r'C:\Windows\Fonts\tahomabd.ttf')))
OUT=Path('tmp/pdfs/mytech-europe-pages.pdf');OUT.parent.mkdir(exist_ok=True,parents=True)
c=canvas.Canvas(str(OUT),pagesize=(595.28,841.89));c.setTitle('คู่มือซ่อมพวงมาลัยไฟฟ้า by mytech');c.setAuthor('mytech')
P=0;log=[];overflow=[]
NAVY='#153b4b';TEAL='#007d87';AMBER='#9a5700'
def t(x,y,s,size=10.5,b=False,color=NAVY):
 c.setFillColor(HexColor(color));c.setFont('B' if b else 'T',size);c.drawString(x,y,s)
 if x+pdfmetrics.stringWidth(s,'B' if b else 'T',size)>565:overflow.append((P,s))
def line(x,y,x2,y2,color='#53717f',w=1):c.setStrokeColor(HexColor(color));c.setLineWidth(w);c.line(x,y,x2,y2)
def start(title,ref='แนวทางงานช่างทั่วไป + ผังอ้างอิง HF 2012; ตรวจรุ่นก่อนใช้'):
 global P
 if P:c.showPage()
 P+=1;title=__import__('re').sub(r'^\d+\s*\|\s*','',title);log.append((P,title));c.setFillColor(HexColor(NAVY));c.rect(0,756,596,86,fill=1,stroke=0)
 t(34,808,'พวงมาลัยไฟฟ้า | by mytech',17,True,'#ffffff');t(34,778,title,13,True,'#ffffff')
 t(34,735,ref,8.1,False,AMBER);line(34,44,562,44);t(34,27,'ฉบับ PCB 14 พ.ย. 2026 | แยกภาพจริง / วงจรตัวอย่าง | ตรวจรุ่นก่อนซ่อม',7.5);t(544,27,f'{(1 if P==1 else P+41):02}',9,True)
def para(y,ss,size=10.5,gap=20,x=36):
 for s in ss:t(x,y,s,size);y-=gap
 return y
def title(y,s):t(36,y,s,12,True,TEAL);return y-25
def panel(y,heading,ss):
 h=40+len(ss)*20;c.setFillColor(HexColor('#edf5f6'));c.roundRect(34,y-h+14,528,h,7,fill=1,stroke=0)
 t(46,y,heading,11,True,TEAL);para(y-25,ss,10,20,46);return y-h-14
def table(y,rows,widths,fs=9.3,rh=32):
 for j,row in enumerate(rows):
  x=35
  for val,w in zip(row,widths):
   c.setFillColor(HexColor('#e9f1f4' if j==0 else '#ffffff'));c.setStrokeColor(HexColor('#c9d8de'));c.rect(x,y-rh,w,rh,fill=1,stroke=1);t(x+6,y-rh/2-4,val,fs,j==0);x+=w
  y-=rh
 return y

def photo(path,x,y,w,h,crop=None):
 im=Image.open(path);iw,ih=im.size
 if crop:
  l,u,r,b=crop;cw=(r-l)*iw;ch=(b-u)*ih;scale=min(w/cw,h/ch)
  dw,dh=cw*scale,ch*scale;ox=x+(w-dw)/2;oy=y+(h-dh)/2
  c.saveState();p=c.beginPath();p.rect(ox,oy,dw,dh);c.clipPath(p,stroke=0,fill=0)
  c.drawImage(str(path),ox-l*iw*scale,oy-(1-b)*ih*scale,width=iw*scale,height=ih*scale);c.restoreState()
 else:
  s=min(w/iw,h/ih);c.drawImage(str(path),x+(w-iw*s)/2,y+(h-ih*s)/2,width=iw*s,height=ih*s)
def block(x,y,w,h,label,fill='#e9f2f5',size=10):
 c.setFillColor(HexColor(fill));c.setStrokeColor(HexColor('#527381'));c.roundRect(x,y,w,h,5,fill=1,stroke=1);t(x+9,y+h/2-4,label,size,True)
def flow(y,steps):
 for i,(a,b) in enumerate(steps):
  block(36,y-48,523,48,a);t(48,y-38,b,9.2)
  if i<len(steps)-1:line(297,y-48,297,y-62)
  y-=69
 return y
start('คู่มือซ่อมพวงมาลัยไฟฟ้า by mytech','')
c.setFillColor(HexColor('#102c3a'));c.rect(0,44,596,798,fill=1,stroke=0)
c.setFillColor(HexColor('#ed6c39'));c.rect(35,785,72,6,fill=1,stroke=0)
t(35,748,'คู่มือซ่อม',25,True,'#f5a779');t(35,696,'พวงมาลัยไฟฟ้า',37,True,'#ffffff')
t(37,651,'by mytech',25,True,'#65dbd0');t(37,616,'เน้น PCB / อุปกรณ์ / วงจรภาคขับ | เพิ่มฝั่งยุโรป',12,True,'#dce8ef')
for x,y,path,caption in [(35,376,'output/agent-research-assets/gabisa-tr8-top.jpg','HONDA / TR8-M91'),(305,376,'output/research-assets/toyota-029-1R-ready.jpg','TOYOTA / catalog W-S0029'),(35,155,'output/europe-assets/015_1F.jpg','FIAT / OPEL / W-S0015'),(305,155,'output/europe-assets/080_1F-ready.jpg','MINI / W-S0080')]:
 c.setFillColor(HexColor('#ffffff'));c.roundRect(x,y,255,201,7,fill=1,stroke=0);photo(path,x+8,y+27,239,166);t(x+11,y+10,caption,8.5,True)
t(37,121,'ภาพจริงหลายยี่ห้อ + schematic ผู้ผลิตชิป + จุดตรวจหน้างาน',11,True,'#ffffff')
t(37,91,'เพิ่มยุโรป หน้า 43-54: Fiat/Opel, MINI, Volkswagen/Audi และ Renault',9.5,False,'#b7d0dc')
t(37,66,'ภาพและพิกัดตามแหล่งแต่ละกรณี ไม่ใช่วงจรหรืออะไหล่ร่วมกันทุกรุ่น',8.5,False,'#b7d0dc')
#43
start('เพิ่มยุโรป | เลือกชนิดและรุ่นก่อนชี้จุดซ่อม','ภาพ PCB และ supplier mapping ไม่ใช่ OEM schematic; ไม่ผูกอะไหล่ข้ามรุ่น')
y=table(704,[('กรณีศึกษา','ชนิดในแหล่ง','หน้า'),('Fiat Grande Punto / Opel Corsa D','EPS-C / W-S0015','44-45'),('MINI R55-R61 (ช่วงรวม)','EPS-R / W-S0080','46-47'),('VAG Tiguan / Q3 / Passat CC','EPS-R / W-S0082','48-49'),('Renault Clio III / Modus TRW3','EPS-C / W-S0023','50-51'),('ลำดับตรวจ / ใบงาน / แหล่งข้อมูล','ใช้ตามรุ่นจริง','52-54')],[280,175,70],10,43)
y=title(y-28,'แยกประเภทให้ถูกก่อนซ่อม')
y=para(y,['EPS-C ในบทนี้คือชุดช่วยที่คอพวงมาลัย; EPS-R คือชุดแร็กไฟฟ้า', 'ปั๊มไฟฟ้าขับระบบน้ำมันเป็น EHPS แม้บาง catalog เรียก EPS-P', 'MINI R50/R52/R53 แบบปั๊ม ไม่ใช่กรณี MINI W-S0080 ในบทนี้', 'PSA 206/307/C4 และ Saab 9-3 แบบปั๊ม ต้องแยกเป็นงาน EHPS'])
panel(y-20,'ใช้แผนที่อุปกรณ์อย่างไร',['เทียบ OEM ref / รหัส PCB / ด้าน 1F-1R-2R-3F ให้ตรงก่อน', 'พิกัดใน catalog ช่วยหาอุปกรณ์ ไม่ใช่เลขขาหรือจุดทดสอบ', 'SKU ผู้ขายไม่ใช่เบอร์ semiconductor และไม่ได้ยืนยันตัวเสีย', 'ภาพ PCB ต่างรุ่นไม่ใช้แทนภาพภายใน Honda TS4-Z51'])
#44
start('Fiat / Opel | PCB และพิกัดอุปกรณ์','E1: Emmetec W-S0015; Grande Punto 2005-09 / EVO 2009-12 / Corsa D รุ่นแรก 2006-14')
photo('output/europe-assets/015_1F.jpg',35,414,255,287);photo('output/europe-assets/015_1R.jpg',305,414,255,287)
y=table(385,[('ด้าน / กริดเดิม','หมวดที่ supplier ระบุ','จุดตรวจเบื้องต้น'),('1F A1/B1/C1/A3/B2/C3','MOSFET','เทียบแขนกำลังเมื่อไม่มีไฟ'),('1F B4','Motor-control IC','อ่านเบอร์ก่อนดูขา/วงจร'),('1F H5 / D4','CAN / regulator','ดูไฟและทางสัญญาณจริง'),('1F E4 / E3','Op amp / comparator','ดู reference และวงจรรอบตัว'),('1R F4','Relay','แยกคอยล์/หน้าสัมผัส')],[155,170,200],9.1,34)
para(y-24,['ภาพเป็นคนละด้าน 1F/1R คงกริดเดิม ไม่กลับภาพเพื่อเดาพิกัด', 'แยกภาคกำลัง/ควบคุมตามหลักฐาน ไม่ใช้เบอร์ W-xxxxx เป็นเบอร์ชิป', 'ยังไม่มี netlist / rail voltage / test point ตรง ECU นี้'],10)
#45
start('Fiat / Opel | จากภาพชิปไป datasheet A3935','ภาพอะไหล่ที่ supplier จับคู่ W-05021 → 1F B4 ไม่ใช่การอ่านบนบอร์ดเต็มโดยตรง')
photo('output/europe-assets/mt061909.png',40,550,180,152)
para(663,['Marking ที่อ่านได้: A3935KLQT', 'ตระกูล Allegro 3-phase controller', 'อ่าน datasheet ตาม package/suffix', 'ยังไม่ใช่ schematic ของ ECU ทั้งบอร์ด'],10.2,23,240)
photo('output/europe-assets/allegro-a3935-p1.png',35,224,525,310,(.08,.60,.92,.945))
t(36,205,'ภาพ Typical Application: Allegro A3935 datasheet หน้า 1 © Allegro MicroSystems',8.5)
y=para(176,['วงจรแสดง controller ขับ N-MOSFET 3 เฟส พร้อมส่วนควบคุม/ตรวจวัด', 'ถ้าไม่มี gate output ตรวจไฟ/enable/boost/bootstrap/fault ก่อนกล่าวว่า IC เสีย', 'ค่าทดสอบใช้ datasheet และบอร์ดตรงรุ่น ไม่ใช้ตัวเลขเป็นสเปก Honda Z51'],10)
panel(y-13,'ก่อนเลือกอะไหล่',['marking บนชิปไม่จำเป็นต้องเหมือนรหัสสั่งซื้อพร้อม reel suffix', 'ไม่อนุมัติเบอร์ทดแทนจากชื่อ A3935 หรือแพ็กเกจอย่างเดียว'])
#46
start('MINI | Control PCB 1F / 1R','E2: W-S0080 EPS-R; R55/R56/R57/R58/R59/R60/R61 ช่วงรวมใน catalog 2008-16')
photo('output/europe-assets/080_1F-ready.jpg',35,403,255,294);photo('output/europe-assets/080_1R-ready.jpg',305,403,255,294)
y=table(374,[('ภาพ / กริด','รายการตาม supplier','ข้อจำกัด'),('1F B2','Motor controller','ไม่มี marking เต็มที่ยืนยัน'),('1R D1','CAN chip','ยังไม่แจก pinout จาก SKU'),('1R A3','Dual comparator','ต้องรู้ reference จริง'),('1R B1','Dual op amp','วัดตาม topology จริง')],[105,190,230],9.4,35)
y=para(y-26,['ชิปใหญ่ในภาพ 1F มีสติกเกอร์ ไม่อ่านสติกเกอร์เป็นเบอร์ MCU', 'ภาพและกริดเป็นของชุดนี้ ไม่ยืนยัน BMW รุ่นอื่นหรือ MINI ปั๊ม EHPS', 'หากไม่สื่อสาร ให้เริ่มไฟ/กราวด์ แล้วตรวจ interface ที่ยืนยันจากเบอร์จริง'],10)
panel(y-13,'จุดซ่อมที่ต้องมีผลวัดรองรับ',['ตรวจลายขาด/จุดต่อ/คราบนำไฟ ก่อนตัดสิน MCU หรือ CAN เสีย', 'แยก control PCB จาก power board 3F; อย่าย้ายพิกัดข้ามแผ่น'])
#47
start('MINI | Power board 3F: ตรวจแขนกำลัง','E2: ภาพจริงจาก supplier W-S0080; ไม่ใช่ schematic หรือค่าทดสอบตรงแร็กทุก revision')
photo('output/europe-assets/080_3F-ready.jpg',35,288,525,410)
para(260,['แผนที่ผู้ขายจัดหมวด MOSFET หลายตำแหน่งบนด้าน 3F', 'เทียบภาพจริงและด้านให้ตรงก่อนแยกแขนกำลัง ห้ามเดาขา G/D/S', 'marking 2R5 ที่เห็น ไม่แปลงเป็นหน่วย/หน้าที่โดยไม่มีข้อมูลชิ้นส่วน'],10.2)
panel(165,'ลำดับตรวจแบบไม่จ่ายไฟ',['ตรวจสายและมอเตอร์ภายนอก → ยืนยันไม่มีแรงดันค้าง → เทียบแขนกำลัง', 'ค่าที่ต่างกลุ่มอาจมาจากทางขนาน/ประจุ gate ต้องยืนยันเพิ่ม', 'ไม่ป้อน gate ทดลอง ไม่ bypass fault และไม่ reflow ทั้งแผ่น'])
#48
start('Volkswagen / Audi | แยก power/filter กับ control','E3: W-S0082 EPS-R; Tiguan 2007-16 / Audi Q3 2011-18 / Passat CC 2008-16 ตาม catalog')
photo('output/europe-assets/082_1F-ready.jpg',35,255,225,448);photo('output/europe-assets/082_2F-ready.jpg',282,255,275,448)
t(45,234,'ซ้าย: 1F power / filter / contact',10,True);t(301,234,'ขวา: 2F control / power',10,True)
para(205,['1F ไม่ใช่ logic PCB; 2F มีภาคควบคุมและ interconnect บริเวณล่าง', 'อย่ารบกวนเส้นลวด/จุดต่อหรือขูดเคลือบเพื่อทดลองวัด', 'รุ่นตาม catalog ไม่ใช่หลักฐานว่าใช้กับ Golf / Audi A4 หรือ BMW ได้'],10)
panel(116,'ก่อนสั่งชิ้นส่วน',['เทียบ OEM ref และ revision ของแร็ก/PCB จริงก่อน', 'ภาพหรือขนาดแพ็กเกจอย่างเดียวไม่ยืนยันชนิด/พิกัด IC'])
#49
start('Volkswagen / Audi | ใช้ map โดยไม่แก้ข้อมูลเดาเอง','E3: พิกัดจาก HTML case 82; ไม่ใช่ผลไล่วงจรหรือวัด ECU จริง')
y=table(704,[('ภาพ / กริด','หมวดที่ source ระบุ','ใช้ตรวจอะไร'),('2F B4','EEPROM','เบอร์จริง/รางไฟ/ข้อมูลระบบ'),('2F C4','Crystal','อ่านเบอร์และวงจร clock ก่อน'),('2F C5','Motor controller','ไฟ/enable/fault ตามเบอร์จริง'),('2F A6','Dual op amp','reference และทาง sense'),('2F C2','Regulator items','มีหลายรายการร่วมพิกัด')],[120,180,225],9.4,39)
y=panel(y-28,'พบความไม่สม่ำเสมอในแหล่ง: CAN เขียนกริด 3C',['ไม่แก้เงียบเป็น C3 แล้วชี้ตำแหน่งบนบอร์ด', 'บันทึกว่ารอยืนยันพิกัด/marking ก่อนระบุตัวชิป CAN', 'รหัส W-05181 ในรายการเป็น SKU ผู้ขาย ไม่ใช่ pinout'])
y=title(y,'แนวตรวจซ่อมที่ใช้ได้')
para(y,['ไฟเข้า/กราวด์ → regulator / control enable → interface / power stage', 'หากภาคกำลังผิดปกติ ตรวจทางกำลัง/มอเตอร์และวงจร sense ร่วมกัน', 'ถ้ามี interconnect ละเอียดเสียหาย ต้องใช้งานซ่อมเฉพาะทาง ไม่ฝืนแตะโพรบ', 'ยังไม่มี schematic ทั้งบอร์ดหรือเบอร์ชิปเต็มที่ยืนยันจากภาพ'],10.5)
#50
start('Renault | Clio III / Modus TRW3: บอร์ด 2R','E4: W-S0023 EPS-C; Clio III 2005-14 / Modus TRW3 2004-13 ตาม supplier')
photo('output/europe-assets/renault23-2R.jpg',35,245,525,455)
para(219,['ภาพนี้คือ 2R: ชุดย่อยฝั่งมอเตอร์/Hall ไม่ใช่แผงควบคุม 1R', 'พิกัด 2R C1 จัดหมวดรีเลย์; B2/C3 และ C4 จัดหมวด Hall ตาม source', 'ห้ามนำพิกัด 1R-D4 CAN หรือ 1R-B3 motor IC ไปชี้บนภาพนี้'],10.3)
panel(126,'ก่อนซ่อม',['เทียบด้าน/แผ่น และรหัสชิ้นงานจริง ไม่เหมารวมทุก Clio/Modus', 'ตรวจสาย/ขั้ว/รอยต่อที่ยืนยันก่อนกล่าวว่า Hall หรือวงจรมอเตอร์เสีย'])
#51
start('Renault | ตัวอย่างชิปที่ supplier จับคู่กับ map','ภาพอะไหล่จาก catalog ไม่ใช่การอ่านบนบอร์ด 2R และไม่ใช่ BOM ของ Honda Z51')
for x,y,path,label in [(35,487,'output/europe-assets/renault23-can.png','Philips TJA1050 / CAN'),(305,487,'output/europe-assets/renault23-eeprom.png','ST 24C16WP / EEPROM'),(35,283,'output/europe-assets/renault23-motor-ic.png','MLX15120DB'),(305,283,'output/europe-assets/renault23-mosfet-control.png','MLX15121BA')]:
 photo(path,x,y,255,166);t(x+5,y-18,label,10,True)
para(228,['TJA1050 มี NXP datasheet; เป็น transceiver ไม่ใช่ MCU หรือ gate driver', 'ST ที่ลิงก์เป็นเอกสารตระกูล ไม่ยืนยัน datasheet ตรง suffix 24C16WP', 'MLX15120DB / MLX15121BA อ่านได้ แต่ยังไม่พบ primary datasheet สาธารณะ', 'จึงไม่แต่ง pinout และไม่ใช้ขา DRV3205 หรือ A3935 แทน'],10)
panel(121,'การซ่อมข้อมูล',['เก็บ backup และยืนยันการตั้งค่าระบบก่อนแตะ memory', 'ไม่เขียน virgin/เปลี่ยน EEPROM เป็นวิธีแก้ EPS ทุกอาการ'])
#52
start('ยุโรป | ไล่อาการบน PCB โดยไม่สลับวงจรต่างรุ่น','แนวตรวจทั่วไป; ใช้เงื่อนไขและ datasheet ตรงอุปกรณ์/ECU')
y=table(704,[('อาการ','เริ่มที่ภาค','ตรวจร่วมก่อนเปลี่ยนตัว'),('ไม่สื่อสาร','ไฟเข้า / regulator / CAN','กราวด์ enable และสายภายนอก'),('ฟิวส์ขาด / กินกระแส','protection / power stage','แยกสาย มอเตอร์ ทางขนาน'),('ไม่ขับมอเตอร์','gate driver / FET','control enable / fault / sense'),('แรงช่วยผิดปกติ','sensor / analog / control','กลไก สาย calibration'),('อาการร้อนแล้วหาย','supply / contact / protection','เก็บผลวัดขณะอาการเกิด')],[135,180,210],9.4,42)
y=title(y-28,'จุดสำคัญก่อนวัด')
y=para(y,['โอห์ม/diode mode: ตัดไฟ แยกภายนอก และยืนยันไม่มีแรงดันค้าง', 'วัดในวงจรเป็นเบาะแส ทางขนานอาจทำให้ระบุชิ้นส่วนเสียผิด', 'วัด high-side ใช้ differential/isolated probe ที่ถูกพิกัดและ common-mode', 'ห้ามถอดสายดิน scope หรือบังคับ gate ข้าม fault เพื่อให้หมุน'])
panel(y-16,'ทดสอบหลังซ่อม',['ตรวจสาเหตุร่วมก่อนปิดฝา คืนฉนวน/ซีล/thermal interface ตามงานจริง', 'ยืนยัน software / coding / calibration ของรถนั้น ไม่ใช้ Honda learn แทนทุกรุ่น', 'อ่าน DTC และทดสอบอาการเดิมในระบบที่พร้อมก่อนส่งงาน'])
#53
start('ยุโรป | ใบงานผูกชิ้นส่วนกับหลักฐาน','ใช้บันทึกก่อนสั่งอะไหล่และส่งต่อ Claude / ผู้ตรวจงาน')
para(704,['รถ / ปี / OEM ECU ref: ......................................................................', 'รหัส PCB / revision / map: .................................................................', 'ด้าน / กริด / จุดจริงในภาพ: ................................................................', 'อ่าน marking จาก: [ ] บอร์ดจริง  [ ] ภาพอะไหล่ supplier  [ ] ยังอ่านไม่ได้'],10.5,29)
y=table(562,[('สิ่งที่ต้องยืนยัน','บันทึกผลจริง'),('เบอร์และ suffix / package','................................................................'),('ผู้ผลิต / URL datasheet','................................................................'),('ชิ้นส่วนต่อกับภาคใด','................................................................'),('โหมด / ทิศโพรบ / ผลก่อนแยก','................................................................'),('ผลหลังแยกทางขนาน','................................................................'),('สาเหตุร่วม / ชิ้นส่วนที่ตรวจร่วม','................................................................'),('หลังซ่อม / DTC / coding','................................................................')],[205,320],10,39)
para(y-26,['ข้อที่ยังไม่ยืนยัน: ................................................................................', 'ผู้ซ่อม / ผู้ตรวจ / วันที่: ......................................................................', 'คำสั่งงานถัดไป: ..................................................................................'],10.5,29)
#54
start('ยุโรป | แหล่งหลักและข้อจำกัดที่ต้องคงไว้','เครดิตภาพ supplier: Emmetec / Jada / ORPAV; datasheet: เจ้าของเอกสารแต่ละราย')
elinks=[('E1  Fiat/Opel W-S0015 board map','https://www.emmetec.com/en-us/eps/devices/15'),('E1a Allegro A3935 datasheet / Typical Application','https://www.allegromicro.com/~/media/Files/Datasheets/A3935-Datasheet.ashx'),('E2  MINI W-S0080 board map','https://www.jadausa.com/en-us/eps/devices/80'),('E3  VAG W-S0082 board map','https://www.jadausa.com/en-us/eps/devices/82'),('E4  Renault W-S0023 board map','https://www.emmetec.com/en-us/eps/devices/23'),('E4a NXP TJA1050 datasheet','https://www.nxp.com/docs/en/data-sheet/TJA1050.pdf'),('E4b ST M24C16 family datasheet','https://www.st.com/resource/en/datasheet/m24c16-f.pdf')]
y=702
for name,url in elinks:t(37,y,name,10,True,TEAL);c.linkURL(url,(35,y-4,559,y+14),relative=0);y-=33
y=title(y-12,'แยกหลักฐาน 3 ระดับ')
y=para(y,['1. ภาพ PCB เห็นชิ้นส่วน/รอยต่อจริง แต่ยังไม่ใช่ netlist ทั้งบอร์ด', '2. Supplier map/ภาพอะไหล่ บอกการจับคู่สินค้า ไม่รับรองทุก revision', '3. Datasheet บอกวงจรชิปนั้น ไม่ใช่ schematic ECU ทั้งกล่อง'])
panel(y-20,'ยังไม่มีหลักฐานเพียงพอ',['ไม่มี schematic โรงงานครบทั้งบอร์ดของกรณียุโรปในบทนี้', 'ไม่มี pinout/rail voltage/test point ที่อนุมานจากภาพอย่างเดียว', 'ยังไม่มีภาพ PCB ภายใน Honda TS4-Z51 ที่ยืนยันตรงรหัส', 'ข้อจำกัดเหล่านี้ต้องส่งต่อใน README ไม่ลบทิ้งเพื่อให้ดูสมบูรณ์'])
c.save();Path('output/europe-page-index.json').write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding='utf8');Path('tmp/pdfs/europe-overflow.json').write_text(json.dumps(overflow,ensure_ascii=False,indent=2),encoding='utf8');print('Europe raw pages',P,'overflows',len(overflow))

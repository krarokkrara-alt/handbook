# Agent research: Renault TRW / PSA / French EPS PCB

วันที่ตรวจ: 14 พฤศจิกายน 2026
สถานะ: อ่านหน้า Emmetec และเปิดตรวจภาพจริงครบทุกไฟล์ที่ระบุด้านล่าง ไม่แก้หนังสือหลัก

## กรณีหลักที่พร้อมใช้: Renault Clio III / Modus TRW 3

- Source primary ของผู้จัดทำ board map/อะไหล่: https://www.emmetec.com/en-us/eps/devices/23
- รหัส map: **W-S0023 / EPS-C / Z-35007 (7-C)**
- รุ่น/ปีตาม source: Renault Clio III 2005-2014; Renault Modus TRW 3 2004-2013
- EPS-C = column electric power steering ตามการแบ่งของแหล่งนี้ เป็น direct EPS ไม่ใช่ปั๊ม EHPS
- ภาพ map ที่โหลดได้: output/europe-assets/renault23-2R.jpg (1000x1254 px)
- URL: https://emmetec.blob.core.windows.net/70px/023_2R.jpg
- ภาพ 2R เป็นบอร์ดวงแหวนฝั่งมอเตอร์/เซนเซอร์ มีรีเลย์และ IC/อุปกรณ์รอบวง ไม่ใช่แผงควบคุม 1R
- เห็น silkscreen CCTECHCO-1 CR1 / 94V-0 / 0205 และจุด J1, U1, Q1/Q2/Q3; ไม่อ้างว่าเป็นเบอร์ IC
- ยังไม่มี OEM ECU part number ที่ยืนยันในภาพนี้ จึงไม่ใช้เป็นความเข้ากันได้ทุก Clio III/Modus

### แยกภาพและพิกัด 1F / 1R / 2R ให้ถูกต้อง

ตำแหน่งจากตาราง Emmetec เป็นข้อมูลผู้จัดทำ map ไม่ใช่เบอร์ขาปลั๊กรถ:

| ภาพ map | Grid | หมวดของ source | รหัสสินค้า Emmetec |
|---|---|---|---|
| 1F | B1 | EEPROM | W-01030 |
| 1F | D3 | Relay | W-01005 / W-01005A |
| 1R | B3 | Motor-control IC | W-01016 |
| 1R | D4 | CAN IC | W-01040 |
| 1R | D3 / D4 | Voltage regulator | W-05043 |
| 1R | B4 | MOSFET-control IC | W-05179 |
| 2R | C1 | Relay | W-01004 |
| 2R | B2 / C3 | Hall sensor | W-01028 |
| 2R | C4 | Hall sensor | W-05189 |

**สำคัญ:** ภาพ renault23-2R.jpg ไม่สามารถนำลูกศรชี้พิกัด 1R-D4 CAN ลงไปได้ เพราะเป็นคนละบอร์ด/ด้านของชุด

ภาพ map 1F/1R มี URL ที่เห็นจริงจาก HTML แต่ดาวน์โหลด timeout จึงยังไม่ตรวจภาพและไม่มีไฟล์พร้อมใช้:
- https://emmetec.blob.core.windows.net/70px/023_1F.jpg
- https://emmetec.blob.core.windows.net/70px/023_1R.jpg

เก็บ HTML source ที่อ่านได้: output/europe-assets/emmetec-renault23.html

## ภาพชิ้นส่วนจาก catalog ที่ตรวจ marking ได้

**เป็นภาพอะไหล่ที่ catalog ผูกเข้ากับ map นี้ ไม่ใช่การอ่านเลขจากอุปกรณ์ที่ยังบัดกรีอยู่บนบอร์ด 2R หรือบอร์ดรถผู้ใช้** ต้องคงข้อความนี้ในหนังสือ

| ไฟล์ | Catalog association | อ่านจากภาพ | ความมั่นใจ / ขอบเขต |
|---|---|---|---|
| renault23-eeprom.png | W-01030, 1F B1 | ST logo; 24C16WP | กลุ่ม serial I2C EEPROM; ไม่ใช้ suffix ในภาพอนุมาน exact automotive grade/แรงดันทุกเวอร์ชัน |
| renault23-can.png | W-01040, 1R D4 | Philips logo; TJA1050 (บรรทัดอื่นไม่ชัด) | ยืนยัน family CAN transceiver เพื่ออธิบายหลักการได้ ไม่ใช่ proof ว่า ECUทุกrevisionใช้เหมือนกัน |
| renault23-motor-ic.png | W-01016, 1R B3 | MLX15120DB / 0318480 / 0347 | markingอ่านชัด แต่ยังไม่พบ datasheet primary public จึงไม่แจก pinout/แรงดัน/วิธีทดสอบ ICนี้ |
| renault23-mosfet-control.png | W-05179, 1R B4 | MLX15121BA / T144267/US 0740 | markingอ่านชัด แต่ยังไม่พบ datasheet primary public; ห้ามใช้ DRV3205 pinoutแทน |
| renault23-regulator.png | W-05043, 1R D3/D4 | ไม่มี markingชัด | ระบุได้เพียงแพ็กเกจ power 5ขาในภาพ ไม่ระบุว่าเป็นรุ่นใด |

URLs ภาพ:
- EEPROM https://emmetec.blob.core.windows.net/400px/mt060391.png
- CAN https://emmetec.blob.core.windows.net/400px/mt061398.png
- Motor IC https://emmetec.blob.core.windows.net/400px/mt061771.png
- MOSFET-control https://emmetec.blob.core.windows.net/400px/mt071934.png
- Regulator https://emmetec.blob.core.windows.net/400px/mt066992.png

## Datasheet primary ที่ยืนยันได้

### TJA1050
- NXP product: https://www.nxp.com/products/interfaces/can-transceivers/legacy-can/high-speed-can-transceiver:TJA1050
- PDF: https://www.nxp.com/docs/en/data-sheet/TJA1050.pdf
- Application note: https://www.nxp.com/docs/en/application-note/AN00020.pdf
- ใช้อธิบาย CAN physical transceiver: TXD/RXD ฝั่ง MCU และ CANH/CANL ฝั่งบัส, 5V supply family
- ห้ามเรียกว่า MCU/CAN controller หรือ gate driver
- ตรวจ datasheet revisionและactualpackageก่อนอ้างเลขขา ไม่ผูกขา TJA1050 เข้ากับปลั๊ก ECU โดยยังไม่ไล่วงจร

### 24C16 family
- ST product: https://www.st.com/en/memories/m24c16-w.html
- ST PDF ครอบคลุม M24C16-W/R/F: https://www.st.com/resource/en/datasheet/m24c16-f.pdf
- ใช้อธิบาย 16Kbit / 2Kbyte I2C EEPROM, SDA/SCL/WC/VCC/VSS ตาม family
- ไม่แนะนำเขียนทับ/virgin EEPROM เป็นวิธีแก้ทุกกรณี; ต้องเก็บ backupและยืนยันรุ่น/การตั้งค่าระบบก่อน
- ไม่ใช้ datasheet M24C16-A125 รุ่นใหม่แทนชิปเก่าในภาพแล้วสรุป drop-in

### MLX15120DB / MLX15121BA
- ค้น melexis.com ด้วยรหัสแล้วไม่พบ public primary datasheet ในรอบนี้
- มี markingจริงจากภาพ catalog แต่ไม่มี pin-level specification ที่รับรอง จึงเป็นกรณีศึกษาข้อจำกัดข้อมูล ไม่แต่ง schematicหรือเบอร์เทียบ

## กรณี PSA ที่ต้องแยกเป็น EHPS

- Emmetec map W-S0028 EPS-P: https://www.emmetec.com/de-de/eps/devices/28
- รุ่นตาม source: Peugeot206 1998-2013; Peugeot307 2001-2009; CitroenC4 2004-2010
- Sourceอธิบายปั๊ม JTEKT/HPI มี reservoir, pump, oil seals: https://warsztat.pl/artykuly/regeneracja-eps-p-w-samochodach-peugeot-206-307-oraz-citroen-c4,54583,bm9uZSE1NDU4MyEhbm93b2N6ZXNueXdhcnN6dGF0LnBsL2FydHlrdWx5LzEwLTIwMTYvb2xlamUvMw
- จัดหมวด **EHPS ปั๊มไฟฟ้าขับระบบไฮดรอลิก** แม้ catalogเขียน EPS-P ห้ามเรียก directEPS และห้ามปนผังขามอเตอร์ rack assist
- ภาพ/HTMLของบทความและ PDF catalogใหญ่โหลด timeout รอบนี้ ไม่ถือมีassetพร้อมใช้

## กรณี Peugeot207 direct rack EPS ที่มี primary support

- Emmetec index https://www.emmetec.com/en-us/eps/devices ระบุ W-S0027 EPS-R: CitroenC3 Picasso2009-2017 / Peugeot207 9H2006-2015 และ W-S0077 EPS-R Peugeot207 8H2006-2015
- JTEKT official programming PDF: https://www.jtekt.eu/app/uploads/2025/09/DE-Technische-Daten-fuer-die-Programmierung-von-Lenkgetriebe.pdf หน้า2 ระบุ PEUGEOT207/C3PICASSO ในบริบท EPS programming
- แหล่งร้านบางแห่งเรียก column/pumpปะปน จึงไม่ใช้captionร้านยืนยัน topologyหรือบอร์ดที่ไม่มีเลข
- ไม่มีcompletePCBassetสำหรับ Peugeot207 ในงานย่อยนี้ จึงแนะนำใช้ Renaultcase ที่ตรวจภาพได้จริงเป็นบทหลัก

## หมายเหตุ Saab

- https://saabwisonline.com/9-3-9440/2006/6-steering-assembly/electro-hydraulic-power-steering/technical-data/power-steering-unit-ehps
- OEM workshop content (mirror) ชื่อชัดเจน EHPS; ECU integrated in pump housing, brushless12V motor
- ไม่ควรใส่ Saab9-3 pumpboard ในแกลเลอรี directEPS โดยไม่ติดป้าย EHPS

## สรุป assetที่พร้อมจริง

พร้อมใช้งาน: renault23-2R.jpg, renault23-eeprom.png, renault23-can.png, renault23-motor-ic.png, renault23-mosfet-control.png, renault23-regulator.png, emmetec-renault23.html
ตรวจภาพทั้ง6แล้ว. บอร์ด2Rเหมาะหน้าphoto case study; ชิ้นส่วนcatalogเหมาะหน้าrole + evidence cardแยก ไม่ใช้ลูกศรชี้ชิป1Rลงบนบอร์ด2R

captionแนะนำ: “Renault Clio III / Modus TRW3, EPS-C, Emmetec W-S0023, ภาพmap2R. ภาพและพิกัดจากEmmetec ไม่ใช่schematic OEM และไม่ยืนยันทุกrevision.”

ไม่ได้แก้หนังสือหลัก

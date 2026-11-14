# รายงาน agent ค้น PCB / schematic EPS Honda

วันที่ค้น: 14 พฤศจิกายน 2026 (Asia/Bangkok)
ผู้ค้น: source_research agent
สถานะ: ค้นข้อมูลจริงจากเว็บ/ภาพ แล้วเปิดภาพตรวจด้วยตา ไม่ใช่เพียง review ข้อความเดิม

## 1. ผลที่ตรงรหัส

ค้น 39980-TS4-Z51, 39980TS4Z51, 39980 TS4 Z51, 39980-TS4-Z5, S4S6-113282 และ HTS4X-10-14M ทั้งแบบตรงรหัสและผสม repair / PCB / board / schematic / ซ่อม / บอร์ด / 基板 / 电路板 / ремонт / плата

**ไม่พบภาพ PCB ภายในหรือ schematic ที่ยืนยันเลข TS4-Z51/Z5 หรือ S4S6-113282/HTS4X-10-14M ได้จากภาพจริงในการค้นครั้งนี้** ภาพผู้ใช้ด้านฝา/หลัง/ขาปลั๊กเป็นหลักฐานตรงกล่องที่ดีที่สุด ยังไม่มีภาพ PCB เปิดฝาของกล่องผู้ใช้

รายการอะไหล่ตระกูล TS4 ที่พบ:
- https://www.monotaro.com/p/2582/1434/ : ระบุ 39980-TS4-T01 ว่า power steering computer แต่ไม่ใช่ Z51 และไม่มี PCB
- https://www.halfcut.my/honda-civic-tro-hb-steering-ecu-39980-ts4-t0-ak/ : ผู้ขายระบุ 39980-TS4-T0 steering ECU ไม่ใช่ Z51
- https://www.ebay.com.au/itm/186834175695 : ผู้ขายใช้ชื่อ Engine ECU แต่เลข 39980-TS4-T0 ตาราง compatible กว้างและขัดกัน จึงไม่ใช้ยืนยัน pinout หรือรุ่นรถ/ภายใน

การค้นภาพ exact ที่ให้ผล clock spring / key blank / tire pressure sensor เป็นผลผิดเรื่อง ถูกตัดออก ไม่เอามาเพิ่มจำนวนภาพในหนังสือ

## 2. ภาพจริงตระกูลใกล้เคียงที่เปิดตรวจแล้ว

### 2.1 Gabisa: 39980-TR8-M91 / HTR8X-10-11M
หน้า:
https://www.gabisaonline.com.br/modulos/bcm/placa-circuito-do-modulo-central-de-controle-da-direcao-eletrica-elesys-39980tr8m91-honda-new-civic-013-014-015-016

ผู้ขายระบุ Honda New Civic 2013-2016 / SHOWA Elesys / 39980-TR8-M9/M91 / HTR8X-10-11M (ข้อมูลผู้ขาย ไม่ใช่ผู้ผลิต Honda)

ภาพตรง:
- https://images.tcdn.com.br/img/img_prod/371065/placa_circuito_do_modulo_central_de_controle_da_direcao_eletrica_elesys_39980tr8m91_honda_new_civic__42285_1_c1dcd3fea79715a2c134d596a6ec2302.jpg
- https://images.tcdn.com.br/img/img_prod/371065/placa_circuito_do_modulo_central_de_controle_da_direcao_eletrica_elesys_39980tr8m91_honda_new_civic__42285_2_f22ac34665e0761fc7457b71c63e9852.jpg

ไฟล์ที่ดาวน์โหลดเพื่อตรวจ:
- output/agent-research-assets/gabisa-tr8-top.jpg = มุมเฉียงด้านอุปกรณ์
- output/agent-research-assets/gabisa-tr8-bottom.jpg = มุมตรงด้านอุปกรณ์ (แม้ชื่อไฟล์ bottom แต่ไม่ใช่ด้านหลัง)

สิ่งที่เห็นจริงจากภาพ:
- บอร์ดสีเขียวมี elesys / ปลั๊กคู่ใหญ่-เล็ก / capacitor ทรงกระบอก 4 ตัว / IC QFP กลาง-ขวา / IC ขายาวด้านบน / crystal can ใกล้ QFP
- capacitor มีข้อความ 1800 / 35V; ไม่ใช้เป็นข้อกำหนด capacitor ของ Z51 และไม่ระบุค่า ESR/ripple/series โดยเดา
- IC markings มืดหรือไม่ชัดพอระบุ part number อย่างมั่นใจ; ไม่มีเบอร์ MCU/gate driver/regulator ที่ยืนยันได้
- ทั้ง 2 รูปเป็นด้านเดียวกันคนละมุม ไม่ใช่ภาพสองด้านของ PCB
- ไม่เห็นภาพเดียวที่มีสติกเกอร์ TS4-Z51 และ PCB อยู่ร่วมกัน จึงห้ามเรียกภาพนี้ว่า PCB Z51

### 2.2 Life After 40: Civic EX 2012 / replacement 39980-TR3-A11
หน้า:
https://lifeafter40.net/honda-civic-electric-power-steering-eps-unit-replacement/
ภาพ:
https://i0.wp.com/lifeafter40.net/wp-content/uploads/2021/11/Honda-civic-EPS-electric-power-steering-module-scaled.jpg?resize=1536%2C1298&ssl=1
ไฟล์: output/agent-research-assets/lifeafter40-pcb.jpg

บทความเจ้าของรถระบุ replacement 39980-TR3-A11 (ไม่ได้ยืนยันว่าบอร์ดรูปนี้มีสติกเกอร์รหัสใดติดในภาพ)
ภาพเห็น capacitor 4 ตัว, elesys, PCB, ปลั๊กคู่, QFP และคราบขาวบางบริเวณ แต่มีข้อความพาดกลางภาพบัง part markings จึงไม่ระบุเบอร์ชิป/ตำแหน่งเสียจากภาพนี้ และไม่เรียกคราบนั้นว่าการเสีย Z51

ตัวบทความมีคำแนะนำ reset ที่อิงแหล่งอื่น ใช้ภาพเป็นตัวอย่างรูปลักษณ์เท่านั้น ไม่ใช้เป็นเกณฑ์วัดหรือขั้นตอนซ่อม

### 2.3 วิดีโอที่พบเป็นร่องรอยเท่านั้น
- https://www.youtube.com/watch?v=DrCf6lR3aaE : How to replace 2012 Honda civic EPS module (Kris Tran, 2021-11-11) เป็นการถอดเปลี่ยน ไม่พบหลักฐาน Z51 PCB/component marking จากข้อความค้น
- https://www.youtube.com/watch?v=Zs2N8xj4acw : SAM Motoring ตรวจระบบ Civic FB 2014-2015 ไม่ยืนยัน PCB ตรง Z51 จาก search result
- https://rutube.ru/video/42ebe809d6584ab3b22e5a3eca5fe953/ : หัวข้อ EPS Civic 4D; ไม่ได้ตรวจเฟรม/เลขกล่อง จึงไม่ใช้เป็นภาพหรือขั้นตอนซ่อมยืนยัน

## 3. Schematic ผู้ผลิตชิปที่เป็นวงจรจริง ไม่ใช่ Z51

### 3.1 TI DRV3205-Q1 gate driver + inverter
- หน้า official: https://www.ti.com/product/DRV3205-Q1
- datasheet PDF: https://www.ti.com/lit/ds/symlink/drv3205-q1.pdf
- หน้า 22 Figure 17 Typical Application Diagram: gate-driver, 6 N-MOSFET, gate resistors, low-side shunts, boost supply, SPI/PWM/ADC
- หน้า 23 เป็น system example EPS; หน้า 24 Figure19 เป็น layout ไม่ใช่ circuit schematic
- ผู้ผลิตเตือนภาพ schematic ไม่แสดงตำแหน่งขาจริงรอบตัว IC
- ใช้เพื่อสอนหน้าที่ gate driver/inverter เท่านั้น ห้ามถือเบอร์หรือค่าในตัวอย่างเป็น BOM Z51
- EVM: https://www.ti.com/tool/DRV3205EVM
- guide: https://www.ti.com/lit/ug/slvuan3/slvuan3.pdf (web tool เปิด canonical บางครั้งไม่สำเร็จ แต่มี search indexed หน้า2ภาพบอร์ดจริง)

### 3.2 TI resolver excitation + analog front end
- หน้า official: https://www.ti.com/tool/TIDA-01527
- schematic PDF: https://www.ti.com/lit/pdf/TIDRVX9 (5หน้า)
- PDF หน้า2 (index1): Excitation amplifier schematic: PWM-to-sine/phase splitter, TLV4171, BC817/BC807 discrete output stages, EXC+/EXC-
- PDF หน้า3 (index2): Analog front-end schematic: SIN/COS feedback, TLV2171, reference และ CD4053 analog crossbar experimental
- adapter schematic อื่น: https://www.ti.com/lit/pdf/TIDRVY0 (3หน้า เป็น LaunchPad adapter ไม่ใช่ excitation front-end)
- design guide: https://www.ti.com/lit/pdf/TIDUDP0
- ไม่ใช้ค่า drive amplitude/frequency หรือ pinout ของ TI ไปป้อน resolver Z51 เพราะยังไม่มี spec sensor ตรงรุ่น

### 3.3 ภาคไฟเข้า
- https://www.ti.com/tool/TIDA-00992
- schematic https://www.ti.com/lit/pdf/TIDRNE8
- LM5050-Q1 + N-MOS เป็น ideal diode/reverse-polarity design ไม่ใช่หลักฐานว่า Z51 ใช้ชิปนี้หรือเป็น fail-safe disconnect แบบเดียวกัน

### 3.4 สถาปัตยกรรมและอุปกรณ์ภายในอื่น
- NXP EPS block diagram: https://www.nxp.com/assets/block-diagram/en/ElectricPowerSteeringEPS.pdf
- Infineon AN1100: https://documentation.infineon.com/aurixtc3xx/docs/iat1745576007982
- Current sense: https://www.ti.com/lit/gpn/INA240-Q1
- CAN transceiver: https://www.ti.com/lit/gpn/TCAN1042-Q1

ข้อควรแยก topology: 6-FET inverter ≠ phase disconnect; ideal diode ≠ back-to-back disconnect; low-side current shunt ≠ inline/DC-link; modern Hall/SENT torque sensor ≠ VS1/PVF/VS2 inductive interface ตามผัง Honda HF; CAN-FD capability ของชิปใหม่ไม่ยืนยันกล่อง Civic 2012 ใช้ CAN-FD

## 4. แหล่งซ่อม/วัด Honda primary เพิ่มเติม

- A2/A9/ฟิวส์และช่วง DATA LIST: https://charm.li/Honda/2012/Civic%20L4-1.8L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/Manufacturer%20Code%20Charts/11-02/EPS/
- Resolver HF2012 DTC71: https://charm.li/Honda/2012/Civic%20HF%20L4-1.8L/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/Manufacturer%20Code%20Charts/71-02/EPS/
  ค่าคู่มือ R1-R2 13-25 Ω, S1-S3 และ S2-S4 26-49 Ω เป็นค่า sensor/harness ตามการแยกปลั๊กที่ระบุ ไม่ใช่ค่าขา ECU ภายใน ไม่รับรอง Z51 โดยตรง
- AHM/NHTSA investigation 2012-15 Civic DTC33: https://static.nhtsa.gov/odi/tsbs/2015/MC-10107352-9340.pdf
  ยืนยันชื่อ DTC Lower/Upper FET stuck ON ไม่ใช่คำสั่งเปลี่ยน FET และกำหนด VIN 2HG/19X ไม่ใช่ยืนยันรถไทย
- HDS torque learn HF2012: https://charm.li/Honda/2012/Civic%20HF%20L4-1.8L/Repair%20and%20Diagnosis/Steering%20and%20Suspension/Steering/Power%20Steering/Power%20Steering%20Motor/Service%20and%20Repair/

## 5. รูปหลายยี่ห้อที่อาจใช้สืบค้นต่อ

Emmetec catalog (ผู้ผลิต/จำหน่ายอะไหล่ EPS ไม่ใช่ OEM schematic):
https://www.seauto.es/wp-content/uploads/2022/09/emmetec-EPS_62_preview_2021_Bombas-Hidraulicas.pdf
มี board mapping หลายยี่ห้อและ Honda Civic 2001-2006 W-S0035 ซึ่งไม่ตรง FB

https://www.emmetec.com/en-us/eps/devices/95
W-S0095 ใช้ Hyundai i30/Veloster/Kia Cee'd/Elantra มีหมวด MOSFET/CAN/regulator/EEPROM แต่รหัส W-xxxxx เป็นรหัสสินค้า ไม่ใช่เบอร์ semiconductor ที่อนุมานได้เอง

## 6. สิ่งที่ไม่ควรเขียนในหนังสือ

- ห้ามวางรูป TR8/TR3 แล้วเขียนว่าเป็น TS4-Z51
- ห้ามระบุชื่อ/เบอร์ MCU, regulator, FET, gate driver ใน Z51 โดยอาศัยตำแหน่งหรือแพ็กเกจเหมือนกัน
- ห้ามแสดง TI example แล้วเอาลูกศรชี้ไปยังจุดจริงของภาพบอร์ด Z51 ที่ยังไม่มี
- ไม่ควรอ้าง circuit board ABS/VSA repair ของ Civic 2012 เป็น EPS เพราะ search มักปะปนกัน
- ควรให้หลักฐานแต่ละภาพ: รุ่นตาม source, สิ่งที่เห็นเอง, สิ่งที่ยังไม่ยืนยัน และ URL


## 7. ไฟล์ schematic ที่ดาวน์โหลดและ render แล้ว (พร้อมวางหนังสือ)

เก็บใน output/agent-research-assets/ และตรวจภาพด้วย view_image แล้ว:

| ไฟล์ | แหล่งต้นฉบับและหน้า | สถานะ |
|---|---|---|
| ti-gate-driver-figure17-excerpt.png | TI DRV3205-Q1 SLVSCV1E, หน้า22 Figure17, https://www.ti.com/lit/ds/symlink/drv3205-q1.pdf | 300dpi, เฉพาะวงจร gate-driver/inverter/current shunts และคงบรรทัด Copyright 2016 TI ในภาพ |
| ti-resolver-excitation-excerpt.png | TIDRVX9 หน้า2 (sheet 2 of 3), https://www.ti.com/lit/pdf/TIDRVX9 | 300dpi, excerpt 4วงจร excitation/feedback; ต้องใส่ caption เครดิต TI ในหนังสือ |
| ti-resolver-sine-channel-excerpt.png | TIDRVX9 หน้า3 (sheet 2 of 3 ในอีก SchDoc) | 300dpi, เฉพาะช่อง SINE feedback วงจรครบ ป้ายชื่อครบ ไม่มีการวาดแก้เส้น; ต้องใส่ caption เครดิต TI |
| ti-reverse-polarity-excerpt.png | TIDRNE8 หน้า2, https://www.ti.com/lit/pdf/TIDRNE8 | 300dpi เฉพาะวงจรสีพื้นเดิม LM5050-Q1 + MOSFET; ต้องใส่ caption เครดิต TI |

ภาพทั้งหน้าเพื่อดูเครดิต/ข้อจำกัดในต้นฉบับ:
- gate-driver-schematic-22.png (210dpi)
- resolver-schematic-2.png, resolver-schematic-3.png (180dpi)
- reverse-schematic-2.png (180dpi)

**ไม่แนะนำใช้ ti-resolver-sincos-feedback-excerpt.png** เพราะ crop ยาวครั้งแรกมีเศษบล็อกข้างเคียง/หัวข้อบนหาย ให้ใช้ sine-channel-excerpt ที่ตรวจครบแทน หรือภาพทั้งหน้า resolver-schematic-3.png

ต้นฉบับ PDF ที่โหลด: ti-drv3205-q1.pdf / ti-resolver-tidrvx9.pdf / ti-reverse-tidrne8.pdf

caption ที่ควรคงทุกหน้า: “ตัวอย่างวงจรจาก Texas Instruments: [รหัสเอกสาร], หน้า [เลข]. © Texas Instruments. ใช้อธิบายหลักการ ไม่ใช่ schematic/BOM ของ Honda 39980-TS4-Z51.”

สำคัญ: DRV3205 figure17 เป็น schematic ตามฟังก์ชัน ไม่ใช่ physical pin locations. ค่าชิ้นส่วนในภาพเป็นค่าตัวอย่าง TI และยังไม่ยืนยันใช้กับ Z51. Resolver TIDA-01527 มี analog crossbar ที่ต้นฉบับระบุ EXPERIMENTAL; อย่าอ้างว่าเป็น topology ใน Honda.

# หลักฐาน OEM / DENSO — P0093, 1KD-FTV และ 2KD-FTV

สถานะรอบวิจัย 1: 21 ตุลาคม 2026 (ประเทศไทย) • นักวิจัย AI • ยังไม่ใช่การรับรองรถราย VIN

## หลักการใช้ข้อมูล

แยก **เอกสารต้นทาง OEM ที่โฮสต์บนเว็บภายนอก** ออกจาก **เว็บไซต์ทางการผู้ผลิต** เสมอ ไม่อนุมานปีรถจากชื่อโฟลเดอร์เว็บ ไม่รวมค่าไฟฟ้าข้ามรุ่น และไม่เปลี่ยนคำว่า “ค่าอ้างอิง” เป็น “เกณฑ์ตัดสินอะไหล่เสีย”

## เอกสารที่อ่านแล้ว

| ID | เอกสาร / ขอบเขต | แหล่งและตำแหน่ง | ความเชื่อมั่น / ข้อจำกัด |
|---|---|---|---|
| T01 | Toyota Hilux Repair Manual (Argentina), DR201E; ECD 1KD/2KD TASA made for Argentina; P0093/78 | [PDF หน้า 05–84 ถึง 05–88](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0084.pdf) | เนื้อหา OEM reproduced บน GitLab mirror ไม่ใช่ Toyota official hosting; ยังไม่ทราบปีพิมพ์จากหน้าที่ตรวจ |
| T02 | DR201E: rail sensor และ P0087/P0190/P0192/P0193 | [PDF หน้า 05–70 ถึง 05–77](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0070.pdf) | ใช้เป็นตัวอย่าง pinout เฉพาะชุดเอกสารนี้ ตรวจด้วยหน้าวงจร 05–73 และตาราง 05–75 |
| T03 | DR201E: P0088/P1229, SCV | [PDF หน้า 05–78 ถึง 05–83](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0078.pdf) | reproduced OEM; pinout/โอห์ม/รูปคลื่นใช้เฉพาะรุ่นที่ตรงเอกสาร |
| T04 | DR201E: system description และวงจรภาพรวม | [PDF หน้า 05–5 ถึง 05–15](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0005.pdf) | reproduced OEM; มีภาพ ECM–EDU–injector, rail sensor, SCV และทางเดินน้ำมัน |
| T05 | Toyota RM1151E, ECD 1KD-FTV “From August, 2004”; P0093/78 | [PDF หน้า 05–501 ถึง 05–504](https://toyotamanuals.gitlab.io/PZ471-Z00W0-CA/htmlweb/rm/rm1151e/m_05_0501.pdf) | รุ่นรถ/ตลาดยังไม่ยืนยันจากปกเอกสาร; จงเรียก “ตัวอย่าง RM1151E 1KD ตั้งแต่ Aug 2004” ห้ามติดป้าย Hiluxไทย |
| T06 | RM1151E: rail sensor | [PDF หน้า 05–486 ถึง 05–492](https://toyotamanuals.gitlab.io/PZ471-Z00W0-CA/htmlweb/rm/rm1151e/m_05_0486.pdf) | แสดง sensor หลายสายต่างจาก DR201E จึงยืนยันว่าห้ามใช้ pinout 3 สายเป็นสากล |
| D01 | DENSO, Fourth generation common rail diesel diagnosis – suction control valve, 11 May 2023 | [เว็บทางการ DENSO](https://www.denso-am.eu/news/fourth-generation-common-rail-diesel-diagnosis-suction-control-valve), หัวข้อ Fuel pump – suction control valve | ทางการ; ใช้อธิบายหลักการ NO/NC ไม่ใช่ประกาศว่าวาล์วทุก 1KD/2KD เป็นชนิดเดียวกัน |
| D02 | DENSO, Common Rail SCV, ชนิดวาล์วและการติดตั้ง | [เว็บทางการ DENSO](https://www.denso-am.eu/it/home-prodotti/componenti-diesel/valvole-common-rail-scv), Tipologie / Installazione | ทางการ; ค่าแรงขันทั่วไปบนหน้าเว็บห้ามแทนคู่มือรถรายรุ่น |
| D03 | DENSO, Common Rail Injector | [เว็บทางการ DENSO](https://www.denso-am.eu/products/diesel-components/common-rail-injector), How common rail injectors work / Types | ทางการ; ให้หลักการสะสมแรงดันและหัวฉีด solenoid ไม่ได้ให้เกณฑ์ leak-back เฉพาะ 1KD/2KD |
| D04 | DENSO Service Manual: Toyota Hilux / Kijyang Innova / Innova 1KD/2KD, July 2004 | [PDF reproduced บน Pumba Overland](https://www.pumbaoverland.com/files/TOYOTA_Injection_manual_1KD_2KD.pdf), 68 PDF pages | กำลังตรวจภาพต้นฉบับ: text layer บนเว็บแปลงตัวอักษรผิด ไม่คัดลอกตัวเลข/เบอร์อะไหล่จาก text ที่เพี้ยน |
| D05 | DENSO: Toyota 1KD/2KD Engine, ระบบ Aug 2009 | [PDF reproduced บน service-engine](https://www.service-engine.com.ua/webroot/pdf/TOYOTA%201KD%202KD%20ENGINE.pdf), 31 PDF pages | ใช้ตรวจการเปลี่ยนยุคระบบ ต้องอ่านปกและ applicability ก่อนใช้ |
| O01 | Toyota-Tech, Diagnostic Snapshot Library | [เว็บ Toyota ทางการ](https://www.toyota-tech.eu/DiagnosticTools/dsl.aspx) | เป็นช่องทางต้นทางสำหรับ waveform/freeze frame แต่ต้อง GTS และสิทธิ์เข้าถึง ไม่ได้ใช้เป็นหลักฐานตัวเลขที่ยังไม่ได้อ่าน |
| T07 | DR201E: initialization หลังเปลี่ยน supply pump / ECM | [PDF หน้า 05–38/39](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0038.pdf) | reproduced OEM; มีเงื่อนไขและข้อยกเว้น ไม่ใช่ reset แบบเดียวทุกคัน |
| P01 | Pico Technology: CRD injector back-leakage, AGT-786 | [คู่มือผู้ผลิตเครื่องมือ](https://www.picoauto.com/library/automotive-guided-tests/pres/wps500x-pressure-transducer/AGT-786-crd-injector-back-leakage/), Further guidance | ทางการของเครื่องมือ; ใช้เฉพาะ solenoid / low return pressure ตามขอบเขต ไม่ใช่เกณฑ์ผ่าน Toyota รายรุ่น |
| D06 | DENSO Common Rail SCV (English) | [เว็บทางการฉบับภาษาอังกฤษ](https://www.denso-am.eu/products/diesel-components/common-rail-suction-control-valve-scv), How common rail SCVs work / Types | เปิดตรวจเองรอบ 2; คนละ URL กับ D02 ฉบับอิตาลี จึงแยก ID แม้เนื้อหาหลักใกล้กัน |
| D07 | DENSO Diesel Injector Replacement Warning Bulletin | [PDF ทางการหนึ่งหน้า](https://assets.denso-am.eu/production/attachments/Diesel-Injector-replacement-warning-Bulletin-English.pdf), หน้า 1 | เปิดอ่านฉบับเต็มเองรอบ 2; ไม่พบเลขฉบับ/วันที่ในหน้าเอกสาร ห้ามเติมเอง |

## ข้อสรุปพร้อมใช้ในต้นฉบับ

1. P0093 คือข้อสรุปของระบบติดตามแรงดัน ไม่ใช่ชื่อชิ้นส่วนเสีย และอาจมีการรั่วภายในแม้ไม่เห็นน้ำมันภายนอก (T01 หน้า 05–85/86)
2. อ่าน freeze frame ก่อนลบรหัส และแยก P0200 ที่ขึ้นร่วมไปตรวจวงจรขับหัวฉีดตามผัง (T01 หน้า 05–85/86)
3. ถ้ามี P1229 ร่วม อย่ามุ่งหาแรงดันต่ำอย่างเดียว: ภาวะแรงดันสูงจน limiter เปิดเป็นเส้นทางหนึ่งที่คู่มือเตือนไว้ (T01 หน้า 05–84; T03 หน้า 05–78)
4. DR201E 1KD มีค่าอ้างอิงเดินเบา 30–40 MPa และ 3,000 rpm ไม่มีโหลด 50–70 MPa; 2KD เป็น 25–35 และ 35–55 MPa ตามลำดับ (T01 หน้า 05–84) ไม่ใช่ค่ากำหนดขณะเร่งบนถนน
5. RM1151E 1KD ให้ 3,000 rpm ไม่มีโหลด 50–80 MPa และ monitor enable 500 rpm ต่างจาก DR201E จึงต้องแยกตาราง ไม่เฉลี่ยหรือเลือกค่าหนึ่งครอบทุกคัน (T05 หน้า 05–501/502)
6. DENSO ระบุ HP3 SCV มีทั้ง normally open และ normally closed การถอดปลั๊กจึงให้ผลตรงข้ามตามชนิด ห้ามเสนอเป็นวิธีทดสอบสากล (D01)

## ตารางตัวอย่างวงจรที่ยืนยันตำแหน่งได้

**ตัวอย่าง DR201E เท่านั้น — ต้องตรง connector ID, รุ่น ECU, ปี/ตลาด ก่อนใช้บนรถ**

| วงจร | ขั้วอุปกรณ์ | ขั้ว ECM | หลักฐาน |
|---|---|---|---|
| Rail sensor VC | F9–3 | E8–18 (VC) | T02 หน้า 05–73/75 |
| Rail sensor signal | F9–2 (PR) | E8–26 (PCR1) | T02 หน้า 05–73/75 |
| Sensor return | F9–1 (E2) | E8–28 (E2) | T02 หน้า 05–73/75 |
| SCV PCV+ | S8–1 | E8–2 (PCV+) | T03 หน้า 05–80/82 |
| SCV PCV– | S8–2 | E8–1 (PCV–) | T03 หน้า 05–80/82 |

หน้ามองขั้วปลั๊กต้องใช้ภาพคู่มือประกอบ อย่าแปลงเลขขาเป็นซ้าย/ขวาโดยไม่มี connector-view annotation

## ช่องว่างที่ต้องเก็บเพิ่ม

- ยังไม่ยืนยันคู่มือไทยราย VIN, ปีผลิต, เกียร์, มาตรฐานไอเสีย และ calibration ID
- ยังไม่มีเกณฑ์ P0093 เป็น MPa drop เดียวสำหรับทุก ECU; ห้ามสร้างตัวเลขขึ้นเอง
- ยังไม่มีปริมาตร leak-back mL/time/temperature ที่ยืนยันตรง injector part number; ให้แบบฟอร์มบันทึกแทนเกณฑ์ปลอม
- ยังไม่มี SCV duty/frequency/current มาตรฐานเดียวสำหรับ 1KD/2KD; ภาพคลื่นสอนต้องระบุ illustrative ถ้าไม่ใช่ค่าจากรุ่นตรง
- ไม่มีหลักฐานว่า sensor ground E2 ต่อ chassis โดยตรงทุกจุด จึงห้ามสอนต่อสาย bypass ถาวร
- ภาพ OEM และ DENSO ไม่ได้กลายเป็น public domain เพราะใส่อ้างอิง ต้องวาดภาพการสอนใหม่และระบุแหล่งหลักการ ไม่ฝัง PDF ต้นทางลงฉบับจำหน่าย

## ข้อกำกับบรรณาธิการ

เก็บข้อมูลใน claim_ledger.json และ model_matrix.json คู่กัน ตัวเลขทุกรายการต้องมีเอกสาร/หน้า/เงื่อนไข และแสดงความแตกต่างระหว่างรุ่นอย่างเห็นได้ชัด คำแนะนำวินิจฉัยของผู้เขียนที่ต่อยอดจากหลักการต้องติดป้าย “วิธีคิดวินิจฉัย” ไม่อ้างว่าเป็นขั้นตอน Toyota ทุกข้อ

## เพิ่มเติมหลังตรวจรอบแรก

- T02/T03 ดาวน์โหลดได้และตรวจภาพหน้า 05–73/80 แล้ว ตาราง pinout ด้านบนตรงกับภาพจริง เก็บภาพสำหรับตรวจหลักฐานภายในเท่านั้น ไม่ใช้เป็นภาพตีพิมพ์
- D05 อ่านปกผ่านเว็บแล้ว: เอกสาร **00400706E ออก September 2009** ส่วนตาราง applicability บอก August 2009 ทั้งสองเป็นคนละความหมาย ห้ามสลับ “เดือนพิมพ์” กับ “เดือนเริ่มใช้ระบบ”
- D05 หน้า 1–1 ระบุเปลี่ยนเพียงบางส่วนของ CRS; หน้า 1–3 มีรายการปั๊ม IMV ตลาด Thailand หลายเบอร์ จึงไม่อนุมานชนิดวาล์วจากปี 2009 เพียงอย่างเดียว
- D05 หน้า 1–6 ระบุ SCV normally closed ของ configuration ในเอกสาร; หน้า 1–8 กล่าวถึง pressure discharge valve แยกต่างหากจาก mechanical pressure limiter ต้องให้ผังระบบระบุ configuration
- Pico P01 เน้นว่าปริมาตร/แรงดัน return ขึ้นกับสภาพและการควบคุมระบบรวมทั้ง rail pressure ต้องเก็บเงื่อนไขทดสอบก่อนเทียบค่าหัวฉีด ไม่ใช้ mL เดียวครอบทุกกรณี
- DENSO D01 หัวข้อ Safety first ห้ามใช้นิ้วสัมผัสจุดแรงดันสูงระหว่างเดินเครื่อง/ทดสอบแรงดัน จัดเป็นข้อปฏิบัติที่วางติดขั้นตอนทดสอบ ไม่ซ่อนไว้ท้ายเล่ม
- การดาวน์โหลด D04 พบการตอบสนองค้างจึงยุติและลบไฟล์ศูนย์ไบต์ของรอบนี้แล้ว ส่วนข้อความเว็บ D04 ยังเพี้ยนและไม่ใช้ยืนยันเบอร์อะไหล่
- ไฟล์ dr201e_*.pdf และ *_evidence.png เป็นหลักฐานตรวจภายใน ห้ามรวมเป็น asset ตีพิมพ์หรืออัปโหลดสาธารณะโดยอัตโนมัติ ให้ใส่ลิงก์ต้นทางและภาพวาดใหม่ในหนังสือแทน

## รอบ 2 — bulletin การเปลี่ยนหัวฉีด/ปั๊ม

D07 ระบุให้ลงทะเบียน ID ของหัวฉีด **ที่มี compensation code** ด้วยเครื่องมือ genuine OEM หรือ DENSO ส่วนการเปลี่ยน fuel pump ให้ตรวจด้วยเครื่องมือดังกล่าวว่าจำเป็นต้อง reset learning หรือไม่ ไม่ใช่ประกาศให้ reset ทุกปั๊ม/ทุก SCV/ทุกรุ่น และไม่ได้ให้เมนูปฏิบัติเฉพาะ VIN บันทึกเป็น C033/C034 ใน ledger แล้ว

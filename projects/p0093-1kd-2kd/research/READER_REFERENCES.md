# แหล่งอ้างอิงและขอบเขตการนำไปใช้

หนังสือใช้เอกสารผู้ผลิตเพื่ออธิบายการทำงานและตัวอย่างวิธีตรวจ โดยแยกเอกสาร Toyota/DENSO ที่มีผู้เผยแพร่สำเนาออกจากหน้าเว็บไซต์ทางการ **ชื่อเครื่องยนต์ 1KD หรือ 2KD เพียงอย่างเดียวไม่ยืนยันว่ารถใช้วงจร อุปกรณ์ หรือค่าทดสอบชุดเดียวกัน** ก่อนใช้กับรถจริงต้องตรวจ VIN รุ่นรถ ตลาด เดือนผลิต ECU/calibration และหมายเลขอุปกรณ์ให้ตรงกัน

## เอกสาร Toyota

### T01 — P0093/78: Hilux TASA Argentina

**Toyota Hilux Repair Manual (Argentina), DR201E — ECD SYSTEM, 1KD-FTV / 2KD-FTV (TASA made for Argentina).** หน้า05–84ถึง05–88 ให้คำอธิบายP0093/78 เงื่อนไขmonitor ค่าแรงดันอ้างอิง การแยกรหัสร่วมและแนวตรวจยืนยัน ใช้เฉพาะขอบเขตเอกสารนี้ ไม่อนุมานปีรถจากชื่อโฟลเดอร์เว็บไซต์ และไม่ถือว่าเป็นคู่มือHiluxไทยทุกปี

[อ่าน T01: P0093/78 หน้า05–84–88](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0084.pdf) — สำเนาเอกสารToyotaบนเว็บไซต์อิสระ ไม่ใช่Toyota official hosting

### T02 — วงจรเซนเซอร์แรงดันราง DR201E

**DR201E, Hilux TASA Argentina, 1KD-FTV / 2KD-FTV.** หน้า05–70ถึง05–77 ครอบคลุมP0087/P0190/P0192/P0193 วงจรตัวอย่างF9–E8 และวิธีตรวจสาย หน้า05–73/75เป็นแหล่งของภาพต่อสายเซนเซอร์ในหนังสือ ต้องตรวจมุมมองขั้วปลั๊กก่อนนำเลขขาไปใช้จริง

[อ่าน T02: วงจรและการตรวจเซนเซอร์ หน้า05–70–77](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0070.pdf) — สำเนาเอกสารToyotaบนเว็บไซต์อิสระ

### T03 — วงจร SCV และรหัสแรงดันสูง DR201E

**DR201E, Hilux TASA Argentina, 1KD-FTV / 2KD-FTV.** หน้า05–78ถึง05–83 อธิบายP0088/P1229 และตัวอย่างSCVปลั๊กS8ถึงECM E8 ภาพต่อสายอ้างหน้า05–80/82 ส่วนค่าขดลวดและการตั้งสโคปเป็นข้อกำหนดเฉพาะชุดเอกสาร ไม่ใช่ค่าของSCVทุกเบอร์

[อ่าน T03: SCV และ P0088/P1229 หน้า05–78–83](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0078.pdf) — สำเนาเอกสารToyotaบนเว็บไซต์อิสระ

### T04 — การทำงานของระบบ common rail DR201E

**DR201E, Hilux TASA Argentina, 1KD-FTV / 2KD-FTV.** หน้า05–5ถึง05–15 แสดงความสัมพันธ์ECM–EDU–หัวฉีด ทางเดินน้ำมัน ปั๊ม พลันเจอร์ และSCV ใช้รองรับคำอธิบายการทำงานและภาพหลักการ โดยไม่เติมวงจรภายในECUที่เอกสารไม่ได้ให้

[อ่าน T04: System description หน้า05–5–15](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0005.pdf) — สำเนาเอกสารToyotaบนเว็บไซต์อิสระ

### T05 — P0093/78: ตัวอย่าง RM1151E 1KD-FTV

**Toyota RM1151E — ECD SYSTEM (1KD-FTV), From August, 2004.** หน้า05–501ถึง05–504 มีค่าอ้างอิงและเงื่อนไขmonitorที่ต่างจากDR201Eบางรายการ หนังสือจึงแยกตารางไว้ ไม่เฉลี่ยหรือรวมช่วง รุ่นรถและตลาดของเอกสารชุดนี้ยังไม่ยืนยันจากปกที่ตรวจ จึงไม่ติดป้ายว่าใช้กับรถไทยทุกคัน และไม่ย้ายค่าของ1KDไปใช้2KD

[อ่าน T05: P0093/78 หน้า05–501–504](https://toyotamanuals.gitlab.io/PZ471-Z00W0-CA/htmlweb/rm/rm1151e/m_05_0501.pdf) — สำเนาเอกสารToyotaบนเว็บไซต์อิสระ

### T06 — เซนเซอร์แรงดันรางแบบต่างจาก DR201E

**Toyota RM1151E — ECD SYSTEM (1KD-FTV), From August, 2004.** หน้า05–486ถึง05–492; ภาพวงจรหน้า05–490มีสัญญาณและขั้วหลายสายต่างจากตัวอย่างDR201E จึงใช้ย้ำว่าห้ามนำเลขขาของเซนเซอร์สามสายไปเสียบวัดอีกแบบโดยตรง รุ่นรถ/ตลาดยังมีข้อจำกัดเดียวกับT05

[อ่าน T06: วงจรเซนเซอร์ หน้า05–486–492](https://toyotamanuals.gitlab.io/PZ471-Z00W0-CA/htmlweb/rm/rm1151e/m_05_0486.pdf) — สำเนาเอกสารToyotaบนเว็บไซต์อิสระ

### T07 — Initialization ที่มีเงื่อนไข DR201E

**DR201E, Hilux TASA Argentina, 1KD-FTV / 2KD-FTV.** หน้า05–38/39 อธิบายการพิจารณาinitializationหลังเปลี่ยนsupply pump/ECM พร้อมเงื่อนไขและข้อยกเว้น ใช้อ้างอิงขั้นตอนในขอบเขตนั้น ไม่ใช่คำสั่งresetทุกSCVหรือทุกรุ่น

[อ่าน T07: Initialization หน้า05–38/39](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0038.pdf) — สำเนาเอกสารToyotaบนเว็บไซต์อิสระ

## เอกสารและคำอธิบาย DENSO

### D01 — หลักการ SCV และข้อควรปฏิบัติระหว่างตรวจ

**DENSO, Fourth generation common rail diesel diagnosis – suction control valve, 11 May 2023.** หัวข้อFuel pump–SCVอธิบายความต่างnormally open/closed; หัวข้อSafety firstอธิบายความเสี่ยงของการสัมผัสจุดแรงดันสูง ใช้หลักการทั่วไปที่เกี่ยวข้อง โดยไม่ย้ายข้อจำกัดการซ่อมระบบgeneration4ไปครอบKDทุกแบบ

[อ่าน D01: บทความ SCV ของ DENSO](https://www.denso-am.eu/news/fourth-generation-common-rail-diesel-diagnosis-suction-control-valve) — เว็บไซต์ทางการผู้ผลิต

### D02 / D06 — Common Rail SCV

**DENSO Common Rail SCV.** หัวข้อHow common rail SCVs workและTypes and characteristics อธิบายหน้าที่ควบคุมปริมาณเชื้อเพลิงและชนิดวาล์วตามapplication D02เป็นหน้าภาษาอิตาลี ส่วนD06เป็นหน้าภาษาอังกฤษ จึงใช้คนละIDตามURL ค่าแนะนำติดตั้งทั่วไปไม่ใช้แทนแรงบิดหรือขั้นตอนของรถเฉพาะรุ่น

[อ่าน D06: Common Rail SCV ภาษาอังกฤษ](https://www.denso-am.eu/products/diesel-components/common-rail-suction-control-valve-scv) · [อ่าน D02: ฉบับภาษาอิตาลี](https://www.denso-am.eu/it/home-prodotti/componenti-diesel/valvole-common-rail-scv) — เว็บไซต์ทางการผู้ผลิต

### D03 — หน้าที่ของหัวฉีด common rail

**DENSO Common Rail Injector.** หัวข้อHow common rail injectors workและTypesอธิบายระบบสะสมแรงดันและชนิดactuator ใช้รองรับหน้าที่พื้นฐาน ไม่ใช่เกณฑ์ปริมาตรน้ำมันไหลกลับของหัวฉีดKDทุกหมายเลข

[อ่าน D03: Common Rail Injector](https://www.denso-am.eu/products/diesel-components/common-rail-injector) — เว็บไซต์ทางการผู้ผลิต

### D04 — เอกสารระบบ Hilux / Innova ปี2004

**DENSO Service Manual: Common Rail System for Toyota Hilux / Kijyang Innova / Innova 1KD/2KD, July 2004.** เอกสาร68หน้าPDF ใช้เป็นเอกสารประกอบของระบบยุคที่ระบุ บางส่วนของข้อความที่แสดงบนเว็บอ่านผิดรูปแบบ จึงไม่ใช้ข้อความส่วนนั้นตัดสินหมายเลขอะไหล่หรือสเปกในหนังสือ; รายการที่ยังไม่ยืนยันไม่ถูกยกระดับเป็นค่าทดสอบ

[อ่าน D04: เอกสาร DENSO ปี2004](https://www.pumbaoverland.com/files/TOYOTA_Injection_manual_1KD_2KD.pdf) — สำเนาเอกสารผู้ผลิตบนเว็บไซต์อิสระ

### D05 — การเปลี่ยน configuration ของระบบ KD

**DENSO 00400706E, Common Rail System (CRS), Toyota 1KD/2KD Engine.** ออกSeptember2009; ตารางapplicabilityหน้า1–1กล่าวถึงAugust2009และรถที่ระบุ หน้า1–6/7อธิบายSCVของconfigurationนั้น หน้า1–8อธิบายการเปลี่ยนเป็นpressure discharge valve เอกสารกล่าวถึงการเปลี่ยนเพียงบางส่วนของระบบ จึงไม่ใช้ปี2009แบ่งรถทุกคันเป็นแบบเดียวกัน

[อ่าน D05: DENSO 00400706E](https://www.service-engine.com.ua/webroot/pdf/TOYOTA%201KD%202KD%20ENGINE.pdf) — สำเนาเอกสารผู้ผลิตบนเว็บไซต์อิสระ

### D07 — คำเตือนเมื่อเปลี่ยนหัวฉีดหรือปั๊ม

**DENSO Diesel Injector Replacement Warning Bulletin, หน้า1.** หัวฉีดที่มีcompensation codeต้องลงทะเบียนIDด้วยเครื่องมือที่ผู้ผลิตระบุ ส่วนการเปลี่ยนfuel pumpให้ตรวจว่าจำเป็นต้องreset learningหรือไม่ เอกสารไม่ได้ให้เมนูเฉพาะVINหรือสั่งresetทุกกรณี ไม่พบวันที่/เลขฉบับในหน้าที่อ่าน

[อ่าน D07: Replacement warning bulletin](https://assets.denso-am.eu/production/attachments/Diesel-Injector-replacement-warning-Bulletin-English.pdf) — PDFจากเว็บไซต์ทางการผู้ผลิต

## แหล่งวิธีตรวจด้วยเครื่องมือ

### P01 — การประเมิน injector back-leakage

**Pico Technology, Automotive Guided Test AGT-786: CRD injector back-leakage.** หัวข้อFurther guidanceอธิบายการไหลกลับและปัจจัยที่เกี่ยวข้อง วิธีในหน้านี้จำกัดไว้กับหัวฉีดsolenoidและระบบreturn pressureต่ำ ไม่ขยายไปใช้กับpiezoหรือระบบที่ต้องรักษาแรงดันทางกลับ และไม่ใช่เกณฑ์ผ่านToyotaรายรุ่น

[อ่าน P01: Pico AGT-786](https://www.picoauto.com/library/automotive-guided-tests/pres/wps500x-pressure-transducer/AGT-786-crd-injector-back-leakage/) — เว็บไซต์ทางการผู้ผลิตเครื่องมือ

### O01 — ช่องทางข้อมูลอ้างอิง Toyota

**Toyota-Tech Diagnostic Snapshot Library.** เป็นช่องทางมาตรฐานwaveformและfreeze-frameที่ต้องมีGTSและสิทธิ์เข้าถึง หนังสือไม่ได้อ้างตัวเลขจากรายการที่ยังไม่ได้เปิดตรวจ

[เปิด O01: Toyota Diagnostic Snapshot Library](https://www.toyota-tech.eu/DiagnosticTools/dsl.aspx) — เว็บไซต์Toyotaทางการ

### แหล่งหลักการที่บทเรียนอ้างด้วย URL โดยตรง

บทเรียนวงจรอ้าง [DENSO Common Rail Pump](https://www.denso-am.eu/products/diesel-components/common-rail-pump) และ [DENSO Diesel Components](https://www.denso-am.eu/products/diesel-components) สำหรับหน้าที่ภาพรวม และอ้าง [Pico AGT-833: Negative priming fuel pressure](https://www.picoauto.com/library/automotive-guided-tests/pressure-transducers/wps500x-pressure-transducer/AGT-833-negative-priming-fuel-pressure-diesel/) สำหรับขอบเขตการตรวจทางป้อนแบบvacuum-fed แหล่งเหล่านี้ไม่แทนคู่มือซ่อมหรือเกณฑ์ผ่านเฉพาะรถ

## ขอบเขตที่ยังต้องยืนยันก่อนลงมือกับรถจริง

1. **รถใช้ระบบชุดใด:** ตรวจVIN เดือนผลิต ตลาด ECU/calibration และเลขปั๊ม/ราง/หัวฉีด ไม่เลือกค่าจากชื่อ1KD/2KDอย่างเดียว
2. **เลขขาและหน้าปลั๊ก:** ตัวอย่างDR201Eเป็นขอบเขตArgentina ต้องมีผังและมุมมองconnectorที่ตรงรถก่อนเสียบวัด ห้ามพ่วงsensor returnลงตัวถังเป็นคำตอบสากล
3. **เกณฑ์ตรวจจับP0093:** หนังสือไม่ให้MPadropสากล เงื่อนไขmonitorและdurationไม่ใช่เกณฑ์ปริมาตรรั่ว และไม่ย้ายค่าระหว่างเอกสาร
4. **ค่าทดสอบSCV:** ต้องทราบชนิดNO/NC หมายเลขอะไหล่และนิยามPIDก่อนแปลduty/current ไม่มีfrequencyหรือcurrentเดียวครอบทุกแบบ
5. **การไหลกลับหัวฉีด:** ต้องใช้test planตรงหมายเลขอุปกรณ์ พร้อมเวลา อุณหภูมิ รอบ แรงดันและวิธีต่อ ไม่มีค่าmLเดียวตัดสินทุกหัวฉีด
6. **การเปิดระบบและประกอบกลับ:** ตรวจข้อกำหนดลดแรงดันตกค้าง เครื่องมือ แรงบิด ท่อและซีลที่ใช้ครั้งเดียวจากคู่มือรถ ห้ามเดาค่าแทนเอกสาร
7. **Coding/learningและการยืนยันผล:** ทำเฉพาะroutineที่รุ่นกำหนด ตรวจเงื่อนไขเดิมอย่างปลอดภัย การไม่มีรหัสซ้ำช่วงเดินเบาไม่รับรองการใช้งานครบทุกโหลด
8. **ภาพและตัวอย่างในหนังสือ:** ภาพหลักการและกราฟสังเคราะห์ช่วยอธิบาย ไม่ใช่ผลวัดรถจริงหรือวงจรภายในECUที่ยืนยันแล้ว ภาพวาดต่อสายเฉพาะเอกสารต้องคงป้ายapplicationและแหล่งอ้างอิงไว้

ตรวจแหล่งที่อ้างและขอบเขตข้างต้น ณ **21 ตุลาคม 2026** เอกสารผู้ผลิตอาจมีฉบับปรับปรุงเพิ่มเติม จึงต้องยืนยันฉบับที่ตรงรถก่อนใช้งาน

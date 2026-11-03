# ตรวจภาคสอนจูน LPG ผ่านโปรแกรม
ผู้ตรวจ: tuning_instruction_audit • 3 พฤศจิกายน 2026

## ขอบเขต
ตรวจหลักการใช้งานและการจับคู่หน้าจอกับคำสอน ไม่ติดตั้งโปรแกรม ไม่เชื่อมรถ ไม่เขียนค่าลง ECU ไม่ทดสอบรถจริง รออ่าน tuning-content.json และภาพฉบับจริงก่อนปิดผลตรวจ

## ข้อท้าทายที่ส่งผู้เขียนทันที

|รหัส|ระดับ|ประเด็นที่ต้องกัน|หลักฐานและคำตัดสินที่ต้องใช้|
|---|---|---|---|
|T01|Majorหากสลับความหมาย|ห้ามใช้เครื่องหมายบวก/ลบเหมือนกันทุกหน้าจอ|STAG QBOX deviation D บวกหมายถึงส่วนผสมหนากว่าอ้างอิง ส่วน conventional STFTบวกเป็นการชดเชยเมื่อบาง และบางECUกลับเครื่องหมาย ต้องแยกชนิดPID/กราฟ|
|T02|Majorหากbackupผิด|KME Save settingsลงPC ไม่ใช่ปุ่มSave modelเข้าcontroller; Factory settingsไม่ใช่undo|KMEหน้า25–27และ101–102 ระบุหน้าที่ต่างกัน ต้องเก็บสำรองก่อนแก้และตรวจรุ่น/firmwareก่อนrestore|
|T03|Majorหากจูนโหลดจากidle|Autocalibrationไม่ใช่ผลยืนยันการจูนทั้งช่วงโหลด|STAGแยกขั้นidle auto-calibrationออกจากการเก็บpetrol/gas map; การสำเร็จidleไม่พิสูจน์loadmap|
|T04|Majorหากยกค่าแผนที่|KMEModelแกนP[ms]กับG[ms]ไม่ใช่RPM/loadmapหรือcorrection[%]|ต้องเขียนแกน/หน่วยก่อนอธิบายเลื่อนจุด ห้ามยกตัวเลขในscreenเป็นค่าเริ่มทุกคัน|
|T05|Clarification|ภาพรุ่นเก่าต้องติดป้ายจริง|STAGmanualv1.6(2014-11-17)ภาพตัวอย่างACSTAG0.15.7; KMEmanualv1.0.9(17-09-2020)software5.0.2.2 ไม่เรียกlatest|
|T06|Majorหากปิดระบบเพื่อกลบอาการ|ไม่ใช้auto-clearDTC/ปิดsafety/emissionsเป็นขั้นจูน|การอ่านDTC/backup/logก่อนแก้เป็นหลักฐาน; ระบบDIใช้กลยุทธ์เฉพาะเครื่องยนต์ ไม่สอนpetrolshareเป็นศูนย์กลาง|

## แหล่งปฐมภูมิที่เปิดตรวจ

1. AC S.A., STAG-4 QBOX Controller User Manual v1.6, 17-11-2014; หน้า10,18,24,34,40,42–44 ตามเลขพิมพ์ ใช้ตรวจความหมายหน้าต่าง/ลำดับงาน ไม่คัดข้อความยาว
https://www.stag.gr/sites/default/files/stag-4_q-box_-_manual_eng_ver.1.6.pdf

2. KME, NEVO-SKY Program and Configuration Manual v1.0.9, 17-09-2020; software5.0.2.2; PDF154หน้า(เลขพิมพ์153); หน้า25–27,75–76,96–102 ใช้ตรวจSave/LoadและModel
https://kme.eu/schematy_kp_instrukcje_pobierz/schematy/EN_Software_manual.pdf

## ข้อกำกับด้านภาพและขอบเขตเนื้อหา

ภาพหน้าจอจากคู่มือเป็นdocumentation screenshot ไม่ใช่ผลจูนรถของทีม ไม่อ้างว่าเป็นเวอร์ชันปัจจุบันหรือใช้แทนโปรแกรมรุ่นอื่น ภาพUIที่ตัดมาควรมีเฉพาะส่วนที่วิจารณ์/สอน ไม่ยกหน้าคู่มือเต็มหลายหน้า ข้อความและUIที่อ้างจากแหล่งเดียวต้องคุมรวมตามขอบเขตsource ไม่ตั้งขอบใหม่ต่อบท

## รอตรวจฉบับเขียน
ยังไม่สรุปว่าภาคนี้ผ่าน จนกว่าจะอ่านไฟล์เนื้อหาและเห็นภาพที่ใช้จริง

## ตรวจภาพหน้าจอจริงรอบแรก

- STAG Monitor: เปิดดู PNG แล้วค่าภาพ RPM=0, P/G=0 จึงเป็นตัวอย่างหยุดเครื่อง ไม่ใช่หลักฐานเดินเบา Captionระบุถูก ไม่มีการแก้ตัวเลข ภาพเห็น Lambda1ใต้กลุ่ม Other[V/mA/%] จึงต้องคงข้อจำกัดไม่ใช่lambdaไร้หน่วยโดยอัตโนมัติ
- STAG Multiplier: เปิดดู PNG แกนนอนms แกนซ้ายMultiplier แกนขวาMAPpressure[bar] ฟ้า/เขียวคือแผนที่เวลาpetrolเมื่อใช้น้ำมัน/แก๊ส ตามหลักฐานหน้า24–25 Captionไม่เรียกAFRหรือgasinjtime ถูก
- KME Device: ภาพจริงมีOff-lineถูกติ๊ก ไม่ใช้เป็นผลเชื่อมรถ เมนูSave/Load/Factoryแยกหน้าที่ตามmetadataถูก
- LPGTECH Map/Table: ภาพจริงมีข้อความให้เก็บจุดสองเชื้อเพลิง ไม่ใช่ผลจูนเสร็จ Metadataอ้างเวอร์ชัน2.0.29.68และหน้าPDF8 Img14ตรง ภาพเป็นexcerptหน้าต่างที่มีmarkอ้างอิงจากคู่มือ ไม่ใช่mockupของทีม

แหล่งเพิ่ม: LPGTECH TUNING IN TECH SYSTEM (ไม่ระบุฉบับ), https://download.lpgtech.pl/files/Tuning-in-TECH-System.pdf หน้าPDF4และ8 ใช้ยืนยันลำดับautocalidleกับmapแยกขั้นและสถานะภาพ ไม่ยกเกณฑ์lambdaแบบnarrowbandในเอกสารมาใช้กับwidebandทุกคัน

# วิจัย PCB EPS — Toyota / Nissan (14 พ.ย. 2026)

## หลักฐานที่นำไปใช้ได้

### Nissan March / Micra K12 2003–2008
- แหล่ง primary สำหรับข้อมูลของผู้ขาย: https://www.jadausa.com/en-us/eps/devices/20
- แผนที่ W-S0020, ประเภท EPS-C, test cable Z-35007 (7-C). นี่เป็นรหัส catalog ไม่ใช่ OEM ECU part number; ไม่ได้แยกตลาด/รุ่นย่อยให้ยืนยันทุกคัน
- ภาพเต็มที่ตรวจ PIL.verify() และเปิดดูจริงแล้ว: `output/research-assets/nissan-020-2F.jpg` (1000×636)
- URL ภาพ: https://emmetec.blob.core.windows.net/70px/020_2F.jpg
- ภาพ 2F เป็น sensor-related board/ชุดกลไกวงกลม ไม่ใช่ภาพ main power PCB และไม่ควรชี้ MOSFET/MCU ลงบนภาพนี้
- ตารางผู้ขายแยก board/side: 1F มี EEPROM; 1R มี relay, CAN chip, motor-controller, MOSFET, voltage regulator; 2F ตำแหน่ง D2 ระบุ relay; 2R มี Hall sensor.
- ตัวอย่าง mapping ผู้ขายที่มีประโยชน์: 1R C4 = CAN (W-01011 หรือ W-01022 ตามรายการ); 1R A3/B3 = motor-controller W-01016; 1R D3 = regulator W-05043; 1R A2/B2/C2/D2 = power-device items. การมีหลาย SKU บริเวณเดียวไม่พิสูจน์ว่าใส่พร้อมกันทั้งหมด
- รหัส W-xxxxx คือ SKU ผู้ขาย ไม่ใช่ marking ผู้ผลิต semiconductor, ห้ามนำไปอ้าง datasheet chip หรือ G/D/S pinout
- printed catalog index ระบุหน้า 239–241/62 สำหรับ W-S0020; **ยังไม่ได้ยืนยันเลขหน้า PDF ด้วยตัวอ่านไฟล์เต็ม**. ใช้เว็บรายละเอียดและชื่อภาพเป็น citation หลัก

### Toyota Yaris / Vitz / Vios กลุ่ม W-S0029
- เว็บข้อมูลผู้ขาย: https://www.jadausa.com/en-us/eps/devices/29
- catalog ระบุ Vios 2007–2013, Yaris 2005–2011 และรุ่นอื่นร่วมกลุ่ม; EPS-C, cable Z-35013 (15-C)
- ไม่ได้ระบุ OEM ECU suffix/ตลาดเดียวอย่างแน่ชัด ต้องเทียบภาพบอร์ดและฉลาก ECU ก่อนผูกกับรถจริง
- ภาพต้นทาง: https://emmetec.blob.core.windows.net/70px/029_1F.jpg , https://emmetec.blob.core.windows.net/70px/029_1R.jpg , https://emmetec.blob.core.windows.net/70px/029_2F.jpg
- map ผู้ขาย: 1F A4 EEPROM W-05171; 1R C3/C4 relay W-01036; 2F A1/A3/B2/B3 MOSFET products W-05155 หรือ W-05347
- รายการนี้บอกประเภท/บริเวณ ไม่ใช่ full schematic, netlist, ความเสียหายประจำรุ่น หรือคำสั่งเปลี่ยนทันที
- ยังไม่ยืนยัน printed mapping page และ PDF page; ไม่ควรใส่เลขหน้าโดยเดา

## วิเคราะห์หน้างานที่รองรับจาก board map
1. เลือก case จากปี/รหัส ECU/รูป PCB ที่ตรง ไม่เลือกจากชื่อยี่ห้อเพียงอย่างเดียว
2. ถ่ายทั้งสองด้านและวางเดือย/ขั้วเหมือนภาพ catalog ก่อนใช้ grid; grid A1/B2 ไม่ใช่เลข connector pin
3. จุดที่ระบุเป็น relay: ตรวจรอยร้อน/รอยต่อและเปิด datasheet จาก marking จริงก่อนวัด coil/contact; ห้าม bridge contact
4. จุดที่ระบุ MOSFET: อ่าน marking จริงและเปิด datasheet เพื่อยืนยันขา; diode-mode ในวงจรให้เพียงเบาะแส เพราะมีทางขนานและประจุ gate
5. จุด regulator/CAN/controller: ไม่ทราบ rail voltage/enable/pinout จากชื่อหมวด ต้องอ่าน marking และตามวงจรจริงก่อนวัดขณะทำงาน
6. EEPROM ใน map ไม่ใช่หลักฐานว่า EEPROM เสีย และไม่รับรองว่าคัดลอกข้อมูลข้ามกล่องได้

## ความมั่นใจและภาพสำหรับปก
- main PCB schematic โรงงาน: ยังไม่พบ
- PCBภาพจริงพร้อมหมวดตำแหน่งจากผู้ขาย: พบ
- chip marking / official datasheet ที่ผูกกับบอร์ดสองcase: ยังไม่อ่านยืนยัน จึงไม่เสนอเบอร์ชิปทดแทน
- ภาพ Nissan 020-2F ที่สมบูรณ์ใช้เป็นภาพกรณีศึกษานี้ได้ โดยคงเลข grid/credit; ไม่แนะนำเป็นภาพ main power PCB เพราะเป็นอีกชุดย่อย
- catalog PDF แหล่งเต็ม https://www.seauto.es/wp-content/uploads/2022/09/emmetec-EPS_62_preview_2021_Bombas-Hidraulicas.pdf มีลิขสิทธิ์ ORPAV; สรุป/อ้างลิงก์และใช้ภาพที่เกี่ยวกับการวิเคราะห์เฉพาะส่วน ไม่คัดลอกหลายหน้าทั้งเล่ม
- ไฟล์ `emmetec-eps-catalog.pdf` ใน research-assets เป็น partial download และ **ห้ามใช้เป็น PDFสมบูรณ์**; ภาพ JPG ที่ไม่มีคำว่า ready นอกจาก Nissan0202F อาจเป็น partial เช่นกัน

## ข้อมูลรถระดับ wiring สำรอง (ไม่ใช่ PCB)
- 2007 Toyota Yaris NCP91/93, EWD EM01V0U (ปกยืนยันรุ่น/ปี): https://device.report/m/a8e4732e8017a2cc0ea5293f3e1d658056c93c843a39d16245be584522d1decc.pdf . EPS หน้าเอกสาร 172–175; ปลั๊ก A19 / D31 / b1 / c1. ห้ามผูกกับ W-S0029 โดยอัตโนมัติ
- Toyota Yaris PS repair excerpt: https://www.mgaguru.com/mgtech/steering/pdf/power_steering_yaris.pdf มี terminals PS-24 แต่ excerptไม่มีปกให้ยืนยันรุ่นปี จึงไม่อ้างเป็น 2007 โดยเดา
- 2014 Nissan Sentra NAM, revision October2013 STC: https://www.nicoclub.com/service-manual?fsm_download=Sentra%2F2014%2FSTC.pdf เป็นคนละรุ่นกับ MicraK12 ห้ามยืม pinout มาผสม

## อัปเดตภาพ Toyota สมบูรณ์ (พร้อมใช้)
- `output/research-assets/toyota-029-1F-ready.jpg` 1000×1033 ผ่าน PIL.verify และเปิดตรวจด้วยตา
- `output/research-assets/toyota-029-1R-ready.jpg` 1000×884 ผ่าน PIL.verify และเปิดตรวจด้วยตา
- รหัส PCB ในภาพอ่านได้ `112931-0301`
- ภาพ 1R เห็นรีเลย์ OMRON `G8SE-1A4-E`, `12VDC`, `225Ω` บนตัวรีเลย์ทั้งสองตัว เป็นเพียงข้อมูล marking ที่เห็น ไม่ใช่การอนุมัติอะไหล่ทดแทนหรือยืนยัน pinout
- ไม่อ่านเบอร์ MCU/ASIC จากภาพที่คลุมเครือ และไม่ผูก MOSFET board2F กับแพ็กเกจที่ไม่มีภาพครบ
- ไม่จำเป็นต้องรอ PDFใหญ่อีก ใช้เว็บรายละเอียดและภาพเหล่านี้อ้างหลักฐาน case ได้

# เพิ่มยุโรปในหนังสือ mytech — เน้น PCB (14 พฤศจิกายน 2026)

## สถานะหลักฐานและไฟล์พร้อมใช้

ตรวจทุกไฟล์ด้วย PIL.verify(), decode ด้วย Image.load() และเปิดภาพดูด้วยตาแล้ว **ครบ 5 ภาพ ไม่ใช่ partial**:

|ไฟล์|ขนาด|สิ่งที่เห็นจริง|
|---|---|---|
|output/europe-assets/080_1F-ready.jpg|1000×778|MINI logic/control PCB ด้าน 1F มี IC, passive และ capacitor|
|output/europe-assets/080_1R-ready.jpg|1000×811|ด้าน 1R ของ control PCB; อย่ากลับภาพเพื่อเดาพิกัด|
|output/europe-assets/080_3F-ready.jpg|1000×875|แผ่นกำลัง 3F เห็น power devices, ทางกระแส และชิ้นส่วนพิมพ์ 2R5|
|output/europe-assets/082_1F-ready.jpg|1000×2474|ชุด power/filter/contact และ capacitor; ไม่ใช่ภาพ logic PCB|
|output/europe-assets/082_2F-ready.jpg|1000×1702|logic/control + power module/interconnect ของ VAG; อย่าสัมผัส bond wire|

ต้นทางภาพทุกรูป: `https://emmetec.blob.core.windows.net/70px/<ชื่อก่อน-ready>.jpg` เช่น https://emmetec.blob.core.windows.net/70px/080_3F.jpg . โฟลเดอร์ชื่อ70px แต่ภาพต้นฉบับที่ได้มีความกว้าง1000pxจริง

หลักฐานระดับ **ภาพจริง + map ผู้จัดทำ catalog** ไม่ใช่ OEM schematic, netlist, PCB layout file หรือผลวัดบอร์ดจริง และไม่ได้ยืนยันกล่องทุกตลาด/ทุก revision ของรถปีนั้น

## Case E1 — MINI EPS-R, W-S0080

- Primary supplier page: https://www.jadausa.com/en-us/eps/devices/80
- สำเนา HTML ที่อ่านตรวจ: output/europe-assets/case-80.html
- ชนิดใน catalog: **EPS-R** (electric rack), cable catalog Z-36009 (27-R)
- รุ่น/ปีตามผู้ขาย: MINI R55/R56/R57/R58/R59/R60/R61, 2008–2016. เป็นช่วงรวมในcatalog ไม่รับรองว่ารถทุกbodyผลิตครบทุกปีนั้น
- ไม่ใช่ MINI R50/R52/R53 แบบปั๊มไฟฟ้าช่วยไฮดรอลิก และไม่ใช่หลักฐานสำหรับรถ BMW E/F/G รุ่นอื่น

### Map ที่ใช้ได้จากแหล่ง (คงตัวเลขด้าน/กริดเดิม)
|ภาพ/กริด|ชนิดที่ผู้ขายระบุ|SKU catalog|
|---|---|---|
|1F B2|Motor controller|W-05258|
|1R D1|CAN chip|W-01022|
|1R A3|Dual voltage comparator|W-05130|
|1R B1|Dual operational amplifier|W-05239|
|3F A1/A2/B1/B2/C1/C2/C3|MOSFET items|W-05216|

SKU ไม่ใช่เบอร์ผู้ผลิต semiconductor; พิกัดหนึ่งอาจครอบคลุมหลายชิ้นหรือหลายrevision ไม่บอกpinout/ตำแหน่งG-D-S. ภาพ3Fเห็นอุปกรณ์พิมพ์2R5 แต่ **ห้ามแปลงหน่วย/กำหนดค่าโอห์มหรือหน้าที่จากmarkingอย่างเดียว**. รูป1Fมีสติกเกอร์บนชิปใหญ่ จึงไม่อ่านสติกเกอร์เป็นเบอร์MCU. เบอร์ชิปอื่นไม่คมพอให้ผูก official datasheet อย่างแน่นอน

### วิธีตรวจแบบช่างที่รองรับได้
1. ยืนยันรูปแผ่นจริงตรงด้าน1F/1R/3F ก่อนทำแผนที่; แยกcontrol boardกับpower board
2. อาการไม่สื่อสาร: ตรวจไฟ/กราวด์และmodeจากเบอร์จริงก่อนตรวจบริเวณCANที่mapระบุ; mapไม่ได้บอกแรงดันหรือค่าtermination
3. อาการภาคกำลัง: ตัดไฟและยืนยันไม่มีแรงดันค้าง ตรวจสาย/มอเตอร์ภายนอกก่อนเปรียบเทียบแขนกำลังของ3F
4. diode-modeที่ต่างกลุ่มยังไม่ฟันธงMOSFET เพราะอาจมีทางขนาน/ประจุgate ต้องอ่านเบอร์และวงจรจริงก่อนแยกวัด
5. ไม่แนะนำเปลี่ยนชิปตามSKU, reflowทั้งแผ่น, bypassrelay หรือป้อนgateเพื่อทดสอบ

## Case E2 — VAG EPS-R, W-S0082

- Primary supplier page: https://www.jadausa.com/en-us/eps/devices/82 (บางครั้งwebtoolcacheเข้าไม่ได้ แต่ดาวน์โหลดHTMLโดยตรงสำเร็จ)
- สำเนา HTMLที่ตรวจ: output/europe-assets/case-82.html
- Primary indexยืนยันชื่อรุ่นร่วม: https://www.emmetec.com/en-us/eps/devices
- ชนิดcatalog **EPS-R**, cable Z-36014 + Z-36014A (35-R)
- รุ่นตามcatalog: Volkswagen Tiguan2007–2016, PassatCC2008–2016, Sharan2010–, Santana2012–, AudiQ32011–2018, SEATAlhambra2010–2015
- **ไม่เขียนว่าGolf/AudiA4/BMW** เพราะหน้านี้ไม่ได้ระบุ; รถเหล่านั้นอาจใช้ระบบต่างแบบ

### Map เลือกเฉพาะภาคสำคัญ
|ภาพ/กริด|ชนิดที่แหล่งระบุ|SKU|
|---|---|---|
|2F B4|EEPROM|W-05102|
|2F C4|Crystal|W-05159|
|2F C5|Motor controller|W-05258|
|2F A6|Dual operational amplifier|W-05389|
|2F C2|Voltage regulator items|W-05401 / W-05573|

**จุดคลาดเคลื่อนแหล่งที่ต้องคงไว้:** แถวCANchip W-05181 เขียนกริด **3C** ในHTML ไม่ใช่C3ตามรูปแบบแถวอื่น. ไม่แก้เงียบเป็นC3แล้วชี้ชิป ควรระบุว่าcatalogพิกัดไม่สม่ำเสมอและรอยืนยันก่อนระบุตัว. เช่นกัน C2 มีทั้งregulatorและMOSFETในตาราง ไม่แปลว่าชิ้นเดียวกันทำหน้าที่ทั้งหมด

### ภาพจริงและการตรวจ
- 1F เป็นชุดทางกำลัง/กรอง/หน้าสัมผัส มีcapacitorโลหะที่พิมพ์ **3300µF 25VDC** ตามภาพ แต่แรงดันพิกัดcapacitorไม่ใช่แรงดันที่ต้องจ่ายและไม่ใช่การอนุมัติอะไหล่แทน
- 2F แยกcontrol circuitryกับโมดูลกำลัง/จุดเชื่อมเส้นลวดที่ภาพส่วนล่าง; **ห้ามขูด เจาะ เคลื่อน bond wire หรือถอดgel/เคลือบด้วยการทดลอง**
- บริเวณcontroller/regulatorควรเริ่มอ่านmarkingจริงแล้วเปิดdatasheet ไม่ใช้ขนาดpackageเดาหน้าที่
- รีเลย์/ทางกำลังที่ขาดหรือร้อนต้องตรวจcontactและรอยต่อพร้อมสาเหตุโหลด ห้ามbridgeให้ทำงาน
- ยังไม่มีMCU/driver/CANmarkingที่อ่านยืนยันครบsuffix, ไม่มีแรงดันทดสอบตรงรุ่น และไม่มีschematicโรงงาน: จึงไม่ผูกเบอร์ชิป/datasheetหรือtest-pointขึ้นเอง

## สิ่งที่ยังไม่พบและขอบเขตยุโรป
- ยังไม่พบ internal schematic โรงงานแบบอุปกรณ์ครบสำหรับสองcaseนี้
- Official chipdatasheets ในเล่มเดิมใช้เป็นตัวอย่างหลักการได้ แต่ยังไม่ผูกเป็นชิปของMINI80/VAG82
- MINI80เป็นตัวแทนกรณีศึกษาจากMINI ไม่ใช้คำว่าเป็นหลักฐานPCBรถBMWทุกรุ่น
- AudiA4/A5/Q5มีsuppliermap W-S0126 อีกชุด แต่ **ไม่ได้เลือกใช้และไม่ได้ดาวน์โหลดรูปมาปะปน** กับW-S0082
- Emmetec EPS-P หมายถึงelectricpumpในcatalog ไม่ใช่pinion EPS เสมอ; ต้องแยกEPS-R/EPS-C/EHPSให้ถูก

## แนวแบ่งภาคยุโรป8หน้า
1. เลือกประเภท/ปี/revisionก่อนใช้case; แยกMINIR-seriesกับBMWอื่นและEHPS
2. MINI control PCB1F/1R (ภาพคู่และmapจุดควบคุม)
3. MINI powerboard3F (เต็มหน้า+ตรวจแขนกำลังแบบไม่จ่ายไฟ)
4. MINIแผนซ่อมอาการ→วงจร→วัด→ข้อจำกัด
5. VAGชุดpower/filter1F (อย่าเรียกlogicboard)
6. VAGcontrol/powermodule2F (เต็มหน้ากับคำเตือนinterconnect)
7. VAGmapที่ยืนยันและความคลาดเคลื่อน3C/C3; ห้ามใช้pinoutข้ามรุ่น
8. ใบงาน/แหล่งอ้างอิง/ตารางสิ่งที่ยังไม่มีหลักฐาน

## เครดิตภาพ
ภาพcatalogลิขสิทธิ์ORPAV/Emmetec; ใช้เฉพาะภาพเกี่ยวกับการวิเคราะห์พร้อมแหล่งข้างภาพ คงเลขgrid/ด้านเพื่อไม่บิดตำแหน่ง ไม่คัดลอกcatalogทั้งเล่ม

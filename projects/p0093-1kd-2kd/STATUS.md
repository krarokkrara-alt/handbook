# สถานะหนังสือ P0093 1KD 2KD

## กำหนดส่ง

21 ตุลาคม 2569 เวลา 07:00 น. Asia/Bangkok = 2026-10-21T00:00:00Z

## งานต่อเนื่อง

ตั้ง thread automation แล้ว รหัส p0093-1kd-2kd-07 รอบ :00 และ :30 สิ้นสุดตามกำหนด สถานะ ACTIVE ณ เริ่มงาน ต้องเปิดเครื่องและแอปไว้ให้เข้าถึงไฟล์ในเครื่องได้

## รอบเริ่มต้น 00:35 ถึง 00:45

- สร้างโครงการเฉพาะ แยกจากหนังสือ ECU เดิม
- เริ่มทีม p0093_oem_research, p0093_circuit_author, p0093_diagnostic_editor
- นักวิจัยกำลังเทียบเอกสาร Toyota DR201E และ RM1151E กับเอกสาร DENSO ต้องตรวจขอบเขตความใช้ได้ก่อนใส่ตัวเลข
- เนื้อหาและวงจรยังอยู่ระหว่างวิจัย ไม่มี PDF/DOCX ฉบับตรวจเสร็จในโครงการใหม่นี้

## งานถัดไป

1. ตรวจไฟล์ที่ทีมบันทึกในresearch/circuits/manuscript และข้อขัดแย้งระหว่างเอกสาร
2. รวมclaimledgerกับmodelmatrix แล้วทำbibliographyที่สืบกลับได้
3. ขยายวงจรและตารางวินิจฉัยตามข้อยืนยัน ไม่ใส่pinoutหรือค่าที่เดา
4. เขียนmaster manuscriptตามBOOK_PLAN.md และเลือกภาพให้ทุกบทสำคัญ
5. ก่อน06:00เริ่มรวมเล่ม/สร้างไฟล์อ่านและแก้ไขได้ ตรวจทุกหน้าก่อนส่ง

## ช่องว่างที่ต้องยืนยัน

- ยังไม่ได้กำหนดรุ่นรถ ปี ตลาด และ ECU เดียวสำหรับทั้งเล่ม จึงต้องแยกความใช้ได้ตามแหล่ง
- ยังไม่ยืนยันpinoutและค่าทดสอบทุกระบบ ห้ามยกระดับข้อมูลทั่วไปเป็นข้อกำหนดตรงรุ่น
- ไม่อ้างว่ามีการทดสอบฮาร์ดแวร์จริงหรือรับรองผลซ่อมจริงจากเอเจนต์

## ผลงานเริ่มต้นที่บันทึกแล้ว

- research/OEM_SOURCES.md มีแหล่งToyotaและDENSO พร้อมขอบเขตเอกสารและหน้าที่ตรวจ
- manuscript/DIAGNOSTIC_WORKFLOW.md มีเนื้อหาวิเคราะห์รอบแรกแล้ว กำลังเพิ่มREPAIR_MATRIX.md
- circuits/ มีภาพSVGและPNGรอบแรก10ภาพ:ทางน้ำมัน feedback sensor SCV NC/NO วาล์วราง หัวฉีด กราวด์และสมดุลการไหล
- รอบตรวจSVG03พบภาพเครื่องวัดต้องแสดงsignal-to-returnจริง ไม่ต่อreturn-to-return ได้ส่งให้ผู้เขียนแก้แล้ว ต้องตรวจไฟล์ล่าสุดก่อนใช้
- ยังต้องปรับหัว/คำอธิบายภาพเป็นภาษาไทยหรือสองภาษาและทบทวนทุกภาพก่อนนำจัดเล่ม
- รหัสอ้างอิงข้ามทีมยังต่างรูปแบบ เช่น T01/T1 และ D01/D1 ต้องnormalizeในmaster bibliography ไม่รวมโดยเดาความหมาย
- claim_ledger.json และmodel_matrix.json ให้ตรวจว่าOEMagentสร้างแล้วหรือยัง ห้ามอ้างว่าครบถ้าไฟล์ยังไม่ปรากฏ

## แนวปฏิบัติการเผยแพร่

PDFคู่มือOEMที่ดาวน์โหลดเป็นเอกสารวิจัยในเครื่องและถูกgitignore ห้ามนำขึ้นrepositoryโดยไม่มีสิทธิ์เผยแพร่ ให้ใช้ลิงก์และภาพวาดต้นฉบับที่อธิบายขอบเขตแทน หนังสือใหม่นี้ยังไม่ควรถูกระบุว่าเป็นฉบับเสร็จหรือแทนหนังสือเดิม

## อัปเดตหลักฐานรอบแรก

OEMagentบันทึกmodel_matrix.jsonและclaim_ledger.jsonแล้ว รายงาน27claims ให้ใช้ไฟล์จริงตรวจรายการและapplicabilityก่อนรวมเลขขา/สเปก ยังต้องทำtechnicalreviewกับคัดไทยdiagram และปิดประเด็นวิธีresetที่มีข้อยกเว้นตามคู่มือ

## รอบต่อเนื่อง 2026-10-21 01:00 +0700

- ตรวจต้นฉบับที่แต่ละฝ่ายส่งแล้ว: workflow12ส่วน repairmatrix15กิ่ง/8เคส และทะเบียนหลักฐาน32ข้อ
- สร้าง manuscript/MASTER_DRAFT.md รวมเนื้อหาปัจจุบันกับวงจร12ภาพและแหล่งอ้างอิง เป็นฉบับทำงาน ไม่ใช่ฉบับส่งมอบ
- สร้าง tools/assemble_master.py สำหรับรวมใหม่หลังทีมแก้ต้นฉบับ โดยแยกรหัสDIAG:T1/D1ไม่ปนทะเบียนฝ่ายวิจัย
- ตรวจลิงก์รูป/ไฟล์ภายในmasterแล้วไม่ขาด และJSONปัจจุบันอ่านผ่าน ไม่พบอักขระreplacementในไฟล์ต้นฉบับ
- คำอธิบายSVG03/08ถูกแก้แล้วตามรายงานทีม แต่ต้องตรวจภาพรอบใหม่พร้อมQAของฝ่ายวงจรก่อนปิดเล่ม

### งานที่มอบหมายรอบถัดไปแล้ว

- p0093_oem_research ตรวจข้ามต้นฉบับกับหลักฐานแบบread-only แล้วเขียนresearch/CROSS_REVIEW.md และช่วยแผนที่รหัสอ้างอิงตามURL
- p0093_circuit_author ขยายภาพ13–16ตามแผนและเขียนQA.md ตรวจครบทุกภาพ ไม่เพิ่มค่าOEMที่ไม่มีหลักฐาน
- p0093_diagnostic_editor ขยาย8เคสเป็นmanuscript/CASE_WORKBOOK.md พร้อมเฉลยแยกและsourcealias_map.json

### ลำดับของcoordinatorเมื่อรอบถัดไปเริ่ม

1. อ่านCROSS_REVIEWและปิดประเด็นที่กระทบความถูกต้องก่อนรวมตัวเลข/ขั้นตอนเฉพาะรุ่น
2. ตรวจภาพล่าสุดและQAไฟล์จริง ทบทวนsensorหลายสายกับscopeของDR201Eไม่ให้ปนกัน
3. รวมCASE_WORKBOOKและภาพใหม่ด้วยassemble_master แล้วพัฒนาบทเรียนวงจรเป็นลำดับอ่าน ไม่ใช้เพียงatlasอย่างเดียว
4. เริ่มทำต้นแบบจัดเล่มที่ตรวจง่ายล่วงหน้า ไม่รอ06:00ค่อยเริ่มระบบผลิตไฟล์
5. ยังไม่มีPDF/DOCXฉบับใหม่ที่ตรวจครบ จึงห้ามประกาศส่งมอบเสร็จ

## รอบต่อเนื่อง 2026-10-21 01:37 +0700

- อ่านCROSS_REVIEWและรับคำยืนยันแก้XR01/XR02แล้ว วงจร16ภาพมีQAจากผู้เขียน ไม่ใช้หลักฐานนี้แทนตรวจหน้าA4
- รวมCASE_WORKBOOK8กรณี บทเรียนวงจร8ตอน FIELD_WORKSHEETS6แบบ และVERIFIED_SPEC_TABLEจากclaimledger35ข้อเข้าต้นฉบับหลัก
- Normalizeการอ้างT1/T2/D1–D4เป็นcanonicalIDsด้วยsource_alias_mapโดยassertURLตรงregistry ไม่จับคู่จากชื่อย่อ
- MASTER_DRAFTปัจจุบัน232090bytes ภาพ16จุด ลิงก์ไฟล์ภายในขาด0จุด
- สร้างtools/build_prototype.pyและrender_prototype.cjs พร้อมproduction/P0093_Prototype.docx/PDFต้นแบบ64หน้า ใช้sharedsemanticblocks ไม่ใช่ฉบับปิดเล่ม
- เปลี่ยนตารางมากกว่า4คอลัมน์เป็นบัตรทีละรายการ แก้หน้าหัวเรื่องว่าง/หัวภาคซ้อนในรอบแรก แก้sourcecaptionภาพ08ที่ว่างและไม่แสดงชื่อไฟล์MDภายในในตัวอ่าน
- เปิดดูตัวอย่างหน้าPDFรอบแก้แล้ว5หน้า เนื้อหาอ่านได้ แต่ยังไม่ตรวจทุกหน้าจึงไม่ส่งมอบ
- ตัวแปลงDOCXมาตรฐานไม่มีsoffice.exeและcleanuppermissionerror จึงใช้PDFChromiumต้นแบบสำหรับตรวจเนื้อหา/รูปเล่ม DOCXยังไม่มีvisualapproval ห้ามระบุว่าDOCXตรวจทุกหน้าแล้ว

### งานกำลังตรวจสำหรับรอบ02:00

- circuit_author: เปิดดูPDFหน้า1–20 เน้นวงจร16ภาพย่อA4 อ่านlabelและภาพวัดจริง เขียนproduction/reviews/CIRCUIT_LAYOUT_REVIEW.md
- diagnostic_editor: เปิดหน้า21–42 ตรวจบัตรวิธีแก้และการตัดหน้า เขียนDIAGNOSTIC_LAYOUT_REVIEW.md
- oem_research: เปิดหน้า43–64ตรวจworkbook/sources/specและความตรงรุ่น เขียนOEM_LAYOUT_REVIEW.md
- ใช้SHA256ในproduction/prototype_status.jsonยืนยันว่าQAอ้างไฟล์รุ่นเดียวกัน ห้ามแก้PDFระหว่างตรวจโดยไม่แจ้งทีม

### สิ่งควรทำต่อหลังรับผล

1. ปิดประเด็นความอ่านง่ายและtechnicalissuesจากQAก่อนขยายเนื้อหา
2. ลดกรณีA–Hแบบสั้นในrepairmatrixให้เป็นindexเพราะมีworkbookเต็มแล้ว ตัดmetadataงานบรรณาธิการออกจากข้อความสำหรับผู้อ่าน
3. ปรับแทรกภาพใกล้บทที่กล่าวถึง ไม่ปล่อยatlasอยู่ต้นเล่มทั้งหมดหากทำให้อ่านต่อยาก
4. สร้างสารบัญใช้ชื่อหัวข้อและเลขหน้าฉบับPDFจริง พร้อมรายการขอบเขต/สิ่งยังไม่ยืนยันที่อ่านง่าย
5. ตรวจDOCXด้วยวิธีที่เหมาะหรือคงเป็นeditablecompanionโดยไม่รับรองpaginationเท่าPDF
6. ค่อยพัฒนารูปจริง/ภาพเจาะส่วนที่มีสิทธิ์และมีประโยชน์ต่อP0093 ไม่คัดหน้าOEMเต็มมาประกอบเป็นหนังสือใหม่

## รอบต่อเนื่อง 2026-10-21 02:42 +0700

- ปรับแผ่นวงจรทั้ง16แผ่นเป็นA4แนวนอนด้วยprint assetsแยกจากต้นฉบับ: labelเล็กสุด9.038–9.313ptตามผลวัดจริง ฝ่ายวงจรเปิดตรวจครบหน้า2–17แล้ว CL01ปิด; ภาพ03/08การต่อDMMถูกต้อง ภาพ09ระบุNCสมมติและ11/12คงscopeDR201E
- R2ต้นแบบ71หน้าได้รับvisual reviewครบช่วง30–60และ61–71 โดยรายงานLANDSCAPE_PLATE_REVIEW, WORKBOOK_R2_REVIEW, REFERENCES_R2_REVIEWในproduction/reviewsอ้างhashของรุ่นนั้น ไม่ถือว่าอนุมัติไฟล์ใหม่อัตโนมัติ
- ตัดข้อมูลภายในออกจากตัวอ่าน ใช้READER_REFERENCES.mdและcanonical source IDs16รายการ ตรวจ17claim IDsของตารางสเปกตรงledger35ข้อ
- แก้แบบ03จาก3เป็น2recordsพร้อมคำแนะนำสำเนาเพิ่ม แสดงlabelสิ่งที่วัดเหนือช่องว่าง แก้ความกว้างแบบ01เป็น35:65 แก้อ้างอิงท้ายworkbookจากช่วงรหัสย้อนเป็นรายการcanonical และแก้โครงสร้างเลขหน้าDOCX
- rebuildล่าสุด70หน้า SHA256 4c043663f4cd85643cf720b856cf78b982010f7e6120e98c3ab123df60f4fcf6 ภาพขาด0จุด อัปเดตprototype_status.jsonแล้ว ยังเป็นต้นแบบไม่ส่งมอบ
- ฝ่ายdiagnosticกำลังตรวจแบบฟอร์มR3และฝ่ายOEMตรวจportraitบทเรียนหน้า18–29ที่ยังไม่เคยเปิดครบ ห้ามแก้PDFระหว่างตรวจ

### งานรอบถัดไป
1. รับFORMS_R3_REVIEWและLESSONS_R3_REVIEW ปิดปัญหาแบบ03ครบหน้าเดียวและหัวข้อช่องวัดจริง
2. ทำสารบัญพร้อมเลขหน้าPDFจริงและnavigation โดยคง16วงจรอ่านได้ ไม่ลดภาพให้เล็กอีก
3. DOCXยังไม่visualapprovedเพราะsofficeไม่ติดตั้ง ต้องหาวิธีตรวจWordอย่างจำกัดเวลาหรือระบุเป็นeditablecompanionชัดเจน
4. ก่อนส่งมอบทำQAฉบับสุดท้ายทุกหน้า พร้อมระบุช่องว่างVIN/model/yearและตัวเลขที่ยังไม่มีหลักฐานตรงรุ่น
5. ยังไม่แก้หนังสือECUเดิม ไม่แก้syncedsources ไม่เผยแพร่PDFคู่มือOEMวิจัย และยังไม่pushโครงการใหม่

## รอบต่อเนื่อง 2026-10-21 03:12 +0700

- รับFORMS_R3_REVIEW: เปิด48–59ครบ12หน้า แบบ01ช่องตอบกว้างขึ้นผ่าน แบบ03สองrecordsพร้อมlabelครบหน้าเดียว และ6forms52–57ครบหนึ่งแบบต่อหน้า ปิดข้อค้างหลัก
- รับLESSONS_R3_REVIEW: เปิด18–29ครบ12หน้า ไม่มีscopeผิด/ตารางล้น พบLR01หัวบทเรียน5ค้างท้าย22 จึงแก้ให้ขึ้นหน้าใหม่พร้อมเนื้อหาในbuilderแล้ว
- เพิ่มtools/build_navigation.pyและrender_contents.cjs ใช้PDFoutlineที่Chromiumสร้างระบุpageจริง ไม่พึ่งextractข้อความไทยที่มีอักขระซ้ำจากfontshaping
- สร้างproduction/P0093_ReadingProof.pdf71หน้า: ต้นแบบ70หน้า+สารบัญหน้า2หนึ่งหน้า มี23bookmarks และfooterเลขหน้าจริงใหม่ทุกหน้า ไม่ใช้เลขเดิมก่อนแทรกสารบัญ
- เปิดตรวจภาพสารบัญจริงแล้ว ตาราง23รายการอ่านได้ครบในหน้าเดียว SHA256ปัจจุบันde141f977a9fd3105e581615e9614c0fea4fc96448978066d6f4d1d8890e5044 ยังไม่final
- OEMกำลังตรวจnavigation_map/สารบัญ/bookmarkและหน้าแก้LR01ในNAVIGATION_REVIEW.md; circuitauthorตรวจช่องว่างรูปอุปกรณ์จริงพร้อมสิทธิ์/applicationในPHOTO_GAP_PLAN.md

### งานรอบ03:30
1. รับnavigationreview ตรวจpageoffsetหลังinsertและfooterภาพแนวนอนจริง
2. ทำDOCXproofด้วยWordCOMแบบhiddenและจำกัดเวลา หากไม่สำเร็จคงคำอธิบายeditablecompanionไม่รับรองpagination; ห้ามส่งDOCXที่ยังไม่ตรวจว่าเป็นฉบับสมบูรณ์
3. ใส่สารบัญWordแบบdynamicfieldเพื่อupdateในWord แยกเลขหน้าของWordจากPDF และตรวจโครงสร้างfile
4. สรุปcoverageหลักฐานกับขอบเขตที่ยังไม่ยืนยันให้ผู้อ่านเข้าใจ ก่อนเข้าสู่consolidation06:00

## รอบต่อเนื่อง 2026-10-21 03:35 +0700

- รับNAVIGATION_REVIEW: ทุกentryสารบัญ23ข้อและbookmarkปลายทางตรงจริง รวม24bookmarksเมื่อรวมสารบัญ หน้า2เป็นสารบัญข้อความ ส่วนbookmarkกดนำทางได้ ปิดLR01หัวบท5แล้ว
- เปลี่ยนChromiumฐานไม่พิมพ์footerเก่า ก่อนmergefooterใหม่เพียงชุดเดียว แก้ข้อจำกัดoldfooterซ่อนในcopy/search ReadingProofยัง71หน้า SHA256 3b8bcd9fd195374a178448d35bbbea8b6095bf2e2665319531c84c4e0d004b5e OEMกำลังตรวจaddendumnavigation
- WordCOMในsandboxถูกaccessdenied; escalationได้รับอนุมัติแล้ว WordเปิดDOCX/repaginateได้91หน้า แต่ExportAsFixedFormatไม่เสร็จเกินสองนาที จึงปิดเฉพาะWINWORDทดสอบPID5440ที่ตรวจStartTime03:31:06และไม่มีหน้าต่าง ไม่ปิดWordอื่น และหยุดsession92752แล้ว ไม่มีWordPDFที่ตรวจได้
- แก้builderDOCX: เพิ่มTOCfieldแบบupdateในWord และยกเลิกบังคับขึ้นหน้าใหม่ทุกหัวคำอธิบายภาพ01–16ซึ่งทำWordยาวโดยไม่จำเป็น สร้างDOCXใหม่แล้ว แต่ยังไม่visualapproved จึงห้ามอ้าง91หน้าเป็นจำนวนของDOCXล่าสุด
- PHOTO_GAP_PLANครบ5รายการ ส่วนSCV/HP3/injectorมีลิงก์ผลิตภัณฑ์DENSOแต่ยังไม่มีสิทธิ์ฝังที่ยืนยัน;rail/sensorยังขาดภาพถ่ายตรงapplication ไม่มีภาพเว็บใหม่ถูกใส่โดยอัตโนมัติ ไม่ใช้ภาพGDแทนKD
- FINAL_DIAGNOSTIC_AUDITอ่านworkflow/matrix/workbook/ledgerครบ ไม่พบtechnicalblockerในscopeคู่มือมีเงื่อนไข ไม่ใช่ขั้นตอนครบVIN อนุมัติฝ่ายdiagnosticแก้ถ้อยคำmatrix2จุดให้repairวาล์ว/overpressureแยกเงื่อนไข และreturnไม่บังคับผิดทั้งรายหัวกับรวมพร้อมกัน

### งานรอบ04:00
1. รับmatrix2ถ้อยคำและnavigationaddendum แล้วassemble/rebuild ReadingProofใหม่พร้อมmapping/hash
2. รักษาPDFเป็นฉบับอ้างอิงการอ่าน;DOCXเป็นต้นฉบับแก้ไขได้ที่ยังไม่มีvisualapprovalจนกว่าจะมีrenderสำเร็จ ไม่ลองWordexportค้างซ้ำโดยไม่มีวิธีใหม่
3. เพิ่มคู่มือเริ่มอ่าน/แผนการสอนย่อแบบชี้หน้าและhighlightเฉพาะจุดสำคัญ โดยใช้เนื้อหาที่ตรวจแล้ว ไม่เพิ่มตัวเลขหรือclaimใหม่
4. เตรียมรายการไฟล์ส่งมอบ/ข้อจำกัดรูปถ่ายและapplicationให้READMEตรงผลงานจริง ก่อนfinalQAทุกหน้ารอบ06:00

## รอบต่อเนื่อง 2026-10-21 04:10 +0700

- รวมmatrixสองถ้อยคำแล้ว rebuildครบสายการผลิต ReadingProofยัง71หน้า hash70225592077be7334468af95d01d38faf9f3b13c4de8c501500924b342957818
- รับREPAIR_R4_REVIEWเปิด34–38ครบ5หน้าจริง เทียบ15cards ไม่มีข้อมูลตัดหรือหัวลอยจากข้อความใหม่ railvalve/returnถูกเงื่อนไข NAV23/23ยังตรง
- สร้างmanuscript/COURSE_GUIDE.mdโดยฝ่ายdiagnostic: เส้นทางเรียน6ภาพ/ไฮไลต์3จุดและกิจกรรมจำลองA/G+rubric/forms01–06 ไม่มีค่าOEMใหม่หรือผลทดลองจริง
- เพิ่มtools/build_course.py/render_course.cjs สร้างCourseProof15หน้า: คำแนะนำ2หน้า+วงจร01/02/03/04/05/16จำนวน6แผ่น+forms6หน้า+อ้างอิง1หน้า คัดจากbasePDFไม่มีfooterเดิมและใส่เลขหน้าคอร์สของตนเอง มีbookmarksและcourse_page_map.json
- ต้นแบบคอร์สรอบแรกส่วนสองยาวเกินจึงย่อเหลือ2394chars แก้parserให้rubricเป็นตารางจริงและhighlightเฉพาะ3จุด ล่าสุดhash47c92e91fe2a9f962869a5858b75a6751583f779a8c449fccedf5edf82004b41 ฝ่ายdiagnosticกำลังเปิดตรวจครบ15หน้าในCOURSE_R1_REVIEW
- READMEอัปเดตลิงก์ผลงานจริง/ข้อจำกัดDOCX/หลักฐานตรงapplication/ช่องว่างภาพถ่าย ไม่ระบุว่าเริ่มวิจัยอย่างเดียวแล้ว

### งานรอบ04:30
1. รับCOURSE_R1_REVIEW ปิดoverflow/เนื้อหาคัดไม่ครบก่อนfreezecourse
2. ตรวจโครงสร้างDOCXล่าสุดแบบread-only: TOCfield/landscape/ภาพ16/แหล่งลิงก์/อักขระไทย และเขียนDOCX_SOURCE_CHECK ไม่รับรองvisualpagination
3. เตรียมdeliverymanifestและpublishallowlist ไม่รวมOEMresearchPDF,QApagePNGsหรือไฟล์ชั่วคราว
4. ช่วง05:00เริ่มตรวจรายการไฟล์และscopeฉบับผู้อ่าน ช่วง06:00freezePDFสุดท้ายแล้วแบ่งทีมเปิดตรวจทุกหน้าของhashสุดท้าย

## รอบต่อเนื่อง 2026-10-21 04:36 +0700

- รับCOURSE_R1_REVIEW เปิดภาพจริงครบ15หน้า hash47c92e91fe2a9f962869a5858b75a6751583f779a8c449fccedf5edf82004b41 ไม่พบblocker 2guideมี3highlights+rubricจริง 6plates/6formsครบหน้า หน้าอ้างอิง14ลิงก์และใต้ภาพ18ลิงก์รวม32HTTPS annotations ไม่มีlocalURI
- ตรวจDOCXล่าสุดแบบread-only ZIP/OOXMLผ่าน ภาพฝัง16/drawings16/sections3(แนวนอน1)/TOCfield1/ไม่มีreplacementchar เขียนDOCX_SOURCE_CHECK.mdและJSON hashb5afd95052ce11f09af1bb7659999f0b5d69e5b8c30145d2bc3bbcdb4a59afb4 ไม่อ้างว่าvisualapproved
- เพิ่มDELIVERY_PLAN.mdกำหนดผลงานหลัก/ข้อจำกัด/allowlistไฟล์ ห้ามรวมOEMresearchPDF/screenshots/QAimages/logs/HTMLabsolutepathsในrepoหรือZIP
- ขยาย.gitignoreให้productionoutputsและQAimagesไม่เข้าgitโดยอัตโนมัติ ยกเว้นรายงานMDและmetadataที่จำเป็น FinaldeliveryPDFจะอยู่delivery/แยกจากproofs

### งานรอบ05:00
1. ตรวจข้อความเปิดเล่มกับREADMEให้เป็นฉบับผู้อ่าน ไม่เหลือข้อความกระบวนการผลิตที่ไม่จำเป็น และแจ้งข้อจำกัดจริง
2. เตรียมfinaleditionlabels/pathsแล้วfreezeฉบับสำหรับตรวจครบทุกหน้า รอบ06:00ไม่ขยายเนื้อหา
3. สร้างชุดไฟล์ส่งมอบ+manifestจากallowlistที่ตรวจ ไม่มีOEMreferencePDF ตรวจgitstagedก่อนpublishเฉพาะprojectนี้
4. หากDOCXยังไม่มีrenderสำเร็จ ส่งเป็นeditable sourceตามสถานะ ไม่ตั้งชื่อหรือสรุปว่าตรวจรูปเล่มWordครบแล้ว

## รอบต่อเนื่อง 2026-10-21 05:05 +0700

- ปรับหน้าเปิดเล่มให้อธิบายเป้าการอ่าน/หลักคิดP0093ชัด ตัดข้อความnormalizeURLภายในออก ใช้ฉบับศึกษาและฝึกวินิจฉัยพร้อมวันจัดทำ ไม่อ้างรับรองรถรายVIN
- เปลี่ยนfooterเป็นBOOK/COURSEและสร้างdelivery/ไฟล์ชื่อส่งมอบ: Book71หน้า hashf5174053131447d35b81cfa8ccfcee0fa97f7831d4faed7737b746724fa19836, Course15หน้า hash46a15e0d432a458ebc0f0de35574816e76551c0b72b14d07232e5e55525c7161, EditableSourceDOCXhash1949502037ade962180591b97cf8f29b32e2f36d636db04e0c600e0714d63053
- บันทึกproduction/final_freeze.jsonและตรึงไฟล์ทั้งสองPDF ห้ามแก้ระหว่างทีมตรวจ เริ่มfinalQAก่อน06:00เพื่อเผื่อเวลาแก้จริง
- circuitauthorเปิดตรวจBook1–25;diagnosticเปิดBook26–48และCourse1–15;OEMเปิดBook49–71พร้อมnavigation/footer/linkaudit ทุกคนต้องดูภาพจริงรายหน้าของhashนี้ ห้ามอ้างreviewรุ่นเก่าแทน
- เพิ่มdelivery/READ_ME_TH.mdระบุยังอยู่ระหว่างfinalQA วิธีเลือกไฟล์/ข้อจำกัดVIN/ภาพถ่าย/DOCX/กรณีจำลองให้ครบ ยังไม่ประกาศส่งมอบ

### งานรอบ05:30
1. รับFINAL_BOOK_01_25/26_48/49_71และFINAL_COURSE_01_15 หากพบblockerแก้แบบจำกัดและตรวจหน้าที่เปลี่ยนกับหน้าไหลต่อ
2. ตรวจDOCXsourceหลังปรับหน้าเปิดอีกครั้ง อัปเดตhashไม่ยกQAโครงสร้างของไฟล์เก่าอัตโนมัติ
3. สร้างsourceZIP/manifestด้วยallowlist ไม่ใส่OEMPDFหรือQAimages ตรวจstageรายการไฟล์เฉพาะprojectนี้
4. หากผ่านครบก่อน06:30ให้ปิดเฉพาะconsolidation/packaging ไม่เริ่มขยายเนื้อหาใหม่ แต่ยังไม่รายงานfinalก่อนงานตรวจเสร็จจริง


## ปิดรอบหลัง deadline 2026-10-21 09:10 +0700

หยุดเพิ่มเนื้อหาและไม่เริ่มวิจัยรอบใหม่ ส่งมอบ Book71หน้า/Course15หน้า/EditableDOCX/SourceZIP พร้อม QA_STATUS ตามจริง finalBookเปิดดู28/71หน้า (26–30,49–71) ยังไม่ครบ43หน้า; finalCourseเปิด0/15หน้า ไม่ยกผลต้นแบบมาอ้างตรวจfinalครบ. OEMautoauditnav23/23 footer71/71 และ107URIไม่มีlocalpathผ่าน. DOCXstructureผ่านแต่visualไม่อนุมัติ. ไม่รับรองรูปเล่มสมบูรณ์ ภาพถ่ายจริงยังขาดและไม่มีVINตรงรถ. ชุดไฟล์ไม่รวมOEMresearchPDF. ขั้นตอนที่เหลือในอนาคตต้องเป็นคำสั่งใหม่จากผู้ใช้ ไม่เริ่มต่ออัตโนมัติหลังเวลาปิด.

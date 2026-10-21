# References / specifications — ตรวจต้นแบบรอบ2

21 ตุลาคม 2026 • ผู้ตรวจฝ่ายวิจัยOEM (AI) • ไม่ใช่การรับรองรถรายVIN

## ไฟล์และวิธีตรวจ

- production/P0093_Prototype.pdf **71หน้า**
- SHA256 **bbbd1c45c2eb193449d8d34bf27153127e25d5f021a96f0607236f9685668f61**
- Renderด้วยbundledPython/pypdfium2 scale1.65 และเปิดPNG **61–71ทุกหน้า100%** เพิ่มตรวจ57–60เพื่อปิดประเด็นแบบฟอร์มและsourceIDต้นภาคผนวก
- เก็บภาพและmanifestที่ production/reviews/references-r2-png/ พร้อมtext_ledger_audit.json
- ตรวจPDFtextทุก71หน้าเพื่อหาaliasเก่า/researchlog; เทียบclaimIDsและค่าช่วง63–71กับresearch/claim_ledger.json โดยไม่แก้PDF/builder/ledger

## ผลรวม

**ผ่านการตรวจขอบเขตนี้:** ภาคอ้างอิงอ่านได้ ใช้sourceIDกลางครบ16รายการ ไม่พบT1/D1 aliasเดี่ยวหลงในPDFtext ไม่พบresearchlog/localdownload/internal-fileinstructionsหรือLedgerauditท้ายฉบับอ่าน ไม่พบตารางหรือชื่อURLกดอ่านล้นหน้า ค่าตรวจและข้อยกเว้นresetยังครบ ไม่พบการยกระดับแหล่งDENSOภาพรวมหรือPicoเป็นเกณฑ์เฉพาะToyotaโดยไม่มีหลักฐาน

## ปิดประเด็นจาก OEM_LAYOUT_REVIEW

| ประเด็นเดิม | ผลรอบนี้ | หลักฐาน |
|---|---|---|
| OL03 — IDแตกบรรทัดในคอลัมน์แคบ | **ปิด** เปลี่ยนเป็นหัวข้อsourceIDและย่อหน้า อ่านT01/T07/P01เต็มคำ | เปิดภาพ59–61; PDFtextมีT01–T07,D01–D07,P01,O01 |
| OL04 — researchlog/paragraphรอบ2โดดเดี่ยว | **ปิด** ไม่พบlogดาวน์โหลด ไฟล์ศูนย์ไบต์ หรือหัวข้อรอบ2; คงข้อมูลD04textlayerเพี้ยนเฉพาะผลต่อการใช้หลักฐาน ซึ่งเกี่ยวกับผู้อ่านโดยตรง | เปิด59–62; textscanทุก71หน้า |
| OL05 — การ์ดสเปกยาว/ซ้ำ | **ยอมรับสำหรับต้นแบบ** การ์ดยังใช้หลายหน้าแต่อ่านง่าย ไม่ตัดขอบเขตหรือหน่วยเพื่อประหยัดหน้า ไม่มีเหตุบังคับลดขนาดตัวอักษร | เปิด63–70 |
| OL06 — auditinternalท้ายเล่ม | **ปิด** หน้า71จบด้วยข้อห้ามย้ายค่า ไม่มีLedgeraudit/JSONfilenames/รายการgapsอังกฤษภายในต่อท้าย | เปิด71; textscanทุก71หน้า |

เพิ่มเติมนอกคำขอหลัก: เปิดหน้า57พบแบบ05เริ่มหน้าใหม่พร้อมตาราง จึงปิดOL01ในช่วงที่เห็นได้ หน้า58แบบ06อ่านได้; OL02หมายเหตุการผลิตไม่พบในPDFtextฉบับนี้

## ตรวจ source IDs และความใช้ได้

- กลางที่พบครบ: **T01,T02,T03,T04,T05,T06,T07,D01,D02,D03,D04,D05,D06,D07,P01,O01**
- ผลค้นaliasแบบเดี่ยว `T1…T9` / `D1…D9` ทั้งPDF: **0รายการ** ไม่จับT01/D01หรือข้อความengineเป็นaliasผิด
- D05ยังระบุissuedSeptember2009แยกapplicabilityAugust2009 และไม่แบ่งรถทุกคันด้วยปีเดียว
- D07คงเงื่อนไขหัวฉีดมีcompensationcodeและการconsultความจำเป็นresetpump ไม่กลายเป็นresetทุกSCV
- P01คงข้อจำกัดsolenoid/low-return-pressure ไม่ขยายเป็นเกณฑ์mLหรือใช้กับpiezo/ระบบpositive-returnโดยอัตโนมัติ
- DENSOCommonRailPump/DieselComponentsและPicoAGT833อ้างเพื่อหลักการภาพรวม/ขอบเขตvacuum-fedตามบทเรียนเท่านั้น หน้า61ระบุชัดว่าไม่แทนคู่มือหรือเกณฑ์ผ่านเฉพาะรถ ไม่เพิ่มapplicationclaimจากURLgeneric
- O01เป็นช่องทางข้อมูลที่ต้องสิทธิ์/GTS ไม่อ้างว่าหนังสืออ่านค่าที่ถูกล็อกแล้ว

## ตรวจค่าตาม ledger

ช่วง63–71พบ17claimIDsและมีอยู่ในledgerทั้งหมด **missing=[]** ได้แก่C001–C005,C010,C012,C013,C016–C019,C025,C026,C033–C035

| รายการ | ผลตรวจ |
|---|---|
| DR201E1KD/2KDreference | 30–40/50–70MPaและ25–35/35–55MPaแยกถูก;3,000rpmไม่มีโหลดระบุครบ |
| RM1151E1KDreference | 30,000–40,000/50,000–80,000kPaและข้อความแปลงMPaถูก;ไม่รวมช่วงกับDR201E |
| Monitorenable | 750/600/500rpmแยกconfigurationครบ;ไม่เปลี่ยนเป็นidleหรือleakthreshold |
| Duration/MIL/inhibit | 1s/1drivingcycle/วงจรsensorหรือSCVขัดข้องตรงแหล่ง;ไม่สร้างMPadropหรือmL/s |
| Coil/harness | 1.9–2.3Ωที่20°CเฉพาะDR201E;<1Ωและ≥10kΩมีเงื่อนไขถอดปลั๊กสองปลาย;ไม่อ้างผลไฟฟ้ารับรองไฮดรอลิก |
| Scope | 10V/div;5ms/divเป็นtoolsettingและมีข้อจำกัด ไม่ถูกแปลงเป็นPWMfrequency/duty/current |
| Confirmation | 2,500rpm30sหลังidle1minแยกจากreference3,000rpm ไม่มีการย้าย50–70/35–55MPaเป็นเกณฑ์2500 |
| Reset/learning | คงDR201Econditionalinitialization;idle≥1min/coolant≥60°C/fuel≥20°C; DENSOconsultnecessityไม่ใช่บังคับทุกคัน |

## บันทึกรายหน้าที่เปิดตรวจ

| หน้า | เนื้อหา | ผล |
|---:|---|---|
| 61 | D05/D07/P01/O01และURLgeneric,ขอบเขตข้อ1–4 | อ่านได้ ไม่ล้น sourceและscopeตรง |
| 62 | ขอบเขตข้อ5–8/วันที่ตรวจ | ภาษาไทยครบ ไม่พบinternalnotes; มีพื้นที่ว่างท้ายบทแต่ไม่ใช่หน้าlogโดดเดี่ยว |
| 63 | นิยามreference/monitor/test/H-Uและ1KDidle | ค่าถูก ไม่ล้น |
| 64 | DR201Ereferenceที่เหลือ | ทั้ง3การ์ดตรงledger |
| 65 | RM1151Ereferenceและแปลงหน่วย | สองการ์ดแยกkPa/no-loadถูก |
| 66 | Monitorenable3configuration | 750/600/500rpmถูก |
| 67 | StrategyและDR201Einhibit | C002/C035/C003ตรง |
| 68 | RM1151Einhibit,MIL,leakthresholdข้อจำกัด | ไม่มีthresholdสร้างขึ้น |
| 69 | Coilและsensorharness | เงื่อนไข/หน่วย/ขอบเขตครบ |
| 70 | SCVharness/scopesetting | ครบ ไม่มีการตีความsettingเป็นfrequency |
| 71 | Confirmation/reset/ห้ามย้ายค่า | เงื่อนไขครบ จบโดยไม่มีauditinternal |
| 57เพิ่มเติม | แบบ05 | หัวและตารางอยู่หน้าเดียวกัน |
| 58เพิ่มเติม | แบบ06 | อ่านได้ ไม่ล้น |
| 59เพิ่มเติม | T01–T05 | IDเต็มคำ/market/linksไม่ล้น |
| 60เพิ่มเติม | T06/T07/D01–D04 | IDเต็มคำ/เงื่อนไขD04ไม่ถูกนำไปตัดสินอะไหล่ |

PDFannotationsช่วง61–71มี39ลิงก์ ทุกลิงก์https เก็บURLในauditเพื่อเทียบรุ่นถัดไป ไม่ใช่การรับรองเว็บปลายทางออนไลน์ตลอดเวลา ผลตรวจนี้ใช้กับhashข้างต้นเท่านั้น หากจัดหน้าใหม่ให้ตรวจหน้าที่เปลี่ยนซ้ำ

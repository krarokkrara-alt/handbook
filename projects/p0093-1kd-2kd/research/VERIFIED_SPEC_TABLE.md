# ตารางค่าที่ตรวจสอบแล้ว: P0093 / 1KD-FTV / 2KD-FTV

ตรวจหลักฐานวันที่ **21 ตุลาคม 2026** • อ่านคู่กับแหล่งอ้างอิงและขอบเขตการนำไปใช้

**ตารางนี้เป็นตัวอย่างจากเอกสารที่ระบุชื่อ ไม่ใช่สเปกรถไทยทุกคัน** ต้องยืนยัน VIN, model/chassis, เดือนผลิต, ตลาด, ECU/calibration ID และหมายเลขอุปกรณ์ก่อนนำไปตัดสินรถจริง

## ความหมายและความเชื่อมั่น

- **REFERENCE:** ค่าอ้างอิงแรงดันตามสภาพเครื่อง ไม่ใช่เกณฑ์ชี้ว่าอะไหล่ใดเสีย และไม่ใช่ขีดจำกัด P0093
- **MONITOR ENABLE / STRATEGY:** เงื่อนไขที่ระบบเริ่มตรวจและวิธีติดตาม ไม่ใช่ค่ารั่วไหล และไม่ใช่รอบเดินเบามาตรฐาน
- **TEST STANDARD:** เกณฑ์การวัดเฉพาะวงจร/อุปกรณ์ในคู่มือนั้น ต้องรักษาวิธีถอดปลั๊กและอุณหภูมิ ไม่เท่ากับพิสูจน์การทำงานไฮดรอลิกครบ
- **H/U:** มั่นใจสูงว่าอยู่ในเอกสารที่อ่าน; applicability ของรถเป้าหมายยังไม่ยืนยัน

**วันที่เอกสาร:** DR201E ยังไม่ยืนยันเดือน/ปีพิมพ์จากหน้าที่ตรวจ ชื่อ folder URL ไม่ใช่ปีรถ; RM1151E มีหัวข้อ applicability “From August, 2004” แต่ยังไม่ยืนยันรุ่นรถ/ตลาดจากปก เอกสาร Toyota ทั้งสองอ่านจาก mirror อิสระ ไม่ใช่ official Toyota hosting

## 1. REFERENCE — แรงดันรางตามสภาพเครื่อง

ทุกค่าเป็น **ประมาณ** ตามคู่มือ ไม่ใช้เดินเบาบนรถคันหนึ่งแทนเงื่อนไขโหลดบนถนน

| เอกสาร / ขอบเขต | เครื่องยนต์ | สภาพเครื่อง | ค่า | หน่วย | หน้า / แหล่ง | Ledger | ตรวจวันที่ / ความเชื่อมั่น |
|---|---|---|---:|---|---|---|---|
| DR201E Hilux TASA Argentina | 1KD-FTV | เดินเบา; ตารางไม่ได้กำหนดอุณหภูมิไว้ในช่องนี้ | 30–40 | MPa | [T01 หน้า05–84](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0084.pdf) | C004 | 2026-10-21 / H/U |
| DR201E Hilux TASA Argentina | 1KD-FTV | 3,000 rpm **ไม่มีโหลดเครื่องยนต์** | 50–70 | MPa | [T01 หน้า05–84](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0084.pdf) | C004 | 2026-10-21 / H/U |
| DR201E Hilux TASA Argentina | 2KD-FTV | เดินเบา; ตารางไม่ได้กำหนดอุณหภูมิไว้ในช่องนี้ | 25–35 | MPa | [T01 หน้า05–84](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0084.pdf) | C005 | 2026-10-21 / H/U |
| DR201E Hilux TASA Argentina | 2KD-FTV | 3,000 rpm **ไม่มีโหลดเครื่องยนต์** | 35–55 | MPa | [T01 หน้า05–84](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0084.pdf) | C005 | 2026-10-21 / H/U |
| RM1151E ECD FromAug2004; รุ่นรถ/ตลาดยังไม่ยืนยัน | 1KD-FTV | เดินเบา; ตารางไม่ได้กำหนดอุณหภูมิไว้ในช่องนี้ | 30,000–40,000 | kPa | [T05 หน้า05–501](https://toyotamanuals.gitlab.io/PZ471-Z00W0-CA/htmlweb/rm/rm1151e/m_05_0501.pdf) | C012 | 2026-10-21 / H/U |
| RM1151E ECD FromAug2004; รุ่นรถ/ตลาดยังไม่ยืนยัน | 1KD-FTV | 3,000 rpm **ไม่มีโหลดเครื่องยนต์** | 50,000–80,000 | kPa | [T05 หน้า05–501](https://toyotamanuals.gitlab.io/PZ471-Z00W0-CA/htmlweb/rm/rm1151e/m_05_0501.pdf) | C012 | 2026-10-21 / H/U |

RM1151E พิมพ์หน่วย kPa: เมื่อแสดงเป็น MPa ใน model matrix จึงเป็น 30–40 และ 50–80 ตามลำดับ ต้องแสดงว่าเป็นการแปลงหน่วย ไม่ใช่ตัวเลขคนละสเปก ห้ามนำช่วง 50–80 ของ RM1151E ไปแทน 50–70 ของ DR201E และห้ามย้ายค่า 1KD ไปใช้ 2KD

## 2. MONITOR ENABLE / STRATEGY — P0093

| เอกสาร / เครื่องยนต์ | รายการ | เงื่อนไข / ค่า | หน่วยหรือชนิด | หน้า / แหล่ง | Ledger | ตรวจวันที่ / ความเชื่อมั่น |
|---|---|---|---|---|---|---|
| DR201E / 1KD-FTV | รอบขั้นต่ำที่เปิดให้ monitor ทำงาน | 750 | rpm | [T01 หน้า05–85](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0084.pdf) | C003 | 2026-10-21 / H/U |
| DR201E / 2KD-FTV | รอบขั้นต่ำที่เปิดให้ monitor ทำงาน | 600 | rpm | [T01 หน้า05–85](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0084.pdf) | C003 | 2026-10-21 / H/U |
| RM1151E / 1KD-FTV | รอบขั้นต่ำที่เปิดให้ monitor ทำงาน | 500 | rpm | [T05 หน้า05–502](https://toyotamanuals.gitlab.io/PZ471-Z00W0-CA/htmlweb/rm/rm1151e/m_05_0501.pdf) | C013 | 2026-10-21 / H/U |
| DR201E / 1KDและ2KD | Required sensor / frequency / duration | Fuel pressure sensor / continuous / 1 | s สำหรับ duration | [T01 หน้า05–85](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0084.pdf) | C002 | 2026-10-21 / H/U |
| RM1151E / 1KD | Required sensor / frequency / duration | Fuel pressure sensor / continuous / 1 | s สำหรับ duration | [T05 หน้า05–502](https://toyotamanuals.gitlab.io/PZ471-Z00W0-CA/htmlweb/rm/rm1151e/m_05_0501.pdf) | C035 | 2026-10-21 / H/U |
| DR201E / 1KDและ2KD | เงื่อนไขไม่เปิด monitor | วงจร fuel-pressure sensor หรือ SCV มีความขัดข้อง | ข้อกำหนดเชิงสถานะ | [T01 หน้า05–85](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0084.pdf) | C003 | 2026-10-21 / H/U |
| RM1151E / 1KD | เงื่อนไขไม่เปิด monitor | วงจร fuel-pressure sensor หรือ SCV มีความขัดข้อง | ข้อกำหนดเชิงสถานะ | [T05 หน้า05–502](https://toyotamanuals.gitlab.io/PZ471-Z00W0-CA/htmlweb/rm/rm1151e/m_05_0501.pdf) | C035 | 2026-10-21 / H/U |
| DR201E / 1KDและ2KD | MIL / detection logic | 1 driving cycle / 1-trip | รอบการตรวจตามเอกสาร | [T01 หน้า05–84/85](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0084.pdf) | C001/C002 | 2026-10-21 / H/U |
| RM1151E / 1KD | MIL | 1 driving cycle | รอบการตรวจตามเอกสาร | [T05 หน้า05–502](https://toyotamanuals.gitlab.io/PZ471-Z00W0-CA/htmlweb/rm/rm1151e/m_05_0501.pdf) | C035 | 2026-10-21 / H/U |

**Leak threshold ที่ยืนยันได้เป็นคำอธิบาย:** ทั้งสองเอกสารกล่าวถึงแรงดันภายในรางลดลงมากขณะฉีด ไม่ได้ให้ค่า MPa drop สากลในหน้าที่อ้าง ระยะ monitor 1s จึงไม่ใช่เกณฑ์รั่ว mL/s หรือคำสั่งให้สร้างค่าความต่างแรงดันเอง

## 3. TEST STANDARD — ตัวอย่างวงจร DR201E เท่านั้น

| ขอบเขต | สิ่งที่ตรวจ | สภาพและวิธี | ค่า / หน่วย | หน้า / แหล่ง | Ledger | ตรวจวันที่ / ความเชื่อมั่น |
|---|---|---|---|---|---|---|
| DR201E Hilux TASA Argentina; SCVในชุดเอกสาร | ขดลวด SCV | ถอดปลั๊ก SCV; อุณหภูมิ20°C; ชดเชยความต้านทานสายมิเตอร์เมื่อวัดค่าต่ำ | 1.9–2.3 Ω | [T03 หน้า05–81 step3](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0078.pdf) | C016 | 2026-10-21 / H/U |
| DR201E; harness rail sensor | ความต่อเนื่องสาย | ถอด ECM E8 และ sensor F9 ทั้งสองปลายตามคู่มือ; ไม่วัดโอห์มขณะมีไฟ | ต่ำกว่า1 Ω | [T02 หน้า05–75 step3](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0070.pdf) | C018 | 2026-10-21 / H/U |
| DR201E; harness rail sensor | การแยกจาก body ground | ถอดทั้งสองปลายเหมือนแถวก่อน; ตามคู่ขั้วที่ตารางคู่มือระบุ | ตั้งแต่10 kΩ | [T02 หน้า05–75 step3](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0070.pdf) | C018 | 2026-10-21 / H/U |
| DR201E; harness SCV | ความต่อเนื่องสาย | ถอด ECM E8 และ SCV S8 ทั้งสองปลายตามคู่มือ | ต่ำกว่า1 Ω | [T03 หน้า05–82 step5](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0078.pdf) | C019 | 2026-10-21 / H/U |
| DR201E; harness SCV | การแยกจาก body ground | ถอดทั้งสองปลาย; ตามคู่ขั้วในคู่มือ | ตั้งแต่10 kΩ | [T03 หน้า05–82 step5](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0078.pdf) | C019 | 2026-10-21 / H/U |
| DR201E; SCV differential measurement | การตั้งสโคปคร่อม PCV+ / PCV– | เครื่องอุ่น ขณะเดินเบาหรือหมุนสตาร์ตตามคู่มือ; ใช้เครื่องมือคร่อมที่พิกัดเหมาะ | 10 V/div;5 ms/div | [T03 หน้า05–82 step6](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0078.pdf) | C017 | 2026-10-21 / H/U |

**ข้อจำกัด:** ค่าโอห์มขดลวดผ่านไม่พิสูจน์วาล์วขยับหรือปั๊มมีปริมาณพอ; continuity ผ่านไม่ตัดขั้วขาดเมื่อร้อน/สั่น; 10V/divและ5ms/divเป็น **การตั้งเครื่องมือ** ไม่ใช่ amplitude, PWMfrequency, duty หรือ current specification อย่าต่อคลิปกราวด์สโคปลง PCV– เพียงเพราะชื่อมีเครื่องหมายลบ

## 4. การตรวจยืนยัน P0093 กับ REFERENCE เป็นคนละรายการ

DR201E หน้า05–87 ให้ตรวจหลังลบรหัสโดยเดินเบา1นาที แล้ว2,500rpm30s และติดตามความนิ่งของแรงดัน (C010/T01) ขณะเดียวกันตารางแรงดันอ้างอิงในหน้าเดียวกันยังระบุ **3,000rpmไม่มีโหลด** จึงห้ามพิมพ์สลับว่า50–70/35–55MPaเป็นเกณฑ์ที่2,500rpm ทดสอบรูปแบบนี้ได้เมื่อระบบปลอดภัยและตรง applicability แล้ว ไม่ทดแทนสภาวะโหลดที่เกิดอาการจริง

## 5. Reset / learning — รักษาเงื่อนไข ไม่สั่งเหมารวม

| แหล่ง | ข้อความที่ใช้ได้ | สภาพ/หน่วยที่เกี่ยวข้อง | Ledger / ความเชื่อมั่น |
|---|---|---|---|
| [T07 DR201E หน้า05–38](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0038.pdf) | หลังเปลี่ยน supply pump/ECM พิจารณา initialization ตามอาการ คู่มือมีข้อยกเว้นเมื่อเครื่องเริ่มทำงานได้ปกติว่าไม่ต้อง initialization แต่ยังทำ idle steps i/j | ตามขั้นตอนเฉพาะเอกสาร | C025 / ตรวจ2026-10-21 H/U |
| [T07 DR201E หน้า05–38 stepsi/j](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0038.pdf) | ขั้นเดินเบาของกระบวนการที่ระบุ | อย่างน้อย1นาที; coolant≥60°C;fuel temp≥20°C | C026 / ตรวจ2026-10-21 H/U |
| [D07 DENSO warning หน้า1](https://assets.denso-am.eu/production/attachments/Diesel-Injector-replacement-warning-Bulletin-English.pdf) | เมื่อเปลี่ยนfuelpump ให้ consult genuineOEM/DENSO diagnostictool ว่าจำเป็นreset fuelpumplearningvalueหรือไม่ | ไม่ให้เลขเวลา/อุณหภูมิ/เมนูเฉพาะVIN; ไม่ย้ายมาสั่งSCVทุกตัว | C034 / ตรวจ2026-10-21 สูงในข้อคำเตือนทั่วไป |
| [D07 DENSO warning หน้า1](https://assets.denso-am.eu/production/attachments/Diesel-Injector-replacement-warning-Bulletin-English.pdf) | หัวฉีดที่มีcompensationcodeต้องregisterIDด้วยเครื่องมือที่ระบุ | ตรวจรูปแบบcode/ตำแหน่งสูบ/วิธีลงตามรุ่น;ไม่กำหนดจำนวนหลักสากล | C033 / ตรวจ2026-10-21 สูงในข้อคำเตือนทั่วไป |

## 6. สิ่งที่ห้ามย้ายใช้หรือเติมจากการเดา

1. ไม่ใช้ DR201E Argentina เป็นคำสั่งเฉพาะ Hiluxไทยเพียงเพราะเครื่อง1KD/2KDเหมือนกัน และไม่ใช้ RM1151E1KD กับ2KDโดยไม่มีหลักฐาน
2. ไม่รวมช่วงแรงดันต่างเอกสาร ไม่ใช้ no-load reference เป็นขีดจำกัดขณะบรรทุก และไม่เปลี่ยน monitorenable เป็นรอบเดินเบาหรือ leakthreshold
3. ไม่ใช้ pinout3สายของDR201EกับsensorหลายสายของRM1151E ไม่วาดตำแหน่งซ้าย/ขวาหน้าปลั๊กจากแผนผังต่อสาย
4. ไม่สมมติว่าSCVทุกตัวเป็นNCหรือNO ไม่ใช้เปอร์เซ็นต์dutyหรือผลถอดปลั๊กในapplicationหนึ่งกับอีกแบบ
5. ไม่เติมเกณฑ์injectorleak-back mL/time/temperature,SCVcurrent/duty/frequency,suctionrestriction,torque หรือMPadropที่ยังไม่ยืนยันตรงอุปกรณ์
6. ไม่ resetlearning แบบเหมารวมและไม่ลบรหัสก่อนเก็บfreeze-frame การไม่มีรหัสซ้ำขณะidleไม่เท่ากับยืนยันงานเต็มสภาวะ


# บันทึกตรวจภาพวงจร — รอบ 2

วันที่ตรวจ: 21 ตุลาคม 2026 เวลาไทย • ผู้ตรวจ: AI บรรณาธิการวงจร / ระบบไฟฟ้ารถยนต์ • สถานะ: ภาพประกอบต้นฉบับ 16 ภาพพร้อมให้กองบรรณาธิการจัดหน้า

## สิ่งที่ตรวจ

เปิดดู PNG ครบทั้ง 16 ภาพ ตรวจเส้นต่อ ตำแหน่งวงจร/เครื่องวัด ป้ายไทยและอังกฤษ ขอบภาพ และข้อจำกัด application จากนั้นตรวจเฉพาะภาพที่แก้ซ้ำ การตรวจนี้เป็นการตรวจต้นฉบับภาพและความสอดคล้องกับแหล่งอ้างอิง ไม่ใช่การรับรองรถจริงราย VIN หรือผลทดสอบบนเครื่องยนต์

`render_audit.json` ผลล่าสุดเป็น `[]`: ไม่มี text bounding box หลุด canvas 1800 × 1250 พิกเซล การผ่านเครื่องมือนี้ไม่ครอบคลุมการซ้อนเส้นภายใน จึงใช้การเปิดภาพดูร่วมด้วย

## ผลรายภาพ

| ภาพ | ผลตรวจ | ประเด็นสำคัญ |
|---|---|---|
| 01 hydraulic paths | ผ่านรอบภาพ | สีแยก low / high / return และทางกลับกลับถัง; จุด A–D เป็นชื่อในภาพ ไม่ใช่ port OEM |
| 02 pressure feedback | ผ่านรอบภาพ | feedback กลับ ECU; command ไม่เท่ากับ delivery; ไม่มี gain / calibration ที่เดา |
| 03 sensor electrical | แก้และตรวจซ้ำผ่าน | ใช้โวลต์มิเตอร์ต่อ signal–sensor return จริง ไม่มีสาย jumper; เส้นวัดข้าม return ใช้สะพานไม่ต่อร่วม; เป็น 3-net principle พร้อม DR201E / RM1151E difference |
| 04 SCV measurement | ผ่านรอบภาพ | differential คร่อม A/B และ clamp สายเดียว; ไม่สมมติขาใดเป็น chassis ground |
| 05 NC/NO | ผ่านรอบภาพ | แสดง rest state ไม่จ่ายไฟต่างกัน; ไม่เสนอ unplug test สากล; SV1/SV2 ไม่แทน NC/NO |
| 06 limiter/discharge | ผ่านรอบภาพ | สอง variant แยกกัน ไม่วาดว่าทุก rail มีทั้งคู่; commanded device มี ECU/EDU path |
| 07 injector command | ผ่านรอบภาพ | electrical feedback แยกจากปริมาณฉีด/return; P0200 ร่วมมีทางตรวจเฉพาะ |
| 08 ground offset | แก้และตรวจซ้ำผ่าน | มิเตอร์คร่อมสองด้านของขั้ว return ที่มีความต้านทาน ไม่ bypass ขั้ว; ไม่แนะนำพ่วงลงตัวถัง |
| 09 event sequence | แก้ตาม cross-review ผ่าน | ในตัวภาพระบุ hypothetical NC application และ synthetic current ไม่แทน NO/NC สากล; ไม่มีค่า OEM |
| 10 fuel balance | ผ่านรอบภาพ | แยก inflow / injection / internal return / rail relief; เป็นโมเดลไม่ใช่อัลกอริทึม ECU |
| 11 DR201E rail wiring | ตรวจ source ภาพจริงผ่าน | F9–3 ↔ E8–18 VC; F9–2 PR ↔ E8–26 PCR1; F9–1 ↔ E8–28 E2 พร้อม junctions; จำกัด DR201E TASA Argentina |
| 12 DR201E SCV wiring | ตรวจ source ภาพจริงผ่าน | S8–1 ↔ E8–2 PCV+; S8–2 ↔ E8–1 PCV–; ไม่มีขา ground ที่เดาและไม่มี connector-face orientation |
| 13 overshoot/drop | ผ่านรอบภาพ | ลำดับเป็น hypothesis ที่ต้องพิสูจน์; mechanical limiter variant เท่านั้น; กราฟสังเคราะห์ไม่มีเกณฑ์ปลอม |
| 14 suction measurement | แก้ layout ผ่าน | ย้าย label A/B ไม่ทับเส้นหัว; จุดวัดก่อน/หลังกรองชัด; no universal vacuum limit / no stop-tap instruction |
| 15 return test conditions | ผ่านรอบภาพ | เก็บเงื่อนไขและแรงดันทางกลับ; ไม่ให้ mL สากล; ไม่ขยายวิธี solenoid เป็น piezo |
| 16 evidence workflow | ผ่านรอบภาพ | workflow พิสูจน์สัญญาณ/ไฮดรอลิก/overshoot และรวมกลับไปแก้–ทดสอบซ้ำ; เส้นรวมมี node ชัด |

## Cross-review ที่ปิดแล้ว

- XR01 จากฝ่าย OEM: เพิ่มคำว่า hypothetical NC ในภาพ 09 เอง ไม่อาศัยคำเตือนใน caption เพียงแห่งเดียว
- XR02 จากฝ่าย OEM: ภาพ 03 ผูก DR201E หน้า 05–73 กับความต่างของ RM1151E หน้า 05–490 และอัปเดต manifest source IDs C08 / C12
- ข้อทักจากบรรณาธิการหลัก: ภาพ 03 / 08 ใส่สัญลักษณ์ DMM และแยก lead ถูกต้อง แก้ความคลุมเครือของสายที่ดูเหมือน bridge

## ข้อจำกัดที่ยังคงแสดงต่อผู้อ่าน

ภาพ 01–10, 13–16 เป็นภาพหลักการ / workflow ไม่ใช้แทน wiring diagram จริง ภาพ 11–12 เป็น connection redraw เฉพาะเอกสาร DR201E ไม่เหมารวมรุ่นไทย ไม่ใส่สีสายหรือมุมมองปลั๊กที่ไม่ได้ตรวจจากรถจริง ไม่มี waveform, โอห์ม, SCV duty, rail-pressure drop threshold หรือ leak-back mL ที่สร้างขึ้นเอง

คำบรรยายไทยและ URL ของทุกภาพอยู่ใน `circuits_manifest.json` / `CIRCUIT_PLAN.md` ไม่คัดลอกภาพ OEM มาเป็น asset ตีพิมพ์ เมื่อจัดลง PDF แล้วฝ่ายผลิตต้องตรวจขนาดตัวอักษรในหน้าจริงอีกครั้ง

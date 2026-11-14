# คู่มือซ่อมพวงมาลัยไฟฟ้า by mytech — เน้น PCB

สถานะส่งต่อ: 14 พฤศจิกายน 2026 · ฉบับญี่ปุ่น/เกาหลี/ยุโรป · **54 หน้า**

## เปิดงานจากตรงนี้

- [หนังสือ PDF ล่าสุด](docs/mytech-eps-pcb-handbook.pdf)
- [หน้าปก](docs/cover.png)
- [เครดิตและขอบเขตสิทธิ์](SOURCES_AND_RIGHTS.md)
- หลักฐานการค้นและตรวจภาพอยู่ใน `research/` และภาพที่ใช้จริงอยู่ใต้ `output/`

## ผู้ใช้ต้องการอะไร

ทำหนังสือคู่มือช่างภาษาไทย ชื่อ **คู่มือซ่อมพวงมาลัยไฟฟ้า — by mytech** ปกรวมภาพชุดควบคุม/PCB หลายรุ่น เน้นวงจรในบอร์ด ภาคต่าง ๆ อุปกรณ์จริง จุดวัด การแปลผล และจุดซ่อม ใช้รูปแบบ **อาการ → จุดวัด → ผลที่พบ → ซ่อม → ทดสอบ** ไม่เน้นคำถามเชิงวิชาการ ผู้ใช้กำชับให้ agent แยกเป็นผู้ค้นข้อมูลจริงและตรวจเข้ม ต้องแยกยี่ห้อ รุ่น ปี revision และชนิดระบบ

งานเริ่มจาก Honda SHOWA/elesys `39980-TS4-Z51 / Z5`, `S4S6-113282`, `HTS4X-10-14M` แล้วขยายเป็นหลายยี่ห้อและฝั่งยุโรป ไม่ใช่หนังสือเฉพาะ Civic อีกต่อไป

## ทำเสร็จแล้ว

1. หนังสือ 54 หน้า พร้อมสารบัญหน้า 2, PDF bookmarks, แหล่งข้อมูลกดเปิดได้ และใบงานพิมพ์ใช้
2. ภาค PCB หน้า 3–13: protection, regulator/PMIC, MCU/reset/clock/memory, CAN, gate driver, MOSFET bridge, current sensing, resolver/torque
3. PCB จริงหลายยี่ห้อหน้า 14–18: Honda TR8-M91, Toyota 89650-12340 และ Yaris/Vios supplier map, Hyundai/Kia และ Nissan
4. วงจรตัวอย่างจริงจาก Texas Instruments หน้า 19–22: DRV3205-Q1, reverse polarity และ resolver excitation/SINE front end
5. ภาคผนวก Honda Z51 หน้า 24–42: ภาพผู้ใช้ หน้าปลั๊กเทียบเคียง วิธีวัดสาย/ไฟ/กราวด์/การสื่อสาร ไล่ DTC และการทดสอบหลังซ่อม
6. ยุโรปหน้า 43–54: Fiat/Opel W-S0015 + Allegro A3935, MINI W-S0080, VAG W-S0082, Renault W-S0023 พร้อมภาพ PCB/ภาพอะไหล่ supplier และแยก EPS-C/EPS-R/EHPS
7. agent สามสายค้นข้อมูลโดยตรง และ reviewer ตรวจ pinout, การใช้ภาพ/กริด, suffix, high-side probing, ความคลาดเคลื่อน source และเลขหน้า

## จุดสำคัญที่ Claude ต้องรักษา

- **ยังไม่มีภาพ PCB ภายในหรือ schematic โรงงานที่ยืนยันตรง Honda TS4-Z51** ห้ามเปลี่ยนป้าย TR8/TR3 หรือบอร์ดยี่ห้ออื่นเป็น Z51
- ภาพ PCB, supplier mapping, ภาพชิ้นส่วนใน catalog, schematic ผู้ผลิตชิป และผลวัดจริงเป็นคนละระดับหลักฐาน
- รหัส `W-xxxxx` เป็น SKU ของ supplier ไม่ใช่เบอร์ชิปหรือ reference designator ของ PCB
- ภาพ chip close-up ที่ supplier จับคู่ ไม่เท่ากับอ่าน marking จากชิปที่ยังติดอยู่บนบอร์ดเต็ม
- การไม่พบ gate drive อาจมาจาก supply/enable/fault/control ไม่ใช่ driver เสียเสมอไป
- ห้ามแต่ง rail voltage, test point, MCU reset polarity, IC pinout หรือเบอร์ทดแทนจากหน้าตาชิ้นส่วน
- ห้ามใช้โหมดโอห์ม/diode บนวงจรที่มีไฟ/ประจุค้าง ห้าม earth clip scope แตะ switching phase/high-side source; ไม่ถอดสายดิน scope ให้เครื่องลอย
- ภาพ HF2012 ที่ใช้กับ Honda เป็นวงจรเทียบเคียง รูปเรียงขามาจาก Hybrid ต้องตรวจเลขหล่อและด้านมองจริง
- Torque แบบคอยล์ VS1/PVF/VS2 ไม่เอาวงจร Hall/potentiometer มาเสียบแทน

### สิ่งผิด/ไม่แน่นอนที่ตรวจเจอแล้ว

- บทความ Toyota พิมพ์เบอร์รีเลย์คลาดเคลื่อน ห้ามใช้ `C811... / AGB...` เป็นเลขสั่งซื้อ ภาพสอดคล้องกับตระกูล Panasonic `ACB36101 / CB1a-T-P-12V` แต่ต้องอ่านอะไหล่จริงให้ครบ
- Hyundai 1F และ 1R เป็นคนละด้าน ห้าม mirror เพื่อเดาพิกัด
- Nissan 2F ไม่ใช่ภาพ 1R ห้ามชี้พิกัดชิป 1R ลงรูป 2F
- MINI ชิปมีสติกเกอร์ ไม่ถือสติกเกอร์เป็น marking MCU; ไม่ใช้ MINI R50 EHPS ปนกับ W-S0080 EPS-R
- VAG catalog แถว CAN เขียน `3C` ไม่แก้เงียบเป็น `C3`; ภาพ 1F เป็น power/filter/contact, 2F มี interconnect ละเอียด
- Renault 2R เป็นชุดย่อยมอเตอร์/Hall ไม่ใช่ control PCB 1R; `MLX15120DB / MLX15121BA` มี marking แต่ยังไม่มี public primary datasheet
- `A3935KLQT` อ่านจาก supplier component photo ซึ่งจับคู่กับ Fiat/Opel map ไม่ใช่ผลอ่านจากชิปบนบอร์ดเต็ม; ไม่รับรอง ordering suffix หรือ drop-in replacement
- ST M24C16 ที่ลิงก์เป็นเอกสารตระกูล ไม่ยืนยันว่าตรง suffix `24C16WP` ทุกประการ

## งานที่ให้ Claude ทำต่อ (เรียงลำดับ)

1. อ่าน `research/research-europe-*.md`, source URLs, ภาพที่ใช้จริง และ PDF ล่าสุด ตรวจว่าคำอ้าง/รุ่น/พิกัดตรงหลักฐาน เขียนผลเป็น `CLAUDE_REVIEW.md` โดยแยก must-fix / improvement / unresolved
2. ตรวจแหล่งสิทธิ์ภาพและ excerpt schematic ก่อนการเผยแพร่เชิงพาณิชย์หรือทำ edition ที่แจกต่อ การเข้าถึง source บนเว็บไม่เท่ากับมี license ให้ใช้ซ้ำ
3. ค้น exact OEM references/revisions และภาพ installed chip markings ของแต่ละ PCB โดยเฉพาะ Z51; ถ้าไม่มีหลักฐานอย่าเติมให้ดูครบ
4. ถ้าพบ schematic ภายในจริง ให้แยก OEM schematic / reverse-engineered schematic / vendor example อย่างชัดเจน และตรวจ node-by-node ก่อนผูกกับจุดวัด
5. เพิ่ม component-level repair workflow ที่มีหลักฐานได้จริง เช่น supply/enable/fault, gate resistor/driver, shunt/Kelvin/amp, CAN mode/supply โดยไม่กำหนดค่าตายตัวจากคนละรุ่น
6. ปรับ source เป็น structured Markdown/JSON และ layout template หากจะขยายต่อ รักษา build ปัจจุบันและตรวจเลขหน้า/credits หลังแก้ทุกครั้ง
7. สร้างฉบับถัดไปพร้อม render ตรวจทุกหน้าที่เปลี่ยน บันทึกสิ่งที่ตรวจจริง และคงฉบับนี้เป็น baseline

ไม่ต้องแก้หนังสือ/โครงการอื่นใน repo เพื่อทำงานนี้ และไม่ push/publish เองเว้นแต่ผู้ใช้สั่ง การมี README หรือคิวไม่ได้แปลว่า Claude เริ่มรันแล้ว

## สร้าง PDF ซ้ำ

ใช้ Python 3.11+ และ dependency ใน `requirements.txt`:

```powershell
python -m pip install -r requirements.txt
python scripts/build.py
python scripts/validate.py
```

ค่าเริ่มต้น font คือ Windows Tahoma ที่ `C:/Windows/Fonts/` ไม่ได้บรรจุ font ของ Windows ลง repo หากเครื่องอื่นไม่มี ให้ชี้ font ที่รองรับไทยและมีสิทธิ์ใช้งาน:

```powershell
$env:MYTECH_FONT_REGULAR = 'C:/path/to/Thai-Regular.ttf'
$env:MYTECH_FONT_BOLD = 'C:/path/to/Thai-Bold.ttf'
python scripts/build.py
```

Pipeline: `build_mytech_core.py` สร้าง raw 42 หน้า → `order_mytech.py` จัดลำดับเน้น PCB → `build_europe.py` สร้างปกใหม่และภาคเพิ่ม 12 หน้า → `merge_europe.py` รวมเป็น 54 หน้าแล้วคัดลอกไป `docs/` ไม่มีการ download ระหว่าง build; ใช้เฉพาะภาพ complete ที่คัดไว้

การ render QA ใช้ Poppler `pdftoppm` (ติดตั้งแยก) ภาพที่ render เป็น preview ไม่ใช่แหล่งหลักใหม่ ต้องดูไฟล์ต้นฉบับและ source attribution เสมอ

## สถานะตรวจส่งต่อ

- ตรวจภาพครบ 42 หน้า baseline แล้ว; ตรวจภาพภาคใหม่ 12 หน้าและปกแยกแล้ว
- reviewer ไม่พบ must-fix ทางเทคนิคในบท Europe หลังแก้ข้อความ suffix ST ให้ชัด
- ไม่ได้ทดสอบกล่องจริง ไม่ได้วัด PCB จริง และไม่ใช่การรับรองจาก OEM
- สถานะการส่ง Claude ดูไฟล์ `CLAUDE_AUTO_START/latest.json` ที่ราก repo; `queued/awaiting_cli` ไม่ใช่ started/completed

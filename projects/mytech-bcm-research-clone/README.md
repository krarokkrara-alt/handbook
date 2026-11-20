# BCM ค้นคว้าวงจรและการย้ายข้อมูล (MyTech · แจกฟรี)

หนังสือ BCM ภาษาไทยเรื่องวงจรในบอร์ด การย้ายชิป และการย้ายข้อมูล พร้อมเครื่องมือสร้างหนังสือและเปรียบเทียบไฟล์ แยกจาก `../mytech-bcm-pcb` เริ่มจากสำเนาฉบับขยาย ณ commit `01034fc`

## เปิดอ่าน

| ต้องการ | เปิดไฟล์ |
|---|---|
| หนังสือ PDF (67 หน้า มีลายน้ำ และภาพจริง 11 ภาพ) | [books/BCM-MyTech-Handbook.pdf](books/BCM-MyTech-Handbook.pdf) |
| หนังสือ HTML | [books/BCM-MyTech-Handbook.html](books/BCM-MyTech-Handbook.html) |
| สถานะงานล่าสุด | [reports/PROGRESS.md](reports/PROGRESS.md) |
| สิ่งที่เพิ่มจากเล่มตั้งต้น | [reports/NEW_FINDINGS.md](reports/NEW_FINDINGS.md) |
| ผลตรวจเทคนิค / บรรณาธิการ | [reports/TECHNICAL_REVIEW.md](reports/TECHNICAL_REVIEW.md) · [reports/EDITORIAL_REVIEW.md](reports/EDITORIAL_REVIEW.md) |
| ผลเปรียบเทียบข้อมูล | [comparisons/COMPARISON_REPORT.md](comparisons/COMPARISON_REPORT.md) · [ตัวอย่างจำลอง](comparisons/simulated/SIMULATED_RESULT.md) |
| ต้นฉบับ | [manuscript.md](manuscript.md) (บท 1–15) · [supplement-v2.md](supplement-v2.md) (ภาคขยาย) |
| ทะเบียนแหล่งอ้างอิง | [research/SOURCES.csv](research/SOURCES.csv) · [VISUAL_SOURCES.md](VISUAL_SOURCES.md) |
| ภาพจริงสิทธิ์เปิด + ลิงก์ดาวน์โหลด | [assets/real-photos/commons/CREDITS.md](assets/real-photos/commons/CREDITS.md) |
| คำสั่งงานสำหรับ Claude | [CLAUDE.md](CLAUDE.md) |

## โครงสร้างโฟลเดอร์

| โฟลเดอร์ | ใช้เก็บ |
|---|---|
| `books/` | หนังสือ PDF/HTML ที่สร้างจากต้นฉบับ (อย่าแก้ตรง ให้แก้ต้นฉบับแล้วสร้างใหม่) |
| `assets/` | ภาพบอร์ด ภาพวงจร ภาพโปรแกรม พร้อมที่มาใน VISUAL_SOURCES.md |
| `source-documents/` | เอกสารผู้แต่งเดิม 4 หน้า (อยู่หลังปกหน้า 2–5 ห้ามแก้) |
| `research/` | ทะเบียนแหล่ง วงจร รุ่นกล่อง MCU และเครื่องมือ |
| `incoming/` | ไฟล์ชิ้นงานที่เจ้าของนำมาตรวจ **ไม่ขึ้น GitHub** ห้าม dump/VIN/ข้อมูลลับ |
| `comparisons/` | รายงานผลต่าง (ไม่มีค่าไบต์) และตัวอย่างจำลอง |
| `reports/` | สถานะงาน รายงานตรวจเทคนิคและบรรณาธิการ |
| `tools/` | ตัวสร้างหนังสือ ตัวตรวจ และเครื่องมือเปรียบเทียบ |

## ระบบเปรียบเทียบไฟล์

เทียบคู่เดียว (คำสั่งเดิม):

```powershell
python tools/compare_data.py --before incoming/original.bin --after incoming/readback.bin --output comparisons/compare-result.json
```

เทียบหลายคู่จากไฟล์งาน พร้อมรายงานภาษาไทย:

```powershell
python tools/compare_data.py --job incoming/JOB123.json --output comparisons/JOB123.json --markdown comparisons/JOB123.md
```

ดูตัวอย่าง (สร้างไฟล์จำลองแล้วเทียบ 4 คู่):

```powershell
python tools/make_simulated_demo.py
```

ชนิดคู่ที่รองรับ: `read_repeat` (อ่านซ้ำ), `intended_vs_readback` (ตั้งใจเขียนกับอ่านกลับ), `before_after` (ก่อน/หลังซ่อม) เครื่องมือให้ข้อสรุปเฉพาะที่หลักฐานรองรับ แสดงขนาด SHA-256 จำนวนไบต์ต่าง และช่วง offset **ไม่แสดงค่าไบต์และไม่แก้ไฟล์ต้นฉบับ** ผลตรงกันทั้งไฟล์ไม่ยืนยันว่ากล่องทดแทนใช้กับรถได้

## สร้างหนังสือใหม่

ต้องมี Python 3 + `pip install reportlab Pillow pypdf` และฟอนต์ Tahoma (หรือกำหนด `MYTECH_FONT_REGULAR` / `MYTECH_FONT_BOLD`)

```powershell
python tools/build_book.py
```

```powershell
python tools/validate.py
```

ลายน้ำค่าเริ่มต้นคือ `MyTech · แจกฟรี` ใส่ทุกหน้าตั้งแต่หน้า 6 และใน HTML เปลี่ยนข้อความได้ด้วยตัวแปร `MYTECH_WATERMARK` ตัวตรวจจะล้มถ้าหน้าใดขาดลายน้ำ หรือถ้าปก/หน้าผู้แต่งถูกแก้ หลังเปลี่ยนเนื้อหาต้องเปิดดูภาพหน้า PDF ด้วยตาทุกครั้ง

## ข้อจำกัด

หนังสือนี้ไม่มีผลโคลนหรือผลทดสอบบนรถจริง ตัวอย่างผลต่างทั้งหมดเป็นข้อมูลจำลอง ภาพบอร์ดจริงเป็นของเจ้าของภาพต้นทาง การแจกฟรีไม่เปลี่ยนสิทธิ์ภาพ ดู [reports/PROGRESS.md](reports/PROGRESS.md) สำหรับงานที่ยังขาด

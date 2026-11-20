# ผลเปรียบเทียบข้อมูล

สถานะ: **ยังไม่มีไฟล์ชิ้นงานจริง** ไม่มีผลโคลนหรือผลทดสอบบนรถในรายงานนี้ มีเฉพาะตัวอย่างจำลองที่ [simulated/SIMULATED_RESULT.md](simulated/SIMULATED_RESULT.md) (ข้อมูลจำลองเพื่ออธิบายการเปรียบเทียบ)

## วิธีทำเมื่อมีไฟล์จริง

1. วางไฟล์ใน `incoming/` (ไม่ขึ้น GitHub) ตั้งชื่อตามเลขงานและพื้นที่ เช่น `JOB123_EEPROM_read1.bin`
2. สร้างไฟล์งาน `incoming/JOB123.json` ตามรูปแบบ `comparisons/simulated/job.json` ใส่ 3 คู่:
   - `read_repeat` อ่านรอบ 1 กับรอบ 2
   - `intended_vs_readback` ไฟล์ที่ตั้งใจเขียนกับไฟล์อ่านกลับ
   - `before_after` ก่อนกับหลังซ่อม/ย้าย
3. ถ้ามีแผนที่พื้นที่จากเอกสาร ให้ใส่ใน `regions` พร้อม `source` ห้ามใส่แผนที่ที่เดาเอง
4. รัน

```powershell
python tools/compare_data.py --job incoming/JOB123.json --output comparisons/JOB123.json --markdown comparisons/JOB123.md
```

5. ตรวจรายงานด้วยตาก่อน commit ว่าไม่มีชื่อไฟล์ที่มี VIN หรือข้อมูลบุคคล

## สิ่งที่ต้องบันทึกเพิ่มในใบงาน

ชนิดพื้นที่ข้อมูล เครื่องมือ/เวอร์ชัน วิธี verify (ของเครื่อง หรือเทียบ read-back เอง) และข้อจำกัด ผลต่างไม่ได้ยืนยันความหมายของข้อมูลที่ offset นั้น

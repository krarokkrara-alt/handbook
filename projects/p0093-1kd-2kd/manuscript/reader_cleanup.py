from pathlib import Path
import re

root = Path(__file__).resolve().parent

p = root / 'OPERATING_CIRCUITS.md'
s = p.read_text(encoding='utf-8')
s = re.sub(r'^ต้นฉบับบทเรียน 8 ตอน.*\n\n', '', s, flags=re.M)
replacements = {
    '**แทรกภาพ 01 คู่กับภาพ 02; วางภาพ 10 ท้ายบทเรียน**': '**ดูภาพ 01, 02 และ 10**',
    '**แทรกภาพ 02 และภาพ 09; ภาพ 09 เป็นกราฟสังเคราะห์ของ hypothetical NC application**': '**ดูภาพ 02 และ 09 — ภาพ 09 เป็นกราฟจำลองของระบบ NC สมมติ ไม่ใช่ผลวัดรถจริง**',
    '**แทรกภาพ 04 และภาพ 05; ใส่ภาพ 12 ในกรอบ “ตัวอย่างวงจรจริงเฉพาะ DR201E”**': '**ดูภาพ 04, 05 และ 12 — ภาพ 12 ใช้เฉพาะ configuration ของเอกสาร DR201E ที่ระบุ**',
    '**แทรกภาพ 06 คู่กับภาพ 13**': '**ดูภาพ 06 และ 13**',
    '**แทรกภาพ 16 เต็มหน้าหรือหน้าคู่ แล้วใช้ตารางด้านล่างเป็นใบงาน**': '**ดูภาพ 16 ประกอบตารางสิ่งที่วัดด้านล่าง**',
}
for old, new in replacements.items():
    s = s.replace(old,new)
s = re.sub(r'^\*\*แทรกภาพ (.*?)\*\*$', r'**ดูภาพ \1**', s, flags=re.M)
s = s.replace('ใช้ canonical source IDs ของ `research/claim_ledger.json` ตรงกันทั้งบท ภาพใน `circuits_manifest.json` อาจยังมีรหัส Cxx เดิมของชุดภาพ ให้จับคู่ด้วย URL และแปลงเป็นทะเบียนกลางตอนจัดเล่ม รหัส C001 เป็นต้นใน claim ledger เป็น claim ID ไม่ใช่ source ID', 'รหัสอ้างอิงในวงเล็บระบุเอกสารต้นทางในตารางนี้ เลขหน้าที่ตามรหัสใช้ตรวจข้อความและขอบเขตของข้อมูลก่อนนำไปใช้กับรถจริง')
s = s.replace('แหล่งที่ยังไม่ลง canonical ID อ้างด้วย URL ตรง ไม่สร้าง alias ขึ้นเอง:', 'แหล่งข้อมูลประกอบเพิ่มเติม:')
s = s.split('## หมายเหตุให้ฝ่ายจัดหน้าและผู้ตรวจ')[0].rstrip() + '\n'
p.write_text(s,encoding='utf-8')

p = root / 'REPAIR_MATRIX.md'
s = p.read_text(encoding='utf-8')
s = re.sub(r'^ฉบับทำงาน 1.*\n\n', '', s, flags=re.M)
start = s.index('## กรณีศึกษาเพื่อฝึกคิด')
end = s.index('## หลักฐานอ้างอิงและข้อจำกัด',start)
index = '''## ดัชนีกรณีฝึกวิเคราะห์

ทุกกรณีเป็นสถานการณ์จำลอง ไม่มีตัวเลขที่สมมติเป็นสเปกโรงงาน อ่านโจทย์ บัตรหลักฐาน และช่องตอบใน [สมุดฝึกวิเคราะห์](CASE_WORKBOOK.md) แล้วตรวจแนวคำตอบในส่วนผู้สอน

| กรณี | ประเด็นฝึก | ดูในสมุดฝึก |
|---|---|---|
| A | หลังเปลี่ยนกรองแล้วเกิดขณะขึ้นเนิน | กรณี A และแนวคำตอบ A |
| B | return ใกล้กันไม่รับรองปริมาณรวม | กรณี B และแนวคำตอบ B |
| C | แรงดันสูงก่อนตก | กรณี C และแนวคำตอบ C |
| D | เปลี่ยน SCV แล้วอาการกลับเมื่อร้อน | กรณี D และแนวคำตอบ D |
| E | P0093 ร่วม P0200 และขอบเขตเครื่องมือ | กรณี E และแนวคำตอบ E |
| F | การทดสอบไม่มีโหลดไม่แทนอาการบรรทุก | กรณี F และแนวคำตอบ F |
| G | ปัญหาทางข้อมูลและวงจรร่วม | กรณี G และแนวคำตอบ G |
| H | สิ่งปนเปื้อนและความเสียหายซ้ำ | กรณี H และแนวคำตอบ H |

งานรถจริงใช้ [ชุดใบงานภาคสนาม 6 แบบ](FIELD_WORKSHEETS.md) เพื่อเก็บเอกลักษณ์รถ หลักฐาน ผลวัด การตัดสินใจ ผลก่อน–หลัง และรายงานส่งมอบ

'''
s = s[:start] + index + s[end:]
s = s.replace('Toyota DR201E หน้า05-84–88 และ RM1151E หน้า05-501–504; ขอบเขตSCV NO/NCและหน้าที่ใช้DENSO officialตามรายการ[T1,T2,D1–D4](DIAGNOSTIC_WORKFLOW.md#แหล่งข้อมูลและสถานะตรวจสอบ)', 'Toyota DR201E [T01] หน้า05-84–88 และ RM1151E [T05] หน้า05-501–504; ขอบเขตSCV NO/NCและหน้าที่ใช้DENSO [D06,D01,D03] ส่วนคำเตือนลงรหัส/ตรวจความจำเป็นlearningใช้ [D07] ดู [รายการแหล่งข้อมูล](DIAGNOSTIC_WORKFLOW.md#แหล่งข้อมูลและสถานะตรวจสอบ)')
p.write_text(s,encoding='utf-8')

p = root / 'FIELD_WORKSHEETS.md'
s = p.read_text(encoding='utf-8')
s = s.split('### หมายเหตุการผลิต')[0].rstrip()+'\n'
p.write_text(s,encoding='utf-8')

p = root / 'CASE_WORKBOOK.md'
s = p.read_text(encoding='utf-8')
s = re.sub(r'^ต้นฉบับฝ่ายวินิจฉัย.*\n\n', '', s, flags=re.M)
s = re.sub(r'(?m)^### (กรณี [A-H] —.*|[A-H]:.*)$', r'<!-- pagebreak -->\n\n### \1',s)
learner_start=s.index('## ส่วนที่ 1')
teacher_start=s.index('## ส่วนที่ 2')
learner=s[learner_start:teacher_start]
# A separate visible paragraph gives a real writing line for each answer.
learner=re.sub(r'(?m)^(- .*?): [^\n]*_{3,}[^\n]*$',r'\1\n\n________________________________________________________________',learner)
# Five-question cases receive one additional writing line, so all cases offer six lines.
chunks=re.split(r'(?=<!-- pagebreak -->\n\n### กรณี )',learner)
for i,c in enumerate(chunks):
    if '### กรณี ' not in c:
        continue
    count=c.count('________________________________________________________________')
    if count<6:
        tail='\n\nบันทึกเพิ่มเติม\n\n________________________________________________________________\n\n'
        if c.rstrip().endswith('---'):
            c=c.rstrip()[:-3].rstrip()+tail+'---\n\n'
        else:
            c=c.rstrip()+tail
    chunks[i]=c
learner=''.join(chunks)
s=s[:learner_start]+learner+s[teacher_start:]
p.write_text(s,encoding='utf-8')

for name in ['OPERATING_CIRCUITS.md','REPAIR_MATRIX.md','FIELD_WORKSHEETS.md','CASE_WORKBOOK.md']:
    value=(root/name).read_text(encoding='utf-8')
    print(name,len(value.encode('utf-8')),'bytes',value.count('<!-- pagebreak -->'),'pagebreaks')

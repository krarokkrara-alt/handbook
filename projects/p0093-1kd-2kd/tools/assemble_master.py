from pathlib import Path
import json,re
P=Path(__file__).resolve().parents[1]
M=P/'manuscript';R=P/'research';C=P/'circuits'

alias_data=json.loads((M/'source_alias_map.json').read_text(encoding='utf8'))
registry=json.loads((R/'claim_ledger.json').read_text(encoding='utf8'))['source_registry']
aliases={}
for item in alias_data['aliases']:
 key=item['canonical_source_id']
 if key:
  assert registry.get(key)==item['url'],f"Source URL mismatch: {key}"
  aliases[item['local_alias']]=key

def ns_diagnostic(text):
 pattern=r'(?<![A-Za-z0-9])('+'|'.join(re.escape(k) for k in aliases)+r')(?![A-Za-z0-9])'
 return re.sub(pattern,lambda m:aliases[m[1]],text)

def shift(text,levels=1):
 text=re.sub(r'^# [^\n]+\n+', '', text, count=1)
 text=re.sub(r'^(?:ฉบับทำงาน[^\n]*|ต้นฉบับฝ่าย[^\n]*)\n+', '', text,flags=re.M)
 return re.sub(r'^(#{1,5}) ',lambda m:'#'*min(len(m.group(1))+levels,6)+' ',text,flags=re.M)

parts=['# P0093 Toyota 1KD และ 2KD\n\n## วงจรการทำงาน การแยกสาเหตุ และวิธีแก้ตามหลักฐาน\n\nฉบับศึกษาและฝึกวินิจฉัย • 21 ตุลาคม 2569\n\nคู่มือนี้แยกการทำงานของระบบออกจากขั้นตอนตรวจรถจริง ค่าและขั้วที่อ้างเอกสารเฉพาะใช้ได้เมื่อยืนยันรุ่น ตลาด ชุดอุปกรณ์ และรุ่นคู่มือก่อนเท่านั้น ไม่อนุมานความใช้ได้จากชื่อเครื่องยนต์เพียงอย่างเดียว\n\nP0093 เป็นผลการตรวจของระบบ ไม่ใช่คำตัดสินว่าชิ้นส่วนใดเสีย หนังสือพาผู้อ่านแยกคำสั่ง ผลวัด และการทำงานจริง ก่อนเลือกซ่อมและยืนยันผล รหัสอ้างอิง เช่น T01 และ D01 ใช้ค้นเอกสารในภาคผนวก แหล่งคู่มือ OEM ที่โฮสต์ภายนอกระบุเป็นสำเนา ไม่ใช่เว็บไซต์ Toyota ทางการ\n\n']
parts.append('## ภาคหนึ่ง อ่านวงจรจากทางน้ำมันสู่การควบคุม\n\nภาพหลักการใช้แยกหน้าที่และจุดวัด ส่วนภาพเฉพาะเอกสารให้ถือ applicability ที่กำกับภาพเป็นเงื่อนไขสำคัญ ภาพกราฟจำลองไม่ใช่เกณฑ์ตั้งรหัสจากโรงงาน\n\n')
manifest=json.loads((C/'circuits_manifest.json').read_text(encoding='utf8'))
for d in manifest['diagrams']:
 parts.append(f"### ภาพ {d['id']} {d['title_th']}\n\n![{d['title_th']}](../circuits/{d['png']})\n\n{d['caption_th']}\n\n{d['teaching_note_th']}\n\nขอบเขต: {d['scope']}\n\n")
 parts.append(('แหล่งอ้างอิงภาพ: '+' • '.join(f'[แหล่ง {i+1}]({u})' for i,u in enumerate(d['sources'])) if d['sources'] else 'ภาพแบบจำลองทางไฟฟ้าที่ผู้เขียนวาดขึ้น เพื่ออธิบายหลักการ ไม่ใช่วงจรภายใน OEM')+'\n\n')
for title,name in [('บทเรียนวงจรและลำดับการทำงาน','OPERATING_CIRCUITS.md'),('ภาคสอง วินิจฉัยจากหลักฐานไปถึงวิธีแก้','DIAGNOSTIC_WORKFLOW.md'),('ภาคสาม ตารางแก้ปัญหาและการยืนยันผล','REPAIR_MATRIX.md'),('ภาคสี่ แบบฝึกกรณีจำลอง','CASE_WORKBOOK.md'),('ภาคห้า แบบบันทึกผลวัดและส่งมอบ','FIELD_WORKSHEETS.md')]:
 p=M/name
 if p.exists():
  body=p.read_text(encoding='utf8')
  if name=='CASE_WORKBOOK.md' and '## ส่วนที่ 2' in body:
   first,answers=body.split('## ส่วนที่ 2',1)
   body=first+'<!-- pagebreak -->\n\n## ส่วนที่ 2'+answers.replace('<!-- pagebreak -->','')
  parts.extend(['## '+title+'\n\n',shift(ns_diagnostic(body))+'\n\n'])
parts.extend(['## ภาคผนวก แหล่งข้อมูลและขอบเขตที่ต้องยืนยัน\n\n',shift((R/'READER_REFERENCES.md').read_text(encoding='utf8'))+'\n'])
spec=R/'VERIFIED_SPEC_TABLE.md'
if spec.exists():parts.extend(['\n## ตารางอ้างอิงที่แยกตามเอกสาร\n\n',shift(spec.read_text(encoding='utf8'))+'\n'])
(M/'MASTER_DRAFT.md').write_text(''.join(parts),encoding='utf8',newline='\n')
print('Combined draft written; figures:',len(manifest['diagrams']))

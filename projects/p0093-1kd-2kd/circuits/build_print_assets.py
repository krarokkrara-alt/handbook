from pathlib import Path
import xml.etree.ElementTree as ET,json
P=Path(__file__).parent;out=P/'print';out.mkdir(exist_ok=True)
ET.register_namespace('','http://www.w3.org/2000/svg')
N='{http://www.w3.org/2000/svg}'
heights={1:930,2:960,3:1030,4:920,5:900,6:1000,7:930,8:1030,9:1030,10:1030,11:1000,12:1010,13:1020,14:980,15:1020,16:1035}
scopes={
1:'ภาพหลักการ ไม่ใช่ผังขา OEM | ฟ้า = แรงดันต่ำ • แดง = แรงดันสูง • เขียว = น้ำมันกลับ',
2:'วงป้อนกลับเชิงหน้าที่ | คำสั่งไม่พิสูจน์ปริมาณส่ง และ feedback ไม่ใช่การวัดอิสระ | ไม่ใช่อัลกอริทึม OEM',
3:'ภาพหลักการสามหน้าที่ | DR201E หน้า 05–73 / RM1151E หน้า 05–490 ต่างกัน | ยืนยันวงจรรถก่อนใช้',
4:'ภาพหลักการวัดขดลวด | ไม่แสดง topology ภาคขับ และไม่ถือว่าขั้วใดเป็นกราวด์ตัวถัง',
5:'ภาพหลักการสภาพไม่จ่ายไฟ | ห้ามใช้กฎถอดปลั๊กสากล ต้องยืนยันชนิด NC / NO ของคันจริง',
6:'ภาพเปรียบเทียบสอง variant | limiter ทางกล กับ discharge valve สั่งไฟฟ้า | เลือกตามรางและเอกสารรถจริง',
7:'ภาพหน้าที่ไฟฟ้าและน้ำมัน | การยืนยันกระแสไม่ใช่การวัดปริมาณฉีดหรือการรั่วกลับ | ไม่ใช่วงจรภายใน EDU',
8:'แบบจำลองวงจรทั่วไป: Vread = Vsignal-to-local-return + Vreturn-offset | ไม่ใช่วงจรภายใน OEM',
9:'ตัวอย่างสมมติ NC application | กราฟสังเคราะห์ ไม่ใช่คลื่นวัดจริง ไม่มีค่า OEM และไม่แทนพฤติกรรม NO',
10:'แบบจำลองสมดุลการไหล | ไม่ใช่อัลกอริทึม ECU หรือเกณฑ์ calibration สำหรับตัดรหัส',
11:'เฉพาะ DR201E / Hilux TASA Argentina | Toyota หน้า 05–73/75 | ยืนยัน application ก่อนใช้ ไม่แสดงมุมปลั๊ก',
12:'เฉพาะ DR201E / Hilux TASA Argentina | Toyota หน้า 05–80/82 | ไม่สมมติว่า PCV– เป็นกราวด์ตัวถัง',
13:'สมมติฐานทางวินิจฉัยสำหรับ mechanical limiter | ต้องพิสูจน์เหตุ ไม่ใช่ทุก P0093 | กราฟไม่มีค่า OEM',
14:'หลักการวัดด้านดูดเฉพาะระบบ vacuum-fed ที่ยืนยันแล้ว | ไม่มีเกณฑ์ vacuum สากล | ไม่ใช่การวัดรางแรงดันสูง',
15:'ผังเลือกวิธีทดสอบ | ต้องตรงชนิดหัวฉีดและแรงดันทางกลับ | ไม่ใช่วิธีถอด return ที่ใช้ได้ทุกระบบ',
16:'ผังวิธีคิดของบรรณาธิการ ไม่ใช่ขั้นตอน Toyota ทุกข้อ | เลือกทางตรวจตามหลักฐานและคู่มือรถจริง'
}
m=json.loads((P/'circuits_manifest.json').read_text(encoding='utf-8'))
registry=json.loads((P.parent/'research'/'claim_ledger.json').read_text(encoding='utf-8'))['source_registry']
url_to_id={v:k for k,v in registry.items()}
result=[]
for item in m['diagrams']:
 i=int(item['id']);r=ET.parse(P/item['svg']).getroot();removed=[]
 for el in list(r):
  if el.tag==N+'text':
   y=float(el.get('y','0'))
   if y>=1040:
    removed.append(''.join(el.itertext()));r.remove(el);continue
   if y==140:el.text=scopes[i]
   if float(el.get('font-size','22'))<22:el.set('font-size','22')
  if el.tag==N+'polyline' and el.get('points','').startswith('60,1040 '):r.remove(el)
 h=heights[i];r.set('height',str(h));r.set('viewBox',f'0 0 1800 {h}')
 for el in r:
  if el.tag==N+'rect' and el.get('width')=='1800' and el.get('height')=='1250':el.set('height',str(h))
 (out/item['svg']).write_text(ET.tostring(r,encoding='unicode'),encoding='utf-8')
 record={k:v for k,v in item.items() if k not in ['source_ids','review']}
 fitw=min(269,150*1800/h)
 record.update(svg='print/'+item['svg'],png='print/'+item['png'],print_svg='print/'+item['svg'],print_png='print/'+item['png'],viewbox=[0,0,1800,h],canvas_px=[1800,h],min_main_font_px=22,expected_width_mm_fit_269x150=round(fitw,2),expected_min_font_pt_at_fit=round(22*fitw/25.4*72/1800,2),source_ids=[url_to_id[u] for u in item['sources'] if u in url_to_id],unregistered_source_urls=[u for u in item['sources'] if u not in url_to_id],retained_scope_th=scopes[i],removed_below_drawing_text=removed,external_caption_required=True,review='all 16 rendered print PNGs visually reviewed; bounds passed; final PDF fitting still requires QA; see PRINT_ASSETS.md')
 result.append(record)
data=json.dumps({'version':'2026-10-21-print-r1','print_width_mm':269,'max_print_height_mm':150,'created':len(result),'external_caption_and_scope_required':True,'diagrams':result},ensure_ascii=False,indent=2)
(out/'print_manifest.json').write_text(data,encoding='utf-8');(P/'print_manifest.json').write_text(data,encoding='utf-8')
print('print assets',len(result))

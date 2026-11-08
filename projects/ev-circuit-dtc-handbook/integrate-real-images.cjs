const fs=require('fs');
const crypto=require('crypto');
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const read=p=>fs.existsSync(p)?JSON.parse(fs.readFileSync(p,'utf8').replace(/^\uFEFF/,'')):[];
module.exports=function(P){
 const pools=['researched-components.json','researched-systems.json','researched-instruments.json'].flatMap(read);
 const imgs=pools.map(x=>({...x,file:x.localFile||x.localPath,source:x.sourceUrl||x.sourceURL,licenseHref:x.licenseUrl||x.licenseURL||x.sourceUrl||x.sourceURL,subject:x.actualSubject||x.subject||x.title,creator:x.requiredAttribution||x.creator})).filter(x=>x.file&&fs.existsSync(x.file)&&x.eligible!==false&&!['excluded','excluded_rights','excluded_subject','invalid'].includes(x.downloadStatus)&&!x.excluded&&x.id!=='SYS76762500');
 imgs.push({id:'ADA01',title:'Adafruit CAN Bus BFF PCB',file:'assets/can-bff.jpg',subject:'Adafruit CAN Bus BFF — บอร์ดทดลอง ไม่ใช่ ECU รถ',creator:'Adafruit Industries',source:'https://github.com/adafruit/Adafruit-CAN-Bus-BFF-PCB',license:'CC BY-SA 3.0',licenseHref:'https://creativecommons.org/licenses/by-sa/3.0/'});
 const wanted=[
 ['SYS75308683','cmp02'],['SYS20709410','cmp11'],['SYS4661762','cmp52'],['cmp02','cmp11'],['cmp21','cmp17'],
 ['cmp48','cmp44'],['cmp14','cmp44'],['SYS4661762','cmp03'],['SYS4661762','cmp48'],['SYS4661762','cmp44'],
 ['cmp47','cmp48'],['cmp48','cmp52'],['ADA01','SYSA4759'],['cmp44','cmp48'],['cmp45','cmp50'],
 ['cmp50','cmp12'],['cmp50','cmp48'],['cmp52','cmp50'],['cmp25','cmp50'],['cmp52','cmp16'],
 ['cmp18','cmp19'],['cmp18','cmp21'],['cmp52','cmp02'],['cmp03','cmp22'],['cmp29','cmp31'],
 ['cmp05','cmp04'],['cmp06','cmp29'],['cmp31','SYS4661762'],['cmp04','SYS45826314'],['cmp04','SYS20709410'],
 ['ADA01','SYSA5708'],['ADA01','SYSA5724'],['SYSA4759','SYSA5708'],['SYSA5709','SYSA4759'],['SYSA5708','SYSA5724'],
 ['SYS4661762','cmp44'],['cmp52','cmp08'],['cmp45','SYS4661762'],['cmp22','cmp23'],['cmp05','cmp04'],
 ['cmp44','cmp48'],['cmp37','cmp36'],['cmp14','cmp52'],['cmp14','cmp52'],['cmp45','SYS4661762'],
 ['cmp08','cmp52'],['SYS4661762','cmp48'],['cmp14','SYS157506859'],['SYS4661762','cmp52'],['cmp04','cmp18']
 ];
 const captions={
 'cmp02':'ชุดขับเคลื่อน Nissan LEAF ZE1 ที่จัดแสดง', 'cmp03':'ชุดขับเคลื่อน LEAF ZE1 อีกมุม — ไม่เห็น pinout ภายใน',
 'cmp04':'ช่องชาร์จ LEAF — ไม่ใช่ภาพ OBC', 'cmp05':'อุปกรณ์ TC Charger ภายนอก — ไม่ระบุวงจรภายใน', 'cmp06':'TC Charger อีกมุม — ไม่ใช่ผลทดสอบชาร์จ',
 'cmp08':'แพ็ก LEAF จัดแสดง — ไม่ใช่แพ็กที่วินิจฉัยเสีย', 'cmp09':'ตัวอย่างแบตเตอรี่ Nissan ในงานจัดแสดง',
 'cmp10':'โมดูลแบตเตอรี่ Prius — เทียบไฮบริด ไม่ใช่แพ็ก Camry ในกรณีศึกษา',
 'cmp11':'แพ็ก BMW i3 — ตัวอย่างต่างรุ่น ไม่ใช้แทนผังรถ', 'cmp12':'เซลล์ BMW i3 — ภาพประกอบ ไม่ใช่ผลวัดหรือแพ็ก Camry',
 'cmp14':'แพ็ก VinFast VF 8 จัดแสดง — ไม่ใช่รถน้ำท่วม', 'cmp16':'แพ็ก VF 8 — ภาพไม่ระบุทางเดิน HVIL หรือคอนแทกเตอร์',
 'cmp17':'แพ็ก Volkswagen e-up — ภาพไม่ระบุตำแหน่ง NTC', 'cmp18':'Aisin Xin1 ชุดขับเคลื่อนจัดแสดง', 'cmp19':'Astemo BEV e-Axle จัดแสดง',
 'cmp21':'Valeo 48 V motor/inverter — ไม่ใช่ระบบ HV ตัวอย่าง', 'cmp22':'ชุด Inverter/Motor/Gearbox — ไม่ใช่แผนผัง Gate', 'cmp23':'ชุดขับเคลื่อนอีกมุม — ไม่ระบุรหัสอะไหล่รถในกรณีศึกษา',
 'cmp25':'บาลานเซอร์ ELV 2s–4s — ตัวอย่างหลักการ ไม่ใช่ BMS รถ', 'cmp29':'ห้องอุปกรณ์ Mitsubishi i-MiEV — ไม่ใช่ผลตรวจระบบ',
 'cmp31':'ชุดขับเคลื่อน e-Golf ตัดแสดง — ไม่ระบุขา DC-DC', 'cmp36':'ฝาช่องชาร์จ Chevrolet Bolt EV ขณะปิด', 'cmp37':'ช่องชาร์จ Bolt EV ขณะเปิด',
 'cmp38':'Audi e-tron ชุดควบคุมมอเตอร์ตัดแสดง', 'cmp39':'Rimac ECU — ตัวอย่างกล่องควบคุมจริง', 'cmp40':'Kilovac EV200 — คอนแทกเตอร์จริง ไม่ใช่การยืนยันหน้าสัมผัสเสีย',
 'cmp44':'foxBMS Master รุ่น 1 — หัวต่อชุดวิจัย ไม่ใช่ VCU รถ',
 'cmp45':'foxBMS Master เปิดฝา — ชุดวิจัย ไม่ใช่กล่อง OEM รถ',
 'cmp47':'foxBMS Master PCB — ชุดวิจัย ไม่ใช่ ECU OEM',
 'cmp48':'foxBMS Extension I/O — ชุดวิจัย ไม่ใช่กล่อง OEM',
 'cmp50':'foxBMS Slave วัดเซลล์/อุณหภูมิ/balance — ชุดวิจัย ไม่ใช่ OEM',
 'cmp52':'foxBMS Junction Box: sensor/contactor — ชุดวิจัย ไม่ใช่ OEM',
 'SYS4428906':'สายไฟ Geo Storm (รถเครื่องยนต์) — เทียบงานสายเท่านั้น', 'SYS640883':'หัวต่อ ISO เครื่องเสียง — ไม่ใช่หัวต่อ ECU/CAN รถ',
 'SYS4661762':'Fluke 87 III — ภาพเครื่องมือ ไม่ระบุว่าพิกัดเหมาะทุกงาน HV', 'SYS61976909':'Fluke 115 — ใช้อธิบายงาน LV ไม่ใช่จุดวัดรถจริง',
 'SYS120411918':'Fluke 1507 — การตั้งค่า/จุดแยกต้องใช้วิธี OEM', 'SYS7703121':'Fluke 337 — ไม่ใช้ภาพรับรองพิกัดหรือวิธีหนีบสาย HV',
 'SYS16007442':'โต๊ะงานอิเล็กทรอนิกส์ — รูปคลื่นในภาพไม่ใช่ผลวัด CAN รถ',
 'SYS27732615':'PCB กัดกร่อนจาก NiCd รั่ว — ไม่ใช่น้ำท่วมหรือ ECU รถ', 'SYS114916435':'NiCd รั่วบน PCB — เทียบลักษณะกัดกร่อน ไม่ยืนยันน้ำท่วม',
 'SYS75308683':'Nissan LEAF ปี 2018 — ภาพรถจริง', 'SYS76762500':'LEAF Tekna ขณะชาร์จ — ไม่ใช่รถในกรณีศึกษา',
 'SYS20709410':'สถานีชาร์จ Electric Avenue — ภาพประกอบบริบท', 'SYS45826314':'หัวชาร์จ AC Type 2 — ไม่ใช้ภาพนับ pinout รถ',
 'SYS107931146':'หัวชาร์จ DC CHAdeMO — ไม่ใช่ CCS', 'SYS61915668':'เปรียบเทียบ CHAdeMO / CCS2 / Type 2',
 'SYS12303102':'ช่องชาร์จ LEAF — ผังขาต้องใช้เอกสารตรงรุ่น', 'SYS95810200':'EVSE Veefil DC 50 kW — ไม่ใช่ผลทดสอบชาร์จรถ',
 'ADA01':'CAN Bus BFF ของ Adafruit — บอร์ดทดลอง ไม่ใช่ ECU OEM',
 'SYSA4759':'Adafruit Feather M4 CAN — บอร์ดพัฒนา ไม่ใช่ ECU รถ',
 'SYSA5724':'Adafruit RP2040 CAN — บอร์ดทดลอง ไม่ใช่กล่องรถ',
 'SYSA5708':'Adafruit CAN Pal — สวิตช์ termination ไม่ใช่ jumper'
 };
 const placements=[];const missing=[];
 function lookup(id,p){const x=imgs.find(x=>x.id===id);if(!x){missing.push({page:p,id});return null}return x}
 function photo(x,p,position){
  const cap=captions[x.id]||x.subject;placements.push({page:p,position,imageId:x.id,file:x.file,caption:cap,creator:x.creator,sourceUrl:x.source,license:x.license,licenseUrl:x.licenseHref});
  const shortCreator=String(x.creator).includes('Fraunhofer')?'Fraunhofer IISB / foxBMS':x.creator;
  return `<figure class="real-photo" data-image-id="${esc(x.id)}" data-image-type="C"><img src="${esc(x.file)}" alt="${esc(cap)}"><figcaption><b>C · ${esc(cap)}</b><br><a href="${esc(x.source)}">${esc(x.id)} · ${esc(shortCreator)}</a> · <a href="${esc(x.licenseHref)}">${esc(x.license)}</a><br>ภาพจริงประกอบการศึกษา • ย่อจัดหน้า ไม่ใช่หลักฐานอาการเสีย</figcaption></figure>`;
 }
 for(let i=0;i<50;i++){
  const pair=wanted[i].map(id=>lookup(id,i+1));if(pair.some(x=>!x))continue;
  if(pair[0].file===pair[1].file)throw Error('Duplicate source on page '+(i+1));
  const strip=`<div class="real-photo-pair">${pair.map((x,j)=>photo(x,i+1,j+1)).join('')}</div>`;
  P[i].body=strip+P[i].body;
 }
 if(missing.length){fs.writeFileSync('missing-image-placements.json',JSON.stringify(missing,null,2));throw Error('Real photo placements missing: '+JSON.stringify(missing));}
 // A documented reference circuit is not counted as a photograph.
 P[16].body=P[16].body.replace(/<figure class="visual">[\s\S]*?<\/figure>/,`<figure class="actual temp-reference"><img style="height:150px" src="assets/real-images/cmp51.png" alt="วงจรวัดอุณหภูมิอ้างอิง foxBMS"><figcaption><b>A · Actual Wiring Diagram — วงจรอ้างอิง foxBMS รุ่น 1</b><br><a href="https://github.com/foxBMS/foxBMS-documentation/blob/master/doc/sphinx/getting_started/cabling/temperature_sensor.png">Fraunhofer IISB / foxBMS — ภาพจากเอกสารผู้พัฒนา</a> · <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a><br>20 kΩ เป็นค่าของแบบอ้างอิงนี้ ไม่ใช่เกณฑ์รถทุกคัน • ไม่ใช่ผังสายไฟ OEM • คงต้นฉบับ ย่อจัดหน้า</figcaption></figure>`);
 // Enlarge the actual schematic in-page while preserving the original file.
 P[31].body=P[31].body.replace('<img src="assets/can-schematic.png" alt="วงจรจริง Adafruit CAN Bus BFF">','<svg viewBox="850 150 1200 650" xmlns="http://www.w3.org/2000/svg" class="schematic-detail" aria-label="ภาพขยาย IC และ termination จากวงจรต้นฉบับ"><image href="assets/can-schematic.png" width="2760" height="2135"/></svg>').replace('คงภาพต้นฉบับ ย่อเพื่อจัดหน้า','ขยายและแสดงเฉพาะภาค IC/termination; ไฟล์ต้นฉบับเต็มอยู่ assets');
 // New cover uses two actual photographs and deterministic live typography.
 const coverPair=placements.filter(x=>x.page===1);
 P[0].title='EV CIRCUIT<br><span>& DTC</span><br>HANDBOOK';
 P[0].sub='คู่มือวงจรไฟฟ้ารถยนต์ EV<br>พร้อมการตรวจวิเคราะห์รหัสข้อผิดพลาด DTC';
 P[0].body=`<div class="cover-tags">วงจรไฟฟ้า / การตรวจวัด / DTC / รถหลังน้ำท่วม</div><div class="cover-photos">${coverPair.map(x=>photo(imgs.find(v=>v.id===x.imageId),1,x.position)).join('')}</div><div class="cover-bottom"><b>50 หน้า A4</b><span>คู่มือประกอบการเรียนรู้และวางแผนตรวจงาน<br>ฉบับเพิ่มภาพจริงและสอบทวนโดย agent</span></div><div class="cover-disclaimer">ภาพประกอบเป็นรถและอุปกรณ์จริงตามรุ่นที่ระบุ ไม่ใช่หลักฐานผลวัดหรือรถเสียในกรณีศึกษา<br>ต้นฉบับเพื่อการศึกษา • งาน HV ต้องใช้ผู้มีคุณสมบัติและคู่มือ OEM ตาม VIN</div>`;
 // photo() was used again for cover markup; retain one record per page/position.
 const uniquePlacements=[...new Map(placements.map(x=>[x.page+':'+x.position,x])).values()];
 fs.writeFileSync('image-placements.json',JSON.stringify(uniquePlacements,null,2));
 const usedIds=new Set(uniquePlacements.map(x=>x.imageId));
 const manifest=imgs.filter(x=>usedIds.has(x.id)).map(x=>({...x,sha256:crypto.createHash('sha256').update(fs.readFileSync(x.file)).digest('hex'),pages:uniquePlacements.filter(p=>p.imageId===x.id).map(p=>p.page)}));
 fs.writeFileSync('real-images-final-manifest.json',JSON.stringify(manifest,null,2));
 fs.writeFileSync('real-image-credits.md','# เครดิตภาพจริงฉบับเพิ่มภาพ\n\nภาพจริง 2 ไฟล์ต่างกันต่อหน้า รวม '+uniquePlacements.length+' ตำแหน่ง จาก '+manifest.length+' ไฟล์ภาพ มีการใช้ภาพซ้ำข้ามหน้าเมื่อเกี่ยวข้อง ไม่ใช้ภาพสอง crop จากไฟล์เดียวกันให้นับเป็นสองภาพ\n\n'+manifest.map(x=>`## ${x.id} — ${x.subject}\n\n- ภาพต้นทาง: [${x.title}](${x.source})\n- ผู้สร้าง/เครดิต: ${x.creator}\n- เครดิตต้นฉบับเพิ่มเติม: ${x.sourceCredit||''}\n- สิทธิ์: [${x.license}](${x.licenseHref})\n- ไฟล์: ${x.file}\n- หน้า: ${x.pages.join(', ')}\n- ข้อจำกัด: ${x.limitations||x.restrictions||'ภาพประกอบบริบท ไม่ใช่หลักฐานอาการเสียหรือผังสายไฟรถ'}\n- การจัดหน้า: ย่อและวางในกรอบ ไม่แก้ไขสาระภาพ\n`).join('\n'));
 fs.appendFileSync('real-image-credits.md','\n## วงจรอ้างอิง A เพิ่มเติม หน้า17 (ไม่นับภาพถ่าย)\n\nFraunhofer IISB / foxBMS: https://github.com/foxBMS/foxBMS-documentation/blob/master/doc/sphinx/getting_started/cabling/temperature_sensor.png\n\nCopyright (c) 2010–2017 Fraunhofer-Gesellschaft zur Foerderung der angewandten Forschung e.V. This handbook includes parts of foxBMS documentation. CC BY 4.0, https://creativecommons.org/licenses/by/4.0/ . คงต้นฉบับ ย่อจัดหน้า ไม่ใช่ผังสายไฟ OEM\n');
 return {css:`
 .real-photo-pair{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin:10px 0 12px}.real-photo{margin:0;padding:6px;background:#f6f9fa;border:1px solid #cedde3;min-width:0}.real-photo img{width:100%;height:140px;object-fit:contain;display:block;background:#fff}.real-photo figcaption{font-size:9px;line-height:1.4;margin-top:5px}.real-photo figcaption b{color:#183b4b}.page:nth-child(49) .real-photo img{height:112px}.page:nth-child(49) .real-photo figcaption{font-size:8px}.page .actual .schematic-detail{height:260px}.terms{font-size:10px;border-top:1px solid #d1dfe4;padding-top:5px;color:#58717f}
 body{font-size:12.5px}.page table{font-size:12.5px}.page td,.page th{padding:8px 9px}.page figure.visual svg{height:150px}.page .slot{min-height:85px;padding:12px}.page .slot small{font-size:9px}.page .field{font-size:9px;line-height:1.6;padding:8px}.page .steps>div{padding:7px}.page aside{padding:9px 12px;font-size:11.5px;margin:10px 0}.page .refs{font-size:8px}.page .sub{margin-bottom:10px}.page h1{font-size:25px}.page figure.visual{margin:9px 0;padding:7px}.page figure.visual figcaption{font-size:8px}.page .actual img{height:230px}.page .photo img{height:170px}
 .page:first-child{background:#071b2d;color:#fff;padding:14mm}.page:first-child .top{color:#68d5dc;border-color:#3a7082}.page:first-child h1{font-size:49px;line-height:1.04;letter-spacing:-1px;margin:20px 0 17px}.page:first-child h1 span{color:#6cdee3}.page:first-child .sub{font-size:18px;color:#e2edf2;line-height:1.6}.cover-tags{font-size:12px;color:#86d5dc;margin:15px 0}.cover-photos{display:grid;grid-template-columns:1.6fr 1fr;gap:12px;margin:20px 0}.cover-photos .real-photo{background:#102c40;border:1px solid #31566b;color:white;padding:8px}.cover-photos img{height:250px;background:#102c40}.cover-photos figcaption{font-size:9px;line-height:1.55;color:#adc6d4}.cover-photos figcaption b,.cover-photos a{color:#b0e6eb}.cover-bottom{display:flex;gap:25px;align-items:center;border-top:1px solid #31566b;padding-top:18px;margin-top:20px}.cover-bottom b{font-size:30px;color:#6cdee3;white-space:nowrap}.cover-bottom span{font-size:13px;color:#d7e8ef}.cover-disclaimer{font-size:9px;line-height:1.6;margin-top:20px;color:#9eb8c8}.page:first-child .foot{border-color:#31566b;color:#a6c3d2}
 `,summary:{photographicPlacements:uniquePlacements.length,uniquePhotoFiles:manifest.length,eachPageTwoDistinct:true}};
};

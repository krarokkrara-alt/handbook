from pathlib import Path
p=Path('tools/build_prototype.py');s=p.read_text(encoding='utf8')
s=s.replace('from docx.enum.text import WD_ALIGN_PARAGRAPH','from docx.enum.text import WD_ALIGN_PARAGRAPH\nfrom docx.enum.section import WD_SECTION_START,WD_ORIENT\nfrom docx.opc.constants import RELATIONSHIP_TYPE as RT')
s=s.replace("if not t:flush();continue", "if not t:flush();continue\n if t=='<!-- pagebreak -->':flush();blocks.append(('pagebreak',None));continue")
pos=s.index('\ndef inline(s):')
s=s[:pos]+'''
# Replace atlas blocks with physical landscape plates; retain full teaching notes afterwards.
plate_manifest=json.loads((P/'circuits/print_manifest.json').read_text(encoding='utf8'))
plates={d['id']:d for d in plate_manifest['diagrams']}
newblocks=[];notes=[];i=0;in_atlas=False
while i<len(blocks):
 kind,value=blocks[i]
 if kind=='h2' and value.startswith('ภาคหนึ่ง'):
  in_atlas=True;i+=1
  if i<len(blocks) and blocks[i][0]=='p':i+=1
  continue
 match=re.match(r'^ภาพ (\\d+)',value) if kind=='h3' else None
 if in_atlas and match:
  key=match[1].zfill(2);d=plates[key];newblocks.append(('plate',d));notes.append(d);i+=1
  while i<len(blocks) and blocks[i][0]!='h2' and not (blocks[i][0]=='h3' and re.match(r'^ภาพ \\d+',blocks[i][1])):i+=1
  continue
 if in_atlas and notes:
  newblocks.append(('h2','คำอธิบายประกอบแผ่นวงจร'))
  for d in notes:newblocks.extend([('h3','ภาพ '+d['id']+' '+d['title_th']),('p',d['teaching_note_th'])])
  in_atlas=False
 newblocks.append(blocks[i]);i+=1
blocks=newblocks
''' +s[pos:]
s=s.replace("html=[];imcount=0",'''html=[];imcount=0;landscape=False

def page_orientation(wide):
 global landscape
 if wide==landscape:
  if wide:doc.add_page_break()
  return False
 section=doc.add_section(WD_SECTION_START.NEW_PAGE)
 section.orientation=WD_ORIENT.LANDSCAPE if wide else WD_ORIENT.PORTRAIT
 section.page_width=Cm(29.7 if wide else 21);section.page_height=Cm(21 if wide else 29.7)
 section.top_margin=section.bottom_margin=Cm(1.2 if wide else 1.65)
 section.left_margin=section.right_margin=Cm(1.2 if wide else 1.8)
 landscape=wide
 return True

def wordlink(paragraph,label,url):
 link=OxmlElement('w:hyperlink');link.set(qn('r:id'),paragraph.part.relate_to(url,RT.HYPERLINK,is_external=True))
 run=OxmlElement('w:r');rpr=OxmlElement('w:rPr');size=OxmlElement('w:sz');size.set(qn('w:val'),'18');rpr.append(size);run.append(rpr);t=OxmlElement('w:t');t.text=label;run.append(t);link.append(run);paragraph._p.append(link)
''')
s=s.replace("for kind,value in blocks:\n if kind.startswith('h'):",'''for kind,value in blocks:
 if kind=='plate':
  d=value;page_orientation(True);path=P/'circuits'/d['png'];im=Image.open(path);w,h=im.size;ww=min(26.9,15*w/h)
  head=doc.add_paragraph('ภาพ '+d['id']+' '+d['title_th'],'Heading 3');head.paragraph_format.keep_with_next=True
  pp=doc.add_paragraph();pp.alignment=WD_ALIGN_PARAGRAPH.CENTER;pp.paragraph_format.space_after=Pt(2);pp.add_run().add_picture(str(path),width=Cm(ww))
  scope='ตัวอย่าง DR201E Hilux TASA Argentina เท่านั้น' if d['id'] in ['11','12'] else 'ผังหลักการ ไม่ใช่ผัง OEM สากล'
  pp=doc.add_paragraph(d['caption_th']+' • '+scope,'Caption');pp.paragraph_format.space_after=Pt(2)
  pp=doc.add_paragraph('แหล่งอ้างอิง ', 'Caption')
  for n,url in enumerate(d['sources'],1):wordlink(pp,'['+str(n)+'] ',url)
  if not d['sources']:pp.add_run('แบบจำลองวงจรที่ผู้เขียนวาดขึ้น')
  links=' • '.join('<a href="'+escape(u)+'">แหล่ง '+str(j+1)+'</a>' for j,u in enumerate(d['sources'])) or 'แบบจำลองวงจรที่ผู้เขียนวาดขึ้น'
  html.append('<section class="plate"><h3>ภาพ '+d['id']+' '+escape(d['title_th'])+'</h3><img src="'+path.as_uri()+'"><p class="plate-caption">'+escape(d['caption_th'])+' • '+scope+'</p><p class="plate-source">'+links+'</p></section>');imcount+=1;continue
 switched=page_orientation(False) if landscape else False
 if kind=='pagebreak':
  doc.add_page_break();html.append('<div class="pagebreak"></div>');continue
 if kind.startswith('h'):''')
s=s.replace("if level==2 and len(html)>2:p.paragraph_format.page_break_before=True", "if level==2 and len(html)>2 and not switched:p.paragraph_format.page_break_before=True\n  if re.match(r'^แบบ0[1-6]',value):p.paragraph_format.page_break_before=True")
s=s.replace("html.append(f'<h{min(level,4)}>'+inline(value)+f'</h{min(level,4)}>')", "html.append(f'<h{min(level,4)}'+(' class=\"field-start\"' if re.match(r'^แบบ0[1-6]',value) else '')+'>'+inline(value)+f'</h{min(level,4)}>')")
a=s.index("  html.append('<table>'+''.join");b=s.index("\n else:\n  text=clean",a)
s=s[:a]+'''  # Repeat header rows in both rendering paths.
  if tab.rows:
   hp=tab.rows[0]._tr.get_or_add_trPr();flag=OxmlElement('w:tblHeader');hp.append(flag)
  header='<thead><tr>'+''.join('<th>'+inline(c)+'</th>' for c in value[0])+'</tr></thead>'
  bodyrows='<tbody>'+''.join('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in row)+'</tr>' for row in value[1:])+'</tbody>'
  sourceclass=' class="source-table"' if value[0][0].strip().lower() in ['id','รหัส','source id'] else ''
  html.append('<table'+sourceclass+'>'+header+bodyrows+'</table>')''' +s[b:]
s=s.replace("css='''@page{size:A4;", "css='''@page diagram{size:A4 landscape;margin:12mm}@page{size:A4;")
s=s.replace("body='\\n'.join(html);", "css+=''' .plate{page:diagram;width:273mm;break-before:page;break-after:page}.plate h3{margin:0 0 2mm;font-size:14pt}.plate img{width:269mm;height:150mm;max-height:none;object-fit:contain;margin:0 auto 1mm}.plate p{margin:0 0 1mm}.plate-caption{font-size:10pt;line-height:1.22}.plate-source{font-size:9pt;line-height:1.2}.pagebreak,.field-start{break-before:page}thead{display:table-header-group;break-after:avoid}tfoot{display:table-footer-group}.source-table td:first-child,.source-table th:first-child{white-space:nowrap;min-width:12mm} '''\nbody='\\n'.join(html);")
s=s.replace("body=re.sub(r'<h3>(ภาพ .*?)</h3>',r'<h3 class=\"figure-title\">\\1</h3>',body)", "body=body")
p.write_text(s,encoding='utf8',newline='\n')

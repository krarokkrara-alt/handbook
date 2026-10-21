from pathlib import Path
import re,json
p=Path(__file__).parent
s=(p/'CIRCUIT_PLAN.md').read_text(encoding='utf-8')
refs={
'C01':'https://www.denso-am.eu/products/diesel-components/common-rail-suction-control-valve-scv',
'C02':'https://www.denso-am.eu/news/fourth-generation-common-rail-diesel-diagnosis-suction-control-valve',
'C03':'https://www.denso-am.eu/products/diesel-components/common-rail-pump',
'C04':'https://www.denso-am.eu/products/diesel-components',
'C05':'https://www.service-engine.com.ua/webroot/pdf/TOYOTA%201KD%202KD%20ENGINE.pdf',
'C06':'https://toyotamanuals.gitlab.io/PZ471-Z00W0-CA/htmlweb/rm/rm1151e/m_05_0501.pdf',
'C07':'https://www.pumbaoverland.com/files/TOYOTA_Injection_manual_1KD_2KD.pdf',
'C08':'https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0070.pdf',
'C09':'https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0078.pdf',
'C10':'https://www.picoauto.com/library/automotive-guided-tests/pressure-transducers/wps500x-pressure-transducer/AGT-833-negative-priming-fuel-pressure-diesel/',
'C11':'https://www.picoauto.com/library/automotive-guided-tests/pres/wps500x-pressure-transducer/AGT-786-crd-injector-back-leakage/',
'C12':'https://toyotamanuals.gitlab.io/PZ471-Z00W0-CA/htmlweb/rm/rm1151e/m_05_0486.pdf'}
a=[]
for t in re.split(r'\n### ',s)[1:]:
 header=t.splitlines()[0]; name=re.search(r'`([^`]+\.svg)`',t)
 if not name:continue
 cap=re.search(r'\*\*คำบรรยาย:\*\* (.*)',t).group(1)
 teach=re.search(r'\*\*ใช้สอน:\*\* (.*)',t).group(1)
 codes=sorted(set(re.findall(r'C(?:0[1-9]|1[012])',t.split('**คำบรรยาย:')[0])))
 scope='verified connection redraw: Toyota DR201E Hilux TASA Argentina only; not universal pinout' if int(header[:2]) in (11,12) else 'original educational concept; not universal OEM wiring; no inferred pinout'
 a.append(dict(id=header[:2],title_th=header[5:],svg=name.group(1),png=name.group(1).replace('.svg','.png'),caption_th=cap,teaching_note_th=teach,source_ids=codes,sources=[refs[c] for c in codes],scope=scope,review='round-two visual and source-scope review completed; see QA.md; not vehicle certification'))
(p/'circuits_manifest.json').write_text(json.dumps({'version':'2026-10-21-r2','created':len(a),'planned_total':16,'diagrams':a},ensure_ascii=False,indent=2),encoding='utf-8')
print(len(a))

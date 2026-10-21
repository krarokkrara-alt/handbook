from pathlib import Path
p=Path(__file__).parent.parent/'manuscript'/'OPERATING_CIRCUITS.md'
s=p.read_text(encoding='utf-8')
for a,b in {
'C13/T04':'T04','C06/T05':'T05','C01/D02':'D06','C02/D01':'D01','C05/D05':'D05','C09/T03':'T03','C08/T02':'T02','C12/T06':'T06','C11/P01':'P01',
'[C03/C04]':'[DENSO Common Rail Pump](https://www.denso-am.eu/products/diesel-components/common-rail-pump) และ [DENSO Diesel Components](https://www.denso-am.eu/products/diesel-components)',
'; C03]':'; [DENSO Common Rail Pump](https://www.denso-am.eu/products/diesel-components/common-rail-pump)]',
'[C10/P02 สำหรับหลักการตรวจ vacuum-fed supply]':'[Pico AGT-833: หลักการตรวจ vacuum-fed supply](https://www.picoauto.com/library/automotive-guided-tests/pressure-transducers/wps500x-pressure-transducer/AGT-833-negative-priming-fuel-pressure-diesel/)',
'ภาพ 08 ขยายกรณี':'**การอนุมานจากหลักวงจรทั่วไป (derivation ไม่ใช่ข้อกำหนด Toyota):** ภาพ 08 ขยายกรณี'
}.items():s=s.replace(a,b)
start=s.index('## ทะเบียนแหล่งอ้างอิงและ aliases')
end=s.index('## หมายเหตุให้ฝ่ายจัดหน้าและผู้ตรวจ')
refs='''## ทะเบียนแหล่งอ้างอิง

ใช้ canonical source IDs ของ `research/claim_ledger.json` ตรงกันทั้งบท ภาพใน `circuits_manifest.json` อาจยังมีรหัส Cxx เดิมของชุดภาพ ให้จับคู่ด้วย URL และแปลงเป็นทะเบียนกลางตอนจัดเล่ม รหัส C001 เป็นต้นใน claim ledger เป็น claim ID ไม่ใช่ source ID

| Source ID | ต้นทางและขอบเขต |
|---|---|
| D06 | [DENSO Common Rail SCV — English](https://www.denso-am.eu/products/diesel-components/common-rail-suction-control-valve-scv) — ทางการ; หน้าที่/ชนิดทั่วไป; D02 เป็นหน้า Italian ที่เกี่ยวข้อง แต่ URL ไม่เหมือนกัน |
| D01 | [DENSO Fourth generation common rail diesel diagnosis – suction control valve](https://www.denso-am.eu/news/fourth-generation-common-rail-diesel-diagnosis-suction-control-valve) — 11 May 2023; เว็บไซต์ทางการ |
| D05 | [DENSO 00400706E, Toyota 1KD/2KD Engine](https://www.service-engine.com.ua/webroot/pdf/TOYOTA%201KD%202KD%20ENGINE.pdf) — เอกสารผู้ผลิตโฮสต์ภายนอก; ออก September 2009; applicability August 2009 ตามตาราง ไม่ใช่ทุกปีทุกตลาด |
| T05 | [Toyota RM1151E หน้า 05–501 ถึง 05–504](https://toyotamanuals.gitlab.io/PZ471-Z00W0-CA/htmlweb/rm/rm1151e/m_05_0501.pdf) — 1KD-FTV From August 2004; OEM document โฮสต์ภายนอก ไม่อ้างว่าเป็นคู่มือไทย |
| T02 | [Toyota DR201E หน้า 05–70 ถึง 05–77](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0070.pdf) — Hilux TASA Argentina; วงจรเซ็นเซอร์ |
| T03 | [Toyota DR201E หน้า 05–78 ถึง 05–83](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0078.pdf) — Hilux TASA Argentina; SCV / P0088 / P1229 |
| P01 | [Pico AGT-786 CRD injector back-leakage](https://www.picoauto.com/library/automotive-guided-tests/pres/wps500x-pressure-transducer/AGT-786-crd-injector-back-leakage/) — solenoid / low-return-pressure method; ไม่ใช่ return specification ทุกรุ่น |
| T06 | [Toyota RM1151E หน้า 05–486 ถึง 05–492](https://toyotamanuals.gitlab.io/PZ471-Z00W0-CA/htmlweb/rm/rm1151e/m_05_0486.pdf) — ตัวอย่างโครงสร้างเซ็นเซอร์ต่างจาก DR201E |
| T04 | [Toyota DR201E หน้า 05–5 ถึง 05–15](https://toyotamanuals.gitlab.io/hiluxoct2010/rm/dr201e/m_05_0005.pdf) — ระบบควบคุม ปั๊ม และ SCV ของ application ในหัวเอกสาร |

แหล่งที่ยังไม่ลง canonical ID อ้างด้วย URL ตรง ไม่สร้าง alias ขึ้นเอง: [DENSO Common Rail Pump](https://www.denso-am.eu/products/diesel-components/common-rail-pump), [DENSO Diesel Components](https://www.denso-am.eu/products/diesel-components), [Pico AGT-833 Negative priming fuel pressure](https://www.picoauto.com/library/automotive-guided-tests/pressure-transducers/wps500x-pressure-transducer/AGT-833-negative-priming-fuel-pressure-diesel/)

'''
s=s[:start]+refs+s[end:]
p.write_text(s,encoding='utf-8')
print('normalised',len(s),'characters')

# สร้างผังขั้วต่อ ECM, ผังบล็อก, และตารางขา ECM จากข้อมูลชุดเดียวใน FACTS.md
# วิธีใช้: python gen_ecm.py
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / 'circuits'
FONT = 'Tahoma, Leelawadee UI, sans-serif'
COL = {'pw': '#d52830', 'gn': '#222222', 'edu': '#e07b00', 'act': '#0d3b66', 'sen': '#1a7f37', 'io': '#7a4fa3'}
NAME = {'pw': 'ไฟเลี้ยง', 'gn': 'กราวด์', 'edu': 'EDU / TCV', 'act': 'คุมรีเลย์และวาล์ว', 'sen': 'เซ็นเซอร์', 'io': 'สัญญาณอื่น'}

J1 = {
    1: ('0.5 R', 'Cam Sensor (+)', 'E-28/2', 'sen'), 9: ('0.5 W/R', 'VSV EGR1', 'C-31/2', 'act'),
    10: ('0.5 W/B', 'VSV EGR2', 'C-32/2', 'act'), 14: ('0.5 G', 'Boost 5V', 'E-25/3', 'sen'),
    17: ('0.5 G', 'Cam Sensor (−)', 'E-28/1', 'sen'), 23: ('0.5 W', 'TDC Sensor สัญญาณ', 'E-9/2', 'sen'),
    25: ('0.5 Y', 'TCV', 'E-24/2', 'edu'), 26: ('0.5 W/O', 'EVRV', 'C-115/2', 'act'),
    28: ('0.5 G/Y', 'EGR Sensor SIG', 'E-21/2', 'sen'), 33: ('0.5 V', 'EDU', 'E-34/25', 'edu'),
    34: ('0.5 BR', 'EDU', 'E-34/22', 'edu'), 37: ('0.5 B', 'ชีลด์สาย Cam Sensor', 'ปลอกสาย', 'gn'),
    38: ('0.5 B', 'กราวด์ ECM', 'E-10', 'gn'), 41: ('0.5 W/G', 'Fuel Temp SIG', 'E-27/2', 'sen'),
    42: ('0.5 W', 'Coolant Temp SIG', 'E-41/2', 'sen'), 45: ('0.5 R', 'กราวด์เซ็นเซอร์ THW THF', 'E-41/1, E-27/1', 'sen'),
    49: ('0.5 O/G', 'Pump ROM CLK', 'E-26/4', 'sen'), 50: ('0.5 O/L', 'Pump ROM DATA', 'E-26/1', 'sen'),
    54: ('0.5 B', 'กราวด์ ECM', 'E-10', 'gn'), 55: ('0.5 B', 'กราวด์ ECM', 'E-10', 'gn'),
    58: ('0.5 G', 'Boost SIG', 'E-25/2', 'sen'), 60: ('0.5 G/R', 'IAT SIG', 'E-20/1', 'sen'),
    62: ('0.5 GR', 'Boost GND', 'E-25/1', 'sen'),
}
J2 = {
    1: ('0.5 R/G', '+B หลัง Main Relay', 'H-4/5', 'pw'), 2: ('0.5 R/W', 'BATT จาก EB-2', 'H-4/19', 'pw'),
    3: ('0.5 Y', 'TPS1 5V', 'E-22/2', 'sen'), 7: ('0.5 G/R', 'A/C Relay', 'H-4/11', 'act'),
    11: ('0.5 B/R', 'Tacho Meter', 'H-4/10', 'io'), 14: ('0.5 R/W', 'TCM', 'H-22/3', 'io'),
    15: ('0.5 L/R', 'คุม ECM Main Relay', 'X-13/4', 'act'), 16: ('0.5 B/G', 'คุม Spill Valve Relay', 'X-5/4', 'edu'),
    17: ('0.5 R/G', '+B หลัง Main Relay', 'H-4/5', 'pw'), 19: ('0.5 R/W', 'BATT จาก EB-2', 'H-4/19', 'pw'),
    20: ('0.5 G', 'EGR Sensor 5V', 'E-21/3', 'sen'), 23: ('0.5 W/L', 'VSV Intake', 'C-114/2', 'act'),
    29: ('0.5 R/Y', 'เกียร์ถอยหลัง R', 'E-51/4 (A/T), E-43/1 (M/T)', 'io'), 32: ('0.5 BR/Y', 'Check Engine', 'Meter', 'io'),
    33: ('0.5 R', 'TPS2 GND', 'E-23/2', 'sen'), 35: ('0.5 W', 'TPS2 5V', 'E-23/1', 'sen'),
    36: ('0.5 B', 'TPS2 SIG', 'E-23/3', 'sen'), 37: ('0.5 G', 'TPS1 SIG', 'E-22/1', 'sen'),
    40: ('0.5 B/Y', 'VSS', 'Meter', 'io'), 44: ('0.5 R/G', 'Neutral/Park', 'H-4/30 (A/T), E-12/1 (M/T)', 'io'),
    45: ('0.5 G/B', 'A/C Thermo Relay', 'H-4/8', 'act'), 49: ('0.5 L', 'TPS1 GND', 'E-22/3', 'sen'),
    50: ('0.5 GR', 'EGR Sensor GND และ IAT GND', 'E-21/1, E-20/2', 'sen'), 52: ('0.5 W/G', 'IG', 'H-4/25', 'pw'),
    54: ('0.5 G', 'DLC ขา 7', 'H-4/26', 'io'), 61: ('0.5 B/G', 'DLC ขา 6 TE1', 'H-4/22', 'io'),
}


def connector(title, data, rows):
    cw, ch, x0, y0 = 58, 46, 60, 74
    w = x0 * 2 + cw * 16
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 340" font-family="{FONT}">',
             '<rect width="100%" height="100%" fill="#fff"/>',
             f'<text x="{x0}" y="34" font-size="23" font-weight="bold" fill="#000">{title}</text>',
             f'<rect x="{x0-16}" y="{y0-14}" width="{cw*16+32}" height="{ch*4+28}" rx="10" fill="#f2f2f2" stroke="#333" stroke-width="2.5"/>']
    for r, row in enumerate(rows):
        for c, pin in enumerate(row):
            x, y = x0 + c * cw, y0 + r * ch
            d = data.get(pin)
            fill = COL[d[3]] if d else '#ffffff'
            txt = '#fff' if d else '#aaaaaa'
            parts.append(f'<rect x="{x+2}" y="{y+2}" width="{cw-4}" height="{ch-4}" rx="3" fill="{fill}" stroke="#888"/>')
            parts.append(f'<text x="{x+cw/2}" y="{y+ch/2+7}" font-size="19" text-anchor="middle" fill="{txt}" font-weight="{"bold" if d else "normal"}">{pin}</text>')
    lx = x0
    for k in ['pw', 'gn', 'edu', 'act', 'sen', 'io']:
        parts.append(f'<rect x="{lx}" y="298" width="22" height="22" fill="{COL[k]}"/>')
        parts.append(f'<text x="{lx+30}" y="316" font-size="18" fill="#222">{NAME[k]}</text>')
        lx += 62 + len(NAME[k]) * 9.5
    parts.append('</svg>')
    return '\n'.join(parts)


def table(data, keys):
    head = '<table><tr><th style="width:9%">ขา</th><th style="width:15%">สาย</th><th>หน้าที่</th><th style="width:22%">ปลายทาง</th></tr>'
    rows = ''.join(f'<tr><td><b>{k}</b></td><td>{data[k][0]}</td><td>{data[k][1]}</td><td>{data[k][2]}</td></tr>' for k in keys)
    return head + rows + '</table>'


def block():
    w, h = 1090, 640
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="{FONT}">',
         '<defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>',
         f'<rect width="{w}" height="{h}" fill="#fff"/>',
         '<rect x="395" y="50" width="300" height="540" rx="10" fill="#111820"/>',
         '<text x="545" y="300" font-size="40" font-weight="bold" fill="#fff" text-anchor="middle">ECM</text>',
         '<text x="545" y="338" font-size="20" fill="#ddd" text-anchor="middle">J1 = E-32  J2 = E-33</text>',
         '<text x="545" y="366" font-size="20" fill="#ddd" text-anchor="middle">ขั้วละ 64 ขา</text>']
    left = [('sen', 'TPS1 TPS2', 'J2-37, J2-36'), ('sen', 'Cam Speed Sensor', 'J1-1, J1-17'), ('sen', 'TDC Sensor', 'J1-23'),
            ('sen', 'Boost, IAT', 'J1-58, J1-60'), ('sen', 'Coolant, Fuel Temp', 'J1-42, J1-41'), ('sen', 'EGR Sensor', 'J1-28'),
            ('sen', 'Pump ROM', 'J1-50, J1-49'), ('pw', 'IG', 'J2-52'), ('pw', 'BATT', 'J2-2, J2-19'), ('pw', '+B Main Relay', 'J2-1, J2-17')]
    right = [('act', 'ECM Main Relay', 'J2-15'), ('edu', 'Spill Valve Relay', 'J2-16'), ('edu', 'EDU', 'J1-34, J1-33'),
             ('edu', 'TCV', 'J1-25'), ('act', 'EVRV', 'J1-26'), ('act', 'VSV EGR1, EGR2', 'J1-9, J1-10'),
             ('act', 'VSV Intake', 'J2-23'), ('act', 'A/C Relay', 'J2-7'), ('io', 'Meter, TCM, DLC', 'J2-32, J2-14, J2-54')]
    for i, (k, a, b) in enumerate(left):
        y = 72 + i * 51
        p += [f'<rect x="20" y="{y-24}" width="260" height="46" rx="5" fill="#fff" stroke="{COL[k]}" stroke-width="2.5"/>',
              f'<text x="32" y="{y-5}" font-size="17" font-weight="bold" fill="{COL[k]}">{a}</text>',
              f'<text x="32" y="{y+15}" font-size="15.5" fill="#333">{b}</text>',
              f'<line x1="280" y1="{y}" x2="391" y2="{y}" stroke="#333" stroke-width="2" marker-end="url(#a)"/>']
    for i, (k, a, b) in enumerate(right):
        y = 84 + i * 56
        p += [f'<rect x="810" y="{y-24}" width="262" height="46" rx="5" fill="#fff" stroke="{COL[k]}" stroke-width="2.5"/>',
              f'<text x="822" y="{y-5}" font-size="17" font-weight="bold" fill="{COL[k]}">{a}</text>',
              f'<text x="822" y="{y+15}" font-size="15.5" fill="#333">{b}</text>',
              f'<line x1="695" y1="{y}" x2="806" y2="{y}" stroke="#333" stroke-width="2" marker-end="url(#a)"/>']
    p += ['<text x="150" y="622" font-size="18" text-anchor="middle" fill="#333">ขาเข้า</text>',
          '<text x="941" y="622" font-size="18" text-anchor="middle" fill="#333">ขาออกและการสื่อสาร</text>',
          '<text x="545" y="622" font-size="16" text-anchor="middle" fill="#555">กราวด์ J1-38, 54, 55</text>', '</svg>']
    return '\n'.join(p)


def main():
    OUT.mkdir(exist_ok=True)
    rows1 = [list(range(64, 48, -1)), list(range(48, 32, -1)), list(range(32, 16, -1)), list(range(16, 0, -1))]
    rows2 = [list(range(1, 17)), list(range(17, 33)), list(range(33, 49)), list(range(49, 65))]
    (OUT / 'ecm-j1.svg').write_text(connector('ECM J1 (E-32)', J1, rows1), encoding='utf-8')
    (OUT / 'ecm-j2.svg').write_text(connector('ECM J2 (E-33)', J2, rows2), encoding='utf-8')
    (OUT / 'ecm-block.svg').write_text(block(), encoding='utf-8')
    k1, k2 = sorted(J1), sorted(J2)
    (ROOT / 'pages' / '041-ecm-j1.html').write_text(f'''<h1>ขั้วต่อ ECM J1 (E-32)</h1>
<figure><img src="circuits/ecm-j1.svg" style="height:58mm;margin-bottom:1mm"></figure>
<p><span class="tag w">ผังรถ</span> ขาสีคือขาที่มีสายในผัง 4JH1-TC ขาว่างคือไม่มีสายในผังนี้ เรียงเลขตามผังขั้วต่อ ให้ยืนยันด้านมองกับปลั๊กจริงก่อนจิ้ม</p>
<div class="two"><div>{table(J1, k1[:12])}</div><div>{table(J1, k1[12:])}</div></div>
<div class="note">ขา J1-33 และ J1-34 คือสองเส้นที่คุยกับ EDU ส่วน J1-25 คุม TCV หลังไฟเลี้ยงและ J2-16 ผ่านแล้ว ค่อยดูสามขานี้</div>
''', encoding='utf-8')
    (ROOT / 'pages' / '042-ecm-j2.html').write_text(f'''<h1>ขั้วต่อ ECM J2 (E-33)</h1>
<figure><img src="circuits/ecm-j2.svg" style="height:58mm;margin-bottom:1mm"></figure>
<p><span class="tag w">ผังรถ</span> J2 คือฝั่งไฟเลี้ยงกับรีเลย์ทั้งสอง สองขาที่สำคัญต่อ EDU คือ J2-15 คุม Main Relay และ J2-16 คุม Spill Valve Relay ให้ยืนยันด้านมองกับปลั๊กจริงก่อนจิ้ม</p>
<div class="two"><div>{table(J2, k2[:13])}</div><div>{table(J2, k2[13:])}</div></div>
<div class="warn">ห้ามต่อ +12 V เข้าขา J2-15, J2-16 และห้ามจั๊มกราวด์ขณะเสียบปลั๊ก ECM ถ้าทดสอบรีเลย์หลังถอดปลั๊ก ให้จั๊มผ่านฟิวส์ฝั่งสายไฟ และระวังว่า EDU กับ TCV จะมีไฟทันทีเมื่อ X-5 ดูด</div>
''', encoding='utf-8')


if __name__ == '__main__':
    main()

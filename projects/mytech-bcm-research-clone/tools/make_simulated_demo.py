"""Generate SIMULATED files to demonstrate tools/compare_data.py.

ข้อมูลจำลองเพื่ออธิบายการเปรียบเทียบ — the bytes are pseudo-random, not from any vehicle or module.
Size 8192 bytes only mirrors the 64 Kbit M95640 example used in the book; content has no meaning.
The .bin files are git-ignored; the job file and reports are committed.

    python tools/make_simulated_demo.py
"""
from pathlib import Path
import json, random, subprocess, sys

ROOT = Path(__file__).absolute().parents[1]
OUT = ROOT / 'comparisons' / 'simulated'
DATA = OUT / 'data'
SIZE = 8192


def blob(seed):
    return bytearray(random.Random(seed).getrandbits(8) for _ in range(SIZE))


def alter(data, start, length, seed):
    r = random.Random(seed)
    for i in range(start, start + length):
        data[i] = (data[i] + 1 + r.randrange(255)) % 256  # always different from the original byte
    return data


def main():
    DATA.mkdir(parents=True, exist_ok=True)
    read1 = blob(1)
    files = {
        'read1.bin': read1,
        'read2_unstable.bin': alter(bytearray(read1), 0x400, 16, 11),   # simulated poor clip contact
        'read3_after_reseat.bin': bytearray(read1),                      # simulated re-seat, same data
        'intended_write.bin': bytearray(read1),
        'readback.bin': bytearray(read1),
        'after_repair.bin': alter(alter(bytearray(read1), 0x120, 16, 21), 0x1F00, 64, 22),
    }
    for name, data in files.items():
        (DATA / name).write_bytes(bytes(data))
    job = {
        'title': 'ตัวอย่างผลเปรียบเทียบ (ข้อมูลจำลอง)',
        'simulated': True,
        'pairs': [
            {'id': 'read_repeat_fail', 'kind': 'read_repeat', 'label': 'อ่านรอบ 1 กับรอบ 2 (จำลองหนีบไม่แน่น)',
             'before': 'data/read1.bin', 'after': 'data/read2_unstable.bin'},
            {'id': 'read_repeat_pass', 'kind': 'read_repeat', 'label': 'อ่านรอบ 1 กับรอบ 3 หลังแก้การหนีบ',
             'before': 'data/read1.bin', 'after': 'data/read3_after_reseat.bin'},
            {'id': 'intended_vs_readback', 'kind': 'intended_vs_readback', 'label': 'ไฟล์ที่ตั้งใจเขียนกับไฟล์อ่านกลับ',
             'before': 'data/intended_write.bin', 'after': 'data/readback.bin'},
            {'id': 'before_after', 'kind': 'before_after', 'label': 'ก่อนกับหลังซ่อม/กู้ข้อมูล',
             'before': 'data/read1.bin', 'after': 'data/after_repair.bin'},
        ],
        'regions': [
            {'name': 'พื้นที่ A (จำลอง)', 'start': '0x0000', 'end': '0x0FFF', 'source': 'แผนที่จำลอง ไม่ได้มาจากเอกสารรถหรือชิป'},
            {'name': 'พื้นที่ B (จำลอง)', 'start': '0x1000', 'end': '0x1FFF', 'source': 'แผนที่จำลอง ไม่ได้มาจากเอกสารรถหรือชิป'},
        ],
    }
    (OUT / 'job.json').write_text(json.dumps(job, ensure_ascii=False, indent=2), encoding='utf-8')
    subprocess.run([sys.executable, str(ROOT / 'tools' / 'compare_data.py'), '--job', str(OUT / 'job.json'),
                    '--output', str(OUT / 'SIMULATED_RESULT.json'), '--markdown', str(OUT / 'SIMULATED_RESULT.md')],
                   check=True)


if __name__ == '__main__':
    main()

"""Read-only binary comparison for BCM backup / write / transfer work.

Reports sizes, SHA-256, number of differing byte positions and offset ranges.
It NEVER prints or stores byte values, and never modifies the input files.

Single pair (unchanged from the original tool):
    python tools/compare_data.py --before incoming/original.bin --after incoming/readback.bin \
        --output comparisons/compare-result.json

Job with several pairs (read1 vs read2, intended vs read-back, before vs after):
    python tools/compare_data.py --job comparisons/job.json --output comparisons/result.json \
        --markdown comparisons/result.md

Job file format (paths are relative to the job file):
{
  "title": "...", "simulated": false,
  "pairs": [{"id": "read_repeat", "kind": "read_repeat", "label": "...", "before": "a.bin", "after": "b.bin"}],
  "regions": [{"name": "...", "start": "0x0", "end": "0x7ff", "source": "where this map comes from"}]
}
kind is one of: read_repeat, intended_vs_readback, before_after.
Regions are declared by the operator from documentation. The tool does not infer what data means.
"""
from pathlib import Path
import argparse, hashlib, json

KINDS = {
    'read_repeat': 'อ่านรอบ 1 กับรอบ 2',
    'intended_vs_readback': 'ไฟล์ที่ตั้งใจเขียนกับไฟล์อ่านกลับ',
    'before_after': 'ก่อนกับหลังซ่อม/ย้าย',
}
LIMIT = ('ผลนี้เป็นการเทียบระดับไบต์เท่านั้น ไม่ยืนยันว่าเลือกพื้นที่หน่วยความจำถูก กล่องเข้ากันได้ '
         'หรือรถทำงานครบ ช่วง offset ที่ต่างไม่ได้บอกว่าเป็น VIN, key, checksum หรือ coding')


def diff_ranges(a: bytes, b: bytes):
    ranges, start, count = [], None, 0
    n = max(len(a), len(b))
    for i in range(n):
        different = i >= len(a) or i >= len(b) or a[i] != b[i]
        if different:
            count += 1
            if start is None:
                start = i
        elif start is not None:
            ranges.append((start, i - 1)); start = None
    if start is not None:
        ranges.append((start, n - 1))
    return ranges, count


def parse_int(v):
    return v if isinstance(v, int) else int(str(v), 0)


def region_tally(ranges, regions):
    out = []
    for r in regions or []:
        s, e = parse_int(r['start']), parse_int(r['end'])
        hits = sum(max(0, min(e, re_) - max(s, rs) + 1) for rs, re_ in ranges)
        out.append({'name': r['name'], 'start_hex': hex(s), 'end_hex': hex(e),
                    'different_bytes': hits, 'source': r.get('source', 'ไม่ระบุแหล่ง')})
    return out


def verdict(kind, identical, size_equal):
    if not size_equal:
        return 'ขนาดไฟล์ไม่เท่ากัน: ตรวจว่าเลือกชิป/พื้นที่/ขนาดเดียวกันก่อนตีความผลต่าง'
    if kind == 'read_repeat':
        return ('อ่านสองรอบตรงกัน: การอ่านสม่ำเสมอ (ยังไม่ยืนยันว่าเลือกพื้นที่ถูก)' if identical else
                'อ่านสองรอบไม่ตรงกัน: หยุดงาน ตรวจการสัมผัส แหล่งจ่าย และสภาวะวงจรก่อนทำคำสั่งอื่น')
    if kind == 'intended_vs_readback':
        return ('อ่านกลับตรงไฟล์ที่ตั้งใจเขียน: ผ่านเฉพาะการเขียนชิป ยังต้องตั้งค่าและทดสอบบนรถ' if identical else
                'อ่านกลับไม่ตรงไฟล์ที่ตั้งใจเขียน: ห้ามติดตั้งใช้งาน ตรวจพื้นที่ที่เขียน การต่อ และ verify ของเครื่อง')
    if kind == 'before_after':
        return ('ไม่มีผลต่างระหว่างก่อนและหลัง: ข้อมูลในพื้นที่นี้ไม่ได้ถูกเปลี่ยน' if identical else
                'มีผลต่างตามช่วงที่แสดง: ต้องมีเอกสารยืนยันว่าเป็นการเปลี่ยนที่ตั้งใจ ก่อนสรุปว่างานถูกต้อง')
    return 'ไม่ระบุชนิดคู่เปรียบเทียบ'


def compare(a: bytes, b: bytes, kind=None, regions=None):
    ranges, count = diff_ranges(a, b)
    identical = a == b
    result = {
        'before_size': len(a), 'after_size': len(b),
        'before_sha256': hashlib.sha256(a).hexdigest(), 'after_sha256': hashlib.sha256(b).hexdigest(),
        'identical': identical, 'different_byte_positions': count,
        'different_ranges_inclusive': [{'start_hex': hex(s), 'end_hex': hex(e), 'length': e - s + 1} for s, e in ranges],
        'interpretation': 'Binary equality only; does not prove correct memory region, module compatibility '
                          'or vehicle operation. Missing bytes count as different positions.',
    }
    if regions:
        result['declared_regions'] = region_tally(ranges, regions)
    if kind:
        result['kind'] = kind
        result['verdict_th'] = verdict(kind, identical, len(a) == len(b))
    return result


def to_markdown(job, results, max_ranges=20):
    simulated = job.get('simulated', False)
    lines = ['# ' + job.get('title', 'ผลเปรียบเทียบข้อมูล'), '']
    if simulated:
        lines += ['> **ข้อมูลจำลองเพื่ออธิบายการเปรียบเทียบ** ไม่ใช่ข้อมูลจากกล่องหรือรถจริง ห้ามนำไปรายงานเป็นผลโคลนจริง', '']
    lines += ['## สรุปทุกคู่', '',
              '| คู่เปรียบเทียบ | ขนาด (ไบต์) | SHA-256 (12 ตัวแรก) | ไบต์ต่าง | ช่วงต่าง | ข้อสรุปที่หลักฐานรองรับ |',
              '|---|---|---|---|---|---|']
    for p, r in results:
        size = f"{r['before_size']} / {r['after_size']}"
        sha = f"{r['before_sha256'][:12]} / {r['after_sha256'][:12]}"
        lines.append(f"| {p.get('label') or KINDS.get(p.get('kind'), p['id'])} | {size} | {sha} | "
                     f"{r['different_byte_positions']} | {len(r['different_ranges_inclusive'])} | {r.get('verdict_th', '')} |")
    for p, r in results:
        lines += ['', f"## {p.get('label') or p['id']}", '',
                  f"- ไฟล์ก่อน: `{p['before']}` SHA-256 `{r['before_sha256']}`",
                  f"- ไฟล์หลัง: `{p['after']}` SHA-256 `{r['after_sha256']}`"]
        rngs = r['different_ranges_inclusive']
        if rngs:
            lines += ['', '| ลำดับ | offset เริ่ม | offset จบ | จำนวนไบต์ |', '|---|---|---|---|']
            for i, x in enumerate(rngs[:max_ranges], 1):
                lines.append(f"| {i} | {x['start_hex']} | {x['end_hex']} | {x['length']} |")
            if len(rngs) > max_ranges:
                lines.append(f'| … | อีก {len(rngs) - max_ranges} ช่วง ดูไฟล์ JSON | | |')
        if r.get('declared_regions'):
            lines += ['', 'พื้นที่ที่ผู้ปฏิบัติงานประกาศจากเอกสาร (เครื่องมือไม่ได้ตีความเอง):', '',
                      '| พื้นที่ | ช่วง | ไบต์ต่างในพื้นที่ | แหล่งที่มาของแผนที่ |', '|---|---|---|---|']
            for g in r['declared_regions']:
                lines.append(f"| {g['name']} | {g['start_hex']}–{g['end_hex']} | {g['different_bytes']} | {g['source']} |")
    lines += ['', '## ข้อจำกัด', '', LIMIT, '',
              'รายงานนี้ไม่แสดงค่าไบต์ ไม่เก็บ dump และไม่แก้ไฟล์ต้นฉบับ']
    return '\n'.join(lines) + '\n'


def run_job(job_path: Path, regions_override=None):
    job = json.loads(job_path.read_text(encoding='utf-8'))
    base = job_path.parent
    regions = regions_override or job.get('regions')
    results = []
    for p in job['pairs']:
        if p.get('kind') and p['kind'] not in KINDS:
            raise SystemExit(f"unknown kind {p['kind']!r}; use one of {', '.join(KINDS)}")
        a, b = (base / p['before']).read_bytes(), (base / p['after']).read_bytes()
        results.append((p, compare(a, b, p.get('kind'), regions)))
    return job, results


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--before', type=Path); ap.add_argument('--after', type=Path)
    ap.add_argument('--kind', choices=list(KINDS))
    ap.add_argument('--job', type=Path, help='JSON job with several pairs')
    ap.add_argument('--regions', type=Path, help='JSON list of operator-declared regions')
    ap.add_argument('--output', type=Path, required=True, help='JSON result')
    ap.add_argument('--markdown', type=Path, help='also write a Thai Markdown report')
    args = ap.parse_args()
    if not args.job and not (args.before and args.after):
        ap.error('give --before and --after, or --job')
    regions = json.loads(args.regions.read_text(encoding='utf-8')) if args.regions else None
    if args.job:
        job, results = run_job(args.job, regions)
        inputs = [args.job] + [args.job.parent / p[k] for p, _ in results for k in ('before', 'after')]
    else:
        job = {'title': 'ผลเปรียบเทียบข้อมูล', 'simulated': False}
        pair = {'id': 'pair', 'kind': args.kind, 'before': str(args.before), 'after': str(args.after)}
        results = [(pair, compare(args.before.read_bytes(), args.after.read_bytes(), args.kind, regions))]
        inputs = [args.before, args.after]
    for out in [args.output, args.markdown]:
        if out and out.resolve() in [i.resolve() for i in inputs]:
            ap.error('Output must not overwrite an input')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    payload = results[0][1] if not args.job else {
        'title': job.get('title'), 'simulated': job.get('simulated', False),
        'pairs': [{'id': p['id'], 'label': p.get('label'), 'before': p['before'], 'after': p['after'], **r} for p, r in results]}
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text(to_markdown(job, results), encoding='utf-8')
    for p, r in results:
        print(f"{p['id']}: identical={r['identical']} different_byte_positions={r['different_byte_positions']} "
              f"ranges={len(r['different_ranges_inclusive'])}")


if __name__ == '__main__':
    main()

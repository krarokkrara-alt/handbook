"""Compare two binary reads without modifying either input.

This is a file integrity helper, not an ABS compatibility or checksum tool.
"""
import argparse
import hashlib
import json
from pathlib import Path


def compare(left, right, expected_size=None):
    a, b = Path(left).read_bytes(), Path(right).read_bytes()
    sample = []
    differing = 0
    for offset, (x, y) in enumerate(zip(a, b)):
        if x != y:
            differing += 1
            if len(sample) < 32:
                sample.append(f'0x{offset:08X}')
    size_ok = len(a) == len(b) and (expected_size is None or len(a) == expected_size)
    identical = a == b
    empty = not a or not b
    return {
        'status': 'EMPTY_INPUT' if empty else ('SIZE_MISMATCH' if not size_ok else ('IDENTICAL' if identical else 'DIFFERENT')),
        'identical': identical,
        'size_left': len(a),
        'size_right': len(b),
        'expected_size': expected_size,
        'sha256_left': hashlib.sha256(a).hexdigest(),
        'sha256_right': hashlib.sha256(b).hexdigest(),
        'different_bytes_in_shared_range': differing,
        'extra_bytes': abs(len(a) - len(b)),
        'sample_different_offsets': sample,
        'scope': 'Raw file equality only; no vehicle compatibility or ECU validation.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('left')
    parser.add_argument('right')
    parser.add_argument('--expected-size', type=int)
    args = parser.parse_args()
    if args.expected_size is not None and args.expected_size <= 0:
        parser.error('--expected-size must be positive')
    try:
        result = compare(args.left, args.right, args.expected_size)
    except OSError as exc:
        parser.exit(2, f'Cannot read input: {exc}\n')
    print(json.dumps(result, indent=2))
    return 0 if result['status'] == 'IDENTICAL' else 1


if __name__ == '__main__':
    raise SystemExit(main())

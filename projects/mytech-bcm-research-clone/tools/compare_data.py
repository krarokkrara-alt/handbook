"""Read-only binary comparison. Reports offsets and hashes, never byte values."""
from pathlib import Path
import argparse,hashlib,json

def compare(a,b):
    ranges=[];start=None;count=0
    for i in range(max(len(a),len(b))):
        different=i>=len(a) or i>=len(b) or a[i]!=b[i]
        if different:
            count+=1
            if start is None:start=i
        elif start is not None:ranges.append([start,i-1]);start=None
    if start is not None:ranges.append([start,max(len(a),len(b))-1])
    return {'before_size':len(a),'after_size':len(b),'before_sha256':hashlib.sha256(a).hexdigest(),'after_sha256':hashlib.sha256(b).hexdigest(),'identical':a==b,'different_byte_positions':count,'different_ranges_inclusive':[{'start_hex':hex(s),'end_hex':hex(e),'length':e-s+1} for s,e in ranges],'interpretation':'Binary equality only; does not prove correct memory region, module compatibility or vehicle operation. Missing bytes count as different positions.'}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--before',type=Path,required=True);ap.add_argument('--after',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    if args.output.resolve() in [args.before.resolve(),args.after.resolve()]:ap.error('Output must not overwrite either input')
    result=compare(args.before.read_bytes(),args.after.read_bytes());args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2),encoding='utf-8');print('Identical:',result['identical'],'Different byte positions:',result['different_byte_positions'])

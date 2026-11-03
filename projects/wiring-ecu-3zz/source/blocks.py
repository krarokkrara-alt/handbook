import sys,json
sys.path.insert(0, sys.argv[1])
import pymupdf
d=pymupdf.open(sys.argv[2]); out={}
for i,p in enumerate(d):
    if i==0: continue
    b=[]
    for x in p.get_image_info(): b.append(['I',[round(v) for v in x['bbox']]])
    for x in p.get_text('dict')['blocks']:
        if x['type']==0: b.append(['T',[round(v) for v in x['bbox']]])
    for dr in p.get_drawings():
        r=dr['rect']; 
        if r.width>3 and r.height>3: b.append(['D',[round(r.x0),round(r.y0),round(r.x1),round(r.y1)]])
    b.sort(key=lambda z:(z[1][1],z[1][0]))
    out[i+1]=b
print('size',d[1].rect)
json.dump(out,open(sys.argv[3],'w'))
for k,v in out.items():
    print(k,' '.join(f"{t}{r}" for t,r in v if t!='D'), 'D%d'%sum(1 for t,_ in v if t=='D'))

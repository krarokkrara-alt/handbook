# สร้าง relayout.json: ย้ายภาพและคำบรรยายของหน้าเดิมให้อยู่กลาง และขยายภาพเดี่ยวเมื่อหน้ามีที่ว่าง
import json,sys
B=json.load(open(sys.argv[1])); W=595.32; CX=W/2; LIMIT=772; MAXW=490
ROT={'35','36','37','38','39','40'}  # ผังแนวนอน REF10-REF15 หมุน 90 องศาให้เต็มหน้า
GAP=8  # ระยะเพิ่มระหว่างภาพที่วางซ้อนกัน
out={}
def mv(clip,to,s=1,src=None,cover=True,rot=0):
    m={'clip':clip,'to':[round(to[0],1),round(to[1],1)],'scale':round(s,3)}
    if rot: m['rotate']=rot
    if src: m['src']=src
    if not cover: m['cover']=False
    return m
def ctr(r,s=1): return CX-(r[2]-r[0])*s/2
s_af=None
for k in map(str,range(3,41)):
    b=B[k]; imgs=[r for t,r in b if t=='I']; texts=[r for t,r in b if t=='T']
    if k=='7': imgs=imgs[:1]
    if not imgs: continue
    moves=[]
    def caption(img):
        c=[t for t in texts if t[2]-t[0]>10 and img[3]-2<t[1]<img[3]+22]
        return c[0] if c else None
    def marker(img): return [t for t in texts if t[2]-t[0]<=10 and abs(t[3]-img[3])<8]
    if len(imgs)==1:
        img=imgs[0]; cap=caption(img)
        rest=[r for t,r in b if r[1]>=img[3]-2 and r is not cap and not (t=='T' and r[2]-r[0]<=10)]
        last=max([r[3] for t,r in b if not (k=='7' and r[1]>=639)])
        iw,ih=img[2]-img[0],img[3]-img[1]
        s=min(1.3,1+(LIMIT-last)/ih,MAXW/iw)
        if k=='7' and s_af: s=min(s,s_af[0]/iw)
        if s<1.04: s=1
        d=ih*(s-1)
        if k in ROT:
            s=min(610/iw,MAXW/ih); d=iw*s-ih
            moves.append(mv(img,(CX-ih*s/2,img[1]),s,rot=90))
        else:
            moves.append(mv(img,(ctr(img,s),img[1]),s))
        for m in marker(img): moves.append(mv(m,(m[0],m[1]),cover=True)|{'drop':True})
        if cap: moves.append(mv(cap,(ctr(cap),cap[1]+d)))
        rest=[r for r in rest if (cap is None or r[1]>cap[3]-2) and not (k=='7' and r[1]>=639)]
        if rest:
            band=[0,min(r[1] for r in rest)-2,W,max(r[3] for r in rest)+2]
            if d: moves.append(mv(band,(0,band[1]+d)))
        if k=='5': s_af=(iw*s, img[1], ih*s)
    else:
        for i,img in enumerate(imgs):
            moves.append(mv(img,(ctr(img),img[1]+i*GAP)))
            for m in marker(img): moves.append(mv(m,(m[0],m[1]))|{'drop':True})
            cap=caption(img)
            if cap: moves.append(mv(cap,(ctr(cap),cap[1]+i*GAP)))
    if k=='7':
        moves.append(mv([51,639,134,783],(0,0))|{'drop':True})
    out[k]=moves
# หน้า 8: ภาพ AF05 อยู่ท้ายหน้า 7 แต่คำบรรยายอยู่หน้า 8 ย้ายภาพมาไว้กับคำบรรยาย
af=[51,639,131,781]; s=450/(af[3]-af[1]); w=(af[2]-af[0])*s; h=450  # ภาพต้นฉบับ 221x393 px ขยายเกินนี้จะแตก
cap=[51,45,389,59]; rec=[51,66,199,79]
out['8']=[mv(af,(CX-w/2,45),s,src=7,cover=False), mv(cap,(ctr(cap),45+h+9)), mv(rec,(51,45+h+30))]
# ปก: ภาพชิดซ้าย ย้ายให้อยู่กลาง
cov=[51,128,476,728]; out['1']=[mv(cov,(ctr(cov),cov[1]))]
json.dump(out,open(sys.argv[2],'w',encoding='utf8'),indent=1)
for k,v in out.items(): print(k,[ (m['to'],m['scale']) for m in v if not m.get('drop')][:3])

import json,math,collections
exec(open("geo.py").read().split("# ---------- topojson")[0])  # reutiliza proyección

# --- Natural Earth ---
ne=json.load(open("rivers.json"))
NE={"Duero":["Duero"],"Ebro":["Ebro"],"Tajo":["Tajo","Tejo"],"Guadiana":["Guadiana"],
    "Guadalquivir":["Guadalquivir"],"Miño":["Minho","Mio"],"Segre":["Segre"]}
def inib(pts): return any(-10<p[0]<4.5 and 35<p[1]<44.5 for p in pts)
raw=collections.defaultdict(list)
for f in ne["features"]:
    nm=f["properties"].get("name")
    if not nm: continue
    g=f["geometry"]; cs=g["coordinates"]
    segs=[cs] if g["type"]=="LineString" else cs
    for key,alias in NE.items():
        if nm in alias:
            for s in segs:
                if inib(s): raw[key].append([[c[0],c[1]] for c in s])

osm=json.load(open("osm_rios.json"))
for k,v in {"Júcar":"Jucar","Segura":"Segura","Turia":"Turia","Nalón":"Nalon","Genil":"Genil"}.items():
    raw[k]=osm[v]

# --- encadenar tramos en polilíneas continuas ---
def chain(segs,snap=0.02):
    segs=[s for s in segs if len(s)>1]
    key=lambda p:(round(p[0]/snap),round(p[1]/snap))
    used=[False]*len(segs); out=[]
    ends=collections.defaultdict(list)
    for i,s in enumerate(segs):
        ends[key(s[0])].append((i,0)); ends[key(s[-1])].append((i,1))
    for i in range(len(segs)):
        if used[i]: continue
        used[i]=True; line=list(segs[i])
        for _ in range(2):
            while True:
                k=key(line[-1]); nxt=None
                for j,end in ends.get(k,[]):
                    if not used[j]: nxt=(j,end); break
                if not nxt: break
                j,end=nxt; used[j]=True
                line.extend((segs[j][::-1] if end==1 else segs[j])[1:])
            line.reverse()
        out.append(line)
    out.sort(key=len,reverse=True)
    return out

def simplify(pts,tol):
    # Douglas-Peucker iterativo
    if len(pts)<3: return pts
    keep=[0,len(pts)-1]; stack=[(0,len(pts)-1)]
    while stack:
        a,b=stack.pop()
        if b-a<2: continue
        ax,ay=pts[a]; bx,by=pts[b]; dx,dy=bx-ax,by-ay
        n=math.hypot(dx,dy) or 1e-9
        best=0; bi=-1
        for i in range(a+1,b):
            px,py=pts[i]
            d=abs(dy*px-dx*py+bx*ay-by*ax)/n
            if d>best: best,bi=d,i
        if best>tol:
            keep.append(bi); stack.append((a,bi)); stack.append((bi,b))
    keep.sort()
    return [pts[i] for i in keep]

rios=[]
ORDEN=["Ebro","Tajo","Duero","Guadiana","Guadalquivir","Miño","Júcar","Segura","Turia","Nalón","Genil","Segre"]
for nm in ORDEN:
    ch=chain(raw[nm])
    # nos quedamos con los cauces largos (descarta afluentes sueltos mal etiquetados)
    ch=[c for c in ch if len(c)>=8][:6]
    d=[]; total=0
    for c in ch:
        pts=[proj(lo,la) for lo,la in c]
        pts=simplify(pts,0.8)
        if len(pts)<4: continue
        total+=len(pts)
        d.append("M"+" ".join(f"{x},{y}" for x,y in pts))
    rios.append({"id":nm.lower().replace("ñ","n").replace("ú","u").replace("ó","o"),"n":nm,"d":"".join(d)})
    print(f"{nm:14s} {len(ch):2d} cauces -> {total:4d} pts, {len(''.join(d)):5d} chars")
json.dump(rios,open("out_rios.json","w"),ensure_ascii=False)
print("TOTAL rios:",len(rios),"|",sum(len(r['d']) for r in rios)//1024,"KB")

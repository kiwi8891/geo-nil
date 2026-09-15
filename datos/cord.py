import json,math
exec(open("geo.py").read().split("# ---------- topojson")[0])

reg=json.load(open("regions.json"))
def pts_of(c):
    if isinstance(c[0],(int,float)): yield c
    else:
        for x in c: yield from pts_of(x)
NE={"PYRENEES":"Pirineos","Cord. Cantábrica":"Cordillera Cantábrica",
    "Sierra Morena":"Sierra Morena","S. Nevada":"Sierra Nevada"}
def rings_of(f):
    g=f["geometry"]
    return g["coordinates"] if g["type"]=="Polygon" else [r for p in g["coordinates"] for r in p]

def poly_path(rings,tol=1.2):
    d=[]
    for r in rings:
        pts=[proj(lo,la) for lo,la in r]
        s=[pts[0]]
        for p in pts[1:]:
            if abs(p[0]-s[-1][0])+abs(p[1]-s[-1][1])>tol: s.append(p)
        if len(s)<4: continue
        d.append("M"+" ".join(f"{x},{y}" for x,y in s)+"Z")
    return "".join(d)

cord=[]
for f in reg["features"]:
    nm=f["properties"].get("NAME")
    if nm in NE and any(-10<p[0]<5 and 35<p[1]<44.5 for p in pts_of(f["geometry"]["coordinates"])):
        cord.append({"n":NE[nm],"d":poly_path(rings_of(f))})
        print(f"NE  {NE[nm]:24s} {len(cord[-1]['d']):5d} chars")

# --- trazadas a mano: banda alrededor de una línea central ---
def banda(eje,ancho):
    """eje: [(lon,lat)...] ; ancho en grados -> polígono cerrado proyectado"""
    L=[proj(lo,la) for lo,la in eje]
    w=ancho*(H/(MAIN["lat1"]-MAIN["lat0"]))   # grados -> px verticales
    izq,der=[],[]
    for i,(x,y) in enumerate(L):
        a=L[max(i-1,0)]; b=L[min(i+1,len(L)-1)]
        dx,dy=b[0]-a[0],b[1]-a[1]; n=math.hypot(dx,dy) or 1
        nx,ny=-dy/n*w,dx/n*w
        izq.append((round(x+nx,1),round(y+ny,1))); der.append((round(x-nx,1),round(y-ny,1)))
    ring=izq+der[::-1]
    return "M"+" ".join(f"{x},{y}" for x,y in ring)+"Z"

MANO={
 "Sistema Central":([(-6.80,40.20),(-6.10,40.30),(-5.40,40.28),(-4.80,40.45),(-4.20,40.65),
                     (-3.85,40.85),(-3.55,41.05),(-3.25,41.25)],0.22),
 "Sistema Ibérico":([(-3.15,42.15),(-2.70,42.00),(-2.20,41.85),(-1.85,41.78),(-1.70,41.35),
                     (-1.75,40.95),(-1.95,40.55),(-1.75,40.20),(-1.20,40.10),(-0.75,39.90)],0.20),
}
for n,(eje,w) in MANO.items():
    cord.append({"n":n,"d":banda(eje,w),"mano":1})
    print(f"MANO {n:23s} {len(cord[-1]['d']):5d} chars")

for c in cord: c["id"]=c["n"].lower().replace(" ","_").replace("í","i").replace("é","e")
cord.sort(key=lambda x:x["n"])
json.dump(cord,open("out_cord.json","w"),ensure_ascii=False)
print("TOTAL cordilleras:",len(cord))

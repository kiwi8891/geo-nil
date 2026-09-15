import json, math

# ---------- proyección ----------
# Península+Baleares en el lienzo principal; Canarias en recuadro aparte.
W,H=1000,700
LAT0=40.0; K=math.cos(math.radians(LAT0))
MAIN=dict(lon0=-9.9,lon1=4.7,lat0=34.9,lat1=44.4)
def mk(box,x0,y0,w,h):
    sx=w/((box["lon1"]-box["lon0"])*K); sy=h/(box["lat1"]-box["lat0"]); s=min(sx,sy)
    ox=x0+(w-(box["lon1"]-box["lon0"])*K*s)/2; oy=y0+(h-(box["lat1"]-box["lat0"])*s)/2
    def f(lon,lat):
        return (round(ox+(lon-box["lon0"])*K*s,1), round(oy+(box["lat1"]-lat)*s,1))
    return f
P_MAIN=mk(MAIN,0,0,W,H)
CAN=dict(lon0=-18.3,lon1=-13.3,lat0=27.5,lat1=29.5)
P_CAN=mk(CAN,18,H-150,300,132)
def inCan(lon,lat): return lon<-12.5 and lat<30.5
def proj(lon,lat): return (P_CAN if inCan(lon,lat) else P_MAIN)(lon,lat)

# ---------- topojson CCAA ----------
tj=json.load(open("atlas_ccaa.json"))
tr=tj["transform"]; SC,TR=tr["scale"],tr["translate"]
def decode(arc):
    x=y=0; out=[]
    for dx,dy in arc:
        x+=dx; y+=dy; out.append((x*SC[0]+TR[0], y*SC[1]+TR[1]))
    return out
ARCS=[decode(a) for a in tj["arcs"]]
def ring(idxs):
    pts=[]
    for i in idxs:
        a=ARCS[~i][::-1] if i<0 else ARCS[i]
        pts.extend(a if not pts else a[1:])
    return pts
def polys(g):
    t=g["type"]; c=g["coordinates"] if t!="Polygon" and t!="MultiPolygon" else None
    if t=="Polygon":   return [g["arcs"]]
    if t=="MultiPolygon": return [p for p in g["arcs"]]
    return []

def path_from_rings(rings, minpts=6, tol=0.6):
    d=[]
    for r in rings:
        pts=[proj(lon,lat) for lon,lat in r]
        # simplificar: quitar puntos casi colineales/cercanos
        s=[pts[0]]
        for p in pts[1:]:
            if abs(p[0]-s[-1][0])+abs(p[1]-s[-1][1])>tol: s.append(p)
        if len(s)<minpts: continue
        d.append("M"+" ".join(f"{x},{y}" for x,y in s)+"Z")
    return "".join(d)

NOMBRES={
 "Andalucía":("Andalucía","Sevilla"),"Aragón":("Aragón","Zaragoza"),
 "Principado de Asturias":("Asturias","Oviedo"),"Illes Balears":("Baleares","Palma"),
 "Cantabria":("Cantabria","Santander"),"Castilla y León":("Castilla y León","Valladolid"),
 "Castilla-La Mancha":("Castilla-La Mancha","Toledo"),"Cataluña/Catalunya":("Cataluña","Barcelona"),
 "Comunitat Valenciana":("Comunidad Valenciana","Valencia"),"Extremadura":("Extremadura","Mérida"),
 "Galicia":("Galicia","Santiago de Compostela"),"Comunidad de Madrid":("Madrid","Madrid"),
 "Región de Murcia":("Murcia","Murcia"),"Comunidad Foral de Navarra":("Navarra","Pamplona"),
 "País Vasco/Euskadi":("País Vasco","Vitoria"),"La Rioja":("La Rioja","Logroño"),
 "Ciudad Autónoma de Ceuta":("Ceuta","Ceuta"),"Ciudad Autónoma de Melilla":("Melilla","Melilla"),
 "Canarias":("Canarias","Las Palmas / Santa Cruz"),
}
ccaa=[]
for g in tj["objects"]["autonomous_regions"]["geometries"]:
    nm=g["properties"].get("name")
    if nm not in NOMBRES: continue     # descarta Gibraltar
    corto,cap=NOMBRES[nm]
    rings=[]
    for poly in polys(g):
        for r in poly: rings.append(ring(r))
    tol = 0.35 if corto in ("Ceuta","Melilla","Canarias","Baleares") else 0.7
    d=path_from_rings(rings,tol=tol)
    ccaa.append({"id":corto.lower().replace(" ","_"),"n":corto,"cap":cap,"d":d})
ccaa.sort(key=lambda x:x["n"])
print("CCAA:",len(ccaa),"| peso path:",sum(len(c["d"]) for c in ccaa)//1024,"KB")
for c in ccaa:
    if not c["d"]: print("  !! sin path:",c["n"])
json.dump(ccaa,open("out_ccaa.json","w"),ensure_ascii=False)

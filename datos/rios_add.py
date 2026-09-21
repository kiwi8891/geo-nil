# -*- coding: utf-8 -*-
"""Añade ríos a out_mapa.json. Idempotente: si el río ya está, lo reemplaza.

Dos fuentes, por este orden:
  1. ne_10m_rivers_europe (Natural Earth, suplemento europeo). Es la buena:
     un fichero, sin rate limit, 33 ríos españoles con nombre. El global
     (ne_10m_rivers_lake_centerlines) que usó rios.py solo traía 8.
  2. osm_rios2.json (Overpass), para lo que Natural Earth no tiene.
     Overpass se satura mucho: overpass.osm.jp además tiene el certificado
     roto (hostname mismatch), así que ese servidor no sirve.

No se puede recorrer el pipeline entero (rios.py + bundle.py): los intermedios
ya no están en disco, solo quedaron out_mapa.json y progress.json.
"""
import json, math, struct, collections, os

exec(open("geo.py").read().split("# ---------- topojson")[0])   # proyección

# ---------- lectura de shapefile (sin pyshp: no está instalado) ----------
def dbf(path):
    f = open(path, "rb"); h = f.read(32)
    n = struct.unpack("<I", h[4:8])[0]
    hlen = struct.unpack("<H", h[8:10])[0]
    rlen = struct.unpack("<H", h[10:12])[0]
    campos = []
    while True:
        d = f.read(32)
        if d[0:1] in (b"\r", b""): break
        campos.append((d[:11].rstrip(b"\0").decode("latin-1"), d[16]))
    f.seek(hlen)
    filas = []
    for _ in range(n):
        r = f.read(rlen)
        if not r or r[0:1] == b"*": continue
        o = 1; fila = {}
        for nom, w in campos:
            fila[nom] = r[o:o+w].decode("utf-8", "replace").strip(); o += w
        filas.append(fila)
    return filas

def shp_polylines(path):
    f = open(path, "rb"); f.seek(100)
    out = []
    while True:
        h = f.read(8)
        if len(h) < 8: break
        _, clen = struct.unpack(">II", h)
        c = f.read(clen*2)
        if struct.unpack("<i", c[:4])[0] != 3: out.append([]); continue
        nparts, npts = struct.unpack("<ii", c[36:44])
        parts = list(struct.unpack("<%di" % nparts, c[44:44+4*nparts])) + [npts]
        off = 44 + 4*nparts
        pts = struct.unpack("<%dd" % (2*npts), c[off:off+16*npts])
        out.append([[[pts[2*k], pts[2*k+1]] for k in range(parts[i], parts[i+1])]
                    for i in range(nparts)])
    return out

# ---------- geometría ----------
def chain(segs, snap=0.02):
    segs = [s for s in segs if len(s) > 1]
    key = lambda p: (round(p[0]/snap), round(p[1]/snap))
    used = [False]*len(segs); out = []
    ends = collections.defaultdict(list)
    for i, s in enumerate(segs):
        ends[key(s[0])].append((i, 0)); ends[key(s[-1])].append((i, 1))
    for i in range(len(segs)):
        if used[i]: continue
        used[i] = True; line = list(segs[i])
        for _ in range(2):
            while True:
                k = key(line[-1]); nxt = None
                for j, end in ends.get(k, []):
                    if not used[j]: nxt = (j, end); break
                if not nxt: break
                j, end = nxt; used[j] = True
                line.extend((segs[j][::-1] if end == 1 else segs[j])[1:])
            line.reverse()
        out.append(line)
    out.sort(key=len, reverse=True)
    return out

def simplify(pts, tol):
    if len(pts) < 3: return pts
    keep = [0, len(pts)-1]; stack = [(0, len(pts)-1)]
    while stack:
        a, b = stack.pop()
        if b - a < 2: continue
        ax, ay = pts[a]; bx, by = pts[b]; dx, dy = bx-ax, by-ay
        n = math.hypot(dx, dy) or 1e-9
        best = 0; bi = -1
        for i in range(a+1, b):
            px, py = pts[i]
            d = abs(dy*px - dx*py + bx*ay - by*ax)/n
            if d > best: best, bi = d, i
        if best > tol:
            keep.append(bi); stack.append((a, bi)); stack.append((bi, b))
    keep.sort()
    return [pts[i] for i in keep]

def trazo(segs):
    """segs en lon/lat -> path SVG proyectado y simplificado.

    Se queda con el cauce más largo y solo con los tramos que caen CERCA de él.
    Sin este filtro el Alagón salía repartido por media España: Natural Earth
    tiene varios ríos con el mismo nombre y el encadenado los pintaba todos.
    """
    chains = [x for x in chain(segs) if len(x) >= 5]
    if not chains: return ""
    def bbox(c):
        xs = [p[0] for p in c]; ys = [p[1] for p in c]
        return min(xs), min(ys), max(xs), max(ys)
    bx0, by0, bx1, by1 = bbox(chains[0])
    CERCA = 1.2                      # grados: un afluente de verdad no se va más lejos
    buenos = []
    for c in chains[:12]:
        x0, y0, x1, y1 = bbox(c)
        if (x0 > bx1 + CERCA or x1 < bx0 - CERCA or
            y0 > by1 + CERCA or y1 < by0 - CERCA): continue
        buenos.append(c)
        bx0, by0 = min(bx0, x0), min(by0, y0)
        bx1, by1 = max(bx1, x1), max(by1, y1)
    d = []
    for c in buenos[:8]:
        pts = simplify([proj(lo, la) for lo, la in c], 0.8)
        if len(pts) < 4: continue
        d.append("M" + " ".join(f"{x},{y}" for x, y in pts))
    return "".join(d)

# ---------- qué ríos queremos ----------
# nombre en la fuente -> (id, nombre que lee Nil)
NE = {"Sil":("sil","Sil"), "Pisuerga":("pisuerga","Pisuerga"),
      "Tormes":("tormes","Tormes"), "Cinca":("cinca","Cinca"), "Jalón":("jalon","Jalón"),
      "Henares":("henares","Henares"), "Alberche":("alberche","Alberche"),
      "Narcea":("narcea","Narcea"), "Mijares":("mijares","Mijares"),
      "Cabriel":("cabriel","Cabriel")}
# fuera a propósito: Alagón (Natural Earth mezcla varios ríos con ese nombre y salía
# repartido por media España), Adaja y Tiétar (demasiado menores: apelotonaban el
# Sistema Central sin que Nil pueda distinguirlos).
QUITAR = ["alagon", "adaja", "tietar"]
OSM = {"Esla":("esla","Esla"),       # OSM lo trae entero; Natural Earth, a trozos
       "Llobregat":("llobregat","Llobregat"), "Ter":("ter","Ter"), "Jarama":("jarama","Jarama"),
       "Gallego":("gallego","Gállego"), "Guadalete":("guadalete","Guadalete"),
       "Bidasoa":("bidasoa","Bidasoa"), "Orbigo":("orbigo","Órbigo")}

def en_esp(segs):
    return any(-10 < x < 4.6 and 35.5 < y < 44.3 for s in segs for x, y in s)

mapa = json.load(open("out_mapa.json"))
antes = len(mapa["rios"])
fuera = [r["n"] for r in mapa["rios"] if r["id"] in QUITAR]
if fuera:
    mapa["rios"] = [r for r in mapa["rios"] if r["id"] not in QUITAR]
    print("retirados:", ", ".join(fuera))
por_id = {r["id"]: i for i, r in enumerate(mapa["rios"])}

def meter(rid, nombre, segs):
    d = trazo(segs)
    if not d:
        print(f"  !! {nombre}: sin trazo utilizable"); return False
    reg = {"id": rid, "n": nombre, "d": d, "art": "el", "lv": 5}
    if rid in por_id: mapa["rios"][por_id[rid]] = reg
    else: por_id[rid] = len(mapa["rios"]); mapa["rios"].append(reg)
    print(f"  {nombre:11s} {len(d):5d} chars")
    return True

base = "ne_10m_rivers_europe"
if os.path.exists(base + ".shp"):
    recs, geos = dbf(base + ".dbf"), shp_polylines(base + ".shp")
    junta = collections.defaultdict(list)
    for r, g in zip(recs, geos):
        nm = (r.get("name") or "").strip()
        if nm in NE and g and en_esp(g): junta[nm].extend(g)
    print("Natural Earth Europa:")
    for nm, segs in junta.items():
        rid, nombre = NE[nm]; meter(rid, nombre, segs)
else:
    print("!! falta ne_10m_rivers_europe.shp")

if os.path.exists("osm_rios2.json"):
    osm = json.load(open("osm_rios2.json"))
    pend = {k: v for k, v in osm.items() if k in OSM}
    if pend:
        print("OpenStreetMap:")
        for k, segs in pend.items():
            rid, nombre = OSM[k]; meter(rid, nombre, segs)

json.dump(mapa, open("out_mapa.json", "w"), ensure_ascii=False, separators=(",", ":"))
print(f"\nríos: {antes} -> {len(mapa['rios'])} | out_mapa.json {os.path.getsize('out_mapa.json')//1024} KB")

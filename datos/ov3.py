"""Ríos nuevos desde OpenStreetMap (Overpass). Reanudable: guarda en osm_rios2.json.

Overpass se satura a ratos: por eso los tres servidores y el fichero de progreso,
igual que en ov2.py. El nombre va anclado (^...$) porque "Ter" o "Sil" sueltos
enganchan cualquier arroyo que los lleve dentro.
"""
import json, urllib.request, urllib.parse, time, os, sys

# nombre -> (regex OSM, bbox south,west,north,east)
Q = {
 "Esla":      (r"^(R[íi]o )?Esla$",        (41.2, -6.3, 43.2, -5.0)),
 "Sil":       (r"^(R[íi]o )?Sil$",         (42.2, -7.9, 43.2, -5.9)),
 "Llobregat": (r"^(El )?Llobregat$",       (41.2,  1.4, 42.4,  2.4)),
 "Ter":       (r"^(El )?Ter$",             (41.8,  1.8, 42.8,  3.3)),
 "Jarama":    (r"^(R[íi]o )?Jarama$",      (39.9, -3.9, 41.2, -3.1)),
 "Pisuerga":  (r"^(R[íi]o )?Pisuerga$",    (41.4, -4.9, 43.1, -3.7)),
 "Tormes":    (r"^(R[íi]o )?Tormes$",      (40.1, -6.7, 40.9, -4.8)),
 "Guadalete": (r"^(R[íi]o )?Guadalete$",   (36.3, -6.4, 37.1, -5.1)),
 "Bidasoa":   (r"^(R[íi]o )?Bidasoa$",     (42.8, -2.0, 43.4, -1.4)),
 "Cinca":     (r"^(R[íi]o )?Cinca$",       (41.3, -0.5, 42.8,  0.6)),
 "Gallego":   (r"^(R[íi]o )?G[áa]llego$",  (41.4, -1.1, 42.9,  0.0)),
 "Orbigo":    (r"^(R[íi]o )?[ÓO]rbigo$",   (41.7, -6.3, 42.9, -5.4)),
}
SRV = ["https://overpass.kumi.systems/api/interpreter",
       "https://overpass-api.de/api/interpreter",
       "https://overpass.osm.jp/api/interpreter"]

F = "osm_rios2.json"
out = json.load(open(F)) if os.path.exists(F) else {}
solo = sys.argv[1:] or list(Q)

for k in solo:
    if out.get(k): print(f"{k:11s} ya estaba ({len(out[k])} tramos)"); continue
    rx, (s, w, n, e) = Q[k]
    body = f'[out:json][timeout:120];(way["waterway"="river"]["name"~"{rx}"]({s},{w},{n},{e}););out geom;'
    for srv in SRV:
        try:
            r = urllib.request.urlopen(urllib.request.Request(srv,
                data=urllib.parse.urlencode({"data": body}).encode(),
                headers={"User-Agent":"geo-nil/1.0"}), timeout=180)
            d = json.loads(r.read())
            segs = [[[round(p["lon"],4), round(p["lat"],4)] for p in x["geometry"]]
                    for x in d.get("elements", []) if x.get("geometry")]
            if segs:
                out[k] = segs
                json.dump(out, open(F,"w"))
                print(f"{k:11s} OK  {len(segs):3d} tramos via {srv.split('/')[2]}")
                break
            print(f"{k:11s} vacío en {srv.split('/')[2]}")
        except Exception as ex:
            print(f"{k:11s} {srv.split('/')[2]:24s} -> {ex}"); time.sleep(4)
    time.sleep(2)
print("\nguardados:", sorted(out))

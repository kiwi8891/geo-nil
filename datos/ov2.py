import json,urllib.request,urllib.parse,time
Q={"Jucar":'way["waterway"="river"]["name"~"Xúquer|Júcar"](38.0,-2.5,40.6,0.5);',
   "Nalon":'way["waterway"="river"]["name"~"Nalón"](42.9,-6.6,43.6,-5.4);'}
SRV=["https://overpass-api.de/api/interpreter",
     "https://overpass.kumi.systems/api/interpreter",
     "https://overpass.osm.jp/api/interpreter"]
out=json.load(open("osm_rios.json"))
for k,q in Q.items():
    if out.get(k): continue
    body="[out:json][timeout:180];("+q+");out geom;"
    for s in SRV:
        try:
            r=urllib.request.urlopen(urllib.request.Request(s,
                data=urllib.parse.urlencode({"data":body}).encode(),
                headers={"User-Agent":"geo-nil/1.0"}),timeout=200)
            d=json.loads(r.read())
            segs=[[[round(p["lon"],4),round(p["lat"],4)] for p in w["geometry"]] for w in d["elements"] if w.get("geometry")]
            if segs:
                out[k]=segs; print(f"{k:7s} OK via {s.split('/')[2]:26s} {len(segs)} tramos"); break
        except Exception as e:
            print(f"{k:7s} {s.split('/')[2]:26s} -> {e}"); time.sleep(5)
json.dump(out,open("osm_rios.json","w"))
print("rios OSM guardados:",list(out.keys()))

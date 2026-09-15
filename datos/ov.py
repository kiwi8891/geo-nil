import json,urllib.request,urllib.parse,time
RIOS={"Jucar":"Xúquer/Júcar","Segura":"Segura","Turia":"Túria/Turia","Nalon":"Nalón","Genil":"Genil"}
Q={
 "Jucar":'way["waterway"="river"]["name"~"^(Xúquer|Riu Xúquer|Río Júcar|Júcar)$"](38.0,-2.5,40.6,0.5);',
 "Segura":'way["waterway"="river"]["name"~"^(Río Segura|Segura)$"](37.5,-3.0,38.6,-0.5);',
 "Turia":'way["waterway"="river"]["name"~"^(Riu Túria|Río Turia|Túria|Turia|Riu Túria/Río Turia)$"](39.4,-2.0,39.9,-0.2);',
 "Nalon":'way["waterway"="river"]["name"~"^(Río Nalón|Nalón)$"](42.9,-6.6,43.6,-5.4);',
 "Genil":'way["waterway"="river"]["name"~"^(Río Genil|Genil)$"](36.9,-5.5,37.9,-3.2);',
}
out={}
for k,q in Q.items():
    body="[out:json][timeout:120];("+q+");out geom;"
    for intento in range(3):
        try:
            r=urllib.request.urlopen(urllib.request.Request(
                "https://overpass-api.de/api/interpreter",
                data=urllib.parse.urlencode({"data":body}).encode(),
                headers={"User-Agent":"geo-nil/1.0"}),timeout=150)
            d=json.loads(r.read()); break
        except Exception as e:
            print(k,"intento",intento+1,"->",e); time.sleep(8); d=None
    if not d: continue
    segs=[[[round(p["lon"],4),round(p["lat"],4)] for p in w["geometry"]] for w in d["elements"] if w.get("geometry")]
    out[k]=segs
    print(f"{k:8s} -> {len(segs):4d} tramos, {sum(len(s) for s in segs):6d} puntos")
json.dump(out,open("osm_rios.json","w"))

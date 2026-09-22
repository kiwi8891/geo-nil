import json,os,io
P="/Users/gerardollanomartinez/Documents/SYNC DOCUMENTS/15_PROYECTOS/JUEGO_GEOGRAFIA"
mapa=json.load(open("out_mapa.json"))

# --- liga: Real Madrid primero, luego el resto ---
prog=json.load(open("progress.json"))
ORDEN=["Real Madrid","Barcelona","Atletico Madrid","Athletic Bilbao","Real Sociedad","Sevilla",
    "Real Betis","Valencia","Villarreal","Celta Vigo","Osasuna","Rayo Vallecano","Getafe",
    "Girona","Mallorca","Alaves","Espanyol","Elche","Levante","Real Oviedo"]
liga=[]
for nom in ORDEN:
    v=prog.get(nom)
    if not v or not v.get("jug"): continue
    liga.append({"eq":v["eq"],"escudo":v["escudo"],"c1":v.get("c1") or "","c2":v.get("c2") or "",
                 "estadio":v.get("estadio") or "","ciudad":v.get("ciudad") or "","anio":v.get("anio") or "",
                 "jug":[{"n":j["n"],"pos":j.get("pos") or "","num":j.get("num") or "",
                         "img":j.get("img") or "","nac":j.get("nac") or ""}
                        for j in v["jug"]]})
POS={"Goalkeeper":"Portero","Centre-Back":"Defensa central","Left-Back":"Lateral izquierdo",
 "Right-Back":"Lateral derecho","Defender":"Defensa","Defensive Midfield":"Pivote",
 "Central Midfield":"Centrocampista","Attacking Midfield":"Mediapunta","Midfielder":"Centrocampista",
 "Left Midfield":"Interior izquierdo","Right Midfield":"Interior derecho",
 "Left Wing":"Extremo izquierdo","Right Wing":"Extremo derecho","Right Winger":"Extremo derecho",
 "Left Winger":"Extremo izquierdo","Winger":"Extremo","Centre-Forward":"Delantero centro",
 "Forward":"Delantero","Attacker":"Delantero","Second Striker":"Segundo delantero",
 "Striker":"Delantero","Manager":"Entrenador"}
for e in liga:
    for j in e["jug"]:
        j["pos"]=POS.get(j["pos"], j["pos"] or "")
# La API devuelve el país en inglés y Nil lee "Spain". Se traduce aquí, al hornear.
NAC={"Algeria":"Argelia","Argentina":"Argentina","Austria":"Austria","Brazil":"Brasil",
 "Cameroon":"Camerún","Chile":"Chile","Colombia":"Colombia","Croatia":"Croacia",
 "DR Congo":"R. D. del Congo","Denmark":"Dinamarca","England":"Inglaterra","France":"Francia",
 "Georgia":"Georgia","Germany":"Alemania","Ghana":"Ghana","Hungary":"Hungría","Italy":"Italia",
 "Kenya":"Kenia","Mali":"Malí","Mexico":"México","Morocco":"Marruecos","Nigeria":"Nigeria",
 "Norway":"Noruega","Portugal":"Portugal","Romania":"Rumanía","Russia":"Rusia",
 "Senegal":"Senegal","Slovakia":"Eslovaquia","Spain":"España","Sweden":"Suecia",
 "The Netherlands":"Países Bajos","Togo":"Togo","Turkey":"Turquía","Ukraine":"Ucrania",
 "United States":"Estados Unidos","Uruguay":"Uruguay","Japan":"Japón",
 "Slovenia":"Eslovenia","Belgium":"Bélgica"}
for e in liga:
    for j in e["jug"]:
        j["nac"]=NAC.get(j["nac"], j["nac"] or "")
sin={j["pos"] for e in liga for j in e["jug"]} - set(POS.values()) - {""}
if sin: print("!! posiciones sin traducir:", sin)
sinac={j["nac"] for e in liga for j in e["jug"]} - set(NAC.values()) - {""}
if sinac: print("!! nacionalidades sin traducir:", sinac)

J=lambda o: json.dumps(o,ensure_ascii=False,separators=(",",":"))
html="".join(open(f).read() for f in
  ["tpl_head.html","tpl_body.html","tpl_js1.html","tpl_js2.html","tpl_js3.html","tpl_js4.html",
   "tpl_js6.html","tpl_js5.html"])   # js5 cierra el <script>, va siempre el último
banderas=json.load(open("out_banderas.json"))
# El atlas del modo aprender: las claves llevan el prefijo del tipo ("ccaa:galicia")
# porque "murcia" es a la vez comunidad, capital y ciudad.
atlas_raw=json.load(open("out_atlas.json")) if os.path.exists("out_atlas.json") else {}
atlas={(k if ":" in k else "ccaa:"+k):v for k,v in atlas_raw.items()}
html=(html.replace("/*__MAPA__*/",J(mapa)).replace("/*__LIGA__*/",J(liga))
          .replace("/*__BANDERAS__*/",J(banderas))
          .replace("/*__ATLAS__*/",J(atlas)))
for hueco in ("/*__MAPA__*/","/*__LIGA__*/","/*__BANDERAS__*/","/*__ATLAS__*/"):
    assert hueco not in html, "hueco sin rellenar: "+hueco
open(os.path.join(P,"index.html"),"w").write(html)

man={"name":"GEO NIL","short_name":"GEO NIL","start_url":"./index.html","display":"standalone",
     "orientation":"landscape","background_color":"#0d1b2e","theme_color":"#0d1b2e",
     "icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},
              {"src":"icon-512.png","sizes":"512x512","type":"image/png"}]}
json.dump(man,open(os.path.join(P,"manifest.json"),"w"),ensure_ascii=False,indent=1)
kb=os.path.getsize(os.path.join(P,"index.html"))/1024
cromos = sum(len(e["jug"]) for e in liga) + len(liga)     # +1 cromo de estadio por equipo
print(f"index.html {kb:.0f} KB | equipos {len(liga)} | cromos {cromos}"
      f" (jugadores {sum(len(e['jug']) for e in liga)} + estadios {len(liga)})"
      f" | con foto {sum(1 for e in liga for j in e['jug'] if j['img'])}"
      f" | banderas {len(banderas)} | fichas de atlas {len(atlas)}"
      f" ({sum(len(v['fotos']) for v in atlas.values())} fotos)")
sin_est = [e["eq"] for e in liga if not e["estadio"]]
if sin_est: print("!! equipos sin estadio:", ", ".join(sin_est))
print("equipos:", ", ".join(e["eq"] for e in liga))

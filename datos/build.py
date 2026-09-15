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
                 "jug":[{"n":j["n"],"pos":j.get("pos") or "","num":j.get("num") or "","img":j.get("img") or ""}
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
sin={j["pos"] for e in liga for j in e["jug"]} - set(POS.values()) - {""}
if sin: print("!! posiciones sin traducir:", sin)

J=lambda o: json.dumps(o,ensure_ascii=False,separators=(",",":"))
html="".join(open(f).read() for f in
  ["tpl_head.html","tpl_body.html","tpl_js1.html","tpl_js2.html","tpl_js3.html","tpl_js4.html","tpl_js5.html"])
html=html.replace("/*__MAPA__*/",J(mapa)).replace("/*__LIGA__*/",J(liga))
open(os.path.join(P,"index.html"),"w").write(html)

man={"name":"GEO NIL","short_name":"GEO NIL","start_url":"./index.html","display":"standalone",
     "orientation":"landscape","background_color":"#0d1b2e","theme_color":"#0d1b2e",
     "icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},
              {"src":"icon-512.png","sizes":"512x512","type":"image/png"}]}
json.dump(man,open(os.path.join(P,"manifest.json"),"w"),ensure_ascii=False,indent=1)
kb=os.path.getsize(os.path.join(P,"index.html"))/1024
print(f"index.html {kb:.0f} KB | equipos {len(liga)} | cromos {sum(len(e['jug']) for e in liga)}"
      f" | con foto {sum(1 for e in liga for j in e['jug'] if j['img'])}")
print("equipos:", ", ".join(e["eq"] for e in liga))

import json,urllib.request,urllib.parse,time,os
B="https://www.thesportsdb.com/api/v1/json/3/"
def get(u,n=6):
    for i in range(n):
        try:
            r=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"geo-nil/1.0"}),timeout=35)
            t=r.read()
            if t.strip(): return json.loads(t)
        except Exception: pass
        time.sleep(3+i*3)
    return {}
EQ=["Real Madrid","Barcelona","Atletico Madrid","Athletic Bilbao","Real Sociedad","Sevilla",
    "Real Betis","Valencia","Villarreal","Celta Vigo","Osasuna","Rayo Vallecano","Getafe",
    "Girona","Mallorca","Alaves","Espanyol","Elche","Levante","Real Oviedo"]
prog=json.load(open("progress.json")) if os.path.exists("progress.json") else {}
for nom in EQ:
    if prog.get(nom,{}).get("jug"): continue
    d=get(B+"searchteams.php?t="+urllib.parse.quote(nom))
    ts=[t for t in (d.get("teams") or []) if t.get("strLeague")=="Spanish La Liga"]
    if not ts: print(f"  ?? {nom}: equipo no hallado"); time.sleep(3); continue
    t=ts[0]
    pl=(get(B+f"lookup_all_players.php?id={t['idTeam']}") or {}).get("player") or []
    jug=[{"n":p.get("strPlayer"),"pos":p.get("strPosition"),"num":p.get("strNumber"),
          "img":p.get("strCutout") or "","nac":p.get("strNationality") or ""} for p in pl if p.get("strPlayer")]
    if not jug: print(f"  ?? {nom} (id {t['idTeam']}): plantilla vacia"); time.sleep(3); continue
    prog[nom]={"id":t["idTeam"],"eq":t["strTeam"],"escudo":t.get("strBadge") or "",
               "c1":t.get("strColour1") or "","c2":t.get("strColour2") or "","jug":jug}
    json.dump(prog,open("progress.json","w"),ensure_ascii=False)
    print(f"  OK {t['strTeam']:20s} {len(jug):2d} jug, {sum(1 for j in jug if j['img']):2d} con foto")
    time.sleep(3)
falta=[e for e in EQ if not prog.get(e,{}).get("jug")]
print("\nCONSEGUIDOS:",len(prog),"| FALTAN:",falta)
print("JUGADORES:",sum(len(v['jug']) for v in prog.values()),
      "| CON FOTO:",sum(1 for v in prog.values() for j in v['jug'] if j['img']))

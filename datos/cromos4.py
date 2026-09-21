"""Completa progress.json: los 4 equipos que faltaban y el estadio de todos.

Por qué hacía falta otro script y no valía cromos3.py:
  - TheSportsDB etiqueta MAL la liga. Girona, Mallorca y Real Oviedo figuran como
    "Spanish La Liga 2", así que el filtro strLeague=="Spanish La Liga" los tiraba.
  - searchteams.php?t=Alaves devuelve el equipo FEMENINO (Alavés Gloriosas, Liga F).
    El masculino sale buscando "Deportivo Alaves".
  Ahora se filtra por país + género, que es lo que la API sí tiene bien, y cada
  equipo lleva su alias de búsqueda cuando el nombre corto no basta.
"""
import json, urllib.request, urllib.parse, time, os

B = "https://www.thesportsdb.com/api/v1/json/3/"
def get(u, n=5):
    for i in range(n):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent":"geo-nil/1.0"}), timeout=35)
            t = r.read()
            if t.strip(): return json.loads(t)
        except Exception: pass
        time.sleep(3 + i*3)
    return {}

# nombre en progress.json -> término de búsqueda
EQ = {"Real Madrid":"Real Madrid", "Barcelona":"Barcelona", "Atletico Madrid":"Atletico Madrid",
      "Athletic Bilbao":"Athletic Bilbao", "Real Sociedad":"Real Sociedad", "Sevilla":"Sevilla",
      "Real Betis":"Real Betis", "Valencia":"Valencia", "Villarreal":"Villarreal",
      "Celta Vigo":"Celta Vigo", "Osasuna":"Osasuna", "Rayo Vallecano":"Rayo Vallecano",
      "Getafe":"Getafe", "Girona":"Girona", "Mallorca":"Mallorca",
      "Alaves":"Deportivo Alaves",            # <- el corto da el equipo femenino
      "Espanyol":"Espanyol", "Elche":"Elche", "Levante":"Levante", "Real Oviedo":"Real Oviedo"}

prog = json.load(open("progress.json")) if os.path.exists("progress.json") else {}

def bueno(t):
    """Club masculino español. La liga no se mira: la API la tiene mal en 4 de 20."""
    return (t.get("strCountry") == "Spain"
            and (t.get("strGender") or "Male") == "Male"
            and (t.get("strSport") or "Soccer") == "Soccer")

for nom, busca in EQ.items():
    cur = prog.get(nom, {})
    if cur.get("jug") and cur.get("estadio"): continue          # ya completo
    d = get(B + "searchteams.php?t=" + urllib.parse.quote(busca))
    ts = [t for t in (d.get("teams") or []) if bueno(t)]
    if not ts:
        print(f"  ?? {nom}: no hallado"); time.sleep(2); continue
    t = ts[0]
    jug = cur.get("jug") or []
    if not jug:
        pl = (get(B + f"lookup_all_players.php?id={t['idTeam']}") or {}).get("player") or []
        jug = [{"n":p.get("strPlayer"), "pos":p.get("strPosition"), "num":p.get("strNumber"),
                "img":p.get("strCutout") or "", "nac":p.get("strNationality") or ""}
               for p in pl if p.get("strPlayer")]
        time.sleep(2)
    prog[nom] = {"id": t["idTeam"], "eq": t["strTeam"], "escudo": t.get("strBadge") or "",
                 "c1": t.get("strColour1") or "", "c2": t.get("strColour2") or "",
                 "c3": t.get("strColour3") or "",
                 "estadio": t.get("strStadium") or "", "ciudad": t.get("strLocation") or "",
                 "anio": t.get("intFormedYear") or "", "corto": t.get("strTeamShort") or "",
                 "fanart": t.get("strFanart1") or t.get("strFanart2") or "",
                 "jug": jug}
    json.dump(prog, open("progress.json","w"), ensure_ascii=False)
    print(f"  OK {t['strTeam']:22s} {len(jug):2d} jug | {t.get('strStadium','')}")
    time.sleep(2)

falta = [e for e in EQ if not prog.get(e,{}).get("jug")]
sin_est = [e for e in EQ if not prog.get(e,{}).get("estadio")]
print("\nEQUIPOS:", len(prog), "| SIN PLANTILLA:", falta, "| SIN ESTADIO:", sin_est)
print("JUGADORES:", sum(len(v["jug"]) for v in prog.values()),
      "| CON FOTO:", sum(1 for v in prog.values() for j in v["jug"] if j["img"]))

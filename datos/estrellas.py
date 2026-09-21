# -*- coding: utf-8 -*-
"""Añade las estrellas de cada equipo al álbum.

lookup_all_players.php devuelve los 10 primeros POR ORDEN ALFABÉTICO, no los
mejores: el Real Madrid salía con Alexis Ciria y sin Mbappé, y el Barça sin
Lewandowski ni Yamal. Para un niño de 6 años eso es un álbum roto.

searchplayers.php?p=<nombre> sí trae a uno concreto, con su cutout. Se pide por
nombre y SOLO se acepta si strTeam coincide con el equipo esperado: así un
fichaje reciente no acaba metido en el club que ya dejó.

Reanudable: guarda en progress.json tras cada equipo.
"""
import json, urllib.request, urllib.parse, time, os, unicodedata

B = "https://www.thesportsdb.com/api/v1/json/3/"
def get(u, n=4):
    for i in range(n):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent":"geo-nil/1.0"}), timeout=35)
            t = r.read()
            if t.strip(): return json.loads(t)
        except Exception: pass
        time.sleep(3 + i*3)
    return {}

def norm(s):
    s = unicodedata.normalize("NFD", (s or "").lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.replace("-", " ").replace(".", "").strip()

# equipo en progress.json -> jugadores que Nil reconocería
ESTRELLAS = {
 "Real Madrid": ["Kylian Mbappe", "Vinicius Junior", "Jude Bellingham", "Thibaut Courtois",
                 "Federico Valverde", "Eduardo Camavinga", "Rodrygo"],
 "Barcelona": ["Lamine Yamal", "Robert Lewandowski", "Pedri", "Raphinha", "Marc-Andre ter Stegen",
               "Ronald Araujo", "Gavi"],
 "Atletico Madrid": ["Antoine Griezmann", "Julian Alvarez", "Jan Oblak", "Koke", "Alexander Sorloth"],
 "Athletic Bilbao": ["Nico Williams", "Inaki Williams", "Oihan Sancet", "Unai Simon"],
 "Real Sociedad": ["Mikel Oyarzabal", "Takefusa Kubo", "Alex Remiro", "Brais Mendez"],
 "Sevilla": ["Dodi Lukebakio", "Nemanja Gudelj", "Isaac Romero"],
 "Real Betis": ["Isco", "Giovani Lo Celso", "Antony", "Marc Bartra"],
 "Valencia": ["Hugo Duro", "Pepelu", "Giorgi Mamardashvili"],
 "Villarreal": ["Gerard Moreno", "Ayoze Perez", "Dani Parejo"],
 "Celta Vigo": ["Iago Aspas", "Borja Iglesias"],
 "Osasuna": ["Ante Budimir", "Lucas Torro"],
 "Rayo Vallecano": ["Isi Palazon", "Raul de Tomas", "Augusto Batalla"],
 "Getafe": ["Borja Mayoral", "David Soria"],
 "Girona": ["Cristhian Stuani", "Paulo Gazzaniga"],
 "Mallorca": ["Vedat Muriqi", "Antonio Raillo"],
 "Alaves": ["Kike Garcia", "Antonio Sivera"],
 "Espanyol": ["Javi Puado", "Joan Garcia"],
 "Elche": ["Pedro Bigas"],
 "Levante": ["Carlos Alvarez"],
 "Real Oviedo": ["Santiago Cazorla", "Alberto Reina"],
}

prog = json.load(open("progress.json"))
total = 0
for equipo, nombres in ESTRELLAS.items():
    v = prog.get(equipo)
    if not v: print(f"  ?? {equipo}: no está en progress.json"); continue
    ya = {norm(j["n"]) for j in v["jug"]}
    esperado = {norm(v["eq"]), norm(equipo)}
    nuevos = 0
    for nom in nombres:
        if norm(nom) in ya: continue
        d = get(B + "searchplayers.php?p=" + urllib.parse.quote(nom))
        pl = d.get("player") or []
        elegido = None
        for p in pl:
            t = norm(p.get("strTeam"))
            # el club tiene que cuadrar; se acepta el nombre corto de la API
            # ("Vallecano" por "Rayo Vallecano"), pero no el filial ni el femenino
            if any(t == e or (len(t) > 4 and (t in e or e in t)) for e in esperado) \
               and not any(x in t for x in (" b", " ii", "femen", "women")):
                elegido = p; break
        if not elegido:
            visto = ", ".join(str(p.get("strTeam")) for p in pl[:2]) or "sin resultados"
            # Se descarta a propósito: si la API lo pone en otro club, gana la API.
            # Lewandowski en Chicago Fire o Griezmann en Orlando City parecen errores
            # pero son traspasos reales; forzarlos metería cromos falsos en el álbum.
            print(f"     - {nom:24s} descartado (aparece en: {visto})")
            time.sleep(2); continue
        v["jug"].append({"n": elegido.get("strPlayer"), "pos": elegido.get("strPosition"),
                         "num": elegido.get("strNumber") or "", "img": elegido.get("strCutout") or "",
                         "nac": elegido.get("strNationality") or ""})
        ya.add(norm(nom)); nuevos += 1; total += 1
        time.sleep(2)
    json.dump(prog, open("progress.json", "w"), ensure_ascii=False)
    print(f"  {v['eq']:22s} +{nuevos} -> {len(v['jug'])} jugadores")

print(f"\nañadidos {total} | jugadores totales {sum(len(v['jug']) for v in prog.values())}"
      f" | con foto {sum(1 for v in prog.values() for j in v['jug'] if j['img'])}")

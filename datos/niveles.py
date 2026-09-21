# -*- coding: utf-8 -*-
"""Reparte los sitios del mapa en 5 niveles. Idempotente: se puede correr siempre.

Antes eran 3 y el salto de Fácil a Normal metía media España de golpe. Con 5
entran unos pocos cada vez. El orden dentro de cada lista es el de un mapa
escolar: primero lo que un niño ya ha oído, al final lo que hay que estudiarse.
"""
import json, collections

CCAA = [
 ["Andalucía", "Cataluña", "Galicia", "Canarias", "Baleares"],
 ["Castilla y León", "Madrid", "Comunidad Valenciana", "Aragón"],
 ["Castilla-La Mancha", "Extremadura", "Asturias", "Murcia"],
 ["País Vasco", "Navarra", "Cantabria"],
 ["La Rioja", "Ceuta", "Melilla"],
]
CAPITALES = [
 ["Madrid", "Barcelona", "Valencia", "Sevilla"],
 ["Zaragoza", "Toledo", "Valladolid", "Oviedo"],
 ["Santiago de Compostela", "Mérida", "Murcia", "Palma"],
 ["Santander", "Pamplona", "Vitoria", "Logroño"],
 ["Las Palmas de Gran Canaria", "Santa Cruz de Tenerife", "Ceuta", "Melilla"],
]
CIUDADES = [
 ["Bilbao", "Málaga", "Vigo"],
 ["A Coruña", "Gijón", "Alicante", "Córdoba"],
 ["Granada", "Salamanca", "Cádiz", "León"],
 ["Burgos", "Almería", "Badajoz", "Tarragona"],
 ["Girona", "Huesca", "Cuenca", "Albacete", "Cáceres"],
]
RIOS = [
 ["Ebro", "Tajo", "Duero", "Guadalquivir"],
 ["Guadiana", "Miño", "Segura"],
 ["Júcar", "Turia", "Genil", "Segre"],
 ["Nalón", "Sil", "Esla", "Pisuerga", "Tormes", "Llobregat"],
 ["Narcea", "Cinca", "Jalón", "Henares", "Alberche", "Mijares", "Cabriel",
  "Ter", "Jarama", "Gállego"],
]
# Solo hay 6 cordilleras, así que el nivel 1 se lleva 3: una ronda necesita
# al menos 3 sitios distintos o el bloque no arranca.
CORD = [
 ["Pirineos", "Cordillera Cantábrica", "Sierra Nevada"],
 ["Sistema Central"],
 ["Sierra Morena"],
 ["Sistema Ibérico"],
 [],
]
AGUAS = [
 ["Mar Mediterráneo", "Océano Atlántico", "Mar Cantábrico", "Islas Baleares"],
 ["Islas Canarias", "Estrecho de Gibraltar", "Mallorca", "Tenerife"],
 ["Golfo de Vizcaya", "Golfo de Cádiz", "Gran Canaria", "Cabo de Gata"],
 ["Golfo de Valencia", "Cabo Finisterre", "Menorca", "Ibiza"],
 ["Cabo de Creus", "Cabo de Palos", "Lanzarote", "Fuerteventura", "La Palma"],
]

def aplicar(items, tabla, etiqueta):
    nivel = {}
    for i, grupo in enumerate(tabla, 1):
        for n in grupo: nivel[n] = i
    sueltos = []
    for x in items:
        if x["n"] in nivel: x["lv"] = nivel[x["n"]]
        else: x["lv"] = 5; sueltos.append(x["n"])
    if sueltos: print(f"  !! {etiqueta}: sin nivel asignado (van al 5): {', '.join(sueltos)}")
    sobran = [n for n in nivel if n not in {x["n"] for x in items}]
    if sobran: print(f"  ?? {etiqueta}: en la tabla pero no en el mapa: {', '.join(sobran)}")
    return items

if __name__ == "__main__":
    m = json.load(open("out_mapa.json"))
    aplicar(m["ccaa"], CCAA, "ccaa")
    aplicar(m["rios"], RIOS, "ríos")
    aplicar(m["cord"], CORD, "cordilleras")
    aplicar(m["aguas"], AGUAS, "aguas")
    aplicar([c for c in m["ciudades"] if c.get("cap")], CAPITALES, "capitales")
    aplicar([c for c in m["ciudades"] if not c.get("cap")], CIUDADES, "ciudades")
    json.dump(m, open("out_mapa.json", "w"), ensure_ascii=False, separators=(",", ":"))

    print("\nsitios disponibles por nivel (acumulado):")
    caps = [c for c in m["ciudades"] if c.get("cap")]
    ciu  = [c for c in m["ciudades"] if not c.get("cap")]
    filas = [("COMUNIDADES", m["ccaa"]), ("CAPITALES", caps), ("RÍOS", m["rios"]),
             ("MONTAÑAS", m["cord"]), ("CIUDADES Y MARES", ciu + m["aguas"])]
    print(f"  {'bloque':18s}" + "".join(f"  lv{l}" for l in range(1, 6)))
    for nom, arr in filas:
        print(f"  {nom:18s}" + "".join(f"  {sum(1 for x in arr if x['lv'] <= l):3d}" for l in range(1, 6)))

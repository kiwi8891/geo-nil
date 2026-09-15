import json
exec(open("geo.py").read().split("# ---------- topojson")[0])

# (nombre, lon, lat, es_capital_ccaa, nivel 1=fácil)
CIU=[
 ("Madrid",-3.703,40.417,1,1),("Barcelona",2.173,41.385,1,1),("Valencia",-0.376,39.470,1,1),
 ("Sevilla",-5.994,37.389,1,1),("Zaragoza",-0.889,41.649,1,1),("Bilbao",-2.935,43.263,0,1),
 ("Málaga",-4.421,36.721,0,1),("Santiago de Compostela",-8.545,42.878,1,2),
 ("Valladolid",-4.724,41.652,1,2),("Toledo",-4.027,39.862,1,2),("Mérida",-6.344,38.916,1,2),
 ("Oviedo",-5.845,43.362,1,2),("Santander",-3.805,43.462,1,2),("Pamplona",-1.644,42.817,1,2),
 ("Vitoria",-2.673,42.847,1,2),("Logroño",-2.445,42.466,1,2),("Murcia",-1.130,37.992,1,2),
 ("Palma",2.650,39.570,1,2),("Las Palmas de Gran Canaria",-15.430,28.124,1,2),
 ("Santa Cruz de Tenerife",-16.251,28.469,1,2),("Ceuta",-5.316,35.889,1,3),("Melilla",-2.938,35.292,1,3),
 ("A Coruña",-8.396,43.371,0,3),("Vigo",-8.721,42.231,0,3),("Gijón",-5.662,43.545,0,3),
 ("Alicante",-0.483,38.345,0,3),("Córdoba",-4.779,37.889,0,3),("Granada",-3.599,37.177,0,3),
 ("Salamanca",-5.664,40.965,0,3),("Burgos",-3.700,42.344,0,3),("León",-5.567,42.599,0,3),
 ("Cádiz",-6.292,36.530,0,3),("Almería",-2.464,36.834,0,3),("Badajoz",-6.970,38.879,0,3),
 ("Tarragona",1.250,41.119,0,3),("Girona",2.824,41.984,0,3),("Huesca",-0.409,42.140,0,3),
 ("Cuenca",-2.135,40.070,0,3),("Albacete",-1.858,38.995,0,3),("Cáceres",-6.371,39.476,0,3),
]
ciudades=[{"id":n.lower().replace(" ","_"),"n":n,"cap":c,"lv":lv,
           "x":proj(lo,la)[0],"y":proj(lo,la)[1]} for n,lo,la,c,lv in CIU]

# mares, golfos, cabos, islas, estrecho — chinchetas en agua o punta
AGUA=[
 ("Mar Mediterráneo",0.9,39.3,1),("Océano Atlántico",-9.3,38.0,1),
 ("Mar Cantábrico",-4.3,44.0,1),("Estrecho de Gibraltar",-5.55,35.95,1),
 ("Golfo de Vizcaya",-2.6,44.15,2),("Golfo de Cádiz",-7.0,36.8,2),
 ("Golfo de Valencia",0.35,39.6,2),("Cabo de Gata",-2.19,36.72,2),
 ("Cabo Finisterre",-9.27,42.88,2),("Cabo de Creus",3.32,42.32,3),
 ("Cabo de Palos",-0.70,37.63,3),("Islas Baleares",2.9,39.6,1),
 ("Islas Canarias",-15.6,28.1,1),("Mallorca",3.0,39.62,2),("Menorca",4.08,39.95,3),
 ("Ibiza",1.43,38.98,3),("Tenerife",-16.60,28.28,2),("Gran Canaria",-15.60,27.96,2),
 ("Lanzarote",-13.62,29.03,3),("Fuerteventura",-14.02,28.36,3),("La Palma",-17.87,28.68,3),
]
aguas=[{"id":n.lower().replace(" ","_").replace("á","a").replace("é","e").replace("í","i"),
        "n":n,"lv":lv,"x":proj(lo,la)[0],"y":proj(lo,la)[1]} for n,lo,la,lv in AGUA]

json.dump({"ciudades":ciudades,"aguas":aguas},open("out_puntos.json","w"),ensure_ascii=False)
print("ciudades:",len(ciudades),"(capitales CCAA:",sum(c["cap"] for c in ciudades),")")
print("mares/costas/islas:",len(aguas))
fuera=[c["n"] for c in ciudades+aguas if not(0<=c["x"]<=1000 and 0<=c["y"]<=700)]
print("fuera de lienzo:",fuera or "ninguno")

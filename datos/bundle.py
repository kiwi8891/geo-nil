import json
L=lambda f: json.load(open(f))
ccaa,rios,cord,pts,vec=L("out_ccaa.json"),L("out_rios.json"),L("out_cord.json"),L("out_puntos.json"),L("out_vecinos.json")

CAP2CCAA={"Sevilla":"Andalucía","Zaragoza":"Aragón","Oviedo":"Asturias","Palma":"Baleares",
 "Santander":"Cantabria","Valladolid":"Castilla y León","Toledo":"Castilla-La Mancha",
 "Barcelona":"Cataluña","Valencia":"Comunidad Valenciana","Mérida":"Extremadura",
 "Santiago de Compostela":"Galicia","Madrid":"Madrid","Murcia":"Murcia","Pamplona":"Navarra",
 "Vitoria":"País Vasco","Logroño":"La Rioja","Ceuta":"Ceuta","Melilla":"Melilla",
 "Las Palmas de Gran Canaria":"Canarias","Santa Cruz de Tenerife":"Canarias"}
for c in pts["ciudades"]:
    if c.get("cap"): c["ccaaNom"]=CAP2CCAA.get(c["n"],"")
LV_CCAA={1:["Andalucía","Galicia","Cataluña","Canarias","Baleares","Castilla y León"],
         2:["Aragón","Extremadura","Castilla-La Mancha","Comunidad Valenciana","Asturias","Murcia","Madrid"]}
LV_RIOS={1:["Ebro","Tajo","Duero","Guadiana","Guadalquivir"],2:["Miño","Júcar","Segura"]}
LV_CORD={1:["Pirineos","Cordillera Cantábrica","Sierra Nevada"],2:["Sistema Central","Sierra Morena"]}
def setlv(lst,mapa):
    for x in lst:
        x["lv"]=1 if x["n"] in mapa[1] else (2 if x["n"] in mapa[2] else 3)
setlv(ccaa,LV_CCAA); setlv(rios,LV_RIOS); setlv(cord,LV_CORD)

# artículo para la frase de la pregunta
ART={"Ebro":"el","Tajo":"el","Duero":"el","Guadiana":"el","Guadalquivir":"el","Miño":"el",
     "Júcar":"el","Segura":"el","Turia":"el","Nalón":"el","Genil":"el","Segre":"el",
     "Pirineos":"los","Cordillera Cantábrica":"la","Sistema Central":"el","Sistema Ibérico":"el",
     "Sierra Morena":"","Sierra Nevada":""}
for r in rios: r["art"]="el"
for c in cord: c["art"]=ART.get(c["n"],"")
def art_agua(n):
    for p,a in (("Mar ","el"),("Océano ","el"),("Estrecho","el"),("Golfo","el"),("Cabo","el"),("Islas","las")):
        if n.startswith(p): return a
    return ""
for a in pts["aguas"]: a["art"]=art_agua(a["n"])

D={"ccaa":ccaa,"rios":rios,"cord":cord,"ciudades":pts["ciudades"],"aguas":pts["aguas"],"vec":vec,
   "W":1000,"H":700,"canario":[8,540,322,152]}
json.dump(D,open("out_mapa.json","w"),ensure_ascii=False,separators=(",",":"))
import os
print("mapa.json:",os.path.getsize("out_mapa.json")//1024,"KB")
for k in ("ccaa","rios","cord"):
    print(" ",k,{lv:sum(1 for x in D[k] if x["lv"]<=lv) for lv in (1,2,3)})
print("  ciudades",{lv:sum(1 for x in D['ciudades'] if x['lv']<=lv) for lv in (1,2,3)},
      "| aguas",{lv:sum(1 for x in D['aguas'] if x['lv']<=lv) for lv in (1,2,3)})

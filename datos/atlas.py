# -*- coding: utf-8 -*-
"""Baja las fotos del modo APRENDER y arma out_atlas.json.

Las fotos van AL REPO (carpeta img/), no dentro del index.html: metidas en el
HTML lo dejarían en varios MB y tarda en abrir; enlazadas a Wikipedia se verían
solo con internet y al capricho de que las URL sigan vivas.

Son de Wikimedia Commons y el repo es público, así que se guarda el autor y la
licencia de cada una y la ficha los muestra en pequeño.

OJO: la imagen principal del artículo de una comunidad es su MAPA de situación,
que no sirve para enseñarle a un niño qué es Galicia. Por eso en atlas_datos.py
se nombran sitios concretos (la catedral, un hórreo, las Cíes) y no la comunidad.

Los metadatos se piden EN LOTES de 20 títulos: de uno en uno son tres llamadas
por foto y Wikipedia responde 429 enseguida.

Reanudable: no vuelve a bajar lo que ya está en img/.
"""
import json, os, re, urllib.request, urllib.parse, time, sys

UA = {"User-Agent": "geo-nil/1.0 (juego de geografía infantil; uso familiar)"}
P = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(P, "..", "img")
ANCHO, LOTE = 640, 20

def pedir(u, binario=False, intentos=5):
    espera = 4
    for i in range(intentos):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40)
            b = r.read()
            return b if binario else json.loads(b)
        except urllib.error.HTTPError as e:
            if e.code != 429 or i == intentos - 1: raise
            time.sleep(espera); espera *= 2
        except Exception:
            if i == intentos - 1: raise
            time.sleep(espera)
    raise RuntimeError("sin respuesta")

NO_FOTO = ("escudo", "bandera", "coat", "flag", "mapa", "map", "locator", "location",
           "ubicacion", "situacion", "logo", "seal", "icon", "blason", "wappen", "plano",
           "diagram", "svg", "loc_map", "karte", "commons", "bandeira", "senyera")
# Categorías de Commons que delatan un símbolo aunque el fichero sea .jpg y se
# llame de forma inocente. Es el filtro que de verdad funciona: hay banderas y
# escudos servidos como JPG con nombres que no dicen nada.
CAT_MALA = ("flags", "coats of arms", "banderas", "escudos", "maps", "mapas", "locator",
            "heraldry", "emblems", "logos", "seals", "diagrams", "svg")
MIN_KB = 16      # una bandera de colores planos comprime muchísimo; una foto no
# Lo que se cuela igualmente: senyeras (muchas franjas = mucho detalle = pesan),
# mapas y escudos con filigrana. Señalado a mano mirando la hoja de contactos.
EXCLUIR = set()
try:
    from atlas_excluir import EXCLUIR          # se crea al revisar las fotos
except Exception:
    pass

def candidatos_de(titulos, cuantos=6):
    """{título: [ficheros candidatos, en orden de aparición en el artículo]}.

    pageimages devuelve la imagen de la ficha lateral, que en ciudades y
    comunidades es el escudo, la bandera o el mapa. media-list las da EN EL
    ORDEN DEL ARTÍCULO, donde las fotos van detrás de bandera y escudo.
    Se recogen varios candidatos porque el primero aún puede ser un símbolo:
    quién lo es de verdad lo decide después la categoría de Commons.
    """
    out = {}
    for t in titulos:
        lista = []
        try:
            d = pedir("https://es.wikipedia.org/api/rest_v1/page/media-list/" + urllib.parse.quote(t))
            items = [i for i in d.get("items", []) if i.get("type") == "image"]
        except Exception:
            items = []
        if not items:
            # media-list devuelve 500 en algunos artículos: se prueba la API clásica
            try:
                pg = list(pedir("https://es.wikipedia.org/w/api.php?action=query&format=json"
                                "&redirects=1&prop=images&imlimit=40&titles="
                                + urllib.parse.quote(t))["query"]["pages"].values())[0]
                items = [{"title": im.get("title", "")} for im in pg.get("images", [])]
            except Exception:
                items = []
        for it in items:
            nom = (it.get("title") or "").replace("Archivo:", "").replace("File:", "")
            bajo = nom.lower()
            if not bajo.endswith((".jpg", ".jpeg")): continue
            if any(x in bajo for x in NO_FOTO): continue
            lista.append(nom)
            if len(lista) >= cuantos: break
        out[t] = lista
        time.sleep(0.7)
    return out

def info_de(ficheros):
    """{fichero: (url, credito, es_simbolo)} en lotes, mirando las categorías."""
    out = {}
    ficheros = sorted({f for f in ficheros if f})
    for i in range(0, len(ficheros), LOTE):
        trozo = ficheros[i:i+LOTE]
        u = ("https://commons.wikimedia.org/w/api.php?action=query&format=json"
             "&prop=imageinfo|categories&cllimit=max&iiprop=url|extmetadata&iiurlwidth=%d&titles=%s"
             % (ANCHO, urllib.parse.quote("|".join("File:"+f for f in trozo))))
        try:
            d = pedir(u)
        except Exception:
            continue
        for pg in d.get("query", {}).get("pages", {}).values():
            t = pg.get("title", "").replace("File:", "").replace("Archivo:", "")
            ii = (pg.get("imageinfo") or [{}])[0]
            m = ii.get("extmetadata", {})
            autor = re.sub("<[^>]+>", " ", m.get("Artist", {}).get("value", ""))
            autor = re.sub(r"\s+", " ", autor).strip(" ,")
            autor = re.sub(r"No machine-readable author provided\.?\s*", "", autor)
            autor = re.sub(r"\s*assumed \(based on copyright claims\)\.?", "", autor).strip(" ,.")
            lic = m.get("LicenseShortName", {}).get("value", "")
            cred = (autor[:70] or "Wikimedia Commons") + (" · " + lic if lic else "")
            cats = " ".join(c.get("title", "").lower() for c in pg.get("categories", []))
            simbolo = any(x in cats for x in CAT_MALA)
            out[t.replace("_", " ")] = (ii.get("thumburl") or ii.get("url"), cred, simbolo)
        time.sleep(1.2)
    return out

def construir(tablas):
    """tablas = [(prefijo_de_clave, diccionario)]"""
    os.makedirs(IMG, exist_ok=True)
    fsal = os.path.join(P, "out_atlas.json")
    atlas = json.load(open(fsal)) if os.path.exists(fsal) else {}
    # de qué fichero de Commons viene cada imagen que ya está en disco
    previo = {f["f"].split("/")[-1]: f.get("src")
              for v in atlas.values() for f in v.get("fotos", [])}

    titulos = sorted({t for _, tab in tablas for v in tab.values() for t in v["fotos"]})
    print(f"pidiendo datos de {len(titulos)} fotos en lotes de {LOTE}...")
    cands = candidatos_de(titulos)
    datos = info_de([f for lista in cands.values() for f in lista])
    simbolos = sum(1 for v in datos.values() if v[2])
    print(f"  {len(datos)} ficheros consultados, {simbolos} descartados por ser "
          f"bandera, escudo o mapa\n")

    fallos = []
    for prefijo, tabla in tablas:
        for sid, d in tabla.items():
            clave = prefijo + sid
            fotos = []
            for i, titulo in enumerate(d["fotos"], 1):
                slug = re.sub(r"[^a-z0-9]+", "-", clave.replace(":", "-").lower()).strip("-")
                elegida = None
                # Se prueban los candidatos EN ORDEN y se comprueba el peso de lo
                # descargado: ni el nombre ni las categorías de Commons distinguen
                # bien una bandera de una foto (hay banderas en .jpg, con nombre
                # inocente y sin categoría que las delate), pero el peso sí. Una
                # bandera son colores planos y comprime a 8-15 KB; una foto no baja
                # de 25 KB al mismo ancho.
                for cand in cands.get(titulo, []):
                    url, credito, simbolo = datos.get(cand.replace("_", " "), (None, None, True))
                    if not url or simbolo or cand in EXCLUIR: continue
                    ext = os.path.splitext(url.split("?")[0])[1].lower()
                    if ext not in (".jpg", ".jpeg", ".png", ".webp"): ext = ".jpg"
                    nombre = f"{slug}-{i}{ext}"
                    ruta = os.path.join(IMG, nombre)
                    alt = os.path.join(IMG, f"{slug}-{i}.jpg")
                    if ext != ".jpg" and os.path.exists(alt):
                        nombre, ruta = f"{slug}-{i}.jpg", alt
                    if os.path.exists(ruta) and previo.get(nombre) not in (None, cand):
                        os.remove(ruta)          # en disco hay otra foto distinta
                    if not os.path.exists(ruta):
                        try:
                            open(ruta, "wb").write(pedir(url, binario=True))
                            time.sleep(0.35)
                        except Exception as e:
                            fallos.append(f"{clave}: «{titulo}» -> {str(e)[:40]}"); continue
                    peso = os.path.getsize(ruta)//1024
                    if peso < MIN_KB:
                        os.remove(ruta)                  # era un símbolo: siguiente candidato
                        continue
                    elegida = {"f": "img/" + nombre, "cred": credito, "kb": peso, "src": cand}
                    break
                if elegida: fotos.append(elegida)
                else: fallos.append(f"{clave}: «{titulo}» sin foto utilizable")
            atlas[clave] = {"texto": d["texto"], "dato": d["dato"], "fotos": fotos}
            json.dump(atlas, open(fsal, "w"), ensure_ascii=False)
            print(f"  {clave:32s} {len(fotos)} fotos")
    return atlas, fallos

if __name__ == "__main__":
    import atlas_datos as D
    tablas = [("ccaa:", D.CCAA), ("cord:", D.CORD), ("rio:", D.RIOS), ("cap:", D.CAPITALES)]
    if hasattr(D, "CIUDADES"): tablas.append(("ciudad:", D.CIUDADES))
    if hasattr(D, "AGUAS"): tablas.append(("agua:", D.AGUAS))
    atlas, fallos = construir(tablas)
    peso = sum(x["kb"] for v in atlas.values() for x in v["fotos"])
    print(f"\nfichas: {len(atlas)} | fotos: {sum(len(v['fotos']) for v in atlas.values())}"
          f" | {peso/1024:.1f} MB (sin optimizar: pasa optimizar.py)")
    if fallos:
        print("\nSIN FOTO (corregir el título en atlas_datos.py):")
        for f in fallos: print("  !!", f)

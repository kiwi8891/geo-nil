# -*- coding: utf-8 -*-
"""Aprieta las fotos de img/ para que el repo no se ponga imposible.

Wikipedia sirve el thumbnail al tamaño estándar que le da la gana (pide 640 y
devuelve 960) y algunas vienen en PNG de un mega. A 640 px de ancho y JPEG 62
se ven igual de bien en el iPad y pesan la quinta parte.

Usa sips, que viene con macOS: nada que instalar.
"""
import os, subprocess, json, sys

P = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(P, "..", "img")
ANCHO, CALIDAD = 520, 58

def kb(f): return os.path.getsize(f) / 1024

antes = total = 0
renombres = {}
for nombre in sorted(os.listdir(IMG)):
    if not nombre.lower().endswith((".jpg", ".jpeg", ".png", ".webp")): continue
    ruta = os.path.join(IMG, nombre)
    antes += kb(ruta)
    base, ext = os.path.splitext(nombre)
    destino = os.path.join(IMG, base + ".jpg")
    r = subprocess.run(["sips", "-Z", str(ANCHO), "-s", "format", "jpeg",
                        "-s", "formatOptions", str(CALIDAD), ruta, "--out", destino],
                       capture_output=True)
    if r.returncode != 0:
        print("  !!", nombre, r.stderr.decode()[:70]); total += kb(ruta); continue
    if ext.lower() != ".jpg":
        os.remove(ruta)
        renombres[nombre] = base + ".jpg"
    total += kb(destino)
    print(f"  {nombre:26s} {kb(ruta) if os.path.exists(ruta) else 0:6.0f} KB -> {kb(destino):5.0f} KB")

# si algún .png pasó a .jpg, el atlas tiene que apuntar al nombre nuevo
f = os.path.join(P, "out_atlas.json")
if renombres and os.path.exists(f):
    atlas = json.load(open(f))
    for v in atlas.values():
        for foto in v.get("fotos", []):
            n = foto["f"].split("/")[-1]
            if n in renombres: foto["f"] = "img/" + renombres[n]
    json.dump(atlas, open(f, "w"), ensure_ascii=False)
    print("  (atlas actualizado con", len(renombres), "cambios de extensión)")

print(f"\ntotal: {antes/1024:.1f} MB -> {total/1024:.1f} MB")

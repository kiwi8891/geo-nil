# -*- coding: utf-8 -*-
"""Banderas de las 19 comunidades, dibujadas a mano en SVG y horneadas en el HTML.

Van inline y no como imagen remota porque el iPad juega sin red. Son banderas
ESCOLARES: franjas y símbolos reconocibles, con los escudos reducidos a su silueta
(el de Ceuta o el de Melilla a tamaño cromo serían una mancha). Lienzo 60x40,
el contenido va dentro de un <svg viewBox="0 0 60 40"> que pone el JS.
"""
import json

def barras(n=4, vert=False):
    """Palos de Aragón / senyera: 9 franjas, 4 rojas sobre amarillo."""
    d = ['<rect width="60" height="40" fill="#fcdd09"/>']
    for i in range(n):
        if vert:
            d.append(f'<rect x="{6.67*(2*i+1):.2f}" y="0" width="6.67" height="40" fill="#da121a"/>')
        else:
            d.append(f'<rect x="0" y="{4.44*(2*i+1):.2f}" width="60" height="4.44" fill="#da121a"/>')
    return "".join(d)

def castillo(x, y, s, c="#fcdd09"):
    """Castillo de tres torres, silueta."""
    u = s / 6.0
    return (f'<path fill="{c}" d="M{x} {y+6*u}h{6*u}v{-3*u}h{-0.8*u}v{-1.2*u}h{-1.1*u}v{1.2*u}'
            f'h{-1.0*u}v{-1.2*u}h{-1.1*u}v{1.2*u}h{-1.0*u}v{-1.2*u}h{-1.1*u}v{1.2*u}h{-0.8*u}z"/>')

def leon(x, y, s, c="#7b3f98"):
    """León rampante. Silueta hecha a mano: a 14 px de alto el león heráldico
    de verdad se convierte en una mancha, así que va exagerado de melena,
    zarpa y cola, que es lo que lo hace leíble de un vistazo."""
    u = s / 10.0
    def P(*pts): return " ".join(f"{x+a*u:.2f},{y+b*u:.2f}" for a, b in pts)
    return (
      f'<g fill="{c}">'
      # cuerpo: cabeza arriba-izquierda, lomo en diagonal, grupa abajo-derecha
      f'<polygon points="{P((1.3,3.0),(2.6,1.2),(3.5,2.1),(4.9,1.9),(5.2,3.4),(6.8,4.4),(8.0,6.2),(7.7,8.0),(6.3,8.0),(6.6,6.6),(5.2,5.9),(4.6,7.6),(3.2,7.5),(3.6,5.6),(2.4,4.6),(1.1,4.4))}"/>'
      # zarpa delantera levantada
      f'<polygon points="{P((1.1,4.4),(0.2,3.4),(0.6,2.7),(1.9,3.6))}"/>'
      # cola en gancho
      f'<polygon points="{P((7.9,6.6),(9.5,5.0),(9.3,2.6),(10.2,3.2),(10.3,5.6),(8.6,7.4))}"/>'
      f'</g>')

def corona(x, y, s, c="#fcdd09"):
    u = s / 6.0
    return (f'<path fill="{c}" d="M{x} {y+4*u}h{6*u}l{-0.6*u}-{2.6*u}-{1.5*u}{1.2*u}'
            f'-{0.9*u}-{1.8*u}-{0.9*u}{1.8*u}-{1.5*u}-{1.2*u}z"/>')

def estrella(cx, cy, r, c="#fff"):
    import math
    p = []
    for i in range(10):
        ang = -math.pi/2 + i*math.pi/5
        rr = r if i % 2 == 0 else r*0.42
        p.append(f"{cx+rr*math.cos(ang):.2f},{cy+rr*math.sin(ang):.2f}")
    return f'<polygon fill="{c}" points="{" ".join(p)}"/>'

B = {}

B["andalucía"] = ('<rect width="60" height="40" fill="#fff"/>'
    '<rect width="60" height="13.3" fill="#00814f"/><rect y="26.7" width="60" height="13.3" fill="#00814f"/>')

def escudo_aragon(cx, cy, w):
    """Escudo cuartelado, muy reducido. Solo tiene que decir «esta lleva escudo»."""
    h = w * 1.15
    x, y = cx - w/2, cy - h/2
    d = (f'M{x} {y}h{w}v{h*0.55}c0 {h*0.32} {-w*0.22} {h*0.42} {-w/2} {h*0.45}'
         f'c{-w*0.28}-{h*0.03} {-w/2}-{h*0.13} {-w/2}-{h*0.45}z')
    return (f'<path d="{d}" fill="#fff" stroke="#8a6a00" stroke-width=".8"/>'
            f'<clipPath id="esar"><path d="{d}"/></clipPath>'
            f'<g clip-path="url(#esar)">'
            f'<rect x="{x}" y="{y}" width="{w/2}" height="{h/2}" fill="#fcdd09"/>'
            f'<path d="M{x+w*0.18} {y+h*0.06}v{h*0.36}M{x+w*0.06} {y+h*0.24}h{w*0.24}" stroke="#d52b1e" stroke-width="1.1"/>'
            f'<rect x="{x+w/2}" y="{y}" width="{w/2}" height="{h/2}" fill="#0053a5"/>'
            f'<path d="M{x+w*0.75} {y+h*0.06}v{h*0.36}M{x+w*0.63} {y+h*0.24}h{w*0.24}" stroke="#fff" stroke-width="1.1"/>'
            f'<rect x="{x}" y="{y+h/2}" width="{w/2}" height="{h/2}" fill="#fff"/>'
            f'<path d="M{x+w*0.18} {y+h*0.56}v{h*0.36}M{x+w*0.06} {y+h*0.74}h{w*0.24}" stroke="#d52b1e" stroke-width="1.1"/>'
            f'<rect x="{x+w/2}" y="{y+h/2}" width="{w/2}" height="{h/2}" fill="#fcdd09"/>'
            f'<path d="M{x+w*0.60} {y+h/2}v{h/2}M{x+w*0.72} {y+h/2}v{h/2}M{x+w*0.84} {y+h/2}v{h/2}" stroke="#d52b1e" stroke-width="1.6"/>'
            f'</g>')

B["aragón"] = barras() + escudo_aragon(30, 20, 15)

B["asturias"] = ('<rect width="60" height="40" fill="#0072c6"/>'
    '<path fill="#fcdd09" d="M28 8h4v7h9v4h-9v15h-4V19h-9v-4h9z"/>'
    '<path fill="#fcdd09" d="M25.5 15.5l3-4.5 3 4.5z" opacity=".9"/>')

B["baleares"] = (barras() +
    '<path fill="#5c2d91" d="M0 0h26v18H0z"/>' + castillo(8, 4, 11, "#fff"))

B["canarias"] = ('<rect width="20" height="40" fill="#fff"/>'
    '<rect x="20" width="20" height="40" fill="#0053a5"/><rect x="40" width="20" height="40" fill="#fcdd09"/>')

B["cantabria"] = ('<rect width="60" height="20" fill="#fff"/><rect y="20" width="60" height="20" fill="#d52b1e"/>')

B["castilla y león"] = ('<rect width="30" height="20" fill="#d52b1e"/><rect x="30" width="30" height="20" fill="#fff"/>'
    '<rect y="20" width="30" height="20" fill="#fff"/><rect x="30" y="20" width="30" height="20" fill="#d52b1e"/>'
    + castillo(9, 5, 12) + castillo(39, 25, 12) + leon(37, 3, 14) + leon(7, 23, 14))

B["castilla-la mancha"] = ('<rect width="60" height="40" fill="#fff"/><rect width="30" height="40" fill="#d52b1e"/>'
    + castillo(9, 13, 13))

B["cataluña"] = barras()

B["ceuta"] = ('<rect width="60" height="40" fill="#fff"/>'
    '<path fill="#1a1a1a" d="M30 20L0 0h15zM30 20L30 0h15zM30 20L60 0v12zM30 20L60 40H45z'
    'M30 20L30 40H15zM30 20L0 40V28z"/>'
    '<circle cx="30" cy="20" r="6" fill="#fff" stroke="#1a1a1a" stroke-width="1.5"/>')

B["comunidad valenciana"] = (barras() +
    '<rect width="13" height="40" fill="#0053a5"/>' + corona(3.5, 14, 6, "#fcdd09"))

B["extremadura"] = ('<rect width="60" height="13.3" fill="#00814f"/>'
    '<rect y="13.3" width="60" height="13.3" fill="#fff"/><rect y="26.6" width="60" height="13.4" fill="#1a1a1a"/>')

B["galicia"] = ('<rect width="60" height="40" fill="#fff"/>'
    '<path fill="#0053a5" d="M0 4l52 36h8v-4L8 0H0z"/>')

B["la rioja"] = ('<rect width="60" height="10" fill="#d52b1e"/><rect y="10" width="60" height="10" fill="#fff"/>'
    '<rect y="20" width="60" height="10" fill="#00814f"/><rect y="30" width="60" height="10" fill="#fcdd09"/>')

B["madrid"] = ('<rect width="60" height="40" fill="#c1121f"/>'
    + "".join(estrella(12 + i*12, 14, 4) for i in range(4))
    + "".join(estrella(18 + i*12, 28, 4) for i in range(3)))

B["melilla"] = ('<rect width="60" height="40" fill="#aad4f5"/>'
    '<path fill="#fff" stroke="#1a3d6b" stroke-width="1.2" d="M23 9h14v13c0 5-4 8-7 9-3-1-7-4-7-9z"/>'
    '<path fill="#d52b1e" d="M29 12h2v5h5v2h-5v5h-2v-5h-5v-2h5z"/>')

B["murcia"] = ('<rect width="60" height="40" fill="#c1121f"/>'
    + castillo(5, 4, 9) + castillo(16, 4, 9) + castillo(5, 15, 9) + castillo(16, 15, 9)
    + "".join(corona(32 + (i % 4)*7, 16 + (i // 4)*9, 5.5) for i in range(7)))

B["navarra"] = ('<rect width="60" height="40" fill="#d52b1e"/>'
    '<g stroke="#fcdd09" stroke-width="2.2" fill="none">'
    '<circle cx="30" cy="20" r="11"/>'
    '<path d="M30 9v22M19 20h22M22.2 12.2l15.6 15.6M37.8 12.2L22.2 27.8"/></g>'
    '<circle cx="30" cy="20" r="3.4" fill="#00814f" stroke="#fcdd09" stroke-width="1.2"/>')

B["país vasco"] = ('<rect width="60" height="40" fill="#d52b1e"/>'
    '<path stroke="#00814f" stroke-width="7" d="M0 0l60 40M60 0L0 40"/>'
    '<path stroke="#fff" stroke-width="7" d="M30 0v40M0 20h60"/>')

# los dos ids que en el mapa van sin tilde/con guion bajo
ALIAS = {"andalucía":"andalucía", "aragón":"aragón", "país vasco":"país_vasco",
         "castilla y león":"castilla_y_león", "castilla-la mancha":"castilla-la_mancha",
         "comunidad valenciana":"comunidad_valenciana", "la rioja":"la_rioja"}
out = {ALIAS.get(k, k.replace(" ", "_")): v for k, v in B.items()}

json.dump(out, open("out_banderas.json", "w"), ensure_ascii=False, separators=(",", ":"))
import os
print(f"banderas: {len(out)} | {os.path.getsize('out_banderas.json')/1024:.1f} KB")
print("ids:", ", ".join(sorted(out)))

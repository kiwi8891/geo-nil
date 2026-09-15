import json
L=lambda f: json.load(open(f))
ccaa,rios,cord,pts,vec=L("out_ccaa.json"),L("out_rios.json"),L("out_cord.json"),L("out_puntos.json"),L("out_vecinos.json")
p=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="700" viewBox="0 0 1000 700">',
   '<rect width="1000" height="700" fill="#cfe4f2"/>',
   '<g clip-path="url(#c)"><clipPath id="c"><rect width="1000" height="700"/></clipPath>']
for v in vec: p.append(f'<path d="{v["d"]}" fill="#e3e0d6" stroke="#c4bfae" stroke-width="1"/>')
p.append('<rect x="8" y="540" width="322" height="152" fill="#cfe4f2"/>')
for c in ccaa: p.append(f'<path d="{c["d"]}" fill="#f6efdd" stroke="#b9a87e" stroke-width="1"/>')
for c in cord: p.append(f'<path d="{c["d"]}" fill="#a98b5e" fill-opacity=".7" stroke="#7a5f36" stroke-width="1"/>')
for r in rios: p.append(f'<path d="{r["d"]}" fill="none" stroke="#2f7fc4" stroke-width="2.4" stroke-linecap="round"/>')
for c in pts["ciudades"]: p.append(f'<circle cx="{c["x"]}" cy="{c["y"]}" r="3.6" fill="#c0392b"/>')
for a in pts["aguas"]: p.append(f'<circle cx="{a["x"]}" cy="{a["y"]}" r="3.2" fill="#1b5e8a"/>')
p.append('<rect x="8" y="540" width="322" height="152" fill="none" stroke="#8a7a52" stroke-width="1.5" stroke-dasharray="6 4"/></g></svg>')
open("mapa.svg","w").write("\n".join(p))

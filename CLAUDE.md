# GEO NIL — reglas cortas

Juego de geografía para Nil. Contexto completo en `CONTEXTO_PROYECTO.md`. Léelo antes de tocar nada.

## Innegociable
- **Se toca el mapa.** Nunca test de 4 opciones ni arrastrar.
- **El mapa está dibujado pero mudo.** Nunca etiquetas de nombres sobre el mapa.
- **Sin voz.** Nada de TTS. Leer el nombre es parte del ejercicio.
- **Fichero único** `index.html`. No modularizar.
- **JS con comillas dobles siempre** (las simples se corrompen al copiar desde iPhone).
- Nivel 1-2 en MAYÚSCULAS, nivel 3 en minúscula.

## Cómo se regenera
`index.html` se **construye**, no se edita a mano. Fuentes en `datos/`:

```
cd datos
python3 geo.py ciudades.py rios.py cord.py   # capas del mapa (proyección en geo.py)
python3 bundle.py                            # -> out_mapa.json (niveles, artículos)
python3 cromos3.py                           # -> progress.json (reanudable, La Liga)
python3 build.py                             # tpl_*.html + datos -> index.html
```

Editar la app = editar `datos/tpl_*.html` y volver a correr `build.py`.
`tpl_js2.html` es el mapa, `tpl_js3.html` el bucle de juego, `tpl_js4.html` álbum y sobres.

## Gotchas ya pagados
- **TheSportsDB clave gratuita `3`:** `all_leagues.php` y `lookup_league.php` están cerrados.
  `searchteams.php?t=<nombre>` sí funciona y es la vía buena. **La liga id 4335 NO es La Liga**
  (devuelve equipos ingleses) — comprobar siempre `strLeague === "Spanish La Liga"`.
  Tope de **10 jugadores por equipo**. Rate-limita: `cromos3.py` es reanudable a propósito.
- **El SVG no recorta solo:** los vecinos se dibujan adrede fuera del marco, hace falta el
  `<g clip-path>` o salen bandas grises.
- **`align-items:center` en un `.scr`** encoge al `.scroll` y el grid de cromos colapsa.
  Por eso `.scroll` lleva `align-self:stretch`.
- **Todo lo dibujado tiene que ser tocable.** Las CCAA son el mapa base y se ven siempre,
  así que son tocables las 19 aunque el nivel no las pregunte. Si Nil toca algo y no pasa
  nada, no entiende el juego.
- **Overpass se satura:** reintentar en `overpass.kumi.systems` (ver `ov2.py`).
- **Copias de seguridad en iPad:** `<a download>` con `data:` URI **no hace nada** en Safari iOS,
  y menos con la app en la pantalla de inicio. La vía buena es `navigator.share` con un `File`
  (abre la hoja de compartir -> Archivos / Filen / iCloud). Debajo hay escalones: portapapeles,
  textarea a pelo, y descarga con `blob:` para el ordenador. Restaurar admite fichero **y texto
  pegado**, y pide confirmación mostrando qué trae la copia frente a lo que hay.
- No servir el proyecto desde la carpeta sync (Filen bloquea): copiar a `~/tmp/` y servir ahí.
- **`go("home")` a pelo deja la portada congelada:** el contador de monedas y el botón del
  sobre solo se refrescan en `pintarHome()`. Volver a la portada sin repintar hacía que Nil
  ganara monedas y viera un 0 fijo con el sobre desactivado. Usar siempre `irHome()`.

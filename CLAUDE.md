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

## Cambios de la v2 (2026-09-21)
- **Cinco bloques**: las capitales salieron del bloque de comunidades y tienen el suyo.
- **Cinco niveles** en vez de tres (`datos/niveles.py` tiene las tablas, una lista por nivel).
  El estado guardado se migra solo (v1 -> v2: niveles 1,2,3 -> 1,3,5) en `migrar()`.
- **Banderas de las CCAA** dibujadas a mano en `datos/banderas.py` -> `out_banderas.json`,
  horneadas en el HTML. Se usan como pista junto a la pregunta y como premio al acertar;
  nunca se pregunta por ellas.
- **Cromos**: 253 = 233 jugadores (204 con foto) + 1 estadio por equipo. Se amplían tocándolos (`ampliar()`).
- **Tienda**: sobre de 5 al azar (200) o elegir un cromo concreto (500, `S.eco.cromo`).
- **23 ríos** (eran 12).

## Gotchas ya pagados (v2)
- **`go("home")` a pelo deja la portada congelada:** el contador de monedas y el botón del
  sobre solo se refrescan en `pintarHome()`. Volver a la portada sin repintar hacía que Nil
  ganara monedas y viera un 0 fijo con el sobre desactivado. Usar siempre `irHome()`.
- **`lookup_all_players.php` devuelve los 10 primeros POR ORDEN ALFABÉTICO**, no los mejores:
  el Real Madrid salía con Alexis Ciria y sin Mbappé. Las estrellas se piden una a una con
  `searchplayers.php?p=<nombre>` (`datos/estrellas.py`) y solo se aceptan si `strTeam` cuadra.
- **Si la API pone a un jugador en otro club, gana la API.** Lewandowski aparece en Chicago
  Fire y Griezmann en Orlando City: parecen errores y son traspasos reales más recientes que
  lo que sabe el modelo. Forzarlos metería cromos falsos. Sí se acepta el nombre corto
  ("Vallecano" por "Rayo Vallecano"), pero nunca el filial ni el femenino.
- **TheSportsDB tiene mal la liga de 4 equipos:** Girona, Mallorca y Real Oviedo figuran como
  `Spanish La Liga 2`. Filtrar por `strLeague` los tiraba. Ahora se filtra por
  `strCountry == "Spain"` + `strGender == "Male"`, que sí están bien.
- **`searchteams.php?t=Alaves` devuelve el equipo FEMENINO** (Alavés Gloriosas, Liga F).
  El masculino sale buscando "Deportivo Alaves". Por eso `cromos4.py` lleva alias de búsqueda.
- **Los intermedios del mapa ya no están en disco** (`rivers.json`, `out_ccaa.json`, `atlas_ccaa.json`...):
  `geo.py` / `rios.py` / `bundle.py` NO se pueden re-ejecutar. `rios_add.py` y `niveles.py`
  trabajan sobre `out_mapa.json` directamente y son idempotentes.
- **Natural Earth mezcla ríos homónimos:** el Alagón salía repartido por media España porque
  el encadenado pintaba todos los tramos con ese nombre. `trazo()` se queda con el cauce más
  largo y descarta lo que caiga a más de 1,2 grados.
- **Overpass está casi siempre saturado** y `overpass.osm.jp` tiene el certificado roto
  (hostname mismatch). Para ríos, la fuente buena es `ne_10m_rivers_europe` (suplemento
  europeo de Natural Earth): 33 ríos españoles con nombre, un fichero, sin rate limit.
  El global `ne_10m_rivers_lake_centerlines` solo traía 8.

## Modo APRENDER (2026-09-22)
Sección aparte del juego: **sin preguntas, sin monedas y sin fallos**. Se toca cualquier
cosa del mapa (o se busca en la lista de abajo) y sale su ficha: bandera, fotos, dos o tres
frases para leerle en voz alta, un «¿Sabías que...?» y un mini-mapa de dónde cae.
**109 fichas**: 19 comunidades, 20 capitales, 23 ríos, 6 montañas, 20 ciudades, 21 mares e islas.

- Contenido a mano en `datos/atlas_datos.py` (texto y qué sitios fotografiar).
- `datos/atlas.py` baja las fotos de Wikipedia -> `img/` + `out_atlas.json`.
- `datos/optimizar.py` las aprieta con `sips` (nativo de macOS): 33 MB -> 7,5 MB.
- El mapa se comparte con el juego: `dibujarMapa(bloque, activos, {nivel, alTocar})`.

### Gotchas de las fotos (caros, todos)
- **La imagen principal de Wikipedia para una comunidad o ciudad es el ESCUDO, la BANDERA
  o el mapa de situación.** `prop=pageimages` devuelve la imagen de la ficha lateral. La vía
  buena es `page/media-list`, que las da EN EL ORDEN DEL ARTÍCULO: las fotos van detrás.
- **Hay banderas y escudos servidos como .jpg**, con nombre inocente y sin categoría de
  Commons que los delate. Ni el nombre ni las categorías bastan: **el peso sí**. Una bandera
  son colores planos y comprime a 8-15 KB; una foto no baja de 25 KB al mismo ancho
  (`MIN_KB`). Se descarga el candidato, se pesa, y si es un símbolo se prueba el siguiente.
- **`media-list` devuelve HTTP 500** en algunos artículos (Guggenheim, Catedral de Murcia):
  hay respaldo con `prop=images` y, si tampoco, se cambia el título en `atlas_datos.py`.
- **La caché del descargador iba por nombre LOCAL** (`cap-barcelona-1.jpg`): si el script
  elegía otra foto, el nombre no cambiaba y se quedaba la vieja en disco mientras el JSON
  decía otra cosa. Por eso cada foto guarda `src` (su fichero en Commons) y se compara.
- **En zsh, `rm -f img/*.jpg img/*.png` NO BORRA NADA si uno de los dos patrones no casa**
  ("no matches found" aborta el comando entero, y `2>/dev/null` solo silencia el aviso).
  Usar `find img -type f -delete`. Costó tres rondas de revisión mirando fotos viejas.
- Las fotos son de Commons y el repo es público: cada una guarda autor y licencia, y la
  ficha los muestra en pequeño.

## Pendiente
- **Llobregat, Ter, Jarama y Gállego**: no están en Natural Earth y Overpass no respondió.
  `python3 ov3.py Llobregat Ter Jarama Gallego` es reanudable; después `rios_add.py` y
  `niveles.py` (sus nombres ya están en las tablas de nivel 4 y 5).

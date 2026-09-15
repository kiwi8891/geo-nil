# GEO NIL — juego de geografía para Nil

App hermana de `LEER_ESCRIBIR`. Mismo niño (6 años), mismo iPad, mismo patrón:
`index.html` único, JS vanilla, sin build system, publicado en GitHub Pages.

- **Repo:** `kiwi8891/geo-nil` (público, Pages desde `main`)
- **Local:** `Documents/SYNC DOCUMENTS/15_PROYECTOS/JUEGO_GEOGRAFIA/`
- **Definido:** 2026-09-15, en interrogatorio con Ger.

---

## 1. Principios que no se cambian sin preguntar

- **Se toca el mapa.** La pregunta es «toca el EBRO» y Nil toca el río en el mapa SVG.
  No es test de 4 opciones, no es arrastrar etiquetas.
- **El mapa está dibujado pero mudo.** Se ven ríos, chinchetas y fronteras de CCAA,
  nunca los nombres. Es reconocer entre lo que se ve, no recordar sobre un papel vacío.
- **Sin voz.** Igual que en LEER_ESCRIBIR: nada de TTS. Leer «GUADALQUIVIR» es parte
  del ejercicio.
- **Papá fija el nivel**, Nil elige a qué jugar.
- **Fichero único.** No modularizar.

## 2. Alcance

**v1 = solo España, completa.** Europa y Mundo quedan como estructura preparada y vacía;
no se tocan hasta que la v1 esté probada con Nil delante.

## 3. Bloques de contenido (Nil elige uno por ronda)

| Bloque | Qué entra |
|---|---|
| **CCAA** | Las 17 + Ceuta y Melilla, y sus capitales |
| **RÍOS** | Ebro, Tajo, Duero, Guadiana, Guadalquivir, Miño, Júcar, Segura, Turia, Nalón, Genil, Segre, Esla |
| **MONTAÑAS** | **Cordilleras**, no picos (decisión de Ger, 2026-09-15): Pirineos, Cordillera Cantábrica, Sistema Central, Sistema Ibérico, Sierra Morena, Sierra Nevada / Béticas |
| **CIUDADES Y MARES** | Ciudades grandes como chinchetas; mares, golfos, cabos, islas y el Estrecho |

## 4. Mecánica de una ronda

1. Nil elige bloque → **10 preguntas**.
2. «Toca el EBRO» → toca el mapa.
3. **Acierto:** se marca en verde, monedas.
4. **Fallo:** el mapa resalta dónde estaba de verdad, se queda un momento, **y se pasa**.
   No hay segundo intento y la pregunta no reaparece en esa ronda.
5. Pantalla final con monedas ganadas. Puede encadenar rondas.

**Las ciudades** son chinchetas visibles con **zona táctil generosa** alrededor:
se toca la chincheta, no el píxel.

## 5. Qué cambia el nivel (lo fija papá)

1. **Cuántos elementos entran.** Fácil = 5 ríos gordos y 6 CCAA. Difícil = los 13 ríos y las 19 CCAA.
2. **Cuántos distractores se dibujan.** Fácil = solo 4 ríos dibujados en el mapa. Difícil = los 13.
3. **Mayúsculas/minúsculas.** Fácil en MAYÚSCULAS, difícil en minúscula — igual que en
   LEER_ESCRIBIR, donde se premia leer en minúscula.

Papá también activa o desactiva bloques enteros (solo CCAA esta semana, ríos la siguiente).

## 6. Economía y cromos

- Acierto = **10 monedas**. Ronda perfecta = 100.
- **Sobre = 200 monedas** (≈ 2 rondas buenas).
- **Racha de días: x1,5 desde el 3.º**, misma regla que LEER_ESCRIBIR. Nada más de
  gamificación extra.

**El sobre** (decisión delegada en Claude, 2026-09-15):
- **5 cromos**, con **al menos 1 nuevo garantizado** mientras le falten.
- Los **repetidos se convierten solos en monedas**.
- Razón: Ger eligió sobre por azar en vez de tienda (al contrario que en LEER_ESCRIBIR,
  y avisado de ello). La garantía de novedad evita el problema del coleccionista: con
  ~200 cromos y azar puro, los últimos 20 tardarían semanas y el juego se pudre al final.

**El cromo:** foto recortada del jugador + nombre + escudo del equipo + posición + dorsal.

## 7. Datos: de dónde salen (verificado 2026-09-15)

### Cromos — TheSportsDB, clave gratuita `3`
- `lookup_all_teams.php?id=4335` → 24 equipos de La Liga con escudo (`strBadge`).
- `lookup_all_players.php?id=<idTeam>` → plantilla con `strPlayer`, `strPosition`,
  `strNumber`, `idWikidata` y **`strCutout`: PNG del jugador recortado sobre fondo
  transparente**, que es exactamente la figurita de un cromo.
- **Límite real: 10 jugadores por equipo** con la clave gratuita → ~200 cromos. Suficiente.
- **No todos tienen `strCutout`** (9 de 10 en el Barça). Fallback: cromo con escudo grande
  y silueta, mismo patrón de `onerror` que JUEGO_BANDERAS.
- **Se bajan UNA VEZ y se hornea el JSON dentro del `index.html`.** Cero llamadas en
  tiempo de ejecución, cero dependencia de que la API siga viva. Las fotos se sirven
  desde `r2.thesportsdb.com`.
- **Nil es del Real Madrid:** sus cromos salen primero y su página abre el álbum.

### Mapa
- **CCAA:** `https://unpkg.com/es-atlas/es/autonomous_regions.json` — TopoJSON de 37 KB
  con las 20 regiones, Canarias, Ceuta y Melilla incluidas. Se hornea también.
- **Ríos:** Natural Earth (`ne_10m_rivers_lake_centerlines`) solo trae 8 españoles:
  Duero, Ebro, Tajo, Guadiana, Guadalquivir, Miño, Segre y Esla. **Faltan Júcar, Segura,
  Turia, Nalón y Genil** → hay que sacarlos de OpenStreetMap (Overpass, `waterway=river`
  con nombre) y simplificarlos.
- **Cordilleras:** Natural Earth `ne_10m_geography_regions_polys` (`FEATURECLA: Range/mtn`)
  trae como polígonos **Pirineos, Cord. Cantábrica, Sierra Morena y Sierra Nevada**.
  **Sistema Central y Sistema Ibérico no están** → trazados a mano, aproximados, como en
  un mapa escolar.
- **Ciudades:** coordenadas a mano, son pocas y exactas.

## 8. Estética

**Álbum de cromos.** Todo el juego vestido de Panini: brillos, troquelado, y la pantalla
de **abrir el sobre como el momento fuerte** de la app. El mapa es una página más del álbum.

## 9. Técnico

- **iPad, horizontal.** `manifest.json` con `display:standalone` **no es opcional**:
  Safari iOS borra el localStorage de webs normales a los ~7 días, no el de una app
  añadida a la pantalla de inicio.
- Estado en `localStorage`, con **export/import JSON** como LEER_ESCRIBIR.
- **JS siempre con comillas dobles** (gotcha heredado de JUEGO_BANDERAS: las simples se
  corrompían al copiar desde iPhone).
- Imágenes via `createElement`, `onerror` solo en JS y nunca inline en el HTML.

## 10. Abierto / pendiente

- Overpass para los 5 ríos que faltan.
- Trazar a mano Sistema Central y Sistema Ibérico.
- Precio del sobre (200) y monedas por acierto (10) están sin calibrar con uso real.
  La bitácora de uso es la fuente de verdad, igual que en LEER_ESCRIBIR.
- Europa y Mundo: fuera de v1.

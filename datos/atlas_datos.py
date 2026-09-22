# -*- coding: utf-8 -*-
"""Contenido del modo APRENDER: qué se enseña de cada sitio.

No es material de examen: es lo que papá le va contando a Nil mientras miran
fotos. Por eso el texto va en frases cortas y concretas (nada de "nacionalidad
histórica" ni "vertiente mediterránea") y cada sitio lleva un dato de los que
se le quedan a un niño de seis años.

  fotos -> títulos de artículos de Wikipedia en español. De ahí sale la imagen.
  texto -> dos o tres frases para leer en voz alta.
  dato  -> la cosa que se recuerda.
"""

CCAA = {
"galicia": dict(
  fotos=["Catedral de Santiago de Compostela", "Hórreo", "Islas Cíes"],
  texto="Está en la esquina de arriba a la izquierda de España. Casi siempre está verde, "
        "porque llueve muchísimo. El mar se mete dentro de la tierra formando unas entradas "
        "largas que se llaman rías, y de ahí sacan mejillones, almejas y pulpo. "
        "Aquí se habla gallego además de castellano.",
  dato="A Santiago llega gente andando desde muy lejos, a veces durante un mes entero: es el Camino de Santiago."),

"asturias": dict(
  fotos=["Lagos de Covadonga", "Picos de Europa", "Sidra"],
  texto="Es pequeña y está entre montañas muy altas y el mar. Está tan verde como Galicia. "
        "Tiene vacas por todas partes, y de su leche sale la leche que bebemos y muchos quesos. "
        "La bebida de aquí es la sidra, que se echa desde muy alto para que haga espuma.",
  dato="En Asturias hay osos de verdad viviendo en el monte."),

"cantabria": dict(
  fotos=["Cueva de Altamira", "Palacio de la Magdalena", "Santander (España)"],
  texto="Es una comunidad pequeñita en el norte, con playas y montañas muy cerca la una de la otra. "
        "Su capital, Santander, tiene una bahía enorme. Aquí también llueve mucho y está todo verde.",
  dato="En la cueva de Altamira hay bisontes pintados hace más de 14.000 años, por personas de la prehistoria."),

"país_vasco": dict(
  fotos=["Bilbao", "Gaztelugatxe", "San Sebastián"],
  texto="Está en el norte, junto al mar Cantábrico. Aquí se habla euskera, una lengua rarísima "
        "que no se parece a ninguna otra del mundo. Se come muy bien: los pinchos son pequeñas "
        "tapas que se ponen encima de un trozo de pan.",
  dato="En Gaztelugatxe hay una ermita en una isla, y para llegar hay que subir 241 escalones."),

"navarra": dict(
  fotos=["Bardenas Reales", "Selva de Irati", "Sanfermines"],
  texto="Está pegada a Francia, debajo de los Pirineos. Tiene de todo: bosques enormes al norte "
        "y un desierto de tierra al sur que parece otro planeta.",
  dato="En los Sanfermines, en Pamplona, la gente corre por la calle delante de los toros."),

"la_rioja": dict(
  fotos=["Monasterio de Suso", "Viñedo", "Enciso (La Rioja)"],
  texto="Es la comunidad más pequeña de todas las que están en la península. Está llena de viñedos, "
        "que son campos de uvas puestas en filas, y con esas uvas se hace vino.",
  dato="En La Rioja hay miles de huellas de dinosaurio pisadas en la roca, y se pueden ir a ver."),

"aragón": dict(
  fotos=["Basílica de Nuestra Señora del Pilar", "Parque nacional de Ordesa y Monte Perdido", "Albarracín"],
  texto="Es larga y va de los Pirineos, arriba, hasta casi Valencia, abajo. Por el medio pasa el río Ebro, "
        "que es el que más agua lleva de España. Arriba hay montañas con nieve y abajo hace mucho calor.",
  dato="En Teruel encontraron un dinosaurio gigante, y le llamaron Turiasaurus por el río Turia."),

"cataluña": dict(
  fotos=["Templo Expiatorio de la Sagrada Familia", "Montserrat", "Costa Brava"],
  texto="Está en la esquina de arriba a la derecha, junto al mar Mediterráneo. Aquí se habla catalán "
        "además de castellano. Barcelona, su capital, está pegada al mar y tiene edificios "
        "que parecen hechos de plastilina, del arquitecto Gaudí.",
  dato="La Sagrada Familia lleva construyéndose más de 140 años y todavía no está terminada."),

"comunidad_valenciana": dict(
  fotos=["Ciudad de las Artes y las Ciencias", "Fallas", "Paella"],
  texto="Está en la costa del Mediterráneo, con playas larguísimas de arena. Hace bueno casi todo el año. "
        "Aquí se cultivan las naranjas, y de aquí es la paella de verdad.",
  dato="En las Fallas construyen muñecos gigantes de cartón durante todo el año... y luego los queman en una noche."),

"murcia": dict(
  fotos=["Mar Menor", "Teatro romano de Cartagena", "Murcia"],
  texto="Es pequeña, está en el sureste y es de los sitios más secos y calurosos de España. "
        "Aun así está llena de huertas con verduras y frutas, porque riegan con canales. "
        "Le llaman la huerta de Europa.",
  dato="El Mar Menor es un mar pequeño separado del grande por una lengua de arena. El agua está calentita y no cubre casi."),

"andalucía": dict(
  fotos=["Alhambra", "Mezquita-catedral de Córdoba", "Giralda"],
  texto="Es la comunidad más grande y la que tiene más gente. Está abajo del todo, con mar a los dos lados. "
        "Hace mucho calor en verano. Aquí nacieron el flamenco, que se baila dando palmas y taconazos, "
        "y el gazpacho, que es una sopa de tomate fría.",
  dato="Durante 800 años mandaron aquí los musulmanes, y por eso hay palacios como la Alhambra, con patios llenos de fuentes."),

"extremadura": dict(
  fotos=["Teatro romano de Mérida", "Real Monasterio de Santa María de Guadalupe", "Cáceres"],
  texto="Está pegada a Portugal, en el oeste. Tiene unos campos enormes con encinas separadas unas de otras "
        "que se llaman dehesas, y allí viven los cerdos que comen bellotas. De ahí sale el jamón ibérico.",
  dato="En Mérida hay un teatro romano de hace 2.000 años donde todavía se hacen obras de teatro en verano."),

"castilla_y_león": dict(
  fotos=["Acueducto de Segovia", "Catedral de Burgos", "Plaza Mayor de Salamanca"],
  texto="Es la comunidad más grande de toda España y la más llana: son campos de trigo hasta donde llega la vista. "
        "En invierno hace mucho frío. Está llena de castillos y catedrales, y por eso se llama Castilla.",
  dato="El acueducto de Segovia lo hicieron los romanos con piedras encajadas, sin pegamento de ningún tipo. Y ahí sigue."),

"castilla-la_mancha": dict(
  fotos=["Consuegra", "Toledo", "Casas Colgadas"],
  texto="Está justo debajo de Madrid, en el centro. También es muy llana y muy grande, con campos "
        "de cereales y molinos de viento en lo alto de las lomas.",
  dato="Don Quijote, el de los libros, confundió estos molinos con gigantes y se lanzó a atacarlos con una lanza."),

"madrid": dict(
  fotos=["Palacio Real de Madrid", "Puerta de Alcalá", "Museo del Prado"],
  texto="Es pequeña pero es donde vive más gente junta, porque en ella está Madrid, la capital de España. "
        "Está justo en el centro del país. Allí están el Gobierno y el Rey.",
  dato="En la Puerta del Sol hay una placa en el suelo que es el kilómetro 0: desde ahí se miden las carreteras de toda España."),

"baleares": dict(
  fotos=["Catedral de Mallorca", "Cala Macarella", "Ibiza"],
  texto="No está pegada al resto de España: son islas en medio del mar Mediterráneo. Las grandes son "
        "Mallorca, Menorca, Ibiza y Formentera. Para llegar hay que ir en barco o en avión. "
        "Aquí también se habla catalán.",
  dato="Tienen calas escondidas entre rocas con el agua tan transparente que se ven los peces desde arriba."),

"canarias": dict(
  fotos=["Teide", "Dunas de Maspalomas", "Parque nacional de Timanfaya"],
  texto="Son islas, pero están lejísimos: al lado de África, no de España. Por eso allí nunca hace frío, "
        "ni siquiera en invierno. Las islas nacieron de volcanes, y por eso hay playas de arena negra.",
  dato="El Teide es la montaña más alta de España, y desde arriba se ven las otras islas asomando entre las nubes."),

"ceuta": dict(
  fotos=["Murallas Reales de Ceuta", "Ceuta"],
  texto="Es una ciudad muy pequeña y no está en la península: está en África, al otro lado del Estrecho. "
        "Se llega en barco desde Algeciras en menos de una hora.",
  dato="Desde Ceuta se ve España al otro lado del mar, porque el Estrecho solo tiene 14 kilómetros de ancho."),

"melilla": dict(
  fotos=["Melilla la Vieja"],
  texto="Igual que Ceuta: es una ciudad española que está en África, en la costa de Marruecos. "
        "También es muy pequeña y se va en barco o en avión.",
  dato="Melilla está llena de edificios modernistas, con formas curvas y flores en las fachadas. Es la segunda ciudad con más de España, después de Barcelona."),
}


# ---------------------------------------------------------------- montañas
CORD = {
"pirineos": dict(
  fotos=["Pirineos", "Pico Aneto"],
  texto="Es la cordillera que separa España de Francia, de un mar al otro. Son las montañas más "
        "altas que tenemos después de Sierra Nevada, y están nevadas casi todo el año. "
        "Para pasar al otro lado hay que cruzar puertos de montaña o túneles.",
  dato="En los Pirineos todavía viven unos pocos osos pardos, y también rebecos, que son cabras que saltan por las rocas."),

"cordillera_cantábrica": dict(
  fotos=["Cordillera Cantábrica", "Picos de Europa"],
  texto="Va por el norte de España, pegada al mar Cantábrico, desde el País Vasco hasta Galicia. "
        "Hace de pared: las nubes que vienen del mar chocan contra ella y descargan toda el agua, "
        "y por eso el norte está tan verde y el centro tan seco.",
  dato="Los Picos de Europa se llaman así porque eran lo primero que veían los marineros al volver de América."),

"sistema_central": dict(
  fotos=["Sistema Central", "Sierra de Guadarrama"],
  texto="Cruza el centro de España de lado a lado, como un cinturón, y parte la meseta en dos mitades. "
        "Está justo al lado de Madrid: es donde van a esquiar y a ver la nieve.",
  dato="Tiene montañas con nombres de mujer, como la Mujer Muerta, porque desde lejos la silueta parece una persona tumbada."),

"sistema_iberico": dict(
  fotos=["Sistema Ibérico", "Moncayo"],
  texto="Va en diagonal por el este, entre la meseta y el valle del Ebro. Sus montañas no son tan altas, "
        "pero es una zona con muy poca gente: hay pueblos enteros vacíos.",
  dato="En el Sistema Ibérico nacen dos de los ríos más importantes: el Tajo y el Duero."),

"sierra_morena": dict(
  fotos=["Sierra Morena"],
  texto="Separa la meseta de Andalucía, como un escalón largo de lado a lado. No es muy alta, "
        "pero antiguamente era difícil de cruzar y estaba llena de bandoleros.",
  dato="Se llama Morena porque desde lejos se ve oscura, del color de las encinas y los matorrales que la cubren."),

"sierra_nevada": dict(
  fotos=["Sierra Nevada (España)", "Mulhacén"],
  texto="Está en Andalucía, al lado de Granada, y aunque es de los sitios más al sur de España "
        "tiene nieve casi todo el año. Por eso se llama Nevada.",
  dato="En el Mulhacén está el pico más alto de la península, y desde arriba se ve el mar y hasta África."),
}

# ---------------------------------------------------------------- ríos
RIOS = {
"ebro": dict(
  fotos=["Ebro", "Delta del Ebro"],
  texto="Es el río que más agua lleva de España. Nace en Cantabria y cruza todo el noreste hasta "
        "el mar Mediterráneo. Va al revés que casi todos los demás, que van hacia el oeste.",
  dato="Al llegar al mar forma el delta: la tierra que el río ha ido soltando durante miles de años, "
       "tan llana que está llena de arrozales y flamencos."),

"tajo": dict(
  fotos=["Tajo", "Toledo"],
  texto="Es el río más largo de España: nace en Teruel, cruza Madrid, Toledo y Extremadura, "
        "y sigue por Portugal hasta llegar al mar en Lisboa.",
  dato="En Toledo el Tajo rodea la ciudad entera dando una vuelta, como si fuera un foso de castillo."),

"duero": dict(
  fotos=["Duero", "Zamora"],
  texto="Cruza Castilla y León de este a oeste y luego hace de frontera con Portugal, "
        "donde se llama Douro. A su lado crecen viñedos por todas partes.",
  dato="En la frontera con Portugal el río ha excavado unos cortados de piedra altísimos: son los Arribes, y allí vuelan buitres."),

"guadalquivir": dict(
  fotos=["Guadalquivir", "Parque nacional de Doñana"],
  texto="Es el río de Andalucía. Pasa por Córdoba y por Sevilla, y desemboca cerca de Cádiz. "
        "Su nombre viene del árabe y quiere decir río grande.",
  dato="Es el único río de España por el que pueden subir barcos grandes: Sevilla tiene puerto aunque está tierra adentro."),

"guadiana": dict(
  fotos=["Guadiana"],
  texto="Pasa por Castilla-La Mancha y Extremadura, y también hace de frontera con Portugal antes "
        "de llegar al mar. Es un río tranquilo, de tierra llana.",
  dato="Tiene un tramo en el que el río desaparece bajo tierra y vuelve a salir kilómetros después: los llaman los Ojos del Guadiana."),

"mino": dict(
  fotos=["Río Miño"],
  texto="Es el río más importante de Galicia. Nace allí mismo y baja hasta el mar haciendo "
        "de frontera con Portugal en su tramo final.",
  dato="A sus orillas se cultiva la uva del vino albariño, en emparrados altos para que no se pudra con tanta lluvia."),
}

RIOS.update({
"jucar": dict(
  fotos=["Júcar"],
  texto="Baja desde las montañas de Cuenca hasta el mar, en Valencia. Ha ido cortando la roca "
        "y deja hoces, que son curvas muy cerradas entre paredes de piedra.",
  dato="Cuando llueve muchísimo de golpe, el Júcar se desborda: por eso a su paso hay embalses que guardan el agua."),
"segura": dict(
  fotos=["Segura (río)"],
  texto="Es el río de Murcia y Alicante, la zona más seca de España. Con su agua se riegan "
        "huertas enteras de limones, lechugas y melones.",
  dato="Casi toda su agua se usa para regar, así que llega al mar con muy poquita."),
"turia": dict(
  fotos=["Río Turia"],
  texto="Pasa por Teruel y llega a Valencia. Antes cruzaba la ciudad por el medio, "
        "pero lo desviaron después de una riada muy grande.",
  dato="El cauce viejo que quedó vacío dentro de Valencia lo convirtieron en un parque larguísimo con árboles y campos de fútbol."),
"nalon": dict(
  fotos=["Nalón"],
  texto="Es el río más importante de Asturias. Baja desde la montaña hasta el Cantábrico "
        "atravesando valles verdes y pueblos mineros.",
  dato="En sus valles se sacaba carbón de debajo de la tierra durante más de cien años."),
"narcea": dict(
  fotos=["Río Narcea"],
  texto="También es asturiano y se junta con el Nalón. Es famoso por sus salmones.",
  dato="Cada primavera los salmones suben nadando río arriba, contracorriente, para poner sus huevos donde nacieron."),
"genil": dict(
  fotos=["Genil"],
  texto="Nace en la nieve de Sierra Nevada y baja hasta juntarse con el Guadalquivir. "
        "Pasa por Granada.",
  dato="Su agua es nieve derretida: empieza el viaje a más de 3.000 metros de altura."),
"segre": dict(
  fotos=["Segre"],
  texto="Baja de los Pirineos por Lérida y se junta con el Ebro. Es el río más caudaloso "
        "de los que van a parar al Ebro.",
  dato="Pasa por Andorra arriba del todo, así que empieza su camino en otro país."),
"sil": dict(
  fotos=["Sil"],
  texto="Río gallego que se junta con el Miño. Ha excavado un desfiladero tan profundo "
        "que lo llaman la Ribeira Sacra.",
  dato="Hay un dicho en Galicia: «el Miño lleva la fama y el Sil lleva el agua», porque el Sil baja con más."),
"esla": dict(
  fotos=["Esla"],
  texto="Es el afluente más grande del Duero. Cruza León y Zamora por tierras llanas de cereal.",
  dato="Es tan largo que en algunos tramos lleva más agua que el propio Duero antes de juntarse con él."),
"pisuerga": dict(
  fotos=["Pisuerga"],
  texto="Baja desde la montaña de Palencia y pasa por Valladolid antes de entregar su agua al Duero.",
  dato="Hay una frase que se usa en toda España: «meter el Pisuerga por Valladolid», que significa cambiar de tema a lo tonto."),
"tormes": dict(
  fotos=["Tormes"],
  texto="Nace en la sierra de Gredos y pasa por Salamanca, por debajo de su puente romano.",
  dato="En sus orillas empieza el Lazarillo de Tormes, uno de los primeros libros de aventuras escritos en español."),
"cinca": dict(
  fotos=["Cinca"],
  texto="Nace en lo más alto de los Pirineos, en Ordesa, y baja por Huesca hasta el Segre.",
  dato="Nace de una cascada enorme llamada la Cola de Caballo, en el circo de Pineta."),
"jalon": dict(
  fotos=["Río Jalón"],
  texto="Río de Aragón que desemboca en el Ebro. Su valle ha sido siempre el camino "
        "natural para ir de Madrid a Zaragoza.",
  dato="Por su valle pasan la autovía y el tren de alta velocidad, siguiendo el mismo paso que usaban los romanos."),
"henares": dict(
  fotos=["Henares"],
  texto="Pasa por Guadalajara y Alcalá de Henares y se junta con el Jarama, cerca de Madrid.",
  dato="En Alcalá de Henares, a su orilla, nació Cervantes, el que escribió Don Quijote."),
"alberche": dict(
  fotos=["Alberche"],
  texto="Baja de la sierra de Gredos y va a parar al Tajo, al oeste de Madrid.",
  dato="Tiene pozas de agua muy fría entre las rocas donde la gente se baña en verano."),
"mijares": dict(
  fotos=["Río Mijares"],
  texto="Nace en Teruel y llega al Mediterráneo por Castellón, atravesando barrancos.",
  dato="En su recorrido hay pueblos colgados en lo alto de las peñas, puestos ahí para defenderse."),
"cabriel": dict(
  fotos=["Cabriel"],
  texto="Afluente del Júcar. Es uno de los ríos con el agua más limpia de España, "
        "porque pasa por sitios donde casi no vive nadie.",
  dato="Las Hoces del Cabriel son tan bonitas que se han rodado allí películas del Oeste."),
})


# ---------------------------------------------------------------- capitales
CAPITALES = {
"madrid": dict(
  fotos=["Puerta del Sol", "Parque del Buen Retiro"],
  texto="Es la capital de España y la ciudad donde vive más gente del país. Está justo en el centro, "
        "y por eso todas las carreteras y los trenes salen de aquí.",
  dato="En el Retiro hay un palacio hecho entero de cristal, y un estanque donde se puede remar."),
"barcelona": dict(
  fotos=["Barcelona", "Park Güell"],
  texto="Es la capital de Cataluña y la segunda ciudad más grande. Está pegada al mar, "
        "con playa dentro de la ciudad y una montaña, el Tibidabo, con un parque de atracciones arriba.",
  dato="Gaudí llenó la ciudad de casas con formas de animales y bancos de trocitos de azulejo de colores."),
"valencia": dict(
  fotos=["Valencia", "Lonja de la Seda"],
  texto="Capital de la Comunidad Valenciana, junto al Mediterráneo. Tiene un puerto grande, "
        "playas anchas y un barrio antiguo con torres de piedra.",
  dato="Aquí se inventó la paella, y se hace con arroz de la Albufera, una laguna que está al lado."),
"sevilla": dict(
  fotos=["Plaza de España (Sevilla)", "Real Alcázar de Sevilla"],
  texto="Capital de Andalucía, a orillas del Guadalquivir. En verano es de los sitios más calurosos "
        "de Europa: se pasan de 40 grados.",
  dato="De aquí salían los barcos hacia América hace 500 años, y aquí volvían cargados de cosas nuevas como el tomate o el chocolate."),
"zaragoza": dict(
  fotos=["Basílica de Nuestra Señora del Pilar"],
  texto="Capital de Aragón, a orillas del Ebro. Está a medio camino entre Madrid, Barcelona y Bilbao.",
  dato="Sopla un viento tan fuerte llamado cierzo que a veces cuesta andar por la calle."),
"toledo": dict(
  fotos=["Toledo", "Catedral de Toledo"],
  texto="Capital de Castilla-La Mancha, subida en un cerro y rodeada por el río Tajo. "
        "Entera parece un castillo.",
  dato="Aquí convivieron cristianos, musulmanes y judíos, y por eso hay iglesias, mezquitas y sinagogas en las mismas calles."),
"valladolid": dict(
  fotos=["Valladolid"],
  texto="Capital de Castilla y León, en plena meseta, junto al río Pisuerga. "
        "Hace mucho frío en invierno y mucho calor en verano.",
  dato="Fue capital de España durante unos años, antes que Madrid."),
"oviedo": dict(
  fotos=["Oviedo", "Catedral de Oviedo"],
  texto="Capital de Asturias, entre montañas verdes y con el mar cerca. Llueve muy a menudo.",
  dato="A las afueras hay iglesias de hace más de 1.200 años, de las más antiguas que quedan en pie en España."),
"santiago_de_compostela": dict(
  fotos=["Catedral de Santiago de Compostela", "Santiago de Compostela"],
  texto="Capital de Galicia. Es una ciudad de piedra, con soportales para caminar sin mojarse, "
        "porque llueve muchísimo.",
  dato="Es el final del Camino de Santiago: llega gente andando desde Francia, Alemania o más lejos."),
"mérida": dict(
  fotos=["Teatro romano de Mérida", "Puente romano de Mérida"],
  texto="Capital de Extremadura, junto al Guadiana. Es pequeña, pero fue una ciudad romana muy importante.",
  dato="Su puente romano tiene 60 arcos y sigue en pie después de 2.000 años."),
"murcia": dict(
  fotos=["Murcia", "Mar Menor"],
  texto="Capital de la Región de Murcia, en medio de una huerta enorme regada por el Segura.",
  dato="De aquí salen muchísimas de las verduras y frutas que se comen en toda Europa."),
"palma": dict(
  fotos=["Catedral de Mallorca", "Palma de Mallorca"],
  texto="Capital de Baleares, en la isla de Mallorca, con una bahía llena de barcos.",
  dato="Su catedral está pegada al mar y tiene un rosetón gigante llamado el Ojo del Gótico."),
"santander": dict(
  fotos=["Santander (España)", "Palacio de la Magdalena"],
  texto="Capital de Cantabria, en una bahía muy grande. Tiene playas dentro de la propia ciudad.",
  dato="Un incendio quemó casi todo el casco viejo en 1941, así que la ciudad se reconstruyó casi entera."),
"pamplona": dict(
  fotos=["Pamplona", "Sanfermines"],
  texto="Capital de Navarra, rodeada de murallas antiguas que todavía se pueden recorrer andando.",
  dato="Cada julio, en los Sanfermines, sueltan toros por la calle y la gente corre delante de ellos."),
"vitoria": dict(
  fotos=["Vitoria", "Catedral de Santa María de Vitoria"],
  texto="Capital del País Vasco. Es una ciudad muy verde: está rodeada por un anillo de parques.",
  dato="La eligieron Capital Verde Europea por la cantidad de árboles y carriles bici que tiene."),
"logroño": dict(
  fotos=["Logroño"],
  texto="Capital de La Rioja, junto al Ebro y rodeada de viñedos.",
  dato="Tiene una calle, la del Laurel, donde cada bar hace un solo pincho distinto y la gente va probando de uno en uno."),
"las_palmas_de_gran_canaria": dict(
  fotos=["Las Palmas de Gran Canaria", "Playa de Las Canteras"],
  texto="Es una de las dos capitales de Canarias, en la isla de Gran Canaria. "
        "Hace buen tiempo los doce meses del año.",
  dato="Colón paró aquí con sus barcos antes de cruzar el Atlántico hacia América."),
"santa_cruz_de_tenerife": dict(
  fotos=["Santa Cruz de Tenerife", "Auditorio de Tenerife"],
  texto="La otra capital de Canarias, en la isla de Tenerife, con el Teide detrás.",
  dato="Canarias es la única comunidad con dos capitales: se turnan cada cuatro años."),
"ceuta": dict(
  fotos=["Murallas Reales de Ceuta"],
  texto="Es una ciudad española en la costa de África, al otro lado del Estrecho de Gibraltar.",
  dato="Se puede llegar en barco desde Algeciras en menos de una hora."),
"melilla": dict(
  fotos=["Melilla la Vieja"],
  texto="La otra ciudad española en África, en la costa de Marruecos, con una fortaleza junto al mar.",
  dato="Después de Barcelona, es la ciudad con más edificios modernistas de España."),
}


# ---------------------------------------------------------------- otras ciudades
# Una foto cada una: son 20 y con dos se dispara el peso del repo.
CIUDADES = {
"bilbao": dict(fotos=["Bilbao"],
  texto="La ciudad más grande del País Vasco, a orillas de la ría. Antes estaba llena de fábricas "
        "y astilleros, y era gris y sucia; ahora es todo lo contrario.",
  dato="El museo Guggenheim está forrado de titanio y brilla como un pez cuando le da el sol."),
"málaga": dict(fotos=["Málaga"],
  texto="Ciudad andaluza en la Costa del Sol, con playa, palmeras y buen tiempo casi siempre.",
  dato="Aquí nació Picasso, el pintor que dibujaba las caras con los dos ojos del mismo lado."),
"a_coruña": dict(fotos=["Torre de Hércules"],
  texto="Ciudad gallega rodeada de mar por casi todos lados, con playas urbanas y mucho viento.",
  dato="Su faro, la Torre de Hércules, lo construyeron los romanos y sigue encendiéndose cada noche: es el más antiguo del mundo en funcionamiento."),
"vigo": dict(fotos=["Vigo"],
  texto="La ciudad más grande de Galicia, en una ría enorme. Vive del mar y de una fábrica de coches.",
  dato="De su puerto sale más pescado que de casi ningún otro puerto de Europa."),
"gijón": dict(fotos=["Gijón"],
  texto="La ciudad más grande de Asturias, asomada al Cantábrico, con una playa larga en pleno centro.",
  dato="Tiene un barrio de pescadores subido en una península, con casas de colores mirando al mar."),
"alicante": dict(fotos=["Alicante"],
  texto="Ciudad de la costa mediterránea, con un castillo enorme en lo alto de una montaña "
        "justo detrás de la playa.",
  dato="Desde el castillo de Santa Bárbara se ve toda la ciudad y el mar de golpe."),
"córdoba": dict(fotos=["Mezquita-catedral de Córdoba"],
  texto="Ciudad andaluza a orillas del Guadalquivir. Hace muchos siglos fue una de las ciudades "
        "más grandes e importantes del mundo entero.",
  dato="En mayo llena los patios de las casas de macetas con flores y los abre para que entre quien quiera."),
"granada": dict(fotos=["Alhambra"],
  texto="Ciudad andaluza a los pies de Sierra Nevada. Se puede esquiar por la mañana y estar "
        "en la playa por la tarde.",
  dato="En la Alhambra hay un patio con doce leones de piedra sujetando una fuente."),
"salamanca": dict(fotos=["Salamanca"],
  texto="Ciudad de Castilla y León, toda de piedra dorada que brilla al atardecer. "
        "Está llena de estudiantes venidos de todas partes.",
  dato="En la fachada de la universidad hay escondida una rana tallada, y hay que encontrarla."),
"burgos": dict(fotos=["Catedral de Burgos"],
  texto="Ciudad castellana famosa por su catedral y por el frío que hace en invierno.",
  dato="Cerca, en Atapuerca, se encontraron los huesos de los primeros europeos: vivieron hace casi un millón de años."),
"león": dict(fotos=["Catedral de León"],
  texto="Ciudad de Castilla y León, al pie de la montaña. Su catedral es casi toda de cristal.",
  dato="Sus vidrieras tienen 1.800 metros cuadrados de cristal de colores: al entrar parece que llueva luz."),
"cádiz": dict(fotos=["Cádiz"],
  texto="Ciudad andaluza casi rodeada de mar, colgada de una lengua de tierra muy estrecha.",
  dato="Es la ciudad más antigua de Europa occidental: la fundaron los fenicios hace 3.000 años."),
"almería": dict(fotos=["Alcazaba de Almería"],
  texto="Ciudad del sureste, en la zona más seca de España, con una fortaleza árabe enorme.",
  dato="A su lado está el desierto de Tabernas, donde se rodaron muchísimas películas del Oeste."),
"badajoz": dict(fotos=["Badajoz"],
  texto="La ciudad más grande de Extremadura, pegada a la frontera con Portugal.",
  dato="Se puede ir andando a Portugal a comprar el pan."),
"tarragona": dict(fotos=["Tarragona"],
  texto="Ciudad catalana junto al Mediterráneo, llena de ruinas romanas.",
  dato="Su anfiteatro está justo al lado del mar: los gladiadores luchaban con las olas de fondo."),
"girona": dict(fotos=["Gerona"],
  texto="Ciudad catalana con casas de colores asomadas al río y una muralla que se recorre por arriba.",
  dato="Algunas escenas de Juego de Tronos se rodaron en sus escaleras de la catedral."),
"huesca": dict(fotos=["Huesca"],
  texto="Ciudad aragonesa pequeña, a los pies de los Pirineos.",
  dato="Es la puerta de entrada a Ordesa, uno de los parques nacionales más antiguos de España."),
"cuenca": dict(fotos=["Casas Colgadas"],
  texto="Ciudad de Castilla-La Mancha construida en lo alto de una peña, entre dos ríos "
        "que han excavado barrancos a los lados.",
  dato="Tiene casas colgadas literalmente del borde del precipicio, con balcones de madera sobre el vacío."),
"albacete": dict(fotos=["Albacete"],
  texto="Ciudad manchega en medio de una llanura enorme. Muy fría en invierno y muy calurosa en verano.",
  dato="Es famosa por sus navajas, que se fabrican allí desde hace siglos."),
"cáceres": dict(fotos=["Cáceres"],
  texto="Ciudad extremeña con un casco antiguo de piedra que no ha cambiado en 500 años.",
  dato="En sus torres anidan cigüeñas: se ven los nidos enormes desde la plaza."),
}

# ---------------------------------------------------------------- mares, islas y costas
AGUAS = {
"mar_mediterraneo": dict(fotos=["Mar Mediterráneo"],
  texto="Es el mar que baña toda la costa este y sur de España. Es cálido, tranquilo y muy salado, "
        "porque está casi cerrado por tierra.",
  dato="Solo se conecta con el océano por el Estrecho de Gibraltar, que es estrechísimo."),
"oceano_atlantico": dict(fotos=["Océano Atlántico"],
  texto="Es el océano que hay al oeste, entre España y América. Es muchísimo más grande y frío "
        "que el Mediterráneo, y tiene olas mucho mayores.",
  dato="Colón lo cruzó en 1492 con tres barcos, y tardó más de dos meses en llegar a América."),
"mar_cantabrico": dict(fotos=["Mar Cantábrico"],
  texto="Es el mar del norte de España. Es frío, bravo y con muchas olas, y de él sale "
        "gran parte del pescado que se come en el país.",
  dato="Sus olas son tan buenas que vienen surfistas de todo el mundo a cogerlas."),
"estrecho_de_gibraltar": dict(fotos=["Estrecho de Gibraltar"],
  texto="Es el paso estrecho que separa Europa de África y une el Mediterráneo con el Atlántico. "
        "Desde España se ve Marruecos a simple vista.",
  dato="Solo mide 14 kilómetros de ancho en su punto más corto: se puede cruzar a nado."),
"golfo_de_vizcaya": dict(fotos=["Golfo de Vizcaya"],
  texto="Es la gran curva de mar entre el norte de España y Francia. Tiene fama de bravo "
        "y de dar tormentas fuertes.",
  dato="Por aquí pasan las ballenas en sus viajes, y a veces se ven desde los barcos."),
"golfo_de_cadiz": dict(fotos=["Golfo de Cádiz"],
  texto="Es la curva de costa del suroeste, entre Portugal y el Estrecho, ya en el Atlántico. "
        "Tiene playas larguísimas de arena fina.",
  dato="De aquí salen los atunes que se pescan con una técnica de hace 3.000 años llamada almadraba."),
"golfo_de_valencia": dict(fotos=["Golfo de Valencia"],
  texto="Es la curva de la costa mediterránea a la altura de Valencia, de aguas tranquilas y poco profundas.",
  dato="Sus playas son tan llanas que puedes andar muchos metros mar adentro sin que te cubra."),
"cabo_de_gata": dict(fotos=["Cabo de Gata"],
  texto="Es una punta de tierra en Almería, de roca volcánica, con calas escondidas y casi sin casas.",
  dato="Es el lugar más seco de toda Europa: hay años en que casi no llueve nada."),
"cabo_finisterre": dict(fotos=["Cabo Finisterre"],
  texto="Es una punta de Galicia asomada al Atlántico. Su nombre significa fin de la tierra.",
  dato="Los romanos creían que aquí se acababa el mundo y que más allá no había nada."),
"cabo_de_creus": dict(fotos=["Cabo de Creus"],
  texto="Es la punta más al este de la península, en Girona, con rocas retorcidas por el viento.",
  dato="Es el primer sitio de España donde amanece cada día."),
"cabo_de_palos": dict(fotos=["Cabo de Palos"],
  texto="Punta rocosa de Murcia con un faro muy alto, junto al Mar Menor.",
  dato="Debajo del agua hay barcos hundidos, y la gente bucea para verlos."),
"islas_baleares": dict(fotos=["Islas Baleares"],
  texto="Son las islas españolas del Mediterráneo: Mallorca, Menorca, Ibiza y Formentera.",
  dato="Se puede ir de una a otra en barco en un rato, y desde Ibiza se ve Formentera."),
"islas_canarias": dict(fotos=["Islas Canarias"],
  texto="Son ocho islas en el Atlántico, frente a África. Nacieron todas de volcanes.",
  dato="Están tan al sur que allí crecen plátanos, que no crecen en ningún otro sitio de España."),
"mallorca": dict(fotos=["Mallorca"],
  texto="Es la isla más grande de Baleares, con una sierra de montañas al norte y calas al sur.",
  dato="Su sierra de Tramuntana está llena de muros de piedra puestos a mano, uno a uno, hace siglos."),
"menorca": dict(fotos=["Menorca"],
  texto="La segunda isla de Baleares, más tranquila y más llana que Mallorca.",
  dato="Está llena de construcciones de piedra prehistóricas llamadas talayots, de hace más de 3.000 años."),
"ibiza": dict(fotos=["Ibiza"],
  texto="Isla de Baleares famosa por sus calas de agua transparente y por su música.",
  dato="Frente a su costa hay una roca enorme saliendo del mar, Es Vedrà, de 400 metros de alto."),
"tenerife": dict(fotos=["Tenerife"],
  texto="La isla más grande de Canarias, con el Teide en el centro.",
  dato="En un mismo día puedes estar en la playa y luego subir a ver nieve en el Teide."),
"gran_canaria": dict(fotos=["Gran Canaria"],
  texto="Isla canaria muy variada: tiene playas, montañas, bosques y hasta un desierto de dunas.",
  dato="Le llaman continente en miniatura porque cabe de todo en una isla redonda y pequeña."),
"lanzarote": dict(fotos=["Lanzarote"],
  texto="Isla canaria con paisaje de volcanes, tierra negra y casi nada de vegetación. Parece la Luna.",
  dato="En Timanfaya el suelo está tan caliente a pocos metros de profundidad que asan carne con el calor de la tierra."),
"fuerteventura": dict(fotos=["Fuerteventura"],
  texto="Isla canaria llana y con playas de arena blanquísima y mucho viento.",
  dato="Es la isla más antigua de Canarias: su volcán se apagó hace millones de años."),
"la_palma": dict(fotos=["La Palma"],
  texto="Isla canaria muy verde y montañosa, con volcanes todavía vivos.",
  dato="En 2021 entró en erupción un volcán durante casi tres meses. Y su cielo es tan limpio que hay telescopios gigantes para mirar las estrellas."),
}

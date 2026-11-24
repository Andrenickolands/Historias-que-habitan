# Copy deck del inicio

Historias que Habitan · Versión 3 · 19/11/2026 · Estado: propuesta, sin validar con usuarios ni con el negocio.

Esta versión sigue el orden de 14 secciones aprobado por el negocio (`docs/estructura-inicio.md`) y el wireframe `prototipos/inicio-estructura.html`. Reemplaza a la versión 1, que tenía 22 secciones y el hero de la lámpara. El 19/11/2026 se agregó la sección 3 de testimonios y «Nosotros» y «Lo que se pregunta antes de comprar» pasaron a compartir franja (hoy la 8): en escritorio, lado a lado con un divisorio; cada una conserva sus textos. Después entró «Lo nuevo» en la 3, tras las categorías.

Lo que está entre corchetes falta confirmarlo con el negocio. Nada de este documento es una cifra, una reseña o una promoción real.

## 0. Entorno (Paso 0)

| Revisión | Resultado |
|---|---|
| Perfiles | diseno, marketing, seo y scroll activos. Desarrollo: `ecc` y `superpowers` disponibles. |
| Skills del prompt | Todas disponibles. Dos cambian de nombre: `vercel:vercel-react-best-practices` se llama `vercel:react-best-practices` y `vercel:next-best-practices` se llama `vercel:nextjs`. |
| Skills cargadas en esta fase | `/marketing-skills:copywriting` → diagnóstico, prueba de las tres preguntas, CTA con verbo y objeto, sin muletillas de IA. `/marketing-skills:cro` → una acción principal por pantalla, objeciones antes del cierre. |
| Proyecto | Prototipos en HTML estático generados con Python (`herramientas/`). No hay `package.json`, `components.json`, Tailwind, TypeScript, alias `@/` ni `lib/utils.ts`. |
| Plataforma | Sigue abierta: Shopify o Next.js a medida (`docs/arquitectura-informacion.md` §9 y `docs/handoff-desarrollo.md` §1). El prompt asume Next.js + TypeScript + Tailwind + shadcn. |

**Entorno listo** para mensaje, copy y diseño. Para el código que pide el prompt (`ShoppableGallery`, `CategoryShowcase` y el resto en React) falta decidir la plataforma.

## 1. Las referencias del zip

Un video de 14 s y tres capturas de redes sociales con cuatro sitios de otros estudios: uno de interiorismo, una app de decoración, una tienda de muebles y una tienda de objetos de cerámica. Son trabajo ajeno: de ahí salen principios, no imágenes, nombres, textos ni composición.

| Se toma | Se deja |
|---|---|
| Hero a todo el ancho con un espacio cálido y un titular grande en serif | La palabra «luxury»: el manual prohíbe «lujo» |
| Tarjeta flotante con el producto y su precio sobre la foto | Las cifras «10+ años, 98 % satisfechos, 50K+ clientes»: no hay datos reales |
| Colecciones en mosaico: una pieza grande y varias pequeñas | El tuteo de los textos de ejemplo |
| Sugerencias de búsqueda en fichas («Jarrones», «Copas») | El fondo oscuro de toda la página: la paleta de la marca es clara |
| Banda final a todo el ancho con un CTA | |
| Preguntas frecuentes antes del cierre | |

## 2. Supuestos

- **Siete categorías, no seis.** El prompt pide máximo seis; con siete los arcos de la sección 2 quedan completos y no hay que esconder una.
- **No hay fotos ni modelos 3D.** El wireframe usa dibujos y marcadores `[FOTO …]`. El giro del hero necesita 24 fotos de la escultura real.
- **La pieza del hero es la Escultura curva blanca** ($179.900) [POR CONFIRMAR con el negocio]: se arma por capas, se posa en su base y gira.
- **«Más vendidos» se llama «Piezas de la selección»** hasta que haya datos de ventas.
- **Las reseñas de la sección 4 son de ejemplo** para el diseño, igual que en la ficha. La sección se publica solo con reseñas reales y con permiso. En el inicio se muestran solo reseñas de 3 estrellas o más (`MIN_ESTRELLAS` en `herramientas/inicio_secciones.py`), y entre ellas va al menos una de 3 y una de 4, porque una página con solo cinco estrellas genera menos confianza. Las de 1 y 2 no se esconden: siguen en la ficha de cada pieza, con la respuesta de la tienda. Por eso el texto de apoyo ya no dice «Publicamos las reseñas como llegan».
- **Espacios:** sala, comedor, alcoba y entrada, para el camino «Busco ideas para mi casa». Pide un campo «espacio» en cada pieza [POR CONFIRMAR].
- **Usted en todo.** Los ejemplos del prompt vienen en tú; aquí «Baje para verla armarse y girar», «Mírela de cerca».
- **Navidad:** se puede pedir cualquier día, sin fecha de corte. Ningún texto promete entrega antes del 24 de diciembre; el tiempo por ciudad se ve antes de pagar.
- **Descuentos (arco 4 de la sección 6 y página `descuentos.html`):** solo descuentos reales, con el precio anterior verificable y sus fechas [POR CONFIRMAR: regla del precio anterior]. El cuestionario ya no está en la sección 6; sigue en el botón «Ayúdeme a elegir» del hero.
- **Retracto:** el inicio no fija días. El plazo lo definen la página legal y el aviso antes de pagar.
- **Envío gratis desde $300.000** y **medios de pago** (tarjeta, PSE, Nequi, Daviplata) siguen [POR CONFIRMAR], igual que en la ficha y en Preguntas.

## 3. Estrategia en 5 líneas

1. **A quién:** personas en Colombia, sobre todo en Bogotá, que arman o renuevan su casa, reciben visitas o buscan un regalo que se guarde. Compran desde el celular [HIPÓTESIS A VALIDAR].
2. **Qué las frena:** comprar una pieza frágil sin verla. No saben cómo es de verdad, de qué tamaño, ni si llegará entera.
3. **Qué deben sentir:** que ven la pieza puesta en una casa como la suya y saben de qué está hecha y por qué se eligió.
4. **Qué deben hacer:** entrar en un toque a una categoría, una colección o un espacio, o tocar un punto de la foto e ir a la ficha.
5. **Por qué aquí:** cada pieza viene contada en tres niveles (hecho, diseño e historia) y nada se inventa.

## 4. Hero

| | A · Elegida | B · Para la prueba |
|---|---|---|
| H1 | Piezas que se miran desde todos sus lados | Sepa cómo es la pieza antes de comprarla |
| Subtítulo | Esculturas, porcelanas, jarrones y lámparas para su casa. De cada pieza le contamos material, medidas y origen. | El mismo |
| CTA principal | Ver todas las piezas (a la tienda) | Ver todas las piezas (a la tienda) |
| CTA secundario | Ayúdeme a elegir | Ayúdeme a elegir |
| Movimiento | La Escultura curva blanca se arma por capas, se posa en su base mientras aparece la sala y gira sobre sí misma | El mismo |

**Por qué A.** El titular dice lo que el movimiento muestra: la escultura gira y se ve por todos sus lados. El subtítulo dice qué se vende y qué distingue a la tienda.

**El botón principal lleva a la tienda** («Ver todas las piezas», a `tienda.html`), no a una sola pieza: quien llega al inicio todavía está mirando. La escultura tiene su propia etiqueta en la escena, «Escultura curva blanca · $179.900», que lleva a su ficha sin competir con el botón.

**Prueba A/B:** A contra B con el mismo movimiento. B responde al miedo de comprar algo frágil sin verlo, y el giro le da la prueba. Métrica principal: clics en «Ver todas las piezas» sobre sesiones. Secundaria: piezas agregadas al carrito desde el inicio. Control: rebote. El tamaño de muestra depende del tráfico mensual [POR CONFIRMAR].

**Qué pasó con las variantes anteriores.** La A de la lámpara («La mesa puesta y la luz encendida») salió cuando la lámpara dejó el hero. La C de Navidad («Regalos que se guardan, para esta Navidad») ya no es hero: es la sección 5 y cambia con cada temporada. Las tres siguen en `prototipos/inicio-variantes.html` como referencia.

El antetítulo del manual («Hay objetos que no solo decoran. Cuentan historias.») va arriba del H1. Su estructura («no solo… sino…») es la que la skill de copy pide evitar, pero es el lema del manual y no se cambia aquí.

## 5. Copy deck

Orden propuesto del inicio. Los caracteres no cuentan lo que está entre corchetes. ⚠ marca un texto que pasa su límite de palabras.

| Sección | Elemento | Copy | Caracteres | Intención | Variante A/B |
|---|---|---|---|---|---|
| Global · Anuncio y cabecera | Barra de anuncio | Envío gratis en pedidos desde $300.000 [POR CONFIRMAR: monto y cobertura] | 38 | actuar | A |
| Global · Anuncio y cabecera | Barra de anuncio (si no hay envío gratis) | Enviamos a todo el país, con embalaje para piezas frágiles | 58 | confiar | B |
| Global · Anuncio y cabecera | Buscador: etiqueta | Buscar en la tienda | 19 | actuar | — |
| Global · Anuncio y cabecera | Buscador: texto de ejemplo | Buscar jarrones, copas, lámparas… | 33 | actuar | — |
| Global · Modal de bienvenida (variante D) | Antetítulo | Boletín | 7 | atrapar | — |
| Global · Modal de bienvenida (variante D) | H2 | Nuevas piezas y nuevas ofertas | 30 | atrapar | — |
| Global · Modal de bienvenida (variante D) | Línea | Suscríbase y entérese de todo. Le avisamos sobre ofertas exclusivas y nuestros nuevos productos. | 96 | desear | — |
| Global · Modal de bienvenida (variante D) | Ayuda del celular | Diez dígitos. Por ahí le avisamos por WhatsApp. | 47 | confiar | — |
| Global · Modal de bienvenida (variante D) | Ayuda de la empresa (opcional) | Si compra para un negocio, le contamos también sobre los precios al por mayor. | 78 | confiar | — |
| Global · Modal de bienvenida (variante D) | Casilla de datos | Autorizo el tratamiento de mis datos para recibir novedades y ofertas por correo y WhatsApp, según la política de privacidad. | 125 | confiar | — |
| Global · Modal de bienvenida (variante D) | Botón principal | Sí, quiero suscribirme | 22 | actuar | — |
| Global · Modal de bienvenida (variante D) | Botón secundario (grande, con borde) | Por el momento no | 17 | actuar | — |
| Global · Modal de bienvenida (variante D) | Letra chica | Puede darse de baja cuando quiera, desde cualquier correo. | 58 | confiar | — |
| Global · Modal de bienvenida (variante D) | Confirmación | Listo, le avisaremos. Le escribiremos a [correo] y por WhatsApp al [celular] cuando lleguen piezas nuevas o haya ofertas. | 104 | confiar | — |
| 1 · Hero 3D | Antetítulo (manual de marca) | Hay objetos que no solo decoran. Cuentan historias. | 51 | atrapar | — |
| 1 · Hero 3D | H1 | Piezas que se miran desde todos sus lados | 41 | atrapar | A (elegida) |
| 1 · Hero 3D | H1 | Sepa cómo es la pieza antes de comprarla | 40 | confiar | B (prueba) |
| 1 · Hero 3D | Subtítulo | Esculturas, porcelanas, jarrones y lámparas para su casa. De cada pieza le contamos material, medidas y origen. | 111 | desear | A y B |
| 1 · Hero 3D | CTA principal (lleva a la tienda) | Ver todas las piezas | 20 | actuar | — |
| 1 · Hero 3D | Etiqueta de la pieza en la escena | Escultura curva blanca · $179.900 | 33 | desear | — |
| 1 · Hero 3D | CTA secundario | Ayúdeme a elegir | 16 | actuar | — |
| 1 · Hero 3D | Pista (escritorio) | Baje para verla armarse y girar | 31 | atrapar | — |
| 1 · Hero 3D | Nombre accesible de la escena | Escultura curva blanca sobre un pedestal, en una sala con luz de tarde | 70 | confiar | — |
| 2 · Categorías por tipo (arcos) | H2 | Elija por tipo de pieza | 23 | actuar | — |
| 2 · Categorías por tipo (arcos) | Apoyo | Siete categorías, de la porcelana a las lámparas. Cada pieza tiene su ficha con material, medidas y origen. | 107 | confiar | — |
| 2 · Categorías por tipo (arcos) | Porcelanas y figuras: línea | Figuras y piezas para la repisa | 31 | desear | — |
| 2 · Categorías por tipo (arcos) | Porcelanas y figuras: CTA | Ver porcelanas | 14 | actuar | — |
| 2 · Categorías por tipo (arcos) | Jarrones y recipientes: línea | Para flores, ramas o solos | 26 | desear | — |
| 2 · Categorías por tipo (arcos) | Jarrones y recipientes: CTA | Ver jarrones | 12 | actuar | — |
| 2 · Categorías por tipo (arcos) | Flores artificiales: línea | Ramos que no se marchitan | 25 | desear | — |
| 2 · Categorías por tipo (arcos) | Flores artificiales: CTA | Ver flores | 10 | actuar | — |
| 2 · Categorías por tipo (arcos) | Mesa: línea | Vajillas, copas y accesorios para servir | 40 | desear | — |
| 2 · Categorías por tipo (arcos) | Mesa: CTA | Ver la mesa | 11 | actuar | — |
| 2 · Categorías por tipo (arcos) | Centros de mesa: línea | Para el centro del comedor | 26 | desear | — |
| 2 · Categorías por tipo (arcos) | Centros de mesa: CTA | Ver centros de mesa | 19 | actuar | — |
| 2 · Categorías por tipo (arcos) | Esculturas pequeñas: línea | Formas para la mesa de centro | 29 | desear | — |
| 2 · Categorías por tipo (arcos) | Esculturas pequeñas: CTA | Ver esculturas | 14 | actuar | — |
| 2 · Categorías por tipo (arcos) | Decoraciones del hogar: línea | Lámparas y objetos para cada rincón | 35 | desear | — |
| 2 · Categorías por tipo (arcos) | Decoraciones del hogar: CTA | Ver decoración | 14 | actuar | — |
| 2 · Categorías por tipo (arcos) | Botón al pie (centrado, lleva a la tienda) | Ver todo | 8 | actuar | — |
| 3 · Lo nuevo | H2 | Lo nuevo | 8 | desear | — |
| 3 · Lo nuevo | Apoyo | Las piezas que acaban de llegar a la tienda. [POR CONFIRMAR: cada cuánto llegan piezas nuevas] | 44 | desear | — |
| 3 · Lo nuevo | Botón sobre la foto (lleva a Lo nuevo) | Lo quiero todo | 14 | actuar | — |
| 3 · Lo nuevo | Tarjeta de cada pieza (4, las más recientes) | [Nombre de la pieza] · [Precio]. Oferta y «Quedan pocas» salen del catálogo | 46 | desear | — |
| 4 · Testimonios (nueva) | H2 | Lo que dicen quienes ya compraron | 33 | confiar | — |
| 4 · Testimonios (nueva) | Apoyo | Una muestra de lo que dicen quienes ya compraron. En la ficha de cada pieza están todas sus reseñas. [POR CONFIRMAR: política de reseñas] | 100 | confiar | — |
| 4 · Testimonios (nueva) | Botón | Pausar las reseñas | 18 | confiar | — |
| 4 · Testimonios (nueva) | Botón en pausa | Reanudar las reseñas | 20 | confiar | — |
| 4 · Testimonios (nueva) | Aviso del prototipo | [Reseñas de ejemplo para el diseño. Esta sección se publica solo con reseñas reales y con permiso de quien las escribe.] | 0 | confiar | — |
| 4 · Testimonios (nueva) | Reseña de ejemplo · 5 estrellas | Llegó entera y bien empacada. Pedí el jarrón con asas para Medellín. Venía en caja, con papel de seda, y es igual al de la foto. | 128 | confiar | — |
| 4 · Testimonios (nueva) | Reseña de ejemplo · 5 estrellas | La mesa quedó lista para la visita. Compré la vajilla blanca y las copas. Combinan entre sí y no tuve que buscar nada más. | 122 | desear | — |
| 4 · Testimonios (nueva) | Reseña de ejemplo · 3 estrellas | Una copa llegó despicada. La caja venía golpeada y una de las seis copas tenía el borde despicado. Me la cambiaron, pero tardó más de lo que esperaba. | 150 | confiar | — |
| 4 · Testimonios (nueva) | Respuesta de la tienda (reseñas de 3 o menos) | [RESPUESTA REAL PENDIENTE] | 0 | confiar | — |
| 4 · Testimonios (nueva) | Regla | En el inicio, solo reseñas de 3 estrellas o más. Las de 1 y 2 siguen en la ficha de cada pieza. | 95 | confiar | — |
| 4 · Testimonios (nueva) | Reseña de ejemplo · 4 estrellas | Bonita, más pequeña de lo que imaginé. La escultura es preciosa, pero la imaginaba más grande. Las medidas estaban en la ficha; debí mirarlas mejor. | 148 | confiar | — |
| 4 · Testimonios (nueva) | Reseña de ejemplo · 5 estrellas | Llegó bien hasta Pereira. La mandé directo a la casa de mi mamá como regalo de Navidad y le llegó bien embalada. | 112 | confiar | — |
| 4 · Testimonios (nueva) | Reseña de ejemplo · 5 estrellas | Nadie cree que sean de tela. Llevo meses con el ramo en la entrada y sigue igual. Todos preguntan si son naturales. | 115 | desear | — |
| 4 · Testimonios (nueva) | Firma de cada reseña | [Nombre e inicial del apellido] · [ciudad] · [pieza, con enlace a su ficha] | 4 | confiar | — |
| 5 · Temporada | Antetítulo | Temporada de Navidad | 20 | atrapar | — |
| 5 · Temporada | H2 | Regalos que se guardan, para esta Navidad | 41 | atrapar | — |
| 5 · Temporada | Apoyo | Porcelanas, cristalería y figuras para regalar, embaladas para viajar. Envíos a todo el país. | 93 | desear | — |
| 5 · Temporada | Presupuestos | Hasta $100.000 · De $100.000 a $250.000 · Más de $250.000 | 57 | actuar | — |
| 5 · Temporada | CTA | Encontrar un regalo | 19 | actuar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | H2 | ¿Qué lo trae hoy? | 17 | actuar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | Apoyo | Elija por dónde empezar. | 24 | actuar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | Arco: antetítulo | Inspiración | 11 | atrapar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | Arco: título | Busco ideas para mi casa | 24 | atrapar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | Arco: línea | Sala, comedor, alcoba o entrada | 31 | confiar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | Arco: CTA | Ver ideas por espacio | 21 | actuar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | Arco: antetítulo | Búsqueda | 8 | atrapar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | Arco: título | Ya sé qué pieza quiero | 22 | atrapar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | Arco: línea | Búsquela por su nombre | 22 | confiar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | Arco: CTA | Buscar una pieza | 16 | actuar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | Arco: antetítulo | Regalos | 7 | atrapar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | Arco: título | Busco un regalo | 15 | atrapar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | Arco: línea | Por ocasión o por presupuesto | 29 | confiar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | Arco: CTA | Ver regalos | 11 | actuar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | Arco: antetítulo | Descuentos | 10 | atrapar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | Arco: título | Busco descuentos | 16 | atrapar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | Arco: línea | Piezas rebajadas, con el precio anterior a la vista | 51 | confiar | — |
| 6 · ¿Qué lo trae hoy? (arcos con foto) | Arco: CTA | Ver descuentos | 14 | actuar | — |
| 7 · Galería de colecciones | H2 | Mire cada colección puesta en casa | 34 | desear | — |
| 7 · Galería de colecciones | Apoyo | Toque una pieza de la foto para ver su precio y abrir su ficha. | 63 | actuar | — |
| 7 · Galería de colecciones | Franja cerrada (escritorio) | [Nombre de la colección] | 0 | actuar | — |
| 7 · Galería de colecciones | Punto: nombre accesible | Ver [nombre de la pieza], [precio] | 5 | actuar | — |
| 7 · Galería de colecciones | Tarjeta del punto: CTA | Ver la pieza | 12 | actuar | — |
| 7 · Galería de colecciones | Lista bajo la foto (celular) | [n] piezas en esta foto | 19 | confiar | — |
| 7 · Galería de colecciones | La mesa que recibe | Vajillas, cristalería y centros de mesa que funcionan juntos, para cuando llega visita. | 87 | desear | — |
| 7 · Galería de colecciones | CTA | Ver La mesa que recibe | 22 | actuar | — |
| 7 · Galería de colecciones | Primer hogar | Pocas piezas que combinan, para empezar una casa sin comprarlo todo de una vez. | 79 | desear | — |
| 7 · Galería de colecciones | CTA | Ver Primer hogar | 16 | actuar | — |
| 7 · Galería de colecciones | Regalos que se guardan | Para bodas, inauguraciones y fechas especiales, con medidas y material a la vista. | 82 | desear | — |
| 7 · Galería de colecciones | CTA | Ver regalos | 11 | actuar | — |
| 7 · Galería de colecciones | Piezas protagonistas | Las piezas de mayor presencia, las que se ven al entrar a una sala. | 67 | desear | — |
| 7 · Galería de colecciones | CTA | Ver las protagonistas | 21 | actuar | — |
| 8 · Nosotros y lo que se pregunta | Izquierda · H2 | Cómo contamos cada pieza | 24 | confiar | — |
| 8 · Nosotros y lo que se pregunta | Izquierda · Apoyo | Separamos lo que se puede comprobar, nuestra lectura del diseño y un lugar posible en su casa. | 94 | confiar | — |
| 8 · Nosotros y lo que se pregunta | Izquierda · Hecho | Material, medidas y origen. | 27 | confiar | — |
| 8 · Nosotros y lo que se pregunta | Izquierda · Diseño | Nuestra lectura de su forma y su estilo. | 40 | confiar | — |
| 8 · Nosotros y lo que se pregunta | Izquierda · Historia | Un lugar posible para ella en su casa. | 38 | desear | — |
| 8 · Nosotros y lo que se pregunta | Izquierda · Texto de marca | [TEXTO PENDIENTE en la voz de Paula Heredia] | 0 | confiar | — |
| 8 · Nosotros y lo que se pregunta | Izquierda · CTA | Conocer la marca | 16 | confiar | — |
| 8 · Nosotros y lo que se pregunta | Derecha · H2 | Lo que se pregunta antes de comprar | 35 | confiar | — |
| 8 · Nosotros y lo que se pregunta | Derecha · Duda 1 | ¿Será como en la foto? | 22 | confiar | — |
| 8 · Nosotros y lo que se pregunta | Derecha · Respuesta 1 | Cada ficha trae medidas, material, origen y fotos de la pieza en una casa. | 74 | confiar | — |
| 8 · Nosotros y lo que se pregunta | Derecha · Duda 2 | ¿Llegará entera? | 16 | confiar | — |
| 8 · Nosotros y lo que se pregunta | Derecha · Respuesta 2 | La embalamos para viajar. Si llega rota, la reponemos o le devolvemos el dinero. [POR CONFIRMAR: plazo] | 80 | confiar | — |
| 8 · Nosotros y lo que se pregunta | Derecha · Duda 3 | ¿Y si tengo una duda? | 21 | confiar | — |
| 8 · Nosotros y lo que se pregunta | Derecha · Respuesta 3 | Escríbanos por WhatsApp antes de comprar y le respondemos con medidas, fotos o lo que necesite. [POR CONFIRMAR: horario] | 95 | confiar | — |
| 8 · Nosotros y lo que se pregunta | Derecha · Enlace | Ver envíos y cambios | 20 | confiar | — |
| 9 · Estantería | H2 | Piezas de la selección | 22 | desear | — |
| 9 · Estantería | Apoyo | Mírela de cerca, póngala en su carrito y recíbala en su ciudad. | 63 | actuar | — |
| 9 · Estantería | Enlace | Ver toda la selección | 21 | actuar | — |
| 9 · Estantería | Botón de cada pieza | Agregar al carrito | 18 | actuar | — |
| 9 · Estantería | Botón tras agregar (1,3 s) | Agregada | 8 | confiar | — |
| 9 · Estantería | Aviso tras agregar | Agregó [pieza]. [n] piezas en el carrito. Le faltan [$] para el envío gratis. | 64 | actuar | — |
| 9 · Estantería | Enlace del aviso | Ver el carrito | 14 | actuar | — |
| 9 · Estantería | Debajo de la repisa | Envío gratis desde $300.000 [POR CONFIRMAR: monto y cobertura] | 27 | actuar | — |
| 10 · Materiales | H2 | Calidad que se ve de cerca | 26 | desear | — |
| 10 · Materiales | Apoyo | Mire de cerca el esmalte, el borde de una copa y la tela de un pétalo antes de elegir. | 86 | desear | — |
| 10 · Materiales | Nota | El material exacto de cada pieza está en su ficha. | 50 | confiar | — |
| 10 · Materiales | Porcelana | Esmalte liso, de brillo suave. [POR CONFIRMAR con las piezas reales] | 30 | desear | — |
| 10 · Materiales | CTA | Ver piezas de porcelana | 23 | actuar | — |
| 10 · Materiales | Cerámica | Más gruesa, con una textura que se siente al tacto. | 51 | desear | — |
| 10 · Materiales | CTA | Ver piezas de cerámica | 22 | actuar | — |
| 10 · Materiales | Vidrio | Transparente o en ámbar, como las copas y los jarrones. | 55 | desear | — |
| 10 · Materiales | CTA | Ver cristalería | 15 | actuar | — |
| 10 · Materiales | Tela | Pétalos que no se marchitan ni piden agua. | 42 | desear | — |
| 10 · Materiales | CTA | Ver flores artificiales | 23 | actuar | — |
| 11 · Historias | H2 | Historias | 9 | desear | — |
| 11 · Historias | Apoyo | Guías para poner la mesa, empezar una casa y conocer de dónde viene cada forma. | 79 | desear | — |
| 11 · Historias | Guía 1 | Costumbres · El pesebre en casa [GUÍA PENDIENTE] | 31 | desear | — |
| 11 · Historias | Guía 2 | Costumbres · Cómo poner la mesa para recibir [GUÍA PENDIENTE] | 44 | desear | — |
| 11 · Historias | Guía 3 | Origen · La forma del ánfora en el jarrón de hoy [GUÍA PENDIENTE] | 48 | desear | — |
| 11 · Historias | Guía 4 | Por comenzar · El primer jarrón de una casa [GUÍA PENDIENTE] | 43 | desear | — |
| 11 · Historias | Enlace de cada guía | Leer la guía | 12 | actuar | — |
| 11 · Historias | CTA | Ver todas las guías | 19 | actuar | — |
| 12 · Antes de comprar | H2 | Antes de comprar | 16 | confiar | — |
| 12 · Antes de comprar | Envíos a todo el país | El costo y el tiempo se calculan con su ciudad antes de pagar. Gratis desde $300.000 [POR CONFIRMAR] | 84 | confiar | — |
| 12 · Antes de comprar | Embalaje para piezas frágiles | En caja, con papel de seda y protección. [POR CONFIRMAR] | 40 | confiar | — |
| 12 · Antes de comprar | Pago sin crear cuenta | Tarjeta, PSE, Nequi y Daviplata. [POR CONFIRMAR: pasarela] | 32 | confiar | — |
| 12 · Antes de comprar | Cambios y garantía | Las condiciones están a la vista antes de pagar. [POR CONFIRMAR: plazo de cambios] | 48 | confiar | — |
| 12 · Antes de comprar | Enlace | Ver cambios y garantía | 22 | confiar | — |
| 12 · Antes de comprar | Si llega rota | La reponemos o le devolvemos el dinero. | 39 | confiar | — |
| 12 · Antes de comprar | Enlace | Reportar una pieza rota | 23 | confiar | — |
| 12 · Antes de comprar | Atención por WhatsApp | Escribirnos por WhatsApp [POR CONFIRMAR: horario] | 24 | confiar | — |
| 12 · Antes de comprar | Subtítulo | Preguntas frecuentes | 20 | confiar | — |
| 12 · Antes de comprar | CTA | Ver todas las preguntas | 23 | confiar | — |
| 13 · Por mayor | H2 | ¿Compra para un negocio? | 24 | actuar | — |
| 13 · Por mayor | Apoyo | Cotizamos por volumen y le respondemos por WhatsApp. | 52 | actuar | — |
| 13 · Por mayor | CTA | Solicitar cotización por mayor | 30 | actuar | — |
| 14 · Cierre | Antetítulo | Tienda en línea | 15 | atrapar | — |
| 14 · Cierre | H2 | Recorra la tienda, pieza por pieza | 34 | actuar | — |
| 14 · Cierre | Apoyo (palabras de búsqueda) | Porcelanas, jarrones, vajillas, flores artificiales y lámparas para decorar su casa, con envío a todo Colombia. | 111 | desear | — |
| 14 · Cierre | Botón grande | Ver todas las piezas | 20 | actuar | — |
| 14 · Cierre | Bajo el botón | Envío a todo el país · Embalaje para piezas frágiles · Compra sin crear cuenta | 78 | confiar | — |
| Página nueva · Toda la tienda | H1 | Toda la tienda | 14 | actuar | — |
| Página nueva · Toda la tienda | Introducción | Porcelanas, jarrones, vajillas, flores artificiales, esculturas y lámparas para decorar su casa, con envío a todo Colombia. En cada pieza encuentra el material, las medidas y el origen. | 185 | confiar | — |
| Página nueva · Toda la tienda | Descripción para buscadores | Decoración para el hogar en línea: porcelanas, jarrones, vajillas, flores artificiales, esculturas y lámparas. Envíos a todo Colombia. | 134 | atrapar | — |
| Página nueva · Descuentos | H1 | Descuentos | 10 | actuar | — |
| Página nueva · Descuentos | Introducción | Piezas con el precio rebajado. Al lado de cada precio está el anterior, para que vea cuánto ahorra. [POR CONFIRMAR: fechas y condiciones de cada descuento] | 99 | confiar | — |
| Página nueva · Descuentos | Pregunta 1 | ¿El precio anterior es real? Sí. Es el precio al que se vendió la pieza antes de la rebaja. [POR CONFIRMAR: regla del precio anterior] | 91 | confiar | — |
| Página nueva · Descuentos | Descripción para buscadores | Piezas de decoración con descuento, con el precio anterior a la vista. Envíos a todo Colombia. | 94 | atrapar | — |
| Página nueva · Lo nuevo | Introducción | Las piezas que acaban de llegar a la tienda, de la más reciente a la más antigua. [POR CONFIRMAR: cada cuánto llegan piezas nuevas y por cuánto tiempo una pieza se muestra aquí] | 81 | desear | — |
| Página nueva · Lo nuevo | Pregunta 1 | ¿Cada cuánto llegan piezas nuevas? [POR CONFIRMAR] | 34 | confiar | — |
| Página nueva · Lo nuevo | Descripción para buscadores | Piezas de decoración recién llegadas: porcelanas, jarrones, centros de mesa y vajilla. Envíos a todo Colombia. | 110 | atrapar | — |
| Pie · Boletín | H2 | Guías y piezas nuevas en su correo | 34 | desear | — |
| Pie · Boletín | Apoyo | [POR CONFIRMAR: frecuencia] le escribimos con una guía de decoración y las piezas que llegaron. Puede darse de baja con un clic. | 100 | confiar | — |
| Pie · Boletín | Etiqueta | Correo electrónico | 18 | actuar | — |
| Pie · Boletín | Casilla (sin marcar) | Autorizo a Historias que Habitan a tratar mis datos para enviarme correos, según la Política de tratamiento de datos. | 117 | confiar | — |
| Pie · Boletín | Botón | Suscribirme | 11 | actuar | — |
| Pie · Boletín | Confirmación | Listo. Le enviamos un correo para confirmar la suscripción. | 59 | confiar | — |
| Pie · Boletín | Error: correo | Revise el correo: le falta la @ o el dominio. | 45 | confiar | — |
| Pie · Boletín | Error: casilla | Para suscribirse, marque la autorización de datos. | 50 | confiar | — |
| Pie · Boletín | Error: servidor | No pudimos guardar su correo. Intente de nuevo en unos minutos. | 63 | confiar | — |
| Pie · Por mayor | Enlace | Solicitar cotización por mayor | 30 | actuar | — |
| Microcopy | Buscador: sugerencias | Jarrones · Copas · Centros de mesa · Regalos de boda · Lámparas | 63 | actuar | — |
| Microcopy | Buscador: sin resultados | No encontramos «{término}». Pruebe con «jarrón», «copa» o «lámpara», o escríbanos por WhatsApp. | 95 | confiar | — |
| Microcopy | Carrito vacío | Su carrito está vacío. Empiece por las piezas de la selección. | 62 | actuar | — |
| Microcopy | Carrito vacío: CTA | Ver la selección | 16 | actuar | — |
| Microcopy | Pieza agregada (anuncio) | Pieza agregada al carrito. {n} en total. | 40 | confiar | — |
| Cargas | Rejilla de piezas (> 1 s) | Cargando piezas… | 16 | confiar | — |
| Cargas | Colección La mesa que recibe (> 1 s) | Preparando su mesa… | 19 | confiar | — |
| Cargas | Giro de la escultura (> 1 s) | Preparando la escultura… | 24 | confiar | — |
| Cargas | Búsqueda (> 1 s) | Buscando piezas… | 16 | confiar | — |

**Ritmo:** solo el hero tiene movimiento fuerte. Las secciones de imagen (1, 5, 7, 8, 10, 11 y 14) se alternan con secciones claras de producto o texto. La 2 y la 6 comparten la forma de arco, pero la 6 lleva una foto de fondo en cada arco, así que no se repiten.

**Lo nuevo (3).** En escritorio, una foto grande a la izquierda con el botón «Lo quiero todo» (lleva a `lo-nuevo.html`) y, a la derecha, las 4 piezas más recientes en una cuadrícula de 2 × 2, con su nombre y su precio. La foto toma el alto de la cuadrícula. En celular, la foto va arriba y las piezas debajo. Solo muestra piezas que llegaron de verdad; oferta y «Quedan pocas» salen del catálogo, igual que en la tienda.

**Galería de colecciones (7).** Una foto por colección, con un punto sobre cada pieza que abre su tarjeta (nombre, material, precio y «Ver la pieza»). Es el diseño de image-gallery: en escritorio la colección se abre al pasar el cursor, al llegar con el teclado o al tocarla, y no se cierra mientras haya una tarjeta abierta. En celular las fotos pasan de lado y cada una lleva debajo la lista de sus piezas. En Shopify es una sección del tema con un bloque por colección y un bloque por punto.

**Testimonios (4).** Tarjetas que pasan solas, despacio, con el diseño de infinite-moving-cards y sin el cargo de la persona. Se detienen al pasar el cursor, al llegar con el teclado o con el botón «Pausar las reseñas», y quietas si se pidió movimiento reducido. Cada reseña enlaza a la pieza que se compró.

**¿Qué lo trae hoy? (6).** Cada arco lleva una foto que lo llena por completo y el texto va abajo, sobre un degradado oscuro: antetítulo, título, una línea y un botón píldora con flecha. Título y línea tienen alto fijo de dos renglones, así los cuatro arcos quedan alineados. Fotos por producir: una sala con piezas de la tienda, una repisa con piezas, un regalo abierto con una figura y tres piezas distintas sobre una mesa.

**Cierre (14): SEO e incentivo.** Antes invitaba a los regalos de Navidad; ahora invita a recorrer toda la tienda y no cambia con la temporada (la temporada vive en la 5).
- *SEO:* el H2 y la línea de apoyo nombran lo que la gente busca (porcelanas, jarrones, vajillas, flores artificiales, lámparas, decorar la casa, Colombia) en una frase natural, sin repetir palabras. El enlace dice adónde va («Ver todas las piezas») y siempre apunta a `/tienda`, la página comercial principal; el hero y la cabecera apuntan al mismo lugar, así esa señal se refuerza. En producción la foto de las repisas va como `<img>` con texto alternativo, carga diferida y medidas fijas.
- *Incentivo:* «Recorra la tienda, pieza por pieza» invita a mirar sin presión, como en una tienda física. Las repisas llenas muestran surtido. Hay una sola acción grande, con el mismo texto del hero, y debajo tres frases que quitan los miedos del último paso: envío a todo el país, embalaje para frágiles y compra sin crear cuenta. Sin urgencia ni escasez.
- *Si se confirma:* «Más de [N] piezas» en el antetítulo (la cifra concreta convence más) y el envío gratis desde $300.000, solo con datos reales.

**Estantería (9).** Cada pieza tiene «Agregar al carrito». Al agregar, el aviso dice cuánto falta para el envío gratis, con el monto real del carrito.

**Si el inicio queda muy largo, se quitan en este orden:** 11 (Historias) y 10. Las secciones 1, 2, 4, 7, 8, 9, 12 y 14 no se tocan.

## 6. Piezas destacadas: nombre y una línea

Se usan los nombres del catálogo, que dicen qué es cada pieza. El prompt sugiere nombres evocadores («Jarrón Aurora»), pero inventarlos es decisión del negocio. Si se quieren, la regla sería «nombre + descripción» («Jarrón [nombre], de cerámica blanca con asas») para no perder la búsqueda. Los materiales se confirman con cada ficha.

| Pieza | Línea de material o uso |
|---|---|
| Escultura curva blanca | Cerámica, para la mesa de centro o una repisa |
| Jarrón de cerámica blanca con asas | Cerámica, para la consola o el centro del comedor |
| Lámpara de mesa con base de cerámica | Tres tonos de luz, para la mesa de noche |
| Juego de 6 copas de vino | Vidrio, para la mesa de domingo |
| Recipiente pequeño de cerámica | Cerámica, para la mesa o la entrada |
| Vajilla de 16 piezas blanca | Porcelana, para la mesa de todos los días |
| Ramo de flores rosa y champaña | Flores artificiales, para un jarrón de la entrada |

## 7. Preguntas frecuentes del inicio

Salen de `preguntas.html`; la sección 12 muestra cuatro desplegables y enlaza al resto. Van en HTML real, con marcado FAQPage solo cuando las respuestas estén confirmadas.

1. **¿Hacen envíos fuera de Bogotá?** Sí. Enviamos a todo el país. El costo y el tiempo se calculan con su ciudad antes de pagar.
2. **¿Desde qué valor el envío es gratis?** Desde $300.000 [POR CONFIRMAR: monto y ciudades]. Por debajo, el costo aparece en el carrito antes de pagar.
3. **¿Cómo llegan embaladas las piezas frágiles?** En caja, con papel de seda y protección [POR CONFIRMAR: materiales del embalaje].
4. **¿Qué pasa si una pieza llega rota?** La reponemos o le devolvemos el dinero. Repórtela con fotos en «Reportar una pieza rota» [POR CONFIRMAR: plazo].
5. **¿Puedo cambiar una pieza?** Sí, con las condiciones de «Cambios, garantía y retracto», que están a la vista antes de pagar [POR CONFIRMAR: plazo y estado de la pieza]. El inicio no fija días: el plazo lo define la página legal.
6. **¿Qué medios de pago reciben?** Tarjeta, PSE, Nequi y Daviplata [POR CONFIRMAR: pasarela]. Puede comprar sin crear una cuenta.
7. **¿Cómo cuido la porcelana y el cristal?** [POR CONFIRMAR: indicaciones de cuidado por material, por ejemplo si van o no al lavavajillas].

## 8. Lo que no se escribió y qué lo desbloquea

| Texto que falta | Por qué no se escribió | Qué lo desbloquea |
|---|---|---|
| «Más vendidos» | No hay datos de ventas | Informe de ventas por pieza |
| «Con precio con IVA y la ficha completa a un toque» | Es cierto, pero no empuja la compra; el negocio lo quitó | — (el IVA sigue incluido en cada precio) |
| Cifras de clientes o satisfacción | No hay datos | Una encuesta real con su fecha y su muestra |
| «Si llega rota, se la reponemos sin costo» | La política no tiene plazo ni condiciones | Política escrita de piezas rotas |
| Tiempos de entrega («llega en 2 días») | No hay acuerdo con transportadora | Tiempos por ciudad de la transportadora |
| «Hecho a mano», «soplado», «pintado a mano» | No está en las fichas; además «artesanal» está prohibido | Ficha del proveedor por pieza |
| Reseñas reales de la sección 4 | No hay reseñas; las del prototipo son de ejemplo | Reseñas reales con permiso de publicar y respuesta de la tienda a las de 3 estrellas o menos |
| «Llega antes del 24 de diciembre» | Se puede pedir cualquier día y el tiempo depende de la ciudad | Tiempos por ciudad de la transportadora, mostrados antes de pagar |

## 9. Revisión automática del copy deck

185 textos revisados con un guion: límite de palabras por tipo, palabras prohibidas del manual (incluidas las de la lista ampliada), CTA genéricos («Ver más», «Enviar», «OK»), tuteo y rayas en textos cortos.

Sin avisos: ningún texto pasa su límite de palabras, no aparece ninguna palabra prohibida, no hay CTA genéricos, tuteo ni rayas en textos cortos.

Excepciones aprobadas:
- Global · Modal de bienvenida (variante D) / Línea: «exclusivas», aprobado por el negocio el 23/11/2026: hay ofertas que reciben solo los suscriptores

Revisado a mano: «Exclusivo» solo como sello visual y nunca en textos, el origen solo en la ficha técnica y el tratamiento de usted.

## 10. Lo que sigue

Con este orden aprobado: confirmar la plataforma (la recomendación es Shopify con un tema propio), luego dirección de arte y lista de tomas, empezando por las 24 fotos de la escultura girando y las fotos de detalle de los materiales.

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

{{TABLA}}

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

{{N}} textos revisados con un guion: límite de palabras por tipo, palabras prohibidas del manual (incluidas las de la lista ampliada), CTA genéricos («Ver más», «Enviar», «OK»), tuteo y rayas en textos cortos.

{{REVISION}}

Revisado a mano: «Exclusivo» solo como sello visual y nunca en textos, el origen solo en la ficha técnica y el tratamiento de usted.

## 10. Lo que sigue

Con este orden aprobado: confirmar la plataforma (la recomendación es Shopify con un tema propio), luego dirección de arte y lista de tomas, empezando por las 24 fotos de la escultura girando y las fotos de detalle de los materiales.

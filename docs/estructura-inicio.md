# Estructura del inicio

Historias que Habitan · Versión 1 · 18/11/2026 · Estado: propuesta sobre el orden que pidió el negocio, sin validar con usuarios.

Wireframe: `prototipos/inicio-estructura.html`. Textos: `docs/copy-deck-home.md` (se actualiza cuando se apruebe este orden).

## 1. El orden propuesto, sección por sección

| # | Lo que pidió | Funciona | Lo que cambio y por qué |
|---|---|---|---|
| 1 | Hero con efecto 3D y un producto estrella | Sí: sorprende desde el primer pantallazo | Se hace como en el video: la pieza aparece en capas y se arma al bajar, hasta quedar encendida en su lugar. Va con CSS, sin WebGL ni JavaScript, para no retrasar la carga |
| 2 | Validar lo que siente el cliente al comprar | Sí: responde la duda justo después del deseo | Se queda en tres frases cortas con lo que se pregunta el cliente («¿Será como en la foto?») y la respuesta. Los detalles de envío van en la 9, para no repetir |
| 3 | Contenido de temporada (la variante C) | Sí: en noviembre y diciembre es la compra con más intención | Fuera de temporada se cambia por la siguiente fecha o se oculta. Nunca queda una Navidad vieja en el inicio |
| 4 | Categorías según lo que busca el cliente, sin mayorista | Sí, si no repite la 5 | Si se arma con «regalar, recibir, primer hogar», repite las colecciones de la 5. La propuesta es por momento de compra: ideas, una pieza concreta, un regalo, o ayuda para elegir (el cuestionario). El mayorista queda en la cabecera y el pie |
| 5 | Galería de colecciones | Sí: ya está hecha, con puntos sobre cada pieza | Sin cambios |
| 6 | Llamado a la acción sobre nosotros | Sí, pero en otro lugar | Pasa a la 8. En la 6 corta la compra justo cuando la persona está mirando piezas |
| 7 | Categorías por tipo, como en el video | Sí | Sube a la 6: después de mirar colecciones, quien ya sabe qué quiere entra por tipo |
| 8 | Algo que lleve a la estantería | Sí | Sube a la 7, pegada a las categorías, con la transición de la pieza a su ficha que ya existe |
| 9 | Confianza: envíos, empaque y demás | Sí | Se junta con nosotros (8) para responder todas las objeciones antes del cierre. Incluye las preguntas frecuentes |
| 10 | Último llamado con un botón grande | Sí | Sigue a la temporada: en Navidad lleva a regalos y el resto del año a La mesa que recibe |

Agregados después, a pedido del negocio: **Historias** (9), **preguntas frecuentes desplegables** dentro de «Antes de comprar» (10) con enlace a todas, y **la franja de mayoristas** (11). La franja va antes del cierre para que el botón grande siga siendo lo último de la página.

## 2. Orden final

Versión 5 (19/11/2026). Sobre el orden aprobado el 18/11: entran los testimonios (4), encima de la temporada; «Nosotros» y «Lo que se pregunta antes de comprar» pasan a compartir una franja (8), lado a lado; y entra «Lo nuevo» (3), después de las categorías. Quedan 14 secciones.

| # | Sección | Etapa de compra | CTA principal | Movimiento |
|---|---|---|---|---|
| 1 | Hero 3D: la escultura se arma por capas, se posa en su pedestal y gira | Atención | Ver todas las piezas (tienda) | Fuerte: tres tiempos ligados al scroll |
| 2 | Categorías por tipo de pieza (arcos) | Consideración | Uno por categoría · «Ver todo» al pie (tienda) | Suave: los arcos entran al verse |
| 3 | Lo nuevo: foto grande a la izquierda y las 4 piezas más recientes a la derecha (2 × 2) | Consideración | Lo quiero todo (sobre la foto) · una por pieza | Suave: la pieza se acerca al pasar o enfocar |
| 4 | Testimonios (infinite-moving-cards, sin el cargo) | Confianza | La pieza de cada reseña | Suave: pasan solas, con pausa |
| 5 | Temporada (Navidad) | Deseo e intención | Encontrar un regalo | Ninguno |
| 6 | ¿Qué lo trae hoy? (arcos con foto de fondo) | Consideración | Uno por camino (ideas, buscador, regalos, descuentos) | Suave: la foto se acerca al pasar o enfocar |
| 7 | Galería de colecciones (diseño de image-gallery), con puntos sobre cada pieza | Deseo | Ver la pieza / Ver la colección | Medio: paneles que se abren al pasar el cursor |
| 8 | Nosotros (izquierda) y Lo que se pregunta antes de comprar (derecha), separadas por un divisorio | Confianza | Conocer la marca · Ver envíos y cambios | Ninguno |
| 9 | Estantería: piezas de la selección en repisas, con «Agregar al carrito» | Decisión | Agregar al carrito · Ver toda la selección | Suave: la pieza viaja a su ficha |
| 10 | Calidad que se ve de cerca: porcelana, cerámica, vidrio y tela | Deseo y confianza | Uno por material | Suave: paralaje de las texturas |
| 11 | Historias (rejilla de image-gallery) | Confianza y búsqueda | Leer la guía · Ver todas las guías | Suave: la foto se oscurece al pasar o enfocar |
| 12 | Antes de comprar: envíos, embalaje, pago, cambios y preguntas desplegables | Objeciones | Ver todas las preguntas | Ninguno |
| 13 | ¿Compra para un negocio? | Otro público | Solicitar cotización por mayor | Ninguno |
| 14 | Cierre a todo el ancho: repisas de la tienda | Acción | Ver todas las piezas (tienda) | Ninguno |

**Para tener en cuenta:**
- **Las categorías justo después del hero** son un buen atajo: quien ya sabe qué busca entra en un toque.
- **Lo nuevo en la 3, después de las categorías:** quien vuelve ve primero lo que llegó. Del primer diseño de referencia quedan los títulos centrados. En escritorio, la foto va a la izquierda, del alto de la cuadrícula, y a la derecha van las 4 piezas más recientes, dos por fila, con nombre y precio; el resto está en `lo-nuevo.html`. Solo muestra piezas que llegaron de verdad [POR CONFIRMAR: cada cuánto llegan y por cuánto tiempo una pieza cuenta como nueva]. «Lo quiero todo», sobre la foto, lleva a `lo-nuevo.html`.
- **Los testimonios en la 4** dan confianza temprano, antes de la temporada y de las colecciones. Las reseñas del prototipo son de ejemplo; la sección solo se publica con reseñas reales. En el inicio van solo las de 3 estrellas o más, con al menos una de 3 y una de 4; las de 1 y 2 siguen en la ficha de cada pieza, con la respuesta de la tienda.
- **Las tarjetas pasan solas, pero se pueden detener:** con el cursor, con el foco del teclado y con el botón «Pausar las reseñas» (WCAG 2.2.2). El prompt pedía reseñas sin carrusel automático; con la pausa visible cumple la norma.
- **La 2 y la 6 comparten la forma de arco,** pero la 2 muestra la pieza recortada y la 6 una foto que llena el arco. Así no se repiten.
- **La 8 junta dos bloques en una franja, cada uno con sus textos de siempre.** A la izquierda, «Cómo contamos cada pieza» con la foto y «Conocer la marca»; a la derecha, las tres dudas en la voz del cliente y «Ver envíos y cambios». En escritorio van lado a lado con un divisorio vertical de bajo contraste; en celular y tableta, una debajo de la otra con el divisorio horizontal. Va justo antes de la estantería, para que la duda quede resuelta antes de «Agregar al carrito». La 12 trae los datos de envío, embalaje y pago, con las preguntas desplegables.

Pie: boletín, enlace a por mayor, datos del vendedor y enlaces legales.

**Modal de bienvenida (variante D, fuera de la numeración):** «Nuevas piezas y nuevas ofertas». Aparece una vez, desde la segunda página de la visita, a los 20 segundos o al bajar la mitad; pide nombre, correo, celular y empresa opcional, con «Sí, quiero suscribirme» y «Por el momento no». Detalle y reglas en `docs/handoff-desarrollo.md`; las cuatro variantes, en `prototipos/modal-bienvenida.html`.

**Ritmo:** solo el hero tiene movimiento fuerte. Las secciones de imagen (1, 3, 5, 7, 8, 10, 11 y 14) se alternan con secciones claras de producto o texto.

## 3. Qué pasa con las secciones del plan anterior

| Del plan anterior | Dónde queda |
|---|---|
| Recorrido del objeto al espacio | Dentro del hero 3D (la escultura se arma, se posa en su lugar y gira) |
| Imagen completa «compre el look» | En la galería de colecciones (7) |
| Compra por espacio | Camino «Busco ideas para mi casa» de la 6 |
| Galería de inspiración y mosaico de colecciones | Galería de colecciones (7) |
| Vista 3D de una pieza | El giro del hero (1); el visor 3D queda en la ficha |
| Materiales y detalles | Sección propia (10): calidad que se ve de cerca |
| Reseñas | Sección propia (4), con reseñas de ejemplo hasta tener las reales |
| Regalos por ocasión | Temporada (5) y camino «Busco un regalo» (6) |
| Guías de Historias | Sección propia (11) y camino «Busco ideas» (6) |
| Preguntas frecuentes | Desplegables en la 12, con enlace a todas |
| Boletín | Pie |
| Por mayor | Franja propia (13) y pie |

## 4. Hero 3D: cómo sorprende sin volverse lento

El hero toma los efectos del video de referencia y los encadena en **tres tiempos** con una escultura:

1. **Se arma por capas.** La Escultura curva blanca aparece separada en capas inclinadas que flotan (la vista explotada del video) y se juntan de abajo hacia arriba.
2. **Se posa en su lugar.** Sube una base baja de madera, la escultura queda apoyada y aparece la sala alrededor: la ventana, el cuadro y una luz cálida desde arriba.
3. **Gira sobre sí misma.** La escultura da una vuelta completa y la luz recorre su superficie, como el «objeto firma» del video. Se mira por todos sus lados, igual que dice el titular.

- **Pieza estrella:** la Escultura curva blanca, $179.900 [POR CONFIRMAR con el negocio]. Tiene una etiqueta en la escena que lleva a su ficha. El botón principal es «Ver todas las piezas» y lleva a la tienda.
- **Titular:** «Piezas que se miran desde todos sus lados». Reemplaza a «La mesa puesta y la luz encendida», que hablaba de la lámpara.
- **Técnica:** capas con transformaciones 3D de CSS ligadas al scroll, sin WebGL y sin JavaScript. Solo se animan `transform` y `opacity`.
- **Escritorio:** la sección queda fija mientras se baja el equivalente a 1,4 pantallas. Quien baja controla la velocidad y puede detenerse o devolverse.
- **Celular:** la sección no queda fija. La escultura se arma mientras su escena entra en pantalla y gira al seguir bajando.
- **Navegadores sin animaciones ligadas al scroll:** se arma y da una vuelta sola al cargar, en unos 5 segundos, y queda quieta. No gira sin parar.
- **Movimiento reducido:** se muestra armada, de frente y quieta.
- **Lo que carga primero:** el titular (que es el LCP) y las capas, unas 6 imágenes recortadas de ≈ 30 KB cada una.

**Cómo se produce el giro (sin JavaScript):** 24 fotos de la escultura girando sobre un plato, puestas una debajo de otra en una sola imagen (≈ 15 KB por foto, ≈ 360 KB en total). Un marco muestra una foto a la vez y la imagen se desplaza con `transform` y `steps(24)` al ritmo del scroll. Esa imagen carga después de la primera pantalla; mientras tanto se ve la primera foto.

**Cómo se producen las capas (de menos a más costo):**
1. **Foto real de la escultura, recortada en franjas horizontales.** Es fiel a la pieza y barato, pero las franjas se ven planas.
2. **Render de un modelo 3D de la escultura.** Cada capa sale con volumen, como en el video, y el mismo modelo sirve para la vista 3D de la ficha.
3. **Video generado con IA (scroll-world).** Solo si se aprueba su costo y partiendo de fotos reales, porque la pieza mostrada tiene que ser la que se entrega (Ley 1480 de 2011).

## 4b. Secciones de arcos (2 y 6)

- **6 · ¿Qué lo trae hoy?** usa la forma de arco de team-showcase, pero cada arco lleva una foto de fondo que lo llena. El texto va abajo, sobre un degradado oscuro: antetítulo en champaña, título en serif, una línea y un botón píldora con flecha. Título y línea tienen alto fijo de dos renglones para que los cuatro queden alineados. Al pasar el cursor o enfocar, la foto se acerca y el botón se llena. En celular pasan de lado. El cuarto arco es «Busco descuentos» y lleva a la página de descuentos; el cuestionario sigue en el botón «Ayúdeme a elegir» del hero.
- **2 · Categorías por tipo** usa los mismos arcos de la 6, con las siete categorías y su pieza. En escritorio van los siete en una fila; en celular pasan de lado, dos a la vista.

## 4c. Cierre y páginas nuevas

**Cierre (14).** Ya no es de regalos de Navidad: invita a recorrer toda la tienda y no cambia con la temporada.
- **Texto:** antetítulo «Tienda en línea», H2 «Recorra la tienda, pieza por pieza», la línea «Porcelanas, jarrones, vajillas, flores artificiales y lámparas para decorar su casa, con envío a todo Colombia», el botón grande «Ver todas las piezas» y, debajo, «Envío a todo el país · Embalaje para piezas frágiles · Compra sin crear cuenta».
- **SEO:** la línea nombra lo que la gente busca en una frase natural, sin repetir palabras. El enlace describe su destino y siempre apunta a `/tienda`, igual que el hero y la cabecera. Un cierre que no caduca evita que el inicio cambie de contenido cada temporada. En producción la foto va como `<img>` con texto alternativo, carga diferida y medidas fijas (CLS 0).
- **Incentivo:** invitar a recorrer sin presión, mostrar surtido con las repisas llenas, una sola acción grande con el mismo texto del hero y tres frases que quitan los miedos del último paso. Sin urgencia ni escasez. Si se confirman, «Más de [N] piezas» y el envío gratis desde $300.000 suman, solo con datos reales.

**Páginas nuevas.** Se generan con la misma plantilla de categoría (estantería, filtros y viaje de la pieza a su ficha):
- `tienda.html` (`/tienda`) · «Toda la tienda»: las 37 piezas, con enlaces a cada categoría, a Lámparas y a Descuentos. Es el destino de los botones del hero y del cierre. Para buscadores, el título podría ser «Decoración para el hogar en línea · Historias que Habitan» [POR CONFIRMAR con `/claude-seo:seo-plan`].
- `descuentos.html` (`/descuentos`) · «Descuentos»: las piezas con precio rebajado y el precio anterior a la vista, con preguntas sobre la regla del precio anterior, las fechas y los cambios. Si queda sin piezas, se muestra un aviso y no se indexa.
- `lo-nuevo.html` (`/lo-nuevo`) · «Lo nuevo»: las piezas recién llegadas, de la más reciente a la más antigua, según `NUEVAS` en `herramientas/catalogo.py`. Es el destino de «Lo quiero todo» (sección 3) y aparece entre las categorías de la tienda. [POR CONFIRMAR: por cuánto tiempo una pieza cuenta como nueva]
- **Arquitectura:** las dos rutas se agregan a `docs/arquitectura-informacion.md` cuando se aprueben. Las migas de cada pieza siguen siendo las de su categoría.

## 5. Presupuesto de velocidad por sección

Metas en celular de gama media con 4G: LCP ≤ 2,0 s, INP ≤ 150 ms, CLS ≤ 0,05, JavaScript inicial ≤ 150 KB, primera pantalla ≤ 500 KB. Los pesos son estimados de diseño; se miden cuando exista el tema.

| # | Sección | Imágenes | JavaScript que agrega | ¿Primera pantalla? | Cómo carga | Versión liviana |
|---|---|---|---|---|---|---|
| 1 | Hero 3D (capas y giro) | 6 recortes ≈ 30 KB c/u + fondo ≈ 80 KB; giro: 24 fotos ≈ 360 KB después de la primera pantalla | 0 KB | Sí (sin el giro) | Capas con prioridad alta; el giro, diferido | Movimiento reducido: armada, de frente y quieta |
| 2 | Categorías por tipo | 7 recortes ≈ 25 KB c/u | 0 KB | En escritorio, en parte | Diferida | Igual |
| 3 | Lo nuevo | 1 foto ≈ 120 KB + 4 recortes ≈ 25 KB c/u | 0 KB | No | Diferida | Igual |
| 4 | Testimonios | Ninguna | ≈ 1 KB (pausa) | No | Con la página | Fila quieta que se desliza a mano |
| 5 | Temporada | 1 foto ≈ 120 KB | 0 KB | No | Diferida | Igual |
| 6 | ¿Qué lo trae hoy? | 4 fotos ≈ 50 KB c/u | 0 KB | No | Diferida | Color de fondo sin foto |
| 7 | Galería de colecciones | 4 fotos ≈ 120 KB c/u | ≈ 3 KB | No | Diferida; en celular, solo la visible y la siguiente | Igual |
| 8 | Nosotros y lo que se pregunta | 1 foto ≈ 100 KB | 0 KB | No | Diferida | Igual |
| 9 | Estantería | 4 recortes ≈ 25 KB c/u | ≈ 2 KB (viaje a la ficha y agregar al carrito) | No | Diferida | Sin transición a la ficha |
| 10 | Materiales | 4 fotos de detalle ≈ 60 KB c/u | 0 KB | No | Diferida | Sin paralaje |
| 11 | Historias | 4 fotos ≈ 40 KB c/u | 0 KB | No | Diferida | Sin fotos, solo títulos |
| 12 | Antes de comprar | Íconos en SVG | 0 KB (preguntas con `<details>`) | No | Con la página | Igual |
| 13 | Por mayor | Ninguna | 0 KB | No | Con la página | Igual |
| 14 | Cierre | 1 foto ≈ 150 KB | 0 KB | No | Diferida | Color de fondo sin foto |

**Primera pantalla estimada:** HTML ≈ 30 KB + CSS ≈ 15 KB + 2 fuentes en subconjunto ≈ 60 KB + capas y fondo del hero ≈ 260 KB ≈ 365 KB, dentro de la meta de 500 KB. **JavaScript inicial:** el de cabecera, menú y carrito; el hero no agrega nada.

**Si algo no cabe, se quita primero:** el fondo del ambiente del hero (queda el color), luego los recortes de las categorías (2).

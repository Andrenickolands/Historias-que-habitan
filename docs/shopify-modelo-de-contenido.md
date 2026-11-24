# Shopify: modelo de contenido y administración · Historias que Habitan

Versión 1 · 23/11/2026 · De: diseño de producto · Para: desarrollo del tema, y para quien administre la tienda.

**Para qué sirve:** dice dónde vive cada cosa del prototipo en Shopify y cómo se cambia sin tocar código. El tema se construye a medida desde los prototipos de `prototipos/`; no se parte de una plantilla de la tienda de temas.

**Regla de base:** ningún texto, foto, precio ni estado queda escrito en el código. Todo sale del admin de Shopify: productos, colecciones, blog, páginas, metacampos, metaobjetos, menús, ajustes del tema o textos del tema.

Lo que dice [POR CONFIRMAR] se decide al montar la tienda o con el negocio. Las capacidades de Shopify citadas se revisaron en shopify.dev el 23/11/2026.

## 1. Dónde vive cada cosa

| Contenido | Dónde se edita en Shopify | Nota |
|---|---|---|
| Piezas: nombre, descripción, precio, fotos, variantes, modelo 3D | **Productos** | El modelo 3D en formato GLB lo trae Shopify |
| Oferta | **Productos** → «Precio de comparación» | La pieza sale en oferta y entra sola a Descuentos |
| Quedan pocas y Agotada | **Productos** → inventario | Salen solos del inventario; no se marcan a mano |
| Hecho, Diseño, Historia, medidas, origen, sello «Exclusivo», piezas que combinan | **Productos** → metacampos (sección 2) | Campos propios en el formulario de cada pieza |
| Categorías, Toda la tienda, Lo nuevo, Descuentos, colecciones de ambiente | **Productos → Colecciones** (sección 3) | Automáticas con reglas, o manuales |
| Testimonios, preguntas frecuentes, materiales, caminos, temporada, escenas de la galería | **Contenido → Metaobjetos** (sección 4) | Fichas con campos fijos, que se llenan como un formulario |
| Inicio: orden de las secciones, títulos, fotos, botones | **Tienda online → Personalizar** (sección 5) | Las secciones se arrastran, se ocultan y se editan |
| Historias | **Tienda online → Blog** (sección 6) | Cada historia es una entrada, con plantilla elegida |
| Nosotros, Envíos, Cambios, Por mayor, Preguntas frecuentes | **Tienda online → Páginas** (sección 7) | Cada una con su plantilla |
| Términos, privacidad, reembolsos y envíos | **Configuración → Políticas** | Shopify crea esas páginas y las enlaza en el pago |
| Menú de la cabecera y columnas del pie | **Tienda online → Navegación** | Un menú por lugar (sección 5) |
| WhatsApp, monto del envío gratis, datos legales, umbral de «quedan pocas», reglas del modal | **Personalizar → Ajustes del tema** (sección 8) | Valores de toda la tienda |
| Textos fijos: botones, errores, estados, mensajes del carrito | **Temas → Editar el contenido predeterminado del tema** (sección 9) | Sale del copy deck |

## 2. Productos

**Campos propios de Shopify que se usan:**
- Título y descripción.
- Precio y «precio de comparación»: la oferta.
- Inventario, con seguimiento activado en cada variante.
- Variantes: color y tamaño.
- Multimedia: cuatro fotos por pieza, recorte para la estantería y modelo 3D (GLB).
- Tipo de producto: la categoría.
- Proveedor: la marca, si la hay.
- Etiquetas: `nuevo`, entre otras.
- SEO.

**Metacampos de producto** (espacio `custom`). Se crean primero, antes de cargar las piezas, en **Configuración → Datos personalizados → Productos**:

| Clave | Tipo | Dónde se ve | Ejemplo o regla |
|---|---|---|---|
| `custom.hecho` | Texto de varias líneas | Ficha: «Hecho, diseño e historia» | Material, medidas y origen comprobables; nada sin fuente |
| `custom.diseno` | Texto de varias líneas | Ficha | Lectura de la forma y el estilo |
| `custom.historia` | Texto de varias líneas | Ficha | Un lugar posible para la pieza en la casa |
| `custom.alto`, `custom.ancho`, `custom.diametro` | Dimensión (cm) | Ficha técnica y tarjetas | Medidas reales de la pieza |
| `custom.material` | Referencia a metaobjeto «Material» (lista) | Ficha, filtros, sección Materiales | Cerámica, porcelana, vidrio, tela |
| `custom.origen` | Texto de una línea | **Solo** en la ficha técnica | Regla de marca: el origen no va en tarjetas ni títulos |
| `custom.exclusivo` | Verdadero o falso | Sello «Exclusivo» sobre la foto | Solo como sello visual |
| `custom.combina_con` | Lista de productos | Ficha: «Combínela con» | Elegidos a mano |
| `custom.parecidas` | Lista de productos | Ficha agotada: «Parecidas y disponibles» | Si se deja vacío, el tema toma tres de la misma colección y precio cercano |
| `custom.recorte` | Archivo (imagen PNG sin fondo) | Estantería, arcos, Lo nuevo | El dibujo del prototipo es su lugar |
| `custom.cuidados` | Texto de varias líneas | Ficha | Cómo limpiarla |
| `custom.foto_apagada`, `custom.foto_calida`, `custom.foto_neutra`, `custom.foto_fria` | Archivo (imagen) | Solo lámparas: controles de luz | Una foto por estado de luz |
| `custom.bombillo`, `custom.potencia`, `custom.voltaje` | Texto de una línea | Solo lámparas: ficha técnica | [POR CONFIRMAR con el proveedor] |

Para los filtros por color y material, se usan los metacampos estándar de la categoría de producto de Shopify cuando existan, y si no, estos. [POR CONFIRMAR al montar]

**Estados de la pieza:** nadie los escribe. El tema los calcula con los mismos datos en todo el sitio, como hoy hace `herramientas/catalogo.py`:
- **Oferta:** el precio de comparación es mayor que el precio. Una pieza agotada no se muestra en oferta.
- **Quedan pocas:** las unidades disponibles son iguales o menos que el umbral de los ajustes del tema (3 [POR CONFIRMAR]).
- **Agotada:** la pieza no tiene unidades disponibles.

## 3. Colecciones

| Colección | Tipo | Regla en Shopify |
|---|---|---|
| Porcelanas y figuras, Jarrones y recipientes, Flores artificiales, Mesa, Centros de mesa, Esculturas pequeñas, Decoraciones del hogar, Lámparas | Automática | «Tipo de producto» igual a la categoría |
| Toda la tienda | La de Shopify | `/collections/all` ya existe |
| Lo nuevo | Automática | Etiqueta igual a `nuevo`, ordenada «de la más nueva a la más antigua». Shopify no tiene regla por fecha de creación; se quita la etiqueta cuando la pieza deja de ser nueva [POR CONFIRMAR: después de cuántos días; se puede automatizar con Shopify Flow] |
| Descuentos | Automática, «cumplir todas» | Precio de comparación mayor que 0 **y** inventario mayor que 0: así una agotada no sale en Descuentos |
| La mesa que recibe, Primer hogar, Regalos que se guardan | Manual | Las piezas se eligen a mano |
| Selección del inicio (estantería) | Manual | Las piezas que el negocio quiere mostrar en el inicio |

**Metacampos de colección** (para los arcos y las colecciones de ambiente):
- `custom.linea`: texto corto bajo el nombre.
- `custom.recorte`: la pieza que se ve en el arco.
- `custom.color`: el color de fondo.
- `custom.escena`: referencia a una «Escena» de la galería.

## 4. Metaobjetos: contenido que se repite

Regla: lo que aparece **una sola vez** (un título del inicio, por ejemplo) va en los ajustes de la sección. Lo que es una **lista** o se usa en **varios lugares** va en un metaobjeto. Se crean en **Configuración → Datos personalizados → Metaobjetos** y se llenan en **Contenido → Metaobjetos**.

| Metaobjeto | Campos | Lo usan |
|---|---|---|
| **Pregunta frecuente** | Pregunta · Respuesta (texto enriquecido) · Tema (envíos, pagos, cambios, piezas, mayoristas) · «Mostrar en el inicio» (sí o no) · Orden | Página de preguntas, «Antes de comprar» del inicio, categorías, Descuentos |
| **Testimonio** (si no se usa una app de reseñas) | Estrellas (1 a 5) · Título · Texto · Nombre e inicial · Ciudad · Pieza (producto) · Respuesta de la tienda · Fecha · Permiso de publicar (sí o no) | Testimonios del inicio (solo 3 estrellas o más) y fichas (todas) |
| **Material** | Nombre · Foto de detalle · Texto corto · Colección a la que lleva | «Calidad que se ve de cerca», ficha, filtros |
| **Camino** | Antetítulo · Título · Línea · Foto de fondo · Enlace · Texto del botón | «¿Qué lo trae hoy?» |
| **Temporada** | Nombre · Título · Texto · Foto · Fecha de inicio · Fecha de fin · Colección · Rangos de presupuesto (enlaces) | Sección de temporada: se muestra solo entre sus fechas |
| **Escena** | Foto del ambiente · Colección · Puntos (lista de «Punto») | Galería de colecciones |
| **Punto** | Producto · Posición horizontal (%) · Posición vertical (%) | Los puntos sobre cada foto de la galería |
| **Garantía** | Ícono · Título · Texto | «Antes de comprar», carrito, pago |
| **Paso de una guía** | Título · Texto · Foto | Plantilla de entrada «Guía» |

## 5. Inicio y partes globales: secciones del tema

Cada sección del prototipo es una sección del tema con ajustes. El movimiento (el hero 3D, los arcos, la galería) va en el código; el contenido, en los ajustes. Shopify admite hasta 25 secciones por página; el inicio tiene 14.

| # | Sección del prototipo | Qué se edita en Personalizar | De dónde salen los datos |
|---|---|---|---|
| 1 | Hero 3D | Pieza destacada, capas o fotos del giro, textos, dos botones | Producto elegido; imágenes de la sección |
| 2 | Categorías por tipo (arcos) | Un bloque por categoría y el texto de «Ver todo» | Colección elegida y sus metacampos |
| 3 | Lo nuevo | Colección (Lo nuevo), cuántas piezas (4), foto grande, texto «Lo quiero todo» | Colección Lo nuevo |
| 4 | Testimonios | Título, mínimo de estrellas (3), velocidad | App de reseñas o metaobjeto «Testimonio» |
| 5 | Temporada | Qué temporada mostrar | Metaobjeto «Temporada»; se oculta fuera de sus fechas |
| 6 | ¿Qué lo trae hoy? | Bloques «Camino» | Metaobjeto «Camino» |
| 7 | Galería de colecciones | Bloques «Escena» | Metaobjeto «Escena» y sus «Punto» |
| 8 | Nosotros y lo que se pregunta | Foto, texto y botón de la marca; las tres dudas | Ajustes de la sección; dudas desde «Pregunta frecuente» marcadas para el inicio |
| 9 | Estantería | Colección (Selección del inicio), cuántas piezas, texto del enlace | Colección; «Agregar al carrito» con la API del carrito de Shopify |
| 10 | Calidad que se ve de cerca | Bloques de material | Metaobjeto «Material» |
| 11 | Historias | Blog y cuántas entradas | Últimas entradas del blog Historias |
| 12 | Antes de comprar | Garantías, cuántas preguntas, enlace a todas | Metaobjetos «Garantía» y «Pregunta frecuente» |
| 13 | ¿Compra para un negocio? | Texto y botón | Ajustes de la sección |
| 14 | Cierre | Foto, textos, botón, tres frases de confianza | Ajustes de la sección |

**Partes globales** (grupos de secciones de Shopify, editables en todas las páginas):
- **Cabecera:**
  - Menú «Principal» de Navegación: Tienda, Lo nuevo, Descuentos, Colecciones, Historias, Por mayor. Lo nuevo y Descuentos llevan su estilo destacado por ajuste.
  - Menú «Atajos de celular» de Navegación.
  - Íconos de cuenta, favoritos y carrito.
- **Menú lateral:** menú «Tienda», más las dos tarjetas destacadas (Lo nuevo y Descuentos) como ajustes.
- **Pie:**
  - Franja del boletín, con títulos y textos por ajuste.
  - Cuatro menús de Navegación: Tienda, Ayuda, Su cuenta y La marca.
  - Datos legales desde los ajustes del tema.
- **Modal de bienvenida (variante D):** sección o bloque de aplicación con sus textos, los segundos de espera, los días sin volver a mostrarse y un interruptor para apagarlo.

## 6. Historias: el blog de Shopify

- **Un blog llamado «Historias».** Cada historia es una entrada con título, extracto, foto, contenido, autor, fecha, etiquetas y SEO. Etiquetas sugeridas: Costumbres, Ideas para la casa, Piezas, Temporada.
- **Plantillas prediseñadas:** son plantillas de entrada del tema. Quien escribe la elige en «Plantilla del tema» al crear la entrada:

| Plantilla | Archivo | Qué trae, en orden |
|---|---|---|
| General | `article.json` | Foto, título, texto, piezas relacionadas |
| Historia de una pieza | `article.pieza.json` | Foto vertical, Hecho · Diseño · Historia de la pieza, texto, la pieza con «Agregar al carrito», piezas que combinan |
| Guía o ideas para decorar | `article.guia.json` | Foto, introducción, pasos con foto, cuadrícula de piezas, preguntas |
| Costumbre o temporada | `article.temporada.json` | Foto a todo el ancho, cita destacada, texto, colección de la temporada |

- **Metacampos de entrada** (Configuración → Datos personalizados → Entradas de blog): `custom.portada_vertical` (imagen), `custom.cita` (texto), `custom.piezas` (lista de productos), `custom.coleccion` (colección), `custom.pasos` (lista de «Paso de una guía»). La plantilla los acomoda sola; si un campo está vacío, su bloque no aparece.
- **Límite honesto:** el cuerpo de una entrada es un editor de texto enriquecido (títulos, negritas, listas, fotos, enlaces), no un constructor de arrastrar y soltar. El diseño lo pone la plantilla.
  - No se recomienda una app de construcción de páginas (por ejemplo, PageFly o Shogun): agrega peso a la página, cobra cada mes y rompe la coherencia del diseño.
- **Listado del blog** (`blog.json`): entrada destacada arriba, filtro por etiqueta y cuadrícula. La sección Historias del inicio toma las últimas entradas sola.
- **Reglas editoriales:**
  - Hecho, Diseño e Historia, con los hechos con fuente.
  - Trato de usted.
  - Las palabras prohibidas del manual de marca.
  - Nada inventado: si una cifra o un dato no está confirmado, se marca.

## 7. Páginas

| Página del prototipo | En Shopify |
|---|---|
| Nosotros | Página con plantilla `page.nosotros.json` |
| Envíos, Cambios y garantía | Páginas; además, las políticas de envío y de reembolso en **Configuración → Políticas** |
| Términos, Tratamiento de datos | **Configuración → Políticas** (términos del servicio y política de privacidad) [POR CONFIRMAR: textos revisados por un abogado] |
| Política de cookies | Página propia, más el aviso de cookies de Shopify (Privacidad del cliente) |
| Preguntas frecuentes | Página con plantilla `page.preguntas.json` que lista el metaobjeto «Pregunta frecuente» por tema |
| Por mayor | Página con plantilla `page.por-mayor.json` y formulario de contacto con campos de empresa |
| Reportar una pieza rota | Página con formulario de contacto (foto, pedido, descripción) [POR CONFIRMAR: si se usa una app para adjuntar fotos] |
| Seguir mi pedido | Estado del pedido de Shopify, o la app del operador logístico [POR CONFIRMAR] |
| Cuestionario de orientación | Página con plantilla propia; preguntas y resultados en metaobjetos [POR DEFINIR] |
| Mis favoritos | Página con plantilla propia, conectada a la app de favoritos (sección 10) |
| Mi cuenta | Cuentas de cliente de Shopify, con «Mis favoritos» y «Avisos de llegada» |

## 8. Ajustes del tema (toda la tienda)

- Colores y fuentes: los tokens de `docs/tokens.json`.
- Número de WhatsApp de la marca.
- Monto del envío gratis (solo el texto; el envío real se configura en **Configuración → Envíos** y ambos deben coincidir).
- Tiempo de entrega que se muestra («De 2 a 5 días hábiles»).
- Umbral de «quedan pocas» (3).
- Datos del vendedor para el pie: razón social, NIT, dirección y correo.
- Barra de anuncio: texto y enlace.
- Modal de bienvenida: encendido o apagado, segundos (20), días sin volver a mostrarse (14) y textos.

## 9. Textos fijos del tema

Botones («Agregar al carrito», «Sí, quiero suscribirme», «Por el momento no»), estados («Oferta», «Quedan pocas», «Agotada»), errores de formulario, mensajes del carrito y de favoritos: van en `locales/es.default.json`. Se cambian en **Temas → Editar el contenido predeterminado del tema**, sin tocar código.

La fuente es `docs/copy-deck-home.md`; si se cambia un texto en Shopify, se actualiza también el copy deck.

## 10. Lo que Shopify no trae y necesita una app

| Función del prototipo | Opción | Nota |
|---|---|---|
| Reseñas con estrellas y respuesta de la tienda | App de reseñas (por ejemplo, Judge.me) [POR CONFIRMAR] | Debe permitir mostrar en el inicio solo las de 3 estrellas o más |
| Aviso de llegada de las agotadas | App de «back in stock» o Klaviyo [POR CONFIRMAR] | Un aviso por correo; sin suscribir a otros correos |
| Favoritos guardados en la cuenta | App de favoritos, o código propio con metacampos del cliente [POR CONFIRMAR] | El prototipo los guarda en el navegador |
| Filtros por material, color, tamaño y precio | Search & Discovery (gratis, de Shopify) | Usa los metacampos de la sección 2 |
| Boletín y modal D | Formulario de clientes del tema o Shopify Forms (gratis) | Nombre, correo y celular; la empresa como etiqueta del cliente [POR CONFIRMAR: campo extra en Shopify Forms] |
| Correos del boletín | Shopify Email o Klaviyo [POR CONFIRMAR] | |
| Pasarela de pago | [POR CONFIRMAR] | Ver «Decisiones del negocio» en el handoff |
| Operador logístico | [POR CONFIRMAR] | Tarifa por ciudad y seguimiento del pedido |

## 11. Lo que limita el pago (checkout)

El pago de Shopify se personaliza poco sin **Shopify Plus**: las extensiones del checkout y su marca son solo de Plus. En el plan estándar:
- **Casillas legales separadas** (términos y datos): no se pueden agregar al pago. Opción: pedirlas en el carrito, antes de pasar a pagar, o usar los enlaces legales que el pago ya muestra.
- **Pago con sesión que abre en el segundo paso:** Shopify ya llena los datos guardados del cliente, pero el orden de los pasos lo decide Shopify.
- **Un solo tipo de envío** y **pago como invitado:** se pueden configurar en cualquier plan.

[POR CONFIRMAR: plan de Shopify]

## 12. Rutina: quién cambia qué

| Tarea | Dónde | Pasos |
|---|---|---|
| Subir una pieza nueva | Productos → Agregar producto | Fotos y recorte, precio, inventario, tipo, metacampos (Hecho, Diseño, Historia, medidas, material, origen), etiqueta `nuevo`, publicar |
| Ponerla en oferta | La pieza → Precio de comparación | Al terminar la oferta, borrar el precio de comparación |
| Quitarla de Lo nuevo | La pieza → Etiquetas | Borrar `nuevo` [POR CONFIRMAR: o automático] |
| Cambiar la foto o el texto de una sección del inicio | Tienda online → Personalizar | Elegir la sección y editar |
| Activar la temporada | Contenido → Metaobjetos → Temporada | Fechas, foto, textos y colección |
| Publicar una historia | Tienda online → Blog → Agregar entrada | Elegir la plantilla, escribir, llenar foto y piezas |
| Agregar una pregunta frecuente | Contenido → Metaobjetos → Pregunta frecuente | Pregunta, respuesta, tema y si va en el inicio |
| Cambiar el menú | Tienda online → Navegación | Editar el menú Principal, Atajos o los del pie |
| Cambiar el texto de un botón | Temas → Editar el contenido predeterminado del tema | Buscar el texto y cambiarlo |

## 13. Orden de construcción

1. **Modelo de contenido:** crear las definiciones de metacampos (sección 2 y 6) y de metaobjetos (sección 4) antes de cargar productos.
2. **Tema:**
   - tokens;
   - cabecera, menú, pie y modal (hoy en `herramientas/sitio.py`);
   - tarjeta de producto con estados;
   - ficha, colección, carrito, páginas;
   - el inicio con sus 14 secciones;
   - blog y las cuatro plantillas de entrada.
3. **Carga:** productos con sus metacampos (importación por CSV o en bloque), colecciones, metaobjetos, páginas, menús y políticas.
4. **Apps** de la sección 10.
5. **Guía corta para el equipo** con la rutina de la sección 12, y una capacitación.
6. **Pruebas:** los recorridos de la sección 5 del handoff y las hipótesis de su sección 13.

## 14. Pendientes por confirmar

- Plan de Shopify (estándar o Plus): define qué se puede hacer en el pago.
- Apps finales y su costo mensual.
- Cuántos días una pieza cuenta como nueva.
- Quién escribe las historias y cada cuánto se publican.
- Si se importan reseñas que ya existan.
- Textos legales revisados por un abogado en Colombia.

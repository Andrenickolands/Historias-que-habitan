# Contrato de handoff · Historias que Habitan

Versión 1 · 15/11/2026 · De: diseño de producto · Para: Agente Arquitecto de Software y Desarrollo, y los agentes de copy, historias, SEO y legal.

**Estado:** prototipos de diseño en HTML, sin validar con usuarios y sin prueba manual de accesibilidad. Ningún prototipo se declara conforme a WCAG. Todo dato de ejemplo está marcado en pantalla.

## 1. Qué se entrega

| Archivo | Contenido |
|---|---|
| `prototipos/inicio.html` | Inicio |
| `prototipos/categoria.html` | Categoría con filtros, orden, vista de estantería y de cuadrícula |
| `prototipos/ficha-producto.html` | Ficha con variantes, oferta, carrito en hoja, reseñas, visor 3D |
| `prototipos/pago.html` | Pago en tres pasos, regalo, estados de pago y confirmación |
| `prototipos/quiz-orientacion.html` | Cuestionario de orientación y solicitud de cotización por mayor |
| `prototipos/cargas.html` | Demostración del sistema de cargas |
| `prototipos/base.css`, `base.js` | Fuente compartida de inicio y categoría (va incrustada en esos dos HTML) |
| `docs/tokens.json` | Tokens de diseño |
| `docs/arquitectura-informacion.md` | Jerarquía, URLs, navegación, enlaces internos, filtros |
| `docs/sistema-de-cargas.md` | Especificación de cargas y transiciones |
| `Contexto/Historias-que-Habitan-Manual-de-marca.pdf` | Manual de marca; manda sobre todo lo demás. Es material interno: no está en el repositorio público, se pide al equipo |

Añadidas el 17/11/2026: `colecciones.html`, `coleccion.html`, `historias.html`, `historia.html`, `nosotros.html`, `por-mayor.html`, `seguimiento.html`, `pieza-rota.html`, `envios.html`, `cambios-y-garantia.html`, `preguntas.html`, `buscar.html` (sugerencias y tolerancia a errores de escritura), `carrito.html`, `lamparas.html`, `ficha-lampara.html` y tres páginas legales con marcador (`politica-de-datos.html`, `terminos.html`, `politica-de-cookies.html`). Todas llevan el aviso de cookies.

**Pago como invitado (17/11/2026):** el paso 1 pide solo nombre, correo, celular, dirección, datos complementarios (casa, interior, apartamento), barrio o conjunto, ciudad y país. Se quitaron documento y departamento. La cuenta se ofrece después de pagar, con un solo botón que envía un enlace al correo para elegir la contraseña. El indicador Datos · Envío · Pago queda fijo arriba mientras se baja, con el paso actual relleno y los hechos con visto bueno. Si la factura electrónica exige documento, hay que volver a pedirlo [POR CONFIRMAR].

Añadidas el 17/11/2026 con las mismas plantillas: `porcelanas.html`, `flores-artificiales.html`, `mesa.html` con sus subcategorías (`mesa-vajillas.html`, `mesa-cristaleria.html`, `mesa-accesorios.html`), `centros-de-mesa.html`, `esculturas.html`, `decoracion.html` (con acceso a Lámparas), `coleccion-primer-hogar.html` y `coleccion-regalos.html`. Los filtros de cada categoría muestran solo los valores que tienen sus piezas. Los generadores están en `herramientas/`.

Añadidas el 18/11/2026: una ficha por cada pieza del catálogo (`pieza-*.html`, 36) y por cada lámpara (`ficha-lampara.html`, `lampara-2.html` a `lampara-6.html`), todas desde la plantilla `ficha-producto.html`. Cada ficha trae su precio, su oferta con el descuento real, su estado agotado, su miga de pan, su origen y tres piezas de la misma categoría en «Piezas que combinan». Las lámparas de un solo tono ocultan el selector de tono. La pieza viaja de la repisa a su ficha y vuelve desde cualquier categoría o colección. También: `coleccion-protagonistas.html`, tres guías (`historia-pesebre.html`, `historia-anfora.html`, `historia-primer-jarron.html`), `cuenta.html` (ingreso con enlace al correo, pedidos, datos de envío, comunicaciones y cerrar sesión) y `404.html`. Las fichas tienen ahora el mismo menú y la misma navegación de escritorio que las demás páginas.

**Diseño completo en prototipo.** Lo que falta ya no es diseño de pantallas: es contenido real, decisiones del negocio, construcción en la plataforma y pruebas con personas (secciones 2, 8 y 13).

## 2. Decisiones del negocio que bloquean

| Decisión | Afecta a |
|---|---|
| Plataforma: Shopify o Next.js | URLs, pago, filtros, estantería en React (sección 9) |
| Pasarela y medios de pago; contraentrega | Paso 3 del pago |
| Operador logístico, tarifas y tiempos | Calculadora de envío, paso 2, confirmación |
| Política de roturas, cambios, garantía y retracto | Ficha, pago, páginas de ayuda |
| Monto del envío gratis y cobertura | Barra del carrito |
| Si se ofrece empaque de regalo y su valor | Ficha y pago |
| Condiciones mayoristas | Quiz y página «Por mayor» |
| Logo y monograma en SVG | Cabecera, cargas, pago |
| Número de WhatsApp, dominio, razón social y NIT | Todas las páginas |
| Inventario, precios y fotos reales | Todas las páginas |
| Formato de «Exclusivo»; si la factura exige documento | Ficha; pago |

## 3. Inventario de componentes

| Componente | Propósito | Variantes y estados | Accesibilidad |
|---|---|---|---|
| Cabecera | Marca, menú, buscar, carrito | Móvil con botón de menú; escritorio con cinco enlaces; contador del carrito | Enlace «Saltar al contenido»; el carrito dice «Carrito, 2 piezas» |
| Menú | Navegar y buscar | Panel lateral; categoría actual marcada | `dialog` modal: el foco entra, queda dentro, Esc cierra y vuelve al botón |
| Botón | Acción | Principal (uno por pantalla), secundario, claro sobre fondo oscuro, enlace; ocupado, deshabilitado | Mínimo 48 px de alto; ocupado con `aria-busy` y texto «Aplicando…» |
| Tarjeta de pieza | Llevar a la ficha | Cuadrícula o estantería; normal, oferta, «Exclusivo», agotada, cargando | Un solo enlace por tarjeta; oferta leída como «Ahora… Antes…»; «Agotado» en texto |
| Sello «Exclusivo» | Destacar piezas | Sobre la foto; en la ficha con «¿Qué significa?» | Nunca sugiere escasez; no va en títulos, metadatos ni schema |
| Precio | Mostrar el valor | Normal; oferta con anterior tachado, sello y vigencia | Formato `$189.900`, «IVA incluido»; cambio por variante anunciado en `aria-live` |
| Galería | Ver la pieza | Cuatro tomas: fondo limpio, ambiente, detalle, escala; ampliar | Botones anterior y siguiente, flechas del teclado, «Foto 2 de 4» |
| Selector de variantes | Color, tamaño, acabado, set | Elegida, disponible, agotada | Grupo de radio con `fieldset`; nombre del color en texto; agotada con texto y borde punteado |
| Cantidad | Elegir unidades | 1 a 20 | Botones «Quitar una unidad» y «Agregar una unidad»; campo numérico |
| Barra de compra | Comprar sin subir | Aparece cuando el botón principal no está a la vista | Fija, no desplaza el contenido; el foco no queda tapado |
| Hoja del carrito | Confirmar y seguir | Vacía, con piezas, con envío gratis logrado; dos recomendadas | `dialog` modal; barra de envío con `progress` y texto; cambios anunciados |
| Reseñas | Confianza | Resumen de tres bajo el botón; lista completa; vacío | Estrellas como «4 de 5 estrellas»; sin reseñas reales el bloque no se muestra |
| Ficha técnica | Datos de la pieza | Lista de definiciones | Medidas, peso, material, acabado, cuidados, contenido, origen, garantía |
| Hecho · Diseño · Historia | Relato en tres niveles | Con o sin hecho; tipo de relato: origen, costumbres, por comenzar | `details` nativo; el contenido está en el HTML; el hecho lleva fuente |
| Acordeón | Secciones y preguntas | Abierto, cerrado | `details` y `summary`; anuncia su estado |
| Visor 3D | Girar la pieza | Inicial, cargando, listo, error | Se descarga a pedido; botones para girar y acercar; flechas del teclado |
| Calculadora de envío | Costo y tiempo antes de pagar | Vacía, con resultado, sin ciudad | Etiqueta visible; resultado con `role="status"` |
| Filtros | Acotar la lista | Hoja inferior; material, color, tamaño, ambiente, precio; fichas activas | Casillas y radios nativos; precio sin arrastre; contador en el botón |
| Vista de lista | Estantería o cuadrícula | Dos botones con `aria-pressed` | El cambio se anuncia |
| Campo de formulario | Pedir un dato | Normal, con ayuda, con error | Etiqueta arriba; error junto al campo y en resumen con enlaces; `autocomplete` |
| Pasos del pago | Ubicar a la persona | Actual, hecho, pendiente; paso plegado con «Cambiar» | Lista ordenada con `aria-current="step"` |
| Botón de pago | Pagar y esperar a la pasarela | Verde; normal, procesando (píldora y círculo que gira), aprobado (visto bueno), rechazado | `aria-busy`, formulario `inert` mientras procesa, anuncios en `aria-live`; el rechazo aclara que no hubo cobro |
| Tarjeta del pedido | Mostrar los detalles sin esconderlos | En el pago: piezas y totales; en la confirmación: pedido, fecha, medio de pago, entrega, envío, regalo, piezas y total | Listas y `dl` nativos |
| Cuestionario | Orientar la compra | Portada, pregunta, datos mayoristas, resultado | Una pregunta por pantalla; progreso real; foco al título de cada paso |
| WhatsApp flotante | Ayuda consistente | Mismo lugar en todas las páginas | 56 px; por encima de las barras inferiores |
| Esqueleto y marcador de imagen | Esperas de 1 a 3 s | Tarjeta, ficha, carrito, búsqueda | `aria-busy` y anuncio; fijo con movimiento reducido |

## 4. Presupuesto de rendimiento

Objetivo en celular de gama media con 4G: LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1.

| Qué consume | Regla |
|---|---|
| Fotografía (el mayor consumo) | AVIF o WebP, tamaños responsivos, menos de 300 KB por foto; la principal en el HTML con prioridad; el resto diferidas; proporción fija 4:5 |
| Fuentes | Tres archivos (Cormorant variable, Cormorant cursiva, Jost variable), subconjunto latino, `font-display: swap`; alojarlas en el dominio propio |
| Visor 3D | 163 KB de script solo al tocar el botón; modelo de hasta 3 MB [POR CONFIRMAR]; solo en piezas con modelo |
| Estantería | Fotos recortadas con transparencia pesan más: WebP o AVIF con canal alfa |
| Cargas y transiciones | Unos 6 KB en total, sin librerías |
| Terceros | Analítica y píxeles diferidos; nada bloquea la primera pintura |
| Componentes estables | Barras fijas, hoja del carrito, WhatsApp y banner de cookies van encima; no desplazan contenido |

Peso objetivo de la ficha, sin el 3D: [POR CONFIRMAR con desarrollo]. Propuesta: menos de 900 KB en la primera carga. No se ha medido nada: los prototipos no son un build.

## 5. Recorridos críticos para pruebas de extremo a extremo

1. **De Instagram a la compra:** abrir la ficha exacta en el navegador interno de Instagram y de TikTok → elegir variante → agregar → hoja del carrito → pagar como invitado con Nequi o PSE → confirmación.
2. **Compra de regalo:** agregar → pago → marcar «Es un regalo» → datos de quien recibe y mensaje → empaque → confirmar que el total cambia y que la dirección se pide una vez.
3. **Pieza rota:** desde la confirmación o el pie → reportar con número de pedido y foto → recibir respuesta. (Página por diseñar.)
4. **Solicitud por mayor:** «Por mayor» → cuestionario → datos → WhatsApp con el resumen escrito.
5. **Encontrar y filtrar:** categoría → filtrar por material y precio → sin resultados → borrar filtros → ficha.
6. **Pago rechazado:** intentar pagar → rechazo → cambiar de medio sin volver a escribir datos.
7. **Solo teclado y lector de pantalla:** repetir el recorrido 1 completo.

## 6. Visibilidad: SEO, respuestas e IA

Skills según la fase: arquitectura con `/marketing-skills:site-architecture`; estrategia con `/claude-seo:seo-plan`; marcado con `/marketing-skills:schema`; páginas desde datos con `/marketing-skills:programmatic-seo`. Con URL o build: `/claude-seo-ai:audit`, `/claude-seo:seo audit`, `/geo audit`, `/web-quality-skills:core-web-vitals`.

- **En el HTML del servidor:** nombre, precio, disponibilidad, variantes, envío, ficha técnica, historia y preguntas. Los acordeones usan `details`, así que su texto está en el documento.
- **Datos estructurados:** Product o ProductGroup con variantes, Offer en COP con IVA, BreadcrumbList, FAQPage con las preguntas visibles, detalles de envío, MerchantReturnPolicy y Organization. Sin AggregateRating ni Review hasta tener reseñas reales. Organization no menciona ningún otro negocio.
- **Rastreo:** `noindex` en búsqueda, carrito, pago, seguimiento y pasos internos del cuestionario; canonical en filtros; sitemap; decisión explícita sobre rastreadores de IA en robots.txt; `llms.txt` solo como experimento.
- **Feeds:** Google Merchant Center y catálogo de Pinterest, con el mismo precio y disponibilidad que la página.
- **Búsqueda visual:** cuatro fotos por pieza, la principal sin texto encima; botón «Guardar en Pinterest».
- **hreflang:** no aplica. **Tienda física:** no existe; no crear página de local ni dirección.

## 7. Eventos de analítica

Los prototipos ya los envían a `dataLayer`.

| Evento | Cuándo |
|---|---|
| `ver_producto` | Al abrir una ficha (por añadir) |
| `abrir_historia` | Al abrir «Hecho, diseño e historia» |
| `ver_3d` | Al cargar el visor |
| `agregar_al_carrito`, `agregar_recomendada` | Al agregar desde la ficha o desde la hoja |
| `filtrar`, `cambiar_vista` | En la categoría |
| `iniciar_pago`, `elegir_envio`, `agregar_pago`, `compra` | En el pago |
| `quiz_inicio`, `quiz_paso`, `quiz_resultado`, `quiz_whatsapp` | En el cuestionario |
| `cotizacion_mayorista_lista` | Al terminar la solicitud por mayor |
| Por añadir | `busqueda_interna`, `busqueda_sin_resultados`, `guardar_pinterest`, `reportar_pieza_rota` |

Medir además el origen del tráfico: Instagram, TikTok, Pinterest, buscadores y asistentes de IA.

**Cómo se mide el éxito:** conversión; abandono por paso del pago; tiempo hasta completar la compra; uso y fracaso del buscador; apertura de la historia y su relación con la compra; uso del cuestionario y compra posterior; SUS en pruebas; reportes de piezas rotas; quejas relacionadas con la web. No se fijan metas hasta tener datos.

## 8. Contenido pendiente y responsables

| Contenido | Responsable | Skill sugerida |
|---|---|---|
| Nombres, descripciones y respuesta breve de cada pieza | Copy | `/marketing-skills:copywriting`, `/anthropic-skills:brand-voice` |
| Hecho · Diseño · Historia por pieza, con fuentes verificadas | Historias de producto | Redacción en tres niveles; ningún hecho sin fuente |
| Textos de categoría, preguntas frecuentes, guías de «Historias» | SEO y contenido | `/claude-seo:seo-plan`, `/claude-blog:blog write "<tema>"` |
| Términos, tratamiento de datos, retracto, garantía, roturas, cookies | Legal, con abogado en Colombia | `/legal:compliance-check` |
| Fotos reales: cuatro tomas por pieza y recorte para la estantería | Marca | — |
| Modelos 3D de las piezas protagonistas | Marca | — |
| Reseñas reales, con fecha y permiso | Posventa | `/anthropic-skills:d2c-marketing` |

## 9. Estantería en React (componente «Product Shelf» que pidió el cliente)

El cliente entregó un componente de React, «Product Shelf» de Aakash Mehra, para la categoría y el estante de productos. El proyecto hoy es HTML sin React, Tailwind ni TypeScript, así que en los prototipos se adaptó la idea en CSS: las piezas se apoyan en repisas, con sus tamaños relativos. Al tocar una pieza, esta viaja de la repisa a la ficha y, al volver, regresa a su lugar. Se hace con View Transitions entre páginas (`@view-transition`, `view-transition-name: pieza`, 550 ms, curva de salida), sin librerías y con cada pieza en su propia URL. Solo funciona servido por HTTP, no al abrir los archivos sueltos; sin soporte del navegador o con movimiento reducido, la navegación es normal. Las piezas dibujadas son ilustraciones de ejemplo que ocupan el lugar de las fotos recortadas. Para usar el componente original:

**Requisitos (solo si la plataforma es Next.js o React):**

1. Crear el proyecto con TypeScript y Tailwind: `npx create-next-app@latest --typescript --tailwind`.
2. Iniciar shadcn: `npx shadcn@latest init`. Deja los componentes en `components/ui` y crea `lib/utils.ts` con `cn`. Esa carpeta importa porque el componente importa desde `@/lib/utils` y las demás piezas de shadcn se instalan ahí.
3. Instalar dependencias: `npm install motion lucide-react`.
4. Copiar el archivo a `components/ui/skincare-product-shelf.tsx`.

En Shopify con tema Liquid no se puede usar tal cual; solo en Hydrogen o como isla de React.

**Qué hay que cambiar antes de usarlo:**

| En el componente | Cambio |
|---|---|
| Dibujos SVG de cosméticos (frasco, tubo, gotero) | Reemplazar por fotos reales recortadas de cada pieza; los dibujos no representan el catálogo |
| Marca «SKASMAN» impresa y en la cabecera | Quitar; usar el logo de Historias que Habitan |
| Calificaciones y número de reseñas de ejemplo | Quitar hasta tener reseñas reales |
| «Free delivery», «Pickup at most stores» | Quitar: no hay tienda física y el envío se calcula por ciudad |
| Precios en dólares, textos en inglés | Pesos colombianos con IVA, español de Colombia, trato de usted |
| Cuatro columnas fijas, también en celular | Dos columnas en celular: a 375 px cada pieza quedaría de unos 80 px |
| Ficha dentro de un diálogo | Cada pieza necesita su URL propia y su HTML en el servidor; el diálogo solo no sirve para SEO ni para llegar desde redes |
| Arrastrar para girar | Añadir botones y teclado; arrastrar no puede ser la única forma |
| Tipos de letra y colores | Tokens de `docs/tokens.json` |
| Crédito del autor y licencia | Confirmar la licencia de uso comercial antes de publicar |

Lo que sí conviene conservar: la pieza que viaja del estante a la ficha, los resortes sin rebote y el fundido con movimiento reducido.

## 10. Reporte de accesibilidad

Probado con medición de contraste, revisión del código y recorridos automatizados a 375 px. **No se hizo prueba manual** con teclado, lector de pantalla, zoom ni movimiento reducido.

| Criterio WCAG | Nivel | Dónde | Estado | Nota |
|---|---|---|---|---|
| 1.4.3 Contraste | AA | Todos | Medido, pasa | El par más justo: café humo sobre oatmeal, 4.64:1 |
| 1.4.11 Contraste de no texto | AA | Controles | Medido, pasa | Bordes en café humo (6.03:1); perla solo en líneas decorativas |
| 1.4.1 Uso del color | A | Agotado, oferta, error | Revisado en código | Siempre con texto o ícono |
| 1.3.1, 4.1.2 Estructura, nombre y rol | A | Todos | Revisado en código | HTML nativo; falta lector de pantalla |
| 2.1.1 Teclado | A | Todos | Sin probar | Visor 3D y galería tienen teclado en el código |
| 2.4.7, 2.4.11 Foco visible y no tapado | AA | Barras fijas | Sin probar | Hay margen de desplazamiento; falta comprobarlo |
| 2.5.7 Arrastre | AA | Galería, 3D, filtros | Revisado en código | Todos tienen botones |
| 2.5.8 Tamaño del objetivo | AA | Todos | Medido a 375 px, pasa | Ninguno por debajo de 24 px |
| 1.4.10, 1.4.4 Reflujo y zoom | AA | Todos | Parcial | Sin desborde a 375 px; faltan 320 px, 200 % y 400 % |
| 2.3.3, 2.2.2 Movimiento | AA | Cargas | Sin probar | Versiones reducidas escritas |
| 3.3.1, 3.3.3 Errores | A, AA | Pago, cotización | Recorrido automatizado, pasa | Error junto al campo y resumen |
| 3.3.7 Entrada redundante | A | Pago | Revisado | Dirección una vez; «mismos datos para la factura» |
| 3.3.8 Autenticación accesible | AA | — | No aplica | Compra sin cuenta |
| 3.2.6 Ayuda consistente | A | Todas | Revisado | WhatsApp en el mismo lugar |
| 4.1.3 Mensajes de estado | AA | Carrito, filtros, precio | Revisado en código | Falta oírlos con lector de pantalla |

Pendiente conocido: el botón de WhatsApp puede quedar sobre el borde de un campo al desplazarse en el pago.

## 11. Revisión heurística

| Heurística | Estado | Comentario |
|---|---|---|
| 1. Estado del sistema | ✅ | Pasos del pago, contador del carrito, cargas |
| 2. Lenguaje del usuario | ⚠️ | Nombres de categoría sin validar con card sorting |
| 3. Control y libertad | ✅ | «Cambiar» en el pago, quitar del carrito, borrar filtros |
| 4. Consistencia y estándares | ✅ | Carrito a la derecha, logo al inicio |
| 5. Prevención de errores | ✅ | Requisitos antes del error; pago sin doble pulsación |
| 6. Reconocer antes que recordar | ⚠️ | Faltan vistos recientemente y favoritos guardados |
| 7. Flexibilidad y eficiencia | ⚠️ | Falta recompra y pedido rápido para mayoristas |
| 8. Estética y minimalismo | ✅ | Un botón principal por pantalla |
| 9. Recuperarse de errores | ✅ | Mensajes con causa y solución |
| 10. Ayuda | ⚠️ | WhatsApp visible; faltan las páginas de ayuda |

## 12. Listas de comprobación

**Reglas de marca**

| Regla | Estado |
|---|---|
| 1. Origen honesto | ✅ «Hecho en China» en ficha técnica y tarjetas |
| 2. Nada inventado | ✅ Todo dato de ejemplo va marcado; sin reseñas ni cifras falsas |
| 3. La historia acompaña la compra | ✅ Compra arriba; historia en sección propia |
| 4. Tres niveles | ✅ Rótulo y tipografía distintos; el hecho exige fuente |
| 5. Tres tipos de relato | ✅ Rótulo «Tipo de relato»; la ficha funciona sin hecho |
| 6. «Exclusivo» | ✅ Solo visual, con explicación; formato por confirmar |
| 7. Lenguaje prohibido | ✅ No aparece en los prototipos |
| 8. Confidencialidad | ✅ Ningún otro negocio aparece |
| 9. Colecciones por experiencia | ✅ |
| 10. Partir del concepto existente | ✅ Tokens y voz del manual |

**Esenciales de ecommerce**

| Punto | Estado |
|---|---|
| Buscador con autocompletado y tolerancia a errores | ❌ Solo el campo; falta diseñarlo |
| Filtros y orden en móvil | ✅ |
| Carrito desde cualquier página, con edición y regalo | ⚠️ Hoja en la ficha; falta el carrito completo |
| Pago como invitado con progreso | ✅ |
| Medios de pago visibles antes del pago | ✅ En ficha e inicio, por confirmar |
| Precios en formato colombiano con IVA | ✅ |
| WhatsApp consistente | ✅ |
| Acceso mayorista separado | ⚠️ En el cuestionario; falta la página «Por mayor» |
| Confirmación y seguimiento | ⚠️ Confirmación sí; seguimiento por diseñar |
| Plan de eventos | ✅ |

**Patrones oscuros:** sin falsa escasez ni urgencia ✅ · sin costos ocultos ✅ · sin casillas premarcadas de pago o consentimiento ✅ · sin confirmshaming ✅ · sin botones engañosos ✅ · sin reseñas inventadas ✅ · sin progreso falso ✅ · baja de suscripción: N/A, no hay suscripciones.

**Visibilidad:** un H1 y jerarquía ✅ · migas ✅ · enlaces reales ✅ · URLs legibles ✅ (documento) · filtros controlados ✅ (documento) · respuesta breve al inicio ✅ · preguntas en HTML ✅ · ficha técnica estructurada ✅ · fechas y autor en guías ✅ (espacio previsto) · compra como invitado ✅ · velocidad medida ❌ (no hay build) · local N/A.

## 13. Hipótesis por validar y plan

| Hipótesis | Cómo se valida | Con quién | Qué se observa |
|---|---|---|---|
| Se entiende qué vende la tienda | Prueba de 5 segundos del inicio | 10 personas | Que digan «decoración» u «objetos para la casa» |
| La compra se completa en celular | Prueba moderada: de una publicación a la confirmación | 5 del perfil detal, incluidas dos señoras mayores | Éxito, tiempo, dudas, SUS |
| La historia ayuda y no estorba | Observar si abren «Hecho, diseño e historia» | Las mismas 5 | Apertura y comentarios |
| El cuestionario orienta | Tarea: «no sabe qué regalar» | Las mismas 5 | Si llegan a una pieza |
| La estantería se entiende | Comparar estantería y cuadrícula | Las mismas 5 | Cuál prefieren y si encuentran más rápido |
| El 3D aporta | Ofrecerlo en una pieza | Las mismas 5 | Si lo usan y si aclara el tamaño |
| Los nombres de categoría son claros | Card sorting | 8 a 10 | Acuerdo en los grupos |
| El flujo mayorista sirve | Prueba aparte | 3 comercios | Si piden cotización sin ayuda |
| Funciona en navegadores internos | Prueba técnica en Instagram y TikTok | Desarrollo | Pago completo sin bloqueos |

Pruebas A/B: solo cuando haya tráfico suficiente.

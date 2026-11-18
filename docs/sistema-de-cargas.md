# Sistema de cargas y transiciones · Historias que Habitan

Versión 1 · 15/11/2026 · Demostración: `prototipos/cargas.html`
Skills aplicadas: `make-interfaces-feel-better`, `vectorlab-ux-skills:loaders`, `web-interface-guidelines`.

**Regla de oro:** la animación de marca hace que la espera se sienta corta, pero nunca alarga la espera real ni retrasa el contenido.

**Pendiente que afecta a todo el sistema:** el monograma de la demostración es un marcador dibujado a partir de la descripción del manual (H externa, arco de la puerta, estrella). Se reemplaza por los trazos del logo vectorizado. [MONOGRAMA SVG PENDIENTE]

## 1. Qué mostrar según la espera real

| Espera | Qué se muestra |
|---|---|
| Menos de 100 ms | Nada. El indicador se retrasa 100 ms para que las respuestas rápidas no parpadeen. |
| 100 ms a 1 s | Indicador dentro del control: el botón dice «Aplicando…» con `aria-busy`. |
| 1 a 3 s | Esqueleto con la forma real del contenido, o marcador de imagen. |
| Más de 3 s | Mensaje con la voz de la marca y progreso solo si el avance es real. |
| Pago | Aviso que bloquea, con mensaje tranquilo; no se puede pulsar dos veces. |

## 2. Tokens de movimiento

```css
--t-instante: 100ms;  /* respuesta al toque, retraso del indicador */
--t-rapida:   200ms;  /* cambios de estado, fundidos */
--t-media:    300ms;  /* transición entre páginas, aparición de fotos, hojas y paneles */
--t-lenta:    400ms;  /* recorridos largos: la pieza que viaja al carrito */
--t-marca:    800ms;  /* carga inicial de marca, una sola vez */
--t-brillo:   1500ms; /* brillo del esqueleto */
--c-salida: cubic-bezier(.2, .7, .2, 1);  /* entradas, salidas y transiciones de página */
--c-estado: cubic-bezier(.2, 0, 0, 1);    /* cambios de estado de un control */
```

Sin rebotes. Solo se animan `opacity`, `translate`, `scale`, `filter` y el trazo del SVG. Nunca `transition: all`. Presión de botón: `scale: .96`.

## 3. Especificación por pieza

### 3.1 Transición entre páginas

| | |
|---|---|
| Guion | 1) Tarjeta en la lista. 2) La foto crece y se mueve hasta ocupar el lugar de la foto de la ficha. 3) El resto se funde. Al volver, el recorrido inverso. |
| Aparece | Al tocar una tarjeta de pieza o «Volver». |
| Termina | A los 300 ms. Si la página nueva tarda, se ve el esqueleto de la ficha. |
| Duración y curva | 300 ms, salida. |
| Marca | La fotografía de la pieza es la protagonista. |
| Movimiento reducido | Cambio inmediato, sin recorrido. |
| Técnica | View Transitions en CSS (`@view-transition` entre páginas y `view-transition-name` en la foto). Sin soporte: fundido de 200 ms. |
| Peso | 0 KB de script. |

### 3.2 Carga inicial de marca

| | |
|---|---|
| Guion | 0–450 ms: la H se dibuja con trazo fino. 350–600 ms: aparece la estrella, la luz. 600–800 ms: las dos hojas de la puerta se abren hacia los lados y dejan ver la página. |
| Aparece | Solo en la primera visita y solo si la carga tarda más de 1 s. |
| Termina | A los 800 ms, o de inmediato si el contenido llega antes (fundido de 100 ms). Nunca en cada navegación. |
| Duración y curva | 800 ms en total, salida. |
| Marca | Monograma H, estrella y la idea de la puerta que se abre. |
| Movimiento reducido | H fija y fundido de 200 ms. |
| Técnica | SVG en línea con `stroke-dashoffset` y CSS. Va encima del contenido: el título, la foto principal y el botón se pintan debajo sin esperar. |
| Peso | Menos de 2 KB. |

### 3.3 Esqueletos de marca

| | |
|---|---|
| Guion | Bloques en oatmeal con la forma de la tarjeta, la ficha, el carrito y la búsqueda; un brillo claro los recorre. Al llegar el contenido, fundido de 200 ms. |
| Aparece | Cuando la espera supera 1 s. |
| Termina | Al llegar el contenido. |
| Duración y curva | Brillo de 1,5 s en bucle, lineal. |
| Marca | Colores de la paleta (oatmeal sobre blanco hueso). |
| Movimiento reducido | Bloques fijos, sin brillo. |
| Técnica | CSS. La región lleva `aria-busy="true"` y un anuncio «Cargando piezas…». |
| Peso | Menos de 1 KB. |

### 3.4 Marcadores de imagen

| | |
|---|---|
| Guion | El espacio de la foto está reservado con su proporción y pintado con el color dominante. La foto aparece con un fundido. |
| Aparece | Mientras carga cada foto. |
| Termina | Al cargar la foto. |
| Duración y curva | 300 ms, salida. |
| Marca | Tonos greige del manual. |
| Movimiento reducido | La foto aparece sin fundido. |
| Técnica | `aspect-ratio` o `width` y `height` en la imagen, color de fondo por foto. La foto principal carga con prioridad; las demás, diferidas. |
| Peso | Un color por foto. |

### 3.5 Microinteracciones

| Acción | Guion | Duración y curva | Movimiento reducido | Anuncio |
|---|---|---|---|---|
| Agregar al carrito | Una miniatura viaja de la foto al ícono del carrito; el contador sube; el botón dice «Agregada» 1,3 s. En la ficha, además, sube la hoja del carrito. | 400 ms salida; contador 200 ms | Sin viaje: cambian el contador y el texto | «Pieza agregada al carrito. 2 en total.» |
| Favoritos | El corazón de línea cambia a relleno con fundido y escala de 0,25 a 1. | 200 ms estado | Cambio sin escala | Texto «Guardada en favoritos» y `aria-pressed` |
| Aplicar cupón | Botón ocupado con «Aplicando…» si tarda más de 100 ms; luego mensaje de éxito o de error junto al campo. | Lo que tarde la respuesta | Sin giro | Mensaje con `role="status"` |
| Filtros | La ficha del filtro cambia de color y el contador se actualiza. | 100 a 200 ms estado | Igual | «3 piezas» |

Técnica: transiciones CSS. Peso: menos de 1 KB de script. El movimiento nunca es la única señal: siempre cambian un texto, un ícono o un número.

### 3.6 Estado de pago

| | |
|---|---|
| Guion | El botón verde «Pagar $X» se parte en una píldora que dice «Procesando…» y un círculo con un indicador que gira. Encima aparece «No cierre ni recargue esta página». Al aprobarse, el círculo dibuja un visto bueno y la píldora dice «Pago aprobado». Luego se muestra la confirmación con el detalle del pedido. (Versión 2; reemplaza al aviso centrado con la H.) |
| Aparece | Al pulsar «Pagar», mientras responde la pasarela. |
| Termina | Con la confirmación o con el error «No pudimos procesar el pago. No se hizo ningún cobro». |
| Duración y curva | 600 a 700 ms para partirse, 450 ms el visto bueno, curva de salida. El giro dura lo que tarde la pasarela. |
| Marca | Monograma H. |
| Movimiento reducido | Cambio de texto e ícono sin movimiento. |
| Técnica | CSS y un filtro SVG que une las dos formas. El formulario queda `inert` y el botón con `aria-busy` mientras procesa; los cambios se anuncian en `aria-live`. Sin barra de progreso, porque el avance no se conoce. En el prototipo la espera es simulada (1,5 s); en producción no se añade espera. |
| Peso | Menos de 1 KB. |

### 3.7 Sin conexión o error de carga

| | |
|---|---|
| Guion | H fija con la estrella apagada, «No hay conexión», «Lo que tiene en el carrito sigue guardado» y el botón «Reintentar». |
| Aparece | Cuando falla la red o una carga. |
| Termina | Al recuperar la conexión o al reintentar con éxito. |
| Duración y curva | Sin animación. El botón dice «Reintentando…» mientras prueba. |
| Marca | Monograma H. |
| Movimiento reducido | Igual. |
| Técnica | SVG fijo y texto. |
| Peso | Menos de 1 KB. |

## 4. Accesibilidad

- `prefers-reduced-motion`: cada pieza tiene su versión fija o con fundido (columna de cada tabla).
- Regiones que cargan: `aria-busy="true"` y anuncio en `aria-live`.
- Ninguna animación parpadea más de tres veces por segundo ni se mueve más de cinco segundos seguidos.
- El foco se conserva o se mueve al título de lo nuevo; nunca se pierde tras una transición.

## 5. Para desarrollo

1. Peso total del sistema: unos 5 KB de CSS y 1 KB de script, sin librerías. No se necesita GSAP, Motion ni Lottie.
2. Los prototipos de ficha, pago, inicio y categoría usan hoy 200 y 300 ms con la curva de salida, que coinciden con estos tokens; falta nombrarlos con las variables de este documento.
3. El selector «Cámara lenta (10 %)» de la demostración sirve para revisar cada animación; no va en producción.
4. Medir con `/web-quality-skills:core-web-vitals` cuando exista un build: la carga inicial de marca no puede retrasar el LCP ni mover el contenido.

## 6. Qué se probó

- Probado en la demostración a 375 px: las siete piezas responden, el telón termina solo y se corta al llegar el contenido, el cupón muestra «Aplicando…» y luego éxito o error, el contador y los filtros se actualizan, sin desborde horizontal.
- Sin probar: la simulación de movimiento reducido, la cámara lenta, navegadores sin View Transitions, lector de pantalla y celulares de gama media.

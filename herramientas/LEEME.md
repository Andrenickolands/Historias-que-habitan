# Generadores de los prototipos

Estos scripts generan las páginas de `prototipos/` que comparten cabecera, menú, pie, aviso de cookies y estilos.
Se editan a mano: `ficha-producto.html` (plantilla de las fichas), `pago.html`, `quiz-orientacion.html` y `cargas.html`.

| Archivo | Qué genera |
|---|---|
| `construir_paginas.py` | Inicio, Jarrones y recipientes, Lámparas; incrusta `base.css` y `base.js`; enlaza las páginas entre sí |
| `paginas_extra.py` | Colecciones, Historias, Nosotros, Por mayor, seguimiento, pieza rota, ayuda, búsqueda, carrito y legales |
| `paginas_cat.py` | Porcelanas, Flores, Mesa y sus tres subcategorías, Centros de mesa, Esculturas, Decoraciones, Primer hogar y Regalos |
| `arte.py` | Las ilustraciones de ejemplo de las piezas |
| `paginas_mas.py` | Piezas protagonistas, tres guías, Mi cuenta y la página de error |
| `fichas.py` | Una ficha por cada pieza (`pieza-*.html`) y por cada lámpara (`ficha-lampara.html`, `lampara-*.html`), a partir de `ficha-producto.html` |
| `construir_ficha_lampara.py` | La plantilla de lámpara; la llama `fichas.py` |

Para regenerar todo, desde la carpeta del proyecto:

```bash
python herramientas/construir_paginas.py prototipos
```

`ficha-producto.html` es la plantilla de todas las fichas: si cambia, hay que volver a correr el comando.
Cada tarjeta con precio crea su ficha automáticamente; el nombre del archivo sale del nombre de la pieza.

## Copy deck del inicio

`copy_deck_home.py` arma `docs/copy-deck-home.md` con los textos de la tabla y `copy_deck_home_plantilla.md`, y revisa límites de palabras, palabras prohibidas, CTA genéricos y tuteo:

    python herramientas/copy_deck_home.py docs/copy-deck-home.md herramientas/copy_deck_home_plantilla.md

## Galería de colecciones

`galeria_colecciones.py` arma `prototipos/galeria-colecciones.html`: una escena por colección con un punto sobre cada pieza. Las piezas, posiciones y escalas están en `COLECCIONES`; los dibujos salen de `arte.py`.

    python herramientas/galeria_colecciones.py prototipos

## Secciones 1, 4 y 6 del wireframe del inicio

`inicio_secciones.py` escribe en `prototipos/inicio-estructura.html` el hero que se arma por capas, los arcos de «¿Qué lo trae hoy?» y las tarjetas de categorías con flechas. Cada bloque va entre marcadores `hero`, `arcos`, `vitrina` y `vitrina-js`. Después de correr `galeria_colecciones.py`:

    python herramientas/inicio_secciones.py prototipos

## Catálogo de estados (oferta, quedan pocas, agotada)

`catalogo.py` es la única fuente del precio anterior y de las unidades de cada pieza. Lo leen `construir_paginas.py` (tarjetas, fichas, búsqueda, Descuentos), `inicio_secciones.py` (estantería del inicio) y `galeria_colecciones.py`. Para cambiar un estado se edita `ESTADO` y se vuelve a construir todo:

    python herramientas/construir_paginas.py prototipos
    python herramientas/galeria_colecciones.py prototipos
    python herramientas/inicio_secciones.py prototipos

## Cabecera, menú y pie (sitio.py)

`sitio.py` es la única fuente de la cabecera (con Lo nuevo, Descuentos, cuenta, favoritos y carrito), los atajos de celular, el menú lateral y el pie con el boletín, con sus estilos (`SITIO_CSS`) y su comportamiento (`SITIO_JS`: cuenta, contador del carrito, favoritos, avisos de llegada y boletín). Llega a tres lugares:

- las páginas de `construir_paginas.py`, por `cabecera()` y `PIE`;
- la plantilla `prototipos/ficha-producto.html`, con `sincronizar()` antes de copiarla a todas las fichas y lámparas;
- el inicio aprobado, que lo inyecta `inicio_secciones.py`.

La página «Mis favoritos» la arma `favoritos_pagina.py`. En el navegador, el prototipo guarda `hqh-favoritos`, `hqh-avisos`, `hqh-sesion` y `hqh-bienvenida`. Después de cambiar `sitio.py` se vuelve a construir todo:

    python herramientas/construir_paginas.py prototipos
    python herramientas/galeria_colecciones.py prototipos
    python herramientas/inicio_secciones.py prototipos

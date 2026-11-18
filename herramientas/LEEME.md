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

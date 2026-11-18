# Generadores de los prototipos

Estos scripts generan las páginas de `prototipos/` que comparten cabecera, menú, pie, aviso de cookies y estilos.
Las demás (`ficha-producto.html`, `pago.html`, `quiz-orientacion.html`, `cargas.html`) se editan a mano.

| Archivo | Qué genera |
|---|---|
| `construir_paginas.py` | Inicio, Jarrones y recipientes, Lámparas; incrusta `base.css` y `base.js`; enlaza las páginas entre sí |
| `paginas_extra.py` | Colecciones, Historias, Nosotros, Por mayor, seguimiento, pieza rota, ayuda, búsqueda, carrito y legales |
| `paginas_cat.py` | Porcelanas, Flores, Mesa y sus tres subcategorías, Centros de mesa, Esculturas, Decoraciones, Primer hogar y Regalos |
| `arte.py` | Las ilustraciones de ejemplo de las piezas |
| `construir_ficha_lampara.py` | `ficha-lampara.html`, a partir de `ficha-producto.html` |

Para regenerar todo, desde la carpeta del proyecto:

```bash
python herramientas/construir_paginas.py prototipos
python herramientas/construir_ficha_lampara.py prototipos
```

Si cambia `ficha-producto.html`, hay que volver a correr el segundo comando.

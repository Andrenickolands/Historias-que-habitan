"""Genera docs/copy-deck-home.md desde copy_deck_home_plantilla.md, con conteo de caracteres y revisión automática.
Uso: python herramientas/copy_deck_home.py docs/copy-deck-home.md herramientas/copy_deck_home_plantilla.md"""
import io, re, sys

SALIDA = sys.argv[1]

# Límite de palabras por tipo de elemento (del prompt v3)
LIM = {'h1': 8, 'sub': 20, 'apoyo': 25, 'confianza': 5, 'cat': 6, 'paso': 12}

# (sección, elemento, copy, intención, variante, tipo de límite o None). Orden del inicio aprobado el 18/11/2026
D = [
    ('Global · Anuncio y cabecera', 'Barra de anuncio', 'Envío gratis en pedidos desde $300.000 [POR CONFIRMAR: monto y cobertura]', 'actuar', 'A', None),
    ('Global · Anuncio y cabecera', 'Barra de anuncio (si no hay envío gratis)', 'Enviamos a todo el país, con embalaje para piezas frágiles', 'confiar', 'B', None),
    ('Global · Anuncio y cabecera', 'Buscador: etiqueta', 'Buscar en la tienda', 'actuar', '', None),
    ('Global · Anuncio y cabecera', 'Buscador: texto de ejemplo', 'Buscar jarrones, copas, lámparas…', 'actuar', '', None),
    ('Global · Modal de bienvenida (variante D)', 'Antetítulo', 'Boletín', 'atrapar', '', 'apoyo'),
    ('Global · Modal de bienvenida (variante D)', 'H2', 'Nuevas piezas y nuevas ofertas', 'atrapar', '', None),
    ('Global · Modal de bienvenida (variante D)', 'Línea', 'Suscríbase y entérese de todo. Le avisamos sobre ofertas exclusivas y nuestros nuevos productos.', 'desear', '', 'apoyo'),
    ('Global · Modal de bienvenida (variante D)', 'Ayuda del celular', 'Diez dígitos. Por ahí le avisamos por WhatsApp.', 'confiar', '', None),
    ('Global · Modal de bienvenida (variante D)', 'Ayuda de la empresa (opcional)', 'Si compra para un negocio, le contamos también sobre los precios al por mayor.', 'confiar', '', 'apoyo'),
    ('Global · Modal de bienvenida (variante D)', 'Casilla de datos', 'Autorizo el tratamiento de mis datos para recibir novedades y ofertas por correo y WhatsApp, según la política de privacidad.', 'confiar', '', None),
    ('Global · Modal de bienvenida (variante D)', 'Botón principal', 'Sí, quiero suscribirme', 'actuar', '', None),
    ('Global · Modal de bienvenida (variante D)', 'Botón secundario (grande, con borde)', 'Por el momento no', 'actuar', '', None),
    ('Global · Modal de bienvenida (variante D)', 'Letra chica', 'Puede darse de baja cuando quiera, desde cualquier correo.', 'confiar', '', None),
    ('Global · Modal de bienvenida (variante D)', 'Confirmación', 'Listo, le avisaremos. Le escribiremos a [correo] y por WhatsApp al [celular] cuando lleguen piezas nuevas o haya ofertas.', 'confiar', '', None),

    ('1 · Hero 3D', 'Antetítulo (manual de marca)', 'Hay objetos que no solo decoran. Cuentan historias.', 'atrapar', '', None),
    ('1 · Hero 3D', 'H1', 'Piezas que se miran desde todos sus lados', 'atrapar', 'A (elegida)', 'h1'),
    ('1 · Hero 3D', 'H1', 'Sepa cómo es la pieza antes de comprarla', 'confiar', 'B (prueba)', 'h1'),
    ('1 · Hero 3D', 'Subtítulo', 'Esculturas, porcelanas, jarrones y lámparas para su casa. De cada pieza le contamos material, medidas y origen.', 'desear', 'A y B', 'sub'),
    ('1 · Hero 3D', 'CTA principal (lleva a la tienda)', 'Ver todas las piezas', 'actuar', '', None),
    ('1 · Hero 3D', 'Etiqueta de la pieza en la escena', 'Escultura curva blanca · $179.900', 'desear', '', None),
    ('1 · Hero 3D', 'CTA secundario', 'Ayúdeme a elegir', 'actuar', '', None),
    ('1 · Hero 3D', 'Pista (escritorio)', 'Baje para verla armarse y girar', 'atrapar', '', None),
    ('1 · Hero 3D', 'Nombre accesible de la escena', 'Escultura curva blanca sobre un pedestal, en una sala con luz de tarde', 'confiar', '', None),

    ('2 · Categorías por tipo (arcos)', 'H2', 'Elija por tipo de pieza', 'actuar', '', None),
    ('2 · Categorías por tipo (arcos)', 'Apoyo', 'Siete categorías, de la porcelana a las lámparas. Cada pieza tiene su ficha con material, medidas y origen.', 'confiar', '', 'apoyo'),
    ('2 · Categorías por tipo (arcos)', 'Porcelanas y figuras: línea', 'Figuras y piezas para la repisa', 'desear', '', 'cat'),
    ('2 · Categorías por tipo (arcos)', 'Porcelanas y figuras: CTA', 'Ver porcelanas', 'actuar', '', None),
    ('2 · Categorías por tipo (arcos)', 'Jarrones y recipientes: línea', 'Para flores, ramas o solos', 'desear', '', 'cat'),
    ('2 · Categorías por tipo (arcos)', 'Jarrones y recipientes: CTA', 'Ver jarrones', 'actuar', '', None),
    ('2 · Categorías por tipo (arcos)', 'Flores artificiales: línea', 'Ramos que no se marchitan', 'desear', '', 'cat'),
    ('2 · Categorías por tipo (arcos)', 'Flores artificiales: CTA', 'Ver flores', 'actuar', '', None),
    ('2 · Categorías por tipo (arcos)', 'Mesa: línea', 'Vajillas, copas y accesorios para servir', 'desear', '', 'cat'),
    ('2 · Categorías por tipo (arcos)', 'Mesa: CTA', 'Ver la mesa', 'actuar', '', None),
    ('2 · Categorías por tipo (arcos)', 'Centros de mesa: línea', 'Para el centro del comedor', 'desear', '', 'cat'),
    ('2 · Categorías por tipo (arcos)', 'Centros de mesa: CTA', 'Ver centros de mesa', 'actuar', '', None),
    ('2 · Categorías por tipo (arcos)', 'Esculturas pequeñas: línea', 'Formas para la mesa de centro', 'desear', '', 'cat'),
    ('2 · Categorías por tipo (arcos)', 'Esculturas pequeñas: CTA', 'Ver esculturas', 'actuar', '', None),
    ('2 · Categorías por tipo (arcos)', 'Decoraciones del hogar: línea', 'Lámparas y objetos para cada rincón', 'desear', '', 'cat'),
    ('2 · Categorías por tipo (arcos)', 'Decoraciones del hogar: CTA', 'Ver decoración', 'actuar', '', None),
    ('2 · Categorías por tipo (arcos)', 'Botón al pie (centrado, lleva a la tienda)', 'Ver todo', 'actuar', '', None),

    ('3 · Lo nuevo', 'H2', 'Lo nuevo', 'desear', '', None),
    ('3 · Lo nuevo', 'Apoyo', 'Las piezas que acaban de llegar a la tienda. [POR CONFIRMAR: cada cuánto llegan piezas nuevas]', 'desear', '', 'apoyo'),
    ('3 · Lo nuevo', 'Botón sobre la foto (lleva a Lo nuevo)', 'Lo quiero todo', 'actuar', '', None),
    ('3 · Lo nuevo', 'Tarjeta de cada pieza (4, las más recientes)', '[Nombre de la pieza] · [Precio]. Oferta y «Quedan pocas» salen del catálogo', 'desear', '', None),

    ('4 · Testimonios (nueva)', 'H2', 'Lo que dicen quienes ya compraron', 'confiar', '', None),
    ('4 · Testimonios (nueva)', 'Apoyo', 'Una muestra de lo que dicen quienes ya compraron. En la ficha de cada pieza están todas sus reseñas. [POR CONFIRMAR: política de reseñas]', 'confiar', '', 'apoyo'),
    ('4 · Testimonios (nueva)', 'Botón', 'Pausar las reseñas', 'confiar', '', None),
    ('4 · Testimonios (nueva)', 'Botón en pausa', 'Reanudar las reseñas', 'confiar', '', None),
    ('4 · Testimonios (nueva)', 'Aviso del prototipo', '[Reseñas de ejemplo para el diseño. Esta sección se publica solo con reseñas reales y con permiso de quien las escribe.]', 'confiar', '', None),
    ('4 · Testimonios (nueva)', 'Reseña de ejemplo · 5 estrellas', 'Llegó entera y bien empacada. Pedí el jarrón con asas para Medellín. Venía en caja, con papel de seda, y es igual al de la foto.', 'confiar', '', None),
    ('4 · Testimonios (nueva)', 'Reseña de ejemplo · 5 estrellas', 'La mesa quedó lista para la visita. Compré la vajilla blanca y las copas. Combinan entre sí y no tuve que buscar nada más.', 'desear', '', None),
    ('4 · Testimonios (nueva)', 'Reseña de ejemplo · 3 estrellas', 'Una copa llegó despicada. La caja venía golpeada y una de las seis copas tenía el borde despicado. Me la cambiaron, pero tardó más de lo que esperaba.', 'confiar', '', None),
    ('4 · Testimonios (nueva)', 'Respuesta de la tienda (reseñas de 3 o menos)', '[RESPUESTA REAL PENDIENTE]', 'confiar', '', None),
    ('4 · Testimonios (nueva)', 'Regla', 'En el inicio, solo reseñas de 3 estrellas o más. Las de 1 y 2 siguen en la ficha de cada pieza.', 'confiar', '', None),
    ('4 · Testimonios (nueva)', 'Reseña de ejemplo · 4 estrellas', 'Bonita, más pequeña de lo que imaginé. La escultura es preciosa, pero la imaginaba más grande. Las medidas estaban en la ficha; debí mirarlas mejor.', 'confiar', '', None),
    ('4 · Testimonios (nueva)', 'Reseña de ejemplo · 5 estrellas', 'Llegó bien hasta Pereira. La mandé directo a la casa de mi mamá como regalo de Navidad y le llegó bien embalada.', 'confiar', '', None),
    ('4 · Testimonios (nueva)', 'Reseña de ejemplo · 5 estrellas', 'Nadie cree que sean de tela. Llevo meses con el ramo en la entrada y sigue igual. Todos preguntan si son naturales.', 'desear', '', None),
    ('4 · Testimonios (nueva)', 'Firma de cada reseña', '[Nombre e inicial del apellido] · [ciudad] · [pieza, con enlace a su ficha]', 'confiar', '', None),

    ('5 · Temporada', 'Antetítulo', 'Temporada de Navidad', 'atrapar', '', None),
    ('5 · Temporada', 'H2', 'Regalos que se guardan, para esta Navidad', 'atrapar', '', None),
    ('5 · Temporada', 'Apoyo', 'Porcelanas, cristalería y figuras para regalar, embaladas para viajar. Envíos a todo el país.', 'desear', '', 'apoyo'),
    ('5 · Temporada', 'Presupuestos', 'Hasta $100.000 · De $100.000 a $250.000 · Más de $250.000', 'actuar', '', None),
    ('5 · Temporada', 'CTA', 'Encontrar un regalo', 'actuar', '', None),

    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'H2', '¿Qué lo trae hoy?', 'actuar', '', None),
    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'Apoyo', 'Elija por dónde empezar.', 'actuar', '', 'apoyo'),
    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'Arco: antetítulo', 'Inspiración', 'atrapar', '', None),
    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'Arco: título', 'Busco ideas para mi casa', 'atrapar', '', None),
    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'Arco: línea', 'Sala, comedor, alcoba o entrada', 'confiar', '', 'apoyo'),
    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'Arco: CTA', 'Ver ideas por espacio', 'actuar', '', None),
    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'Arco: antetítulo', 'Búsqueda', 'atrapar', '', None),
    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'Arco: título', 'Ya sé qué pieza quiero', 'atrapar', '', None),
    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'Arco: línea', 'Búsquela por su nombre', 'confiar', '', 'apoyo'),
    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'Arco: CTA', 'Buscar una pieza', 'actuar', '', None),
    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'Arco: antetítulo', 'Regalos', 'atrapar', '', None),
    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'Arco: título', 'Busco un regalo', 'atrapar', '', None),
    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'Arco: línea', 'Por ocasión o por presupuesto', 'confiar', '', 'apoyo'),
    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'Arco: CTA', 'Ver regalos', 'actuar', '', None),
    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'Arco: antetítulo', 'Descuentos', 'atrapar', '', None),
    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'Arco: título', 'Busco descuentos', 'atrapar', '', None),
    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'Arco: línea', 'Piezas rebajadas, con el precio anterior a la vista', 'confiar', '', 'apoyo'),
    ('6 · ¿Qué lo trae hoy? (arcos con foto)', 'Arco: CTA', 'Ver descuentos', 'actuar', '', None),

    ('7 · Galería de colecciones', 'H2', 'Mire cada colección puesta en casa', 'desear', '', None),
    ('7 · Galería de colecciones', 'Apoyo', 'Toque una pieza de la foto para ver su precio y abrir su ficha.', 'actuar', '', 'apoyo'),
    ('7 · Galería de colecciones', 'Franja cerrada (escritorio)', '[Nombre de la colección]', 'actuar', '', None),
    ('7 · Galería de colecciones', 'Punto: nombre accesible', 'Ver [nombre de la pieza], [precio]', 'actuar', '', None),
    ('7 · Galería de colecciones', 'Tarjeta del punto: CTA', 'Ver la pieza', 'actuar', '', None),
    ('7 · Galería de colecciones', 'Lista bajo la foto (celular)', '[n] piezas en esta foto', 'confiar', '', None),
    ('7 · Galería de colecciones', 'La mesa que recibe', 'Vajillas, cristalería y centros de mesa que funcionan juntos, para cuando llega visita.', 'desear', '', 'apoyo'),
    ('7 · Galería de colecciones', 'CTA', 'Ver La mesa que recibe', 'actuar', '', None),
    ('7 · Galería de colecciones', 'Primer hogar', 'Pocas piezas que combinan, para empezar una casa sin comprarlo todo de una vez.', 'desear', '', 'apoyo'),
    ('7 · Galería de colecciones', 'CTA', 'Ver Primer hogar', 'actuar', '', None),
    ('7 · Galería de colecciones', 'Regalos que se guardan', 'Para bodas, inauguraciones y fechas especiales, con medidas y material a la vista.', 'desear', '', 'apoyo'),
    ('7 · Galería de colecciones', 'CTA', 'Ver regalos', 'actuar', '', None),
    ('7 · Galería de colecciones', 'Piezas protagonistas', 'Las piezas de mayor presencia, las que se ven al entrar a una sala.', 'desear', '', 'apoyo'),
    ('7 · Galería de colecciones', 'CTA', 'Ver las protagonistas', 'actuar', '', None),

    ('8 · Nosotros y lo que se pregunta', 'Izquierda · H2', 'Cómo contamos cada pieza', 'confiar', '', None),
    ('8 · Nosotros y lo que se pregunta', 'Izquierda · Apoyo', 'Separamos lo que se puede comprobar, nuestra lectura del diseño y un lugar posible en su casa.', 'confiar', '', 'apoyo'),
    ('8 · Nosotros y lo que se pregunta', 'Izquierda · Hecho', 'Material, medidas y origen.', 'confiar', '', None),
    ('8 · Nosotros y lo que se pregunta', 'Izquierda · Diseño', 'Nuestra lectura de su forma y su estilo.', 'confiar', '', None),
    ('8 · Nosotros y lo que se pregunta', 'Izquierda · Historia', 'Un lugar posible para ella en su casa.', 'desear', '', None),
    ('8 · Nosotros y lo que se pregunta', 'Izquierda · Texto de marca', '[TEXTO PENDIENTE en la voz de Paula Heredia]', 'confiar', '', None),
    ('8 · Nosotros y lo que se pregunta', 'Izquierda · CTA', 'Conocer la marca', 'confiar', '', None),
    ('8 · Nosotros y lo que se pregunta', 'Derecha · H2', 'Lo que se pregunta antes de comprar', 'confiar', '', None),
    ('8 · Nosotros y lo que se pregunta', 'Derecha · Duda 1', '¿Será como en la foto?', 'confiar', '', None),
    ('8 · Nosotros y lo que se pregunta', 'Derecha · Respuesta 1', 'Cada ficha trae medidas, material, origen y fotos de la pieza en una casa.', 'confiar', '', 'apoyo'),
    ('8 · Nosotros y lo que se pregunta', 'Derecha · Duda 2', '¿Llegará entera?', 'confiar', '', None),
    ('8 · Nosotros y lo que se pregunta', 'Derecha · Respuesta 2', 'La embalamos para viajar. Si llega rota, la reponemos o le devolvemos el dinero. [POR CONFIRMAR: plazo]', 'confiar', '', 'apoyo'),
    ('8 · Nosotros y lo que se pregunta', 'Derecha · Duda 3', '¿Y si tengo una duda?', 'confiar', '', None),
    ('8 · Nosotros y lo que se pregunta', 'Derecha · Respuesta 3', 'Escríbanos por WhatsApp antes de comprar y le respondemos con medidas, fotos o lo que necesite. [POR CONFIRMAR: horario]', 'confiar', '', 'apoyo'),
    ('8 · Nosotros y lo que se pregunta', 'Derecha · Enlace', 'Ver envíos y cambios', 'confiar', '', None),

    ('9 · Estantería', 'H2', 'Piezas de la selección', 'desear', '', None),
    ('9 · Estantería', 'Apoyo', 'Mírela de cerca, póngala en su carrito y recíbala en su ciudad.', 'actuar', '', 'apoyo'),
    ('9 · Estantería', 'Enlace', 'Ver toda la selección', 'actuar', '', None),
    ('9 · Estantería', 'Botón de cada pieza', 'Agregar al carrito', 'actuar', '', None),
    ('9 · Estantería', 'Botón tras agregar (1,3 s)', 'Agregada', 'confiar', '', None),
    ('9 · Estantería', 'Aviso tras agregar', 'Agregó [pieza]. [n] piezas en el carrito. Le faltan [$] para el envío gratis.', 'actuar', '', None),
    ('9 · Estantería', 'Enlace del aviso', 'Ver el carrito', 'actuar', '', None),
    ('9 · Estantería', 'Debajo de la repisa', 'Envío gratis desde $300.000 [POR CONFIRMAR: monto y cobertura]', 'actuar', '', None),

    ('10 · Materiales', 'H2', 'Calidad que se ve de cerca', 'desear', '', None),
    ('10 · Materiales', 'Apoyo', 'Mire de cerca el esmalte, el borde de una copa y la tela de un pétalo antes de elegir.', 'desear', '', 'apoyo'),
    ('10 · Materiales', 'Nota', 'El material exacto de cada pieza está en su ficha.', 'confiar', '', None),
    ('10 · Materiales', 'Porcelana', 'Esmalte liso, de brillo suave. [POR CONFIRMAR con las piezas reales]', 'desear', '', 'apoyo'),
    ('10 · Materiales', 'CTA', 'Ver piezas de porcelana', 'actuar', '', None),
    ('10 · Materiales', 'Cerámica', 'Más gruesa, con una textura que se siente al tacto.', 'desear', '', 'apoyo'),
    ('10 · Materiales', 'CTA', 'Ver piezas de cerámica', 'actuar', '', None),
    ('10 · Materiales', 'Vidrio', 'Transparente o en ámbar, como las copas y los jarrones.', 'desear', '', 'apoyo'),
    ('10 · Materiales', 'CTA', 'Ver cristalería', 'actuar', '', None),
    ('10 · Materiales', 'Tela', 'Pétalos que no se marchitan ni piden agua.', 'desear', '', 'apoyo'),
    ('10 · Materiales', 'CTA', 'Ver flores artificiales', 'actuar', '', None),


    ('11 · Historias', 'H2', 'Historias', 'desear', '', None),
    ('11 · Historias', 'Apoyo', 'Guías para poner la mesa, empezar una casa y conocer de dónde viene cada forma.', 'desear', '', 'apoyo'),
    ('11 · Historias', 'Guía 1', 'Costumbres · El pesebre en casa [GUÍA PENDIENTE]', 'desear', '', None),
    ('11 · Historias', 'Guía 2', 'Costumbres · Cómo poner la mesa para recibir [GUÍA PENDIENTE]', 'desear', '', None),
    ('11 · Historias', 'Guía 3', 'Origen · La forma del ánfora en el jarrón de hoy [GUÍA PENDIENTE]', 'desear', '', None),
    ('11 · Historias', 'Guía 4', 'Por comenzar · El primer jarrón de una casa [GUÍA PENDIENTE]', 'desear', '', None),
    ('11 · Historias', 'Enlace de cada guía', 'Leer la guía', 'actuar', '', None),
    ('11 · Historias', 'CTA', 'Ver todas las guías', 'actuar', '', None),

    ('12 · Antes de comprar', 'H2', 'Antes de comprar', 'confiar', '', None),
    ('12 · Antes de comprar', 'Envíos a todo el país', 'El costo y el tiempo se calculan con su ciudad antes de pagar. Gratis desde $300.000 [POR CONFIRMAR]', 'confiar', '', 'apoyo'),
    ('12 · Antes de comprar', 'Embalaje para piezas frágiles', 'En caja, con papel de seda y protección. [POR CONFIRMAR]', 'confiar', '', 'apoyo'),
    ('12 · Antes de comprar', 'Pago sin crear cuenta', 'Tarjeta, PSE, Nequi y Daviplata. [POR CONFIRMAR: pasarela]', 'confiar', '', 'apoyo'),
    ('12 · Antes de comprar', 'Cambios y garantía', 'Las condiciones están a la vista antes de pagar. [POR CONFIRMAR: plazo de cambios]', 'confiar', '', 'apoyo'),
    ('12 · Antes de comprar', 'Enlace', 'Ver cambios y garantía', 'confiar', '', None),
    ('12 · Antes de comprar', 'Si llega rota', 'La reponemos o le devolvemos el dinero.', 'confiar', '', 'apoyo'),
    ('12 · Antes de comprar', 'Enlace', 'Reportar una pieza rota', 'confiar', '', None),
    ('12 · Antes de comprar', 'Atención por WhatsApp', 'Escribirnos por WhatsApp [POR CONFIRMAR: horario]', 'confiar', '', None),
    ('12 · Antes de comprar', 'Subtítulo', 'Preguntas frecuentes', 'confiar', '', None),
    ('12 · Antes de comprar', 'CTA', 'Ver todas las preguntas', 'confiar', '', None),

    ('13 · Por mayor', 'H2', '¿Compra para un negocio?', 'actuar', '', None),
    ('13 · Por mayor', 'Apoyo', 'Cotizamos por volumen y le respondemos por WhatsApp.', 'actuar', '', 'apoyo'),
    ('13 · Por mayor', 'CTA', 'Solicitar cotización por mayor', 'actuar', '', None),


    ('14 · Cierre', 'Antetítulo', 'Tienda en línea', 'atrapar', '', None),
    ('14 · Cierre', 'H2', 'Recorra la tienda, pieza por pieza', 'actuar', '', None),
    ('14 · Cierre', 'Apoyo (palabras de búsqueda)', 'Porcelanas, jarrones, vajillas, flores artificiales y lámparas para decorar su casa, con envío a todo Colombia.', 'desear', '', 'apoyo'),
    ('14 · Cierre', 'Botón grande', 'Ver todas las piezas', 'actuar', '', None),
    ('14 · Cierre', 'Bajo el botón', 'Envío a todo el país · Embalaje para piezas frágiles · Compra sin crear cuenta', 'confiar', '', None),
    ('Página nueva · Toda la tienda', 'H1', 'Toda la tienda', 'actuar', '', None),
    ('Página nueva · Toda la tienda', 'Introducción', 'Porcelanas, jarrones, vajillas, flores artificiales, esculturas y lámparas para decorar su casa, con envío a todo Colombia. En cada pieza encuentra el material, las medidas y el origen.', 'confiar', '', None),
    ('Página nueva · Toda la tienda', 'Descripción para buscadores', 'Decoración para el hogar en línea: porcelanas, jarrones, vajillas, flores artificiales, esculturas y lámparas. Envíos a todo Colombia.', 'atrapar', '', None),
    ('Página nueva · Descuentos', 'H1', 'Descuentos', 'actuar', '', None),
    ('Página nueva · Descuentos', 'Introducción', 'Piezas con el precio rebajado. Al lado de cada precio está el anterior, para que vea cuánto ahorra. [POR CONFIRMAR: fechas y condiciones de cada descuento]', 'confiar', '', None),
    ('Página nueva · Descuentos', 'Pregunta 1', '¿El precio anterior es real? Sí. Es el precio al que se vendió la pieza antes de la rebaja. [POR CONFIRMAR: regla del precio anterior]', 'confiar', '', None),
    ('Página nueva · Descuentos', 'Descripción para buscadores', 'Piezas de decoración con descuento, con el precio anterior a la vista. Envíos a todo Colombia.', 'atrapar', '', None),
    ('Página nueva · Lo nuevo', 'Introducción', 'Las piezas que acaban de llegar a la tienda, de la más reciente a la más antigua. [POR CONFIRMAR: cada cuánto llegan piezas nuevas y por cuánto tiempo una pieza se muestra aquí]', 'desear', '', None),
    ('Página nueva · Lo nuevo', 'Pregunta 1', '¿Cada cuánto llegan piezas nuevas? [POR CONFIRMAR]', 'confiar', '', None),
    ('Página nueva · Lo nuevo', 'Descripción para buscadores', 'Piezas de decoración recién llegadas: porcelanas, jarrones, centros de mesa y vajilla. Envíos a todo Colombia.', 'atrapar', '', None),

    ('Pie · Boletín', 'H2', 'Guías y piezas nuevas en su correo', 'desear', '', None),
    ('Pie · Boletín', 'Apoyo', '[POR CONFIRMAR: frecuencia] le escribimos con una guía de decoración y las piezas que llegaron. Puede darse de baja con un clic.', 'confiar', '', 'apoyo'),
    ('Pie · Boletín', 'Etiqueta', 'Correo electrónico', 'actuar', '', None),
    ('Pie · Boletín', 'Casilla (sin marcar)', 'Autorizo a Historias que Habitan a tratar mis datos para enviarme correos, según la Política de tratamiento de datos.', 'confiar', '', None),
    ('Pie · Boletín', 'Botón', 'Suscribirme', 'actuar', '', None),
    ('Pie · Boletín', 'Confirmación', 'Listo. Le enviamos un correo para confirmar la suscripción.', 'confiar', '', None),
    ('Pie · Boletín', 'Error: correo', 'Revise el correo: le falta la @ o el dominio.', 'confiar', '', None),
    ('Pie · Boletín', 'Error: casilla', 'Para suscribirse, marque la autorización de datos.', 'confiar', '', None),
    ('Pie · Boletín', 'Error: servidor', 'No pudimos guardar su correo. Intente de nuevo en unos minutos.', 'confiar', '', None),

    ('Pie · Por mayor', 'Enlace', 'Solicitar cotización por mayor', 'actuar', '', None),

    ('Microcopy', 'Buscador: sugerencias', 'Jarrones · Copas · Centros de mesa · Regalos de boda · Lámparas', 'actuar', '', None),
    ('Microcopy', 'Buscador: sin resultados', 'No encontramos «{término}». Pruebe con «jarrón», «copa» o «lámpara», o escríbanos por WhatsApp.', 'confiar', '', None),
    ('Microcopy', 'Carrito vacío', 'Su carrito está vacío. Empiece por las piezas de la selección.', 'actuar', '', None),
    ('Microcopy', 'Carrito vacío: CTA', 'Ver la selección', 'actuar', '', None),
    ('Microcopy', 'Pieza agregada (anuncio)', 'Pieza agregada al carrito. {n} en total.', 'confiar', '', None),

    ('Cargas', 'Rejilla de piezas (> 1 s)', 'Cargando piezas…', 'confiar', '', None),
    ('Cargas', 'Colección La mesa que recibe (> 1 s)', 'Preparando su mesa…', 'confiar', '', None),
    ('Cargas', 'Giro de la escultura (> 1 s)', 'Preparando la escultura…', 'confiar', '', None),
    ('Cargas', 'Búsqueda (> 1 s)', 'Buscando piezas…', 'confiar', '', None),
]

# Palabras que el manual prohíbe en interfaz, microcopy y metadatos
PROHIBIDAS = r'\b(innovador\w*|únic[oa]s?|revolucionari\w*|sostenible\w*|lujo\w*|monopolio\w*|auténtic\w*|original\w*|históric\w*|artesanal\w*|ecológic\w*|heredad\w*|de época|asesoría personalizada|exclusiv\w*)\b'
CTA_DEBILES = r'^(Ver más|Clic aquí|Enviar|OK|Más información|Comprar ahora)$'
# Imperativos y posesivos de tú. «Compra», «mira» y «encuentra» quedan fuera: también son formas de usted («¿Compra para un negocio?», «En cada pieza encuentra…»)
TUTEO = r'\b(tu|tus|puedes|quieres|arrastra|descubre|elige|empieza|explora|decora|agrega)\b'


def sin_marcas(t):
    return re.sub(r'\[[^\]]*\]', '', t).strip()


def palabras(t):
    return len([w for w in re.split(r'\s+', sin_marcas(t)) if re.search(r'\w', w)])


# Excepciones que el negocio aprobó a sabiendas; quedan listadas en la revisión, no se esconden
EXCEPCIONES = {('Global · Modal de bienvenida (variante D)', 'Línea'): '«exclusivas», aprobado por el negocio el 23/11/2026: hay ofertas que reciben solo los suscriptores'}
filas, avisos, aprobadas = [], [], []
for sec, el, copy, intencion, var, lim in D:
    limpio = sin_marcas(copy)
    n = len(limpio)
    p = palabras(copy)
    nota = ''
    if lim and p > LIM[lim]:
        avisos.append('%s / %s: %d palabras (límite %d)' % (sec, el, p, LIM[lim]))
        nota = ' ⚠'
    if re.search(PROHIBIDAS, copy, re.I):
        if (sec, el) in EXCEPCIONES:
            aprobadas.append('%s / %s: %s' % (sec, el, EXCEPCIONES[(sec, el)]))
        else:
            avisos.append('%s / %s: palabra prohibida' % (sec, el))
    if el.startswith('CTA') and re.match(CTA_DEBILES, copy):
        avisos.append('%s / %s: CTA genérico' % (sec, el))
    if re.search(TUTEO, limpio.lower()):
        avisos.append('%s / %s: posible tuteo, revisar' % (sec, el))
    if '—' in copy:
        avisos.append('%s / %s: raya en texto corto' % (sec, el))
    filas.append('| %s | %s | %s | %d%s | %s | %s |' % (sec, el, copy, n, nota, intencion, var or '—'))

TABLA = '\n'.join(['| Sección | Elemento | Copy | Caracteres | Intención | Variante A/B |',
                   '|---|---|---|---|---|---|'] + filas)
REVISION = ('Sin avisos: ningún texto pasa su límite de palabras, no aparece ninguna palabra prohibida, '
            'no hay CTA genéricos, tuteo ni rayas en textos cortos.' if not avisos
            else '\n'.join('- ' + a for a in avisos))
if aprobadas:
    REVISION += '\n\nExcepciones aprobadas:\n' + '\n'.join('- ' + a for a in aprobadas)

plantilla = io.open(sys.argv[2], encoding='utf-8').read()
doc = plantilla.replace('{{TABLA}}', TABLA).replace('{{REVISION}}', REVISION).replace('{{N}}', str(len(D)))
io.open(SALIDA, 'w', encoding='utf-8', newline='\n').write(doc)
print(REVISION)
print(len(D), 'filas')

# Categorías y colecciones generadas desde datos con las mismas plantillas.
# Se ejecuta dentro de construir_paginas.py: usa CUERPO_CAT, JS_CAT, CSS_CAT, CSS_DOC, tarjetas_cat, FILTROS, grupo, d, tarjeta, pagina, EXTRA.

CSS_CATS = CSS_CAT + r'''
.subcats{display:flex;flex-wrap:wrap;gap:var(--s2);margin-top:var(--s4)}
.subcats a{display:inline-flex;align-items:center;min-height:44px;padding:0 var(--s4);border:1px solid var(--cafe-humo);border-radius:999px;text-decoration:none;font-size:.9375rem}
.subcats a:hover{background:var(--suave)}
.subcats a[aria-current]{background:var(--tinta);color:var(--hueso);border-color:var(--tinta)}
.destacado{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:var(--s3) var(--s5);margin-top:var(--s5);padding:var(--s4);background:var(--espresso);color:var(--hueso);border-radius:6px}
.destacado h2{font-size:1.5rem;line-height:1.2;color:var(--champagne)}
.destacado p{margin-top:var(--s1);max-width:46ch}
.destacado .boton{border-color:var(--hueso);color:var(--hueso);background:transparent}
.destacado .boton:hover{background:rgba(251,250,249,.14)}
.destacado :focus-visible{outline-color:var(--hueso)}
'''
FILTRO_ETIQUETAS = [('Material', 'material'), ('Color', 'color'), ('Tamaño', 'tamano'), ('Ambiente', 'ambiente')]
P = '<span class="pendiente">%s</span>'


def rep_una(texto, a, b):
    assert texto.count(a) == 1, (a[:70], texto.count(a))
    return texto.replace(a, b)


def piezas_html(piezas):
    html, valores = '', {k: [] for _, k in FILTRO_ETIQUETAS}
    for pz in piezas:
        nombre, meta, precio, (material, color, tamano, ambiente), dibujo = pz[:5]
        extra = pz[5] if len(pz) > 5 else {}
        valor = int(precio.replace('$', '').replace('.', ''))
        for k, v in zip(('material', 'color', 'tamano', 'ambiente'), (material, color, tamano, ambiente)):
            if v not in valores[k]:
                valores[k].append(v)
        html += tarjeta(nombre, meta, precio, datos=d(material, color, tamano, ambiente, valor), dibujo=dibujo, **extra)
    return html, valores


TODAS = []  # todas las piezas de las categorías, para «Toda la tienda» y «Descuentos»


def categoria_pag(archivo, nombre, intro, piezas, elegir, faqs, migas_medio=(), subnav=None, despues_intro='', descripcion='', tienda=False):
    tarjetas, valores = piezas_html(piezas)
    if not tienda:
        TODAS.extend(pz for pz in piezas if pz[0] not in [x[0] for x in TODAS])
    for pz in piezas:
        if not tienda and 'pieza-' + slug(pz[0]) + '.html' in REG:
            REG['pieza-' + slug(pz[0]) + '.html']['cat'] = (nombre, archivo, 'Mesa' if migas_medio else None)
    n = len(piezas)
    filtros = FILTROS
    for titulo, clave in FILTRO_ETIQUETAS:
        viejo = grupo(titulo, clave, {'material': ['Cerámica', 'Porcelana', 'Vidrio'], 'color': ['Blanco', 'Arena', 'Ámbar', 'Verde', 'Transparente'],
                                      'tamano': ['Pequeño', 'Mediano', 'Grande'], 'ambiente': ['Sala', 'Mesa', 'Entrada']}[clave])
        filtros = rep_una(filtros, viejo, grupo(titulo, clave, valores[clave]) if len(valores[clave]) > 1 else '')
    filtros = rep_una(filtros, 'Ver 8 piezas', 'Ver %d piezas' % n)
    c = CUERPO_CAT.replace(FILTROS, filtros)
    medio = ''.join('<li><a href="%s">%s</a></li>' % (u, t) for t, u in migas_medio)
    c = rep_una(c, '<li><span aria-current="page">Jarrones y recipientes</span></li>', medio + '<li><span aria-current="page">%s</span></li>' % nombre)
    c = rep_una(c, '<h1>Jarrones y recipientes</h1>', '<h1>%s</h1>' % nombre)
    c = rep_una(c, 'Jarrones, floreros y recipientes decorativos de cerámica, porcelana y vidrio, para usar solos o con flores y ramas. En cada pieza encuentra las medidas, el material y el origen. <span class="pendiente">[TEXTO DE EJEMPLO]</span>', intro)
    if subnav:
        enlaces = ''.join('<a href="%s"%s>%s</a>' % (u, ' aria-current="page"' if t == nombre else '', t) for t, u in subnav)
        c = rep_una(c, '  </header>\n\n  <div class="barra-lista">', '    <nav class="subcats" aria-label="Tipos de pieza en Mesa">%s</nav>\n  </header>\n\n  <div class="barra-lista">' % enlaces)
    if despues_intro:
        c = rep_una(c, '  </header>\n\n  <div class="barra-lista">', '  </header>\n' + despues_intro + '\n  <div class="barra-lista">')
    c = rep_una(c, '<p id="cuenta" role="status">8 piezas</p>', '<p id="cuenta" role="status">%d %s</p>' % (n, 'pieza' if n == 1 else 'piezas'))
    c = rep_una(c, tarjetas_cat, tarjetas)
    c = rep_una(c, '<div class="mas" id="mas"><a class="boton secundario" href="?pagina=2" data-proto>Ver más piezas</a></div>', '<div class="mas" id="mas" hidden></div>')
    c = rep_una(c, '<h2 id="t-elegir">Cómo elegir un jarrón</h2>', '<h2 id="t-elegir">%s</h2>' % elegir)
    i = c.index('      <details class="faq">')
    j = c.index('    </section>\n  </div>\n</main>')
    c = c[:i] + ''.join('      <details class="faq"><summary>%s</summary><p>%s</p></details>\n' % f for f in faqs) + c[j:]
    io.open(dest + '/' + archivo, 'w', encoding='utf-8', newline='\n').write(pagina(
        nombre + ' · Historias que Habitan', descripcion or intro, CSS_CATS, c, actual=nombre.split(':')[0], guion=JS_CAT))
    EXTRA.append(archivo)


ENVIOS = ('¿Hacen envíos fuera de Bogotá?', 'Sí. Hacemos envíos a todo el país. El costo y el tiempo se calculan con su ciudad antes de pagar.')
EMBALAJE = ('¿Cómo llegan embaladas las piezas frágiles?', 'En caja, con papel de seda y protección. ' + P % '[POR CONFIRMAR]')
CH, PA = 'Hecho en China', 'Hecho en Panamá'

categoria_pag('porcelanas.html', 'Porcelanas y figuras',
              'Figuras y piezas de porcelana: animales, personajes y formas para una repisa, una mesa auxiliar o un regalo. En cada pieza encuentra las medidas, el acabado y el origen. ' + P % '[TEXTO DE EJEMPLO]',
              [('[Ave de porcelana blanca]', 'Porcelana · ' + CH, '$89.900', ('Porcelana', 'Blanco', 'Pequeño', 'Sala'), ('figura', '#F4F2EE'), {'sello': True}),
               ('[Ave de porcelana azul]', 'Porcelana · ' + CH, '$94.900', ('Porcelana', 'Azul', 'Pequeño', 'Sala'), ('figura', '#C9D6E3')),
               ('[Figura de porcelana rosa]', 'Porcelana · ' + PA, '$129.900', ('Porcelana', 'Rosa', 'Mediano', 'Entrada'), ('figura', '#E7C3BB')),
               ('[Esfera de porcelana]', 'Porcelana · ' + CH, '$74.900', ('Porcelana', 'Blanco', 'Pequeño', 'Mesa'), ('esfera', '#F1EEE8'), {'antes': '$89.900'}),
               ('[Recipiente de porcelana con tapa]', 'Porcelana · ' + CH, '$109.900', ('Porcelana', 'Blanco', 'Mediano', 'Mesa'), ('tarro', '#F4F2EE')),
               ('[Figura de cerámica arena]', 'Cerámica · ' + CH, '$159.900', ('Cerámica', 'Arena', 'Grande', 'Entrada'), ('figura', '#D9C7AE'), {'agotado': True})],
              'Cómo elegir una figura de porcelana',
              [('¿Las figuras son hechas a mano?', 'No todas. En cada ficha decimos cómo se hizo la pieza y de dónde viene. ' + P % '[POR CONFIRMAR por pieza]'), EMBALAJE, ENVIOS])

categoria_pag('flores-artificiales.html', 'Flores artificiales',
              'Ramos y tallos de flores artificiales de apariencia natural, en varios tamaños y colores, para componer con un jarrón o un recipiente. No necesitan agua ni cuidados. ' + P % '[TEXTO DE EJEMPLO]',
              [('[Ramo de flores rosa y champaña]', 'Tela · ' + CH, '$49.900', ('Tela', 'Rosa', 'Mediano', 'Mesa'), ('flores', '#DDE6E8', True)),
               ('[Ramo alto con florero]', 'Tela y vidrio · ' + CH, '$119.900', ('Tela', 'Rosa', 'Grande', 'Sala'), ('flores', '#E8E2D8', True), {'sello': True}),
               ('[Arreglo bajo en cuenco]', 'Tela y cerámica · ' + CH, '$89.900', ('Tela', 'Champaña', 'Pequeño', 'Mesa'), ('centro', '#D9C7AE')),
               ('[Ramo en cuenco blanco]', 'Látex y cerámica · ' + PA, '$99.900', ('Látex', 'Champaña', 'Mediano', 'Entrada'), ('centro', '#F4F2EE'), {'antes': '$119.900'})],
              'Cómo combinar flores y jarrón',
              [('¿Las flores vienen con el jarrón?', 'Depende del producto. La ficha dice qué incluye la caja.'), ('¿Cómo se limpian?', 'Con un paño seco o aire frío. ' + P % '[POR CONFIRMAR con el proveedor]'), ENVIOS])

MESA_SUB = [('Vajillas', 'mesa-vajillas.html'), ('Cristalería', 'mesa-cristaleria.html'), ('Accesorios de mesa', 'mesa-accesorios.html')]
VAJ = [('[Vajilla de 16 piezas blanca]', 'Porcelana · ' + CH, '$389.900', ('Porcelana', 'Blanco', 'Grande', 'Comedor'), ('plato', '#F4F2EE'), {'sello': True}),
       ('[Juego de 6 platos arena]', 'Cerámica · ' + PA, '$179.900', ('Cerámica', 'Arena', 'Mediano', 'Comedor'), ('plato', '#D9C7AE')),
       ('[Juego de 6 platos verdes]', 'Cerámica · ' + CH, '$169.900', ('Cerámica', 'Verde', 'Mediano', 'Comedor'), ('plato', '#8A9A82'), {'antes': '$199.900'})]
CRI = [('[Juego de 6 copas de vino]', 'Vidrio · ' + CH, '$149.900', ('Vidrio', 'Transparente', 'Mediano', 'Comedor'), ('copa', '#DDE6E8', True)),
       ('[Juego de 6 copas ámbar]', 'Vidrio · ' + CH, '$159.900', ('Vidrio', 'Ámbar', 'Mediano', 'Comedor'), ('copa', '#C9934E', True)),
       ('[Jarra de vidrio]', 'Vidrio · ' + PA, '$89.900', ('Vidrio', 'Transparente', 'Grande', 'Comedor'), ('florero', '#DDE6E8', True), {'agotado': True})]
ACC = [('[Azucarera de cerámica]', 'Cerámica · ' + CH, '$59.900', ('Cerámica', 'Blanco', 'Pequeño', 'Comedor'), ('tarro', '#F4F2EE')),
       ('[Cuenco para servir]', 'Cerámica · ' + CH, '$69.900', ('Cerámica', 'Arena', 'Mediano', 'Comedor'), ('cuenco', '#D9C7AE'))]
MESA_FAQ = [('¿Se pueden lavar en lavavajillas?', P % '[POR CONFIRMAR por pieza]'), ('¿Venden piezas sueltas de una vajilla?', P % '[POR CONFIRMAR]'), EMBALAJE]
INTRO_MESA = 'Vajillas, cristalería y accesorios para la mesa de todos los días y para la que recibe visita. En cada pieza encuentra el material, las medidas y los cuidados. ' + P % '[TEXTO DE EJEMPLO]'
categoria_pag('mesa.html', 'Mesa', INTRO_MESA, VAJ + CRI + ACC, 'Cómo armar una vajilla para recibir', MESA_FAQ, subnav=MESA_SUB)
for (sub, archivo), lista in zip(MESA_SUB, (VAJ, CRI, ACC)):
    categoria_pag(archivo, sub, sub + ' para la mesa. ' + P % '[TEXTO DE EJEMPLO]', lista, 'Cómo elegir ' + sub.lower(), MESA_FAQ,
                  migas_medio=[('Mesa', 'mesa.html')], subnav=MESA_SUB, descripcion=sub + ' para la mesa. Envíos a todo el país.')

categoria_pag('centros-de-mesa.html', 'Centros de mesa',
              'Arreglos, cuencos y floreros bajos para el centro de la mesa, que no tapan la vista entre quienes se sientan. ' + P % '[TEXTO DE EJEMPLO]',
              [('[Centro de mesa con flores]', 'Tela y cerámica · ' + CH, '$129.900', ('Cerámica', 'Arena', 'Mediano', 'Comedor'), ('centro', '#D9C7AE'), {'sello': True}),
               ('[Cuenco bajo blanco]', 'Cerámica · ' + CH, '$79.900', ('Cerámica', 'Blanco', 'Pequeño', 'Comedor'), ('cuenco', '#F4F2EE')),
               ('[Bandeja con florero]', 'Vidrio · ' + PA, '$99.900', ('Vidrio', 'Transparente', 'Pequeño', 'Sala'), ('flores', '#DDE6E8', True)),
               ('[Centro de mesa en cuenco blanco]', 'Látex y cerámica · ' + CH, '$149.900', ('Cerámica', 'Blanco', 'Grande', 'Comedor'), ('centro', '#F4F2EE'), {'antes': '$169.900'})],
              'Qué altura debe tener un centro de mesa',
              [('¿Qué tamaño de centro de mesa necesito?', P % '[TEXTO PENDIENTE: según el largo de la mesa]'), EMBALAJE, ENVIOS])

categoria_pag('esculturas.html', 'Esculturas pequeñas',
              'Esculturas y formas decorativas para una repisa, un escritorio o una mesa de centro. Piezas que se notan sin ocupar mucho espacio. ' + P % '[TEXTO DE EJEMPLO]',
              [('[Escultura curva café]', 'Cerámica · ' + CH, '$179.900', ('Cerámica', 'Café', 'Mediano', 'Sala'), ('escultura', '#5B4632'), {'sello': True}),
               ('[Escultura curva blanca]', 'Cerámica · ' + CH, '$179.900', ('Cerámica', 'Blanco', 'Mediano', 'Estudio'), ('escultura', '#F4F2EE')),
               ('[Esfera sobre base]', 'Resina · ' + PA, '$139.900', ('Resina', 'Arena', 'Pequeño', 'Estudio'), ('esfera', '#D9C7AE')),
               ('[Ave de cerámica café]', 'Cerámica · ' + CH, '$119.900', ('Cerámica', 'Café', 'Pequeño', 'Sala'), ('figura', '#7A5C48'), {'antes': '$139.900'})],
              'Dónde poner una escultura pequeña',
              [('¿Son piezas irrepetibles?', 'No. Son piezas de nuestra selección, producidas en serie. En la ficha decimos su origen.'), EMBALAJE, ENVIOS])

categoria_pag('decoracion.html', 'Decoraciones del hogar',
              'Otras piezas para la casa que no caben en las demás categorías. ' + P % '[POR CONFIRMAR: qué incluye esta categoría]',
              [('[Recipiente con tapa verde]', 'Cerámica · ' + CH, '$99.900', ('Cerámica', 'Verde', 'Pequeño', 'Entrada'), ('tarro', '#6E7F68')),
               ('[Jarrón con relieve]', 'Porcelana · ' + PA, '$219.900', ('Porcelana', 'Blanco', 'Mediano', 'Sala'), ('relieve', '#F4F2EE')),
               ('[Esfera decorativa]', 'Resina · ' + CH, '$69.900', ('Resina', 'Arena', 'Pequeño', 'Estudio'), ('esfera', '#D9C7AE'))],
              'Ideas para decorar una entrada', [EMBALAJE, ENVIOS],
              despues_intro='  <section class="destacado" aria-labelledby="t-luz"><div><h2 id="t-luz">Lámparas</h2><p>Véalas apagadas y encendidas, y en luz cálida, neutra o fría.</p></div><a class="boton" href="lamparas.html">Ver lámparas</a></section>')


# ---------------------------------------------------------------- Toda la tienda y Descuentos
# Las piezas de Jarrones y recipientes se escriben en construir_paginas.py con tarjeta(); aquí van como datos para la tienda
JARRONES = [('Jarrón de cerámica blanca con asas', 'Cerámica · ' + CH, '$189.900', ('Cerámica', 'Blanco', 'Mediano', 'Entrada'), ('anfora', '#F1EEE8'), {'sello': True, 'href': 'ficha-producto.html'}),
            ('[Jarrón de vidrio ámbar]', 'Vidrio · ' + CH, '$129.900', ('Vidrio', 'Ámbar', 'Mediano', 'Sala'), ('panza', '#B8752A', True)),
            ('[Recipiente pequeño de cerámica]', 'Cerámica · ' + PA, '$79.900', ('Cerámica', 'Arena', 'Pequeño', 'Mesa'), ('cuenco', '#D9C7AE'), {'antes': '$99.900'}),
            ('[Jarrón alto de porcelana]', 'Porcelana · ' + CH, '$319.900', ('Porcelana', 'Blanco', 'Grande', 'Sala'), ('alto', '#F4F2EE')),
            ('[Florero de vidrio transparente]', 'Vidrio · ' + CH, '$69.900', ('Vidrio', 'Transparente', 'Pequeño', 'Mesa'), ('florero', '#DDE6E8', True)),
            ('[Ánfora decorativa de cerámica]', 'Cerámica · ' + CH, '$259.900', ('Cerámica', 'Arena', 'Grande', 'Entrada'), ('anfora', '#D9C7AE'), {'agotado': True}),
            ('[Jarrón de porcelana con relieve]', 'Porcelana · ' + PA, '$219.900', ('Porcelana', 'Blanco', 'Mediano', 'Sala'), ('relieve', '#F4F2EE'), {'sello': True}),
            ('[Recipiente con tapa de cerámica]', 'Cerámica · ' + CH, '$99.900', ('Cerámica', 'Verde', 'Pequeño', 'Mesa'), ('tarro', '#6E7F68'))]
TODAS[:0] = [pz for pz in JARRONES if pz[0] not in [x[0] for x in TODAS]]
CATS_TIENDA = ('  <nav class="subcats" aria-label="Categorías de la tienda">'
               + ''.join('<a href="%s">%s</a>' % (u, t) for t, u in [('Porcelanas y figuras', 'porcelanas.html'), ('Jarrones y recipientes', 'categoria.html'),
                                                                     ('Flores artificiales', 'flores-artificiales.html'), ('Mesa', 'mesa.html'), ('Centros de mesa', 'centros-de-mesa.html'),
                                                                     ('Esculturas pequeñas', 'esculturas.html'), ('Decoraciones del hogar', 'decoracion.html'), ('Lámparas', 'lamparas.html'), ('Lo nuevo', 'lo-nuevo.html'), ('Descuentos', 'descuentos.html')])
               + '</nav>')
categoria_pag('tienda.html', 'Toda la tienda',
              'Porcelanas, jarrones, vajillas, flores artificiales, esculturas y lámparas para decorar su casa, con envío a todo Colombia. En cada pieza encuentra el material, las medidas y el origen.',
              TODAS, 'Cómo combinar piezas en un mismo espacio',
              [ENVIOS, EMBALAJE, ('¿Tengo que crear una cuenta para comprar?', 'No. Puede comprar como invitado y crear su cuenta al final, si quiere.')],
              despues_intro=CATS_TIENDA, tienda=True,
              descripcion='Decoración para el hogar en línea: porcelanas, jarrones, vajillas, flores artificiales, esculturas y lámparas. Envíos a todo Colombia.')
# Descuentos: lo decide el catálogo único (y una pieza agotada no se anuncia como oferta)
DESCUENTOS = [pz for pz in TODAS if estado_pieza(pz[0])['antes'] and not estado_pieza(pz[0])['agotada']]
categoria_pag('descuentos.html', 'Descuentos',
              'Piezas con el precio rebajado. Al lado de cada precio está el anterior, para que vea cuánto ahorra. ' + P % '[POR CONFIRMAR: fechas y condiciones de cada descuento]',
              DESCUENTOS, 'Cómo leemos un descuento',
              [('¿El precio anterior es real?', 'Sí. Es el precio al que se vendió la pieza antes de la rebaja. ' + P % '[POR CONFIRMAR: regla del precio anterior, por ejemplo el de los últimos 30 días]'),
               ('¿Hasta cuándo dura cada descuento?', P % '[POR CONFIRMAR: fecha de fin de cada descuento]'),
               ('¿Las piezas con descuento tienen cambio?', 'Sí, con las mismas condiciones de Cambios, garantía y retracto. ' + P % '[POR CONFIRMAR]')],
              migas_medio=[('Toda la tienda', 'tienda.html')], tienda=True,
              descripcion='Piezas de decoración con descuento, con el precio anterior a la vista. Envíos a todo Colombia.')

# Lo nuevo: lo decide el catálogo único (catalogo.NUEVAS), en el mismo orden que la sección 3 del inicio
from catalogo import NUEVAS, clave as clave_cat
LO_NUEVO = [next(pz for pz in TODAS if clave_cat(pz[0]) == c) for c in NUEVAS]
categoria_pag('lo-nuevo.html', 'Lo nuevo',
              'Las piezas que acaban de llegar a la tienda, de la más reciente a la más antigua. ' + P % '[POR CONFIRMAR: cada cuánto llegan piezas nuevas y por cuánto tiempo una pieza se muestra aquí]',
              LO_NUEVO, 'Cómo combinar piezas en un mismo espacio',
              [('¿Cada cuánto llegan piezas nuevas?', P % '[POR CONFIRMAR]'), ENVIOS, EMBALAJE],
              migas_medio=[('Toda la tienda', 'tienda.html')], tienda=True,
              descripcion='Piezas de decoración recién llegadas: porcelanas, jarrones, centros de mesa y vajilla. Envíos a todo Colombia.')


# ---------------------------------------------------------------- Colecciones
def coleccion_pag(archivo, nombre, color, texto, piezas, guia, otras):
    tarjetas = ''.join(tarjeta(p[0], p[1], p[2], dibujo=p[3], **(p[4] if len(p) > 4 else {})) for p in piezas)
    otras_html = ''.join('      <p><a class="enlace" href="%s">%s</a></p>\n' % (u, t) for t, u in otras)
    nueva(archivo, nombre, texto, migas(INI, ('Colecciones', 'colecciones.html'), (nombre, '')) + '''
  <header class="banda-col" style="background:var(--%s)">
    <h1>%s</h1>
    <p>%s</p>
    %s
  </header>
  <div class="estado-lista" style="padding-top:var(--s5)"><p>%d piezas</p></div>
  <h2 class="oculto-visual">Piezas de la colección</h2>
  <ul class="rejilla estanteria">
%s  </ul>
  <div class="texto-cat">
    <section aria-labelledby="t-guia">
      <h2 id="t-guia">La guía de esta colección</h2>
      <ul class="guias"><li><a href="historias.html"><h3>%s</h3><p>Guía · [Autora] · Actualizada el [fecha]</p></a></li></ul>
    </section>
    <section aria-labelledby="t-otras">
      <h2 id="t-otras">Otras colecciones</h2>
%s    </section>
  </div>''' % (color, nombre, texto, P % '[TEXTO DE EJEMPLO]', len(piezas), tarjetas, guia, otras_html))


coleccion_pag('coleccion-primer-hogar.html', 'Primer hogar', 'mocha',
              'Pocas piezas que combinan entre sí, para empezar una casa sin tener que comprarlo todo de una vez.',
              [('[Jarrón de vidrio ámbar]', 'Vidrio · ' + CH, '$129.900', ('panza', '#B8752A', True)),
               ('[Ramo de flores rosa y champaña]', 'Tela · ' + CH, '$49.900', ('flores', '#DDE6E8', True)),
               ('[Juego de 6 platos arena]', 'Cerámica · ' + PA, '$179.900', ('plato', '#D9C7AE')),
               ('[Escultura curva blanca]', 'Cerámica · ' + CH, '$179.900', ('escultura', '#F4F2EE'))],
              '[GUÍA PENDIENTE] Las primeras piezas de una casa',
              [('La mesa que recibe', 'coleccion.html'), ('Regalos que se guardan', 'coleccion-regalos.html')])

coleccion_pag('coleccion-regalos.html', 'Regalos que se guardan', 'espresso',
              'Piezas para regalar en bodas, inauguraciones y fechas especiales, con la medida, el material y el origen a la vista.',
              [('[Ave de porcelana blanca]', 'Porcelana · ' + CH, '$89.900', ('figura', '#F4F2EE'), {'sello': True}),
               ('[Juego de 6 copas de vino]', 'Vidrio · ' + CH, '$149.900', ('copa', '#DDE6E8', True)),
               ('[Centro de mesa con flores]', 'Tela y cerámica · ' + CH, '$129.900', ('centro', '#D9C7AE')),
               ('Jarrón de cerámica blanca con asas', 'Cerámica · ' + CH, '$189.900', ('anfora', '#F1EEE8'), {'href': 'ficha-producto.html'})],
              '[GUÍA PENDIENTE] Cómo elegir un regalo para una casa que no conoce',
              [('La mesa que recibe', 'coleccion.html'), ('Primer hogar', 'coleccion-primer-hogar.html')])


# Piezas protagonistas, guías, Mi cuenta y error
exec(io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'paginas_mas.py'), encoding='utf-8').read())

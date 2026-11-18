# Fichas de producto de todas las piezas, a partir de prototipos/ficha-producto.html y prototipos/ficha-lampara.html.
# Se ejecuta al final de construir_paginas.py: usa REG (registro de tarjetas), LAMPARAS, arte, dest, io, os.
import re

P = '<span class="pendiente">%s</span>'
SIN_COLOR, SIN_TAMANO = 'Color de la foto', 'Estándar'  # cuando la pieza no tiene variantes
COLORES = {'#F4F2EE': 'Blanco', '#F1EEE8': 'Blanco', '#E8E2D8': 'Blanco', '#D9C7AE': 'Arena', '#DDE6E8': 'Transparente', '#B8752A': 'Ámbar',
           '#C9934E': 'Ámbar', '#6E7F68': 'Verde', '#8A9A82': 'Verde', '#C9D6E3': 'Azul', '#E7C3BB': 'Rosa', '#5B4632': 'Café', '#7A5C48': 'Café'}
CATEGORIAS_ARCH = {'Porcelanas y figuras': 'porcelanas.html', 'Jarrones y recipientes': 'categoria.html', 'Flores artificiales': 'flores-artificiales.html',
                   'Mesa': 'mesa.html', 'Centros de mesa': 'centros-de-mesa.html', 'Esculturas pequeñas': 'esculturas.html', 'Decoraciones del hogar': 'decoracion.html'}


def r1(texto, a, b):
    assert texto.count(a) == 1, (a[:70], texto.count(a))
    return texto.replace(a, b)


def pesos(n):
    return '$' + format(n, ',').replace(',', '.')


def cat_por_nombre(nombre):
    n = nombre.lower()
    for claves, cat in (('copa jarra', ('Cristalería', 'mesa-cristaleria.html', 'Mesa')), ('plato vajilla', ('Vajillas', 'mesa-vajillas.html', 'Mesa')),
                        ('azucarera servir', ('Accesorios de mesa', 'mesa-accesorios.html', 'Mesa')), ('ramo arreglo', ('Flores artificiales', 'flores-artificiales.html', None)),
                        ('centro bandeja', ('Centros de mesa', 'centros-de-mesa.html', None)), ('escultura esfera', ('Esculturas pequeñas', 'esculturas.html', None)),
                        ('ave figura', ('Porcelanas y figuras', 'porcelanas.html', None))):
        if any(c in n for c in claves.split()):
            return cat
    return ('Jarrones y recipientes', 'categoria.html', None)


def migas_html(cat):
    nombre, archivo, madre = cat
    medio = '<li><a href="%s">%s</a></li>' % (CATEGORIAS_ARCH[madre], madre) if madre else ''
    return '<li><a href="inicio.html">Inicio</a></li>%s<li><a href="%s">%s</a></li>' % (medio, archivo, nombre)


def variantes(color, tamano, precio, antes):
    oferta = ' data-oferta="%d"' % precio if antes else ''
    base = antes or precio
    oc = ' hidden' if color == SIN_COLOR else ''
    ot = ' hidden' if tamano == SIN_TAMANO else ''
    return ('''<fieldset%(oc)s>
          <legend>Color: <span id="color-elegido">%(c)s</span></legend>
          <div class="variantes">
            <label class="variante"><input type="radio" name="color" value="%(c)s" checked><span>%(c)s</span></label>
          </div>
        </fieldset>
        <fieldset%(ot)s>
          <legend>Tamaño: <span id="tamano-elegido">%(t)s</span></legend>
          <div class="variantes">
            <label class="variante"><input type="radio" name="tamano" value="%(t)s" data-precio="%(b)d"%(o)s checked><span>%(t)s<small>%(m)s</small></span></label>
          </div>
        </fieldset>''' % dict(c=color, t=tamano, b=base, o=oferta, oc=oc, ot=ot, m='[medidas por confirmar]'))


VIEJAS_VARIANTES = None


def personalizar(t, info, hermanos):
    """Cambia en la plantilla todo lo que depende de la pieza."""
    global VIEJAS_VARIANTES
    nombre, precio, antes = info['nombre'], info['precio'], info.get('antes')
    i = t.index('<form id="form-compra" novalidate>\n        <fieldset>') + len('<form id="form-compra" novalidate>\n        ')
    j = t.index('</fieldset>', t.index('<fieldset>', t.index('</fieldset>', i))) + len('</fieldset>')
    t = t[:i] + variantes(info['color'], info['tamano'], precio, antes) + t[j:]
    t = re.sub(r'<title>\[EJEMPLO\] [^<]*</title>', '<title>[EJEMPLO] %s · Historias que Habitan</title>' % nombre, t)
    t = re.sub(r'<h1>[^<]*</h1>', '<h1>%s</h1>' % nombre, t, count=1)
    t = re.sub(r'<p class="respuesta">.*?</p>', '<p class="respuesta">%s</p>' % (P % '[RESPUESTA BREVE PENDIENTE: qué es, para qué espacio y por qué elegirla]'), t, count=1, flags=re.S)
    base = pesos(antes or precio)
    t = re.sub(r'<strong id="precio">[^<]*</strong>', '<strong id="precio">%s</strong>' % pesos(precio), t)
    t = re.sub(r'<s id="precio-antes">[^<]*</s>', '<s id="precio-antes">%s</s>' % base, t)
    t = re.sub(r'<strong id="precio-barra">[^<]*</strong>', '<strong id="precio-barra">%s</strong>' % pesos(precio), t)
    t = re.sub(r'<span id="variante-barra">[^<]*</span>', '<span id="variante-barra">%s</span>' % (' · '.join(v for v in (info['color'], info['tamano']) if v not in (SIN_COLOR, SIN_TAMANO)) or 'IVA incluido'), t)
    if antes:
        pct = round((1 - precio / antes) * 100)
        t = t.replace('Descuento del 20 %', 'Descuento del %d %%' % pct).replace('<span aria-hidden="true">−20 %</span>', '<span aria-hidden="true">−%d %%</span>' % pct)
        t = t.replace('const DESCUENTO = 20;', 'const DESCUENTO = %d;' % pct)
    if not info.get('sello'):
        t = re.sub(r'\n      <details class="destacada">.*?</details>\n', '\n', t, count=1, flags=re.S)
    t = re.sub(r'(<ol><li><a href="inicio.html">Inicio</a></li>)<li><a href="[^"]*">[^<]*</a></li>(</ol>)', lambda m: '<ol>' + migas_html(info['cat']) + '</ol>', t, count=1)
    estado = 'oferta' if antes else 'agotado' if info.get('agotado') else ''
    if estado:
        t = t.replace('<body>', '<body data-estado="%s">' % estado, 1)
    # Ficha técnica, relato y preguntas
    t = re.sub(r'<dt>Medidas</dt><dd>.*?</dd>', '<dt>Medidas</dt><dd>%s</dd>' % (P % '[POR CONFIRMAR]'), t, count=1)
    t = re.sub(r'<dt>Peso</dt><dd>.*?</dd>', '<dt>Peso</dt><dd>%s</dd>' % (P % '[POR CONFIRMAR]'), t, count=1)
    t = re.sub(r'<dt>Material</dt><dd>.*?</dd>', '<dt>Material</dt><dd>%s</dd>' % info['material'], t, count=1)
    t = re.sub(r'<dt>Acabado</dt><dd>.*?</dd>', '<dt>Acabado</dt><dd>%s</dd>' % (P % '[POR CONFIRMAR]'), t, count=1)
    t = re.sub(r'<dt>Cuidados</dt><dd>.*?</dd>', '<dt>Cuidados</dt><dd>%s</dd>' % (P % '[POR CONFIRMAR con el proveedor]'), t, count=1)
    t = re.sub(r'<dt>En la caja</dt><dd>.*?</dd>', '<dt>En la caja</dt><dd>%s</dd>' % (P % '[POR CONFIRMAR]'), t, count=1)
    t = re.sub(r'<dt>Origen</dt><dd>.*?</dd>', '<dt>Origen</dt><dd>%s</dd>' % info['origen'], t, count=1)
    t = re.sub(r'(<h3>Diseño <span>· nuestra lectura de la forma</span></h3>\s*)<p>.*?</p>', r'\1<p>%s</p>' % (P % '[LECTURA DE DISEÑO PENDIENTE]'), t, count=1, flags=re.S)
    t = re.sub(r'(<div class="nivel historia">\s*<h3>Historia <span>· una propuesta, no un hecho</span></h3>\s*)<p>.*?</p>', r'\1<p>%s</p>' % (P % '[PROPUESTA PENDIENTE]').replace('class="pendiente"', 'class="pendiente" style="font-style:normal"'), t, count=1, flags=re.S)
    t = t.replace('<span class="relato">Tipo de relato: por comenzar</span>', '<span class="relato">Tipo de relato: %s</span>' % P % '[POR CONFIRMAR]')
    t = re.sub(r'<details class="faq"><summary>¿Se puede usar con agua y flores naturales\?</summary>.*?</details>',
               '<details class="faq"><summary>¿Cómo se limpia?</summary><p>%s</p></details>' % (P % '[POR CONFIRMAR con el proveedor]'), t, flags=re.S)
    t = re.sub(r'<details class="faq"><summary>¿Incluye las flores de la foto\?</summary>.*?</details>',
               '<details class="faq"><summary>¿De dónde viene esta pieza?</summary><p>%s. Lo decimos en la ficha técnica, junto al material.</p></details>' % info['origen'], t, flags=re.S)
    t = t.replace('<section class="bloque" id="tres-d" aria-labelledby="t-3d">', '<section class="bloque" id="tres-d" aria-labelledby="t-3d" hidden>')
    t = re.sub(r'<a class="enlace-boton" href="coleccion-primer-hogar.html">Ver la colección Primer hogar</a>',
               '<a class="enlace-boton" href="%s">Ver más en %s</a>' % (info['cat'][1], info['cat'][0]), t, count=1)
    # Piezas que combinan: otras de la misma categoría
    if hermanos:
        lis = ''.join('      <li><a href="%s"><div class="foto">%s</div><h3>%s</h3><p>%s</p></a></li>\n'
                      % (h['archivo'], arte(*h['dibujo']) if h.get('dibujo') else '[FOTO DEL PRODUCTO]', h['nombre'], pesos(h['precio'])) for h in hermanos)
        t = re.sub(r'(<ul class="combinan">\n).*?(    </ul>)', lambda m: m.group(1) + lis + m.group(2), t, count=1, flags=re.S)
    return t


def con_arte(t, dibujo):
    i = t.index('<li class="con-arte">') + len('<li class="con-arte">')
    j = t.index('</svg>', i) + len('</svg>')
    return t[:i] + arte(*dibujo) + t[j:]


# ---------------------------------------------------------------- piezas
plantilla = io.open(os.path.join(dest, 'ficha-producto.html'), encoding='utf-8').read()
plantilla = plantilla.replace('.combinan .foto{aspect-ratio:4/5;background:var(--perla);display:grid;place-content:center;',
                              '.combinan .foto{aspect-ratio:4/5;background:var(--suave);display:flex;align-items:flex-end;justify-content:center;padding:var(--s2);')
for info in REG.values():
    info['color'] = info.get('color') or COLORES.get((info.get('dibujo') or ('', ''))[1], SIN_COLOR)
    info['tamano'] = info.get('tamano') or SIN_TAMANO
    info.setdefault('cat', cat_por_nombre(info['nombre']))
hechas = 0
for archivo, info in REG.items():
    hermanos = [h for h in REG.values() if h['cat'][1] == info['cat'][1] and h is not info][:3]
    if len(hermanos) < 3:
        hermanos += [h for h in REG.values() if h is not info and h not in hermanos][:3 - len(hermanos)]
    t = personalizar(plantilla, info, hermanos)
    if info.get('dibujo'):
        t = con_arte(t, info['dibujo'])
    io.open(os.path.join(dest, archivo), 'w', encoding='utf-8', newline='\n').write(t)
    hechas += 1
print('fichas de piezas:', hechas)

# ---------------------------------------------------------------- lámparas
exec(io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'construir_ficha_lampara.py'), encoding='utf-8').read())
plantilla_luz = io.open(os.path.join(dest, 'ficha-lampara.html'), encoding='utf-8').read()
LUZ = []
for k, (nombre, precio, tonos, lx, ly, dibujo) in enumerate(LAMPARAS):
    LUZ.append(dict(nombre=nombre, precio=int(precio.replace('$', '').replace('.', '')), tonos=tonos, lx=lx, ly=ly, dibujo_svg=dibujo,
                    archivo='ficha-lampara.html' if k == 0 else 'lampara-%d.html' % (k + 1), material='[Material]', origen='[Origen]',
                    color=SIN_COLOR, tamano=SIN_TAMANO, cat=('Lámparas', 'lamparas.html', 'Decoraciones del hogar')))
for info in LUZ:
    t = personalizar(plantilla_luz, info, [l2 for l2 in LUZ if l2 is not info][:0])
    t = re.sub(r'<li class="luz-foto" data-tonos="\d"><div class="escena" style="[^"]*"><span class="halo"></span><svg viewBox="0 0 200 250" aria-hidden="true" focusable="false">.*?</svg>',
               lambda m: '<li class="luz-foto" data-tonos="%d"><div class="escena" style="--lx:%d%%;--ly:%d%%"><span class="halo"></span><svg viewBox="0 0 200 250" aria-hidden="true" focusable="false">%s</svg>'
               % (info['tonos'], info['lx'], info['ly'], info['dibujo_svg']), t, count=1, flags=re.S)
    if info['tonos'] == 1:
        t = r1(t, '<fieldset class="tonos">', '<fieldset class="tonos" hidden>')
        t = re.sub(r'<dt>Luz</dt><dd>.*?</dd>', '<dt>Luz</dt><dd>Solo luz cálida. %s</dd>' % (P % '[POR CONFIRMAR: bombillo, potencia y voltaje]'), t, count=1)
        t = re.sub(r'<details class="faq"><summary>¿Cómo se cambia el tono de la luz\?</summary>.*?</details>',
                   '<details class="faq"><summary>¿Se puede cambiar el tono de la luz?</summary><p>No. Esta lámpara tiene solo luz cálida.</p></details>', t, flags=re.S)
        t = t.replace('Tiene tres tonos de luz: cálida, neutra y fría.', 'Tiene solo luz cálida.')
    else:
        t = re.sub(r'<dt>Luz</dt><dd>.*?</dd>', '<dt>Luz</dt><dd>Tres tonos: cálida, neutra y fría. %s</dd>' % (P % '[POR CONFIRMAR: bombillo, potencia y voltaje]'), t, count=1)
    t = re.sub(r'<small>\[ILUSTRACIÓN DE EJEMPLO\][^<]*</small>', '<small>[ILUSTRACIÓN DE EJEMPLO] Aquí van las fotos reales: apagada y encendida%s</small>' % (' en cada tono' if info['tonos'] == 3 else ''), t, count=1)
    io.open(os.path.join(dest, info['archivo']), 'w', encoding='utf-8', newline='\n').write(t)
# La lista de lámparas enlaza cada tarjeta con su ficha
h = io.open(os.path.join(dest, 'lamparas.html'), encoding='utf-8').read()
for info in LUZ[1:]:
    h = h.replace('<a href="/decoracion/lamparas/ejemplo" data-proto>', '<a href="%s">' % info['archivo'], 1)
io.open(os.path.join(dest, 'lamparas.html'), 'w', encoding='utf-8', newline='\n').write(h)
print('fichas de lámparas:', len(LUZ))

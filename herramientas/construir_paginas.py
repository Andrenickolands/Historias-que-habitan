import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from arte import arte
dest = sys.argv[1]

FUENTES = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
           '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500..600;1,500&family=Jost:wght@400..500&display=swap" rel="stylesheet">')

WA_ICONO = ('<svg class="icono" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.5a8.5 8.5 0 0 0-7.3 12.85L3.5 20.5l4.3-1.1A8.5 8.5 0 1 0 12 3.5Z"/>'
            '<path d="M9.2 8.6c-.3 2.9 2.3 5.8 5.3 6.2l1-1.3-1.7-1-.7.7c-.9-.4-1.7-1.2-2.1-2.1l.7-.7-1-1.7z"/></svg>')

CATEGORIAS = [('Porcelanas y figuras', '/porcelanas', None), ('Jarrones y recipientes', '/jarrones', 'categoria.html'),
              ('Flores artificiales', '/flores-artificiales', None), ('Mesa', '/mesa', None),
              ('Centros de mesa', '/centros-de-mesa', None), ('Esculturas pequeñas', '/esculturas', None),
              ('Decoraciones del hogar', '/decoracion', None)]


def enlace(nombre, url, archivo, extra=''):
    if archivo:
        return '<a href="%s"%s>%s</a>' % (archivo, extra, nombre)
    return '<a href="%s" data-proto%s>%s</a>' % (url, extra, nombre)


def cabecera(actual):
    cats = '\n'.join('        <li>%s</li>' % enlace(n, u, a, ' aria-current="page"' if n == actual else '') for n, u, a in CATEGORIAS)
    cats += ('\n        <li><a href="lamparas.html" style="padding-left:var(--s4);font:400 1rem/1.5 var(--texto)"%s>Lámparas</a></li>'
             % (' aria-current="page"' if actual == 'Lámparas' else ''))
    return '''<a class="salto" href="#contenido">Saltar al contenido</a>
<header class="cabecera">
  <div class="ancho">
    <button class="boton-icono solo-movil" type="button" data-abrir-menu aria-label="Abrir el menú"><svg class="icono" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
    <!-- [LOGO SVG PENDIENTE] -->
    <a class="marca" href="inicio.html" translate="no">Historias que Habitan</a>
    <nav class="nav-escritorio" aria-label="Principal">
      <button type="button" data-abrir-menu>Tienda</button>
      <a href="/colecciones" data-proto>Colecciones</a>
      <a href="/historias" data-proto>Historias</a>
      <a href="quiz-orientacion.html">Orientación</a>
      <a href="/por-mayor" data-proto>Por mayor</a>
    </nav>
    <button class="boton-icono" type="button" data-abrir-menu aria-label="Buscar"><svg class="icono" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="m16 16 4.5 4.5"/></svg></button>
    <a class="boton-icono" href="/carrito" aria-label="Carrito, 0 piezas" data-proto><svg class="icono" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 8h14l-1 12H6L5 8Z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg></a>
  </div>
</header>

<dialog class="panel" id="menu" aria-labelledby="t-menu">
  <div class="panel-cab"><h2 id="t-menu" tabindex="-1">Menú</h2><button class="boton-icono" type="button" data-cerrar aria-label="Cerrar el menú"><svg class="icono" viewBox="0 0 24 24" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg></button></div>
  <div class="panel-cuerpo">
    <form class="buscar" role="search">
      <label class="oculto-visual" for="q">Buscar en la tienda</label>
      <input id="q" name="q" type="search" placeholder="Buscar: jarrón, vajilla…" autocomplete="off" enterkeyhint="search">
      <button class="boton secundario" type="submit">Buscar</button>
    </form>
    <nav aria-label="Menú de la tienda">
      <p class="menu-titulo" id="m-tienda">Tienda</p>
      <ul class="menu-lista grande" aria-labelledby="m-tienda">
''' + cats + '''
      </ul>
      <p class="menu-titulo" id="m-col">Colecciones</p>
      <ul class="menu-lista" aria-labelledby="m-col">
        <li><a href="/colecciones/la-mesa-que-recibe" data-proto>La mesa que recibe</a></li>
        <li><a href="/colecciones/primer-hogar" data-proto>Primer hogar</a></li>
        <li><a href="/colecciones/regalos-que-se-guardan" data-proto>Regalos que se guardan</a></li>
      </ul>
      <ul class="menu-lista">
        <li><a href="/historias" data-proto>Historias</a></li>
        <li><a href="quiz-orientacion.html">Orientación: le ayudamos a elegir</a></li>
        <li><a href="/por-mayor" data-proto>Por mayor</a></li>
        <li><a href="/seguimiento" data-proto>Seguir mi pedido</a></li>
        <li><a href="#" data-wa>Ayuda por WhatsApp</a></li>
      </ul>
    </nav>
  </div>
</dialog>
'''


PIE = '''<footer class="pie">
  <div class="ancho">
    <ul>
      <li><a href="/envios" data-proto>Envíos</a></li><li><a href="/cambios-y-garantia" data-proto>Cambios y garantía</a></li>
      <li><a href="/pieza-rota" data-proto>Reportar una pieza rota</a></li><li><a href="/seguimiento" data-proto>Seguir mi pedido</a></li>
      <li><a href="/nosotros" data-proto>Nosotros</a></li><li><a href="/por-mayor" data-proto>Por mayor</a></li>
      <li><a href="/politica-de-datos" data-proto>Tratamiento de datos</a></li><li><a href="#" data-wa>Ayuda por WhatsApp</a></li>
    </ul>
    <p>Historias que Habitan · Decoración y objetos para el hogar · <span class="pendiente">[POR CONFIRMAR: razón social, NIT y correo]</span></p>
    <p>Superintendencia de Industria y Comercio: <a href="https://www.sic.gov.co" rel="noopener" style="min-height:0;display:inline">www.sic.gov.co</a></p>
  </div>
</footer>

<div class="cookies" id="cookies" role="region" aria-label="Aviso de cookies" hidden>
  <p>Usamos cookies necesarias para que la tienda funcione y, si usted acepta, otras para medir las visitas. <a href="/politica-de-cookies" data-proto>Política de cookies</a> <span class="pendiente">[POR CONFIRMAR: texto legal]</span></p>
  <div><button class="boton secundario" type="button" data-cookies="necesarias">Solo las necesarias</button><button class="boton secundario" type="button" data-cookies="todas">Aceptar todas</button></div>
</div>
<a class="wa-flotante" href="#" data-wa aria-label="Ayuda por WhatsApp">''' + WA_ICONO + '''</a>
<p id="aviso-proto" hidden style="position:fixed;left:16px;right:88px;bottom:16px;z-index:30;max-width:420px;background:var(--tinta);color:var(--hueso);padding:12px 16px;border-radius:6px;font-size:.9375rem">Prototipo: esta página todavía no existe.</p>
<p class="oculto-visual" id="anuncio" aria-live="polite"></p>
<script src="base.js"></script>
'''


def tarjeta(nombre, meta, precio, antes=None, sello=False, agotado=False, datos='', href=None, dibujo=None):
    p = '<strong>%s</strong>' % precio
    if antes:
        p = ('<span class="oculto-visual">Ahora </span><strong>%s</strong><span class="oculto-visual">. Antes </span><s>%s</s>'
             '<span class="oferta"><span class="oculto-visual">. Descuento del 20 %%. </span><span aria-hidden="true">−20 %%</span></span>') % (precio, antes)
    a = '<a href="%s">' % href if href else '<a href="/jarrones/ejemplo" data-proto>'
    return ('    <li class="tarjeta"%s>%s<div class="foto">%s%s</div><h3>%s</h3><p class="meta">%s</p><p class="precio">%s</p>%s</a></li>\n'
            % (datos, a, '<span class="sello">Exclusivo</span>' if sello else '',
               arte(*dibujo) if dibujo else '<span class="recorte">[FOTO DEL PRODUCTO]</span>', nombre, meta, p,
               '<p class="agotado-txt">Agotado por ahora</p>' if agotado else ''))


def pagina(titulo, descripcion, estilos, cuerpo, actual=None, guion=''):
    return '''<!doctype html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#FBFAF9">
<title>%s</title>
<meta name="description" content="%s">
%s
<link rel="stylesheet" href="base.css">
<style>%s</style>
</head>
<body>
%s
%s
%s%s</body>
</html>
''' % (titulo, descripcion, FUENTES, estilos, cabecera(actual), cuerpo, PIE, guion)


# ---------------------------------------------------------------- INICIO
CSS_INICIO = r'''
.portada{display:grid;gap:var(--s5);padding:var(--s5) 0 var(--s6)}
.portada h1{font-size:2.375rem;line-height:1.08}
.portada .apoyo{font-size:1.125rem;line-height:1.5;margin-top:var(--s3);max-width:44ch}
.portada .acciones{display:flex;flex-wrap:wrap;align-items:center;gap:var(--s3) var(--s5);margin-top:var(--s5)}
.portada .foto{aspect-ratio:4/5;margin:0 calc(var(--s4) * -1)}
.frase{font:italic 500 1.5rem/1.25 var(--titulo);margin-top:var(--s5);padding-top:var(--s4);border-top:1px solid var(--perla);max-width:28ch}
.tramo{padding:var(--s7) 0 0}
.tramo>h2,.tramo .cab h2{font-size:2rem;line-height:1.12}
.tramo .cab{display:flex;align-items:baseline;justify-content:space-between;flex-wrap:wrap;gap:var(--s1) var(--s4);margin-bottom:var(--s4)}
.categorias{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s4) var(--s3);list-style:none;margin:var(--s4) 0 0;padding:0}
.categorias a{display:block;text-decoration:none}
.categorias .foto{aspect-ratio:1;margin-bottom:var(--s2)}
.categorias span{font:600 1.25rem/1.2 var(--titulo)}
.categorias a:hover span{text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px}
.categorias li:last-child{grid-column:1/-1}
.categorias li:last-child .foto{aspect-ratio:2/1}
.coleccion{color:var(--hueso);display:grid}
.coleccion .foto{aspect-ratio:4/3;background:rgba(251,250,249,.16);color:var(--hueso)}
.coleccion div{padding:var(--s5) var(--s4) var(--s6)}
.coleccion h3{font-size:2rem;line-height:1.1}
.coleccion p{margin:var(--s2) 0 var(--s5);max-width:40ch}
.coleccion :focus-visible{outline-color:var(--hueso)}
.colecciones{margin:var(--s4) calc(var(--s4) * -1) 0;display:grid}
.c-mesa{background:var(--borgona)} .c-mesa h3{color:var(--champagne)}
.c-hogar{background:var(--mocha)} .c-regalo{background:var(--espresso)}
.c-hogar .foto,.c-regalo .foto{display:none}
.metodo{display:grid;gap:var(--s5)}
.metodo dl{margin:0;border-top:1px solid var(--tinta)}
.metodo dt{font:600 1.5rem/1.2 var(--titulo);padding-top:var(--s4)}
.metodo dd{margin:var(--s1) 0 0;padding-bottom:var(--s4);border-bottom:1px solid var(--perla);max-width:56ch}
.metodo .origen{font:italic 500 1.375rem/1.3 var(--titulo);max-width:30ch}
.tranquila{list-style:none;margin:var(--s4) 0 0;padding:0;border-top:1px solid var(--tinta)}
.tranquila li{padding:var(--s4) 0;border-bottom:1px solid var(--perla);display:grid;gap:var(--s1)}
.tranquila strong{font-weight:500}
.banda{background:var(--oatmeal);margin:var(--s7) calc(var(--s4) * -1) 0;padding:var(--s6) var(--s4)}
.banda h2{font-size:1.875rem;line-height:1.15;max-width:18ch}
.banda p{margin:var(--s2) 0 var(--s5);max-width:44ch}
.guias{list-style:none;margin:0;padding:0;border-top:1px solid var(--tinta)}
.guias li{border-bottom:1px solid var(--perla)}
.guias a{display:block;padding:var(--s4) 0;text-decoration:none}
.guias h3{font-size:1.375rem;line-height:1.25}
.guias a:hover h3{text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px}
.guias p{font-size:.875rem;color:var(--cafe-humo);margin-top:var(--s1)}
.mayor{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:var(--s3) var(--s5);border-top:1px solid var(--tinta);border-bottom:1px solid var(--tinta);padding:var(--s4) 0;margin-top:var(--s7)}
@media (min-width:640px){
  .portada h1{font-size:3rem}
  .portada .foto{margin:0}
  .categorias{grid-template-columns:repeat(4,minmax(0,1fr))}
  .categorias li:last-child{grid-column:span 2}
  .colecciones{margin-left:0;margin-right:0;grid-template-columns:1fr 1fr}
  .c-mesa{grid-column:1/-1;grid-template-columns:1fr 1fr;align-items:center}
  .banda{margin-left:0;margin-right:0;padding:var(--s7) var(--s6)}
}
@media (min-width:960px){
  .portada{grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:var(--s8);align-items:center;padding:var(--s7) 0}
  .portada h1{font-size:3.75rem;line-height:1.04}
  .portada .foto{aspect-ratio:1}
  .tramo{padding-top:var(--s8)}
  .tramo>h2,.tramo .cab h2{font-size:2.5rem}
  .metodo{grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:var(--s8)}
  .tranquila{display:grid;grid-template-columns:1fr 1fr;column-gap:var(--s8)}
  .banda{margin-top:var(--s8)}
}
'''

cats_inicio = '\n'.join('      <li>%s</li>' % enlace('<div class="foto">[FOTO DE LA CATEGORÍA]</div><span>%s</span>' % n, u, a) for n, u, a in CATEGORIAS)

CUERPO_INICIO = ('''<main id="contenido">
  <div class="ancho">
    <section class="portada">
      <div>
        <h1>Porcelanas, jarrones y piezas para su mesa y su casa</h1>
        <p class="apoyo">Decoración y objetos para el hogar, elegidos uno por uno. De cada pieza le contamos el material, las medidas, el origen y lo que sabemos de su forma. Envíos a todo el país.</p>
        <div class="acciones">
          <a class="boton" href="#categorias">Ver la tienda</a>
          <a class="enlace" href="quiz-orientacion.html">Ayúdeme a elegir</a>
        </div>
        <p class="frase">Hay objetos que no solo decoran. Cuentan historias.</p>
      </div>
      <!-- Imagen principal: en el HTML, con prioridad de carga y sin carga diferida -->
      <div class="foto">[FOTO PRINCIPAL: una pieza real en una casa, con luz natural]</div>
    </section>

    <section class="tramo" id="categorias" aria-labelledby="t-cat">
      <h2 id="t-cat">La tienda, por tipo de objeto</h2>
      <ul class="categorias">
''' + cats_inicio + '''
      </ul>
    </section>

    <section class="tramo" aria-labelledby="t-col">
      <h2 id="t-col">O empiece por el momento</h2>
      <div class="colecciones">
        <article class="coleccion c-mesa">
          <div class="foto">[FOTO DE LA COLECCIÓN: mesa servida]</div>
          <div><h3>La mesa que recibe</h3><p>Vajillas, cristalería y centros de mesa que funcionan juntos. <span class="pendiente">[TEXTO DE EJEMPLO]</span></p><a class="boton claro" href="/colecciones/la-mesa-que-recibe" data-proto>Ver la colección</a></div>
        </article>
        <article class="coleccion c-hogar">
          <div class="foto"></div>
          <div><h3>Primer hogar</h3><p>Pocas piezas que combinan, para empezar una casa. <span class="pendiente">[TEXTO DE EJEMPLO]</span></p><a class="boton claro" href="/colecciones/primer-hogar" data-proto>Ver la colección</a></div>
        </article>
        <article class="coleccion c-regalo">
          <div class="foto"></div>
          <div><h3>Regalos que se guardan</h3><p>Para bodas, inauguraciones y fechas especiales. <span class="pendiente">[TEXTO DE EJEMPLO]</span></p><a class="boton claro" href="/colecciones/regalos-que-se-guardan" data-proto>Ver la colección</a></div>
        </article>
      </div>
    </section>

    <section class="tramo" aria-labelledby="t-piezas">
      <div class="cab"><h2 id="t-piezas">Piezas de la selección</h2><a class="enlace" href="categoria.html">Ver jarrones y recipientes</a></div>
      <ul class="rejilla estanteria" id="piezas">
''' + tarjeta('Jarrón de cerámica blanca con asas', 'Cerámica · Hecho en China', '$189.900 <span class="pendiente">[EJEMPLO]</span>', sello=True, href='ficha-producto.html', dibujo=('anfora', '#F1EEE8'))
    + tarjeta('[Jarrón alto de porcelana]', 'Porcelana · Hecho en China', '$319.900', dibujo=('alto', '#F4F2EE'))
    + tarjeta('[Recipiente pequeño de cerámica]', 'Cerámica · Hecho en Panamá', '$79.900', antes='$99.900', dibujo=('cuenco', '#D9C7AE'))
    + tarjeta('[Florero de vidrio transparente]', 'Vidrio · Hecho en China', '$69.900', dibujo=('florero', '#DDE6E8', True)) + '''      </ul>
    </section>

    <section class="tramo metodo" aria-labelledby="t-metodo">
      <div>
        <h2 id="t-metodo">Cómo contamos cada pieza</h2>
        <p class="origen" style="margin-top:var(--s4)">Nuestras piezas vienen de China y Panamá, y lo decimos en cada ficha.</p>
      </div>
      <dl>
        <dt>Hecho</dt><dd>Lo que se puede comprobar: material, medidas, origen y, cuando existe, un dato histórico con su fuente.</dd>
        <dt>Diseño</dt><dd>Nuestra lectura de la forma y los acabados. Es una interpretación y así la presentamos.</dd>
        <dt>Historia</dt><dd>Una propuesta sobre el lugar que la pieza puede tener en su casa. No es un hecho que ya ocurrió.</dd>
      </dl>
    </section>

    <section class="tramo" aria-labelledby="t-tranquila">
      <h2 id="t-tranquila">Antes de comprar</h2>
      <ul class="tranquila">
        <li><strong>Envíos a todo el país</strong><span>El costo y el tiempo se calculan con su ciudad antes de pagar. <span class="pendiente">[POR CONFIRMAR: operador]</span></span></li>
        <li><strong>Embalaje para piezas frágiles</strong><span>Si una pieza llega rota, la reponemos o le devolvemos el dinero. <span class="pendiente">[POR CONFIRMAR: política]</span></span></li>
        <li><strong>Precio con IVA incluido</strong><span>Tarjeta, PSE, Nequi y Daviplata. <span class="pendiente">[POR CONFIRMAR: pasarela]</span></span></li>
        <li><strong>Cambios, garantía y retracto</strong><span><a href="/cambios-y-garantia" data-proto>Lea las condiciones</a> antes de comprar. <span class="pendiente">[POR CONFIRMAR: revisión legal]</span></span></li>
      </ul>
    </section>

    <section class="banda" aria-labelledby="t-orienta">
      <h2 id="t-orienta">¿No sabe por dónde empezar?</h2>
      <p>Responda cuatro o cinco preguntas y le mostramos una colección o dos categorías para su espacio. No le pedimos datos para ver el resultado.</p>
      <a class="boton secundario" href="quiz-orientacion.html">Empezar el cuestionario</a>
    </section>

    <section class="tramo" aria-labelledby="t-historias">
      <div class="cab"><h2 id="t-historias">Historias</h2><a class="enlace" href="/historias" data-proto>Ver todas las guías</a></div>
      <ul class="guias">
        <li><a href="/historias/como-poner-la-mesa-para-recibir" data-proto><h3>[GUÍA PENDIENTE] Cómo poner la mesa para recibir</h3><p>Guía · [Autora] · Actualizada el [fecha]</p></a></li>
        <li><a href="/historias/el-pesebre-en-casa" data-proto><h3>[GUÍA PENDIENTE] El pesebre en casa</h3><p>Costumbres · [Autora] · Actualizada el [fecha]</p></a></li>
      </ul>
    </section>

    <p class="mayor"><span>¿Compra para un negocio? Cotizamos por volumen y le respondemos por WhatsApp.</span><a class="enlace" href="/por-mayor" data-proto>Solicitar cotización por mayor</a></p>
  </div>
</main>
''')

io.open(dest + '/inicio.html', 'w', encoding='utf-8', newline='\n').write(pagina(
    'Historias que Habitan · Decoración y objetos para el hogar',
    'Porcelanas, jarrones, flores artificiales, vajillas y cristalería. Tienda en línea de decoración y objetos para el hogar, con envíos a todo el país.',
    CSS_INICIO, CUERPO_INICIO))

# ---------------------------------------------------------------- CATEGORÍA
CSS_CAT = r'''
.migas{font-size:.875rem;padding:var(--s2) 0}
.migas ol{list-style:none;display:flex;flex-wrap:wrap;gap:var(--s2);margin:0;padding:0}
.migas li+li::before{content:"/";margin-right:var(--s2);color:var(--cafe-humo)}
.migas a{display:inline-flex;align-items:center;min-height:44px}
.migas [aria-current]{display:inline-flex;align-items:center;min-height:44px;color:var(--cafe-humo)}
.intro h1{font-size:2.25rem;line-height:1.1}
.intro p{margin-top:var(--s3);max-width:62ch}
.barra-lista{position:sticky;top:64px;z-index:10;background:var(--hueso);display:flex;align-items:center;gap:var(--s3);padding:var(--s3) 0;margin-top:var(--s5);border-top:1px solid var(--tinta);border-bottom:1px solid var(--perla)}
.barra-lista .boton{min-height:44px;padding:0 var(--s4)}
#n-filtros{margin-left:.4em}
.barra-lista label{margin-left:auto;font-size:.875rem;color:var(--cafe-humo)}
.barra-lista select{min-height:44px;max-width:150px;font:inherit;color:var(--tinta);background:#fff;border:1px solid var(--cafe-humo);border-radius:2px;padding:0 var(--s2)}
.estado-lista{display:flex;flex-wrap:wrap;align-items:center;gap:var(--s2);padding:var(--s3) 0 var(--s4)}
.estado-lista p{margin-right:var(--s2);font-variant-numeric:tabular-nums}
.ficha-filtro{display:inline-flex;align-items:center;gap:var(--s1);min-height:36px;padding:0 var(--s1) 0 var(--s3);font:inherit;font-size:.875rem;color:var(--tinta);background:var(--oatmeal);border:1px solid var(--tinta);border-radius:999px;cursor:pointer}
.ficha-filtro svg{width:18px;height:18px}
.ficha-filtro:hover{background:var(--piedra)}
.vacio{padding:var(--s6) var(--s4);background:var(--suave);border-radius:6px;display:grid;gap:var(--s3);justify-items:start}
.vacio h2{font-size:1.5rem}
.mas{display:flex;justify-content:center;padding-top:var(--s6)}
.vistas{display:inline-flex;margin-left:auto;border:1px solid var(--cafe-humo);border-radius:2px;overflow:hidden}
.vistas button{min-height:44px;padding:0 var(--s3);font:inherit;font-size:.875rem;color:var(--tinta);background:var(--hueso);border:0;cursor:pointer}
.vistas button:focus-visible{outline-offset:-3px}
.vistas button[aria-pressed=true]{background:var(--tinta);color:var(--hueso)}
.texto-cat{margin-top:var(--s8);display:grid;gap:var(--s6)}
.texto-cat h2{font-size:1.75rem;line-height:1.2;margin-bottom:var(--s3)}
.texto-cat p{max-width:62ch}
.faq{border-top:1px solid var(--perla);max-width:68ch}
.faq summary{min-height:48px;padding:var(--s3) 0;cursor:pointer;font-weight:500}
.faq p{padding-bottom:var(--s4)}
#filtros{margin:auto 0 0;width:100%;max-width:100%;max-height:86dvh;border-radius:12px 12px 0 0}
#filtros[open]{animation:subir 300ms var(--curva)}
#filtros fieldset{border:0;padding:0;margin:0 0 var(--s5);min-width:0}
#filtros legend{font-weight:500;padding:0;margin-bottom:var(--s1)}
.casilla{display:flex;align-items:center;gap:var(--s3);min-height:44px;cursor:pointer}
.casilla input{flex:none;width:22px;height:22px;margin:0;accent-color:var(--tinta)}
.dos-col{display:grid;grid-template-columns:1fr 1fr;column-gap:var(--s4)}
.cargando .tarjeta .foto,.cargando .tarjeta h3,.cargando .tarjeta .meta,.cargando .tarjeta .precio{color:transparent;background:linear-gradient(100deg,var(--suave) 30%,var(--oatmeal) 50%,var(--suave) 70%) 0 0/300% 100%;border-radius:2px;animation:brillo 1.4s linear infinite}
.cargando .tarjeta *{color:transparent!important;border-color:transparent!important}
.cargando .tarjeta .sello,.cargando .tarjeta .oferta,.cargando .tarjeta s{visibility:hidden}
@keyframes brillo{to{background-position:-150% 0}}
@media (min-width:640px){.intro h1{font-size:2.75rem}}
@media (min-width:960px){
  .barra-lista{top:72px}
  .texto-cat{grid-template-columns:1fr 1fr;gap:var(--s8)}
  #filtros{margin:0 0 0 auto;width:440px;height:100dvh;max-height:100dvh;border-radius:0}
}
'''


def d(material, color, tamano, ambiente, precio):
    return ' data-material="%s" data-color="%s" data-tamano="%s" data-ambiente="%s" data-precio="%d"' % (material, color, tamano, ambiente, precio)


tarjetas_cat = (
    tarjeta('Jarrón de cerámica blanca con asas', 'Cerámica · Hecho en China', '$189.900', sello=True, datos=d('Cerámica', 'Blanco', 'Mediano', 'Entrada', 189900), dibujo=('anfora', '#F1EEE8'), href='ficha-producto.html')
    + tarjeta('[Jarrón de vidrio ámbar]', 'Vidrio · Hecho en China', '$129.900', datos=d('Vidrio', 'Ámbar', 'Mediano', 'Sala', 129900), dibujo=('panza', '#B8752A', True))
    + tarjeta('[Recipiente pequeño de cerámica]', 'Cerámica · Hecho en Panamá', '$79.900', antes='$99.900', datos=d('Cerámica', 'Arena', 'Pequeño', 'Mesa', 79900), dibujo=('cuenco', '#D9C7AE'))
    + tarjeta('[Jarrón alto de porcelana]', 'Porcelana · Hecho en China', '$319.900', datos=d('Porcelana', 'Blanco', 'Grande', 'Sala', 319900), dibujo=('alto', '#F4F2EE'))
    + tarjeta('[Florero de vidrio transparente]', 'Vidrio · Hecho en China', '$69.900', datos=d('Vidrio', 'Transparente', 'Pequeño', 'Mesa', 69900), dibujo=('florero', '#DDE6E8', True))
    + tarjeta('[Ánfora decorativa de cerámica]', 'Cerámica · Hecho en China', '$259.900', agotado=True, datos=d('Cerámica', 'Arena', 'Grande', 'Entrada', 259900), dibujo=('anfora', '#D9C7AE'))
    + tarjeta('[Jarrón de porcelana con relieve]', 'Porcelana · Hecho en Panamá', '$219.900', sello=True, datos=d('Porcelana', 'Blanco', 'Mediano', 'Sala', 219900), dibujo=('relieve', '#F4F2EE'))
    + tarjeta('[Recipiente con tapa de cerámica]', 'Cerámica · Hecho en China', '$99.900', datos=d('Cerámica', 'Verde', 'Pequeño', 'Mesa', 99900), dibujo=('tarro', '#6E7F68')))


def grupo(titulo, nombre, valores):
    c = ''.join('<label class="casilla"><input type="checkbox" name="%s" value="%s"><span>%s</span></label>' % (nombre, v, v) for v in valores)
    return '<fieldset><legend>%s</legend><div class="dos-col">%s</div></fieldset>\n' % (titulo, c)


FILTROS = ('''
<dialog class="panel" id="filtros" aria-labelledby="t-filtros">
  <div class="panel-cab"><h2 id="t-filtros" tabindex="-1">Filtrar</h2><button class="boton-icono" type="button" data-cerrar aria-label="Cerrar los filtros"><svg class="icono" viewBox="0 0 24 24" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg></button></div>
  <form class="panel-cuerpo" id="form-filtros">
''' + grupo('Material', 'material', ['Cerámica', 'Porcelana', 'Vidrio'])
    + grupo('Color', 'color', ['Blanco', 'Arena', 'Ámbar', 'Verde', 'Transparente'])
    + grupo('Tamaño', 'tamano', ['Pequeño', 'Mediano', 'Grande'])
    + grupo('Ambiente', 'ambiente', ['Sala', 'Mesa', 'Entrada'])
    + '''<fieldset><legend>Precio <span class="pendiente">[POR CONFIRMAR: rangos]</span></legend>
      <label class="casilla"><input type="radio" name="precio" value="" checked><span>Cualquier precio</span></label>
      <label class="casilla"><input type="radio" name="precio" value="0-100000"><span>Hasta $100.000</span></label>
      <label class="casilla"><input type="radio" name="precio" value="100000-250000"><span>De $100.000 a $250.000</span></label>
      <label class="casilla"><input type="radio" name="precio" value="250000-9999999"><span>Más de $250.000</span></label>
    </fieldset>
  </form>
  <div class="panel-pie"><button class="enlace" type="button" id="borrar-panel">Borrar todo</button><button class="boton" type="submit" form="form-filtros" id="ver-piezas">Ver 8 piezas</button></div>
</dialog>
''')

CUERPO_CAT = '''<div class="proto" role="region" aria-label="Controles del prototipo">
  <span>Prototipo: las piezas, los precios y los textos son de ejemplo. Los dibujos ocupan el lugar de las fotos recortadas reales.</span>
  <label>Ver estado <select id="ver-estado"><option value="lista">Lista</option><option value="cargando">Cargando</option></select></label>
</div>
<main id="contenido" class="ancho">
  <nav class="migas" aria-label="Ruta de navegación"><ol><li><a href="inicio.html">Inicio</a></li><li><span aria-current="page">Jarrones y recipientes</span></li></ol></nav>
  <header class="intro">
    <h1>Jarrones y recipientes</h1>
    <p>Jarrones, floreros y recipientes decorativos de cerámica, porcelana y vidrio, para usar solos o con flores y ramas. En cada pieza encuentra las medidas, el material y el origen. <span class="pendiente">[TEXTO DE EJEMPLO]</span></p>
  </header>

  <div class="barra-lista">
    <button class="boton secundario" type="button" id="abrir-filtros">Filtrar<span id="n-filtros"></span></button>
    <label for="orden">Ordenar</label>
    <select id="orden"><option value="rec">Recomendadas</option><option value="menor">Precio: menor a mayor</option><option value="mayor">Precio: mayor a menor</option></select>
  </div>
  <div class="estado-lista"><p id="cuenta" role="status">8 piezas</p><span id="fichas"></span><div class="vistas" role="group" aria-label="Ver las piezas como"><button type="button" data-vista="estanteria" aria-pressed="true">Estantería</button><button type="button" data-vista="cuadricula" aria-pressed="false">Cuadrícula</button></div></div>

  <h2 class="oculto-visual">Piezas de esta categoría</h2>
  <ul class="rejilla estanteria" id="lista">
''' + tarjetas_cat + '''  </ul>
  <div class="vacio" id="vacio" hidden>
    <h2>Ninguna pieza coincide con esos filtros</h2>
    <p>Quite algún filtro o déjenos orientarle con unas preguntas.</p>
    <button class="boton secundario" type="button" id="borrar-vacio">Borrar los filtros</button>
    <a class="enlace" href="quiz-orientacion.html">Ayúdeme a elegir</a>
  </div>
  <div class="mas" id="mas"><a class="boton secundario" href="?pagina=2" data-proto>Ver más piezas</a></div>

  <div class="texto-cat">
    <section aria-labelledby="t-elegir">
      <h2 id="t-elegir">Cómo elegir un jarrón</h2>
      <p><span class="pendiente">[TEXTO PENDIENTE: lo escribe el agente de contenido]</span> Espacio para dos o tres párrafos que respondan qué tamaño conviene según el espacio y qué material según el uso.</p>
    </section>
    <section aria-labelledby="t-faq">
      <h2 id="t-faq">Preguntas frecuentes</h2>
      <details class="faq"><summary>¿Hacen envíos fuera de Bogotá?</summary><p>Sí. Hacemos envíos a todo el país. El costo y el tiempo se calculan con su ciudad antes de pagar.</p></details>
      <details class="faq"><summary>¿Cómo llegan embalados los jarrones?</summary><p>En caja, con papel de seda y protección. <span class="pendiente">[POR CONFIRMAR]</span></p></details>
      <details class="faq"><summary>¿Sirven para flores naturales con agua?</summary><p><span class="pendiente">[POR CONFIRMAR con el proveedor, por pieza]</span></p></details>
    </section>
  </div>
</main>
''' + FILTROS

JS_CAT = r'''<script>
/* Filtros de la categoría. En producción las tarjetas llegan en el HTML del servidor y la URL refleja los filtros. */
const $ = id => document.getElementById(id);
const lista = $('lista'), tarjetas = [...lista.children], formF = $('form-filtros'), panelF = $('filtros');
const GRUPOS = ['material', 'color', 'tamano', 'ambiente'];
const elegidos = () => Object.fromEntries(GRUPOS.map(g => [g, [...formF.querySelectorAll(`[name=${g}]:checked`)].map(i => i.value)]));
const rango = () => (formF.precio.value || '0-99999999').split('-').map(Number);
const pasa = (t, f, [min, max]) => GRUPOS.every(g => !f[g].length || f[g].includes(t.dataset[g])) && +t.dataset.precio >= min && +t.dataset.precio <= max;
const cuantas = () => { const f = elegidos(), r = rango(); return tarjetas.filter(t => pasa(t, f, r)).length; };
const piezas = n => n === 1 ? '1 pieza' : `${n} piezas`;

function aplicar(anunciarlo) {
  const f = elegidos(), r = rango(); let n = 0;
  tarjetas.forEach(t => { const ok = pasa(t, f, r); t.hidden = !ok; if (ok) n++; });
  const activos = GRUPOS.flatMap(g => f[g].map(v => [g, v])).concat(formF.precio.value ? [['precio', formF.querySelector('[name=precio]:checked').nextElementSibling.textContent]] : []);
  $('cuenta').textContent = piezas(n);
  $('n-filtros').textContent = activos.length ? `(${activos.length})` : '';
  $('fichas').replaceChildren(...activos.map(([g, v]) => {
    const b = document.createElement('button'); b.type = 'button'; b.className = 'ficha-filtro'; b.dataset.grupo = g; b.dataset.valor = v;
    b.setAttribute('aria-label', `Quitar el filtro ${v}`);
    b.innerHTML = '<span></span><svg class="icono" viewBox="0 0 24 24" aria-hidden="true"><path d="m7 7 10 10M17 7 7 17"/></svg>'; b.firstChild.textContent = v; return b;
  }));
  $('vacio').hidden = n > 0; lista.hidden = n === 0; $('mas').hidden = n === 0 || activos.length > 0;
  try { const q = new URLSearchParams(activos.map(([g, v]) => [g, v])); history.replaceState(null, '', q.toString() ? '?' + q : location.pathname); } catch (e) {}
  if (anunciarlo) { anunciar(n ? `${piezas(n)} con esos filtros` : 'Ninguna pieza coincide con esos filtros'); track('filtrar', { filtros: activos.length, resultados: n }); }
}
function borrar() { formF.reset(); $('ver-piezas').textContent = `Ver ${piezas(tarjetas.length)}`; aplicar(true); }

$('abrir-filtros').onclick = () => { panelF.showModal(); $('t-filtros').focus(); };
formF.addEventListener('change', () => { const n = cuantas(); $('ver-piezas').textContent = n ? `Ver ${piezas(n)}` : 'Sin piezas con esos filtros'; });
formF.addEventListener('submit', e => { e.preventDefault(); aplicar(true); panelF.close(); });
$('borrar-panel').onclick = borrar; $('borrar-vacio').onclick = () => { borrar(); $('abrir-filtros').focus(); };
$('fichas').addEventListener('click', e => {
  const b = e.target.closest('.ficha-filtro'); if (!b) return;
  if (b.dataset.grupo === 'precio') formF.precio.value = ''; else formF.querySelector(`[name=${b.dataset.grupo}][value="${b.dataset.valor}"]`).checked = false;
  $('ver-piezas').textContent = `Ver ${piezas(cuantas())}`; aplicar(true); $('abrir-filtros').focus();
});
$('orden').addEventListener('change', e => {
  const v = e.target.value, orden = v === 'rec' ? tarjetas : [...tarjetas].sort((a, b) => (a.dataset.precio - b.dataset.precio) * (v === 'menor' ? 1 : -1));
  lista.append(...orden); anunciar(`Orden: ${e.target.selectedOptions[0].textContent}`);
});
document.querySelector('.vistas').addEventListener('click', e => {
  const b = e.target.closest('[data-vista]'); if (!b) return;
  lista.classList.toggle('estanteria', b.dataset.vista === 'estanteria');
  document.querySelectorAll('[data-vista]').forEach(x => x.setAttribute('aria-pressed', x === b));
  anunciar(`Vista de ${b.textContent.toLowerCase()}`); track('cambiar_vista', { vista: b.dataset.vista });
});
$('ver-estado').addEventListener('change', e => {
  const c = e.target.value === 'cargando'; lista.classList.toggle('cargando', c); lista.setAttribute('aria-busy', c);
  $('cuenta').textContent = c ? 'Cargando piezas…' : piezas(tarjetas.filter(t => !t.hidden).length);
});
</script>
'''

io.open(dest + '/categoria.html', 'w', encoding='utf-8', newline='\n').write(pagina(
    'Jarrones y recipientes · Historias que Habitan',
    'Jarrones, floreros y recipientes decorativos de cerámica, porcelana y vidrio. Envíos a todo el país.',
    CSS_CAT, CUERPO_CAT, actual='Jarrones y recipientes', guion=JS_CAT))
print('ok')

# ---------------------------------------------------------------- LÁMPARAS
CSS_LUZ = CSS_CAT + r"""
/* Lámparas: interruptor de apagadas a encendidas y selector de tono.
   En producción cada estado es una foto real con el mismo encuadre; aquí la luz se simula con capas. */
.barra-luz{display:flex;flex-wrap:wrap;align-items:center;gap:var(--s3) var(--s6);padding:var(--s3) 0;margin-top:var(--s5);border-top:1px solid var(--tinta);border-bottom:1px solid var(--perla)}
.interruptor{display:flex;align-items:center;gap:var(--s3)}
.interruptor button{position:relative;width:56px;height:44px;padding:0;background:none;border:0;cursor:pointer}
.interruptor button::before{content:"";position:absolute;left:0;top:7px;width:56px;height:30px;border-radius:15px;border:1.5px solid var(--tinta);background:var(--hueso);transition:background-color 300ms var(--curva)}
.interruptor .perilla{position:absolute;left:5px;top:12px;width:20px;height:20px;border-radius:50%;background:var(--tinta);transition:translate 300ms var(--curva),background-color 300ms var(--curva)}
.interruptor button[aria-checked=true]::before{background:var(--tinta)}
.interruptor button[aria-checked=true] .perilla{translate:26px 0;background:var(--champagne)}
#estado-luz{min-width:9ch;color:var(--cafe-humo)}
.tonos{display:flex;align-items:center;flex-wrap:wrap;gap:var(--s2) var(--s3);border:0;padding:0;margin:0;min-width:0}
.tonos legend{float:left;padding:0;margin-right:var(--s3)}
.tonos div{display:inline-flex;border:1px solid var(--cafe-humo);border-radius:2px;overflow:hidden}
.tonos label{position:relative;cursor:pointer}
.tonos input{position:absolute;inset:0;opacity:0;margin:0;cursor:pointer}
.tonos span{display:inline-flex;align-items:center;gap:var(--s2);min-height:44px;padding:0 var(--s3);font-size:.9375rem;background:var(--hueso)}
.tonos i{width:12px;height:12px;border-radius:50%;border:1px solid var(--cafe-humo)}
.tonos input:checked+span{background:var(--tinta);color:var(--hueso)}
.tonos input:focus-visible+span{outline:2px solid var(--tinta);outline-offset:-4px}
.tonos input:checked:focus-visible+span{outline-color:var(--hueso)}
.luces{--tono:#FFB259;--nucleo:#FFE9C6}
.luces[data-tono=neutra]{--tono:#FFE2B0;--nucleo:#FFF7E8}
.luces[data-tono=fria]{--tono:#C9DEFF;--nucleo:#F3F8FF}
.luces li[data-tonos="1"]{--tono:#FFB259;--nucleo:#FFE9C6}
.escena{position:relative;aspect-ratio:4/5;background:#DAD3C9;overflow:hidden;margin-bottom:var(--s2)}
.escena::before,.escena .halo{content:"";position:absolute;inset:0;opacity:0;transition:opacity 350ms var(--curva)}
.escena::before{background:#2A1D16}
.escena .halo{background:radial-gradient(circle at var(--lx,50%) var(--ly,45%),color-mix(in srgb,var(--tono) 92%,transparent) 0,color-mix(in srgb,var(--tono) 40%,transparent) 26%,transparent 64%),radial-gradient(circle at var(--lx,50%) var(--ly,45%),transparent 0,transparent 100%);transition:opacity 350ms var(--curva),background 500ms var(--curva)}
.escena svg{position:absolute;inset:0;width:100%;height:100%}
.escena .pantalla{fill:#EDE7DE;stroke:#B9AFA3;stroke-width:1;transition:fill 350ms var(--curva),filter 350ms var(--curva),stroke 350ms var(--curva)}
.escena .metal{fill:#3B2A20}.escena .trazo{fill:none;stroke:#3B2A20;stroke-width:3;stroke-linecap:round}
.escena .ceramica{fill:#F1EEE8;stroke:#B9AFA3}.escena .mesa{fill:#C9BFB2}
:is(.luces[data-luz=on] li[data-tonos="3"],.luces[data-luz=on][data-tono=calida] li[data-tonos="1"]) .escena::before{opacity:.5;transition-duration:700ms}
:is(.luces[data-luz=on] li[data-tonos="3"],.luces[data-luz=on][data-tono=calida] li[data-tonos="1"]) .halo{opacity:1;transition-duration:700ms,500ms}
:is(.luces[data-luz=on] li[data-tonos="3"],.luces[data-luz=on][data-tono=calida] li[data-tonos="1"]) .pantalla{fill:var(--nucleo);stroke:var(--tono);filter:drop-shadow(0 0 9px var(--tono));transition-duration:700ms}
.luces .tarjeta h3{font-size:1.25rem;line-height:1.2}
.luz-nota.apagada{border-style:dashed;color:var(--cafe-humo)}
.luz-nota{display:inline-block;margin-top:var(--s1);font-size:.8125rem;border:1px solid var(--cafe-humo);border-radius:999px;padding:1px var(--s2)}
@media (prefers-reduced-motion:reduce){.escena::before,.escena .halo,.escena .pantalla{transition:none!important}}
"""

MESA = '<rect class="mesa" x="0" y="232" width="200" height="18"/>'
LAMPARAS = [
    ('[Lámpara de mesa con base de cerámica]', '$249.900', 3, 50, 40, MESA
     + '<path class="ceramica" d="M92 232 H108 L112 224 Q124 200 116 176 Q110 160 104 150 H96 Q90 160 84 176 Q76 200 88 224 Z"/>'
       '<rect class="metal" x="98" y="126" width="4" height="26"/><path class="pantalla" d="M68 128 L84 68 H116 L132 128 Z"/>'),
    ('[Colgante de vidrio en globo]', '$189.900', 1, 50, 60,
     '<path class="trazo" d="M100 0 V118" stroke-width="2"/><rect class="metal" x="93" y="116" width="14" height="10" rx="2"/><circle class="pantalla" cx="100" cy="152" r="27"/>'),
    ('[Aplique doble de pared]', '$159.900', 3, 50, 50,
     '<rect class="pantalla" x="86" y="68" width="28" height="40" rx="7"/><rect class="pantalla" x="86" y="144" width="28" height="40" rx="7"/><rect class="metal" x="91" y="102" width="18" height="48" rx="4"/>'),
    ('[Lámpara de mesa tipo hongo]', '$219.900', 3, 50, 40, MESA
     + '<path class="metal" d="M76 232 H124 L118 222 H82 Z"/><rect class="metal" x="96" y="118" width="8" height="106"/><path class="pantalla" d="M58 122 Q58 70 100 70 Q142 70 142 122 Z"/>'),
    ('[Colgante de tres globos]', '$389.900', 1, 50, 54,
     '<path class="trazo" d="M100 0 V94" stroke-width="2"/><path class="trazo" d="M58 122 Q58 94 100 94 Q142 94 142 122"/>'
     '<circle class="pantalla" cx="58" cy="136" r="15"/><circle class="pantalla" cx="100" cy="136" r="15"/><circle class="pantalla" cx="142" cy="136" r="15"/>'),
    ('[Farol de mesa]', '$129.900', 1, 50, 64, MESA
     + '<path class="trazo" d="M84 112 Q100 84 116 112"/><rect class="pantalla" x="82" y="120" width="36" height="100" rx="2"/>'
       '<path class="trazo" d="M78 114 H122 V228 H78 Z M100 114 V228" stroke-width="2.5"/>'),
]


def lampara(nombre, precio, tonos, lx, ly, dibujo):
    nota = '3 tonos de luz' if tonos == 3 else 'Solo luz cálida'
    return ('    <li class="tarjeta" data-tonos="%d"><a href="/decoracion/lamparas/ejemplo" data-proto>'
            '<div class="escena" style="--lx:%d%%;--ly:%d%%"><span class="halo"></span>'
            '<svg viewBox="0 0 200 250" aria-hidden="true" focusable="false">%s</svg></div>'
            '<h3>%s</h3><p class="meta">[Material] · [Origen]</p><p class="precio"><strong>%s</strong></p>'
            '<span class="luz-nota">%s</span></a></li>\n' % (tonos, lx, ly, dibujo, nombre, precio, nota))


CUERPO_LUZ = ("""<div class="proto" role="region" aria-label="Controles del prototipo">
  <span>Prototipo: las lámparas son dibujos y la luz está simulada. En producción cada estado es una foto real de la misma lámpara, con el mismo encuadre: apagada y encendida en cada tono.</span>
</div>
<main id="contenido" class="ancho">
  <nav class="migas" aria-label="Ruta de navegación"><ol><li><a href="inicio.html">Inicio</a></li><li><a href="/decoracion" data-proto>Decoraciones del hogar</a></li><li><span aria-current="page">Lámparas</span></li></ol></nav>
  <header class="intro">
    <h1>Lámparas</h1>
    <p>Lámparas de mesa, colgantes y apliques. Enciéndalas para ver cómo iluminan; algunas cambian entre luz cálida, neutra y fría. <span class="pendiente">[TEXTO DE EJEMPLO]</span> <span class="pendiente">[POR CONFIRMAR: si es categoría propia]</span></p>
  </header>

  <div class="barra-luz">
    <div class="interruptor"><span id="et-luz">Luz</span>
      <button type="button" role="switch" aria-checked="false" aria-labelledby="et-luz" id="luz"><span class="perilla"></span></button>
      <span id="estado-luz" aria-hidden="true">Apagadas</span></div>
    <fieldset class="tonos"><legend>Tono</legend><div>
      <label><input type="radio" name="tono" value="calida" checked><span><i style="background:#FFB259"></i>Cálida</span></label>
      <label><input type="radio" name="tono" value="neutra"><span><i style="background:#FFE2B0"></i>Neutra</span></label>
      <label><input type="radio" name="tono" value="fria"><span><i style="background:#C9DEFF"></i>Fría</span></label>
    </div></fieldset>
  </div>
  <div class="estado-lista"><p id="cuenta">6 lámparas</p><p style="color:var(--cafe-humo);font-size:.875rem;margin:0" id="nota-tonos">Las lámparas que no vienen en el tono elegido se apagan.</p></div>

  <h2 class="oculto-visual">Lámparas de esta sección</h2>
  <ul class="rejilla luces" id="lista" data-luz="off" data-tono="calida">
""" + ''.join(lampara(*l) for l in LAMPARAS) + """  </ul>
</main>
""")

CUERPO_LUZ = CUERPO_LUZ.replace('<a href="/decoracion/lamparas/ejemplo" data-proto>', '<a href="ficha-lampara.html">', 1)

JS_LUZ = r"""<script>
/* Encender y apagar las lámparas y elegir el tono. La que no viene en el tono elegido se apaga y lo dice. */
const lista = document.getElementById('lista'), llave = document.getElementById('luz');
const TONOS = { calida: 'cálida', neutra: 'neutra', fria: 'fría' };
function refrescar(decir = true) {
  const on = lista.dataset.luz === 'on', tono = lista.dataset.tono, total = lista.children.length;
  let encendidas = 0;
  [...lista.children].forEach(li => {
    const prende = on && (li.dataset.tonos === '3' || tono === 'calida'); if (prende) encendidas++;
    const nota = li.querySelector('.luz-nota'); if (li.dataset.tonos !== '1') return;
    const apagada = on && !prende; nota.classList.toggle('apagada', apagada);
    nota.textContent = apagada ? `Apagada: no viene en luz ${TONOS[tono]}` : 'Solo luz cálida';
  });
  llave.setAttribute('aria-checked', on);
  document.getElementById('estado-luz').textContent = on ? 'Encendidas' : 'Apagadas';
  document.getElementById('cuenta').textContent = on ? `${encendidas} de ${total} encendidas` : `${total} lámparas`;
  if (decir) anunciar(on ? `Luz ${TONOS[tono]}: ${encendidas} de ${total} lámparas encendidas` : 'Lámparas apagadas');
  track('luz_lamparas', { encendidas: on, tono });
}
llave.addEventListener('click', () => { lista.dataset.luz = lista.dataset.luz === 'on' ? 'off' : 'on'; refrescar(); });
document.querySelector('.tonos').addEventListener('change', e => { lista.dataset.tono = e.target.value; lista.dataset.luz = 'on'; refrescar(); });
</script>
"""

io.open(dest + '/lamparas.html', 'w', encoding='utf-8', newline='\n').write(pagina(
    'Lámparas · Historias que Habitan',
    'Lámparas de mesa, colgantes y apliques. Véalas apagadas y encendidas, en luz cálida, neutra o fría.',
    CSS_LUZ, CUERPO_LUZ, actual='Lámparas', guion=JS_LUZ))

EXTRA = []
exec(io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'paginas_extra.py'), encoding='utf-8').read())

# Los estilos y el guion compartidos se incrustan: así cada prototipo abre solo, sin depender de otros archivos.
css = io.open(dest + '/base.css', encoding='utf-8').read()
js = io.open(dest + '/base.js', encoding='utf-8').read()
for nombre in ['inicio.html', 'categoria.html', 'lamparas.html'] + EXTRA:
    h = io.open(dest + '/' + nombre, encoding='utf-8').read()
    a, b = '<link rel="stylesheet" href="base.css">', '<script src="base.js"></script>'
    assert h.count(a) == 1 and h.count(b) == 1
    h = h.replace(a, '<style>\n' + css + '</style>').replace(b, '<script>\n' + js + '</script>')
    io.open(dest + '/' + nombre, 'w', encoding='utf-8', newline='\n').write(h)
print('incrustado')

# El viaje de la pieza entre páginas: la lista debe estar pintada antes de la transición.
CABEZA = """<link rel="expect" blocking="render" href="#%s">
<script>
/* Al volver de la ficha, la pieza regresa a su lugar en la repisa */
addEventListener('pagereveal', e => {
  document.documentElement.dataset.transicion = e.viewTransition ? 'si' : 'no';
  const de = window.navigation && navigation.activation && navigation.activation.from;
  if (!e.viewTransition || !de || !de.url.includes('ficha-producto')) return;
  const arte = document.querySelector('.tarjeta a[href*="ficha-producto"] .arte'); if (!arte) return;
  arte.style.viewTransitionName = 'pieza';
  e.viewTransition.finished.finally(() => arte.style.viewTransitionName = '');
});
</script>
</head>"""
for nombre, lista in (('inicio.html', 'piezas'), ('categoria.html', 'lista')):
    h = io.open(dest + '/' + nombre, encoding='utf-8').read()
    assert h.count('</head>') == 1
    io.open(dest + '/' + nombre, 'w', encoding='utf-8', newline='\n').write(h.replace('</head>', CABEZA % lista))
print('viaje listo')

# Enlaces reales entre las páginas del prototipo
MAPA = [('/colecciones/primer-hogar', 'coleccion-primer-hogar.html'), ('/colecciones/regalos-que-se-guardan', 'coleccion-regalos.html'), ('/porcelanas', 'porcelanas.html'), ('/flores-artificiales', 'flores-artificiales.html'), ('/mesa', 'mesa.html'), ('/centros-de-mesa', 'centros-de-mesa.html'), ('/esculturas', 'esculturas.html'), ('/decoracion', 'decoracion.html'), ('/jarrones', 'categoria.html'), ('/colecciones', 'colecciones.html'), ('/politica-de-datos', 'politica-de-datos.html'), ('/terminos', 'terminos.html'), ('/politica-de-cookies', 'politica-de-cookies.html'), ('/carrito', 'carrito.html'), ('/colecciones/la-mesa-que-recibe', 'coleccion.html'), ('/historias/como-poner-la-mesa-para-recibir', 'historia.html'), ('/historias', 'historias.html'), ('/por-mayor', 'por-mayor.html'), ('/seguimiento', 'seguimiento.html'), ('/pieza-rota', 'pieza-rota.html'), ('/envios', 'envios.html'), ('/cambios-y-garantia', 'cambios-y-garantia.html'), ('/nosotros', 'nosotros.html'), ('/preguntas', 'preguntas.html')]
for nombre in ['inicio.html', 'categoria.html', 'lamparas.html'] + EXTRA:
    h = io.open(dest + '/' + nombre, encoding='utf-8').read()
    for ruta, archivo in MAPA:
        h = h.replace('href="%s" data-proto' % ruta, 'href="%s"' % archivo)
    h = h.replace('href="/carrito" aria-label="Carrito, 0 piezas" data-proto', 'href="carrito.html" aria-label="Carrito, 0 piezas" data-contador')
    io.open(dest + '/' + nombre, 'w', encoding='utf-8', newline='\n').write(h)
print('enlaces listos')

"""Cabecera, menú y pie del sitio, con sus estilos y su comportamiento. Una sola fuente para:
- las páginas que arma construir_paginas.py (cabecera() y PIE),
- la plantilla de la ficha (ficha-producto.html, de la que salen todas las fichas), con sincronizar(),
- el inicio aprobado (inicio-estructura.html), que lo inyecta inicio_secciones.py.

Qué trae la cabecera: Lo nuevo y Descuentos destacados; cuenta (Ingresar o «Hola, [nombre]»); Favoritos, con las piezas
guardadas y los avisos de llegada de las agotadas; carrito. En celular, una fila de atajos con Buscar, Lo nuevo y Descuentos.
El pie trae el formulario del boletín (los mismos campos del modal de bienvenida) y los enlaces en columnas."""
import re

# ---------------------------------------------------------------- Íconos
def icono(trazo, clase='icono'):
    return '<svg class="%s" viewBox="0 0 24 24" aria-hidden="true" focusable="false">%s</svg>' % (clase, trazo)


I_MENU = icono('<path d="M4 7h16M4 12h16M4 17h16"/>')
I_BUSCAR = icono('<circle cx="11" cy="11" r="6.5"/><path d="m16 16 4.5 4.5"/>')
I_CUENTA = icono('<circle cx="12" cy="8.5" r="3.8"/><path d="M4.8 20.2c1.2-3.5 3.9-5.4 7.2-5.4s6 1.9 7.2 5.4"/>')
CORAZON = '<path d="M12 20.3 4.8 13.4a4.7 4.7 0 0 1 0-6.6 4.6 4.6 0 0 1 6.5 0l.7.7.7-.7a4.6 4.6 0 0 1 6.5 0 4.7 4.7 0 0 1 0 6.6Z"/>'
I_CORAZON = icono(CORAZON)
I_BOLSA = icono('<path d="M5 8h14l-1 12H6L5 8Z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>')
I_CERRAR = icono('<path d="m6 6 12 12M18 6 6 18"/>')
I_BUSCAR_CHICO = icono('<circle cx="11" cy="11" r="6.5"/><path d="m16 16 4.5 4.5"/>', 'icono chico')

CATEGORIAS = [('Porcelanas y figuras', 'porcelanas.html'), ('Jarrones y recipientes', 'categoria.html'), ('Flores artificiales', 'flores-artificiales.html'),
              ('Mesa', 'mesa.html'), ('Centros de mesa', 'centros-de-mesa.html'), ('Esculturas pequeñas', 'esculturas.html'),
              ('Decoraciones del hogar', 'decoracion.html')]


def _cur(si):
    return ' aria-current="page"' if si else ''


def cabecera(actual=None):
    """Cabecera + atajos de celular + menú lateral. `actual` es el nombre de la categoría o de la página (Lo nuevo, Descuentos)."""
    cats = ''.join('        <li><a href="%s"%s>%s</a></li>\n' % (u, _cur(n == actual), n) for n, u in CATEGORIAS)
    cats += '        <li><a class="sub" href="lamparas.html"%s>Lámparas</a></li>\n' % _cur(actual == 'Lámparas')
    return '''<a class="salto" href="#contenido">Saltar al contenido</a>
<header class="cabecera">
  <div class="ancho">
    <button class="util solo-movil" type="button" data-abrir-menu aria-label="Abrir el menú">''' + I_MENU + '''<span class="u-txt" aria-hidden="true">Menú</span></button>
    <!-- [LOGO SVG PENDIENTE] -->
    <a class="marca" href="inicio-estructura.html" translate="no">Historias que Habitan</a>
    <nav class="nav-escritorio" aria-label="Principal">
      <button type="button" data-abrir-menu>Tienda</button>
      <a class="nav-nuevo" href="lo-nuevo.html"''' + _cur(actual == 'Lo nuevo') + '''>Lo nuevo</a>
      <a class="nav-desc" href="descuentos.html"''' + _cur(actual == 'Descuentos') + '''>Descuentos</a>
      <a href="colecciones.html">Colecciones</a>
      <a class="nav-opcional" href="historias.html">Historias</a>
      <a href="por-mayor.html">Por mayor</a>
    </nav>
    <div class="utiles">
      <button class="util solo-escritorio" type="button" data-abrir-menu data-buscar aria-label="Buscar en la tienda">''' + I_BUSCAR + '''<span class="u-txt" aria-hidden="true">Buscar</span></button>
      <a class="util" href="cuenta.html" data-cuenta>''' + I_CUENTA + '''<span class="u-txt"><span class="u-corto">Ingresar</span><span class="u-largo">Ingresar</span></span></a>
      <a class="util" href="favoritos.html" data-favoritos aria-label="Favoritos">''' + I_CORAZON + '''<span class="u-txt" aria-hidden="true">Favoritos</span></a>
      <a class="util" href="carrito.html" id="carrito" data-contador data-carrito aria-label="Carrito, 0 piezas">''' + I_BOLSA + '''<span class="u-txt" aria-hidden="true">Carrito</span><span class="contador" id="contador" aria-hidden="true" hidden>0</span></a>
    </div>
  </div>
</header>
<nav class="atajos" aria-label="Atajos de la tienda">
  <div class="ancho">
    <button type="button" class="atajo" data-abrir-menu data-buscar>''' + I_BUSCAR_CHICO + '''Buscar</button>
    <a class="atajo atajo-nuevo" href="lo-nuevo.html"''' + _cur(actual == 'Lo nuevo') + '''>Lo nuevo</a>
    <a class="atajo atajo-desc" href="descuentos.html"''' + _cur(actual == 'Descuentos') + '''>Descuentos</a>
    <a class="atajo" href="tienda.html"''' + _cur(actual == 'Toda la tienda') + '''>Toda la tienda</a>
    <a class="atajo" href="colecciones.html">Colecciones</a>
  </div>
</nav>

<dialog class="panel" id="menu" aria-labelledby="t-menu">
  <div class="panel-cab"><h2 id="t-menu" tabindex="-1">Menú</h2><button class="boton-icono" type="button" data-cerrar aria-label="Cerrar el menú">''' + I_CERRAR + '''</button></div>
  <div class="panel-cuerpo">
    <form class="buscar" role="search">
      <label class="oculto-visual" for="q">Buscar en la tienda</label>
      <input id="q" name="q" type="search" placeholder="Buscar: jarrón, vajilla…" autocomplete="off" enterkeyhint="search">
      <button class="boton secundario" type="submit">Buscar</button>
    </form>
    <div class="menu-destacados">
      <a class="menu-dest nuevo" href="lo-nuevo.html"><b>Lo nuevo</b><span>Las piezas que acaban de llegar</span></a>
      <a class="menu-dest desc" href="descuentos.html"><b>Descuentos</b><span>Con el precio anterior a la vista</span></a>
    </div>
    <nav aria-label="Menú de la tienda">
      <p class="menu-titulo" id="m-tienda">Tienda</p>
      <ul class="menu-lista grande" aria-labelledby="m-tienda">
        <li><a href="tienda.html"''' + _cur(actual == 'Toda la tienda') + '''>Toda la tienda</a></li>
''' + cats + '''      </ul>
      <p class="menu-titulo" id="m-col">Colecciones</p>
      <ul class="menu-lista" aria-labelledby="m-col">
        <li><a href="coleccion.html">La mesa que recibe</a></li>
        <li><a href="coleccion-primer-hogar.html">Primer hogar</a></li>
        <li><a href="coleccion-regalos.html">Regalos que se guardan</a></li>
      </ul>
      <p class="menu-titulo" id="m-cuenta">Su cuenta</p>
      <ul class="menu-lista" aria-labelledby="m-cuenta">
        <li><a href="cuenta.html" data-cuenta-menu>Ingresar a mi cuenta</a></li>
        <li><a href="favoritos.html">Mis favoritos y avisos de llegada</a></li>
        <li><a href="seguimiento.html">Seguir mi pedido</a></li>
      </ul>
      <ul class="menu-lista">
        <li><a href="historias.html">Historias</a></li>
        <li><a href="quiz-orientacion.html">Orientación: le ayudamos a elegir</a></li>
        <li><a href="por-mayor.html">Por mayor</a></li>
        <li><a href="#" data-wa>Ayuda por WhatsApp</a></li>
      </ul>
    </nav>
  </div>
</dialog>
'''


# ---------------------------------------------------------------- Pie con el boletín
def _col(titulo, enlaces):
    return ('      <div><h2 class="pie-h">%s</h2><ul>%s</ul></div>\n'
            % (titulo, ''.join('<li><a href="%s"%s>%s</a></li>' % (u, ' data-wa' if u == '#wa' else '', t) for t, u in enlaces))).replace('href="#wa"', 'href="#"')


FOOTER = '''<footer class="pie">
  <section class="pie-boletin" aria-labelledby="pie-t">
    <div class="ancho">
      <div>
        <h2 class="pie-titulo" id="pie-t">Nuevas piezas y nuevas ofertas</h2>
        <p class="pie-linea"><strong>Suscríbase y entérese de todo.</strong> Le avisamos sobre ofertas exclusivas y nuestros nuevos productos.</p>
      </div>
      <div>
        <form class="pie-form" novalidate data-boletin>
          <div class="pf-dos">
            <div class="pf-campo"><label for="pf-nombre">Nombre y apellido</label>
              <input id="pf-nombre" name="nombre" type="text" autocomplete="name" aria-describedby="pf-e-nombre"><div id="pf-e-nombre" role="alert"></div></div>
            <div class="pf-campo"><label for="pf-correo">Correo electrónico</label>
              <input id="pf-correo" name="correo" type="email" autocomplete="email" inputmode="email" spellcheck="false" autocapitalize="off" aria-describedby="pf-e-correo"><div id="pf-e-correo" role="alert"></div></div>
          </div>
          <div class="pf-dos">
            <div class="pf-campo"><label for="pf-celular">Celular</label>
              <input id="pf-celular" name="celular" type="tel" autocomplete="tel-national" inputmode="tel" aria-describedby="pf-a-celular pf-e-celular"><span class="pf-ayuda" id="pf-a-celular">Diez dígitos. Por ahí le avisamos por WhatsApp.</span><div id="pf-e-celular" role="alert"></div></div>
            <div class="pf-campo"><label for="pf-empresa">Empresa <small>(opcional)</small></label>
              <input id="pf-empresa" name="empresa" type="text" autocomplete="organization" aria-describedby="pf-a-empresa"><span class="pf-ayuda" id="pf-a-empresa">Si compra para un negocio, le contamos también sobre los precios al por mayor.</span></div>
          </div>
          <label class="pf-casilla"><input type="checkbox" id="pf-datos" name="datos" aria-describedby="pf-e-datos"><span>Autorizo el tratamiento de mis datos para recibir novedades y ofertas por correo y WhatsApp, según la <a href="politica-de-datos.html">política de privacidad</a>.</span></label>
          <div id="pf-e-datos" role="alert"></div>
          <button type="submit" class="pf-boton">Sí, quiero suscribirme</button>
          <p class="pf-chica">Puede darse de baja cuando quiera, desde cualquier correo.</p>
        </form>
        <div class="pf-ok" tabindex="-1" hidden><p class="pf-ok-t">Listo, le avisaremos</p><p class="pf-ok-d"></p></div>
      </div>
    </div>
  </section>
  <div class="ancho">
    <div class="pie-cols">
''' + _col('Tienda', [('Toda la tienda', 'tienda.html'), ('Lo nuevo', 'lo-nuevo.html'), ('Descuentos', 'descuentos.html'), ('Colecciones', 'colecciones.html'), ('Lámparas', 'lamparas.html'), ('Por mayor', 'por-mayor.html')]) \
  + _col('Ayuda', [('Envíos', 'envios.html'), ('Cambios y garantía', 'cambios-y-garantia.html'), ('Reportar una pieza rota', 'pieza-rota.html'), ('Seguir mi pedido', 'seguimiento.html'), ('Preguntas frecuentes', 'preguntas.html'), ('Ayuda por WhatsApp', '#wa')]) \
  + _col('Su cuenta', [('Mi cuenta', 'cuenta.html'), ('Mis favoritos', 'favoritos.html'), ('Avisos de llegada', 'favoritos.html#avisos')]) \
  + _col('La marca', [('Nosotros', 'nosotros.html'), ('Historias', 'historias.html'), ('Términos y condiciones', 'terminos.html'), ('Tratamiento de datos', 'politica-de-datos.html'), ('Política de cookies', 'politica-de-cookies.html')]) + '''    </div>
    <div class="pie-legal">
      <p>Historias que Habitan · Decoración y objetos para el hogar · Bogotá, con envíos a todo Colombia · <span class="pendiente">[POR CONFIRMAR: razón social, NIT y correo]</span></p>
      <p>Superintendencia de Industria y Comercio: <a href="https://www.sic.gov.co" rel="noopener">www.sic.gov.co</a></p>
    </div>
  </div>
</footer>
'''

# Aviso de cookies, WhatsApp flotante y avisos para lectores de pantalla: van con el pie en todas las páginas
I_WA = ('<svg class="icono" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.5a8.5 8.5 0 0 0-7.3 12.85L3.5 20.5l4.3-1.1A8.5 8.5 0 1 0 12 3.5Z"/>'
        '<path d="M9.2 8.6c-.3 2.9 2.3 5.8 5.3 6.2l1-1.3-1.7-1-.7.7c-.9-.4-1.7-1.2-2.1-2.1l.7-.7-1-1.7z"/></svg>')
EXTRAS = '''<div class="cookies" id="cookies" role="region" aria-label="Aviso de cookies" hidden>
  <p>Usamos cookies necesarias para que la tienda funcione y, si usted acepta, otras para medir las visitas. <a href="politica-de-cookies.html">Política de cookies</a> <span class="pendiente">[POR CONFIRMAR: texto legal]</span></p>
  <div><button class="boton secundario" type="button" data-cookies="necesarias">Solo las necesarias</button><button class="boton secundario" type="button" data-cookies="todas">Aceptar todas</button></div>
</div>
<a class="wa-flotante" href="#" data-wa aria-label="Ayuda por WhatsApp">''' + I_WA + '''</a>
<p id="aviso-proto" hidden style="position:fixed;left:16px;right:88px;bottom:16px;z-index:30;max-width:420px;background:var(--tinta);color:var(--hueso);padding:12px 16px;border-radius:6px;font-size:.9375rem">Prototipo: esta página todavía no existe.</p>
<p class="oculto-visual" id="anuncio" aria-live="polite"></p>
'''

# ---------------------------------------------------------------- Estilos nuevos (van después de los de base.css)
SITIO_CSS = r'''/* ===== Sitio: cabecera, atajos, menú, favoritos y pie con boletín (herramientas/sitio.py) ===== */
[hidden]{display:none!important}
/* El menú cerrado no se ve nunca, aunque la página use otra clase .panel (la galería del inicio la usa) */
dialog.panel:not([open]){display:none!important}
#menu:modal{position:fixed;flex:none}
.cabecera .ancho{display:flex;align-items:center;gap:0;min-height:64px}
.marca{margin-right:auto;max-width:10em;line-height:1.3;padding:0 var(--s2)}
.utiles{display:flex;align-items:center}
.util{position:relative;display:inline-flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;min-width:52px;min-height:56px;padding:4px 2px;background:none;border:0;border-radius:4px;color:var(--tinta);font:500 .75rem/1.15 var(--texto);text-decoration:none;cursor:pointer}
.util:hover{background:var(--suave)}
.util .icono{width:24px;height:24px}
.util .contador{top:2px;right:calc(50% - 24px)}
.util.con-sesion .icono{color:var(--borgona)}
.u-largo{display:none}
.solo-escritorio{display:none!important}
.icono.chico{width:18px;height:18px}
/* Atajos de celular y tableta: Buscar, Lo nuevo y Descuentos siempre a la vista, con texto */
.atajos{background:var(--hueso);border-bottom:1px solid var(--perla)}
.atajos .ancho{display:flex;gap:var(--s2);overflow-x:auto;padding-top:var(--s2);padding-bottom:var(--s2);scrollbar-width:none;overscroll-behavior-x:contain}
.atajos .ancho::-webkit-scrollbar{display:none}
.atajo{flex:none;display:inline-flex;align-items:center;gap:6px;min-height:44px;padding:0 var(--s4);border:1px solid var(--perla);border-radius:999px;background:#fff;color:var(--tinta);font:500 .9375rem/1 var(--texto);text-decoration:none;white-space:nowrap;cursor:pointer}
.atajo:hover{background:var(--suave)}
.atajo[aria-current]{border-color:var(--tinta);box-shadow:inset 0 0 0 1px var(--tinta)}
.atajo-nuevo::before{content:"";flex:none;width:8px;height:8px;border-radius:50%;background:#B7872F}
.atajo-desc{background:#F6E9EA;color:var(--borgona);border-color:#E3C3C7}
.atajo-desc:hover{background:#F0DCDE}
/* Menú: Lo nuevo y Descuentos como dos tarjetas arriba */
.menu-destacados{display:grid;grid-template-columns:1fr 1fr;gap:var(--s2);margin:0 0 var(--s5)}
.menu-dest{display:flex;flex-direction:column;gap:4px;min-height:92px;padding:var(--s3);border-radius:6px;background:var(--suave);color:var(--tinta);text-decoration:none}
.menu-dest b{font:600 1.375rem/1.15 var(--titulo)}
.menu-dest span{font-size:.875rem;line-height:1.35;color:var(--cafe-humo)}
.menu-dest.nuevo b::after{content:"";display:inline-block;width:8px;height:8px;margin-left:6px;border-radius:50%;background:#B7872F;vertical-align:middle}
.menu-dest.desc{background:#F6E9EA}
.menu-dest.desc b{color:var(--borgona)}
.menu-lista a.sub{padding-left:var(--s4);font:400 1rem/1.5 var(--texto)}
/* Favoritos: el corazón sobre la foto de cada pieza */
.tarjeta{position:relative}
.fav{position:absolute;top:var(--s2);right:var(--s2);z-index:3;width:44px;height:44px;display:grid;place-items:center;padding:0;border:0;border-radius:50%;background:rgba(251,250,249,.94);color:var(--tinta);box-shadow:0 1px 4px rgba(49,38,32,.14);cursor:pointer}
.fav:hover{background:#fff}
.fav svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linejoin:round}
.fav[aria-pressed=true]{color:var(--borgona)}
.fav[aria-pressed=true] svg{fill:currentColor}
.tarjeta:has(.fav) .chips{top:60px}
/* En la ficha: botón con texto, grande y con borde */
.fav-ficha{display:inline-flex;align-items:center;justify-content:center;gap:var(--s2);width:100%;min-height:52px;margin-top:var(--s3);padding:0 var(--s5);border:2px solid var(--tinta);border-radius:2px;background:transparent;color:var(--tinta);font:500 1rem/1.2 var(--texto);cursor:pointer}
.fav-ficha:hover{background:var(--suave)}
.fav-ficha svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linejoin:round}
.fav-ficha[aria-pressed=true]{border-color:var(--borgona);color:var(--borgona)}
.fav-ficha[aria-pressed=true] svg{fill:currentColor}
@media (prefers-reduced-motion:no-preference){
  .fav[aria-pressed=true] svg,.fav-ficha[aria-pressed=true] svg{animation:latido 320ms var(--curva)}
  @keyframes latido{50%{transform:scale(1.2)}}
}
/* Pie con el boletín */
.pie{display:block;margin-top:var(--s8);border-top:0;padding:0 0 calc(var(--s8) + var(--s6));font-size:.9375rem;color:var(--cafe-humo)}
.pie-boletin{background:var(--oatmeal);color:var(--tinta);padding:var(--s7) 0}
.pie-boletin .ancho{display:grid;gap:var(--s5)}
.pie .pie-titulo{font-size:2rem;line-height:1.1}
.pie .pie-linea{margin-top:var(--s2);max-width:44ch;color:var(--mocha)}
.pie .pie-linea strong{color:var(--tinta);font-weight:500}
.pf-dos{display:grid;gap:0 var(--s3)}
@media (min-width:480px){.pf-dos{grid-template-columns:1fr 1fr}}
.pf-campo{margin-bottom:var(--s3)}
.pf-campo label{display:block;margin-bottom:var(--s1);font-weight:500;color:var(--tinta)}
.pf-campo label small{font-weight:400;font-size:.9375rem;color:var(--mocha)}
.pf-campo input{width:100%;min-height:48px;padding:var(--s3) var(--s4);font:inherit;color:var(--tinta);background:#fff;border:1px solid var(--cafe-humo);border-radius:2px}
.pf-campo [aria-invalid=true]{border-color:var(--error);box-shadow:inset 0 0 0 1px var(--error)}
.pf-ayuda{display:block;margin-top:var(--s1);font-size:.9375rem;color:var(--mocha)}
.pf-casilla{display:flex;gap:var(--s3);align-items:flex-start;min-height:44px;padding:var(--s1) 0;color:var(--tinta);cursor:pointer}
.pf-casilla input{flex:none;width:22px;height:22px;margin:1px 0 0;accent-color:var(--tinta)}
.pf-casilla a,.pie .pf-casilla a{display:inline;min-height:0}
.pf-error{display:flex;gap:var(--s2);margin:var(--s1) 0 var(--s2);padding:var(--s2) var(--s3);font-size:.9375rem;color:var(--error);background:var(--error-fondo);border-radius:2px}
.pf-error::before{content:"!";flex:none;width:18px;height:18px;display:grid;place-content:center;font-weight:500;font-size:.75rem;border:1.5px solid currentColor;border-radius:50%}
.pf-boton{display:inline-flex;align-items:center;justify-content:center;width:100%;min-height:52px;margin-top:var(--s3);padding:0 var(--s6);font:500 .875rem/1.43 var(--texto);letter-spacing:.08em;text-transform:uppercase;border:1px solid var(--tinta);border-radius:2px;background:var(--tinta);color:var(--hueso);cursor:pointer}
.pf-boton:hover{background:#1F1814}
.pie .pf-chica{margin-top:var(--s2);font-size:.9375rem;color:var(--mocha)}
.pf-ok{padding:var(--s5);background:var(--hueso);border-radius:6px;color:var(--tinta)}
.pf-ok:focus{outline:2px solid var(--tinta);outline-offset:3px}
.pie .pf-ok-t{font:600 1.5rem/1.2 var(--titulo)}
.pie .pf-ok-d{margin-top:var(--s2)}
.pie-cols{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s5) var(--s4);padding:var(--s7) 0 var(--s5)}
.pie-h{margin-bottom:var(--s2);font:500 .8125rem/1.3 var(--texto);letter-spacing:.12em;text-transform:uppercase;color:var(--tinta)}
.pie .pie-cols ul{display:block;margin:0;padding:0;list-style:none}
.pie-cols a{display:flex;align-items:center;min-height:44px;color:var(--tinta);text-decoration:none}
.pie-cols a:hover{text-decoration:underline;text-underline-offset:3px}
.pie-legal{padding-top:var(--s4);border-top:1px solid var(--perla)}
.pie-legal p{margin:0 0 var(--s2)}
.pie-legal a{display:inline;min-height:0}
@media (min-width:960px){
  .atajos{display:none}
  .solo-escritorio{display:inline-flex!important}
  .solo-movil{display:none!important}
  .cabecera .ancho{min-height:72px}
  .marca{max-width:none;margin-right:var(--s5)}
  .u-corto{display:none}.u-largo{display:inline}
  .nav-escritorio{display:flex;align-items:center;gap:var(--s4);margin-right:auto}
  .nav-escritorio a,.nav-escritorio button{display:inline-flex;align-items:center;gap:6px;min-height:44px;padding:0;font:inherit;color:inherit;background:none;border:0;text-decoration:none;cursor:pointer}
  .nav-escritorio a:hover,.nav-escritorio button:hover{text-decoration:underline;text-underline-offset:4px}
  .nav-escritorio a[aria-current]{text-decoration:underline;text-underline-offset:6px;text-decoration-thickness:2px}
  .nav-escritorio .nav-nuevo::after{content:"";align-self:flex-start;width:7px;height:7px;margin-top:10px;border-radius:50%;background:#B7872F}
  .nav-escritorio .nav-desc{min-height:38px;padding:0 var(--s4);border:1px solid #E3C3C7;border-radius:999px;background:#F6E9EA;color:var(--borgona);font-weight:500}
  .nav-escritorio .nav-desc:hover{background:#F0DCDE;text-decoration:none}
  .util{min-width:66px}
  .pie-boletin .ancho{grid-template-columns:minmax(0,5fr) minmax(0,7fr);align-items:start;gap:var(--s7)}
  .pf-boton{width:auto}
  .pie-cols{grid-template-columns:repeat(4,minmax(0,1fr))}
}
@media (min-width:960px) and (max-width:1199px){
  .nav-escritorio .nav-opcional{display:none}
  .nav-escritorio{gap:var(--s3)}
  .util .u-txt{display:none}
  .util{min-width:48px;min-height:48px}
  .util .contador{right:2px}
}
@media (max-width:359px){.util .u-txt{display:none}.util{min-width:44px}}
'''

# ---------------------------------------------------------------- Comportamiento compartido
SITIO_JS = r'''/* Sitio: cuenta, carrito, favoritos, avisos de llegada y boletín del pie (herramientas/sitio.py) */
(() => {
  const leer = (k, d) => { try { const v = JSON.parse(localStorage.getItem(k)); return v == null ? d : v; } catch (e) { return d; } };
  const guardar = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} };
  const decir = t => { if (window.anunciar) window.anunciar(t); };
  const evento = (e, x) => (window.dataLayer = window.dataLayer || []).push({ event: e, ...x });
  const archivo = () => location.pathname.split('/').pop() || 'inicio-estructura.html';

  /* Cuenta: con sesión saluda por el nombre; sin sesión invita a ingresar. Se repinta al ingresar o salir */
  function pintarCuenta() {
    const ses = leer('hqh-sesion', null), nombre = ses ? (ses.nombre || '').trim().split(' ')[0] : '';
    document.querySelectorAll('[data-cuenta]').forEach(a => {
      a.classList.toggle('con-sesion', !!ses);
      a.querySelector('.u-corto').textContent = ses ? 'Mi cuenta' : 'Ingresar';
      a.querySelector('.u-largo').textContent = ses ? (nombre ? 'Hola, ' + nombre : 'Mi cuenta') : 'Ingresar';
    });
    document.querySelectorAll('[data-cuenta-menu]').forEach(a => { a.textContent = ses ? (nombre ? `Mi cuenta (${nombre})` : 'Mi cuenta') : 'Ingresar a mi cuenta'; });
  }
  pintarCuenta();

  /* Buscar: abre el menú con el buscador listo para escribir */
  document.addEventListener('click', e => { if (e.target.closest('[data-buscar]')) setTimeout(() => document.getElementById('q')?.focus(), 60); });

  /* Carrito: el número de piezas guardadas, en la cabecera de todas las páginas */
  function pintarCarrito() {
    const n = leer('hqh-carrito', []).reduce((t, x) => t + (x.cantidad || 0), 0);
    document.querySelectorAll('[data-contador]').forEach(a => {
      a.setAttribute('aria-label', `Carrito, ${n} ${n === 1 ? 'pieza' : 'piezas'}`);
      let c = a.querySelector('.contador');
      if (!c) { c = document.createElement('span'); c.className = 'contador'; c.setAttribute('aria-hidden', 'true'); a.append(c); }
      c.hidden = !n; c.textContent = n;
    });
  }

  /* Favoritos y avisos de llegada: el corazón guarda la pieza; las agotadas con aviso también cuentan como guardadas */
  const FAV = 'hqh-favoritos';
  const favs = () => leer(FAV, []), avisos = () => leer('hqh-avisos', []);
  const urlDe = b => (b.dataset.fav === 'auto' ? archivo() : b.dataset.fav);
  const nombreDe = b => (b.dataset.nombre || document.querySelector('h1')?.textContent.trim() || 'La pieza').replace(/^\[|\]$/g, '');   // sin los corchetes de los nombres de ejemplo
  function pintarFavoritos() {
    const urls = favs().map(x => x.url);
    document.querySelectorAll('[data-fav]').forEach(b => {
      const on = urls.includes(urlDe(b)), nombre = nombreDe(b), txt = b.querySelector('.fav-txt');
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
      if (txt) txt.textContent = on ? 'Guardada en favoritos' : 'Guardar en favoritos';
      else b.setAttribute('aria-label', `Guardar ${nombre} en favoritos`);
    });
    const n = favs().length + avisos().length;
    document.querySelectorAll('[data-favoritos]').forEach(a => {
      a.setAttribute('aria-label', n ? `Favoritos, ${n} ${n === 1 ? 'guardada' : 'guardadas'}` : 'Favoritos');
      let c = a.querySelector('.contador');
      if (!c) { c = document.createElement('span'); c.className = 'contador'; c.setAttribute('aria-hidden', 'true'); a.append(c); }
      c.hidden = !n; c.textContent = n;
    });
    document.dispatchEvent(new CustomEvent('hqh:favoritos'));
  }
  document.addEventListener('click', e => {
    const b = e.target.closest('[data-fav]'); if (!b) return;
    e.preventDefault(); e.stopPropagation();
    const url = urlDe(b), nombre = nombreDe(b), ya = favs().some(x => x.url === url);
    guardar(FAV, ya ? favs().filter(x => x.url !== url) : favs().concat({ url, nombre, fecha: Date.now() }));
    pintarFavoritos();
    decir(ya ? `${nombre} salió de sus favoritos.` : `${nombre} quedó guardada en sus favoritos.`);
    evento(ya ? 'favorito_quitar' : 'favorito_agregar', { pieza: nombre });
  });
  window.hqhSitio = { favs, avisos, guardarAvisos: v => guardar('hqh-avisos', v), pintarFavoritos, pintarCarrito, pintarCuenta };
  document.addEventListener('hqh:carrito', pintarCarrito);
  document.addEventListener('hqh:sesion', pintarCuenta);
  addEventListener('storage', e => { if (e.key === 'hqh-carrito') pintarCarrito(); if (e.key === FAV || e.key === 'hqh-avisos') pintarFavoritos(); if (e.key === 'hqh-sesion') pintarCuenta(); });
  pintarCarrito(); pintarFavoritos();

  /* Boletín del pie: los mismos campos y reglas del modal de bienvenida. Quien ya se suscribió ve el agradecimiento */
  const f = document.querySelector('form[data-boletin]');
  if (!f) return;
  const ok = f.parentElement.querySelector('.pf-ok');
  if ((leer('hqh-bienvenida', null) || {}).suscrito) {
    f.hidden = true; ok.hidden = false; ok.querySelector('.pf-ok-t').textContent = 'Ya está suscrito';
    ok.querySelector('.pf-ok-d').textContent = 'Le avisamos sobre ofertas exclusivas y nuestros nuevos productos. Gracias.';
  }
  const $ = id => document.getElementById(id);
  function marcar(id, m) {
    const caja = $('pf-e-' + id), campo = $('pf-' + id);
    caja.replaceChildren();
    if (m) { const p = document.createElement('p'); p.className = 'pf-error'; p.textContent = m; caja.append(p); }
    if (campo.type !== 'checkbox') campo.setAttribute('aria-invalid', m ? 'true' : 'false');
  }
  f.addEventListener('change', e => { if (e.target.id === 'pf-datos' && e.target.checked) marcar('datos', ''); });
  f.addEventListener('submit', e => {
    e.preventDefault();
    const el = f.elements, correo = el.correo.value.trim(), cel = el.celular.value.replace(/\D/g, '').replace(/^57(?=3\d{9}$)/, '');
    const fallas = [
      ['nombre', el.nombre.value.trim().includes(' ') ? '' : 'Escriba su nombre y su apellido.'],
      ['correo', !correo ? 'Escriba su correo para avisarle.' : /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(correo) ? '' : 'Revise el correo: le falta la @ o el dominio.'],
      ['celular', !cel ? 'Escriba su celular: diez dígitos que empiecen por 3.' : /^3\d{9}$/.test(cel) ? '' : 'Escriba un celular de diez dígitos que empiece por 3. Ejemplo: 300 123 4567.'],
      ['datos', el.datos.checked ? '' : 'Para avisarle, autorice el tratamiento de sus datos.'],
    ];
    fallas.forEach(([id, m]) => marcar(id, m));
    const primera = fallas.find(([, m]) => m);
    if (primera) return $('pf-' + primera[0]).focus();
    guardar('hqh-bienvenida', { suscrito: true, fecha: Date.now() });   // [PROTOTIPO] en producción lo guarda la plataforma; el modal ya no aparece
    evento('suscripcion_boletin', { lugar: 'pie', negocio: !!el.empresa.value.trim() });
    f.hidden = true; ok.hidden = false;
    ok.querySelector('.pf-ok-d').textContent = `Le escribiremos a ${correo} y por WhatsApp al ${cel.replace(/(\d{3})(\d{3})(\d{4})/, '$1 $2 $3')} cuando lleguen piezas nuevas o haya ofertas.`;
    ok.focus();
  });
})();
'''

# ---------------------------------------------------------------- Para páginas que no traen base.css (el inicio)
PREFIJOS_BASE = ('.icono{', '.oculto-visual{', '.salto', '.cabecera', '.marca{', '.boton-icono', '.nav-escritorio{', 'dialog.panel', '.panel-cab',
                 '.panel-cuerpo', '#menu', '@keyframes de-lado', '.buscar', '.menu-lista', '.menu-titulo', '.contador{', '.cookies', '.pie{', '.pie ',
                 '.wa-flotante', '.boton.secundario')


def css_base(base_css):
    """Las reglas de base.css que necesitan la cabecera, el menú y el pie en una página que no carga base.css."""
    fuera, nivel = [], 0
    for linea in base_css.splitlines():
        if nivel == 0 and linea.startswith('@media'):
            nivel = linea.count('{') - linea.count('}')   # las de una sola línea quedan en 0 y se saltan
            continue
        if nivel > 0:
            nivel += linea.count('{') - linea.count('}')
            continue
        if linea.startswith(PREFIJOS_BASE):
            fuera.append(linea)
    return '/* Reglas de base.css que usan la cabecera, el menú y el pie */\n' + '\n'.join(fuera) + '\n'


# ---------------------------------------------------------------- Sincronizar páginas hechas a mano (plantilla de la ficha)
def _entre(s, ini, fin, desde=0):
    i = s.index(ini, desde)
    j = s.index(fin, i) + len(fin)
    return i, j


def sincronizar(html, actual=None):
    """Cambia la cabecera, el menú y el pie de una página hecha a mano por los del sitio y le agrega estilos y guion."""
    # Cabecera (con su enlace para saltar) y menú lateral
    i = html.index('<header class="cabecera">')
    salto = html.rfind('<a class="salto"', 0, i)
    if salto != -1 and i - salto < 200:
        i = salto
    _, j = _entre(html, '<dialog class="panel" id="menu"', '</dialog>')
    html = html[:i] + cabecera(actual).rstrip('\n') + html[j:]
    # Pie
    i, j = _entre(html, '<footer class="pie">', '</footer>')
    html = html[:i] + FOOTER.rstrip('\n') + html[j:]
    # Estilos y guion, entre marcadores (se reemplazan en cada pasada)
    css = '/* sitio:ini */\n' + SITIO_CSS + '/* sitio:fin */\n'
    if '/* sitio:ini */' in html:
        i, j = _entre(html, '/* sitio:ini */', '/* sitio:fin */\n')
        html = html[:i] + css + html[j:]
    else:
        k = html.index('</style>')
        html = html[:k] + css + html[k:]
    js = '<!-- sitio-js:ini -->\n<script>\n' + SITIO_JS + '</script>\n<!-- sitio-js:fin -->\n'
    if '<!-- sitio-js:ini -->' in html:
        i, j = _entre(html, '<!-- sitio-js:ini -->', '<!-- sitio-js:fin -->\n')
        html = html[:i] + js + html[j:]
    else:
        k = html.rindex('</body>')
        html = html[:k] + js + html[k:]
    return html

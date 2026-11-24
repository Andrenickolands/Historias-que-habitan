"""Secciones 1, 4 y 6 del wireframe del inicio (prototipos/inicio-estructura.html).
1: hero con la lámpara que se arma por capas al bajar y se enciende (como el video de referencia), sin JavaScript.
4: «¿Qué lo trae hoy?» con tarjetas en arco y la pieza saliendo del arco (diseño de team-showcase, adaptado).
6: categorías por tipo en tarjetas con flechas, como en el video.
Uso: python herramientas/inicio_secciones.py prototipos
Cada bloque se reemplaza entre sus marcadores; la primera vez usa los comentarios de sección del archivo."""
import io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import arte as _arte
from arte import arte
from catalogo import estado as estado_pieza, texto_pocas, texto_unidades
import sitio as _sitio   # cabecera, menú, pie con boletín y favoritos
_arte._n[0] = 1000  # ids propios: la galería de colecciones, en la misma página, usa pz1, pz2…

ARCHIVO = os.path.join(sys.argv[1], 'inicio-estructura.html')

# ---------- 1 · Hero: la escultura se arma por capas, se posa en su pedestal y gira ----------
ESC = 'M86 286 H114 V272 Q144 252 136 204 Q130 164 100 140 Q74 164 66 202 Q58 248 86 272 Z'
# Degradados y recorte compartidos por todas las capas (un solo SVG oculto; no display:none para que funcionen en todos los navegadores)
DEFS = ('<svg class="defs-3d" width="0" height="0" aria-hidden="true" focusable="false"><defs>'
        '<linearGradient id="esc-c" x1="0" x2="1"><stop offset="0" stop-color="#B9B2A8"/><stop offset=".22" stop-color="#E9E5DF"/>'
        '<stop offset=".42" stop-color="#FBFAF8"/><stop offset=".7" stop-color="#E6E1DA"/><stop offset="1" stop-color="#A79F95"/></linearGradient>'
        '<linearGradient id="esc-h" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".85"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
        '<clipPath id="esc-k"><path d="%s"/></clipPath></defs></svg>' % ESC)
CUERPO = '<path d="%s" fill="url(#esc-c)" stroke="#9E968C" stroke-width=".6"/>' % ESC


def capa(clase, i, dx, dy, dz, rx, rz, cuerpo):
    return ('<div class="capa %s" style="--i:%d;--dx:%s;--dy:%s;--dz:%s;--rx:%s;--rz:%s"><svg viewBox="0 0 200 300" aria-hidden="true" focusable="false">%s</svg></div>'
            % (clase, i, dx, dy, dz, rx, rz, cuerpo))


CAPAS = ''.join([
    capa('anillo b1', 4, '-15%', '-20%', '60px', '36deg', '8deg', CUERPO),
    capa('anillo b2', 3, '13%', '-11%', '40px', '30deg', '-7deg', CUERPO),
    capa('anillo b3', 2, '-11%', '-3%', '20px', '24deg', '5deg', CUERPO),
    capa('anillo b4', 1, '9%', '5%', '0px', '18deg', '-4deg', CUERPO),
    capa('anillo b5', 0, '-6%', '12%', '-20px', '12deg', '3deg', CUERPO),
])
# Encima de las capas ya armadas: el brillo que recorre la superficie y el surco que da la vuelta al girar
SOBRE = ('<div class="sobre"><svg viewBox="0 0 200 300" aria-hidden="true" focusable="false"><g clip-path="url(#esc-k)">'
         '<rect class="haz" x="62" y="130" width="30" height="170" fill="url(#esc-h)"/>'
         '<path class="surco" d="M101 146 Q 86 196 98 236 Q 104 258 100 272" fill="none" stroke="#B5ADA2" stroke-width="2.4" stroke-linecap="round"/>'
         '</g></svg></div>')

AMBIENTE = ('<svg viewBox="0 0 600 600" preserveAspectRatio="xMidYMax slice" aria-hidden="true" focusable="false">'
            '<defs><linearGradient id="h3d-p" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4B382B"/><stop offset="1" stop-color="#34251C"/></linearGradient>'
            '<linearGradient id="h3d-v" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F4D9A0" stop-opacity=".3"/><stop offset="1" stop-color="#F4D9A0" stop-opacity="0"/></linearGradient></defs>'
            '<rect width="600" height="600" fill="url(#h3d-p)"/><path d="M36 40 H196 V440 H36 Z" fill="url(#h3d-v)"/>'
            '<path d="M116 40 V440 M36 240 H196" stroke="#FBFAF9" stroke-opacity=".08" stroke-width="3"/>'
            '<rect x="420" y="96" width="112" height="144" fill="#4F3C2F" stroke="#6E5642" stroke-width="6"/>'
            '<path d="M438 214 Q476 148 514 214" fill="none" stroke="#8A7360" stroke-width="2"/></svg>')

HERO_HTML = """  <section class="sec hero-sec" style="border-top:0" aria-labelledby="s1">
    <p class="nota"><b>1</b><span>Atención</span><span>CTA: Ver todas las piezas (tienda)</span><span>Movimiento fuerte, en tres tiempos: se arma por capas, se posa en su pedestal y gira</span><span>0 KB de JavaScript · capas ≈ 6 × 30 KB · giro: 24 fotos ≈ 15 KB c/u, después de cargar</span></p>
    <div class="hero3d">
      <div class="pin">
        <div class="hero">
          <div class="texto">
            <p class="ante">Hay objetos que no solo decoran. Cuentan historias.</p>
            <h1 id="s1">Piezas que se miran desde todos sus lados</h1>
            <p class="sub">Esculturas, porcelanas, jarrones y lámparas para su casa. De cada pieza le contamos material, medidas y origen.</p>
            <div class="ctas"><a class="boton" href="tienda.html">Ver todas las piezas</a><a class="boton sec2" href="quiz-orientacion.html">Ayúdeme a elegir</a></div>
          </div>
          <div class="escenario3d" role="img" aria-label="Escultura curva blanca sobre un pedestal, en una sala con luz de tarde">
            %(defs)s
            <div class="amb">%(ambiente)s</div>
            <div class="halo3d"></div>
            <div class="pedestal"></div>
            <div class="figura3d">
              <div class="sombra"></div>
              <div class="giro">%(capas)s%(sobre)s</div>
            </div>
            <a class="pieza-hero" href="pieza-escultura-curva-blanca.html">Escultura curva blanca · $179.900</a>
            <p class="pista-baje" aria-hidden="true">Baje para verla armarse y girar</p>
            <p class="etq">[En producción: recortes de la escultura real por capas y 24 fotos de ella girando, o un render de su modelo 3D]</p>
          </div>
        </div>
      </div>
    </div>
  </section>
""" % {'defs': DEFS, 'ambiente': AMBIENTE, 'capas': CAPAS, 'sobre': SOBRE}

HERO_CSS = """/* 1 · Hero en tres tiempos, como el video de referencia:
   1) la escultura aparece separada en capas inclinadas y se arma; 2) se posa en su pedestal y aparece la sala;
   3) gira sobre sí misma mientras la luz recorre su superficie.
   Solo transform y opacity. Escritorio: ligado al scroll con la sección fija. Celular: ligado a la entrada de la escena.
   Sin soporte: se arma y da una vuelta sola al cargar, y se detiene. Movimiento reducido: armada, de frente y quieta. */
.hero{background:var(--espresso);color:var(--hueso);display:grid;margin:0 calc(var(--s4) * -1)}
.hero .texto{padding:var(--s6) var(--s4);position:relative;z-index:1}
.hero .ante{color:var(--champagne)}
.hero h1{font-size:clamp(2.5rem,6vw,4.5rem);line-height:1.02;margin-top:var(--s3);max-width:12ch}
.hero .sub{margin-top:var(--s3);color:var(--oatmeal);max-width:42ch}
.hero .ctas{display:flex;flex-wrap:wrap;gap:var(--s3);margin-top:var(--s5)}
.hero .boton{background:var(--hueso);color:var(--tinta);border-color:var(--hueso)}
.hero .boton.sec2{background:transparent;color:var(--hueso)}
.hero :focus-visible{outline-color:var(--champagne)}
.defs-3d{position:absolute;width:0;height:0;overflow:hidden}
.escenario3d{position:relative;overflow:hidden;aspect-ratio:4/5;background:#2C1F18}
.escenario3d .amb,.escenario3d .amb svg{position:absolute;inset:0;width:100%;height:100%;display:block}
.halo3d{position:absolute;left:56%;top:30%;width:110%;aspect-ratio:1;translate:-50% -50%;pointer-events:none;
  background:radial-gradient(circle,rgba(244,217,160,.42) 0,rgba(244,194,122,.18) 26%,transparent 62%)}
.pedestal{position:absolute;left:56%;bottom:0;width:46%;height:13%;translate:-50% 0;background:linear-gradient(90deg,#4E3B2D,#6E5642 45%,#5B4632 80%,#46352A)}
.pedestal::before{content:"";position:absolute;left:0;right:0;top:0;height:14%;background:#8A7360}
.figura3d{position:absolute;left:56%;bottom:10%;height:66%;aspect-ratio:2/3;translate:-50% 0}
.giro{position:absolute;inset:0;perspective:900px}
.sombra{position:absolute;left:22%;right:22%;bottom:1%;height:5%;border-radius:50%;background:radial-gradient(closest-side,rgba(20,14,10,.55),transparent)}
.capa,.sobre{position:absolute;inset:0}
.capa svg,.sobre svg{width:100%;height:100%;display:block;overflow:visible}
.b1{clip-path:inset(46.5% 0 43% 0)} .b2{clip-path:inset(56.5% 0 33% 0)} .b3{clip-path:inset(66.5% 0 23% 0)}
.b4{clip-path:inset(76.5% 0 13.8% 0)} .b5{clip-path:inset(85.8% 0 0 0)}
.pista-baje{display:none;position:absolute;left:0;right:0;bottom:var(--s4);z-index:2;text-align:center;font-size:.8125rem;letter-spacing:.08em;text-transform:uppercase;color:var(--oatmeal)}
.escenario3d .etq{position:absolute;left:var(--s3);right:var(--s3);top:var(--s3);font-size:.75rem;color:var(--piedra)}
/* La pieza de la escena, con su precio: un acceso directo a su ficha que no compite con el botón principal */
.pieza-hero{position:absolute;right:var(--s4);bottom:var(--s4);z-index:3;display:inline-flex;align-items:center;min-height:40px;padding:0 var(--s4);border-radius:999px;background:rgba(31,24,20,.55);border:1px solid rgba(251,250,249,.4);color:var(--hueso);font-size:.8125rem;text-decoration:none;backdrop-filter:blur(4px)}
.pieza-hero:hover{background:rgba(31,24,20,.75)}
@media (min-width:960px){.pista-baje{right:auto;left:var(--s4);text-align:left}}
@keyframes armar{from{transform:translate3d(var(--dx),var(--dy),var(--dz)) rotateX(var(--rx)) rotateZ(var(--rz))}}
@keyframes aparecer{from{opacity:.12}}
@keyframes mostrar{from{opacity:0}}
@keyframes subir{from{opacity:0;transform:translateY(40%)}}
@keyframes girar{25%{transform:scaleX(.62)}50%{transform:scaleX(1)}75%{transform:scaleX(.62)}}
@keyframes barrer{from{transform:translateX(-46px)}49.9%{transform:translateX(112px)}50%{transform:translateX(-46px)}to{transform:translateX(112px)}}
@keyframes rodear{22%{transform:translateX(24px);opacity:.25}25%{opacity:0}75%{transform:translateX(-24px);opacity:0}78%{opacity:.25}}
@keyframes pista{to{opacity:0}}
.haz,.surco{transform-box:view-box}
/* Sin soporte de animaciones ligadas al scroll: se arma, se posa y da una vuelta al cargar; después queda quieta */
.capa{animation:armar 1.2s cubic-bezier(.2,.7,.2,1) calc(.3s + var(--i) * .12s) both}
.pedestal{animation:subir .8s cubic-bezier(.2,.7,.2,1) .15s both}
.escenario3d .amb,.halo3d{animation:aparecer 1s ease 1.4s both}
.sobre{animation:mostrar .3s ease 2s both}
.giro,.sombra{animation:girar 3.2s ease-in-out 2.1s both}
.haz{animation:barrer 3.2s ease-in-out 2.1s both}
.surco{animation:rodear 3.2s ease-in-out 2.1s both}
@supports (animation-timeline:view()){
  @media (prefers-reduced-motion:no-preference){
    /* Celular: avanza mientras la escena entra en pantalla, sin fijar la sección */
    .escenario3d{view-timeline:--e3d block}
    .capa{animation:armar linear both;animation-timeline:--e3d;animation-range:cover calc(6% + var(--i) * 3%) cover calc(30% + var(--i) * 3%)}
    .pedestal{animation:subir linear both;animation-timeline:--e3d;animation-range:cover 4% cover 24%}
    .escenario3d .amb,.halo3d{animation:aparecer linear both;animation-timeline:--e3d;animation-range:cover 34% cover 46%}
    .sobre{animation:mostrar linear both;animation-timeline:--e3d;animation-range:cover 42% cover 46%}
    .giro,.sombra{animation:girar linear both;animation-timeline:--e3d;animation-range:cover 46% cover 78%}
    .haz{animation:barrer linear both;animation-timeline:--e3d;animation-range:cover 46% cover 78%}
    .surco{animation:rodear linear both;animation-timeline:--e3d;animation-range:cover 46% cover 78%}
  }
  @media (min-width:960px) and (prefers-reduced-motion:no-preference){
    /* Escritorio: la sección queda fija mientras se baja 1,4 pantallas; quien baja controla la velocidad y puede devolverse */
    .hero3d{height:240vh;view-timeline:--h3d block}
    .pin{position:sticky;top:0}
    .capa{animation-timeline:--h3d;animation-range:contain calc(var(--i) * 4%) contain calc(24% + var(--i) * 4%)}
    .pedestal{animation-timeline:--h3d;animation-range:contain 0% contain 20%}
    .escenario3d .amb,.halo3d{animation-timeline:--h3d;animation-range:contain 30% contain 50%}
    .sobre{animation-timeline:--h3d;animation-range:contain 44% contain 50%}
    .giro,.sombra,.haz,.surco{animation-timeline:--h3d;animation-range:contain 50% contain 95%}
    .pista-baje{display:block;animation:pista linear both;animation-timeline:--h3d;animation-range:contain 0% contain 8%}
  }
}
@media (prefers-reduced-motion:reduce){.capa,.pedestal,.escenario3d .amb,.halo3d,.sobre,.giro,.sombra,.haz,.surco{animation:none}.surco{opacity:1}}
@media (min-width:960px){
  .hero{grid-template-columns:1fr 1.05fr;height:100vh;min-height:560px;margin:0}
  .hero .texto{padding:var(--s8) var(--s7);align-self:center}
  .escenario3d{aspect-ratio:auto;height:100%}
}

"""

# ---------- 5 · ¿Qué lo trae hoy? Arcos con una foto de fondo en cada uno ----------
def colocar(forma, color, vidrio, cx, base, s):
    """Una pieza de arte.py (200 × 300, de pie en y = 286) con su base en (cx, base) y escala s, dentro de una escena."""
    x, y = cx - 100 * s, base - 286 * s
    return arte(forma, color, vidrio).replace('<svg class="arte"', '<svg x="%.1f" y="%.1f" width="%.1f" height="%.1f"' % (x, y, 200 * s, 300 * s), 1)


def escena(fondo, cuerpo):
    """Escena vertical de 300 × 450 que llena el arco. Lo importante va arriba: abajo va el texto."""
    return ('<svg viewBox="0 0 300 450" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">%s%s</svg>' % (fondo, cuerpo))


def degradado(nombre, a, b):
    return '<defs><linearGradient id="%s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs><rect width="300" height="450" fill="url(#%s)"/>' % (nombre, a, b, nombre)


ESCENAS = {
    # Una sala: ventana con luz, cuadro, sofá y una mesa auxiliar con flores
    'ideas': escena(degradado('fa-1', '#D8CABA', '#B9A48C'),
                    '<rect x="26" y="40" width="112" height="196" fill="#FFF7EA" fill-opacity=".38"/><path d="M82 40 V236 M26 138 H138" stroke="#FFF" stroke-opacity=".5" stroke-width="3"/>'
                    '<rect x="170" y="66" width="92" height="74" fill="#CDBBA5" stroke="#8A7360" stroke-width="4"/><path d="M182 128 Q216 86 250 128" fill="none" stroke="#8A7360" stroke-width="2"/>'
                    '<rect x="0" y="336" width="300" height="114" fill="#7A604B"/>'
                    '<rect x="-10" y="232" width="236" height="70" rx="20" fill="#EDE4D7"/><rect x="-16" y="286" width="250" height="56" rx="16" fill="#E2D6C6"/>'
                    '<ellipse cx="60" cy="262" rx="34" ry="24" fill="#C9B49A"/><ellipse cx="150" cy="262" rx="34" ry="24" fill="#9C8467"/>'
                    '<rect x="238" y="254" width="52" height="8" fill="#6E5642"/><rect x="260" y="262" width="6" height="74" fill="#6E5642"/>'
                    + colocar('flores', '#DDE6E8', True, 264, 254, .62)),
    # Una repisa con varias piezas: quien ya sabe qué busca
    'pieza': escena(degradado('fa-2', '#F1EBE2', '#DED3C4'),
                    '<rect x="0" y="196" width="300" height="9" fill="#C9B49A"/><rect x="0" y="205" width="300" height="6" fill="#000" fill-opacity=".06"/>'
                    '<rect x="0" y="318" width="300" height="9" fill="#C9B49A"/><rect x="0" y="327" width="300" height="6" fill="#000" fill-opacity=".06"/>'
                    + colocar('anfora', '#F1EEE8', False, 66, 196, .56) + colocar('alto', '#D9C7AE', False, 150, 196, .6)
                    + colocar('florero', '#DDE6E8', True, 232, 196, .62)
                    + colocar('figura', '#F4F2EE', False, 74, 318, .48) + colocar('tarro', '#6E7F68', False, 156, 318, .46)
                    + colocar('cuenco', '#D9C7AE', False, 236, 318, .5)),
    # Un regalo: caja abierta con papel de seda y una figura de porcelana
    'regalo': escena(degradado('fa-3', '#7B3A41', '#3E1A1F'),
                     '<radialGradient id="fa-3l" cx="50%" cy="30%" r="60%"><stop offset="0" stop-color="#F4D9A0" stop-opacity=".45"/><stop offset="1" stop-color="#F4D9A0" stop-opacity="0"/></radialGradient>'
                     '<rect width="300" height="450" fill="url(#fa-3l)"/>'
                     '<path d="M70 128 L150 100 L232 130 L150 156 Z" fill="#5E262D"/><path d="M146 100 V156" stroke="#F4D9A0" stroke-width="6"/>'
                     '<path d="M150 106 q-30 -34 6 -32 q16 4 14 28 q2 -24 18 -28 q36 -2 2 32" fill="none" stroke="#F4D9A0" stroke-width="5" stroke-linecap="round"/>'
                     '<path d="M92 198 L130 166 L176 192 L214 164 L232 206 Z" fill="#F7F2EA" fill-opacity=".92"/>'
                     + colocar('figura', '#F4F2EE', False, 154, 214, .5) +
                     '<rect x="80" y="206" width="140" height="104" fill="#F1E7D6"/><rect x="80" y="206" width="140" height="10" fill="#E2D3BB"/>'
                     '<path d="M150 206 V310" stroke="#722F37" stroke-width="12"/>'),
    # Descuentos: piezas sobre una repisa, una con su etiqueta de precio rebajado
    'descuentos': escena(degradado('fa-5', '#EFE5D6', '#D8C7AE'),
                         '<rect x="0" y="262" width="300" height="10" fill="#B89B7C"/><rect x="0" y="272" width="300" height="178" fill="#9C8467"/>'
                         + colocar('cuenco', '#D9C7AE', False, 92, 264, .62) + colocar('esfera', '#F1EEE8', False, 208, 264, .6) +
                         '<path d="M126 196 Q150 150 186 128" fill="none" stroke="#5E4C42" stroke-width="1.5"/>'
                         '<g transform="rotate(-14 214 118)"><path d="M186 100 H244 L256 118 L244 136 H186 Z" fill="#722F37"/><circle cx="194" cy="118" r="4" fill="#EFE5D6"/>'
                         '<text x="222" y="124" text-anchor="middle" font-family="Jost, sans-serif" font-size="16" font-weight="500" fill="#FBFAF9">−20 %</text></g>'),
    # (escena anterior, ya sin uso en el inicio)
    'ayuda': escena(degradado('fa-4', '#EADFCB', '#D3C0A4'),
                    '<radialGradient id="fa-4l" cx="50%" cy="25%" r="55%"><stop offset="0" stop-color="#FFF8EC" stop-opacity=".8"/><stop offset="1" stop-color="#FFF8EC" stop-opacity="0"/></radialGradient>'
                    '<rect width="300" height="450" fill="url(#fa-4l)"/>'
                    '<rect x="0" y="282" width="300" height="10" fill="#9C8467"/><rect x="0" y="292" width="300" height="158" fill="#8A6E55"/>'
                    + colocar('cuenco', '#F1EEE8', False, 66, 284, .5) + colocar('panza', '#B8752A', True, 150, 284, .56)
                    + colocar('escultura', '#5B4632', False, 234, 284, .56)),
}

# (antetítulo, título, línea, CTA, destino, escena)
CAMINOS = [
    ('Inspiración', 'Busco ideas para mi casa', 'Sala, comedor, alcoba o entrada', 'Ver ideas por espacio', 'historias.html', 'ideas'),
    ('Búsqueda', 'Ya sé qué pieza quiero', 'Búsquela por su nombre', 'Buscar una pieza', 'buscar.html', 'pieza'),
    ('Regalos', 'Busco un regalo', 'Por ocasión o por presupuesto', 'Ver regalos', 'coleccion-regalos.html', 'regalo'),
    ('Descuentos', 'Busco descuentos', 'Piezas rebajadas, con el precio anterior a la vista', 'Ver descuentos', 'descuentos.html', 'descuentos'),
]
FLECHA_CTA = '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
ARCOS_HTML = """  <section class="sec" aria-labelledby="s4">
    <p class="nota"><b>6</b><span>Consideración: según lo que busca</span><span>Un CTA por camino</span><span>Suave: la foto se acerca al pasar o enfocar; los arcos entran al bajar</span><span>4 fotos ≈ 50 KB c/u, diferidas · 0 KB de JavaScript</span></p>
    <h2 class="t" id="s4">¿Qué lo trae hoy?</h2>
    <p class="apoyo">Elija por dónde empezar.</p>
    <ul class="arcos arcos-foto">
%s    </ul>
    <p class="arcos-nota">Fotos por producir: %s</p>
  </section>
""" % (''.join(
    '      <li style="--i:%d"><a href="%s"><span class="arco"><span class="arco-img">%s</span><span class="arco-txt">'
    '<span class="arco-k">%s</span><span class="arco-t">%s</span><span class="arco-d">%s</span><span class="arco-cta">%s %s</span></span></span></a></li>\n'
    % (i, href, ESCENAS[esc], k, t, d, cta, FLECHA_CTA) for i, (k, t, d, cta, href, esc) in enumerate(CAMINOS)),
    '<span class="pendiente">[FOTO: sala con piezas de la tienda]</span> <span class="pendiente">[FOTO: repisa con piezas]</span> '
    '<span class="pendiente">[FOTO: regalo abierto con una figura]</span> <span class="pendiente">[FOTO: piezas con su etiqueta de descuento]</span>')

ARCOS_CSS = '''/* 4 · ¿Qué lo trae hoy? Arcos con la pieza saliendo del arco (team-showcase adaptado:
   enlaces reales, foco igual que el cursor, sin superponer en celular, tonos de la marca, entra al verse una vez) */
.arcos{list-style:none;margin:var(--s5) 0 0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:var(--s5) var(--s3);perspective:1000px}
.arcos a{display:flex;flex-direction:column;gap:var(--s3);text-decoration:none;color:var(--tinta)}
.arco{position:relative;display:flex;flex-direction:column;align-items:center;text-align:center;height:280px;padding:var(--s6) var(--s3) 0;border-radius:50% 50% 0 0;background:var(--tono);overflow:hidden;
  transition:transform 250ms cubic-bezier(.2,.7,.2,1),box-shadow 250ms}
.arco-t{font:600 1.25rem/1.15 var(--titulo);max-width:12ch}
.arco-d{margin-top:var(--s1);font-size:.8125rem;color:#5E4C42;max-width:18ch}
.arco-img{position:absolute;left:8%;right:8%;bottom:0;height:62%}
.arco-img svg{width:100%;height:100%;display:block}
.arco-cta{font-weight:500;font-size:.9375rem;text-decoration:underline;text-underline-offset:3px;text-align:center}
.arcos a:hover .arco,.arcos a:focus-visible .arco{transform:translateY(-10px) scale(1.03);box-shadow:0 14px 28px rgba(49,38,32,.14)}
.arcos a:focus-visible{outline:none}
.arcos a:focus-visible .arco-cta{outline:2px solid var(--tinta);outline-offset:4px}
@supports (animation-timeline:view()){
  @media (prefers-reduced-motion:no-preference){
    .arcos li{animation:entrar-arco linear both;animation-timeline:view();animation-range:entry calc(5% + var(--i) * 6%) cover calc(22% + var(--i) * 2%)}
    @keyframes entrar-arco{from{opacity:0;transform:translateY(48px) rotateX(14deg)}}
  }
}
@media (prefers-reduced-motion:reduce){.arco{transition:none}.arcos a:hover .arco,.arcos a:focus-visible .arco{transform:none}}
@media (min-width:960px){
  .arcos{grid-template-columns:repeat(4,1fr);gap:var(--s4);align-items:end}
  .arco{height:360px;padding-top:var(--s7)}
  .arco-t{font-size:1.5rem}
}

/* 5 · Arcos con foto: la foto llena el arco y el texto va abajo, sobre un degradado oscuro que asegura el contraste.
   Antetítulo en champaña, título en serif, línea corta y un botón píldora con flecha. Al pasar o enfocar, la foto se acerca. */
.arcos-foto .arco{height:340px;padding:0;justify-content:flex-end;background:#2C1F18;isolation:isolate}
.arcos-foto .arco-img{position:absolute;inset:0;left:0;right:0;height:auto}
.arcos-foto .arco-img svg{transition:transform 600ms cubic-bezier(.2,.7,.2,1)}
.arcos-foto .arco::after{content:"";position:absolute;inset:0;z-index:0;pointer-events:none;
  background:linear-gradient(0deg,rgba(31,24,20,.9) 0,rgba(31,24,20,.72) 30%,rgba(31,24,20,.25) 52%,rgba(31,24,20,0) 66%)}
.arcos-foto .arco-txt{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;gap:var(--s1);padding:0 var(--s4) var(--s5);color:var(--hueso)}
.arcos-foto .arco-k{font:500 .6875rem/1.3 var(--texto);letter-spacing:.16em;text-transform:uppercase;color:var(--champagne)}
/* Título y línea con alto fijo de dos renglones: los cuatro arcos quedan alineados aunque el texto sea más corto o más largo */
.arcos-foto .arco-t{display:flex;align-items:flex-end;justify-content:center;min-height:2.2em;font-size:1.5rem;line-height:1.1;color:var(--hueso);max-width:13ch;text-wrap:balance}
.arcos-foto .arco-d{margin-top:2px;min-height:2.8em;font-size:.8125rem;line-height:1.4;color:var(--oatmeal);max-width:22ch;text-wrap:balance}
.arcos-foto .arco-cta{margin-top:var(--s3);display:inline-flex;align-items:center;justify-content:center;gap:6px;min-height:40px;padding:6px var(--s4);
  border:1px solid rgba(251,250,249,.75);border-radius:999px;font:500 .8125rem/1.2 var(--texto);letter-spacing:.02em;color:var(--hueso);text-decoration:none;
  transition:background-color 200ms,color 200ms}
.arcos-foto .arco-cta svg{flex:none;width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.arcos-foto a:hover .arco-img svg,.arcos-foto a:focus-visible .arco-img svg{transform:scale(1.06)}
.arcos-foto a:hover .arco-cta,.arcos-foto a:focus-visible .arco-cta{background:var(--hueso);color:var(--tinta);border-color:var(--hueso)}
.arcos-foto a:focus-visible .arco-cta{outline:none}
.arcos-foto a:focus-visible .arco{outline:2px solid var(--tinta);outline-offset:4px}
.arcos-nota{margin-top:var(--s4);display:flex;flex-wrap:wrap;gap:var(--s1) var(--s2);font-size:.8125rem}
/* Celular: pasan de lado, como los arcos de la sección 2; dentro del carrusel no se animan */
@media (max-width:959px){
  .arcos-foto{display:flex;gap:var(--s3);overflow-x:auto;scroll-snap-type:x mandatory;margin:var(--s5) calc(var(--s4) * -1) 0;padding:var(--s4) var(--s4) var(--s2);scroll-padding:0 var(--s4);overscroll-behavior-x:contain}
  .arcos-foto li{flex:0 0 72%;scroll-snap-align:start;animation:none}
  .arcos-foto .arco{height:330px}
}
@media (prefers-reduced-motion:reduce){.arcos-foto .arco-img svg,.arcos-foto .arco-cta{transition:none}.arcos-foto a:hover .arco-img svg,.arcos-foto a:focus-visible .arco-img svg{transform:none}}
@media (min-width:960px){
  .arcos-foto .arco{height:400px;padding:0}
  .arcos-foto .arco-t{font-size:1.625rem}
}

'''

# ---------- 6 · Categorías por tipo, como en el video ----------
CATS = [('Porcelanas y figuras', 'Figuras y piezas para la repisa', 'Ver porcelanas', 'porcelanas.html', ('figura', '#F4F2EE', False)),
        ('Jarrones y recipientes', 'Para flores, ramas o solos', 'Ver jarrones', 'categoria.html', ('anfora', '#D9C7AE', False)),
        ('Flores artificiales', 'Ramos que no se marchitan', 'Ver flores', 'flores-artificiales.html', ('flores', '#E8E2D8', True)),
        ('Mesa', 'Vajillas, copas y accesorios para servir', 'Ver la mesa', 'mesa.html', ('copa', '#DDE6E8', True)),
        ('Centros de mesa', 'Para el centro del comedor', 'Ver centros de mesa', 'centros-de-mesa.html', ('centro', '#D9C7AE', False)),
        ('Esculturas pequeñas', 'Formas para la mesa de centro', 'Ver esculturas', 'esculturas.html', ('escultura', '#5B4632', False)),
        ('Decoraciones del hogar', 'Lámparas y objetos para cada rincón', 'Ver decoración', 'decoracion.html', ('esfera', '#F4F2EE', False))]
TONOS_CAT = ['#E8DCC6', '#E4D7CC', '#E9E3DC', '#F1E4C9', '#DDD5CA', '#EAD9CF', '#E6E0D4']
VITRINA_HTML = '''  <section class="sec" aria-labelledby="s6">
    <p class="nota"><b>2</b><span>Consideración: por tipo de pieza</span><span>CTA: uno por categoría · «Ver todo» al pie, lleva a la tienda</span><span>Suave: los arcos entran al bajar y se levantan al pasar o enfocar (mismo arco de «¿Qué lo trae hoy?»)</span><span>7 recortes ≈ 25 KB · 0 KB de JavaScript</span></p>
    <div class="cab-vitrina">
      <div><h2 class="t" id="s6">Elija por tipo de pieza</h2>
      <p class="apoyo">Siete categorías, de la porcelana a las lámparas. Cada pieza tiene su ficha con material, medidas y origen.</p></div>
    </div>
    <ul class="arcos arcos-cat">
%s    </ul>
    <p class="ver-todo"><a href="tienda.html" aria-label="Ver todo en la tienda">Ver todo</a></p>
  </section>
''' % ''.join(
    '      <li style="--tono:%s;--i:%d"><a href="%s"><span class="arco"><span class="arco-t">%s</span><span class="arco-d">%s</span><span class="arco-img">%s</span></span><span class="arco-cta">%s</span></a></li>\n'
    % (TONOS_CAT[i], i, href, n, d, arte(*dib), cta) for i, (n, d, cta, href, dib) in enumerate(CATS))

VITRINA_CSS = '''/* 6 · Categorías por tipo con los arcos de la 4. Escritorio: los siete en una fila.
   Celular: pasan de lado (en un carrusel la entrada ligada al scroll no avanza, así que ahí no se anima). */
.cab-vitrina{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:var(--s2) var(--s5)}
.arcos-cat{display:flex;gap:var(--s3);overflow-x:auto;scroll-snap-type:x mandatory;margin:var(--s5) calc(var(--s4) * -1) 0;padding:var(--s4) var(--s4) var(--s2);scroll-padding:0 var(--s4);overscroll-behavior-x:contain}
.arcos-cat li{flex:0 0 44%;scroll-snap-align:start}
@media (max-width:959px){.arcos-cat li{animation:none}}
.arcos-cat .arco{height:250px;padding-top:var(--s5)}
/* Al pie: «Ver todo», centrado. En reposo solo una línea de bajo contraste (el texto sí tiene contraste pleno);
   al pasar el puntero o enfocar con teclado se llena de color sólido. En pantallas táctiles, el relleno se ve al tocar */
.ver-todo{display:flex;justify-content:center;margin:var(--s6) 0 0}
.ver-todo a{display:inline-flex;align-items:center;justify-content:center;min-height:48px;min-width:200px;padding:0 var(--s6);font:500 .875rem/1.43 var(--texto);letter-spacing:.08em;text-transform:uppercase;text-decoration:none;color:var(--tinta);background:transparent;border:1px solid var(--perla);border-radius:2px;transition:background-color var(--dur) var(--curva),border-color var(--dur) var(--curva),color var(--dur) var(--curva)}
@media (hover:hover){.ver-todo a:hover{background:var(--tinta);border-color:var(--tinta);color:var(--hueso)}}
.ver-todo a:focus-visible,.ver-todo a:active{background:var(--tinta);border-color:var(--tinta);color:var(--hueso)}
@media (prefers-reduced-motion:reduce){.ver-todo a{transition:none}}
.arcos-cat .arco-t{font-size:1.125rem}
@media (min-width:960px){
  .arcos-cat{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:var(--s3);overflow:visible;margin:var(--s5) 0 0;padding:0}
  .arcos-cat .arco{height:300px;padding:var(--s6) var(--s2) 0}
  .arcos-cat .arco-t{font-size:1.125rem}
  .arcos-cat .arco-d{font-size:.75rem}
  .arcos-cat .arco-img{left:6%;right:6%;height:58%}
  .arcos-cat .arco-cta{font-size:.875rem}
}

'''

VITRINA_JS = ''  # las flechas del diseño anterior ya no se usan


# ---------- 9 · Historias: rejilla de image-gallery ----------
GUIAS = [('Costumbres', 'El pesebre en casa', 'historia-pesebre.html', '#5E262D', ('figura', '#F4F2EE', False)),
         ('Costumbres', 'Cómo poner la mesa para recibir', 'historia.html', '#CFC5B8', ('centro', '#D9C7AE', False)),
         ('Origen', 'La forma del ánfora en el jarrón de hoy', 'historia-anfora.html', '#D9C7AE', ('anfora', '#F1EEE8', False)),
         ('Por comenzar', 'El primer jarrón de una casa', 'historia-primer-jarron.html', '#E8DCC6', ('panza', '#B8752A', True))]
FLECHA = '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
GUIAS_HTML = '''  <section class="sec" aria-labelledby="s9">
    <p class="nota"><b>11</b><span>Confianza y búsqueda: contenido de la marca</span><span>CTA: Leer la guía · Ver todas las guías</span><span>Suave: la foto se oscurece y aparece «Leer la guía» al pasar o enfocar</span><span>4 fotos ≈ 40 KB, diferidas · 0 KB de JavaScript</span></p>
    <header class="guias-cab">
      <h2 class="t" id="s9">Historias</h2>
      <p class="apoyo">Guías para poner la mesa, empezar una casa y conocer de dónde viene cada forma.</p>
    </header>
    <ul class="guias">
%s    </ul>
    <p class="guias-pie"><a class="boton sec2" href="historias.html">Ver todas las guías</a></p>
  </section>
''' % ''.join(
    '      <li><a href="%s" style="--tono:%s"><span class="g-img">%s</span><span class="g-txt"><span class="g-tipo">%s</span>'
    '<span class="g-t">%s</span><span class="pendiente">[GUÍA PENDIENTE]</span><span class="g-mas">Leer la guía %s</span></span></a></li>\n'
    % (href, tono, arte(*dib), tipo, t, FLECHA) for tipo, t, href, tono, dib in GUIAS)

GUIAS_CSS = '''/* 9 · Historias: rejilla de image-gallery. Tarjetas cuadradas con la foto; al pasar el cursor o al enfocar se oscurecen
   y aparece «Leer la guía». El tipo y el título se ven siempre (en celular no hay cursor) y toda la tarjeta es el enlace. */
.guias-cab{text-align:center;max-width:48rem;margin-inline:auto}
.guias-cab .apoyo{margin-inline:auto}
.guias{list-style:none;margin:var(--s6) 0 0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:var(--s3)}
.guias a{position:relative;display:block;aspect-ratio:1/1;border-radius:8px;overflow:hidden;background:var(--tono);color:var(--hueso);text-decoration:none}
.g-img{position:absolute;inset:0}
.g-img svg{position:absolute;left:22%;right:22%;top:5%;width:56%;height:58%;transition:transform 300ms cubic-bezier(.2,.7,.2,1)}
.guias a::after{content:"";position:absolute;inset:0;background:rgba(31,24,20,.5);opacity:0;transition:opacity 300ms}
.g-txt{position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:flex-end;align-items:flex-start;gap:2px;padding:var(--s3);
  background:linear-gradient(0deg,rgba(31,24,20,.84) 0,rgba(31,24,20,.62) 40%,rgba(31,24,20,0) 68%)}
.g-tipo{font:500 .6875rem/1.3 var(--texto);letter-spacing:.14em;text-transform:uppercase;color:var(--champagne)}
.g-t{font:600 1.125rem/1.15 var(--titulo)}
.g-txt .pendiente{margin-top:2px;font-size:.6875rem}
.g-mas{display:inline-flex;align-items:center;gap:4px;margin-top:var(--s1);font-size:.8125rem;color:rgba(251,250,249,.85);opacity:0;transform:translateY(4px);transition:opacity 300ms,transform 300ms}
.g-mas svg{width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.guias a:hover::after,.guias a:focus-visible::after{opacity:1}
.guias a:hover .g-mas,.guias a:focus-visible .g-mas{opacity:1;transform:none}
.guias a:hover .g-img svg,.guias a:focus-visible .g-img svg{transform:scale(1.04)}
.guias a:focus-visible{outline:2px solid var(--tinta);outline-offset:3px}
@media (hover:none){.g-mas{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.guias a::after,.g-mas,.g-img svg{transition:none}}
.guias-pie{text-align:center;margin-top:var(--s6)}
@media (min-width:960px){
  .guias{display:flex;flex-wrap:wrap;justify-content:center;gap:var(--s4);max-width:64rem;margin-inline:auto}
  .guias li{width:224px}
  .g-txt{padding:var(--s4)}
  .g-t{font-size:1.25rem}
}

'''


def bloque(texto, nombre, nuevo, ini_viejo, fin_viejo, css=False):
    """Pone `nuevo` entre los marcadores de `nombre`. Si aún no existen, reemplaza desde ini_viejo hasta fin_viejo.
    (Las secciones 7 y su guion se definen más abajo, antes de usarse.)"""
    a, b = ('/* %s:ini */' % nombre, '/* %s:fin */' % nombre) if css else ('<!-- %s:ini -->' % nombre, '<!-- %s:fin -->' % nombre)
    envuelto = a + '\n' + nuevo + b + '\n'
    if a in texto:
        i, j = texto.index(a), texto.index(b) + len(b) + 1
    else:
        i, j = texto.index(ini_viejo), texto.index(fin_viejo)
    return texto[:i] + envuelto + texto[j:]


# ---------- 7 · Estantería: piezas en repisas, viajan a su ficha y se agregan al carrito desde aquí ----------
LAMPARA_ARTE = ('<svg class="arte" viewBox="40 40 120 200" aria-hidden="true" focusable="false">'
                '<path d="M92 232 H108 L112 224 Q124 200 116 176 Q110 160 104 150 H96 Q90 160 84 176 Q76 200 88 224 Z" fill="#EFE6DA" stroke="#C9B9A6"/>'
                '<rect x="98" y="126" width="4" height="26" fill="#3B2A20"/><path d="M68 128 L84 68 H116 L132 128 Z" fill="#EDE7DE" stroke="#B9AFA3"/></svg>')
# nombre, material, precio, precio antes, sello, ficha, dibujo
ESTANTE = [('Jarrón de cerámica blanca con asas', 'Cerámica', 189900, None, True, 'ficha-producto.html', arte('anfora', '#F1EEE8')),
           ('Lámpara de mesa con base de cerámica', 'Cerámica', 249900, None, False, 'ficha-lampara.html', LAMPARA_ARTE),
           ('Juego de 6 copas de vino', 'Vidrio', 149900, None, False, 'pieza-juego-de-6-copas-de-vino.html', arte('copa', '#DDE6E8', True)),
           ('Recipiente pequeño de cerámica', 'Cerámica', 79900, 99900, False, 'pieza-recipiente-pequeno-de-ceramica.html', arte('cuenco', '#D9C7AE'))]


def pesos(n):
    return '$' + format(n, ',').replace(',', '.')


def tarjeta_estante(nombre, material, precio, antes, sello, href, dibujo):
    e = estado_pieza(nombre)  # el catálogo manda
    antes, agotada = e['antes'] or antes, e['agotada']
    precio_html = '<strong>%s</strong>' % pesos(precio)
    if antes and not agotada:
        precio_html = ('<strong>%s</strong><s><span class="sr">Antes </span>%s</s><span class="oferta">−%d %%</span>'
                       % (pesos(precio), pesos(antes), round((antes - precio) * 100 / antes)))
    chips = ('<span class="chip-estado chip-oferta" aria-hidden="true">Oferta</span>' if antes and not agotada else '') \
        + ('<span class="chip-estado chip-pocas" aria-hidden="true">Quedan pocas</span>' if e['pocas'] else '') \
        + ('<span class="chip-estado chip-agotada">Agotada</span>' if agotada else '')
    abajo = ('<span class="pocas-txt">%s</span>' % texto_unidades(e['unidades']) if e['pocas'] and not agotada else '')
    boton = ('<a class="agregar" href="%s#aviso-llegada">Avisarme cuando llegue</a>' % href if agotada else
             '<button type="button" class="agregar" data-nombre="%s" data-precio="%d"%s>Agregar al carrito</button>' % (nombre, precio, ' data-unidades="%d"' % e['unidades'] if e['pocas'] else ''))
    fav = (('<button type="button" class="fav" data-fav="%s" data-nombre="%s" aria-pressed="false" aria-label="Guardar %s en favoritos"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">' + _sitio.CORAZON + '</svg></button>') % (href, nombre, nombre))
    return ('        <li class="tarjeta%s"><a href="%s"><span class="foto">%s%s%s</span><h3>%s</h3><span class="meta">%s</span><span class="precio">%s</span>%s</a>%s%s</li>\n'
            % (' agotada' if agotada else '', href, '<span class="sello">Exclusivo</span>' if sello else '', '<span class="chips">%s</span>' % chips if chips else '', dibujo,
               nombre, material, precio_html, abajo, fav, boton))


# ---------- 3 · Lo nuevo: galería con scroll vertical. Foto quieta a la izquierda, piezas que pasan a la derecha ----------
from catalogo import NUEVAS, clave as clave_cat
NUEVO = [('Ave de porcelana azul', 94900, 'pieza-ave-de-porcelana-azul.html', ('figura', '#C9D6E3'), False),
         ('Jarrón de vidrio ámbar', 129900, 'pieza-jarron-de-vidrio-ambar.html', ('panza', '#B8752A', True), False),
         ('Centro de mesa con flores', 129900, 'pieza-centro-de-mesa-con-flores.html', ('centro', '#D9C7AE'), True),
         ('Cuenco para servir', 69900, 'pieza-cuenco-para-servir.html', ('cuenco', '#D9C7AE'), False),
         ('Ave de porcelana blanca', 89900, 'pieza-ave-de-porcelana-blanca.html', ('figura', '#F4F2EE'), True),
         ('Bandeja con florero', 99900, 'pieza-bandeja-con-florero.html', ('flores', '#DDE6E8', True), False)]
assert [clave_cat(n) for n, *_ in NUEVO] == NUEVAS, 'Lo nuevo del inicio debe coincidir con catalogo.NUEVAS'
EN_INICIO = 4  # la cuadrícula del inicio muestra solo las 4 más recientes; el resto está en lo-nuevo.html


def tarjeta_nueva(nombre, precio, href, dibujo, sello):
    e = estado_pieza(nombre)  # el catálogo manda: oferta, quedan pocas, agotada
    antes, agotada = e['antes'], e['agotada']
    precio_html = '<strong>%s</strong>' % pesos(precio)
    if antes and not agotada:
        precio_html += '<s><span class="sr">Antes </span>%s</s><span class="oferta">−%d %%</span>' % (pesos(antes), round((antes - precio) * 100 / antes))
    chips = ('<span class="chip-estado chip-oferta" aria-hidden="true">Oferta</span>' if antes and not agotada else '') \
        + ('<span class="chip-estado chip-pocas" aria-hidden="true">Quedan pocas</span>' if e['pocas'] else '') \
        + ('<span class="chip-estado chip-agotada">Agotada</span>' if agotada else '')
    abajo = ('<span class="agotado-txt"><b>Suscríbase</b> para que le avisemos cuando llegue</span>' if agotada else
             '<span class="pocas-txt">%s</span>' % texto_unidades(e['unidades']) if e['pocas'] else '')
    fav = (('<button type="button" class="fav" data-fav="%s" data-nombre="%s" aria-pressed="false" aria-label="Guardar %s en favoritos"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">' + _sitio.CORAZON + '</svg></button>') % (href, nombre, nombre))
    return ('        <li class="nueva%s"><a href="%s%s"><span class="nuevo-foto">%s%s%s</span><h3>%s</h3><span class="nuevo-precio">%s</span>%s</a>%s</li>\n'
            % (' agotada' if agotada else '', href, '#aviso-llegada' if agotada else '',
               '<span class="sello">Exclusivo</span>' if sello else '', '<span class="chips">%s</span>' % chips if chips else '',
               arte(*dibujo), nombre, precio_html, abajo, fav))


# La foto: [FOTO] las piezas nuevas juntas en una casa. En el prototipo, sus dibujos sobre una mesa
ESCENA_NUEVO = [(('panza', '#B8752A', True), 9, 46), (('centro', '#D9C7AE'), 33, 28), (('figura', '#C9D6E3'), 58, 30), (('flores', '#DDE6E8', True), 75, 40)]
ESCENA_NUEVO_HTML = ''.join('<span class="pz" style="left:%d%%;height:%d%%">%s</span>' % (x, h, arte(*dib)) for dib, x, h in ESCENA_NUEVO)

NUEVO_HTML = """  <section class="sec sec-nuevo" aria-labelledby="s-nuevo">
    <p class="nota"><b>3</b><span>Consideración: lo nuevo</span><span>CTA: Lo quiero todo (sobre la foto, lleva a Lo nuevo) · una por pieza</span><span>Suave: la pieza se acerca un poco al pasar o enfocar</span><span>1 foto ≈ 120 KB + 4 recortes ≈ 25 KB c/u, diferidos · 0 KB de JavaScript</span></p>
    <div class="cab-nuevo">
      <h2 class="t" id="s-nuevo">Lo nuevo</h2>
      <p class="apoyo">Las piezas que acaban de llegar a la tienda. <span class="pendiente">[POR CONFIRMAR: cada cuánto llegan piezas nuevas]</span></p>
    </div>
    <div class="nuevo">
      <div class="nuevo-escena">
        <span class="pendiente nuevo-foto-nota">[FOTO: las piezas nuevas juntas, puestas en una casa]</span>
        <span class="mesa" aria-hidden="true"></span>%s
        <a class="nuevo-cta" href="lo-nuevo.html" aria-label="Lo quiero todo: ver todo lo nuevo">Lo quiero todo<span aria-hidden="true"> →</span></a>
      </div>
      <ul class="nuevo-lista">
%s      </ul>
    </div>
  </section>
""" % (ESCENA_NUEVO_HTML, ''.join(tarjeta_nueva(*x) for x in NUEVO[:EN_INICIO]))

NUEVO_CSS = """/* 3 · Lo nuevo: títulos centrados; debajo, una foto grande con «Lo quiero todo» y las 4 piezas más recientes (2 × 2).
   Escritorio: la foto a la izquierda, del mismo alto que la cuadrícula. Celular: la foto arriba y las piezas debajo. Sin JavaScript */
.cab-nuevo{text-align:center}
.cab-nuevo .apoyo{margin-inline:auto}
.nuevo{display:grid;gap:var(--s5);margin-top:var(--s5)}
.nuevo-escena{position:relative;aspect-ratio:1;overflow:hidden;border-radius:4px;background:linear-gradient(180deg,#E9DCC8 0%,#DCCBB3 72%,#CDB89C 100%)}
.nuevo-escena .mesa{position:absolute;left:0;right:0;bottom:0;height:24%;background:linear-gradient(180deg,#6B5240,#4A3628);box-shadow:0 -1px 0 #7E644F}
.nuevo-escena .pz{position:absolute;bottom:21%;display:block;aspect-ratio:2/3}
.nuevo-escena .pz .arte{display:block;width:100%;height:100%}
.nuevo-foto-nota{position:absolute;left:var(--s3);top:var(--s3);z-index:2}
.nuevo-cta{position:absolute;right:var(--s4);bottom:var(--s4);z-index:2;display:inline-flex;align-items:center;min-height:48px;padding:0 var(--s5);background:var(--hueso);color:var(--tinta);border:1px solid var(--hueso);font:500 .875rem/1.43 var(--texto);letter-spacing:.08em;text-transform:uppercase;text-decoration:none;transition:background-color var(--dur) var(--curva),color var(--dur) var(--curva),border-color var(--dur) var(--curva)}
@media (hover:hover){.nuevo-cta:hover{background:var(--tinta);border-color:var(--tinta);color:var(--hueso)}}
.nuevo-cta:focus-visible,.nuevo-cta:active{background:var(--tinta);border-color:var(--tinta);color:var(--hueso);outline-color:var(--hueso)}
.nuevo-lista{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s5) var(--s3)}
.nueva{position:relative}
.nueva:has(.fav) .chips{top:60px}
.nueva a{display:block;text-decoration:none;color:inherit}
.nuevo-foto{position:relative;display:grid;place-items:center;aspect-ratio:1;overflow:hidden;border-radius:4px;background:#F6F4F1}
.nuevo-foto .arte{display:block;height:80%;width:auto;max-width:100%;transition:transform 400ms var(--curva)}
.nuevo-foto .chips{top:var(--s2);right:var(--s2);margin:0}
.nuevo-foto .sello{position:absolute;left:var(--s2);top:var(--s2);z-index:2;font:500 .6875rem/1.4 var(--texto);letter-spacing:.12em;text-transform:uppercase;background:var(--hueso);border:1px solid var(--tinta);padding:2px 6px;border-radius:2px}
.nueva h3{margin-top:var(--s3);font:400 1rem/1.35 var(--texto)}
.nuevo-precio{display:flex;flex-wrap:wrap;align-items:baseline;gap:2px var(--s2);margin-top:var(--s1);font-variant-numeric:tabular-nums}
.nuevo-precio strong{font-weight:600;font-size:1.0625rem;color:var(--mocha)}
.nuevo-precio s{font-size:.8125rem;color:var(--cafe-humo)}
.nuevo-precio .oferta{font-size:.8125rem;font-weight:500;color:var(--borgona)}
.nueva .pocas-txt,.nueva .agotado-txt{display:block;margin-top:2px;font-size:.8125rem}
.nueva a:hover .arte,.nueva a:focus-visible .arte{transform:scale(1.05)}
.nueva a:focus-visible{outline:2px solid var(--tinta);outline-offset:4px}
.nueva.agotada .arte{opacity:.5;filter:grayscale(.6)}
@media (min-width:960px){
  .nuevo{grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:var(--s7);align-items:stretch}
  .nuevo-escena{aspect-ratio:auto;min-height:100%}
  .nuevo-lista{gap:var(--s6) var(--s4)}
}
@media (prefers-reduced-motion:reduce){.nuevo-foto .arte,.nuevo-cta{transition:none}.nueva a:hover .arte,.nueva a:focus-visible .arte{transform:none}}

"""


ESTANTE_HTML = '''  <section class="sec sec-estante" aria-labelledby="s7">
    <p class="nota"><b>9</b><span>Decisión: ver la pieza y llevarla</span><span>CTA: Agregar al carrito · Ver toda la selección</span><span>Suave: la pieza viaja a su ficha</span><span>4 recortes ≈ 25 KB · ≈ 2 KB de JavaScript</span></p>
    <div class="cab-estante">
      <div><h2 class="t" id="s7">Piezas de la selección</h2>
      <p class="apoyo">Mírela de cerca, póngala en su carrito y recíbala en su ciudad.</p></div>
      <a class="enlace" href="categoria.html">Ver toda la selección</a>
    </div>
    <ul class="rejilla estanteria">
%s    </ul>
    <div class="aviso-carrito" hidden><span></span><a href="carrito.html">Ver el carrito</a></div>
    <p class="sr" role="status" id="estado-estante"></p>
    <p class="envio-meta">Envío gratis desde %s <span class="pendiente">[POR CONFIRMAR: monto y cobertura]</span></p>
  </section>
''' % (''.join(tarjeta_estante(*x) for x in ESTANTE), pesos(300000))

ESTANTE_CSS = '''/* 7 · Estantería: las piezas en repisas, como en las categorías. Al tocar una, viaja a su ficha (View Transitions);
   «Agregar al carrito» la guarda sin salir del inicio y dice cuánto falta para el envío gratis. */
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
.cab-estante{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:var(--s2) var(--s5)}
.sec-estante .rejilla{--hueco:var(--s3);list-style:none;margin:var(--s6) 0 0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s7) var(--hueco)}
.sec-estante .tarjeta{display:flex;flex-direction:column;text-align:center}
.sec-estante .tarjeta>a{flex:1;display:flex;flex-direction:column;text-decoration:none;color:var(--tinta)}
.sec-estante .foto{position:relative;display:flex;align-items:flex-end;justify-content:center;aspect-ratio:4/5;padding:var(--s3) var(--s2) 0;background:none;font-size:inherit}
/* La repisa: una tabla de madera clara con sombra, continua entre piezas vecinas */
.sec-estante .foto::after{content:"";position:absolute;left:calc(var(--hueco) / -2 - 1px);right:calc(var(--hueco) / -2 - 1px);top:100%;height:16px;
  background:linear-gradient(to bottom,#E2DDD6 0,#FBFAF9 8px,#fff 8px,#E7E2DB 16px);box-shadow:0 1px 0 rgba(49,38,32,.06),0 20px 22px -14px rgba(49,38,32,.36)}
.sec-estante .arte{position:relative;z-index:1;display:block;height:100%;width:auto;max-width:100%;translate:0 7px;transition:translate var(--dur) var(--curva)}
.sec-estante .tarjeta a:hover .arte{translate:0 3px}
.sec-estante .sello{position:absolute;left:0;top:0;z-index:2;font:500 .6875rem/1.4 var(--texto);letter-spacing:.12em;text-transform:uppercase;background:var(--hueso);border:1px solid var(--tinta);padding:2px 6px;border-radius:2px}
.sec-estante h3{margin-top:calc(16px + var(--s4));font-size:1.125rem;line-height:1.2}
.sec-estante .tarjeta a:hover h3{text-decoration:underline;text-underline-offset:3px}
.sec-estante .meta{display:block;font-size:.875rem;color:var(--cafe-humo);margin-top:2px}
.sec-estante .precio{display:flex;flex-wrap:wrap;justify-content:center;align-items:baseline;gap:2px var(--s2);margin-top:var(--s1);font-variant-numeric:tabular-nums}
.sec-estante .precio strong{font-weight:500}
.sec-estante .precio s{font-size:.875rem;color:var(--cafe-humo)}
.sec-estante .oferta{font-size:.8125rem;font-weight:500;color:var(--hueso);background:var(--borgona);padding:3px 8px;border-radius:2px}
/* Estados de la pieza (catálogo único): oferta, quedan pocas, agotada. Iguales a los de la tienda y la ficha */
span.chips{position:absolute;right:var(--s2);top:var(--s2);z-index:2;display:flex;flex-direction:column;align-items:flex-end;gap:4px}
.chip-estado{font:500 .75rem/1.3 var(--texto);padding:3px 8px;border-radius:2px;white-space:nowrap}
.chip-oferta{background:var(--borgona);color:var(--hueso)}
.chip-pocas{background:#F6E7C6;color:#5B4632;border:1px solid #C9A46A}
.chip-agotada{background:#E6E3DF;color:#5F5953;border:1px solid #BBB2A8}
.pocas-txt{display:block;font-size:.8125rem;color:#7A5A1E;margin-top:2px}
.agotado-txt{display:block;font-size:.8125rem;color:#8E2B33;margin-top:2px}
.sec-estante .chips{top:0;right:0}
.sec-estante .tarjeta.agotada .arte{opacity:.5;filter:grayscale(.6)}
a.agregar{display:inline-flex;align-items:center;justify-content:center;text-decoration:none}
.agregar{margin-top:var(--s3);min-height:44px;padding:0 var(--s3);border:1px solid var(--tinta);border-radius:2px;background:transparent;color:var(--tinta);font:500 .8125rem/1.2 var(--texto);letter-spacing:.06em;text-transform:uppercase;cursor:pointer;transition:background-color var(--dur) var(--curva),color var(--dur) var(--curva)}
.agregar:hover{background:var(--oatmeal)}
.agregar.lista{background:var(--tinta);color:var(--hueso)}
.aviso-carrito{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:var(--s2) var(--s4);margin-top:var(--s6);padding:var(--s3) var(--s4);background:var(--suave);border-left:3px solid var(--tinta)}
.aviso-carrito[hidden]{display:none}
.aviso-carrito a{display:inline-flex;align-items:center;min-height:44px;font-weight:500}
.envio-meta{margin-top:var(--s4);text-align:center;font-size:.875rem;color:var(--cafe-humo)}
@view-transition{navigation:auto}
::view-transition-group(pieza){animation-duration:550ms;animation-timing-function:cubic-bezier(.2,.7,.2,1)}
::view-transition-old(pieza),::view-transition-new(pieza){width:100%;height:100%;object-fit:contain}
@media (prefers-reduced-motion:reduce){@view-transition{navigation:none}.sec-estante .arte,.agregar{transition:none}}
@media (min-width:640px){.sec-estante .rejilla{--hueco:var(--s4)}.sec-estante .foto{aspect-ratio:1}}
@media (min-width:960px){.sec-estante .rejilla{--hueco:var(--s5);grid-template-columns:repeat(4,minmax(0,1fr))}}

'''

ESTANTE_CABEZA = '''<script>
/* Al volver de una ficha, la pieza regresa a su lugar en la repisa */
addEventListener('pagereveal', e => {
  if (e.viewTransition) { e.viewTransition.ready.catch(() => {}); e.viewTransition.finished.catch(() => {}); }   // si el navegador cancela la transición, no es un error
  const de = window.navigation && navigation.activation && navigation.activation.from;
  if (!e.viewTransition || !de) return;
  const archivo = de.url.split('/').pop().split(/[?#]/)[0];
  if (!/^(pieza-|ficha-|lampara-)/.test(archivo)) return;
  const arte = document.querySelector('.sec-estante .tarjeta a[href="' + archivo + '"] .arte'); if (!arte) return;
  arte.style.viewTransitionName = 'pieza';
  const limpiar = () => arte.style.viewTransitionName = '';
  e.viewTransition.finished.then(limpiar, limpiar);
});
</script>
'''

ESTANTE_JS = '''<script>
// Sección 7: la pieza tocada es la que viaja a su ficha; «Agregar al carrito» la guarda en el mismo carrito de la ficha y del pago
(() => {
  const sec = document.querySelector('.sec-estante'); if (!sec) return;
  const GRATIS = 300000; // [POR CONFIRMAR: monto real y cobertura]
  const pesos = n => '$' + n.toLocaleString('es-CO');
  const aviso = sec.querySelector('.aviso-carrito'), estado = document.getElementById('estado-estante');
  sec.addEventListener('click', e => {
    const a = e.target.closest('.tarjeta a');
    if (a) {
      sec.querySelectorAll('.arte').forEach(x => x.style.viewTransitionName = '');
      const arte = a.querySelector('.arte'); if (arte) arte.style.viewTransitionName = 'pieza';
      return;
    }
    const b = e.target.closest('.agregar'); if (!b) return;
    let carro = []; try { carro = JSON.parse(localStorage.getItem('hqh-carrito')) || []; } catch (_) {}
    if (!Array.isArray(carro)) carro = [];
    const item = { nombre: b.dataset.nombre, variante: '', precio: +b.dataset.precio, cantidad: 1 };
    const igual = carro.find(x => x.nombre === item.nombre && x.variante === '');
    // Con pocas unidades, no deja agregar más de las que hay
    const tope = +b.dataset.unidades || Infinity;
    if (igual && igual.cantidad >= tope) {
      const aviso_tope = `Ya tiene en el carrito ${tope === 1 ? 'la única unidad que queda' : `las ${tope} unidades que quedan`} de ${item.nombre}.`;
      aviso.querySelector('span').textContent = aviso_tope; aviso.hidden = false; estado.textContent = aviso_tope; return;
    }
    igual ? igual.cantidad++ : carro.push(item);
    try { localStorage.setItem('hqh-carrito', JSON.stringify(carro)); } catch (_) {}
    document.dispatchEvent(new Event('hqh:carrito'));   // la cabecera actualiza su contador
    const n = carro.reduce((t, x) => t + x.cantidad, 0), sub = carro.reduce((t, x) => t + x.cantidad * x.precio, 0), falta = Math.max(0, GRATIS - sub);
    const envio = falta ? `Le faltan ${pesos(falta)} para el envío gratis.` : 'Su pedido ya tiene envío gratis.';
    const texto = `Agregó ${item.nombre}. ${n} ${n === 1 ? 'pieza' : 'piezas'} en el carrito. ${envio}`;
    b.textContent = 'Agregada'; b.classList.add('lista');
    clearTimeout(b.t); b.t = setTimeout(() => { b.textContent = 'Agregar al carrito'; b.classList.remove('lista'); }, 1300);
    aviso.querySelector('span').textContent = texto; aviso.hidden = false;
    estado.textContent = texto;
  });
})();
</script>
'''

# ---------- 8 · Materiales: calidad que se ve de cerca ----------
import random
_r = random.Random(7)  # siempre las mismas motas
MOTAS = ''.join('<circle cx="%d" cy="%d" r="%.1f" fill="%s" fill-opacity="%.2f"/>'
                % (_r.randint(0, 800), _r.randint(0, 450), _r.uniform(.8, 2.6), _r.choice(['#7A6650', '#5B4632', '#9C8467']), _r.uniform(.35, .8))
                for _ in range(260))
TEXTURAS = {
    'porcelana': ('<defs><linearGradient id="mt-pf" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F7F5F1"/><stop offset="1" stop-color="#DCD5CB"/></linearGradient>'
                  '<radialGradient id="mt-pb" cx="62%" cy="36%" r="60%"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".55" stop-color="#F1EEE8"/><stop offset="1" stop-color="#CBC2B6"/></radialGradient></defs>'
                  '<rect width="800" height="450" fill="url(#mt-pf)"/>'
                  '<path d="M240 470 C 290 260, 420 110, 650 84 C 770 70, 850 120, 870 170 L 870 470 Z" fill="url(#mt-pb)"/>'
                  '<path d="M330 470 C 372 300, 474 186, 660 146" fill="none" stroke="#FFFFFF" stroke-width="12" stroke-opacity=".85" stroke-linecap="round"/>'
                  '<path d="M240 470 C 290 268, 418 118, 646 90" fill="none" stroke="#A99C8D" stroke-opacity=".4" stroke-width="2"/>'),
    'ceramica': ('<defs><linearGradient id="mt-cf" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E3D4BE"/><stop offset="1" stop-color="#C9B49A"/></linearGradient></defs>'
                 '<rect width="800" height="450" fill="url(#mt-cf)"/>' + MOTAS +
                 '<path d="M-20 360 C 200 300, 520 300, 820 380" fill="none" stroke="#F4ECDF" stroke-width="10" stroke-opacity=".7"/>'),
    'vidrio': ('<defs><linearGradient id="mt-vf" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4B382B"/><stop offset="1" stop-color="#2C1F18"/></linearGradient>'
               '<radialGradient id="mt-va" cx="45%" cy="45%" r="60%"><stop offset="0" stop-color="#F2C27C"/><stop offset=".6" stop-color="#C98A3A"/><stop offset="1" stop-color="#8E5A22"/></radialGradient></defs>'
               '<rect width="800" height="450" fill="url(#mt-vf)"/>'
               '<ellipse cx="400" cy="250" rx="300" ry="230" fill="url(#mt-va)" fill-opacity=".85"/>'
               '<path d="M150 210 C 210 90, 360 40, 520 60" fill="none" stroke="#FFF6E6" stroke-width="7" stroke-opacity=".75" stroke-linecap="round"/>'
               '<ellipse cx="560" cy="300" rx="60" ry="22" fill="#FFF6E6" fill-opacity=".25" transform="rotate(-20 560 300)"/>'),
    'tela': ('<defs><linearGradient id="mt-tf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F6ECE6"/><stop offset="1" stop-color="#E9D6CC"/></linearGradient>'
             '<radialGradient id="mt-tp" cx="50%" cy="30%" r="70%"><stop offset="0" stop-color="#F7E4DD"/><stop offset="1" stop-color="#D9A9A0"/></radialGradient>'
             '<radialGradient id="mt-tc" cx="50%" cy="30%" r="70%"><stop offset="0" stop-color="#FBEBC8"/><stop offset="1" stop-color="#E2BE7E"/></radialGradient></defs>'
             '<rect width="800" height="450" fill="url(#mt-tf)"/>'
             + ''.join('<ellipse cx="%d" cy="%d" rx="%d" ry="%d" fill="url(#%s)" transform="rotate(%d %d %d)"/>' % (x, y, rx, ry, g, a, x, y)
                       for x, y, rx, ry, g, a in [(250, 260, 210, 120, 'mt-tp', -24), (520, 230, 230, 130, 'mt-tc', 18), (390, 380, 220, 110, 'mt-tp', 4), (660, 400, 190, 100, 'mt-tp', -12)])
             + '<path d="M140 250 C 240 230, 330 250, 420 290 M430 220 C 520 200, 610 210, 700 250 M300 380 C 380 370, 450 380, 520 400" fill="none" stroke="#FFFFFF" stroke-opacity=".5" stroke-width="3"/>'),
}
MATERIALES = [('porcelana', 'Porcelana', 'Esmalte liso, de brillo suave.', 'Ver piezas de porcelana', 'porcelanas.html', True),
              ('ceramica', 'Cerámica', 'Más gruesa, con una textura que se siente al tacto.', 'Ver piezas de cerámica', 'categoria.html', False),
              ('vidrio', 'Vidrio', 'Transparente o en ámbar, como las copas y los jarrones.', 'Ver cristalería', 'mesa-cristaleria.html', False),
              ('tela', 'Tela', 'Pétalos que no se marchitan ni piden agua.', 'Ver flores artificiales', 'flores-artificiales.html', False)]
MAT_HTML = '''  <section class="sec sec-mat" aria-labelledby="s-mat">
    <p class="nota"><b>10</b><span>Deseo y confianza: el material</span><span>CTA: uno por material</span><span>Suave: las texturas se mueven un poco al bajar</span><span>4 fotos de detalle ≈ 60 KB c/u, diferidas · 0 KB de JavaScript</span></p>
    <div class="mat">
      <div class="mat-txt">
        <h2 class="t" id="s-mat">Calidad que se ve de cerca</h2>
        <p class="apoyo">Mire de cerca el esmalte, el borde de una copa y la tela de un pétalo antes de elegir.</p>
        <p class="mat-nota">El material exacto de cada pieza está en su ficha. <span class="pendiente">[POR CONFIRMAR: fotos de detalle de las piezas reales]</span></p>
      </div>
%s    </div>
  </section>
''' % ''.join(
    '      <a class="mat-t%s" href="%s"><span class="mat-img"><svg viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">%s</svg></span>'
    '<span class="mat-cap"><span class="mat-n">%s</span><span class="mat-d">%s</span><span class="mat-cta">%s</span></span></a>\n'
    % (' grande' if grande else '', href, TEXTURAS[clave], n, d, cta) for clave, n, d, cta, href, grande in MATERIALES)

MAT_CSS = '''/* 8 · Materiales: fotos de detalle de cada material, como «Materials and details» del video.
   Texto a la izquierda, porcelana grande a la derecha y los otros tres debajo. Paralaje suave solo con transform. */
.mat{display:grid;gap:var(--s3)}
.mat-txt{padding-bottom:var(--s3)}
.mat-nota{margin-top:var(--s3);font-size:.875rem;color:#5E4C42}
.mat-t{position:relative;display:block;overflow:clip;border-radius:8px;aspect-ratio:16/10;text-decoration:none;color:var(--tinta);background:var(--suave)}
.mat-img{position:absolute;inset:-8% 0;display:block}
.mat-img svg{width:100%;height:100%;display:block}
.mat-cap{position:absolute;left:var(--s3);right:var(--s3);bottom:var(--s3);max-width:300px;display:flex;flex-direction:column;gap:2px;padding:var(--s3);background:var(--hueso);border-radius:6px;box-shadow:0 8px 20px rgba(20,14,10,.16)}
.mat-n{font:600 1.25rem/1.15 var(--titulo)}
.mat-d{font-size:.875rem;color:#5E4C42}
.mat-cta{margin-top:var(--s1);font-size:.875rem;font-weight:500;text-decoration:underline;text-underline-offset:3px}
.mat-t:hover .mat-cta{text-decoration-thickness:2px}
.mat-t:focus-visible{outline:2px solid var(--tinta);outline-offset:3px}
@supports (animation-timeline:view()){
  @media (prefers-reduced-motion:no-preference){
    /* overflow:clip y no hidden: hidden convierte la tarjeta en contenedor de scroll y el paralaje no avanzaría */
    .mat-img{animation:paralaje linear both;animation-timeline:view();animation-range:cover 0% cover 100%}
    @keyframes paralaje{from{transform:translateY(-5%)}to{transform:translateY(5%)}}
  }
}
@media (min-width:640px){
  .mat{grid-template-columns:1fr 1fr}
  .mat-txt,.mat-t.grande{grid-column:1 / -1}
  .mat-t{aspect-ratio:4/3}
  .mat-t:last-child{grid-column:1 / -1;aspect-ratio:16/7}
}
@media (min-width:960px){
  .mat{grid-template-columns:repeat(3,1fr)}
  .mat-txt{grid-column:1;grid-row:1;align-self:center;padding:0 var(--s5) 0 0}
  .mat-t.grande{grid-column:2 / 4;grid-row:1;aspect-ratio:16/9}
  .mat-t,.mat-t:last-child{grid-column:auto;aspect-ratio:4/3}
}

'''


# ---------- 3 · Testimonios: tarjetas que pasan solas (infinite-moving-cards, adaptado) ----------
# Reseñas DE EJEMPLO para el diseño: el inicio solo las publica cuando sean reales y con permiso.
# (estrellas, título, texto, pieza, ficha, ciudad, nombre)
RESENAS = [
    (5, 'Llegó entera y bien empacada', 'Pedí el jarrón con asas para Medellín. Venía en caja, con papel de seda, y es igual al de la foto.',
     'Jarrón de cerámica blanca con asas', 'ficha-producto.html', 'Medellín', 'Carolina R.'),
    (5, 'La mesa quedó lista para la visita', 'Compré la vajilla blanca y las copas. Combinan entre sí y no tuve que buscar nada más.',
     'Vajilla de 16 piezas blanca', 'pieza-vajilla-de-16-piezas-blanca.html', 'Bogotá', 'Andrés P.'),
    (3, 'Una copa llegó despicada', 'La caja venía golpeada y una de las seis copas tenía el borde despicado. Me la cambiaron, pero tardó más de lo que esperaba.',
     'Juego de 6 copas de vino', 'pieza-juego-de-6-copas-de-vino.html', 'Barranquilla', 'Felipe S.'),
    (4, 'Bonita, más pequeña de lo que imaginé', 'La escultura es preciosa, pero la imaginaba más grande. Las medidas estaban en la ficha; debí mirarlas mejor.',
     'Escultura curva blanca', 'pieza-escultura-curva-blanca.html', 'Cali', 'Mariana G.'),
    (5, 'Llegó bien hasta Pereira', 'La mandé directo a la casa de mi mamá como regalo de Navidad y le llegó bien embalada.',
     'Ave de porcelana blanca', 'pieza-ave-de-porcelana-blanca.html', 'Pereira', 'Juliana T.'),
    (5, 'Nadie cree que sean de tela', 'Llevo meses con el ramo en la entrada y sigue igual. Todos preguntan si son naturales.',
     'Ramo de flores rosa y champaña', 'pieza-ramo-de-flores-rosa-y-champana.html', 'Bucaramanga', 'Diana C.'),
]


# En el inicio, solo reseñas de 3 estrellas o más. Las de 1 y 2 no se esconden: siguen en la ficha de cada pieza,
# con la respuesta de la tienda [POR CONFIRMAR: política de reseñas]
MIN_ESTRELLAS = 3
RESENAS_INICIO = [r for r in RESENAS if r[0] >= MIN_ESTRELLAS]


def tarjeta_resena(n, titulo, texto, pieza, href, ciudad, nombre, copia):
    respuesta = ('<p class="testi-resp"><b>Respuesta de la tienda:</b> <span class="pendiente">[RESPUESTA REAL PENDIENTE]</span></p>' if n <= 3 else '')
    return ('        <li class="testi-t"%s><span class="testi-estrellas" role="img" aria-label="%d de 5 estrellas">%s<span class="vacias">%s</span></span>'
            '<h3 class="testi-titulo">%s</h3><p class="testi-texto">%s</p>%s'
            '<p class="testi-tags"><a href="%s">%s</a><span>%s</span></p>'
            '<p class="testi-nombre">%s <span class="pendiente">[RESEÑA REAL PENDIENTE]</span></p></li>\n'
            % (' aria-hidden="true" inert' if copia else '', n, '★' * n, '★' * (5 - n), titulo, texto, respuesta, href, pieza, ciudad, nombre))


TESTI_HTML = """  <section class="sec sec-testi" aria-labelledby="s-testi">
    <p class="nota"><b>4</b><span>Confianza: lo que dicen otros clientes</span><span>CTA: la pieza de cada reseña</span><span>Suave: las tarjetas pasan solas; se pausan con el cursor, el foco o el botón</span><span>0 imágenes · ≈ 1 KB de JavaScript</span></p>
    <div class="testi-cab">
      <div><h2 class="t" id="s-testi">Lo que dicen quienes ya compraron</h2>
      <p class="apoyo">Una muestra de lo que dicen quienes ya compraron. En la ficha de cada pieza están todas sus reseñas. <span class="pendiente">[POR CONFIRMAR: política de reseñas]</span></p></div>
      <button type="button" class="testi-pausa" aria-pressed="false"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path class="i-pausa" d="M4 3h3v10H4zM9 3h3v10H9z"/><path class="i-play" d="M4 3l9 5-9 5z"/></svg><span>Pausar las reseñas</span></button>
    </div>
    <p class="testi-aviso pendiente">[Reseñas de ejemplo para el diseño. Esta sección se publica solo con reseñas reales y con permiso de quien las escribe.]</p>
    <div class="testi">
      <ul class="testi-pista">
%s      </ul>
    </div>
  </section>
""" % (''.join(tarjeta_resena(*r, copia=False) for r in RESENAS_INICIO) + ''.join(tarjeta_resena(*r, copia=True) for r in RESENAS_INICIO))

TESTI_CSS = """/* 3 · Testimonios: el diseño de infinite-moving-cards sin el cargo de la persona.
   Pasan solas, despacio (≈ 26 px/s), y se detienen con el cursor, con el foco del teclado o con el botón de pausa (WCAG 2.2.2).
   Solo transform. La segunda copia de las tarjetas es solo visual: aria-hidden e inert. Movimiento reducido: fila quieta que se desliza a mano. */
.testi-cab{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:var(--s3) var(--s5)}
.testi-pausa{display:inline-flex;align-items:center;gap:var(--s2);min-height:44px;padding:0 var(--s4);border:1px solid var(--tinta);border-radius:999px;background:transparent;color:var(--tinta);font:500 .8125rem/1 var(--texto);cursor:pointer}
.testi-pausa:hover{background:var(--oatmeal)}
.testi-pausa svg{width:14px;height:14px;fill:currentColor}
.testi-pausa .i-play,.testi-pausa[aria-pressed=true] .i-pausa{display:none}
.testi-pausa[aria-pressed=true] .i-play{display:inline}
.testi-aviso{margin-top:var(--s3)}
.testi{--hueco:var(--s4);position:relative;margin:var(--s5) calc(var(--s4) * -1) 0;overflow:hidden;
  -webkit-mask-image:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent);mask-image:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent)}
.testi-pista{display:flex;gap:var(--hueco);width:max-content;margin:0;padding:var(--s2) var(--s4);list-style:none;animation:desfile 80s linear infinite}
.testi:hover .testi-pista,.testi:focus-within .testi-pista,.testi.pausado .testi-pista,.testi.fuera .testi-pista{animation-play-state:paused}
@keyframes desfile{to{transform:translateX(calc(-50% - var(--hueco) / 2))}}
.testi-t{flex:0 0 auto;width:min(20rem,calc(100vw - 4rem));display:flex;flex-direction:column;gap:var(--s2);padding:var(--s4) var(--s5) var(--s5);background:#fff;border:1px solid var(--perla);border-radius:16px;box-shadow:0 1px 2px rgba(49,38,32,.05);transition:transform 200ms ease}
.testi-t:hover{transform:translateY(-2px)}
.testi-estrellas{font-size:1rem;letter-spacing:2px;color:#A97A26}
.testi-estrellas .vacias{color:var(--perla)}
.testi-titulo{font:600 1.25rem/1.2 var(--titulo)}
.testi-texto{font-size:.9375rem;line-height:1.55;color:#5E4C42}
.testi-resp{font-size:.8125rem;color:#5E4C42;padding:var(--s2) var(--s3);background:var(--suave);border-radius:8px}
.testi-tags{display:flex;flex-wrap:wrap;gap:6px}
.testi-tags a,.testi-tags span{display:inline-flex;align-items:center;min-height:24px;padding:2px 10px;border:1px solid var(--perla);border-radius:999px;background:var(--suave);font-size:.75rem;color:#5E4C42;text-decoration:none}
.testi-tags a{color:var(--tinta);text-decoration:underline;text-underline-offset:2px}
.testi-tags a:focus-visible{outline:2px solid var(--tinta);outline-offset:2px}
.testi-nombre{margin-top:auto;padding-top:var(--s2);font-size:.875rem;font-weight:500}
.testi-nombre .pendiente{font-weight:400;font-size:.6875rem}
@media (prefers-reduced-motion:reduce){
  .testi{overflow-x:auto;-webkit-mask-image:none;mask-image:none;scroll-snap-type:x mandatory}
  .testi-pista{animation:none}
  .testi-pista [aria-hidden=true]{display:none}
  .testi-t{scroll-snap-align:start;transition:none}
  .testi-pausa{display:none}
}
@media (min-width:960px){.testi{margin:var(--s5) 0 0}}

"""

TESTI_JS = """<script>
// Sección 3: botón de pausa de las reseñas; además se detienen cuando la sección no está en pantalla
(() => {
  const caja = document.querySelector('.testi'), b = document.querySelector('.testi-pausa'); if (!caja || !b) return;
  b.addEventListener('click', () => {
    const pausar = b.getAttribute('aria-pressed') !== 'true';
    b.setAttribute('aria-pressed', pausar); caja.classList.toggle('pausado', pausar);
    b.querySelector('span').textContent = pausar ? 'Reanudar las reseñas' : 'Pausar las reseñas';
  });
  new IntersectionObserver(([e]) => caja.classList.toggle('fuera', !e.isIntersecting)).observe(caja);
})();
</script>
"""


# ---------- 14 · Cierre: invitar a recorrer la tienda (no de temporada) ----------
ESTANTES = []
for fila, base in enumerate((176, 344, 512)):
    piezas = [('anfora', '#F1EEE8', False), ('copa', '#C9934E', True), ('figura', '#F4F2EE', False), ('panza', '#B8752A', True), ('escultura', '#5B4632', False),
              ('flores', '#E8E2D8', True), ('tarro', '#6E7F68', False), ('alto', '#D9C7AE', False), ('cuenco', '#F4F2EE', False), ('esfera', '#D9C7AE', False)]
    for k in range(7):
        forma, color, vidrio = piezas[(k * 3 + fila * 2) % len(piezas)]
        ESTANTES.append(colocar(forma, color, vidrio, 110 + k * 165 + (fila % 2) * 40, base, .5 if forma in ('alto', 'flores') else .56))
REPISAS = ''.join('<rect x="0" y="%d" width="1200" height="10" fill="#7A604B"/><rect x="0" y="%d" width="1200" height="8" fill="#000" fill-opacity=".25"/>' % (y, y + 10) for y in (176, 344, 512))
ESCENA_CIERRE = ('<svg viewBox="0 0 1200 600" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">'
                 '<defs><linearGradient id="ci-p" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4B382B"/><stop offset="1" stop-color="#2A1E17"/></linearGradient></defs>'
                 '<rect width="1200" height="600" fill="url(#ci-p)"/>' + REPISAS + ''.join(ESTANTES) + '</svg>')
ICONOS = {'envio': '<path d="M3 7h11v9H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="17.5" r="1.5"/><circle cx="17" cy="17.5" r="1.5"/>',
          'caja': '<path d="M4 8l8-4 8 4v8l-8 4-8-4z"/><path d="M4 8l8 4 8-4M12 12v8"/>',
          'cuenta': '<circle cx="12" cy="8" r="3.5"/><path d="M5 20c1.5-3.5 4-5 7-5s5.5 1.5 7 5"/><path d="M17 4l4 4M21 4l-4 4"/>'}
CIERRE_HTML = """  <section class="sec" aria-labelledby="s-cierre">
    <p class="nota"><b>14</b><span>Acción: entrar a la tienda</span><span>CTA: Ver todas las piezas</span><span>Sin movimiento</span><span>1 foto ≈ 150 KB, diferida · 0 KB de JavaScript</span></p>
    <div class="cierre2">
      <div class="cierre2-img">%s</div>
      <div class="cierre2-txt">
        <p class="ante">Tienda en línea</p>
        <h2 id="s-cierre">Recorra la tienda, pieza por pieza</h2>
        <p class="cierre2-sub">Porcelanas, jarrones, vajillas, flores artificiales y lámparas para decorar su casa, con envío a todo Colombia.</p>
        <a class="boton grande" href="tienda.html">Ver todas las piezas</a>
        <ul class="cierre2-garantias">%s</ul>
      </div>
    </div>
    <p class="cierre2-nota"><span class="pendiente">[FOTO a todo el ancho: repisas con piezas reales de la tienda. En producción va como &lt;img&gt; con texto alternativo y carga diferida]</span></p>
  </section>
""" % (ESCENA_CIERRE, ''.join('<li><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">%s</svg>%s</li>' % (ICONOS[i], t)
                               for i, t in [('envio', 'Envío a todo el país'), ('caja', 'Embalaje para piezas frágiles'), ('cuenta', 'Compra sin crear cuenta')]))

CIERRE_CSS = """/* 14 · Cierre: repisas llenas de piezas a todo el ancho (el «estante» de la tienda) y una sola acción grande.
   Debajo del botón, tres frases que quitan los miedos del último paso. El velo oscuro del centro asegura el contraste del texto. */
.cierre2{position:relative;overflow:hidden;margin:0 calc(var(--s4) * -1);min-height:520px;display:grid;place-items:center;background:#2A1E17;color:var(--hueso);text-align:center}
.cierre2-img{position:absolute;inset:0}
.cierre2-img svg{width:100%;height:100%;display:block}
.cierre2::after{content:"";position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse 62% 72% at 50% 50%,rgba(31,24,20,.9) 0,rgba(31,24,20,.74) 55%,rgba(31,24,20,.5) 100%)}
.cierre2-txt{position:relative;z-index:1;display:grid;justify-items:center;gap:var(--s3);padding:var(--s8) var(--s4);max-width:46rem}
.cierre2 .ante{color:var(--champagne)}
.cierre2 h2{font-size:clamp(2.25rem,5.4vw,3.75rem);line-height:1.05;max-width:14ch}
.cierre2-sub{color:var(--oatmeal);max-width:46ch}
.cierre2 .boton.grande{margin-top:var(--s3)}
.cierre2 .boton.grande:hover{background:var(--oatmeal);border-color:var(--oatmeal)}
.cierre2 :focus-visible{outline-color:var(--champagne)}
.cierre2-garantias{list-style:none;margin:var(--s2) 0 0;padding:0;display:flex;flex-wrap:wrap;justify-content:center;gap:var(--s2) var(--s5);font-size:.875rem;color:var(--oatmeal)}
.cierre2-garantias li{display:inline-flex;align-items:center;gap:var(--s2)}
.cierre2-garantias svg{flex:none;width:18px;height:18px;fill:none;stroke:var(--champagne);stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.cierre2-nota{margin-top:var(--s3)}
@media (min-width:960px){.cierre2{margin:0;min-height:580px}}

"""

t = io.open(ARCHIVO, encoding='utf-8').read()
# Tokens de movimiento que usan la galería y la estantería
if '--curva:' not in t.split('</style>')[0]:
    t = t.replace('  --titulo:"Cormorant Garamond"', '  --dur:200ms; --curva:cubic-bezier(.2,.7,.2,1);\n  --titulo:"Cormorant Garamond"', 1)
t = bloque(t, 'estante', ESTANTE_CSS, '/* 7 · Estantería */', '/* 8 · Nosotros */', css=True)
t = bloque(t, 'estante', ESTANTE_HTML, '  <!-- 7 -->\n', '  <!-- 8 -->')
t = bloque(t, 'estante-cabeza', ESTANTE_CABEZA, '</head>', '</head>')
t = bloque(t, 'estante-js', ESTANTE_JS, '</body>', '</body>')
t = t.replace('  .estante{grid-template-columns:repeat(4,1fr)}\n', '')  # regla del diseño anterior
t = bloque(t, 'hero', HERO_CSS, '/* 1 · Hero 3D */', '/* 2 · Lo que se pregunta */', css=True)
t = bloque(t, 'arcos', ARCOS_CSS, '/* 4 · ¿Qué lo trae hoy? */', '/* 5 · Galería', css=True)
t = bloque(t, 'vitrina', VITRINA_CSS, '/* 6 · Categorías por tipo */', '/* 7 · Estantería */', css=True)
t = bloque(t, 'hero', HERO_HTML, '  <!-- 1 -->\n', '  <!-- 2 -->')
t = bloque(t, 'arcos', ARCOS_HTML, '  <!-- 4 -->\n', '  <!-- 5 -->')
t = bloque(t, 'vitrina', VITRINA_HTML, '  <!-- 6 -->\n', '  <!-- 7 -->')
t = bloque(t, 'vitrina-js', VITRINA_JS, '</body>', '</body>')
t = bloque(t, 'nuevo', NUEVO_CSS, '/* testimonios:ini */', '/* testimonios:ini */', css=True)
t = bloque(t, 'nuevo', NUEVO_HTML, '<!-- testimonios:ini -->', '<!-- testimonios:ini -->')
t = bloque(t, 'guias', GUIAS_CSS, '/* 9 · Historias */', '.faq-t{', css=True)
t = bloque(t, 'guias', GUIAS_HTML, '  <!-- 9 -->\n', '  <!-- 10 -->')
t = t.replace('  .historias{grid-template-columns:repeat(3,1fr)}\n', '')  # regla del diseño anterior
t = bloque(t, 'materiales', MAT_CSS, '/* materiales:ini */', '/* materiales:fin */', css=True)
t = bloque(t, 'materiales', MAT_HTML, '<!-- materiales:ini -->', '<!-- materiales:fin -->')
t = bloque(t, 'testimonios', TESTI_CSS, '/* testimonios:ini */', '/* testimonios:fin */', css=True)
t = bloque(t, 'testimonios', TESTI_HTML, '<!-- testimonios:ini -->', '<!-- testimonios:fin -->')
t = bloque(t, 'testimonios-js', TESTI_JS, '</body>', '</body>')
t = bloque(t, 'cierre', CIERRE_CSS, '/* 12 · Cierre */', '/* 12 · Cierre */', css=True)
t = bloque(t, 'cierre', CIERRE_HTML, '  <!-- 14 -->\n', '  <footer class="pie"')
# ---------- Global · Modal de bienvenida (variante D, elegida el 23/11/2026) ----------
# Reglas: una sola vez, desde la segunda página de la visita, a los 20 s o al bajar la mitad (lo que pase primero);
# en computador también al ir a salir de la pestaña. No vuelve en 14 días si se cierra, ni nunca si ya se suscribió.
# No aparece en carrito, pago, Mi cuenta ni ayuda: en el tema solo se carga en las páginas de catálogo e inicio.
BIENVENIDA_CSS = """/* Modal de bienvenida (variante D). Prefijo bv- para no chocar con el inicio */
html:has(.bv[open]){overflow:hidden}
.bv{--error:#8E2B33;--error-fondo:#F5E3E4;border:0;padding:0;width:calc(100% - 32px);max-width:580px;max-height:calc(100dvh - 32px);overflow:auto;border-radius:12px;background:var(--hueso);color:var(--tinta);box-shadow:0 24px 64px rgba(30,20,14,.35)}
.bv::backdrop{background:rgba(49,38,32,.56)}
.bv[open]{animation:bv-entra 260ms var(--curva)}
@keyframes bv-entra{from{opacity:0;transform:translateY(14px)}}
.bv-cerrar{position:absolute;top:var(--s2);right:var(--s2);z-index:3;width:44px;height:44px;display:grid;place-items:center;border:0;border-radius:50%;background:rgba(251,250,249,.92);color:var(--tinta);cursor:pointer}
.bv-cerrar svg{width:18px;height:18px;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;fill:none}
.bv-piezas{display:grid;place-items:end center;height:112px;padding-top:var(--s4);background:var(--oatmeal)}
.bv-piezas svg{display:block;width:190px;height:86px}
.bv-cuerpo{padding:var(--s5);text-align:center}
.bv-ante{font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;color:var(--borgona)}
.bv-titulo{margin-top:var(--s2);font-size:1.875rem;line-height:1.1}
.bv-linea{margin-top:var(--s2);color:var(--cafe-humo)}
.bv-linea strong{color:var(--tinta);font-weight:500}
.bv-form{margin-top:var(--s5);text-align:left}
.bv-campo{margin-bottom:var(--s4)}
.bv-campo label{display:block;font-weight:500;margin-bottom:var(--s1)}
.bv-campo label small{font-weight:400;font-size:.9375rem;color:var(--cafe-humo)}
.bv-campo input{width:100%;min-height:48px;padding:var(--s3) var(--s4);font:inherit;color:var(--tinta);background:#fff;border:1px solid var(--cafe-humo);border-radius:2px}
.bv-campo [aria-invalid=true]{border-color:var(--error);box-shadow:inset 0 0 0 1px var(--error)}
.bv-ayuda{display:block;margin-top:var(--s1);font-size:.9375rem;color:var(--cafe-humo)}
.bv-dos{display:grid;gap:0 var(--s3)}
@media (min-width:480px){.bv-dos{grid-template-columns:1fr 1fr}}
.bv-casilla{display:flex;gap:var(--s3);align-items:flex-start;min-height:44px;padding:var(--s1) 0;cursor:pointer}
.bv-casilla input{flex:none;width:22px;height:22px;margin:1px 0 0;accent-color:var(--tinta)}
.bv-error{display:flex;gap:var(--s2);margin:var(--s1) 0 var(--s2);padding:var(--s2) var(--s3);font-size:.9375rem;color:var(--error);background:var(--error-fondo);border-radius:2px}
.bv-error::before{content:"!";flex:none;width:18px;height:18px;display:grid;place-content:center;font-weight:500;font-size:.75rem;border:1.5px solid currentColor;border-radius:50%}
.bv-acciones{display:grid;gap:var(--s3);margin-top:var(--s4)}
.bv-boton{display:inline-flex;align-items:center;justify-content:center;width:100%;min-height:52px;padding:0 var(--s5);font:500 .875rem/1.43 var(--texto);letter-spacing:.08em;text-transform:uppercase;border-radius:2px;border:1px solid var(--tinta);background:var(--tinta);color:var(--hueso);cursor:pointer;transition:background-color var(--dur) var(--curva)}
.bv-boton:hover{background:#1F1814}
/* «Por el momento no»: del mismo tamaño que el principal y con borde, para que se reconozca como botón */
.bv-boton.sec{background:transparent;color:var(--tinta);border:2px solid var(--tinta)}
.bv-boton.sec:hover{background:var(--suave)}
.bv-chica{font-size:.9375rem;color:var(--cafe-humo);text-align:center}
.bv-listo h3{font-size:1.75rem;line-height:1.15}
.bv-listo p{margin-top:var(--s2)}
.bv-listo .bv-boton{margin-top:var(--s5)}
/* [PROTOTIPO] botón para abrirlo sin esperar las reglas */
.bv-proto{position:fixed;left:var(--s3);top:148px;z-index:40;min-height:44px;padding:0 var(--s4);font:500 .8125rem/1 var(--texto);color:var(--info);background:var(--info-fondo);border:1px solid var(--info);border-radius:999px;cursor:pointer}
@media (max-width:639px){
  .bv{width:100%;max-width:100%;margin:auto 0 0;max-height:92dvh;border-radius:16px 16px 0 0}
  .bv[open]{animation:bv-sube 300ms var(--curva)}
  @keyframes bv-sube{from{transform:translateY(100%)}}
}
@media (prefers-reduced-motion:reduce){.bv[open]{animation:none}.bv-boton{transition:none}}

"""

BIENVENIDA_HTML = """<dialog class="bv" id="bienvenida" aria-labelledby="bv-t" aria-describedby="bv-d">
  <button type="button" class="bv-cerrar" data-bv-cerrar aria-label="Cerrar"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg></button>
  <div class="bv-piezas" aria-hidden="true">
    <svg viewBox="0 0 220 100"><g stroke="#5B4632" stroke-width="1.3" stroke-linejoin="round">
      <path d="M44 92 Q34 70 41 52 Q47 39 45 28 L43 19 H65 L63 28 Q61 39 67 52 Q74 70 64 92 Z" fill="#FBFAF9"/>
      <path d="M88 74 Q90 92 110 92 Q130 92 132 74 Z" fill="#F4D9A0"/>
      <path d="M163 92 Q154 80 160 66 Q164 58 166 47 L166 36 H174 L174 47 Q176 58 180 66 Q186 80 177 92 Z" fill="#D9C7AE"/>
      <path d="M170 36 Q168 22 172 9" fill="none"/></g>
      <circle cx="172" cy="9" r="5" fill="#722F37"/><rect x="0" y="92" width="220" height="5" fill="#5B4632"/></svg>
  </div>
  <div class="bv-cuerpo">
    <p class="bv-ante">Boletín</p>
    <h2 class="bv-titulo" id="bv-t">Nuevas piezas y nuevas ofertas</h2>
    <p class="bv-linea" id="bv-d"><strong>Suscríbase y entérese de todo.</strong> Le avisamos sobre ofertas exclusivas y nuestros nuevos productos.</p>
    <form class="bv-form" novalidate>
      <div class="bv-dos">
        <div class="bv-campo"><label for="bv-nombre">Nombre y apellido</label>
          <input id="bv-nombre" name="nombre" type="text" autocomplete="name" aria-describedby="bv-e-nombre"><div id="bv-e-nombre" role="alert"></div></div>
        <div class="bv-campo"><label for="bv-correo">Correo electrónico</label>
          <input id="bv-correo" name="correo" type="email" autocomplete="email" inputmode="email" spellcheck="false" autocapitalize="off" aria-describedby="bv-e-correo"><div id="bv-e-correo" role="alert"></div></div>
      </div>
      <div class="bv-dos">
        <div class="bv-campo"><label for="bv-celular">Celular</label>
          <input id="bv-celular" name="celular" type="tel" autocomplete="tel-national" inputmode="tel" aria-describedby="bv-a-celular bv-e-celular"><span class="bv-ayuda" id="bv-a-celular">Diez dígitos. Por ahí le avisamos por WhatsApp.</span><div id="bv-e-celular" role="alert"></div></div>
        <div class="bv-campo"><label for="bv-empresa">Empresa <small>(opcional)</small></label>
          <input id="bv-empresa" name="empresa" type="text" autocomplete="organization" aria-describedby="bv-a-empresa"><span class="bv-ayuda" id="bv-a-empresa">Si compra para un negocio, le contamos también sobre los precios al por mayor.</span></div>
      </div>
      <label class="bv-casilla"><input type="checkbox" name="datos" id="bv-datos" aria-describedby="bv-e-datos"><span>Autorizo el tratamiento de mis datos para recibir novedades y ofertas por correo y WhatsApp, según la <a href="politica-de-datos.html">política de privacidad</a>.</span></label>
      <div id="bv-e-datos" role="alert"></div>
      <div class="bv-acciones">
        <button type="submit" class="bv-boton">Sí, quiero suscribirme</button>
        <button type="button" class="bv-boton sec" data-bv-cerrar>Por el momento no</button>
        <p class="bv-chica">Puede darse de baja cuando quiera, desde cualquier correo.</p>
      </div>
    </form>
    <div class="bv-listo" hidden>
      <h3 tabindex="-1">Listo, le avisaremos</h3>
      <p>Le escribiremos a <b data-bv="correo"></b> y por WhatsApp al <b data-bv="celular"></b> cuando lleguen piezas nuevas o haya ofertas.</p>
      <p><span class="pendiente">[PROTOTIPO: no se envía nada]</span></p>
      <button type="button" class="bv-boton" data-bv-cerrar>Seguir mirando</button>
    </div>
  </div>
</dialog>
<button type="button" class="bv-proto" id="bv-proto">[PROTOTIPO] Ver el modal de bienvenida</button>
<script>
/* Modal de bienvenida. Reglas de aparición: ver docs/handoff-desarrollo.md */
(() => {
  const d = document.getElementById('bienvenida'); if (!d || !d.showModal) return;
  const f = d.querySelector('form'), listo = d.querySelector('.bv-listo');
  const CLAVE = 'hqh-bienvenida', DIAS = 14, SEGUNDOS = 20;   // [POR CONFIRMAR con prueba A/B]
  const evento = (e, x = {}) => (window.dataLayer = window.dataLayer || []).push({ event: e, variante: 'D', ...x });
  const leer = () => { try { return JSON.parse(localStorage.getItem(CLAVE)); } catch (e) { return null; } };
  const guardar = v => { try { localStorage.setItem(CLAVE, JSON.stringify(v)); } catch (e) {} };
  // Páginas vistas en esta visita: el modal espera a la segunda (así no tapa la página al llegar desde un buscador)
  let paginas = 1; try { paginas = +(sessionStorage.getItem('hqh-paginas') || 0) + 1; sessionStorage.setItem('hqh-paginas', paginas); } catch (e) {}
  const est = leer();
  const bloqueado = !!(est && (est.suscrito || (est.cerrado && Date.now() - est.cerrado < DIAS * 864e5)));

  function reiniciar() {
    f.reset(); f.hidden = false; listo.hidden = true; d.dataset.suscrito = '';
    f.querySelectorAll('[role=alert]').forEach(e => e.replaceChildren());
    f.querySelectorAll('[aria-invalid]').forEach(e => e.removeAttribute('aria-invalid'));
  }
  function abrir(motivo) {
    if (d.open || document.querySelector('dialog[open]')) return;
    reiniciar(); d.showModal(); evento('modal_bienvenida_ver', { motivo });
  }
  d.addEventListener('click', e => { if (e.target === d) d.close('fuera'); else if (e.target.closest('[data-bv-cerrar]')) d.close('cerrar'); });
  d.addEventListener('close', () => {
    if (d.dataset.suscrito) return;
    guardar({ cerrado: Date.now() }); evento('modal_bienvenida_cerrar', { como: d.returnValue || 'esc' });
  });

  if (!bloqueado && paginas >= 2) {
    let hecho = false;
    const disparar = motivo => {
      if (hecho) return;
      const a = document.activeElement;
      if (a && a.matches('input, textarea, select')) return void setTimeout(() => disparar(motivo), 5000);   // no interrumpe a quien escribe
      hecho = true; limpiar(); abrir(motivo);
    };
    const t = setTimeout(() => disparar('tiempo'), SEGUNDOS * 1000);
    const alBajar = () => { if (scrollY + innerHeight >= document.documentElement.scrollHeight * 0.5) disparar('mitad'); };
    const alSalir = e => { if (e.clientY <= 0 && !e.relatedTarget) disparar('salida'); };
    const limpiar = () => { clearTimeout(t); removeEventListener('scroll', alBajar); document.removeEventListener('mouseout', alSalir); };
    addEventListener('scroll', alBajar, { passive: true });
    if (matchMedia('(pointer: fine)').matches) document.addEventListener('mouseout', alSalir);
  }

  /* Validación junto a cada campo; el foco va al primero que falte, en el orden en que se ven */
  const $ = id => document.getElementById(id);
  function marcar(id, m) {
    const caja = $('bv-e-' + id), campo = $('bv-' + id);
    caja.replaceChildren();
    if (m) { const p = document.createElement('p'); p.className = 'bv-error'; p.textContent = m; caja.append(p); }
    if (campo.type !== 'checkbox') campo.setAttribute('aria-invalid', m ? 'true' : 'false');
  }
  f.addEventListener('change', e => { if (e.target.id === 'bv-datos' && e.target.checked) marcar('datos', ''); });
  f.addEventListener('submit', e => {
    e.preventDefault();
    const el = f.elements, correo = el.correo.value.trim(), cel = el.celular.value.replace(/\\D/g, '').replace(/^57(?=3\\d{9}$)/, '');
    const fallas = [
      ['nombre', el.nombre.value.trim().includes(' ') ? '' : 'Escriba su nombre y su apellido.'],
      ['correo', !correo ? 'Escriba su correo para avisarle.' : /^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/.test(correo) ? '' : 'Revise el correo: le falta la @ o el dominio.'],
      ['celular', !cel ? 'Escriba su celular: diez dígitos que empiecen por 3.' : /^3\\d{9}$/.test(cel) ? '' : 'Escriba un celular de diez dígitos que empiece por 3. Ejemplo: 300 123 4567.'],
      ['datos', el.datos.checked ? '' : 'Para avisarle, autorice el tratamiento de sus datos.'],
    ];
    fallas.forEach(([id, m]) => marcar(id, m));
    const primera = fallas.find(([, m]) => m);
    if (primera) return $('bv-' + primera[0]).focus();
    d.dataset.suscrito = '1'; guardar({ suscrito: true, fecha: Date.now() });   // [PROTOTIPO] en producción lo guarda la plataforma
    evento('suscripcion_bienvenida', { beneficio: 'novedades', negocio: !!el.empresa.value.trim() });
    listo.querySelector('[data-bv=correo]').textContent = correo;
    listo.querySelector('[data-bv=celular]').textContent = cel.replace(/(\\d{3})(\\d{3})(\\d{4})/, '$1 $2 $3');
    f.hidden = true; listo.hidden = false; listo.querySelector('h3').focus();
  });

  document.getElementById('bv-proto').addEventListener('click', () => abrir('prototipo'));
})();
</script>
"""
t = bloque(t, 'bienvenida', BIENVENIDA_CSS, '/* testimonios:ini */', '/* testimonios:ini */', css=True)
t = bloque(t, 'bienvenida', BIENVENIDA_HTML, '</body>', '</body>')
# ---------- Sitio: la misma cabecera, menú y pie de todas las páginas (herramientas/sitio.py) ----------
_dir = os.path.dirname(ARCHIVO)
_base_css = io.open(os.path.join(_dir, 'base.css'), encoding='utf-8').read()
_base_js = io.open(os.path.join(_dir, 'base.js'), encoding='utf-8').read()
t = bloque(t, 'sitio', _sitio.css_base(_base_css) + _sitio.SITIO_CSS, '</style>\n<!-- estante-cabeza:ini -->', '</style>\n<!-- estante-cabeza:ini -->', css=True)
_proto = '<div class="proto" role="region" aria-label="Nota del prototipo">'
t = bloque(t, 'cabecera-sitio', _sitio.cabecera(), _proto, _proto)
t = bloque(t, 'pie-sitio', '</main>\n' + _sitio.FOOTER + _sitio.EXTRAS + '<script>\n' + _base_js + '\n' + _sitio.SITIO_JS + '</script>\n',
           '  <footer class="pie" aria-label="Pie de página (resumen)">', '<!-- vitrina-js:ini -->')
if '<main class="ancho">' in t:
    t = t.replace('<main class="ancho">', '<main class="ancho" id="contenido">', 1)
io.open(ARCHIVO, 'w', encoding='utf-8', newline='\n').write(t)
ids = re.findall(r' id="([^"]+)"', t)
print('inicio-estructura.html', len(t) // 1024, 'KB · ids repetidos:', sorted({i for i in ids if ids.count(i) > 1}) or 'ninguno')

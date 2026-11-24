"""Galería de colecciones «compre el look»: una escena por colección, con un punto sobre cada pieza.
Uso: python herramientas/galeria_colecciones.py prototipos
Las escenas son dibujos de ejemplo (arte.py); en producción cada una es una foto real del ambiente."""
import io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from arte import arte, FORMAS
from catalogo import estado as estado_pieza, pesos as pesos_cat, texto_pocas, texto_unidades

DEST = sys.argv[1]
W, H = 800, 600  # lienzo de cada escena


def pieza(forma, color, vidrio, cx, base, s):
    """Coloca un dibujo de 200 × 300 (de pie en y = 286) con su base en (cx, base) y escala s.
    Devuelve el SVG anidado y el centro de la pieza, donde va el punto."""
    x, y = cx - 100 * s, base - 286 * s
    bx, by, bw, bh = FORMAS[forma][1]
    svg = arte(forma, color, vidrio).replace('<svg class="arte"', '<svg x="%.1f" y="%.1f" width="%.1f" height="%.1f"' % (x, y, 200 * s, 300 * s), 1)
    return svg, (round(x + (bx + bw / 2) * s), round(y + (by + bh / 2) * s))


# Fondo de cada escena: pared, luz y la superficie donde se apoyan las piezas
def fondo(pared, pared2, sup, sup2, base, luz='#FFF6E6', extra=''):
    return ('<defs><linearGradient id="{i}-p" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>'
            '<radialGradient id="{i}-l" cx="560" cy="120" r="520" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="%s" stop-opacity=".75"/><stop offset="1" stop-color="%s" stop-opacity="0"/></radialGradient></defs>'
            '<rect width="800" height="600" fill="url(#{i}-p)"/><rect width="800" height="600" fill="url(#{i}-l)"/>%s'
            '<rect x="-10" y="%d" width="820" height="10" fill="%s"/><rect x="-10" y="%d" width="820" height="%d" fill="%s"/>'
            % (pared, pared2, luz, luz, extra, base, sup, base + 10, 600 - base, sup2))


VENTANA = '<path d="M60 40 H260 V360 H60 Z" fill="#FFFFFF" fill-opacity=".22"/><path d="M160 40 V360 M60 200 H260" stroke="#FFFFFF" stroke-opacity=".35" stroke-width="4"/>'
CUADRO = '<rect x="470" y="70" width="150" height="190" fill="none" stroke="%s" stroke-width="8"/><path d="M494 228 Q545 140 596 228" fill="none" stroke="%s" stroke-width="2"/>'
CAJA = ('<g transform="translate(-44 0)"><path d="M128 398 L160 374 L200 392 L160 418 Z" fill="#F7F2EA" opacity=".9"/><rect x="120" y="402" width="104" height="48" fill="#722F37"/>'
        '<path d="M172 402 V450" stroke="#F4D9A0" stroke-width="5"/><path d="M114 396 L226 388 L230 402 L118 408 Z" fill="#5E262D"/>'
        '<path d="M160 396 q-16 -18 4 -16 q8 2 8 14 q0 -12 8 -14 q20 -2 4 16" fill="none" stroke="#F4D9A0" stroke-width="3"/></g>')
PEDESTAL = '<rect x="430" y="446" width="100" height="74" fill="#CFC5B8"/><rect x="422" y="440" width="116" height="8" fill="#DDD5CA"/>'

# Colección: nombre, página, texto, CTA, fondo y piezas (nombre, material, precio, ficha, forma, color, vidrio, cx, base, escala)
COLECCIONES = [
    ('La mesa que recibe', 'coleccion.html',
     'Vajillas, cristalería y centros de mesa que funcionan juntos, para cuando llega visita.', 'Ver La mesa que recibe',
     fondo('#EFE5D4', '#E2D3BC', '#8A6E55', '#6B5240', 440, extra=VENTANA),
     [('Recipiente con tapa de cerámica', 'Cerámica', '$99.900', 'pieza-recipiente-con-tapa-de-ceramica.html', 'tarro', '#6E7F68', False, 215, 440, 1.15),
      ('Florero de vidrio transparente', 'Vidrio', '$69.900', 'pieza-florero-de-vidrio-transparente.html', 'florero', '#DDE6E8', True, 305, 440, 1.35),
      ('Vajilla de 16 piezas blanca', 'Porcelana', '$389.900', 'pieza-vajilla-de-16-piezas-blanca.html', 'plato', '#F4F2EE', False, 440, 446, 1.35),
      ('Juego de 6 copas de vino', 'Vidrio', '$149.900', 'pieza-juego-de-6-copas-de-vino.html', 'copa', '#DDE6E8', True, 565, 440, 1.2)],
     [('copa', '#DDE6E8', True, 618, 446, 1.1)]),
    ('Primer hogar', 'coleccion-primer-hogar.html',
     'Pocas piezas que combinan, para empezar una casa sin comprarlo todo de una vez.', 'Ver Primer hogar',
     fondo('#F3F0ED', '#E6E0DA', '#C9B49A', '#B39B80', 420, extra=CUADRO % ('#BBB2A8', '#BBB2A8')),
     [('Jarrón de vidrio ámbar', 'Vidrio', '$129.900', 'pieza-jarron-de-vidrio-ambar.html', 'panza', '#B8752A', True, 225, 420, 1.25),
      ('Ramo de flores rosa y champaña', 'Tela', '$49.900', 'pieza-ramo-de-flores-rosa-y-champana.html', 'flores', '#DDE6E8', True, 345, 420, 1.4),
      ('Juego de 6 platos arena', 'Cerámica', '$179.900', 'pieza-juego-de-6-platos-arena.html', 'plato', '#D9C7AE', False, 480, 424, 1.2),
      ('Escultura curva blanca', 'Cerámica', '$179.900', 'pieza-escultura-curva-blanca.html', 'escultura', '#F4F2EE', False, 598, 420, 1.2)],
     [('plato', '#D9C7AE', False, 480, 410, 1.12)]),
    ('Regalos que se guardan', 'coleccion-regalos.html',
     'Para bodas, inauguraciones y fechas especiales, con medidas y material a la vista.', 'Ver regalos',
     fondo('#6E3A3A', '#4E2A2B', '#7A604B', '#5B4632', 450, luz='#F4D9A0', extra=CAJA),
     [('Ave de porcelana blanca', 'Porcelana', '$89.900', 'pieza-ave-de-porcelana-blanca.html', 'figura', '#F4F2EE', False, 240, 450, 1.25),
      ('Juego de 6 copas de vino', 'Vidrio', '$149.900', 'pieza-juego-de-6-copas-de-vino.html', 'copa', '#DDE6E8', True, 340, 450, 1.2),
      ('Centro de mesa con flores', 'Tela y cerámica', '$129.900', 'pieza-centro-de-mesa-con-flores.html', 'centro', '#D9C7AE', False, 462, 450, 1.4),
      ('Jarrón de cerámica blanca con asas', 'Cerámica', '$189.900', 'ficha-producto.html', 'anfora', '#F1EEE8', False, 592, 450, 1.1)],
     []),
    ('Piezas protagonistas', 'coleccion-protagonistas.html',
     'Las piezas de mayor presencia, las que se ven al entrar a una sala.', 'Ver las protagonistas',
     fondo('#D9D2C9', '#C8BFB4', '#A89886', '#8E7D6B', 520, extra=PEDESTAL),
     [('Jarrón alto de porcelana', 'Porcelana', '$319.900', 'pieza-jarron-alto-de-porcelana.html', 'alto', '#F4F2EE', False, 222, 520, 1.4),
      ('Ánfora decorativa de cerámica', 'Cerámica', '$259.900', 'pieza-anfora-decorativa-de-ceramica.html', 'anfora', '#D9C7AE', False, 348, 520, 1.3),
      ('Escultura curva café', 'Cerámica', '$179.900', 'pieza-escultura-curva-cafe.html', 'escultura', '#5B4632', False, 480, 440, 1.1),
      ('Ramo alto con florero', 'Tela y vidrio', '$119.900', 'pieza-ramo-alto-con-florero.html', 'flores', '#E8E2D8', True, 608, 520, 1.6)],
     []),
]


def escena(i, fondo_svg, piezas, adornos):
    cuerpo, puntos = '', []
    for forma, color, vidrio, cx, base, s in adornos:  # piezas repetidas de la escena, sin punto propio
        cuerpo += pieza(forma, color, vidrio, cx, base, s)[0]
    for nombre, material, precio, href, forma, color, vidrio, cx, base, s in piezas:
        svg, (px, py) = pieza(forma, color, vidrio, cx, base, s)
        cuerpo += svg
        puntos.append((nombre, material, precio, href, px, py, (forma, color, vidrio)))
    svg = ('<svg class="dibujo" viewBox="0 0 %d %d" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">%s%s</svg>'
           % (W, H, fondo_svg.replace('{i}', 'e%d' % i), cuerpo))
    return svg, puntos


def panel(i, col):
    nombre, href, texto, cta, fondo_svg, piezas, adornos = col
    svg, puntos = escena(i, fondo_svg, piezas, adornos)
    botones, tarjetas, lista = '', '', ''
    for j, (pn, mat, pr, ph, px, py, dib) in enumerate(puntos):
        tid = 't%d-%d' % (i, j)
        # Mismo estado que en la tienda y la ficha
        e = estado_pieza(pn)
        valor = int(pr.replace('$', '').replace('.', ''))
        precio_txt, extra, cta, destino = '<strong>%s</strong>' % pr, '', 'Ver la pieza', ph
        if e['agotada']:
            extra, cta, destino = '<span class="chip-estado chip-agotada">Agotada</span>', 'Avisarme cuando llegue', ph + '#aviso-llegada'
        else:
            if e['antes']:
                precio_txt += ' <s>%s</s> <span class="chip-estado chip-oferta">−%d %%</span>' % (pesos_cat(e['antes']), round((1 - valor / e['antes']) * 100))
            if e['pocas']:
                extra = '<span class="chip-estado chip-pocas">%s</span>' % texto_unidades(e['unidades'])
        estado_lista = ' · Agotada' if e['agotada'] else ' · %s' % texto_pocas(e['unidades']) if e['pocas'] else ' · Oferta' if e['antes'] else ''
        botones += ('<button type="button" class="punto" data-x="%d" data-y="%d" aria-expanded="false" aria-controls="%s" aria-label="Ver %s, %s"></button>'
                    % (px, py, tid, pn, pr))
        tarjetas += ('<div class="tarjeta-punto" id="%s" hidden><div class="mini">%s</div><div><h4>%s</h4><p>%s</p><span class="precio-punto">%s</span>%s'
                     '<a href="%s">%s</a></div></div>' % (tid, arte(*dib), pn, mat, precio_txt, extra, destino, cta))
        lista += '<li><a href="%s"><span class="mini">%s</span><span><span class="n">%s</span><span class="p">%s%s</span></span></a></li>' % (destino, arte(*dib), pn, pr, estado_lista)
    activa = ' activa' if i == 0 else ''
    return ('<li class="panel%s" data-panel>'
            '<div class="info" id="info%d"><h3>%s</h3><p>%s</p>'
            '<p class="cuenta">%d piezas en esta foto</p>'
            '<ul class="en-foto" aria-label="Piezas de esta foto">%s</ul>'
            '<a class="boton" href="%s">%s</a></div>'
            '<div class="escena-col">%s<div class="puntos">%s%s</div>'
            '<button type="button" class="abrir" aria-expanded="%s" aria-controls="info%d"><span>%s</span></button></div></li>'
            % (activa, i, nombre, texto, len(puntos), lista, href, cta, svg, botones, tarjetas, 'true' if i == 0 else 'false', i, nombre))


PAGINA = '''<!doctype html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Galería de colecciones · Historias que Habitan</title>
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500..600;1,500&family=Jost:wght@400..500&display=swap" rel="stylesheet">
<style>
:root{
  --tinta:#312620; --cafe-humo:#705C51; --piedra:#BBB2A8; --perla:#CDC9C6; --hueso:#FBFAF9; --oatmeal:#E8DCC6; --suave:#F3F0ED;
  --espresso:#3B2A20; --champagne:#F4D9A0; --info:#3E5A73; --info-fondo:#E4EAF0;
  --s1:4px; --s2:8px; --s3:12px; --s4:16px; --s5:24px; --s6:32px; --s7:48px; --s8:64px;
  --dur:200ms; --curva:cubic-bezier(.2,.7,.2,1);
  --titulo:"Cormorant Garamond",Georgia,serif; --texto:"Jost",system-ui,-apple-system,"Segoe UI",sans-serif;
}
*{box-sizing:border-box}
[hidden]{display:none!important}
body{margin:0;background:var(--hueso);color:var(--tinta);font:400 1rem/1.5 var(--texto);-webkit-text-size-adjust:100%}
a{color:inherit;text-underline-offset:3px;text-decoration-thickness:1px}
:focus-visible{outline:2px solid var(--tinta);outline-offset:3px}
h1,h2,h3,h4{font-family:var(--titulo);font-weight:600;margin:0;text-wrap:balance}
p{margin:0}
.ancho{max-width:1200px;margin:0 auto;padding:0 var(--s4)}
.proto{background:var(--info-fondo);color:var(--info);font-size:.875rem;padding:var(--s2) var(--s4)}
.proto a{font-weight:500}

/* Sección: así va en el inicio */
.colecciones{padding:var(--s7) 0 var(--s8)}
.galeria-cab{text-align:center;max-width:48rem;margin-inline:auto}
.galeria-cab h2{font-size:clamp(2rem,4vw,2.75rem);line-height:1.1}
.galeria-cab p{margin:var(--s2) auto 0;color:var(--cafe-humo);max-width:56ch}
.galeria{list-style:none;margin:var(--s5) calc(var(--s4) * -1) 0;padding:0 var(--s4) var(--s3);display:flex;gap:var(--s3);overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding:0 var(--s4);overscroll-behavior-x:contain}
.panel{flex:0 0 86%;scroll-snap-align:start;min-width:0;display:flex;flex-direction:column}
.escena-col{position:relative;aspect-ratio:4/5;overflow:hidden;background:var(--perla);border-radius:8px}
.dibujo{position:absolute;inset:0;width:100%;height:100%;display:block}
.abrir{display:none}
.info{order:2;padding-top:var(--s3)}
.info h3{font-size:1.5rem;line-height:1.2}
.info>p{margin-top:var(--s1);color:var(--cafe-humo);font-size:.9375rem}
.info .cuenta{margin-top:var(--s3);font-size:.8125rem;letter-spacing:.06em;text-transform:uppercase;color:var(--cafe-humo)}
.en-foto{list-style:none;margin:var(--s2) 0 0;padding:0;display:grid;gap:var(--s1)}
.en-foto a{display:grid;grid-template-columns:44px 1fr;gap:var(--s3);align-items:center;min-height:52px;text-decoration:none;padding:var(--s1) 0;border-bottom:1px solid var(--perla)}
.en-foto .mini{display:block;width:44px;height:44px;background:var(--suave)}
.en-foto .mini svg,.tarjeta-punto .mini svg{width:100%;height:100%;display:block}
.en-foto .n{display:block;font-size:.9375rem;line-height:1.3}
.en-foto .p{display:block;font-size:.8125rem;color:var(--cafe-humo)}
.en-foto a:hover .n{text-decoration:underline}
.boton{display:inline-flex;align-items:center;justify-content:center;min-height:48px;margin-top:var(--s4);padding:0 var(--s5);font:500 .875rem/1.43 var(--texto);letter-spacing:.08em;text-transform:uppercase;text-decoration:none;border-radius:2px;border:1px solid var(--tinta);background:var(--tinta);color:var(--hueso);transition:background-color var(--dur) var(--curva)}
.boton:hover{background:#1F1814}

/* Puntos «compre el look» */
.puntos{position:absolute;inset:0}
.galeria [hidden]{display:none!important}  /* también dentro de otras páginas que no traen esta regla */
.punto{position:absolute;left:var(--x);top:var(--y);translate:-50% -50%;width:44px;height:44px;border-radius:50%;border:0;padding:0;background:transparent;cursor:pointer;display:grid;place-content:center;z-index:2}
.punto::before{content:"";width:28px;height:28px;border-radius:50%;background:rgba(49,38,32,.28);border:2px solid var(--hueso);box-shadow:0 0 0 1px rgba(49,38,32,.45),0 2px 8px rgba(49,38,32,.3)}
.punto::after{content:"";position:absolute;inset:0;margin:auto;width:8px;height:8px;border-radius:50%;background:var(--hueso)}
.punto:hover::before,.punto[aria-expanded=true]::before{background:rgba(49,38,32,.5)}
.punto:focus-visible{outline:2px solid var(--tinta);outline-offset:2px;box-shadow:0 0 0 5px var(--hueso);border-radius:50%}
.tarjeta-punto{position:absolute;z-index:3;left:var(--tx);top:var(--ty);width:min(260px,calc(100% - 16px));display:grid;grid-template-columns:64px 1fr;gap:var(--s3);padding:var(--s3);background:var(--hueso);color:var(--tinta);border-radius:2px;box-shadow:0 12px 32px rgba(20,14,10,.3)}
.tarjeta-punto .mini{background:var(--suave);aspect-ratio:1/1}
.tarjeta-punto h4{font:600 1.0625rem/1.2 var(--titulo)}
.tarjeta-punto p{font-size:.8125rem;color:var(--cafe-humo);margin-top:2px}
.tarjeta-punto .precio-punto{display:block;margin-top:var(--s1)}
.tarjeta-punto .precio-punto strong{font-weight:500}
.tarjeta-punto .precio-punto s{font-size:.8125rem;color:var(--cafe-humo)}
.tarjeta-punto .chip-estado{display:inline-block;margin-top:var(--s1)}
.chips-no{position:absolute;right:var(--s2);top:var(--s2);z-index:2;display:flex;flex-direction:column;align-items:flex-end;gap:4px}
.chip-estado{font:500 .75rem/1.3 var(--texto);padding:3px 8px;border-radius:2px;white-space:nowrap}
.chip-oferta{background:var(--borgona);color:var(--hueso)}
.chip-pocas{background:#F6E7C6;color:#5B4632;border:1px solid #C9A46A}
.chip-agotada{background:#E6E3DF;color:#5F5953;border:1px solid #BBB2A8}
.pocas-txt{display:block;font-size:.8125rem;color:#7A5A1E;margin-top:2px}
.agotado-txt{display:block;font-size:.8125rem;color:#8E2B33;margin-top:2px}

.tarjeta-punto a{display:inline-flex;align-items:center;min-height:44px;font-size:.875rem;font-weight:500}
@media (prefers-reduced-motion:no-preference){.tarjeta-punto:not([hidden]){animation:asomar 200ms var(--curva)}@keyframes asomar{from{opacity:0;translate:0 -4px}}}

/* Escritorio: diseño de image-gallery. La colección se abre al pasar el cursor, al llegar con el teclado o al tocarla.
   Las cerradas se ven como franjas de la foto con su nombre; la abierta muestra su texto y sus puntos. */
@media (min-width:960px){
  .galeria{margin:var(--s6) auto 0;padding:0;overflow:visible;max-width:64rem;height:clamp(400px,56vh,520px);gap:var(--s2)}
  .panel{flex:1 1 0;position:relative;transition:flex-grow 500ms var(--curva)}
  /* Cerrado, el panel mide poco: lo que no cabe (el botón oculto de la colección) no puede ensanchar la página */
  .galeria .panel{overflow:clip;overflow-clip-margin:4px}
  .panel.activa{flex-grow:5}
  .escena-col{position:absolute;inset:0;aspect-ratio:auto}
  .abrir{display:flex;position:absolute;inset:0;z-index:4;width:100%;border:0;padding:var(--s4);cursor:pointer;align-items:flex-end;justify-content:flex-start;border-radius:8px;
    background:linear-gradient(0deg,rgba(49,38,32,.6),rgba(49,38,32,0) 50%);color:var(--hueso);font:600 1.25rem/1.15 var(--titulo);text-align:left}
  .abrir:focus-visible{outline:2px solid var(--tinta);outline-offset:3px}
  /* En la abierta, el botón queda solo para el teclado: no tapa los puntos ni se ve */
  .panel.activa .abrir{pointer-events:none;background:none}
  .panel.activa .abrir span{opacity:0}
  .puntos,.info{opacity:0;visibility:hidden}
  .panel.activa .puntos,.panel.activa .info{opacity:1;visibility:visible;transition:opacity 250ms ease 350ms,visibility 0s 350ms}
  .info{position:absolute;z-index:3;left:var(--s4);top:var(--s4);width:min(340px,calc(100% - 32px));padding:var(--s4);background:var(--hueso);border-radius:6px;box-shadow:0 8px 24px rgba(20,14,10,.18)}
  .info .cuenta,.en-foto{display:none}
  .info .boton{margin-top:var(--s3)}
}
@media (prefers-reduced-motion:reduce){.panel,.panel.activa .puntos,.panel.activa .info{transition:none}}
.notas{padding:0 0 var(--s8);color:var(--cafe-humo);font-size:.9375rem;max-width:72ch}
.notas li+li{margin-top:var(--s2)}
</style>
</head>
<body>
<div class="proto" role="region" aria-label="Nota del prototipo">Prototipo de una sección del inicio. Las escenas y las piezas son dibujos; en producción, cada escena es una foto real del ambiente con las piezas de la colección. <a href="inicio-variantes.html">Ver las variantes del hero</a></div>
<main class="ancho">
  <section class="colecciones" aria-labelledby="t-col">
    <header class="galeria-cab">
      <h2 id="t-col">Mire cada colección puesta en casa</h2>
      <p>Toque una pieza de la foto para ver su precio y abrir su ficha.</p>
    </header>
    <ul class="galeria">
%(paneles)s
    </ul>
  </section>
  <ul class="notas">
    <li>En escritorio, como en image-gallery, la colección se abre al pasar el cursor, al llegar con el teclado o al tocarla. Mientras una tarjeta de pieza está abierta, su colección no se cierra, para que los puntos no se muevan.</li>
    <li>En celular, las colecciones pasan de lado y cada foto lleva debajo la lista de sus piezas, porque los puntos pequeños son difíciles de tocar.</li>
    <li>En Shopify es una sección del tema: cada colección es un bloque con su foto, y cada punto es un bloque con la pieza y su posición, que el equipo ajusta en el editor sin programar.</li>
  </ul>
</main>
<script>
// Cada punto se coloca sobre su pieza según cómo se recorte la foto en cada pantalla
function colocar(panel) {
  const svg = panel.querySelector('.dibujo'), m = svg.getScreenCTM(), caja = panel.querySelector('.escena-col').getBoundingClientRect();
  if (!m || !caja.width) return;
  panel.querySelectorAll('.punto').forEach(b => {
    const p = new DOMPoint(+b.dataset.x, +b.dataset.y).matrixTransform(m);
    const x = p.x - caja.left, y = p.y - caja.top;
    b.style.setProperty('--x', x + 'px'); b.style.setProperty('--y', y + 'px');
    b.hidden = x < 22 || y < 22 || x > caja.width - 22 || y > caja.height - 22;  // pieza recortada: sin punto
    const t = document.getElementById(b.getAttribute('aria-controls'));
    if (!t.hidden) ubicar(t, x, y, caja);
  });
}
// La tarjeta se abre al lado del punto que tenga espacio, sin salirse de la foto
function ubicar(t, x, y, caja) {
  const w = t.offsetWidth, h = t.offsetHeight;
  const tx = Math.min(Math.max(x > caja.width / 2 ? x - w + 22 : x - 22, 8), caja.width - w - 8);
  const ty = y + 30 + h < caja.height - 8 ? y + 30 : Math.max(y - 30 - h, 8);
  t.style.setProperty('--tx', tx + 'px'); t.style.setProperty('--ty', ty + 'px');
}
function activar(panel) {
  if (panel.classList.contains('activa')) return;
  cerrarTodas();
  document.querySelectorAll('[data-panel]').forEach(p => {
    const si = p === panel; p.classList.toggle('activa', si);
    p.querySelector('.abrir').setAttribute('aria-expanded', si);
  });
}
function cerrarTodas(salvo) {
  document.querySelectorAll('.punto[aria-expanded=true]').forEach(b => { if (b !== salvo) { b.setAttribute('aria-expanded', 'false'); document.getElementById(b.getAttribute('aria-controls')).hidden = true; } });
}
document.querySelectorAll('[data-panel]').forEach(panel => {
  new ResizeObserver(() => colocar(panel)).observe(panel);
  panel.querySelectorAll('.punto').forEach(b => {
    const t = document.getElementById(b.getAttribute('aria-controls'));
    b.addEventListener('click', () => {
      const abrir = t.hidden; cerrarTodas(b);
      t.hidden = !abrir; b.setAttribute('aria-expanded', abrir);
      if (abrir) colocar(panel);
    });
    const esc = e => { if (e.key === 'Escape' && !t.hidden) { t.hidden = true; b.setAttribute('aria-expanded', 'false'); b.focus(); } };
    b.addEventListener('keydown', esc); t.addEventListener('keydown', esc);
  });
  // Abrir otra colección (escritorio): al pasar el cursor, al llegar con el teclado o al tocarla
  const abrir = panel.querySelector('.abrir');
  panel.addEventListener('pointerenter', e => {
    if (e.pointerType !== 'mouse' || !matchMedia('(min-width: 960px)').matches) return;
    if (document.querySelector('.punto[aria-expanded=true]')) return;  // con una tarjeta abierta, no se mueve nada
    activar(panel);
  });
  abrir.addEventListener('focus', () => activar(panel));
  abrir.addEventListener('click', () => {
    activar(panel);
    // Al elegirla, el foco pasa al título de la colección para seguir con el teclado
    const h = panel.querySelector('.info h3'); h.tabIndex = -1; h.focus({ preventScroll: true });
  });
});
document.addEventListener('click', e => { if (!e.target.closest('.punto, .tarjeta-punto')) cerrarTodas(); });
</script>
</body>
</html>
'''

paneles = '\n'.join('      ' + panel(i, c) for i, c in enumerate(COLECCIONES))
html = PAGINA.replace('%(paneles)s', paneles)
io.open(os.path.join(DEST, 'galeria-colecciones.html'), 'w', encoding='utf-8', newline='\n').write(html)
ids = re.findall(r' id="([^"]+)"', html)
dup = sorted({i for i in ids if ids.count(i) > 1})
# La misma galería entra en el wireframe del inicio, entre sus marcadores
est = os.path.join(DEST, 'inicio-estructura.html')
if os.path.exists(est):
    css = PAGINA[PAGINA.index('/* Sección: así va en el inicio */'):PAGINA.index('.notas{')]
    css = css.replace('.boton{', '.galeria .boton{').replace('.boton:hover', '.galeria .boton:hover')
    js = PAGINA[PAGINA.index('<script>'):PAGINA.index('</script>') + 9]
    bloque = '<style>\n' + css + '</style>\n    <ul class="galeria">\n' + paneles + '\n    </ul>\n' + js
    e = io.open(est, encoding='utf-8').read()
    e, n = re.subn(r'(<!-- galeria:inicio -->).*?(\s*<!-- galeria:fin -->)', lambda m: m.group(1) + '\n' + bloque + m.group(2), e, flags=re.S)
    io.open(est, 'w', encoding='utf-8', newline='\n').write(e)
    print('inicio-estructura.html: galería', 'actualizada' if n else 'sin marcadores')
print('galeria-colecciones.html', len(html) // 1024, 'KB', '· ids repetidos:', dup[:6] if dup else 'ninguno')

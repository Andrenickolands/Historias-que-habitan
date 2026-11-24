"""Genera ficha-lampara.html a partir de ficha-producto.html: misma ficha, con una lámpara y sus controles de luz."""
import io, os, sys
proto = sys.argv[1]
s = io.open(os.path.join(proto, 'ficha-producto.html'), encoding='utf-8').read()
# El guion del sitio (cabecera, favoritos, boletín) va al final: se aparta mientras se arma la lámpara y vuelve al final
_SITIO_JS = ''
if '<!-- sitio-js:ini -->' in s:
    _i, _j = s.index('<!-- sitio-js:ini -->'), s.index('<!-- sitio-js:fin -->\n') + len('<!-- sitio-js:fin -->\n')
    _SITIO_JS, s = s[_i:_j], s[:_i] + s[_j:]


def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)


rep('<title>[EJEMPLO] Jarrón de cerámica blanca con asas · Historias que Habitan</title>', '<title>[EJEMPLO] Lámpara de mesa con base de cerámica · Historias que Habitan</title>')
rep('<h1>Jarrón de cerámica blanca con asas</h1>', '<h1>Lámpara de mesa con base de cerámica</h1>')
rep('Jarrón de cerámica esmaltada de 28 cm, para ramas, flores artificiales o solo. Va bien en una mesa de entrada o en un aparador.',
    'Lámpara de mesa con base de cerámica y pantalla de tela. Tiene tres tonos de luz: cálida, neutra y fría.')
rep('<li><a href="inicio-estructura.html">Inicio</a></li><li><a href="categoria.html">Jarrones y recipientes</a></li>', '<li><a href="inicio-estructura.html">Inicio</a></li><li><a href="lamparas.html">Lámparas</a></li>')
rep('<ul class="fotos" id="fotos"', '<ul class="fotos luces" data-luz="off" data-tono="calida" id="fotos"')

i = s.index('<li class="con-arte">')
j = s.index('</li>', i) + 5
s = s[:i] + ('<li class="luz-foto" data-tonos="calida neutra fria"><div class="escena" style="--lx:50%;--ly:40%"><span class="halo"></span>'
             '<svg viewBox="0 0 200 250" aria-hidden="true" focusable="false"><rect class="mesa" x="0" y="232" width="200" height="18"/>'
             '<path class="ceramica" d="M92 232 H108 L112 224 Q124 200 116 176 Q110 160 104 150 H96 Q90 160 84 176 Q76 200 88 224 Z"/>'
             '<rect class="metal" x="98" y="126" width="4" height="26"/><path class="pantalla" d="M68 128 L84 68 H116 L132 128 Z"/></svg></div>'
             '<small>[ILUSTRACIÓN DE EJEMPLO] Aquí van las fotos reales: apagada y encendida en cada tono</small></li>') + s[j:]

rep('      <div class="acciones-foto">', '''      <div class="barra-luz">
        <div class="interruptor"><span id="et-luz">Luz</span>
          <button type="button" role="switch" aria-checked="false" aria-labelledby="et-luz" id="luz"><span class="perilla"></span></button>
          <span id="estado-luz" aria-hidden="true">Apagada</span></div>
        <fieldset class="tonos" hidden><legend>Tono</legend><div>
          <label><input type="radio" name="tono-luz" value="calida" checked><span><i style="background:#FFB259"></i>Cálida</span></label>
          <label><input type="radio" name="tono-luz" value="neutra"><span><i style="background:#FFE2B0"></i>Neutra</span></label>
          <label><input type="radio" name="tono-luz" value="fria"><span><i style="background:#C9DEFF"></i>Fría</span></label>
        </div></fieldset>
      </div>
      <div class="acciones-foto">''')

rep('<section class="bloque" id="tres-d" aria-labelledby="t-3d">', '<section class="bloque" id="tres-d" aria-labelledby="t-3d" hidden>')
rep('<dd>1 jarrón y la tarjeta de la pieza. No incluye flores.</dd>', '<dd>1 lámpara con su pantalla y la tarjeta de la pieza. <span class="pendiente">[POR CONFIRMAR: si incluye bombillo]</span></dd>')
rep('          <dt>Origen</dt>', '          <dt>Luz</dt><dd>Tres tonos: cálida, neutra y fría. <span class="pendiente">[POR CONFIRMAR: bombillo, potencia y voltaje]</span></dd>\n          <dt>Origen</dt>')
rep('<summary>¿Se puede usar con agua y flores naturales?</summary>', '<summary>¿Incluye el bombillo?</summary>')
rep('<details class="faq"><summary>¿Incluye las flores de la foto?</summary><p>No. Las flores se venden por separado en Flores artificiales.</p></details>',
    '<details class="faq"><summary>¿Cómo se cambia el tono de la luz?</summary><p><span class="pendiente">[POR CONFIRMAR con el proveedor]</span></p></details>')
rep('Las dos asas y el cuello estrecho recuerdan la silueta de los recipientes antiguos de dos asas. Es una pieza nueva, inspirada en esa forma.',
    'La base toma la silueta de un jarrón y la pantalla abre la luz hacia abajo, sobre la mesa.')
rep('Puede ser el primer jarrón de una casa que apenas empieza.', 'Puede ser la luz que se enciende cuando llega visita.')

rep('\n/* Esqueletos', r'''
/* Luz de la lámpara: interruptor y tono. En producción cada estado es una foto real con el mismo encuadre. */
.barra-luz{display:flex;flex-wrap:wrap;align-items:center;gap:var(--s2) var(--s5);padding:var(--s3) var(--s4) 0}
.interruptor{display:flex;align-items:center;gap:var(--s3)}
.interruptor button{position:relative;width:56px;height:44px;padding:0;background:none;border:0;cursor:pointer}
.interruptor button::before{content:"";position:absolute;left:0;top:7px;width:56px;height:30px;border-radius:15px;border:1.5px solid var(--tinta);background:var(--hueso);transition:background-color 300ms var(--curva)}
.interruptor .perilla{position:absolute;left:5px;top:12px;width:20px;height:20px;border-radius:50%;background:var(--tinta);transition:translate 300ms var(--curva),background-color 300ms var(--curva)}
.interruptor button[aria-checked=true]::before{background:var(--tinta)}
.interruptor button[aria-checked=true] .perilla{translate:26px 0;background:#F4D9A0}
#estado-luz{min-width:8ch;color:var(--cafe-humo)}
.tonos{display:flex;align-items:center;flex-wrap:wrap;gap:var(--s2) var(--s3);border:0;padding:0;margin:0;min-width:0}
.tonos:not([hidden]){animation:aparecer-tono 250ms var(--curva)}
@keyframes aparecer-tono{from{opacity:0;translate:-6px 0}}
@media (prefers-reduced-motion:reduce){.tonos:not([hidden]){animation:none}}
.tonos legend{float:left;padding:0;margin:0 var(--s3) 0 0;font-weight:400}
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
.fotos li.luz-foto{position:relative;display:block;padding:0;background:#DAD3C9}
.escena{position:absolute;inset:0;overflow:hidden}
.escena::before,.escena .halo{content:"";position:absolute;inset:0;opacity:0;transition:opacity 350ms var(--curva)}
.escena::before{background:#2A1D16}
.escena .halo{background:radial-gradient(circle at var(--lx,50%) var(--ly,45%),color-mix(in srgb,var(--tono) 92%,transparent) 0,color-mix(in srgb,var(--tono) 40%,transparent) 26%,transparent 64%)}
.escena svg{position:absolute;inset:0;width:100%;height:100%}
.escena .pantalla{fill:#EDE7DE;stroke:#B9AFA3;stroke-width:1;transition:fill 350ms var(--curva),filter 350ms var(--curva),stroke 350ms var(--curva)}
.escena .metal{fill:#3B2A20}.escena .ceramica{fill:#F1EEE8;stroke:#B9AFA3}.escena .mesa{fill:#C9BFB2}
.luces[data-luz=on] .escena::before{opacity:.5;transition-duration:700ms}
.luces[data-luz=on] .halo{opacity:1;transition-duration:700ms}
.luces[data-luz=on] .pantalla{fill:var(--nucleo);stroke:var(--tono);filter:drop-shadow(0 0 9px var(--tono));transition-duration:700ms}
.luz-foto small{position:absolute;left:0;right:0;top:var(--s3);padding:0 var(--s4);text-align:center;font-size:.75rem;transition:color 350ms var(--curva)}
.luces[data-luz=on] .luz-foto small{color:var(--hueso)}
@media (min-width:640px){.barra-luz{padding-left:0;padding-right:0}}
@media (prefers-reduced-motion:reduce){.escena::before,.escena .halo,.escena .pantalla,.luz-foto small{transition:none!important}}

/* Esqueletos''')

rep('</script>\n</body>', r'''
/* Luz de la lámpara: encender, apagar y elegir entre sus tres tonos */
{
  const llave = $('luz'), TONOS = { calida: 'cálida', neutra: 'neutra', fria: 'fría' };
  const poner = (on, decir = true) => {
    fotos.dataset.luz = on ? 'on' : 'off'; llave.setAttribute('aria-checked', on);
    $('estado-luz').textContent = on ? 'Encendida' : 'Apagada';
    // El tono solo se elige con la luz encendida, y solo en lámparas de dos o tres tonos
    const tres = (document.querySelector('.luz-foto').dataset.tonos || '').split(' ').length > 1; // dos o tres tonos
    document.querySelector('.tonos').hidden = !(on && tres);
    if (fotoActual() !== 0) irA(0); // la luz se ve en la primera foto
    if (decir) anunciar(on ? `Lámpara encendida, luz ${TONOS[fotos.dataset.tono]}${tres ? '. Ya puede elegir el tono.' : ''}` : 'Lámpara apagada');
    track('luz_lampara', { encendida: on, tono: fotos.dataset.tono });
  };
  llave.addEventListener('click', () => poner(llave.getAttribute('aria-checked') !== 'true'));
  document.querySelector('.tonos').addEventListener('change', e => { fotos.dataset.tono = e.target.value; poner(true, false); anunciar(`Luz ${TONOS[e.target.value]}`); });
}
</script>
</body>''')
s = s[:s.rindex('</body>')] + _SITIO_JS + s[s.rindex('</body>'):]
io.open(os.path.join(proto, 'ficha-lampara.html'), 'w', encoding='utf-8', newline='\n').write(s)
print('ficha de lámpara lista')

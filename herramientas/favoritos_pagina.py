# Mis favoritos y avisos de llegada (favoritos.html). Se ejecuta al final de paginas_mas.py, dentro de construir_paginas.py:
# usa tarjeta, REG, nueva, migas, INI, pesos_cat y CORAZON_SITIO.
# Todas las piezas van en la página, ocultas; se muestran las que la persona guardó (hqh-favoritos) y, en «Avisos de
# llegada», las agotadas que pidió (hqh-avisos). [PROTOTIPO] En producción vienen de la cuenta o del navegador.
_FAV_TARJETAS = tarjeta('Jarrón de cerámica blanca con asas', 'Cerámica · Hecho en China', '$189.900', sello=True,
                        datos=' data-url="ficha-producto.html" hidden', href='ficha-producto.html', dibujo=('anfora', '#F1EEE8'))
_FAV_TARJETAS += ''.join(tarjeta(r['nombre'], r['material'] + (' · ' + r['origen'] if r['origen'] else ''), pesos_cat(r['precio']),
                                 sello=r['sello'], agotado=r['agotado'], datos=' data-url="%s" hidden' % a, href=a, dibujo=r['dibujo'])
                         for a, r in sorted(REG.items()))
_CORAZON = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">' + CORAZON_SITIO + '</svg>'

FAVORITOS = migas(INI, ('Mis favoritos', '')) + '''
  <style>
  .fav-cab{margin-top:var(--s4)}
  .fav-cab h1{font-size:2.5rem;line-height:1.1}
  .fav-cab p{margin-top:var(--s2);color:var(--cafe-humo);max-width:60ch}
  .fav-sec{margin-top:var(--s7)}
  .fav-sec h2{font-size:1.75rem;line-height:1.2}
  .fav-sec h2 span{font:400 1rem/1 var(--texto);color:var(--cafe-humo)}
  .fav-sec>p{margin:var(--s2) 0 var(--s4);color:var(--cafe-humo)}
  .fav-sec .vacio{padding:var(--s5);background:var(--suave);border-radius:6px;color:var(--tinta)}
  .lista-avisos{list-style:none;margin:0;padding:0;display:grid;gap:var(--s3)}
  .lista-avisos li{display:grid;grid-template-columns:72px 1fr;gap:var(--s2) var(--s4);align-items:center;padding:var(--s3);border:1px solid var(--perla);border-radius:6px;background:#fff}
  .aviso-mini{display:grid;place-items:center;width:72px;height:72px;border-radius:4px;background:var(--suave);overflow:hidden}
  .aviso-mini .arte{width:auto;height:64px}
  .aviso-nombre{font:600 1.25rem/1.2 var(--titulo)}
  .lista-avisos p{margin-top:var(--s1);color:var(--cafe-humo)}
  .lista-avisos .boton{grid-column:1/-1;justify-self:start;border-width:2px}
  @media (min-width:640px){.lista-avisos li{grid-template-columns:72px 1fr auto}.lista-avisos .boton{grid-column:auto}}
  </style>
  <header class="fav-cab">
    <h1>Mis favoritos</h1>
    <p><span id="fav-donde">Se guardan en este dispositivo.</span> <a href="cuenta.html" id="fav-ingresar">Ingrese a su cuenta</a></p>
  </header>
  <section class="fav-sec" aria-labelledby="h-fav">
    <h2 id="h-fav">Piezas guardadas <span id="n-fav"></span></h2>
    <p>Toque el corazón de una pieza para guardarla aquí, y otra vez para quitarla.</p>
    <p class="vacio" id="fav-vacio">Todavía no tiene piezas guardadas. <a href="lo-nuevo.html">Ver lo nuevo</a> · <a href="tienda.html">Ver toda la tienda</a></p>
    <ul class="rejilla" id="lista-fav">
''' + _FAV_TARJETAS + '''    </ul>
  </section>
  <section class="fav-sec" id="avisos" aria-labelledby="h-avisos">
    <h2 id="h-avisos">Avisos de llegada <span id="n-avisos"></span></h2>
    <p>Piezas agotadas que nos pidió avisarle cuando vuelvan.</p>
    <p class="vacio" id="avisos-vacio">No tiene avisos. En una pieza agotada, toque «Avísenme cuando llegue».</p>
    <ul class="lista-avisos" id="lista-avisos"></ul>
  </section>'''

FAVORITOS_JS = '''<script>
/* Mis favoritos: se pintan desde el navegador y se actualizan al tocar un corazón o cancelar un aviso */
(() => {
  const S = window.hqhSitio; if (!S) return;
  const $ = id => document.getElementById(id), lista = $('lista-fav'), CORAZON = %s;
  let ses = null; try { ses = JSON.parse(localStorage.getItem('hqh-sesion')); } catch (e) {}
  if (ses) { $('fav-donde').textContent = `Se guardan en su cuenta (${ses.correo}).`; $('fav-ingresar').hidden = true; }
  else $('fav-ingresar').textContent = 'Ingrese a su cuenta para verlos en cualquier lugar';
  const tarjetaDe = url => [...lista.querySelectorAll('li[data-url]')].find(li => li.dataset.url === url);
  function pintar() {
    const f = S.favs();
    lista.querySelectorAll('.simple').forEach(li => li.remove());
    lista.querySelectorAll('li[data-url]').forEach(li => li.hidden = true);
    f.slice().reverse().forEach(x => {   // la última guardada, primero
      let li = tarjetaDe(x.url);
      if (!li) {   // una pieza sin tarjeta aquí (por ejemplo, una lámpara): tarjeta sencilla con su nombre
        li = document.createElement('li'); li.className = 'tarjeta simple'; li.dataset.url = x.url;
        const a = document.createElement('a'), foto = document.createElement('div'), h = document.createElement('h3'), b = document.createElement('button');
        a.href = x.url; foto.className = 'foto'; foto.textContent = '[FOTO]'; h.textContent = x.nombre; a.append(foto, h);
        b.type = 'button'; b.className = 'fav'; b.dataset.fav = x.url; b.dataset.nombre = x.nombre; b.setAttribute('aria-pressed', 'true');
        b.setAttribute('aria-label', `Guardar ${x.nombre} en favoritos`); b.innerHTML = CORAZON;
        li.append(a, b);
      }
      li.hidden = false; lista.append(li);
    });
    $('n-fav').textContent = f.length ? `(${f.length})` : '';
    $('fav-vacio').hidden = f.length > 0;
    const av = S.avisos(), ul = $('lista-avisos');
    ul.replaceChildren(...av.map(x => {
      const li = document.createElement('li'), mini = document.createElement('a'), txt = document.createElement('div'),
            a = document.createElement('a'), d = document.createElement('p'), b = document.createElement('button');
      mini.href = x.url; mini.className = 'aviso-mini'; mini.tabIndex = -1; mini.setAttribute('aria-hidden', 'true');
      const arte = tarjetaDe(x.url)?.querySelector('.arte'); if (arte) mini.append(arte.cloneNode(true));
      a.href = x.url; a.className = 'aviso-nombre'; a.textContent = x.pieza;
      d.textContent = `Agotada. Le avisaremos a ${x.correo} cuando vuelva · desde ${x.fecha}`;
      b.type = 'button'; b.className = 'boton secundario'; b.textContent = 'Cancelar el aviso';
      b.addEventListener('click', () => { S.guardarAvisos(S.avisos().filter(y => y.url !== x.url)); S.pintarFavoritos(); if (window.anunciar) anunciar(`Canceló el aviso de ${x.pieza}.`); });
      txt.append(a, d); li.append(mini, txt, b); return li;
    }));
    $('n-avisos').textContent = av.length ? `(${av.length})` : '';
    $('avisos-vacio').hidden = av.length > 0;
  }
  document.addEventListener('hqh:favoritos', pintar);
  pintar();
})();
</script>
''' % repr(_CORAZON)

nueva('favoritos.html', 'Mis favoritos', 'Las piezas que guardó y las agotadas que le avisaremos cuando vuelvan.', FAVORITOS, guion=FAVORITOS_JS)

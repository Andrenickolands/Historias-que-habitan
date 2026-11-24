# Piezas protagonistas, guías de Historias, Mi cuenta y página de error.
# Se ejecuta al final de paginas_cat.py: usa coleccion_pag, nueva, migas, tarjeta, INI, P, CH, PA.

# ---------------------------------------------------------------- Piezas protagonistas (la sugiere el cuestionario)
coleccion_pag('coleccion-protagonistas.html', 'Piezas protagonistas', 'tinta',
              'Las piezas de mayor presencia del catálogo: las que se ven al entrar a una sala, una oficina o una recepción. ' + P % '[POR CONFIRMAR: nombre de la sección]',
              [('[Jarrón alto de porcelana]', 'Porcelana · ' + CH, '$319.900', ('alto', '#F4F2EE')),
               ('[Ánfora decorativa de cerámica]', 'Cerámica · ' + CH, '$259.900', ('anfora', '#D9C7AE'), {'agotado': True}),
               ('[Escultura curva café]', 'Cerámica · ' + CH, '$179.900', ('escultura', '#5B4632'), {'sello': True}),
               ('[Ramo alto con florero]', 'Tela y vidrio · ' + CH, '$119.900', ('flores', '#E8E2D8', True))],
              '[GUÍA PENDIENTE] Cómo elegir una pieza que se note',
              [('La mesa que recibe', 'coleccion.html'), ('Primer hogar', 'coleccion-primer-hogar.html')])


# ---------------------------------------------------------------- Guías de Historias
def guia(archivo, titulo, tipo, piezas, coleccion):
    tarjetas = ''.join(tarjeta(p[0], p[1], p[2], dibujo=p[3]) for p in piezas)
    cuerpo = migas(INI, ('Historias', 'historias.html'), (titulo, '')) + '''
  <article class="doc">
    <header class="intro"><span class="tipo">%s</span><h1>[GUÍA PENDIENTE] %s</h1>
      <p class="firma">Por [Autora, con su cargo] · Publicada el [fecha] · Actualizada el [fecha]</p></header>
    <div class="caja"><p><strong>En corto:</strong> %s</p></div>
    <h2>[Subtítulo pendiente]</h2>
    <p>%s</p>
    <h2>Lo que se sabe</h2>
    <div class="caja"><p><strong>Hecho.</strong> %s</p><p class="firma">Fuente: %s</p></div>
    <p><strong>Nuestra lectura.</strong> %s</p>
    <h2>Piezas de esta guía</h2>
  </article>
  <ul class="rejilla estanteria">
%s  </ul>
  <p style="margin-top:var(--s6)"><a class="boton secundario" href="%s">Ver la colección %s</a></p>
  <p class="firma" style="max-width:68ch;margin-top:var(--s5)">Esta guía es contenido de Historias que Habitan y recomienda piezas de nuestra tienda.</p>''' % (
        tipo, titulo, P % '[RESPUESTA EN DOS O TRES FRASES: lo escribe el agente de contenido]', P % '[TEXTO PENDIENTE]',
        P % '[HECHO PENDIENTE: solo se publica con fuente verificada]', P % '[ENLACE A LA FUENTE]',
        P % '[INTERPRETACIÓN PENDIENTE, presentada como interpretación]', tarjetas, coleccion[1], coleccion[0])
    nueva(archivo, titulo, titulo + '. Guía de Historias que Habitan.', cuerpo)


guia('historia-pesebre.html', 'El pesebre en casa', 'Costumbres',
     [('[Ave de porcelana blanca]', 'Porcelana · ' + CH, '$89.900', ('figura', '#F4F2EE')),
      ('[Figura de porcelana rosa]', 'Porcelana · ' + PA, '$129.900', ('figura', '#E7C3BB'))],
     ('Regalos que se guardan', 'coleccion-regalos.html'))
guia('historia-anfora.html', 'La forma del ánfora en el jarrón de hoy', 'Origen',
     [('[Ánfora decorativa de cerámica]', 'Cerámica · ' + CH, '$259.900', ('anfora', '#D9C7AE')),
      ('[Jarrón alto de porcelana]', 'Porcelana · ' + CH, '$319.900', ('alto', '#F4F2EE'))],
     ('Piezas protagonistas', 'coleccion-protagonistas.html'))
guia('historia-primer-jarron.html', 'El primer jarrón de una casa', 'Por comenzar',
     [('[Jarrón de vidrio ámbar]', 'Vidrio · ' + CH, '$129.900', ('panza', '#B8752A', True)),
      ('[Ramo de flores rosa y champaña]', 'Tela · ' + CH, '$49.900', ('flores', '#DDE6E8', True))],
     ('Primer hogar', 'coleccion-primer-hogar.html'))

# ---------------------------------------------------------------- Mi cuenta (opcional: se crea después de comprar)
CUENTA = migas(INI, ('Mi cuenta', '')) + '''
  <article class="doc">
    <header class="intro"><h1>Mi cuenta</h1><p>No necesita cuenta para comprar. Si la creó después de una compra, ingrese con su correo: le enviamos un enlace y no tiene que recordar ninguna contraseña.</p></header>
    <section id="ingreso" aria-labelledby="t-ingreso">
      <h2 id="t-ingreso" class="oculto-visual">Ingresar</h2>
      <form id="form-ingreso" novalidate style="margin-top:var(--s5)">
        <div class="campo"><label for="correo">Correo electrónico</label>
          <input id="correo" name="correo" type="email" autocomplete="email" spellcheck="false" autocapitalize="off" aria-describedby="e-correo"><p class="error" id="e-correo" role="alert"></p></div>
        <button class="boton" type="submit">Enviarme el enlace para ingresar</button>
      </form>
      <div class="caja bien" id="enviado" hidden tabindex="-1"><p><strong>Revise su correo.</strong></p><p>Enviamos a <span id="enviado-a"></span> un enlace para ingresar. Vence en 15 minutos. ''' + P % '[PROTOTIPO: no se envía nada]' + '''</p>
        <p><button class="enlace" type="button" id="reenviar">Reenviar el enlace</button> · <button class="enlace" type="button" id="otro-correo">Usar otro correo</button></p></div>
      <p class="firma" style="margin-top:var(--s5)"><button class="enlace" type="button" id="demo">Prototipo: ver la cuenta como si ya hubiera ingresado</button></p>
    </section>
    <section id="panel" hidden aria-labelledby="t-panel" tabindex="-1">
      <h2 id="t-panel">Hola, [Nombre]</h2>
      <h3>Mis pedidos</h3>
      <ul class="resultados">
        <li><a href="seguimiento.html"><strong>Pedido HQH-0001</strong><b>$251.800</b><span>[fecha] · En camino · 2 piezas</span></a></li>
        <li><a href="seguimiento.html"><strong>Pedido HQH-0000</strong><b>$129.900</b><span>[fecha] · Entregado · 1 pieza</span></a></li>
      </ul>
      <p class="firma">''' + P % '[EJEMPLO: en producción vienen de la plataforma]' + '''</p>
      <h3>Mis datos de envío</h3>
      <div class="caja"><p id="datos-envio">[Nombre] · [Celular]<br>[Dirección, datos complementarios, barrio o conjunto]<br>[Ciudad], Colombia</p><p><button class="enlace" type="button" data-proto>Cambiar los datos de envío</button></p></div>
      <h3>Mis favoritos</h3>
      <p>Las piezas que guarde con el corazón, y las agotadas que le avisaremos, están en <a href="favoritos.html">Mis favoritos</a>.</p>
      <h3>Avisos de llegada</h3>
      <p id="sin-avisos">Cuando una pieza esté agotada, toque «Avisarme cuando llegue» en su ficha y aparecerá aquí.</p>
      <ul class="resultados" id="mis-avisos"></ul>
      <h3>Mis comunicaciones</h3>
      <label class="casilla"><input type="checkbox" id="novedades"><span>Quiero recibir novedades por WhatsApp o correo</span></label>
      <p style="display:flex;flex-wrap:wrap;gap:var(--s3) var(--s5);margin-top:var(--s5)"><button class="boton secundario" type="button" id="salir">Cerrar sesión</button><button class="enlace" type="button" data-proto>Eliminar mi cuenta</button></p>
      <p class="firma">Eliminar la cuenta borra sus datos guardados; los pedidos ya hechos se conservan por obligación legal. ''' + P % '[POR CONFIRMAR con un abogado]' + '''</p>
    </section>
  </article>'''

GUION_CUENTA = r'''<script>
const $ = id => document.getElementById(id);
const valido = v => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim());
$('form-ingreso').addEventListener('submit', e => {
  e.preventDefault(); const c = $('correo');
  if (!valido(c.value)) { $('e-correo').textContent = 'Escriba un correo como nombre@ejemplo.com.'; c.setAttribute('aria-invalid', 'true'); return c.focus(); }
  $('e-correo').textContent = ''; c.setAttribute('aria-invalid', 'false');
  $('enviado-a').textContent = c.value.trim(); e.target.hidden = true; $('enviado').hidden = false; $('enviado').focus(); track('pedir_enlace_ingreso');
});
$('reenviar').onclick = () => anunciar('Enviamos otro enlace.');
$('otro-correo').onclick = () => { $('enviado').hidden = true; $('form-ingreso').hidden = false; $('correo').focus(); };
/* [PROTOTIPO] La sesión de ejemplo se guarda en el navegador para que la ficha de una pieza agotada ofrezca el aviso en un toque */
// [EJEMPLO] Datos ficticios de una cuenta; en producción vienen de la plataforma
const SESION = { correo: 'cliente@ejemplo.co', nombre: 'Cliente Ejemplo', celular: '3001234567', direccion: 'Calle 10 # 43-20', complemento: 'Apto 502', barrio: 'El Poblado', ciudad: 'Medellín' };
function pintarAvisos() {
  let a = []; try { a = JSON.parse(localStorage.getItem('hqh-avisos')) || []; } catch (e) {}
  $('sin-avisos').hidden = a.length > 0;
  $('mis-avisos').replaceChildren(...a.map(x => { const li = document.createElement('li'), l = document.createElement('a'), n = document.createElement('strong'), d = document.createElement('span');
    l.href = x.url; n.textContent = x.pieza; d.textContent = `Le avisaremos a ${x.correo} cuando vuelva · desde ${x.fecha}`; l.append(n, d); li.append(l); return li; }));
}
function pintarDatos() {
  let s = null; try { s = JSON.parse(localStorage.getItem('hqh-sesion')); } catch (e) {}
  if (!s || !s.ciudad) return;
  const lineas = [`${s.nombre} · ${s.celular.replace(/(\d{3})(\d{3})(\d{4})/, '$1 $2 $3')}`, [s.direccion, s.complemento, s.barrio].filter(Boolean).join(', '), `${s.ciudad}, Colombia`];
  $('datos-envio').replaceChildren(...lineas.flatMap((t, i) => i ? [document.createElement('br'), t] : [t]));
}
function abrirPanel() { $('ingreso').hidden = true; $('panel').hidden = false; pintarAvisos(); pintarDatos(); }
$('demo').onclick = () => { try { localStorage.setItem('hqh-sesion', JSON.stringify(SESION)); } catch (e) {} document.dispatchEvent(new Event('hqh:sesion')); abrirPanel(); $('panel').focus(); };
try { if (localStorage.getItem('hqh-sesion')) abrirPanel(); } catch (e) {}
$('salir').onclick = () => { try { localStorage.removeItem('hqh-sesion'); } catch (e) {} document.dispatchEvent(new Event('hqh:sesion')); $('panel').hidden = true; $('ingreso').hidden = false; $('enviado').hidden = true; $('form-ingreso').hidden = false; anunciar('Cerró la sesión'); };
$('novedades').onchange = e => anunciar(e.target.checked ? 'Recibirá novedades' : 'No recibirá novedades');
</script>
'''
nueva('cuenta.html', 'Mi cuenta', 'Ingrese con su correo para ver sus pedidos y sus datos de envío.', CUENTA, guion=GUION_CUENTA)

# ---------------------------------------------------------------- Página no encontrada
nueva('404.html', 'Página no encontrada', 'La página que busca no existe o cambió de dirección.', '''
  <article class="doc" style="padding-top:var(--s7)">
    <header class="intro"><h1>No encontramos esta página</h1><p>Puede que la dirección haya cambiado o que la pieza ya no esté en la tienda.</p></header>
    <form class="buscador" action="buscar.html" role="search">
      <label class="oculto-visual" for="b404">Buscar en la tienda</label>
      <input id="b404" name="q" type="search" autocomplete="off" enterkeyhint="search" placeholder="Jarrón, vajilla, lámpara…">
      <button class="boton" type="submit">Buscar</button>
    </form>
    <p style="margin-top:var(--s5)"><a class="enlace" href="inicio-estructura.html">Ir al inicio</a> · <a class="enlace" href="colecciones.html">Ver las colecciones</a> · <a class="enlace" href="#" data-wa>Escribirnos por WhatsApp</a></p>
  </article>''')


# Mis favoritos y avisos de llegada: página propia
exec(io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else '.', 'favoritos_pagina.py'), encoding='utf-8').read())

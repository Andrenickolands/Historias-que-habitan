# Páginas adicionales. Se ejecuta dentro de construir_paginas.py: usa pagina(), tarjeta(), CSS_CAT, dest, io y EXTRA.

CSS_DOC = CSS_CAT + r'''
.doc{max-width:68ch;padding-bottom:var(--s5)}
.doc h2{font-size:1.75rem;line-height:1.2;margin:var(--s6) 0 var(--s3)}
.doc h3{font-size:1.375rem;line-height:1.25;margin:var(--s5) 0 var(--s2)}
.doc p{margin-bottom:var(--s3)}
.doc ul,.doc ol{padding-left:var(--s5);margin:0 0 var(--s4)}
.doc li{margin-bottom:var(--s2)}
.firma{font-size:.875rem;color:var(--cafe-humo);margin-top:var(--s2)}
.frase{font:italic 500 1.5rem/1.25 var(--titulo);margin:var(--s5) 0;padding:var(--s4) 0;border-top:1px solid var(--perla);border-bottom:1px solid var(--perla);max-width:30ch}
.caja{background:var(--suave);border-radius:6px;padding:var(--s5);margin:var(--s5) 0;max-width:68ch}
.caja>:last-child{margin-bottom:0}
.caja.bien{background:#E6EEE7;color:#3F6B4E}
.campo{margin-bottom:var(--s5);max-width:480px}
.campo label,.grupo legend{display:block;font-weight:500;margin-bottom:var(--s1);padding:0}
.campo input,.campo select,.campo textarea{width:100%;min-height:48px;padding:var(--s3) var(--s4);font:inherit;color:var(--tinta);background:#fff;border:1px solid var(--cafe-humo);border-radius:2px}
.campo textarea{min-height:120px;resize:vertical}
.campo input[type=file]{padding:var(--s2)}
.campo [aria-invalid=true]{border-color:var(--error);box-shadow:inset 0 0 0 1px var(--error)}
.ayuda-campo{display:block;color:var(--cafe-humo);font-size:.875rem;margin-bottom:var(--s2)}
.error{color:var(--error);background:var(--error-fondo);padding:var(--s2) var(--s3);margin:var(--s2) 0 0;border-radius:2px;font-size:.9375rem}
.error:empty{display:none}
fieldset.grupo{border:0;padding:0;margin:0 0 var(--s5);min-width:0}
.pasos-lista{counter-reset:paso;list-style:none;padding:0;margin:var(--s4) 0 var(--s5);max-width:68ch}
.pasos-lista li{counter-increment:paso;display:grid;grid-template-columns:36px 1fr;gap:var(--s3);padding:var(--s4) 0;border-top:1px solid var(--perla);margin:0}
.pasos-lista li::before{content:counter(paso);width:36px;height:36px;border:1px solid var(--tinta);border-radius:50%;display:grid;place-content:center;font-variant-numeric:tabular-nums}
.pasos-lista strong{display:block;font-weight:500}
.ruta{list-style:none;padding:0;margin:var(--s4) 0}
.ruta li{display:grid;grid-template-columns:28px 1fr;gap:var(--s3);padding-bottom:var(--s4);position:relative;margin:0}
.ruta li::before{content:"";width:18px;height:18px;margin:3px 5px 0;border-radius:50%;border:1.5px solid var(--cafe-humo);background:var(--hueso);position:relative;z-index:1}
.ruta li.hecho::before{background:var(--tinta);border-color:var(--tinta)}
.ruta li+li::after{content:"";position:absolute;left:13.5px;top:-100%;bottom:calc(100% - 4px);width:1.5px;background:var(--cafe-humo);height:100%}
.ruta strong{display:block;font-weight:500}
.ruta span{color:var(--cafe-humo);font-size:.9375rem}
.banda-col{background:var(--borgona);color:var(--hueso);margin:0 calc(var(--s4) * -1);padding:var(--s6) var(--s4)}
.banda-col h1{font-size:2.5rem;line-height:1.05;color:var(--champagne)}
.banda-col p{margin-top:var(--s3);max-width:52ch}
.banda-col .pendiente{margin-top:var(--s2)}
.guias{list-style:none;margin:0;padding:0;border-top:1px solid var(--tinta);max-width:800px}
.guias li{border-bottom:1px solid var(--perla)}
.guias a{display:block;padding:var(--s4) 0;text-decoration:none}
.guias h2,.guias h3{font-size:1.5rem;line-height:1.2;margin:0}
.guias a:hover :is(h2,h3){text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px}
.guias p{font-size:.875rem;color:var(--cafe-humo);margin-top:var(--s1)}
.tipo{display:inline-block;font-size:.8125rem;border:1px solid var(--cafe-humo);border-radius:999px;padding:1px var(--s2);margin-bottom:var(--s2)}
.buscador{display:flex;gap:var(--s2);max-width:640px;margin-top:var(--s4)}
.buscador input{flex:1;min-width:0;min-height:52px;padding:0 var(--s4);font:inherit;font-size:1.125rem;color:var(--tinta);background:#fff;border:1px solid var(--cafe-humo);border-radius:2px}
.sugerencias{list-style:none;margin:var(--s2) 0 0;padding:0;max-width:640px;border:1px solid var(--perla);border-radius:6px;background:#fff}
.sugerencias:empty{display:none}
.sugerencias a{display:flex;justify-content:space-between;gap:var(--s3);min-height:48px;align-items:center;padding:0 var(--s4);text-decoration:none;border-top:1px solid var(--perla)}
.sugerencias li:first-child a{border-top:0}
.sugerencias a:hover{background:var(--suave)}
.sugerencias span:last-child{color:var(--cafe-humo);font-size:.875rem}
.resultados{list-style:none;margin:var(--s4) 0 0;padding:0;border-top:1px solid var(--tinta);max-width:800px}
.resultados a{display:grid;grid-template-columns:1fr auto;gap:var(--s1) var(--s4);padding:var(--s4) 0;border-bottom:1px solid var(--perla);text-decoration:none}
.resultados strong{font:600 1.25rem/1.2 var(--titulo)}
.resultados span{font-size:.875rem;color:var(--cafe-humo)}
.resultados b{font-weight:500;font-variant-numeric:tabular-nums}
.carro{list-style:none;margin:0;padding:0;border-top:1px solid var(--tinta);max-width:800px}
.carro li{display:grid;grid-template-columns:64px 1fr auto;grid-template-areas:"foto info quitar" "foto pie pie";gap:var(--s1) var(--s3);padding:var(--s4) 0;border-bottom:1px solid var(--perla);transition:opacity 200ms var(--curva)}
.carro li.sale{opacity:0}
.carro .mini{grid-area:foto;aspect-ratio:4/5;background:var(--perla)}
.carro .info{grid-area:info;min-width:0}
.carro .info strong{display:block;font-weight:500}
.carro .info span{font-size:.875rem;color:var(--cafe-humo)}
.carro [data-quitar]{grid-area:quitar;color:var(--cafe-humo)}
.carro .pie-linea{grid-area:pie;display:flex;align-items:center;justify-content:space-between;gap:var(--s3)}
.paso-cant{display:inline-flex;align-items:center;border:1px solid var(--cafe-humo);border-radius:2px}
.paso-cant button{width:44px;height:44px;display:grid;place-content:center;background:none;border:0;color:var(--tinta);cursor:pointer}
.paso-cant button:hover{background:var(--suave)}
.paso-cant button:disabled{color:var(--piedra);cursor:default;background:none}
.paso-cant span{min-width:28px;text-align:center}
.carro b{font-weight:500;font-variant-numeric:tabular-nums}
.resumen-carro{max-width:800px;display:grid;gap:var(--s3);padding-top:var(--s4)}
.resumen-carro .fila{display:flex;justify-content:space-between;align-items:baseline;gap:var(--s3)}
.resumen-carro .fila strong{font-weight:500;font-size:1.375rem;font-variant-numeric:tabular-nums}
.gratis progress{display:block;width:100%;height:10px;appearance:none;-webkit-appearance:none;border:1px solid var(--cafe-humo);border-radius:5px;background:var(--hueso);overflow:hidden;margin-top:var(--s2)}
.gratis progress::-webkit-progress-bar{background:var(--hueso)}
.gratis progress::-webkit-progress-value{background:var(--tinta)}
.gratis progress::-moz-progress-bar{background:var(--tinta)}
.casilla{display:flex;align-items:flex-start;gap:var(--s3);min-height:44px;cursor:pointer}
@media (min-width:640px){.banda-col{margin:0;padding:var(--s7) var(--s6)}.banda-col h1{font-size:3.25rem}}
'''


def migas(*pares):
    li = ''.join('<li><a href="%s">%s</a></li>' % (u, n) for n, u in pares[:-1])
    return '<nav class="migas" aria-label="Ruta de navegación"><ol>%s<li><span aria-current="page">%s</span></li></ol></nav>' % (li, pares[-1][0])


def nueva(archivo, titulo, descripcion, cuerpo, guion=''):
    io.open(dest + '/' + archivo, 'w', encoding='utf-8', newline='\n').write(
        pagina(titulo + ' · Historias que Habitan', descripcion, CSS_DOC, '<main id="contenido" class="ancho">\n' + cuerpo + '\n</main>\n', guion=guion))
    EXTRA.append(archivo)


INI = ('Inicio', 'inicio-estructura.html')  # el inicio aprobado; inicio.html queda como el diseño anterior
P = '<span class="pendiente">%s</span>'

# ---------------------------------------------------------------- Colección
nueva('coleccion.html', 'La mesa que recibe', 'Vajillas, cristalería y centros de mesa para recibir en casa.',
      migas(INI, ('Colecciones', '/colecciones'), ('La mesa que recibe', '')) + '''
  <header class="banda-col">
    <h1>La mesa que recibe</h1>
    <p>Vajillas, cristalería y centros de mesa que funcionan juntos, para vestir la mesa con pocas piezas cuando llega visita.</p>
    ''' + P % '[TEXTO DE EJEMPLO]' + '''
  </header>
  <div class="estado-lista" style="padding-top:var(--s5)"><p>4 piezas</p></div>
  <h2 class="oculto-visual">Piezas de la colección</h2>
  <ul class="rejilla estanteria">
''' + tarjeta('[Recipiente con tapa de cerámica]', 'Cerámica · Hecho en China', '$99.900', dibujo=('tarro', '#F4F2EE'))
      + tarjeta('[Florero de vidrio transparente]', 'Vidrio · Hecho en China', '$69.900', dibujo=('florero', '#DDE6E8', True))
      + tarjeta('[Juego de 6 copas de vino]', 'Vidrio · Hecho en China', '$149.900', dibujo=('copa', '#DDE6E8', True))
      + tarjeta('[Vajilla de 16 piezas blanca]', 'Porcelana · Hecho en China', '$389.900', dibujo=('plato', '#F4F2EE')) + '''  </ul>
  <div class="texto-cat">
    <section aria-labelledby="t-guia">
      <h2 id="t-guia">La guía de esta colección</h2>
      <ul class="guias"><li><a href="historia.html"><h3>[GUÍA PENDIENTE] Cómo poner la mesa para recibir</h3><p>Guía · [Autora] · Actualizada el [fecha]</p></a></li></ul>
    </section>
    <section aria-labelledby="t-otras">
      <h2 id="t-otras">Otras colecciones</h2>
      <p><a class="enlace" href="/colecciones/primer-hogar" data-proto>Primer hogar</a></p>
      <p><a class="enlace" href="/colecciones/regalos-que-se-guardan" data-proto>Regalos que se guardan</a></p>
    </section>
  </div>''')

# ---------------------------------------------------------------- Historias
nueva('historias.html', 'Historias', 'Guías y relatos sobre los objetos de la casa y las costumbres que los acompañan.',
      migas(INI, ('Historias', '')) + '''
  <header class="intro"><h1>Historias</h1>
    <p>Guías y relatos sobre los objetos de la casa: de dónde vienen sus formas, qué costumbres los acompañan y cómo usarlos. Cada dato histórico lleva su fuente.</p></header>
  <ul class="guias" style="margin-top:var(--s5)">
    <li><a href="historia.html"><span class="tipo">Costumbres</span><h2>[GUÍA PENDIENTE] Cómo poner la mesa para recibir</h2><p>[Autora] · Actualizada el [fecha] · Lectura de [N] minutos</p></a></li>
    <li><a href="/historias/el-pesebre-en-casa" data-proto><span class="tipo">Costumbres</span><h2>[GUÍA PENDIENTE] El pesebre en casa</h2><p>[Autora] · Actualizada el [fecha]</p></a></li>
    <li><a href="/historias/la-forma-del-anfora" data-proto><span class="tipo">Origen</span><h2>[GUÍA PENDIENTE] La forma del ánfora en el jarrón de hoy</h2><p>[Autora] · Actualizada el [fecha] · ''' + P % '[Dato histórico por verificar con fuente]' + '''</p></a></li>
    <li><a href="/historias/el-primer-jarron" data-proto><span class="tipo">Por comenzar</span><h2>[GUÍA PENDIENTE] El primer jarrón de una casa</h2><p>[Autora] · Actualizada el [fecha]</p></a></li>
  </ul>
  <p class="firma" style="margin-top:var(--s5);max-width:68ch">Las guías son contenido de Historias que Habitan y recomiendan piezas de nuestra tienda.</p>''')

nueva('historia.html', 'Cómo poner la mesa para recibir', 'Guía para vestir la mesa cuando llega visita, con pocas piezas.',
      migas(INI, ('Historias', 'historias.html'), ('Cómo poner la mesa para recibir', '')) + '''
  <article class="doc">
    <header class="intro"><span class="tipo">Costumbres</span><h1>[GUÍA PENDIENTE] Cómo poner la mesa para recibir</h1>
      <p class="firma">Por [Autora, con su cargo] · Publicada el [fecha] · Actualizada el [fecha]</p></header>
    <div class="caja"><p><strong>En corto:</strong> ''' + P % '[RESPUESTA EN DOS O TRES FRASES: lo escribe el agente de contenido]' + '''</p></div>
    <h2>Qué piezas hacen falta</h2>
    <p>''' + P % '[TEXTO PENDIENTE]' + ''' Espacio para una lista corta: plato base, plato llano, copa de agua, copa de vino, servilleta y un centro de mesa.</p>
    <h2>El orden de los puestos</h2>
    <p>''' + P % '[TEXTO PENDIENTE]' + '''</p>
    <h2>De dónde viene la costumbre</h2>
    <div class="caja"><p><strong>Hecho.</strong> ''' + P % '[HECHO PENDIENTE: solo se publica con fuente verificada]' + '''</p><p class="firma">Fuente: ''' + P % '[ENLACE A LA FUENTE]' + '''</p></div>
    <p><strong>Nuestra lectura.</strong> ''' + P % '[INTERPRETACIÓN PENDIENTE, presentada como interpretación]' + '''</p>
    <h2>Piezas de esta guía</h2>
  </article>
  <ul class="rejilla estanteria">
''' + tarjeta('[Florero de vidrio transparente]', 'Vidrio · Hecho en China', '$69.900', dibujo=('florero', '#DDE6E8', True))
      + tarjeta('[Recipiente con tapa de cerámica]', 'Cerámica · Hecho en China', '$99.900', dibujo=('tarro', '#F4F2EE')) + '''  </ul>
  <p style="margin-top:var(--s6)"><a class="boton secundario" href="coleccion.html">Ver la colección La mesa que recibe</a></p>
  <p class="firma" style="max-width:68ch;margin-top:var(--s5)">Esta guía es contenido de Historias que Habitan y recomienda piezas de nuestra tienda.</p>''')

# ---------------------------------------------------------------- Nosotros
nueva('nosotros.html', 'Nosotros', 'Quiénes somos y cómo elegimos las piezas de Historias que Habitan.',
      migas(INI, ('Nosotros', '')) + '''
  <article class="doc">
    <header class="intro"><h1>Nosotros</h1></header>
    <p class="frase">Hay objetos que no solo decoran. Cuentan historias.</p>
    <p>Historias que Habitan es una tienda en línea de decoración y objetos para el hogar. Vendemos al detal y al por mayor porcelanas, jarrones, flores artificiales, vajillas, cristalería y objetos decorativos, y de cada pieza contamos lo que se sabe y lo que puede llegar a significar en una casa.</p>
    <h2>La H</h2>
    <p>La H de nuestro nombre es la de Historias, la de Habitan y la de Heredia, el apellido de quien impulsa la marca. También recuerda una puerta, una ventana o un marco: detrás de cada una puede haber una historia.</p>
    <p>''' + P % '[TEXTO PENDIENTE en primera persona, en la voz de Paula Heredia]' + '''</p>
    <h2>Cómo elegimos</h2>
    <ul><li>Miramos los acabados y los detalles de fabricación.</li><li>Buscamos piezas que combinen entre sí y que sigan gustando después de una temporada.</li><li>No prometemos que una pieza sea irrepetible ni antigua.</li></ul>
    <h2>De dónde vienen las piezas</h2>
    <p>El origen de cada pieza está en su ficha técnica, junto al material y las medidas. No lo escondemos ni lo reemplazamos por un relato.</p>
    <h2>Cómo contamos cada pieza</h2>
    <p>Separamos tres cosas: el hecho que se puede comprobar, nuestra lectura del diseño y una propuesta sobre el lugar que la pieza puede tener en su casa. No presentamos una interpretación como un hecho.</p>
    <h2>Dónde estamos</h2>
    <p>Somos una tienda 100 % en línea, sin local. Atendemos por WhatsApp y enviamos a todo el país.</p>
    <p><a class="boton secundario" href="#" data-wa>Escribirnos por WhatsApp</a></p>
    <p class="firma">''' + P % '[POR CONFIRMAR: razón social, NIT, correo y horario de atención]' + '''</p>
  </article>''')

# ---------------------------------------------------------------- Por mayor
nueva('por-mayor.html', 'Compras por mayor', 'Cotización por volumen para comercios, hoteles, restaurantes y regalos corporativos.',
      migas(INI, ('Por mayor', '')) + '''
  <article class="doc">
    <header class="intro"><h1>Compras por mayor</h1>
      <p>Cotizamos por volumen para tiendas de decoración y regalos, floristerías, eventos, hoteles, restaurantes y regalos corporativos. Le responde una persona por WhatsApp.</p></header>
    <p style="margin-top:var(--s5)"><a class="boton" href="quiz-orientacion.html">Solicitar cotización</a></p>
    <p class="firma">Son cuatro preguntas y sus datos de contacto. No necesita crear cuenta.</p>
    <h2>Cómo funciona</h2>
    <ol class="pasos-lista">
      <li><span><strong>Nos cuenta qué busca</strong>Tipo de negocio, categorías que le interesan y cada cuánto compra.</span></li>
      <li><span><strong>Le enviamos la cotización por WhatsApp</strong>Con precios por volumen y condiciones. ''' + P % '[POR CONFIRMAR: tiempo de respuesta]' + '''</span></li>
      <li><span><strong>Confirmamos el pedido y el despacho</strong>''' + P % '[POR CONFIRMAR: medios de pago y envío para mayoristas]' + '''</span></li>
    </ol>
    <h2>Condiciones</h2>
    <p>''' + P % '[POR CONFIRMAR: compra mínima, precios por volumen y plazos]' + '''</p>
    <h2>Preguntas frecuentes</h2>
    <details class="faq"><summary>¿Necesito NIT para comprar por mayor?</summary><p>''' + P % '[POR CONFIRMAR]' + '''</p></details>
    <details class="faq"><summary>¿Hacen envíos por mayor a otras ciudades?</summary><p>Sí, enviamos a todo el país. El costo depende del volumen y la ciudad.</p></details>
    <details class="faq"><summary>¿Puedo ver las piezas antes de comprar?</summary><p>No tenemos local. Le enviamos fotos y medidas de cada pieza por WhatsApp.</p></details>
  </article>''')

# ---------------------------------------------------------------- Seguimiento
nueva('seguimiento.html', 'Seguir mi pedido', 'Consulte el estado de su pedido con el número y su correo.',
      migas(INI, ('Seguir mi pedido', '')) + '''
  <article class="doc">
    <header class="intro"><h1>Seguir mi pedido</h1><p>No necesita cuenta. Escriba el número del pedido, que está en el correo de confirmación, y su correo.</p></header>
    <form id="form-seg" novalidate style="margin-top:var(--s5)">
      <div class="campo"><label for="pedido">Número de pedido</label><span class="ayuda-campo" id="a-pedido">Ejemplo: HQH-0001</span>
        <input id="pedido" name="pedido" type="text" autocomplete="off" spellcheck="false" autocapitalize="characters" aria-describedby="a-pedido e-pedido"><p class="error" id="e-pedido" role="alert"></p></div>
      <div class="campo"><label for="correo">Correo electrónico</label>
        <input id="correo" name="correo" type="email" autocomplete="email" spellcheck="false" aria-describedby="e-correo"><p class="error" id="e-correo" role="alert"></p></div>
      <button class="boton" type="submit">Consultar mi pedido</button>
    </form>
    <section id="resultado" hidden tabindex="-1" aria-labelledby="t-res">
      <h2 id="t-res">Pedido <span id="res-num"></span></h2>
      <p>''' + P % '[ESTADO DE EJEMPLO: en producción viene del operador logístico]' + '''</p>
      <ol class="ruta">
        <li class="hecho"><span><strong>Pedido recibido</strong><span>[fecha y hora]</span></span></li>
        <li class="hecho"><span><strong>Embalado</strong><span>Con protección para piezas frágiles.</span></span></li>
        <li class="hecho"><span><strong>Despachado</strong><span>Guía [N.º de guía] con [operador].</span></span></li>
        <li><span><strong>En camino</strong><span>Entrega estimada: [fecha].</span></span></li>
        <li><span><strong>Entregado</strong><span>Pendiente.</span></span></li>
      </ol>
      <p><a class="enlace" href="pieza-rota.html">¿Llegó una pieza rota? Repórtela aquí</a></p>
    </section>
  </article>''', guion=r'''<script>
document.getElementById('form-seg').addEventListener('submit', e => {
  e.preventDefault(); const f = e.target.elements;
  const errores = { pedido: f.pedido.value.trim() ? '' : 'Escriba el número de pedido. Está en el correo de confirmación.',
    correo: /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(f.correo.value.trim()) ? '' : 'Escriba un correo como nombre@ejemplo.com.' };
  let primero = null;
  for (const id in errores) { document.getElementById('e-' + id).textContent = errores[id]; f[id].setAttribute('aria-invalid', !!errores[id]); if (errores[id] && !primero) primero = f[id]; }
  if (primero) return primero.focus();
  document.getElementById('res-num').textContent = f.pedido.value.trim().toUpperCase();
  const r = document.getElementById('resultado'); r.hidden = false; r.focus(); anunciar('Estado del pedido cargado'); track('seguir_pedido');
});
</script>
''')

# ---------------------------------------------------------------- Pieza rota
nueva('pieza-rota.html', 'Reportar una pieza rota', 'Si una pieza llegó rota, repórtela con una foto y le damos solución.',
      migas(INI, ('Reportar una pieza rota', '')) + '''
  <article class="doc">
    <header class="intro"><h1>Reportar una pieza rota</h1>
      <p>Lamentamos que haya pasado. Cuéntenos qué llegó roto y adjunte una foto: con eso basta para darle solución. ''' + P % '[POR CONFIRMAR: plazo para reportar y tiempo de respuesta]' + '''</p></header>
    <form id="form-rota" novalidate style="margin-top:var(--s5)">
      <div class="campo"><label for="pedido">Número de pedido</label><span class="ayuda-campo" id="a-pedido">Está en el correo de confirmación. Ejemplo: HQH-0001</span>
        <input id="pedido" name="pedido" type="text" autocomplete="off" spellcheck="false" aria-describedby="a-pedido e-pedido"><p class="error" id="e-pedido" role="alert"></p></div>
      <div class="campo"><label for="correo">Correo o celular para responderle</label>
        <input id="correo" name="correo" type="text" autocomplete="email" aria-describedby="e-correo"><p class="error" id="e-correo" role="alert"></p></div>
      <div class="campo"><label for="que">¿Qué pieza llegó rota y qué le pasó?</label>
        <textarea id="que" name="que" aria-describedby="e-que"></textarea><p class="error" id="e-que" role="alert"></p></div>
      <div class="campo"><label for="foto">Foto de la pieza y de la caja</label><span class="ayuda-campo" id="a-foto">Puede adjuntar hasta 3 fotos. Si no puede, envíelas después por WhatsApp.</span>
        <input id="foto" name="foto" type="file" accept="image/*" multiple aria-describedby="a-foto"></div>
      <fieldset class="grupo"><legend>¿Qué prefiere?</legend>
        <label class="casilla"><input type="radio" name="solucion" value="Reposición de la pieza" checked><span>Que me envíen la pieza de nuevo</span></label>
        <label class="casilla"><input type="radio" name="solucion" value="Devolución del dinero"><span>Que me devuelvan el dinero</span></label>
        <p class="ayuda-campo">''' + P % '[POR CONFIRMAR: política de roturas]' + '''</p></fieldset>
      <button class="boton" type="submit">Enviar el reporte</button>
    </form>
    <div class="caja bien" id="listo" hidden tabindex="-1"><p><strong>Recibimos su reporte.</strong></p><p>Le respondemos a <span id="listo-contacto"></span>. No tiene que devolver la pieza para que revisemos el caso. ''' + P % '[PROTOTIPO: no se envía nada]' + '''</p></div>
    <p style="margin-top:var(--s5)"><a class="enlace" href="#" data-wa>Prefiero escribir por WhatsApp</a></p>
  </article>''', guion=r'''<script>
document.getElementById('form-rota').addEventListener('submit', e => {
  e.preventDefault(); const f = e.target.elements;
  const errores = { pedido: f.pedido.value.trim() ? '' : 'Escriba el número de pedido.', correo: f.correo.value.trim().length > 5 ? '' : 'Escriba un correo o un celular para responderle.',
    que: f.que.value.trim().length > 9 ? '' : 'Cuéntenos qué pieza llegó rota y qué le pasó.' };
  let primero = null;
  for (const id in errores) { document.getElementById('e-' + id).textContent = errores[id]; f[id].setAttribute('aria-invalid', !!errores[id]); if (errores[id] && !primero) primero = f[id]; }
  if (primero) return primero.focus();
  document.getElementById('listo-contacto').textContent = f.correo.value.trim();
  e.target.hidden = true; const l = document.getElementById('listo'); l.hidden = false; l.focus(); track('reportar_pieza_rota', { solucion: f.solucion.value });
});
</script>
''')

# ---------------------------------------------------------------- Ayuda
nueva('envios.html', 'Envíos', 'Cobertura, costos, tiempos y embalaje de los envíos de Historias que Habitan.',
      migas(INI, ('Envíos', '')) + '''
  <article class="doc">
    <header class="intro"><h1>Envíos</h1><p>Enviamos a todo el país. El costo y el tiempo se calculan con su ciudad y se muestran antes de pagar.</p></header>
    <h2>Costos y tiempos</h2><p>''' + P % '[POR CONFIRMAR: operador, tarifas por ciudad y tiempos de entrega]' + '''</p>
    <h2>Envío gratis</h2><p>''' + P % '[POR CONFIRMAR: monto mínimo y ciudades donde aplica]' + '''</p>
    <h2>Cómo embalamos las piezas frágiles</h2><p>Cada pieza viaja en caja, envuelta en papel de seda y con protección para el camino. ''' + P % '[POR CONFIRMAR: detalle del embalaje]' + '''</p>
    <h2>Si una pieza llega rota</h2><p>Repórtela con una foto y la reponemos o le devolvemos el dinero. ''' + P % '[POR CONFIRMAR: plazo y condiciones]' + '''</p>
    <p><a class="enlace" href="pieza-rota.html">Reportar una pieza rota</a></p>
    <h2>Seguimiento</h2><p>Cuando su pedido sale, le escribimos por WhatsApp con el número de guía.</p>
    <p><a class="enlace" href="seguimiento.html">Seguir mi pedido</a></p>
    <p class="firma">Actualizado el [fecha].</p>
  </article>''')

nueva('cambios-y-garantia.html', 'Cambios, garantía y retracto', 'Condiciones de cambios, garantía y derecho de retracto.',
      migas(INI, ('Cambios, garantía y retracto', '')) + '''
  <article class="doc">
    <header class="intro"><h1>Cambios, garantía y retracto</h1><p>''' + P % '[TEXTO LEGAL PENDIENTE: lo redacta y revisa un abogado en Colombia. Ley 1480 de 2011]' + '''</p></header>
    <h2>Derecho de retracto</h2><p>En las compras por internet usted puede retractarse dentro del plazo que fija la ley. ''' + P % '[POR CONFIRMAR: plazo, condiciones y cómo pedirlo]' + '''</p>
    <h2>Cambios</h2><p>''' + P % '[POR CONFIRMAR: plazo y estado de la pieza]' + '''</p>
    <h2>Garantía</h2><p>''' + P % '[POR CONFIRMAR: plazo y cobertura por tipo de pieza]' + '''</p>
    <h2>Piezas que llegan rotas</h2><p><a class="enlace" href="pieza-rota.html">Reportar una pieza rota</a></p>
    <h2>Cómo pedir un cambio o una devolución</h2><p>Escríbanos por WhatsApp con el número de su pedido.</p>
    <p><a class="boton secundario" href="#" data-wa>Escribir por WhatsApp</a></p>
    <p class="firma">Superintendencia de Industria y Comercio: <a href="https://www.sic.gov.co" rel="noopener">www.sic.gov.co</a> · Actualizado el [fecha].</p>
  </article>''')

nueva('preguntas.html', 'Preguntas frecuentes', 'Respuestas sobre envíos, pagos, piezas y cambios.',
      migas(INI, ('Preguntas frecuentes', '')) + '''
  <article class="doc">
    <header class="intro"><h1>Preguntas frecuentes</h1></header>
    <h2>Envíos</h2>
    <details class="faq"><summary>¿Hacen envíos fuera de Bogotá?</summary><p>Sí. Enviamos a todo el país. El costo y el tiempo se calculan con su ciudad antes de pagar.</p></details>
    <details class="faq"><summary>¿Cómo llegan embaladas las piezas?</summary><p>En caja, con papel de seda y protección. ''' + P % '[POR CONFIRMAR]' + '''</p></details>
    <details class="faq"><summary>¿Qué pasa si una pieza llega rota?</summary><p>La reponemos o le devolvemos el dinero. <a href="pieza-rota.html">Repórtela aquí</a>. ''' + P % '[POR CONFIRMAR: plazo]' + '''</p></details>
    <h2>Pagos</h2>
    <details class="faq"><summary>¿Qué medios de pago reciben?</summary><p>Tarjeta, PSE, Nequi y Daviplata. ''' + P % '[POR CONFIRMAR: pasarela]' + '''</p></details>
    <details class="faq"><summary>¿Tengo que crear una cuenta para comprar?</summary><p>No. Puede comprar como invitado. Si quiere, crea su cuenta al final, después de pagar.</p></details>
    <details class="faq"><summary>¿Los precios incluyen IVA?</summary><p>Sí. Todos los precios incluyen IVA.</p></details>
    <h2>Las piezas</h2>
    <details class="faq"><summary>¿De dónde vienen las piezas?</summary><p>Cada ficha técnica dice el origen de la pieza, junto al material y las medidas.</p></details>
    <details class="faq"><summary>¿Tienen tienda física?</summary><p>No. Somos una tienda en línea y atendemos por WhatsApp.</p></details>
    <details class="faq"><summary>¿Venden por mayor?</summary><p>Sí. <a href="por-mayor.html">Solicite una cotización</a>.</p></details>
  </article>''')

# ---------------------------------------------------------------- Búsqueda
nueva('buscar.html', 'Buscar', 'Busque piezas por nombre, material o categoría.',
      migas(INI, ('Buscar', '')) + '''
  <header class="intro"><h1>Buscar</h1></header>
  <form class="buscador" id="form-buscar" role="search">
    <label class="oculto-visual" for="b">Buscar en la tienda</label>
    <input id="b" name="q" type="search" autocomplete="off" enterkeyhint="search" placeholder="Jarrón, vajilla, lámpara…" aria-describedby="estado-b" aria-controls="sugerencias">
    <button class="boton" type="submit">Buscar</button>
  </form>
  <ul class="sugerencias" id="sugerencias" aria-label="Sugerencias"></ul>
  <p id="estado-b" role="status" style="margin-top:var(--s4)"></p>
  <ul class="resultados" id="resultados"></ul>
  <div class="vacio" id="sin" hidden style="margin-top:var(--s4)">
    <h2>No encontramos piezas con esa búsqueda</h2>
    <p>Revise la escritura o pruebe con una palabra más general, como «jarrón» o «vidrio».</p>
    <p><a class="enlace" href="categoria.html">Ver jarrones y recipientes</a> · <a class="enlace" href="lamparas.html">Ver lámparas</a></p>
    <a class="boton secundario" href="quiz-orientacion.html">Ayúdeme a elegir</a>
  </div>
  <p class="firma" style="margin-top:var(--s6)">''' + P % '[PROTOTIPO: busca en 14 piezas de ejemplo. En producción lo resuelve el buscador de la plataforma]' + '''</p>''', guion=r'''<script>
/* Búsqueda con sugerencias y tolerancia a errores de escritura (jarron, porselana, lampra) */
const ESTADOS = __ESTADOS__; // del catálogo único: oferta, quedan pocas, agotada
const PIEZAS = [
  ['Jarrón de cerámica blanca con asas', 'Jarrones y recipientes', 189900, 'ficha-producto.html'], ['Jarrón de vidrio ámbar', 'Jarrones y recipientes', 129900],
  ['Recipiente pequeño de cerámica', 'Jarrones y recipientes', 79900], ['Jarrón alto de porcelana', 'Jarrones y recipientes', 319900],
  ['Florero de vidrio transparente', 'Jarrones y recipientes', 69900], ['Ánfora decorativa de cerámica', 'Jarrones y recipientes', 259900],
  ['Jarrón de porcelana con relieve', 'Jarrones y recipientes', 219900], ['Recipiente con tapa de cerámica', 'Jarrones y recipientes', 99900],
  ['Lámpara de mesa con base de cerámica', 'Lámparas', 249900, 'ficha-lampara.html'], ['Colgante de vidrio en globo', 'Lámparas', 189900],
  ['Aplique doble de pared', 'Lámparas', 159900], ['Lámpara de mesa tipo hongo', 'Lámparas', 219900], ['Colgante de tres globos', 'Lámparas', 389900], ['Farol de mesa', 'Lámparas', 129900]
].map(([nombre, cat, precio, url]) => ({ nombre, cat, precio, url, ...(ESTADOS[nombre.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '')] || {}) }));
const limpio = t => t.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9 ]/g, ' ').trim();
const distancia = (a, b) => { const d = Array.from({ length: a.length + 1 }, (_, i) => [i]); for (let j = 1; j <= b.length; j++) d[0][j] = j;
  for (let i = 1; i <= a.length; i++) for (let j = 1; j <= b.length; j++) d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] !== b[j - 1])); return d[a.length][b.length]; };
const coincide = (palabra, texto) => texto.split(' ').some(t => t.startsWith(palabra) || (palabra.length > 3 && distancia(palabra, t.slice(0, Math.max(palabra.length, t.length))) <= (palabra.length > 6 ? 2 : 1)));
const buscar = q => { const ps = limpio(q).split(' ').filter(Boolean); return ps.length ? PIEZAS.filter(p => ps.every(w => coincide(w, limpio(p.nombre + ' ' + p.cat)))) : []; };
const $ = id => document.getElementById(id), pesos = n => '$' + new Intl.NumberFormat('es-CO').format(n);
const fila = (p, clase) => { const li = document.createElement('li'), a = document.createElement('a'); a.href = p.url || '/pieza/ejemplo'; if (!p.url) a.dataset.proto = '';
  if (clase) { const n = document.createElement('span'), c = document.createElement('span'); n.textContent = p.nombre; c.textContent = p.cat; a.append(n, c); }
  else { const n = document.createElement('strong'), b = document.createElement('b'), c = document.createElement('span'); n.textContent = p.nombre; b.textContent = pesos(p.precio); c.textContent = p.cat; a.append(n, b, c);
    // Mismos estados que en la tienda y la ficha
    if (p.antes && !p.agotada) { const s = document.createElement('s'), o = document.createElement('span'); s.textContent = pesos(p.antes); o.className = 'chip-estado chip-oferta'; o.textContent = `−${Math.round((1 - p.precio / p.antes) * 100)} %`; b.append(' ', s, ' ', o); }
    if (p.agotada || p.pocas) { const e = document.createElement('span'); e.className = 'chip-estado ' + (p.agotada ? 'chip-agotada' : 'chip-pocas'); e.textContent = p.agotada ? 'Agotada' : p.unidades === 1 ? 'Queda 1' : `Quedan ${p.unidades}`; c.append(' · ', e); } }
  li.append(a); return li; };
function mostrar(q) {
  const r = buscar(q); $('sugerencias').replaceChildren();
  $('resultados').replaceChildren(...r.map(p => fila(p)));
  $('sin').hidden = !q.trim() || r.length > 0;
  $('estado-b').textContent = !q.trim() ? '' : r.length ? `${r.length} ${r.length === 1 ? 'pieza' : 'piezas'} para «${q.trim()}»` : `Sin resultados para «${q.trim()}»`;
  track(r.length ? 'busqueda_interna' : 'busqueda_sin_resultados', { resultados: r.length });
  try { history.replaceState(null, '', q.trim() ? '?q=' + encodeURIComponent(q.trim()) : location.pathname); } catch (e) {}
}
$('b').addEventListener('input', e => { const r = e.target.value.trim().length > 1 ? buscar(e.target.value).slice(0, 5) : []; $('sugerencias').replaceChildren(...r.map(p => fila(p, true))); });
$('form-buscar').addEventListener('submit', e => { e.preventDefault(); mostrar($('b').value); });
const inicial = new URLSearchParams(location.search).get('q'); if (inicial) { $('b').value = inicial; mostrar(inicial); }
</script>
'''.replace('__ESTADOS__', __import__('json').dumps({k: dict(estado_pieza(k), antes=estado_pieza(k)['antes']) for k in __import__('catalogo').ESTADO}, ensure_ascii=False)))

# ---------------------------------------------------------------- Carrito completo
nueva('carrito.html', 'Su carrito', 'Revise las piezas de su carrito antes de pagar.',
      migas(INI, ('Su carrito', '')) + '''
  <header class="intro"><h1>Su carrito</h1></header>
  <div class="vacio" id="vacio" hidden style="margin-top:var(--s5)">
    <h2>Su carrito está vacío</h2><p>Puede empezar por una colección o por una categoría.</p>
    <a class="boton secundario" href="categoria.html">Ver jarrones y recipientes</a><a class="enlace" href="coleccion.html">Ver la colección La mesa que recibe</a>
  </div>
  <div id="lleno" hidden>
    <div class="gratis" style="max-width:800px;margin:var(--s5) 0 var(--s4)"><p id="envio-texto"></p><progress id="envio-barra" max="300000" value="0" aria-labelledby="envio-texto"></progress>
      <p style="margin-top:var(--s2)">''' + P % '[POR CONFIRMAR: monto real y ciudades donde aplica]' + '''</p></div>
    <ul class="carro" id="carro"></ul>
    <div class="resumen-carro">
      <p class="fila"><span>Subtotal <span id="n-piezas"></span><br><small style="color:var(--cafe-humo)">IVA incluido. El envío se calcula con su ciudad en el siguiente paso.</small></span><strong id="subtotal"></strong></p>
      <p style="font-size:.9375rem">¿Es un regalo? En el pago puede poner otro destinatario, un mensaje y el empaque. ''' + P % '[POR CONFIRMAR: si se ofrece]' + '''</p>
      <p style="display:flex;flex-wrap:wrap;gap:var(--s3) var(--s5);align-items:center"><a class="boton" href="pago.html">Ir a pagar</a><a class="enlace" href="categoria.html">Seguir mirando</a></p>
      <p class="firma">Compra como invitado: no necesita crear cuenta.</p>
    </div>
  </div>''', guion=r'''<script>
const $ = id => document.getElementById(id), pesos = n => '$' + new Intl.NumberFormat('es-CO').format(n), GRATIS = 300000;
let carro = []; try { carro = JSON.parse(localStorage.getItem('hqh-carrito')) || []; } catch (e) {}
const X = '<svg class="icono" viewBox="0 0 24 24" aria-hidden="true"><path d="m7 7 10 10M17 7 7 17"/></svg>';
function pintar() {
  try { localStorage.setItem('hqh-carrito', JSON.stringify(carro)); } catch (e) {}
  const n = carro.reduce((s, x) => s + x.cantidad, 0), sub = carro.reduce((s, x) => s + x.cantidad * x.precio, 0);
  $('vacio').hidden = n > 0; $('lleno').hidden = n === 0;
  $('subtotal').textContent = pesos(sub); $('n-piezas').textContent = `(${n} ${n === 1 ? 'pieza' : 'piezas'})`;
  $('envio-barra').value = Math.min(sub, GRATIS); $('envio-texto').textContent = sub >= GRATIS ? 'Su pedido ya tiene envío gratis.' : `Le faltan ${pesos(GRATIS - sub)} para el envío gratis.`;
  $('carro').replaceChildren(...carro.map((x, i) => { const li = document.createElement('li'); li.dataset.i = i;
    li.innerHTML = '<div class="mini"></div><div class="info"><strong></strong><span></span></div><button class="boton-icono" type="button" data-quitar>' + X + '</button>'
      + '<div class="pie-linea"><div class="paso-cant"><button type="button" data-d="-1"><svg class="icono" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 12h10"/></svg></button><span></span>'
      + '<button type="button" data-d="1"><svg class="icono" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 12h10M12 7v10"/></svg></button></div><b></b></div>';
    li.querySelector('strong').textContent = x.nombre; li.querySelector('.info span').textContent = `${x.variante ? x.variante + ' · ' : ''}${pesos(x.precio)} c/u`;
    li.querySelector('.paso-cant span').textContent = x.cantidad; li.querySelector('b').textContent = pesos(x.precio * x.cantidad);
    li.querySelector('[data-quitar]').setAttribute('aria-label', `Quitar ${x.nombre}`);
    li.querySelector('[data-d="-1"]').setAttribute('aria-label', `Quitar una unidad de ${x.nombre}`); li.querySelector('[data-d="-1"]').disabled = x.cantidad === 1;
    li.querySelector('[data-d="1"]').setAttribute('aria-label', `Agregar una unidad de ${x.nombre}`); return li; }));
  const c = document.querySelector('.cabecera [href="carrito.html"]'); if (c) c.setAttribute('aria-label', `Carrito, ${n} ${n === 1 ? 'pieza' : 'piezas'}`);
  const cont = c && c.querySelector('.contador'); if (cont) { cont.textContent = n; cont.hidden = !n; }
}
$('carro').addEventListener('click', e => { const li = e.target.closest('li'); if (!li) return; const x = carro[+li.dataset.i];
  if (e.target.closest('[data-quitar]')) { carro.splice(+li.dataset.i, 1); pintar(); anunciar(`Quitó ${x.nombre}. Subtotal ${$('subtotal').textContent}`); document.querySelector('h1').setAttribute('tabindex', '-1'); document.querySelector('h1').focus(); }
  const b = e.target.closest('[data-d]'); if (b) { x.cantidad = Math.min(20, Math.max(1, x.cantidad + +b.dataset.d)); pintar(); anunciar(`${x.nombre}: ${x.cantidad}. Subtotal ${$('subtotal').textContent}`); $('carro').children[+li.dataset.i].querySelector(`[data-d="${b.dataset.d}"]`).focus(); }
});
pintar();
</script>
''')

# ---------------------------------------------------------------- Colecciones y textos legales
nueva('colecciones.html', 'Colecciones', 'Colecciones de Historias que Habitan, organizadas por momentos y ambientes de la casa.',
      migas(INI, ('Colecciones', '')) + '''
  <header class="intro"><h1>Colecciones</h1><p>Piezas reunidas por el momento o el ambiente de la casa, no por época. Cada pieza sigue estando en su categoría.</p></header>
  <ul class="guias" style="margin-top:var(--s5)">
    <li><a href="coleccion.html"><h2>La mesa que recibe</h2><p>Vajillas, cristalería y centros de mesa para recibir en casa.</p></a></li>
    <li><a href="/colecciones/primer-hogar" data-proto><h2>Primer hogar</h2><p>Pocas piezas que combinan, para empezar una casa.</p></a></li>
    <li><a href="/colecciones/regalos-que-se-guardan" data-proto><h2>Regalos que se guardan</h2><p>Para bodas, inauguraciones y fechas especiales.</p></a></li>
  </ul>''')

for archivo, titulo, desc in [
        ('politica-de-datos.html', 'Política de tratamiento de datos', 'Cómo tratamos sus datos personales, según la Ley 1581 de 2012.'),
        ('terminos.html', 'Términos de compra', 'Condiciones de compra en Historias que Habitan.'),
        ('politica-de-cookies.html', 'Política de cookies', 'Qué cookies usamos y cómo elegir cuáles acepta.')]:
    nueva(archivo, titulo, desc, migas(INI, (titulo, '')) + '''
  <article class="doc">
    <header class="intro"><h1>''' + titulo + '''</h1></header>
    <div class="caja"><p>''' + P % '[TEXTO LEGAL PENDIENTE: lo redacta y revisa un abogado en Colombia]' + '''</p></div>
    <p class="firma">Responsable: ''' + P % '[POR CONFIRMAR: razón social, NIT, dirección de notificación y correo]' + ''' · Actualizada el [fecha].</p>
  </article>''')


# Categorías y colecciones desde datos
exec(io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else '.', 'paginas_cat.py'), encoding='utf-8').read())

/* Historias que Habitan · comportamiento compartido de inicio y categoría (prototipo). */
const WHATSAPP = ''; // [POR CONFIRMAR: número de la marca]
const anuncio = document.getElementById('anuncio');
window.anunciar = t => { anuncio.textContent = ''; requestAnimationFrame(() => anuncio.textContent = t); };
window.track = (event, datos) => (window.dataLayer = window.dataLayer || []).push({ event, ...datos });

/* Menú: el foco entra al abrir, Esc lo cierra y el foco vuelve al botón (comportamiento nativo de dialog) */
const menu = document.getElementById('menu');
document.addEventListener('click', e => {
  if (e.target.closest('[data-abrir-menu]')) { menu.showModal(); return; }
  const panel = e.target.closest('dialog.panel');
  if (panel && (e.target === panel || e.target.closest('[data-cerrar]'))) return panel.close();
  const wa = e.target.closest('[data-wa]');
  if (wa) { e.preventDefault(); return window.open(`https://wa.me/${WHATSAPP}?text=${encodeURIComponent('Buen día. Tengo una pregunta sobre Historias que Habitan.')}`, '_blank', 'noopener'); }
  const proto = e.target.closest('[data-proto]');
  if (proto) { e.preventDefault(); anunciar('Prototipo: esta página todavía no existe.'); const a = document.getElementById('aviso-proto'); a.hidden = false; clearTimeout(a.t); a.t = setTimeout(() => a.hidden = true, 3500); }
});
document.querySelector('.buscar')?.addEventListener('submit', e => { e.preventDefault(); const q = e.target.elements.q.value.trim(); location.href = 'buscar.html' + (q ? '?q=' + encodeURIComponent(q) : ''); });

/* La pieza que se toca es la que viaja a la ficha */
document.addEventListener('click', e => {
  const a = e.target.closest('.tarjeta a[href$=".html"]'); if (!a) return;
  document.querySelectorAll('.arte').forEach(x => x.style.viewTransitionName = '');
  const arte = a.querySelector('.arte'); if (arte) arte.style.viewTransitionName = 'pieza';
});

/* El ícono del carrito muestra cuántas piezas hay guardadas */
try {
  const guardado = JSON.parse(localStorage.getItem('hqh-carrito')) || [], n = guardado.reduce((t, x) => t + x.cantidad, 0), icono = document.querySelector('[data-contador]');
  if (icono && n) { icono.setAttribute('aria-label', `Carrito, ${n} ${n === 1 ? 'pieza' : 'piezas'}`); const b = document.createElement('span'); b.className = 'contador'; b.textContent = n; icono.append(b); }
} catch (e) {}

/* Aviso de cookies: no bloquea la página, las dos opciones pesan lo mismo y nada viene aceptado */
try {
  const aviso = document.getElementById('cookies');
  if (aviso && !localStorage.getItem('hqh-cookies')) aviso.hidden = false;
  aviso?.addEventListener('click', e => { const b = e.target.closest('[data-cookies]'); if (!b) return; localStorage.setItem('hqh-cookies', b.dataset.cookies); aviso.hidden = true; anunciar(b.dataset.cookies === 'todas' ? 'Cookies aceptadas' : 'Solo cookies necesarias'); });
} catch (e) {}

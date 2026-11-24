"""Estado comercial de cada pieza, en un solo lugar: precio anterior (oferta) y unidades disponibles.

Lo leen todas las páginas que muestran piezas: tienda, categorías, colecciones, descuentos, fichas, inicio
(estantería y galería de colecciones) y búsqueda. Así una pieza nunca aparece en oferta en un lugar y a precio
normal en otro, ni disponible en la tienda y agotada en su ficha.

[EJEMPLO] Los valores son de prototipo. En producción salen del inventario y de los precios de la plataforma:
- «Oferta» solo con una rebaja real, con el precio anterior verificable y sus fechas.
- «Quedan pocas» solo con el conteo real de unidades. Nunca se inventa ni se usa para apurar.
"""
import re
import unicodedata

POCAS = 3  # [POR CONFIRMAR] con 3 unidades o menos se muestra «Quedan N»

# clave (nombre sin tildes ni corchetes): antes = precio anterior en pesos · unidades = existencias (0 = agotada)
ESTADO = {
    # Ofertas
    'recipiente-pequeno-de-ceramica': dict(antes=99900),
    'esfera-de-porcelana': dict(antes=89900, unidades=2),       # oferta y además quedan pocas
    'ramo-en-cuenco-blanco': dict(antes=119900),
    'juego-de-6-platos-verdes': dict(antes=199900),
    'centro-de-mesa-en-cuenco-blanco': dict(antes=169900),
    'ave-de-ceramica-cafe': dict(antes=139900),
    # Quedan pocas
    'jarron-de-vidrio-ambar': dict(unidades=2),
    'juego-de-6-copas-ambar': dict(unidades=3),
    'juego-de-6-copas-de-vino': dict(unidades=2),
    'escultura-curva-cafe': dict(unidades=1),
    # Agotadas
    'anfora-decorativa-de-ceramica': dict(unidades=0),
    'figura-de-ceramica-arena': dict(unidades=0),
    'jarra-de-vidrio': dict(unidades=0),
}

# [EJEMPLO] Lo nuevo: piezas recién llegadas, de la más reciente a la más antigua. Lo leen el inicio (sección 3) y
# lo-nuevo.html. En producción sale de la fecha de publicación o de una etiqueta de la plataforma
# [POR CONFIRMAR: por cuánto tiempo una pieza cuenta como nueva]
NUEVAS = ['ave-de-porcelana-azul', 'jarron-de-vidrio-ambar', 'centro-de-mesa-con-flores', 'cuenco-para-servir',
          'ave-de-porcelana-blanca', 'bandeja-con-florero']


def clave(nombre):
    t = unicodedata.normalize('NFD', nombre.lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')


def estado(nombre):
    """antes (int o None), unidades (int o None), agotada, pocas."""
    e = ESTADO.get(clave(nombre), {})
    u = e.get('unidades')
    return dict(antes=e.get('antes'), unidades=u, agotada=u == 0, pocas=u is not None and 0 < u <= POCAS)


def pct(precio, antes):
    return round((1 - precio / antes) * 100) if precio and antes else 0


def pesos(n):
    return '$' + format(int(n), ',').replace(',', '.')


# Textos de los estados, iguales en todo el sitio
def texto_pocas(u):
    return 'Queda 1' if u == 1 else 'Quedan %d' % u


def texto_unidades(u):
    return 'Queda 1 unidad' if u == 1 else 'Quedan %d unidades' % u

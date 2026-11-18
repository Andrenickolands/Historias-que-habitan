"""Ilustraciones de ejemplo de piezas de decoración, de pie sobre y = 286 en un lienzo de 200 x 300.
Son marcadores: en producción se reemplazan por la foto recortada de cada pieza."""

BLANCO = [255, 255, 255]


def _hex(h):
    return [int(h[i:i + 2], 16) for i in (1, 3, 5)]


def _mix(a, b, t):
    return [a[i] + (b[i] - a[i]) * t for i in range(3)]


def _css(c, k=1.0, a=1.0):
    r, g, b = [max(0, min(255, round(x * k))) for x in c]
    return 'rgba(%d,%d,%d,%.2f)' % (r, g, b, a)


# cuerpo (silueta) y caja (x, y, ancho, alto) de cada forma
FORMAS = {
    'anfora': ('M84 60 H116 Q120 60 119 66 L116 92 Q150 112 152 170 Q154 236 124 282 Q122 286 116 286 H84 Q78 286 76 282 Q46 236 48 170 Q50 112 84 92 L81 66 Q80 60 84 60 Z', (48, 60, 104, 226)),
    'alto': ('M86 30 H114 Q118 30 117 36 L114 70 Q136 110 136 180 Q136 250 122 284 Q121 286 116 286 H84 Q79 286 78 284 Q64 250 64 180 Q64 110 86 70 L83 36 Q82 30 86 30 Z', (64, 30, 72, 256)),
    'panza': ('M88 96 H112 Q116 96 115 102 L113 124 Q152 144 152 200 Q152 262 120 284 Q118 286 114 286 H86 Q82 286 80 284 Q48 262 48 200 Q48 144 87 124 L85 102 Q84 96 88 96 Z', (48, 96, 104, 190)),
    'florero': ('M74 150 H126 Q130 150 129 156 L123 280 Q123 286 117 286 H83 Q77 286 77 280 L71 156 Q70 150 74 150 Z', (70, 150, 60, 136)),
    'tarro': ('M62 190 Q60 170 78 168 H122 Q140 170 138 190 L134 278 Q133 286 124 286 H76 Q67 286 66 278 Z', (60, 168, 80, 118)),
    'cuenco': ('M56 214 H144 Q148 214 147 220 Q142 270 118 284 Q116 286 112 286 H88 Q84 286 82 284 Q58 270 53 220 Q52 214 56 214 Z', (52, 214, 96, 72)),
}
FORMAS['relieve'] = FORMAS['panza']
FORMAS.update({
    'figura': ('M68 286 H132 Q134 270 120 262 Q142 246 140 214 Q138 194 122 188 Q127 174 116 166 Q103 158 93 168 L78 164 L90 179 Q72 196 70 224 Q68 250 84 264 Q66 270 68 286 Z', (68, 158, 74, 128)),
    'copa': ('M74 118 H126 Q130 166 106 186 Q103 188 103 192 V266 Q122 270 130 286 H70 Q78 270 97 266 V192 Q97 188 94 186 Q70 166 74 118 Z', (70, 118, 60, 168)),
    'plato': ('M34 250 H166 Q170 250 168 256 L160 278 Q157 286 148 286 H52 Q43 286 40 278 L32 256 Q30 250 34 250 Z', (32, 250, 136, 36)),
    'flores': ('M80 212 H120 Q124 212 123 218 L118 280 Q118 286 112 286 H88 Q82 286 82 280 L77 218 Q76 212 80 212 Z', (76, 212, 48, 74)),
    'centro': ('M50 236 H150 Q154 236 153 242 Q148 274 122 284 Q119 286 114 286 H86 Q81 286 78 284 Q52 274 47 242 Q46 236 50 236 Z', (46, 236, 108, 50)),
    'escultura': ('M86 286 H114 V272 Q144 252 136 204 Q130 164 100 140 Q74 164 66 202 Q58 248 86 272 Z', (58, 140, 86, 146)),
    'esfera': ('M72 286 H128 L122 262 H108 Q136 250 136 214 Q136 176 100 176 Q64 176 64 214 Q64 250 92 262 H78 Z', (64, 176, 72, 110)),
})

_TALLOS = '<path d="%s" fill="none" stroke="#6E7F68" stroke-width="2.2" stroke-linecap="round"/>'
_HOJA = '<path d="%s" fill="#7C8C74"/>'
_FLOR = '<circle cx="%d" cy="%d" r="%d" fill="%s"/><circle cx="%d" cy="%d" r="%d" fill="#fff" opacity=".35"/>'


def _ramo(base_y, alto):
    t = base_y - alto
    tallos = ''.join(_TALLOS % d for d in ('M100 %d Q96 %d 78 %d' % (base_y, base_y - 40, t + 18), 'M100 %d V%d' % (base_y, t), 'M100 %d Q106 %d 124 %d' % (base_y, base_y - 40, t + 12),
                                                 'M100 %d Q90 %d 66 %d' % (base_y, base_y - 20, t + 46), 'M100 %d Q112 %d 136 %d' % (base_y, base_y - 24, t + 40)))
    hojas = _HOJA % ('M94 %d q-16 -6 -20 -18 q14 0 20 18z' % (base_y - 30)) + _HOJA % ('M106 %d q16 -6 20 -18 q-14 0 -20 18z' % (base_y - 40))
    flores = ''.join(_FLOR % (x, y, r, c, x - r // 3, y - r // 3, r // 3) for x, y, r, c in (
        (78, t + 18, 13, '#E7C3BB'), (100, t, 15, '#F4D9A0'), (124, t + 12, 13, '#E7C3BB'), (66, t + 46, 10, '#F1EEE8'), (136, t + 40, 11, '#F4D9A0')))
    return tallos + hojas + flores


EXTRAS = {
    'flores': lambda i: (_ramo(222, 150), ''),
    'centro': lambda i: (_ramo(246, 96), ''),
    'plato': lambda i: ('', '<path d="M38 262 H162 M42 272 H158" stroke="#000" stroke-opacity=".08" stroke-width="1.5"/>'),
}
_n = [0]


def arte(forma, color, vidrio=False):
    _n[0] += 1
    i = 'pz%d' % _n[0]
    cuerpo, (bx, by, bw, bh) = FORMAS[forma]
    c = _hex(color)
    a = 0.62 if vidrio else 1.0
    paradas = [(0, _css(c, .5, a)), (.08, _css(c, .8, a)), (.18, _css(_mix(c, BLANCO, .38), 1, a)), (.34, _css(c, 1, a)),
               (.6, _css(c, .9, a)), (.82, _css(c, .68, a)), (.94, _css(_mix(c, BLANCO, .12), .86, a)), (1, _css(c, .52, a))]
    grad = ''.join('<stop offset="%s" stop-color="%s"/>' % p for p in paradas)
    antes, despues = '', ''
    if forma == 'anfora':
        antes = ('<path d="M86 84 Q52 82 58 126" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round"/>'
                 '<path d="M114 84 Q148 82 142 126" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round"/>'
                 '<path d="M84 82 Q56 82 59 118" fill="none" stroke="#fff" stroke-opacity=".45" stroke-width="1.4" stroke-linecap="round"/>'
                 % (_css(c, .8), _css(c, .62)))
    if forma == 'tarro':
        despues = ('<rect x="70" y="150" width="60" height="20" rx="4" fill="url(#%s-c)"/>'
                   '<circle cx="100" cy="143" r="8" fill="url(#%s-c)"/>'
                   '<rect x="66" y="168" width="68" height="3" fill="#000" opacity=".18"/>'
                   '<path d="M73 152 H127" stroke="#fff" stroke-opacity=".6"/>' % (i, i))
    if forma in EXTRAS:
        extra_antes, extra_despues = EXTRAS[forma](i)
        antes += extra_antes
        despues += extra_despues
    dentro = ''
    if forma == 'relieve':
        dentro = ''.join('<path d="M40 %d Q100 %d 160 %d" fill="none" stroke="#000" stroke-opacity=".09" stroke-width="2"/>' % (y, y + 10, y)
                         for y in range(150, 270, 14))
    if vidrio:
        dentro += '<rect x="%d" y="272" width="%d" height="14" fill="%s"/><path d="M%d 273 H%d" stroke="#fff" stroke-opacity=".55"/>' % (
            bx, bw, _css(c, .55, .5), bx + 8, bx + bw - 8)
    return (
        '<svg class="arte" viewBox="0 0 200 300" aria-hidden="true" focusable="false"><defs>'
        '<linearGradient id="%(i)s-c" x1="0" x2="1">%(grad)s</linearGradient>'
        '<linearGradient id="%(i)s-v" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".14"/>'
        '<stop offset=".2" stop-color="#fff" stop-opacity="0"/><stop offset=".84" stop-color="#000" stop-opacity="0"/>'
        '<stop offset="1" stop-color="#000" stop-opacity=".2"/></linearGradient>'
        '<radialGradient id="%(i)s-s"><stop offset="0" stop-color="#000" stop-opacity=".3"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>'
        '<clipPath id="%(i)s-k"><path d="%(cuerpo)s"/></clipPath></defs>'
        '<ellipse cx="100" cy="287" rx="%(sx).1f" ry="6" fill="url(#%(i)s-s)"/>'
        '<ellipse cx="100" cy="286.4" rx="%(lx).1f" ry="1.3" fill="#000" opacity=".3"/>'
        '%(antes)s<path d="%(cuerpo)s" fill="url(#%(i)s-c)"/>'
        '<g clip-path="url(#%(i)s-k)">%(dentro)s'
        '<rect x="%(bx)d" y="%(by)d" width="%(bw)d" height="%(bh)d" fill="url(#%(i)s-v)"/>'
        '<rect x="%(h1).1f" y="%(by)d" width="%(w1).1f" height="%(bh)d" fill="#fff" opacity=".26"/>'
        '<rect x="%(h2).1f" y="%(y2)d" width="%(w2).1f" height="%(bh2)d" rx="1.5" fill="#fff" opacity=".7"/>'
        '<rect x="%(h3).1f" y="%(y2)d" width="%(w3).1f" height="%(bh2)d" rx="1" fill="#fff" opacity=".24"/></g>'
        '<path d="%(cuerpo)s" fill="none" stroke="%(borde)s" stroke-width=".7"/>%(despues)s</svg>'
    ) % dict(i=i, grad=grad, cuerpo=cuerpo, antes=antes, despues=despues, dentro=dentro, bx=bx, by=by, bw=bw, bh=bh,
             sx=bw * .5, lx=bw * .3, h1=bx + bw * .14, w1=bw * .13, h2=bx + bw * .21, w2=bw * .035,
             h3=bx + bw * .86, w3=bw * .028, y2=by + 10, bh2=bh - 24, borde=_css(c, .5, .4))

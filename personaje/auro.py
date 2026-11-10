"""AURO (M3), la mascota robot de Pertx, en SVG.

Se dibuja centrado en (300, 244), en el lado derecho de un marco de 400x400.
`auro(i, cara)` devuelve el código; `cara` cambia la pantalla y el holograma:
"feliz", "pensativo", "sorprendido", "senalando" o "celebrando".
El prefijo `i` debe ser el mismo que el de pertx_cuerpo.defs (usa su degradado dorado).
"""


def _px(cells, x0, y0, s=5):
    return "".join(f'<rect x="{x0 + cx * s}" y="{y0 + cy * s}" width="{s}" height="{s}"/>' for cx, cy in cells)


def _pantalla(cara):
    """Ojos de píxel dentro de la pantalla (x 264-336, y 210-252)."""
    if cara == "feliz":
        ojo = [(0, 1), (1, 0), (2, 1)]
        return _px(ojo, 276, 225) + _px(ojo, 309, 225), '<rect x="296" y="242" width="8" height="3" fill="#D4AF37"/>'
    if cara == "pensativo":
        return (_px([(0, 0), (1, 0), (2, 0)], 276, 230) + _px([(1, 0)], 309, 224) + _px([(0, 1), (1, 1), (2, 1)], 309, 224),
                '<rect x="300" y="243" width="8" height="3" fill="#D4AF37"/>')
    if cara == "sorprendido":
        anillo = [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
        return _px(anillo, 276, 221, 4.5) + _px(anillo, 310, 221, 4.5), '<rect x="297" y="241" width="6" height="6" fill="none" stroke="#D4AF37" stroke-width="2"/>'
    if cara == "senalando":
        flecha = [(0, 0), (1, 1), (2, 2), (1, 3), (0, 4)]
        return _px(flecha, 280, 220, 4) + _px(flecha, 312, 220, 4), '<rect x="296" y="243" width="8" height="3" fill="#D4AF37"/>'
    if cara == "celebrando":
        return ("", '<text x="300" y="241" font-family="Consolas, \'Courier New\', monospace" font-weight="700" font-size="24" '
                    'fill="#F5DE9A" text-anchor="middle" letter-spacing="10">$$</text>')
    raise ValueError(cara)


def _holograma(i, cara):
    caja = '<rect x="0" y="0" width="54" height="36" rx="4" fill="#D4AF37" fill-opacity=".08" stroke="#D4AF37" stroke-opacity=".6"/>'
    if cara in ("feliz", "celebrando"):
        dentro = (f'<path d="M6 28 L18 20 L28 24 L46 8" stroke="#F5DE9A" stroke-width="2" fill="none" filter="url(#{i}ag)"/>'
                  '<path d="M40 8 L46 8 L46 14" stroke="#F5DE9A" stroke-width="2" fill="none"/>')
    elif cara == "pensativo":
        dentro = '<text x="27" y="27" font-family="Arial Black, Arial, sans-serif" font-size="22" fill="#F5DE9A" text-anchor="middle">?</text>'
    elif cara == "sorprendido":
        dentro = '<text x="27" y="28" font-family="Arial Black, Arial, sans-serif" font-size="24" fill="#F5DE9A" text-anchor="middle">!</text>'
    else:  # senalando
        dentro = '<path d="M10 18 H42 M32 8 L44 18 L32 28" stroke="#F5DE9A" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    return f'<g transform="translate(334 150)">{caja}{dentro}</g>'


def auro(i, cara="feliz"):
    ojos, boca = _pantalla(cara)
    confeti = ""
    if cara == "celebrando":
        confeti = "".join(
            f'<rect x="{x}" y="{y}" width="5" height="5" fill="{c}" transform="rotate({r} {x} {y})"/>'
            for x, y, c, r in [(236, 168, "#F5DE9A", 20), (256, 140, "#D4AF37", -15), (350, 120, "#F5DE9A", 35),
                               (372, 196, "#D4AF37", 10), (226, 214, "#8E6E1E", -30), (378, 252, "#F5DE9A", 45)])
    return f"""
  <defs>
    <radialGradient id="{i}orb" cx="38%" cy="30%" r="75%"><stop offset="0" stop-color="#3A393E"/><stop offset=".55" stop-color="#151417"/><stop offset="1" stop-color="#050506"/></radialGradient>
    <radialGradient id="{i}thr" cx="50%" cy="0%" r="100%"><stop offset="0" stop-color="#F5DE9A"/><stop offset="1" stop-color="#D4AF37" stop-opacity="0"/></radialGradient>
    <filter id="{i}ag" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <ellipse cx="300" cy="374" rx="34" ry="6" fill="#000" opacity=".6"/>
  <!-- propulsores -->
  <path d="M286 300 L280 334 L292 334 Z" fill="url(#{i}thr)" opacity=".8"/>
  <path d="M314 300 L308 334 L320 334 Z" fill="url(#{i}thr)" opacity=".8"/>
  <!-- antena -->
  <path d="M300 186 L300 166" stroke="#2C2A30" stroke-width="3"/>
  <circle cx="300" cy="162" r="5" fill="#D4AF37" filter="url(#{i}ag)"/>
  <!-- esfera -->
  <circle cx="300" cy="244" r="58" fill="url(#{i}orb)"/>
  <ellipse cx="300" cy="262" rx="58" ry="12" fill="none" stroke="url(#{i}gold)" stroke-width="3"/>
  <path d="M242 262 A58 58 0 0 0 358 262" fill="#0A0A0B" opacity=".35"/>
  <!-- pantalla-cara -->
  <rect x="264" y="210" width="72" height="42" rx="16" fill="#050506" stroke="#2C2A30" stroke-width="1.5"/>
  <g fill="#F5DE9A" filter="url(#{i}ag)">{ojos}</g>
  {boca}
  <ellipse cx="282" cy="204" rx="16" ry="7" fill="#FFFFFF" opacity=".07" transform="rotate(-25 282 204)"/>
  {_holograma(i, cara)}{confeti}"""

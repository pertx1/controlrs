"""Pertx de cuerpo completo (P1 Sombra con la paleta de P5), en SVG.

Se dibuja en un marco de 200x400. `defs(id)` y `cuerpo(id)` devuelven el
código SVG; `id` es un prefijo para que los degradados no choquen cuando
hay varios dibujos en la misma página.
"""

GOLD = "#D4AF37"


def defs(i):
    return f"""
    <radialGradient id="{i}glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#F5DE9A" stop-opacity=".75"/><stop offset=".45" stop-color="#D4AF37" stop-opacity=".35"/><stop offset="1" stop-color="#D4AF37" stop-opacity="0"/></radialGradient>
    <linearGradient id="{i}hood" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0E0E10"/><stop offset=".55" stop-color="#1F1E22"/><stop offset="1" stop-color="#2E2A24"/></linearGradient>
    <linearGradient id="{i}body" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0E0E10"/><stop offset=".5" stop-color="#1F1E22"/><stop offset="1" stop-color="#2A2620"/></linearGradient>
    <linearGradient id="{i}legs" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0B0B0C"/><stop offset=".5" stop-color="#18171A"/><stop offset="1" stop-color="#232019"/></linearGradient>
    <radialGradient id="{i}mask" cx="42%" cy="35%" r="70%"><stop offset="0" stop-color="#2C2C2E"/><stop offset="1" stop-color="#0B0B0C"/></radialGradient>
    <linearGradient id="{i}skin" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5A3C2A"/><stop offset=".45" stop-color="#C08E6A"/><stop offset="1" stop-color="#E2BE7A"/></linearGradient>
    <linearGradient id="{i}gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F5DE9A"/><stop offset=".5" stop-color="#D4AF37"/><stop offset="1" stop-color="#8E6E1E"/></linearGradient>
    <pattern id="{i}knit" width="4" height="3.2" patternUnits="userSpaceOnUse"><path d="M0 1.6 Q1 0 2 1.6 T4 1.6" stroke="#000" stroke-opacity=".5" fill="none" stroke-width=".7"/></pattern>
    <filter id="{i}b1"><feGaussianBlur stdDeviation="1"/></filter>
    <filter id="{i}b6" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>"""


def brazo_libre(i):
    return f"""
    <!-- brazo derecho relajado, sin nada en la mano -->
    <path d="M144 120 Q166 132 166 182 L160 212 L144 210 L150 178 Z" fill="url(#{i}body)"/>
    <path d="M144 206 Q152 214 160 208" stroke="#0B0B0C" stroke-width="3" fill="none"/>
    <ellipse cx="152" cy="218" rx="7.5" ry="8.5" fill="#B98A66"/>
    <path d="M147 222 Q152 226 157 222" stroke="#8A6248" stroke-width="1.2" fill="none"/>"""


def brazo_movil(i):
    return f"""
    <!-- brazo derecho mirando el móvil -->
    <path d="M144 118 Q168 128 170 176 L154 180 L148 150 Z" fill="url(#{i}body)"/>
    <path d="M162 176 L146 150" stroke="#1F1E22" stroke-width="15" stroke-linecap="round"/>
    <ellipse cx="136" cy="128" rx="26" ry="20" fill="url(#{i}glow)" filter="url(#{i}b6)"/>
    <rect x="130" y="124" width="16" height="27" rx="3" fill="#0B0B0C" stroke="#3A3640" stroke-width="1"/>
    <rect x="132" y="127" width="12" height="20" rx="1.5" fill="#F5DE9A" opacity=".85"/>
    <ellipse cx="146" cy="148" rx="7" ry="7.5" fill="#B98A66"/>"""


def brazo_portatil(i):
    return f"""
    <!-- brazo derecho sujetando el portátil abierto -->
    <path d="M144 120 Q166 132 168 178 L162 204 L146 200 L150 174 Z" fill="url(#{i}body)"/>
    <ellipse cx="160" cy="170" rx="44" ry="34" fill="url(#{i}glow)" filter="url(#{i}b6)"/>
    <path d="M132 168 L186 166 L188 202 L130 204 Z" fill="#0B0B0C" stroke="#2C2A30" stroke-width="1.5"/>
    <text x="159" y="190" font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="10" fill="url(#{i}gold)" text-anchor="middle">PX</text>
    <path d="M126 204 L192 202 L190 208 L128 210 Z" fill="#1F1E22"/>
    <ellipse cx="156" cy="206" rx="8" ry="6" fill="#B98A66"/>
    <path d="M132 168 L186 166" stroke="#F5DE9A" stroke-width="1.6" filter="url(#{i}b1)" opacity=".9"/>"""


def brazo_senalar(i):
    return f"""
    <!-- brazo derecho señalando a la derecha (pantalla) -->
    <path d="M144 118 Q172 122 198 130 L198 146 Q172 142 150 152 Z" fill="url(#{i}body)"/>
    <path d="M196 128 Q202 136 196 148" stroke="#0B0B0C" stroke-width="3" fill="none"/>
    <ellipse cx="204" cy="138" rx="7" ry="7.5" fill="#B98A66"/>
    <rect x="207" y="134.5" width="14" height="4.5" rx="2.2" fill="#B98A66"/>"""


def brazo_celebrar(i):
    return f"""
    <!-- brazo derecho levantado celebrando -->
    <path d="M142 120 Q160 96 164 54 L180 56 Q178 102 152 132 Z" fill="url(#{i}body)"/>
    <path d="M162 56 Q171 62 180 57" stroke="#0B0B0C" stroke-width="3" fill="none"/>
    <circle cx="171" cy="46" r="9" fill="#B98A66"/>
    <path d="M165 42 L177 42 M165 46 L177 46" stroke="#8A6248" stroke-width="1.2"/>"""


def _ojo_base(dx=0, dy=0, rx=4.8, ry=3.1, pr=2.3):
    out = ""
    for cx in (89, 111):
        out += f"""
    <ellipse cx="{cx}" cy="65.5" rx="{rx}" ry="{ry}" fill="#E4DCD2"/>
    <circle cx="{cx + .6 + dx}" cy="{65.6 + dy}" r="{pr}" fill="#2E2219"/>
    <circle cx="{cx + 1.4 + dx}" cy="{66.5 + dy}" r=".8" fill="#F5DE9A"/>"""
    return out


def ojos_feliz():
    out = ""
    for cx in (89, 111):
        out += f"""
    <path d="M{cx-5} 67 Q{cx} 61.5 {cx+5} 67 Q{cx} 65 {cx-5} 67 Z" fill="#E4DCD2"/>
    <path d="M{cx-5} 67 Q{cx} 61.5 {cx+5} 67" stroke="#1A120D" stroke-width="1.4" fill="none"/>
    <path d="M{cx-4} 69.5 Q{cx} 71 {cx+4} 69.5" stroke="#8A6248" stroke-width=".9" fill="none"/>"""
    return out


def ojos_pensativo():
    return _ojo_base(dx=-1.6, dy=-1) + """
    <path d="M83 63 L95 62 M105 61 Q111 58.5 117 61.5" stroke="#1A120D" stroke-width="1.6" fill="none"/>"""


def ojos_sorprendido():
    return _ojo_base(rx=5.4, ry=4.2, pr=1.7)


def ojos_decidido():
    return _ojo_base(dx=1) + """
    <path d="M83.5 63 L95 64.5 M105 64.5 L116.5 63" stroke="#0A0A0B" stroke-width="2.4" stroke-linecap="round"/>"""


OJOS = {"normal": _ojo_base, "feliz": ojos_feliz, "pensativo": ojos_pensativo,
        "sorprendido": ojos_sorprendido, "decidido": ojos_decidido}

BRAZO = {None: brazo_libre, "movil": brazo_movil, "portatil": brazo_portatil,
         "senalar": brazo_senalar, "celebrar": brazo_celebrar}


def cuerpo(i, prop=None, ojos="normal", parpadeo=False):
    """prop: None (manos libres), "movil", "portatil", "senalar" o "celebrar".
    ojos: "normal", "feliz", "pensativo", "sorprendido" o "decidido"."""
    return f"""
    <ellipse cx="100" cy="380" rx="62" ry="7" fill="#000" opacity=".55"/>
    <!-- piernas: jogger negro -->
    <path d="M66 234 Q63 300 68 352 L97 352 L100 246 Z" fill="url(#{i}legs)"/>
    <path d="M134 234 Q137 300 132 352 L103 352 L100 246 Z" fill="url(#{i}legs)"/>
    <path d="M78 292 Q84 300 92 296 M122 292 Q116 300 108 296" stroke="#000" stroke-width="1.5" fill="none" opacity=".7"/>
    <rect x="67" y="342" width="31" height="11" rx="4" fill="#0B0B0C"/>
    <rect x="102" y="342" width="31" height="11" rx="4" fill="#0B0B0C"/>
    <!-- zapatillas negras con detalle dorado -->
    <path d="M58 375 Q56 352 74 351 L95 351 Q104 353 104 365 L104 377 L58 377 Z" fill="#141416"/>
    <path d="M142 375 Q144 352 126 351 L105 351 Q96 353 96 365 L96 377 L142 377 Z" fill="#141416"/>
    <rect x="57" y="372" width="48" height="5" rx="2.5" fill="#8E6E1E"/>
    <rect x="95" y="372" width="48" height="5" rx="2.5" fill="#8E6E1E"/>
    <path d="M70 362 L90 360 M130 362 L110 360" stroke="url(#{i}gold)" stroke-width="2.4" stroke-linecap="round"/>

    <!-- brazo izquierdo: mano al bolsillo -->
    <path d="M58 120 Q36 132 34 182 L42 210 L66 208 L60 178 Z" fill="url(#{i}body)"/>
    <!-- torso sudadera oversize -->
    <path d="M56 116 Q100 104 144 116 L152 234 Q100 244 48 234 Z" fill="url(#{i}body)"/>
    <path d="M70 196 L130 196 L136 228 L64 228 Z" fill="#141416"/>
    <path d="M70 196 L130 196" stroke="#2C2A30" stroke-width="1.5"/>
    <path d="M48 226 Q100 236 152 226 L152 236 Q100 246 48 236 Z" fill="#0E0E10"/>
    <path d="M42 206 Q52 214 66 208" stroke="#0B0B0C" stroke-width="3" fill="none"/>
    <!-- cordones -->
    <path d="M90 112 Q88 132 90 150 M110 112 Q112 132 110 150" stroke="#E8DCC4" stroke-width="2" fill="none" stroke-linecap="round"/>
    <rect x="88.4" y="149" width="3.2" height="6" rx="1.4" fill="url(#{i}gold)"/>
    <rect x="108.4" y="149" width="3.2" height="6" rx="1.4" fill="url(#{i}gold)"/>

    <g class="pxcab" style="transform-box:fill-box;transform-origin:50% 90%">
    <!-- capucha -->
    <path d="M58 120 Q46 30 100 6 Q154 30 142 120 Q128 104 100 104 Q72 104 58 120 Z" fill="url(#{i}hood)"/>
    <path d="M67 108 Q62 46 100 24 Q138 46 133 108 Q120 98 100 98 Q80 98 67 108 Z" fill="#060607"/>
    <!-- cabeza con pasamontañas -->
    <path d="M74 68 Q73 32 100 30 Q127 32 126 68 Q126 96 112 104 Q100 110 88 104 Q74 96 74 68 Z" fill="url(#{i}mask)"/>
    <path d="M74 68 Q73 32 100 30 Q127 32 126 68 Q126 96 112 104 Q100 110 88 104 Q74 96 74 68 Z" fill="url(#{i}knit)"/>
    <path d="M100 31 L100 57 M100 74 L100 108" stroke="#000" stroke-width="1" opacity=".5"/>
    <rect x="78" y="57" width="44" height="16" rx="8" fill="url(#{i}skin)"/>
    <rect x="78" y="57" width="44" height="6" rx="3" fill="#2A1C14" opacity=".55"/>
{OJOS[ojos]()}
    <path d="M78 65 Q78 57 86 57 L114 57 Q122 57 122 65" stroke="#0A0A0B" stroke-width="2" fill="none"/>
    {'<rect class="blink" data-o="0" x="78" y="57" width="44" height="16" rx="8" fill="#1B1A1D" style="opacity:0"/>' if parpadeo else ''}
    </g>

<g class="pxbrazo" style="transform-box:fill-box;transform-origin:20% 5%">{BRAZO[prop](i)}</g>

    <!-- luz dorada de borde -->
    <path d="M142 120 Q154 30 100 6" stroke="url(#{i}gold)" stroke-width="1.8" fill="none" opacity=".6" filter="url(#{i}b1)"/>
    <path d="M144 118 L152 234" stroke="url(#{i}gold)" stroke-width="1.4" opacity=".35" filter="url(#{i}b1)"/>
    <path d="M134 236 Q137 300 132 352" stroke="url(#{i}gold)" stroke-width="1.2" fill="none" opacity=".3"/>
    <path d="M78 72 Q100 80 122 72" stroke="#F5DE9A" stroke-width="1.2" fill="none" opacity=".35" filter="url(#{i}b1)"/>"""


def fondo(i, w, h):
    return f"""
    <radialGradient id="{i}bg" cx="50%" cy="32%" r="80%"><stop offset="0" stop-color="#2A2219"/><stop offset=".55" stop-color="#13100C"/><stop offset="1" stop-color="#080706"/></radialGradient>""", f"""
  <rect width="{w}" height="{h}" fill="url(#{i}bg)"/>
  <path d="M0 {h-22} H{w}" stroke="url(#{i}gold)" stroke-width=".8" opacity=".35"/>"""


def badge(code, nombre, x=12, y=12):
    w = max(86, len(code) * 16 + 20)
    return f"""
  <g font-family="Arial, Helvetica, sans-serif" text-anchor="middle">
    <rect x="{x}" y="{y}" width="{w}" height="44" rx="11" fill="#D4AF37"/>
    <text x="{x+w/2}" y="{y+28}" font-size="24" font-weight="800" fill="#13100C">{code}</text>
    <text x="{x+w/2}" y="{y+39}" font-size="8" font-weight="700" fill="#3A2C0A" letter-spacing=".6">{nombre}</text>
  </g>"""


def svg_solo(prop=None):
    i = "pc" + (prop or "")[:2]
    gdefs, bg = fondo(i, 300, 400)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 400" width="300" height="400">
  <!-- Pertx · cuerpo completo · P1 Sombra con colores de P5 · objeto: {prop or "ninguno"} -->
  <defs>{defs(i)}{gdefs}
  </defs>{bg}
  <g transform="translate(50 12)">{cuerpo(i, prop)}
  </g>{badge("P1", "SOMBRA ORO")}
</svg>
"""


def svg_escenas():
    """Las 3 variantes una al lado de otra: manos libres, móvil y portátil."""
    i = "pe"
    gdefs, bg = fondo(i, 600, 400)
    partes = []
    for n, (prop, txt) in enumerate([(None, "SIN OBJETO"), ("movil", "MÓVIL"), ("portatil", "PORTÁTIL")]):
        partes.append(f"""
  <g transform="translate({n * 200} 12)">{cuerpo(i, prop)}
  </g>
  <text x="{n * 200 + 100}" y="396" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="#D4AF37" text-anchor="middle" letter-spacing="1.5">{txt}</text>""")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="600" height="400">
  <!-- Pertx · el objeto cambia según la escena -->
  <defs>{defs(i)}{gdefs}
  </defs>{bg}{"".join(partes)}{badge("P1", "SOMBRA ORO")}
</svg>
"""

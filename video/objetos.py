import html as _h

"""Objetos de Pertx en SVG (negro y oro), centrados en (0,0) y de unos 64 px de ancho.

`objeto(tipo)` devuelve el dibujo. Tipos: moneda, monedas, euro, camiseta, caja, bolsa, etiqueta, movil,
portatil, grafica, trofeo, reloj, bombilla, papel, cohete, calendario, web, tienda, check, error, libro, lupa.
"""
G, G2, G3 = "#D4AF37", "#F5DE9A", "#8E6E1E"
N, N2, L, C = "#0E0D0B", "#1F1E22", "#2E281E", "#F3EEE3"


def _moneda(x=0, y=0, r=22):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{G3}"/><circle cx="{x}" cy="{y - 2}" r="{r}" fill="{G}"/>'
            f'<circle cx="{x}" cy="{y - 2}" r="{r * .72}" fill="none" stroke="{G2}" stroke-width="2"/>'
            f'<text x="{x}" y="{y + r * .36}" font-family="Inter, Arial" font-weight="900" font-size="{r * 1.05}" fill="{G3}" text-anchor="middle">€</text>')


DIBUJOS = {
    "moneda": lambda: _moneda(),
    "monedas": lambda: _moneda(-14, 10, 16) + _moneda(12, 6, 16) + _moneda(-2, -10, 18),
    "euro": lambda: (f'<circle r="30" fill="{N}" stroke="{G}" stroke-width="3"/>'
                     f'<text y="13" font-family="Inter, Arial" font-weight="900" font-size="38" fill="{G}" text-anchor="middle">€</text>'),
    "camiseta": lambda: (f'<path d="M-14 -28 L-34 -18 L-28 -2 L-20 -6 L-20 30 L20 30 L20 -6 L28 -2 L34 -18 L14 -28 Q0 -18 -14 -28 Z" '
                         f'fill="{N2}" stroke="{G}" stroke-width="2" stroke-linejoin="round"/>'
                         f'<path d="M-14 -28 Q0 -18 14 -28" fill="none" stroke="{G}" stroke-width="2"/>'
                         f'<rect x="-9" y="-6" width="18" height="12" rx="2" fill="{G}"/>'),
    "caja": lambda: (f'<path d="M-30 -10 L0 -24 L30 -10 L0 4 Z" fill="#B98A50"/><path d="M-30 -10 L0 4 L0 30 L-30 16 Z" fill="#8C6538"/>'
                     f'<path d="M30 -10 L0 4 L0 30 L30 16 Z" fill="#A47645"/><path d="M-15 -17 L15 -3 L15 6" stroke="{G2}" stroke-width="4" fill="none"/>'),
    "bolsa": lambda: (f'<path d="M-24 -14 L24 -14 L28 30 L-28 30 Z" fill="{N2}" stroke="{G}" stroke-width="2"/>'
                      f'<path d="M-12 -14 Q-12 -32 0 -32 Q12 -32 12 -14" fill="none" stroke="{G}" stroke-width="3"/>'
                      f'<text y="14" font-family="Georgia, serif" font-weight="700" font-size="14" fill="{G}" text-anchor="middle">PX</text>'),
    "etiqueta": lambda: (f'<path d="M-30 -14 L18 -14 L32 0 L18 14 L-30 14 Z" fill="{G}"/><circle cx="18" cy="0" r="4" fill="{N}"/>'),
    "movil": lambda: (f'<rect x="-18" y="-32" width="36" height="64" rx="7" fill="{N}" stroke="#3A3640" stroke-width="2"/>'
                      f'<rect x="-14" y="-26" width="28" height="50" rx="3" fill="#13100C"/>'
                      f'<rect x="-12" y="-20" width="24" height="12" rx="3" fill="{G}"/><rect x="-12" y="-4" width="24" height="5" rx="2" fill="{L}"/>'
                      f'<rect x="-12" y="5" width="16" height="5" rx="2" fill="{L}"/>'),
    "portatil": lambda: (f'<rect x="-30" y="-24" width="60" height="38" rx="4" fill="{N}" stroke="{L}" stroke-width="2"/>'
                         f'<rect x="-25" y="-19" width="50" height="28" rx="2" fill="#13100C"/>'
                         f'<path d="M-20 -12 H4 M-20 -5 H14 M-20 2 H0" stroke="{G}" stroke-width="2.5" stroke-linecap="round"/>'
                         f'<path d="M-36 14 H36 L32 20 H-32 Z" fill="{N2}"/>'),
    "grafica": lambda: (f'<rect x="-30" y="-26" width="60" height="52" rx="8" fill="{N}" stroke="{L}" stroke-width="2"/>'
                        f'<rect x="-20" y="4" width="8" height="12" fill="{G3}"/><rect x="-6" y="-4" width="8" height="20" fill="{G}"/>'
                        f'<rect x="8" y="-14" width="8" height="30" fill="{G2}"/>'
                        f'<path d="M-20 -6 L-4 -14 L6 -10 L22 -20" stroke="{G2}" stroke-width="2.5" fill="none"/><path d="M15 -21 L22 -20 L21 -13" stroke="{G2}" stroke-width="2.5" fill="none"/>'),
    "trofeo": lambda: (f'<path d="M-18 -26 H18 V-8 Q18 10 0 12 Q-18 10 -18 -8 Z" fill="{G}"/>'
                       f'<path d="M-18 -20 Q-32 -20 -28 -6 Q-25 2 -16 0 M18 -20 Q32 -20 28 -6 Q25 2 16 0" stroke="{G}" stroke-width="4" fill="none"/>'
                       f'<rect x="-4" y="12" width="8" height="10" fill="{G3}"/><rect x="-16" y="22" width="32" height="8" rx="2" fill="{G3}"/>'),
    "reloj": lambda: (f'<circle r="28" fill="{N}" stroke="{G}" stroke-width="3"/><path d="M0 -18 V0 L12 8" stroke="{G2}" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
                      f'<circle r="3" fill="{G}"/>'),
    "bombilla": lambda: (f'<circle cy="-8" r="22" fill="{G2}" opacity=".25"/><path d="M-16 -8 Q-16 -28 0 -28 Q16 -28 16 -8 Q16 4 8 10 V16 H-8 V10 Q-16 4 -16 -8 Z" fill="{G}"/>'
                         f'<rect x="-8" y="17" width="16" height="5" rx="2" fill="{L}"/><rect x="-6" y="24" width="12" height="5" rx="2" fill="{L}"/>'),
    "papel": lambda: (f'<rect x="-20" y="-24" width="40" height="48" rx="3" fill="{C}" transform="rotate(-8)"/>'
                      f'<path d="M-12 -12 H12 M-12 -4 H12 M-12 4 H6" stroke="#B3A994" stroke-width="2.5" transform="rotate(-8)"/>'),
    "cohete": lambda: (f'<path d="M0 -32 Q16 -16 12 14 H-12 Q-16 -16 0 -32 Z" fill="{C}"/><circle cy="-8" r="6" fill="{G}"/>'
                       f'<path d="M-12 6 L-22 22 L-10 16 Z M12 6 L22 22 L10 16 Z" fill="{G}"/><path d="M-7 16 Q0 34 7 16 Z" fill="#FF8A3D"/>'),
    "calendario": lambda: (f'<rect x="-28" y="-24" width="56" height="52" rx="6" fill="{N}" stroke="{L}" stroke-width="2"/><rect x="-28" y="-24" width="56" height="14" rx="6" fill="{G}"/>'
                           + "".join(f'<rect x="{-20 + c * 14}" y="{-4 + f * 12}" width="9" height="8" rx="2" fill="{L if (c + f) % 3 else G3}"/>' for f in range(3) for c in range(4))),
    "web": lambda: (f'<rect x="-34" y="-26" width="68" height="52" rx="6" fill="{N}" stroke="{L}" stroke-width="2"/><rect x="-34" y="-26" width="68" height="10" rx="5" fill="{N2}"/>'
                    f'<circle cx="-27" cy="-21" r="2" fill="{G}"/><rect x="-26" y="-10" width="52" height="14" rx="3" fill="{G}"/><rect x="-26" y="8" width="24" height="12" rx="3" fill="{L}"/><rect x="2" y="8" width="24" height="12" rx="3" fill="{L}"/>'),
    "tienda": lambda: (f'<rect x="-30" y="-6" width="60" height="36" fill="{N2}" stroke="{L}"/><path d="M-34 -6 L-28 -26 H28 L34 -6 Z" fill="{G}"/>'
                       + "".join(f'<path d="M{-34 + k * 17} -6 Q{-25.5 + k * 17} 4 {-17 + k * 17} -6" fill="{G3}"/>' for k in range(4))
                       + f'<rect x="-8" y="8" width="16" height="22" fill="#13100C"/><rect x="-26" y="6" width="14" height="12" fill="{G2}" opacity=".5"/>'),
    "check": lambda: f'<circle r="26" fill="#1E3A20" stroke="#9FD17A" stroke-width="3"/><path d="M-12 0 L-3 10 L13 -10" stroke="#9FD17A" stroke-width="5" fill="none" stroke-linecap="round"/>',
    "error": lambda: f'<circle r="26" fill="#3A0E0E" stroke="#E5484D" stroke-width="3"/><path d="M-10 -10 L10 10 M10 -10 L-10 10" stroke="#E5484D" stroke-width="5" stroke-linecap="round"/>',
    "libro": lambda: (f'<path d="M-30 -20 Q-15 -26 0 -18 Q15 -26 30 -20 V22 Q15 16 0 24 Q-15 16 -30 22 Z" fill="{N2}" stroke="{G}" stroke-width="2"/>'
                      f'<path d="M0 -18 V24" stroke="{G}" stroke-width="2"/><path d="M-22 -8 H-8 M-22 0 H-8 M8 -8 H22 M8 0 H22" stroke="#8A8070" stroke-width="2"/>'),
    "lupa": lambda: f'<circle cx="-6" cy="-6" r="18" fill="{G2}" fill-opacity=".15" stroke="{G}" stroke-width="5"/><path d="M7 7 L24 24" stroke="{G}" stroke-width="8" stroke-linecap="round"/>',
}
TIPOS = sorted(DIBUJOS)


def objeto(tipo: str, etiqueta: str = "", k: float = 1.0) -> str:
    """Dibujo del objeto (centrado en 0,0) con una etiqueta opcional debajo."""
    if tipo not in DIBUJOS:
        raise ValueError(f"objeto «{tipo}» no existe. Usa: {', '.join(TIPOS)}")
    et = ""
    if etiqueta:
        w = len(etiqueta) * 7.4 + 18
        et = (f'<rect x="{-w / 2}" y="38" width="{w}" height="20" rx="10" fill="#13100C" stroke="{G}" stroke-width="1.2"/>'
              f'<text y="52" font-family="Inter, Arial" font-weight="900" font-size="11" fill="{G}" text-anchor="middle">{_h.escape(etiqueta)}</text>')
    return f'<g transform="scale({k})">{DIBUJOS[tipo]()}{et}</g>'

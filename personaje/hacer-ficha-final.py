#!/usr/bin/env python3
"""Crea las imágenes de la ficha final de Pertx (P1-oro + M3 Auro).

Uso (desde la carpeta del proyecto):  python3 personaje/hacer-ficha-final.py
Crea: personaje/svg/FINAL-P1oro-M3.svg  (imagen principal)
      personaje/svg/FINAL-expresiones.svg (las 5 poses y expresiones)
"""
import pathlib
import sys

AQUI = pathlib.Path(__file__).parent
sys.path.insert(0, str(AQUI))
import auro  # noqa: E402
import pertx_cuerpo as pertx  # noqa: E402

POSES = [
    ("feliz", "FELIZ", None, "feliz", "feliz"),
    ("pensativo", "PENSATIVO", None, "pensativo", "pensativo"),
    ("sorprendido", "SORPRENDIDO", None, "sorprendido", "sorprendido"),
    ("senalando", "SEÑALANDO LA PANTALLA", "senalar", "decidido", "senalando"),
    ("celebrando", "CELEBRANDO", "celebrar", "feliz", "celebrando"),
]


def panel(i, prop, ojos, cara):
    return f"""
  <g transform="translate(14 14) scale(.96)">{pertx.cuerpo(i, prop, ojos)}
  </g>{auro.auro(i, cara)}"""


def principal():
    i = "fm"
    gdefs, bg = pertx.fondo(i, 400, 400)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <!-- FICHA FINAL · P1-oro + M3 Auro -->
  <defs>{pertx.defs(i)}{gdefs}
  </defs>{bg}{panel(i, None, "normal", "feliz")}{pertx.badge("P1+M3", "PERTX + AURO")}
</svg>
"""


def expresiones():
    i = "fe"
    w = 400 * len(POSES)
    gdefs, bg = pertx.fondo(i, w, 400)
    partes = []
    for n, (_, titulo, prop, ojos, cara) in enumerate(POSES):
        partes.append(f"""
  <g transform="translate({n * 400} 0)">{panel(i, prop, ojos, cara)}
    <text x="200" y="396" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="#D4AF37" text-anchor="middle" letter-spacing="1.5">{n + 1}. {titulo}</text>
  </g>""")
        if n:
            partes.append(f'\n  <path d="M{n * 400} 30 V370" stroke="#2E281E" stroke-width="1"/>')
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 400" width="{w}" height="400">
  <!-- FICHA FINAL · poses y expresiones de Pertx + Auro -->
  <defs>{pertx.defs(i)}{gdefs}
  </defs>{bg}{"".join(partes)}{pertx.badge("P1+M3", "PERTX + AURO")}
</svg>
"""


def main():
    d = AQUI / "svg"
    (d / "FINAL-P1oro-M3.svg").write_text(principal(), encoding="utf-8")
    (d / "FINAL-expresiones.svg").write_text(expresiones(), encoding="utf-8")
    print("Hecho: svg/FINAL-P1oro-M3.svg y svg/FINAL-expresiones.svg")


if __name__ == "__main__":
    main()

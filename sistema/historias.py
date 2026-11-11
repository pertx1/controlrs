#!/usr/bin/env python3
"""Crea una historia (1080x1920) por día para Instagram/TikTok: "NUEVO VÍDEO" + título + Pertx y Auro.

  npm run historias -- 1        # semana 1 → video/salida/semana-01/historia-dia-NN.png

La parte de abajo se deja libre para el sticker (enlace al vídeo o encuesta) que se pone desde la app.
La pregunta de la encuesta de cada día sale en el panel y en `encuesta` del guion (si existe).
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import textwrap

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "personaje"))
sys.path.insert(0, str(RAIZ / "video"))
import auro  # noqa: E402
import pertx_cuerpo as px  # noqa: E402
from motor import fondo_escena  # noqa: E402

FONDOS = ["habitacion", "escenario", "calle"]


def svg_historia(g: dict, n: int) -> str:
    gdefs, bg = px.fondo("h", 360, 640)
    lineas = textwrap.wrap(g["titulo"].upper(), 16)[:4]
    tam = 34 if len(lineas) <= 2 else 28
    titulo = "".join(
        f'<text x="180" y="{150 + k * (tam + 8)}" font-family="Inter, Arial Black, sans-serif" font-size="{tam}" font-weight="900" '
        f'fill="{"#D4AF37" if k == len(lineas) - 1 else "#F3EEE3"}" text-anchor="middle" stroke="#080706" stroke-width="5" paint-order="stroke">{l}</text>'
        for k, l in enumerate(lineas))
    y_px = 150 + len(lineas) * (tam + 8) + 10
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 640" width="360" height="640">
  <defs>{px.defs("h")}{gdefs}</defs>{bg}
  {fondo_escena(FONDOS[n % len(FONDOS)])}
  <rect x="0" y="0" width="360" height="640" fill="#080706" opacity=".35"/>
  <text x="20" y="40" font-family="Georgia, serif" font-weight="700" font-size="14" fill="#D4AF37" letter-spacing="1.5">PX</text>
  <rect x="110" y="72" width="140" height="26" rx="13" fill="#D4AF37"/>
  <text x="180" y="90" font-family="Inter, Arial, sans-serif" font-size="12" font-weight="900" fill="#13100C" text-anchor="middle" letter-spacing="1.5">NUEVO VÍDEO</text>
  {titulo}
  <g transform="translate(60 {y_px}) scale(.62)">{px.cuerpo("h", None, "decidido")}</g>
  <g transform="translate({262 - 300 * .38} {y_px + 70 - 244 * .38}) scale(.38)">{auro.auro("h", "feliz")}</g>
  <text x="180" y="{y_px + 268}" font-family="Inter, Arial, sans-serif" font-size="13" font-weight="800" fill="#F3EEE3" text-anchor="middle">Toca el enlace para verlo ↓</text>
</svg>"""


RENDER = r"""
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:360,height:640},deviceScaleFactor:3});
for(const [svg,png] of JSON.parse(fs.readFileSync(0,'utf8'))){await p.setContent('<body style="margin:0">'+fs.readFileSync(svg,'utf8')+'</body>');
await p.evaluate(()=>document.fonts.ready);await p.locator('svg').first().screenshot({path:png});}
await b.close();})();
"""


def main(sem: int):
    carpeta = RAIZ / "video" / "salida" / f"semana-{sem:02d}"
    carpeta.mkdir(parents=True, exist_ok=True)
    trabajos = []
    for ruta in sorted((RAIZ / "guiones" / f"semana-{sem:02d}").glob("dia-*.json")):
        g = json.loads(ruta.read_text(encoding="utf-8"))
        n = g["dia"]
        svg = carpeta / f".historia-dia-{n:02d}.svg"
        svg.write_text(svg_historia(g, n), encoding="utf-8")
        trabajos.append([str(svg), str(carpeta / f"historia-dia-{n:02d}.png")])
    subprocess.run(["node", "-e", RENDER], input=json.dumps(trabajos), text=True, check=True, cwd=RAIZ)
    for s, _ in trabajos:
        pathlib.Path(s).unlink()
    print(f"Hecho: {len(trabajos)} historias en {carpeta.relative_to(RAIZ)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(int(sys.argv[1]))

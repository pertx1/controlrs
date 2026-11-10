#!/usr/bin/env python3
"""Genera personaje/galeria.html metiendo dentro los SVG de personaje/svg/.

Uso (desde la carpeta del proyecto):  python3 personaje/hacer-galeria.py
Vuelve a ejecutarlo cada vez que cambies un SVG.
"""
import html
import pathlib

AQUI = pathlib.Path(__file__).parent

VERSIONES = [
    {
        "code": "P1", "estilo": "Sombra", "edad": "Noir semi-realista",
        "vibe": "Construye de noche, a solas, con la luz de la pantalla.",
        "habla": "Poco y despacio, frases que pegan.",
        "mejor": "Construir con IA, números reales, mentalidad.",
        "colores": ["#141518", "#1C1D22", "#29D3FF", "#C99A78", "#BFC6CF", "#07080A"],
        "nota": "Mi favorito",
    },
    {
        "code": "P2", "estilo": "Glitch", "edad": "Cyberpunk neón",
        "vibe": "Medio humano, medio IA, con ojos LED.",
        "habla": "Frío y rápido: \u201cproceso completado\u201d.",
        "mejor": "Herramientas de IA, automatizaciones.",
        "colores": ["#15131C", "#00F0FF", "#FF2BD6", "#231D36", "#0D0221", "#FFFFFF"],
        "nota": "El más fácil de animar",
    },
    {
        "code": "P3", "estilo": "Calle", "edad": "Póster serigrafía",
        "vibe": "Streetwear rebelde, como un cartel pegado en la pared.",
        "habla": "Sin filtro: \u201cdeja de mirar tutoriales, construye\u201d.",
        "mejor": "Mentalidad, opiniones fuertes, portadas.",
        "colores": ["#0E0E0E", "#E10600", "#E9E2D3", "#1A1A1A", "#1C1C1C", "#050505"],
        "nota": "El que más destaca",
    },
    {
        "code": "P4", "estilo": "Icono", "edad": "Flat monocromo",
        "vibe": "Un logo con vida: negro total y un color de marca.",
        "habla": "Seco y ordenado: \u201cpaso 1, paso 2, hecho\u201d.",
        "mejor": "Esquina de vídeos, tutoriales, logo y perfil.",
        "colores": ["#000000", "#C6FF00", "#121212", "#D9A27E", "#FFFFFF", "#1E1E1E"],
        "nota": "Ideal como logo",
    },
    {
        "code": "P5", "estilo": "Élite", "edad": "Lujo oscuro",
        "vibe": "El empresario silencioso: elegante y sin presumir.",
        "habla": "Calmado y con autoridad, en tono bajo.",
        "mejor": "Dinero y finanzas, miniaturas de YouTube.",
        "colores": ["#0B0B0C", "#D4AF37", "#F5DE9A", "#1F1E22", "#C08E6A", "#2A2219"],
        "nota": "",
    },
]


def tarjeta(v):
    svg = (AQUI / "svg" / f"{v['code']}.svg").read_text(encoding="utf-8")
    svg = svg.replace('width="300" height="400"', 'role="img" aria-label="Personaje ' + v["code"] + '"', 1)
    swatches = "".join(
        f'<li><span style="background:{c}"></span><code>{c}</code></li>' for c in v["colores"]
    )
    nota = f'<p class="nota">{html.escape(v["nota"])}</p>' if v["nota"] else ""
    return f"""
    <article class="card" id="{v['code']}">
      <div class="art">{svg}</div>
      <div class="info">
        <div class="head"><span class="code">{v['code']}</span><span class="estilo">{html.escape(v['estilo'])}</span></div>
        {nota}
        <p class="vibe">{html.escape(v['vibe'])}</p>
        <dl>
          <dt>Estilo</dt><dd>{html.escape(v['edad'])}</dd>
          <dt>Habla</dt><dd>{html.escape(v['habla'])}</dd>
          <dt>Mejor para</dt><dd>{html.escape(v['mejor'])}</dd>
        </dl>
        <ul class="pal">{swatches}</ul>
      </div>
    </article>"""


def main():
    tarjetas = "".join(tarjeta(v) for v in VERSIONES)
    out = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pertx Personajes</title>
<style>
:root{{
  --bg:#F3F3F1; --surface:#FFFFFF; --line:#E2E2DE; --ink:#16181D; --ink-2:#5A5F6B; --accent:#C6FF00;
  --font:system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
}}
@media (prefers-color-scheme: dark){{
  :root:not([data-theme="light"]){{ --bg:#111318; --surface:#1A1D24; --line:#2A2E38; --ink:#F1F2F4; --ink-2:#A3A8B4; }}
}}
:root[data-theme="dark"]{{ --bg:#111318; --surface:#1A1D24; --line:#2A2E38; --ink:#F1F2F4; --ink-2:#A3A8B4; }}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:var(--font);line-height:1.45}}
header{{padding:28px 16px 8px;max-width:1500px;margin:0 auto}}
.kicker{{font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-2);margin:0}}
h1{{font-size:clamp(26px,4vw,40px);margin:6px 0 6px;letter-spacing:-.02em}}
header p{{margin:0;color:var(--ink-2);max-width:62ch}}
main{{max-width:1500px;margin:0 auto;padding:20px 16px 8px;
  display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:14px}}
@media (max-width:1100px){{ main{{grid-template-columns:repeat(auto-fill,minmax(250px,1fr))}} }}
.card{{background:var(--surface);border:1px solid var(--line);border-radius:16px;overflow:hidden;display:flex;flex-direction:column}}
.art svg{{display:block;width:100%;height:auto}}
.info{{padding:14px 14px 16px;display:flex;flex-direction:column;gap:8px}}
.head{{display:flex;align-items:baseline;gap:8px}}
.code{{font-size:26px;font-weight:800;letter-spacing:-.02em}}
.estilo{{font-weight:600;color:var(--ink-2)}}
.nota{{margin:0;font-size:12px;font-weight:700;align-self:flex-start;padding:3px 8px;border-radius:999px;background:var(--accent);color:#16181D}}
.vibe{{margin:0;font-weight:500}}
dl{{margin:0;display:grid;grid-template-columns:auto 1fr;gap:4px 10px;font-size:13px}}
dt{{color:var(--ink-2)}} dd{{margin:0}}
.pal{{list-style:none;margin:4px 0 0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:6px}}
.pal li{{display:flex;align-items:center;gap:6px;font-size:11px}}
.pal span{{width:16px;height:16px;border-radius:4px;border:1px solid rgba(0,0,0,.15);flex:none}}
.pal code{{font-family:ui-monospace,Menlo,Consolas,monospace;color:var(--ink-2)}}
footer{{max-width:1500px;margin:0 auto;padding:18px 16px 40px}}
.pregunta{{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:18px}}
.pregunta strong{{font-size:18px}}
.pregunta p{{margin:6px 0 0;color:var(--ink-2)}}
</style>
</head>
<body>
<header>
  <p class="kicker">Pertx · Etapa 1 · Personaje</p>
  <h1>5 versiones de Pertx · ronda 2</h1>
  <p>Oscuro y con la cara tapada. Dibujadas en código (SVG). Fichas completas con prompts en <code>FICHAS-PERSONAJE.md</code>.</p>
</header>
<main>{tarjetas}
</main>
<footer>
  <div class="pregunta">
    <strong>¿Qué versión eliges (P1-P5)? ¿Quieres mezclar algo de otra?</strong>
    <p>Ejemplo de respuesta: "P1, pero con el PX dorado de P5".</p>
  </div>
</footer>
</body>
</html>
"""
    (AQUI / "galeria.html").write_text(out, encoding="utf-8")
    print("Galería creada:", AQUI / "galeria.html")


if __name__ == "__main__":
    main()

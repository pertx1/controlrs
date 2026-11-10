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
        "code": "P1", "estilo": "3D suave", "edad": "19 años",
        "vibe": "El chaval majo que está empezando y se lo curra.",
        "habla": "Cercano y optimista, se ríe de sus fallos.",
        "mejor": "Ganchos, reacciones, emprender joven, miniaturas.",
        "colores": ["#F2A93B", "#1F2A44", "#5A3825", "#E8B894", "#6B8E4E", "#FF6B35"],
        "nota": "Mi favorito",
    },
    {
        "code": "P2", "estilo": "Anime", "edad": "18 años",
        "vibe": "El hacker prodigio que programa de noche.",
        "habla": "Seguro, rápido y un poco chulito.",
        "mejor": "Construir con IA en pantalla, retos de 24 h.",
        "colores": ["#121318", "#00E5FF", "#7A6FF0", "#16181D", "#2E3138", "#0E1530"],
        "nota": "",
    },
    {
        "code": "P3", "estilo": "Semi-realista", "edad": "24 años",
        "vibe": "Creador serio de escritorio nocturno.",
        "habla": "Calmado, directo y con números.",
        "mejor": "Miniaturas de YouTube largo, dinero.",
        "colores": ["#2B1F17", "#D9A57E", "#5C3B22", "#3A3A3C", "#FFB347", "#3D7BFF"],
        "nota": "No recomendado como cara principal",
    },
    {
        "code": "P4", "estilo": "Flat minimal", "edad": "Sin edad",
        "vibe": "Icono de marca simple y reconocible.",
        "habla": "Ordenado, humor seco, “tres pasos, sin rollo”.",
        "mejor": "Pantalla con personaje en esquina, carruseles, logo.",
        "colores": ["#2B59FF", "#1B1B1B", "#F1C6A0", "#E1E4EC", "#FF6B6B", "#EEF1FF"],
        "nota": "El más fácil de animar gratis",
    },
    {
        "code": "P5", "estilo": "Cartoon 2D", "edad": "22 años",
        "vibe": "Caos creativo, energía a tope.",
        "habla": "Hiperactivo y exagerado: “¡TÍO, MIRA ESTO!”",
        "mejor": "Humor, fails, disciplina siendo desordenado.",
        "colores": ["#FF7A00", "#7B2FF7", "#FFD23F", "#8EC5FF", "#FF3B3B", "#F0C08A"],
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
          <dt>Edad</dt><dd>{html.escape(v['edad'])}</dd>
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
  --bg:#F6F4EF; --surface:#FFFFFF; --line:#E4E0D6; --ink:#16181D; --ink-2:#5A5F6B; --accent:#F2A93B;
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
  <h1>5 versiones de Pertx</h1>
  <p>Dibujadas en código (SVG). Fichas completas con prompts en <code>FICHAS-PERSONAJE.md</code>.</p>
</header>
<main>{tarjetas}
</main>
<footer>
  <div class="pregunta">
    <strong>¿Qué versión eliges (P1-P5)? ¿Quieres mezclar algo de otra?</strong>
    <p>Ejemplo de respuesta: "P1, pero con las gafas de P5".</p>
  </div>
</footer>
</body>
</html>
"""
    (AQUI / "galeria.html").write_text(out, encoding="utf-8")
    print("Galería creada:", AQUI / "galeria.html")


if __name__ == "__main__":
    main()

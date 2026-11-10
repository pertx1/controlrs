"""Vídeo 2 · Formato F2 LA HERRAMIENTA · "Claude Code, mi opinión sincera" (38 s)."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from motor import (GOLD, CREMA, Video, escribiendo, panel, perfil_movil, texto)  # noqa: E402

v = Video("v02-la-herramienta", 38.0)
X, Y, PW, PH = 14, 92, 332, 250   # panel a lo ancho

# ---------- S1 · gancho (0 – 3.4) ----------
v.pertx(0, 3.4, 96, 140, .8, prop="portatil", ojos="decidido", blink_off=1.0)
trozos = [(20, 110, "function guardar()"), (226, 150, "if (gasto > 0)"), (18, 200, "total += gasto"), (240, 260, "return lista")]
for n, (x, y, t) in enumerate(trozos):
    v.add(0.2 + n * 0.35, 3.4, f'<rect x="{x}" y="{y-14}" width="{len(t)*6.4+16}" height="22" rx="6" fill="#13100C" stroke="#2E281E"/>'
          + texto(x + 8, y + 1, t, 9.5, GOLD, 600, mono=True), a="pop", flota=(2, 2.6 + n * .3))
    v.sfx.append((0.2 + n * 0.35, "pop"))
v.sub(0.1, 1.7, "esta IA programa", "dentro")
v.sub(1.7, 3.4, "de mi", "ordenador")
v.voz(0.1, 3.4, "Pertx", "Esta IA programa dentro de mi ordenador.")

# ---------- S2 · qué es (3.4 – 9) ----------
v.add(3.4, 16, panel(X, Y, PW, PH, "TERMINAL"), a="up")
v.add(3.7, 9, escribiendo(X + 14, Y + 44, "~/mi-proyecto $ claude", 3.7, 4.9, 11, CREMA))
v.add(5.2, 9, f'<rect x="{X+14}" y="{Y+60}" width="{PW-28}" height="62" rx="8" fill="none" stroke="{GOLD}" stroke-dasharray="3 3"/>'
      + texto(X + 28, Y + 84, "✻ Claude Code", 12, GOLD, 800, mono=True)
      + texto(X + 28, Y + 104, "¿En qué te ayudo hoy?", 10, CREMA, 500, mono=True), a="pop")
v.sfx.append((5.2, "ding"))
v.add(6.6, 9, texto(X + 14, Y + 150, "> _", 11, GOLD, 600, mono=True), a="fade")
v.pertx(3.4, 27, 18, 430, .42, ojos="normal", blink_off=.3)
v.auro(3.6, 27, 318, 64, .3, "feliz")
v.sub(3.5, 5.4, "se llama", "Claude Code")
v.sub(5.4, 7.2, "y trabaja en tu", "terminal")
v.sub(7.2, 9.0, "como un", "compañero")
v.voz(3.5, 9.0, "Pertx", "Se llama Claude Code, y trabaja en tu terminal, como un compañero.")

# ---------- S3 · le hablas y crea archivos (9 – 16) ----------
v.add(9.0, 16, f'<rect x="{X+96}" y="{Y+34}" width="{PW-106}" height="30" rx="12" fill="{GOLD}"/>'
      + texto(X + PW - 14, Y + 53, "Hazme una página de login", 10, "#13100C", 800, "end"), a="right")
v.sfx.append((9.1, "pop"))
archivos = [("login.html", "+38"), ("estilos.css", "+52"), ("auth.js", "+41")]
for n, (f, l) in enumerate(archivos):
    s = 10.6 + n * 0.7
    v.add(s, 16, f'<rect x="{X+14}" y="{Y+82+n*30}" width="{PW-28}" height="24" rx="6" fill="#1A1712"/>'
          + texto(X + 26, Y + 98 + n * 30, f"✓ {f}", 10, "#9FD17A", 700, mono=True)
          + texto(X + PW - 26, Y + 98 + n * 30, f"{l} líneas", 9, "#8A8070", 500, "end", mono=True), a="left")
    v.sfx.append((s, "pop"))
v.add(13.0, 16, escribiendo(X + 14, Y + 190, "Hecho. ¿Quieres que lo pruebe?", 13.0, 14.6, 10, CREMA), a="fade")
v.sub(9.1, 11.0, "le pides lo que", "necesitas")
v.sub(11.0, 13.2, "y él crea los", "archivos")
v.sub(13.2, 16, "y te pregunta antes de", "seguir")
v.voz(9.1, 16, "Pertx", "Le pides lo que necesitas, y él crea los archivos… y te pregunta antes de seguir.")

# ---------- S4 · lee todo el proyecto (16 – 22) ----------
v.add(16, 22, panel(X, Y, PW, PH, "LEYENDO PROYECTO"), a="fade")
ficheros = ["index.html", "estilos.css", "gastos.js", "auth.js", "base-de-datos.js", "README.md"]
for n, f in enumerate(ficheros):
    y = Y + 34 + n * 32
    v.add(16.1, 22, f'<rect x="{X+14}" y="{y}" width="{PW-28}" height="26" rx="6" fill="#141210"/>'
          + texto(X + 26, y + 17, f, 10, "#B3A994", 600, mono=True))
    s = 16.5 + n * 0.55
    v.add(s, 22, f'<rect x="{X+14}" y="{y}" width="{PW-28}" height="26" rx="6" fill="none" stroke="{GOLD}" stroke-width="1.5"/>'
          + texto(X + PW - 26, y + 17, "leído ✓", 9, GOLD, 700, "end", mono=True), a="fade", din=0.15)
v.auro(16, 22, 318, 64, .3, "pensativo")
v.sub(16.0, 18.0, "antes de tocar nada", "lee")
v.sub(18.0, 20.0, "todo tu", "proyecto")
v.sub(20.0, 22.0, "así no rompe lo que ya", "funciona")
v.voz(16.0, 22.0, "Pertx", "Antes de tocar nada, lee todo tu proyecto. Así no rompe lo que ya funciona.")

# ---------- S5 · cuánto cuesta (22 – 27) ----------
v.add(22, 27, panel(X, Y, PW, PH, "¿CUÁNTO CUESTA?") +
      f'<rect x="{X+30}" y="{Y+60}" width="{PW-60}" height="110" rx="14" fill="#1A1712" stroke="{GOLD}"/>'
      + texto(X + PW / 2, Y + 96, "INCLUIDO", 22, GOLD, 900, "middle")
      + texto(X + PW / 2, Y + 120, "en los planes de pago de Claude", 10, CREMA, 600, "middle")
      + texto(X + PW / 2, Y + 150, "(mira el precio actual en su web)", 8.5, "#8A8070", 500, "middle"), a="pop")
v.sfx.append((22.3, "ding"))
v.auro(22, 27, 318, 64, .3, "celebrando")
v.sub(22.1, 24.4, "va incluido en los", "planes de pago")
v.sub(24.4, 27.0, "de", "Claude")
v.voz(22.1, 27.0, "Pertx", "Va incluido en los planes de pago de Claude.")

# ---------- S6 · opinión sincera (27 – 33.5) ----------
v.pertx(27, 30.8, 70, 150, .8, ojos="pensativo", a="pop", blink_off=.5)
v.pertx(30.8, 33.5, 70, 150, .8, ojos="decidido", a="fade", blink_off=2.2)
v.auro(27.2, 33.5, 292, 170, .5, "pensativo")
v.sub(27.1, 29.0, "pero si no sabes qué quieres", "construir")
v.sub(29.0, 30.8, "no te", "sirve")
v.sub(30.8, 33.5, "y revisa siempre lo que", "hace")
v.voz(27.1, 33.5, "Pertx", "Pero si no sabes qué quieres construir, no te sirve. Y revisa siempre lo que hace.")

# ---------- S7 · CTA (33.5 – 38) ----------
v.add(33.5, 38, perfil_movil(), a="up", dout=0.4)
v.pertx(33.5, 38, 0, 150, .78, prop="senalar", ojos="feliz", blink_off=.8)
v.sfx.append((34.0, "pop"))
v.sub(33.6, 35.8, "sígueme y te enseño lo que", "construyo")
v.sub(35.8, 38, "¿qué hago", "primero?")
v.voz(33.6, 38, "Pertx", "Sígueme y te enseño todo lo que construyo con ella. ¿Qué hago primero?")

for t in (3.4, 9.0, 16.0, 22.0, 27.0, 33.5):
    v.sfx.append((t - 0.15, "whoosh"))

if __name__ == "__main__":
    out = v.render(pathlib.Path(__file__).resolve().parent.parent / "salida", solo_html="--html" in sys.argv)
    print("Hecho:", out)

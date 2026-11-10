"""Vídeo 1 · Formato F1 NOVATO VS PERTX · "Aprender a programar" (36 s)."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from motor import (GOLD, CREMA, Video, barra, escribiendo, etiqueta, panel, perfil_movil, texto)  # noqa: E402

v = Video("v01-novato-vs-pertx", 36.0)
L, R = 14, 188          # x de los paneles izquierdo y derecho
PW, PY, PH = 158, 92, 250

# ---------- persistente: línea central ----------
v.add(0, 27.5, '<path d="M180 70 V520" stroke="#D4AF37" stroke-width="1.6" opacity=".65"/>', dout=0.3)

# ---------- S1 · gancho (0 – 3.6) ----------
v.add(0, 3.6, texto(180, 62, "DÍA 1", 10, GOLD, 800, "middle", extra=' letter-spacing="2"') + barra(60, 70, 240, 0, 3.6, 0.05, 0.25))
v.pertx(0, 3.6, 8, 140, .78, ojos="normal", gris=True)
v.pertx(0, 3.6, 196, 140, .78, ojos="decidido", blink_off=1.3)
v.add(0.1, 3.6, etiqueta(58, 462, "NOVATO", oro=False, w=64) + etiqueta(238, 462, "PERTX", w=64), a="up")
v.sub(0.15, 1.8, "un novato y yo", "empezamos")
v.sub(1.8, 3.6, "a programar el", "mismo día")
v.voz(0.1, 3.6, "Pertx", "Un novato y yo empezamos a programar el mismo día.")

# ---------- S2 · el novato ve tutoriales (3.6 – 9.4) ----------
v.add(3.6, 22, panel(L, PY, PW, PH, "YOUTUBE"), a="left")
v.add(3.6, 9.4, panel(R, PY, PW, PH, "PERTX") + texto(R + PW / 2, PY + 130, "…", 30, "#3A3428", 800, "middle"), a="right")
tutoriales = ["Curso completo 0 a 100", "Tutorial 2: variables", "Tutorial 3: bucles", "Tutorial 4: funciones", "Tutorial 47: repaso"]
for n, t in enumerate(tutoriales):
    y = PY + 32 + n * 40
    card = (f'<rect x="{L+8}" y="{y}" width="{PW-16}" height="32" rx="6" fill="#1A1712" stroke="#2E281E"/>'
            f'<rect x="{L+14}" y="{y+6}" width="34" height="20" rx="3" fill="#2C2A30"/>'
            f'<path d="M{L+27} {y+11} L{L+36} {y+16} L{L+27} {y+21} Z" fill="{CREMA}"/>'
            + texto(L + 54, y + 15, t, 8.5, CREMA, 600) + texto(L + 54, y + 26, "1:32:10", 7.5, "#8A8070", 500))
    v.add(4.0 + n * 1.0, 22, card, a="up", dout=0.3)
    v.sfx.append((4.0 + n * 1.0, "pop"))
v.pertx(3.6, 27.5, 28, 430, .42, gris=True)
v.pertx(3.6, 27.5, 222, 430, .42, ojos="normal", blink_off=.4)
v.sub(3.7, 5.6, "el novato ve", "tutoriales")
v.sub(5.6, 7.4, "uno detrás de", "otro")
v.sub(7.4, 9.4, "y todavía no ha", "construido nada")
v.voz(3.7, 9.4, "Pertx", "El novato ve tutoriales, uno detrás de otro… y todavía no ha construido nada.")

# ---------- S3 · Pertx construye con Claude Code (9.4 – 16) ----------
v.add(9.4, 16, panel(R, PY, PW, PH, "TERMINAL"), a="right")
term = [(9.7, 10.3, "> claude"), (10.5, 11.9, "> hazme una web para"), (11.9, 12.8, "  apuntar mis gastos")]
for n, (s, e, t) in enumerate(term):
    v.add(s, 16, escribiendo(R + 10, PY + 42 + n * 16, t, s, e, 9.5, GOLD if n else CREMA))
for n, f in enumerate(["index.html", "estilos.css", "gastos.js"]):
    s = 13.2 + n * 0.5
    v.add(s, 16, texto(R + 10, PY + 104 + n * 16, f"✓ creado {f}", 9.5, "#9FD17A", 600, mono=True), a="left")
    v.sfx.append((s, "pop"))
v.add(14.9, 16, texto(R + 10, PY + 168, "Listo. ¿Lo revisamos juntos?", 8.5, CREMA, 500), a="up")
v.auro(9.6, 16, 318, 64, .3, "feliz")
v.sub(9.5, 11.3, "yo le pido a", "Claude Code")
v.sub(11.3, 13.2, "algo que", "necesito")
v.sub(13.2, 16, "y lo construimos", "juntos")
v.voz(9.5, 16, "Pertx", "Yo le pido a Claude Code algo que necesito… y lo construimos juntos.")

# ---------- S4 · copiar vs entender (16 – 22) ----------
v.add(16, 22, (f'<rect x="{L+10}" y="{PY+150}" width="{PW-20}" height="56" rx="8" fill="#3A0E0E" stroke="#E5484D"/>'
               + texto(L + PW / 2, PY + 172, "ERROR en la línea 12", 10, "#FF8A8A", 800, "middle")
               + texto(L + PW / 2, PY + 190, "(copiado del vídeo)", 8.5, "#FFB3B3", 500, "middle")), a="pop")
v.sfx.append((16.4, "error"))
v.add(16, 22, panel(R, PY, PW, PH, "CLAUDE CODE"), a="fade")
v.add(16.2, 22, (f'<rect x="{R+30}" y="{PY+36}" width="{PW-40}" height="38" rx="10" fill="{GOLD}"/>'
                 + texto(R + PW / 2 + 10, PY + 52, "¿Por qué esto", 9, "#13100C", 700, "middle")
                 + texto(R + PW / 2 + 10, PY + 65, "funciona así?", 9, "#13100C", 700, "middle")), a="right")
resp = [(17.6, 18.8, "Porque guarda cada"), (18.8, 19.8, "gasto en una lista"), (19.8, 20.8, "y luego los suma.")]
for n, (s, e, t) in enumerate(resp):
    v.add(s, 22, escribiendo(R + 12, PY + 98 + n * 15, t, s, e, 9, CREMA, mono=False))
v.auro(16, 22, 318, 64, .3, "pensativo")
v.sub(16.0, 17.8, "el novato copia y", "falla")
v.sub(17.8, 19.8, "yo pregunto por qué", "funciona")
v.sub(19.8, 22, "y así", "aprendo")
v.voz(16.0, 22, "Pertx", "El novato copia… y falla. Yo pregunto por qué funciona. Y así aprendo.")

# ---------- S5 · resultado (22 – 27.5) ----------
v.add(22, 27.5, panel(L, PY, PW, PH, "UN MES DESPUÉS") + "".join(
    f'<rect x="{L+20+n*6}" y="{PY+60+n*28}" width="{PW-50}" height="22" rx="4" fill="#2C2A30" stroke="#3A3640"/>'
    for n in range(5)) + texto(L + PW / 2, PY + 228, "MUCHA TEORÍA", 12, "#8A8070", 900, "middle"), a="left")
web = (panel(R, PY, PW, PH, "MIS GASTOS")
       + texto(R + 12, PY + 44, "Noviembre", 10, GOLD, 800)
       + "".join(f'<rect x="{R+10}" y="{PY+54+n*24}" width="{PW-20}" height="20" rx="5" fill="#1A1712"/>'
                 + texto(R + 18, PY + 68 + n * 24, a, 9, CREMA, 600) + texto(R + PW - 16, PY + 68 + n * 24, b, 9, CREMA, 600, "end")
                 for n, (a, b) in enumerate([("Café", "2,50 €"), ("Bus", "1,40 €"), ("Comida", "8,90 €")]))
       + f'<path d="M{R+10} {PY+132} H{R+PW-10}" stroke="#2E281E"/>'
       + texto(R + 18, PY + 150, "Total", 10, CREMA, 800) + texto(R + PW - 16, PY + 150, "12,80 €", 10, GOLD, 900, "end")
       + f'<rect x="{R+24}" y="{PY+180}" width="{PW-48}" height="30" rx="15" fill="{GOLD}"/>'
       + texto(R + PW / 2, PY + 199, "✓ FUNCIONA", 11, "#13100C", 900, "middle"))
v.add(22.2, 27.5, web, a="right")
v.sfx.append((24.2, "ding"))
v.auro(22, 27.5, 318, 64, .3, "feliz")
v.sub(22.1, 24.0, "un mes después él tiene", "teoría")
v.sub(24.0, 26.0, "y yo tengo algo", "que funciona")
v.sub(26.0, 27.5, "y que", "entiendo")
v.voz(22.1, 27.5, "Pertx", "Un mes después, él tiene teoría. Y yo tengo algo que funciona… y que entiendo.")

# ---------- S6 · moraleja (27.5 – 31.5) ----------
v.pertx(27.5, 31.5, 70, 150, .8, ojos="decidido", a="pop", blink_off=2.0)
v.auro(27.7, 31.5, 292, 170, .5, "senalando")
v.sub(27.6, 29.5, "no se aprende", "mirando")
v.sub(29.5, 31.5, "se aprende", "construyendo")
v.voz(27.6, 31.5, "Pertx", "No se aprende mirando. Se aprende construyendo.")

# ---------- S7 · CTA (31.5 – 36) ----------
perfil = perfil_movil()
v.add(31.5, 36, perfil, a="up", dout=0.4)
v.pertx(31.5, 36, 0, 150, .78, prop="senalar", ojos="feliz", blink_off=.8)
v.sfx.append((32.0, "pop"))
v.sub(31.6, 33.6, "sígueme y mira cómo", "construyo")
v.sub(33.6, 36, "¿y tú cómo estás", "aprendiendo?")
v.voz(31.6, 36, "Pertx", "Sígueme y mira cómo construyo. ¿Y tú, cómo estás aprendiendo?")

for t in (3.6, 9.4, 16.0, 22.0, 27.5, 31.5):
    v.sfx.append((t - 0.15, "whoosh"))

if __name__ == "__main__":
    out = v.render(pathlib.Path(__file__).resolve().parent.parent / "salida", solo_html="--html" in sys.argv)
    print("Hecho:", out)

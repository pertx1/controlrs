#!/usr/bin/env python3
"""Dibuja las 5 mascotas (M1-M5) junto a Pertx y crea galeria-mascota.html.

Uso (desde la carpeta del proyecto):  python3 personaje/hacer-mascotas.py
Crea: personaje/svg/P1-oro-cuerpo.svg, personaje/svg/M1.svg ... M5.svg
      y personaje/galeria-mascota.html
"""
import html
import pathlib
import sys

AQUI = pathlib.Path(__file__).parent
sys.path.insert(0, str(AQUI))
import pertx_cuerpo as pertx  # noqa: E402

W, H = 400, 400


# ---------- mascotas (dibujadas en el lado derecho, x 200-400) ----------

def m1(i):  # Cuervo
    return f"""
  <defs>
    <radialGradient id="{i}feat" cx="40%" cy="30%" r="75%"><stop offset="0" stop-color="#3A3640"/><stop offset=".5" stop-color="#16151A"/><stop offset="1" stop-color="#060607"/></radialGradient>
  </defs>
  <!-- pedestal -->
  <rect x="252" y="330" width="92" height="48" rx="4" fill="#0E0E10" stroke="#2C2A30" stroke-width="1.5"/>
  <path d="M252 330 H344" stroke="url(#{i}gold)" stroke-width="1.6"/>
  <text x="298" y="360" font-family="Georgia, serif" font-weight="700" font-size="14" fill="url(#{i}gold)" text-anchor="middle" letter-spacing="2">PX</text>
  <!-- patas -->
  <path d="M286 312 L284 330 M306 312 L308 330" stroke="#2A2620" stroke-width="3.5" stroke-linecap="round"/>
  <path d="M278 330 L292 330 M302 330 L316 330" stroke="#2A2620" stroke-width="3" stroke-linecap="round"/>
  <rect x="302" y="318" width="9" height="5" rx="2" fill="url(#{i}gold)"/>
  <!-- cola -->
  <path d="M262 296 L226 322 L250 320 L232 340 L262 324 L256 344 L284 312 Z" fill="#0A0A0C"/>
  <!-- cuerpo -->
  <path d="M258 300 Q246 244 290 228 Q334 222 340 262 Q342 296 318 314 L276 316 Z" fill="url(#{i}feat)"/>
  <!-- ala -->
  <path d="M266 270 Q284 244 318 252 Q312 284 286 306 Q262 304 266 270 Z" fill="#0B0B0D"/>
  <path d="M276 278 L304 262 M278 290 L306 274 M282 300 L304 288" stroke="#3A3640" stroke-width="1.4" opacity=".8"/>
  <!-- cabeza -->
  <circle cx="320" cy="222" r="24" fill="url(#{i}feat)"/>
  <path d="M300 206 Q312 192 330 198" stroke="#3A3640" stroke-width="2" fill="none" opacity=".7"/>
  <!-- pico -->
  <path d="M338 214 L372 226 L338 236 Z" fill="#141318"/>
  <path d="M338 226 L366 226" stroke="#2C2A30" stroke-width="1.2"/>
  <!-- ojo dorado con ceja -->
  <circle cx="324" cy="218" r="5.5" fill="#D4AF37"/>
  <circle cx="325" cy="218" r="2.6" fill="#0A0A0A"/>
  <circle cx="323" cy="216.5" r="1" fill="#FFF5D6"/>
  <path d="M314 210 L332 212" stroke="#060607" stroke-width="3" stroke-linecap="round"/>
  <!-- brillo -->
  <path d="M340 262 Q342 296 318 314" stroke="url(#{i}gold)" stroke-width="1.4" fill="none" opacity=".5"/>"""


def m2(i):  # Criatura de humo
    return f"""
  <defs>
    <radialGradient id="{i}smoke" cx="45%" cy="40%" r="60%"><stop offset="0" stop-color="#2A2830"/><stop offset=".7" stop-color="#0D0C10"/><stop offset="1" stop-color="#0D0C10" stop-opacity="0"/></radialGradient>
    <filter id="{i}wisp" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2.5"/></filter>
    <filter id="{i}eg" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <ellipse cx="300" cy="376" rx="40" ry="6" fill="#D4AF37" opacity=".12"/>
  <!-- estela de humo -->
  <path d="M286 300 Q270 330 290 346 Q304 358 292 372" stroke="#1A1920" stroke-width="16" fill="none" stroke-linecap="round" filter="url(#{i}wisp)" opacity=".9"/>
  <path d="M312 304 Q326 326 314 344" stroke="#1A1920" stroke-width="10" fill="none" stroke-linecap="round" filter="url(#{i}wisp)" opacity=".7"/>
  <!-- cuerpo -->
  <path d="M248 250 Q244 196 300 188 Q356 196 352 250 Q352 296 322 310 Q300 318 278 310 Q248 296 248 250 Z" fill="#0D0C10" filter="url(#{i}wisp)"/>
  <path d="M252 250 Q250 200 300 194 Q350 200 348 250 Q348 292 320 304 Q300 312 280 304 Q252 292 252 250 Z" fill="url(#{i}smoke)"/>
  <!-- cuernitos -->
  <path d="M266 204 L258 176 L280 196 Z" fill="#0D0C10"/>
  <path d="M334 204 L342 176 L320 196 Z" fill="#0D0C10"/>
  <path d="M258 176 L262 186 M342 176 L338 186" stroke="url(#{i}gold)" stroke-width="2" stroke-linecap="round"/>
  <!-- ojos de media luna, pícaros -->
  <path d="M268 240 Q282 226 296 240 Q282 236 268 240 Z" fill="#F5DE9A" filter="url(#{i}eg)"/>
  <path d="M304 240 Q318 226 332 240 Q318 236 304 240 Z" fill="#F5DE9A" filter="url(#{i}eg)"/>
  <!-- sonrisa dentada -->
  <path d="M276 264 L284 272 L292 264 L300 272 L308 264 L316 272 L324 264" stroke="#D4AF37" stroke-width="2.4" fill="none" stroke-linejoin="round" filter="url(#{i}eg)"/>
  <!-- brazitos de humo -->
  <path d="M250 262 Q232 268 230 252" stroke="#141319" stroke-width="9" fill="none" stroke-linecap="round" filter="url(#{i}wisp)"/>
  <path d="M350 262 Q370 270 374 252" stroke="#141319" stroke-width="9" fill="none" stroke-linecap="round" filter="url(#{i}wisp)"/>
  <!-- chispas -->
  <circle cx="240" cy="210" r="1.8" fill="#F5DE9A"/><circle cx="362" cy="224" r="1.4" fill="#F5DE9A"/><circle cx="350" cy="182" r="1.2" fill="#D4AF37"/>"""


def m3(i):  # Robot orbe
    return f"""
  <defs>
    <radialGradient id="{i}orb" cx="38%" cy="30%" r="75%"><stop offset="0" stop-color="#3A393E"/><stop offset=".55" stop-color="#151417"/><stop offset="1" stop-color="#050506"/></radialGradient>
    <radialGradient id="{i}thr" cx="50%" cy="0%" r="100%"><stop offset="0" stop-color="#F5DE9A"/><stop offset="1" stop-color="#D4AF37" stop-opacity="0"/></radialGradient>
    <filter id="{i}g" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <ellipse cx="300" cy="374" rx="34" ry="6" fill="#000" opacity=".6"/>
  <!-- propulsores -->
  <path d="M286 300 L280 334 L292 334 Z" fill="url(#{i}thr)" opacity=".8"/>
  <path d="M314 300 L308 334 L320 334 Z" fill="url(#{i}thr)" opacity=".8"/>
  <!-- antena -->
  <path d="M300 186 L300 166" stroke="#2C2A30" stroke-width="3"/>
  <circle cx="300" cy="162" r="5" fill="#D4AF37" filter="url(#{i}g)"/>
  <!-- esfera -->
  <circle cx="300" cy="244" r="58" fill="url(#{i}orb)"/>
  <ellipse cx="300" cy="262" rx="58" ry="12" fill="none" stroke="url(#{i}gold)" stroke-width="3"/>
  <path d="M242 262 A58 58 0 0 0 358 262" fill="#0A0A0B" opacity=".35"/>
  <!-- pantalla-cara -->
  <rect x="264" y="210" width="72" height="42" rx="16" fill="#050506" stroke="#2C2A30" stroke-width="1.5"/>
  <!-- ojos felices ^ ^ en píxeles -->
  <g fill="#F5DE9A" filter="url(#{i}g)">
    <rect x="276" y="230" width="5" height="5"/><rect x="281" y="225" width="5" height="5"/><rect x="286" y="230" width="5" height="5"/>
    <rect x="309" y="230" width="5" height="5"/><rect x="314" y="225" width="5" height="5"/><rect x="319" y="230" width="5" height="5"/>
  </g>
  <rect x="296" y="242" width="8" height="3" fill="#D4AF37"/>
  <!-- brillo -->
  <ellipse cx="282" cy="204" rx="16" ry="7" fill="#FFFFFF" opacity=".07" transform="rotate(-25 282 204)"/>
  <!-- holograma: gráfica subiendo -->
  <g transform="translate(334 150)">
    <rect x="0" y="0" width="54" height="36" rx="4" fill="#D4AF37" fill-opacity=".08" stroke="#D4AF37" stroke-opacity=".6"/>
    <path d="M6 28 L18 20 L28 24 L46 8" stroke="#F5DE9A" stroke-width="2" fill="none" filter="url(#{i}g)"/>
    <path d="M40 8 L46 8 L46 14" stroke="#F5DE9A" stroke-width="2" fill="none"/>
  </g>"""


def m4(i):  # Reloj de arena con vida
    return f"""
  <defs>
    <linearGradient id="{i}glass" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".05"/><stop offset=".3" stop-color="#FFFFFF" stop-opacity=".16"/><stop offset="1" stop-color="#FFFFFF" stop-opacity=".03"/></linearGradient>
  </defs>
  <ellipse cx="300" cy="378" rx="46" ry="6" fill="#000" opacity=".6"/>
  <!-- piernas y brazos finos dorados -->
  <path d="M286 344 L280 372 L270 374 M314 344 L320 372 L330 374" stroke="url(#{i}gold)" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M262 252 Q240 262 236 288 M338 252 Q360 240 362 214" stroke="url(#{i}gold)" stroke-width="3" fill="none" stroke-linecap="round"/>
  <circle cx="236" cy="290" r="4" fill="#D4AF37"/>
  <circle cx="362" cy="212" r="4" fill="#D4AF37"/>
  <!-- tapas -->
  <rect x="252" y="160" width="96" height="14" rx="4" fill="url(#{i}gold)"/>
  <rect x="252" y="332" width="96" height="14" rx="4" fill="url(#{i}gold)"/>
  <rect x="258" y="174" width="6" height="158" fill="#8E6E1E"/>
  <rect x="336" y="174" width="6" height="158" fill="#8E6E1E"/>
  <!-- cristal -->
  <path d="M268 174 L332 174 Q332 222 306 250 L306 256 Q332 284 332 332 L268 332 Q268 284 294 256 L294 250 Q268 222 268 174 Z" fill="#0B0B0D" stroke="#3A3640" stroke-width="2"/>
  <!-- arena -->
  <path d="M276 196 L324 196 Q320 226 302 246 L298 246 Q280 226 276 196 Z" fill="#D4AF37" opacity=".9"/>
  <path d="M299.2 246 L300.8 246 L300.8 314 L299.2 314 Z" fill="#F5DE9A"/>
  <path d="M272 330 Q286 304 300 300 Q314 304 328 330 Z" fill="#D4AF37"/>
  <path d="M268 174 L332 174 Q332 222 306 250 L306 256 Q332 284 332 332 L268 332 Q268 284 294 256 L294 250 Q268 222 268 174 Z" fill="url(#{i}glass)"/>
  <!-- cara en la parte de arriba: seria, cejas firmes -->
  <circle cx="288" cy="208" r="5" fill="#0A0A0A"/>
  <circle cx="312" cy="208" r="5" fill="#0A0A0A"/>
  <circle cx="289.5" cy="206.5" r="1.5" fill="#FFF5D6"/>
  <circle cx="313.5" cy="206.5" r="1.5" fill="#FFF5D6"/>
  <path d="M280 198 L294 202 M320 198 L306 202" stroke="#0A0A0A" stroke-width="3" stroke-linecap="round"/>
  <path d="M292 222 L308 222" stroke="#0A0A0A" stroke-width="2.6" stroke-linecap="round"/>"""


def m5(i):  # Gato negro
    return f"""
  <defs>
    <radialGradient id="{i}fur" cx="40%" cy="30%" r="75%"><stop offset="0" stop-color="#34323A"/><stop offset=".55" stop-color="#141317"/><stop offset="1" stop-color="#060607"/></radialGradient>
    <radialGradient id="{i}eye" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#F5DE9A"/><stop offset="1" stop-color="#C9971F"/></radialGradient>
  </defs>
  <ellipse cx="300" cy="378" rx="56" ry="7" fill="#000" opacity=".6"/>
  <!-- cola -->
  <path d="M340 366 Q384 360 380 318 Q378 290 356 284" stroke="#0B0B0D" stroke-width="13" fill="none" stroke-linecap="round"/>
  <!-- cuerpo sentado -->
  <path d="M258 376 Q246 310 274 270 L326 270 Q354 310 342 376 Z" fill="url(#{i}fur)"/>
  <path d="M276 376 L280 330 M324 376 L320 330" stroke="#060607" stroke-width="2" opacity=".8"/>
  <ellipse cx="282" cy="374" rx="12" ry="6" fill="#141317"/>
  <ellipse cx="318" cy="374" rx="12" ry="6" fill="#141317"/>
  <!-- collar con chapa PX -->
  <path d="M272 272 Q300 284 328 272" stroke="url(#{i}gold)" stroke-width="5" fill="none"/>
  <circle cx="300" cy="288" r="8" fill="url(#{i}gold)"/>
  <text x="300" y="291" font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="6.5" fill="#13100C" text-anchor="middle">PX</text>
  <!-- cabeza -->
  <path d="M262 196 L268 158 L290 184 Z" fill="#141317"/>
  <path d="M338 196 L332 158 L310 184 Z" fill="#141317"/>
  <path d="M268 166 L272 184 L284 186 Z M332 166 L328 184 L316 186 Z" fill="#3A2A22" opacity=".7"/>
  <ellipse cx="300" cy="226" rx="44" ry="40" fill="url(#{i}fur)"/>
  <!-- ojos dorados, mirada de "te estoy vigilando" -->
  <ellipse cx="282" cy="222" rx="10" ry="8" fill="url(#{i}eye)"/>
  <ellipse cx="318" cy="222" rx="10" ry="8" fill="url(#{i}eye)"/>
  <ellipse cx="282" cy="222" rx="2.4" ry="7" fill="#0A0A0A"/>
  <ellipse cx="318" cy="222" rx="2.4" ry="7" fill="#0A0A0A"/>
  <path d="M271 216 Q282 212 293 217 M307 217 Q318 212 329 216" stroke="#060607" stroke-width="3.5" fill="none" stroke-linecap="round"/>
  <circle cx="285" cy="219" r="1.4" fill="#FFF5D6"/><circle cx="321" cy="219" r="1.4" fill="#FFF5D6"/>
  <!-- nariz y boca -->
  <path d="M296 238 L304 238 L300 243 Z" fill="#3A2A22"/>
  <path d="M300 243 Q296 250 290 248 M300 243 Q304 250 310 248" stroke="#3A3640" stroke-width="1.6" fill="none"/>
  <!-- bigotes -->
  <path d="M276 242 L244 236 M276 247 L246 250 M324 242 L356 236 M324 247 L354 250" stroke="#8E8A80" stroke-width="1" opacity=".7"/>
  <!-- brillo dorado de borde -->
  <path d="M342 376 Q354 310 326 270" stroke="url(#{i}gold)" stroke-width="1.4" fill="none" opacity=".45"/>"""


MASCOTAS = [
    {
        "code": "M1", "prop": None, "nombre": "ONYX", "tipo": "Cuervo (animal real)", "dibujo": m1,
        "vibe": "Listo, observador y con humor negro. Siempre vigila.",
        "rol": "Recuerda la disciplina y suelta datos.",
        "colores": ["#16151A", "#060607", "#3A3640", "#D4AF37", "#141318", "#2A2620"],
        "nota": "Mi favorita",
    },
    {
        "code": "M2", "prop": None, "nombre": "NOX", "tipo": "Criatura de humo (inventada)", "dibujo": m2,
        "vibe": "Pícaro y caótico, nace de la sombra de Pertx.",
        "rol": "Pone las tentaciones y las excusas, y hace las bromas.",
        "colores": ["#0D0C10", "#2A2830", "#141319", "#F5DE9A", "#D4AF37", "#1A1920"],
        "nota": "",
    },
    {
        "code": "M3", "prop": None, "nombre": "AURO", "tipo": "Robot orbe (IA)", "dibujo": m3,
        "vibe": "Asistente IA leal, eficiente y algo pedante.",
        "rol": "Enseña los números y celebra las ventas.",
        "colores": ["#151417", "#3A393E", "#050506", "#D4AF37", "#F5DE9A", "#2C2A30"],
        "nota": "El más fácil de animar",
    },
    {
        "code": "M4", "prop": None, "nombre": "TEMPO", "tipo": "Reloj de arena (objeto con vida)", "dibujo": m4,
        "vibe": "Serio y estricto, cada grano de arena cuenta.",
        "rol": "Marca el tiempo, avisa de las tareas y de las fechas límite.",
        "colores": ["#D4AF37", "#8E6E1E", "#F5DE9A", "#0B0B0D", "#3A3640", "#0A0A0A"],
        "nota": "",
    },
    {
        "code": "M5", "prop": None, "nombre": "NERO", "tipo": "Gato negro (animal real)", "dibujo": m5,
        "vibe": "Elegante, vago y juzgón. Mira con desprecio.",
        "rol": "Reacciona con caras, juzga tus excusas y aprueba tus victorias.",
        "colores": ["#141317", "#34323A", "#060607", "#F5DE9A", "#C9971F", "#D4AF37"],
        "nota": "El más viral",
    },
]


def combo_svg(m):
    i = m["code"].lower()
    gdefs, bg = pertx.fondo(i, W, H)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <!-- {m['code']} · {m['nombre']} · {m['tipo']} · con Pertx -->
  <defs>{pertx.defs(i)}{gdefs}
  </defs>{bg}
  <g transform="translate(14 14) scale(.96)">{pertx.cuerpo(i, m['prop'])}
  </g>{m['dibujo'](i)}{pertx.badge(m['code'], m['nombre'], x=W - 98)}
</svg>
"""


CSS = """
:root{ --bg:#0E0C0A; --surface:#17140F; --line:#2E281E; --ink:#F3EEE3; --ink-2:#B3A994; --accent:#D4AF37;
  --font:system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }
@media (prefers-color-scheme: light){ :root:not([data-theme="dark"]){ --bg:#F4F1EA; --surface:#FFFFFF; --line:#E2DCCD; --ink:#16130E; --ink-2:#6A604C; } }
:root[data-theme="light"]{ --bg:#F4F1EA; --surface:#FFFFFF; --line:#E2DCCD; --ink:#16130E; --ink-2:#6A604C; }
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--font);line-height:1.45}
header,main,footer{max-width:1500px;margin:0 auto;padding-left:16px;padding-right:16px}
header{padding-top:28px}
.kicker{font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-2);margin:0}
h1{font-size:clamp(26px,4vw,40px);margin:6px 0;letter-spacing:-.02em}
header p{margin:0;color:var(--ink-2);max-width:66ch}
.hero{display:flex;gap:16px;align-items:center;margin-top:18px;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:12px}
.hero svg{width:120px;height:auto;border-radius:10px;flex:none}
.hero p{margin:0}
main{padding-top:18px;padding-bottom:8px;display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:14px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:16px;overflow:hidden;display:flex;flex-direction:column}
.art svg{display:block;width:100%;height:auto}
.info{padding:14px 14px 16px;display:flex;flex-direction:column;gap:8px}
.head{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}
.code{font-size:26px;font-weight:800;letter-spacing:-.02em}
.nombre{font-weight:700;color:var(--accent);letter-spacing:.06em}
.tipo{color:var(--ink-2);font-size:13px;width:100%}
.nota{margin:0;font-size:12px;font-weight:700;align-self:flex-start;padding:3px 8px;border-radius:999px;background:var(--accent);color:#16130E}
.vibe{margin:0;font-weight:500}
dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:4px 10px;font-size:13px}
dt{color:var(--ink-2)} dd{margin:0}
.pal{list-style:none;margin:4px 0 0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:6px}
.pal li{display:flex;align-items:center;gap:6px;font-size:11px}
.pal span{width:16px;height:16px;border-radius:4px;border:1px solid rgba(127,127,127,.35);flex:none}
.pal code{font-family:ui-monospace,Menlo,Consolas,monospace;color:var(--ink-2)}
footer{padding-top:18px;padding-bottom:40px}
.pregunta{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:18px}
.pregunta strong{font-size:18px}
.pregunta p{margin:6px 0 0;color:var(--ink-2)}
"""


def tarjeta(m, svg):
    svg = svg.replace(f'width="{W}" height="{H}"', f'role="img" aria-label="Pertx con la mascota {m["code"]}"', 1)
    sw = "".join(f'<li><span style="background:{c}"></span><code>{c}</code></li>' for c in m["colores"])
    nota = f'<p class="nota">{html.escape(m["nota"])}</p>' if m["nota"] else ""
    return f"""
    <article class="card" id="{m['code']}">
      <div class="art">{svg}</div>
      <div class="info">
        <div class="head"><span class="code">{m['code']}</span><span class="nombre">{m['nombre']}</span><span class="tipo">{html.escape(m['tipo'])}</span></div>
        {nota}
        <p class="vibe">{html.escape(m['vibe'])}</p>
        <dl><dt>Rol</dt><dd>{html.escape(m['rol'])}</dd></dl>
        <ul class="pal">{sw}</ul>
      </div>
    </article>"""


def main():
    svgdir = AQUI / "svg"
    solo = pertx.svg_solo()
    (svgdir / "P1-oro-cuerpo.svg").write_text(solo, encoding="utf-8")
    (svgdir / "P1-oro-escenas.svg").write_text(pertx.svg_escenas(), encoding="utf-8")
    tarjetas = []
    for m in MASCOTAS:
        s = combo_svg(m)
        (svgdir / f"{m['code']}.svg").write_text(s, encoding="utf-8")
        tarjetas.append(tarjeta(m, s))
    hero = solo.replace('width="300" height="400"', 'role="img" aria-label="Pertx de cuerpo completo"', 1)
    page = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pertx Mascotas</title>
<style>{CSS}</style>
</head>
<body>
<header>
  <p class="kicker">Pertx · Etapa 2 · Mascota</p>
  <h1>5 mascotas para Pertx</h1>
  <p>Todas en el mismo estilo oscuro y dorado que el personaje elegido. Fichas completas con prompts en <code>FICHAS-MASCOTA.md</code>.</p>
  <div class="hero">{hero}<p><strong>Personaje elegido:</strong> P1 Sombra con los colores de P5, de cuerpo completo. Por defecto va sin nada en la mano; solo lleva móvil o portátil si la escena lo pide.</p></div>
</header>
<main>{''.join(tarjetas)}
</main>
<footer>
  <div class="pregunta">
    <strong>¿Qué mascota eliges (M1-M5)?</strong>
    <p>Puedes mezclar, por ejemplo: "M5, pero con los ojos LED de M3".</p>
  </div>
</footer>
</body>
</html>
"""
    (AQUI / "galeria-mascota.html").write_text(page, encoding="utf-8")
    print("Hecho: svg/P1-oro-cuerpo.svg, svg/M1-M5.svg y galeria-mascota.html")


if __name__ == "__main__":
    main()

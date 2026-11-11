#!/usr/bin/env python3
"""Monta un vídeo de Pertx a partir de su guion (guiones/semana-XX/dia-NN.json).

Uso (desde la carpeta del proyecto; en Windows `npm run video -- 1 1` o `py video/montar.py 1 1`):

  python3 video/montar.py 1 1            # semana 1, día 1 → video/salida/semana-01/dia-01.mp4 (sin voz)
  python3 video/montar.py 1 1 --voz      # con las voces de video/voz/semana-01/ (créalas con video/voz.py)
  python3 video/montar.py 1 1 --html     # solo la previsualización .html (rápido)
  python3 video/montar.py 1 1b           # el vídeo B (píldora) del día 1 → dia-01b.mp4
  python3 video/montar.py 1 todos        # todos los días de la semana (A y B)

Cada escena del guion tiene una `plantilla` (ver guiones/ESQUEMA.md) que dice cómo se dibuja.
Los subtítulos salen solos de la voz: palabras de unión pequeñas + palabra clave grande en oro.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
import textwrap

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from motor import (CREMA, GOLD, RAIZ, Video, esc, leer_audio, movil, panel,  # noqa: E402
                   perfil_movil, texto, SR)

ROJO = "#E5484D"
VERDE = "#9FD17A"
GRIS = "#8A8070"
PENDIENTE = re.compile(r"\[[^\]]+\]")

# Palabras "de unión": van pequeñas encima de la palabra clave.
UNION = set("""a al ante con de del desde el en entre es esta este esto ha han hay la las le les lo los me mi mis muy
no nos o para pero por que qué se si sí sin su sus te tu tus un una uno y ya yo él ella eso son soy fue era ser
tan más menos cada como cómo cuando donde aquí así""".split())


# ------------------------------------------------------------ utilidades
def envolver(t: str, ancho: int) -> list[str]:
    return textwrap.wrap(t, ancho) or [""]


def lineas_svg(x, y, t, ancho, tam=10, color=CREMA, peso=600, anchor="start", interlinea=1.35):
    return "".join(texto(x, y + k * tam * interlinea, linea, tam, color, peso, anchor)
                   for k, linea in enumerate(envolver(t, ancho)))


def trozos_subtitulo(voz: str):
    """Parte la frase en trozos: (palabras de unión, palabra clave)."""
    voz = voz.replace("…", "… ")
    palabras = [p for p in voz.split() if p]
    trozos, peque = [], []
    for p in palabras:
        limpia = re.sub(r"[¿?¡!.,:;…\"«»()]", "", p).lower()
        sigla = re.sub(r"[^A-ZÁÉÍÓÚÑ]", "", p)
        if (limpia in UNION or len(limpia) <= 2) and not re.search(r"\d", limpia) and len(sigla) < 2:
            peque.append(p)
            continue
        trozos.append((" ".join(peque), p))
        peque = []
    if peque:
        if trozos:
            ult = trozos[-1]
            trozos[-1] = (ult[0], ult[1] + " " + " ".join(peque))
        else:
            trozos.append(("", " ".join(peque)))
    return trozos


def limpiar_clave(p: str) -> str:
    return re.sub(r"[.,:;…]+$", "", p).strip("«»\"").upper()


def pastilla(t: str, y=50):
    w = min(320, len(t) * 8.2 + 30)
    return (f'<rect x="{180 - w/2}" y="{y}" width="{w}" height="24" rx="12" fill="{GOLD}"/>'
            + texto(180, y + 16.5, t, 11.5, "#13100C", 900, "middle", extra=' letter-spacing=".5"'))


# ------------------------------------------------------------ plantillas
MANO = {None: (152, 218), "movil": (138, 138), "portatil": (158, 186), "senalar": (214, 137), "celebrar": (171, 46)}
POS_X = {"izquierda": 0, "centro": 70, "derecha": 140}


def p_pertx(v, s, e, es, p):
    """Pertx grande. params: posicion (izquierda/centro/derecha), mov (idle/habla/camina/salta),
    poses: [{"en": 0.5, "objeto": "celebrar", "ojos": "feliz", "mov": "salta"}] para cambiar de pose a mitad de escena."""
    pe = es.get("pertx") or {"ojos": "normal", "objeto": None}
    x = POS_X.get(p.get("posicion"), 0 if pe.get("objeto") == "senalar" else 70)
    mov0 = p.get("mov") or ("habla" if es.get("quien", "Pertx") == "Pertx" else "idle")
    tramos = [{"en": 0, "objeto": pe.get("objeto"), "ojos": pe.get("ojos", "normal"), "mov": mov0}] + p.get("poses", [])
    for k, tr in enumerate(tramos):
        a = s + (e - s) * tr["en"]
        b = s + (e - s) * tramos[k + 1]["en"] if k + 1 < len(tramos) else e
        v.pertx(a, b, x, 150, .8, prop=tr.get("objeto"), ojos=tr.get("ojos", "normal"), mov=tr.get("mov", "habla" if k else mov0),
                a="pop" if k == 0 and mov0 != "camina" else "fade", din=0.25 if k == 0 else 0.06, blink_off=s % 3)
        if k == 0:
            hx, hy = MANO.get(tr.get("objeto"), MANO[None])
            v._mano = (x + hx * .8, 150 + hy * .8)
    if es.get("auro"):
        v.auro(s, e, 292, 170, .5, es["auro"])


def p_contadores(v, s, e, es, p):
    items = p.get("items", [])[:3]
    for k, it in enumerate(items):
        y = 96 + k * 80
        svg = (f'<rect x="14" y="{y}" width="332" height="66" rx="14" fill="#13100C" stroke="#2E281E" stroke-width="1.5"/>'
               + texto(30, y + 25, it.get("etiqueta", ""), 11, GRIS, 800, extra=' letter-spacing="1.5"')
               + texto(30, y + 46, it.get("nota", ""), 9.5, "#B3A994", 500)
               + texto(330, y + 45, it.get("valor", ""), 28 if len(it.get("valor", "")) <= 9 else 20, GOLD, 900, "end"))
        v.add(s + 0.15 + k * 0.45, e, svg, a="left", din=0.3)
        v.sfx.append((s + 0.15 + k * 0.45, "pop"))


def p_tarjetas(v, s, e, es, p):
    items = p.get("items", [])[:5]
    paso = min(0.9, (e - s) * 0.6 / max(1, len(items)))
    for k, it in enumerate(items):
        y = 92 + k * 52
        svg = (f'<rect x="14" y="{y}" width="332" height="44" rx="10" fill="#13100C" stroke="#2E281E"/>'
               f'<rect x="14" y="{y}" width="5" height="44" rx="2" fill="{GOLD}"/>'
               + texto(30, y + 19, it.get("titulo", ""), 11.5, CREMA, 800)
               + texto(30, y + 35, it.get("sub", ""), 9.5, GOLD, 600))
        t0 = s + 0.1 + (k * paso if not it.get("ya") else 0)
        v.add(t0, e, svg, a="up", din=0.25)
        if not it.get("ya"):
            v.sfx.append((t0, "pop"))


def p_terminal(v, s, e, es, p):
    v.add(s, e, panel(14, 92, 332, 250, p.get("titulo", "TERMINAL")), a="up")
    lineas = p.get("lineas", [])[:11]
    if not lineas:
        return
    dur = (e - s) * 0.8 / len(lineas)
    for k, l in enumerate(lineas):
        t0 = s + 0.2 + k * dur
        color = VERDE if l.startswith("✓") else GOLD if l.startswith((">", "✻")) else CREMA
        v.add(t0, e, texto(28, 134 + k * 19, "", 10.5, color, 600, mono=True,
                           extra=f' data-type="{t0:.2f},{t0 + dur * 0.8:.2f}" data-full="{esc(l)}"'), din=0.05)


def p_chat(v, s, e, es, p):
    msgs = p.get("mensajes", [])[:4]
    y = 96
    paso = (e - s) * 0.6 / max(1, len(msgs))
    for k, m in enumerate(msgs):
        yo = m.get("de") == "yo"
        lin = envolver(m.get("texto", ""), 36)
        h = 16 + len(lin) * 14
        w = min(300, max(len(x) for x in lin) * 6.1 + 26)
        x = 346 - w if yo else 14
        fondo, color = (GOLD, "#13100C") if yo else ("#1F1E22", CREMA)
        svg = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fondo}"/>'
               + "".join(texto(x + 13, y + 20 + j * 14, l, 10, color, 600) for j, l in enumerate(lin)))
        v.add(s + 0.1 + k * paso, e, svg, a="right" if yo else "left")
        v.sfx.append((s + 0.1 + k * paso, "pop"))
        y += h + 10


def p_partida(v, s, e, es, p):
    v.add(s, e, '<path d="M180 84 V470" stroke="#D4AF37" stroke-width="1.6" opacity=".65"/>', din=0.05, dout=0.05)
    v.add(s, e, f'<rect x="48" y="88" width="84" height="20" rx="10" fill="#2C2A30"/>' + texto(90, 102, "NOVATO", 9.5, "#B3A994", 800, "middle")
          + f'<rect x="228" y="88" width="84" height="20" rx="10" fill="{GOLD}"/>' + texto(270, 102, "PERTX", 9.5, "#13100C", 800, "middle"),
          din=0.05, dout=0.05)
    for lado, x0, col, fondo in (("izquierda", 14, "#B3A994", "#1A1918"), ("derecha", 188, CREMA, "#13100C")):
        items = p.get(lado, [])[:5]
        paso = min(0.8, (e - s) * 0.55 / max(1, len(items)))
        for k, it in enumerate(items):
            y = 118 + k * 46
            lin = envolver(it, 24)
            borde = GOLD if lado == "derecha" else "#2E281E"
            svg = (f'<rect x="{x0}" y="{y}" width="158" height="38" rx="8" fill="{fondo}" stroke="{borde}"/>'
                   + "".join(texto(x0 + 79, y + 16 + j * 12 + (6 if len(lin) == 1 else 0), l, 9.5, col, 700, "middle") for j, l in enumerate(lin[:2])))
            t0 = s + 0.1 + k * paso
            v.add(t0, e, svg, a="left" if lado == "izquierda" else "right")
            v.sfx.append((t0, "pop"))
    v.pertx(s, e, 28, 430, .42, gris=True)
    pe = es.get("pertx") or {}
    v.pertx(s, e, 222, 430, .42, ojos=pe.get("ojos", "normal"), blink_off=.4)


def p_movil(v, s, e, es, p):
    if p.get("tipo", "perfil") == "perfil":
        v.add(s, e, perfil_movil(), a="up", dout=0.4)
        pe = es.get("pertx") or {}
        v.pertx(s, e, 0, 150, .78, prop="senalar", ojos=pe.get("ojos", "feliz"), blink_off=.8)
        return
    filas = p.get("filas", [])[:5]
    cont = (texto(60, 50, p.get("titulo", ""), 11, GOLD, 900, "middle")
            + "".join(f'<rect x="16" y="{62 + k * 26}" width="88" height="20" rx="5" fill="#1F1E22"/>'
                      + texto(22, 76 + k * 26, a, 8, CREMA, 600) + texto(98, 76 + k * 26, b, 8, GOLD, 700, "end")
                      for k, (a, b) in enumerate(filas))
            + (f'<rect x="20" y="184" width="80" height="22" rx="11" fill="{GOLD}"/>' + texto(60, 199, p["boton"], 9, "#13100C", 800, "middle")
               if p.get("boton") else ""))
    v.add(s, e, movil(120, 90, 1.0, cont), a="up")


def p_auro(v, s, e, es, p):
    lineas = p.get("lineas", [])[:3]
    if lineas:
        svg = (f'<rect x="40" y="88" width="280" height="{30 + 44 * len(lineas)}" rx="14" fill="#D4AF37" fill-opacity=".07" stroke="{GOLD}" stroke-opacity=".6"/>'
               + "".join(texto(180, 128 + k * 44, l, 26 if len(l) <= 12 else 18, GOLD if k else "#F5DE9A", 900, "middle") for k, l in enumerate(lineas)))
        v.add(s + 0.1, e, svg, a="pop")
    v.auro(s, e, 180, 300, .62, es.get("auro") or "feliz")


def p_lista(v, s, e, es, p):
    pasos = p.get("pasos", [])[:5]
    activo = p.get("activo", -1)
    for k, t in enumerate(pasos):
        y = 96 + k * 50
        on = k == activo
        hecho = activo >= 0 and k < activo
        svg = (f'<rect x="14" y="{y}" width="332" height="42" rx="10" fill="{"#1A1712" if on else "#100E0B"}" stroke="{GOLD if on else "#2E281E"}" stroke-width="{2 if on else 1}"/>'
               f'<circle cx="38" cy="{y + 21}" r="13" fill="{GOLD if on or hecho else "#2C2A30"}"/>'
               + texto(38, y + 26, "✓" if hecho else str(k + 1), 12, "#13100C" if on or hecho else "#8A8070", 900, "middle")
               + texto(62, y + 26, t, 12, CREMA if on else "#8A8070", 800 if on else 600))
        v.add(s, e, svg, a="pop" if on else "fade", din=0.2)
    if es.get("pertx"):
        pe = es["pertx"]
        v.pertx(s, e, 24, 430, .42, ojos=pe.get("ojos", "normal"), prop=pe.get("objeto") if pe.get("objeto") in ("movil", "portatil") else None)


def p_texto(v, s, e, es, p):
    palabras = p.get("palabras", [])[:4]
    paso = (e - s) * 0.75 / max(1, len(palabras))
    for k, t in enumerate(palabras):
        tam = 34 if len(t) <= 12 else 26 if len(t) <= 18 else 19
        v.add(s + k * paso, e, texto(180, 150 + k * 52, t, tam, GOLD if k == len(palabras) - 1 else CREMA, 900, "middle",
                                     extra=' stroke="#080706" stroke-width="5" paint-order="stroke"'), a="pop", din=0.12)
        v.sfx.append((s + k * paso, "pop"))


def poner_objetos(v, s, e, p):
    """params.objetos: [{"tipo","x","y","etiqueta","k","anim": pop|mano|izquierda|derecha|arriba|abajo,"en": 0.3,"gira","flota"}]
    params.lluvia: {"tipo": "moneda", "n": 8} → caen desde arriba."""
    for o in p.get("objetos", []):
        x, y = o.get("x", 180), o.get("y", 200)
        t0 = s + (e - s) * o.get("en", 0.15)
        anim = o.get("anim", "pop")
        dx, dy = {"izquierda": (-260, 0), "derecha": (260, 0), "arriba": (0, -320), "abajo": (0, 300)}.get(anim, (0, 0))
        if anim == "mano":
            dx, dy = v._mano[0] - x, v._mano[1] - y
        a = "pop" if anim == "pop" else "desde"
        v.objeto(t0, e, x, y, o["tipo"], o.get("etiqueta", ""), o.get("k", 1.0), a=a, dx=dx, dy=dy,
                 gira=o.get("gira", 0), flota=(3, 2.4) if o.get("flota", True) else None, din=0.45 if a == "desde" else 0.3)
    ll = p.get("lluvia")
    if ll:
        import random
        rnd = random.Random(int(s * 100))
        for k in range(ll.get("n", 8)):
            x = rnd.uniform(30, 330)
            y = rnd.uniform(140, 330)
            t0 = s + (e - s) * (0.1 + 0.5 * k / max(1, ll.get("n", 8)))
            v.objeto(t0, e, x, y, ll.get("tipo", "moneda"), "", rnd.uniform(.5, .8), a="desde", dx=0, dy=-y - 60,
                     gira=rnd.choice([-120, 120, 200, -200]), din=0.6)


PLANTILLAS = {"pertx": p_pertx, "contadores": p_contadores, "tarjetas": p_tarjetas, "terminal": p_terminal,
              "chat": p_chat, "partida": p_partida, "movil": p_movil, "auro": p_auro, "lista": p_lista, "texto": p_texto}
GRANDES = {"pertx", "movil", "auro", "partida"}   # plantillas que ya dibujan sus personajes


# ------------------------------------------------------------ montaje
def textos(obj):
    """Todos los textos que hay dentro de un guion (para buscar huecos [ASÍ])."""
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for x in obj.values():
            yield from textos(x)
    elif isinstance(obj, list):
        for x in obj:
            yield from textos(x)


def ident(dia) -> str:
    """1 → "01" (vídeo A) · "1b" → "01b" (vídeo B, la píldora de las 13:00)."""
    m = re.fullmatch(r"(\d+)([a-z]?)", str(dia).strip().lower())
    if not m:
        sys.exit(f"Día no válido: {dia} (usa 1, 01, 1b…)")
    return f"{int(m.group(1)):02d}{m.group(2)}"


def ruta_guion(sem, dia):
    return RAIZ / "guiones" / f"semana-{sem:02d}" / f"dia-{ident(dia)}.json"


def ruta_voz(sem, dia, k):
    return RAIZ / "video" / "voz" / f"semana-{sem:02d}" / f"dia-{ident(dia)}-{k:02d}.mp3"


def tiempos(g, sem, dia, con_voz):
    """Devuelve [(inicio, fin, ruta_voz | None)]. Con voz, cada escena dura lo que su audio + un respiro."""
    out, t = [], 0.0
    for k, es in enumerate(g["escenas"], 1):
        a, b = es["t"]
        ruta = ruta_voz(sem, dia, k)
        if con_voz and ruta.exists():
            dur = max(1.4, len(leer_audio(ruta, robot=es.get("quien") == "Auro")) / SR + 0.3)
        else:
            dur, ruta = b - a, None
        out.append((round(t, 2), round(t + dur, 2), ruta))
        t += dur
    return out


def montar(sem: int, dia, con_voz=False, solo_html=False):
    g = json.loads(ruta_guion(sem, dia).read_text(encoding="utf-8"))
    pend = sorted({m for t in textos(g["escenas"]) for m in PENDIENTE.findall(t)})
    if pend:
        print(f"  ⏳ Día {dia}: aún tiene datos pendientes {', '.join(pend)}. Se monta como BORRADOR.")
    ts = tiempos(g, sem, dia, con_voz)
    v = Video(f"dia-{ident(dia)}", ts[-1][1])
    voces = []
    for (s, e, ruta), es in zip(ts, g["escenas"]):
        plant = es.get("plantilla", "pertx")
        prm = es.get("params", {})
        v.fondo(s, e, prm.get("fondo"))
        v._mano = (191, 324)
        PLANTILLAS[plant](v, s, e, es, prm)
        poner_objetos(v, s, e, prm)
        if plant not in GRANDES:
            if es.get("pertx") and plant != "lista":
                pe = es["pertx"]
                prop = pe.get("objeto") if pe.get("objeto") in ("movil", "portatil") else None
                v.pertx(s, e, 24, 430, .42, ojos=pe.get("ojos", "normal"), prop=prop, blink_off=s % 2,
                        mov="habla" if es.get("quien", "Pertx") == "Pertx" else "idle")
            if es.get("auro"):
                v.auro(s, e, 318, 64, .3, es["auro"])
        elif plant in ("partida", "movil") and es.get("auro"):
            v.auro(s, e, 318, 64, .3, es["auro"])
        if es.get("texto") and plant not in ("texto", "partida"):
            v.add(s, e, pastilla(" · ".join(es["texto"])), a="down", din=0.2)
        # subtítulos: reparto proporcional a las letras de cada trozo
        trozos = trozos_subtitulo(es["voz"])
        total = sum(len(a) + len(b) + 4 for a, b in trozos) or 1
        t, util = s + 0.05, (e - s) - 0.15
        for peque, clave in trozos:
            d = util * (len(peque) + len(clave) + 4) / total
            v.sub(round(t, 2), round(t + d, 2), peque, limpiar_clave(clave))
            t += d
        if es.get("sonido"):
            v.sfx.append((max(0, s - 0.1), es["sonido"]))
        if ruta:
            voces.append((s + 0.05, e, ruta, es.get("quien") == "Auro"))
        v.guion.append((s, e, es.get("quien", "Pertx"), es["voz"]))
    if pend:
        v.add(0, v.dur, texto(340, 38, "BORRADOR", 9, ROJO, 900, "end", extra=' letter-spacing="1.5"'))
    v.voces_fijas = voces
    carpeta = RAIZ / "video" / "salida" / f"semana-{sem:02d}"
    final = v.render(carpeta, solo_html=solo_html, con_voz=con_voz)
    return final


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        sys.exit(__doc__)
    sem = int(args[0])
    dias = ([p.stem.split("-")[1] for p in sorted((RAIZ / "guiones" / f"semana-{sem:02d}").glob("dia-*.json"))]
            if args[1] == "todos" else [ident(args[1])])
    for d in dias:
        print(f"Semana {sem} · día {d}…")
        print("  Hecho:", montar(sem, d, con_voz="--voz" in sys.argv, solo_html="--html" in sys.argv))

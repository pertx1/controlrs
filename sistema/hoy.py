#!/usr/bin/env python3
"""npm run hoy · Qué publicar, qué preparar y qué tarea hacer HOY.

Uso:
  npm run hoy                          # hoy
  npm run hoy -- 2026-11-30            # como si fuera ese día (para mirar el futuro)
  npm run hoy -- --empezar 2026-11-24  # guarda la fecha del DÍA 1 (el primer día que publicas)
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CONFIG = RAIZ / "sistema" / "config.json"
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
PEND = re.compile(r"\[[^\]]+\]")

# Tareas fijas de cada día de la semana (además de la del proyecto)
RUTINA = {
    0: "Lee la sección NECESITO DE TI y pásame esos datos hoy, así la semana sale sin parones.",
    1: "15 min contestando comentarios y mensajes de los vídeos (nunca datos personales).",
    2: "Busca 3 negocios sin web en Google Maps y apúntalos (lista de clientes de Pertx Studio).",
    3: "15 min viendo vídeos de tu nicho: apunta 2 ganchos o formatos que te llamen la atención.",
    4: "Escribe los guiones de la semana que viene en Claude Code: /guiones-semana {sig}",
    5: "Revisa que los vídeos de la semana que viene están montados (npm run video -- {sig} todos).",
    6: "Métricas de la semana: npm run metricas -- crear {sem}, rellénalas y luego en Claude Code: /metricas-semana {sem}",
}


def cargar_config() -> dict:
    if CONFIG.exists():
        return json.loads(CONFIG.read_text(encoding="utf-8"))
    return {"fecha_inicio": None, "hora_publicar": "19:00", "redes": ["TikTok", "Instagram"]}


def guardar_config(c: dict):
    CONFIG.parent.mkdir(parents=True, exist_ok=True)
    CONFIG.write_text(json.dumps(c, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def calendario() -> dict[int, dict]:
    ruta = RAIZ / "estrategia" / "calendario-30.csv"
    return {int(f["dia"]): f for f in csv.DictReader(ruta.open(encoding="utf-8"))}


def guion(n: int, b: str = "") -> dict | None:
    """b = "" para el vídeo principal (19:00) o "b" para la píldora (13:00)."""
    sem = (n - 1) // 7 + 1
    ruta = RAIZ / "guiones" / f"semana-{sem:02d}" / f"dia-{n:02d}{b}.json"
    return json.loads(ruta.read_text(encoding="utf-8")) if ruta.exists() else None


def textos(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            yield from textos(v)
    elif isinstance(o, list):
        for v in o:
            yield from textos(v)


def estado_video(n: int, b: str = "") -> tuple[str, list[str], list[str]]:
    """(resumen, pasos que faltan, datos pendientes del usuario)"""
    sem = (n - 1) // 7 + 1
    g = guion(n, b)
    if not g or not g.get("escenas"):
        return "sin guion", [f"Escribir el guion{' de la píldora' if b else ''}: en Claude Code → /guiones-semana {sem}"], []
    pend = sorted({m for t in textos(g["escenas"]) for m in PEND.findall(t)})
    voz = [RAIZ / "video" / "voz" / f"semana-{sem:02d}" / f"dia-{n:02d}{b}-{k:02d}.mp3" for k in range(1, len(g["escenas"]) + 1)]
    mp4 = RAIZ / "video" / "salida" / f"semana-{sem:02d}" / f"dia-{n:02d}{b}.mp4"
    pasos = []
    if pend:
        pasos.append("Pasarme los datos que faltan (abajo)")
    if not all(v.exists() for v in voz):
        pasos.append(f"Voz: npm run voz -- {sem} {n}{b}")
    if not mp4.exists():
        pasos.append(f"Montar: npm run video -- {sem} {n}{b} --voz")
    resumen = "✅ listo para publicar" if not pasos else ("⏳ faltan datos" if pend else "🎬 falta producirlo")
    datos = g.get("necesita_de_ti") or ([f"Datos que faltan en el guion: {', '.join(pend)}"] if pend else [])
    return resumen, pasos, datos


def tarea_proyecto(hoy: dt.date) -> str | None:
    """Una tarea pendiente del PLAN.md, rotando cada día."""
    plan = (RAIZ / "PLAN.md").read_text(encoding="utf-8")
    pend = [re.sub(r"\*\*|`", "", l.strip()[6:]) for l in plan.splitlines() if l.strip().startswith("- [ ]")]
    return pend[hoy.toordinal() % len(pend)] if pend else None


def linea(t=""):
    print(t)


def main():
    args = sys.argv[1:]
    c = cargar_config()
    if "--empezar" in args:
        fecha = args[args.index("--empezar") + 1]
        dt.date.fromisoformat(fecha)
        c["fecha_inicio"] = fecha
        guardar_config(c)
        print(f"Guardado: el DÍA 1 es el {fecha}.")
        return
    hoy = dt.date.fromisoformat(args[0]) if args else dt.date.today()

    linea("━" * 52)
    linea(f" PERTX · {DIAS[hoy.weekday()]} {hoy.strftime('%d/%m/%Y')}")
    linea("━" * 52)

    if not c.get("fecha_inicio"):
        linea("\n🧱 TODAVÍA NO HAS EMPEZADO A PUBLICAR")
        linea("  1. Crea y calienta las cuentas (CUENTAS.md).")
        linea("  2. Cuando sepas el primer día de publicación:  npm run hoy -- --empezar AAAA-MM-DD")
        t = tarea_proyecto(hoy)
        if t:
            linea(f"\n✅ TAREA DE HOY (del PLAN)\n  {t}")
        linea("")
        return

    inicio = dt.date.fromisoformat(c["fecha_inicio"])
    n = (hoy - inicio).days + 1
    if n < 1:
        linea(f"\n⏳ Faltan {1 - n} días para el DÍA 1 ({inicio.strftime('%d/%m')}).")
        linea("  Mientras: calienta las cuentas y prepara los vídeos de la semana 1:")
        for d in range(1, 8):
            res, pasos, _ = estado_video(d)
            linea(f"   · Día {d}: {res}" + (f" → {pasos[0]}" if pasos else ""))
        linea("")
        return

    sem = (n - 1) // 7 + 1
    cal = calendario()
    f = cal.get(n, {})
    g = guion(n)
    linea(f" Día {n} · semana {sem}" + (f" · {f.get('serie', '')}" if f else ""))

    # 1. Publicar hoy
    linea("\n📤 PUBLICAR HOY " + f"({' + '.join(c.get('redes', []))})")
    hechos = 0
    for b, hora, nombre in (("b", c.get("hora_pildora", "13:00"), "Píldora"), ("", c.get("hora_publicar", "19:00"), "Vídeo principal")):
        gb = guion(n, b)
        if not gb:
            continue
        hechos += 1
        res, pasos, _ = estado_video(n, b)
        linea(f"  {hora} · {nombre}: «{gb['titulo']}» · {res}")
        for p in pasos:
            linea(f"   → {p}")
        linea("  Descripción para copiar:")
        linea("  " + gb["descripcion"])
        linea("  " + " ".join(gb["hashtags"]))
    if hechos:
        linea("  ⚠️ Activa la etiqueta de IA al publicar. La historia va con el vídeo de las 19:00.")
    elif f:
        linea(f"  «{f['titulo']}» · sin guion → en Claude Code: /guiones-semana {sem}")
    else:
        linea(f"  Fuera del calendario de 30 días → pídeme el siguiente mes y /guiones-semana {sem}")

    # 2. Preparar los próximos días
    linea("\n🎬 PREPARAR (próximos 3 días)")
    necesito = []
    for d in range(n + 1, n + 4):
        res, pasos, datos = estado_video(d)
        titulo = (guion(d) or cal.get(d) or {}).get("titulo", "—")
        linea(f"  Día {d} · {titulo} · {res}")
        for p in pasos[:2]:
            linea(f"     → {p}")
        res_b, pasos_b, _ = estado_video(d, "b")
        linea(f"     + píldora · {res_b}" + (f" → {pasos_b[0]}" if pasos_b else ""))
        necesito += [f"Día {d}: {x}" for x in datos]

    # 3. Lo que necesito de ti esta semana
    for d in range(n + 4, n + 8):
        _, _, datos = estado_video(d)
        necesito += [f"Día {d}: {x}" for x in datos]
    if necesito:
        linea("\n✍️  NECESITO DE TI (próximos 7 días)")
        for x in dict.fromkeys(necesito):
            linea(f"  · {x}")

    # 4. Tareas
    linea("\n✅ TAREAS DE HOY")
    linea("  · " + RUTINA[hoy.weekday()].format(sem=sem, sig=sem + 1))
    t = tarea_proyecto(hoy)
    if t:
        linea(f"  · Del plan: {t}")
    linea("")


if __name__ == "__main__":
    main()

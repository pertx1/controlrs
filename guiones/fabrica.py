#!/usr/bin/env python3
"""Fábrica de guiones de Pertx.

Uso (desde la carpeta del proyecto; en Windows usa `py` o `python` en vez de `python3`):

  python3 guiones/fabrica.py semana 1     # crea guiones/semana-01/ con un esqueleto por día (sale del calendario)
  python3 guiones/fabrica.py revisar 1    # revisa los guiones: ritmo de voz, duración, gancho, líneas rojas, pendientes
  python3 guiones/fabrica.py fichas 1     # crea las fichas .md (para leer y grabar) y el resumen de la semana

Cada guion es un .json (lo rellena Claude con el comando /guiones-semana) y su ficha .md se genera sola.
El formato está explicado en guiones/ESQUEMA.md.
"""
from __future__ import annotations

import csv
import json
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
GUIONES = RAIZ / "guiones"
CALENDARIO = RAIZ / "estrategia" / "calendario-30.csv"

MAX_PAL_SEG = 3.0        # palabras por segundo como máximo en una escena (la voz va a ~2,5)
MAX_ESCENA = 7.0         # segundos máximos de una escena (la imagen tiene que cambiar a menudo)
MAX_GANCHO = 4.5         # la primera escena (gancho) termina antes de esto
DUR_MIN, DUR_MAX = 20, 60

# Líneas rojas (DIRECCION.md). Se buscan como palabras sueltas, sin distinguir mayúsculas.
PROHIBIDAS = [
    "akerra", "bilbao", "bizkaia", "vizcaya", "euskadi", "país vasco", "pais vasco", "vasco", "vasca",
    "15 años", "quince años", "instituto de", "colegio de",
    "política", "politica", "partido", "religión", "religion", "dios",
    "cripto", "bitcoin", "trading", "forex", "dinero rápido", "dinero rapido", "hazte rico",
    "garantizado", "100% seguro",
]
PENDIENTE = re.compile(r"\[[^\]]+\]")
sys.path.insert(0, str(RAIZ / "video"))
from objetos import TIPOS as OBJETOS  # noqa: E402
PLANTILLAS = {"pertx", "contadores", "tarjetas", "terminal", "chat", "partida", "movil", "auro", "lista", "texto"}


def carpeta(n: int) -> pathlib.Path:
    return GUIONES / f"semana-{n:02d}"


def palabras(t: str) -> int:
    return len([p for p in re.split(r"\s+", PENDIENTE.sub("X", t.strip())) if p])


# ---------------------------------------------------------------- semana
def cmd_semana(n: int):
    filas = list(csv.DictReader(CALENDARIO.open(encoding="utf-8")))
    dias = [f for f in filas if (int(f["dia"]) - 1) // 7 + 1 == n]
    if not dias:
        sys.exit(f"El calendario no tiene la semana {n}. Añade días a estrategia/calendario-30.csv.")
    c = carpeta(n)
    c.mkdir(parents=True, exist_ok=True)
    creados = 0
    for f in dias:
        ruta = c / f"dia-{int(f['dia']):02d}.json"
        if ruta.exists():
            continue
        esqueleto = {
            "dia": int(f["dia"]), "dia_semana": f["dia_semana"], "serie": f["serie"], "formato": f["formato"],
            "pilar": f["pilar"], "titulo": f["titulo"], "duracion": 0,
            "ganchos": [f["gancho"], "", ""], "gancho_elegido": 0,
            "escenas": [],
            "descripcion": "", "hashtags": [], "cta": f["cta"],
            "necesita_de_ti": [] if f["necesita_de_ti"].strip().lower() == "nada" else [f["necesita_de_ti"]],
            "etiqueta_ia": True, "estado": "esqueleto",
        }
        ruta.write_text(json.dumps(esqueleto, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        creados += 1
    print(f"Semana {n}: {creados} esqueletos nuevos en {c.relative_to(RAIZ)} ({len(dias)} días).")


# ---------------------------------------------------------------- revisar
def revisar_guion(g: dict) -> tuple[list[str], list[str], list[str]]:
    errores, avisos, pendientes = [], [], []
    esc = g.get("escenas", [])
    if not esc:
        return [f"día {g.get('dia')}: no tiene escenas"], [], []
    if len([x for x in g.get("ganchos", []) if x.strip()]) < 3:
        errores.append("faltan ganchos (tienen que ser 3)")
    fin_anterior = 0.0
    for k, e in enumerate(esc, 1):
        a, b = e["t"]
        if abs(a - fin_anterior) > 0.05:
            errores.append(f"escena {k}: empieza en {a} s y la anterior acaba en {fin_anterior} s")
        if b - a > MAX_ESCENA:
            errores.append(f"escena {k}: dura {b-a:.1f} s (máximo {MAX_ESCENA}); pártela en dos")
        pps = palabras(e.get("voz", "")) / max(0.1, b - a)
        if pps > MAX_PAL_SEG:
            errores.append(f"escena {k}: {pps:.1f} palabras/s (máximo {MAX_PAL_SEG}); quita palabras o dale más tiempo")
        if not e.get("texto"):
            avisos.append(f"escena {k}: no tiene texto en pantalla")
        for o in (e.get("params") or {}).get("objetos", []) + ([(e.get("params") or {})["lluvia"]] if (e.get("params") or {}).get("lluvia") else []):
            if o.get("tipo") not in OBJETOS:
                errores.append(f"escena {k}: el objeto «{o.get('tipo')}» no existe")
        if e.get("plantilla", "pertx") not in PLANTILLAS:
            errores.append(f"escena {k}: plantilla «{e.get('plantilla')}» no existe ({', '.join(sorted(PLANTILLAS))})")
        if not e.get("visual"):
            errores.append(f"escena {k}: falta 'visual' (qué se ve)")
        fin_anterior = b
    if esc[0]["t"][1] > MAX_GANCHO:
        errores.append(f"el gancho dura {esc[0]['t'][1]} s (tiene que acabar antes de {MAX_GANCHO} s)")
    dur = esc[-1]["t"][1]
    if abs(dur - g.get("duracion", dur)) > 0.05:
        avisos.append(f"'duracion' dice {g.get('duracion')} s pero las escenas acaban en {dur} s")
    if not DUR_MIN <= dur <= DUR_MAX:
        errores.append(f"dura {dur} s (entre {DUR_MIN} y {DUR_MAX})")
    if not 3 <= len(g.get("hashtags", [])) <= 6:
        errores.append("tiene que llevar entre 3 y 6 hashtags")
    if not g.get("descripcion"):
        errores.append("falta la descripción")
    if not g.get("etiqueta_ia"):
        errores.append("etiqueta_ia tiene que ser true (Pertx y su voz son IA)")
    todo = json.dumps(g, ensure_ascii=False).lower()
    for p in PROHIBIDAS:
        if re.search(r"(?<!\w)" + re.escape(p) + r"(?!\w)", todo):
            errores.append(f"línea roja: aparece «{p}»")
    for e in esc:
        for m in PENDIENTE.findall(e.get("voz", "") + " " + " ".join(e.get("texto", []))):
            pendientes.append(m)
    for m in PENDIENTE.findall(g.get("titulo", "") + " " + g.get("descripcion", "")):
        pendientes.append(m)
    return errores, avisos, sorted(set(pendientes))


def cmd_revisar(n: int) -> bool:
    ok = True
    for ruta in sorted(carpeta(n).glob("dia-*.json")):
        g = json.loads(ruta.read_text(encoding="utf-8"))
        err, av, pend = revisar_guion(g)
        estado = "❌" if err else ("⏳" if pend else "✅")
        print(f"{estado} {ruta.name} · {g['titulo']}")
        for x in err:
            print("    ERROR:", x)
        for x in av:
            print("    aviso:", x)
        if pend:
            print("    pendiente de ti:", ", ".join(pend))
        ok = ok and not err
    return ok


# ---------------------------------------------------------------- fichas
def ficha_md(g: dict) -> str:
    esc = g["escenas"]
    gancho = g["ganchos"][g.get("gancho_elegido", 0)]
    filas = []
    for e in esc:
        a, b = e["t"]
        p = e.get("pertx") or {}
        quien = e.get("quien", "Pertx")
        personaje = []
        if p:
            personaje.append(f"Pertx: ojos {p.get('ojos', 'normal')}" + (f", {p['objeto']}" if p.get("objeto") else ""))
        if e.get("auro"):
            personaje.append(f"Auro: {e['auro']}")
        grabar = e.get("grabar") or "—"
        filas.append(f"| {a:g}–{b:g} s | **{quien}:** {e['voz']} | {e['visual']}{' · ' + ' · '.join(personaje) if personaje else ''} | "
                     f"{' / '.join('**' + t + '**' for t in e.get('texto', []))} | {grabar} |")
    err, _av, pend = revisar_guion(g)
    estado = "❌ Tiene errores (ver `revisar`)" if err else ("⏳ Faltan datos tuyos" if pend else "✅ Listo para producir")
    otros = [x for k, x in enumerate(g["ganchos"]) if k != g.get("gancho_elegido", 0)]
    necesita = "\n".join(f"- [ ] {x}" for x in g.get("necesita_de_ti", [])) or "- Nada: lo hago yo todo."
    pend_txt = ("\n\n**Datos que faltan (cámbialos por tus datos reales):** " + ", ".join(f"`{x}`" for x in pend)) if pend else ""
    return f"""# Día {g['dia']} · {g['dia_semana']} · {g['titulo']}

**Serie:** {g['serie']} · **Formato:** {g['formato']} · **Pilar:** {g['pilar']} · **Duración:** {esc[-1]['t'][1]:g} s · **Estado:** {estado}

## Gancho elegido
> {gancho}

Otros ganchos para probar: {' · '.join(f'«{x}»' for x in otros)}

## Guion
| Tiempo | Voz | Qué se ve | Texto en pantalla | Qué grabas tú |
|---|---|---|---|---|
{chr(10).join(filas)}

## Para publicar
**Descripción:**
```
{g['descripcion']}

{' '.join(g['hashtags'])}
```
**CTA:** {g['cta']} · **Etiqueta de IA:** {'sí, actívala' if g.get('etiqueta_ia') else 'NO'}

## Lo que necesito de ti
{necesita}{pend_txt}
"""


def cmd_fichas(n: int):
    c = carpeta(n)
    resumen = [f"# Semana {n} · guiones", "", "| Día | Serie | Título | Duración | Estado | Necesito de ti |", "|---|---|---|---|---|---|"]
    for ruta in sorted(c.glob("dia-*.json")):
        g = json.loads(ruta.read_text(encoding="utf-8"))
        if not g.get("escenas"):
            continue
        (c / ruta.name.replace(".json", ".md")).write_text(ficha_md(g), encoding="utf-8")
        err, _av, pend = revisar_guion(g)
        estado = "❌" if err else ("⏳ faltan datos" if pend else "✅")
        nec = "; ".join(g.get("necesita_de_ti", [])) or "Nada"
        resumen.append(f"| [{g['dia']} · {g['dia_semana']}]({ruta.name.replace('.json', '.md')}) | {g['serie']} | {g['titulo']} | "
                       f"{g['escenas'][-1]['t'][1]:g} s | {estado} | {nec} |")
    (c / "README.md").write_text("\n".join(resumen) + "\n", encoding="utf-8")
    print(f"Fichas creadas en {c.relative_to(RAIZ)}")


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in {"semana", "revisar", "fichas"}:
        sys.exit(__doc__)
    num = int(sys.argv[2])
    {"semana": cmd_semana, "fichas": cmd_fichas}.get(sys.argv[1], lambda x: sys.exit(0 if cmd_revisar(x) else 1))(num)

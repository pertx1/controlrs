#!/usr/bin/env python3
"""Métricas semanales de Pertx.

  npm run metricas -- crear 1      # crea metricas/semana-01-videos.csv y semana-01-negocio.csv para rellenar
  npm run metricas -- analizar 1   # crea metricas/analisis-semana-01.md (luego, en Claude Code: /metricas-semana 1)

Rellena los CSV con Excel, Google Sheets o el Bloc de notas. Los datos salen de las estadísticas de TikTok
(Ver estadísticas de cada vídeo) e Instagram (Estadísticas del reel). Si un dato no lo sabes, déjalo vacío.
"""
from __future__ import annotations

import csv
import json
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CARPETA = RAIZ / "metricas"
REDES = ["TikTok", "Instagram"]
COL_VIDEO = ["dia", "titulo", "serie", "red", "visualizaciones", "porcentaje_visto_completo", "tiempo_medio_s",
             "likes", "comentarios", "compartidos", "guardados", "seguidores_ganados"]
NEGOCIO = [
    ("seguidores_tiktok_total", "Seguidores totales en TikTok el domingo"),
    ("seguidores_instagram_total", "Seguidores totales en Instagram el domingo"),
    ("emails_nuevos", "Emails nuevos en MailerLite esta semana"),
    ("visitas_web", "Visitas a la web (Vercel → Analytics), si lo sabes"),
    ("ventas_guia", "Guías vendidas"),
    ("negocios_contactados", "Negocios a los que has ofrecido web"),
    ("respuestas_negocios", "Negocios que han respondido"),
    ("clientes_nuevos", "Clientes que han dicho que sí"),
    ("euros_webs", "€ cobrados por webs esta semana"),
    ("euros_apps", "€ ganados con apps esta semana"),
    ("horas_trabajadas", "Horas que le has dedicado a Pertx"),
    ("aprendizaje", "Lo que has aprendido esta semana (una frase)"),
]


def rutas(n):
    return CARPETA / f"semana-{n:02d}-videos.csv", CARPETA / f"semana-{n:02d}-negocio.csv"


def crear(n: int):
    CARPETA.mkdir(exist_ok=True)
    rv, rn = rutas(n)
    if rv.exists() or rn.exists():
        sys.exit(f"Ya existen las métricas de la semana {n}. Ábrelas y rellénalas: {rv.relative_to(RAIZ)}")
    filas = []
    for d in range(7 * (n - 1) + 1, 7 * n + 1):
        g = RAIZ / "guiones" / f"semana-{n:02d}" / f"dia-{d:02d}.json"
        datos = json.loads(g.read_text(encoding="utf-8")) if g.exists() else {}
        for red in REDES:
            filas.append({"dia": d, "titulo": datos.get("titulo", ""), "serie": datos.get("serie", ""), "red": red})
    with rv.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COL_VIDEO)
        w.writeheader()
        w.writerows(filas)
    with rn.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["dato", "valor", "que_es"])
        for k, desc in NEGOCIO:
            w.writerow([k, "", desc])
    print(f"Creadas:\n  {rv.relative_to(RAIZ)}\n  {rn.relative_to(RAIZ)}\nRellénalas y luego: npm run metricas -- analizar {n}")


def num(x):
    try:
        return float(str(x).replace("%", "").replace(",", ".").strip())
    except ValueError:
        return None


def leer(n):
    rv, rn = rutas(n)
    if not rv.exists():
        return None, None
    videos = list(csv.DictReader(rv.open(encoding="utf-8-sig")))
    negocio = {r["dato"]: r["valor"] for r in csv.DictReader(rn.open(encoding="utf-8-sig"))} if rn.exists() else {}
    return videos, negocio


def analizar(n: int):
    videos, negocio = leer(n)
    if videos is None:
        sys.exit(f"No hay métricas de la semana {n}. Primero: npm run metricas -- crear {n}")
    for v in videos:
        for k in COL_VIDEO[4:]:
            v[k] = num(v.get(k))
    con_datos = [v for v in videos if v["visualizaciones"]]
    if not con_datos:
        sys.exit("Las métricas están vacías. Rellena al menos las visualizaciones.")

    # Por vídeo (sumando redes)
    por_video = {}
    for v in con_datos:
        p = por_video.setdefault(v["dia"], {"titulo": v["titulo"], "serie": v["serie"], "vis": 0, "seg": 0, "int": 0, "visto": []})
        p["vis"] += v["visualizaciones"] or 0
        p["seg"] += v["seguidores_ganados"] or 0
        p["int"] += sum(v[k] or 0 for k in ("likes", "comentarios", "compartidos", "guardados"))
        if v["porcentaje_visto_completo"] is not None:
            p["visto"].append(v["porcentaje_visto_completo"])
    for p in por_video.values():
        p["eng"] = 100 * p["int"] / p["vis"] if p["vis"] else 0
        p["visto_m"] = sum(p["visto"]) / len(p["visto"]) if p["visto"] else None
        p["seg_1000"] = 1000 * p["seg"] / p["vis"] if p["vis"] else 0

    # Por red
    por_red = {}
    for v in con_datos:
        r = por_red.setdefault(v["red"], {"vis": 0, "seg": 0})
        r["vis"] += v["visualizaciones"] or 0
        r["seg"] += v["seguidores_ganados"] or 0

    # Por serie
    por_serie = {}
    for p in por_video.values():
        s = por_serie.setdefault(p["serie"].split(" · ")[0] or "—", [])
        s.append(p)

    top = sorted(por_video.items(), key=lambda kv: kv[1]["vis"], reverse=True)
    top_seg = sorted(por_video.items(), key=lambda kv: kv[1]["seg_1000"], reverse=True)
    out = [f"# Métricas · semana {n}", ""]
    tot_vis = sum(p["vis"] for p in por_video.values())
    tot_seg = sum(p["seg"] for p in por_video.values())
    out += [f"**Visualizaciones:** {tot_vis:,.0f} · **Seguidores ganados:** {tot_seg:,.0f} · **Vídeos con datos:** {len(por_video)}".replace(",", "."), ""]

    out += ["## Vídeos (TikTok + Instagram)", "", "| Día | Vídeo | Visualizaciones | % visto entero | Interacción | Seguidores | Seg. cada 1.000 vis. |", "|---|---|---|---|---|---|---|"]
    for d, p in top:
        visto = f"{p['visto_m']:.0f} %" if p["visto_m"] is not None else "—"
        out.append(f"| {d} | {p['titulo']} | {p['vis']:,.0f} | {visto} | {p['eng']:.1f} % | {p['seg']:,.0f} | {p['seg_1000']:.1f} |".replace(",", "."))

    out += ["", "## Por red", "", "| Red | Visualizaciones | Seguidores ganados |", "|---|---|---|"]
    for red, r in por_red.items():
        out.append(f"| {red} | {r['vis']:,.0f} | {r['seg']:,.0f} |".replace(",", "."))

    out += ["", "## Por serie (media por vídeo)", "", "| Serie | Vídeos | Visualizaciones | Seguidores |", "|---|---|---|---|"]
    for s, lst in sorted(por_serie.items(), key=lambda kv: -sum(p["vis"] for p in kv[1]) / len(kv[1])):
        out.append(f"| {s} | {len(lst)} | {sum(p['vis'] for p in lst) / len(lst):,.0f} | {sum(p['seg'] for p in lst) / len(lst):,.1f} |".replace(",", "."))

    if negocio:
        out += ["", "## Negocio", "", "| Dato | Valor |", "|---|---|"]
        for k, desc in NEGOCIO:
            out.append(f"| {desc} | {negocio.get(k) or '—'} |")

    # Conclusiones automáticas (sencillas; el análisis bueno lo hago yo con /metricas-semana)
    rec = []
    if top:
        rec.append(f"**Vídeo que más ha llegado:** día {top[0][0]} «{top[0][1]['titulo']}». Repite su gancho y su formato.")
    if top_seg and top_seg[0][1]["seg"]:
        rec.append(f"**Vídeo que más seguidores convierte:** día {top_seg[0][0]} «{top_seg[0][1]['titulo']}».")
    vistos = [p["visto_m"] for p in por_video.values() if p["visto_m"] is not None]
    if vistos and sum(vistos) / len(vistos) < 25:
        rec.append("**El % visto entero es bajo** (< 25 %): ganchos más cortos y cambiar la imagen antes (cada 2 s).")
    if tot_vis and tot_seg / tot_vis * 1000 < 2:
        rec.append("**Pocos seguidores por visualización:** el CTA tiene que dar una razón para seguir (la serie, el contador).")
    out += ["", "## Conclusiones rápidas", ""] + [f"- {r}" for r in rec]
    out += ["", f"> Para el análisis completo y los cambios del calendario: en Claude Code → `/metricas-semana {n}`"]

    destino = CARPETA / f"analisis-semana-{n:02d}.md"
    destino.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Hecho: {destino.relative_to(RAIZ)}")


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("crear", "analizar"):
        sys.exit(__doc__)
    (crear if sys.argv[1] == "crear" else analizar)(int(sys.argv[2]))

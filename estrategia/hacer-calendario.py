#!/usr/bin/env python3
"""Crea estrategia/CALENDARIO-30.md a partir de estrategia/calendario-30.csv.

Uso (desde la carpeta del proyecto):  python3 estrategia/hacer-calendario.py
Edita siempre el CSV (es la fuente) y vuelve a ejecutar esto.
"""
import csv
import pathlib

AQUI = pathlib.Path(__file__).parent

filas = list(csv.DictReader((AQUI / "calendario-30.csv").open(encoding="utf-8")))
out = ["# PERTX · Calendario de los primeros 30 días", "",
       "El **día 1** es el primer lunes después de los 5 días de calentamiento. Un vídeo al día.",
       "La columna **Necesito de ti** dice qué me tienes que pasar o grabar para ese vídeo (si pone *Nada*, lo hago yo todo).",
       "", "> Fuente: `calendario-30.csv`. Si cambias algo, edita el CSV y ejecuta `python3 estrategia/hacer-calendario.py`.", ""]
semana = 0
for f in filas:
    d = int(f["dia"])
    s = (d - 1) // 7 + 1
    if s != semana:
        semana = s
        out += ["", f"## Semana {s}", "", "| Día | Serie | Título | Gancho (0–3 s) | CTA | Necesito de ti |", "|---|---|---|---|---|---|"]
    out.append(f"| **{d}** · {f['dia_semana']} | {f['serie']} | {f['titulo']} | {f['gancho']} | {f['cta']} | {f['necesita_de_ti']} |")
(AQUI / "CALENDARIO-30.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("Hecho:", AQUI / "CALENDARIO-30.md")

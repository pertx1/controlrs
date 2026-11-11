#!/usr/bin/env python3
"""Genera las voces de un guion con ElevenLabs (una por escena) y las guarda en video/voz/semana-XX/.

Uso (desde la carpeta del proyecto; en Windows `npm run voz -- 1 1`):

  python3 video/voz.py 1 1          # semana 1, día 1: te dice cuántos caracteres gasta y te pregunta antes
  python3 video/voz.py 1 1 --si     # sin preguntar
  python3 video/voz.py 1 todos      # todos los días de la semana

Necesita tu clave de ElevenLabs:
  - Ve a elevenlabs.io → tu perfil → API Keys → crea una.
  - Crea el archivo `video/.env` (no se sube a git) con esta línea:  ELEVENLABS_API_KEY=tu_clave
No regenera escenas que ya tienen audio (borra el .mp3 si quieres rehacerlo).
Las escenas con huecos [ASÍ] se saltan: primero rellena los datos.
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CONFIG = json.loads((RAIZ / "video" / "config.json").read_text(encoding="utf-8"))
PENDIENTE = re.compile(r"\[[^\]]+\]")


def clave() -> str:
    k = os.environ.get("ELEVENLABS_API_KEY", "")
    env = RAIZ / "video" / ".env"
    if not k and env.exists():
        for linea in env.read_text(encoding="utf-8").splitlines():
            if linea.startswith("ELEVENLABS_API_KEY="):
                k = linea.split("=", 1)[1].strip()
    if not k:
        sys.exit("Falta la clave de ElevenLabs. Crea video/.env con: ELEVENLABS_API_KEY=tu_clave (mira la ayuda arriba).")
    return k


def generar(texto: str, voz: str, destino: pathlib.Path, api_key: str):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voz}?output_format=mp3_44100_128"
    datos = json.dumps({"text": texto, "model_id": CONFIG["modelo"]}).encode("utf-8")
    req = urllib.request.Request(url, data=datos, method="POST",
                                 headers={"xi-api-key": api_key, "Content-Type": "application/json", "Accept": "audio/mpeg"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            destino.write_bytes(r.read())
    except urllib.error.HTTPError as e:
        sys.exit(f"ElevenLabs ha respondido {e.code}: {e.read().decode('utf-8', 'ignore')[:300]}")


def pendientes_del_dia(sem: int, dia: int):
    g = json.loads((RAIZ / "guiones" / f"semana-{sem:02d}" / f"dia-{dia:02d}.json").read_text(encoding="utf-8"))
    out = []
    for k, es in enumerate(g["escenas"], 1):
        destino = RAIZ / "video" / "voz" / f"semana-{sem:02d}" / f"dia-{dia:02d}-{k:02d}.mp3"
        if destino.exists():
            continue
        if PENDIENTE.search(es["voz"]):
            print(f"  día {dia} escena {k}: se salta (tiene datos pendientes)")
            continue
        voz = CONFIG["voces"].get(es.get("quien", "Pertx"), CONFIG["voces"]["Pertx"])
        out.append((es["voz"], voz["id"], destino))
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        sys.exit(__doc__)
    sem = int(args[0])
    dias = ([int(p.stem.split("-")[1]) for p in sorted((RAIZ / "guiones" / f"semana-{sem:02d}").glob("dia-*.json"))]
            if args[1] == "todos" else [int(args[1])])
    trabajo = [x for d in dias for x in pendientes_del_dia(sem, d)]
    if not trabajo:
        sys.exit("No hay voces que generar.")
    caracteres = sum(len(t) for t, _, _ in trabajo)
    print(f"Voy a generar {len(trabajo)} audios ({caracteres} caracteres de tu plan de ElevenLabs; "
          f"con el modelo {CONFIG['modelo']} suele gastar ~1 crédito por carácter).")
    if "--si" not in sys.argv and input("¿Sigo? (s/n) ").strip().lower() not in ("s", "si", "sí", "y"):
        sys.exit("Cancelado.")
    api_key = clave()
    for n, (texto, voz, destino) in enumerate(trabajo, 1):
        destino.parent.mkdir(parents=True, exist_ok=True)
        generar(texto, voz, destino, api_key)
        print(f"  {n}/{len(trabajo)} {destino.relative_to(RAIZ)}")
    print("Hecho. Ahora monta el vídeo con voz: python3 video/montar.py", sem, args[1], "--voz")

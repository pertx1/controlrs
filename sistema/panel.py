#!/usr/bin/env python3
"""Crea el panel de descarga de una semana: video/salida/semana-XX/panel.html

  npm run panel -- 1

El panel enseña cada día con su vídeo, su historia, la descripción para copiar, la encuesta para la historia
y una casilla de "publicado". Se publica como página privada (Artifact) con los vídeos y las historias dentro.
"""
from __future__ import annotations

import datetime as dt
import html
import json
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
PEND = re.compile(r"\[[^\]]+\]")

# Encuesta sugerida para la historia de cada día (si el guion no trae "encuesta")
ENCUESTAS = {
    1: ("¿Llegará Pertx a su primer euro con apps?", ["Sí", "Ni de broma"]),
    2: ("¿Has creado alguna web con IA?", ["Sí", "Todavía no"]),
    3: ("¿Tú eres novato o Pertx?", ["Novato", "Pertx"]),
    4: ("¿Lo consigue en 30 días?", ["Sí", "No"]),
    5: ("¿Tus prompts son de novato?", ["Un poco", "Para nada"]),
    6: ("¿Cuál de los 3 errores te ha pasado?", ["El margen", "Los envíos", "Dejar de publicar"]),
    7: ("¿Qué número quieres ver la semana que viene?", ["Seguidores", "Ventas", "Horas"]),
}


def textos(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            yield from textos(v)
    elif isinstance(o, list):
        for v in o:
            yield from textos(v)


def datos_semana(sem: int):
    salida = RAIZ / "video" / "salida" / f"semana-{sem:02d}"
    cfg = json.loads((RAIZ / "sistema" / "config.json").read_text(encoding="utf-8")) if (RAIZ / "sistema" / "config.json").exists() else {}
    inicio = dt.date.fromisoformat(cfg["fecha_inicio"]) if cfg.get("fecha_inicio") else None
    dias, ficheros = [], {}
    hora_a = cfg.get("hora_publicar", "19:00")
    rutas = sorted((RAIZ / "guiones" / f"semana-{sem:02d}").glob("dia-*.json"),
                   key=lambda r: (int(re.sub(r"\D", "", r.stem)), 0 if r.stem.endswith("b") else 1))
    for ruta in rutas:
        g = json.loads(ruta.read_text(encoding="utf-8"))
        ide = ruta.stem.split("-")[1]           # "01" (vídeo A) o "01b" (píldora)
        n = int(re.sub(r"\D", "", ide))
        pildora = g.get("tipo") == "pildora"
        pend = sorted({m for t in textos(g["escenas"]) for m in PEND.findall(t)})
        mp4 = salida / f"dia-{ide}.mp4"
        png = salida / f"historia-dia-{n:02d}.png"
        listo = mp4.exists() and not pend
        if listo:
            ficheros[f"videos/dia-{ide}.mp4"] = str(mp4)
        historia = png.exists() and not pildora
        if historia:
            ficheros[f"historias/historia-dia-{n:02d}.png"] = str(png)
        pregunta, opciones = ("", []) if pildora else (g.get("encuesta") or ENCUESTAS.get(n, ("", [])))
        fecha = (inicio + dt.timedelta(days=n - 1)).strftime("%d/%m") if inicio else ""
        dias.append({
            "n": n, "id": ide, "hora": g.get("hora", cfg.get("hora_pildora", "13:00")) if pildora else hora_a,
            "tipo": "Píldora" if pildora else "Vídeo principal",
            "dia": g.get("dia_semana", DIAS[(n - 1) % 7]), "fecha": fecha, "serie": g["serie"], "titulo": g["titulo"],
            "texto": g["descripcion"] + "\n\n" + " ".join(g["hashtags"]),
            "video": f"videos/dia-{ide}.mp4" if listo else None,
            "historia": f"historias/historia-dia-{n:02d}.png" if historia else None,
            "pregunta": pregunta, "opciones": opciones,
            "falta": (g.get("necesita_de_ti") or ([f"Datos: {', '.join(pend)}"] if pend else [])) if not listo else [],
        })
    return dias, ficheros


PLANTILLA = """<title>Panel de Pertx</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500;600;800&display=swap">
<style>
/* Layout: one column of day "slots" (like a publishing rundown), each pairing the vertical video with its story and copy. */
:root{
  --bg:#0B0907; --panel:#15110D; --panel-2:#1C1712; --line:#2E271D; --ink:#F3EEE3; --ink-2:#B3A994; --ink-3:#8A8070;
  --oro:#D4AF37; --oro-2:#F5DE9A; --ok:#9FD17A; --aviso:#E8A33D;
  --display:"Space Grotesk","Inter",system-ui,sans-serif; --texto:"Inter",system-ui,-apple-system,"Segoe UI",sans-serif;
  color-scheme:dark;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--texto);line-height:1.5;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.marco{max-width:920px;margin:0 auto;padding-block:28px 56px;display:grid;gap:22px}
header{display:grid;gap:6px}
.kicker{font:700 12px/1 var(--display);letter-spacing:.16em;text-transform:uppercase;color:var(--oro)}
h1{font:700 clamp(28px,6vw,40px)/1.05 var(--display);margin:0;text-wrap:balance}
.sub{color:var(--ink-2);margin:0;max-width:62ch}
.pasos{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 0;padding:0;list-style:none}
.pasos li{background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:6px 12px;font-size:13px;color:var(--ink-2)}
.pasos b{color:var(--oro)}
.dia{background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:16px;display:grid;grid-template-columns:200px 1fr;gap:18px}
.dia.hecho{opacity:.6}
.medios{display:grid;grid-template-columns:1fr;gap:10px}
video,.historia,.vacio{width:100%;aspect-ratio:9/16;border-radius:12px;background:#000;display:block;object-fit:cover}
.vacio{display:grid;place-items:center;text-align:center;padding:14px;color:var(--ink-3);font-size:13px;border:1px dashed var(--line);background:var(--panel-2)}
.info{display:grid;gap:12px;align-content:start;min-width:0}
.cab{display:flex;flex-wrap:wrap;align-items:baseline;gap:8px 12px}
.num{font:700 14px var(--display);color:var(--oro);letter-spacing:.06em;text-transform:uppercase}
.serie{font-size:11.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2);border:1px solid var(--line);border-radius:999px;padding:3px 9px}
h2{font:700 21px/1.2 var(--display);margin:0;text-wrap:balance}
.estado{font-size:12.5px;font-weight:800;border-radius:999px;padding:4px 10px;justify-self:start}
.estado.ok{background:rgba(159,209,122,.12);color:var(--ok)} .estado.falta{background:rgba(232,163,61,.13);color:var(--aviso)}
.texto{white-space:pre-wrap;background:var(--panel-2);border:1px solid var(--line);border-radius:12px;padding:12px;font-size:13.5px;color:var(--ink);margin:0;overflow-wrap:anywhere}
.encuesta{font-size:13.5px;color:var(--ink-2)} .encuesta b{color:var(--ink)}
.encuesta span{display:inline-block;border:1px solid var(--line);border-radius:999px;padding:2px 9px;margin:4px 6px 0 0;color:var(--oro-2)}
.botones{display:flex;flex-wrap:wrap;gap:8px}
.btn{font:700 14px var(--texto);border-radius:11px;padding:10px 14px;border:1px solid var(--oro);background:var(--oro);color:#13100C;text-decoration:none;cursor:pointer}
.btn.sec{background:transparent;color:var(--oro)}
.btn:focus-visible,.publicado input:focus-visible{outline:2px solid var(--oro-2);outline-offset:2px}
.publicado{display:flex;gap:8px;align-items:center;font-size:13.5px;color:var(--ink-2)}
.falta{margin:0;padding-left:18px;color:var(--aviso);font-size:13.5px}
.pie{color:var(--ink-3);font-size:12.5px}
@media (max-width:620px){.dia{grid-template-columns:1fr}.medios{grid-template-columns:1fr 1fr}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
<div class="marco">
  <header>
    <span class="kicker">Pertx · semana __SEM__</span>
    <h1>Lo que publicas esta semana</h1>
    <p class="sub">Cada día hay <b>2 vídeos</b>: la <b>píldora a las 13:00</b> y el <b>vídeo principal a las 19:00</b> (con su historia). Descarga, copia la descripción y publica en TikTok y en Reels de Instagram.</p>
    <ul class="pasos">
      <li><b>1</b> Descarga el vídeo</li><li><b>2</b> Súbelo a TikTok y a Reels</li><li><b>3</b> Pega la descripción</li>
      <li><b>4</b> Activa la etiqueta de IA</li><li><b>5</b> Sube la historia con la encuesta o el enlace</li>
    </ul>
  </header>
  <main id="dias" class="marco" style="padding:0"></main>
  <p class="pie">Los botones de descarga abren el archivo en otra pestaña: ahí lo guardas (en el móvil, mantén pulsado o usa ⋮ → Descargar). Las casillas de "publicado" solo se guardan en este navegador.</p>
</div>
<script>
const DIAS = __DATOS__;
const abs = (p) => new URL(p, location.href).href;
const clave = (n) => "pertx-publicado-__SEM__-" + n;
const leer = (k) => { try { return localStorage.getItem(k) === "1"; } catch { return false; } };
const guardar = (k, v) => { try { localStorage.setItem(k, v ? "1" : "0"); } catch {} };
const esc = (t) => String(t).replace(/[&<>"]/g, (c) => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));

function tarjeta(d) {
  const listo = !!d.video;
  const hecho = leer(clave(d.id));
  const el = document.createElement("article");
  el.className = "dia" + (hecho ? " hecho" : "");
  el.innerHTML = `
    <div class="medios">
      ${listo ? `<video controls preload="metadata" playsinline src="${esc(d.video)}"></video>` : `<div class="vacio">Vídeo pendiente</div>`}
      ${d.historia ? `<img class="historia" alt="Historia del día ${d.n}: ${esc(d.titulo)}" src="${esc(d.historia)}">` : ""}
    </div>
    <div class="info">
      <div class="cab"><span class="num">Día ${d.n} · ${esc(d.dia)}${d.fecha ? " · " + d.fecha : ""} · <b>${esc(d.hora)}</b> · ${esc(d.tipo)}</span><span class="serie">${esc(d.serie)}</span></div>
      <h2>${esc(d.titulo)}</h2>
      <span class="estado ${listo ? "ok" : "falta"}">${listo ? "Listo para publicar" : "Falta algo"}</span>
      ${d.falta.length ? `<ul class="falta">${d.falta.map((f) => `<li>${esc(f)}</li>`).join("")}</ul>` : ""}
      <pre class="texto" id="texto-${d.id}">${esc(d.texto)}</pre>
      ${d.pregunta ? `<div class="encuesta"><b>Encuesta para la historia:</b> ${esc(d.pregunta)}<br>${d.opciones.map((o) => `<span>${esc(o)}</span>`).join("")}</div>` : ""}
      <div class="botones">
        ${listo ? `<a class="btn" href="${abs(d.video)}" target="_blank" rel="noopener">Descargar vídeo</a>` : ""}
        ${d.historia ? `<a class="btn sec" href="${abs(d.historia)}" target="_blank" rel="noopener">Descargar historia</a>` : ""}
        <button class="btn sec" type="button" data-copiar="${d.id}">Copiar descripción</button>
      </div>
      <label class="publicado"><input type="checkbox" id="pub-${d.id}" ${hecho ? "checked" : ""}> Publicado</label>
    </div>`;
  el.querySelector("[data-copiar]").addEventListener("click", async (ev) => {
    const b = ev.currentTarget, pre = el.querySelector(".texto");
    try { await navigator.clipboard.writeText(d.texto); b.textContent = "Copiado"; }
    catch { const r = document.createRange(); r.selectNodeContents(pre); const s = getSelection(); s.removeAllRanges(); s.addRange(r); b.textContent = "Seleccionado: cópialo"; }
    setTimeout(() => (b.textContent = "Copiar descripción"), 2200);
  });
  el.querySelector("input").addEventListener("change", (ev) => { guardar(clave(d.id), ev.target.checked); el.classList.toggle("hecho", ev.target.checked); });
  return el;
}
const cont = document.getElementById("dias");
DIAS.forEach((d) => cont.appendChild(tarjeta(d)));
</script>
"""


def main(sem: int):
    dias, ficheros = datos_semana(sem)
    destino = RAIZ / "video" / "salida" / f"semana-{sem:02d}" / "panel.html"
    pagina = PLANTILLA.replace("__SEM__", str(sem)).replace("__DATOS__", json.dumps(dias, ensure_ascii=False))
    destino.write_text(pagina, encoding="utf-8")
    (destino.parent / "panel-ficheros.json").write_text(json.dumps(ficheros, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Hecho: {destino.relative_to(RAIZ)} · {sum(1 for d in dias if d['video'])} vídeos listos de {len(dias)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(int(sys.argv[1]))

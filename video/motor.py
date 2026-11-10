"""Motor de vídeo de Pertx: anima SVG en el navegador y lo exporta a MP4 9:16 (1080x1920).

Todo es gratis y local: Python dibuja, Chromium (Playwright) hace las fotos de cada
fotograma, ffmpeg monta el vídeo y la música/efectos se sintetizan con numpy.

Cómo se usa: mira video/videos/*.py. Cada vídeo crea un `Video`, le añade elementos
con tiempos y llama a `render()`.
"""
from __future__ import annotations

import html
import json
import math
import pathlib
import subprocess
import sys
import wave

import numpy as np

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "personaje"))
import auro as _auro  # noqa: E402
import pertx_cuerpo as _pertx  # noqa: E402

W, H = 360, 640          # espacio de dibujo (se exporta x3 = 1080x1920)
FPS = 30
GOLD, GOLD2, GOLD3 = "#D4AF37", "#F5DE9A", "#8E6E1E"
CREMA = "#F3EEE3"
FUENTE = "Inter, 'Arial Black', Arial, sans-serif"
SR = 44100


def esc(t):
    return html.escape(str(t), quote=True)


class Video:
    def __init__(self, nombre: str, duracion: float):
        self.nombre = nombre
        self.dur = duracion
        self.capas: list[str] = []
        self.sfx: list[tuple[float, str]] = []   # (segundo, "whoosh" | "ding" | "pop" | "error")
        self.guion: list[tuple[float, float, str, str]] = []  # (inicio, fin, quién, frase)

    # ---------- elementos ----------
    def add(self, s, e, svg, a="fade", din=0.25, dout=0.2, flota=None, extra=""):
        f = f' data-f="{flota[0]},{flota[1]}"' if flota else ""
        self.capas.append(
            f'<g data-s="{s}" data-e="{e}" data-a="{a}" data-din="{din}" data-dout="{dout}"{f}{extra} '
            f'style="opacity:0;transform-box:fill-box;transform-origin:center">{svg}</g>')

    def pertx(self, s, e, x, y, k, prop=None, ojos="normal", gris=False, a="fade", blink_off=0.0):
        cuerpo = _pertx.cuerpo("v", prop, ojos)
        parpadeo = f'<rect class="blink" data-o="{blink_off}" x="78" y="57" width="44" height="16" rx="8" fill="#1B1A1D" style="opacity:0"/>'
        filtro = ' filter="url(#gris)" opacity=".5"' if gris else ""
        self.add(s, e, f'<g transform="translate({x} {y}) scale({k})"{filtro}>{cuerpo}{parpadeo}</g>', a=a)

    def auro(self, s, e, x, y, k, cara="feliz", a="pop"):
        # Auro se dibuja centrado en (300,244) dentro de su marco: lo movemos para que su centro quede en (x,y)
        svg = f'<g transform="translate({x - 300 * k} {y - 244 * k}) scale({k})">{_auro.auro("v", cara)}</g>'
        self.add(s, e, svg, a=a, flota=(3, 2.2))

    def sub(self, s, e, peque, grande):
        """Subtítulo de dos niveles: palabras de unión en crema + palabra clave grande en oro."""
        svg = (f'<text x="{W/2}" y="384" font-family="{FUENTE}" font-size="15" font-weight="700" fill="{CREMA}" '
               f'text-anchor="middle" stroke="#080706" stroke-width="4" paint-order="stroke">{esc(peque)}</text>'
               f'<text x="{W/2}" y="424" font-family="{FUENTE}" font-size="{_tam(grande)}" font-weight="900" fill="{GOLD}" '
               f'text-anchor="middle" letter-spacing="-.5" stroke="#080706" stroke-width="6" paint-order="stroke">{esc(grande.upper())}</text>')
        self.add(s, e, svg, a="pop", din=0.09, dout=0.05)

    def voz(self, s, e, quien, frase):
        self.guion.append((s, e, quien, frase))

    # ---------- salida ----------
    def html(self) -> str:
        gdefs, _ = _pertx.fondo("v", W, H)
        defs = _pertx.defs("v") + gdefs + '<filter id="gris"><feColorMatrix type="saturate" values="0"/></filter>'
        fondo = (f'<rect width="{W}" height="{H}" fill="url(#vbg)"/>'
                 f'<text x="20" y="38" font-family="Georgia, serif" font-weight="700" font-size="14" fill="{GOLD}" letter-spacing="1.5">PX</text>')
        return PLANTILLA.replace("%W%", str(W)).replace("%H%", str(H)).replace("%DEFS%", defs) \
            .replace("%FONDO%", fondo).replace("%CAPAS%", "\n".join(self.capas))

    def render(self, carpeta: pathlib.Path, solo_html=False, con_voz=False):
        """con_voz=True mete las voces de video/voz/. Por defecto el vídeo sale SIN voz."""
        carpeta.mkdir(parents=True, exist_ok=True)
        pag = carpeta / f"{self.nombre}.html"
        pag.write_text(self.html(), encoding="utf-8")
        (carpeta / f"{self.nombre}-guion-voz.md").write_text(self.guion_md(), encoding="utf-8")
        if solo_html:
            return pag
        mudo = carpeta / f".{self.nombre}-mudo.mp4"
        subprocess.run(["node", str(pathlib.Path(__file__).parent / "render.js"), str(pag), str(self.dur), str(FPS), str(mudo)], check=True)
        audio = carpeta / f".{self.nombre}-audio.wav"
        escribir_wav(audio, mezcla(self.dur, self.sfx, self.voces() if con_voz else ()))
        final = carpeta / f"{self.nombre}.mp4"
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(mudo), "-i", str(audio),
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(final)], check=True)
        mudo.unlink()
        audio.unlink()
        return final

    def voces(self):
        """Busca video/voz/<vNN>-<n>.mp3 para cada frase del guion (n empieza en 1)."""
        pref = self.nombre.split("-")[0]
        out = []
        for n, (s, e, _q, _f) in enumerate(self.guion, 1):
            ruta = RAIZ / "video" / "voz" / f"{pref}-{n}.mp3"
            if ruta.exists():
                out.append((s, e, ruta))
        return out

    def guion_md(self) -> str:
        filas = "\n".join(f"| {s:05.1f}–{e:05.1f} s | {q} | {f} |" for s, e, q, f in self.guion)
        return (f"# Guion de voz · {self.nombre}\n\nCada frase se genera aparte y el motor la coloca en su tramo.\n"
                f"Voz de Pertx: ElevenLabs, 'Tom - Calma y claridad' (voice_id B0r3rOF9WOwQ4BBKhRWO), modelo eleven_v4.\nLos audios van en video/voz/<vNN>-<n>.mp3 (n = número de frase).\n\n"
                f"| Tiempo | Quién | Frase |\n|---|---|---|\n{filas}\n")


def _tam(palabra):
    n = len(palabra)
    return 40 if n <= 8 else 34 if n <= 11 else 28 if n <= 14 else 23


# ---------- piezas de dibujo reutilizables ----------

def panel(x, y, w, h, titulo=""):
    t = (f'<rect x="{x}" y="{y}" width="{w}" height="22" rx="10" fill="#1A1712"/>'
         f'<circle cx="{x+12}" cy="{y+11}" r="3" fill="{GOLD3}"/><circle cx="{x+22}" cy="{y+11}" r="3" fill="#3A3428"/><circle cx="{x+32}" cy="{y+11}" r="3" fill="#3A3428"/>'
         f'<text x="{x+w/2}" y="{y+15}" font-family="{FUENTE}" font-size="9" font-weight="700" fill="#B3A994" text-anchor="middle">{esc(titulo)}</text>') if titulo else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#0E0D0B" stroke="#2E281E" stroke-width="1.5"/>{t}')


def texto(x, y, t, tam=11, color=CREMA, peso=600, anchor="start", mono=False, extra=""):
    fam = "'IBM Plex Mono', 'DejaVu Sans Mono', monospace" if mono else FUENTE
    return f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{tam}" font-weight="{peso}" fill="{color}" text-anchor="{anchor}"{extra}>{esc(t)}</text>'


def escribiendo(x, y, t, s, e, tam=11, color=CREMA, mono=True):
    """Texto que se escribe letra a letra entre s y e."""
    return texto(x, y, "", tam, color, 500, mono=mono, extra=f' data-type="{s},{e}" data-full="{esc(t)}"')


def etiqueta(x, y, t, oro=True, w=None):
    w = w or (len(t) * 7 + 22)
    fondo, color = (GOLD, "#13100C") if oro else ("#2C2A30", "#B3A994")
    return (f'<rect x="{x}" y="{y}" width="{w}" height="18" rx="9" fill="{fondo}"/>'
            + texto(x + w / 2, y + 12.5, t, 9, color, 800, "middle"))


def barra(x, y, w, s, e, desde=0.0, hasta=1.0, color=GOLD):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="8" rx="4" fill="#2C2A30"/>'
            f'<rect x="{x}" y="{y}" width="{w*desde}" height="8" rx="4" fill="{color}" data-w="{s},{e},{w*desde},{w*hasta}"/>')


def movil(x, y, k=1.0, contenido=""):
    return (f'<g transform="translate({x} {y}) scale({k})">'
            f'<rect x="0" y="0" width="120" height="220" rx="18" fill="#0B0B0C" stroke="#3A3640" stroke-width="2"/>'
            f'<rect x="8" y="10" width="104" height="200" rx="12" fill="#13100C"/>'
            f'<rect x="45" y="14" width="30" height="5" rx="2.5" fill="#2C2A30"/>{contenido}</g>')


# ---------- audio ----------

def _env(n, a=0.005, r=0.2):
    t = np.arange(n) / SR
    return np.minimum(1, t / a) * np.exp(-t / r)


def musica(dur):
    """Base oscura y tranquila: 84 BPM, La menor, bombo + charles + sub + acordes de pad."""
    n = int(dur * SR)
    out = np.zeros(n)
    bpm = 84
    beat = 60 / bpm
    # acordes (Am, F, Dm, E) en frecuencias
    acordes = [[220.0, 261.63, 329.63], [174.61, 220.0, 261.63], [146.83, 174.61, 220.0], [164.81, 207.65, 246.94]]
    bajos = [55.0, 43.65, 36.71, 41.20]
    t_all = np.arange(n) / SR
    compas = beat * 4
    for i in range(int(dur / compas) + 1):
        t0 = i * compas
        a = acordes[i % 4]
        i0, i1 = int(t0 * SR), min(n, int((t0 + compas) * SR))
        if i0 >= n:
            break
        tt = t_all[i0:i1] - t0
        env = np.minimum(1, tt / 0.6) * np.minimum(1, (compas - tt) / 0.4)
        pad = sum(np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * f * 2.003 * tt) for f in a)
        out[i0:i1] += 0.035 * pad * env
        out[i0:i1] += 0.10 * np.sin(2 * np.pi * bajos[i % 4] * tt) * env
    for k in range(int(dur / beat) + 1):
        t0 = k * beat
        i0 = int(t0 * SR)
        if i0 >= n:
            break
        if k % 2 == 0:  # bombo
            m = min(n - i0, int(0.35 * SR))
            tt = np.arange(m) / SR
            f = 50 + 70 * np.exp(-tt * 30)
            out[i0:i0 + m] += 0.45 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 9)
        for h in (0, 0.5):  # charles en corcheas
            j0 = int((t0 + h * beat) * SR)
            m = min(n - j0, int(0.05 * SR))
            if m > 0:
                out[j0:j0 + m] += 0.03 * np.random.default_rng(k * 2 + int(h * 2)).standard_normal(m) * _env(m, 0.001, 0.015)
        if k % 4 == 2:  # palmada suave
            m = min(n - i0, int(0.2 * SR))
            out[i0:i0 + m] += 0.08 * np.random.default_rng(1000 + k).standard_normal(m) * _env(m, 0.001, 0.06)
    # entrada y salida suaves
    fade = int(1.0 * SR)
    out[:fade] *= np.linspace(0, 1, fade)
    out[-fade:] *= np.linspace(1, 0, fade)
    return out


def efecto(tipo):
    if tipo == "ding":
        m = int(0.6 * SR)
        tt = np.arange(m) / SR
        return 0.22 * (np.sin(2 * np.pi * 1318.5 * tt) + 0.5 * np.sin(2 * np.pi * 1975.5 * tt)) * _env(m, 0.002, 0.18)
    if tipo == "pop":
        m = int(0.12 * SR)
        tt = np.arange(m) / SR
        return 0.25 * np.sin(2 * np.pi * (600 + 900 * np.exp(-tt * 40)) * tt) * _env(m, 0.001, 0.03)
    if tipo == "error":
        m = int(0.35 * SR)
        tt = np.arange(m) / SR
        return 0.15 * np.sign(np.sin(2 * np.pi * 180 * tt)) * _env(m, 0.002, 0.12)
    # whoosh: ruido filtrado que sube y baja
    m = int(0.45 * SR)
    rng = np.random.default_rng(7)
    ruido = rng.standard_normal(m)
    k = np.ones(40) / 40
    suave = np.convolve(ruido, k, mode="same")
    env = np.sin(np.linspace(0, np.pi, m)) ** 2
    return 0.35 * (ruido - suave) * env * 0.5 + 0.2 * suave * env


def leer_audio(ruta, tempo=1.0):
    """Decodifica un audio (mp3, wav...) a mono 44,1 kHz con ffmpeg. tempo>1 lo acelera sin cambiar el tono."""
    filtros = ["-af", f"atempo={tempo:.3f}"] if abs(tempo - 1) > 0.001 else []
    raw = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(ruta), *filtros,
                          "-f", "s16le", "-ac", "1", "-ar", str(SR), "-"], check=True, capture_output=True).stdout
    return np.frombuffer(raw, dtype="<i2").astype(np.float64) / 32768


def mezcla(dur, sfx, voces=()):
    n = int(dur * SR)
    mus = musica(dur)
    mus = mus / (np.max(np.abs(mus)) or 1)
    voz = np.zeros(n)
    hay_voz = np.zeros(n)
    for s, e, ruta in voces:
        hueco = max(0.5, e - s - 0.05)
        a = leer_audio(ruta)
        tempo = min(1.15, len(a) / SR / hueco) if len(a) / SR > hueco else 1.0
        if tempo > 1:
            a = leer_audio(ruta, tempo)
        a = a / (np.max(np.abs(a)) or 1) * 0.92
        i0 = int(s * SR)
        m = min(len(a), n - i0)
        voz[i0:i0 + m] += a[:m]
        hay_voz[i0:i0 + m] = 1
    # la música baja cuando habla Pertx (con transiciones suaves)
    k = int(0.25 * SR)
    suave = np.convolve(hay_voz, np.ones(k) / k, mode="same") if voces else hay_voz
    nivel_musica = 0.30 - 0.18 * suave if voces else np.full(n, 0.45)
    fx = np.zeros(n)
    for t, tipo in sfx:
        e = efecto(tipo)
        i0 = int(t * SR)
        m = min(len(e), n - i0)
        if m > 0:
            fx[i0:i0 + m] += e[:m]
    out = voz + mus * nivel_musica + fx * (0.45 if voces else 0.9)
    return np.tanh(out * 1.1) * 0.9


def escribir_wav(ruta, mono):
    est = (np.stack([mono, mono], axis=1) * 32767).astype("<i2")
    with wave.open(str(ruta), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(est.tobytes())


PLANTILLA = r"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<style>html,body{margin:0;background:#080706}svg{display:block}</style></head>
<body>
<svg id="v" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %W% %H%" width="%W%" height="%H%">
<defs>%DEFS%</defs>
%FONDO%
%CAPAS%
</svg>
<script>
const capas=[...document.querySelectorAll('[data-s]')];
const ease=x=>x<=0?0:x>=1?1:1-Math.pow(1-x,3);
window.setT=function(t){
  for(const el of capas){
    const s=+el.dataset.s,e=+el.dataset.e,a=el.dataset.a,din=+el.dataset.din,dout=+el.dataset.dout;
    if(t<s||t>e){el.style.opacity=0;continue}
    const pi=ease((t-s)/din),po=ease((e-t)/dout);
    let tf='';
    if(a==='pop')tf=`scale(${0.82+0.18*pi})`;
    else if(a==='up')tf=`translateY(${(1-pi)*28}px)`;
    else if(a==='left')tf=`translateX(${(1-pi)*-50}px)`;
    else if(a==='right')tf=`translateX(${(1-pi)*50}px)`;
    else if(a==='down')tf=`translateY(${(1-pi)*-40}px)`;
    if(el.dataset.f){const [amp,per]=el.dataset.f.split(',').map(Number);tf+=` translateY(${Math.sin(t*2*Math.PI/per)*amp}px)`}
    el.style.opacity=Math.min(pi,po);el.style.transform=tf;
  }
  for(const el of document.querySelectorAll('[data-type]')){
    const [s,e]=el.dataset.type.split(',').map(Number),full=el.dataset.full;
    el.textContent=full.slice(0,Math.round(Math.max(0,Math.min(1,(t-s)/(e-s)))*full.length));
  }
  for(const el of document.querySelectorAll('[data-w]')){
    const [s,e,a,b]=el.dataset.w.split(',').map(Number);
    el.setAttribute('width',a+(b-a)*ease((t-s)/(e-s)));
  }
  for(const el of document.querySelectorAll('[data-count]')){
    const [s,e,a,b]=el.dataset.count.split(',').map(Number);
    el.textContent=Math.round(a+(b-a)*ease((t-s)/(e-s)))+(el.dataset.suf||'');
  }
  for(const el of document.querySelectorAll('.blink')){
    const ph=(t+(+el.dataset.o))%3.6;el.style.opacity=ph<0.13?1:0;
  }
};
window.setT(0);
</script>
</body></html>
"""


def perfil_movil(x=176, y=86):
    """Móvil con el perfil de @pertx y el botón Seguir (para el CTA)."""
    return movil(x, y, 1.0,
                 f'<circle cx="60" cy="56" r="22" fill="#1F1E22" stroke="{GOLD}" stroke-width="2"/>'
                 + texto(60, 61, "PX", 12, GOLD, 800, "middle")
                 + texto(60, 96, "@pertx", 11, CREMA, 800, "middle")
                 + texto(60, 112, "Construyo negocios", 7.5, "#B3A994", 500, "middle")
                 + texto(60, 122, "con IA desde 0", 7.5, "#B3A994", 500, "middle")
                 + f'<rect x="20" y="136" width="80" height="24" rx="12" fill="{GOLD}"/>' + texto(60, 152, "Seguir", 10, "#13100C", 800, "middle")
                 + "".join(f'<rect x="{14+n*32}" y="172" width="28" height="30" rx="4" fill="#1F1E22"/>' for n in range(3)))

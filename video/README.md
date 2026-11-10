# Carpeta `video/` · fábrica de vídeos (prototipo)

Monta vídeos 9:16 (1080x1920, 30 fps) **gratis y en local**, con Pertx y Auro animados, subtítulos de dos niveles, música y efectos.

| Archivo | Qué es |
|---|---|
| `salida/v01-novato-vs-pertx.mp4` | Vídeo de muestra 1 · formato F1 NOVATO VS PERTX (36 s) |
| `salida/v02-la-herramienta.mp4` | Vídeo de muestra 2 · formato F2 LA HERRAMIENTA · Claude Code (38 s) |
| `salida/*-guion-voz.md` | El texto que tienes que grabar con tu voz, con los tiempos |
| `salida/*.html` | El vídeo como página animada (para previsualizar) |
| `videos/*.py` | El guion de cada vídeo en código: escenas, tiempos, subtítulos, sonidos |
| `motor.py` | El motor: dibuja, anima, sintetiza la música y monta el MP4 |
| `render.js` | Hace las fotos de cada fotograma con Chromium y se las pasa a ffmpeg |

## Cómo crear o rehacer un vídeo
```
python3 video/videos/v01_novato_vs_pertx.py          # MP4 completo (~1-2 min)
python3 video/videos/v01_novato_vs_pertx.py --html   # solo la previsualización
python3 video/videos/v01_novato_vs_pertx.py --voz    # con la voz de video/voz/ (solo si lo pides)
```

## Qué falta (honesto)
- **Voz:** los vídeos salen **sin voz** por defecto. La voz de Pertx es de ElevenLabs ("Tom - Calma y claridad"). Las frases de los vídeos 1 y 2 ya están generadas en `video/voz/` (`v01-1.mp3`…), pero **no se usan** hasta que lo pidas con `--voz`.
- **Música:** es una base sintetizada por el propio motor (libre de derechos). Para publicar puedes usar también un sonido de la biblioteca de TikTok.
- **Pantalla real:** ahora todo son mockups. Cuando grabes tu pantalla, se mete como un plano más.

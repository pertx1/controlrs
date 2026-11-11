# Carpeta `video/` · fábrica de vídeos

Monta vídeos 9:16 (1080x1920, 30 fps) **gratis y en local** a partir de los guiones de `guiones/`: Pertx y Auro animados, pantallas dibujadas (sin grabaciones), subtítulos automáticos con la palabra clave en oro, música, efectos y, si quieres, voz de ElevenLabs.

## Del guion al vídeo
```
npm run video -- 1 1 --html   # previsualización rápida del día 1 de la semana 1 (ábrela en el navegador)
npm run video -- 1 1          # vídeo sin voz → video/salida/semana-01/dia-01.mp4
npm run voz -- 1 1            # genera la voz de cada escena con ElevenLabs (te dice el gasto y pregunta)
npm run video -- 1 1 --voz    # vídeo con voz (cada escena dura lo que su frase)
npm run video -- 1 todos      # toda la semana
```
Primera vez en tu portátil: sigue **`INSTALAR-WINDOWS.md`**.

| Archivo | Qué es |
|---|---|
| `montar.py` | Lee un guion `.json` y monta el vídeo con las plantillas de escena |
| `voz.py` | Genera las voces con ElevenLabs (necesita tu clave en `video/.env`) |
| `config.json` | Qué voces usa cada personaje: Pertx = Tom; Auro = Lucas + filtro robótico |
| `motor.py` | El motor: dibuja, anima, sintetiza música y efectos, mezcla y exporta |
| `render.js` | Hace la foto de cada fotograma con Chromium y se la pasa a ffmpeg |
| `salida/semana-XX/` | Los vídeos montados (no se suben a git) |
| `voz/semana-XX/` | Las voces generadas, una por escena |
| `videos/`, `salida/v0*` | Los 2 vídeos de muestra del principio (sin voz, no se publican) |

Los vídeos con avatar o voz IA se publican **siempre con la etiqueta de IA**.

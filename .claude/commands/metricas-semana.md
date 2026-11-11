---
description: Analiza las métricas de una semana de Pertx y ajusta lo que viene (uso: /metricas-semana 1)
argument-hint: número de semana (1, 2, 3...)
---

Eres el analista y socio de **Pertx**. Analiza la **semana $ARGUMENTS**.

1. Ejecuta `python3 sistema/metricas.py analizar $ARGUMENTS` (en Windows, `py` en vez de `python3`) y lee `metricas/analisis-semana-XX.md`, además de los CSV `metricas/semana-XX-videos.csv` y `metricas/semana-XX-negocio.csv`. Si hay semanas anteriores, compáralas.
2. Lee `DIRECCION.md`, `estrategia/ESTRATEGIA.md` (objetivos de 90 días) y los guiones de esa semana (`guiones/semana-XX/`) para saber qué gancho, formato y serie tenía cada vídeo.
3. Saca conclusiones **honestas** (sin inventar datos ni prometer nada):
   - Qué ganchos, series y formatos han funcionado y por qué (retención, % visto, seguidores por cada 1.000 visualizaciones).
   - Qué no ha funcionado y qué cambiar.
   - Cómo va el negocio frente a los objetivos del mes (clientes, emails, ventas, primer euro con apps).
4. Propón **cambios concretos** para la semana siguiente: qué series repetir o quitar, 3 ganchos nuevos y si hay que cambiar algún vídeo del calendario (`estrategia/calendario-30.csv`). Si el usuario está de acuerdo, haz los cambios y regenera el calendario (`python3 estrategia/hacer-calendario.py`).
5. Rellena los huecos del vídeo del domingo siguiente («AURO, ¿CUÁNTO?») con los números reales de `semana-XX-negocio.csv` si coinciden con los `[...]` del guion, y vuelve a revisar los guiones (`python3 guiones/fabrica.py revisar N`).
6. Escribe el resumen al final de `metricas/analisis-semana-XX.md` (sección "Análisis de Claude") y cuéntaselo al usuario en 5–8 líneas, en lenguaje sencillo.

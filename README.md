# Parrilla

Programador de publicaciones para redes sociales, inspirado en el planificador de Metricool.

- Calendario por semana (sombreado con tus mejores horas), mes y cola.
- Editor con selección de redes, contador de caracteres por red, multimedia por URL pública, primer comentario y opciones por red (Reel/Historia, título de YouTube, tablero de Pinterest, Google Business).
- Vista previa por red y validación con las reglas de Metricool.
- Programación real en Metricool, borradores, filtros y arrastrar para reprogramar.

## Cómo funciona

`index.html` es una sola página sin dependencias de build.

Abierta como Artifact en claude.ai usa sus capacidades de runtime: base de datos compartida, conector de Metricool (`getBrandSettings`, `getBestTimeToPostByNetwork`, `getScheduledPosts`, `createScheduledPost`) e IA para reescribir textos.

Abierta como página estática (por ejemplo `npx serve .` o GitHub Pages) funciona en modo local: las publicaciones se guardan en el navegador y la conexión con Metricool queda desactivada.

---

# Pertx

Marca personal faceless en castellano (TikTok, Reels, Shorts). Se construye por etapas y no se pasa a la siguiente sin "aprobado".

| Etapa | Estado | Dónde |
|---|---|---|
| 1. Personaje (P1-P5) | Esperando elección | `personaje/galeria.html`, `personaje/FICHAS-PERSONAJE.md` |
| 2. Mascota (M1-M5) | Pendiente | `personaje/galeria-mascota.html` |
| 3. Análisis de referencias | Pendiente | `referencias/ANALISIS.md` |
| 4. Desarrollo (estrategia, guiones, edición, web, sistema diario) | Pendiente | `PLAN.md` |

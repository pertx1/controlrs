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

# TemaTest

En [`tematest/`](tematest/) está TemaTest: convierte el temario de oposiciones en tests tipo examen. Puesta en marcha en [`tematest/README.md`](tematest/README.md) y plan de lanzamiento en [`tematest/LANZAMIENTO.md`](tematest/LANZAMIENTO.md).

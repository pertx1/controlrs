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
| 1. Personaje (P1-P5) | Elegido: P1 con colores de P5 (`personaje/png/P1-oro.png`) | `personaje/galeria.html`, `personaje/FICHAS-PERSONAJE.md` |
| 2. Mascota (M1-M5) | Elegida: M3 Auro · código final `P1-oro+M3` (`personaje/FICHA-FINAL.md`) | `personaje/galeria-mascota.html` |
| 3. Análisis de referencias | Hecho | `referencias/ANALISIS.md` |
| Vídeos de muestra | 2 hechos, sin voz y sin publicar | `video/salida/` |
| Dirección de la cuenta | Aprobada | `DIRECCION.md` |
| Fase 1 · Estrategia | Hecha (producto: A con C dentro, luego B) | `estrategia/` |
| Fase 2 · Fábrica de guiones | Hecha · semana 1 escrita | `guiones/` · comando `/guiones-semana N` |
| 0. Crear y calentar cuentas (TikTok + Instagram) | Te toca a ti, con tu padre o tu madre | `CUENTAS.md` |
| 4. Desarrollo (estrategia, guiones, edición, web, sistema diario) | En marcha · siguiente: Fase 1 Estrategia | **`PLAN.md`** |

**Empieza por aquí:** `DIRECCION.md` (hacia dónde va Pertx), `PLAN.md` (qué falta) y `CUENTAS.md` (lo que tienes que hacer tú).

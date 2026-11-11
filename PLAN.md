# PERTX · PLAN (Etapa 4)

Vamos **fase por fase**. Al empezar cada fase te hago las preguntas que falten. Marca con una `x` lo que esté hecho.

## Lo que sé de ti (respuestas de la Etapa 4)

| Pregunta | Respuesta | Qué significa para el plan |
|---|---|---|
| Suscripciones | **Higgsfield, Vercel, ElevenLabs** | Voz con ElevenLabs, web en Vercel, Higgsfield solo si hiciera falta una imagen o vídeo IA (el personaje lo dibujamos en código) |
| Ordenador | **Windows, portátil** | Todos los comandos tienen que funcionar en Windows (Node + Python + ffmpeg) |
| Micrófono | Tienes, pero **no quieres usarlo** | Voz de Pertx 100 % IA: **ElevenLabs "Tom · Calma y claridad"** → todos los vídeos se marcan como IA |
| Tiempo | **El que haga falta** | Plan de 1 vídeo al día desde la semana 2 |
| Primer producto | **De todo** | Orden: 1) servicios de webs y tiendas online, 2) producto digital barato, 3) afiliados, 4) la web para creadores, 5) curso (ver `DIRECCION.md`) |
| Cuentas | **No creadas** · de momento **solo TikTok e Instagram** | Fase 0 (guía en `CUENTAS.md`) |
| Edad | **Menor de edad** | Tus padres son los titulares de las cuentas y los cobros. En los vídeos: "menor de edad" o "estudiante", nunca la edad exacta |
| Dirección | Objetivo: dinero pronto + clientes. Tono duro y directo. Sincero con todos los números | **`DIRECCION.md`** (aprobada) |

## Ya hecho (Etapas 1–3 y muestras)
- [x] Personaje y mascota: **P1-oro+M3** (`personaje/FICHA-FINAL.md`)
- [x] Análisis de referencias, fórmula Pertx y 5 formatos (`referencias/ANALISIS.md`)
- [x] Motor de vídeo gratis en local, con 2 vídeos de muestra **sin voz y sin publicar** (`video/`)
- [x] Voz de Pertx elegida (las frases de los 2 vídeos ya están generadas en `video/voz/`, sin usar)
- [x] Foto de perfil (`personaje/png/perfil.png`)

---

## Paso previo · Dirección de la cuenta
- [x] Aprobar `DIRECCION.md`

## Fase 0 · Cuentas (tú, con tu padre o tu madre, 5–6 días)
- [ ] Crear el Gmail de la marca, TikTok e Instagram a nombre de tu padre o tu madre → `CUENTAS.md` (**YouTube de momento no**; opcional reservar el nombre)
- [ ] Decirme el **nombre de usuario** que ha quedado libre
- [ ] 5 días de calentamiento

## Fase 1 · Estrategia (yo, mientras calientas las cuentas)
- [x] Posicionamiento: a quién hablamos, qué prometemos y en qué nos diferenciamos
- [x] Bios definitivas (`estrategia/ESTRATEGIA.md`)
- [x] Series recurrentes (basadas en F1–F5) con su día de la semana
- [x] Oferta de **servicios** (qué se vende, a quién, precios orientativos y cómo conseguir los primeros clientes)
- [x] Producto digital decidido: **A** principal (19 €, con **C** dentro y como regalo gratis) y **B** en el mes 3
- [x] Serie estrella "De 0 € a mi primer euro con apps"
- [x] Plan de 90 días (objetivos honestos por mes)
- [x] Calendario de los primeros 30 días (`estrategia/CALENDARIO-30.md`)

## Fase 2 · Fábrica de guiones
- [x] Comando que genera los guiones de la semana (`/guiones-semana N` en Claude Code + `guiones/fabrica.py`)
- [x] Usa la dirección, la estrategia, la ficha del personaje y la fórmula de las referencias, y revisa líneas rojas y ritmo
- [x] Primeros 7 guiones (`guiones/semana-01/`): 5 listos, 2 esperando tus datos (sin grabaciones)

## Fase 3 · Edición automática
- [x] Prototipo del motor (SVG + Chromium + ffmpeg, 1080x1920)
- [x] Del guion al vídeo con un comando: `npm run video -- SEMANA DIA` (10 plantillas de escena, subtítulos automáticos, música y efectos)
- [x] Voz automática con ElevenLabs por escena: `npm run voz -- SEMANA DIA` (te dice el gasto y pregunta antes)
- [x] Voz de Auro (otra voz + filtro robótico en local)
- [x] ~~Meter tus grabaciones de pantalla~~ → no hace falta: las pantallas se dibujan
- [x] Plantillas de escena reutilizables para los 5 formatos
- [x] Vida en las escenas: Pertx camina, habla, salta y cambia de pose; 21 objetos; 3 escenarios
- [x] Día 1 de la semana 1 montado **con voz** (`video/salida/semana-01/dia-01.mp4`)
- [ ] Instalación y prueba en **tu portátil Windows** (`video/INSTALAR-WINDOWS.md`)
- [x] Del guion al MP4 con un solo comando

## Fase 4 · Embudo de ventas
- [ ] Web link-in-bio en **Next.js en Vercel**
- [ ] Primer producto digital (el que elijas en la Fase 1)
- [ ] Captación de emails (con una opción gratis)
- [ ] 5 emails de bienvenida

## Fase 5 · Sistema diario
- [ ] `npm run hoy`: qué grabar, qué publicar y qué tarea hacer hoy
- [ ] Registro semanal de métricas que yo analizo y con el que ajusto el calendario

---

## Reglas que no cambian
- Nada de ingresos ni datos falsos. Si es un ejemplo, se dice.
- Todo vídeo con avatar o voz IA lleva la etiqueta de IA.
- 0 € extra: solo herramientas gratis y tus suscripciones (Higgsfield, Vercel, ElevenLabs).
- Antes de gastar créditos de Higgsfield o ElevenLabs en algo nuevo, te aviso de cuánto cuesta.

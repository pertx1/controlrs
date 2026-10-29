# Kit de lanzamiento de TemaTest

Objetivo: 11 ventas a 9,99 € = 100 €. Con un 3 % de conversión hacen falta unas 370 personas que lo prueben.

## Calendario

| Días | Qué haces | Cuándo pasas a lo siguiente |
|---|---|---|
| 1–3 | Puesta en marcha (README): clave de Gemini, tienda de Lemon Squeezy, Vercel | La web genera tests reales |
| 4–10 | Pruebas con 10 opositores, gratis a cambio de opinión | 10 personas han hecho un test y 3 dicen que lo usarían cada semana |
| 10 | Activas el cobro y pones el enlace de compra | Funciona el pago de prueba |
| 10–40 | 1 vídeo diario + 20 min al día en comunidades | Primera venta antes del día 25 |

**Reglas para decidir:**
- Si en 7 días nadie repite (hace un segundo test otro día), el problema es el producto, no el marketing. Habla con 5 usuarios antes de tocar nada.
- Si repiten pero nadie paga, prueba 4,99 € o 5 tests gratis a la semana en lugar de 3 al día.
- Si un vídeo pasa de 5.000 visitas, graba 3 variaciones de ese mismo vídeo.

## Dónde está tu público
- **TikTok e Instagram**: busca "opositora", "oposiciones 2027", "auxiliar administrativo", "estudia conmigo". Comenta con aportaciones útiles en vídeos de esas cuentas antes de publicar los tuyos.
- **Telegram**: hay grupos por oposición (Auxiliar Administrativo del Estado, Tramitación Procesal, Policía Nacional…). Búscalos en el buscador de Telegram y en webs que los listan.
- **Reddit**: r/oposiciones.
- **Foros**: las secciones por oposición de Foro Oposiciones.

Regla: aporta valor primero. En los grupos, menciona la web solo cuando alguien pregunte cómo practicar o pida tests.

## Mensajes para la fase de pruebas (días 4–10)

**Telegram o grupo de WhatsApp:**
> Hola. Estoy probando una web que convierte el PDF de tu tema en un test tipo examen (4 opciones, penalización y la explicación con la cita del tema). Busco 10 opositores que la prueben gratis con su temario y me digan con sinceridad qué falla. ¿Alguien se apunta? Os paso el enlace por privado.

**Reddit (r/oposiciones), en formato historia:**
> **Título:** Hice una web que convierte tu tema en test tipo examen. Busco opositores que la destrocen.
>
> Hacer tests de mi propio temario me llevaba horas, y las plataformas grandes usan su banco de preguntas, no el de mi academia. Así que hice una web: subes el PDF del tema, eliges cuántas preguntas y te genera un test con 4 opciones, penalización de −1/3 y la explicación de cada respuesta con la frase del tema que la justifica. Guarda las que fallas para repasarlas.
>
> Es gratis para probar y no hace falta registrarse. Lo que más me interesa: ¿las preguntas se parecen a las del examen real? ¿Qué le falta para que la uséis a diario?
>
> [enlace]

## Guiones de vídeo (sin salir en cámara: grabas la pantalla del móvil con voz o texto encima)

1. **"Convierto el tema 5 en un test en 30 segundos"**
   - 0–3 s: el PDF del tema en pantalla. Texto: *"Me quedan 47 temas y no tengo tests de mi temario"*.
   - 3–20 s: subes el PDF, pulsas Generar y aparece el test.
   - 20–30 s: contestas una pregunta, fallas y aparece la explicación con la cita. Texto: *"Y me dice exactamente dónde está en el tema"*.
   - Cierre: *"Se llama TemaTest, enlace en el perfil"*.
2. **"Esta pregunta trampa sale en todos los exámenes"**: una pregunta difícil generada de una ley que entra en muchas oposiciones (Constitución, Ley 39/2015). Deja que la gente la conteste en comentarios y da la respuesta al día siguiente. Genera comentarios y seguidores.
3. **"Cómo estudio con tests de mi temario (método)"**: leer el tema, test de 10 preguntas, repasar falladas al día siguiente. La herramienta aparece como parte del método, no como anuncio.
4. **"Mi nota del simulacro de hoy"**: serie diaria con el resultado del test. Engancha porque la gente vuelve a ver si mejoras.
5. **"Lo que nadie te dice de la penalización −1/3"**: cuándo compensa contestar si dudas entre dos opciones. Es contenido útil, y la herramienta sirve para practicarlo.

Publica a las 21:00–23:00 o a las 7:00–8:30, cuando estudian los opositores. Usa siempre tus mejores horas en Parrilla.

## Bio y enlace
- **Bio:** "Convierte tu temario en tests de examen · 3 gratis al día 👇"
- **Enlace:** la web de Vercel. Usa el mismo nombre de usuario en todas las redes.

## Qué medir cada domingo

| Métrica | Dónde | Objetivo semana 1 → semana 4 |
|---|---|---|
| Visitas a la web | Vercel Analytics (gratis) | 50 → 400 |
| Tests generados | Logs de Vercel (`/api/generate`) | 30 → 300 |
| Ventas | Lemon Squeezy | 0 → 11 en total |
| Mejor vídeo | TikTok e Instagram | Repite su formato |

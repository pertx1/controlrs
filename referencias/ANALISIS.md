# PERTX · Etapa 3 · Análisis de los vídeos de referencia

Vídeos analizados (guardados en `referencias/videos/`, fuera de git porque no son nuestros):

| Código | Cuenta | Duración | Tema |
|---|---|---|---|
| **REF01** | @yuww333.finance | 42 s (37 s de contenido + 5 s del cierre que añade TikTok al descargar) | "Primer mes de un novato y de un pro automatizando canales de YouTube" |
| **REF02** | @notfound404.es | 96 s (92 s de contenido + 4 s de cierre de TikTok) | "20 móviles Android en la nube": reseña de una herramienta para llevar muchas cuentas |

> **Cómo lo he analizado:** he sacado fotogramas cada 0,3–0,5 s, he detectado los cortes con ffmpeg y he medido el audio. Los guiones los he leído de los subtítulos quemados en el vídeo. No puedo *escuchar* el audio: lo que digo de la música se basa en los niveles de volumen, así que tómalo como aproximado.

---

## REF01 · "Novato vs Pro" (animación 2D)

### Cómo es
- **Formato:** animación 2D plana (estilo flat), sin persona real. Pantalla partida en dos con una línea vertical azul brillante.
- **Personajes:** a la izquierda, el **"novato"**: un muñeco gris sin cara, muy simple. A la derecha, el **"pro"**: un gato/pantera negro con traje verde y sombrero. Es la mascota de la cuenta.
- **Fondo:** azul marino oscuro con textura suave, suelo negro.
- **Elementos:** etiquetas "NOVATO" y "PRO", barra de progreso "MES 1", calendario "SEMANA 2" con los días L-M-X-J-V-S-D, máquina de bolas con "5/7 subidos", tarjetas de vídeos, relojes, notificación de móvil "Tu Short ha superado el millón de visualizaciones", un robot pequeño de IA con barra "IA ×8".

### Gancho (0–3 s)
- **Texto:** "Primer mes de un novato y de un pro automatizando canales de YouTube."
- **Imagen:** los dos personajes, uno a cada lado, con la barra "MES 1" y dos móviles con "Crear canal" (uno "a mano" y otro "automático").
- **Por qué engancha:** plantea una **comparación** (¿quién gana?) y promete una historia con final ("primer mes"). Te quedas para ver el resultado.

### Guion completo (leído de los subtítulos)
> Primer mes de un novato y de un pro automatizando canales de YouTube.
> **Semana 1.** El novato pasa 7 días editando un solo vídeo. El pro sube uno cada día, y cada uno distinto.
> **Semana 2.** El vídeo perfecto del novato: 200 visitas. El pro mira sus datos: 6 no funcionan, pero uno está explotando.
> **Semana 3.** El novato vuelve a empezar de cero. El pro clona ese formato con inteligencia artificial y solo revisa.
> **Semana 4.** El novato lleva 2 vídeos. El pro, 30. Y le llega [la notificación: su Short ha superado el millón].
> El pro no trabaja más que el novato. Solo prueba más rápido.
> Si quieres saber más sobre este modelo de negocio, revisa mi biografía, que tienes una clase gratuita.

### Estructura
| Tramo | Tiempo | Qué pasa |
|---|---|---|
| Gancho | 0–3,5 s | Planteamiento: novato vs pro, mes 1 |
| Semana 1 | 3,5–11 s | Diferencia de método (1 vídeo vs 1 al día) |
| Semana 2 | 11–19 s | Resultados y datos |
| Semana 3 | 19–25 s | El pro usa IA para repetir lo que funciona |
| Semana 4 | 25–30 s | Resultado final (2 vs 30 vídeos + notificación) |
| Moraleja | 30–33 s | "No trabaja más, prueba más rápido" |
| CTA | 33–37 s | Biografía → clase gratuita |

### Ritmo
- **Duración útil:** 37 s.
- **Cambio de imagen:** cada **~2–2,5 s** (cada frase trae un elemento nuevo). No hay cortes de cámara: todo son animaciones que entran y salen. Por eso la detección de cortes casi no encuentra ninguno.
- **Velocidad de voz:** ~95 palabras en 37 s → **~2,6 palabras por segundo** (rápido).
- **Subtítulos:** cambian cada **0,5–1 s**.

### Subtítulos
- **Arriba en el centro**, a ~15 % de la altura.
- **2–3 palabras** por bloque.
- Blanco en negrita, con **la palabra clave en amarillo** ("novato", "pro", "datos", "inteligencia").
- Sin caja de fondo, con una sombra suave.

### Música y voz
- Voz en off narrando todo el rato. El audio casi nunca baja de volumen (solo 1 silencio en todo el vídeo), así que **muy probablemente hay música de fondo** continua por debajo de la voz.

### CTA (llamada a la acción)
"Revisa mi biografía, que tienes una clase gratuita". Sale el perfil en un móvil con un botón "Clase gratuita", que se pulsa y se abre un regalo con "¡Apuntado!". Es un **imán de emails**: dan algo gratis para captar contactos.

### Por qué funciona
1. **Comparación con dos personajes:** el cerebro quiere saber quién gana.
2. **Estructura por semanas:** sabes cuánto falta y aguantas hasta el final.
3. **Números concretos** (7 días, 200 visitas, 6 de 7, 2 vs 30).
4. **Moraleja que se puede compartir:** "No trabaja más. Prueba más rápido."
5. **El espectador se ve en el novato** y quiere ser el pro, y el CTA le da el primer paso.
6. **No hace falta cara:** la mascota es la marca.

---

## REF02 · "La herramienta" (persona con pasamontañas + pantalla)

### Cómo es
- **Formato:** mezcla de **3 tipos de plano**:
  1. **Grabación real** de un monitor con 20 móviles Android y un dedo señalando (solo en el gancho).
  2. **Pantallas y mockups animados** sobre fondo negro: tarjetas de móviles, perfiles, chat entre "Dani" y "Marcos", campo de contraseña bloqueada, precios, lista de redes, comentarios de seguidores.
  3. **Persona a cámara con pasamontañas negro y gafas redondas oscuras**, sudadera negra, luz azul de neón detrás. Habla gesticulando con las manos (planos cortos de las manos).
- **Fondo:** negro casi total, toques azules.

### Gancho (0–3 s)
- **Texto:** "Estos son **20** móviles **ANDROID** funcionando a la vez y **NINGUNO** [está en mi casa]…"
- **Imagen:** grabación real de un monitor lleno de móviles rosas y un dedo señalándolos.
- **Por qué engancha:** **prueba visual real** + dato raro (20 móviles) + un **misterio** que se resuelve en el segundo 4 ("están todos en la nube").

### Guion (leído de los subtítulos; entre [corchetes] las partes que no se ven del todo)
> Estos son 20 móviles Android funcionando a la vez y ninguno [está aquí]. Están todos en la **nube** y los controlo desde mi **ordenador** con una **herramienta** que se llama [GeeLark]. Cada uno es un [teléfono de verdad, con Play Store y aplicaciones] y su **propia** [sesión].
> Sirve para **llevar** [varias cuentas]: cada una vive en su **teléfono** y **saltas** a otra en un **segundo**.
> En el **vídeo** [anterior] me **llenasteis** de **preguntas**. La que más se **repitió**: [¿cuánto cuesta?]. Pues **empezar** [es gratis], ya trae dos [perfiles]. Si **necesitas** más, los **planes** salen por unos 14 **dólares** al mes. Eso sí, el **tiempo** de cada móvil se [cobra por minutos].
> Y desde el **vídeo** [anterior] han añadido lo que me **parece** lo más útil si **trabajas** con gente. Hasta ahora, si alguien te **ayudaba** con las cuentas, tenías que **pasarle** la contraseña. Ahora la **guardas** y la **bloqueas**. Esa **persona** trabaja con **normalidad**, pero no puede ver la contraseña ni **cambiarla**. Y lo mismo con las claves de **verificación** en dos pasos.
> **Funciona** con siete [redes] entre ellas [TikTok, Instagram, Facebook…]. **También** han abierto una [tienda de plantillas con tareas ya hechas].
> Te digo lo que **pienso**: si solo **tienes** una **cuenta**, no lo **necesitas**. Pero si **llevas** redes de un **negocio** o de varios **clientes**, te ahorra **muchísimo tiempo**. Y **recuerda**: la **herramienta** solo **organiza**. El **contenido** lo sigues **poniendo** tú, y siempre **dentro** de las normas de cada red.
> Y si te has **quedado** con alguna duda, tengo [un tutorial] **completo** [en YouTube] donde **enseño** [paso a paso]. Lo **tienes** en mi **perfil**. ¿Tú cuántas **cuentas llevas**?

### Estructura
| Tramo | Tiempo | Qué pasa | Plano |
|---|---|---|---|
| Gancho | 0–4 s | 20 móviles, ninguno en casa | Grabación real |
| Qué es | 4–20 s | Nube, herramienta, cada móvil es real, saltar de cuenta | Pantalla / mockups |
| Respuesta a comentarios | 20–36 s | "Me llenasteis de preguntas" → precio | Comentarios + tarjetas de precio |
| Novedad | 36–66 s | Contraseñas bloqueadas, 2FA, 7 redes, plantillas | Cara → mockups de chat y contraseña |
| Opinión honesta | 67–81 s | Para quién sí y para quién no + normas | **A cámara con pasamontañas** |
| CTA | 81–92 s | Tutorial completo en YouTube → perfil + pregunta | Miniatura de YouTube + cámara |

### Ritmo
- **Duración útil:** 92 s (largo para TikTok, pero aguanta gracias al ritmo).
- **Cambio de imagen:** cada **~2–4 s** en los tramos de pantalla. Los tramos a cámara duran más (6–25 s), pero los subtítulos y los gestos mantienen el ritmo.
- **Velocidad de voz:** **~2,5 palabras por segundo**.
- **Subtítulos:** cambian cada **~0,3 s** (palabra a palabra).

### Subtítulos (lo más característico del vídeo)
- En la **parte media-baja** de la pantalla (~60–70 % de la altura).
- **Dos niveles:**
  - Palabras de unión **pequeñas, en blanco**, encima ("en el", "que más se", "pero no puede ver la").
  - **La palabra clave ENORME, en MAYÚSCULAS, en rojo** (`NUBE`, `HERRAMIENTA`, `TRABAJAS`, `CONTRASEÑA`, `PERFIL`).
- Entran con un pequeño **fundido o desenfoque** (se ve un frame borroso antes de cada palabra).
- Fuente gruesa, condensada y sin sombra.

### Música y voz
- La voz es la del creador, con su voz real. Hay **15 pausas cortas** de silencio, así que la música (si la hay) va muy baja o se corta entre frases. La voz manda.

### CTA
1. **Tutorial completo en YouTube:** enseña su miniatura (él con pasamontañas + "20 MÓVILES EN TU PC GRATIS"). Lleva a la gente de TikTok a YouTube.
2. **"Lo tienes en mi perfil".**
3. **Pregunta final para comentarios:** "¿Tú cuántas cuentas llevas?". Así hay más comentarios y le dan ideas para el siguiente vídeo.

### Por qué funciona
1. **Gancho con prueba real** (se ve el monitor con los 20 móviles).
2. **Responde a comentarios del vídeo anterior:** crea serie y comunidad ("me llenasteis de preguntas").
3. **Información útil y concreta:** precio, qué trae gratis, novedades.
4. **Opinión honesta** ("si solo tienes una cuenta, no lo necesitas") que da **confianza**.
5. **Persona con pasamontañas:** misterio y marca personal sin enseñar la cara. **Es casi idéntico a Pertx.**
6. **Subtítulo palabra a palabra con la clave en grande:** se entiende sin sonido y obliga a mirar.
7. **Embudo TikTok → YouTube** con el tutorial largo.

---

## Patrones comunes

| Patrón | REF01 | REF02 | Para Pertx |
|---|---|---|---|
| **Sin cara** | Mascota animada | Pasamontañas | ✅ Pertx + Auro |
| **Fondo oscuro** con un color de acento | Azul marino + amarillo | Negro + rojo (y azul) | Negro cálido + **oro** |
| **Gancho = dato o comparación concreta** en <3 s | "novato vs pro" | "20 móviles, ninguno en casa" | Siempre un número o un contraste |
| **Subtítulos con palabra clave destacada** | Amarillo, arriba | Rojo enorme, abajo | **Clave en oro, grande, MAYÚSCULAS** |
| **Cambio visual cada 2–3 s** | ✅ | ✅ | Regla fija |
| **Voz rápida** (~2,5 palabras/s) | ✅ | ✅ | Guiones de ~90 palabras para 35 s |
| **Tema: ganar tiempo y dinero con herramientas o IA** | ✅ | ✅ | Pilar 1 y 4 |
| **Números concretos** | 7 días, 200 visitas, 2 vs 30 | 20 móviles, 14 $/mes, 7 redes | Solo números **reales** tuyos |
| **CTA a algo gratis en el perfil** | Clase gratuita | Tutorial en YouTube | Recurso gratis + email (Etapa 4) |
| **Cierre con moraleja o pregunta** | "Prueba más rápido" | "¿Tú cuántas cuentas llevas?" | Una de las dos, siempre |
| **Mockups de interfaz** en vez de grabar la pantalla tal cual | Tarjetas, calendario, móviles | Chats, contraseñas, precios | Nuestros mockups en negro y oro |

### Honestidad: lo que NO vamos a copiar
- **REF01 promete "automatizar canales de YouTube"** y sacar 30 vídeos al mes con IA. Desde 2025 YouTube **desmonetiza el contenido "masivo y repetitivo"** hecho con IA. Pertx enseñará a construir cosas reales con IA, no granjas de vídeos.
- **REF02 habla de llevar muchas cuentas.** Él mismo avisa: "siempre dentro de las normas de cada red". Nosotros igual: nada de trucos para saltarse las normas.
- **Los números de las referencias no sabemos si son reales.** Los de Pertx, sí o sí, serán reales (o se dirá que son un ejemplo).

---

## La fórmula Pertx

> **GANCHO con dato o contraste (0–3 s) → HISTORIA en pasos cortos con cambio visual cada 2–3 s → GIRO o DATO REAL → MORALEJA de una frase → CTA (gratis en el perfil + pregunta)**

### Las piezas
| Pieza | Cómo lo hacemos en Pertx |
|---|---|
| **Pertx (avatar)** | Narrador y protagonista. Aparece animado (de nuestros SVG) en los tramos de historia, con sus 5 expresiones. |
| **Pertx en carne y hueso (opcional, muy recomendado)** | Como en REF02: **tú grabándote con un pasamontañas negro y una sudadera negra con capucha**, igual que el avatar. Planos de manos, escritorio, teclado. Es gratis, no hay que marcarlo como IA y da credibilidad. El avatar y tú sois "el mismo Pertx". |
| **Auro (mascota)** | El "pro" o el ayudante: muestra los datos en hologramas, celebra las ventas, hace de contraste. |
| **Pantalla** | Grabaciones reales de Claude Code, apps y webs que construyes, o mockups en negro y oro cuando la pantalla real sea fea o tenga datos privados. |
| **POV** | Planos en primera persona: tus manos tecleando, el móvil con una notificación, el escritorio de noche. |
| **B-roll** | Solo si hace falta (cielo nocturno, ciudad de noche). Sin stock genérico. |

### Estilo visual fijo
- **Fondo:** negro cálido `#080706`–`#13100C`.
- **Acento:** oro `#D4AF37`. **Prohibido** el azul, el cian y el morado (eso es de REF02: nosotros somos negro y oro).
- **Subtítulos (mezcla de los dos):**
  - Palabras de unión **pequeñas, en crema** `#F3EEE3`, encima.
  - **Palabra clave GRANDE, MAYÚSCULAS, en oro** `#D4AF37`, fuente gruesa condensada.
  - Posición **media-baja** (~60 % de la altura), fuera de la zona de botones de TikTok (derecha y abajo).
  - Cambian **palabra a palabra o de 2 en 2**, con una entrada rápida (fundido de 2 frames).
- **Ritmo:** cambio visual cada **2–3 s** como máximo. Voz a ~2,5 palabras por segundo.
- **Duración objetivo:** **30–45 s** para empezar (REF01). Los formatos largos (60–90 s, como REF02) cuando ya haya audiencia.
- **Música:** base suave, oscura (lo-fi/trap lento), **muy baja** por debajo de la voz. Siempre de la biblioteca de sonidos de cada red o sin derechos de autor.
- **Sonidos:** "ding" de Auro en cada dato, "whoosh" suave en cada cambio de escena.
- **Marca:** "PX" dorado pequeño en una esquina. Sin marcas de agua de otras apps.

### Reglas de la fórmula
1. En el segundo 1 ya hay **un número o un contraste** en pantalla.
2. **Un vídeo = una idea.** Si hay dos ideas, son dos vídeos.
3. Cada frase del guion tiene **su propia imagen**.
4. Los números son **reales** o se dice claramente "ejemplo".
5. Termina siempre con **moraleja** o **pregunta**, y el CTA a lo gratis del perfil.
6. Contenido con avatar o voz IA → **etiqueta de IA** activada.

---

## 5 formatos propios

| # | Nombre | Basado en | Pilar | Duración |
|---|---|---|---|---|
| F1 | **NOVATO VS PERTX** | REF01 | Construir con IA / Emprender | 35–45 s |
| F2 | **LA HERRAMIENTA** | REF02 | Construir con IA | 45–75 s |
| F3 | **AURO, ¿CUÁNTO?** | REF01 (datos) + REF02 (precio) | Dinero / Emprender | 30–40 s |
| F4 | **CONTRARRELOJ** | REF01 (pasos por tiempo) | Construir con IA / Disciplina | 35–50 s |
| F5 | **ME PREGUNTASTEIS** | REF02 (respuesta a comentarios) | Cualquiera | 30–60 s |

Los guiones de ejemplo usan `[corchetes]` donde va un dato **tuyo y real**. No me invento cifras.

---

### F1 · NOVATO VS PERTX

**Idea:** pantalla partida. A la izquierda, "el novato" (un Pertx gris y apagado, sin oro). A la derecha, **Pertx** con Auro. Se comparan dos formas de hacer lo mismo, paso a paso. Gana el que usa IA con cabeza, no el que trabaja más.

**Guion de ejemplo: "Crear una web para un cliente"** (≈40 s)

| Tiempo | Voz (Pertx) | Plano / qué se ve | Texto en pantalla |
|---|---|---|---|
| 0–3 s | "Un novato y yo hacemos la misma web para un cliente." | Pantalla partida: NOVATO (gris) / PERTX (oro) + Auro. Barra "DÍA 1" | `NOVATO` · `PERTX` · **WEB** |
| 3–8 s | "Día 1. El novato abre una plantilla y empieza a mover cajas." | Izq.: novato arrastrando bloques, reloj girando | **DÍA 1** · `4 h` |
| 8–13 s | "Yo le explico a Claude Code lo que quiere el cliente, en cinco frases." | Der.: grabación real de tu pantalla escribiendo el prompt | **5 FRASES** |
| 13–18 s | "En 20 minutos tengo la primera versión. Y la reviso línea a línea." | Der.: la web real apareciendo + Auro con `^ ^` | **20 MIN** · `REVISAR` |
| 18–24 s | "Día 2. El cliente pide cambios. El novato rehace la mitad." | Izq.: novato con cara de agobio, cajas cayendo | **DÍA 2** · `CAMBIOS` |
| 24–29 s | "Yo pido los cambios, los pruebo en el móvil y la subo a Vercel." | Der.: POV del móvil con la web + notificación "Desplegado" | **VERCEL** |
| 29–34 s | "Resultado: el novato, [X] horas. Yo, [Y] horas. Mismo precio." | Auro con holograma: barras [X] vs [Y] | **[X] h** vs **[Y] h** |
| 34–37 s | "No trabajo más que él. Uso mejor las herramientas." | Pertx a cámara, ojos de "decidido" | **MEJOR** |
| 37–40 s | "La guía de cómo lo hago, gratis en mi perfil. ¿Tú cuánto tardas?" | Móvil con el perfil y el botón "Guía gratis" | **PERFIL** · `¿Y tú?` |

**Qué grabar tú:** tu pantalla con Claude Code (8–13 s), la web real (13–18 s) y el móvil con la web (24–29 s). Todo lo demás es animación.

**Descripción:** `Mismo cliente, misma web. Uno trabaja más, otro trabaja mejor. ¿Tú cuánto tardas en hacer una web? 👇`
**Hashtags:** `#claudecode #ia #emprender #desarrolloweb #pertx`

---

### F2 · LA HERRAMIENTA

**Idea:** reseña honesta de **una** herramienta de IA que usas de verdad. Gancho con prueba real, qué es, cuánto cuesta, lo mejor, **para quién NO es**, y CTA. Tú con pasamontañas a cámara en la parte de la opinión (o el avatar si no grabas).

**Guion de ejemplo: "Claude Code"** (≈60 s)

| Tiempo | Voz (Pertx) | Plano / qué se ve | Texto en pantalla |
|---|---|---|---|
| 0–3 s | "Esta app la he hecho sin escribir casi ni una línea de código." | POV: tu móvil enseñando una app real tuya | **SIN CÓDIGO** |
| 3–8 s | "La ha escrito una IA que vive en mi terminal. Se llama Claude Code." | Grabación real de la terminal con Claude Code trabajando | **TERMINAL** |
| 8–15 s | "Le hablas como a un compañero: 'hazme una página de login'. Y lo hace, archivo por archivo." | Mockup oro: bocadillo de chat → lista de archivos creándose | **COMPAÑERO** |
| 15–22 s | "¿Cuánto cuesta? Va con la suscripción de Claude. Yo pago [plan y precio real]." | Auro con holograma de precio | **[PRECIO]** |
| 22–32 s | "Lo que más me gusta: lee todo tu proyecto antes de tocar nada, así no rompe lo que ya funciona." | Pantalla real: Claude leyendo archivos + Auro "pensativo" | **LEE TODO** |
| 32–45 s | "Te digo lo que pienso: si no sabes qué quieres construir, no te sirve de nada. La IA programa. Las ideas y las decisiones son tuyas." | **Tú a cámara con pasamontañas**, planos de manos (o Pertx avatar "pensativo") | **IDEAS** · **TUYAS** |
| 45–52 s | "Y revisa siempre lo que hace. Se equivoca, como cualquiera." | Pantalla con un error real y cómo lo arreglas | **REVISA** |
| 52–60 s | "Tengo una guía gratis con mis primeros pasos. En el perfil. ¿Qué quieres que construya con ella?" | Móvil con perfil + Pertx "señalando" | **PERFIL** · `¿Qué construyo?` |

**Qué grabar tú:** la app en tu móvil, la terminal con Claude Code, un error real, y tus manos y escritorio con pasamontañas.

**Descripción:** `Mi opinión sincera de Claude Code después de [X] proyectos. Lo bueno, lo malo y para quién no es.`
**Hashtags:** `#claudecode #inteligenciaartificial #programacion #herramientasia #pertx`

---

### F3 · AURO, ¿CUÁNTO?

**Idea:** Pertx le pregunta a Auro por los **números reales** del mes de un proyecto (ventas, visitas, gastos, horas). Auro los saca en hologramas. Al final, lo que se aprende. Es la serie de "números reales".

**Guion de ejemplo: "Mes 1 de Pertx"** (≈35 s)

| Tiempo | Voz | Plano / qué se ve | Texto en pantalla |
|---|---|---|---|
| 0–3 s | **Pertx:** "Auro, ¿cuánto he ganado este mes?" · **Auro:** "Calculando…" | Pertx "pensativo" + Auro con `?` | **¿CUÁNTO?** |
| 3–8 s | **Auro:** "Dato: [X] euros. De [N] ventas." *(ding)* | Auro con ojos `$ $` y holograma con la cifra | **[X] €** |
| 8–13 s | **Pertx:** "¿Y cuánto he gastado?" · **Auro:** "[Y] euros. Casi todo en [cosa real]." | Holograma de gastos | **−[Y] €** |
| 13–18 s | **Auro:** "Has trabajado [H] horas. Sale a [X/H] euros la hora." | Reloj + división animada | **[€/h]** |
| 18–25 s | **Pertx:** "No es mucho. Pero el mes pasado era cero." | Pertx a cámara / tus manos con el móvil | **CERO** → **[X]** |
| 25–30 s | **Pertx:** "Lo que más ha funcionado: [aprendizaje real]." | Pantalla real del proyecto | **[CLAVE]** |
| 30–35 s | **Auro:** "Próximo informe en 30 días." · **Pertx:** "¿Qué número quieres ver el mes que viene?" | Los dos juntos, Auro "feliz" | **MES 2** · `Comenta 👇` |

**Qué grabar tú:** tu móvil o panel con los datos reales (difuminando lo privado) y una pantalla del proyecto.

**Aviso legal:** son tus números, no consejos de inversión. Lo pondremos en la descripción.

**Descripción:** `Números reales del mes [N] de Pertx. Sin filtros. No es consejo financiero.`
**Hashtags:** `#emprender #numerosreales #negociodigital #ia #pertx`

---

### F4 · CONTRARRELOJ

**Idea:** reto con tiempo: "construyo X en Y horas". Auro hace de cronómetro (holograma con la cuenta atrás). Pasos cortos con la hora en pantalla. Al final, ¿lo consigue o no? (Si no lo consigue, también se publica: los fracasos enganchan).

**Guion de ejemplo: "Una web para la tienda de un amigo en 2 horas"** (≈45 s)

| Tiempo | Voz (Pertx) | Plano / qué se ve | Texto en pantalla |
|---|---|---|---|
| 0–3 s | "Tengo 2 horas para hacer la web de la tienda de un amigo. Auro, cronómetro." | Auro con holograma `2:00:00` y ojos `> >` | **2 HORAS** |
| 3–9 s | "Minuto 0. Le pido a Claude Code la estructura: inicio, productos y contacto." | Pantalla real + reloj `1:59` en una esquina | **MIN 0** |
| 9–15 s | "Minuto 25. Ya hay web… y es fea. Le paso los colores de la tienda." | Pantalla real: antes/después | **MIN 25** · `FEA` |
| 15–22 s | "Minuto 50. Fotos de los productos y un botón de WhatsApp." | POV móvil haciendo fotos + pantalla | **MIN 50** |
| 22–30 s | "Hora y media. Algo se rompe en el móvil." | Pantalla con el error, Auro "sorprendido" `!` | **1:30** · **ERROR** |
| 30–37 s | "Lo arreglo y la subo. Quedan [X] minutos." | Notificación "Desplegado" + Auro "celebrando" | **[X] MIN** |
| 37–42 s | "[Resultado real: ¿le ha gustado? ¿qué ha dicho?]" | Mensaje real del amigo (con permiso) | **[RESULTADO]** |
| 42–45 s | "¿Qué hago en 2 horas la próxima vez? Te leo en comentarios." | Pertx "señalando" | **¿PRÓXIMO RETO?** |

**Qué grabar tú:** la pantalla de principio a fin (luego cortamos), fotos de los productos y el mensaje del amigo.

**Descripción:** `2 horas, 1 web, 0 excusas. ¿Lo conseguí? ⏱️`
**Hashtags:** `#reto #claudecode #desarrolloweb #ia #pertx`

---

### F5 · ME PREGUNTASTEIS

**Idea:** coger el comentario más repetido de un vídeo anterior y responderlo (como REF02). Empieza enseñando los comentarios reales. Así se crea comunidad y la siguiente idea sale sola.

**Guion de ejemplo: "¿Se puede ganar dinero con apps hechas con IA?"** (≈40 s)

| Tiempo | Voz (Pertx) | Plano / qué se ve | Texto en pantalla |
|---|---|---|---|
| 0–3 s | "En el último vídeo me preguntasteis lo mismo [N] veces." | Mockup de comentarios reales en negro y oro, cayendo | **[N] VECES** |
| 3–6 s | "¿Se puede ganar dinero con apps hechas con IA?" | El comentario destacado y ampliado | **¿DINERO?** |
| 6–14 s | "Respuesta corta: sí, pero no como te lo venden. La IA te ahorra tiempo programando. No te trae clientes." | Pertx a cámara (o tú con pasamontañas), "decidido" | **NO TRAE CLIENTES** |
| 14–24 s | "Lo que a mí me ha funcionado: [vía real, por ejemplo hacer webs a negocios de mi zona]." | Pantalla real + Auro con holograma | **[VÍA REAL]** |
| 24–32 s | "Lo que no: [intento real que falló] y perdí [tiempo o dinero real]." | Pertx "pensativo", Auro con `?` | **[FALLO]** |
| 32–37 s | "Así que empieza por un problema real de alguien, no por la app." | Pertx "señalando" | **PROBLEMA REAL** |
| 37–40 s | "¿Cuál es tu siguiente pregunta?" | Los dos juntos | `Comenta 👇` |

**Qué grabar tú:** captura de los comentarios reales y la pantalla de lo que te ha funcionado.

**Descripción:** `La pregunta que más me hacéis. Mi respuesta sincera, con lo que me ha funcionado y lo que no.`
**Hashtags:** `#preguntas #emprenderjoven #ia #apps #pertx`

---

## Qué haría yo para empezar
1. **Formatos principales:** F1 (Novato vs Pertx) y F4 (Contrarreloj). Son los más parecidos a REF01, se pueden hacer casi enteros con nuestra animación en código y enseñan lo que sabes hacer.
2. **Serie fija mensual:** F3 (Auro, ¿cuánto?), aunque los números sean pequeños. Los números reales pequeños dan más confianza que los grandes inventados.
3. **F5 en cuanto haya comentarios.** F2 una vez por semana o cada dos semanas.
4. **Muy recomendado:** comprar o usar un pasamontañas negro y grabar tus manos y escritorio, como en REF02. Eso une el avatar contigo y le da credibilidad.
5. **Más referencias:** con 2 vídeos ya hay una fórmula clara. Si me pasas 3–5 más (sobre todo de dinero, finanzas y disciplina), la afino.

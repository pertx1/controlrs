# PERTX · Etapa 2 · 5 mascotas

- Cada mascota junto a Pertx: `personaje/png/M1.png` … `M5.png` (los originales en código están en `personaje/svg/`)
- Galería con las 5: `personaje/galeria-mascota.html`
- Pertx de cuerpo completo: `personaje/png/P1-oro-cuerpo.png`
- Pertx con los 3 objetos de escena: `personaje/png/P1-oro-escenas.png`

**Regla del objeto:** por defecto Pertx va **sin nada en la mano**. Solo lleva algo si la escena lo pide:

| Objeto | Cuándo |
|---|---|
| Nada (por defecto) | Casi siempre |
| Móvil | Mirar métricas, ventas que entran, notificaciones, redes |
| Portátil | Construir con IA, programar, enseñar la pantalla |

Más adelante podemos añadir otros (libreta, café, auriculares…).

Todas las mascotas usan el mismo estilo que Pertx: fondo negro cálido, sombras profundas y detalles en oro (`#D4AF37`, `#F5DE9A`, `#8E6E1E`).

---

## M1 · ONYX (cuervo · animal real)

**Archivo:** `png/M1.png` · En la imagen sale posado en un pedestal negro con "PX" dorado.

### Descripción física
| Parte | Detalle | HEX |
|---|---|---|
| Plumas | Negro con brillo morado-gris | `#16151A` / `#3A3640` / `#060607` |
| Ojo | Dorado con pupila negra y una ceja marcada (cara de listo) | `#D4AF37` |
| Pico | Negro mate, grande | `#141318` |
| Patas | Gris muy oscuro, con una anilla dorada en una pata | `#2A2620` / `#D4AF37` |
| Pedestal | Bloque negro con borde dorado y "PX" | `#0E0E10` |

### Personalidad y forma de hablar
Listo, observador y con humor negro. Habla poco y seco: "Tercer día sin publicar. Interesante." Se sabe todos tus datos y te los recuerda cuando no quieres.

### Rol en los vídeos
- **Disciplina:** aparece cuando te saltas una tarea ("Te vi, eh").
- **Datos:** suelta la cifra clave del vídeo ("312 € este mes. No está mal.").
- **Gancho:** grazna o aterriza en el plano en el segundo 0.

### Prompt maestro
```
Dark cinematic semi-realistic illustration, a sleek black raven mascot called Onyx perched on a black stone pedestal with a thin gold edge and a small gold serif "PX" engraved on it. Glossy black feathers with subtle purple-grey sheen (#16151A, #3A3640), one intelligent gold eye (#D4AF37) with a sharp raised feather brow giving a smart sarcastic look, matte black beak, a tiny gold ring on one leg. Standing next to a faceless young man in a black balaclava and black hoodie with hood up. Deep warm-black background (#080706 to #2A2219), thin gold rim light, quiet luxury, film noir mood, high detail.
```

### Prompt negativo
```
cute cartoon bird, big eyes, colorful feathers, parrot, crow with open wings attacking, horror, blood, gore, bright colors, daylight, real brand logos, extra text, multiple birds, watermark, blurry
```

### Por qué encaja
Un cuervo es misterioso, nocturno e inteligente, como Pertx. Le sigue el rollo al personaje sin hacerlo infantil y da para humor seco muy de TikTok.

---

## M2 · NOX (criatura de humo · inventada)

**Archivo:** `png/M2.png` · En la imagen, Pertx va sin nada en la mano.

### Descripción física
| Parte | Detalle | HEX |
|---|---|---|
| Cuerpo | Bola de humo negro que flota, con bordes difuminados y una estela abajo | `#0D0C10` / `#2A2830` |
| Ojos | Medias lunas brillantes en oro claro (mirada pícara) | `#F5DE9A` |
| Boca | Sonrisa en zigzag dorada | `#D4AF37` |
| Cuernitos | Dos cuernos pequeños con la punta dorada | `#0D0C10` / `#D4AF37` |
| Brazos | Dos brazos de humo | `#141319` |
| Extras | Chispas doradas alrededor | `#F5DE9A` |

### Personalidad y forma de hablar
Pícaro, caótico y tentador. Es la voz de las excusas: "Venga, hoy no publiques, mañana lo haces mejor." Se ríe de todo.

### Rol en los vídeos
- **Tentaciones y excusas:** Pertx le gana (o pierde) y eso es la historia del vídeo.
- **Bromas** y comentarios sarcásticos sobre tus fallos.
- **Celebra** las ventas inflándose y soltando chispas.

### Prompt maestro
```
Dark cinematic illustration, a small floating black smoke creature mascot called Nox, round body made of dense black smoke (#0D0C10, #2A2830) with soft blurry edges and a wispy smoke tail, two small horns with gold tips, glowing pale-gold crescent-shaped mischievous eyes (#F5DE9A), a thin glowing gold zigzag grin (#D4AF37), two little smoky arms, tiny gold sparks floating around. Floating next to a faceless young man in a black balaclava and black hoodie with hood up, with empty hands. Deep warm-black background (#080706 to #2A2219), gold rim light, mysterious, playful but not childish, high detail.
```

### Prompt negativo
```
cute kawaii, pastel colors, ghost with sheet, demon horror, scary teeth, blood, fire, bright colors, daylight, real brand logos, extra text, multiple creatures, watermark, blurry
```

### Por qué encaja
Es como la "sombra" de Pertx, así que conecta directo con el personaje. Es perfecto para el pilar de mentalidad: la lucha contra las excusas se cuenta sola.

---

## M3 · AURO (robot orbe · IA)

**Archivo:** `png/M3.png` · En la imagen, Pertx va sin nada en la mano.

### Descripción física
| Parte | Detalle | HEX |
|---|---|---|
| Cuerpo | Esfera negra mate que flota | `#151417` / `#3A393E` / `#050506` |
| Anillo | Anillo dorado alrededor, como un planeta | `#D4AF37` |
| Cara | Pantalla negra con ojos de píxel dorados (`^ ^` cuando está feliz) | `#050506` / `#F5DE9A` |
| Antena | Corta, con una luz dorada en la punta | `#D4AF37` |
| Propulsores | Dos chorros de luz dorada debajo | `#F5DE9A` |
| Extra | Holograma con una gráfica que sube | `#D4AF37` |

### Personalidad y forma de hablar
Asistente IA leal, eficiente y algo pedante: "He calculado que si publicas hoy, tu probabilidad de éxito sube un 34 %." Habla con frases exactas y datos.

### Rol en los vídeos
- **Enseña los números** con hologramas (ventas, visitas, seguidores).
- **Celebra las ventas:** los ojos cambian a `$ $` o `^ ^` y suena un "ding".
- **Ayudante en los tutoriales de IA:** representa a Claude Code y a las herramientas (sin usar sus logos).

### Prompt maestro
```
Dark cinematic illustration, a small floating spherical robot mascot called Auro, matte black sphere (#151417) with a thin gold ring around it like a planet (#D4AF37), a black glass face screen showing happy pixel-art eyes "^ ^" in pale gold (#F5DE9A), short antenna with a glowing gold tip, two soft golden thruster glows underneath, a small gold holographic chart with an upward arrow floating beside it. Hovering next to a faceless young man in a black balaclava and black hoodie with hood up, with empty hands. Deep warm-black background (#080706 to #2A2219), gold rim light, premium tech, high detail.
```

### Prompt negativo
```
humanoid robot, cute kawaii, big cartoon eyes, blue or neon colors, real AI company logos, ChatGPT logo, Claude logo, toy plastic look, daylight, extra text, multiple robots, watermark, blurry
```

### Por qué encaja
Es la mascota más "IA" y la que mejor encaja con el pilar de construir con IA y con enseñar números reales. Además es la más fácil de animar gratis: los ojos son píxeles y se pueden cambiar con código.

---

## M4 · TEMPO (reloj de arena · objeto con vida)

**Archivo:** `png/M4.png` · En la imagen, Pertx va sin nada en la mano.

### Descripción física
| Parte | Detalle | HEX |
|---|---|---|
| Estructura | Tapas y columnas doradas | `#D4AF37` / `#8E6E1E` |
| Cristal | Negro transparente con un brillo suave | `#0B0B0D` / `#3A3640` |
| Arena | Dorada, cayendo en un hilo fino | `#D4AF37` / `#F5DE9A` |
| Cara | En la parte de arriba: ojos negros y cejas firmes, boca recta (serio) | `#0A0A0A` |
| Brazos y piernas | Finos y dorados, con una mano levantada como avisando | `#D4AF37` |

### Personalidad y forma de hablar
Serio y estricto, como un entrenador: "Te quedan 3 horas. Muévete." No tiene paciencia con las excusas, pero se alegra en secreto cuando cumples.

### Rol en los vídeos
- **Marca el tiempo:** retos de "construyo esto en 1 hora" o cuentas atrás.
- **Recuerda las tareas** del sistema diario (`npm run hoy`).
- **Cambia la arena:** cuando se acaba, el reto termina. Queda muy visual.

### Prompt maestro
```
Dark cinematic illustration, a living hourglass mascot called Tempo, gold frame (#D4AF37, #8E6E1E) with dark smoked glass (#0B0B0D), gold sand flowing in a thin stream from top to bottom, a stern face on the upper glass bulb with black eyes and firm angled eyebrows and a straight mouth, thin gold arms and legs, one arm raised as if warning about time. Standing next to a faceless young man in a black balaclava and black hoodie with hood up. Deep warm-black background (#080706 to #2A2219), gold rim light, quiet luxury, high detail.
```

### Prompt negativo
```
cute cartoon clock, big smiling face, pastel colors, wooden hourglass, broken glass, bright colors, daylight, real brand logos, extra text, multiple objects, watermark, blurry
```

### Por qué encaja
Representa la disciplina, que es justo lo que tú necesitas siendo desordenado. Es original (casi nadie usa un objeto así) y da para formatos con cuenta atrás.

---

## M5 · NERO (gato negro · animal real)

**Archivo:** `png/M5.png` · En la imagen, Pertx va sin nada en la mano.

### Descripción física
| Parte | Detalle | HEX |
|---|---|---|
| Pelo | Negro con brillo suave | `#141317` / `#34323A` / `#060607` |
| Ojos | Dorados con pupila en raya y cejas de "te estoy juzgando" | `#F5DE9A` / `#C9971F` |
| Collar | Dorado con una chapa redonda "PX" | `#D4AF37` |
| Nariz | Marrón oscuro | `#3A2A22` |
| Pose | Sentado, con la cola enroscada | — |

### Personalidad y forma de hablar
Elegante, vago y juzgón. Casi no habla, juzga con la mirada. Cuando habla: "¿Eso es todo lo que has hecho hoy?" Aprueba tus victorias con un parpadeo lento.

### Rol en los vídeos
- **Reacciones:** su cara de asco o de aprobación vale por un meme.
- **Juzga tus excusas** sin decir nada.
- **Aprueba las victorias** con un parpadeo lento o tumbándose encima del portátil.

### Prompt maestro
```
Dark cinematic semi-realistic illustration, an elegant black cat mascot called Nero sitting upright with its tail curled, glossy black fur (#141317, #34323A), half-lidded judging gold eyes (#F5DE9A to #C9971F) with vertical slit pupils, a slim gold collar with a round gold "PX" tag. Sitting next to a faceless young man in a black balaclava and black hoodie with hood up, with empty hands. Deep warm-black background (#080706 to #2A2219), thin gold rim light, quiet luxury, film noir mood, high detail.
```

### Prompt negativo
```
cute kitten, big cartoon eyes, kawaii, colorful fur, white patches, scary cat, horror, bright colors, daylight, real brand logos, extra text, multiple cats, watermark, blurry
```

### Por qué encaja
Los gatos funcionan muy bien en TikTok, y un gato negro elegante encaja con el estilo oscuro y premium. Es el que más fácil hace reír sin decir nada.

---

## Mi recomendación como socio (honesta)

| | Encaja con Pertx | Fácil de animar gratis | Humor / viralidad | Original |
|---|---|---|---|---|
| **M1** Onyx (cuervo) | **Muy alto** | Media | Alta | Alta |
| **M2** Nox (humo) | Alto | Media | Alta | Alta |
| **M3** Auro (robot) | Alto | **Muy alta** | Media | Media |
| **M4** Tempo (reloj) | Medio | Alta | Media | **Muy alta** |
| **M5** Nero (gato) | Alto | Media | **Muy alta** | Media |

- **Mi favorita: M1 Onyx.** Es oscuro, listo y nocturno como Pertx, y da humor seco que no queda infantil.
- **Si quieres lo más viral: M5 Nero.** Los gatos reaccionando funcionan muy bien.
- **Si quieres lo más fácil de producir: M3 Auro.** Se puede animar entero con código y encaja con los vídeos de IA.
- **Idea extra:** Tempo (M4) podría salir de vez en cuando como "objeto" en los retos con tiempo, aunque elijas otra mascota.

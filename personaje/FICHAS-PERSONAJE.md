# PERTX · Etapa 1 · 5 versiones del personaje

- Dibujos (hechos en código SVG, con su código puesto): `personaje/svg/P1.svg` … `P5.svg`
- Galería para verlas juntas: `personaje/galeria.html` (ábrela con doble clic en el navegador)

> Los 5 dibujos los he hecho yo a mano en código, sin herramientas externas. Son **vistas previas de estilo**: sirven para elegir. Los *prompts maestros* de cada ficha están listos por si más adelante quieres sacar una versión con más detalle en un generador de imágenes (Higgsfield u otro), pero no hace falta usarlos ahora.

**Cómo usar los prompts (cuando toque):** copia el *prompt maestro* tal cual y pega el *prompt negativo* en el campo "negative prompt" (si la herramienta no lo tiene, añádelo al final con "Avoid: …"). Para que salga siempre igual, sube además el dibujo como imagen de referencia.

---

## P1 · 3D suave (tipo película de animación)

**Archivo:** `svg/P1.svg` · **Edad aparente:** 19 años · **Vibe:** el chaval majo que está empezando y se lo curra.

### Descripción física
| Parte | Detalle | HEX |
|---|---|---|
| Cara | Ovalada, rasgos suaves y redondeados, pecas en la nariz, media sonrisa, mofletes sonrosados | — |
| Piel | Oliva clara | `#E8B894` |
| Pelo | Castaño, rizado/ondulado y despeinado, un mechón cayendo en la frente | `#5A3825` |
| Ojos | Grandes, color avellana verdoso, cejas gruesas y expresivas | `#6B8E4E` |
| Sudadera | Oversize amarillo mostaza, logo blanco "PX" en el pecho, cordones blancos | `#F2A93B` |
| Camiseta | Blanca, se ve el cuello | `#FFFFFF` |
| Pantalón | Jogger cargo azul marino | `#1F2A44` |
| Zapatillas | Blancas gruesas con detalles naranja | `#FF6B35` |
| Accesorios | Smartwatch negro, un auricular blanco, portátil plateado con pegatinas de colores | — |
| Fondo | Gris cálido claro | `#F4F1EC` |

### Personalidad y forma de hablar
Cercano, optimista y algo torpe. Habla como un colega: frases cortas, "mira esto", "no te lo vas a creer", se ríe de sus propios fallos. Explica lo técnico como si se lo contara a su madre.

### Prompt maestro
```
Stylized 3D animated feature-film character, soft Pixar-like rendering, full body, front view, standing relaxed and confident. A 19-year-old young entrepreneur called Pertx. Soft rounded facial features, slightly oval face, light olive skin (#E8B894), a few freckles over the nose, rosy cheeks, big expressive hazel-green eyes (#6B8E4E), thick expressive dark-brown eyebrows, friendly confident half smile. Messy curly-wavy chestnut-brown hair (#5A3825) with one lock falling on the forehead. Wearing an oversized mustard-yellow hoodie (#F2A93B) with white drawstrings and a small white "PX" logo on the chest, white t-shirt collar visible, dark navy cargo joggers (#1F2A44), chunky plain white sneakers with orange accents (#FF6B35), thin black smartwatch, one white wireless earbud. Holding a slim silver laptop with colorful generic geometric stickers under his left arm. Soft studio lighting, subsurface scattering on skin, plain warm light-grey background (#F4F1EC), soft contact shadow, character design reference, centered, clean, high detail.
```

### Prompt negativo
```
real brand logos, Apple logo, Nike swoosh, flags, text other than PX, extra fingers, deformed hands, different hairstyle, straight hair, beard, glasses, hat, realistic photo, anime style, 2D, dark moody lighting, older face, muscular body, female, multiple characters, watermark, blurry
```

### Por qué encaja y dónde funciona mejor
- El estilo 3D "de peli" cae bien a todo el mundo y es fácil de animar con IA sin que dé mal rollo.
- Se lleva muy bien con una mascota al lado (estilo dúo de película).
- **Mejor para:** ganchos e intros, reacciones, vídeos de "emprender joven" y "mentalidad", miniaturas de YouTube.
- **Ojo:** si algún día lo generas en 3D con IA, hay que vigilar que la cara y la ropa no cambien entre vídeos (por eso siempre usaremos la misma referencia).

---

## P2 · Anime

**Archivo:** `svg/P2.svg` · **Edad aparente:** 18 años · **Vibe:** el hacker prodigio que programa de noche.

### Descripción física
| Parte | Detalle | HEX |
|---|---|---|
| Cara | Mandíbula afilada, sonrisa de medio lado, lunar bajo el ojo izquierdo | — |
| Piel | Clara | `#F3D2BC` |
| Pelo | Negro azabache en punta, mechón cian eléctrico en el flequillo | `#121318` / `#00E5FF` |
| Ojos | Rasgados, violeta grisáceo con brillos | `#7A6FF0` |
| Chaqueta | Cortavientos techwear negro, cuello alto, ribetes cian | `#16181D` / `#00E5FF` |
| Camiseta | Blanca con el símbolo `</>` | `#F5F5F5` |
| Pantalón | Cargo gris carbón con bolsillos laterales | `#2E3138` |
| Zapatillas | Botas altas blancas y negras, sin marca | — |
| Accesorios | Cascos blancos al cuello con aro cian, tablet holográfica con código | `#F5F5F5` |
| Fondo | Degradado azul marino con suelo de rejilla | `#0E1530` → `#1B2A5C` |

### Personalidad y forma de hablar
Seguro, rápido y un poco chulito (con gracia). Frases tipo "esto lo hice en 2 horas", "nadie te cuenta esto". Habla con ritmo, como si narrara un anime.

### Prompt maestro
```
Modern anime cel-shaded character illustration, clean crisp lineart, full body, front view. An 18-year-old young coder entrepreneur called Pertx, slim tall build, sharp jawline, determined smirk, fair skin (#F3D2BC). Spiky jet-black hair (#121318) with a bright electric-cyan streak (#00E5FF) in the fringe, narrow focused violet-grey eyes (#7A6FF0) with bright highlights, small mole under the left eye. Wearing an open black techwear windbreaker (#16181D) with high collar and cyan piping (#00E5FF), white t-shirt with a "</>" code symbol, charcoal tapered cargo pants (#2E3138) with side pockets, plain black and white high-top sneakers without logos, white over-ear headphones (#F5F5F5) resting around his neck with cyan rings. One hand in pocket, the other holding a glowing holographic tablet showing lines of code. Plain deep navy gradient background (#0E1530 to #1B2A5C) with a subtle perspective grid floor, cyan rim light, high quality anime key visual, character design sheet style, centered.
```

### Prompt negativo
```
real brand logos, Nike swoosh, Jordan logo, chibi, 3D render, realistic photo, western cartoon, extra fingers, deformed hands, different hair color, long hair, glasses, beard, female, multiple characters, text, watermark, blurry, sketchy lines
```

### Por qué encaja y dónde funciona mejor
- El anime tiene muchísimo tirón entre gente de 15–25 años y en nichos de programación y productividad.
- Queda muy bien sobre fondos oscuros de pantalla (editor de código).
- **Mejor para:** vídeos de "construir con IA" (pantalla + personaje en una esquina), retos tipo "hago una app en 24 h".
- **Ojo:** es más difícil de mantener igual cuando se anima y puede parecer "otra cuenta más de anime". Encaja peor con el pilar de dinero/finanzas (transmite menos seriedad).

---

## P3 · Semi-realista cinematográfico

**Archivo:** `svg/P3.svg` · **Edad aparente:** 24 años · **Vibe:** creador serio, emprendedor de escritorio nocturno.

> En SVG no se puede hacer una foto real: es una ilustración con proporciones realistas, luces y sombras. Si eliges este estilo, la versión "final" saldría de un generador de imágenes con el prompt de abajo.

### Descripción física
| Parte | Detalle | HEX |
|---|---|---|
| Cara | Mandíbula marcada, barba de pocos días, expresión tranquila con sonrisa ligera | — |
| Piel | Clara cálida | `#D9A57E` |
| Pelo | Castaño oscuro corto, texturizado, con degradado en los lados | `#2B1F17` |
| Ojos | Marrones cálidos | `#5C3B22` |
| Jersey | Punto, cuello redondo, gris carbón | `#3A3A3C` |
| Camiseta | Cuello blanco asomando | `#F2F2F2` |
| Accesorios | Reloj negro minimalista, taza negra | — |
| Entorno | Escritorio de madera, monitor con código (luz azul), lámpara ámbar, ventana con luces de ciudad | `#FFB347` / `#3D7BFF` |

### Personalidad y forma de hablar
Calmado, directo y con datos. "Te cuento cómo lo hice, con números." Pocas bromas, mucha claridad.

### Prompt maestro
```
Cinematic semi-realistic portrait, medium shot from the waist up, of a 24-year-old young entrepreneur called Pertx sitting at a minimalist wooden desk at night with forearms resting on the desk. Short textured dark-brown hair (#2B1F17) with a low fade, light stubble beard, warm brown eyes (#5C3B22), warm light skin (#D9A57E), calm focused expression with a slight knowing smile, looking at camera. Wearing a charcoal crewneck knit sweater (#3A3A3C) over a white t-shirt collar (#F2F2F2), minimal black watch, black mug on the desk. Behind him a monitor glowing with code, a warm amber desk lamp (#FFB347) and a cool blue monitor glow (#3D7BFF) as split lighting, window with blurred generic city lights at night. 50mm lens look, shallow depth of field, natural skin texture, editorial YouTube creator aesthetic, high detail.
```

### Prompt negativo
```
cartoon, anime, 3D render, plastic skin, airbrushed, real company logos, ChatGPT logo, readable brand names, recognizable landmarks, extra fingers, deformed hands, long hair, glasses, hat, heavy beard, older than 30, female, multiple people, text, watermark, overexposed
```

### Por qué encaja y dónde funciona mejor
- Da imagen "premium" y seria, útil para el pilar de dinero y para vender servicios.
- **Mejor para:** miniaturas de YouTube largo, vídeos de números reales.
- **Ojo, honestamente no te lo recomiendo como cara principal:**
  1. Un humano realista hecho con IA parece una persona real que no eres tú. En una marca que va de "contar mi camino en público" eso puede sentirse como un engaño, aunque lo etiquetes.
  2. Es el más difícil de mantener idéntico (cada generación cambia un poco la cara) y en vídeo se nota mucho el "valle inquietante".
  3. Las plataformas son más estrictas con avatares realistas: siempre habría que marcarlo como contenido IA.

---

## P4 · Minimalista / flat

**Archivo:** `svg/P4.svg` · **Edad aparente:** joven sin edad concreta · **Vibe:** icono de marca, simple y reconocible.

### Descripción física
| Parte | Detalle | HEX |
|---|---|---|
| Cara | Cabeza redonda perfecta, sin nariz, dos ojos de punto, sonrisa de línea, mofletes coral | — |
| Piel | Melocotón | `#F1C6A0` |
| Pelo | Negro, bloque geométrico con flequillo recto y patilla | `#1B1B1B` |
| Sudadera | Azul cobalto con bolsillo canguro y cordones blancos | `#2B59FF` / `#1F45D6` |
| Pantalón | Recto gris muy claro | `#E1E4EC` |
| Zapatillas | Coral con suela blanca | `#FF6B6B` |
| Accesorios | Portátil abierto en una mano, saludando con la otra | `#CDD2DD` |
| Fondo | Lila muy claro con círculo decorativo | `#EEF1FF` / `#DDE3FF` |

### Personalidad y forma de hablar
Tranquilo, ordenado y con humor seco. Es "la versión organizada de ti": "tres pasos, sin rollo". Frases cortas y en lista.

### Prompt maestro
```
Minimalist flat vector character illustration, geometric shapes, no gradients, no outlines, no texture, clean modern brand mascot style. Full body front view of a young entrepreneur character called Pertx, ageless young adult. Perfectly round head with peach skin (#F1C6A0), no nose, two small solid black dot eyes (#1B1B1B), a simple curved smile line, small coral blush circles. Geometric black hair block (#1B1B1B) with a straight fringe and one sideburn. Wearing a cobalt-blue hoodie (#2B59FF) with darker kangaroo pocket (#1F45D6) and white drawstrings, straight very light grey trousers (#E1E4EC), coral sneakers (#FF6B6B) with white soles. One arm raised waving, the other holding an open simple grey laptop (#CDD2DD). Simple long limbs. Plain pale lilac background (#EEF1FF) with one soft decorative circle (#DDE3FF), flat shadow ellipse under the feet, centered, lots of negative space, vector art, Dribbble-quality illustration.
```

### Prompt negativo
```
gradients, outlines, texture, 3D, realistic, anime, detailed face, nose, big eyes, teeth, hat, logos, text, extra fingers, complex background, shading, multiple characters, watermark, blurry
```

### Por qué encaja y dónde funciona mejor
- Es **el más fácil de mantener idéntico** siempre y el más fácil de animar gratis (incluso con código en la etapa de edición, Remotion/SVG). Encaja perfecto con "0 € extra".
- **Mejor para:** vídeos de pantalla con el personaje en una esquina, explicaciones paso a paso, carruseles, stickers y logo de marca.
- **Ojo:** al ser tan simple transmite menos emoción en primer plano; necesita una mascota con mucha expresión para compensar.

---

## P5 · Cartoon 2D

**Archivo:** `svg/P5.svg` · **Edad aparente:** 22 años · **Vibe:** caos creativo, energía a tope.

### Descripción física
| Parte | Detalle | HEX |
|---|---|---|
| Cara | Cabeza grande y redonda, sonrisa enorme con hueco entre los dientes, cejas levantadas | — |
| Piel | Bronceado claro | `#F0C08A` |
| Ojos | Grandes, gafas redondas gruesas negras | `#111111` |
| Pelo | Rizado negro asomando por los lados | `#1A1A1A` |
| Gorro | Beanie naranja vivo con dobladillo | `#FF7A00` / `#E86A00` |
| Chaqueta | Bomber morada con parche "Pertx" | `#7B2FF7` / `#5B1FC2` |
| Camiseta | Amarilla con un rayo | `#FFD23F` |
| Pantalón | Vaquero ancho azul claro | `#8EC5FF` |
| Zapatillas | Rojas gruesas | `#FF3B3B` |
| Accesorios | Móvil en el bolsillo del pecho, pulgar arriba | — |
| Fondo | Crema amarillento con destellos | `#FFF4D6` |
| Contorno | Línea negra gruesa en todo | `#111111` |

### Personalidad y forma de hablar
Hiperactivo, exagerado y muy gracioso. "¡TÍO, MIRA ESTO!" Reacciona a todo y celebra cada pequeña victoria. Ideal para reírse de ser desordenado.

### Prompt maestro
```
Bold modern 2D cartoon character, thick black outlines (#111111), flat bright cel colors, sticker-like look, exaggerated proportions with a very big head and small body, expressive like a modern YouTube animated series. Full body front view of a 22-year-old hyperactive young entrepreneur called Pertx doing a thumbs up with a huge open grin showing a small gap between front teeth, raised eyebrows. Round face, light tan skin (#F0C08A), big round black eyes with white highlights behind round thick black glasses, curly black hair (#1A1A1A) sticking out on both sides from a bright orange ribbed beanie (#FF7A00). Wearing a purple bomber jacket (#7B2FF7) with a small white "Pertx" name patch, yellow t-shirt (#FFD23F) with a black lightning bolt, light blue baggy jeans (#8EC5FF), red chunky sneakers (#FF3B3B). A smartphone in the chest pocket, other hand on the hip. Plain warm cream-yellow background (#FFF4D6) with two small yellow sparkles, simple ground shadow, centered, clean vector cartoon, high quality.
```

### Prompt negativo
```
3D render, realistic, anime, thin lines, gradients, real brand logos, extra fingers, deformed hands, no glasses, different hat color, straight hair, beard, female, multiple characters, extra text, watermark, blurry, muted colors
```

### Por qué encaja y dónde funciona mejor
- Destaca muchísimo en el feed (colores fuertes) y es perfecto para humor y memes.
- **Mejor para:** el pilar de "mentalidad y disciplina siendo desordenado", reacciones, fails y celebraciones de ventas.
- **Ojo:** tanta energía cansa en vídeos largos y resta credibilidad a los temas de dinero.

---

## Mi recomendación como socio (honesta)

| | Constancia (sale siempre igual) | Fácil de animar gratis | Cae bien / viralidad | Credibilidad (dinero, servicios) |
|---|---|---|---|---|
| **P1** 3D suave | Media-alta | Media | **Alta** | Alta |
| **P2** Anime | Media | Baja | Alta (nicho) | Media |
| **P3** Semi-realista | Baja | Baja | Media | Alta, pero riesgo de parecer engaño |
| **P4** Flat minimal | **Muy alta** | **Muy alta** | Media | Media-alta |
| **P5** Cartoon 2D | Alta | Alta | Alta | Baja-media |

- **Mi favorito: P1.** Es el que mejor equilibra simpatía, credibilidad y dúo con mascota.
- **Plan B si quieres lo más barato y constante:** P4 (se puede animar entero con código, gratis).
- **Mezcla que funcionaría bien:** cuerpo y cara de P1 con el contorno negro grueso de P5 → queda más "sticker" y es más fácil de animar en 2D.
- **No recomiendo P3** como cara principal por lo explicado arriba.

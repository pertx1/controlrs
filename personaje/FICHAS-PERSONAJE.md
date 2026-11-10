# PERTX · Etapa 1 · 5 versiones del personaje (ronda 2: oscuro y con la cara tapada)

- Dibujos con su código puesto: `personaje/png/P1.png` … `P5.png` (los originales en código están en `personaje/svg/`)
- Galería con las 5 juntas: `personaje/galeria.html`
- La ronda 1 (estilo infantil, descartada) está guardada en `personaje/descartados/v1/`

**Idea común:** Pertx nunca enseña la cara. Lleva pasamontañas (o algo parecido) y el estilo es oscuro y adulto. El misterio forma parte de la marca: "no importa quién soy, importa lo que construyo".

Los *prompts maestros* están listos por si algún día quieres una versión con más detalle en un generador de imágenes. Para elegir no hace falta usarlos.

---

## ✅ VERSIÓN ELEGIDA: P1 Sombra con los colores de P5 (`P1-oro`)

Archivos: `svg/P1-oro.svg` · `png/P1-oro.png`

Es el mismo diseño que P1 (pasamontañas de una ranura, capucha puesta, portátil con "PX"), pero con la paleta de P5: negro cálido y oro en lugar de cian.

| Parte | Detalle | HEX |
|---|---|---|
| Pasamontañas | Negro mate de punto, una ranura horizontal para los ojos | `#0B0B0C` → `#2C2C2E` |
| Ojos | Marrón oscuro con reflejo dorado | `#2E2219` / `#F5DE9A` |
| Piel (ranura) | Morena cálida, iluminada en dorado desde abajo | `#C08E6A` |
| Sudadera | Negra cálida con la capucha puesta | `#1F1E22` / `#0E0E10` |
| Cordones | Crema con puntas doradas | `#E8DCC4` / `#D4AF37` |
| Luz | Brillo dorado del portátil y línea de luz dorada en el borde de la capucha | `#D4AF37` |
| Portátil | Negro con "PX" dorado en la tapa | `#0B0B0C` / `#D4AF37` |
| Fondo | Negro cálido | `#080706` → `#2A2219` |

**Prompt maestro (provisional)**
```
Dark cinematic semi-realistic illustration, waist-up portrait, front view, of a faceless young entrepreneur called Pertx wearing a matte black knitted balaclava with a single horizontal eye slit, only his dark brown eyes visible with warm gold reflections, hood of a warm-black hoodie (#1F1E22) pulled up over the balaclava, cream drawstrings with gold tips. He sits in a dark room lit only by the warm golden glow (#D4AF37) of a black laptop in front of him; the laptop lid faces the viewer with a small gold "PX" logo. Thin gold rim light on the edge of the hood, deep warm-black background (#080706 to #2A2219), quiet luxury, film noir mood, subtle knit texture, mysterious, high detail.
```

**Prompt negativo (provisional)**
```
visible face, visible mouth, nose, smile, cyan or blue light, bright colors, daylight, cartoon, anime, childish, cute, weapons, cash, money bags, gold chains, criminal scene, police, real brand logos, text other than PX, extra fingers, deformed hands, multiple people, watermark, blurry
```

La ficha definitiva, con poses, expresiones, voz y reglas, irá en `FICHA-FINAL.md` cuando elijas la mascota.

---

## P1 · SOMBRA (noir semi-realista)

**Vibe:** el que construye de noche, a solas, con la luz de la pantalla. Serio y con misterio.

### Descripción física
| Parte | Detalle | HEX |
|---|---|---|
| Pasamontañas | Negro de punto, con una sola ranura horizontal para los ojos | `#141518` |
| Ojos | Marrón oscuro, con reflejo cian de la pantalla | `#2E2219` / `#7DE6FF` |
| Piel (ranura) | Morena cálida, en sombra | `#C99A78` |
| Sudadera | Negra/gris carbón, con la capucha puesta y cordones gris claro | `#1C1D22` / `#BFC6CF` |
| Luz | Solo del monitor, en cian, con una línea de luz en el borde de la capucha | `#29D3FF` |
| Accesorios | Portátil de espaldas con "PX" brillando en la tapa | `#0C0D10` |
| Fondo | Casi negro | `#07080A` → `#1A1C22` |

### Personalidad y forma de hablar
Habla poco, despacio y con frases cortas que pegan: "Nadie me conoce. Pero esto ya factura." Tono de narrador de documental, sin gritar. Nada de humor fácil.

### Prompt maestro
```
Dark cinematic semi-realistic illustration, waist-up portrait, front view, of a faceless young entrepreneur called Pertx wearing a black knitted balaclava with a single horizontal eye slit, only his dark brown eyes visible, hood of a charcoal-black hoodie pulled up over the balaclava, light grey drawstrings. He sits in a pitch-dark room lit only by the cyan glow (#29D3FF) of a laptop in front of him; the laptop lid faces the viewer with a small glowing "PX" logo. Cyan rim light on the edge of the hood, cyan reflections in the eyes, deep shadows, film noir mood, subtle knit texture, moody, mysterious, high detail, near-black background (#07080A).
```

### Prompt negativo
```
visible face, visible mouth, nose, smile, bright colors, daylight, cartoon, anime, childish, cute, weapons, money bags, criminal scene, police, real brand logos, text other than PX, extra fingers, deformed hands, multiple people, watermark, blurry
```

### Por qué encaja y dónde funciona mejor
- Es el que mejor cuenta la historia de "chaval que construye de noche con IA".
- Queda natural metido en la esquina de un vídeo de pantalla oscura (editor de código, Claude Code).
- **Mejor para:** construir con IA, números reales, frases de mentalidad con texto grande en pantalla.

---

## P2 · GLITCH (cyberpunk neón)

**Vibe:** medio humano, medio IA. Tiene los ojos de LED y parece que "se cuelga" con un glitch.

### Descripción física
| Parte | Detalle | HEX |
|---|---|---|
| Pasamontañas | Gris oscuro de punto, con dos agujeros para los ojos y uno para la boca | `#15131C` → `#3A3742` |
| Ojos | Luces LED blancas con brillo cian (no se ve el ojo real) | `#FFFFFF` / `#00F0FF` |
| Boca | Ranura negra con una línea magenta | `#07050D` / `#FF2BD6` |
| Chaqueta | Techwear morado oscuro con costuras de neón y cuello alto con LED | `#231D36` / `#FF2BD6` / `#00F0FF` |
| Detalle | Parche "PX" en el pecho en cian | `#00F0FF` |
| Efecto | Barras de glitch magenta, cian y blancas alrededor de la cabeza | — |
| Fondo | Ciudad neón de noche con suelo de rejilla | `#0D0221` → `#1D0B45` |

### Personalidad y forma de hablar
Frío y rápido, como un sistema: "Proceso completado. 3 clientes nuevos." Puede usar efectos de voz robótica suave y frases tipo "iniciando…".

### Prompt maestro
```
Cyberpunk neon digital illustration, waist-up portrait, front view, of a faceless young entrepreneur called Pertx wearing a dark grey knitted ski mask with two eye holes and a mouth slit; instead of eyes, two glowing white LED lights with cyan glow (#00F0FF); a thin magenta line (#FF2BD6) glowing in the mouth slit. Wearing a dark purple techwear jacket (#231D36) with high collar, magenta LED strip on the collar, neon cyan and magenta seams, small cyan "PX" patch on the chest. Subtle digital glitch effect: horizontal magenta and cyan slices displaced around the head. Background: night neon city skyline and perspective grid floor in deep purple (#0D0221 to #1D0B45). High contrast, sharp, synthwave mood.
```

### Prompt negativo
```
visible face, human eyes, skin, smile, daylight, cartoon, childish, cute, anime, weapons, criminal scene, real brand logos, text other than PX, extra fingers, deformed hands, multiple people, watermark, blurry, low contrast
```

### Por qué encaja y dónde funciona mejor
- Es el más "IA" de todos: encaja directo con el pilar de construir con IA.
- Los ojos LED se pueden animar muy fácil (parpadeo, brillo cuando habla), gratis y con código.
- **Mejor para:** herramientas de IA, automatizaciones, "la IA hizo esto en 10 minutos".
- **Ojo:** la estética cyberpunk está muy vista. Encaja peor con los temas de dinero y disciplina.

---

## P3 · CALLE (póster de serigrafía)

**Vibe:** streetwear, rebelde, como un cartel pegado en la pared. Mucha fuerza gráfica.

### Descripción física
| Parte | Detalle | HEX |
|---|---|---|
| Cabeza | Gorra negra y la capucha negra por encima | `#0E0E0E` / `#1C1C1C` |
| Cara | En sombra total; solo se ve el brillo de los ojos | `#050505` / `#E9E2D3` |
| Braga de cuello | Negra, tapa nariz y boca, con dos rayas rojas | `#1A1A1A` / `#E10600` |
| Sudadera | Negra, cordones blancos roto, pegatina roja "PX" | `#0E0E0E` / `#E10600` |
| Fondo | Papel crema con un gran círculo rojo, puntos de trama y "PERTX" en vertical | `#E9E2D3` / `#E10600` |
| Textura | Grano de papel y trama de puntos | — |

### Personalidad y forma de hablar
Directo y sin filtro: "Deja de mirar tutoriales. Construye." Frases cortas, como eslóganes. Rebeldía contra "lo de siempre" (estudiar, trabajar, esperar).

### Prompt maestro
```
Bold screenprint street poster illustration, two-color style black (#0E0E0E) and red (#E10600) on cream paper (#E9E2D3), waist-up front view of a faceless young entrepreneur called Pertx: black cap pulled low with a black hoodie hood over it, face completely in shadow with only two small eye highlights visible, black neck gaiter covering nose and mouth with two red stripes, black hoodie with off-white drawstrings and a red "PX" sticker. Behind him a large red circle with halftone dot texture, the word "PERTX" in bold black vertical letters on the right side. Paper grain, halftone shading, high contrast, stencil graphic look, streetwear poster aesthetic.
```

### Prompt negativo
```
visible face, mouth, nose, smile, gradients, 3D, realistic photo, many colors, cartoon, childish, cute, weapons, gang signs, criminal scene, real brand logos, extra text, extra fingers, deformed hands, multiple people, watermark, blurry
```

### Por qué encaja y dónde funciona mejor
- Es el que más destaca en el feed: rojo, negro y crema se ven desde lejos.
- Queda muy bien como portada fija de vídeo y en carruseles con frases.
- **Mejor para:** mentalidad y disciplina, opiniones fuertes, portadas de serie.
- **Ojo:** es más un estilo de cartel que un personaje para animar. Funciona mejor en imágenes fijas que hablando en vídeo.

---

## P4 · ICONO (flat monocromo + verde ácido)

**Vibe:** un logo con vida. Negro total con un único color de marca.

### Descripción física
| Parte | Detalle | HEX |
|---|---|---|
| Pasamontañas | Negro puro, forma redondeada simple, una sola abertura para los ojos | `#000000` |
| Ojos | Dos círculos blancos con pupila negra | `#FFFFFF` / `#000000` |
| Piel (abertura) | Morena clara | `#D9A27E` |
| Cuerpo | Silueta negra de sudadera | `#000000` |
| Color de marca | Verde ácido en el suelo, el parche "PX" y la etiqueta | `#C6FF00` |
| Fondo | Gris casi negro con cuadrícula suave | `#121212` / `#1E1E1E` |

### Personalidad y forma de hablar
Seco y ordenado: "Paso 1. Paso 2. Paso 3. Hecho." Humor muy seco de vez en cuando. Es el sistema de organización que tú necesitas.

### Prompt maestro
```
Minimal flat vector icon-style character, no gradients, no texture, bold simple geometric shapes, front view, of a faceless young entrepreneur called Pertx: pure black rounded balaclava (#000000) with a single wide rounded eye opening showing light tan skin (#D9A27E) and two simple white round eyes with black pupils, three subtle horizontal knit lines on the lower mask, simple black hoodie silhouette with a small acid-green (#C6FF00) "PX" patch. Dark charcoal background (#121212) with a faint grid, solid acid-green floor band at the bottom. Logo-ready, high contrast, clean modern brand mascot.
```

### Prompt negativo
```
gradients, texture, 3D, realistic, anime, visible mouth, nose, detailed face, helmet, many colors, cartoon, childish, cute, weapons, real brand logos, extra text, extra fingers, multiple characters, watermark, blurry
```

### Por qué encaja y dónde funciona mejor
- Es **el más fácil de mantener siempre igual** y de animar gratis con código (parpadeo, moverse, reaccionar).
- Se puede usar como logo, foto de perfil, sticker y marca de agua en todos los vídeos.
- **Mejor para:** el personaje en la esquina de vídeos de pantalla, tutoriales paso a paso, el sistema diario.
- **Ojo:** al ser tan simple, transmite poca emoción. Necesitará una mascota con más expresión.

---

## P5 · ÉLITE (lujo oscuro con oro)

**Vibe:** el empresario silencioso. Elegante, frío y con dinero, pero sin presumir.

### Descripción física
| Parte | Detalle | HEX |
|---|---|---|
| Pasamontañas | Negro mate de punto con "PX" bordado en oro en la frente, dos agujeros para los ojos | `#0B0B0C` → `#2C2C2E` / `#D4AF37` |
| Ojos | Marrones, mirada tranquila, con un brillo dorado | `#2A1C12` / `#F5DE9A` |
| Piel (agujeros) | Morena cálida | `#C08E6A` |
| Ropa | Jersey negro de cuello alto y abrigo negro de lana con solapas | `#111111` / `#1F1E22` |
| Detalle | Broche dorado redondo en la solapa | `#D4AF37` |
| Luz | Foco cálido dorado desde arriba, con una línea de luz dorada en el borde | `#D4AF37` |
| Fondo | Negro cálido | `#080706` → `#2A2219` |

### Personalidad y forma de hablar
Calmado, seguro y con autoridad: "El dinero no se gana. Se construye." Habla poco y en tono bajo, nunca de forma exagerada.

### Prompt maestro
```
Dark luxury cinematic illustration, waist-up portrait, front view, of a faceless young entrepreneur called Pertx wearing a matte black knitted balaclava with two eye holes and a small gold embroidered "PX" (#D4AF37) on the forehead, calm brown eyes with a warm gold reflection. Wearing a black ribbed turtleneck sweater and a tailored black wool overcoat with wide lapels and a small round gold pin. Soft warm golden spotlight from above, thin gold rim light on the edges, deep warm black background (#080706 to #2A2219), elegant, minimal, quiet wealth aesthetic, high detail.
```

### Prompt negativo
```
visible face, mouth, nose, smile, flashy jewelry, gold chains, cash, money bags, sports cars, weapons, criminal scene, bright colors, cartoon, childish, cute, anime, real brand logos, extra text, extra fingers, deformed hands, multiple people, watermark, blurry
```

### Por qué encaja y dónde funciona mejor
- Da mucha credibilidad para los temas de dinero, finanzas y venta de servicios.
- Queda muy bien en miniaturas de YouTube y portadas de vídeos largos.
- **Mejor para:** dinero y finanzas, ingresos reales, frases de mentalidad "premium".
- **Ojo:** "pasamontañas + dinero" puede parecer un ladrón o un "gurú de cursos". Por eso nada de billetes, cadenas ni coches: el oro solo en detalles pequeños.

---

## Mi recomendación como socio (honesta)

| | Sale siempre igual | Fácil de animar gratis | Destaca en el feed | Credibilidad (dinero, servicios) |
|---|---|---|---|---|
| **P1** Sombra | Alta | Media | Media-alta | Alta |
| **P2** Glitch | Alta | **Muy alta** (ojos LED) | Alta | Media |
| **P3** Calle | Media | Baja (mejor en imagen fija) | **Muy alta** | Media |
| **P4** Icono | **Muy alta** | **Muy alta** | Media | Media-alta |
| **P5** Élite | Alta | Media | Media | **Muy alta** |

- **Mi favorito: P1 (Sombra).** Cuenta tu historia (construir de noche con IA), encaja con los 4 pilares y queda natural sobre vídeos de pantalla.
- **Mezcla que yo haría: P1 con el "PX" bordado en oro de P5.** Tienes el misterio de P1 y un toque premium para los vídeos de dinero.
- **P4 como logo y foto de perfil**, combinado con el personaje que elijas.
- **Un aviso sincero:** la estética de pasamontañas está de moda en cuentas faceless de dinero e IA. Funciona, pero te van a comparar. Lo que te diferenciará será la mascota, enseñar tu pantalla real y dar números de verdad, no el pasamontañas.

# PERTX · FICHA FINAL DEL PERSONAJE

## Código definitivo: `P1-oro+M3`

**Pertx** (P1 Sombra con la paleta de P5) + **AURO** (M3, robot orbe de IA).

Esta ficha es **la referencia para todo lo demás**: guiones, edición, miniaturas, web. Si algo no cuadra con esta ficha, está mal.

| Imagen | Archivo |
|---|---|
| Imagen principal (Pertx + Auro) | `png/FINAL-P1oro-M3.png` |
| Las 5 poses y expresiones | `png/FINAL-expresiones.png` |
| Pertx de cuerpo completo | `png/P1-oro-cuerpo.png` |
| Pertx con los objetos de escena | `png/P1-oro-escenas.png` |

Los dibujos están hechos en código (carpeta `svg/` y scripts `.py`). Si cambias algo, ejecuta:
```
python3 personaje/hacer-mascotas.py
python3 personaje/hacer-ficha-final.py
```

---

## 1. Descripción fija

### Pertx
Joven emprendedor **sin cara**. Nunca se le ve la cara, la boca ni el pelo.

| Parte | Siempre así | HEX |
|---|---|---|
| Pasamontañas | Negro mate de punto, con **una sola ranura horizontal** para los ojos y una costura vertical en el centro | `#0B0B0C` → `#2C2C2E` |
| Ojos | Marrón oscuro, con un pequeño reflejo dorado | `#2E2219` / `#F5DE9A` |
| Piel (solo en la ranura) | Morena cálida | `#C08E6A` |
| Sudadera | Negra cálida oversize, **capucha siempre puesta**, bolsillo canguro | `#1F1E22` / `#0E0E10` |
| Cordones | Crema con puntas doradas | `#E8DCC4` / `#D4AF37` |
| Pantalón | Jogger negro con puños | `#18171A` / `#0B0B0C` |
| Zapatillas | Negras, con una raya dorada y la suela oscura dorada | `#141416` / `#D4AF37` / `#8E6E1E` |
| Manos | Piel morena, sin guantes ni anillos | `#B98A66` |
| Luz | Siempre luz dorada en el borde (de la capucha y del lado derecho) | `#D4AF37` |

### Objeto en la mano (según la escena)
| Objeto | Cuándo | Detalle |
|---|---|---|
| Nada | Mentalidad, reflexiones, reaccionar a Auro | Mano izquierda en el bolsillo |
| Móvil | Métricas, ventas, notificaciones, redes | Pantalla dorada que le ilumina |
| Portátil | Construir con IA, programar, enseñar la pantalla | Negro, con **"PX" dorado** en la tapa, brillo dorado |

### AURO (mascota)
| Parte | Siempre así | HEX |
|---|---|---|
| Cuerpo | Esfera negra mate, **flota** (nunca toca el suelo) | `#151417` / `#3A393E` / `#050506` |
| Anillo | Anillo dorado alrededor, un poco inclinado, como un planeta | `#D4AF37` |
| Cara | Pantalla negra redondeada con **ojos de píxel dorados** | `#050506` / `#F5DE9A` |
| Antena | Corta, con la luz dorada en la punta | `#D4AF37` |
| Propulsores | Dos chorros de luz dorada debajo | `#F5DE9A` |
| Holograma | Panel dorado transparente al lado (gráfica, ?, !, flecha) | `#D4AF37` |
| Tamaño | Más o menos como la cabeza y los hombros de Pertx | — |

### Fondo y ambiente
Negro cálido con un foco dorado suave desde arriba (`#080706` → `#13100C` → `#2A2219`). Línea dorada fina en el suelo. Nada de colores fríos (azul, cian, morado).

---

## 2. Paleta de colores

| Uso | Nombre | HEX |
|---|---|---|
| Fondo | Negro cálido | `#080706` |
| Fondo | Marrón muy oscuro | `#13100C` |
| Fondo (foco) | Marrón dorado oscuro | `#2A2219` |
| Ropa | Negro carbón | `#1F1E22` |
| Ropa (sombras) | Negro | `#0B0B0C` |
| Acento principal | Oro | `#D4AF37` |
| Acento claro | Oro pálido | `#F5DE9A` |
| Acento oscuro | Oro viejo | `#8E6E1E` |
| Piel | Moreno cálido | `#C08E6A` |
| Texto claro | Crema | `#F3EEE3` |

**Para textos en pantalla y subtítulos:** blanco crema `#F3EEE3`, y la palabra clave en oro `#D4AF37`.

---

## 3. Prompts maestros (por si usas un generador de imágenes o vídeo)

Sube siempre `png/FINAL-P1oro-M3.png` como **imagen de referencia**. Así sale mucho más parecido.

### Pertx solo
```
Dark cinematic semi-realistic illustration, full body, front view, of a faceless young entrepreneur called Pertx: matte black knitted balaclava with a single horizontal eye slit and a vertical center seam, only his dark brown eyes visible with small warm gold reflections, warm brown skin (#C08E6A) only inside the slit, oversized warm-black hoodie (#1F1E22) with the hood always up and a kangaroo pocket, cream drawstrings with gold tips, black jogger pants with cuffs, black sneakers with a thin gold stripe and dark gold soles. Left hand in the hoodie pocket. Thin warm gold rim light (#D4AF37) on the edge of the hood and the right side of the body. Deep warm-black background (#080706 to #2A2219) with a soft golden spotlight from above and a thin gold floor line. Quiet luxury, film noir mood, subtle knit texture, high detail.
```

### Auro solo
```
Dark cinematic illustration, a small floating spherical robot mascot called Auro: matte black sphere (#151417) with a thin gold ring around it slightly tilted like a planet (#D4AF37), a rounded black glass face screen with pale-gold pixel-art eyes (#F5DE9A), short antenna with a glowing gold tip, two soft golden thruster glows underneath, always floating above the ground, a small transparent gold holographic panel floating beside it. Deep warm-black background (#080706 to #2A2219), gold rim light, premium tech, high detail.
```

### Pertx + Auro juntos
```
Dark cinematic semi-realistic illustration, full body, of a faceless young entrepreneur called Pertx (matte black knitted balaclava with a single horizontal eye slit, dark brown eyes, warm-black oversized hoodie with hood up, cream drawstrings with gold tips, black joggers, black sneakers with gold stripe) standing on the left, and his small floating spherical robot companion Auro on the right (matte black sphere, tilted gold ring, black screen face with pale-gold pixel eyes, gold-tipped antenna, golden thruster glows). Deep warm-black background (#080706 to #2A2219), soft golden spotlight from above, thin gold rim light, quiet luxury, film noir mood, high detail.
```

### Prompt negativo (para todos)
```
visible face, mouth, nose, hair, smile, removed balaclava, hood down, sunglasses, cyan or blue or purple light, neon, bright colors, daylight, white background, cartoon, anime, chibi, kawaii, childish, humanoid robot, robot with arms or legs, weapons, cash, money bags, gold chains, jewelry, criminal scene, police, real brand logos, Apple logo, ChatGPT logo, Claude logo, text other than PX, extra fingers, deformed hands, multiple people, watermark, blurry
```

---

## 4. Poses y expresiones

Pertx solo puede expresar con **los ojos, las cejas y el cuerpo**. Auro expresa con **la pantalla (ojos de píxel) y el holograma**. Mira `png/FINAL-expresiones.png`.

| # | Expresión | Pertx | Auro | Cuándo usarla |
|---|---|---|---|---|
| 1 | **Feliz** | Ojos entrecerrados en media luna (sonríe con los ojos), móvil en la mano | Ojos `^ ^`, gráfica subiendo | Buenas noticias, resultados, final positivo |
| 2 | **Pensativo** | Mira hacia arriba a un lado, una ceja levantada, manos libres | Un ojo plano y otro levantado, `?` en el holograma | Preguntas, dudas, "¿merece la pena…?" |
| 3 | **Sorprendido** | Ojos muy abiertos, pupilas pequeñas, móvil en la mano | Ojos cuadrados `□ □`, boca `o`, `!` en el holograma | Gancho del principio, datos que impactan |
| 4 | **Señalando la pantalla** | Cejas bajas (decidido), brazo derecho estirado señalando | Ojos de flecha `> >`, flecha en el holograma | Tutoriales, "mira esto", enseñar Claude Code |
| 5 | **Celebrando** | Ojos felices, puño derecho levantado | Ojos `$ $`, gráfica subiendo, confeti dorado | Ventas, objetivos cumplidos, hitos |

### Prompts de pose (añádelos al final del prompt "Pertx + Auro juntos")
```
1 FELIZ: Pertx's eyes squinting into happy crescents as if smiling behind the mask, holding a glowing phone; Auro's screen shows happy "^ ^" pixel eyes and a rising gold chart hologram.
2 PENSATIVO: Pertx looking up to one side with one eyebrow raised, hands relaxed; Auro's screen shows one flat eye and one raised eye, a gold "?" hologram.
3 SORPRENDIDO: Pertx's eyes wide open with small pupils, holding a glowing phone; Auro's screen shows square hollow pixel eyes and a small "o" mouth, a gold "!" hologram.
4 SEÑALANDO LA PANTALLA: Pertx with determined lowered eyebrows, right arm fully extended pointing to the right side of the frame; Auro's screen shows arrow-shaped pixel eyes "> >", a gold arrow hologram pointing right.
5 CELEBRANDO: Pertx with happy squinting eyes, right fist raised high in celebration; Auro's screen shows "$ $" pixel eyes, rising gold chart hologram, small gold confetti squares around.
```

---

## 5. Voz recomendada

| | Pertx | Auro |
|---|---|---|
| **Quién la pone** | **Tu voz real** (recomendado) | Voz sintética (IA) |
| **Tono** | Grave, calmado, frases cortas, sin gritar. Como un narrador de documental | Neutra, clara y algo robótica, un poco más aguda que Pertx |
| **Ritmo** | Pausado en las frases clave, rápido en las explicaciones | Rápido y exacto, "ding" antes de dar un dato |
| **Muletillas** | "Mira." · "Esto es lo que nadie te cuenta." · "Vamos." | "Calculando…" · "Dato:" · "Venta detectada." |
| **Ejemplo** | "Hace 30 días no tenía nada. Hoy esto factura." | "Dato: 312 € este mes. Un 40 % más que el anterior." |

**Por qué tu voz para Pertx:** es gratis, no hace falta marcarla como IA y da más confianza. Una voz IA para el personaje principal suena "a cuenta genérica". Si no quieres que se te reconozca, se le puede bajar un poco el tono con un efecto gratuito (lo veremos en la etapa de edición).

**Auro con voz IA:** sí. Hay que marcar el vídeo como "contenido generado con IA" en cada plataforma. Qué herramienta usar lo decidimos en la Etapa 4, cuando me digas qué suscripciones tienes.

---

## 6. Reglas para que salgan SIEMPRE iguales

**Pertx**
1. **Nunca** se le ve la cara, la boca, la nariz ni el pelo. La capucha siempre puesta.
2. El pasamontañas tiene **una sola ranura** para los ojos (no dos agujeros, no boca).
3. Ropa siempre igual: sudadera negra, cordones crema con puntas doradas, jogger negro, zapatillas negras con raya dorada. **No cambia de ropa** (como un uniforme).
4. Lleva solo **un objeto** a la vez: nada, móvil o portátil.
5. El único logo que aparece es **"PX"** en dorado (tapa del portátil). Nunca logos de marcas reales.
6. Nada de dinero en efectivo, cadenas, armas ni nada que parezca un robo.

**Auro**
7. Siempre **flota**, nunca tiene brazos ni piernas.
8. Expresa solo con los **ojos de píxel dorados** y el holograma. No tiene boca de dibujo animado.
9. Siempre a la **derecha** de Pertx (o en la esquina inferior derecha en vídeos de pantalla), más pequeño que él.

**Ambiente**
10. Paleta solo negro cálido + oro. **Prohibido** el azul, el cian y el morado.
11. Luz dorada en el borde, fondo oscuro con foco suave desde arriba.
12. Encuadre vertical 9:16 para vídeo. Pertx a la izquierda o en el centro y Auro a la derecha.

**Producción**
13. Para generar algo nuevo, parte **siempre** de los archivos de esta carpeta (o súbelos como referencia). Nunca de un prompt "desde cero".
14. Todo vídeo con avatar o voz IA se marca como **generado con IA** en TikTok, Instagram y YouTube.

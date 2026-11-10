# Carpeta `personaje/`

Aquí está todo lo del personaje (y luego la mascota) de Pertx.

| Archivo | Qué es |
|---|---|
| `galeria.html` | **Ábrelo con doble clic.** Las 5 versiones (ronda 2: oscuras y con la cara tapada) una al lado de otra, con su código. |
| `FICHAS-PERSONAJE.md` | La ficha completa de cada versión: descripción, colores HEX, personalidad, prompt maestro y prompt negativo. |
| `svg/P1.svg` … `svg/P5.svg` | Los dibujos de cada versión, hechos en código. |
| `png/P1.png` … `png/P5.png` | Los mismos dibujos en imagen normal (PNG 1200x1600) para verlos o compartirlos. |
| `svg/P1-oro.svg`, `png/P1-oro.png` | **El personaje elegido:** P1 con los colores de P5. |
| `svg/P1-oro-cuerpo.svg`, `png/P1-oro-cuerpo.png` | Pertx de cuerpo completo, sin objeto. |
| `png/P1-oro-escenas.png` | Por defecto Pertx va sin nada en la mano; aquí se ven el móvil y el portátil, que solo se usan si la escena lo pide. |
| `galeria-mascota.html` | **Ábrelo con doble clic.** Las 5 mascotas (M1-M5), cada una junto a Pertx. |
| `FICHAS-MASCOTA.md` | La ficha completa de cada mascota: descripción, colores, personalidad, rol, prompts. |
| `svg/M1.svg` … `M5.svg`, `png/M1.png` … `M5.png` | Cada mascota junto a Pertx. |
| `pertx_cuerpo.py` | El dibujo de Pertx de cuerpo completo en código (lo usan los demás scripts). |
| `hacer-mascotas.py` | Vuelve a crear las mascotas y `galeria-mascota.html`: `python3 personaje/hacer-mascotas.py` |
| **`FICHA-FINAL.md`** | **La referencia de todo:** código `P1-oro+M3`, descripción fija, colores, prompts, poses, voz y reglas. |
| `png/FINAL-P1oro-M3.png` | Imagen principal: Pertx + Auro. |
| `png/FINAL-expresiones.png` | Las 5 poses y expresiones (feliz, pensativo, sorprendido, señalando, celebrando). |
| `auro.py` | El dibujo de Auro con sus caras, en código. |
| `hacer-ficha-final.py` | Vuelve a crear las imágenes de la ficha final: `python3 personaje/hacer-ficha-final.py` |
| `png/perfil.png` | Foto de perfil para TikTok, Instagram y YouTube (1080x1080). |
| `descartados/v1/` | La primera ronda (estilo infantil) que no te gustó. Guardada por si acaso. |
| `hacer-galeria.py` | Vuelve a crear `galeria.html` si cambias un SVG: `python3 personaje/hacer-galeria.py` |

**Código definitivo: `P1-oro+M3`** (Pertx + Auro). Todo lo demás se basa en `FICHA-FINAL.md`.

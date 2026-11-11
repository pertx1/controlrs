# Carpeta `guiones/` · fábrica de guiones

## Cómo sacar los guiones de una semana
En Claude Code, dentro de esta carpeta del proyecto, escribe:
```
/guiones-semana 2
```
Claude lee la dirección, la estrategia, la ficha del personaje y las referencias, prepara la semana a partir del calendario, escribe los 7 guiones, los revisa y te dice qué tienes que grabar o contarle.

## Qué hay aquí
| Archivo | Qué es |
|---|---|
| `semana-01/README.md` | **Empieza aquí:** resumen de la semana, con el estado de cada vídeo y lo que necesito de ti |
| `semana-01/dia-NN.md` | Ficha de cada vídeo: gancho, guion con tiempos, qué se ve, texto en pantalla, qué grabas, descripción y hashtags |
| `semana-01/dia-NN.json` | El mismo guion en formato para el motor de vídeo (Fase 3) |
| `ESQUEMA.md` | Explicación del formato `.json` |
| `fabrica.py` | `semana N` (prepara), `revisar N` (comprueba) y `fichas N` (crea las fichas) |

**Estados:** ✅ listo para producir · ⏳ faltan datos tuyos (los huecos entre `[corchetes]`) · ❌ tiene errores.

**Qué revisa la fábrica:** 3 ganchos, el gancho dura menos de 4,5 s, la imagen cambia cada 7 s como mucho, la voz no pasa de 3 palabras por segundo, la duración, los hashtags, la etiqueta de IA y **las líneas rojas** (nombre de tu marca de ropa, ciudad o región, edad exacta, política, religión, cripto…).

# Formato de un guion (`guiones/semana-XX/dia-NN.json`)

Cada vídeo es un archivo `.json`. La ficha para leer (`.md`) se genera sola con `python3 guiones/fabrica.py fichas N`. En la Fase 3, el motor de vídeo leerá este mismo `.json` para montar el vídeo.

```json
{
  "dia": 1,
  "dia_semana": "lunes",
  "serie": "DE 0 € A MI PRIMER EURO · Ep. 0",
  "formato": "Presentación",
  "pilar": "Emprender",
  "titulo": "Quién es Pertx",
  "duracion": 37,
  "ganchos": ["gancho 1", "gancho 2", "gancho 3"],
  "gancho_elegido": 0,
  "escenas": [
    {
      "t": [0, 4],
      "quien": "Pertx",
      "voz": "Lo que dice (la primera escena es el gancho elegido).",
      "visual": "Qué se ve en pantalla",
      "texto": ["PALABRA CLAVE"],
      "grabar": null,
      "pertx": {"ojos": "decidido", "objeto": null},
      "auro": null,
      "sonido": "whoosh"
    }
  ],
  "descripcion": "Texto de la publicación",
  "hashtags": ["#claudecode", "#emprender", "#pertx"],
  "cta": "Sígueme para ver el contador subir",
  "necesita_de_ti": ["Qué tiene que grabar o contar el usuario"],
  "etiqueta_ia": true,
  "estado": "borrador"
}
```

| Campo | Qué es |
|---|---|
| `t` | Segundo en que empieza y acaba la escena. Las escenas van seguidas, sin huecos. |
| `quien` | `Pertx` o `Auro` (quién habla). |
| `voz` | Lo que se dice. Máximo ~3 palabras por segundo de escena. |
| `visual` | Qué se ve: animación, mockup, grabación de pantalla… |
| `texto` | 1–2 palabras clave que salen grandes en oro (el resto de subtítulos salen solos de `voz`). |
| `grabar` | Normalmente `null`: las pantallas son animadas. Solo si hace falta, una captura de un proyecto real. |
| `pertx` | `ojos`: `normal`, `feliz`, `pensativo`, `sorprendido` o `decidido`. `objeto`: `null` (por defecto), `movil`, `portatil`, `senalar` o `celebrar`. `null` si Pertx no sale. |
| `auro` | `feliz`, `pensativo`, `sorprendido`, `senalando`, `celebrando` o `null`. |
| `sonido` | `whoosh`, `ding`, `pop`, `error` o `null`. |
| `[...]` | Un hueco con un dato real que falta. La revisión lo marca como ⏳ pendiente. |

**Reglas que comprueba `revisar`:** 3 ganchos; el gancho acaba antes de 4,5 s; escenas de 7 s como máximo; máximo 3 palabras por segundo; duración de 20 a 60 s; 3–6 hashtags; descripción; etiqueta de IA; y **las líneas rojas** de `DIRECCION.md` (marca de ropa por su nombre, ciudad o región, edad exacta, política, religión, cripto, "dinero rápido"…).

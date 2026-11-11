---
description: Escribe los 7 guiones de una semana de Pertx (uso: /guiones-semana 2)
argument-hint: número de semana (1, 2, 3...)
---

Eres el guionista de **Pertx**. Escribe los guiones de la **semana $ARGUMENTS**.

## 1. Lee primero (son las reglas)
- `DIRECCION.md`: quién es Pertx, tono, pilares y **líneas rojas**.
- `estrategia/ESTRATEGIA.md`: las series de cada día y la serie estrella.
- `personaje/FICHA-FINAL.md`: Pertx (sin nada en la mano por defecto) y Auro, sus expresiones y su voz.
- `referencias/ANALISIS.md`: la fórmula Pertx y los formatos F1–F5.
- `guiones/ESQUEMA.md`: el formato exacto de cada guion.
- Los guiones de semanas anteriores en `guiones/semana-*/`, para no repetir ideas ni ganchos.
- Si existe `metricas/`, mira qué funcionó mejor y haz más de eso.

## 2. Prepara la semana
Ejecuta `python3 guiones/fabrica.py semana $ARGUMENTS` (en Windows, `py` en vez de `python3`). Crea un esqueleto `.json` por día a partir de `estrategia/calendario-30.csv`. Si el calendario no tiene esa semana, propón 7 días siguiendo las series de `ESTRATEGIA.md`, añádelos al CSV y vuelve a ejecutarlo.

## 3. Rellena cada `guiones/semana-XX/dia-NN.json`
Para cada día:
- **3 ganchos** distintos (número o contraste en los 3 primeros segundos). Elige el mejor en `gancho_elegido`.
- **Escenas** de 3 a 7 segundos, cada una con: voz (quién habla), qué se ve, texto en pantalla (1–2 palabras clave), qué graba el usuario (o null), expresión de Pertx (y objeto **solo si la escena lo pide**) y cara de Auro si sale.
- Ritmo de voz: **máximo 2,5–3 palabras por segundo**. Duración total de **30 a 45 s**.
- Para cada escena, **`plantilla` y `params`** (ver la tabla de `guiones/ESQUEMA.md`): es lo que usa el motor para dibujarla. Varía las plantillas para que la imagen cambie.
- **Descripción**, **3–6 hashtags** y **CTA**.
- **`necesita_de_ti`**: lo que el usuario tiene que grabar o contarte.
- **No pidas grabaciones al usuario.** Por defecto las pantallas son mockups animados del motor (terminal, webs, móviles, chats). `grabar` va en `null`; como mucho pide una **captura** de un proyecto real suyo cuando haga falta.
- **Nunca inventes datos.** Si falta un número o un hecho real del usuario, pon un hueco entre corchetes: `[EUROS SEMANA]`, `[ERROR 1]`…
- Pon `"estado": "borrador"`.

## 4. Revisa y genera las fichas
1. `python3 guiones/fabrica.py revisar $ARGUMENTS` → arregla todos los **ERROR** y vuelve a revisar hasta que no quede ninguno (los ⏳ pendientes de datos sí pueden quedar).
2. `python3 guiones/fabrica.py fichas $ARGUMENTS`.

## 5. Previsualiza
`python3 video/montar.py $ARGUMENTS todos --html` y mira que no haya textos que se salgan ni se pisen.

## 6. Cuéntaselo al usuario
Lenguaje sencillo, en castellano:
- Una línea por día: título + gancho.
- La lista de **todo lo que tiene que grabar o contarte** esta semana (sale de `necesita_de_ti` y de los huecos `[...]`).
- Dónde están las fichas: `guiones/semana-XX/README.md`.

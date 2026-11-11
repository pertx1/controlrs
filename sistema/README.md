# Carpeta `sistema/` · tu día a día con Pertx

## Cada día (2 minutos)
```
npm run hoy
```
Te dice:
- **📤 Qué publicar hoy** (y si el vídeo está listo o qué comando falta), con la descripción y los hashtags para copiar.
- **🎬 Qué preparar** para los próximos 3 días.
- **✍️ Qué necesito de ti** esta semana (datos, números…).
- **✅ Tus tareas de hoy**: una fija de cada día de la semana + una pendiente del `PLAN.md`.

**La primera vez:** cuando sepas el primer día de publicación →
```
npm run hoy -- --empezar 2026-11-23
```
Para mirar otro día: `npm run hoy -- 2026-11-30`.

## Cada domingo (15 minutos)
1. `npm run metricas -- crear 1` → crea `metricas/semana-01-videos.csv` y `semana-01-negocio.csv`.
2. Rellénalos (Excel o Google Sheets) con las estadísticas de TikTok e Instagram de cada vídeo y los números del negocio.
3. En Claude Code: **`/metricas-semana 1`** → lo analizo, te digo qué ha funcionado, qué cambiar y ajusto la semana siguiente (y relleno los números del vídeo de Auro).

## La rutina de la semana (sale en `npm run hoy`)
| Día | Tarea fija |
|---|---|
| Lunes | Pasarme los datos de "NECESITO DE TI" |
| Martes | 15 min contestando comentarios |
| Miércoles | Buscar 3 negocios sin web en Google Maps |
| Jueves | 15 min viendo vídeos del nicho: apuntar ganchos |
| Viernes | `/guiones-semana` de la semana siguiente |
| Sábado | Montar los vídeos de la semana siguiente |
| Domingo | Métricas + `/metricas-semana` |

`config.json` guarda la fecha del día 1, la hora de publicar y las redes.

## Panel de descarga (lo que usas para publicar)
Cada semana te dejo un **panel** (página privada) con cada día: el vídeo, la historia, la descripción para copiar, la encuesta de la historia y una casilla de "publicado". Tú solo descargas y publicas.

Cómo lo genero yo:
```
npm run historias -- 1     # una historia 1080x1920 por día
npm run panel -- 1         # video/salida/semana-01/panel.html (+ la lista de archivos que lleva)
```

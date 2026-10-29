// Genera preguntas tipo test a partir del temario con Gemini.
// Variables de entorno:
//   GEMINI_API_KEY  clave de Google AI Studio (obligatoria salvo MOCK=1)
//   GEMINI_MODEL    modelo (por defecto gemini-2.5-flash)
//   LS_STORE_ID     id de tu tienda de Lemon Squeezy, para aceptar solo tus licencias
//   FREE_PER_DAY    tests gratis por IP y día (por defecto 5, el cliente muestra 3)
//   MOCK=1          devuelve preguntas falsas, para probar sin clave

const MAX_CHARS = 60000;
const MIN_CHARS = 300;
const DIFICULTADES = {
  facil: 'fácil: preguntas directas sobre ideas principales',
  media: 'media: como un examen oficial típico, con distractores plausibles',
  dificil: 'difícil: detalles finos (plazos, cifras, órganos competentes, excepciones) y distractores muy parecidos',
};

// Límite gratuito aproximado. La memoria vive por instancia, así que es orientativo;
// si hay abuso, cámbialo por Upstash/Vercel KV.
const usoPorIp = new Map();
const licenciasValidas = new Map();

const schema = {
  type: 'OBJECT',
  properties: {
    preguntas: {
      type: 'ARRAY',
      items: {
        type: 'OBJECT',
        properties: {
          pregunta: { type: 'STRING' },
          opciones: { type: 'ARRAY', items: { type: 'STRING' } },
          correcta: { type: 'INTEGER' },
          explicacion: { type: 'STRING' },
          cita: { type: 'STRING' },
        },
        required: ['pregunta', 'opciones', 'correcta', 'explicacion', 'cita'],
      },
    },
  },
  required: ['preguntas'],
};

function prompt(texto, n, dificultad) {
  return `Eres un preparador de oposiciones en España con 15 años de experiencia redactando exámenes oficiales.

Crea exactamente ${n} preguntas tipo test a partir EXCLUSIVAMENTE del temario que hay entre <temario> y </temario>.

Reglas:
- 4 opciones por pregunta y solo una correcta. "correcta" es el índice (0 a 3) de la opción correcta.
- Dificultad ${DIFICULTADES[dificultad]}.
- Los distractores deben ser plausibles: cambia plazos, cifras, órganos, artículos o matices del propio texto. Nada de opciones absurdas.
- No uses "todas las anteriores" ni "ninguna de las anteriores".
- No preguntes nada que no esté en el temario. No repitas preguntas.
- Reparte las preguntas por todo el temario, no solo por el principio.
- "explicacion": por qué la correcta lo es y por qué falla el distractor más tentador, en 1 o 2 frases.
- "cita": fragmento literal y breve del temario que justifica la respuesta.
- Escribe en español de España.

<temario>
${texto}
</temario>`;
}

function barajar(p) {
  const orden = [0, 1, 2, 3].sort(() => Math.random() - 0.5);
  return { ...p, opciones: orden.map((i) => p.opciones[i]), correcta: orden.indexOf(p.correcta) };
}

function limpiar(preguntas) {
  return preguntas
    .filter((p) => p && typeof p.pregunta === 'string' && Array.isArray(p.opciones) && p.opciones.length === 4
      && Number.isInteger(p.correcta) && p.correcta >= 0 && p.correcta < 4
      && new Set(p.opciones.map((o) => String(o).trim().toLowerCase())).size === 4)
    .map((p) => barajar({
      pregunta: p.pregunta.trim(),
      opciones: p.opciones.map((o) => String(o).trim()),
      correcta: p.correcta,
      explicacion: String(p.explicacion || '').trim(),
      cita: String(p.cita || '').trim(),
    }));
}

async function licenciaValida(clave) {
  if (!clave) return false;
  const cache = licenciasValidas.get(clave);
  if (cache && cache > Date.now()) return true;
  try {
    const r = await fetch('https://api.lemonsqueezy.com/v1/licenses/validate', {
      method: 'POST',
      headers: { Accept: 'application/json', 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({ license_key: clave }),
    });
    const d = await r.json();
    const tienda = process.env.LS_STORE_ID;
    const ok = d.valid === true && (!tienda || String(d.meta?.store_id) === String(tienda));
    if (ok) licenciasValidas.set(clave, Date.now() + 6 * 3600 * 1000);
    return ok;
  } catch {
    return false;
  }
}

function dentroDelLimite(ip) {
  const hoy = new Date().toISOString().slice(0, 10);
  const max = Number(process.env.FREE_PER_DAY || 5);
  const u = usoPorIp.get(ip);
  if (!u || u.dia !== hoy) {
    usoPorIp.set(ip, { dia: hoy, n: 1 });
    return true;
  }
  if (u.n >= max) return false;
  u.n++;
  return true;
}

function preguntasFalsas(n) {
  return Array.from({ length: n }, (_, i) => ({
    pregunta: `Pregunta de prueba ${i + 1}: ¿qué plazo establece el artículo ${i + 1}?`,
    opciones: ['Diez días hábiles', 'Quince días hábiles', 'Un mes', 'Tres meses'],
    correcta: i % 4,
    explicacion: 'Respuesta de ejemplo generada en modo MOCK.',
    cita: `Artículo ${i + 1}. Texto de ejemplo.`,
  }));
}

async function leerCuerpo(req) {
  if (req.body && typeof req.body === 'object') return req.body;
  if (typeof req.body === 'string') return JSON.parse(req.body);
  let raw = '';
  for await (const trozo of req) raw += trozo;
  return raw ? JSON.parse(raw) : {};
}

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Método no permitido' });

  let body;
  try {
    body = await leerCuerpo(req);
  } catch {
    return res.status(400).json({ error: 'Petición mal formada' });
  }

  const texto = String(body.texto || '').replace(/\s+/g, ' ').trim();
  const n = Math.min(Math.max(parseInt(body.n, 10) || 10, 5), 20);
  const dificultad = DIFICULTADES[body.dificultad] ? body.dificultad : 'media';

  if (texto.length < MIN_CHARS) return res.status(400).json({ error: 'El temario es demasiado corto. Pega al menos un par de párrafos.' });
  if (texto.length > MAX_CHARS) return res.status(400).json({ error: `Máximo ${MAX_CHARS.toLocaleString('es-ES')} caracteres por test. Elige menos páginas.` });

  const pro = await licenciaValida(req.headers['x-licencia']);
  const ip = String(req.headers['x-forwarded-for'] || req.socket?.remoteAddress || '').split(',')[0].trim();
  if (!pro && !dentroDelLimite(ip)) {
    return res.status(402).json({ error: 'Has gastado los tests gratis de hoy.', codigo: 'limite' });
  }

  if (process.env.MOCK === '1') return res.status(200).json({ preguntas: limpiar(preguntasFalsas(n)), pro });

  const clave = process.env.GEMINI_API_KEY;
  if (!clave) return res.status(500).json({ error: 'Falta configurar GEMINI_API_KEY en el servidor.' });
  const modelo = process.env.GEMINI_MODEL || 'gemini-2.5-flash';

  try {
    const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${modelo}:generateContent`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'x-goog-api-key': clave },
      body: JSON.stringify({
        contents: [{ role: 'user', parts: [{ text: prompt(texto, n, dificultad) }] }],
        generationConfig: { responseMimeType: 'application/json', responseSchema: schema, temperature: 0.7 },
      }),
    });
    if (r.status === 429) return res.status(503).json({ error: 'La IA está saturada ahora mismo. Prueba en un minuto.' });
    if (!r.ok) {
      console.error('Gemini', r.status, await r.text());
      return res.status(502).json({ error: 'No se pudo generar el test. Inténtalo de nuevo.' });
    }
    const d = await r.json();
    const salida = d.candidates?.[0]?.content?.parts?.map((p) => p.text || '').join('') || '{}';
    const preguntas = limpiar(JSON.parse(salida).preguntas || []);
    if (!preguntas.length) return res.status(502).json({ error: 'La IA no devolvió preguntas válidas. Inténtalo de nuevo.' });
    return res.status(200).json({ preguntas, pro });
  } catch (e) {
    console.error(e);
    return res.status(502).json({ error: 'No se pudo generar el test. Inténtalo de nuevo.' });
  }
}

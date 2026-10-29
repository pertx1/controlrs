// Servidor local: sirve la web y la función /api/generate como lo haría Vercel.
// Uso: GEMINI_API_KEY=... node dev-server.mjs   (o MOCK=1 node dev-server.mjs)
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';
import handler from './api/generate.js';

const raiz = fileURLToPath(new URL('.', import.meta.url));
const tipos = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.css': 'text/css' };
const puerto = Number(process.env.PORT || 3000);

createServer(async (req, res) => {
  const url = new URL(req.url, 'http://localhost');
  if (url.pathname === '/api/generate') {
    res.status = (c) => { res.statusCode = c; return res; };
    res.json = (o) => { res.setHeader('Content-Type', 'application/json'); res.end(JSON.stringify(o)); };
    return handler(req, res);
  }
  const ruta = normalize(join(raiz, url.pathname === '/' ? 'index.html' : url.pathname));
  if (!ruta.startsWith(raiz) || ruta.includes('/api/')) { res.statusCode = 404; return res.end(); }
  try {
    const datos = await readFile(ruta);
    res.setHeader('Content-Type', tipos[extname(ruta)] || 'application/octet-stream');
    res.end(datos);
  } catch {
    res.statusCode = 404;
    res.end('No encontrado');
  }
}).listen(puerto, () => console.log(`TemaTest en http://localhost:${puerto}`));

# TemaTest

Convierte el temario de oposiciones (PDF o texto) en tests tipo examen: 4 opciones, penalización, explicación con la cita del tema y repaso de falladas.

- `index.html`: toda la web. El PDF se lee en el navegador con pdf.js; el progreso y las falladas se guardan en `localStorage`.
- `api/generate.js`: función serverless que llama a Gemini con la clave guardada en el servidor y valida licencias de Lemon Squeezy.
- `dev-server.mjs`: servidor local que imita a Vercel.

Modelo de negocio: 3 tests gratis al día y licencia de pago único (9,99 €) para tests ilimitados. El repaso de falladas no gasta tests ni llamadas a la IA.

## Probar en local

```bash
MOCK=1 node dev-server.mjs
```

Abre http://localhost:3000. Con `MOCK=1` devuelve preguntas de ejemplo sin gastar IA. Para preguntas reales:

```bash
GEMINI_API_KEY=tu_clave node dev-server.mjs
```

## Puesta en marcha (todo gratis)

### 1. Clave de la IA (5 min)
1. Entra en https://aistudio.google.com con tu cuenta de Google.
2. **Get API key → Create API key**. No pide tarjeta.
3. En el panel de AI Studio mira los límites gratuitos del modelo `gemini-2.5-flash`. Cambian a menudo; si ese modelo deja de ser gratis, pon otro en `GEMINI_MODEL`.

### 2. Cobros con Lemon Squeezy (15 min + revisión de la tienda)
1. Crea cuenta en https://lemonsqueezy.com y una tienda. Hacen de vendedor oficial, así que gestionan el IVA europeo por ti. Tienen que aprobar la tienda antes de poder cobrar: pide la activación el primer día.
2. **Products → New product**: "TemaTest ilimitado", 9,99 €, pago único.
3. En el producto activa **Generate license keys**, con duración ilimitada.
4. Copia el enlace de compra (**Share**) y pégalo en `CONFIG.checkoutUrl` de `index.html`.
5. Copia el id de la tienda (**Settings → Stores**) para `LS_STORE_ID`. Así solo se aceptan licencias de tu tienda.

Tras pagar, el cliente recibe su clave por email y la pega en **Tengo licencia**.

### 3. Publicar en Vercel (10 min)
1. Entra en https://vercel.com con tu cuenta de GitHub (plan Hobby, gratis).
2. **Add New → Project** e importa este repositorio.
3. **Root Directory**: `tematest`. Framework: **Other**. Sin comando de build.
4. **Environment Variables**:
   - `GEMINI_API_KEY`: tu clave
   - `LS_STORE_ID`: el id de tu tienda
   - opcional: `GEMINI_MODEL`, `FREE_PER_DAY`
5. **Deploy**. Tendrás la web en `https://<nombre>.vercel.app`.

## Límites conocidos
- El límite gratuito se controla en el navegador y, de forma orientativa, por IP en el servidor (memoria por instancia). Si alguien abusa, sustitúyelo por Upstash o Vercel KV (ambos con capa gratis).
- Los PDF escaneados no tienen texto: hay que pasarlos por OCR.
- Máximo 60.000 caracteres por test (unas 25 páginas).

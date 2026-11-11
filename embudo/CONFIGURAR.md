# Poner en marcha el embudo (web + emails + venta)

**Quién:** tu padre o tu madre (son los titulares), contigo al lado. **Tiempo:** ~1 hora la primera vez.
Todo es **gratis** salvo lo que ya pagáis (Vercel). Las claves **nunca** se pegan en el chat ni se suben a git: van en Vercel (y en `web/.env.local` si pruebas en tu portátil).

---

## 1. MailerLite (emails) · 20 min
1. Crea la cuenta en **mailerlite.com** con el Gmail de la marca (plan gratis, hasta 1.000 suscriptores).
2. **Remitente:** MailerLite te pedirá verificar el email desde el que envías.
   - ⚠️ **Puede que no deje enviar desde un Gmail** (lo hacen para que los emails no acaben en spam) y pida un **dominio propio**. Si pasa, dímelo: la única solución fiable es comprar un dominio (~10 €/año, por ejemplo `pertx.es`). Es el único gasto que puede aparecer en todo el embudo.
3. **Subscribers → Groups → Create group**, tres grupos:
   - `regalo` · `guia` · `creadores`

   Abre cada grupo: el número que sale en la dirección del navegador es su **ID**. Apúntalos.
4. **Integrations → API → Generate new token** → cópialo (es la `MAILERLITE_API_KEY`).
5. **Automations → Create workflow** → disparador **"When subscriber joins a group" → `regalo`** → añade los **5 emails** de `embudo/EMAILS.md` con sus esperas (0, 1, 3, 5 y 7 días).
6. *(Recomendado)* Activa el **double opt-in** (confirmación por email): evita emails falsos.

## 2. Resend (avisos del formulario de servicios) · 5 min
1. Crea la cuenta en **resend.com** con el **Gmail de la marca**.
2. **API Keys → Create API Key** → cópiala (`RESEND_API_KEY`).
3. `CONTACTO_EMAIL` = **ese mismo Gmail**. *(Sin dominio propio, Resend solo puede enviar al email de la cuenta, que es justo lo que queremos: los avisos te llegan a ti).*

## 3. Vercel (la web) · 15 min
1. Entra en la cuenta de Vercel de tus padres → **Add New → Project → Import** el repositorio `pertx1/controlrs`.
2. **Root Directory:** `web` · **Project Name:** `pertx` (así la dirección será `pertx.vercel.app`, si está libre).
3. **Environment Variables** (las de `web/.env.example`):

| Variable | Valor |
|---|---|
| `MAILERLITE_API_KEY` | El token de MailerLite |
| `ML_GRUPO_REGALO`, `ML_GRUPO_GUIA`, `ML_GRUPO_CREADORES` | Los IDs de los grupos |
| `RESEND_API_KEY` | La clave de Resend |
| `CONTACTO_EMAIL` | El Gmail de la marca |
| `NEXT_PUBLIC_TITULAR_NOMBRE` | Nombre y apellidos de tu padre o tu madre |
| `NEXT_PUBLIC_TITULAR_NIF` | Su NIF (sale en el aviso legal: es obligatorio por ley) |
| `NEXT_PUBLIC_TITULAR_EMAIL` | El Gmail de la marca |
| `NEXT_PUBLIC_GUMROAD_URL` | Vacío hasta que la guía esté a la venta |

4. **Deploy.** Si la dirección no es `pertx.vercel.app`, dímela y la cambio en `web/lib/config.js` y en los emails.

> Si queréis, **la despliego yo** desde aquí en vuestra cuenta de Vercel; solo tenéis que poner las claves en Vercel después.

## 4. Gumroad (venta de la guía) · cuando la guía esté lista
1. Cuenta en **gumroad.com** a nombre de tu padre o tu madre (los cobros van a su banco).
2. **New product → Digital product** → "De 0 a 5.000 €: cómo lancé mi marca de ropa" → 19 € → sube el PDF.
3. Copia el enlace del producto en `NEXT_PUBLIC_GUMROAD_URL` (Vercel) → **Redeploy**. La página `/guia` cambia sola de "apúntate" a "comprar".
4. Gumroad hace de vendedor ante Hacienda en la UE (cobra y declara el IVA). Aun así, **preguntad a la gestoría** cómo declarar lo que os paga.

## 5. Probar (5 min)
- [ ] Apúntate tú en `/regalo` → te llega el email 1 con la calculadora.
- [ ] Rellena el formulario de `/servicios` → te llega el aviso al Gmail.
- [ ] `/aviso-legal` y `/privacidad` muestran los datos de verdad (no `[NOMBRE DEL TITULAR]`).
- [ ] Pon `https://pertx.vercel.app` en la bio de Instagram (y en TikTok cuando lo desbloquees).

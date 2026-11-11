# Carpeta `web/` · la web de Pertx (link-in-bio + embudo)

Next.js en Vercel. Negro y oro, pensada para el móvil.

| Página | Qué es |
|---|---|
| `/` | Link-in-bio: avatar, tus números y 4 botones |
| `/regalo` | Regalo gratis (calculadora de márgenes + checklist) a cambio del email → MailerLite grupo `regalo` |
| `/regalo/calculadora`, `/regalo/checklist` | El regalo (se mandan por email; no salen en Google) |
| `/guia` | La guía de 19 €: lista de espera (grupo `guia`) o botón de compra en Gumroad cuando exista |
| `/servicios` | Pertx Studio: precios y formulario → aviso al Gmail de la marca (Resend) |
| `/creadores` | Lista de espera de tu web para creadores (grupo `creadores`) |
| `/aviso-legal`, `/privacidad` | Obligatorias por ley (LSSI y RGPD) |

**Configurar y publicar:** `embudo/CONFIGURAR.md`. **Emails de bienvenida:** `embudo/EMAILS.md`.

## Probar en tu portátil
```
cd web
npm install
copy .env.example .env.local      (en Mac/Linux: cp .env.example .env.local) y rellénalo
npm run dev                        → abre http://localhost:3000
```
Sin claves la web funciona igual, pero los formularios dicen "todavía no está activado".

Para cambiar textos, precios o enlaces: `lib/config.js`.

import { NextResponse } from "next/server";

const limpia = (t, n) => String(t || "").replace(/[<>]/g, "").slice(0, n);

// Un negocio pide una web → aviso por email al Gmail de la marca (Resend).
export async function POST(req) {
  let d;
  try {
    d = await req.json();
  } catch {
    return NextResponse.json({ error: "Datos no válidos" }, { status: 400 });
  }
  if (d.web) return NextResponse.json({ ok: true }); // trampa para bots
  if (!d.acepto) return NextResponse.json({ error: "Tienes que aceptar la política de privacidad" }, { status: 400 });
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(d.email || "") || !d.negocio) {
    return NextResponse.json({ error: "Falta el nombre del negocio o el email no es válido" }, { status: 400 });
  }
  const key = process.env.RESEND_API_KEY;
  const para = process.env.CONTACTO_EMAIL;
  if (!key || !para) {
    return NextResponse.json({ error: "El formulario todavía no está activado. Escríbenos por Instagram." }, { status: 503 });
  }
  const texto = [
    `Negocio: ${limpia(d.negocio, 80)}`,
    `Email: ${limpia(d.email, 120)}`,
    `Servicio: ${limpia(d.servicio, 60)}`,
    "",
    limpia(d.mensaje, 1500),
  ].join("\n");
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      from: "Web de Pertx <onboarding@resend.dev>",
      to: [para],
      reply_to: limpia(d.email, 120),
      subject: `Nuevo cliente: ${limpia(d.negocio, 60)} (${limpia(d.servicio, 40)})`,
      text: texto,
    }),
  });
  if (!r.ok) return NextResponse.json({ error: "No se ha podido enviar. Inténtalo otra vez." }, { status: 502 });
  return NextResponse.json({ ok: true });
}

import { NextResponse } from "next/server";

const GRUPOS = {
  regalo: process.env.ML_GRUPO_REGALO,
  guia: process.env.ML_GRUPO_GUIA,
  creadores: process.env.ML_GRUPO_CREADORES,
};

// Añade un email a MailerLite en el grupo que toque. MailerLite manda luego los emails automáticos.
export async function POST(req) {
  let datos;
  try {
    datos = await req.json();
  } catch {
    return NextResponse.json({ error: "Datos no válidos" }, { status: 400 });
  }
  const { email = "", nombre = "", grupo = "", acepto, web } = datos;
  if (web) return NextResponse.json({ ok: true }); // trampa para bots
  if (!acepto) return NextResponse.json({ error: "Tienes que aceptar la política de privacidad" }, { status: 400 });
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) || email.length > 120) {
    return NextResponse.json({ error: "Ese email no parece válido" }, { status: 400 });
  }
  const key = process.env.MAILERLITE_API_KEY;
  const idGrupo = GRUPOS[grupo];
  if (!key || !idGrupo) {
    return NextResponse.json({ error: "La lista todavía no está activada. Vuelve en unos días." }, { status: 503 });
  }
  const r = await fetch("https://connect.mailerlite.com/api/subscribers", {
    method: "POST",
    headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json", Accept: "application/json" },
    body: JSON.stringify({ email, fields: { name: String(nombre).slice(0, 60) }, groups: [idGrupo] }),
  });
  if (!r.ok) {
    return NextResponse.json({ error: "No se ha podido apuntar. Inténtalo otra vez." }, { status: 502 });
  }
  return NextResponse.json({ ok: true });
}

"use client";
import { useState } from "react";
import Link from "next/link";

// Formulario de email → /api/suscribir → MailerLite (grupo: regalo | guia | creadores)
export default function FormEmail({ grupo, boton = "Quiero el regalo", ok = "¡Hecho! Revisa tu email (y la carpeta de spam)." }) {
  const [estado, setEstado] = useState("listo");
  const [mensaje, setMensaje] = useState("");

  async function enviar(ev) {
    ev.preventDefault();
    const datos = Object.fromEntries(new FormData(ev.currentTarget));
    setEstado("enviando");
    try {
      const r = await fetch("/api/suscribir", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ ...datos, grupo }) });
      const j = await r.json();
      if (!r.ok) throw new Error(j.error || "Algo ha fallado");
      setEstado("ok");
      setMensaje(ok);
    } catch (e) {
      setEstado("error");
      setMensaje(e.message);
    }
  }

  if (estado === "ok") return <p className="ok" role="status">{mensaje}</p>;

  return (
    <form onSubmit={enviar}>
      <label htmlFor={`nombre-${grupo}`}>Tu nombre</label>
      <input id={`nombre-${grupo}`} name="nombre" autoComplete="given-name" maxLength={60} />
      <label htmlFor={`email-${grupo}`}>Tu email</label>
      <input id={`email-${grupo}`} name="email" type="email" required autoComplete="email" maxLength={120} />
      <div className="trampa" aria-hidden="true">
        <label>No rellenes esto <input name="web" tabIndex={-1} autoComplete="off" /></label>
      </div>
      <label className="consentimiento">
        <input type="checkbox" name="acepto" required />
        <span>
          Acepto recibir emails de Pertx y la <Link href="/privacidad">política de privacidad</Link>. Puedes darte de baja cuando quieras.
        </span>
      </label>
      <button type="submit" disabled={estado === "enviando"}>{estado === "enviando" ? "Enviando…" : boton}</button>
      {estado === "error" && <p className="error" role="alert">{mensaje}</p>}
    </form>
  );
}

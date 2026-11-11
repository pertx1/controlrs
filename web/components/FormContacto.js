"use client";
import { useState } from "react";
import Link from "next/link";
import { SERVICIOS } from "../lib/config";

// Formulario para negocios → /api/contacto → aviso por email al Gmail de la marca (Resend)
export default function FormContacto() {
  const [estado, setEstado] = useState("listo");
  const [mensaje, setMensaje] = useState("");

  async function enviar(ev) {
    ev.preventDefault();
    const datos = Object.fromEntries(new FormData(ev.currentTarget));
    setEstado("enviando");
    try {
      const r = await fetch("/api/contacto", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(datos) });
      const j = await r.json();
      if (!r.ok) throw new Error(j.error || "Algo ha fallado");
      setEstado("ok");
      setMensaje("¡Recibido! Te respondemos por email en 24–48 h.");
    } catch (e) {
      setEstado("error");
      setMensaje(e.message);
    }
  }

  if (estado === "ok") return <p className="ok" role="status">{mensaje}</p>;

  return (
    <form onSubmit={enviar}>
      <label htmlFor="negocio">Nombre del negocio</label>
      <input id="negocio" name="negocio" required maxLength={80} />
      <label htmlFor="email">Email de contacto</label>
      <input id="email" name="email" type="email" required autoComplete="email" maxLength={120} />
      <label htmlFor="servicio">¿Qué necesitas?</label>
      <select id="servicio" name="servicio" defaultValue={SERVICIOS[0].nombre}>
        {SERVICIOS.map((s) => <option key={s.nombre}>{s.nombre}</option>)}
        <option>No lo sé, aconséjame</option>
      </select>
      <label htmlFor="mensaje">Cuéntame un poco (qué hace tu negocio, si ya tienes web…)</label>
      <textarea id="mensaje" name="mensaje" rows={4} maxLength={1500} />
      <div className="trampa" aria-hidden="true">
        <label>No rellenes esto <input name="web" tabIndex={-1} autoComplete="off" /></label>
      </div>
      <label className="consentimiento">
        <input type="checkbox" name="acepto" required />
        <span>Acepto la <Link href="/privacidad">política de privacidad</Link> para que me contestéis.</span>
      </label>
      <button type="submit" disabled={estado === "enviando"}>{estado === "enviando" ? "Enviando…" : "Quiero mi web"}</button>
      {estado === "error" && <p className="error" role="alert">{mensaje}</p>}
    </form>
  );
}

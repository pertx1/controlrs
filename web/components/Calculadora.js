"use client";
import { useState } from "react";

const euros = (n) => (isFinite(n) ? n.toLocaleString("es-ES", { style: "currency", currency: "EUR" }) : "—");

// Calculadora de márgenes para una prenda (el regalo del embudo)
export default function Calculadora() {
  const [v, setV] = useState({ prenda: 6, estampado: 3, envio: 4.5, packaging: 0.8, comision: 3, precio: 25, margen: 55 });
  const cambia = (k) => (e) => setV({ ...v, [k]: parseFloat(e.target.value.replace(",", ".")) || 0 });

  const coste = v.prenda + v.estampado + v.envio + v.packaging;
  const comision = (v.precio * v.comision) / 100;
  const beneficio = v.precio - coste - comision;
  const margen = v.precio > 0 ? (beneficio / v.precio) * 100 : 0;
  const precioIdeal = coste / (1 - v.margen / 100 - v.comision / 100);

  const campo = (k, texto) => (
    <label key={k}>
      {texto}
      <input inputMode="decimal" value={v[k]} onChange={cambia(k)} />
    </label>
  );

  return (
    <div className="panel">
      <form onSubmit={(e) => e.preventDefault()}>
        {campo("prenda", "Coste de la prenda lisa (€)")}
        {campo("estampado", "Estampado: DTF, vinilo o imprenta (€)")}
        {campo("envio", "Envío que pagas tú (€)")}
        {campo("packaging", "Bolsa, etiqueta, pegatina (€)")}
        {campo("comision", "Comisión de la tienda y del pago (%)")}
        {campo("precio", "Precio de venta (€)")}
      </form>
      <table className="tabla">
        <tbody>
          <tr><td>Coste total por prenda</td><td>{euros(coste)}</td></tr>
          <tr><td>Comisiones</td><td>{euros(comision)}</td></tr>
          <tr><td>Te queda por prenda</td><td>{euros(beneficio)}</td></tr>
          <tr><td>Margen</td><td>{isFinite(margen) ? margen.toFixed(0) : "—"} %</td></tr>
        </tbody>
      </table>
      <h2>¿Qué precio necesito?</h2>
      <form onSubmit={(e) => e.preventDefault()}>
        {campo("margen", "Margen que quiero (%)")}
      </form>
      <p>
        Para un margen del {v.margen} %, vende a <b className="oro">{precioIdeal > 0 ? euros(Math.ceil(precioIdeal)) : "—"}</b>.
      </p>
      <p className="aviso">Mi marca tenía un margen del 50–60 %. Los valores de ejemplo son orientativos: cambia cada uno por los tuyos.</p>
    </div>
  );
}

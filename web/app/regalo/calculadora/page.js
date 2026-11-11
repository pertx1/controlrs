import Calculadora from "../../../components/Calculadora";

export const metadata = { title: "Calculadora de márgenes", robots: { index: false } };

export default function PaginaCalculadora() {
  return (
    <main className="contenedor">
      <p className="kicker">Tu regalo</p>
      <h1>Calculadora de <span className="oro">márgenes</span></h1>
      <p className="sub">Cambia los números por los tuyos. Todo se calcula en tu navegador: no se guarda nada.</p>
      <Calculadora />
      <p className="aviso" style={{ marginTop: 16 }}>Siguiente paso: <a href="/regalo/checklist">el checklist para lanzar tu marca</a>.</p>
    </main>
  );
}

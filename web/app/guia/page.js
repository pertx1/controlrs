import Link from "next/link";
import FormEmail from "../../components/FormEmail";
import { GUMROAD_URL } from "../../lib/config";

export const metadata = { title: "De 0 a 5.000 €: cómo lancé mi marca de ropa", description: "Mi experiencia lanzando una marca de ropa con 30 €, paso a paso y con los números reales." };

const CAPITULOS = [
  "La idea y a quién le vendía",
  "Camisetas, sudaderas y camisetas de fútbol: qué se vendía más",
  "Diseños sin saber diseñar (y cómo me ayudó la IA)",
  "De 30 € en una imprenta a mi plancha de DTF",
  "Bajo demanda y luego stock: cuándo dar el salto",
  "Precios y márgenes del 50–60 % (con calculadora)",
  "La tienda online en Shopify",
  "Más de 4.000 seguidores sin pagar anuncios",
  "Los números, sin filtros",
  "Mis errores y lo que me costaron",
  "Lo legal, sin rollo",
  "Tu plan de 30 días",
];

export default function Guia() {
  return (
    <main className="contenedor">
      <Link className="volver" href="/">← Volver</Link>
      <p className="kicker">Guía · 19 €</p>
      <h1>De 0 a 5.000 €: cómo lancé mi <span className="oro">marca de ropa</span></h1>
      <p className="sub">Empecé con 30 € en una imprenta de mi barrio. La primera semana saqué 200 € de beneficio y me compré una plancha. En 3 meses facturé 5.000 € sin pagar anuncios. Aquí está todo, con mis números reales.</p>
      <div className="panel">
        <h2 style={{ marginTop: 0 }}>Lo que hay dentro</h2>
        <ol className="lista">{CAPITULOS.map((c) => <li key={c}>{c}</li>)}</ol>
        <p className="aviso">Incluye: calculadora de márgenes, checklist de lanzamiento y calendario de contenido de 30 días.</p>
        <p className="aviso">Es mi experiencia de 3 meses, no un método mágico. Facturar no es ganar: te enseño las dos cifras.</p>
      </div>
      <div className="panel">
        {GUMROAD_URL ? (
          <a className="boton destacado" href={GUMROAD_URL} rel="noopener">
            <span className="icono" aria-hidden="true">👕</span>
            <span><b>Comprar la guía · 19 €</b><small>Pago seguro con Gumroad. La recibes al momento.</small></span>
          </a>
        ) : (
          <>
            <h2 style={{ marginTop: 0 }}>Todavía no está a la venta</h2>
            <p className="sub" style={{ margin: 0 }}>Apúntate y te aviso el día que salga, con un precio especial para la lista.</p>
            <FormEmail grupo="guia" boton="Avísame cuando salga" ok="¡Apuntado! Te aviso el día del lanzamiento." />
          </>
        )}
      </div>
    </main>
  );
}

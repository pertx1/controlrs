import Link from "next/link";
import FormContacto from "../../components/FormContacto";
import { SERVICIOS } from "../../lib/config";

export const metadata = { title: "Webs y tiendas online para negocios", description: "Te hago la web o la tienda online de tu negocio. Precios de lanzamiento." };

export default function Servicios() {
  return (
    <main className="contenedor">
      <Link className="volver" href="/">← Volver</Link>
      <p className="kicker">Pertx Studio</p>
      <h1>¿Tu negocio no tiene web? <span className="oro">Te la hago.</span></h1>
      <p className="sub">Webs y tiendas online rápidas, que se ven bien en el móvil y que tus clientes entienden en 5 segundos. Monté la tienda de mi propia marca de ropa: sé lo que hace falta para vender.</p>
      <h2>Precios de lanzamiento</h2>
      <p className="aviso">Solo para los 3 primeros clientes, a cambio de tu opinión y de poder enseñar el trabajo.</p>
      <div className="precios">
        {SERVICIOS.map((s) => (
          <article className="precio" key={s.nombre}>
            <header>
              <b>{s.nombre}</b>
              <span><span className="cifra">{s.precio} €</span><span className="antes">{s.antes} €</span></span>
            </header>
            <p>{s.texto} <i>Plazo: {s.plazo}.</i></p>
          </article>
        ))}
      </div>
      <h2>Pídela aquí</h2>
      <div className="panel"><FormContacto /></div>
    </main>
  );
}

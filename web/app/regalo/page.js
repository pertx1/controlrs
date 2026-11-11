import Link from "next/link";
import FormEmail from "../../components/FormEmail";

export const metadata = { title: "Regalo: calculadora de márgenes", description: "La calculadora de márgenes que usé en mi marca de ropa, gratis." };

export default function Regalo() {
  return (
    <main className="contenedor">
      <Link className="volver" href="/">← Volver</Link>
      <p className="kicker">Gratis</p>
      <h1>La calculadora de márgenes de mi <span className="oro">marca de ropa</span></h1>
      <p className="sub">Con ella fijé precios para tener un 50–60 % de margen. Te la mando por email junto con un checklist para lanzar tu marca.</p>
      <div className="panel">
        <ul className="lista">
          <li>Calcula lo que te queda de verdad por cada camiseta o sudadera.</li>
          <li>Te dice a qué precio vender para el margen que quieras.</li>
          <li>Checklist con los pasos que seguí, desde 30 € en una imprenta.</li>
        </ul>
        <FormEmail grupo="regalo" boton="Mándamelo gratis" ok="¡Hecho! Te lo acabo de mandar. Revisa tu email (y la carpeta de spam)." />
      </div>
    </main>
  );
}

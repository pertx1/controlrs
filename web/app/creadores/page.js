import Link from "next/link";
import FormEmail from "../../components/FormEmail";

export const metadata = { title: "Mi web para creadores · lista de espera", description: "Lleva todas tus redes sociales desde un solo sitio. Apúntate a la lista de espera." };

export default function Creadores() {
  return (
    <main className="contenedor">
      <Link className="volver" href="/">← Volver</Link>
      <p className="kicker">En construcción</p>
      <h1>Todas tus redes, <span className="oro">desde un solo sitio</span></h1>
      <p className="sub">Llevaba las redes de mi marca de ropa a mano y perdía horas. Así que estoy construyendo una web para programar, publicar y ver los números de todas tus redes juntas. La construyo en público en mis vídeos.</p>
      <div className="panel">
        <ul className="lista">
          <li>Calendario con todas tus publicaciones.</li>
          <li>Programar en TikTok, Instagram y más desde un sitio.</li>
          <li>Tus números de todas las redes juntos.</li>
        </ul>
        <FormEmail grupo="creadores" boton="Apúntame a la lista de espera" ok="¡Dentro! Serás de los primeros en probarla." />
      </div>
    </main>
  );
}

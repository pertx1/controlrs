import Link from "next/link";
import { SITIO, TITULAR } from "../../lib/config";

export const metadata = { title: "Aviso legal", robots: { index: false } };

export default function AvisoLegal() {
  return (
    <main className="contenedor ancho">
      <Link className="volver" href="/">← Volver</Link>
      <h1>Aviso legal</h1>
      <p>En cumplimiento de la Ley 34/2002 de Servicios de la Sociedad de la Información (LSSI), estos son los datos del titular de {SITIO.url}:</p>
      <ul className="lista">
        <li><b>Titular:</b> {TITULAR.nombre}</li>
        <li><b>NIF:</b> {TITULAR.nif}</li>
        <li><b>Email de contacto:</b> {TITULAR.email}</li>
      </ul>
      <h2>Qué es esta web</h2>
      <p>La web de la marca Pertx: contenido sobre emprendimiento, un regalo gratuito, una guía de pago, servicios de creación de webs y una lista de espera. Pertx es un personaje con avatar y voz generados con inteligencia artificial.</p>
      <h2>Responsabilidad</h2>
      <p>La información de esta web y de los vídeos de Pertx es experiencia personal y tiene fines informativos. Los resultados y números compartidos son reales, pero no garantizan que tú vayas a obtener los mismos. Nada de lo publicado es asesoramiento financiero, fiscal ni legal: consulta a un profesional antes de tomar decisiones.</p>
      <h2>Propiedad intelectual</h2>
      <p>Los textos, el personaje Pertx, la mascota Auro, los diseños y el código de esta web pertenecen a su titular. No se pueden copiar ni usar con fines comerciales sin permiso.</p>
      <h2>Compras</h2>
      <p>Los productos digitales se venden a través de Gumroad, que gestiona el pago, la factura y los impuestos. Al tratarse de contenido digital que se entrega al momento, al comprar aceptas que empiece la entrega y pierdes el derecho de desistimiento (art. 103.m del Real Decreto Legislativo 1/2007). Si tienes cualquier problema, escríbenos a {TITULAR.email}.</p>
    </main>
  );
}

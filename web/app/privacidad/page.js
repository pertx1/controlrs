import Link from "next/link";
import { TITULAR } from "../../lib/config";

export const metadata = { title: "Política de privacidad", robots: { index: false } };

export default function Privacidad() {
  return (
    <main className="contenedor ancho">
      <Link className="volver" href="/">← Volver</Link>
      <h1>Política de privacidad</h1>
      <p>Te explicamos qué datos recogemos, para qué y qué derechos tienes, según el Reglamento General de Protección de Datos (RGPD) y la Ley Orgánica 3/2018 (LOPDGDD).</p>
      <h2>Responsable</h2>
      <p>{TITULAR.nombre} · NIF {TITULAR.nif} · {TITULAR.email}</p>
      <h2>Qué datos recogemos y para qué</h2>
      <ul className="lista">
        <li><b>Regalo, aviso de lanzamiento y lista de espera:</b> tu nombre (opcional) y tu email, para mandarte lo que pides y emails sobre Pertx. Base legal: tu consentimiento.</li>
        <li><b>Formulario de servicios:</b> nombre del negocio, email y tu mensaje, para responderte y preparar un presupuesto. Base legal: tu solicitud (medidas precontractuales).</li>
      </ul>
      <p>No usamos cookies de publicidad ni de seguimiento.</p>
      <h2>Con quién se comparten</h2>
      <p>Solo con los proveedores que necesitamos para funcionar, que actúan como encargados del tratamiento: <b>MailerLite</b> (envío de emails), <b>Resend</b> (avisos del formulario), <b>Vercel</b> (alojamiento de la web) y <b>Gumroad</b> (venta de productos). Algunos pueden tratar datos fuera de la UE con las garantías del RGPD (cláusulas contractuales tipo). No vendemos tus datos a nadie.</p>
      <h2>Cuánto tiempo</h2>
      <p>Hasta que te des de baja (hay un enlace en cada email) o nos pidas que los borremos. Los datos de presupuestos, el tiempo necesario para atenderte y lo que obligue la ley.</p>
      <h2>Tus derechos</h2>
      <p>Puedes pedir acceder, corregir, borrar, oponerte, limitar o llevarte tus datos escribiendo a {TITULAR.email}. Si no te atendemos bien, puedes reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>
      <h2>Menores</h2>
      <p>Si tienes menos de 14 años, necesitas el permiso de tu padre, madre o tutor para apuntarte.</p>
    </main>
  );
}

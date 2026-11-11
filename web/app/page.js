import Link from "next/link";
import { DATOS, SITIO } from "../lib/config";

const ENLACES = [
  { href: "/regalo", icono: "🎁", titulo: "Regalo: calculadora de márgenes", texto: "La que uso para mi marca de ropa. Gratis.", destacado: true },
  { href: "/guia", icono: "👕", titulo: "Cómo lancé mi marca de ropa", texto: "De 30 € a 5.000 € facturados en 3 meses. Mis números." },
  { href: "/servicios", icono: "🛠️", titulo: "¿Tienes un negocio sin web?", texto: "Te la hago. Webs y tiendas online desde 150 €." },
  { href: "/creadores", icono: "📲", titulo: "Mi web para creadores", texto: "Lleva todas tus redes desde un sitio. Lista de espera." },
];

export default function Inicio() {
  return (
    <main className="contenedor">
      <header className="cabecera">
        <img className="avatar" src="/pertx.png" alt="Pertx, el personaje con pasamontañas negro y detalles dorados" width="112" height="112" />
        <p className="kicker">@pertx</p>
        <h1>
          Construyo negocios <span className="oro">desde 0</span>
        </h1>
        <p className="sub">Ropa, reventa y apps con IA. Todos los números, sin humo.</p>
      </header>

      <section className="datos" aria-label="Mis números">
        {DATOS.map((d) => (
          <div className="dato" key={d.texto}>
            <b>{d.cifra}</b>
            <span>{d.texto}</span>
          </div>
        ))}
      </section>

      <nav className="enlaces">
        {ENLACES.map((e) => (
          <Link key={e.href} href={e.href} className={`boton${e.destacado ? " destacado" : ""}`}>
            <span className="icono" aria-hidden="true">{e.icono}</span>
            <span>
              <b>{e.titulo}</b>
              <small>{e.texto}</small>
            </span>
          </Link>
        ))}
      </nav>

      <div className="redes">
        <a href={SITIO.tiktok} rel="noopener">TikTok</a>
        <a href={SITIO.instagram} rel="noopener">Instagram</a>
      </div>
    </main>
  );
}

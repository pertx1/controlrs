import "./globals.css";
import Link from "next/link";
import { SITIO } from "../lib/config";

export const metadata = {
  metadataBase: new URL(SITIO.url),
  title: { default: "Pertx · Construyo negocios desde 0", template: "%s · Pertx" },
  description: SITIO.frase,
  openGraph: { title: "Pertx", description: SITIO.frase, images: ["/pertx-auro.png"], locale: "es_ES", type: "website" },
  icons: { icon: "/pertx.png" },
};

export const viewport = { themeColor: "#080706" };

export default function RootLayout({ children }) {
  return (
    <html lang="es">
      <body>
        {children}
        <footer className="pie">
          <p>Pertx es un personaje con avatar y voz generados con IA. Los números que comparto son reales; no son consejos financieros.</p>
          <p>
            <Link href="/aviso-legal">Aviso legal</Link>·<Link href="/privacidad">Privacidad</Link>
          </p>
        </footer>
      </body>
    </html>
  );
}

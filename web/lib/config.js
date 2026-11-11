// Datos de la web en un solo sitio. Lo que es secreto va en variables de entorno (ver .env.example).
export const SITIO = {
  nombre: "Pertx",
  frase: "Construyo negocios desde 0: ropa, reventa y apps con IA. Todos los números, sin humo.",
  url: "https://pertx.vercel.app",
  tiktok: "https://www.tiktok.com/@pertx",
  instagram: "https://www.instagram.com/pertx",
};

export const DATOS = [
  { cifra: "5.000 €", texto: "facturados con mi marca de ropa" },
  { cifra: "4.000+", texto: "seguidores sin anuncios" },
  { cifra: "50–60 %", texto: "de margen por prenda" },
];

export const GUMROAD_URL = process.env.NEXT_PUBLIC_GUMROAD_URL || "";

export const TITULAR = {
  nombre: process.env.NEXT_PUBLIC_TITULAR_NOMBRE || "[NOMBRE DEL TITULAR]",
  nif: process.env.NEXT_PUBLIC_TITULAR_NIF || "[NIF]",
  email: process.env.NEXT_PUBLIC_TITULAR_EMAIL || "[EMAIL DE CONTACTO]",
};

// Servicios de Pertx Studio (precios de lanzamiento para los 3 primeros clientes)
export const SERVICIOS = [
  { nombre: "Web Básica", precio: 150, antes: 300, plazo: "1 semana", texto: "Una página para tu negocio: se ve bien en el móvil, botón de WhatsApp o llamada, mapa, horario y fotos." },
  { nombre: "Web Completa", precio: 300, antes: 550, plazo: "2 semanas", texto: "Hasta 5 páginas, formulario de contacto, Google Maps y lo básico para salir en Google." },
  { nombre: "Tienda Online", precio: 350, antes: 650, plazo: "2 semanas", texto: "Tu tienda en Shopify lista para vender: hasta 20 productos, pagos y envíos. (La cuota de Shopify la pagas tú)." },
  { nombre: "Mantenimiento", precio: 25, antes: 40, plazo: "al mes", texto: "Cambios pequeños cada mes y que todo siga funcionando." },
];

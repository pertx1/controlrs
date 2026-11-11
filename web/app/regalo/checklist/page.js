export const metadata = { title: "Checklist para lanzar tu marca de ropa", robots: { index: false } };

const PASOS = [
  "Elige a quién le vendes (edad, estilo, dónde está en redes).",
  "Haz 3–5 diseños y enséñaselos a 10 personas de ese público antes de fabricar nada.",
  "Empieza bajo demanda: no compres stock hasta saber qué se vende.",
  "Busca una imprenta cerca o empieza con DTF: yo empecé con 30 € en una imprenta de mi barrio.",
  "Calcula el margen de cada prenda con la calculadora. Si baja del 40 %, sube el precio o baja el coste.",
  "Monta la tienda online con fotos buenas (luz natural vale) y textos cortos.",
  "Prepara 10 publicaciones antes de lanzar: diseños, proceso, detrás de cámaras.",
  "Lanza con una fecha y cuéntala días antes.",
  "Reinvierte el primer beneficio en lo que más te frene (yo compré una plancha de 180 €).",
  "Apunta cada venta y cada gasto desde el día 1. Facturar no es ganar.",
  "Habla con tus padres y con una gestoría de cómo facturar antes de vender en serio.",
];

export default function Checklist() {
  return (
    <main className="contenedor">
      <p className="kicker">Tu regalo</p>
      <h1>Checklist para lanzar tu <span className="oro">marca de ropa</span></h1>
      <p className="sub">Los pasos que seguí yo, en orden. Ve marcándolos.</p>
      <div className="panel">
        {PASOS.map((p, i) => (
          <label className="check" key={i}>
            <input type="checkbox" />
            <span><b>{i + 1}.</b> {p}</span>
          </label>
        ))}
      </div>
      <p className="aviso" style={{ marginTop: 16 }}>¿Quieres todo el proceso con mis números? <a href="/guia">Mira la guía completa</a>.</p>
    </main>
  );
}

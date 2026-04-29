"use client";

import { motion } from "framer-motion";
import { 
  ShieldCheck, 
  MonitorCheck, 
  GraduationCap, 
  BrainCircuit, 
  ShoppingBag, 
  Cloud, 
  Layout,
  ArrowRight
   
} from "lucide-react";

export default function ServiciosPage() {
  const WHATSAPP_NUMBER = "573224612382";

  // Función para generar links de WhatsApp con mensajes dinámicos
  const getWhatsAppLink = (serviceName: string) => {
    const message = `Hola Androdri S.A.S, me gustaría recibir más información detallada sobre el servicio de: ${serviceName}`;
    return `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;
  };

  const services = [
    {
      title: "Desarrollo Web de Élite",
      desc: "Creamos experiencias digitales rápidas y memorables usando Next.js. No solo es estética, es una herramienta de ventas optimizada para Google.",
      icon: <Layout size={28} />,
      impacto: "Velocidad de carga < 1s"
    },
    {
      title: "Seguridad ISO 27001",
      desc: "Protegemos el activo más valioso de tu empresa: los datos. Implementamos protocolos de seguridad bajo estándares internacionales para evitar ataques.",
      icon: <ShieldCheck size={28} />,
      impacto: "Blindaje total"
    },
    {
      title: "E-commerce y Pagos",
      desc: "Vende sin límites. Integramos pasarelas de pago seguras y sistemas de inventario que funcionan en piloto automático las 24 horas.",
      icon: <ShoppingBag size={28} />,
      impacto: "Ventas 24/7"
    },
    {
      title: "Inteligencia Artificial",
      desc: "Implementamos soluciones de IA para automatizar la atención al cliente y predecir tendencias de mercado. Tecnología que ahorra tiempo y dinero.",
      icon: <BrainCircuit size={28} />,
      impacto: "Eficiencia predictiva"
    },
    {
      title: "Capacitación Técnica",
      desc: "Entrenamos a tu equipo en Python, Next.js y metodologías ágiles. Elevamos el nivel técnico de tu empresa para que dominen el futuro.",
      icon: <GraduationCap size={28} />,
      impacto: "Talento de alto nivel"
    },
    {
      title: "Servidores Cloud y KVM",
      desc: "Hosting de alto rendimiento en la nube. Tu plataforma siempre en línea, protegida y con escalabilidad instantánea para tráfico masivo.",
      icon: <Cloud size={28} />,
      impacto: "99.9% Uptime"
    },
    {
      title: "Mantenimiento y Soporte",
      desc: "Limpieza profunda de sistemas e instalación de software empresarial. Optimizamos tus equipos para que la tecnología nunca sea un obstáculo.",
      icon: <MonitorCheck size={28} />,
      impacto: "Equipos al 100%"
    }
  ];

  return (
    <main className="w-full bg-slate-50 text-slate-900">

      {/* 🚀 HERO */}
      <section className="relative py-24 md:py-32 overflow-hidden bg-white">
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full">
          <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] rounded-full bg-blue-50 blur-[120px] opacity-60"></div>
        </div>

        <div className="relative z-10 max-w-5xl mx-auto text-center px-6">
          <motion.span 
            initial={{ opacity: 0 }} 
            animate={{ opacity: 1 }} 
            className="inline-block px-4 py-1 mb-6 text-[#2874A6] font-bold tracking-widest uppercase text-xs bg-blue-50 border border-blue-100 rounded-full"
          >
            Ingeniería de Software de Clase Mundial
          </motion.span>
          <motion.h1 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-5xl md:text-7xl font-extrabold mt-4 mb-8 leading-tight tracking-tight text-slate-900"
          >
            No solo creamos webs, <br />
            <span className="text-[#2874A6]">creamos activos digitales.</span>
          </motion.h1>
          <motion.p 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.2 }}
            className="text-xl text-slate-500 max-w-3xl mx-auto leading-relaxed"
          >
            Fusionamos ingeniería avanzada con diseño orientado a la conversión para 
            escalar tu facturación, proteger tu información y automatizar tu crecimiento.
          </motion.p>
        </div>
      </section>

      {/* 🧩 SERVICIOS */}
      <section className="py-24 px-6 bg-slate-50">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold mb-4 text-slate-900">Soluciones que impulsan tu rentabilidad</h2>
            <p className="text-slate-500 max-w-2xl mx-auto text-lg italic font-medium">Infraestructura técnica robusta diseñada para el mercado global.</p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {services.map((service, i) => (
              <a 
                key={i} 
                href={getWhatsAppLink(service.title)} 
                target="_blank" 
                rel="noopener noreferrer"
                className="block"
              >
                <motion.div
                  whileHover={{ y: -10 }}
                  className="group p-8 bg-white border border-slate-200 rounded-[2rem] shadow-xl shadow-slate-200/40 transition-all duration-300 hover:border-[#2874A6]/30 hover:bg-blue-50/30 h-full flex flex-col"
                >
                  <div className="mb-6 flex justify-between items-start">
                    <div className="p-4 bg-slate-50 rounded-2xl text-[#2874A6] group-hover:scale-110 group-hover:bg-[#2874A6] group-hover:text-white transition-all duration-300">
                      {service.icon}
                    </div>
                    <span className="text-[10px] font-bold uppercase tracking-widest text-[#2874A6] bg-blue-50 px-3 py-1 rounded-full border border-blue-100">
                      {service.impacto}
                    </span>
                  </div>
                  <h3 className="text-2xl font-bold mb-4 text-slate-800">{service.title}</h3>
                  <p className="text-slate-500 leading-relaxed text-sm md:text-base grow">
                    {service.desc}
                  </p>
                  <div className="mt-6 flex items-center gap-2 text-sm font-bold text-[#2874A6] opacity-0 group-hover:opacity-100 transition-opacity">
                    Consultar por WhatsApp <ArrowRight size={16} />
                  </div>
                </motion.div>
              </a>
            ))}
          </div>
        </div>
      </section>

      {/* 🔥 CTA FINAL */}
      <section className="py-32 text-center px-6 bg-slate-50 relative overflow-hidden">
        <div className="max-w-4xl mx-auto relative z-10">
          <h2 className="text-4xl md:text-6xl font-black mb-8 text-slate-900 tracking-tighter">
            ¿Listo para dominar tu <br /> mercado digital?
          </h2>
          <p className="text-slate-500 text-xl mb-12 max-w-2xl mx-auto leading-relaxed">
            Agenda una consultoría técnica hoy mismo. Analizaremos tu infraestructura y te entregaremos una hoja de ruta para tu transformación digital exponencial.
          </p>
          <motion.a
            whileHover={{ scale: 1.05, boxShadow: "0 20px 40px -10px rgba(40, 116, 166, 0.4)" }}
            whileTap={{ scale: 0.95 }}
            href={`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent("Hola Androdri S.A.S, me gustaría agendar una consultoría técnica gratuita para mi empresa.")}`}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-block bg-[#2874A6] text-white px-14 py-6 rounded-3xl text-xl font-extrabold transition-all duration-300 shadow-lg"
          >
            Hablar con un experto ahora
          </motion.a>
        </div>
        <div className="absolute bottom-0 left-0 w-full h-1 bg-[#2874A6]"></div>
      </section>

    </main>
  );
}
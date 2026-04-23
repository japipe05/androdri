"use client";

import { motion } from "framer-motion";
import { Check, Zap, Rocket, Laptop, GraduationCap, Settings2 } from "lucide-react";

const services = [
  {
    id: 1,
    name: "Páginas Web (Propiedad)",
    price: 1400000,
    period: " Pago único",
    description: "Activo digital de tu propiedad. Infraestructura robusta y escalable.",
    icon: <Rocket size={26} />,
    highlight: true,
    features: ["5 pantallas estáticas", "Propiedad del código", "Optimización SEO Élite", "Soporte mensual $70k", "Análisis y Diseño previo"],
    cta: "Obtener Propiedad",
  },
  {
    id: 2,
    name: "Web X Servicios",
    price: 90000,
    period: "/ mes",
    description: "Suscripción ágil con todo incluido para despegar de inmediato.",
    icon: <Zap size={26} />,
    highlight: false,
    features: ["Hosting 1vCPU / 4GB RAM", "Dominio incluido", "Mails de notificación", "Actualizaciones técnicas", "Soporte continuo"],
    cta: "Iniciar Suscripción",
  },
  {
    id: 3,
    name: "Capacitaciones IT",
    price: 70000,
    period: "/ hora",
    description: "Formación experta en Python, NextJS, SQL y metodologías Scrum.",
    icon: <GraduationCap size={26} />,
    highlight: false,
    features: ["Python (APIs & CRUD)", "NextJS & React", "SQL (Oracle/MySQL)", "Metodología Scrum", "Proyectos reales"],
    cta: "Agendar Clase",
  },
  {
    id: 4,
    name: "Mantenimiento Pro",
    price: "Cotizar",
    period: "",
    description: "Optimización y salud preventiva para tus equipos de cómputo.",
    icon: <Laptop size={26} />,
    highlight: false,
    features: ["Limpieza física e interna", "Optimización de S.O.", "Seguridad & Antivirus", "Diagnóstico de hardware", "Soporte correctivo"],
    cta: "Solicitar Soporte",
  },
  {
    id: 5,
    name: "Modificaciones Web",
    price: "Variable",
    period: "",
    description: "Evoluciona tu plataforma actual con nuevas funcionalidades.",
    icon: <Settings2 size={26} />,
    highlight: false,
    features: ["Nuevas secciones", "Integración de APIs", "Mejora de UI/UX", "Refactorización", "Cambios bajo demanda"],
    cta: "Pedir Presupuesto",
  }
];

export function PricingSection() {
  const WHATSAPP_NUMBER =  process.env.NEXT_PUBLIC_WHATSAPP_NUMBER;
  

  return (
    <section id="servicios" className="relative w-full max-w-7xl mx-auto py-32 px-6 overflow-hidden">
      <div className="absolute top-0 left-0 w-72 h-72 bg-blue-100/40 rounded-full blur-[100px] -z-10" />
      
      <div className="text-center mb-20">
        <motion.h2 
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          className="text-4xl md:text-5xl font-black text-slate-900 tracking-tighter"
        >
          Soluciones de Ingeniería Digital 🛠️
        </motion.h2>
        <p className="mt-4 text-slate-500 text-lg max-w-2xl mx-auto">
          Desde el desarrollo de software hasta la capacitación experta, escalamos tu infraestructura.
        </p>
      </div>

      <div className="flex flex-wrap justify-center gap-8">
        {services.map((service, i) => {
          // Generamos el link de WhatsApp con el nombre del servicio dinámico
          const whatsappMessage = encodeURIComponent(
            `Hola Androdri S.A.S, deseo solicitar más información sobre el servicio: ${service.name}`
          );
          const whatsappUrl = `https://wa.me/${WHATSAPP_NUMBER}?text=${whatsappMessage}`;

          return (
            <motion.div
              key={service.id}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.1 }}
              whileHover={{ y: -10 }}
              className={`w-full md:w-[calc(50%-2rem)] lg:w-[calc(33.33%-2rem)] relative rounded-[2.5rem] p-10 border transition-all duration-500 flex flex-col ${
                service.highlight 
                  ? "bg-[#2874A6] text-white shadow-2xl scale-105 z-10 border-transparent" 
                  : "bg-white/60 backdrop-blur-md border-slate-100 text-slate-900 hover:shadow-xl"
              }`}
            >
              {/* Icono */}
              <div className={`w-14 h-14 rounded-2xl flex items-center justify-center mb-8 ${
                service.highlight ? "bg-white/20 text-white" : "bg-blue-50 text-[#2874A6]"
              }`}>
                {service.icon}
              </div>

              {/* Título - BLANCO SI ES HIGHLIGHT */}
              <h3 className={`text-2xl font-bold mb-4 ${service.highlight ? "text-white" : "text-slate-900"}`}>
                {service.name}
              </h3>

              {/* Descripción */}
              <p className={`text-sm mb-8 ${service.highlight ? "text-blue-100" : "text-slate-500"}`}>
                {service.description}
              </p>

              {/* Precio */}
              <div className="mb-10">
                <span className={`text-4xl font-black ${service.highlight ? "text-white" : "text-slate-900"}`}>
                  {typeof service.price === "number" 
                    ? new Intl.NumberFormat("es-CO", { style: "currency", currency: "COP", maximumFractionDigits: 0 }).format(service.price)
                    : service.price}
                </span>
                <span className={`text-xs ml-1 font-bold uppercase ${service.highlight ? "text-blue-200" : "text-slate-400"}`}>
                  {service.period}
                </span>
              </div>

              {/* Features */}
              <ul className="space-y-4 mb-12 flex-grow">
                {service.features.map((feat) => (
                  <li key={feat} className="flex items-center gap-3 text-sm font-medium">
                    <Check size={18} className={service.highlight ? "text-blue-300" : "text-[#2874A6]"} />
                    <span className={service.highlight ? "text-white" : "text-slate-700"}>{feat}</span>
                  </li>
                ))}
              </ul>

              {/* Botón de WhatsApp Dinámico */}
              <a 
                href={whatsappUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="block mt-auto"
              >
                <button className={`w-full py-4 rounded-2xl font-bold transition-all duration-300 shadow-md hover:shadow-xl active:scale-95 ${
                  service.highlight 
                    ? "bg-white text-[#2874A6] hover:bg-blue-50" 
                    : "bg-slate-900 text-white hover:bg-[#2874A6]"
                }`}>
                  {service.cta}
                </button>
              </a>
            </motion.div>
          );
        })}
      </div>
    </section>
  );
}
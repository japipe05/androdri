"use client";
import { TypeAnimation } from "react-type-animation";
import dynamic from "next/dynamic";
import { motion } from "framer-motion";
import { PricingSection } from "@/components/PricingSection";
import {
  ArrowRight, ShieldCheck, Zap, Fingerprint, Bot,
  MonitorCheck, GraduationCap, BrainCircuit, ShoppingBag,
  Cloud, Layout, CheckCircle, Smartphone
} from "lucide-react";

// Cargamos el visor 3D de forma dinámica para no afectar el LCP
const ModelViewer = dynamic(() => import("@/components/ModelViewer"), {
  ssr: false,
  loading: () => <div className="h-[550px] w-full animate-pulse bg-slate-50 rounded-3xl" />
});

export default function Home() {
  return (
    <main className="min-h-screen bg-white text-slate-900 overflow-x-hidden selection:bg-[#2874A6] selection:text-white">

      {/* 🚀 HERO SECTION: Ingeniería de Élite */}
      <section className="relative pt-20 pb-32 px-6 lg:px-12 max-w-7xl mx-auto min-h-[95vh] flex items-center">
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full bg-[radial-gradient(circle_at_center,_#f1f5f9_0%,transparent_70%)] -z-10 opacity-60" />

        <div className="grid lg:grid-cols-2 gap-12 items-center w-full">
          <motion.div
            initial={{ opacity: 0, x: -30 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 1.2, ease: "easeOut" }}
            className="space-y-8 z-10"
          >
            <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-slate-900 text-white text-[10px] font-black uppercase tracking-[0.3em] shadow-sm">
              <span className="relative flex h-2 w-2">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#2874A6] opacity-75"></span>
                <span className="relative inline-flex rounded-full h-2 w-2 bg-[#2874A6]"></span>
              </span>
              Arquitectura de Activos Digitales de Élite
            </div>

            <h1 className="text-fluid-h1 font-black tracking-tighter leading-[0.95] text-slate-900">
              Soluciones que <br />
              <span className="text-[#2874A6]">
                <TypeAnimation
                  sequence={[
                    "Construyen.", 5000,
                    "Blindan.", 5000,
                    "Trascienden.", 5000
                  ]}
                  speed={20}
                  repeat={Infinity}
                />
              </span>
            </h1>


            <div className="space-y-6">
              <p className="text-fluid-body text-slate-500 max-w-lg leading-relaxed font-medium border-l-4 border-[#2874A6] pl-6">
                Diseñamos el futuro de tu infraestructura. En <span className="text-slate-900 font-bold">Androdri S.A.S</span>
                integramos <span className="text-slate-900 font-bold underline decoration-[#2874A6]">Inteligencia Artificial</span>
                para que tu empresa nunca deje de <span className="text-[#2874A6] font-extrabold"> evolucionar.</span>
              </p>

              <blockquote className="pl-6 italic text-slate-400 text-sm border-l-4 border-slate-200">
                "Somos lo que hacemos día tras día. La excelencia, no es un acto, sino un hábito."
                <span className="block mt-2 font-bold text-slate-500">— Aristóteles</span>
                <span className="text-[10px] uppercase tracking-widest text-[#2874A6]">Ingeniería de clase mundial por definición.</span>
              </blockquote>
            </div>
            <div className="flex flex-wrap gap-5 pt-4">
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="bg-[#2874A6] text-white px-10 py-5 rounded-2xl font-black text-sm uppercase tracking-widest shadow-2xl shadow-blue-200 flex items-center gap-3 group"
              >
                Ver Catálogo
                <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </motion.button>
            </div>
          </motion.div>

          {/* MODELO 3D: Interactivo */}
          <motion.div
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.3, duration: 1.5 }}
            className="h-[500px] lg:h-[700px] relative flex items-center justify-center"
          >
            <ModelViewer />
          </motion.div>
        </div>
      </section>

      {/* 🧩 ECOSISTEMA DE SERVICIOS: Silos de Venta */}
      <section className="py-32 bg-slate-50 border-y border-slate-100 px-6">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-24 space-y-4">
            <h2 className="text-fluid-h2 font-black tracking-tighter">Soluciones de <span className="text-[#2874A6]">Alto Impacto</span></h2>
            <p className="text-slate-500 max-w-2xl mx-auto text-lg italic font-medium">Infraestructura técnica robusta diseñada para el mercado global.</p>
            <div className="h-1.5 w-24 bg-[#2874A6] mx-auto rounded-full" />
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            <ServiceCard
              icon={<Layout size={28} />}
              title="Desarrollo Web Élite"
              desc="Estructuras en Next.js optimizadas para SEO y conversión. Velocidad de carga < 1s."
              impacto="ROI Inmediato"
            />
            <ServiceCard
              icon={<ShieldCheck size={28} />}
              title="Seguridad ISO 27001"
              desc="Blindaje total de datos y protocolos de ciberseguridad bajo estándares internacionales."
              impacto="Riesgo Cero"
            />
            <ServiceCard
              icon={<ShoppingBag size={28} />}
              title="E-commerce & Pagos"
              desc="Integración de pasarelas de pago y automatización de flujos transaccionales 24/7."
              impacto="+ Ventas"
            />
            <ServiceCard
              icon={<BrainCircuit size={28} />}
              title="Inteligencia Artificial"
              desc="Modelos predictivos y automatización de procesos para ahorrar tiempo y dinero."
              impacto="Eficiencia"
            />
            <ServiceCard
              icon={<Cloud size={28} />}
              title="Cloud & Infraestructura"
              desc="Servidores KVM, hosting de alto rendimiento y migración a AWS/Azure/Google Cloud."
              impacto="99.9% Uptime"
            />
            <ServiceCard
              icon={<Fingerprint size={28} />}
              title="Firma Digital & Legal"
              desc="Sistemas de autenticación documental y gestión de firmas digitales seguras."
              impacto="Legal Tech"
            />
          </div>
        </div>
      </section>

      {/* ⭐ DIFERENCIADORES: Por qué Androdri? */}
      <section className="py-32 bg-white px-6">
        <div className="max-w-7xl mx-auto grid lg:grid-cols-2 gap-20 items-center">
          <div className="space-y-10">
            <h2 className="text-fluid-h2 font-bold leading-tight text-slate-900">¿Por qué las empresas eligen nuestra ingeniería?</h2>
            <div className="space-y-8">
              {[
                { t: "Cero Cuellos de Botella", d: "Sistemas diseñados para procesar miles de transacciones simultáneas sin errores técnicos." },
                { t: "Estándares Bancarios", d: "Seguridad ISO 27001 para que tu negocio esté blindado contra cualquier vulnerabilidad." },
                { t: "Transferencia de Valor", d: "No solo entregamos software, capacitamos a tu equipo en Python, Next.js y metodologías ágiles." }
              ].map((item, idx) => (
                <motion.div key={idx} initial={{ opacity: 0, y: 10 }} whileInView={{ opacity: 1, y: 0 }} className="flex gap-5 items-start">
                  <div className="p-2 bg-blue-50 rounded-full shrink-0">
                    <CheckCircle className="text-[#2874A6]" size={28} />
                  </div>
                  <div>
                    <h4 className="font-bold text-xl text-slate-800 mb-1">{item.t}</h4>
                    <p className="text-slate-500 leading-relaxed">{item.d}</p>
                  </div>
                </motion.div>
              ))}
            </div>
          </div>

          <motion.div
            whileHover={{ rotate: -1 }}
            className="bg-gradient-to-br from-[#2874A6] to-blue-700 rounded-[3.5rem] p-12 text-white shadow-2xl relative overflow-hidden"
          >
            <div className="relative z-10">
              <div className="text-6xl mb-6 opacity-30 font-serif">“</div>
              <h3 className="text-3xl font-bold mb-6 italic text-blue-50">El costo de no innovar es mayor al de invertir.</h3>
              <p className="text-blue-100 mb-10 text-xl leading-relaxed">
                "Androdri S.A.S transformó nuestra operativa, logrando procesar un 40% más de flujos transaccionales sin errores de servidor."
              </p>
              <div className="flex items-center gap-4">
                <div className="h-1 w-10 bg-blue-300"></div>
                <p className="font-bold tracking-widest uppercase text-xs">Fintech Partner de Alto Impacto</p>
              </div>
            </div>
            <div className="absolute top-[-20%] right-[-10%] w-64 h-64 bg-white/10 rounded-full blur-3xl"></div>
          </motion.div>
        </div>
      </section>

      {/* 💰 TARIFAS */}
      <PricingSection />

      {/* 🔥 CTA FINAL: Conversión Directa */}
      <section className="py-32 text-center px-6 bg-slate-900 relative overflow-hidden">
        <div className="max-w-4xl mx-auto relative z-10 space-y-10">
          <h2 className="text-fluid-h2 font-black text-white tracking-tighter">
            ¿Listo para dominar tu mercado digital?
          </h2>
          <p className="text-slate-400 text-xl max-w-2xl mx-auto leading-relaxed">
            Agenda una consultoría técnica hoy mismo. Analizaremos tu infraestructura y trazaremos la hoja de ruta para tu crecimiento exponencial.
          </p>
          <motion.a
            whileHover={{ scale: 1.05, shadow: "0 20px 50px -10px rgba(40, 116, 166, 0.5)" }}
            whileTap={{ scale: 0.95 }}
            href="https://wa.me/tu-numero"
            className="inline-block bg-[#2874A6] text-white px-14 py-6 rounded-3xl text-xl font-extrabold transition-all duration-300"
          >
            Hablar con un Experto
          </motion.a>
        </div>
        <div className="absolute bottom-0 left-0 w-full h-1 bg-[#2874A6]"></div>
      </section>
    </main>
  );
}

// Componente Interno para las Tarjetas de Servicio
function ServiceCard({ icon, title, desc, impacto }: { icon: React.ReactNode, title: string, desc: string, impacto: string }) {
  return (
    <motion.div
      whileHover={{ y: -10 }}
      className="group p-10 bg-white rounded-[3rem] border border-slate-100 shadow-xl shadow-slate-200/40 transition-all duration-300 hover:border-[#2874A6]/30 flex flex-col h-full"
    >
      <div className="mb-6 flex justify-between items-start">
        <div className="w-16 h-16 rounded-2xl bg-slate-50 flex items-center justify-center text-[#2874A6] group-hover:bg-[#2874A6] group-hover:text-white transition-all duration-500 transform group-hover:rotate-6">
          {icon}
        </div>
        <span className="text-[10px] font-bold uppercase tracking-widest text-[#2874A6] bg-blue-50 px-3 py-1 rounded-full border border-blue-100">
          {impacto}
        </span>
      </div>
      <h3 className="text-2xl font-black text-slate-900 tracking-tight mb-4">{title}</h3>
      <p className="text-slate-500 font-medium leading-relaxed text-sm grow">{desc}</p>
      <div className="mt-8 flex items-center gap-2 text-sm font-bold text-[#2874A6] opacity-0 group-hover:opacity-100 transition-opacity">
        Saber más <ArrowRight size={16} />
      </div>
    </motion.div>
  );
}
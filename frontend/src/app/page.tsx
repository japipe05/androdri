"use client";
import { TypeAnimation } from "react-type-animation";
import dynamic from "next/dynamic";
import { motion } from "framer-motion";
import { PricingSection } from "@/components/PricingSection";
import { 
  ArrowRight, 
  Cpu, 
  Smartphone, 
  ShieldCheck, 
  BarChart3, 
  Layers, 
  Zap, 
  Globe,
  Fingerprint,
  Bot
} from "lucide-react";

const ModelViewer = dynamic(() => import("@/components/ModelViewer"), { ssr: false });

export default function Home() {
  return (
    <main className="min-h-screen bg-white text-slate-900 overflow-x-hidden">
      
      {/* 🚀 HERO SECTION: REEQUILIBRADA */}
      <section className="relative pt-20 pb-32 px-6 lg:px-12 max-w-7xl mx-auto min-h-[90vh] flex items-center">
        {/* Glow de fondo más sutil para no ensuciar el 3D */}
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full bg-[radial-gradient(circle_at_center,_#f1f5f9_0%,transparent_70%)] -z-10 opacity-50" />
        
        <div className="grid lg:grid-cols-2 gap-16 items-center w-full">
          
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 1.5, ease: "easeOut" }} // Movimiento de entrada más lento
            className="space-y-10 z-10"
          >
            <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-slate-900 text-white text-[10px] font-black uppercase tracking-[0.3em] shadow-sm">
              <span className="relative flex h-2 w-2">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#2874A6] opacity-75"></span>
                <span className="relative inline-flex rounded-full h-2 w-2 bg-[#2874A6]"></span>
              </span>
              Sistemas de Alto Rendimiento
            </div>

            <h1 className="text-5xl md:text-7xl font-black tracking-tighter leading-[0.95] text-slate-900">
              Ingeniería que <br />
              <span className="text-[#2874A6] inline-block">
                <TypeAnimation
                  sequence={[
                    "Evoluciona.", 3500, // Aumentado a 3.5 segundos de espera
                    "Escala.", 3500,
                    "Conecta.", 3500,
                  ]}
                  speed={30} // Velocidad de escritura más lenta y elegante
                  repeat={Infinity}
                />
              </span>
            </h1>

            <p className="text-lg md:text-xl text-slate-500 max-w-lg leading-relaxed font-medium border-l-2 border-slate-100 pl-6">
              En <span className="text-slate-900 font-bold">Androdri S.A.S</span>, diseñamos soluciones donde la estética y la potencia técnica convergen para transformar negocios.
            </p>

            <div className="flex flex-wrap gap-5 pt-4">
              <button className="bg-[#2874A6] text-white px-10 py-5 rounded-2xl font-black text-sm uppercase tracking-widest shadow-2xl shadow-blue-100 hover:scale-105 transition-all flex items-center gap-3 group">
                Catálogo
                <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </button>
            </div>
          </motion.div>

          {/* MODELO 3D: Con más espacio visual */}
          <motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.5, duration: 2 }} // El modelo aparece después del texto suavemente
            className="h-[550px] lg:h-[750px] relative flex items-center justify-center cursor-grab active:cursor-grabbing"
          >
            {/* El Modelo es ahora el protagonista absoluto del lado derecho */}
            <ModelViewer />
          </motion.div>
        </div>
      </section>

      {/* SECCIÓN DE SERVICIOS... (se mantiene igual pero con espaciado amplio) */}
      <section className="py-32 bg-slate-50 border-y border-slate-100 px-6">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-24 space-y-6">
            <h2 className="text-4xl md:text-6xl font-black tracking-tighter">Ecosistema <span className="text-[#2874A6]">Digital</span></h2>
            <div className="h-1 w-20 bg-[#2874A6] mx-auto rounded-full" />
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            <ServiceCard icon={<Layers />} title="Apps Web & Móviles" desc="Arquitecturas escalables con Next.js y React Native." />
            <ServiceCard icon={<Bot />} title="Inteligencia Artificial" desc="Automatización y modelos predictivos personalizados." />
            <ServiceCard icon={<Zap />} title="Pasarelas de Pago" desc="Integración de flujos transaccionales y E-commerce." />
            <ServiceCard icon={<Fingerprint />} title="Firma Digital" desc="Sistemas legales de autenticación documental." />
          </div>
        </div>
      </section>

      <section className="py-24 bg-white">
        <PricingSection />
      </section>
    </main>
  );
}

function ServiceCard({ icon, title, desc }: { icon: React.ReactNode, title: string, desc: string }) {
  return (
    <motion.div 
      whileHover={{ y: -10 }}
      className="p-10 bg-white rounded-[3rem] border border-slate-100 shadow-sm hover:shadow-2xl hover:shadow-blue-900/5 transition-all flex flex-col gap-5 group"
    >
      <div className="w-14 h-14 rounded-2xl bg-slate-50 flex items-center justify-center text-[#2874A6] group-hover:bg-[#2874A6] group-hover:text-white transition-all duration-500 transform group-hover:rotate-6">
        {icon}
      </div>
      <h3 className="text-2xl font-black text-slate-900 tracking-tight">{title}</h3>
      <p className="text-slate-500 font-medium leading-relaxed">{desc}</p>
    </motion.div>
  );
}
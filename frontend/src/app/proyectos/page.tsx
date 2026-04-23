"use client";
import { motion } from "framer-motion";
import Image from "next/image";
import { 
   
  ExternalLink, 
  Zap, 
  
  Search,
  MessageSquareCode,
  
  Cpu,
  Globe,
  MousePointer2,
  BarChart3,
  Sparkles
} from "lucide-react";

export default function ProyectosPage() {
    const WHATSAPP_NUMBER = "573224612382";



  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: { staggerChildren: 0.2 }
    }
  };

  const itemVariants = {
    hidden: { y: 20, opacity: 0 },
    visible: { y: 0, opacity: 1 }
  };

  return (
    <main className="bg-white text-slate-900 min-h-screen">
      
      {/* 🏔️ HERO: Glassmorphism & Minimalismo */}
      <section className="relative pt-32 pb-20 px-6 overflow-hidden">
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full bg-[radial-gradient(#e2e8f0_1px,transparent_1px)] [background-size:32px_32px] [mask-image:radial-gradient(ellipse_50%_50%_at_50%_50%,#000_70%,transparent_100%)] -z-10 opacity-50" />
        
        <div className="max-w-7xl mx-auto text-center relative">
          <motion.div 
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-blue-50 border border-blue-100 text-[#2874A6] text-xs font-black uppercase tracking-[0.2em] mb-8"
          >
            <Sparkles className="w-3 h-3" /> Portafolio 2026
          </motion.div>
          
          <motion.h1 
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-6xl md:text-8xl font-black tracking-tighter mb-8 italic"
          >
            Ingeniería que <br />
            <span className="text-[#2874A6] not-italic text-outline">Trasciende.</span>
          </motion.h1>
          
          <motion.p 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.4 }}
            className="text-slate-500 text-lg md:text-2xl max-w-3xl mx-auto font-medium leading-relaxed"
          >
            Convertimos la complejidad técnica en interfaces simples, rápidas y diseñadas para dominar el mercado digital.
          </motion.p>
        </div>
      </section>

      {/* 🚀 CASE STUDY: SISCON ELITE (The "Awesome" Card) */}
      <section className="py-12 px-6 max-w-7xl mx-auto">
        <motion.div 
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true }}
          variants={containerVariants}
          className="grid lg:grid-cols-12 gap-8"
        >
          {/* Lado Visual - Ocupa 7 columnas */}
          <motion.div 
            variants={itemVariants}
            className="lg:col-span-7 relative group"
          >
           <div className="relative rounded-[3.5rem] bg-slate-100 p-2 overflow-hidden border border-slate-200">
  <div className="bg-white rounded-[3rem] overflow-hidden aspect-[16/10] flex items-center justify-center p-12 relative">
   <Image 
  src="/img/sisconelite.png"
  alt="SisconElite S.A.S"
  fill
  className="object-cover z-10 transition-transform duration-700 group-hover:scale-110"
/>
    <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-blue-50 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700" />
  </div>
</div>
            
            {/* Badge Flotante de Performance */}
            <motion.div 
              animate={{ y: [0, -10, 0] }}
              transition={{ repeat: Infinity, duration: 4 }}
              className="absolute -top-4 -right-4 bg-[#2874A6] text-white p-6 rounded-3xl shadow-2xl z-20 hidden md:block border-4 border-white"
            >
              <Cpu className="w-8 h-8 mb-2" />
              <p className="text-3xl font-black">99.9%</p>
              <p className="text-[10px] font-bold uppercase tracking-widest opacity-80">Uptime Garantizado</p>
            </motion.div>
          </motion.div>

          {/* Lado Contenido - Ocupa 5 columnas */}
          <motion.div variants={itemVariants} className="lg:col-span-5 flex flex-col justify-center space-y-8">
            <div className="space-y-4">
              <h2 className="text-4xl md:text-5xl font-black text-slate-900 tracking-tight">SisconElite S.A.S</h2>
              <p className="inline-block px-4 py-1 rounded-lg bg-green-50 text-green-700 font-bold text-sm">Case Study: FinTech & ERP</p>
             <p className="text-slate-600 text-lg leading-relaxed">
  Reinventamos la arquitectura de datos para soportar millones de transacciones contables. Una solución <strong>rápida, segura y visualmente impecable</strong> que redefine la consultoría tributaria.
</p>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div className="p-4 rounded-3xl bg-slate-50 border border-slate-100 group hover:border-[#2874A6] transition-colors">
                <BarChart3 className="text-[#2874A6] mb-2" />
                <h4 className="font-bold text-sm">Escalabilidad</h4>
                <p className="text-xs text-slate-400">Core optimizado para crecimiento masivo.</p>
              </div>
              <div className="p-4 rounded-3xl bg-slate-50 border border-slate-100 group hover:border-[#2874A6] transition-colors">
                <Globe className="w-5 h-5 text-[#2874A6] mb-2" />
                <h4 className="font-bold text-sm">Cloud Ready</h4>
                <p className="text-xs text-slate-400">Implementación en AWS / Azure.</p>
              </div>
            </div>

            <div className="pt-4">
              <a 
                href="https://sisconelite.com/" 
                target="_blank"
                className="group inline-flex items-center gap-4 bg-[#2874A6] text-white pl-8 pr-2 py-2 rounded-full font-bold text-lg hover:bg-slate-900 transition-all shadow-xl shadow-blue-100"
              >
                Explorar Proyecto
                <div className="bg-white/20 p-3 rounded-full group-hover:rotate-45 transition-transform">
                  <ExternalLink className="w-5 h-5" />
                </div>
              </a>
            </div>
          </motion.div>
        </motion.div>
      </section>

      {/* 💎 INNOVATION GRID (Bento Style) */}
      <section className="py-24 px-6 bg-slate-50">
        <div className="max-w-7xl mx-auto">
          <div className="mb-16 text-center">
            <h2 className="text-4xl font-black mb-4">¿Por qué es <span className="text-[#2874A6]">Awesome</span>?</h2>
            <p className="text-slate-500 font-medium italic">La experiencia de usuario que tus clientes contables merecen.</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {/* Card 1 */}
            <div className="md:col-span-2 bg-white p-10 rounded-[3rem] border border-slate-200 flex flex-col justify-between hover:shadow-xl transition-shadow relative overflow-hidden group">
              <div className="relative z-10">
                <Search className="w-12 h-12 text-[#2874A6] mb-6" />
                <h3 className="text-3xl font-black mb-4">Encuentro Fácil</h3>
                <p className="text-slate-500 max-w-md">
                  No solo apareces en Google; dominas la intención de búsqueda. Nuestros algoritmos de SEO posicionan tu consultoría frente a la competencia.
                </p>
              </div>
              <div className="absolute -bottom-10 -right-10 text-[#2874A6]/5 group-hover:scale-110 transition-transform">
                <Globe className="w-64 h-64" />
              </div>
            </div>

            {/* Card 2 */}
            <div className="bg-[#2874A6] p-10 rounded-[3rem] text-white flex flex-col justify-between group hover:bg-slate-900 transition-colors">
              <MousePointer2 className="w-12 h-12 mb-6 group-hover:scale-125 transition-transform" />
              <div>
                <h3 className="text-3xl font-black mb-4 italic">Fricción Cero</h3>
              <p className="text-blue-100 text-sm">
  Interfaces diseñadas para que un cliente pase de {`"curioso"`} a {`"contratado"`} en segundos.
</p>
              </div>
            </div>

            {/* Card 3 */}
            <div className="bg-slate-900 p-10 rounded-[3rem] text-white md:col-span-1 flex flex-col justify-between">
              <Zap className="w-12 h-12 text-yellow-400 mb-6" />
              <div>
                <h3 className="text-3xl font-black mb-4">Rápido</h3>
                <p className="text-slate-400 text-sm italic">Cargas en menos de 1s para retención máxima.</p>
              </div>
            </div>

            {/* Card 4 */}
            <div className="md:col-span-2 bg-white p-10 rounded-[3rem] border border-slate-200 flex items-center gap-8 group">
              <div className="hidden sm:flex w-24 h-24 bg-blue-50 rounded-full items-center justify-center flex-shrink-0 group-hover:rotate-12 transition-transform">
                <MessageSquareCode className="w-10 h-10 text-[#2874A6]" />
              </div>
              <div>
                <h3 className="text-3xl font-black mb-2 italic">Contacto Inteligente</h3>
                <p className="text-slate-500">Integración con WhatsApp Business y CRM contable automatizado.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 🤙 CALL TO ACTION: BOLD & MINIMAL */}
      <section className="py-32 px-6">
        <div className="max-w-5xl mx-auto rounded-[4rem] bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] bg-[#2874A6] p-12 md:p-24 text-center text-white relative overflow-hidden shadow-[0_40px_100px_-20px_rgba(40,116,166,0.4)]">
           <motion.div 
            initial={{ opacity: 0, scale: 0.9 }}
            whileInView={{ opacity: 1, scale: 1 }}
            className="relative z-10"
          >
            <h2 className="text-5xl md:text-7xl font-black mb-8 tracking-tighter">
              ¿Tu empresa es la <br /> <span className="underline decoration-white/30">próxima?</span>
            </h2>
            <a 
              href={`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent("Hola Androdri S.A.S, me gustaría agendar una cita técnica para iniciar un proyecto de alto impacto.")}`}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-block bg-white text-[#2874A6] px-12 py-6 rounded-full font-black text-2xl hover:bg-slate-900 hover:text-white transition-all transform hover:scale-110 active:scale-95 shadow-2xl"
            >
              AGENDA UNA CITA TÉCNICA
            </a>
          </motion.div>
          {/* Círculos decorativos */}
          <div className="absolute top-0 right-0 w-64 h-64 bg-white/10 rounded-full blur-3xl -translate-y-32 translate-x-32" />
          <div className="absolute bottom-0 left-0 w-64 h-64 bg-black/10 rounded-full blur-3xl translate-y-32 -translate-x-32" />
        </div>
      </section>

    </main>
  );
}
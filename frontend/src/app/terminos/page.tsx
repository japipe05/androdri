"use client";

import { motion } from "framer-motion";
import { Scale, Gavel, FileCode, Clock, ShieldAlert, BadgeCheck } from "lucide-react";

export default function TerminosServicio() {


  return (
    <main className="min-h-screen bg-white text-slate-900 py-24 px-6 lg:px-12 selection:bg-[#2874A6] selection:text-white">
      {/* Header */}
      <section className="max-w-4xl mx-auto text-center mb-20">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-slate-900 text-white text-[10px] font-black uppercase tracking-[0.2em] mb-6"
        >
          <Scale size={14} className="text-[#2874A6]" />
          Marco Legal Contractual
        </motion.div>
        <h1 className="text-4xl md:text-5xl font-black tracking-tighter mb-6">
          Términos de <span className="text-[#2874A6]">Servicio</span>
        </h1>
        <p className="text-slate-500 font-medium">
          Acuerdo de prestación de servicios de ingeniería · Androdri S.A.S
        </p>
      </section>

      {/* Contenido Principal */}
      <section className="max-w-4xl mx-auto space-y-16">
        
        {/* Resumen Ejecutivo */}
        <div className="grid md:grid-cols-3 gap-6">
          <HighlightCard 
            icon={<FileCode size={20} />} 
            title="Propiedad Intelectual" 
            text="El código es suyo en planes de propiedad." 
          />
          <HighlightCard 
            icon={<Clock size={20} />} 
            title="Metodología Ágil" 
            text="Entregas basadas en sprints y objetivos." 
          />
          <HighlightCard 
            icon={<ShieldAlert size={20} />} 
            title="Garantía Técnica" 
            text="Soporte post-entrega incluido." 
          />
        </div>

        {/* Artículos Detallados */}
        <div className="space-y-12 text-slate-600">
          
          <article>
            <h2 className="text-2xl font-bold text-slate-900 mb-4 flex items-center gap-3">
              <Gavel className="text-[#2874A6]" size={24} /> 1. Objeto del Servicio
            </h2>
            <p className="leading-relaxed">
              Androdri S.A.S se compromete a la prestación de servicios de consultoría, desarrollo de software, mantenimiento de infraestructura IT y capacitación técnica según lo especificado en la propuesta comercial aceptada por el cliente. Cada proyecto se rige bajo los estándares de calidad de ingeniería moderna.
            </p>
          </article>

          <article>
            <h2 className="text-2xl font-bold text-slate-900 mb-4 flex items-center gap-3">
              <FileCode className="text-[#2874A6]" size={24} /> 2. Propiedad del Código y Activos
            </h2>
          <p className="leading-relaxed">
  En el modelo de <strong>{`"Páginas Web (Propiedad)"`}</strong>, una vez liquidado el pago total, el cliente adquiere la propiedad total sobre el código fuente y activos visuales. En modelos de <strong>{`"Suscripción"`}</strong>, Androdri S.A.S otorga una licencia de uso temporal sobre la infraestructura y el diseño mientras la suscripción permanezca activa.
</p>
          </article>

          <article>
            <h2 className="text-2xl font-bold text-slate-900 mb-4 flex items-center gap-3">
              <Clock className="text-[#2874A6]" size={24} /> 3. Tiempos de Entrega y Soporte
            </h2>
            <p className="leading-relaxed">
              Los plazos de entrega son estimaciones basadas en la disponibilidad técnica y la agilidad de respuesta del cliente. El soporte técnico incluido en los planes cubre errores de código y estabilidad del servidor, excluyendo modificaciones de diseño o nuevas funcionalidades no pactadas inicialmente.
            </p>
          </article>

          <article>
            <h2 className="text-2xl font-bold text-slate-900 mb-4 flex items-center gap-3">
              <ShieldAlert className="text-[#2874A6]" size={24} /> 4. Responsabilidad Limitada
            </h2>
            <p className="leading-relaxed">
              Androdri S.A.S no se hace responsable por pérdidas de datos derivadas de accesos no autorizados por negligencia del cliente (ej. contraseñas débiles) o fallos en proveedores de infraestructura externos (AWS, Azure, Google Cloud), aunque garantizamos la gestión de mitigación bajo protocolos <strong>ISO 27001</strong>.
            </p>
          </article>

          <article>
            <h2 className="text-2xl font-bold text-slate-900 mb-4 flex items-center gap-3">
              <BadgeCheck className="text-[#2874A6]" size={24} /> 5. Modificaciones de Tarifas
            </h2>
            <p className="leading-relaxed">
              Las tarifas de suscripción mensual pueden ser ajustadas anualmente con previo aviso de 30 días calendario, reflejando las mejoras en la infraestructura y los ajustes inflacionarios del mercado tecnológico.
            </p>
          </article>

        </div>

        {/* Footer de Términos */}
        <div className="bg-slate-50 p-10 rounded-[3rem] border border-slate-100 text-center">
          <h3 className="text-xl font-bold mb-4">¿Desea una copia personalizada?</h3>
          <p className="text-slate-500 text-sm mb-8 max-w-md mx-auto">
            Si su empresa requiere un contrato de prestación de servicios con cláusulas de confidencialidad (NDA) específicas, podemos coordinarlo.
          </p>
          <a 
            href="https://wa.me/573224612382?text=Hola%20Androdri%20S.A.S,%20solicito%20un%20contrato%20personalizado%20para%20mi%20proyecto."
            target="_blank"
            rel="noopener noreferrer"
          >
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              className="bg-[#2874A6] text-white px-10 py-5 rounded-2xl font-black text-xs uppercase tracking-widest shadow-xl"
            >
              Contactar al área legal
            </motion.button>
          </a>
        </div>

        <p className="text-center text-slate-400 text-xs">
          Androdri S.A.S © 2026 · Todos los derechos reservados.
        </p>
      </section>
    </main>
  );
}

function HighlightCard({ icon, title, text }: { icon: React.ReactNode, title: string, text: string }) {
  return (
    <div className="p-6 rounded-3xl border border-slate-100 bg-white shadow-sm flex flex-col items-center text-center">
      <div className="text-[#2874A6] mb-3">{icon}</div>
      <h4 className="font-bold text-sm text-slate-900 mb-1">{title}</h4>
      <p className="text-slate-500 text-xs">{text}</p>
    </div>
  );
}
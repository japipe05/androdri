"use client";

import { motion } from "framer-motion";
import { ShieldCheck, Lock, EyeOff, FileText, Server, Globe } from "lucide-react";

export default function PoliticaPrivacidad() {
  const lastUpdate = "22 de abril de 2026";

  return (
    <main className="min-h-screen bg-white text-slate-900 py-24 px-6 lg:px-12 selection:bg-[#2874A6] selection:text-white">
      {/* Encabezado Principal */}
      <section className="max-w-4xl mx-auto text-center mb-20">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-blue-50 text-[#2874A6] text-[10px] font-black uppercase tracking-[0.2em] mb-6"
        >
          <ShieldCheck size={14} />
          Estándar de Seguridad Corporativa
        </motion.div>
        <h1 className="text-4xl md:text-5xl font-black tracking-tighter mb-6">
          Política de <span className="text-[#2874A6]">Privacidad</span>
        </h1>
        <p className="text-slate-500 font-medium italic">
          Última actualización: {lastUpdate}
        </p>
      </section>

      {/* Contenido Estructurado */}
      <section className="max-w-4xl mx-auto space-y-16">
        
        {/* Compromiso ISO 27001 */}
        <motion.div 
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          className="p-8 rounded-[2.5rem] bg-slate-50 border border-slate-100 relative overflow-hidden"
        >
          <div className="relative z-10">
            <h2 className="text-2xl font-bold flex items-center gap-3 mb-4">
              <Lock className="text-[#2874A6]" /> Compromiso ISO 27001
            </h2>
            <p className="text-slate-600 leading-relaxed">
              En <strong>Androdri S.A.S</strong>, la seguridad de la información no es solo una política, es nuestra arquitectura. Aplicamos controles basados en la norma <strong>ISO/IEC 27001</strong> para garantizar la confidencialidad, integridad y disponibilidad de sus datos mediante cifrado de grado militar y protocolos de acceso restringido.
            </p>
          </div>
          <div className="absolute top-0 right-0 p-4 opacity-5">
            <ShieldCheck size={120} />
          </div>
        </motion.div>

        {/* Puntos Clave */}
        <div className="grid md:grid-cols-2 gap-8">
          <Section 
            icon={<EyeOff size={24} />}
            title="Recolección Mínima"
            content="Solo solicitamos los datos estrictamente necesarios para la prestación de servicios de ingeniería y soporte técnico. No comercializamos su información con terceros bajo ninguna circunstancia."
          />
          <Section 
            icon={<Server size={24} />}
            title="Almacenamiento Seguro"
            content="Los datos se alojan en infraestructuras cloud con certificación de cumplimiento y redundancia geográfica, protegidos por firewalls de última generación y monitoreo preventivo."
          />
        </div>

        {/* Detalles Legales */}
        <div className="space-y-8 text-slate-600">
          <article>
            <h3 className="text-xl font-bold text-slate-900 mb-4 flex items-center gap-2">
              <FileText className="text-[#2874A6]" size={20} /> 1. Tratamiento de Datos Personales
            </h3>
            <p>
              De acuerdo con la Ley 1581 de 2012, Androdri S.A.S, identificado con los datos de contacto presentes en este portal, actúa como Responsable del Tratamiento de sus datos. Estos serán utilizados para:
            </p>
            <ul className="list-disc pl-6 mt-4 space-y-2">
              <li>Gestión de servicios de desarrollo web y mantenimiento.</li>
              <li>Envío de actualizaciones técnicas y presupuestos solicitados.</li>
              <li>Cumplimiento de obligaciones contractuales y legales.</li>
            </ul>
          </article>

          <article>
            <h3 className="text-xl font-bold text-slate-900 mb-4 flex items-center gap-2">
              <Globe className="text-[#2874A6]" size={20} /> 2. Derechos del Titular (Habeas Data)
            </h3>
            <p>
              Usted tiene derecho a conocer, actualizar y rectificar sus datos personales en cualquier momento. Para ejercer estos derechos, puede contactar a nuestro oficial de seguridad de la información a través de nuestro canal de WhatsApp corporativo o correo electrónico oficial.
            </p>
          </article>

          <article>
            <h3 className="text-xl font-bold text-slate-900 mb-4 flex items-center gap-2">
              <Lock className="text-[#2874A6]" size={20} /> 3. Protocolos de Cifrado
            </h3>
            <p>
              Toda comunicación entre su navegador y nuestros servidores viaja protegida mediante protocolos TLS/SSL. Realizamos auditorías periódicas de vulnerabilidades para asegurar que nuestra superficie de ataque sea mínima.
            </p>
          </article>
        </div>

        {/* Botón de Contacto Rápido */}
        <div className="text-center pt-10 border-t border-slate-100">
          <p className="text-sm text-slate-400 mb-6 font-medium">
            ¿Tiene dudas sobre el tratamiento de sus datos?
          </p>
          <a 
            href="https://wa.me/573224612382?text=Hola%20Androdri%20S.A.S,%20tengo%20una%20duda%20sobre%20la%20pol%C3%ADtica%20de%20privacidad."
            target="_blank"
            rel="noopener noreferrer"
          >
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              className="bg-slate-900 text-white px-8 py-4 rounded-2xl font-bold text-sm uppercase tracking-widest hover:bg-[#2874A6] transition-colors shadow-lg"
            >
              Consultar con un Experto
            </motion.button>
          </a>
        </div>
      </section>
    </main>
  );
}

function Section({ icon, title, content }: { icon: React.ReactNode, title: string, content: string }) {
  return (
    <div className="space-y-4">
      <div className="w-12 h-12 rounded-xl bg-blue-50 flex items-center justify-center text-[#2874A6]">
        {icon}
      </div>
      <h3 className="text-xl font-bold text-slate-900">{title}</h3>
      <p className="text-slate-500 text-sm leading-relaxed">{content}</p>
    </div>
  );
}
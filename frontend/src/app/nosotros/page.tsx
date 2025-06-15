"use client";
import { motion } from "framer-motion";

export default function Nosotros() {
  return (
    <main className="min-h-screen bg-[var(--color-background)] text-[var(--color-foreground)] px-4 py-16 flex justify-center">
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, ease: "easeOut" }}
        className="max-w-5xl w-full space-y-12"
      >
        <section>
          <h2 className="text-3xl md:text-4xl font-bold text-[#2874A6] mb-4">Misión</h2>
          <p className="text-base sm:text-lg leading-relaxed text-[var(--color-foreground)]/90">
            En ANDRODRI S.A.S., nos comprometemos a desarrollar e implementar soluciones tecnológicas innovadoras y de alto impacto, adaptadas a las necesidades de nuestros clientes. A través del diseño de software a la medida, la integración de inteligencia artificial y la optimización de procesos digitales, buscamos impulsar la transformación digital en diversas industrias. Nuestra prioridad es ofrecer productos y servicios eficientes, seguros y escalables, que generen valor y contribuyan al crecimiento sostenible de nuestros clientes y aliados estratégicos.
          </p>
        </section>

        <section>
          <h2 className="text-3xl md:text-4xl font-bold text-[#2874A6] mb-4">Visión</h2>
          <p className="text-base sm:text-lg leading-relaxed text-[var(--color-foreground)]/90">
            Para el año 2030, ANDRODRI S.A.S. será una empresa líder en el desarrollo de soluciones tecnológicas innovadoras en Latinoamérica, reconocida por su excelencia en el diseño de software, la integración de inteligencia artificial y la transformación digital de negocios. Nos proyectamos como un referente en la implementación de plataformas seguras, eficientes y escalables, contribuyendo al crecimiento y evolución de empresas en múltiples sectores. A través de un enfoque basado en la innovación, la calidad y la satisfacción del cliente, consolidaremos alianzas estratégicas y expandiremos nuestra presencia en mercados internacionales.
          </p>
        </section>

        <section>
          <h2 className="text-3xl md:text-4xl font-bold text-[#2874A6] mb-4">Objetivos Generales</h2>
          <ul className="list-disc pl-6 space-y-3 text-base sm:text-lg text-[var(--color-foreground)]/90">
            <li>Desarrollar soluciones tecnológicas innovadoras que optimicen procesos y mejoren la eficiencia operativa de nuestros clientes.</li>
            <li>Consolidarnos como un referente en desarrollo de software y transformación digital en Colombia y Latinoamérica.</li>
            <li>Garantizar altos estándares de seguridad y calidad en todos nuestros productos y servicios, alineados con normativas internacionales.</li>
            <li>Fomentar la investigación y el desarrollo (I+D) para integrar nuevas tecnologías como inteligencia artificial, blockchain y analítica de datos en nuestras soluciones.</li>
            <li>Fortalecer relaciones estratégicas con clientes, aliados y empresas del sector para expandir nuestro alcance y crecimiento.</li>
          </ul>
        </section>

        <section>
          <h2 className="text-3xl md:text-4xl font-bold text-[#2874A6] mb-4">Objetivos Específicos</h2>
          <ul className="list-disc pl-6 space-y-3 text-base sm:text-lg text-[var(--color-foreground)]/90">
            <li>Diseñar e implementar plataformas web y móviles escalables para diferentes industrias.</li>
            <li>Desarrollar integraciones eficientes con pasarelas de pago, chatbots y firmas digitales para mejorar la experiencia del usuario.</li>
            <li>Implementar estrategias de seguridad informática que garanticen la protección de datos y la privacidad de los usuarios.</li>
            <li>Brindar capacitación y soporte continuo a los clientes para garantizar el uso óptimo de nuestras soluciones.</li>
            <li>Expandir nuestra presencia en el mercado internacional mediante alianzas estratégicas y la apertura de nuevas operaciones fuera de Colombia.</li>
          </ul>
        </section>
                <section>
          <h2 className="text-3xl md:text-4xl font-bold text-[#2874A6] mb-4">
            Principios Corporativos
          </h2>
          <ul className="list-disc pl-6 space-y-4 text-base sm:text-lg text-[var(--color-foreground)]/90">
            <li>
              <strong className="text-[#2874A6]">Innovación Continua 🚀</strong><br />
              Nos mantenemos a la vanguardia tecnológica, desarrollando soluciones creativas y eficientes que generen valor para nuestros clientes y la sociedad.
            </li>
            <li>
              <strong className="text-[#2874A6]">Calidad y Excelencia ✅</strong><br />
              Comprometidos con altos estándares de calidad, garantizamos productos y servicios confiables, seguros y escalables que superen las expectativas del mercado.
            </li>
            <li>
              <strong className="text-[#2874A6]">Ética y Transparencia 🤝</strong><br />
              Actuamos con honestidad, responsabilidad y compromiso, estableciendo relaciones basadas en la confianza y el respeto con nuestros clientes, aliados y colaboradores.
            </li>
            <li>
              <strong className="text-[#2874A6]">Orientación al Cliente 🎯</strong><br />
              Entendemos las necesidades de nuestros clientes y trabajamos con ellos para ofrecer soluciones personalizadas que impulsen su éxito.
            </li>
            <li>
              <strong className="text-[#2874A6]">Compromiso con la Seguridad y la Privacidad 🔐</strong><br />
              Aplicamos las mejores prácticas en seguridad de la información para proteger los datos y garantizar la confidencialidad en cada uno de nuestros proyectos.
            </li>
          </ul>
        </section>

      </motion.div>
    </main>
  );
}

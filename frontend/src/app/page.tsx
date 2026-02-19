"use client";
import { TypeAnimation } from "react-type-animation";
import dynamic from "next/dynamic";
import { motion } from "framer-motion";
import { PricingSection } from "@/components/PricingSection";


const ModelViewer = dynamic(() => import("@/components/ModelViewer"), { ssr: false });

export default function Home() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen bg-[var(--color-background)] text-[var(--color-foreground)] px-4">
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, ease: "easeOut" }}
        className="flex flex-col lg:flex-row items-center justify-between gap-12 max-w-7xl w-full text-center lg:text-left"
      >
        {/* Texto a la izquierda */}
        <div className="flex-1 space-y-6">
          <h1 className="text-4xl font-bold">
            Bienvenido a{" "}
            <span className="text-[#2874A6]">
              <TypeAnimation
                sequence={["Androdri S.A.S", 800]}
                wrapper="span"
                speed={80}
                cursor={false}
                repeat={0}
              />
            </span>
          </h1>

          <p className="text-base sm:text-lg md:text-xl text-[var(--color-foreground)]/80 leading-relaxed">
            Creamos soluciones digitales de alto impacto: apps web y móviles,
            pasarelas de pago, inteligencia artificial, dashboards, firma digital,
            ecommerce, domótica y consultoría tecnológica. Impulsamos tu
            transformación digital con innovación, experiencia y visión estratégica.
          </p>
        </div>

        {/* Modelo 3D a la derecha */}
        <div className="flex-1">
          <ModelViewer />
        </div>
      </motion.div>

      <PricingSection />

    </main>
  );
}

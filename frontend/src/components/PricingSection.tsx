"use client";

import { motion } from "framer-motion";
import Link from "next/link";

const plans = [
  {
    name: "Básico",
    price: 1871917,
    description: "Ideal para empezar a generar presencia online",
    highlight: false,
    features: [
      "Sitio web profesional (hasta 5 páginas)",
      "Diseño moderno y responsive",
      "Formulario de contacto",
      "Optimización básica SEO",
      "Carga rápida y segura",
      "Soporte inicial",
    ],
  },
  {
    name: "Profesional",
    price: 4722681,
    description: "Para negocios que quieren atraer más clientes",
    highlight: true, // 🔥 PLAN DESTACADO
    features: [
      "Todo lo del plan básico",
      "Secciones dinámicas",
      "Integración con base de datos",
      "Optimización SEO avanzada",
      "Mayor rendimiento y velocidad",
      "Preparado para escalar",
    ],
  },
  {
    name: "Enterprise",
    price: 11988345,
    description: "Soluciones completas para empresas que escalan",
    highlight: false,
    features: [
      "Todo lo del plan profesional",
      "E-commerce o sistema personalizado",
      "Integración con APIs",
      "Automatización de procesos",
      "Alta escalabilidad",
      "Soporte prioritario",
    ],
  },
];

export function PricingSection() {
  return (
    <section id="precios" className="w-full max-w-7xl mx-auto py-24 px-4">
      
      {/* 🔥 TÍTULO QUE VENDE */}
      <motion.h2
        initial={{ opacity: 0, y: 30 }}
        whileInView={{ opacity: 1, y: 0 }}
        className="text-3xl md:text-4xl font-bold text-center text-slate-900 mb-6"
      >
        Planes diseñados para hacer crecer tu negocio
      </motion.h2>

      <p className="text-center text-slate-600 mb-16 max-w-2xl mx-auto">
        No solo creamos páginas web, construimos herramientas que generan clientes y aumentan tus ventas.
      </p>

      <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
        {plans.map((plan, i) => (
          <motion.div
            key={plan.name}
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            whileHover={{ y: -10 }}
            transition={{ duration: 0.4, delay: i * 0.05 }}
            className={`relative rounded-2xl p-6 border transition ${
              plan.highlight
                ? "bg-[#2874A6] text-white shadow-2xl scale-105"
                : "bg-white border-slate-200 hover:shadow-[0_0_35px_rgba(40,116,166,0.25)]"
            }`}
          >

            {/* 🔥 BADGE DESTACADO */}
            {plan.highlight && (
              <span className="absolute top-4 right-4 bg-white text-[#2874A6] text-xs px-3 py-1 rounded-full font-bold">
                Más popular
              </span>
            )}

            <h3 className="text-xl font-semibold mb-2">
              {plan.name}
            </h3>

            <p className="text-sm mb-4 opacity-80">
              {plan.description}
            </p>

            <div className="mb-6">
              <span className="text-4xl font-bold">
                {new Intl.NumberFormat("es-CO", {
                  style: "currency",
                  currency: "COP",
                  minimumFractionDigits: 0,
                }).format(plan.price)}
              </span>

              <span className="text-sm opacity-70">
                {" "} / inversión anual
              </span>
            </div>

            <ul className="space-y-3 text-sm mb-10">
              {plan.features.map((feature) => (
                <li key={feature} className="flex gap-2">
                  <span className="font-bold">✓</span>
                  {feature}
                </li>
              ))}
            </ul>

            {/* 🔥 CTA MEJORADO */}
            <Link href="/contacto" className="w-full">
              <button
                className={`w-full rounded-xl py-3 font-medium transition ${
                  plan.highlight
                    ? "bg-white text-[#2874A6] hover:scale-105"
                    : "border border-[#2874A6] text-[#2874A6] hover:bg-[#2874A6] hover:text-white"
                }`}
              >
                {plan.highlight ? "Empezar ahora" : "Solicitar información"}
              </button>
            </Link>

          </motion.div>
        ))}
      </div>
    </section>
  );
}
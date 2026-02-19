"use client";

import { motion } from "framer-motion";
import Link from "next/link";

const plans = [
  {
    name: "Servicios Premium",
    price: 1871917,
    description: "Página web 5 pantallas estáticas",
    features: [
      "Reuniones por Meet",
      "Análisis y Diseño",
      "Desarrollo Web,Pruebas $508.800 COP Anual",
      "Implementación Hosting $1.017.600 COP Anual",
      "Implementación Dominio $46.640 COP Anual",
      "Mails de notificación Mail Free 20 mensual",
      "Entregas del proyecto de 4 a 8 Semanas",
      "Iva $298.877 COP Anual",
    ],
  },
  {
    name: "Servicios VIP",
    price: 4722681,
    description: "Página web 5 pantallas estáticas + 5 dinámicas",
    features: [
      "Reuniones por Meet",
      "Análisis y Diseño",
      "Desarrollo Web,Pruebas $508.800 COP Anual",
      "Implementación Hosting $1.017.600 COP Anual",
      "Implementación Dominio $46.640 COP Anual",
      "Mails de notificación Mail $763.200 COP Anual",
      "Base de datos Mysql $1.017.600,00 COP Anual Variable",
      "S3 imagenes y Videos $101.760,00 COP Anual Variable",
      "Iva $ 754.041 COP Anual",
    ],
  },
  {
    name: "Servicios luxury",
    price: 11988345,
    description: "Página web 5 pantallas estáticas + 5 dinámicas + Facturación + E-commerce",
    features: [
      "Reuniones por Meet",
      "Análisis y Diseño",
      "Desarrollo Web,Pruebas $508.800 COP Anual",
      "Implementación Hosting $1.017.600 COP Anual",
      "Implementación Dominio $46.640 COP Anual",
      "Mails de notificación Mail $763.200 COP Anual",
      "Base de datos Mysql $1.017.600 COP Anual Variable",
      "S3 imagenes y Videos $101.760 COP Anual Variable",
      "Facturación 3.052.800,00 COP Anual Variable",
      "E-comers 3.052.800,00 COP Anual Variable",
      "Iva $ 1.914.105,60 COP Anual",
    ],
  },
];

export function PricingSection() {
  return (
    <section className="w-full max-w-7xl mx-auto py-24 px-4">
      <motion.h2
        initial={{ opacity: 0, y: 30 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 0.6 }}
        className="text-3xl md:text-4xl font-bold text-center text-slate-900 mb-16"
      >
        Servicios planes diseñados Para tu Empresa
      </motion.h2>

      <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
        {plans.map((plan, i) => (
          <motion.div
            key={plan.name}
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            whileHover={{ y: -10 }}
            transition={{ duration: 0.4, delay: i * 0.05 }}
            className="relative rounded-2xl p-6 bg-white border border-slate-200 hover:shadow-[0_0_35px_rgba(40,116,166,0.25)] transition"
          >
            <h3 className="text-xl font-semibold text-slate-900 mb-2">
              {plan.name}
            </h3>

            <p className="text-sm text-slate-600 mb-4">
              {plan.description}
            </p>

            <div className="mb-6">
              <span className="text-4xl font-bold text-slate-900">
  {new Intl.NumberFormat("es-CO", {
    style: "currency",
    currency: "COP",
    minimumFractionDigits: 0,
  }).format(plan.price )}
</span>

              <span className="text-sm text-slate-500"> / Anual con Iva Incluido</span>
            </div>

            <ul className="space-y-3 text-sm text-slate-700 mb-10">
              {plan.features.map((feature) => (
                <li key={feature} className="flex gap-2">
                  <span className="text-[#2874A6] font-bold">✓</span>
                  {feature}
                </li>
              ))}
            </ul>

            <Link href="/contacto" className="w-full">
  <button
    className="w-full rounded-xl py-3 font-medium text-[#2874A6] border border-[#2874A6]
               hover:bg-[#2874A6] hover:text-white transition"
  >
    Contáctanos
  </button>
</Link>

          </motion.div>
        ))}
      </div>
    </section>
  );
}

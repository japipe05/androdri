import type { Config } from "tailwindcss";

const config: Config = {
  // 1. Aseguramos que rastree todos los archivos para no perder estilos
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  darkMode: "media", // O 'class' si prefieres un switch manual
  theme: {
    extend: {
      colors: {
        // Definimos el azul de marca para usarlo como 'text-brand' o 'bg-brand'
        brand: "#2874A6",
        // Colores de fondo dinámicos
        darkBg: "#000000",
        lightBg: "#FFFFFF",
      },
      fontFamily: {
        // Vinculamos con las variables de Next.js que configuramos en el layout
        sans: ["var(--font-ubuntu)", "ui-sans-serif", "system-ui"],
        mono: ["var(--font-geist-mono)", "ui-monospace", "SFMono-Regular"],
      },
      // 2. TIPOGRAFÍA FLUIDA: Aquí ocurre la magia del "agrandar y empequeñecer"
      // Usamos clamp(mínimo, preferido, máximo) para que sea responsive sin media queries
      fontSize: {
        "fluid-h1": ["clamp(2.5rem, 8vw, 5rem)", { lineHeight: "1.1", fontWeight: "800" }],
        "fluid-h2": ["clamp(2rem, 5vw, 3.5rem)", { lineHeight: "1.2", fontWeight: "700" }],
        "fluid-body": ["clamp(1rem, 1.2vw, 1.25rem)", { lineHeight: "1.6" }],
        "fluid-small": ["clamp(0.8rem, 1vw, 1rem)", { lineHeight: "1.5" }],
      },
      // 3. Puntos de ruptura (breakpoints) para pantallas extra grandes
      screens: {
        '3xl': '1920px',
      },
      // 4. Animaciones para el factor "Awesome" (innovación visual)
      animation: {
        'slow-fade': 'fadeIn 1.5s ease-in-out',
        'float': 'float 6s ease-in-out infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(10px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-20px)' },
        }
      },
    },
  },
  plugins: [],
};

export default config;
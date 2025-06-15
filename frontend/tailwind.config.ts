// tailwind.config.ts
const config = {
  content: ["./src/**/*.{ts,tsx}"], // ✅ Ruta real en disco, no alias
  theme: {
    extend: {
      colors: {
        hoverBlue: "#2874A6",
      },
    },
  },
  plugins: [],
};

export default config;

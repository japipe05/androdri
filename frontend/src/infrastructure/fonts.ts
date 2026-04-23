import { Ubuntu, Geist_Mono } from "next/font/google";

const ubuntu = Ubuntu({
  subsets: ["latin"],
  weight: ["400", "700"], // Evita pesos que no uses para ahorrar KBs
  variable: "--font-ubuntu",
  display: 'swap', // Evita el "Flash of Unstyled Text"
});

const geist = Geist_Mono({
  subsets: ["latin"],
  variable: "--font-geist-mono",
  display: 'swap',
});

export const fonts = { ubuntu, geist };
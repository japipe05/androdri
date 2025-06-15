"use client";
import Link from "next/link";
import { useState } from "react";
import { Menu, X } from "lucide-react";

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const navLinkStyle =
    "relative hover:text-[#2874A6] transition-colors after:content-[''] after:absolute after:left-0 after:-bottom-1 after:h-[2px] after:w-0 after:bg-[#2874A6] after:transition-all after:duration-300 hover:after:w-full";

  return (
    <nav className="bg-primary p-6 shadow-md">
      <div className="container mx-auto flex items-center justify-between">
        <h1 className="text-2xl md:text-3xl font-extrabold">Androdri S.A.S</h1>
        <button onClick={() => setIsOpen(!isOpen)} className="md:hidden">
          {isOpen ? <X /> : <Menu />}
        </button>
        <ul className="hidden md:flex gap-8 text-lg font-medium">
          <li><Link className={navLinkStyle} href="/">Inicio</Link></li>
          <li><Link className={navLinkStyle} href="/nosotros">Nosotros</Link></li>
          <li><Link className={navLinkStyle} href="/contacto">Contacto</Link></li>
        </ul>
      </div>

      {isOpen && (
        <ul className="flex flex-col mt-4 gap-4 text-lg font-medium md:hidden">
          <li><Link className={navLinkStyle} href="/">Inicio</Link></li>
          <li><Link className={navLinkStyle} href="/nosotros">Nosotros</Link></li>
          <li><Link className={navLinkStyle} href="/contacto">Contacto</Link></li>
        </ul>
      )}
    </nav>
  );
};

export default Navbar;

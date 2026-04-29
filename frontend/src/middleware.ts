import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  const nonce = Buffer.from(crypto.randomUUID()).toString("base64");
  const isDev = process.env.NODE_ENV === "development";
  
  const scriptSrc = [
    "'self'",
    `'nonce-${nonce}'`,
    "'strict-dynamic'",
    "https://www.googletagmanager.com",
    "https://www.google-analytics.com",
    isDev ? "'unsafe-eval' 'unsafe-inline'" : "", 
  ].filter(Boolean).join(" ");

  const connectSrc = [
    "'self'",
    "blob:",
    "data:",
    "https://androdri.com",
    "https://www.androdri.com",
    "https://www.google-analytics.com",
    "https://cdn.jsdelivr.net",
    "https://raw.githack.com",
    "https://cloudflare-ipfs.com",
    "https://raw.githubusercontent.com", // <--- AGREGADO PARA EL ARCHIVO .HDR
    isDev ? "ws://localhost:3000 http://localhost:3000" : "", 
  ].filter(Boolean).join(" ");

  const imgOrSceneSrc = [
    "'self'",
    "https://androdri.com",
    "https://www.androdri.com",
    "data:",
    "blob:",
    "https:",
    "https://cdn.jsdelivr.net",
    "https://cloudflare-ipfs.com",
    "https://raw.githubusercontent.com", // <--- TAMBIÉN PARA TEXTURAS
  ].join(" ");

  const cspHeader = `
    default-src 'self';
    script-src ${scriptSrc};
    style-src 'self' 'unsafe-inline';
    img-src ${imgOrSceneSrc};
    font-src 'self' data:;
    connect-src ${connectSrc};
    worker-src 'self' blob:;
    frame-src https://www.googletagmanager.com;
    object-src 'none';
    base-uri 'self';
    form-action 'self';
    ${isDev ? "" : "upgrade-insecure-requests;"}
  `.replace(/\s{2,}/g, " ").trim();

  const requestHeaders = new Headers(request.headers);
  requestHeaders.set("x-nonce", nonce);
  requestHeaders.set("Content-Security-Policy", cspHeader);

  const response = NextResponse.next({
    request: { headers: requestHeaders },
  });

  response.headers.set("Content-Security-Policy", cspHeader);
  response.headers.set("X-Content-Type-Options", "nosniff");
  response.headers.set("X-Frame-Options", "DENY");
  response.headers.set("Referrer-Policy", "strict-origin-when-cross-origin");

  return response;
}

export const config = {
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico).*)"],
};
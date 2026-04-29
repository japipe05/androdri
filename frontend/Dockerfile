# ---------- Builder ----------
FROM node:20-alpine AS builder

WORKDIR /app

# Necesario para algunas dependencias nativas
RUN apk add --no-cache libc6-compat

COPY package.json package-lock.json* ./

RUN --mount=type=cache,target=/root/.npm \
    npm ci --prefer-offline --no-audit --progress=false

COPY . .

# --- VARIABLES DE ENTORNO PARA EL BUILD ---
# Definimos los argumentos que recibiremos desde el comando de build o Dokploy
ARG NEXT_PUBLIC_WHATSAPP_NUMBER
ARG NEXT_PUBLIC_FACEBOOK
ARG NEXT_PUBLIC_INSTAGRAM
ARG NEXT_PUBLIC_LINKEDIN
ARG NEXT_PUBLIC_TIKTOK
ARG NEXT_PUBLIC_YOUTUBE
ARG NEXT_PUBLIC_MAILCOPORATIVO

# Las convertimos en variables de entorno para que Next.js las vea al compilar
ENV NEXT_PUBLIC_WHATSAPP_NUMBER=$NEXT_PUBLIC_WHATSAPP_NUMBER \
    NEXT_PUBLIC_FACEBOOK=$NEXT_PUBLIC_FACEBOOK \
    NEXT_PUBLIC_INSTAGRAM=$NEXT_PUBLIC_INSTAGRAM \
    NEXT_PUBLIC_LINKEDIN=$NEXT_PUBLIC_LINKEDIN \
    NEXT_PUBLIC_TIKTOK=$NEXT_PUBLIC_TIKTOK \
    NEXT_PUBLIC_YOUTUBE=$NEXT_PUBLIC_YOUTUBE \
    NEXT_PUBLIC_MAILCOPORATIVO=$NEXT_PUBLIC_MAILCOPORATIVO

# Ahora ejecutamos el build con las variables inyectadas
RUN npm run build


# ---------- Runner ----------
FROM node:20-alpine AS runner

WORKDIR /app
# Importante para optimizaciones de Next.js
ENV NODE_ENV=production

RUN addgroup -S nextjs && adduser -S nextjs -G nextjs

# Copiamos solo lo necesario del modo standalone
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static
COPY --from=builder /app/public ./public

USER nextjs

EXPOSE 3000

# Variable que puede cambiar en tiempo de ejecución (no necesita NEXT_PUBLIC)
ENV PORT=3000
ENV HOSTNAME="0.0.0.0"

CMD ["node", "server.js"]
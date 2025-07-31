# Etapa 1: Build
FROM node:20-alpine AS builder

WORKDIR /app

# Recibe argumentos desde Railway
ARG NEXT_PUBLIC_CONTACT_API_URL

# Expone variables para que estén disponibles en el build
ENV NEXT_PUBLIC_CONTACT_API_URL=$NEXT_PUBLIC_CONTACT_API_URL

# Copia los archivos necesarios para instalar dependencias
COPY package.json package-lock.json* ./ 
COPY tsconfig.json ./ 
COPY tailwind.config.* postcss.config.* ./

# Instala dependencias (dev y prod)
RUN npm install

# Copia el resto del código fuente
COPY . .

# Transpila next.config.ts a next.config.js (requerido para producción)
RUN npx tsx --no-warnings ./next.config.ts > next.config.js

# Build de la app Next.js (modo producción)
RUN npm run build

# Etapa 2: Producción
FROM node:20-alpine AS runner

WORKDIR /app

# Copia solo lo necesario para producción
COPY --from=builder /app/package.json ./
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/next.config.js ./next.config.js

# Expone el puerto usado por la app
EXPOSE 3002

# Comando para iniciar la app en modo producción
CMD ["npm", "start"]

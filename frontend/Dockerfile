# Etapa 1: Build
FROM node:20 AS builder

WORKDIR /app

ARG NEXT_PUBLIC_CONTACT_API_URL
ENV NEXT_PUBLIC_CONTACT_API_URL=$NEXT_PUBLIC_CONTACT_API_URL

COPY package*.json ./
RUN npm install
COPY . .

RUN npm run build

# Etapa 2: Producción
FROM node:20-slim

WORKDIR /app
COPY --from=builder /app ./

ENV NODE_ENV=production
EXPOSE 3000
CMD ["npm", "start"]

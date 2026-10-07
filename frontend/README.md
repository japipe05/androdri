# intalar dependencias
npm install

# ejecutar en local
npm run dev

# crear red
docker network create androdri-net


#2874a6 azul
#17202a negro

3d
https://sketchfab.com/3d-models/cute-robot-companion-glb-0f64197efce74fba8145b941efea323a

## .env

### 📦 variables de entorno

```bash

#local
#EMAIL_API_URL=
NEXT_PUBLIC_WHATSAPP_NUMBER=
#docker
EMAIL_API_URL=
#desa railway
#EMAIL_API_URL="
#produccion 
EMISOR_EMAIL=
EMAIL_API_KEY=

NEXT_PUBLIC_FACEBOOK=
NEXT_PUBLIC_INSTAGRAM=
NEXT_PUBLIC_LINKEDIN=
NEXT_PUBLIC_TIKTOK=
NEXT_PUBLIC_YOUTUBE=
NEXT_PUBLIC_MAILCOPORATIVO=
```

## 🐳 Despliegue con Docker

### 📦 Construcción de imágenes

```bash


docker build `
  --build-arg NEXT_PUBLIC_WHATSAPP_NUMBER="573224612382" `
  --build-arg NEXT_PUBLIC_MAILCOPORATIVO="servicios@androdri.com" `
  --build-arg NEXT_PUBLIC_FACEBOOK="https://www.facebook.com/profile.php?id=61588715758897" `
  --build-arg NEXT_PUBLIC_INSTAGRAM="https://www.instagram.com/androdrisas/" `
  --build-arg NEXT_PUBLIC_LINKEDIN="https://www.linkedin.com/in/androdri-s-a-s-arquitectura-de-activos-digitales-de-%C3%A9lite-132a9b405/" `
  --build-arg NEXT_PUBLIC_TIKTOK="https://www.tiktok.com/@androdri_" `
  --build-arg NEXT_PUBLIC_YOUTUBE="https://www.youtube.com/@androdri05" `
  -t japipe05/androdri-frontend:1.0.0-prod .

docker push japipe05/androdri-frontend:1.0.0-prod

docker run -d `
  --name androdri-frontend `
  --env-file .env `
  -p 3000:3000  `
  japipe05/androdri-frontend:1.0.0-prod

```

# Seguridad

```bash
npm audit fix
npm install next@15.5.15
npm run dev -- -p 7001  
```
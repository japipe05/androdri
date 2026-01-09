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




## 🐳 Despliegue con Docker

### 📦 Construcción de imágenes

```bash
docker build -t japipe05/androdri-frontend:1.0.0-prod .

docker push japipe05/androdri-frontend:1.0.0-prod
```

HELLO_MESSAGE=Hola desde el servidor local
NEXT_PUBLIC_HELLO_MESSAGE=Hola desde el frontend local

---
### ▶️ Ejecución local

```bash
docker run -d `
  --name androdri-frontend `
  --env-file .env `
  --network androdri-net `
  -p 3000:3000  `
  japipe05/androdri-frontend:1.0.0-prod

```


docker run -p 3000:3000 \
  -e TOKEN_URL="https://api.example.com/token" \
  -e EMAIL_URL="https://api.example.com/send" \
  -e EMAIL_API_KEY="super-secret-key" \
  japipe05/androdri-frontend:1.0.0-prod




despues del WORKDIR /app
# Recibe argumentos desde Railway
ARG NEXT_PUBLIC_HELLO_MESSAGE

# Expone variables para que estén disponibles en el build
ENV NEXT_PUBLIC_HELLO_MESSAGE=$NEXT_PUBLIC_HELLO_MESSAGE

```bash
docker build `
  --build-arg NEXT_PUBLIC_HELLO_MESSAGE="Hola desde el frontend local 2" `
  -t japipe05/next-hello-world:1.0.0-prod .

docker push japipe05/next-hello-world:1.0.0-prod

docker run -d `
  --name next-hello-world `
  -p 3000:3000  `
  japipe05/next-hello-world:1.0.0-prod
  
```



  
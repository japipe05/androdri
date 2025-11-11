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
docker build -t japipe05/androdri-frontend:dev-v1.0.0-20251107 .
docker push japipe05/androdri-frontend:dev-v1.0.0-20251107
```

---

### ▶️ Ejecución local

```bash
docker run -d `
  --name androdri-frontend `
  --env-file .env `
  --network androdri-net `
  -p 3000:3000  `
  japipe05/androdri-frontend:dev-v1.0.0-20251107

```

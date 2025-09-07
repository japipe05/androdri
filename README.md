# Ejecutar la aplicacion de python
python -m uvicorn app.main:app --reload
# Ejecutar aplicacion en nextjs
npm run dev


> docker builder prune --all
docker login

# Desarrollo
docker build -t japipe05/androdri-backend:dev ./backend
docker build -t japipe05/androdri-frontend:dev ./frontend

# Test
docker build -t japipe05/androdri-backend:test ./backend
docker build -t japipe05/androdri-frontend:test ./frontend

# Producción (usa versión semántica)
docker build -t japipe05/androdri-backend:v1.0.0 ./backend

docker build `
--build-arg NEXT_PUBLIC_CONTACT_API_URL="https://api.androdri.com" `
-t japipe05/androdri-frontend:v1.0.0 `
./frontend


# Desarrollo
docker push japipe05/androdri-backend:dev
docker push japipe05/androdri-frontend:dev

# Test
docker push japipe05/androdri-backend:test
docker push japipe05/androdri-frontend:test

# Producción
docker push japipe05/androdri-backend:v1.0.0
docker push japipe05/androdri-frontend:v1.0.0


# androdri
> docker-compose up --build -d
#!/bin/bash

# 🚀 Configura aquí tu usuario de Docker Hub
DOCKER_USER=japipe05

# 📦 Nombres de las imágenes
FRONTEND_IMAGE=androdri-frontend
BACKEND_IMAGE=androdri-backend

echo "🔐 Iniciando proceso de despliegue..."

# 🏗️ 1. Construir imágenes
echo "🔧 Construyendo imagen del frontend..."
docker build -t $DOCKER_USER/$FRONTEND_IMAGE:latest ./frontend

echo "🔧 Construyendo imagen del backend..."
docker build -t $DOCKER_USER/$BACKEND_IMAGE:latest ./Backend

# 🐳 2. Hacer push a Docker Hub
echo "🚀 Subiendo $FRONTEND_IMAGE a Docker Hub..."
docker push $DOCKER_USER/$FRONTEND_IMAGE:latest

echo "🚀 Subiendo $BACKEND_IMAGE a Docker Hub..."
docker push $DOCKER_USER/$BACKEND_IMAGE:latest

echo "✅ Despliegue completado exitosamente."

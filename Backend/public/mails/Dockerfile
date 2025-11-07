# ==========================================================
# 🐍 Etapa 1: Build - instalación de dependencias
# ==========================================================
FROM python:3.11-slim AS builder

# Desactivar buffer de salida y asegurar UTF-8
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    LANG=C.UTF-8

# Crear directorio de la app
WORKDIR /app

# Copiar requerimientos e instalarlos
COPY requirements.txt .

# Instalar dependencias en un directorio temporal (para reducir tamaño final)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ==========================================================
# 🏗️ Etapa 2: Runtime - contenedor final más liviano
# ==========================================================
FROM python:3.11-slim

# Variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    LANG=C.UTF-8

# Crear usuario no root por seguridad
RUN adduser --disabled-password --gecos '' fastapiuser

WORKDIR /app

# Copiar dependencias desde builder
COPY --from=builder /usr/local /usr/local

# Copiar el código fuente
COPY . .

# Dar permisos a logs, tmp, etc.
RUN mkdir -p /app/tmp && chown -R fastapiuser:fastapiuser /app

# Cambiar usuario
USER fastapiuser

# Exponer puerto FastAPI
EXPOSE 8000

# Comando por defecto (Uvicorn)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

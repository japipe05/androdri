# =======================================================
# Etapa 1: Build - instala dependencias
# =======================================================
FROM python:3.13-slim AS builder

WORKDIR /app

# Instalar dependencias de sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# =======================================================
# Etapa 2: Runtime - contenedor liviano para producción
# =======================================================
FROM python:3.13-slim

WORKDIR /app

# Copiar dependencias desde el builder
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copiar tu aplicación FastAPI
COPY app ./app

# Variables de entorno
ENV PYTHONUNBUFFERED=1
ENV TZ=America/Bogota

# Exponer puerto
EXPOSE 8000

# Comando principal
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

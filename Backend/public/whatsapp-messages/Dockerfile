# Dockerfile
FROM python:3.13.9-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Copiamos archivos de configuración
COPY ./requirements.txt /app/requirements.txt

# Instalamos dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiamos el código fuente
COPY ./app /app/app
COPY .env /app/.env

# Exponemos el puerto
EXPOSE 8000

# Comando por defecto
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

@echo off
setlocal

echo.
echo ==========================================
echo   DESPLIEGUE BACKEND ANDRODRI
echo ==========================================
echo.

echo [1/4] Deteniendo contenedor anterior...
docker stop androdri-backend >nul 2>&1

echo [2/4] Eliminando contenedor anterior...
docker rm androdri-backend >nul 2>&1

echo [3/4] Construyendo imagen...
docker build -t japipe05/androdri-backend:1.0.0-prod ./Backend

if errorlevel 1 (
    echo ERROR: Fallo la construccion de la imagen.
    exit /b 1
)

echo [4/4] Subiendo imagen a Docker Hub...
docker push japipe05/androdri-backend:1.0.0-prod

if errorlevel 1 (
    echo ERROR: Fallo el push a Docker Hub.
    exit /b 1
)

echo.
echo Iniciando nuevo contenedor...

docker run -d ^
  --name androdri-backend ^
  --env-file ./Backend/.env ^
  -p 8000:8000 ^
  japipe05/androdri-backend:1.0.0-prod

if errorlevel 1 (
    echo ERROR: Fallo al iniciar el contenedor.
    exit /b 1
)

echo.
echo ==========================================
echo   DESPLIEGUE COMPLETADO CON EXITO
echo ==========================================
echo.

docker ps --filter "name=androdri-backend"

echo.
echo ==========================================
echo    DESPLIEGUE FRONTEND ANDRODRI
echo ==========================================
echo.

echo [1/5] Deteniendo contenedor anterior...

docker stop androdri-frontend >nul 2>&1

echo [2/5] Eliminando contenedor anterior...

docker rm androdri-frontend >nul 2>&1

echo [3/5] Construyendo imagen...

docker build ^
  --build-arg NEXT_PUBLIC_WHATSAPP_NUMBER="573224612382" ^
  --build-arg NEXT_PUBLIC_MAILCOPORATIVO="servicios@androdri.com" ^
  --build-arg NEXT_PUBLIC_FACEBOOK="https://www.facebook.com/profile.php?id=61588715758897" ^
  --build-arg NEXT_PUBLIC_INSTAGRAM="https://www.instagram.com/androdrisas/" ^
  --build-arg NEXT_PUBLIC_LINKEDIN="https://www.linkedin.com/in/androdri-s-a-s-arquitectura-de-activos-digitales-de-%C3%A9lite-132a9b405/" ^
  --build-arg NEXT_PUBLIC_TIKTOK="https://www.tiktok.com/@androdri_" ^
  --build-arg NEXT_PUBLIC_YOUTUBE="https://www.youtube.com/@androdri05" ^
  -t japipe05/androdri-frontend:1.0.0-prod ./frontend

if errorlevel 1 (
    echo ERROR: Fallo la construccion de la imagen.
    exit /b 1
)

echo [4/5] Subiendo imagen a Docker Hub...

docker push japipe05/androdri-frontend:1.0.0-prod

if errorlevel 1 (
    echo ERROR: Fallo el push a Docker Hub.
    exit /b 1
)

echo.

echo [5/5] Iniciando nuevo contenedor...

docker run -d ^
  --name androdri-frontend ^
  --env-file frontend\.env ^
  -p 3000:3000 ^
  japipe05/androdri-frontend:1.0.0-prod

if errorlevel 1 (
    echo ERROR: Fallo al iniciar el contenedor.
    exit /b 1
)

echo.

echo ==========================================
echo    DESPLIEGUE COMPLETADO CON EXITO
echo ==========================================
echo.

docker ps --filter "name=androdri-frontend"

echo.

endlocal
"""
===============================================================================
Archivo:        rate_limiter.py
Ubicación:      app/utils/rate_limiter.py
Descripción:    Implementa un sistema de limitación de tasa (rate limiting) 
                basado en ventana deslizante (sliding window) en memoria.
                Controla la frecuencia de solicitudes por dirección IP del cliente,
                con el objetivo de evitar abusos o sobrecarga del sistema.
Autor:          Andres Felipe Rodriguez Roa
Fecha:          2025/06/11
Radicado:       v0006af
===============================================================================
"""

import time
from fastapi import HTTPException, status, Request
from typing import Dict, List
from app.config.settings import settings

# ------------------------------------------------------------------------------
# Estructura en memoria para almacenar los timestamps de las solicitudes
# por cada IP del cliente. En producción se recomienda usar Redis o una
# base de datos compartida para persistencia y escalabilidad.
# ------------------------------------------------------------------------------
_store: Dict[str, List[int]] = {}


# ------------------------------------------------------------------------------
# Función: check_rate_limit
# ------------------------------------------------------------------------------
def check_rate_limit(request: Request) -> None:
    """
    Aplica una política de **rate limiting** basada en ventana deslizante.

    ### Descripción
    Esta función evalúa la cantidad de solicitudes realizadas por una misma IP
    dentro de un intervalo de tiempo configurable. Si el número de solicitudes
    excede el máximo permitido, se lanza una excepción HTTP `429 Too Many Requests`.

    El mecanismo usa una **ventana deslizante (sliding window)**:  
    cada vez que llega una solicitud, se eliminan los timestamps más antiguos
    fuera del rango temporal y se registra el nuevo.

    ### Parámetros
    - **request** (`Request`): Objeto de FastAPI que permite obtener la IP del cliente.

    ### Configuración utilizada
    - `settings.RATE_LIMIT_WINDOW_SECONDS` → Duración de la ventana de tiempo (segundos)
    - `settings.RATE_LIMIT_MAX` → Cantidad máxima de solicitudes permitidas por IP en la ventana

    ### Excepciones
    - **HTTP 429 Too Many Requests** → Si el cliente excede el límite establecido.

    ### Ejemplo de uso
    ```python
    from fastapi import Request
    from app.utils.rate_limiter import check_rate_limit

    @app.get("/data")
    async def get_data(request: Request):
        check_rate_limit(request)
        return {"data": "ok"}
    ```

    ### Ejemplo de mensaje de error
    ```json
    {
        "detail": "Rate limit exceeded: max 10 requests per 60 seconds"
    }
    ```

    ### Nota técnica
    ⚠️ Este limitador es **in-memory**, por lo que:
    - No es adecuado para múltiples instancias de aplicación (no es distribuido)
    - Se reinicia al reiniciar el proceso
    - Para producción, se recomienda usar **Redis** o un **cache distribuido**
    """
    # Obtener IP del cliente (best-effort)
    client_host = request.client.host if request.client else "unknown"

    # Timestamp actual y límite inferior de la ventana
    now = int(time.time())
    window_start = now - settings.RATE_LIMIT_WINDOW_SECONDS

    # Recuperar o inicializar el historial de timestamps de la IP
    hits = _store.get(client_host, [])

    # Filtrar solicitudes dentro de la ventana activa
    hits = [t for t in hits if t >= window_start]
    hits.append(now)

    # Actualizar el almacenamiento
    _store[client_host] = hits

    # Verificar si excede el límite
    if len(hits) > settings.RATE_LIMIT_MAX:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=(
                f"Rate limit exceeded: max {settings.RATE_LIMIT_MAX} "
                f"requests per {settings.RATE_LIMIT_WINDOW_SECONDS} seconds"
            ),
        )

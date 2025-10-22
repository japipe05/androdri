# app/utils/rate_limiter.py
import time
from fastapi import HTTPException, status
from app.config.settings import settings

requests_log = {}

def check_rate_limit(client_id: str):
    now = time.time()
    requests = requests_log.get(client_id, [])
    
    requests = [req for req in requests if now - req < settings.RATE_LIMIT_WINDOW_SECONDS]
    
    if len(requests) >= settings.RATE_LIMIT_MAX:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Demasiadas solicitudes. Espera {settings.RATE_LIMIT_WINDOW_SECONDS} segundos."
        )
    
    requests.append(now)
    requests_log[client_id] = requests

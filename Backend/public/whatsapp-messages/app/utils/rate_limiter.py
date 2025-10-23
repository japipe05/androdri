
# ------------------------
# File: app/utils/rate_limiter.py
# ------------------------
import time
from fastapi import HTTPException, status, Request
from app.config.settings import settings
from typing import Dict, List

# Simple in-memory sliding window limiter per client IP.
# NOTE: in production use Redis / shared store to work across processes/instances.

_store: Dict[str, List[int]] = {}

def check_rate_limit(request: Request) -> None:
    # Get client IP - best-effort
    client_host = request.client.host if request.client else "unknown"
    now = int(time.time())
    window_start = now - settings.RATE_LIMIT_WINDOW_SECONDS
    hits = _store.get(client_host, [])
    # Keep only timestamps inside the window
    hits = [t for t in hits if t >= window_start]
    hits.append(now)
    _store[client_host] = hits
    if len(hits) > settings.RATE_LIMIT_MAX:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded: max {settings.RATE_LIMIT_MAX} requests per {settings.RATE_LIMIT_WINDOW_SECONDS} seconds",
        )

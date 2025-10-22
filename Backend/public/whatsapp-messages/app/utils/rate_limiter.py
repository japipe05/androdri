# app/utils/rate_limiter.py
from fastapi import Request, HTTPException, status, Depends
from time import time
from typing import Dict, List
from app.config.settings import get_settings

settings = get_settings()

# In-memory store: {client_id: [timestamps...]}
_RATE_STORE: Dict[str, List[float]] = {}

def _cleanup_old(timestamps: List[float], window: int) -> List[float]:
    cutoff = time() - window
    return [ts for ts in timestamps if ts > cutoff]

def rate_limit_dependency(request: Request):
    """
    Limit requests per client identifier (by IP) to settings.RATE_LIMIT_MAX per settings.RATE_LIMIT_WINDOW_SECONDS.
    NOTE: This is an in-memory implementation — for multi-process deployments use Redis or other central store.
    """
    client_host = "unknown"
    if request.client:
        client_host = request.client.host

    key = client_host

    timestamps = _RATE_STORE.get(key, [])
    timestamps = _cleanup_old(timestamps, settings.RATE_LIMIT_WINDOW_SECONDS)

    if len(timestamps) >= settings.RATE_LIMIT_MAX:
        # compute retry-after
        earliest = min(timestamps)
        retry_after = int((earliest + settings.RATE_LIMIT_WINDOW_SECONDS) - time())
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Retry after {retry_after} seconds."
        )

    timestamps.append(time())
    _RATE_STORE[key] = timestamps

    # Add headers for diagnostics via response middleware? Here can't mutate response easily, but it's ok.
    return True

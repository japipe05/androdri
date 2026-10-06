import asyncio
import math
import time
from collections import deque
from collections.abc import Callable

from app.application.ports import RateLimitDecision

_PURGE_THRESHOLD = 10_000


class InMemorySlidingWindowRateLimiter:
    """Ventana deslizante: máx. `max_requests` por `window_seconds` para cada clave.

    Con 3 envíos / 3600 s: tras el 3er correo, el 4º se bloquea hasta que el
    primero cumpla 1 hora. Es por proceso; con varios workers/instancias usa
    una implementación Redis del mismo puerto (RateLimiterPort).
    """

    def __init__(
        self,
        max_requests: int,
        window_seconds: int,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        self._max = max_requests
        self._window = window_seconds
        self._clock = clock
        self._hits: dict[str, deque[float]] = {}
        self._lock = asyncio.Lock()

    async def acquire(self, key: str) -> RateLimitDecision:
        async with self._lock:
            now = self._clock()
            if len(self._hits) > _PURGE_THRESHOLD:
                self._purge(now)
            hits = self._hits.setdefault(key, deque())
            self._prune(hits, now)

            if len(hits) >= self._max:
                retry_after = max(1, math.ceil(hits[0] + self._window - now))
                return RateLimitDecision(False, 0, retry_after)

            hits.append(now)
            return RateLimitDecision(True, self._max - len(hits), 0)

    async def release(self, key: str) -> None:
        async with self._lock:
            hits = self._hits.get(key)
            if hits:
                hits.pop()
                if not hits:
                    del self._hits[key]

    def _prune(self, hits: deque[float], now: float) -> None:
        while hits and hits[0] <= now - self._window:
            hits.popleft()

    def _purge(self, now: float) -> None:
        for key in list(self._hits):
            self._prune(self._hits[key], now)
            if not self._hits[key]:
                del self._hits[key]

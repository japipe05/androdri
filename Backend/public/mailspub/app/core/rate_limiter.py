from datetime import datetime, timedelta
from collections import defaultdict


class InMemoryRateLimiter:
    def __init__(self):
        self.requests = defaultdict(list)

    def is_allowed(self, key: str, limit: int = 5, period: int = 3600) -> bool:
        now = datetime.utcnow()
        window_start = now - timedelta(seconds=period)

        self.requests[key] = [
            timestamp for timestamp in self.requests[key]
            if timestamp > window_start
        ]

        if len(self.requests[key]) >= limit:
            return False

        self.requests[key].append(now)
        return True

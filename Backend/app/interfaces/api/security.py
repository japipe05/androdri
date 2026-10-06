from fastapi import FastAPI, Request


def register_security_headers(app: FastAPI, is_production: bool) -> None:
    @app.middleware("http")
    async def security_headers(request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["Cache-Control"] = "no-store"
        if is_production:  # en desarrollo se omite para no romper /docs
            response.headers["Content-Security-Policy"] = "default-src 'none'; frame-ancestors 'none'"
            response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        return response

from fastapi import Request
from loguru import logger
import time


def add_logging_middleware(app):
    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        start_time = time.time()
        endpoint = request.url.path

        response = await call_next(request)

        duration = time.time() - start_time
        result = "success" if response.status_code < 400 else "error"
        logger.info(
            f"Request completed | "
            f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')} | "
            f"Endpoint: {endpoint} | "
            f"Duration: {duration:.2f}s | "
            f"Result: {result}"
        )

        return response
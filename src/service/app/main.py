from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.api.recognize_api import router
from app.middleware import add_logging_middleware  # Импорт middleware
from loguru import logger
from app.config import LOG_LEVEL, LOG_FILE

logger.remove()
logger.add(
    LOG_FILE,
    level=LOG_LEVEL,
    format="{time} - {level} - {message}",
    rotation="10 MB",
    compression="zip"
)
logger.add(
    sink=lambda msg: print(msg, end=""),
    level=LOG_LEVEL,
    format="{time} - {level} - {message}"
)

app = FastAPI(title="License Plate Recognition Service")

add_logging_middleware(app)

@app.exception_handler(Exception)
async def global_exception_handler(request, exc: Exception):
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"status": "error", "message": "Internal server error"}
    )

app.include_router(router)
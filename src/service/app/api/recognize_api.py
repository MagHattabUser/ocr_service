from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas.schemas import RecognitionResponse  # Убрана PingResponse
from app.utils.inference import recognize_plate
from loguru import logger
from PIL import UnidentifiedImageError


router = APIRouter()

@router.get("/ping")
async def ping():
    logger.debug("Ping endpoint called")
    return {"message": "pong"}


@router.post("/recognize", response_model=RecognitionResponse)
async def recognize(file: UploadFile = File(...)):
    logger.debug(f"Recognize endpoint called with file: {file.filename}")

    try:
        if not file.content_type.startswith("image/"):
            logger.warning(f"Invalid file type: {file.content_type}")
            raise HTTPException(status_code=400, detail="File must be an image")

        image_bytes = await file.read()
        if not image_bytes:
            logger.warning("Empty file uploaded")
            raise HTTPException(status_code=400, detail="Empty file")

        plate_number = recognize_plate(image_bytes)
        logger.info(f"Recognition result: {plate_number}")

        return RecognitionResponse(plate_number=plate_number)

    except UnidentifiedImageError:
        logger.error("Failed to process image: invalid image format")
        raise HTTPException(status_code=400, detail="Invalid image format")
    except Exception as e:
        logger.error(f"Recognition failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Recognition failed: {str(e)}")
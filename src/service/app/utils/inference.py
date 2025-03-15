import torch
from loguru import logger
from app.utils.processing import preprocess_image, postprocess_output
from app.models.model import load_model
from app.config import MODEL_WEIGHTS_PATH, ALPHABET


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

try:
    model = load_model(MODEL_WEIGHTS_PATH, num_classes=len(ALPHABET) + 1, device=device)
except Exception as e:
    logger.critical(f"Failed to initialize models: {str(e)}", exc_info=True)
    raise RuntimeError("Cannot start service: Model loading failed")


def recognize_plate(image_bytes):
    try:
        logger.debug("Starting image preprocessing")
        processed_image = preprocess_image(image_bytes).to(device)

        logger.debug("Running PyTorch inference")
        with torch.no_grad():
            output = model(processed_image)
            log_probs = torch.nn.functional.log_softmax(output, dim=2)

        logger.debug("Postprocessing inference output")
        plate_number = postprocess_output(log_probs)

        return plate_number
    except Exception as e:
        logger.error(f"Inference failed: {str(e)}", exc_info=True)
        raise
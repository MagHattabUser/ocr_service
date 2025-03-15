from PIL import Image
from io import BytesIO
from torchvision import transforms

from app.config import ALPHABET, idx_to_char


preprocess_transform = transforms.Compose([
    transforms.Resize((84, 388)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def preprocess_image(image_bytes):
    image = Image.open(BytesIO(image_bytes)).convert('RGB')
    image = preprocess_transform(image)
    return image.unsqueeze(0)

def postprocess_output(log_probs):
    _, preds = log_probs.max(2)
    preds = preds.transpose(1, 0).contiguous().view(-1)

    prev = None
    decoded = []
    for pred in preds:
        if pred != len(ALPHABET) and pred != prev:
            decoded.append(pred.item())
        prev = pred

    return ''.join([idx_to_char[idx] for idx in decoded])
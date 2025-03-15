MODEL_WEIGHTS_PATH = "app/models/license_plate_model.pth"
ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789ABCEHKMOPTXY'
idx_to_char = {idx: char for idx, char in enumerate(ALPHABET)}
LOG_LEVEL = "INFO"
LOG_FILE = "app/logs/app.log"
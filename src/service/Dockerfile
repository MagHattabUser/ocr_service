FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-pip \
    libpng-dev \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем папку app в /app/app
COPY app/ /app/app/

# Копируем веса модели в правильное место
COPY app/models/license_plate_model.pth /app/app/models/license_plate_model.pth

RUN mkdir -p /app/app/logs && chmod -R 777 /app/app/logs

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
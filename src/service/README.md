# License Plate Recognition Service

Этот проект представляет собой сервис для распознавания автомобильных номеров с использованием нейронной сети на основе PyTorch и FastAPI. Сервис принимает изображения номеров через HTTP-запросы и возвращает распознанный текст номера.

## Требования

- **Python**: 3.10 или выше (в Docker используется 3.0)
- **Docker**: Для сборки и запуска контейнера
- **Зависимости**: Перечислены в `requirements.txt`

## Структура проекта
```
.
├── Dockerfile          # Файл для сборки Docker-образа
├── app/                # Основной код приложения
│   ├── api/            # Эндпоинты API
│   │   └── recognize_api.py
│   ├── config.py       # Конфигурация (пути, алфавит, логи)
│   ├── logs/           # Директория для логов
│   ├── main.py         # Точка входа FastAPI
│   ├── middleware.py   # Middleware для логирования запросов
│   ├── models/         # Модель PyTorch
│   │   ├── license_plate_model.pth  # Веса модели
│   │   └── model.py
│   ├── schemas/        # Pydantic-схемы
│   │   └── schemas.py
│   └── utils/          # Утилиты для инференса и обработки
│       ├── inference.py
│       └── processing.py
└── requirements.txt    # Зависимости проекта
```

## Установка

### Локальная установка (без Docker)
1. Создайте виртуальное окружение:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Для Mac/Linux
   .venv\Scripts\activate     # Для Windows

2. Установка зависимостей:
    ````
   cd src/service
   pip install -r requirements.txt
   
3. Запустите сервис:
    ````
   cd src/service
   python -m uvicorn app.main:app --port 8080

### Установка через Docker
1. Убедитесь, что Docker установлен:
    ````
   docker --version
   
2. Соберите Docker-образ:
   ````
    cd src/service
    docker build -t license-plate-service .
   
3. Запустите контейнер:
    ````
   docker run -p 8080:8080 --name ocr-container license-plate-service


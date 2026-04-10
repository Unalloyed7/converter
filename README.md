# converter
=======
Сервис для работы с валютными курсами и конвертацией валют.  

## Технологии

- Python
- FastAPI
- PostgreSQL
- Pydantic

## Архитектура проекта

Проект разделён на несколько логических слоёв:
- `endpoints` — обработка HTTP-запросов и маршрутизация
- `models` — Pydantic-модели для валидации входных и выходных данных
- `core` — конфигурация приложения, безопасность и работа с базой данных
- `utils` — интеграция с внешним API валютных курсов

## Структура проекта

```text
project/
│
├── my_app/
│   ├── api/
│   │   ├── endpoints/
│   │   │   ├── users.py
│   │   │   └── currency.py
│   │   ├── models/
│   │   │   ├── users.py
│   │   │   └── currency.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── database.py
│   │   └── utils/
│   │       └── external_api.py
│
├── tests/
├── .env
├── main.py
├── pyproject.toml
├── requirements.txt
└── README.md

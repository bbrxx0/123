# StayFinder

## Run (Windows / VS Code)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Configure

1) Copy `.env.example` → `.env`  
2) Fill in Gmail SMTP + Stripe keys in `.env`

## Init database

> If you already have an old database, delete: `instance/hotel_booking.sqlite3`

```powershell
python manage.py init-db
python manage.py seed
python manage.py create-admin --email admin@example.com --password Admin123!
```

## Run

```powershell
python manage.py run
```

Open:
- Website: http://127.0.0.1:5000
- Admin: http://127.0.0.1:5000/admin

## UML Documentation

Документация на русском языке для создания UML-диаграмм в Visual Paradigm:

- **[VISUAL_PARADIGM_INSTRUCTIONS_RU.md](./VISUAL_PARADIGM_INSTRUCTIONS_RU.md)** - Полная инструкция:
  - Диаграмма классов (12 классов)
  - Диаграмма активности для полного процесса бронирования (23+ активностей)
  
- **[ACTIVITY_DIAGRAMS_TWO_USE_CASES_RU.md](./ACTIVITY_DIAGRAMS_TWO_USE_CASES_RU.md)** - Две простые диаграммы активности:
  - Use Case 1: Вход в систему (Login) - 8-10 активностей
  - Use Case 2: Поиск отелей (Search Hotels) - 9-12 активностей
  - Пошаговые инструкции для быстрого создания

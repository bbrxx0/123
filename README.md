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

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

## Documentation

### 📊 Use Case Diagram
Complete use case diagram documentation is available in the `docs/` folder:
- **[View Instructions](docs/USE-CASE-INSTRUCTIONS.md)** - Step-by-step guide in Polish/Russian for creating the diagram in Visual Paradigm
- **[View Description](docs/USE-CASE-DESCRIPTION.md)** - Detailed description of all use cases (EN/PL/RU)
- **[View Diagram](docs/StayFinder%20Use%20Case%20Diagram.png)** - Generated diagram image
- **[View Source](docs/use-case-diagram.puml)** - PlantUML source code

**Quick Start:**
- For beginners: Read the step-by-step instructions in `docs/USE-CASE-INSTRUCTIONS.md`
- For advanced users: Import `docs/use-case-diagram.puml` directly into Visual Paradigm

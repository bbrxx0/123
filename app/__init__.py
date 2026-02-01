import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv

db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message_category = "warning"

def create_app():
    load_dotenv()
    app = Flask(__name__, instance_relative_config=True)

    os.makedirs(app.instance_path, exist_ok=True)

    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "dev-secret-change-me"),
        SQLALCHEMY_DATABASE_URI=os.getenv(
            "DATABASE_URL",
            "sqlite:///" + os.path.join(app.instance_path, "hotel_booking.sqlite3"),
        ),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,

        # Auth tokens
        RESET_TOKEN_MAX_AGE_SECONDS=int(os.getenv("RESET_TOKEN_MAX_AGE_SECONDS", "3600")),
        EMAIL_CONFIRM_TOKEN_MAX_AGE_SECONDS=int(os.getenv("EMAIL_CONFIRM_TOKEN_MAX_AGE_SECONDS", "86400")),
        APP_BASE_URL=os.getenv("APP_BASE_URL", "http://127.0.0.1:5000"),

        # Admin audit log
        ADMIN_LOG_PATH=os.path.join(app.instance_path, "admin.log"),

        # Email (Gmail SMTP)
        MAIL_SERVER=os.getenv("MAIL_SERVER", "smtp.gmail.com"),
        MAIL_PORT=int(os.getenv("MAIL_PORT", "587")),
        MAIL_USE_TLS=os.getenv("MAIL_USE_TLS", "1") == "1",
        MAIL_USERNAME=os.getenv("MAIL_USERNAME", ""),
        MAIL_PASSWORD=os.getenv("MAIL_PASSWORD", ""),
        MAIL_DEFAULT_SENDER=os.getenv("MAIL_DEFAULT_SENDER", os.getenv("MAIL_USERNAME", "")),
        MAIL_FROM_NAME=os.getenv("MAIL_FROM_NAME", "StayFinder"),
        EMAIL_DEBUG_PRINT=os.getenv("EMAIL_DEBUG_PRINT", "0") == "1",

        # Stripe
        STRIPE_SECRET_KEY=os.getenv("STRIPE_SECRET_KEY", ""),
        STRIPE_PUBLISHABLE_KEY=os.getenv("STRIPE_PUBLISHABLE_KEY", ""),
        STRIPE_WEBHOOK_SECRET=os.getenv("STRIPE_WEBHOOK_SECRET", ""),
        CURRENCY=os.getenv("CURRENCY", "pln"),
    )

    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    # Blueprints
    from .routes import main_bp
    from .auth import auth_bp
    from .admin import admin_bp
    from .payments import payments_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(payments_bp, url_prefix="/payments")

    # Create tables
    with app.app_context():
        db.create_all()

    return app

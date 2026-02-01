from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from flask import current_app

def _serializer(salt: str) -> URLSafeTimedSerializer:
    return URLSafeTimedSerializer(current_app.config["SECRET_KEY"], salt=salt)

# Password reset
def generate_reset_token(email: str) -> str:
    return _serializer("password-reset").dumps({"email": email})

def verify_reset_token(token: str, max_age_seconds: int) -> str | None:
    try:
        data = _serializer("password-reset").loads(token, max_age=max_age_seconds)
        return data.get("email")
    except (BadSignature, SignatureExpired):
        return None

# Email confirmation
def generate_email_confirm_token(email: str) -> str:
    return _serializer("email-confirm").dumps({"email": email})

def verify_email_confirm_token(token: str, max_age_seconds: int) -> str | None:
    try:
        data = _serializer("email-confirm").loads(token, max_age=max_age_seconds)
        return data.get("email")
    except (BadSignature, SignatureExpired):
        return None

from __future__ import annotations
from flask import current_app, url_for, render_template
from flask_mail import Message
from . import mail

def _send(to_email: str, subject: str, html_body: str, text_body: str | None = None) -> None:
    # If config missing, fall back to console print (useful for local dev)
    debug_print = current_app.config.get("EMAIL_DEBUG_PRINT", False)
    username = current_app.config.get("MAIL_USERNAME")
    password = current_app.config.get("MAIL_PASSWORD")

    if debug_print or not username or not password:
        print(f"[EMAIL DEBUG] To: {to_email}")
        print(f"[EMAIL DEBUG] Subject: {subject}")
        if text_body:
            print(text_body)
        else:
            # keep short
            print(html_body)
        return

    sender_email = current_app.config.get("MAIL_DEFAULT_SENDER") or username
    sender_name = current_app.config.get("MAIL_FROM_NAME", "StayFinder")
    msg = Message(subject=subject, recipients=[to_email], sender=(sender_name, sender_email))
    msg.body = text_body or "Please view this email in an HTML-capable client."
    msg.html = html_body
    mail.send(msg)

def send_password_reset_email(user_email: str, token: str) -> str:
    reset_url = current_app.config["APP_BASE_URL"] + url_for("auth.reset_with_token", token=token)
    subject = "Reset your password"
    html = render_template("emails/password_reset.html", reset_url=reset_url)
    text = f"Reset your password: {reset_url}"
    _send(user_email, subject, html, text)
    return reset_url

def send_email_confirmation(user_email: str, token: str) -> str:
    confirm_url = current_app.config["APP_BASE_URL"] + url_for("auth.confirm_email", token=token)
    subject = "Confirm your email"
    html = render_template("emails/confirm_email.html", confirm_url=confirm_url)
    text = f"Confirm your email: {confirm_url}"
    _send(user_email, subject, html, text)
    return confirm_url

def send_payment_receipt_email(user_email: str, reservation, receipt_ref: str) -> None:
    subject = f"Payment receipt — Booking #{reservation.id}"
    html = render_template("emails/payment_receipt.html", r=reservation, receipt_ref=receipt_ref)
    text = (
        f"Payment receipt for booking #{reservation.id}\n"
        f"Hotel: {reservation.room.hotel.name}\n"
        f"Room: {reservation.room.name}\n"
        f"Dates: {reservation.check_in} to {reservation.check_out} ({reservation.nights} nights)\n"
        f"Total: {reservation.total_price()}\n"
        f"Receipt reference: {receipt_ref}\n"
    )
    _send(user_email, subject, html, text)

from __future__ import annotations
from flask import Blueprint, current_app, redirect, request, url_for, flash, render_template, abort
from flask_login import login_required, current_user
import stripe

from . import db
from .models import Reservation
from .email_utils import send_payment_receipt_email
from .admin_logging import get_admin_logger

payments_bp = Blueprint("payments", __name__)
admin_log = get_admin_logger

def _stripe_configured() -> bool:
    return bool(current_app.config.get("STRIPE_SECRET_KEY")) and bool(current_app.config.get("STRIPE_PUBLISHABLE_KEY"))

def _set_api_key():
    stripe.api_key = current_app.config.get("STRIPE_SECRET_KEY")

@payments_bp.get("/config")
def config():
    # Optional endpoint if you later want JS integration
    return {"publishableKey": current_app.config.get("STRIPE_PUBLISHABLE_KEY", "")}

@payments_bp.get("/checkout/<int:res_id>")
@login_required
def checkout(res_id: int):
    res = Reservation.query.get_or_404(res_id)
    if res.user_id != current_user.id:
        abort(403)
    if res.status == "canceled":
        flash("This booking was canceled.", "warning")
        return redirect(url_for("main.my_reservations"))
    if res.payment_status == "paid":
        flash("This booking is already paid.", "info")
        return redirect(url_for("main.my_reservations"))
    if not _stripe_configured():
        flash("Stripe is not configured. Please set STRIPE_SECRET_KEY and STRIPE_PUBLISHABLE_KEY in .env", "danger")
        return redirect(url_for("main.my_reservations"))

    total_pln = res.total_price()
    if total_pln <= 0:
        flash("Total price is invalid.", "danger")
        return redirect(url_for("main.my_reservations"))

    _set_api_key()
    currency = current_app.config.get("CURRENCY", "pln")

    success_url = current_app.config["APP_BASE_URL"] + url_for("payments.success") + "?session_id={CHECKOUT_SESSION_ID}"
    cancel_url = current_app.config["APP_BASE_URL"] + url_for("payments.cancel", res_id=res.id)

    hotel_name = res.room.hotel.name if res.room and res.room.hotel else "Hotel"
    room_name = res.room.name if res.room else "Room"
    description = f"{hotel_name} — {room_name} ({res.nights} nights)"

    session = stripe.checkout.Session.create(
        mode="payment",
        payment_method_types=["card"],
        customer_email=current_user.email,
        line_items=[
            {
                "quantity": 1,
                "price_data": {
                    "currency": currency,
                    "unit_amount": int(total_pln) * 100,  # PLN -> grosz
                    "product_data": {
                        "name": f"Booking #{res.id}",
                        "description": description,
                    },
                },
            }
        ],
        metadata={"reservation_id": str(res.id), "user_id": str(current_user.id)},
        success_url=success_url,
        cancel_url=cancel_url,
    )

    res.stripe_session_id = session.id
    res.payment_status = "unpaid"
    db.session.commit()

    return redirect(session.url, code=303)

@payments_bp.get("/success")
@login_required
def success():
    session_id = request.args.get("session_id", "")
    if not session_id:
        abort(400)

    if not _stripe_configured():
        flash("Stripe is not configured.", "danger")
        return redirect(url_for("main.my_reservations"))

    _set_api_key()
    session = stripe.checkout.Session.retrieve(session_id)

    res_id = session.metadata.get("reservation_id") if session and session.metadata else None
    if not res_id:
        flash("Unable to identify booking for this payment.", "warning")
        return redirect(url_for("main.my_reservations"))

    res = Reservation.query.get_or_404(int(res_id))
    if res.user_id != current_user.id:
        abort(403)

    if getattr(session, "payment_status", None) != "paid":
        # Not paid
        res.payment_status = "failed"
        db.session.commit()
        flash("Payment not completed.", "warning")
        return redirect(url_for("main.my_reservations"))

    # Mark paid if not already
    if res.payment_status != "paid":
        res.mark_paid(session_id=session.id, payment_intent_id=getattr(session, "payment_intent", None))
        if res.status != "canceled":
            res.status = "confirmed"
        db.session.commit()

        # Receipt email
        receipt_ref = getattr(session, "payment_intent", None) or session.id
        send_payment_receipt_email(current_user.email, res, receipt_ref=receipt_ref)

        # Admin audit log
        admin_log().info(f"PAYMENT_SUCCESS res_id={res.id} user={current_user.email} session={session.id}")

    flash("Payment successful. Receipt has been emailed to you.", "success")
    return render_template("payments/success.html", reservation=res)

@payments_bp.get("/cancel")
@login_required
def cancel():
    res_id = request.args.get("res_id") or request.args.get("reservation_id") or request.args.get("id")
    if res_id:
        try:
            res = Reservation.query.get(int(res_id))
            if res and res.user_id == current_user.id and res.payment_status != "paid":
                res.payment_status = "unpaid"
                db.session.commit()
        except Exception:
            pass
    flash("Payment canceled.", "info")
    return redirect(url_for("main.my_reservations"))

@payments_bp.post("/webhook")
def webhook():
    # Optional Stripe webhook support (recommended for production).
    if not _stripe_configured():
        return "", 204

    _set_api_key()
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature", "")
    secret = current_app.config.get("STRIPE_WEBHOOK_SECRET", "")

    try:
        if secret:
            event = stripe.Webhook.construct_event(payload, sig_header, secret)
        else:
            event = stripe.Event.construct_from(request.json, stripe.api_key)
    except Exception:
        return "", 400

    # Handle checkout.session.completed
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        if session.get("payment_status") == "paid":
            try:
                res_id = int(session.get("metadata", {}).get("reservation_id"))
                res = Reservation.query.get(res_id)
                if res and res.payment_status != "paid":
                    res.mark_paid(session_id=session.get("id"), payment_intent_id=session.get("payment_intent"))
                    if res.status != "canceled":
                        res.status = "confirmed"
                    db.session.commit()
                    admin_log().info(f"PAYMENT_WEBHOOK_SUCCESS res_id={res.id} session={session.get('id')}")
            except Exception:
                pass

    return "", 200

from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, login_required, current_user
from . import db
from .models import User
from .forms import RegisterForm, LoginForm, ResetRequestForm, ResetPasswordForm
from .security import (
    generate_reset_token, verify_reset_token,
    generate_email_confirm_token, verify_email_confirm_token,
)
from .email_utils import send_password_reset_email, send_email_confirmation

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = RegisterForm()
    confirm_url = None

    if form.validate_on_submit():
        email = form.email.data.lower().strip()
        user = User(email=email)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        token = generate_email_confirm_token(email)
        confirm_url = send_email_confirmation(email, token)

        flash("Account created. Please confirm your email (check inbox).", "success")
        return render_template("auth/register_done.html", email=email, confirm_url=confirm_url if current_app.config.get("EMAIL_DEBUG_PRINT") else None)

    return render_template("auth/register.html", form=form)

@auth_bp.route("/confirm/<token>")
def confirm_email(token):
    email = verify_email_confirm_token(token, current_app.config["EMAIL_CONFIRM_TOKEN_MAX_AGE_SECONDS"])
    if not email:
        flash("Confirmation link is invalid or expired.", "warning")
        return redirect(url_for("auth.login"))

    user = User.query.filter_by(email=email).first()
    if not user:
        flash("User not found.", "danger")
        return redirect(url_for("auth.register"))

    if not user.is_email_confirmed:
        user.confirm_email()
        db.session.commit()
        flash("Email confirmed. You can sign in now.", "success")
    else:
        flash("Email already confirmed. You can sign in.", "info")

    return redirect(url_for("auth.login"))

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data.lower().strip()
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(form.password.data):
            if not user.is_email_confirmed and not user.is_admin:
                flash("Please confirm your email before signing in.", "warning")
                return render_template("auth/login.html", form=form)
            login_user(user, remember=form.remember.data)
            next_url = request.args.get("next") or url_for("main.index")
            return redirect(next_url)
        flash("Invalid email or password.", "danger")
    return render_template("auth/login.html", form=form)

@auth_bp.get("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been signed out.", "info")
    return redirect(url_for("main.index"))

@auth_bp.route("/reset", methods=["GET", "POST"])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = ResetRequestForm()
    debug_url = None

    if form.validate_on_submit():
        email = form.email.data.lower().strip()
        user = User.query.filter_by(email=email).first()
        if user:
            token = generate_reset_token(email)
            debug_url = send_password_reset_email(email, token)

        flash("If the email is registered, a reset link has been sent.", "info")

    return render_template("auth/reset_request.html", form=form, reset_url=debug_url if current_app.config.get("EMAIL_DEBUG_PRINT") else None)

@auth_bp.route("/reset/<token>", methods=["GET", "POST"])
def reset_with_token(token):
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    email = verify_reset_token(token, current_app.config["RESET_TOKEN_MAX_AGE_SECONDS"])
    if not email:
        flash("Reset link is invalid or expired. Please request a new one.", "warning")
        return redirect(url_for("auth.reset_request"))

    user = User.query.filter_by(email=email).first()
    if not user:
        flash("User not found.", "danger")
        return redirect(url_for("auth.reset_request"))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash("Password updated. Please sign in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/reset_token.html", form=form)

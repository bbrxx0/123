from datetime import date, timedelta
from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_user, logout_user, current_user
from . import db
from .models import Hotel, Room, Reservation, User
from .forms import HotelForm, RoomForm, AdminLoginForm
from .admin_logging import get_admin_logger

admin_bp = Blueprint("admin", __name__)
log = get_admin_logger

def _is_public_endpoint() -> bool:
    return request.endpoint in {"admin.login"}

@admin_bp.before_request
def guard_admin():
    if _is_public_endpoint():
        return None

    if not current_user.is_authenticated:
        return redirect(url_for("admin.login", next=request.path))

    if not getattr(current_user, "is_admin", False):
        abort(403)

@admin_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated and current_user.is_admin:
        return redirect(url_for("admin.dashboard"))

    form = AdminLoginForm()
    if form.validate_on_submit():
        email = form.email.data.lower().strip()
        user = User.query.filter_by(email=email).first()

        if user and user.is_admin and user.check_password(form.password.data):
            login_user(user)
            log().info(f"ADMIN_LOGIN_SUCCESS email={email} ip={request.remote_addr}")
            flash("Welcome, admin.", "success")
            return redirect(request.args.get("next") or url_for("admin.dashboard"))

        log().info(f"ADMIN_LOGIN_FAIL email={email} ip={request.remote_addr}")
        flash("Invalid admin credentials.", "danger")

    return render_template("admin/login.html", form=form)

@admin_bp.get("/logout")
def logout():
    if current_user.is_authenticated:
        log().info(f"ADMIN_LOGOUT email={current_user.email} ip={request.remote_addr}")
        logout_user()
    flash("Signed out.", "info")
    return redirect(url_for("admin.login"))

@admin_bp.get("/")
def dashboard():
    today = date.today()
    next_week = today + timedelta(days=7)

    stats = {
        "hotels": Hotel.query.count(),
        "rooms": Room.query.count(),
        "users": User.query.count(),
        "reservations": Reservation.query.count(),

        "pending": Reservation.query.filter_by(status="pending").count(),
        "confirmed": Reservation.query.filter_by(status="confirmed").count(),
        "canceled": Reservation.query.filter_by(status="canceled").count(),

        "paid": Reservation.query.filter_by(payment_status="paid").count(),
        "unpaid": Reservation.query.filter_by(payment_status="unpaid").count(),
        "failed": Reservation.query.filter_by(payment_status="failed").count(),
    }

    paid_res = Reservation.query.filter_by(payment_status="paid").order_by(Reservation.created_at.desc()).all()
    stats["revenue_paid"] = sum(r.total_price() for r in paid_res)

    upcoming = (
        Reservation.query
        .filter(Reservation.status != "canceled")
        .filter(Reservation.check_in >= today, Reservation.check_in <= next_week)
        .order_by(Reservation.check_in.asc())
        .limit(10)
        .all()
    )

    latest = Reservation.query.order_by(Reservation.created_at.desc()).limit(12).all()
    latest_users = User.query.order_by(User.created_at.desc()).limit(8).all()
    latest_payments = Reservation.query.filter_by(payment_status="paid").order_by(Reservation.paid_at.desc()).limit(8).all()

    return render_template(
        "admin/dashboard.html",
        stats=stats,
        latest=latest,
        upcoming=upcoming,
        latest_users=latest_users,
        latest_payments=latest_payments,
    )

@admin_bp.get("/hotels")
def hotels_list():
    hotels = Hotel.query.order_by(Hotel.created_at.desc()).all()
    return render_template("admin/hotels_list.html", hotels=hotels)

@admin_bp.route("/hotels/new", methods=["GET", "POST"])
def hotel_new():
    form = HotelForm()
    if form.validate_on_submit():
        hotel = Hotel(
            name=form.name.data,
            city=form.city.data,
            address=form.address.data,
            stars=form.stars.data,
            image_url=form.image_url.data,
            highlights=form.highlights.data,
            description=form.description.data,
        )
        db.session.add(hotel)
        db.session.commit()
        log().info(f"HOTEL_CREATE id={hotel.id} by={current_user.email}")
        flash("Hotel created.", "success")
        return redirect(url_for("admin.hotels_list"))
    return render_template("admin/hotel_form.html", form=form, title="New hotel")

@admin_bp.route("/hotels/<int:hotel_id>/edit", methods=["GET", "POST"])
def hotel_edit(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    form = HotelForm(obj=hotel)
    if form.validate_on_submit():
        form.populate_obj(hotel)
        db.session.commit()
        log().info(f"HOTEL_EDIT id={hotel.id} by={current_user.email}")
        flash("Hotel updated.", "success")
        return redirect(url_for("admin.hotels_list"))
    return render_template("admin/hotel_form.html", form=form, title="Edit hotel")

@admin_bp.post("/hotels/<int:hotel_id>/delete")
def hotel_delete(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    db.session.delete(hotel)
    db.session.commit()
    log().info(f"HOTEL_DELETE id={hotel_id} by={current_user.email}")
    flash("Hotel deleted.", "info")
    return redirect(url_for("admin.hotels_list"))

@admin_bp.get("/hotels/<int:hotel_id>/rooms")
def rooms_list(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    return render_template("admin/rooms_list.html", hotel=hotel)

@admin_bp.route("/hotels/<int:hotel_id>/rooms/new", methods=["GET", "POST"])
def room_new(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    form = RoomForm()
    if form.validate_on_submit():
        room = Room(
            hotel_id=hotel.id,
            name=form.name.data,
            capacity=form.capacity.data,
            price_per_night=form.price_per_night.data,
            description=form.description.data,
        )
        db.session.add(room)
        db.session.commit()
        log().info(f"ROOM_CREATE id={room.id} hotel_id={hotel.id} by={current_user.email}")
        flash("Room created.", "success")
        return redirect(url_for("admin.rooms_list", hotel_id=hotel.id))
    return render_template("admin/room_form.html", form=form, title=f"New room — {hotel.name}", hotel=hotel)

@admin_bp.route("/rooms/<int:room_id>/edit", methods=["GET", "POST"])
def room_edit(room_id):
    room = Room.query.get_or_404(room_id)
    hotel = room.hotel
    form = RoomForm(obj=room)
    if form.validate_on_submit():
        form.populate_obj(room)
        db.session.commit()
        log().info(f"ROOM_EDIT id={room.id} by={current_user.email}")
        flash("Room updated.", "success")
        return redirect(url_for("admin.rooms_list", hotel_id=hotel.id))
    return render_template("admin/room_form.html", form=form, title=f"Edit room — {hotel.name}", hotel=hotel)

@admin_bp.post("/rooms/<int:room_id>/delete")
def room_delete(room_id):
    room = Room.query.get_or_404(room_id)
    hotel_id = room.hotel_id
    db.session.delete(room)
    db.session.commit()
    log().info(f"ROOM_DELETE id={room_id} by={current_user.email}")
    flash("Room deleted.", "info")
    return redirect(url_for("admin.rooms_list", hotel_id=hotel_id))

@admin_bp.get("/reservations")
def reservations_list():
    status = request.args.get("status", "").strip()
    qtext = request.args.get("q", "").strip()

    q = Reservation.query
    if status in {"pending", "confirmed", "canceled"}:
        q = q.filter_by(status=status)

    if qtext:
        q = (
            q.join(User, Reservation.user_id == User.id)
             .join(Room, Reservation.room_id == Room.id)
             .join(Hotel, Room.hotel_id == Hotel.id)
             .filter(
                 (User.email.ilike(f"%{qtext}%")) |
                 (Hotel.name.ilike(f"%{qtext}%")) |
                 (Hotel.city.ilike(f"%{qtext}%"))
             )
        )

    reservations = q.order_by(Reservation.created_at.desc()).limit(500).all()
    return render_template("admin/reservations_list.html", reservations=reservations, status=status, qtext=qtext)

@admin_bp.get("/reservations/<int:res_id>")
def reservation_detail(res_id):
    res = Reservation.query.get_or_404(res_id)
    return render_template("admin/reservation_detail.html", r=res)

@admin_bp.post("/reservations/<int:res_id>/set-status")
def reservation_set_status(res_id):
    res = Reservation.query.get_or_404(res_id)
    new_status = request.form.get("status")
    if new_status not in {"pending", "confirmed", "canceled"}:
        abort(400)
    old = res.status
    res.status = new_status
    db.session.commit()
    log().info(f"RES_STATUS_CHANGE id={res.id} {old}->{new_status} by={current_user.email}")
    flash("Status updated.", "success")
    return redirect(request.referrer or url_for("admin.reservations_list"))

@admin_bp.get("/payments")
def payments_list():
    state = request.args.get("state", "").strip()  # paid/unpaid/failed
    qtext = request.args.get("q", "").strip()

    q = Reservation.query
    if state in {"paid", "unpaid", "failed"}:
        q = q.filter_by(payment_status=state)

    if qtext:
        q = (
            q.join(User, Reservation.user_id == User.id)
             .join(Room, Reservation.room_id == Room.id)
             .join(Hotel, Room.hotel_id == Hotel.id)
             .filter(
                 (User.email.ilike(f"%{qtext}%")) |
                 (Hotel.name.ilike(f"%{qtext}%")) |
                 (Hotel.city.ilike(f"%{qtext}%"))
             )
        )

    reservations = q.order_by(Reservation.created_at.desc()).limit(500).all()
    revenue_paid = sum(r.total_price() for r in reservations if r.payment_status == "paid")

    return render_template("admin/payments_list.html", reservations=reservations, state=state, qtext=qtext, revenue_paid=revenue_paid)

@admin_bp.get("/users")
def users_list():
    users = User.query.order_by(User.created_at.desc()).limit(500).all()
    return render_template("admin/users_list.html", users=users)

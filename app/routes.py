from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from . import db
from .models import Hotel, Room, Reservation, room_is_available
from .forms import BookingForm

main_bp = Blueprint("main", __name__)

@main_bp.get("/")
def index():
    q = request.args.get("q", "").strip()
    city = request.args.get("city", "").strip()

    hotels_query = Hotel.query
    if q:
        hotels_query = hotels_query.filter(Hotel.name.ilike(f"%{q}%"))
    if city:
        hotels_query = hotels_query.filter(Hotel.city.ilike(f"%{city}%"))

    hotels = hotels_query.order_by(Hotel.created_at.desc()).all()
    return render_template("index.html", hotels=hotels, q=q, city=city)

@main_bp.get("/hotels/<int:hotel_id>")
def hotel_detail(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    return render_template("hotel_detail.html", hotel=hotel)

@main_bp.route("/rooms/<int:room_id>/book", methods=["GET", "POST"])
@login_required
def book_room(room_id):
    room = Room.query.get_or_404(room_id)
    form = BookingForm()
    if form.validate_on_submit():
        check_in = form.check_in.data
        check_out = form.check_out.data

        if not room_is_available(room, check_in, check_out):
            flash("This room is not available for the selected dates.", "warning")
            return render_template("book_room.html", room=room, form=form)

        res = Reservation(
            user_id=current_user.id,
            room_id=room.id,
            check_in=check_in,
            check_out=check_out,
            status="pending",
        )
        db.session.add(res)
        db.session.commit()
        flash("Booking request created (status: pending).", "success")
        return redirect(url_for("main.my_reservations"))
    return render_template("book_room.html", room=room, form=form)

@main_bp.get("/me/reservations")
@login_required
def my_reservations():
    reservations = (
        Reservation.query
        .filter_by(user_id=current_user.id)
        .order_by(Reservation.created_at.desc())
        .all()
    )
    return render_template("my_reservations.html", reservations=reservations)

@main_bp.post("/me/reservations/<int:res_id>/cancel")
@login_required
def cancel_reservation(res_id):
    res = Reservation.query.get_or_404(res_id)
    if res.user_id != current_user.id and not current_user.is_admin:
        abort(403)
    if res.status != "canceled":
        res.status = "canceled"
        db.session.commit()
        flash("Booking canceled.", "info")
    return redirect(url_for("main.my_reservations"))

from __future__ import annotations
from datetime import datetime, date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    is_email_confirmed = db.Column(db.Boolean, default=False, nullable=False)
    email_confirmed_at = db.Column(db.DateTime, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    reservations = db.relationship("Reservation", back_populates="user", cascade="all,delete-orphan")

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def confirm_email(self) -> None:
        self.is_email_confirmed = True
        self.email_confirmed_at = datetime.utcnow()

@login_manager.user_loader
def load_user(user_id: str):
    return User.query.get(int(user_id))

class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    highlights = db.Column(db.Text, nullable=True)  # separated by \n
    stars = db.Column(db.Integer, default=5, nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    rooms = db.relationship("Room", back_populates="hotel", cascade="all,delete-orphan")

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey("hotel.id"), nullable=False, index=True)
    name = db.Column(db.String(180), nullable=False)
    capacity = db.Column(db.Integer, default=2, nullable=False)
    price_per_night = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)

    hotel = db.relationship("Hotel", back_populates="rooms")
    reservations = db.relationship("Reservation", back_populates="room", cascade="all,delete-orphan")

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"), nullable=False, index=True)

    check_in = db.Column(db.Date, nullable=False)
    check_out = db.Column(db.Date, nullable=False)

    status = db.Column(db.String(20), default="pending", nullable=False)  # pending/confirmed/canceled
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Payment
    payment_status = db.Column(db.String(20), default="unpaid", nullable=False)  # unpaid/paid/refunded/failed
    stripe_session_id = db.Column(db.String(255), nullable=True)
    stripe_payment_intent_id = db.Column(db.String(255), nullable=True)
    paid_at = db.Column(db.DateTime, nullable=True)

    user = db.relationship("User", back_populates="reservations")
    room = db.relationship("Room", back_populates="reservations")

    @property
    def nights(self) -> int:
        return max((self.check_out - self.check_in).days, 0)

    def total_price(self) -> int:
        return self.nights * (self.room.price_per_night if self.room else 0)

    def mark_paid(self, session_id: str | None = None, payment_intent_id: str | None = None) -> None:
        self.payment_status = "paid"
        self.paid_at = datetime.utcnow()
        if session_id:
            self.stripe_session_id = session_id
        if payment_intent_id:
            self.stripe_payment_intent_id = payment_intent_id

def room_is_available(room: Room, check_in: date, check_out: date, ignore_reservation_id: int | None = None) -> bool:
    if check_out <= check_in:
        return False
    q = Reservation.query.filter_by(room_id=room.id).filter(Reservation.status != "canceled")
    if ignore_reservation_id:
        q = q.filter(Reservation.id != ignore_reservation_id)

    overlap = q.filter(Reservation.check_in < check_out, Reservation.check_out > check_in).first()
    return overlap is None

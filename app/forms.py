from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange, Optional, ValidationError
from .models import User

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=255)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=128)])
    confirm = PasswordField("Confirm password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Create account")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError("This email is already registered.")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=255)])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Sign in")

class AdminLoginForm(FlaskForm):
    email = StringField("Admin email", validators=[DataRequired(), Email(), Length(max=255)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign in (Admin)")

class ResetRequestForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=255)])
    submit = SubmitField("Send reset link")

class ResetPasswordForm(FlaskForm):
    password = PasswordField("New password", validators=[DataRequired(), Length(min=6, max=128)])
    confirm = PasswordField("Confirm password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Update password")

class BookingForm(FlaskForm):
    check_in = DateField("Check-in", validators=[DataRequired()], format="%Y-%m-%d")
    check_out = DateField("Check-out", validators=[DataRequired()], format="%Y-%m-%d")
    submit = SubmitField("Book now")

    def validate_check_in(self, field):
        if field.data < date.today():
            raise ValidationError("Check-in can't be in the past.")

    def validate_check_out(self, field):
        if self.check_in.data and field.data <= self.check_in.data:
            raise ValidationError("Check-out must be after check-in.")

class HotelForm(FlaskForm):
    name = StringField("Hotel name", validators=[DataRequired(), Length(max=180)])
    city = StringField("City", validators=[DataRequired(), Length(max=120)])
    address = StringField("Address", validators=[Optional(), Length(max=255)])
    stars = IntegerField("Stars (1-5)", validators=[DataRequired(), NumberRange(min=1, max=5)])
    image_url = StringField("Image URL", validators=[Optional(), Length(max=500)])
    highlights = TextAreaField("Highlights (one per line)", validators=[Optional(), Length(max=5000)])
    description = TextAreaField("Description", validators=[Optional(), Length(max=5000)])
    submit = SubmitField("Save")

class RoomForm(FlaskForm):
    name = StringField("Room name", validators=[DataRequired(), Length(max=180)])
    capacity = IntegerField("Capacity", validators=[DataRequired(), NumberRange(min=1, max=20)])
    price_per_night = IntegerField("Price per night", validators=[DataRequired(), NumberRange(min=1, max=1000000)])
    description = TextAreaField("Description", validators=[Optional(), Length(max=5000)])
    submit = SubmitField("Save")

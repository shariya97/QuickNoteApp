from datetime import datetime, timedelta

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    session
)
from flask_login import (
    login_user,
    logout_user,
    current_user,
    login_required
)

from . import db
from .models import User
from .forms import SignupForm, LoginForm

auth = Blueprint("auth", __name__)


# -----------------------------
# SIGN UP
# -----------------------------
@auth.route("/signup", methods=["GET", "POST"])
def signup():

    if current_user.is_authenticated:
        return redirect(url_for("views.home"))

    form = SignupForm()

    if form.validate_on_submit():

        existing_user = User.query.filter_by(
            email=form.email.data
        ).first()

        if existing_user:
            flash("Email already exists.", "danger")
            return redirect(url_for("auth.signup"))

        user = User(
            username=form.username.data,
            email=form.email.data
        )

        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash("Account created successfully! Please login.", "success")

        return redirect(url_for("auth.login"))

    return render_template("signup.html", form=form)


# -----------------------------
# LOGIN
# -----------------------------
@auth.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("views.home"))

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if not user:
            flash("Email does not exist.", "danger")
            return redirect(url_for("auth.login"))

        # Account Locked?
        if user.lock_until:

            if datetime.utcnow() < user.lock_until:

                remaining = int(
                    (user.lock_until - datetime.utcnow()).total_seconds() / 60
                ) + 1

                flash(
                    f"Your account is locked. Try again in {remaining} minute(s).",
                    "danger"
                )

                return redirect(url_for("auth.login"))

            else:
                user.failed_attempts = 0
                user.lock_until = None
                db.session.commit()

        # Correct Password?
        if user.check_password(form.password.data):

            user.failed_attempts = 0
            user.lock_until = None

            db.session.commit()

            login_user(user)

            session.permanent = True

            flash("Login successful!", "success")

            return redirect(url_for("views.home"))

        else:

            user.failed_attempts += 1

            attempts_left = 3 - user.failed_attempts

            if user.failed_attempts >= 3:

                user.lock_until = datetime.utcnow() + timedelta(minutes=5)

                flash(
                    "Your account has been locked for 5 minutes due to 3 failed attempts.",
                    "danger"
                )

            else:

                flash(
                    f"Incorrect password. {attempts_left} attempt(s) remaining.",
                    "warning"
                )

            db.session.commit()

    return render_template("login.html", form=form)


# -----------------------------
# LOGOUT
# -----------------------------
@auth.route("/logout")
@login_required
def logout():   

    logout_user()

    flash("Logged out successfully.", "info")

    return redirect(url_for("auth.login"))
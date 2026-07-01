from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request
)

from flask_login import (
    login_required,
    current_user,
    logout_user
)

from . import db
from .models import Note
from .forms import NoteForm

views = Blueprint("views", __name__)


# ------------------------------------
# HOME PAGE
# ------------------------------------
@views.route("/", methods=["GET", "POST"])
@login_required
def home():

    form = NoteForm()

    if form.validate_on_submit():

        note = Note(
            text=form.text.data,
            user_id=current_user.id
        )

        db.session.add(note)
        db.session.commit()

        flash("Note added successfully!", "success")

        return redirect(url_for("views.home"))

    notes = Note.query.filter_by(
        user_id=current_user.id
    ).order_by(Note.date_created.desc()).all()

    return render_template(
        "home.html",
        form=form,
        notes=notes
    )


# ------------------------------------
# DELETE NOTE
# ------------------------------------
@views.route("/delete/<int:id>")
@login_required
def delete_note(id):

    note = Note.query.get_or_404(id)

    if note.user_id != current_user.id:
        flash("Unauthorized action.", "danger")
        return redirect(url_for("views.home"))

    db.session.delete(note)
    db.session.commit()

    flash("Note deleted successfully!", "success")

    return redirect(url_for("views.home"))


# ------------------------------------
# EDIT NOTE
# ------------------------------------
@views.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_note(id):

    note = Note.query.get_or_404(id)

    if note.user_id != current_user.id:
        flash("Unauthorized action.", "danger")
        return redirect(url_for("views.home"))

    form = NoteForm()

    if request.method == "GET":
        form.text.data = note.text

    if form.validate_on_submit():

        note.text = form.text.data

        db.session.commit()

        flash("Note updated successfully!", "success")

        return redirect(url_for("views.home"))

    return render_template(
        "home.html",
        form=form,
        notes=Note.query.filter_by(
            user_id=current_user.id
        ).order_by(Note.date_created.desc()).all(),
        editing=True,
        note_id=id
    )


# ------------------------------------
# SESSION EXPIRED
# ------------------------------------
@views.before_request
def check_session():

    if current_user.is_authenticated:

        from flask import session

        if not session.get("_permanent"):
            logout_user()

            flash(
                "Your session has expired. Please login again.",
                "warning"
            )

            return redirect(url_for("auth.login"))
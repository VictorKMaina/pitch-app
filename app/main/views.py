from flask import render_template, request, redirect, url_for, abort
import datetime
from . import main
from .forms import NewPitchForm, UpdateBioForm
from ..models import User, Pitch, Comment
from flask_login import login_required
from .. import db, photos
from flask_login import login_required, current_user
import markdown2

@main.route("/", methods = ["GET", "POST"])
@login_required
def index():
    """
    View function that returns root page
    """
    pitches = reversed(Pitch.query.all())
    form = NewPitchForm()

    if form.validate_on_submit():
        pitch = form.pitch.data
        time = datetime.datetime.now()
        category = form.category.data

        new_pitch = Pitch(pitch = pitch, likes = 0, dislikes = 0, time_posted = time, category = category)

        new_pitch.save()
        return redirect(url_for('main.index'))

    return render_template("index.html", new_pitch_form = form, pitches = pitches)
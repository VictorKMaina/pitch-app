from flask import render_template, request, redirect, url_for, abort
import datetime
from . import main
from .forms import NewPitchForm, UpdateBioForm
from ..models import User, Pitch, Comment
from flask_login import login_required
from .. import db, photos
from flask_login import login_required, current_user
import markdown2

def sort_id(pitch):
    # print("\n", pitch.id, "\n")
    return pitch.id
def add_likes(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    pitch.likes += 1
    db.session.commit()    

@main.route("/", methods = ["GET", "POST"])
def index():
    """
    View function that returns root page
    """
    pitches = Pitch.query.all()
    pitches.sort(key=sort_id, reverse = True)

    form = NewPitchForm()

    if form.validate_on_submit():
        pitch = form.pitch.data
        time = datetime.datetime.now()
        category = form.category.data

        new_pitch = Pitch(pitch = pitch, likes = 0, dislikes = 0, time_posted = time, category = category)

        new_pitch.save()
        return redirect(url_for('main.index'))

    return render_template("index.html", new_pitch_form = form, pitches = pitches)

@main.route("/likes", methods=['GET','POST'])
def likes():
    data = request.json["data"]

    print("\nLikes", data, "\n")

    add_likes(data[0])

    return "oops"
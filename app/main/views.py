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

def add_dislikes(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    pitch.dislikes += 1
    db.session.commit()

def add_comment(pitch_id, user_id, comment):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    time = datetime.datetime.now()
    new_comment = Comment(comment = comment, pitch_id = pitch_id, user_id = user_id)
    db.session.add(new_comment)
    db.session.commit()

@main.route("/", methods = ["GET", "POST"])
def index():
    """
    View function that returns root page
    """
    pitches = Pitch.query.all()
    pitches.sort(key=sort_id, reverse = True)
    pitch_form = NewPitchForm()

    if pitches == []:
        pitches = None

    comments = Comment.query.all()
    comments.sort(key=sort_id, reverse = True)

    if pitch_form.validate_on_submit():
        pitch = pitch_form.pitch.data
        user_id = current_user.id
        time = datetime.datetime.now()
        category = pitch_form.category.data

        new_pitch = Pitch(pitch = pitch, user_id = user_id, likes = 0, dislikes = 0, time_posted = time, category = category)

        new_pitch.save()
        return redirect(url_for('main.index'))

    return render_template("index.html", new_pitch_form = pitch_form, pitches = pitches, comments = comments)

@main.route("/likes", methods=['GET','POST'])
def likes():
    data = request.form["pitchId"]

    print("\nLikes ", data, "\n")
    add_likes(data[0])

    return redirect(request.referrer)

@main.route("/dislikes", methods=['GET','POST'])
def dislikes():
    data = request.form["pitchId"]

    print("\nDislikes ", data, "\n")
    add_dislikes(data[0])

    return redirect(request.referrer)

@main.route("/comments", methods=['GET','POST'])
def comments():
    data = request.form

    print("\nLikes ", data["pitchId"], "\n")

    add_comment(data["pitchId"], data["userId"], data["comment"])

    return redirect(request.referrer)

@login_required
@main.route("/account", methods=["GET", "POST"])
def account():
    pitches = Pitch.query.filter_by(user_id = current_user.id).all()
    pitches.sort(key=sort_id, reverse = True)

    bio_form = UpdateBioForm()
    username = current_user.user_name
    profile = current_user.profile_pic_path
    bio = current_user.bio

    if bio_form.validate_on_submit():
        current_user.bio = bio_form.bio.data

        db.session.commit()
        return redirect(request.referrer)

    return render_template("account.html", username = username, profile = profile, bio_form = bio_form, bio = bio, pitches = pitches)

@login_required
@main.route("/account/pic", methods=["POST"])
def new_pic():
    user = User.query.filter_by(id = current_user.id).first()

    if 'photo' in request.files:
        filename = photos.save(request.files["photo"])
        path = f"static/profile_pics/{filename}"
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for("main.account"))

@main.route("/category/<category>", methods=["GET", "POST"])
def categories(category):
    pitches = Pitch.query.filter_by(category = category).all()
    pitches.sort(key=sort_id, reverse = True)

    print("\n Category: ", category, "\n")

    if pitches == []:
        pitches = None

    comments = Comment.query.all()
    comments.sort(key=sort_id, reverse = True)

    return render_template("categories.html", pitches = pitches, comments = comments)
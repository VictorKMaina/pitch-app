from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .forms import SigninForm, SignupForm
from .. import db
from ..email import mail_message


@auth.route("/login", methods=["GET", "POST"])
def login():
    signup_form = SigninForm()
    if signup_form.validate_on_submit():
        user = User.query.filter_by(email=signup_form.email.data).first()
        if user is not None and user.verify_password(signup_form.password.data):
            login_user(user, signup_form.remember.data)
            return redirect(request.args.get("next") or url_for("main.index"))
        
        flash("Invalid username or Password")
    
    title = "Pitcher Login"
    return render_template("auth/login.html", signin_form = signup_form, title = title)

@auth.route("/sign-out")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route("/sign-in", methods = ["GET", "POST"])
def sign_in():
    form = SignupForm()

    if form.validate_on_submit():
        user = User(email = form.email.data, user_name = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to Pitcher", "email/welcome_user", user.email, user = user)

        return redirect(url_for("auth.sign_in"))

        title = "New Account"

    return render_template("auth/sign_in.html", signup_form = form)


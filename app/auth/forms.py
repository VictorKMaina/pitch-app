from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, EqualTo
import email_validator
from ..models import User
from wtforms import ValidationError

class SignupForm(FlaskForm):
    email = StringField("Your Email Address", validators=[Required(), Email()])
    username = StringField("Username", validators=[Required()])
    password = PasswordField("Password", validators=[Required(), EqualTo("confirm_password", message = "Password don't match")])
    confirm_password = PasswordField("Confirm Password", validators = [Required()])
    submit = SubmitField("Sign Up")

    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("There is an account with that email")

    def validate_username(self, data_field):
        if User.query.filter_by(user_name = data_field.data).first():
            raise ValidationError("That username is taken")
    
class SigninForm(FlaskForm):
    email = StringField("Your Email Address", validators = [Required(), Email()])
    password = PasswordField("Password", validators = [Required()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign In")

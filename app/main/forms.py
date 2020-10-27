from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required
from ..models import Category

class NewPitchForm(FlaskForm):
    pitch = TextAreaField("Write you idea here...", validators=[Required()])
    category = SelectField("Pick a category", choices=[Category.sales, Category.engagement, Category.product, Category.promotion, Category.pickup_lines, Category.interview, Category.project, Category.other],validators=[Required()])
    submit = SubmitField("Publish")

class UpdateBioForm(FlaskForm):
    bio = TextAreaField("Tell use about you.", validators = [Required()])
    submit = SubmitField("Submit")
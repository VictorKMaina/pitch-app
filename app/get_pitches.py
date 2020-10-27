from . import db
from .models import User, Comment, Pitch, Category

#list of all pitches as objects
pitches = Pitch.query.all()
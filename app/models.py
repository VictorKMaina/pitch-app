from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    """
    Return current user instance
    """
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    """
    Class for defining User instances
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), index = True)
    pass_secure = db.Column(db.String())
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    pitches = db.relationship("Pitch", backref="user")
    comments = db.relationship("Comment", backref="user")

    @property
    def password(self):
        """
        Raise AttributeError is password access is a attempted
        """
        raise AttributeError("You cannot access the password.")
    
    @password.setter
    def password(self, password):
        """
        Create hash of pass_secure property
        """
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        """
        Method to compare password hashes and check if they are the same
        """
        return check_password_hash(self.pass_secure, password)

    def save(self):
        """
        Method for commiting new user to database
        """
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"User {self.user_name}"

class Category:
    """
    Class for defining categories
    """
    sales = "Sales"
    engagement = "Engagement"
    product = "Product"
    promotion = "Promotion"
    pickup_lines = "Pickup_lines"
    interview = "Interview"
    project = "Project"
    other = "Other"



class Comment(db.Model):
    """
    Class for defining Comment instances
    """
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String, index = True)
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    time_posted = db.Column(db.DateTime())
    category = db.Column(db.String())
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def get_username(self):
        return User.query.filter_by(id = self.user_id).first().user_name
    def get_profile_pic(self):
        return User.query.filter_by(id = self.user_id).first().profile_pic_path

class Pitch(db.Model):
    """
    Class for defining Post instances
    """
    __tablename__ = "pitches"
    id = db.Column(db.Integer, primary_key = True)
    pitch = db.Column(db.String, index = True)
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    time_posted = db.Column(db.DateTime())
    category = db.Column(db.String())
    comments = db.relationship("Comment", backref="pitch")


    def get_username(self):
        return User.query.filter_by(id = self.user_id).first().user_name
    def get_profile_pic(self):
        return User.query.filter_by(id = self.user_id).first().profile_pic_path
    def save(self):
        """
        Method for commiting new pitch to database
        """
        db.session.add(self)
        db.session.commit()
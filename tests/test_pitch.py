import unittest
from app import db
from app.models import User, Pitch, Category
from datetime import datetime

class TestPitchClass(unittest.TestCase):
    """
    Test class for checking Pitch class methods
    """
    def setUp(self):
        """
        Runs before each test case
        """
        self.new_user = User(user_name="victormainak", email="contact@victormaina.com", password = "password", first_name="Victor", last_name="Maina", bio="Student at Moringa", profile_pic_path="/static/app-resources/pp.jpg")

        date = datetime(2020, 11, 17, 15, 3)

        self.new_pitch = Pitch(pitch="Are you the wind? Because you're blowing me away.", likes=40, dislikes=26, user_id = User.query.filter_by(user_name = "victormainak").first().id, user_name = User.query.filter_by(user_name  = "victormainak").first().user_name, profile_pic_path = User.query.filter_by(user_name = "victormainak").first().profile_pic_path, time_posted = date, category = Category.sales)

    def tearDown(self):
        """
        Runs after each test case
        """
        User.query.delete()
        Pitch.query.delete()

    def test_pitch_init(self):
        """
        Test case to check if Pitch instance is created
        """
        self.assertEquals(self.new_pitch.pitch, "Are you the wind? Because you're blowing me away.")
        self.assertEquals(self.new_pitch.likes, 40)
        self.assertEquals(self.new_pitch.dislikes, 26)
        self.assertEquals(self.new_pitch.user_id, self.new_user.id)
        self.assertEquals(self.new_pitch.user_name, self.new_user.user_name)
        self.assertEquals(self.new_pitch.profile_pic_path, self.new_user.profile_pic_path)
        self.assertEquals(self.new_pitch.time_posted, date)
        self.assertEquals(self.new_pitch.category, "sales")
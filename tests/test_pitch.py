import unittest
from app import db
from app.models import User, Pitch, Category
import datetime

class TestPitchClass(unittest.TestCase):
    """
    Test class for checking Pitch class methods
    """
    def setUp(self):
        """
        Runs before each test case
        """
        self.new_user = User(id=1, user_name="victormainak", email="contact@victormaina.com", password = "password", first_name="Victor", last_name="Maina", bio="Student at Moringa", profile_pic_path = "/static/app-resources/pp.jpg")

        self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.new_pitch = Pitch(pitch="Are you the wind? Because you're blowing me away.", likes=40, dislikes=26, user_id = User.query.filter_by(user_name = "victormainak").first().id, time_posted = self.time, category = Category.sales)

    def tearDown(self):
        """
        Runs after each test case
        """
        db.session.commit()

    def test_pitch_init(self):
        """
        Test case to check if Pitch instance is created
        """
        self.assertEquals(self.new_pitch.pitch, "Are you the wind? Because you're blowing me away.")
        self.assertEquals(self.new_pitch.likes, 40)
        self.assertEquals(self.new_pitch.dislikes, 26)
        self.assertEquals(self.new_pitch.user_id, self.new_user.id)
        self.assertEquals(self.new_pitch.time_posted, self.time)
        self.assertEquals(self.new_pitch.category, "sales")
    def test_get_username(self):
        """
        Test case to confirm that get_username() returns user_name property of User
        """
        self.assertEquals(self.new_pitch.get_username(), self.new_user.user_name)
    
    def test_get_profile_pic(self):
        """
        Test case to confirm that get_profile_pic() returns profile_pic_path property of User
        """
        self.assertEquals(self.new_pitch.get_profile_pic(), self.new_user.profile_pic_path)
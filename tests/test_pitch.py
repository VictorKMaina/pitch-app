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
        db.create_all()

        self.user = User(user_name = "testing", email = "vk13runic@gmail.com", password = "test", first_name = "Victor", last_name = "Maina", bio = "Student at Moringa", profile_pic_path = "/static/app-resources/pp.jpg")

        self.user.save()

        self.pitch = Pitch(pitch = "Are you the wind? Because you're blowing me away.", likes = 0, dislikes = 3, user_id = self.user.id, time_posted = "2020-11-17 03:30", category = Category.pickup_lines)


    def tearDown(self):
        """
        Runs after each test case
        """
        db.session.commit()
        db.drop_all()

    def test_pitch_instance(self):
        """
        Test case to check if User is instance is created
        """
        db.session.add(self.pitch)
        db.session.commit()

        self.assertIsNotNone(self.pitch.id)
        self.assertEqual(self.pitch.pitch,"Are you the wind? Because you're blowing me away.")
        self.assertEqual(self.pitch.likes, 0)
        self.assertEqual(self.pitch.dislikes, 3)
        self.assertEqual(self.pitch.time_posted, datetime.datetime(2020, 11, 17, 3, 30))

    def test_save(self):
        """
        Test if save method commits new pitch to database
        """
        test_pitch = Pitch(pitch = "Are you the wind? Because you're blowing me away.", likes = 34, dislikes = 43, user_id = 1, time_posted = "2020-11-17 03:30", category = Category.pickup_lines)

        # db.create_all()
        test_pitch.save()

        pitch = Pitch.query.filter_by(id = test_pitch.id).first()

        self.assertEqual(pitch.pitch, "Are you the wind? Because you're blowing me away.")
        self.assertIsNotNone(pitch.user_id)

    def test_get_username(self):
        """
        Test case to see if get_username method returns username associated with pitch
        """
        self.pitch.save()

        username = self.pitch.get_username()

        self.assertEqual(User.query.filter_by(id = self.user.id).first().user_name, username)
    
    def test_get_profile_pic(self):
        """
        Test case to see if get_profile_pic method returns profile pic of user associated with pitch
        """
        self.pitch.save()

        profile_pic_path = self.pitch.get_profile_pic()

        self.assertEqual(User.query.filter_by(id = self.user.id).first().profile_pic_path, profile_pic_path)
    

    
    def test_add_likes_dislikes(self):
        """
        Test case to check if method adds like and dislike to database
        """
        self.pitch.save()
        self.pitch.add_likes()
        self.pitch.add_dislikes()

        self.assertEqual(self.pitch.likes, 1)
        self.assertEqual(self.pitch.dislikes, 4)
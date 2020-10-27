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
        self.pitch = Pitch(pitch = "Are you the wind? Because you're blowing me away.", likes = 34, dislikes = 43, time_posted = "2020-11-17 03:30", category = Category.pickup_lines)


    def tearDown(self):
        """
        Runs after each test case
        """
        # User.query.filter_by(id = self.user_id).delete()

    def test_pitch_instance(self):
        """
        Test case to check if User is instance is created
        """
        db.session.add(self.pitch)
        db.session.commit()

        self.assertIsNotNone(self.pitch.id)
        self.assertEqual(self.pitch.pitch,"Are you the wind? Because you're blowing me away.")
        self.assertEqual(self.pitch.likes, 34)
        self.assertEqual(self.pitch.dislikes, 43)
        self.assertEqual(self.pitch.time_posted, datetime.datetime(2020, 11, 17, 3, 30))
import unittest
from app.models import User, Comment, Pitch, Category
from app import db
import datetime

class TestCommentClass(unittest.TestCase):
    """
    Test class to check Comment class methods

    Args:
        unittest.TestCase: Inherit from unittest.TestCase
    """

    def setUp(self):
        """
        Runs before each test case
        """
        db.create_all()

        self.user = User(user_name = "testing", email = "vk13runic@gmail.com", password = "test", first_name = "Victor", last_name = "Maina", bio = "Student at Moringa", profile_pic_path = "/static/app-resources/pp.jpg")

        self.user.save()

        self.pitch = Pitch(pitch = "Are you the wind? Because you're blowing me away.", likes = 0, dislikes = 3, user_id = self.user.id, time_posted = "2020-11-17 03:30", category = Category.pickup_lines)

        self.pitch.save()

        self.comment = Comment(comment="I love this idea!", pitch_id= self.pitch.id, user_id= self.user.id)

    def tearDown(self):
        """
        Runs after each test case
        """
        db.session.commit()
        db.drop_all()

    def test_comment_instance(self):
        """
        Test class to check Comment class methods
        
        Args:
            unittest.TestCase: Inherit from unittest.TestCase
        """
        db.session.add(self.comment)
        db.session.commit()

        self.assertIsNotNone(self.comment.id)
        self.assertEqual(self.comment.comment,"I love this idea!")
        self.assertEqual(self.comment.pitch_id, self.pitch.id)
        self.assertEqual(self.comment.user_id, self.user.id)

    def test_get_username(self):
        """
        Test case to see if get_username method returns username associated with comment
        """
        db.session.add(self.comment)
        db.session.commit()

        username = self.comment.get_username()

        self.assertEqual(User.query.filter_by(id = self.user.id).first().user_name, username)
    
    def test_get_profile_pic(self):
        """
        Test case to see if get_profile_pic method returns profile pic of user associated with comment
        """
        db.session.add(self.comment)
        db.session.commit()

        profile_pic_path = self.comment.get_profile_pic()

        self.assertEqual(User.query.filter_by(id = self.user.id).first().profile_pic_path, profile_pic_path)
from app.models import User
from app import db
import unittest

class UserClassTest(unittest.TestCase):
    """
    Test class to check User class methods

    Args:
        unittest.TestCase: Inherit from unittest.TestCase
    """
    def setUp(self):
        """
        Runs before each test case
        """
        self.new_user = User(user_name="victormainak", email="contact@victormaina.com", password = "password", first_name="Victor", last_name="Maina", bio="Student at Moringa", profile_pic_path="/static/app-resources/pp.jpg")

    def tearDown(self):
        """
        Run after each test case
        """
        User.query.delete()
    
    def test_user_instance(self):
        """
        Check if User instance is created correctly
        """
        self.assertEquals(self.new_user.user_name, "victormainak")
        self.assertEquals(self.new_user.first_name, "Victor")
        self.assertEquals(self.new_user.last_name, "Maina")
        self.assertEquals(self.new_user.bio, "Student at Moringa")
        self.assertEquals(self.new_user.profile_pic_path, "/static/app-resources/pp.jpg")
    def test_save(self):
        """
        Test case to check if save method commits user to database
        """
        self.new_user.save()

        check_user = User.query.filter_by(id = self.new_user.id).first()
        self.assertEquals(self.new_user, check_user)

    def test_verify_password(self):
        """
        Test case to see if password is verified
        """
        self.assertTrue(self.new_user.verify_password("password"))
        self.assertFalse(self.new_user.verify_password("wrong password"))
from app.models import User
from app import db
import unittest
from werkzeug.security import generate_password_hash, check_password_hash


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
        self.user = User(user_name = "victormainak", email = "vk13runic@gmail.com", password = "test", first_name = "Victor", last_name = "Maina", bio = "Student at Moringa", profile_pic_path = "/static/app-resources/pp.jpg")

    def tearDown(self):
        """
        Run after each test case
        """
        # User.query.filter_by(id = self.user.id).delete()

    def test_user_instance(self):
        """
        Test case to check if User is instance is created
        """
        # db.create_all()
        db.session.add(self.user)
        db.session.commit()

        self.assertIsNotNone(self.user.id)
        self.assertEqual(self.user.user_name, "victormainak")
        self.assertEqual(self.user.email, "vk13runic@gmail.com")
        self.assertTrue(check_password_hash(self.user.pass_secure, "test"))
        self.assertEqual(self.user.first_name, "Victor")
        self.assertEqual(self.user.last_name, "Maina")
        self.assertEqual(self.user.bio, "Student at Moringa")
        self.assertEqual(self.user.profile_pic_path, "/static/app-resources/pp.jpg")

    def test_verify_password(self):
        """
        Test case to if password is verified
        """
        self.assertTrue(self.user.verify_password("test"))

    def test_save(self):
        """
        Test case to check if save method posts to database
        """
        test_user = User(user_name = "victormainak", email = "vk13runic@gmail.com", password = "test", first_name = "Victor", last_name = "Maina", bio = "Student at Moringa", profile_pic_path = "/static/app-resources/pp.jpg")

        # db.create_all()
        test_user.save()

        username = User.query.filter_by(id = test_user.id).first()
        print(username.user_name)

        self.assertEqual(username.user_name, "victormainak")
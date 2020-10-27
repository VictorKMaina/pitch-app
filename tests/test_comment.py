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

    def tearDown(self):
        """
        Runs after each test case
        """

    def test_comment_instance(self):
        """
        Test class to check Comment class methods
        
        Args:
            unittest.TestCase: Inherit from unittest.TestCase
        """
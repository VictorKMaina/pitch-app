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

    def tearDown(self):
        """
        Runs after each test case
        """
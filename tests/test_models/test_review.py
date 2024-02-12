#!/usr/bin/python3
"""Testing Review module."""
import unittest
import pep8
from models.review import Review

class Review_testing(unittest.TestCase):
    """Check BaseModel."""

    def testpep8(self):
        """ testing codestyle """
        pepstyle = pep8.StyleGuide(quiet=True)
        path = 'models/review.py'
        result = pepstyle.check_files([path])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

#!/usr/bin/python3
"""Testing Place."""
import unittest
import pep8
from models.place import Place

class Place_testing(unittest.TestCase):
    """Check BaseModel."""

    def testpep8(self):
        """Testing style."""
        pepstyle = pep8.StyleGuide(quiet=True)
        path = 'models/place.py'
        result = pepstyle.check_files([path])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")i

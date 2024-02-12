#!/usr/bin/python3
"""Test Amenity module."""
import unittest
import pep8
from models.amenity import Amenity

class Amenity_testing(unittest.TestCase):
    """Check BaseModel."""

    def testpep8(self):
        """testing style."""
        pepstyle = pep8.StyleGuide(quiet=True)
        path = 'models/amenity.py'
        result = pepstyle.check_files([path])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

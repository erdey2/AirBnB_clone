#!/usr/bin/python3
"""Testing city module."""
import unittest
import pep8
from models.city import City

class City_testing(unittest.TestCase):
    """Check BaseModel."""

    def testpep8(self):
        """ testing codestyle """
        pepstyle = pep8.StyleGuide(quiet=True)
        path = 'models/city.py'
        result = pepstyle.check_files([path])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

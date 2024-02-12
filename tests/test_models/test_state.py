#!/usr/bin/python3
"""test state module."""
import unittest
import pep8
from models.state import State


class State_test(unittest.TestCase):
    """check BaseModel."""

    def testpep8(self):
        """testing style."""
        pepstyle = pep8.StyleGuide(quiet=True)
        path = 'models/state.py'
        result = pepstyle.check_files([path])
        self.assertEqual(result.total_errors, 0, 
                "found code style errors (and warnings).")

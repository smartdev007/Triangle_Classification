"""
    @author Jenish Kevadia

    Script imports methods from 'HWO1_Jenish_Kevadia.py' script and implements test cases for the type of triangle
"""

import unittest
from HW01_Jenish_Kevadia import classify_triangle, check_input

class TestTriangle(unittest.TestCase):
    """ Test cases """

    def test_classify_triangle(self):
        """ Test case to check the type of triangle"""

        self.assertEqual(classify_triangle(3, 3, 3), ('Equilateral'))
        self.assertEqual(classify_triangle(2, 4, 2), ('Isosceles'))
        self.assertEqual(classify_triangle(3, 4, 5), ('Scalene and Right triangle'))

    def test_classify_triangle_string(self):
        """ Test for string input """
        self.assertEqual(classify_triangle('a', 1, 2), ('Isosceles')) 

    def test_classify_triangle_blank(self):
        """ Test for blank input """
        self.assertEqual(classify_triangle(1, '', 4), ('Scalene'))

    def test_classify_triangle_negative(self):
        """ Test for negative input """
        self.assertEqual(classify_triangle(4, 6, -2), ('Scalene'))


if __name__ == "__main__":
    """ Run test cases on startup """
    unittest.main(exit=False, verbosity=2)
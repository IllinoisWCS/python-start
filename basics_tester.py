'''
DON'T CHANGE ANYTHING IN THIS FILE
'''

import unittest
from basics import Basics as basic
# This creates an object with all the functions we created
b = basic()

class TestBasicMethods(unittest.TestCase):

    def test_addition(self):
        print('Test addition function')
        self.assertTrue(b.addition(1, 1) == 2)
        self.assertTrue(b.addition(-5, -5) == -10)

    def test_pythag(self):
        print('Test Pythagorean theorem function')
        self.assertTrue(b.pythagorean_theorem(b = 4, c = 5) == 3)
        self.assertTrue(b.pythagorean_theorem(a = 3, c = 5) == 4)
        self.assertTrue(b.pythagorean_theorem(a = 3, b = 4) == 5)
        self.assertTrue(b.pythagorean_theorem() == False)

    def test_string_count(self):
        print('Test string count function')
        self.assertTrue(b.string_count('abc acb abc bca cab abc', 'abc') == 3)
        self.assertTrue(b.string_count('abc acb abc bca cab abc', 'abasdfc') == 0)

    def test_min_value(self):
        print('Test min value function')
        self.assertTrue(b.min_value([5, 8, 2, 0, 4, 3, 2]) == 0)

    def test_max_value(self):
        print('Test max value function')
        self.assertTrue(b.max_value([5, 8, 2, 0, 4, 3, 2]) == 8)

    def test_average_value(self):
        print('Test average function')
        self.assertTrue(b.average([4, 0, 2, 3, 0, 3]) == 2)

    def test_median_value(self):
        print('Test median function')
        self.assertTrue(b.median([5, 8, 2, 0, 4, 3, 2]) == 3)
        self.assertTrue(b.median([5, 8, 2, 0, 3, 3]) == 3)

if __name__ == '__main__':
        unittest.main()

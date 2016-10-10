'''
DON'T CHANGE ANYTHING IN THIS FILE
'''

import unittest
from basics import Basics as basic
# This creates an object with all the functions we created
b = basic()

class TestBasicMethods(unittest.TestCase):

    def test_addition(self):
        self.assertTrue(b.addition(1, 1) == 2)
        self.assertTrue(b.addition(-5, -5) == -10)
        print('Addition Success')

    def test_pythag(self):
        self.assertTrue(b.pythagorean_theorem(b = 4, c = 5) == 3)
        self.assertTrue(b.pythagorean_theorem(a = 3, c = 5) == 4)
        self.assertTrue(b.pythagorean_theorem(a = 3, b = 4) == 5)
        self.assertTrue(b.pythagorean_theorem() == False)
        print('Pythagorean Theorem success')

    def test_string_count(self):
        self.assertTrue(b.string_count('abc acb abc bca cab abc', 'abc') == 3)
        self.assertTrue(b.string_count('abc acb abc bca cab abc', 'abasdfc') == 0)
        print('String count function')

    def test_min_value(self):
        self.assertTrue(b.min_value([5, 8, 2, 0, 4, 3, 2]) == 0)
        print('Min value function')

    def test_max_value(self):
        self.assertTrue(b.min_value([5, 8, 2, 0, 4, 3, 2]) == 8)
        print('Max value function')

    def test_average_value(self):
        self.assertTrue(b.average([4, 0, 2, 3, 0, 3]) == 2)
        print('Average function')

    def test_median_value(self):
        self.assertTrue(b.median([5, 8, 2, 0, 4, 3, 2]) == 3)
        self.assertTrue(b.median([5, 8, 2, 0, 3, 3]) == 3)
        print('Median function')

if __name__ == '__main__':
        unittest.main()

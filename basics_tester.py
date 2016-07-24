'''
DON'T CHANGE ANYTHING IN THIS FILE
'''

import unittest
from basics_solution import Basics as basic
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

if __name__ == '__main__':
        unittest.main()

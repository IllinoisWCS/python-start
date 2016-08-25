'''
DON'T CHANGE ANYTHING IN THIS FILE
'''

import unittest
from intermediate import Intermediate as intermediate
# This creates an object with all the functions we created
b = intermediate()

class TestIntermediateMethods(unittest.TestCase):
    def test_dictionary(self):
        book_index = {
            apples: [2, 5, 64, 66, 70],
            oranges: [3, 6, 63, 64, 70],
            grapes: [3, 4, 5, 50, 64]
        }
        self.assertTrue(b.dictionary_exercise(book_index, 'apples', 'oranges') == [64,70])
        print('Dictionary Success')

if __name__ == '__main__':
        unittest.main()

'''
DON'T CHANGE ANYTHING IN THIS FILE
'''

import unittest
from intermediate import Intermediate as intermediate
# This creates an object with all the functions we created
b = intermediate()

class TestIntermediateMethods(unittest.TestCase):
    def test_dictionary(self):
        print('Test dictionary function')
        book_index = {
            apples: [2, 5, 64, 66, 70],
            oranges: [3, 6, 63, 64, 70],
            grapes: [3, 4, 5, 50, 64]
        }
        self.assertTrue(b.dictionary_exercise(book_index, 'apples', 'oranges') == [64,70])

    def test_calculate_GPA_CSV(self):
        print('Test calculate GPA function')
        gpa = b.calculate_GPA_CSV('data/GPAData/gpadata.csv')
        self.assertTrue(round(gpa, 2) == 3.52)

    def test_calculate_statistics(self):
        print('Test calculate statistics function')
        average, max_gdp, min_gdp, country_with_highest_gdp, country_with_lowest_gdp, variance, standard_deviation = b.calculate_statistics('data/GDPData/GDPData.csv')
        self.assertTrue(abs(average - 4.452496609*(10 ** 11)) <= 1)
        self.assertTrue(abs(max_gdp - 1.7946996*(10**13)) <= 1)
        self.assertTrue(country_with_highest_gdp == "United States")
        self.assertTrue(abs(min_gdp - 145237022.012) <= 1)
        self.assertTrue(country_with_lowest_gdp == "Kiribati")
        self.assertTrue(abs(variance - 4.90159965423*(10**26)) <= 4*(10**13))
        self.assertTrue(abs(standard_deviation - 2.21395565769*(10**13)) <= 100)

if __name__ == '__main__':
    unittest.main()

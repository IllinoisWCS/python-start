from math import sqrt

class Basics:
    '''
    Let's start off simple. Fill in this function so that it takes two parameters and returns the sum of those two.
    '''

    def addition(self, a, b):
        return a + b



    '''
    If you got past that, let's create a function for some math formulas you may have learned in the past

    Pythagorean Theorem, used to calculate the length of a missing side of a right triangle (one with a single 90 degree angle) commonly notated as a^2 + b^2 = c^2

    Let's try to get a bit fancier by allowing a user to specify which parameters they have so we don't have to create multiple functions depending on which triangle side is missing
    '''

    def pythagorean_theorem(self, a = None, b = None, c = None):
        # We should detect and reassign 'missing_side' with which parameter is missing so we can calculate it
        missing_side = None

        # Do you understand how this works?
        # Helpful: elif stands for 'else if'
        if a == None and b != None and c != None:
            missing_side = 'a'
            print 'a is missing'
        elif a != None and b == None and c != None:
            missing_side = 'b'
            print 'b is missing'
        elif a != None and b != None and c == None:
            missing_side = 'c'
            print 'c is missing'
        else:
            print 'Your parameters seem wrong... Perhaps you should see what you entered'
            return False

        # Once we know which side is missing, we should calculate and return the result
        # Helpful: the ** operator does exponents, e.g. 2**2 is 4
        # P.S. you can use decimal numbers with **
        if missing_side == 'a':
            return sqrt(c**2 - b**2)
        elif missing_side == 'b':
            return sqrt(c**2 - a**2)
        else:
            return sqrt(a**2 + b**2)


    '''
    If you've mastered the Pythagorean theorem, let's try to use some Python data structures to solve some problems

    Write a function that takes a source string and a target string and returns how many times the target is found in the string.

    e.g. if the source string is
    "There are many times of apples. Granny Smith apples, Fuji apples, and Red Delicious apples are just a few."
    and the target string is "apples" , the function would return 4

    Things to research that may help you:
        - str.split() https://docs.python.org/2/library/stdtypes.html#str.split
        - for loops
    '''

    def string_count(self, source, target):
        return source.count(target)

    '''
    Since this tutorial is mainly about data science, let's figure out some ways to calculate some statistics using some built-in methods for Python. The next few functions all take in an array of numbers.

    An array is just a list of items with a fixed order, all of which have the same data type. We specify the array of numbers as type int. In Python, it will be noted like this: [1, 3, 4, 6, 2]

    Calculate:
        - the minimum value
        - the maximum value
        - the average
        - the median

    Things to research that may help you:
        - max(), min()
        - sorted()
        - len()
        - array indexing in python - how to access an element at position j, j being some number you specify
    '''

    def min_value(self, values):
        return min(values)

    def max_value(self, values):
        return max(values)

    def average(self, values):
        return sum(values) / len(values)

    def median(self, values):
        return sorted(values)[len(values) / 2]

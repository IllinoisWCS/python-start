# This imports the file that we worked in
from basics_solution import Basics as basic
# This creates an object with all the functions we created
b = basic()


assert(b.addition(1, 1) == 2)
assert(b.addition(-5, -5) == -10)
print('Addition Success')

assert(b.pythagorean_theorem(b = 4, c = 5) == 3)
assert(b.pythagorean_theorem(a = 3, c = 5) == 4)
assert(b.pythagorean_theorem(a = 3, b = 4) == 5)
assert(b.pythagorean_theorem() == False)
print('Pythagorean Theorem success')

assert(b.string_count('abc acb abc bca cab abc', 'abc') == 3)
assert(b.string_count('abc acb abc bca cab abc', 'abasdfc') == 0)
print('String count function')


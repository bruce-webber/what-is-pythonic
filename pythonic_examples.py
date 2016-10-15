"""
Examples of Pythonic coding. This file is not intended to be executed from
the command line; instead, copy and paste these examples into a
Python interpreter to execute them.
"""

# Variables we'll use below -------------------------------

# A string.
s = 'this is a string'

# A list.
animals = ['dog', 'cat', 'mouse', 'cow']

# A dictionary.
state_capitals = {
    'Arizona': 'Phoenix',
    'Colorado': 'Denver',
    'Michigan': 'Lansing',
    'New York': 'Albany',
}

# Slices --------------------------------------------------

s[2]           # 'i'
s[2:9]         # 'is is a'
animals[1]     # 'cat'
animals[1:3]   # ['cat', 'mouse']
s[2:]          # 'is is a string'
s[0:2]         # 'th'
s[:2]          # 'th'
s[-1]          # 'g'
s[2:-1]        # 'is is a strin'
s[2:len(s)-1]  # also returns 'is is a strin' but is harder to read

# A string representing a date.
date_str = '20161015'
date_str[0:4]  # '2016'
date_str[4:6]  # '10'
date_str[6:]   # '15'

# Iteration -----------------------------------------------

# Print each item in a list - not Pythonic.
n = 0
while n < len(animals):
    print animals[n]
    n += 1

# Print each item in a list - Pythonic.
for animal in animals:
    print animal

# Print the first 7 even numbers - not Pythonic.
n = 1
while n <= 7:
    print n * 2
    n += 1

# Print the first 7 even numbers - Pythonic.
for n in range(7):
    print (n + 1) * 2

# Iterating over a list gives the elements.
for animal in animals:
    print animal

# Iterating over a string gives the characters.
for c in s:
    print c

# Iterating over a dictionary gives the keys.
for state in state_capitals:
    print state, state_capitals[state]

# Tests ---------------------------------------------------

# Use "in" to test for inclusion.
'r' in s

if 'r' in s:
    print 'The letter "r" is there'

'x' in s

'cat' in animals

'Ohio' in state_capitals

# Python truthiness - see https://docs.python.org/2.4/lib/truth.html

# This also works, but is deprecated - not Pythonic.
state_capitals.has_key('Ohio')

# Tuples --------------------------------------------------

# The comma is the tuple operator.
t = 2, 3

# For readability, enclose a tuple in parentheses.
u = (5, 12, 17)

# If you write a single-element tuple with parentheses, don't forget the comma!
v = (23,)

# Using a working variable to swap values - not Pythonic.
a = 1
b = 2
temp = a
a = b
b = temp

# Tuple unpacking can be used to swap values - Pythonic.
a = 1
b = 2
(a, b) = (b, a)


# Tuple unpacking can be used to return multiple values from a function.
def sum_and_product(x, y):
    return (x+y, x*y)

sum, prd = sum_and_product(3, 4)

# Creating lists ------------------------------------------

# Adding 3 to each element in a list - not Pythonic.
some_numbers = [2, 3, 7, 0]
n = 0
while n < len(some_numbers):
    some_numbers[n] = some_numbers[n] + 3
    n = n + 1

# Use list comprehension instead - Pythonic.
some_numbers = [2, 3, 7, 0]
some_numbers = [i + 3 for i in some_numbers]

# Another example - a list of strings with extra whitespace.
alist = ['dog ', '  cat ', 'mouse']
alist = [i.strip() for i in alist]

# Concatenating a list into a string using join() - Pythonic.
list_of_animals = ', '.join(animals)

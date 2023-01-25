"""
Python Data Structures - A Game-Based Approach
Stack challenge
Robin Andrews - https://compucademy.net/
"""

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# Your solution here.

# The smart way:
# reversed_string = string[::-1]

# The dumb way:

for char in string:
    s.push(char)
while not s.is_empty():
    reverse_string += s.pop()


print(reversed_string)

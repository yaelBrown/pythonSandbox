"""
Python builtin debugger module
"""

import pdb

x = [1,2,3]
y = 2
z = 3

res = y + z
print(res)

pdb.set_trace()
"""
can pass in variable names to check the values at this point
https://docs.python.org/3/library/pdb.html
"""

res2 = y + x # code will generate TypeError, cannot add string to a list. Can add string into a list.
print(res2)
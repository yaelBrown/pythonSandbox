import timeit

# For loop
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

# List comprehension
timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)

# Map()
timeit.timeit('"-".join(map(str, range(100)))', number=10000)



# map function is significantly faster
"""
%timeit (function expression)
  magic function in jupyter notebook
"""
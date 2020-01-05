'''
1,1,2,3,5,8,13

Write a function to return the nTh term of Fibonacci Sequence

(some people argue that the sequence should start with 0 or one)
'''

# def fibonacci(n):
#   if n == 1:
#     return 1
#   elif n == 2:
#     return 1
#   elif n > 2:
#     return fibonacci(n-1) + fibonacci(n-2)


# for n in range(1, 11):
#   print(n, ":", fibonacci(n))

'''
Memoization - Store the values from recent function calls so future calls do not have to repeat the work
'''

# Implement explicitly

fibonacci_cache = {}
fib_preload = {1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55, 11: 89, 12: 144, 13: 233, 14: 377, 15: 610, 16: 987, 17: 1597, 18: 2584, 19: 4181, 20: 6765, 21: 10946, 22: 17711, 23: 28657, 24: 46368, 25: 75025, 26: 121393, 27: 196418, 28: 317811, 29: 514229}

def fibonacci_mem_impl(n):
  # If we have cached value then return it
  # the n represents the key in the dictionary, not the value
  if n in fibonacci_cache:
    return fibonacci_cache[n]

  # Compute the Nth term
  if n == 1:
    value = 1
  elif n == 2:
    value = 1
  elif n > 2:
    value = fibonacci_mem_impl(n-1) + fibonacci_mem_impl(n-2)

  # cache the value and return it
  fibonacci_cache[n] = value
  return value

for n in range(1, 30):
  print(n, ":", fibonacci_mem_impl(n))

if 10 in fib_preload:
  print(fib_preload[10])

# using lru_cache (lru = least recently used)
# clarity over compactness

from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci_mem_lrucache(n):
  # check that the input is a positive integer
  if type(n) != int:
    raise TypeError("n must be a positive int")
  if n < 1:
    raise ValueError("n must be a positive int")

  if n == 1:
    return 1
  elif n == 2:
    return 1
  elif n > 2:
    return fibonacci_mem_lrucache(n-1) + fibonacci_mem_lrucache(n-2)

# golden ratio - two quantities are in the golden ratio if their ratio is the same as the ratio of their sum to the larger of the two quantities.
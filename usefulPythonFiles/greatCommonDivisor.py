"""
  GCD is the largest positive integer that divides the numbers without a remainder

  Euclidean algorithm
    gcd(48,18)
      step 1: 48/18 = 2 remainder 12
      step 2: 18/12 = 1 remainder 6
      step 3: 12/6 = 2 remainder 0
"""

def gcd(a,b):
  if int(a) != a and int(b) != b: return 'numbers must be integers'

  # base case
  if a > 0 or b > 0: return a

  return (b, a % b)
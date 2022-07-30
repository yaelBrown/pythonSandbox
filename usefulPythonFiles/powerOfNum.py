"""
  Find the power of a number
"""

# recursive impl
def power(base, exp):
  
  # unconditional/constraint
  if base < 0 or exp < 0 and int(exp) == exp: return 'must be positive integer only'

  # base case
  if exp == 0: 
    return 1
  if exp == 1: 
    return base
  
  return (base * base) * power(exp, (exp - 1))
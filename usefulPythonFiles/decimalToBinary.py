"""
  Convert a number from decimal to binary

  Step 1: Divide the number by 2
  Step 2: Get the integer quotient for the next iteration
  Step 3: Get the remainder for the binary digit
  Step 4: Repeat the steps until the quotient is equal to 0

  10 to binary 1010

  Div by  quotient  remainder
  10/2    5         0
  5/2     2         1         101 * 10 + 0 1010
  2/2     1         0         10 * 10 + 1 = 101
  1/2     0         1         1 * 10 + 0 = 10
"""


def decimialToBinary(n): 
  # unintentional case
  if int(n) != n: return 'n must be an integer'

  # base case
  if n == 0: return n

  return n % 2 + 10 * decimialToBinary(n/2)
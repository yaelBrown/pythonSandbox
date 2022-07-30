"""
  A method calls itself
  Exit from infinite loop

  Sum of digits in a number: 
    111 = 3
    1234 = 10 
    1+2+3+4 == 10
"""


# recursive impl
def sumOfDigits(n):
  # verify number is positive
  if n < 0: 
    return 0

  # handles constraint (base condition)
  if n == 0:
    return 0
  else: 
    return n % 10 + sumOfDigits(n / 10)







import functools

def generalizedGCD(num, arr): 
  def _gcd(a, b):
    while b > 0:
      a, b = b, a % b
    return a

  return functools.reduce(_gcd, arr)





if __name__ == "__main__":
  print(generalizedGCD())
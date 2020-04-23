import math

def func(a):
  return math.pow(a,2) - (6 * a) + 5

for x in range(-2,6):
  aa = func(x)
  print(f"{x}  {aa}")
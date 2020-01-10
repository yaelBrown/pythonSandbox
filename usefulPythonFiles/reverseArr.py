"""
This is not a kata, just wanted to reverse an array with out a built in method.
"""

def reverseArr(l):
  count = len(l) - 1
  out = []

  while count >= 0:
    out.append(l[count])
    count -= 1

  return out


t = [1,2,3,4,5]

print(reverseArr(t))
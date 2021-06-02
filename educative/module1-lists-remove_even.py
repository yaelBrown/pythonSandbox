# remove even numbers in a list and return the odds

def remove_even(lst):
  out = []
  
  for i in lst: 
    if not (i % 2) == 0:
      out.append(i)
  
  return out


# using list comprehensions (pythonic)
def remove_evenlc(lst):
  return [n for n in lst if not (i % 2) == 0]


print(remove_even([-42, -54, -128, -94, -162, 122, -153, 114, 4, -118, -62, 52, -139, -51, 160, -126, -135, -111, -1, 78, -89, -115, -38, 128, 94, -26, -88, 39, -180, -151, 109, 111, -158, 146, 166, 12, -56, -195, -138, -61, 68, -71, -98, -11, 87, 158, 36, 30, -164, 34, 129, -30, -156, 60, 120, -48, -152, 110, 199, -36, 169, 83, 180, -21, 143, 11, 104, 108]))

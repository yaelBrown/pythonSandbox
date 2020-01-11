from collections import defaultdict

d = {"a": 1}

# d["b"] # will generate KeyError, "b" is not defined in dictionary.


# using defaultdict
d2 = defaultdict(object) # calling in object

d2['one'] # add the key of one, thats type object

# print everything in d2
for item in d2:
  print(item)

d3 = defaultdict(lambda : 0) # if there is no assignment for key, will assign 0
# lambda is like anonymous function

d3["one"] # creates key with value 0


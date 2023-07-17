
def common_elements(tuple1, tuple2):
  out = []
  for i in tuple1:
    if i in tuple2:
      out.append(i)
  
  return tuple(out)            
    

# '&' Intersection operator
def common_elements(tuple1, tuple2):
  return tuple(set(tuple1) & set(tuple2))


"""
Explanation

    def common_elements(tuple1, tuple2): - Define a function called "common_elements" that takes two tuples "tuple1" and "tuple2" as arguments.

    return tuple(set(tuple1) & set(tuple2)) - Convert both input tuples into sets using the set() constructor, then use the set intersection operator & to find the common elements between the two sets. Convert the resulting set of common elements back to a tuple and return it.

Time and Space Complexity

    def common_elements(tuple1, tuple2): - Define a function called "common_elements" that takes two tuples "tuple1" and "tuple2" as arguments. No time or space complexity associated with this line as it is just a function definition.

    return tuple(set(tuple1) & set(tuple2)) - This line creates two sets from the input tuples using the set() constructor, and then computes the set intersection using the & operator. The time complexity of creating each set is O(n), where n is the length of the input tuple. The time complexity of computing the set intersection is O(min(n,m)), where m is the length of the second input tuple. Since the two input tuples are of equal length, the overall time complexity of the function is O(n). The space complexity is also O(n) because the size of the resulting set will be no larger than the size of the smaller of the two input tuples.

Therefore, the overall time complexity of the function is O(n), and the overall space complexity is also O(n), where n is the length of the input tuples.

"""
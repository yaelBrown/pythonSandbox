my_dict = {'a': 5, 'b': 9, 'c': 2}


# for k,v in my_dict.items():
#     print(str(k) + ": " + str(v))



def max_value_key(my_dict):
    # TODO
    maxV = 0
    maxK = 0
    for k,v in my_dict.items():
        if v > maxV: 
            maxK = k 
            maxV = v
    return maxK
    
print(max_value_key(my_dict))



# Correct answer
def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)


"""
  Explanation:

    Call the built-in max() function with the dictionary my_dict as its first argument and key=my_dict.get as its second argument.

    The max() function iterates through the keys in the dictionary and compares the values associated with each key using the get() method. The key parameter specifies a custom function to extract a comparison key from each dictionary key. In this case, the get() method returns the value associated with each key, so the max() function compares the values of the dictionary.

    The time complexity of the max() function is O(n), where n is the number of elements in the dictionary my_dict. The max() function iterates through all the keys in the dictionary once, and the get() method has an average time complexity of O(1).

    Return the key with the highest value found by the max() function.

  Time complexity:

    The overall time complexity of this function is O(n), where n is the number of elements in the dictionary my_dict. This is determined by the max() function, which iterates through all the keys in the dictionary.

  Space complexity:

    The space complexity of this function is O(1), as it does not create any additional data structures or store any intermediate values. The max() function only keeps track of the current maximum value and its corresponding key, which requires constant space.

"""
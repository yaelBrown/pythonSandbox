def max_product(arr):
    # Initialize two variables to store the two largest numbers
    max1, max2 = 0, 0  # O(1), constant time initialization
  
    # Iterate through the array
    for num in arr:  # O(n), where n is the length of the array
        # If the current number is greater than max1, update max1 and max2
        if num > max1:  # O(1), constant time comparison
            max2 = max1  # O(1), constant time assignment
            max1 = num  # O(1), constant time assignment
        # If the current number is greater than max2 but not max1, update max2
        elif num > max2:  # O(1), constant time comparison
            max2 = num  # O(1), constant time assignment
  
    # Return the product of the two largest numbers
    return max1 * max2  # O(1), constant time multiplication
  
arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))  # Output: 63 (9*7)


"""
    def max_product(arr):

        Define a function named max_product that takes an input array arr.

    max1, max2 = 0, 0

        Initialize two variables, max1 and max2, to store the two largest numbers in the array. Set both variables to 0 initially.

    for num in arr:

        Iterate through the elements of the input array arr using a for loop. num represents the current element of the array.

    if num > max1:

        Check if the current number num is greater than the current maximum value max1.

    max2 = max1

        If the condition in line 4 is True, update the second-largest number max2 by assigning it the value of the current largest number max1.

    max1 = num

        Update the largest number max1 by assigning it the value of the current number num.

    elif num > max2:

        If the condition in line 4 is False, check if the current number num is greater than the current second-largest number max2.

    max2 = num

        If the condition in line 7 is True, update the second-largest number max2 by assigning it the value of the current number num.

    return max1 * max2

        After the loop has finished iterating through the array, return the product of the two largest numbers, max1 and max2.

"""
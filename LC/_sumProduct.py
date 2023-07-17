
def sum_product(input_tuple):
    prod = 1
    s = 0
    
    for i in input_tuple: 
        s += i
        prod *= i
        
    return s, prod
    
def sum_product(t):
    sum_result = 0
    product_result = 1
  
    for num in t:
        sum_result += num
        product_result *= num
  
    return sum_result, product_result
  
input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)  # Expected output: 10, 24



"""
Explanation

    def sum_product(t): - Define a function called "sum_product" that takes a tuple "t" as an argument.

    sum_result = 0 - Initialize a variable "sum_result" to store the sum of the elements in the tuple. Set its initial value to 0.

    product_result = 1 - Initialize a variable "product_result" to store the product of the elements in the tuple. Set its initial value to 1.

    for num in t: - Start a for loop that iterates through each element "num" in the tuple "t".

    sum_result += num - Add the current element "num" to the "sum_result".

    product_result *= num - Multiply the current element "num" with the "product_result".

    return sum_result, product_result - After the loop is done, return a tuple containing the "sum_result" and "product_result".

Time and Space Complexity

    sum_result = 0 - Constant time complexity O(1) because it's a single assignment operation. Constant space complexity O(1) because it stores a single integer.

    product_result = 1 - Constant time complexity O(1) because it's a single assignment operation. Constant space complexity O(1) because it stores a single integer.

    for num in t: - Linear time complexity O(n) for the loop, where n is the number of elements in the tuple. This is because the loop iterates through each element in the tuple once. No additional space is used in the loop.

    sum_result += num - Constant time complexity O(1) for each addition operation inside the loop.

    product_result *= num - Constant time complexity O(1) for each multiplication operation inside the loop.

    return sum_result, product_result - Constant time complexity O(1) because it returns a tuple with two integers. Constant space complexity O(1) because it creates a tuple with two integers.

Overall time complexity of the function is O(n) because the loop iterates through each element in the tuple once. The rest of the operations have constant time complexity O(1). The overall space complexity is O(1) because the function uses a constant amount of additional memory to store the sum and product, regardless of the size of the input tuple.
"""


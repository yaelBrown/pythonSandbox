def diagonal_sum(matrix):
    # TODO
    n = len(matrix)
    i = 0
    sum = 0
    while i < n:
        sum += matrix[i][i]
        i += 1
        
    return sum

# use a for loop
def diagonal_sum(matrix):
    # Initialize the sum to 0
    total = 0
  
    # Iterate through the rows of the matrix
    for i in range(len(matrix)):
        # Add the diagonal element to the total sum
        total += matrix[i][i]
  
    return total


"""
  2D Lists

  Given 2D list calculate the sum of diagonal elements.

  Example

      myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
      
      diagonal_sum(myList2D) # 15
"""
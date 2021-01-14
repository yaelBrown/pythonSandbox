# Complete the function below.



def solve(arr):
  if len(arr) > 1: 
    _ = [None] * len(arr)
    evenIdx = 0
    oddIdx = len(arr) - 1

    for n in arr:
      if isEven(n):
        _[evenIdx] = n
        evenIdx += 1
      else:
        _[oddIdx] = n
        oddIdx -= 1
      
    # for n in _:
    #   if n == None: 
    #     _.remove(n)

    arr = _
    del _

    return arr
  else: 
    return arr

def isEven(n):
  if n % 2 == 0:
    return True
  else: 
    return False

if __name__ == "__main__":
  input = [4, 1, 2, 3, 4]

  print(input)

  print(solve(input))
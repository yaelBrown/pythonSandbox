def check_if_sum_possible(arr, k):
  if len(arr) <= 1:
    return False
  else: 
    i = arr[0]
    jIdx = len(arr) - 1 
    j = arr[jIdx] 
    mid = math.ceil(int(len(arr)/2))

    if i + j == k:
      return True

    if i == arr[mid]:
      return False
    else: 
      while i != j:
        if (i + j) == k:
          return True
        else:
          jIdx -= 1
          j = arr[jIdx]

      out = sumHelper(arr[1:], k)
      return out


def sumHelper(curArr, k):
  if len(curArr) == 1:
    return False

  i = curArr[0]
  jIdx = len(curArr) - 1
  j = curArr[len(curArr) - 1]

  while j != i:
    if (i + j) == k:
      return True
    else: 
      jIdx -= 1
      j = curArr[jIdx]
  
  return sumHelper(curArr[1:],k)
  
    


687168
     



"""
1 2 3 4

1,4
1,3
1,2

2,4
2,3

3,4
"""


if __name__ == "__main__":
  c1 = [2,4,8]
  c2 = [2,4,6,8]

  print(check_if_sum_possible(c2, 6))




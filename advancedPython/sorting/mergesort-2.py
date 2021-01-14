#
# Complete the 'merge_sort' function below.
#
# The function accepts an integer array as parameter.
#

def merge_sort(arr):
  if len(arr) > 1:
    mid = int(len(arr) / 2)
    l = arr[:mid]
    r = arr[mid:]

    merge_sort(l)
    merge_sort(r)

    i = j = k = 0

    while i < len(l) and j < len(r):
      if l[i] < r[j]:
        arr[k] = l[i]
        i += 1
      else: 
        arr[k] = r[j]
        j += 1
      
      k += 1

    while i < len(l):
      arr[k] = l[i]
      i += 1
      k += 1

    while j < len(r):
      arr[k] = r[j]
      j += 1
      k += 1

    return arr
  else: 
    return arr
  
  
def printArr(arr):
  for n in arr:
    print(n)

if __name__ == "__main__":
  input = [4,1,7,5,3]
  merge_sort



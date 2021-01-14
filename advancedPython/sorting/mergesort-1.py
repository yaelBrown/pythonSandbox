"""
MergeSort 
  divide and conquer

  divide array and then merge it at the end

"""

def mergeSort(arr):
  if len(arr) > 1:
    mid = int(len(arr) // 2)
    l = arr[:mid]
    r = arr[mid:]

    mergeSort(l)
    mergeSort(r)

    i = j = k = 0

    while i < len(l) and j < len(r):
      if l[i] < r[j]:
        arr[k] = l[i]
        i += 1
      else: 
        arr[k] = r[j]
        j += 1
      
      k += 1      # add this because both code blocks need k incremented. Prevent repeat code

    while i < len(l):
      arr[k] = l[i]
      i += 1      # Need to increment idx
      k += 1

    while j < len(r):
      arr[k] = r[j]
      j += 1      # Need to increment idx
      k += 1

    return arr
  else:
    return arr




if __name__ == "__main__":
  array = [12, 11, 13, 5, 6, 7, 5, 2, 8, 1, 9]

  print(array)
  print(mergeSort(array))

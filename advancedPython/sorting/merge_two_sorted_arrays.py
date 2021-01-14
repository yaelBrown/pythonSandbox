
#
# Complete the merger_first_into_second function below.
#

def merger_first_into_second(arr1, arr2):
  idx = 0
  idx2 = 0

  while idx2 < (len(arr2) - 1) and idx < (len(arr1) - 1):
    if arr1[idx] <= arr2[idx2]:
      arr2.insert(idx2, arr1[idx])
      idx += 1
      idx2 += 1
    else: 
      idx2 += 1

  while 0 in arr2:
    arr2.remove(0)

if __name__ == "__main__":
  a1 = [1, 3, 5]
  a2 = [2, 4, 6, 0, 0, 0]

  print({"a1": a1, "a2": a2})
  merger_first_into_second(a1, a2)

  print(a2)
def swap_pairs(arr):
  def swap(ar, head, next):
    _ = ar[head]
    ar[head] = ar[next]
    ar[next] = _

  i = 0
  j = 1

  while (len(arr) - 0) > 1 and i < len(arr):
    swap(arr, i, j)
    i += 2
    j += 2


if __name__ == "__main__":
  aa = [1,2,3,4]

  swap_pairs(aa)

  print(aa)
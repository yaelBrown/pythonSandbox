def jumpingOnClouds(c):
  # Write your code here
  idx = 0
  maxIdx = (len(c) - 1)
  jumps = 0
    
  while idx < maxIdx:
    if idx == (maxIdx - 1) and maxIdx == 1:
      break

    if (idx + 2) <= maxIdx:
      if c[idx + 2] == 0:
        idx += 2
        jumps += 1
    
    if (idx + 1) <= maxIdx:
      if c[idx + 1] == 0:
        idx += 1
        jumps += 1

    if idx == maxIdx:
      break    
    
  return jumps






if __name__ == '__main__':
  clouds = [0, 0, 1, 0, 0, 1, 0]      # 7 
  clouds2 = [0, 0, 0, 1, 0, 0]        # 6
  
  ans = jumpingOnClouds(clouds)

  print(ans)
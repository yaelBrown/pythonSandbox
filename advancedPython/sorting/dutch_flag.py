def dutch_flag_sort(balls):
  idx = 0
  gCount = 0

  for b in balls: 
    if b == "R":
      _ = balls[idx]
      balls[idx] = b
      idx += 1

    if b == "G":
      gCount += 1

  while gCount > 0:
    if gCount == len(balls):
      return 
    balls[idx] = "G"
    gCount -= 1
    idx += 1

  while idx < len(balls):
    balls[idx] = "B"
    idx += 1

if __name__ == "__main__":
  b = ["G", "B", "G", "G", "R", "B", "R", "G"]
  # b = ["G", "G", "G"]
  print(b)

  dutch_flag_sort(b) 
  print(b)
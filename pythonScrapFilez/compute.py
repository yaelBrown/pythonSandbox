print("hello")

cnt = 600
divByFour = 0
while cnt != 299:
  if cnt % 3 == 0:
    divByFour += 1
  cnt -= 1

print(f"{divByFour} numbers are divisible by 3")
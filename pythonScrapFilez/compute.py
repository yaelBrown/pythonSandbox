print("hello")

cnt = 400
divByFour = 0
while cnt != 199:
  if cnt % 4 == 0:
    divByFour += 1
  cnt -= 1

print(f"{divByFour} numbers are divisible by 4")
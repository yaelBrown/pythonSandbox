

initial = 10000
cnt = 1
maxx = 20000

def compound(i, p):
  return (i * p) + i


curAmt = initial
while curAmt < maxx:
  curAmt = compound(curAmt, .14)
  print(f"Year {cnt}: {curAmt}")
  cnt += 1

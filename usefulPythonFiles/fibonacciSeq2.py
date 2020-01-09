'''
this is an example using the Yield keyword
'''

def gen_fibon(n):
  a = 1
  b = 1
  output = []

  for i in range(n):
    output.append(a)
    a,b = b,a+b

  return output


# using yield keyword
def gen_fibon_yield(n):
  a = 1
  b = 1
  for i in range(n):
    yield n
    a,b = b, a+b # tuple magic

'''
Yield returns the value, more efficient than using the output above.
  Using the output above would use a lot more memory.
  Yield does not save anything in memory, it returns the value and keeps going thru the loop.
'''
'''
Example of a generator.
'''

def create_cubes(n):
  result = []
  for x in range(n):
    result.append(x**3)
  return result


l = create_cubes(10)

print(l)


# more efficient, does not have to create a list in memory then output result.
for x in create_cubes(20):
  print(x)

k = list(create_cubes(5)) # casts to list

print(k)



print("======")


def simple_gen():
  for x in range(5):
    yield x

# simple_gen in action
for n in simple_gen():
  print(n)

g = simple_gen()

print("next()") # built in next() function
print(next(g)) # what the generator is doing internally

print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) # StopIteration

'''
For loops automatically catch the StopIteration error and stops
'''

print("=====")
print("iter()")

s = "apple"
s_iter = iter(s) # converts iterable object to something that can iterated over with next()

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
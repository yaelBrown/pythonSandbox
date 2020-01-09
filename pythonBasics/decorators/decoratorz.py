'''
Example of python decorators
'''

# have function that returns a function
def func(aa="cookies"):
  print("This is the default function")

  def one():
    return 1

  def eleven():
    return 11

  if aa == "cookies":
    return one()
  else:
    return eleven()

# print(func())

# can pass a function into a function. Functions as arguments



def deco(original_func):
  def wrap_func():
    print("some extra code before original function")
    original_func()
    print("Some code after the function")

  return wrap_func

'''
@deco annotation, takes this function and passes into the deco function defined above
  The annotation has to be the name of the function that takes a function as an argument.
'''
@deco
def func_needs_deco():
  print("I want to be decorated")

decorated_func = deco(func_needs_deco)

# decorated_func()

func_needs_deco()
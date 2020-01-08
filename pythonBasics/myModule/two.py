#two.py
import one
print("Top level in two.py")

one.func()

'''
In python code, functions are defined at the top
and then they are called at the bottom. Depending on how the script is ran.
'''

def f():
  pass

def f2():
  pass

def f3():
  pass

'''
Checks how the script is being ran.
'''
if __name__ == '__main__':
  print("Two.py is being run directly!")
else:
  print("Two.py has been imported!")
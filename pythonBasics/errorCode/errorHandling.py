'''
Example of error handling
'''

def add(n1,n2):
  print(n1+n2)

add(10,20) # 30

number1 = 10
# number2 = input("Please provide a number: ") # enter a string
number2 = 20

add(number1, number2) # will raise TypeError

'''
Example try/except
'''
try:
  pass
except:
  print("something went wrong")
  pass
finally:
  print("This is finally ran")

# print(type("this is a string")) # returns 'str'



try:
  number3 = 10
  # number4 = input("Please enter another number: ")
  number4 = 40

  add(number3, number4)
except TypeError:
  print("An exception has occured !")
  if type(number4) == str:
    number4 = int(number4)
else:
  # can use else block to run code if everything is fine now.
  # if there is an error, this block will not run.
  print("This is the else block")
finally:
  print("Finally was ran.")
  add(number3, number4)


'''
How to catch multiple errors
(similar to java)
'''
try:
  f = open('testfile', 'w')
  f.write('write a test line')
except TypeError:
  print("There was a type error ")
except OSError: #if file does not exist
  print("Hey you have an OS Error")
finally:
  print("I always run")


'''
Use a while loop to get what you want.
'''

def ask_for_int():
  while True:
    try:
      result = int(input("Please provide a number: "))
    except:
      print("Whoops! That is not a number")
    else:
      print("Yes, thank you")
      break
    finally:
      print("End of try/except/finally")
  print(result)

ask_for_int()



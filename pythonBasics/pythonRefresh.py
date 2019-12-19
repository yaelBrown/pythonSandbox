# test

"""
This is a multi-line comment
"""

# declare variable/print statement

age = 32
age2 = 64
name = "yael"

print("Hello my name is {} and I am {} years old.".format(name, age))

# if statement example

if age > 10:
    print("Age is greater than 10")

if age > 10:
    print("Yes the age is definitely greater than 10")
else:
    print("age is less than 10")

# functions

def hello():
    print("hello function")


hello()
hello()


def defaultValues(name2="yaelster", age2=0):
    print("name2 is {} and age2 is {}".format(name2, age2))


defaultValues()
defaultValues("bob", 12)
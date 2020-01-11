'''
Testing immutability and how to have read only variables in python
'''

aa = 10

aa = 15

print(aa)



__bb = "apples"

__bb = "asdf"

print(__bb)




cc = ("cookies", "pug")

# cc = "asdfasdf"

# cc[1] = "puggy"

cc = ("cookies", "pug", "puggy")

print(cc)

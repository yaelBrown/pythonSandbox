import json

# initialize db
db = []

# create class
class Parent:
  name = ""
  age = 0

  def __init__(self, n, a):
    self.name = n
    self.a = a

  def __str__(self):
    return f"My name is {self.name}. I am {self.age} years old!"

  def serialize(self):
    return {
      "name" : self.name,
      "age" : self.age
    }

# create instances
Yael = Parent("Yael", 33)
Cookie = Parent("Cookie", 27)
Popcorn = Parent("Popcorn", 30)

# add instances to db
db.append(Yael)
db.append(Cookie)
db.append(Popcorn)

# print(db)
# print(json.dumps(db))

out = []
# for loop impl
# for i in db:
#   out.append(i.serialize())

# list comprehension
out = [i.serialize() for i in db]
print(out)

# json output
print(json.dumps(out))



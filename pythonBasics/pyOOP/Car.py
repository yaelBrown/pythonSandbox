class Car:
  # constructor
  # using default value can overload the method
  def __init__(self, make = None, model = None):
    self.make = make
    self.model = model

  # class object attributes
  wheelSize = 17

  # Methods - operations/actions
  #   have to pass in 'self' keyword as parameter
  def drive(self):
    print("vroom vroom")

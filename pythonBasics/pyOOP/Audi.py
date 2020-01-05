from Car import Car

class Audi(Car):
  def __init__(self):
    Car.__init__(self)

  drivetrain = "AWD"
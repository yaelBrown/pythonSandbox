'''
Abstract class race car
'''

class Racecar():

  def __init__(self):
    print("Racecar was created")

  # this method is meant to be overwritten in another class.
  def go_race(self):
    raise NotImplementedError("Subclass must implement this abstract method")


# from Class import Classname
from Car import Car
from Audi import Audi

# use constructor to instantiate class Car
yael = Car(make = "Audi", model = "A3")

print(yael.make) # audi

print(yael.wheelSize)

yael.drive()

loeb = Audi()
loeb.make = "Audi"

print(loeb.make)
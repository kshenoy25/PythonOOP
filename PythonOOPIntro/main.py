# object = a "bundle" of related attributes (variables) and methods (functions)
#          ex. phone, cup, bool
#          need a class to create many objects
# class = (blueprint) used to design the structure and layout of an object

from car import Car

car1 = Car("Highlander", 2011, "black", False)
car2 = Car("Mustang", 2023, "pruple", True)
car3 = Car("BMW", 2020, "red", False)

#car2.drive()
#car3.stop()
#car1.stop()
car1.describe()
car2.describe()
car3.describe()

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print("*********************************")

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
print(car2.for_sale)

print("*********************************")
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)
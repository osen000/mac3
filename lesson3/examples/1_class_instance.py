# New class declaration
class Car:
    pass


# New class Animal
class Animal(Car):
    pass


# Creating class instances (objects)
toyota_camry = Animal()
lada = Car()
dog = Animal()


# Checking class of objects
print("toyota <- Car", isinstance(toyota_camry, Car))
print("lada <- Car", isinstance(lada, Car))
print("dog <- Car", isinstance(dog, Animal))


# Class is also an object
honda = Car
new_car = honda()

print(isinstance(new_car, Car))

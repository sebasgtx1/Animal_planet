#!/usr/bin/python3

""" main code """

from animals import *

""" creating an generic animal"""

animal_1 = Animal("Firu", "Felino", 5)
animal_1.move()

""" creating an aquatic animal"""

animal_2 = Aquatic("Avocato", "pescao", 10)
animal_2.sound()

""" creating a fish """

animal_3 = Fish("pescadito", "pescao", 10, "sea")
animal_3.where()

""" creating a whale """

animal_4 = Whale("pedro", "whale", 200, "sea")
animal_4.sound()

""" creating a Dog """

animal_5 = Dog("Firulais", "perrito", 5, "terrestrial")
animal_5.sound()

""" creating a cat """

animal_5 = Cat("Misingo", "Gato", 4, "terrestrial")
animal_5.sound()

""" Del method """

print("Number of animals: {}".format(Animal.population))
del animal_1
print("Number of animals: {}".format(Animal.population))

""" Checking Errors"""
try:
    animal_6 = Animal("animal", 2, 3)
except Exception as error:
    print(error)

try:
    animal_7 = Animal(2, "Perro", 3)
except Exception as error:
    print(error)

try:
    animal_8 = Animal("animal", "Specie", "2")
except Exception as error:
    print(error)

try:
    animal_9 = Aquatic("animal", "especie", 3, 5)
except Exception as error:
    print(error)

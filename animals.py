#!/usr/bin/python3
"""Module that conteins the animal class
"""


class Animal:
    """ Class that defines an animal
    """
    population = 0

    def __init__(self, name="", species="", age=0):
        """ constructor method"""
        self.name = name
        self.species = species
        self.age = age
        Animal.population += 1

    @property
    def name(self):
        """ Name getter"""
        return self.__name

    @name.setter
    def name(self, value):
        """ Name setter"""
        if isinstance(value, str):
            self.__name = value
        else:
            raise TypeError("name has to be a string")

    @property
    def species(self):
        """ species getter"""
        return self.__species

    @species.setter
    def species(self, value):
        """ Species setter"""
        if isinstance(value, str):
            self.__species = value
        else:
            raise TypeError("species has to be a string")

    @property
    def age(self):
        """ age getter"""
        return self.__age

    @age.setter
    def age(self, value):
        """ Age setter"""
        if isinstance(value, int):
            self.__age = value
        else:
            raise TypeError("age has to be a int number")

    def move(self):
        """ Move method """
        print("{} is moving".format(self.__name))

    def show(self):
        """ show method """
        print("a {} show up".format(self.__species))

    def sound(self):
        """ sound method"""
        print("{} is making a sound".format(self.__name))

    def __del__(self):
        Animal.population -= 1
        print("Close to extition")


class Aquatic(Animal):
    """ Child class of animal"""

    def __init__(self, name="", species="", age=0, habitat=""):
        """constructor method"""
        super().__init__(name, species, age)
        self.habitat = habitat

    @property
    def habitat(self):
        """ habitat getter"""
        return self.__habitat

    @habitat.setter
    def habitat(self, value):
        """ habitat setter"""
        if isinstance(value, str):
            self.__habitat = value
        else:
            raise TypeError("habitat has to be a string")

    def move(self):
        """ Move method """
        print("{} is swimming".format(self.name))

    def sound(self):
        """ sound method"""
        print("{}: glu glu glu ".format(self.name))

    def where(self):
        """ Where the animal lives method"""
        print("{} lives in the {}".format(self.name, self.__habitat))


class Fish(Aquatic):
    """ class that defines a fish"""
    pass


class Whale(Aquatic):
    """ class that defines a whale"""
    def sound(self):
        """ sound method"""
        print("{}: *speaks in cetacean* ".format(self.name))


class Terrestrial(Animal):
    """ Child class of animal"""

    def __init__(self, name="", species="", age=0, habitat=""):
        """constructor method"""
        super().__init__(name, species, age)
        self.habitat = habitat

    @property
    def habitat(self):
        """ habitat getter """
        return self.__habitat

    @habitat.setter
    def habitat(self, value):
        """ habitat setter """
        if isinstance(value, str):
            self.__habitat = value
        else:
            raise TypeError("habitat has to be a string")

    def where(self):
        """ Where the animal lives method"""
        print("{} lives in the {}".format(self.name, self.__habitat))


class Dog(Terrestrial):
    """ class that defines a dog"""
    def sound(self):
        """ sound method"""
        print("{}: Woof woof !!".format(self.name))


class Cat(Terrestrial):
    """ class that defines a dog"""
    def sound(self):
        """ sound method"""
        print("{}: Miau Miau !!".format(self.name))

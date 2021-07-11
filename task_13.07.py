from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def feline(self):
        raise NotImplementedError()

    @abstractmethod
    def canine(self):
        raise NotImplementedError()


class Pet(Animal):
    def feline(self):
        pass

    def canine(self):
        pass


class Cat(Pet):
    def feline(self):
        print("This is an animal from the feline family")


class Dog(Pet):
    def canine(self):
        print("This is an animal from the canine family")


class WildAnimal(Animal):
    def feline(self):
        pass

    def canine(self):
        pass


class Lion(WildAnimal):
    def feline(self):
        print("This is an animal from the feline family")


class Wolf(WildAnimal):
    def canine(self):
        print("This is an animal from the canine family")

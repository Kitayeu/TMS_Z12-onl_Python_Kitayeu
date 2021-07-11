class Animal:
    pass


class Pet(Animal):
    pass


class Cat(Pet):
    pass


class Dog(Pet):
    pass


class WildAnimal(Animal):
    pass


class Lion(WildAnimal):
    pass


class Wolf(WildAnimal):
    pass


print(Cat.__mro__)

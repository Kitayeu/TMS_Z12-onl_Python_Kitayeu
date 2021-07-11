from random import choice, randint
from string import ascii_uppercase
from abc import ABCMeta, abstractmethod


class Pet(metaclass=ABCMeta):
    counter = 0

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        self.__class__.counter += 1

    @abstractmethod
    def run(self):
        raise NotImplementedError()

    @abstractmethod
    def birthday(self):
        raise NotImplementedError()

    @abstractmethod
    def sleep(self):
        raise NotImplementedError()

    @abstractmethod
    def change_weight(self, x=None):
        raise NotImplementedError()

    @abstractmethod
    def change_height(self, x=None):
        raise NotImplementedError()

    @abstractmethod
    def voice(self):
        raise NotImplementedError()

    @classmethod
    def get_counter(cls):
        print(f"Class {cls.__name__} has {cls.counter} objects")

    @staticmethod
    def get_random_name():
        return f"{choice(ascii_uppercase)}-{randint(1, 100)}"

    def __str__(self):
        return f"name: {self.name}, age: {self.age}, master: {self.master}, weight: {self.weight}, " \
               f"height: {self.height}"

    def __repr__(self):
        return f"{self.__class__} and {self.name}, {self.age}, {self.master}, {self.weight}, {self.height}"


class Dog(Pet):
    def __init__(self, name, age, master, weight, height):
        super().__init__(name, age, master, weight, height)

    def voice(self):
        print(f"{self.name} bark!")

    def jump(self, x):
        if x > 0.5:
            print("Dogs cannot jump so high")
        else:
            print(f"{self.name}, jump {x} meters")

    def run(self):
        print(f"{self.name} run!")

    def birthday(self):
        self.age = self.age + 1

    def sleep(self):
        print(f"{self.name} sleep!")

    def change_weight(self, x=None):
        if x:
            self.weight = self.weight + x
        else:
            self.weight = self.weight + 0.2

    def change_height(self, x=None):
        if x:
            self.height = self.height + x
        else:
            self.height = self.height + 0.2


class Cat(Pet):
    def __init__(self, name, age, master, weight, height):
        super().__init__(name, age, master, weight, height)

    def voice(self):
        print(f"{self.name} meow!")

    def jump(self, x):
        if x > 2:
            print("Cats cannot jump so high")
        else:
            print(f"{self.name}, jump {x} meters")

    def run(self):
        print(f"{self.name} run!")

    def birthday(self):
        self.age = self.age + 1

    def sleep(self):
        print(f"{self.name} sleep!")

    def change_weight(self, x=None):
        if x:
            self.weight = self.weight + x
        else:
            self.weight = self.weight + 0.2

    def change_height(self, x=None):
        if x:
            self.height = self.height + x
        else:
            self.height = self.height + 0.2


class Horse(Pet):
    def __init__(self, name, age, master, weight, height):
        super().__init__(name, age, master, weight, height)

    def voice(self):
        print(f"{self.name} neigh!")

    def run(self):
        print(f"{self.name} run!")

    def birthday(self):
        self.age = self.age + 1

    def sleep(self):
        print(f"{self.name} sleep!")

    def change_weight(self, x=None):
        if x:
            self.weight = self.weight + x
        else:
            self.weight = self.weight + 0.2

    def change_height(self, x=None):
        if x:
            self.height = self.height + x
        else:
            self.height = self.height + 0.2


class Donkey(Pet):
    def __init__(self, name, age, master, weight, height):
        super().__init__(name, age, master, weight, height)

    def voice(self):
        print(f"{self.name} eeyore!")

    def run(self):
        print(f"{self.name} run!")

    def birthday(self):
        self.age = self.age + 1

    def sleep(self):
        print(f"{self.name} sleep!")

    def change_weight(self, x=None):
        if x:
            self.weight = self.weight + x
        else:
            self.weight = self.weight + 0.2

    def change_height(self, x=None):
        if x:
            self.height = self.height + x
        else:
            self.height = self.height + 0.2


class Mule(Donkey):
    def __init__(self, name, age, master, weight, height):
        super().__init__(name, age, master, weight, height)


mule = Mule('Hybrid', 2, 'Misha', 600, 120)
mule.voice()

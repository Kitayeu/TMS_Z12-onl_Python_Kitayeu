class Pet:
    list_obj = []
    _counter = 0

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        self.__class__.list_obj.append(self)
        Pet._counter += 1

    def run(self):
        print(f"{self.name} run!")

    def jump(self, x):
        print(f"{self.name}, jump {x} meters")

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

    def voice(self):
        pass

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


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species

    def fly(self):
        if self.weight > 0.1:
            print("This parrot cannot fly")
        else:
            print(f"{self.name} fly!")

    def change_weight(self, x=None):
        if x:
            self.weight = self.weight + x
        else:
            self.weight = self.weight + 0.05

    def change_height(self, x=None):
        if x:
            self.height = self.height + x
        else:
            self.height = self.height + 0.2

    def jump(self, x):
        if x > 0.05:
            print("Parrots cannot jump so high")
        else:
            print(f"{self.name}, jump {x} meters")

    def voice(self):
        print(f"{self.name} voice!")

    def __str__(self):
        return f"name: {self.name}, age: {self.age}, master: {self.master}, weight: {self.weight}, " \
               f"height: {self.height}, species: {self.species}"

    def __repr__(self):
        return f"{self.__class__} and {self.name}, {self.age}, {self.master}, {self.weight}, {self.height}," \
               f" {self.species}"


def call_voice(x: list) -> None:
    """Function takes list of animals 'x' and calls method 'voice' for each animal from list

    :param x: list of animals to iterate on
    """
    for pets in x:
        pets.voice()


cat = Cat("Lumen", 4, "Ira", 5, 15)
dog = Dog("Rover", 2, "Alice", 10, 30)
parrot = Parrot("Kesha", 1, "Vovka", 0.051, 8, "Ara")
cat_1 = Cat("Tosya", 3, "Anna", 7, 15)
call_voice(cat.list_obj)
print(Pet._counter)

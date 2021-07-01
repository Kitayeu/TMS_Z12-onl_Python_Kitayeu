class Car:
    def __init__(self, brand, model, year_release):
        self.__brand = brand
        self.__model = model
        self.__year_release = year_release

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_year_release(self):
        return self.__year_release

    def set_year_release(self, year_release):
        self.__year_release = year_release

    def color(self):
        print(f"{self.__model} white")

    def fuel(self):
        print(f"{self.__model} petrol")


car = Car("VAZ", "2101", "1976")
print(car.get_brand())
car.set_model("21011")
print(car.get_model())
car.color()
car.fuel()


class Tree:
    def __init__(self, gender, size, variety):
        self.__gender = gender
        self.__size = size
        self.__variety = variety

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def get_variety(self):
        return self.__variety

    def set_variety(self, variety):
        self.__variety = variety

    def condition(self):
        print(f"{self.__gender} in good condition")

    def fruits(self):
        print(f"Аn {self.__gender} has fruits")


tree = Tree("Apple tree", "middle", "Antonovka")
print(tree.get_gender())
tree.set_size("big")
print(tree.get_size())
tree.fruits()
tree.condition()


class Armchair:
    def __init__(self, kind, colour, price):
        self.__kind = kind
        self.__colour = colour
        self.__price = price

    def get_kind(self):
        return self.__kind

    def set_kind(self, kind):
        self.__kind = kind

    def get_colour(self):
        return self.__colour

    def set_colour(self, colour):
        self.__colour = colour

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def where(self):
        print(f"Where is the {self.__kind}?")

    def buy(self):
        print(f"Where did you buy this {self.__kind}?")


armchair = Armchair("Bean bag", "brown", "100 byn")
print(armchair.get_kind())
armchair.set_colour("black")
print(armchair.get_colour())
armchair.where()
armchair.buy()


class Dog:
    def __init__(self, name, age, master):
        self.__name = name
        self.__age = age
        self.__master = master

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_master(self):
        return self.__master

    def set_master(self, master):
        self.__master = master

    def jump(self):
        print(f"{self.__name} jump!")

    def bark(self):
        print(f"{self.__name} bark!")


dog = Dog("Rover", 2, "Alice")
print(dog.get_name())
dog.set_age(3)
print(dog.get_age())
dog.jump()
dog.bark()


class Bird:
    def __init__(self, nickname, address, weight):
        self.__nickname = nickname
        self.__address = address
        self.__weight = weight

    def get_nickname(self):
        return self.__nickname

    def set_nickname(self, nickname):
        self.__nickname = nickname

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def sleep(self):
        print(f"{self.__nickname} sleep!")

    def fly(self):
        print(f"{self.__nickname} fly!")


parrot = Bird("Kesha", "Minsk", 0.02)
print(parrot.get_nickname())
parrot.set_weight(0.05)
print(parrot.get_weight())
parrot.sleep()
parrot.fly()

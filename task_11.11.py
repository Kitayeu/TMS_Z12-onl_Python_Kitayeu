class Pet:
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

    def run(self):
        print(f"{self.name} run!")

    def jump(self):
        print(f"{self.name} jump!")

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


class Dog(Pet):
    def __init__(self, name, age, master, weight, height):
        super().__init__(name, age, master, weight, height)

    def bark(self):
        print(f"{self.name} bark!")


class Cat(Pet):
    def __init__(self, name, age, master, weight, height):
        super().__init__(name, age, master, weight, height)

    def meow(self):
        print(f"{self.name} meow!")


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height):
        super().__init__(name, age, master, weight, height)

    def fly(self):
        if self.weight > 0.1:
            print("This parrot cannot fly")
        else:
            print(f"{self.name} fly!")


cat = Cat("Lumen", 4, "Ira", 5, 15)
dog = Dog("Rover", 2, "Alice", 10, 30)
parrot = Parrot("Kesha", 1, "Vovka", 0.11, 8)
cat.change_weight(1)
print(cat.weight)
cat.change_height()
print(cat.height)
parrot.fly()

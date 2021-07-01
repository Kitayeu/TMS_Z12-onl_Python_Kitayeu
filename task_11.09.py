class Dog:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f"{self.name} run!")

    def jump(self):
        print(f"{self.name} jump!")

    def birthday(self):
        self.age = self.age + 1

    def sleep(self):
        print(f"{self.name} sleep!")

    def bark(self):
        print(f"{self.name} bark!")


class Cat:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f"{self.name} run!")

    def jump(self):
        print(f"{self.name} jump!")

    def birthday(self):
        self.age = self.age + 1

    def sleep(self):
        print(f"{self.name} sleep!")

    def meow(self):
        print(f"{self.name} meow!")


class Parrot:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f"{self.name} run!")

    def jump(self):
        print(f"{self.name} jump!")

    def birthday(self):
        self.age = self.age + 1

    def sleep(self):
        print(f"{self.name} sleep!")

    def fly(self):
        print(f"{self.name} fly!")


cat = Cat("Lumen", 4, "Ira")
print(cat.name)
print(cat.age)
print(cat.master)

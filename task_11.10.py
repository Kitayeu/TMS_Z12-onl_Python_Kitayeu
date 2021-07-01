class Pet:
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


class Dog(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def bark(self):
        print(f"{self.name} bark!")


class Cat(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def meow(self):
        print(f"{self.name} meow!")


class Parrot(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def fly(self):
        print(f"{self.name} fly!")


cat = Cat("Lumen", 4, "Ira")
dog = Dog("Rover", 2, "Alice")
parrot = Parrot("Kesha", 1, "Vovka")
cat.run()
cat.jump()
cat.birthday()
print(cat.age)
cat.sleep()
cat.meow()
dog.run()
dog.jump()
dog.birthday()
print(dog.age)
dog.sleep()
dog.bark()
parrot.run()
parrot.jump()
parrot.birthday()
print(parrot.age)
parrot.sleep()
parrot.fly()

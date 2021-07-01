class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f"{self.name} jump!")

    def run(self):
        print(f"{self.name} run!")

    def bark(self):
        print(f"{self.name} bark!")

    def change_name(self, name):
        self.name = name


dog_1 = Dog(30, 10, "Rover", 2)
print(dog_1.name)
dog_1.change_name("Wanderer")
print(dog_1.name)

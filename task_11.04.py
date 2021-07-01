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


dog_1 = Dog(30, 10, "Rover", 2)
dog_1.jump()
dog_1.run()
dog_1.bark()
print(dog_1.height)
print(dog_1.weight)
print(dog_1.name)
print(dog_1.age)

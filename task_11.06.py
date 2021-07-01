class Dog:
    def __init__(self, height, weight, name, age, master):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.__master = master

    def jump(self):
        print(f"{self.name} jump!")

    def run(self):
        print(f"{self.name} run!")

    def bark(self):
        print(f"{self.name} bark!")

    def change_name(self, name):
        self.name = name

    def get_master(self):
        return self.__master


dog_1 = Dog(30, 10, "Rover", 2, "Alice")
print(dog_1.get_master())

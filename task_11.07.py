class Dog:
    def __init__(self, height, weight, name, age, master, address="Minsk"):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.__master = master
        self.__address = address

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

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address


dog_1 = Dog(30, 10, "Rover", 2, "Alice")
print(dog_1.get_address())
dog_1.set_address("Brest")
print(dog_1.get_address())

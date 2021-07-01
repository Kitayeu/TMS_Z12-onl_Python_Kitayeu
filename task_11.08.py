class Dog:
    def __init__(self, height, weight, name, age, master, address="Minsk"):
        self.__height = height
        self.__weight = weight
        self.__name = name
        self.__age = age
        self.__master = master
        self.__address = address

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    def jump(self):
        print(f"{self.name} jump!")

    def run(self):
        print(f"{self.name} run!")

    def bark(self):
        print(f"{self.name} bark!")


dog_1 = Dog(30, 10, "Rover", 2, "Alice")
print(dog_1.name)
print(dog_1.weight)
dog_1.weight = 12
print(dog_1.weight)
dog_1.jump()

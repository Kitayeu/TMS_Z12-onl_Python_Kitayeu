class Car:
    def __init__(self, brand, model, year_release, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year_release = year_release
        self.__speed = speed

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

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def increase_speed(self):
        self.__speed = self.__speed + 5

    def speed_reduction(self):
        self.__speed = self.__speed - 5

    def stop(self):
        self.__speed = 0

    def current_speed(self):
        print(self.__speed)

    def reverse(self):
        self.__speed = -self.__speed


car = Car("VAZ", "21011", "1976", 100)
car.increase_speed()
car.current_speed()
car.speed_reduction()
car.current_speed()
car.reverse()
car.current_speed()
car.stop()
car.current_speed()

from functools import wraps


def _int_required(func):
    """Function checks input data 'value' for belonging to 'int' type

    :param func: function for which 'value' is checked
    :return: function with entered data
    """
    @wraps(func)
    def wrapper(self, value):
        if not isinstance(value, int):
            raise TypeError("You must enter an integer")
        return func(self, value)
    return wrapper


def _time_required(func):
    """Function checks input data 'other' for belonging to 'MyTime' class

    :param func: function for which 'other' is checked
    :return: function with entered data
    """
    @wraps(func)
    def wrapper(self, other):
        if not isinstance(other, MyTime):
            raise TypeError("Object must belong to 'MyTime' class")
        return func(self, other)
    return wrapper


class MyTime:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @_time_required
    def __eq__(self, other):
        return (self.hours == other.hours and
                self.minutes == other.minutes and
                self.seconds == other.seconds)

    @_time_required
    def __ne__(self, other):
        return (self.hours != other.hours or
                self.minutes != other.minutes or
                self.seconds != other.seconds)

    @_time_required
    def __add__(self, other):
        hours = self.hours + other.hours
        minutes = self.minutes + other.minutes
        seconds = self.seconds + other.seconds
        return hours, minutes, seconds

    @_time_required
    def __sub__(self, other):
        hours = self.hours - other.hours
        minutes = self.minutes - other.minutes
        seconds = self.seconds - other.seconds
        return hours, minutes, seconds

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def __repr__(self):
        return f"{self.__class__} and {self.hours}:{self.minutes}:{self.seconds}"

    @property
    def hours(self):
        return self._hours

    @hours.setter
    @_int_required
    def hours(self, value):
        self._hours = value

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    @_int_required
    def minutes(self, value):
        self._minutes = value

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    @_int_required
    def seconds(self, value):
        self._seconds = value


one = MyTime(1, 5, 6)
two = MyTime(0, 56, 6)
print(one == two)
print(one != two)
print(one - two)
print(two - one)
print(one + two)
print(one)
print(two)
three = MyTime()
print(three)

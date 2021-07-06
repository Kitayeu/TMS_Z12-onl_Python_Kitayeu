from functools import wraps, total_ordering


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


def _balance(x: int, y: int) -> tuple:
    """Function implements usual time display, value of minutes and seconds can`t exceed 60

    :param x: number of minutes or seconds entered for objects of the "MyTime" class
    :param y: number of seconds or minutes entered for objects of the "MyTime" class
    :return: corrected minutes and seconds in tuple
    """
    if y >= 0:
        while y >= 60:
            x += 1
            y -= 60
    elif y < 0:
        while y < 0:
            x -= 1
            y += 60
    return x, y


@total_ordering
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
    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        if self.hours > other.hours:
            return False
        if self.minutes < other.minutes:
            return True
        if self.minutes > other.minutes:
            return False
        return self.seconds < other.seconds

    @_time_required
    def __add__(self, other):
        hours = self.hours + other.hours
        minutes = self.minutes + other.minutes
        seconds = self.seconds + other.seconds
        minutes, seconds = _balance(minutes, seconds)
        hours, minutes = _balance(hours, minutes)
        return hours, minutes, seconds

    @_time_required
    def __sub__(self, other):
        if self > other:
            hours = self.hours - other.hours
            minutes = self.minutes - other.minutes
            seconds = self.seconds - other.seconds
            minutes, seconds = _balance(minutes, seconds)
            hours, minutes = _balance(hours, minutes)
            return hours, minutes, seconds
        else:
            hours = other.hours - self.hours
            minutes = other.minutes - self.minutes
            seconds = other.seconds - self.seconds
            minutes, seconds = _balance(minutes, seconds)
            hours, minutes = _balance(hours, minutes)
            return f"-({hours}, {minutes}, {seconds})"

    @_int_required
    def __mul__(self, other):
        hours = self.hours * other
        minutes = self.minutes * other
        seconds = self.seconds * other
        minutes, seconds = _balance(minutes, seconds)
        hours, minutes = _balance(hours, minutes)
        return hours, minutes, seconds

    @_int_required
    def __rmul__(self, other):
        hours = self.hours * other
        minutes = self.minutes * other
        seconds = self.seconds * other
        minutes, seconds = _balance(minutes, seconds)
        hours, minutes = _balance(hours, minutes)
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
        self._hours, self._minutes = _balance(self._hours, self._minutes)

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    @_int_required
    def seconds(self, value):
        self._seconds = value
        self._minutes, self._seconds = _balance(self._minutes, self._seconds)


one = MyTime(1, 50, 6)
two = MyTime(2, 15, 6)
print(one == two)
print(one != two)
print(one >= two)
print(one <= two)
print(one > two)
print(one < two)
print(one - two)
print(two - one)
print(one + two)
print(two + one)
print(two * 2)
print(2 * two)
print(one)
print(two)

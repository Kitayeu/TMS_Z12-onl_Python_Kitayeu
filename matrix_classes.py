from random import randint
import pprint


class Matrix:
    def __init__(self, n=5, m=5, a=0, b=0):
        """The class creates matrices

        :param n: number of rows
        :param m: number of columns
        :param a: the beginning of random number range
        :param b: the end of the random number range
        """
        if type(n) is not int or type(m) is not int:
            print("Number of columns and rows must be an integer")
            raise TypeError
        elif n < 0 or m < 0:
            print("Number of columns and rows must be greater than zero")
            raise ValueError
        else:
            self.n = n
            self.m = m
        if type(a) is not int or type(b) is not int:
            print("Boundaries of the range of random numbers must be integers")
            raise TypeError
        elif a > b:
            print("Invalid random number range")
            raise ValueError
        else:
            self.a = a
            self.b = b
        self.data = [[randint(self.a, self.b) for _ in range(self.m)] for _ in range(self.n)]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

    def __str__(self):
        return pprint.pformat(self.data)

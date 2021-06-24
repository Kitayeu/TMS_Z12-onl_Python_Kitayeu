f = lambda **kwargs: {key * 2: val for key, val in kwargs.items()}
print(f(ноль=0, один=1, два=2, три=3, четыре=4, пять=5))

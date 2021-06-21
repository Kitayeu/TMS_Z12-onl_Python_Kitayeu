def func(**kwargs: str):
    """The function accepts an indefinite number of named arguments '**kwargs'
    as input and displays those 'key' whose key length is even

    :param kwargs: an indefinite number of named arguments
    """
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
            print(key, value)


names = {'Даша': 'Name',
         'Маша': 'Name',
         'Слава': 'Name',
         'Паша': 'Name',
         'Глаша': 'Name',
         }
func(**names)

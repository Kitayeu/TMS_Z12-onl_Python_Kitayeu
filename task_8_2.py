words = ['Слово', 'Радар', 'Пример']


def palindrome(x: list):
    """The function checks the dictionary 'x' for palindromes

    :param x: the dictionary is checked for palindromes
    """
    for i in x:
        reverse = i[::-1].upper()
        if reverse == i.upper():
            print(f"'{i}' is a palindrome word")


palindrome(words)

import datetime


class Book:
    NOW = datetime.datetime.now().year

    def __init__(self, page_count, year_publication, author, price):
        if type(page_count) is not int:
            print("Number of pages must be an integer")
            raise TypeError
        elif page_count <= 0:
            print("Number of pages must be greater than zero")
            raise ValueError
        else:
            self.page_count = page_count
        if type(year_publication) is not int:
            print("Year of publication must be an integer")
            raise TypeError
        elif year_publication < 0 or year_publication > self.__class__.NOW:
            print("Publication is not possible this year")
            raise ValueError
        else:
            self.year_publication = year_publication
        if type(author) is not str:
            print("There can be no such author")
            raise TypeError
        else:
            self.author = author
        if type(price) is not int and type(price) is not float:
            print("Price must be a number")
            raise TypeError
        elif price <= 0:
            print("There can't be such a price")
            raise ValueError
        else:
            self.price = price

    def __str__(self):
        return f"page count: {self.page_count}, year of publication: {self.year_publication}, author: {self.author}," \
               f" price: {self.price}"

    def __repr__(self):
        return f"{self.__class__} and {self.page_count}, {self.year_publication}, {self.author}, {self.price}"


c = Book(537, 2012, 'Hi', 75)
print(c)

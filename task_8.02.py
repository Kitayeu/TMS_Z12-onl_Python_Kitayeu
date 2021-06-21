cars = [
    {'serial number': 1900013, 'year_release': 1976},
    {'serial number': 1795126, 'year_release': 1982},
    {'serial number': 7891124, 'year_release': 1993},
    {'serial number': 5479128, 'year_release': 1995},
    {'serial number': 9781677, 'year_release': 1999},
    {'serial number': 9944812, 'year_release': 2010},
    ]
n: int = 1994
new_list = [car for car in cars if car['year_release'] > n]
print(new_list)

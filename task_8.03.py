cars = [
    {'serial number': 1900013, 'year_release': 1976},
    {'serial number': 1795126, 'year_release': 1982},
    {'serial number': 7891124, 'year_release': 1993},
    {'serial number': 5479128, 'year_release': 1995},
    {'serial number': 9781677, 'year_release': 1999},
    {'serial number': 9944812, 'year_release': 2010},
    ]
new_dict = [{value: key for key, value in car.items()} for car in cars]
print(new_dict)

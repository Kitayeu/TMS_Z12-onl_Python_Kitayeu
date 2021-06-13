import datetime

trains = [
    {
     'train_number': '679Б',
     'departure_station': 'Минск',
     'departure_time': '06:10',
     'arrival_station': 'Гродно',
     'arrival_time': '13:46',
    },
    {
     'train_number': '712Б',
     'departure_station': 'Минск',
     'departure_time': '06:45',
     'arrival_station': 'Витебск',
     'arrival_time': '10:09',
    },
    {
     'train_number': '684Б',
     'departure_station': 'Минск',
     'departure_time': '00:25',
     'arrival_station': 'Гомель',
     'arrival_time': '07:51',
    },
    {
     'train_number': '727Б',
     'departure_station': 'Минск',
     'departure_time': '09:36',
     'arrival_station': 'Брест',
     'arrival_time': '12:59',
    },
    {
     'train_number': '742Б',
     'departure_station': 'Минск',
     'departure_time': '06:58',
     'arrival-station': 'Могилёв',
     'arrival_time': '09:43',
    },
]
for number in range(len(trains)):
    train = trains[number]
    departure = datetime.datetime.strptime("2021 6 13 " + train['departure_time'], "%Y %m %d %H:%M")
    arrival = datetime.datetime.strptime("2021 6 13 " + train['arrival_time'], "%Y %m %d %H:%M")
    travel_time = arrival - departure
    if travel_time > datetime.timedelta(hours=7, minutes=20):
        print(train)

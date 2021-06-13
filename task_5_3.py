min_number: int = 200
max_number: int = 300
for number_one in range(min_number, max_number + 1):
    number_two = 0
    for i in range(1, number_one):
        if number_one % i == 0:
            number_two += i
    if number_two > number_one:
        answer = 0
        for i in range(1, number_two):
            if number_two % i == 0:
                answer += i
        if answer == number_one:
            print(f"{number_one} {number_two}")

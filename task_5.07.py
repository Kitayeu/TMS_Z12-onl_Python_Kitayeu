from random import randint

print("Guess the number")
min_number = int(input("Enter lower limit: "))
max_number = int(input("Enter upper limit: "))
number_attempts = int(input("Enter number of attempts: "))
answer = randint(min_number, max_number)
attempts = 1
while attempts <= number_attempts:
    number_seven = int(input("Enter your number: "))
    if number_seven == answer:
        print("You are the winner")
        break
    elif number_seven > answer:
        print("Your number is bigger than the answer")
    else:
        print("Your number is less than the answer")
    attempts += 1
if attempts > number_attempts:
    print("You are the loser")
    print(f"Correct answer is: {answer}")

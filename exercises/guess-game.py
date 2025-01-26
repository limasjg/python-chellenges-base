import random

lowest_number = 1
hightest_number = 100
answer = random.randint(lowest_number, hightest_number)
guesses = 0
is_running = True

print(f"Select a number between {lowest_number} and {hightest_number}")

while is_running:
    guess = input("Enter you guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_number or guess > hightest_number:
            print("Value out of the rage, try again.")
        elif guess < answer:
            print("Too low, try again.")
        elif guess > answer:
            print("Too hight, try again")
        else:
            print(f"Correct answer, the number was {answer}")
            print(f"You try {guesses} times")
            is_running = False

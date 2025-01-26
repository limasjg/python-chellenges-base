import random

options = ("rock", "paper", "scissor")
running = True

while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Choice (rock, paper or scissor): ").lower()
        print(player)
        print(computer)
        if player == computer:
            print("You Tied, try again!")
        elif player == "rock" and computer == "scissor":
            print("You win!")
        elif player == "scissor" and computer == "paper":
            print("You win!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        else:
            print("You Lost!")

        if input("Play again?(y/n): ").lower() == "n":
            running = False
            
print("Thanks for play!")
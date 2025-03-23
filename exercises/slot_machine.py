# Game of Slot Machine

import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    #results = []

    # Commum way
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results

    #Best way
    return[random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 2
        elif row[0] == '🍉':
            return bet * 3
        elif row[0] == '🍋':
            return bet * 4
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():

    balance = 100

    print("This is Slot Game")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐ ")

    while balance > 0:

        print(f"Your current balance is {balance}")
        
        bet = input("How much do you want to bet? ")

        if not bet.isdigit():
            print("Invalid Value")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("You can't bet this value")
            continue
            
        balance -= bet

        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won {payout}!")
        else:
            print("You Lose!")

        balance += payout

        play_again = input("Do you want to play again (Y/N)? ").upper()

        if play_again != "Y":
            break 
    print(f"Game over! Your balance is ${balance}")

if __name__ == '__main__':
    main()
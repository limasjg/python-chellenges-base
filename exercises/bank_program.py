# Bank Program

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():

    amount = float(input("Enter an amount: "))

    if amount <= 0:
        print("Invalid Value")
        return 0
    
    else:
        return amount

def withodraw(balance):
    amount = float(input("Enter an amount to withdraw: "))

    if balance < amount:
        print("Insufficient funds")
        return 0
    
    elif amount <= 0:
        print("The value needs to be bigger than 0")
        return 0
    
    else:
        return amount

def main():
        
    balance = 0
    is_running = True

    while is_running:

        print("1. See Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choose = input("Choose a option: ")

        if choose == "1":
            show_balance(balance)

        elif choose == "2":
            balance += deposit()

        elif choose == "3":
            balance -= withodraw(balance)

        elif choose == "4":
            is_running = False

        else:
            print("Invalid value, try again or 4 to exit.")

    print("Good Bye!")


if __name__ == '__main__': 
    main()
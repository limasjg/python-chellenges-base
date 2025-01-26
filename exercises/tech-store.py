consoles = {"ps5": 399.00,
            "xbox s": 349.90,
            "switch": 299.99,
            "pc": 590.50}

cart = []

total = 0

#show the consoles
print("----------Consoles------------")
for key, value in consoles.items():
    print(f"{key:10}: ${value:.2f}")

# get the consoles e put on the cart
while True:
    console = input("Select a console (q to quit): ").lower()
    if console == "q":
        break
    elif consoles.get(console) is not None:
        cart.append(console)

#sum the total
for console in cart:
    total = total + consoles.get(console)
    print(console, end=" ")

print()
print(f"the total is ${total:.2f}")
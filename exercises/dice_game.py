import random


# Dictionary with all sides of a dice.
dice_art = {
    1: ("┏─────────┐", 
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┏─────────┐", 
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┏─────────┐", 
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┏─────────┐", 
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┏─────────┐", 
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┏─────────┐", 
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}
#for linha in dice_art[5]:
#    print(linha)

dice = []
total = 0
num_of_dice = int(input("how many dice? "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

#for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line) 

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end=" ")
    print()

for die in dice:
    total += die

print(f"The total value is {total}")
#print(dice)
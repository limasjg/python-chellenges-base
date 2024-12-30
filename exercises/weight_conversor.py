weight = float(input("What is your weight? "))
unit = input("In Kilograms or Pounds (K ou L)? ")

if unit == "K":
    weight = weight * 2.205
    print(f"You weight in Libras is {round(weight, 2)}L ")
elif unit == "L":
    weight = weight / 2.205
    print(f"You weight in Kilograms is {round(weight, 2)}Kg ")

else:
    print(f"{unit} Is not a unit valid")